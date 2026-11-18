import argparse
import collections
import hashlib
import json
import pathlib
import re

parser = argparse.ArgumentParser()
parser.add_argument("--run", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()
run = pathlib.Path(args.run)
output = pathlib.Path(args.output)
output.mkdir(parents=True, exist_ok=True)


def load(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def dump(name, value):
    (output / name).write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def family(diagnostic):
    message = diagnostic["message"]
    if message.startswith("Description must not match the name of the node it describes."):
        return "uninformative"
    if message == "Descriptions cannot be empty or whitespace-only. Provide a meaningful doc string.":
        return "empty"
    if re.fullmatch(
        r"The .+ named '.+' should have a documentation or description, use doc comment /\*\* \*/ to provide it\.",
        message,
        flags=re.S,
    ):
        return "default"
    raise AssertionError(("Unknown native message family", diagnostic))


manifest = load(run / "manifest.json")
baseline = load(run / "baseline.json")
coverage = load(run / "coverage.json")
projects = baseline["projects"]
validator_members = {member["rule"]: member["observations"] for member in coverage["members"]}
mapping = {
    "DescriptionMustNotBeNodeName": "uninformative",
    "DescriptiveDescriptionRequired": "empty",
}
assert set(validator_members) == set(mapping)
receipts = [
    load(path)
    for path in sorted(run.glob("native-*.json"))
    if re.fullmatch(r"native-\d+\.json", path.name)
]
assert len(receipts) == len(projects) == 490
by_project = {row["project"]: row for row in receipts}
assert len(by_project) == len(receipts)
observations = {}
for path in run.glob("native-*.json.presuppression.json"):
    receipt = load(path)
    assert receipt["project"] not in observations
    observations[receipt["project"]] = receipt
success = {row["project"] for row in receipts if row["status"] == "success"}
assert set(observations) == success
failures = [row for row in receipts if row["status"] != "success"]
native_rows = []
totals = collections.Counter()
for project in sorted(success):
    receipt = by_project[project]
    observation = observations[project]
    assert observation["configuredCount"] == len(receipt["rawDiagnostics"])
    assert observation["preSuppressionCount"] == len(observation["preSuppressionDiagnostics"])
    assert (
        observation["preSuppressionCount"] - observation["configuredCount"]
        == len(observation["capturedSuppressedDiagnostics"])
    )
    configured = collections.Counter(family(row) for row in receipt["rawDiagnostics"])
    suppressed = collections.Counter(family(row) for row in observation["capturedSuppressedDiagnostics"])
    before = collections.Counter(family(row) for row in observation["preSuppressionDiagnostics"])
    assert configured + suppressed == before
    for category, rows in [
        ("configured", receipt["rawDiagnostics"]),
        ("capturedSuppressed", observation["capturedSuppressedDiagnostics"]),
    ]:
        for row in rows:
            native_rows.append(
                {"project": project, "capture": category, "family": family(row), **row}
            )
    for name in ("default", "empty", "uninformative"):
        totals[f"configured:{name}"] += configured[name]
        totals[f"suppressed:{name}"] += suppressed[name]
        totals[f"before:{name}"] += before[name]
assert len(native_rows) == sum(
    totals[f"before:{name}"] for name in ("default", "empty", "uninformative")
)

native_project_families = collections.defaultdict(collections.Counter)
native_capture_counts = collections.Counter()
for row in native_rows:
    native_project_families[row["project"]][row["family"]] += 1
    native_capture_counts[(row["project"], row["family"], row["capture"])] += 1
member_results = {}
member_project_rows = []
for member, native_family in mapping.items():
    full = validator_members[member]
    assessed = [row for row in full if row["project"] in success]
    excluded = [row for row in full if row["project"] not in success]
    swagger_counts = collections.Counter(row["project"] for row in assessed)
    native_counts = {
        project: native_project_families[project][native_family] for project in success
    }
    rows = []
    for project in sorted(success):
        swagger = swagger_counts[project]
        native = native_counts[project]
        row = {
            "member": member,
            "project": project,
            "swagger": swagger,
            "native": native,
            "differenceSwaggerMinusNative": swagger - native,
            "absoluteRawDifference": abs(swagger - native),
            "relativeRawDifferenceToLargerCount": abs(swagger - native) / max(swagger, native) if max(swagger, native) else 0,
            "nativeConfigured": native_capture_counts[(project, native_family, "configured")],
            "nativeCapturedSuppressed": native_capture_counts[(project, native_family, "capturedSuppressed")],
        }
        rows.append(row)
    member_project_rows.extend(rows)
    native_diagnostics = [row for row in native_rows if row["family"] == native_family]
    native_positive = {project for project, count in native_counts.items() if count}
    swagger_positive = set(swagger_counts)
    member_results[member] = {
        "nativeMessageFamily": native_family,
        "selectedSwaggerRaw": len(full),
        "assessedSwaggerRaw": len(assessed),
        "unassessedSwaggerRaw": len(excluded),
        "nativeConfigured": totals[f"configured:{native_family}"],
        "nativeCapturedSuppressed": totals[f"suppressed:{native_family}"],
        "nativeReportedIncludingCapturedSuppressed": len(native_diagnostics),
        "swaggerOccurrenceReceiptKeys": len({
            (row["rule"], row["project"], row["swaggerFile"], json.dumps(row["path"]))
            for row in assessed
        }),
        "swaggerFileIndependentKeys": len({
            (row["rule"], row["project"], json.dumps(row["path"]))
            for row in assessed
        }),
        "swaggerSourceAttribution": dict(collections.Counter(
            row.get("sourceAttribution", "not-recorded") for row in assessed
        )),
        "swaggerPathCategories": dict(collections.Counter(
            "enum-metadata" if "x-ms-enum" in row["path"] else str(row["path"][0])
            for row in assessed
        )),
        "nativeSourceKeys": len({
            (row["rule"], row["project"], row.get("sourceFile"), row.get("line"), row.get("column"))
            for row in native_diagnostics
        }),
        "nativeExactDiagnosticKeys": len({
            (row["rule"], row["project"], row.get("sourceFile"), row.get("line"), row.get("column"), row["message"])
            for row in native_diagnostics
        }),
        "nativeLocationlessDiagnostics": sum(
            not row.get("sourceFile") for row in native_diagnostics
        ),
        "swaggerAffectedProjects": len(swagger_positive),
        "nativeAffectedProjects": len(native_positive),
        "overlapProjects": sorted(swagger_positive & native_positive),
        "swaggerOnlyProjects": sorted(swagger_positive - native_positive),
        "nativeOnlyProjects": sorted(native_positive - swagger_positive),
        "projectsSwaggerHigher": sum(row["swagger"] > row["native"] for row in rows),
        "projectsNativeHigher": sum(row["native"] > row["swagger"] for row in rows),
        "projectsEqual": sum(row["native"] == row["swagger"] for row in rows),
        "swaggerDirectionalExcess": sum(max(0, row["differenceSwaggerMinusNative"]) for row in rows),
        "nativeDirectionalExcess": sum(max(0, -row["differenceSwaggerMinusNative"]) for row in rows),
        "netSwaggerMinusNative": len(assessed) - len(native_diagnostics),
        "largestBothDirections": sorted(
            rows, key=lambda row: -abs(row["differenceSwaggerMinusNative"])
        )[:20],
    }

combined_rows = []
for project in sorted(success):
    member_rows = [row for row in member_project_rows if row["project"] == project]
    swagger = sum(row["swagger"] for row in member_rows)
    native = sum(row["native"] for row in member_rows)
    combined_rows.append({
        "project": project,
        "swagger": swagger,
        "native": native,
        "differenceSwaggerMinusNative": sum(row["differenceSwaggerMinusNative"] for row in member_rows),
        "absoluteRawDifference": abs(swagger - native),
        "relativeRawDifferenceToLargerCount": abs(swagger - native) / max(swagger, native) if max(swagger, native) else 0,
    })
combined = {
    "swaggerReported": sum(row["assessedSwaggerRaw"] for row in member_results.values()),
    "nativeConfigured": sum(row["nativeConfigured"] for row in member_results.values()),
    "nativeCapturedSuppressed": sum(row["nativeCapturedSuppressed"] for row in member_results.values()),
    "nativeReportedIncludingCapturedSuppressed": sum(row["nativeReportedIncludingCapturedSuppressed"] for row in member_results.values()),
    "swaggerDirectionalExcess": sum(max(0, row["differenceSwaggerMinusNative"]) for row in combined_rows),
    "nativeDirectionalExcess": sum(max(0, -row["differenceSwaggerMinusNative"]) for row in combined_rows),
    "projectsEqual": sum(row["differenceSwaggerMinusNative"] == 0 for row in combined_rows),
    "netSwaggerMinusNative": sum(row["differenceSwaggerMinusNative"] for row in combined_rows),
}
assert combined["swaggerReported"] - combined["nativeReportedIncludingCapturedSuppressed"] == combined["netSwaggerMinusNative"]
assert combined["swaggerDirectionalExcess"] - combined["nativeDirectionalExcess"] == combined["netSwaggerMinusNative"]
summary = {
    "schemaVersion": 1,
    "candidateCommit": manifest["candidate"]["commit"],
    "coreCommit": manifest["coreCommit"],
    "specsCommit": manifest["specs"]["commit"],
    "baselineIdentity": manifest["baselineIdentity"],
    "nativeRunStatus": manifest["status"],
    "selectedProjects": len(projects),
    "assessedProjects": len(success),
    "failedProjects": len(failures),
    "suppressionCapture": "all successful source workers; mapped-linter result before compiler suppression, configured findings reconciled as multiset",
    "combined": combined,
    "unfilteredNativeMessageCounts": dict(totals),
    "excludedExistingMissingDocumentation": {
        "configured": totals["configured:default"],
        "capturedSuppressed": totals["suppressed:default"],
        "beforeSuppression": totals["before:default"],
    },
    "members": member_results,
    "equivalence": "not-determined; exact source/emission correspondence requires separate investigation",
}
dump("scoped-summary.json", summary)
dump("per-project-counts.json", {"combined": combined_rows, "members": member_project_rows})
dump("failed-projects.json", failures)
for name, rows in [
    ("native-quality.jsonl", [row for row in native_rows if row["family"] != "default"]),
    ("excluded-missing-docs.jsonl", [row for row in native_rows if row["family"] == "default"]),
]:
    content = "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows)
    (output / name).write_text(content, encoding="utf-8", newline="\n")
print(json.dumps(summary, ensure_ascii=False, indent=2))

"""Reconcile preserved current-source observations, not cross-engine defects."""

import collections
import hashlib
import json
from pathlib import Path
import sys

task = Path(__file__).resolve().parent.parent
fresh = task / "refresh-20261105-inherited"
previous = task / "refresh-20261105"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def key(record):
    return record["project"], record["diagnosticIndex"]


def canonical_locations(value):
    if isinstance(value, list):
        return [canonical_locations(item) for item in value]
    if isinstance(value, dict):
        result = {name: canonical_locations(item) for name, item in value.items()}
        marker = "/node_modules/@azure-tools/typespec-azure-resource-manager/"
        if marker in result.get("sourceFile", ""):
            result["sourceFile"] = "@azure-tools/typespec-azure-resource-manager/" + result["sourceFile"].split(marker, 1)[1]
        return result
    return value


def predicate_context(record):
    return canonical_locations([
        {name: value for name, value in context.items() if name != "warningIndices"}
        for context in record["contexts"]
    ])


def library_members(directory):
    artifacts = load(directory / "provenance/artifact-provenance.json")["artifacts"]
    arm = next(row for row in artifacts if row["file"].startswith("azure-tools-typespec-azure-resource-manager-"))
    return {row["file"]: row["sha256"] for row in arm["files"] if row["file"].startswith("package/lib/")}


assert library_members(previous) == library_members(fresh)
assert library_members(fresh)


current_path = fresh / "source-attribution/observations.json"
current = load(current_path)
old = {key(record): record for record in load(previous / "source-attribution/observations.json")["records"]}
review = load(task / "compatibility-20261105/accepted-contracts.json")
records = {key(record): record for record in current["records"]}
assert len(records) == len(current["records"]) == len(old) == 182
assert records.keys() == old.keys()

accepted = []
for row in review["records"]:
    identity = key(row)
    record = records[identity]
    assert record["swaggerFamily"] == "same-name-schema-inequality"
    assert record["observation"] == old[identity]["observation"] == "source-accepts"
    assert predicate_context(record) == predicate_context(old[identity]), identity
    accepted.append(row)
assert len(accepted) == 79
oracle_groups = {
    1: "compatible-partial-collections",
    5: "compatible-serialized-enums",
}
newly_reviewed = []
for record in records.values():
    if record["project"] != "specification/oracle/resource-manager/Oracle.Database/OracleDatabase":
        continue
    assert old[key(record)]["observation"] == "no-source-pair"
    assert record["observation"] == "source-accepts"
    newly_reviewed.append({
        **{field: record[field] for field in ("project", "diagnosticIndex", "operationId", "name", "sourceFile")},
        "reviewedCurrentSourceDisposition": oracle_groups[record["diagnosticIndex"]],
    })
assert len(newly_reviewed) == 2

changed = [
    {
        **{field: record[field] for field in ("project", "diagnosticIndex", "operationId", "name", "sourceFile")},
        "previousObservation": old[identity]["observation"],
        "currentObservation": record["observation"],
    }
    for identity, record in records.items()
    if record["observation"] != old[identity]["observation"]
]
observed = collections.Counter(record["observation"] for record in records.values())
assert dict(observed) == current["observations"]
by_family = {}
witnesses = collections.defaultdict(set)
for record in records.values():
    by_family.setdefault(record["swaggerFamily"], collections.Counter())[record["observation"]] += 1
    for context in record["contexts"]:
        for index in context["warningIndices"]:
            witnesses[record["swaggerFamily"]].add((record["project"], index))

result = {
    "candidateCommit": load(fresh / "task.json")["candidateCommit"],
    "boundary": (
        "182 original Swagger records retain their identities. Counts below describe "
        "current-source route/predicate contexts, not matched emitted defects, "
        "normalized diagnostic counts or a coverage percentage. The79 acceptance "
        "decisions were manually reviewed at150e; exact unchanged predicate contexts "
        "are verified here, canonicalizing only installed ARM package store prefixes "
        "after verifying every library member's unchanged content hash. Two newly "
        "recovered Oracle contracts were separately reviewed as compatible partial "
        "collection and identical current-source literal contracts."
    ),
    "observationsSha256": hashlib.sha256(current_path.read_bytes()).hexdigest(),
    "observations": dict(observed),
    "bySwaggerFamily": {family: dict(counts) for family, counts in by_family.items()},
    "configuredWarningWitnessesBySwaggerFamily": {family: len(indices) for family, indices in witnesses.items()},
    "unchangedReviewedAcceptedSchemaGroups": dict(
        sorted(collections.Counter(row["reviewedCurrentSourceDisposition"] for row in accepted).items())
    ),
    "allReviewedAcceptedSchemaGroups": dict(sorted(collections.Counter(
        row["reviewedCurrentSourceDisposition"] for row in accepted + newly_reviewed
    ).items())),
    "libraryMemberHashesEqual": len(library_members(fresh)),
    "newlyReviewedAcceptedSchemas": newly_reviewed,
    "changedObservations": changed,
    "unchangedReviewedAcceptedSchemas": accepted,
}
output = Path(__file__).with_name("assessed-contexts.json")
encoded = json.dumps(result, indent=2) + "\n"
if "--check" in sys.argv:
    assert output.read_text(encoding="utf-8") == encoded
else:
    assert not output.exists()
    output.write_text(encoded, encoding="utf-8", newline="\n")
print(json.dumps({name: value for name, value in result.items() if name != "unchangedReviewedAcceptedSchemas"}, indent=2))

routes = {}
for record in records.values():
    identity = record["project"], record.get("route")
    group = routes.setdefault(identity, {"records": [], "warnings": set(), "observations": collections.Counter()})
    group["records"].append(record)
    group["observations"][record["observation"]] += 1
    for context in record["contexts"]:
        group["warnings"].update(context["warningIndices"])
projects = {row["project"]: row for row in load(fresh / "staging-comparison/projects.json")}
lines = [
    "# Retained-record route contexts",
    "",
    "This deterministic index preserves all182retained Swagger record identities. "
    "Each route row counts retained emitted records and distinct configured source "
    "diagnostic indices witnessed by their owning predicate/target contexts. "
    "These are not matched cross-engine defects. Shared warnings may appear on "
    "several routes, so route witness counts must not be added. "
    "The source record contains operation/declaration/leaf details and exact warning indices.",
    "",
    "Project totals include all original reported diagnostics before filtering; "
    "route rows include retained records only. Suppression probes are not configured warnings. "
    "See [semantic decisions](../gap-investigation.md) and "
    "[the complete raw difference inventory](../refresh-20261105-inherited/staging-comparison/differences.md).",
]
for project in sorted({identity[0] for identity in routes}):
    row = projects[project]
    lines.extend([
        "",
        f"## `{project}`",
        "",
        f"Reported project totals: Swagger **{row['swaggerReportedDiagnostics']}** / "
        f"TypeSpec **{row['typeSpecReportedDiagnostics']}**.",
        "",
        "| PATCH route | Retained Swagger records | Witnessed TypeSpec warnings | Context observations |",
        "| --- | ---: | ---: | --- |",
    ])
    for (_, route), group in sorted(
        ((identity, group) for identity, group in routes.items() if identity[0] == project),
        key=lambda item: item[0][1] or "",
    ):
        observations = "; ".join(f"{name}: {count}" for name, count in sorted(group["observations"].items()))
        source = group["records"][0]["sourceFile"]
        lines.append(
            f"| `{route}` | {len(group['records'])} | {len(group['warnings'])} | "
            f"[{observations}](../refresh-20261105-inherited/source-attribution/{source}) |"
        )
markdown = "\n".join(lines) + "\n"
index = Path(__file__).with_name("retained-route-contexts.md")
if "--check" in sys.argv:
    assert index.read_text(encoding="utf-8") == markdown
else:
    assert not index.exists()
    index.write_text(markdown, encoding="utf-8", newline="\n")

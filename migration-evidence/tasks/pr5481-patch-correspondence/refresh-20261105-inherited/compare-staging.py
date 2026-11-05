"""Reconcile saved native receipts and a verified immutable staging supplement."""

import collections
import hashlib
import json
import pathlib
import re
import sys

RULE = "PatchPropertiesCorrespondToPutProperties"


def load(file):
    return json.loads(file.read_text(encoding="utf-8"))


def digest(file):
    return hashlib.sha256(file.read_bytes()).hexdigest()


def identity(value):
    return hashlib.sha256(
        json.dumps(value, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()


def write(file, value):
    file.write_text(
        json.dumps(value, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def markdown(value):
    return str(value).replace("|", "\\|").replace("\n", "<br>")


def difference_report(rows):
    different = sorted(
        (row for row in rows if row["absoluteGap"]),
        key=lambda row: (-row["absoluteGap"], row["project"]),
    )
    lines = [
        "# Complete raw-count difference inventory",
        "",
        "Swagger and TypeSpec rows below are separate identity domains, not paired",
        "diagnostics. Grouping identical target/message records preserves raw",
        "multiplicity; it is not semantic deduplication. Schema/visibility/version",
        "investigations and their limits are in [gap-investigation.md](../../gap-investigation.md).",
        "",
        "| Project | Swagger linter | TypeSpec linter | TypeSpec minus Swagger | Absolute gap | Relative gap |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for index, row in enumerate(different):
        lines.append(
            f"| [{row['project']}](#difference-{index}) | "
            f"{row['swaggerReportedDiagnostics']} | {row['typeSpecReportedDiagnostics']} | "
            f"{row['signedTypeSpecMinusSwagger']} | {row['absoluteGap']} | "
            f"{row['relativeAbsoluteGap']:.2%} |"
        )
    lines.extend(
        [
            "",
            "Relative gap uses `abs(TypeSpec - Swagger) / max(TypeSpec, Swagger, 1)`.",
            "All exact observations, including equal-count and zero-count projects,",
            "are retained in [projects.json](projects.json). Matching totals do not",
            "prove matching defects. Unsupported common-unit counts remain unassessed.",
        ]
    )
    for index, row in enumerate(different):
        lines.extend(
            [
                "",
                f'<a id="difference-{index}"></a>',
                f"## {row['project']}",
                "",
                f"Reported diagnostics: Swagger **{row['swaggerReportedDiagnostics']}**, "
                f"TypeSpec **{row['typeSpecReportedDiagnostics']}**.",
                "The complete groups below account for both counts independently.",
                "",
                "| Engine | Exact diagnostic target | Message | Raw count |",
                "| --- | --- | --- | ---: |",
            ]
        )
        swagger_groups = collections.Counter(
            (
                item["validatorInputFile"],
                item["swaggerFile"],
                json.dumps(item["path"], separators=(",", ":")),
                item["message"],
            )
            for item in row["swaggerDiagnostics"]
        )
        native_groups = collections.Counter(
            (
                item.get("sourceFile"),
                item.get("line"),
                item.get("column"),
                item["message"],
            )
            for item in row["typeSpecDiagnostics"]
        )
        assert sum(swagger_groups.values()) == row["swaggerReportedDiagnostics"]
        assert sum(native_groups.values()) == row["typeSpecReportedDiagnostics"]
        for (input_file, source, target, message), count in sorted(swagger_groups.items()):
            target_text = f"{source}: {target}"
            if input_file != source:
                target_text += f"; invoked through {input_file}"
            lines.append(
                f"| Swagger linter | `{markdown(target_text)}` | {markdown(message)} | {count} |"
            )
        for (source, line, column, message), count in sorted(native_groups.items()):
            lines.append(
                f"| TypeSpec linter | `{markdown(source)}:{line}:{column}` | "
                f"{markdown(message)} | {count} |"
            )
        lines.extend(
            [
                "",
                "**Attribution boundary:** these raw source/latest-emitted observations",
                "do not establish a common-operation count or exact cross-engine",
                "correspondence. Any residual not established by the linked investigation",
                "remains unresolved; no production-rule change is inferred from totals.",
            ]
        )
    return "\n".join(lines) + "\n"


def compare(native_directory, supplement_directory, output):
    task = load(pathlib.Path(__file__).parent / "task.json")
    manifest = load(supplement_directory / "manifest.json")
    assert manifest["schemaVersion"] == 1
    assert manifest["status"] == "complete"
    assert manifest["profile"] == "arm-staging-spectral"
    assert manifest["finishedAt"]
    assert manifest["swaggerGeneration"] == "not-run"
    assert manifest["parentBaselineIdentity"] == task["baselineIdentity"]
    assert manifest["specsCommit"] == task["specsCommit"]
    assert RULE in manifest["rules"]
    assert all(item["status"] == "success" for item in manifest["inputs"])
    inputs = {(item["project"], item["swaggerFile"]) for item in manifest["inputs"]}
    assert len(inputs) == len(manifest["inputs"]), "Duplicate Swagger inputs"
    assert len(inputs) == 649, "Partial frozen Swagger population"
    data = supplement_directory / "data"
    expected = {item["file"]: item["sha256"] for item in manifest["files"]}
    assert len(expected) == len(manifest["files"])
    actual = {}
    for file in data.rglob("*"):
        assert not file.is_symlink(), file
        if file.is_file():
            actual[file.relative_to(data).as_posix()] = digest(file)
    assert actual == expected, "Supplement file hashes/inventory do not match"
    shard = load(data / "rules" / f"{RULE}.json")
    observations = shard["results"]
    assert shard["rule"] == RULE and shard["count"] == len(observations)

    native_manifest = load(native_directory / "manifest.json")
    if native_manifest["status"] != "complete":
        recovery = load(native_directory.parents[1] / "provenance/integrity-reconciliation.json")
        assert native_manifest["status"] == "running"
        assert recovery["status"] == "verified" and recovery["originalExitCode"] == 255
        assert recovery["successfulProjects"] == 487 and recovery["failedOrUnassessedProjects"] == 0
        assert recovery["candidateCommit"] == native_manifest["candidate"]["commit"]
        assert recovery["publishedOriginalManifestSha256"] == digest(native_directory / "manifest.json")
    assert native_manifest["candidate"]["commit"] == task["candidateCommit"]
    assert native_manifest["specs"]["commit"] == task["specsCommit"]
    assert native_manifest["baselineIdentity"] == task["baselineIdentity"]
    assert native_manifest["config"]["validatorRules"] == [RULE]
    assert native_manifest["config"]["tspRules"] == task["mapping"]["tspRules"]
    assert native_manifest["config"]["scope"] == "source"
    assert native_manifest["config"]["nativeMode"] == "target-only"
    assert native_manifest["config"]["baselinePolicy"] == "frozen-reference"
    receipts = [
        load(file)
        for file in sorted(native_directory.glob("native-*.json"))
        if re.fullmatch(r"native-\d+\.json", file.name)
    ]
    assert receipts, "No native project receipts"
    projects = {receipt["project"]: receipt for receipt in receipts}
    assert len(projects) == len(receipts), "Duplicate native receipts"
    assert len(projects) == task["outcome"]["selectedProjects"], "Partial native population"
    assert set(projects) == {item["project"] for item in manifest["inputs"]}
    assert all(item["project"] in projects for item in observations)
    swagger = collections.defaultdict(list)
    for observation in observations:
        assert observation["rule"] == RULE
        assert (observation["project"], observation["validatorInputFile"]) in inputs
        swagger[observation["project"]].append(observation)
    rows = []
    failed = []
    for project, receipt in sorted(projects.items()):
        if receipt["status"] != "success":
            failed.append({"project": project, "error": receipt.get("error")})
            continue
        s = len(swagger[project])
        n = len(receipt["rawDiagnostics"])
        rows.append(
            {
                "project": project,
                "swaggerReportedDiagnostics": s,
                "typeSpecReportedDiagnostics": n,
                "signedTypeSpecMinusSwagger": n - s,
                "absoluteGap": abs(n - s),
                "relativeAbsoluteGap": abs(n - s) / max(s, n, 1),
                "swaggerOnly": s > 0 and n == 0,
                "typeSpecOnly": n > 0 and s == 0,
                "swaggerDiagnostics": swagger[project],
                "typeSpecDiagnostics": receipt["rawDiagnostics"],
            }
        )
    swagger_projects = {row["project"] for row in rows if row["swaggerReportedDiagnostics"]}
    native_projects = {row["project"] for row in rows if row["typeSpecReportedDiagnostics"]}
    native_diagnostics = [
        (row["project"], diagnostic)
        for row in rows
        for diagnostic in row["typeSpecDiagnostics"]
    ]
    occurrence = {
        (item["rule"], item["project"], item["swaggerFile"], json.dumps(item["path"]))
        for item in observations
    }
    no_file = {
        (item["rule"], item["project"], json.dumps(item["path"]))
        for item in observations
    }
    native_positions = {
        (project, item["rule"], item.get("sourceFile"), item.get("line"), item.get("column"))
        for project, item in native_diagnostics
    }
    summary = {
        "assessment": task.get("assessment", "saved-native-observation reanalysis"),
        "supplementIdentity": identity(manifest),
        "parentBaselineIdentity": task["baselineIdentity"],
        "candidateCommit": task["candidateCommit"],
        "specsCommit": task["specsCommit"],
        "swaggerProfile": "arm-staging-spectral",
        "nativeProfile": "source; target-only; authored suppressions retained",
        "selectedProjects": len(projects),
        "assessableProjects": len(rows),
        "failedOrUnassessedProjects": failed,
        "swaggerInputs": len(manifest["inputs"]),
        "swaggerReportedDiagnostics": len(observations),
        "typeSpecReportedDiagnostics": len(native_diagnostics),
        "swaggerDistinctOccurrencePaths": len(occurrence),
        "swaggerDistinctProjectPaths": len(no_file),
        "typeSpecDistinctSourcePositions": len(native_positions),
        "swaggerProjects": sorted(swagger_projects),
        "typeSpecProjects": sorted(native_projects),
        "overlapProjects": sorted(swagger_projects & native_projects),
        "swaggerOnlyProjects": sorted(swagger_projects - native_projects),
        "typeSpecOnlyProjects": sorted(native_projects - swagger_projects),
        "equalRawCountProjects": sum(row["absoluteGap"] == 0 for row in rows),
        "swaggerHigherProjects": sum(row["signedTypeSpecMinusSwagger"] < 0 for row in rows),
        "typeSpecHigherProjects": sum(row["signedTypeSpecMinusSwagger"] > 0 for row in rows),
        "swaggerDirectionalExcess": sum(max(0, -row["signedTypeSpecMinusSwagger"]) for row in rows),
        "typeSpecDirectionalExcess": sum(max(0, row["signedTypeSpecMinusSwagger"]) for row in rows),
        "sumAbsoluteProjectGaps": sum(row["absoluteGap"] for row in rows),
        "relativeGapDenominator": "max(Swagger raw count, TypeSpec raw count, 1) per project",
        "countingCaution": "Raw findings, Swagger paths and native source positions are different units. No semantic correspondence or common-operation normalization is inferred.",
        "semanticEquivalence": "not-determined-by-reanalysis",
    }
    assert sum(row["swaggerReportedDiagnostics"] for row in rows) + sum(
        len(swagger[item["project"]]) for item in failed
    ) == len(observations)
    assert (
        summary["typeSpecDirectionalExcess"] - summary["swaggerDirectionalExcess"]
        == summary["typeSpecReportedDiagnostics"]
        - sum(row["swaggerReportedDiagnostics"] for row in rows)
    )
    output.mkdir(parents=True, exist_ok=False)
    write(output / "summary.json", summary)
    write(output / "projects.json", rows)
    write(output / "swagger-observations.json", shard)
    write(output / "supplement-manifest.json", manifest)
    (output / "differences.md").write_text(
        difference_report(rows), encoding="utf-8", newline="\n"
    )
    return summary


def schema_summary(schema, output):
    rows = sorted(
        (row for row in schema["projects"] if row["swaggerOnly"] or row["typeSpecOnly"]),
        key=lambda row: row["project"],
    )
    assert sum(row["swaggerOnly"] for row in rows) == 294
    assert sum(row["typeSpecOnly"] for row in rows) == 1
    lines = [
        "# Every one-sided project's emitted-schema investigation",
        "",
        "All 295 one-sided projects are retained below. These are original",
        "Swagger-predicate classifications, not matched native diagnostic counts.",
        "The [source-backed investigation](../gap-investigation.md) explains the",
        "matching-name schema-policy difference, the EdgeActions empty/read-only",
        "wrapper, Quota's authored suppression, and BillingTrust's source visibility.",
        "Exact operations, names, candidate schema-key differences and repeated",
        "helper returns remain in [schema-investigation.json](schema-investigation.json).",
        "",
        "| Project | Swagger | TypeSpec | Same name, unequal schema | Absent leaf name | Absent PATCH body |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in rows:
        assert (
            row["sameNameDifferentSchemaFindings"]
            + row["leafNameAbsentFindings"]
            + row["missingPatchBodyFindings"]
            + row["missingPutBodyFindings"]
            == row["swaggerReportedDiagnostics"]
        )
        lines.append(
            f"| {row['project']} | {row['swaggerReportedDiagnostics']} | "
            f"{row['typeSpecReportedDiagnostics']} | "
            f"{row['sameNameDifferentSchemaFindings']} | "
            f"{row['leafNameAbsentFindings']} | {row['missingPatchBodyFindings']} |"
        )
    assert not output.exists()
    output.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__" and sys.argv[1:2] == ["--schema-summary"]:
    schema_summary(load(pathlib.Path(sys.argv[2])), pathlib.Path(sys.argv[3]))
elif __name__ == "__main__":
    result = compare(*(pathlib.Path(value).resolve() for value in sys.argv[1:]))
    print(json.dumps({key: value for key, value in result.items() if not isinstance(value, list)}, indent=2))

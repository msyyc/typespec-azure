"""Recount saved observations without TypeSpec, npm, or either linter."""

import argparse
import collections
import gzip
import json
from pathlib import Path


def source_key(item, index):
    if all(key in item for key in ("sourceFile", "line", "column")):
        return (item["rule"], item["sourceFile"], item["line"], item["column"])
    return ("locationless", index)


def recount(observations):
    selected = {item["sourcePath"]: item for item in observations["projects"]}
    assert len(selected) == len(observations["projects"]), "Duplicate selected project"
    native = {item["project"]: item for item in observations["native"]}
    assert len(native) == len(observations["native"]), "Duplicate TypeSpec receipt"
    assert set(selected) == set(native), "Missing or unexpected TypeSpec receipt"
    swagger = collections.defaultdict(list)
    for item in observations["swagger"]:
        assert item["project"] in selected, "Unexpected Swagger project"
        swagger[item["project"]].append(item)
    rows, failures = [], []
    for name in sorted(selected):
        project, receipt, findings = selected[name], native[name], swagger[name]
        if (
            project["compileStatus"] != "success"
            or project["validationStatus"] != "success"
            or receipt["status"] != "success"
        ):
            failures.append({
                "project": name,
                "swaggerRaw": len(findings),
                "nativeRaw": len(receipt["rawDiagnostics"]),
                "reason": receipt.get("error", "Saved Swagger compilation/validation failed"),
            })
            continue
        raw = len(receipt["rawDiagnostics"])
        aligned = len(receipt["diagnostics"])
        difference = len(findings) - aligned
        rows.append({
            "project": name,
            "apiVersion": project.get("apiVersion"),
            "swaggerRaw": len(findings),
            "swaggerOccurrenceKeys": len({
                (item["rule"], item["swaggerFile"], tuple(item["path"]))
                for item in findings
            }),
            "swaggerFileIndependent": len({
                (item["rule"], tuple(item["path"])) for item in findings
            }),
            "nativeRaw": raw,
            "nativeAligned": aligned,
            "nativeSource": len({
                source_key(item, index)
                for index, item in enumerate(receipt["diagnostics"])
            }),
            "nativeDefault": (
                None if receipt.get("defaultActivation") == "not-assessed"
                else len(receipt.get("defaultTargetDiagnostics", []))
            ),
            "rawDifference": difference,
            "absoluteRawDifference": abs(difference),
            "relativeRawDifference": abs(difference) / max(1, len(findings)),
        })
    swagger_projects = {row["project"] for row in rows if row["swaggerRaw"]}
    native_projects = {row["project"] for row in rows if row["nativeAligned"]}
    totals = {
        "selected": len(selected),
        "assessable": len(rows),
        "unassessed": len(failures),
        "selectedSwaggerRaw": len(observations["swagger"]),
        "swaggerRaw": sum(row["swaggerRaw"] for row in rows),
        "swaggerOccurrenceKeys": sum(row["swaggerOccurrenceKeys"] for row in rows),
        "swaggerFileIndependent": sum(row["swaggerFileIndependent"] for row in rows),
        "nativeRaw": sum(row["nativeRaw"] for row in rows),
        "nativeAligned": sum(row["nativeAligned"] for row in rows),
        "nativeSource": sum(row["nativeSource"] for row in rows),
        "nativeDefault": (
            None if any(row["nativeDefault"] is None for row in rows)
            else sum(row["nativeDefault"] for row in rows)
        ),
        "swaggerProjects": len(swagger_projects),
        "nativeProjects": len(native_projects),
        "overlap": len(swagger_projects & native_projects),
        "swaggerOnly": len(swagger_projects - native_projects),
        "nativeOnly": len(native_projects - swagger_projects),
        "equalRawProjects": sum(row["rawDifference"] == 0 for row in rows),
        "swaggerHigherRawProjects": sum(row["rawDifference"] > 0 for row in rows),
        "nativeHigherRawProjects": sum(row["rawDifference"] < 0 for row in rows),
        "rawSwaggerExcess": sum(max(0, row["rawDifference"]) for row in rows),
        "rawNativeExcess": sum(max(0, -row["rawDifference"]) for row in rows),
        "fileIndependentSwaggerExcess": sum(
            max(0, row["swaggerFileIndependent"] - row["nativeSource"]) for row in rows
        ),
        "fileIndependentNativeExcess": sum(
            max(0, row["nativeSource"] - row["swaggerFileIndependent"]) for row in rows
        ),
        "unassessedSwaggerRaw": sum(row["swaggerRaw"] for row in failures),
        "unassessedNativeRaw": sum(row["nativeRaw"] for row in failures),
    }
    return {
        "schemaVersion": 1,
        "scope": "Saved source/frozen-reference observations; counts are not semantic correspondence.",
        "relativeGapDenominator": "max(1, project Swagger raw findings); prioritization only",
        "totals": totals,
        "swaggerOnlyProjects": sorted(swagger_projects - native_projects),
        "nativeOnlyProjects": sorted(native_projects - swagger_projects),
        "failures": failures,
        "projects": rows,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("observations", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    opener = gzip.open if args.observations.suffix == ".gz" else open
    with opener(args.observations, "rt", encoding="utf-8") as stream:
        result = recount(json.load(stream))
    if args.verify:
        expected = json.loads(args.verify.read_text(encoding="utf-8"))
        assert result == expected, "Saved-observation replay differs from expected assessment"
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "numerical-replay.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    print(json.dumps(result["totals"], indent=2))


if __name__ == "__main__":
    main()

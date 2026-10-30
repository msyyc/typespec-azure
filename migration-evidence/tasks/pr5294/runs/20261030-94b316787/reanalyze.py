"""Independently recount saved observations without executing either linter."""

import argparse
from collections import Counter
import json
from pathlib import Path


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def source_key(diagnostic, index):
    if all(diagnostic.get(k) is not None for k in ("sourceFile", "line", "column")):
        return compact([diagnostic["rule"], diagnostic["sourceFile"],
                        diagnostic["line"], diagnostic["column"]])
    return "locationless:" + str(index)


def recount(root):
    coverage = load(root / "coverage.json")
    population = load(root / "population.json")
    swagger = load(root / "swagger-observations.json")
    native = load(root / "native-results.json")
    selected = {p["sourcePath"]: p for p in population}
    receipts = {p["project"]: p for p in native}
    assert len(selected) == len(population) == coverage["selectedProjectCount"]
    assert len(receipts) == len(native) == len(selected)
    assert set(receipts) == set(selected)
    assert len(swagger) == coverage["selectedValidatorRawCount"]
    rows = []
    failed = []
    for project, metadata in selected.items():
        result = receipts[project]
        observations = [d for d in swagger if d["project"] == project]
        if (metadata["compileStatus"] != "success"
                or metadata["validationStatus"] != "success"
                or result["status"] != "success"):
            failed.append(project)
            continue
        emitted = len(observations)
        reported = len(result["diagnostics"])
        rows.append({
            "project": project,
            "apiVersion": metadata.get("apiVersion"),
            "swagger": emitted,
            "typespec": reported,
            "typespecRaw": len(result["rawDiagnostics"]),
            "swaggerFileIndependent": len({
                compact([d["rule"], d["path"]]) for d in observations}),
            "typespecSourceLocations": len({
                source_key(d, i) for i, d in enumerate(result["diagnostics"])}),
            "signedTypespecMinusSwagger": reported - emitted,
            "absoluteDifference": abs(reported - emitted),
            "relativeDifference": abs(reported - emitted) / max(emitted, reported, 1),
        })
    assessable = {r["project"] for r in rows}
    expected = {p["project"]: p for p in coverage["projects"]}
    assert len(rows) == len(expected) == coverage["assessableProjectCount"]
    assert set(failed) == {p["project"] for p in coverage["unassessedProjects"]}
    for row in rows:
        recorded = expected[row["project"]]
        for our, their in (
            ("swagger", "validatorRawCount"), ("typespec", "nativeAlignedCount"),
            ("typespecRaw", "nativeRawCount"),
            ("swaggerFileIndependent", "validatorFileIndependentCount"),
            ("typespecSourceLocations", "nativeSourceCount"),
        ):
            assert row[our] == recorded[their], (row["project"], our)
    swagger_projects = {r["project"] for r in rows if r["swagger"]}
    typespec_projects = {r["project"] for r in rows if r["typespec"]}
    summary = {
        "selectedProjects": len(selected),
        "assessableProjects": len(rows),
        "failedProjects": sorted(failed),
        "selectedSwaggerRaw": len(swagger),
        "swaggerRaw": sum(r["swagger"] for r in rows),
        "typespecRaw": sum(r["typespecRaw"] for r in rows),
        "typespecAligned": sum(r["typespec"] for r in rows),
        "swaggerOccurrenceLocations": len({
            compact([d["rule"], d["project"], d["swaggerFile"], d["path"]])
            for d in swagger if d["project"] in assessable}),
        "swaggerFileIndependentLocations": sum(r["swaggerFileIndependent"] for r in rows),
        "typespecSourceLocations": sum(r["typespecSourceLocations"] for r in rows),
        "swaggerProjects": sorted(swagger_projects),
        "typespecProjects": sorted(typespec_projects),
        "overlap": sorted(swagger_projects & typespec_projects),
        "swaggerOnly": sorted(swagger_projects - typespec_projects),
        "typespecOnly": sorted(typespec_projects - swagger_projects),
        "equalRawProjects": sum(r["swagger"] == r["typespec"] for r in rows),
        "swaggerHigherProjects": sum(r["swagger"] > r["typespec"] for r in rows),
        "typespecHigherProjects": sum(r["swagger"] < r["typespec"] for r in rows),
        "swaggerExcess": sum(max(0, r["swagger"] - r["typespec"]) for r in rows),
        "typespecExcess": sum(max(0, r["typespec"] - r["swagger"]) for r in rows),
        "absoluteDifference": sum(r["absoluteDifference"] for r in rows),
        "memberSwagger": {
            rule: {"raw": count,
                   "projects": sorted({d["project"] for d in swagger if d["rule"] == rule}),
                   "typespecAttribution": "unassessed"}
            for rule, count in sorted(Counter(d["rule"] for d in swagger).items())
        },
        "crossValidatorOverlap": "not normalized",
        "commonActionableUnit": "unassessed",
        "equivalence": "not determined by recounting",
        "projects": sorted(rows, key=lambda r: (-r["absoluteDifference"], r["project"])),
    }
    for our, their in (
        ("swaggerRaw", "validatorRawCount"), ("typespecRaw", "nativeRawCount"),
        ("typespecAligned", "nativeAlignedCount"),
        ("swaggerFileIndependentLocations", "validatorFileIndependentCount"),
        ("typespecSourceLocations", "nativeSourceCount"),
        ("swaggerExcess", "rawValidatorExcess"), ("typespecExcess", "rawNativeExcess"),
    ):
        assert summary[our] == coverage[their], (our, summary[our], coverage[their])
    for our, their in (
        ("swaggerProjects", "validatorProjects"), ("typespecProjects", "nativeProjects"),
        ("overlap", "overlapProjects"), ("swaggerOnly", "validatorOnlyProjects"),
        ("typespecOnly", "nativeOnlyProjects"),
    ):
        assert summary[our] == sorted(coverage[their]), our
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("observations", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    result = recount(args.observations)
    assert not args.output.exists(), "Use a new output file."
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ("projects", "memberSwagger")}, indent=2))

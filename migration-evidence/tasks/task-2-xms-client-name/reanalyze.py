"""Recount saved comparison observations without running either linter."""

import argparse
import json
from pathlib import Path


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def recount(root):
    run = root / "runs" / "full-native-coverage"
    coverage = load(run / "coverage.json")
    population = load(run / "project-inventory.json")
    observations = load(run / "selected-swagger-observations.json")
    receipts = [
        load(path)
        for path in sorted((run / "native-results").glob("native-*.json"))
    ]
    projects = {item["sourcePath"]: item for item in population}
    native = {item["project"]: item for item in receipts}
    assert len(projects) == len(population)
    assert len(native) == len(receipts)
    assert projects.keys() == native.keys()
    assert all(item["project"] in projects for item in observations)
    rows = []
    failed = []
    for project, selected in projects.items():
        receipt = native[project]
        if (
            selected["compileStatus"] != "success"
            or selected["validationStatus"] != "success"
            or receipt["status"] != "success"
        ):
            failed.append(project)
            continue
        swagger = [item for item in observations if item["project"] == project]
        diagnostics = receipt["diagnostics"]
        rows.append(
            {
                "project": project,
                "swaggerRaw": len(swagger),
                "swaggerOccurrenceKeys": len(
                    {
                        json.dumps(
                            [
                                item.get("rule"),
                                project,
                                item["swaggerFile"],
                                item["path"],
                            ],
                            sort_keys=True,
                        )
                        for item in swagger
                    }
                ),
                "swaggerFileIndependent": len(
                    {
                        json.dumps(
                            [item.get("rule"), project, item["path"]],
                            sort_keys=True,
                        )
                        for item in swagger
                    }
                ),
                "typeSpecRaw": len(receipt["rawDiagnostics"]),
                "typeSpecAligned": len(diagnostics),
                "typeSpecSourceKeys": len(
                    {
                        (
                            json.dumps(
                                [
                                    item["rule"],
                                    project,
                                    item["sourceFile"],
                                    item["line"],
                                    item["column"],
                                ],
                                sort_keys=True,
                            )
                            if all(
                                field in item
                                for field in ("sourceFile", "line", "column")
                            )
                            else f"locationless:{index}"
                        )
                        for index, item in enumerate(diagnostics)
                    }
                ),
                "ambient": len(receipt.get("ambientDiagnostics", [])),
            }
        )
    swagger_projects = sorted(
        row["project"] for row in rows if row["swaggerRaw"] > 0
    )
    typespec_projects = sorted(
        row["project"] for row in rows if row["typeSpecAligned"] > 0
    )
    differences = [
        {
            **row,
            "signedSwaggerMinusTypeSpec": (
                row["swaggerRaw"] - row["typeSpecAligned"]
            ),
            "absoluteDifference": abs(
                row["swaggerRaw"] - row["typeSpecAligned"]
            ),
            "relativeToSwagger": (
                (row["swaggerRaw"] - row["typeSpecAligned"])
                / row["swaggerRaw"]
                if row["swaggerRaw"]
                else None
            ),
        }
        for row in rows
        if row["swaggerRaw"] != row["typeSpecAligned"]
    ]
    result = {
        "schemaVersion": 1,
        "selectedProjects": len(population),
        "assessableProjects": len(rows),
        "failedProjects": sorted(failed),
        "swaggerRaw": sum(row["swaggerRaw"] for row in rows),
        "swaggerOccurrenceKeys": sum(
            row["swaggerOccurrenceKeys"] for row in rows
        ),
        "swaggerFileIndependent": sum(
            row["swaggerFileIndependent"] for row in rows
        ),
        "typeSpecRaw": sum(row["typeSpecRaw"] for row in rows),
        "typeSpecAligned": sum(row["typeSpecAligned"] for row in rows),
        "typeSpecSourceKeys": sum(
            row["typeSpecSourceKeys"] for row in rows
        ),
        "ambientDiagnostics": sum(row["ambient"] for row in rows),
        "swaggerProjects": swagger_projects,
        "typeSpecProjects": typespec_projects,
        "overlapProjects": sorted(
            set(swagger_projects) & set(typespec_projects)
        ),
        "swaggerOnlyProjects": sorted(
            set(swagger_projects) - set(typespec_projects)
        ),
        "typeSpecOnlyProjects": sorted(
            set(typespec_projects) - set(swagger_projects)
        ),
        "swaggerExcess": sum(
            max(0, item["signedSwaggerMinusTypeSpec"])
            for item in differences
        ),
        "typeSpecExcess": sum(
            max(0, -item["signedSwaggerMinusTypeSpec"])
            for item in differences
        ),
        "equalRawProjects": len(rows) - len(differences),
        "differences": sorted(
            differences,
            key=lambda item: (-item["absoluteDifference"], item["project"]),
        ),
        "defaultActivation": "not-assessed in full target-only run",
        "suppressedDiagnostics": (
            "not captured exhaustively; authored suppressions remain honored"
        ),
        "equivalence": "not-determined",
    }
    for own, original in [
        ("selectedProjects", "selectedProjectCount"),
        ("assessableProjects", "assessableProjectCount"),
        ("swaggerRaw", "validatorRawCount"),
        ("swaggerFileIndependent", "validatorFileIndependentCount"),
        ("typeSpecRaw", "nativeRawCount"),
        ("typeSpecAligned", "nativeAlignedCount"),
        ("typeSpecSourceKeys", "nativeSourceCount"),
        ("swaggerExcess", "rawValidatorExcess"),
        ("typeSpecExcess", "rawNativeExcess"),
        ("equalRawProjects", "projectsWithEqualRawCounts"),
        ("swaggerOnlyProjects", "validatorOnlyProjects"),
        ("typeSpecOnlyProjects", "nativeOnlyProjects"),
        ("overlapProjects", "overlapProjects"),
    ]:
        assert result[own] == coverage[original], (own, result[own], coverage[original])
    assert sorted(failed) == sorted(
        item["project"] for item in coverage["unassessedProjects"]
    )
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    print(json.dumps(recount(args.root), ensure_ascii=True, indent=2))

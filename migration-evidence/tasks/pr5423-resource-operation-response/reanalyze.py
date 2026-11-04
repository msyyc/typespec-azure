"""Recount saved observations only; never compiles or executes either linter."""

import argparse
import collections
import hashlib
import json
import pathlib


def summarize(observations, instances=None):
    projects = observations["projects"]
    native = {item["project"]: item for item in observations["native"]}
    assert len(native) == len(projects)
    members = observations["members"]
    swagger = [item for member in members for item in member["observations"]]
    swagger_by_project = collections.Counter(item["project"] for item in swagger)
    member_summary = []
    for member in members:
        rows = member["observations"]
        member_summary.append({
            "rule": member["rule"], "rawCount": len(rows),
            "projectCount": len({item["project"] for item in rows}),
            "nativeAttribution": (
                {
                    "status": "assessed exact operation and relevant comparison",
                    "mappedFindings": next(
                        item["mappedNativeFindings"]
                        for item in instances["summary"]["members"] if item["rule"] == member["rule"]
                    ),
                }
                if instances else "unassessed"
            ),
        })
    rows = []
    for project in projects:
        receipt = native[project["sourcePath"]]
        assert receipt["status"] == "success", receipt
        s = swagger_by_project[project["sourcePath"]]
        n = len(receipt["diagnostics"])
        difference = n - s
        rows.append({
            "project": project["sourcePath"], "apiVersion": project.get("apiVersion"),
            "swagger": s, "native": n,
            "nativeRaw": len(receipt["rawDiagnostics"]),
            "nativeDefault": len(receipt.get("defaultTargetDiagnostics", [])),
            "nativeMinusSwagger": difference,
            "absoluteDifference": abs(difference),
            "relativeDifference": abs(difference) / max(s, n) if max(s, n) else 0,
        })
    sp = {x["project"] for x in rows if x["swagger"]}
    np = {x["project"] for x in rows if x["native"]}
    member_project_comparisons = []
    for member in members:
        member_projects = {item["project"] for item in member["observations"]}
        member_project_comparisons.append({
            "rule": member["rule"],
            "swagger": len(member_projects), "sharedNative": len(np),
            "both": len(member_projects & np),
            "swaggerOnly": len(member_projects - np),
            "sharedNativeOnly": len(np - member_projects),
        })
    source_keys = {
        (project, diagnostic["rule"], diagnostic.get("sourceFile"),
         diagnostic.get("line"), diagnostic.get("column"))
        for project, receipt in native.items() for diagnostic in receipt["diagnostics"]
    }
    result = {
        "selectedProjects": len(projects), "succeededProjects": len(native),
        "failedProjects": [], "members": member_summary,
        "swaggerRaw": len(swagger),
        "swaggerReportedDocumentPathKeys": len({
            (x["rule"], x["project"], x["swaggerFile"], tuple(x["path"])) for x in swagger
        }),
        "swaggerFileIndependentMemberPaths": len({
            (x["rule"], x["project"], tuple(x["path"])) for x in swagger
        }),
        "nativeRaw": sum(x["nativeRaw"] for x in rows),
        "nativeAligned": sum(x["native"] for x in rows),
        "nativeSourceKeys": len(source_keys),
        "nativeDefault": sum(x["nativeDefault"] for x in rows),
        "swaggerProjects": sorted(sp), "nativeProjects": sorted(np),
        "overlapProjects": sorted(sp & np),
        "swaggerOnlyProjects": sorted(sp - np), "nativeOnlyProjects": sorted(np - sp),
        "projectGrouping": {
            "status": "assessed",
            "unit": "Projects with at least one selected finding",
            "identity": "project sourcePath in the frozen 487-project inventory",
            "swagger": len(sp), "native": len(np), "both": len(sp & np),
            "swaggerOnly": len(sp - np), "nativeOnly": len(np - sp),
            "neither": len(projects) - len(sp | np),
            "memberComparisons": member_project_comparisons,
            "limitation": "Shared-rule project overlap is not per-member finding attribution or operation equivalence",
        },
        "equalRawProjects": sum(x["swagger"] == x["native"] for x in rows),
        "swaggerHigherExcess": sum(max(0, x["swagger"] - x["native"]) for x in rows),
        "nativeHigherExcess": sum(max(0, x["native"] - x["swagger"]) for x in rows),
        "absoluteDifference": sum(x["absoluteDifference"] for x in rows),
        "comparableActionableUnit": "unassessed; no established cross-engine normalization",
        "memberNativeAttribution": "unassessed; no deterministic correspondence",
        "projects": sorted(rows, key=lambda x: (-x["absoluteDifference"], x["project"])),
    }
    if instances:
        result["instanceMapping"] = instances["summary"]
        result["comparableActionableUnit"] = (
            "Assessed exact project/HTTP-route references: 256 Swagger, 104 TypeSpec; "
            "routes are not normalized equivalent defects"
        )
        result["memberNativeAttribution"] = (
            "Assessed: 87 request mismatches mapped to PutRequestResponseSchemeArm; "
            "0 matching findings for the other three members; 17 shared-rule findings not credited"
        )
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parent)
    parser.add_argument("--output", type=pathlib.Path)
    parser.add_argument("--verify-inventory", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    if args.verify_inventory:
        inventory = json.loads((root / "integrity.json").read_text(encoding="utf-8"))
        for item in inventory["files"]:
            file = root / item["file"]
            assert file.is_file(), item["file"]
            assert hashlib.sha256(file.read_bytes()).hexdigest() == item["sha256"], item["file"]
    summary = summarize(
        json.loads((root / "observations.json").read_text(encoding="utf-8")),
        json.loads((root / "instance-mapping.json").read_text(encoding="utf-8")),
    )
    expected = json.loads((root / "summary.json").read_text(encoding="utf-8"))
    assert summary == expected, "Saved-observation recount differs from committed summary"
    if args.output:
        args.output.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({key: value for key, value in summary.items() if key != "projects"}, indent=2))

"""Recount saved TypeSpec diagnostics without installing packages or rerunning a linter."""
import collections
import json
import pathlib
import re
import sys

root = pathlib.Path(sys.argv[1])
receipts = []
for file in sorted(root.glob("native-*.json")):
    if re.fullmatch(r"native-\d+\.json", file.name):
        receipts.append(json.loads(file.read_text(encoding="utf-8")))
if not receipts:
    raise SystemExit("No native project receipts found; input must contain native-<index>.json")
groups = collections.Counter()
projects = []
failed = []
distinct_locations = set()
source_locations = set()
for receipt in receipts:
    if receipt["status"] != "success":
        failed.append({"project": receipt["project"], "status": receipt["status"], "error": receipt.get("error"), "ambientErrors": [d for d in receipt.get("ambientDiagnostics", []) if d.get("severity") == "error"]})
        continue
    diagnostics = receipt.get("rawDiagnostics", [])
    for diagnostic in diagnostics:
        distinct_locations.add((receipt["project"], json.dumps(diagnostic, sort_keys=True)))
        source_locations.add((receipt["project"], diagnostic.get("rule"), diagnostic.get("sourceFile"), diagnostic.get("line"), diagnostic.get("column")))
        message = diagnostic["message"]
        if message == "The PATCH operation must have a request body.":
            category = "paired-missing-patch-body"
        elif message == "The PATCH request body must contain at least one property.":
            category = "paired-empty-patch-body"
        elif message.startswith("The property '") and message.endswith("' in the PATCH body does not correspond to a property in the PUT body."):
            category = "paired-missing-json-leaf-name"
        elif "must be a subset" in message:
            category = "existing-resource-subset"
        elif message == "Resource PATCH must contain the 'tags' property.":
            category = "existing-resource-tags"
        elif message == "The request body of a PATCH must be a model with a subset of resource properties":
            category = "existing-resource-body"
        else:
            category = "other-unclassified"
        groups[category] += 1
    projects.append({"project": receipt["project"], "reportedDiagnostics": len(diagnostics), "diagnostics": diagnostics})
summary = {
    "selectedProjects": len(receipts),
    "successfullyCompiledProjects": len(projects),
    "failedOrUnassessedProjects": len(failed),
    "projectsWithTypeSpecFindings": sum(p["reportedDiagnostics"] > 0 for p in projects),
    "typeSpecReportedDiagnostics": sum(p["reportedDiagnostics"] for p in projects),
    "typeSpecDistinctProjectLocationMessageRecords": len(distinct_locations),
    "typeSpecDistinctProjectSourceLocations": len(source_locations),
    "deduplicationCaution": "Exact distinct saved project/location/message records only; not unique HTTP operations or semantic targets. The TypeSpec linter already deduplicates selected source targets internally.",
    "diagnosticsByNativeMessageFamily": dict(sorted(groups.items())),
    "messageFamilyCaution": "Grouping identifies native diagnostic message families only. It does not establish cross-engine semantic attribution or correspondence.",
    "swaggerAssessment": "not-evaluated: original rule is staging-only and was explicitly disabled in all 649 saved production Swagger logs",
    "swaggerReportedDiagnostics": None,
    "crossEngineCountsComparable": False,
    "equivalence": "not-functionally-equivalent; full corpus parity not assessed",
    "failures": failed,
    "projects": sorted(projects, key=lambda p: (-p["reportedDiagnostics"], p["project"])),
}
print(json.dumps(summary, indent=2, ensure_ascii=True))

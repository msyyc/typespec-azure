import collections
import json
import pathlib
import sys

root = pathlib.Path(sys.argv[1]).resolve()
coverage = json.loads((root / "coverage.json").read_text(encoding="utf-8"))
population = json.loads((root / "population.json").read_text(encoding="utf-8"))
selected = {item["sourcePath"] for item in population}
if len(selected) != len(population):
    raise RuntimeError("Duplicate selected project")
swagger = collections.Counter()
swagger_occurrences = set()
swagger_file_independent = set()
for member in coverage["members"]:
    for observation in member["observations"]:
        if observation["project"] not in selected:
            raise RuntimeError("Swagger observation outside frozen population")
        swagger[observation["project"]] += 1
        route = json.dumps(observation["path"], separators=(",", ":"))
        swagger_occurrences.add((member["rule"], observation["project"], observation["swaggerFile"], route))
        swagger_file_independent.add((member["rule"], observation["project"], route))
receipts = {}
for file in (root / "native-results").glob("native-*.json"):
    receipt = json.loads(file.read_text(encoding="utf-8"))
    project = receipt["project"]
    if project in receipts or project not in selected:
        raise RuntimeError("Duplicate or unknown native project")
    receipts[project] = receipt
if set(receipts) != selected:
    raise RuntimeError("Missing selected native receipts")
rows = []
unassessed = []
native_source_locations = set()
native_locationless = 0
for project in sorted(selected):
    receipt = receipts[project]
    if receipt["status"] != "success":
        unassessed.append({"project": project, "reason": receipt.get("error", "failed")})
        continue
    left = swagger[project]
    right = len(receipt["diagnostics"])
    for diagnostic in receipt["diagnostics"]:
        if diagnostic.get("sourceFile") is None:
            native_locationless += 1
        else:
            native_source_locations.add((diagnostic["rule"], project, diagnostic["sourceFile"], diagnostic["line"], diagnostic["column"]))
    rows.append({
        "project": project,
        "swagger": left,
        "native": right,
        "signedDifference": right - left,
        "absoluteDifference": abs(right - left),
        "relativeDifference": abs(right - left) / max(left, right, 1),
    })
result = {
    "selected": len(selected),
    "assessed": len(rows),
    "unassessed": unassessed,
    "rawSwaggerAssessed": sum(item["swagger"] for item in rows),
    "rawNativeAssessed": sum(item["native"] for item in rows),
    "equalRawCountProjects": sum(item["swagger"] == item["native"] for item in rows),
    "swaggerHigherExcess": sum(max(item["swagger"] - item["native"], 0) for item in rows),
    "nativeHigherExcess": sum(max(item["native"] - item["swagger"], 0) for item in rows),
    "absoluteDifference": sum(item["absoluteDifference"] for item in rows),
    "memberNativeAttribution": "unassessed; no inference from diagnostic messages",
    "conservativeLocationSummaries": {
        "swaggerReportedFileOccurrences": len(swagger_occurrences),
        "swaggerFileIndependentPaths": len(swagger_file_independent),
        "nativeSourceLocations": len(native_source_locations),
        "nativeLocationlessDiagnostics": native_locationless,
        "limitation": "Location summaries are not cross-engine actionable identities; distinct checks at one source location remain distinct raw diagnostics.",
    },
    "rows": rows,
}
for field, expected in [
    ("selected", coverage["selectedProjectCount"]),
    ("assessed", coverage["assessableProjectCount"]),
    ("rawSwaggerAssessed", coverage["validatorRawCount"]),
    ("rawNativeAssessed", coverage["nativeAlignedCount"]),
    ("equalRawCountProjects", coverage["projectsWithEqualRawCounts"]),
    ("swaggerHigherExcess", coverage["rawValidatorExcess"]),
    ("nativeHigherExcess", coverage["rawNativeExcess"]),
]:
    if result[field] != expected:
        raise RuntimeError(f"Independent count disagreement: {field}")
if len(swagger_file_independent) != coverage["validatorFileIndependentCount"]:
    raise RuntimeError("Independent Swagger location summary disagreement")
if len(native_source_locations) != coverage["nativeSourceCount"] or native_locationless != coverage["nativeLocationlessCount"]:
    raise RuntimeError("Independent TypeSpec location summary disagreement")
if len(sys.argv) > 2:
    pathlib.Path(sys.argv[2]).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({key: value for key, value in result.items() if key != "rows"}, indent=2))

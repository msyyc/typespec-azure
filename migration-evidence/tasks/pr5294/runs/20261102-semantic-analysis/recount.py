from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

root, archive, output = map(Path, sys.argv[1:])
assert not output.exists()
load = lambda file: json.loads(file.read_text(encoding="utf-8"))
inventory = load(archive / "archive-manifest.json")
for item in inventory["files"]:
    file = archive / item["path"]
    assert file.stat().st_size == item["bytes"], file
    assert hashlib.sha256(file.read_bytes()).hexdigest() == item["sha256"], file
summary = load(root / "analysis.json")
assessment = load(root / "difference-ledger.json")
native_receipts = [load(p) for p in (archive / "native-traces").glob("native-*.json")]
swagger_receipts = [load(p) for p in (archive / "swagger-traces").glob("swagger-*.json")]
assert len(native_receipts) == len(swagger_receipts) == 136
assert all(p["status"] == "success" for p in native_receipts)
assert all(not p["errors"] for p in swagger_receipts)
native = [dict(d, project=p["project"]) for p in native_receipts for d in p["diagnostics"]]
swagger = [dict(d, project=c["project"], route=c["route"], rule=c["rule"], document=c["document"])
           for p in swagger_receipts for c in p["captures"] for d in c["findings"]]
reported = [d for p in swagger_receipts for d in p["diagnostics"]]
original_swagger = load(archive / "saved/swagger-observations.json")
original_native = load(archive / "saved/native-results.json")
sw_identity = lambda d: (
    d["project"], d.get("document", d.get("swaggerFile")), d["rule"], d["message"],
    tuple(map(str, d["path"])),
)
ns_identity = lambda d: tuple(d.get(k) for k in
                              ("project", "rule", "message", "sourceFile", "line", "column"))
assert Counter(map(sw_identity, reported)) == Counter(map(sw_identity, original_swagger))
assert Counter(map(ns_identity, native)) == Counter(
    ns_identity(dict(d, project=p["project"])) for p in original_native for d in p["diagnostics"]
)
route = lambda d: (d["project"], d["route"])
check = lambda d: (*route(d), d["kind"], d["propertyPath"])
sw_routes, ns_routes = set(map(route, swagger)), set(map(route, native))
sc, nc = Counter(map(check, swagger)), Counter(map(check, native))
intersection = sc & nc
assert len(native) == 1337 and len(reported) == 975 and len(swagger) == 1057
assert (len(sw_routes), len(ns_routes), len(sw_routes & ns_routes)) == (304, 321, 277)
assert (sum(intersection.values()), sum((sc - nc).values()), sum((nc - sc).values())) == (834, 223, 503)
assert (len(sc), len(nc)) == (1057, 1333)
for engine, field, expected in (
    ("swaggerBeforeReportingUnshared", "swaggerRemaining", 223),
    ("typespecUnshared", "typespecRemaining", 503),
):
    counts = Counter()
    for row in assessment["differences"]:
        if field in row:
            counts[row[field]["category"]] += row[field]["count"]
    assert dict(counts) == assessment[engine] and sum(counts.values()) == expected
projects = summary["projects"]
for project in projects:
    name = project["project"]
    sw = [d for d in swagger if d["project"] == name]
    ns = [d for d in native if d["project"] == name]
    assert project["swaggerFunctionChecks"] == len(sw)
    assert project["typespecRaw"] == len(ns)
    assert project["swaggerRaw"] == sum(d["project"] == name for d in reported)
    assert project["sharedRoutes"] == len(set(map(route, sw)) & set(map(route, ns)))
assert len(projects) == 487
assert sum(max(0, p["swaggerRaw"] - p["typespecRaw"]) for p in projects) == 102
assert sum(max(0, p["typespecRaw"] - p["swaggerRaw"]) for p in projects) == 464
assert len([p for p in projects if p["swaggerRaw"] != p["typespecRaw"]
            or p["swaggerUnsharedCheckPathOccurrences"] + p["typespecUnsharedCheckPathOccurrences"]]) == 87
result = {
    "status": "passed",
    "mode": "Independent read-only recount and archive hash verification; not new lint execution",
    "inventoriedArchiveFiles": len(inventory["files"]),
    "projects": 487, "activeTraced": 136,
    "reported": {"swagger": 975, "typespec": 1337},
    "functionChecks": {"swagger": 1057, "typespec": 1337},
    "affectedPatchRoutes": {"swagger": 304, "typespec": 321, "shared": 277},
    "equalKeyOccurrences": 834,
    "unsharedObservations": {"swagger": 223, "typespec": 503},
    "differenceProjects": 87,
    "equivalence": "Not certified; source-versus-reference and explicit policy boundaries retained",
}
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps(result, indent=2))

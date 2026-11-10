import collections
import functools
import hashlib
import json
import pathlib
import re
import sys

root = pathlib.Path(sys.argv[1])
output = pathlib.Path(sys.argv[2])
shard = root / "results/by-rule/LatestVersionOfCommonTypesMustBeUsed.json"
data = json.loads(shard.read_text(encoding="utf-8"))
projects = {}


@functools.lru_cache(maxsize=64)
def document(relative):
    return json.loads((root / relative).read_text(encoding="utf-8-sig"))


def lookup(relative, path):
    try:
        value = document(relative)
        for component in path:
            value = value[int(component)] if isinstance(value, list) else value[component]
        return value
    except (KeyError, IndexError, ValueError, TypeError, FileNotFoundError):
        return None


for item in data["results"]:
    project = projects.setdefault(item["project"], {
        "raw": 0, "sourceAttribution": collections.Counter(),
        "observedReferenceGroups": {}, "unresolved": [],
    })
    project["raw"] += 1
    attribution = item.get("sourceAttribution", "missing")
    project["sourceAttribution"][attribution] += 1
    documents = item.get("sourceDocuments", []) or [item["swaggerFile"]]
    matches = [
        (name, value)
        for name in documents
        if isinstance(value := lookup(name, item["path"]), str)
        and "/common-types/resource-management/" in value.lower()
    ]
    if len(matches) != 1:
        project["unresolved"].append({
            "path": item["path"], "swaggerFile": item["swaggerFile"],
            "sourceDocuments": item.get("sourceDocuments", []),
            "sourceAttribution": attribution, "lookupMatches": len(matches),
        })
        continue
    name, value = matches[0]
    match = re.search(r"/common-types/resource-management/(v\d+)/([^/#]+)#", value, re.I)
    if not match:
        project["unresolved"].append({
            "path": item["path"], "swaggerFile": item["swaggerFile"],
            "sourceAttribution": attribution, "reference": value,
        })
        continue
    key = f"{match[1]}/{match[2]}"
    group = project["observedReferenceGroups"].setdefault(key, {
        "count": 0, "sample": {
            "document": name, "validatorInputFile": item.get("validatorInputFile"),
            "sourceAttribution": attribution, "sourceDocuments": item.get("sourceDocuments", []),
            "path": item["path"], "value": value,
        },
    })
    group["count"] += 1

result = {
    "schemaVersion": 1,
    "specsCommit": data["specsCommit"],
    "shardSha256": hashlib.sha256(shard.read_bytes()).hexdigest(),
    "method": "Exact saved JSON path lookup in reported sourceDocuments, falling back only to recorded swaggerFile when sourceDocuments is empty. Successful input-fallback lookups are candidate input values, not proven originating document identities. No fuzzy matching or semantic normalization.",
    "raw": data["count"],
    "projects": dict(sorted(projects.items())),
}
assert sum(p["raw"] for p in projects.values()) == data["count"]
assert sum(sum(g["count"] for g in p["observedReferenceGroups"].values()) + len(p["unresolved"]) for p in projects.values()) == data["count"]
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({
    "raw": result["raw"], "projects": len(projects),
    "exactPathLookupResolved": sum(sum(g["count"] for g in p["observedReferenceGroups"].values()) for p in projects.values()),
    "unresolved": sum(len(p["unresolved"]) for p in projects.values()),
    "references": dict(sum((collections.Counter({k: v["count"] for k, v in p["observedReferenceGroups"].items()}) for p in projects.values()), collections.Counter())),
}, indent=2))

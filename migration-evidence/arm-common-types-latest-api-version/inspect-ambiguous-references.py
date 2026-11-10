import collections
import json
import pathlib
import sys

dataset = pathlib.Path(sys.argv[1])
inspection = json.loads(pathlib.Path(sys.argv[2]).read_text(encoding="utf-8"))
metadata = json.loads((dataset / "_meta.json").read_text(encoding="utf-8"))
inventory = {project["sourcePath"]: project for project in metadata["projects"]}
results = []
for project, previous in inspection["projects"].items():
    if not previous["unresolved"]:
        continue
    documents = {
        name: json.loads((dataset / name).read_text(encoding="utf-8-sig"))
        for name in inventory[project]["swaggerFiles"]
    }
    by_path = collections.defaultdict(list)
    for item in previous["unresolved"]:
        by_path[tuple(item["path"])].append(item)
    groups = []
    for path, observations in by_path.items():
        candidates = []
        for name, source in documents.items():
            try:
                for component in path:
                    source = source[int(component)] if isinstance(source, list) else source[component]
                if isinstance(source, str) and "/common-types/resource-management/" in source:
                    candidates.append({"document": name, "value": source})
            except (KeyError, IndexError, ValueError, TypeError):
                pass
        groups.append({
            "path": list(path),
            "raw": len(observations),
            "validatorInputs": sorted({item["swaggerFile"] for item in observations}),
            "candidateDocuments": candidates,
            "distinctCandidateValues": sorted({item["value"] for item in candidates}),
        })
    results.append({
        "project": project,
        "raw": len(previous["unresolved"]),
        "groups": groups,
        "noCandidateRaw": sum(group["raw"] for group in groups if not group["candidateDocuments"]),
        "singleCandidateRaw": sum(group["raw"] for group in groups if len(group["candidateDocuments"]) == 1),
        "multipleCandidateRaw": sum(group["raw"] for group in groups if len(group["candidateDocuments"]) > 1),
    })
result = {
    "specsCommit": metadata["specsCommit"],
    "method": "For each missing-origin exact JSON path, search only the project's recorded emitted Swagger documents. Candidate documents/values are exact path observations, NOT recovered originating-document attribution or TypeSpec correspondence. Preserve all candidates and input identities.",
    "projects": results,
}
assert sum(project["raw"] for project in results) == 23732
pathlib.Path(sys.argv[3]).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps([
    {key: value for key, value in project.items() if key != "groups"}
    for project in results
], indent=2))

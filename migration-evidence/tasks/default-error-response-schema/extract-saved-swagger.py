import argparse
import collections
import functools
import json
import pathlib
import urllib.parse

parser = argparse.ArgumentParser()
parser.add_argument("--baseline", required=True, type=pathlib.Path)
parser.add_argument("--output", required=True, type=pathlib.Path)
args = parser.parse_args()
assert not args.output.exists(), "Do not replace saved evidence."
root = args.baseline
source = json.loads(
    (root / "results" / "by-rule" / "DefaultErrorResponseSchema.json").read_text(
        encoding="utf-8"
    )
)
documents = {}
source_indexes = {}
resolved_root = root.resolve()


@functools.lru_cache(maxsize=None)
def normalized(path):
    return path.resolve()


def document(path):
    path = normalized(path)
    assert path.is_relative_to(resolved_root)
    if path not in documents:
        documents[path] = json.loads(path.read_text(encoding="utf-8"))
    return documents[path]


def resolve(node, file, seen=()):
    while isinstance(node, dict) and "$ref" in node:
        ref = node["$ref"]
        identity = (str(file), ref)
        if identity in seen:
            raise ValueError(f"Cyclic reference: {identity}")
        seen = (*seen, identity)
        parsed = urllib.parse.urlsplit(ref)
        if parsed.scheme or parsed.netloc:
            raise ValueError(f"Unresolved remote reference: {ref}")
        file = normalized(file.parent / urllib.parse.unquote(parsed.path)) if parsed.path else file
        node = document(file)
        for piece in parsed.fragment.lstrip("/").split("/") if parsed.fragment else []:
            node = node[piece.replace("~1", "/").replace("~0", "~")]
    return node, file


def properties(node, file, seen=()):
    node, file = resolve(node, file, seen)
    if not isinstance(node, dict):
        return {}
    found = {}
    for parent in node.get("allOf", []):
        found.update(properties(parent, file, seen))
    for key, value in node.get("properties", {}).items():
        found[key] = (value, file)
    return found


def schema_facts(response, file):
    facts = {}
    response, response_file = resolve(response, file)
    schema = response.get("schema")
    facts["schema"] = schema
    if schema is None:
        facts["observedSchemaCause"] = "missing-schema"
    else:
        props = properties(schema, response_file)
        facts["topLevelProperties"] = sorted(props)
        if "error" not in props:
            facts["observedSchemaCause"] = "missing-error"
        else:
            inner = properties(*props["error"])
            facts["errorProperties"] = sorted(inner)
            missing = [key for key in ["code", "message"] if key not in inner]
            facts["observedSchemaCause"] = (
                "missing-" + "-and-".join(missing) if missing else "unresolved-predicate"
            )
    return facts


def source_operations(project):
    if project not in source_indexes:
        index = {}
        for file in sorted((root / "projects" / project / "swagger").rglob("*.json")):
            for route, path_item in document(file).get("paths", {}).items():
                for verb, operation in path_item.items():
                    if isinstance(operation, dict) and "responses" in operation:
                        index.setdefault((route, verb), []).append((file, operation))
        source_indexes[project] = index
    return source_indexes[project]


rows = []
for finding in source["results"]:
    row = {
        "project": finding["project"],
        "swaggerFile": finding["swaggerFile"],
        "path": finding["path"],
        "sourceDocuments": finding.get("sourceDocuments"),
        "validatorInputFile": finding.get("validatorInputFile"),
        "sourceAttribution": finding.get("sourceAttribution"),
    }
    candidates = []
    preferred = list(dict.fromkeys([*finding.get("sourceDocuments", []), finding["swaggerFile"]]))
    for relative in preferred:
        file = root / relative
        operation = document(file)
        try:
            for piece in finding["path"][:-2]:
                operation = operation[piece]
        except KeyError:
            continue
        candidates.append((file, operation))
    if not candidates:
        candidates = source_operations(finding["project"]).get(
            (finding["path"][1], finding["path"][2]), []
        )
    row["responseDocumentCandidates"] = [
        file.relative_to(root).as_posix() for file, _ in candidates
    ]
    row["sourceResolution"] = (
        "reported-document-contains-target"
        if candidates and candidates[0][0].relative_to(root).as_posix() in preferred
        else "retained-path-candidates; original file attribution remains ambiguous"
    )
    if not candidates:
        row["observedSchemaCause"] = "unassessed-source"
        rows.append(row)
        continue
    row["candidateOperationIds"] = sorted(
        {operation.get("operationId", "") for _, operation in candidates}
    )
    file, operation = candidates[0]
    response = operation["responses"]["default"]
    row["operationId"] = operation.get("operationId")
    row["response"] = response
    try:
        facts = [
            schema_facts(operation["responses"]["default"], file)
            for file, operation in candidates
        ]
        row.update(facts[0])
        row["candidateSchemaCauses"] = [
            item["observedSchemaCause"] for item in facts
        ]
        if len(set(row["candidateSchemaCauses"])) != 1:
            row["observedSchemaCause"] = "unassessed-ambiguous-source-shape"
    except (OSError, KeyError, ValueError, RecursionError) as error:
        row["observedSchemaCause"] = "unassessed-reference"
        row["error"] = str(error)
    rows.append(row)
summary = collections.Counter(row["observedSchemaCause"] for row in rows)
by_project = {}
for row in rows:
    by_project.setdefault(row["project"], collections.Counter())[row["observedSchemaCause"]] += 1
result = {
    "scope": "Deterministic inspection of retained observations and saved schema/reference closure; no validator or emitter executed.",
    "rawFindings": len(rows),
    "projectCount": len(by_project),
    "schemaCauses": dict(summary),
    "byProject": {key: dict(value) for key, value in sorted(by_project.items())},
    "findings": rows,
}
args.output.write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n"
)
print(json.dumps({key: value for key, value in result.items() if key != "findings"}, indent=2))

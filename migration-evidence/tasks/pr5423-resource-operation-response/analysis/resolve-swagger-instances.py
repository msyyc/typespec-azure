"""Resolve immutable observations against retained Swagger; never executes a linter."""

import argparse
import collections
import functools
import hashlib
import json
import pathlib
import re
import urllib.parse


parser = argparse.ArgumentParser()
parser.add_argument("--observations", type=pathlib.Path, required=True)
parser.add_argument("--dataset", type=pathlib.Path, required=True)
parser.add_argument("--output", type=pathlib.Path, required=True)
parser.add_argument("--traces", type=pathlib.Path)
args = parser.parse_args()
dataset = args.dataset.resolve()
observations = json.loads(args.observations.read_text(encoding="utf-8"))
documents = {}


def read(relative):
    if relative not in documents:
        file = (dataset / relative).resolve()
        assert file.is_relative_to(dataset), relative
        documents[relative] = json.loads(file.read_text(encoding="utf-8"))
    return documents[relative]


def pointer(document, segments):
    for segment in segments:
        document = document[int(segment)] if isinstance(document, list) else document[segment]
    return document


def reference(file, ref):
    external, _, fragment = ref.partition("#")
    parsed = urllib.parse.urlparse(external)
    if parsed.scheme:
        raise ValueError(f"Unexpected remote reference: {ref}")
    target = (dataset / file).parent / urllib.parse.unquote(external) if external else dataset / file
    target = target.resolve()
    assert target.is_relative_to(dataset), ref
    segments = [
        urllib.parse.unquote(x).replace("~1", "/").replace("~0", "~")
        for x in fragment.lstrip("/").split("/")
    ] if fragment else []
    return target.relative_to(dataset).as_posix(), segments


def dereference(file, node):
    seen = set()
    target = None
    while isinstance(node, dict) and isinstance(node.get("$ref"), str):
        file, segments = reference(file, node["$ref"])
        target = {"document": file, "pointer": segments}
        key = (file, tuple(segments))
        if key in seen:
            break
        seen.add(key)
        node = pointer(read(file), segments)
    return file, node, target


def xms_resource(file, schema, visited=None):
    visited = set() if visited is None else visited
    file, node, target = dereference(file, schema)
    key = (file, id(node))
    if key in visited:
        return False
    visited.add(key)
    return bool(isinstance(node, dict) and (
        node.get("x-ms-azure-resource")
        or any(xms_resource(file, base, visited) for base in node.get("allOf", []))
    ))


def schema_info(file, schema):
    if schema is None:
        return None
    resolved_file, resolved, target = dereference(file, schema)
    return {
        "raw": schema,
        "reference": target,
        "topLevelResolvedSchemaSha256": hashlib.sha256(
            json.dumps(resolved, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
        "xmsResourceInHierarchy": xms_resource(file, schema),
    }


def operation_info(file, route, verb, item):
    operation = item[verb]
    parameters = operation.get("parameters", [])
    body = None
    for parameter in parameters:
        parameter_file, parameter, _ = dereference(file, parameter)
        if parameter.get("in") == "body":
            body = schema_info(parameter_file, parameter.get("schema"))
            break
    responses = {}
    for status in ("200", "201", "202"):
        if status in operation.get("responses", {}):
            response_file, response, _ = dereference(file, operation["responses"][status])
            responses[status] = schema_info(response_file, response.get("schema"))
    return {
        "verb": verb, "route": route, "operationId": operation.get("operationId"),
        "request": body, "responses": responses,
    }


@functools.cache
def project_documents(project):
    prefix = dataset / "projects" / project / "swagger"
    return [file.relative_to(dataset).as_posix() for file in sorted(prefix.rglob("*.json"))]


resolved = []
for member in observations["members"]:
    for index, row in enumerate(member["observations"]):
        rule = member["rule"]
        record = {"id": f"{rule}:{index}", "observation": row, "candidates": []}
        path = row["path"]
        message = row.get("message", "")
        match = re.search(r"Operation: ?'([^']+)'", message) or re.search(r"Operation: ?([^\s]+)", message)
        expected_id = match.group(1).rstrip(".") if match else None
        if path and path[0] in ("paths", "x-ms-paths"):
            route = path[1]
            verbs = [path[2]] if len(path) > 2 and path[2] in ("put", "get", "patch") else ["put", "get", "patch"]
            candidates = []
            files = list(dict.fromkeys([row["swaggerFile"], row["validatorInputFile"], *project_documents(row["project"])]))
            for file in files:
                try:
                    document = read(file)
                except FileNotFoundError:
                    continue
                item = document.get(path[0], {}).get(route)
                if not item:
                    continue
                operations = [
                    operation_info(file, route, verb, item)
                    for verb in verbs if isinstance(item.get(verb), dict)
                ]
                if expected_id and not any(op["operationId"] == expected_id for op in operations):
                    continue
                if operations:
                    candidates.append({"document": file, "route": route, "operations": operations})
            record["candidates"] = candidates
            record["binding"] = "exact reported route and explicit operationId where supplied"
        elif rule == "ConsistentResponseSchemaForPut":
            target = {"document": row["swaggerFile"], "pointer": path}
            file = row["validatorInputFile"]
            document = read(file)
            for route, item in document.get("paths", {}).items():
                if not isinstance(item.get("put"), dict):
                    continue
                op = operation_info(file, route, "put", item)
                if any(schema and schema["reference"] == target for schema in op["responses"].values()):
                    record["candidates"].append({"document": file, "route": route, "operations": [op]})
            record["binding"] = "exact referenced schema document and JSON pointer in invoking PUT responses"
        record["candidateCount"] = len(record["candidates"])
        resolved.append(record)
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(resolved, indent=2) + "\n", encoding="utf-8", newline="\n")
if args.traces:
    native_bindings = []
    for trace_file in sorted(args.traces.glob("*.instances.json")):
        trace = json.loads(trace_file.read_text(encoding="utf-8"))
        for index, finding in enumerate(trace["findings"]):
            operation = next(op for op in trace["sourceOperations"] if op["operationKey"] == finding["operationKey"])
            candidates = []
            for file in project_documents(trace["project"]):
                document = read(file)
                for route, item in document.get("paths", {}).items():
                    if re.sub(r"\{[^{}]+\}", "{}", route) != re.sub(r"\{[^{}]+\}", "{}", operation["path"]):
                        continue
                    if isinstance(item.get(operation["verb"]), dict):
                        candidates.append({
                            "document": file, "route": route,
                            "operations": [operation_info(file, route, operation["verb"], item)],
                        })
            native_bindings.append({
                "id": f"{trace['project']}:{index}", "candidates": candidates,
            })
    args.output.with_name("native-swagger-bindings.json").write_text(
        json.dumps(native_bindings, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
print(json.dumps({
    "rawObservations": len(resolved),
    "unresolved": [r["id"] for r in resolved if not r["candidates"]],
    "candidateHistogram": dict(collections.Counter(r["candidateCount"] for r in resolved)),
    "members": {
        member["rule"]: dict(collections.Counter(r["candidateCount"] for r in resolved if r["observation"]["rule"] == member["rule"]))
        for member in observations["members"]
    },
}, indent=2))

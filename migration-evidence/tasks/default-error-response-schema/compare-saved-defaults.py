import argparse
import collections
import json
import pathlib
import urllib.parse


def read(file):
    return json.loads(file.read_text(encoding="utf-8-sig"))


class ProjectDocuments:
    def __init__(self, dataset):
        self.dataset = dataset.resolve()
        self.cache = {}

    def document(self, file):
        file = file.resolve()
        assert file.is_relative_to(self.dataset), file
        if file not in self.cache:
            self.cache[file] = read(file)
        return self.cache[file]

    def resolve(self, node, file):
        seen = set()
        chain = []
        while isinstance(node, dict) and "$ref" in node:
            identity = (file, node["$ref"])
            if identity in seen:
                raise ValueError("Cyclic direct reference")
            seen.add(identity)
            chain.append({
                "document": file.relative_to(self.dataset).as_posix(),
                "reference": node["$ref"],
            })
            reference = urllib.parse.urlsplit(node["$ref"])
            if reference.scheme or reference.netloc:
                raise ValueError("Nonlocal reference requires separate retained-source attribution")
            file = (
                (file.parent / urllib.parse.unquote(reference.path)).resolve()
                if reference.path else file
            )
            node = self.document(file)
            for part in reference.fragment.lstrip("/").split("/") if reference.fragment else []:
                node = node[part.replace("~1", "/").replace("~0", "~")]
        return node, file, chain

    def properties(self, schema, file, seen=frozenset()):
        schema, file, chain = self.resolve(schema, file)
        identity = (file, id(schema))
        if identity in seen:
            raise ValueError("Cyclic inheritance")
        if not isinstance(schema, dict):
            return {}, chain
        result = {}
        for parent in schema.get("allOf", []):
            properties, parent_chain = self.properties(parent, file, seen | {identity})
            result.update(properties)
            chain.extend(parent_chain)
        result.update({
            name: (value, file)
            for name, value in schema.get("properties", {}).items()
        })
        return result, chain

    def response_facts(self, operation, file):
        default = operation.get("responses", {}).get("default")
        if default is None:
            return {"schemaCause": "no-default-response"}
        response, response_file, chain = self.resolve(default, file)
        schema = response.get("schema")
        if schema is None:
            return {"schemaCause": "missing-schema", "referenceChain": chain}
        properties, schema_chain = self.properties(schema, response_file)
        chain.extend(schema_chain)
        if "error" not in properties:
            return {
                "schemaCause": "missing-error",
                "schema": schema,
                "topLevelProperties": sorted(properties),
                "referenceChain": chain,
            }
        error_properties, error_chain = self.properties(*properties["error"])
        chain.extend(error_chain)
        missing = [name for name in ["code", "message"] if name not in error_properties]
        return {
            "schemaCause": "missing-" + "-and-".join(missing) if missing else "property-presence-valid",
            "schema": schema,
            "topLevelProperties": sorted(properties),
            "errorProperties": sorted(error_properties),
            "referenceChain": chain,
        }


def source_key(operation):
    return tuple(operation.get(key) for key in ["sourceFile", "line", "column", "fullName"])


def main(args):
    metadata = read(args.baseline / "_meta.json")
    selected = {project["sourcePath"]: project for project in metadata["projects"]}
    assert len(selected) == 490
    captures = {}
    for directory in args.captures:
        for file in directory.glob("*.json"):
            if file.stem.isdigit():
                capture = read(file)
                captures[capture["project"]] = capture
    ledger = read(args.account / "diagnostic-ledger.json")
    by_project = collections.defaultdict(list)
    for diagnostic in ledger:
        if diagnostic["inScope"]:
            by_project[diagnostic["project"]].append(diagnostic)
    output = []
    for project, diagnostics in sorted(by_project.items()):
        documents = ProjectDocuments(args.baseline)
        operations = collections.defaultdict(list)
        for name in selected[project]["swaggerFiles"]:
            file = (args.baseline / name).resolve()
            document = documents.document(file)
            for section in ["paths", "x-ms-paths"]:
                for route, path_item in document.get(section, {}).items():
                    path_item, path_file, _ = documents.resolve(path_item, file)
                    for verb, operation in path_item.items():
                        if verb not in {"get", "put", "post", "patch", "delete", "head", "options", "trace"}:
                            continue
                        operation, operation_file, _ = documents.resolve(operation, path_file)
                        operations[(route, verb)].append((file, operation_file, operation, section))
        capture = captures[project]
        service_keys = (
            {source_key(operation) for operation in capture["serviceOperations"]}
            if "serviceOperations" in capture else None
        )
        for diagnostic in diagnostics:
            operation = diagnostic["operation"]
            candidates = []
            for file, operation_file, saved_operation, section in operations[
                (operation["path"], operation["verb"])
            ]:
                candidate = {
                    "swaggerDocument": file.relative_to(args.baseline.resolve()).as_posix(),
                    "section": section,
                    "apiVersion": documents.document(file).get("info", {}).get("version"),
                    "operationId": saved_operation.get("operationId"),
                }
                try:
                    candidate.update(documents.response_facts(saved_operation, operation_file))
                except (AssertionError, KeyError, ValueError, OSError, RecursionError) as error:
                    candidate["schemaCause"] = "unassessed-reference"
                    candidate["errorType"] = type(error).__name__
                    candidate["error"] = str(error).replace(
                        str(args.baseline.resolve()), "$DATASET"
                    ).replace(str(args.baseline), "$DATASET")
                candidates.append(candidate)
            output.append({
                "project": project,
                "sourceFile": diagnostic["sourceFile"],
                "line": diagnostic["line"],
                "column": diagnostic["column"],
                "fullName": operation["fullName"],
                "path": operation["path"],
                "verb": operation["verb"],
                "family": diagnostic["family"],
                "emitted": diagnostic["emitted"],
                "inUnprojectedHttpServiceGraph": (
                    source_key(operation) in service_keys if service_keys is not None else None
                ),
                "candidateCount": len(candidates),
                "schemaCauses": sorted({candidate["schemaCause"] for candidate in candidates}),
                "candidates": candidates,
                "boundary": "Exact retained path/verb candidates, not projected-program or equivalent-defect identity.",
            })
    assert len(output) == sum(row["inScope"] for row in ledger)
    assert not args.output.exists(), "Do not overwrite correspondence evidence."
    args.output.mkdir(parents=True)
    (args.output / "saved-default-correspondence.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    summary = {
        "projects": len(by_project),
        "diagnostics": len(output),
        "candidateCauseGroups": dict(collections.Counter(
            ",".join(row["schemaCauses"]) or "no-exact-path-verb-candidate"
            for row in output
        )),
        "sourceCheckAndSavedCauseGroups": dict(collections.Counter(
            row["family"] + ":" + (",".join(row["schemaCauses"]) or "no-exact-path-verb-candidate")
            for row in output
        )),
        "unprojectedServiceGraphAvailable": sum(
            row["inUnprojectedHttpServiceGraph"] is not None for row in output
        ),
        "emitterExecuted": False,
        "swaggerLinterExecuted": False,
    }
    (args.output / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", type=pathlib.Path, required=True)
    parser.add_argument("--account", type=pathlib.Path, required=True)
    parser.add_argument("--captures", type=pathlib.Path, nargs="+", required=True)
    parser.add_argument("--output", type=pathlib.Path, required=True)
    main(parser.parse_args())

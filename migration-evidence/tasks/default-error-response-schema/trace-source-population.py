import argparse
import collections
import importlib.util
import json
import pathlib
import sys

sys.dont_write_bytecode = True
module_spec = importlib.util.spec_from_file_location(
    "saved_defaults", pathlib.Path(__file__).with_name("compare-saved-defaults.py")
)
saved_defaults = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(saved_defaults)
read = saved_defaults.read


def available(events, selected):
    events = sorted(events)
    state = not events or not events[0][1]
    for index, added in events:
        if index <= selected:
            state = added
    return state


def unavailable_scopes(row, project):
    enums = [
        enum for enum in project["versionEnums"]
        if any(member["value"] == row["selectedApiVersion"] for member in enum["members"])
    ]
    if not enums:
        return []
    assert len(enums) == 1
    members = enums[0]["members"]
    ranks = {member["name"]: index for index, member in enumerate(members)}
    selected = next(index for index, member in enumerate(members) if member["value"] == row["selectedApiVersion"])
    scopes = collections.defaultdict(list)
    for annotation in row["annotations"]:
        name = annotation["decorator"].split(".")[-1]
        if name not in {"added", "removed"}:
            continue
        member = annotation["arguments"][0].split(".")[-1]
        assert member in ranks, (row["fullName"], member)
        scopes[(annotation["declaration"], annotation["direct"])].append(
            (ranks[member], name == "added")
        )
    return [
        {
            "declaration": key[0], "direct": key[1],
            "selectedVersionIndex": selected,
            "events": [
                {"index": index, "kind": "added" if added else "removed", **members[index]}
                for index, added in sorted(events)
            ],
        }
        for key, events in scopes.items() if not available(events, selected)
    ]


def main(args):
    assert not args.output.exists(), "Do not replace investigation evidence."
    assert not available([(2, False)], 2)
    assert available([(2, False), (3, True), (5, False)], 4)
    assert not available([(2, False), (3, True), (5, False)], 5)
    assert not available([(3, True)], 2)
    rows = read(args.source)
    project_source = {row["project"]: row for row in read(args.projects)}
    metadata = {row["sourcePath"]: row for row in read(args.baseline / "_meta.json")["projects"]}
    assert len(rows) == 130 and len(metadata) == 490
    indices = {}
    documents = {}

    def candidates(project, route, verb):
        if project not in indices:
            documents[project] = saved_defaults.ProjectDocuments(args.baseline)
            index = collections.defaultdict(list)
            for name in metadata[project]["swaggerFiles"]:
                file = (args.baseline / name).resolve()
                document = documents[project].document(file)
                for section in ["paths", "x-ms-paths"]:
                    for path, path_item in document.get(section, {}).items():
                        path_item, path_file, _ = documents[project].resolve(path_item, file)
                        for method, operation in path_item.items():
                            if method not in {"get", "put", "post", "patch", "delete", "head", "options", "trace"}:
                                continue
                            operation, operation_file, _ = documents[project].resolve(operation, path_file)
                            index[(path, method)].append((file, operation_file, operation))
            indices[project] = index
        return [
            {
                "swaggerDocument": file.relative_to(args.baseline.resolve()).as_posix(),
                "path": route, "verb": verb, "operationId": operation.get("operationId"),
                **documents[project].response_facts(operation, operation_file),
            }
            for file, operation_file, operation in indices[project][(route, verb)]
        ]

    output = []
    for row in rows:
        project = row["project"]
        item = {
            **row, "cause": None, "pathTransform": [], "savedCandidatesAfterExplicitTransform": [],
            "unavailableScopes": [],
        }
        if row["overrides"]:
            assert row["inUnprojectedHttpServiceGraph"] is False
            item["cause"] = "source-only-sdk-override"
        else:
            unavailable = unavailable_scopes(row, project_source[project])
            if unavailable:
                item["cause"] = "version-unavailable-in-selected-snapshot"
                item["unavailableScopes"] = unavailable
            else:
                route = row["capturedPath"]
                for annotation in row["annotations"]:
                    if annotation["decorator"].split(".")[-1] != "renamePathParameter":
                        continue
                    old, new = map(json.loads, annotation["arguments"])
                    assert "{" + old + "}" in route
                    route = route.replace("{" + old + "}", "{" + new + "}")
                    item["pathTransform"].append({"kind": "authored-legacy-parameter-rename", "old": old, "new": new, "annotation": annotation})
                if "Microsoft.ThisWillBeReplaced" in route:
                    providers = project_source[project]["providers"]
                    assert len(providers) == 1
                    provider = providers[0]["providerNamespace"]
                    assert isinstance(provider, str) and provider.startswith("Microsoft.")
                    route = route.replace("Microsoft.ThisWillBeReplaced", provider)
                    item["pathTransform"].append({"kind": "authored-arm-provider-namespace", "provider": providers[0]})
                if item["pathTransform"]:
                    found = candidates(project, route, row["verb"])
                    assert found and all(candidate["schemaCause"] == "property-presence-valid" for candidate in found), row["fullName"]
                    item["cause"] = "explicit-source-path-representation"
                    item["savedCandidatesAfterExplicitTransform"] = found
                else:
                    item["cause"] = "unassessed"
        output.append(item)
    summary = {
        "status": "completed",
        "diagnostics": len(output),
        "causes": dict(collections.Counter(row["cause"] for row in output)),
        "explicitPathTransformKinds": dict(collections.Counter(
            transform["kind"] for row in output for transform in row["pathTransform"]
        )),
        "availabilityControlsPassed": 4,
        "rawDiagnosticsOrCountsChanged": False,
        "compilerOrEmitterExecuted": False,
        "boundary": "Exact source annotations, enum order and source-backed literal substitutions into retained Swagger. Not fuzzy matching, a projected native rerun, current Swagger generation or equivalent-defect normalization.",
    }
    args.output.mkdir()
    for name, value in [("summary.json", summary), ("residual-population.json", output)]:
        (args.output / name).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", type=pathlib.Path, required=True)
    parser.add_argument("--source", type=pathlib.Path, required=True)
    parser.add_argument("--projects", type=pathlib.Path, required=True)
    parser.add_argument("--output", type=pathlib.Path, required=True)
    main(parser.parse_args())

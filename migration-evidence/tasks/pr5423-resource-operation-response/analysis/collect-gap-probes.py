"""Retain the bounded registry/owner experiments without changing corpus observations."""

import argparse
import hashlib
import json
import pathlib
import posixpath
import urllib.parse


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--root", type=pathlib.Path, required=True)
parser.add_argument("--traces", type=pathlib.Path, required=True)
parser.add_argument("--plan", type=pathlib.Path, required=True)
parser.add_argument("--specs", type=pathlib.Path, required=True)
parser.add_argument("--dataset", type=pathlib.Path, required=True)
args = parser.parse_args()
mapping = json.loads((args.root / "instance-mapping.json").read_text(encoding="utf-8"))


def traces():
    rows = {}
    for file in args.traces.glob("*.instances.json"):
        trace = json.loads(file.read_text(encoding="utf-8"))
        assert not trace["metadataDiagnostics"], trace["project"]
        rows[trace["project"]] = trace
    return rows


def operations(group, mode="Source"):
    return [op for binding in group[f"typeSpec{mode}Bindings"] for op in binding["operations"]]


def selected_status(operation):
    return next((s for s in ("200", "201", "202") if s in operation["responses"]), None)


registry_traces = traces()
owner_traces = registry_traces
registry = []
owners = []
for group in mapping["swaggerGroups"]:
    if group["classification"] in (
        "missed-request-registered-response-operation-absent-from-map",
        "missed-request-outside-lifecycle-map",
    ):
        source, = operations(group)
        selected, = operations(group, "Selected")
        status = selected_status(group["swaggerOperations"][0])
        matches = [
            row for row in registry_traces[group["project"]]["registeredPuts"]
            if row["operationKey"] == source["operationKey"]
        ]
        same = any(
            row["kind"] == "createOrUpdate" and not row["requestIsResource"]
            and row["requestBodyKind"] == "single"
            and any(
                str(response["status"]) == status and any(body["isResource"] for body in response["bodies"])
                for response in row["successResponses"]
            )
            for row in matches
        )
        payloads_agree = all(source[key] == selected[key] for key in ("request", "responses"))
        if same:
            assert payloads_agree, group["id"]
        registry.append({
            "checkId": group["id"], "project": group["project"], "operationKey": source["operationKey"],
            "registrations": matches, "selectedStatus": status,
            "sourceSelectedPayloadsAgree": payloads_agree,
            "selectedCanonicalComparison": same,
        })
    empty_verbs = {
        op["verb"] for op in group["swaggerOperations"]
        if selected_status(op) == "200" and op["responses"]["200"] is None
    }
    if group["rule"] == "PutGetPatchResponseSchema" and empty_verbs:
        target_operations = [op for op in operations(group) if op["verb"] in empty_verbs]
        rule = "no-response-body"
    elif group["classification"] == "missed-200-201-response-equality":
        target_operations = operations(group)
        rule = "response-schema-problem"
    else:
        continue
    assert target_operations, group["id"]
    keys = {op["operationKey"] for op in target_operations}
    trace = owner_traces[group["project"]]
    owners.append({
        "checkId": group["id"], "project": group["project"], "ownerRule": rule,
        "targetOperations": [op["operationKey"] for op in target_operations],
        "predicateFindingsIgnoringSuppressions": [
            row for row in trace["ownerPredicates"] if row["operationKey"] in keys and row["rule"] == rule
        ],
        "configuredFindings": [
            row for row in trace["relatedDiagnostics"]
            if row.get("operationKey") in keys and row["rule"].endswith("/" + rule)
        ],
        "authoredSuppressions": [
            {
                "sourceFile": op["sourceFile"], "line": index + 1,
                "directive": line.strip(), "operationKey": op["operationKey"],
            }
            for op in target_operations
            for index, line in enumerate(
                (args.specs / group["project"] / op["sourceFile"]).read_text(encoding="utf-8").splitlines()
            )
            if op["line"] - 8 <= index < op["line"] - 1
            and "#suppress" in line and f"/{rule}\"" in line
        ],
    })
    assert owners[-1]["authoredSuppressions"], group["id"]


def dereference(schema, document):
    seen = set()
    context = None
    while "$ref" in schema:
        ref_document, fragment = urllib.parse.urldefrag(schema["$ref"])
        if ref_document:
            document = posixpath.normpath(posixpath.join(posixpath.dirname(document), ref_document))
        pointer = [part.replace("~1", "/").replace("~0", "~") for part in fragment.lstrip("/").split("/")]
        context = {"document": document, "pointer": pointer}
        key = (document, tuple(pointer))
        assert key not in seen, key
        seen.add(key)
        schema = json.loads((args.dataset / document).read_text(encoding="utf-8"))
        for part in pointer:
            schema = schema[part]
    return schema, document, context


collections = []
for group in mapping["swaggerGroups"]:
    if group["id"] not in {"a4753c8793120f98", "932685760e4abb70", "96597104b5cfbfbf", "2d6708f576319f69"}:
        continue
    roles = []
    for operation in group["swaggerOperations"]:
        response = operation["responses"][selected_status(operation)]
        schema, document, context = dereference(response["raw"], group["document"])
        value = schema.get("properties", {}).get("value")
        if schema.get("type") == "array":
            role, items = "array", schema["items"]
        elif value and value.get("type") == "array":
            role, items = "list-envelope", value["items"]
        else:
            role, items = "entity", None
        if items:
            _, _, entity = dereference(items, document)
        else:
            entity = context
        assert entity, (group["id"], role)
        roles.append({
            "verb": operation["verb"], "operationId": operation["operationId"],
            "role": role, "payload": response["raw"], "itemSchema": items, "entityContext": entity,
        })
    assert all(role["entityContext"] == roles[0]["entityContext"] for role in roles), group["id"]
    collections.append({"checkId": group["id"], "sameEntityContext": True, "roles": roles})

task = json.loads((args.root / "task.json").read_text(encoding="utf-8"))
receipt = {
    "candidate": task["candidateCommit"],
    "core": task["coreCommit"],
    "coreRepository": "https://github.com/microsoft/typespec",
    "specs": task["specsCommit"],
    "scope": "Metadata and existing visitor-predicate inspection only; no source changes, suppression removal, emission or new coverage credit",
    "plan": json.loads(args.plan.read_text(encoding="utf-8")),
}
summary = json.loads((args.traces / "inspection-summary.json").read_text(encoding="utf-8"))
receipt["results"] = summary
receipt["rawTraceHashes"] = [
    {
        "file": file.name, "sha256": hashlib.sha256(file.read_bytes()).hexdigest(),
        "bytes": file.stat().st_size,
    }
    for file in sorted(args.traces.glob("*.instances.json"))
]
receipt["savedDiagnosticEquality"] = all(row["savedDiagnosticEquality"] for row in summary)
receipt["metadataDiagnostics"] = 0
receipt["inspectorScope"] = (
    "Final-source Set-based request traversal, retained-map response traversal and existing owner predicates "
    "were inspected together; findings must exactly reproduce the fresh full-corpus receipts."
)
probes = {
    "registry": {"projects": len({row["project"] for row in registry}), "checks": registry},
    "owners": {"projects": len({row["project"] for row in owners}), "checks": owners},
    "collectionEvidence": collections,
}
(args.root / "gap-probes.json").write_text(json.dumps(probes, indent=2) + "\n", encoding="utf-8", newline="\n")
(args.root / "receipts/gap-tradeoffs-20261105.json").write_text(
    json.dumps(receipt, indent=2) + "\n", encoding="utf-8", newline="\n",
)
print(json.dumps({
    "registryChecks": len(registry), "recoverable": sum(row["selectedCanonicalComparison"] for row in registry),
    "ownerChecks": len(owners),
    "ownerPredicateChecks": sum(bool(row["predicateFindingsIgnoringSuppressions"]) for row in owners),
    "configuredOwnerChecks": sum(bool(row["configuredFindings"]) for row in owners),
}))

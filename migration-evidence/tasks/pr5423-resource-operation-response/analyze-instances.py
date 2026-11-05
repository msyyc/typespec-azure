import argparse
import collections
import hashlib
import json
import pathlib
import re


parser = argparse.ArgumentParser()
parser.add_argument("--root", type=pathlib.Path, required=True)
parser.add_argument("--output", type=pathlib.Path)
args = parser.parse_args()
root = args.root
swagger_rows = json.loads((root / "swagger-bindings.json").read_text(encoding="utf-8"))
traces = {
    trace["project"]: trace
    for trace in json.loads((root / "instance-inputs.json").read_text(encoding="utf-8"))
}
assert all(row["observation"]["project"] in traces for row in swagger_rows)
native_swagger = {
    item["id"]: item["candidates"]
    for item in json.loads((root / "native-swagger-bindings.json").read_text(encoding="utf-8"))
}


def shape(route):
    return re.sub(r"\{[^{}]+\}", "{}", route)


def bind(trace, route, verb, mode):
    operations = trace[mode]
    matches = [op for op in operations if op["verb"] == verb and op["path"] == route]
    if matches:
        return matches, "exact HTTP method and route"
    matches = [op for op in operations if op["verb"] == verb and shape(op["path"]) == shape(route)]
    return matches, "HTTP method and literal route segments with parameter-name normalization"


def family(finding):
    if finding["message"] == "ARM PUT operations must have a request body.":
        return "missingRequest"
    if finding["message"].startswith("PUT request body must use resource model "):
        return "requestMismatch"
    if finding["message"].startswith("[RPC 008]:"):
        return "responseMismatch"
    raise ValueError(finding)


def request_comparison(operation):
    return list(dict.fromkeys(
        association["resource"]
        for association in operation["associations"]
        if association["checkedPutRequest"]
    ))


def body_names(operation, status):
    return {
        body["name"] if body["registeredResource"] else "(unregistered) " + body["name"]
        for response in operation["responses"]
        if str(response["statusCodes"]) == str(status)
        for body in response["bodies"] if body
    }


groups = {}
for row in swagger_rows:
    assert len(row["candidates"]) == 1, row["id"]
    candidate = row["candidates"][0]
    key = json.dumps([
        row["observation"]["rule"], row["observation"]["project"],
        candidate["document"], candidate["route"], candidate["operations"],
    ], sort_keys=True)
    if key not in groups:
        groups[key] = {
            "id": hashlib.sha256(key.encode()).hexdigest()[:16],
            "rule": row["observation"]["rule"],
            "project": row["observation"]["project"],
            "document": candidate["document"],
            "route": candidate["route"],
            "swaggerOperations": candidate["operations"],
            "rawObservationIds": [],
            "rawObservations": [],
        }
    groups[key]["rawObservationIds"].append(row["id"])
    groups[key]["rawObservations"].append({
        k: row["observation"].get(k)
        for k in ("swaggerFile", "validatorInputFile", "path", "message", "sourceAttribution")
    })

native_findings = {}
for project, trace in traces.items():
    for index, finding in enumerate(trace["findings"]):
        identity = f"{project}:{index}"
        matches = [op for op in trace["sourceOperations"] if op["operationKey"] == finding["operationKey"]]
        assert len(matches) == 1, (identity, len(matches))
        operation = matches[0]
        selected = [
            op for op in trace["selectedOperations"]
            if op["operationKey"] == operation["operationKey"]
        ]
        native_findings[identity] = {
            "id": identity, "project": project,
            "family": family(finding), "finding": finding,
            "operation": operation,
            "selectedVersionOperations": selected,
            "sameOperationSwaggerGroups": [],
            "mappedSwaggerGroups": [],
            "emittedBindings": native_swagger[identity],
        }

for group in groups.values():
    trace = traces[group["project"]]
    bound = []
    selected_bound = []
    for op in group["swaggerOperations"]:
        source, source_method = bind(trace, group["route"], op["verb"], "sourceOperations")
        selected, selected_method = bind(trace, group["route"], op["verb"], "selectedOperations")
        bound.append({
            "verb": op["verb"], "binding": source_method,
            "operations": source,
        })
        selected_bound.append({
            "verb": op["verb"], "binding": selected_method,
            "operations": selected,
        })
    group["typeSpecSourceBindings"] = bound
    group["typeSpecSelectedBindings"] = selected_bound
    source_ops = [op for entry in bound for op in entry["operations"]]
    related = [
        finding for finding in native_findings.values()
        if finding["project"] == group["project"]
        and any(op["operationKey"] == finding["operation"]["operationKey"] for op in source_ops)
    ]
    group["sameOperationNativeFindingIds"] = [finding["id"] for finding in related]
    group["mappedNativeFindingIds"] = []
    for finding in related:
        finding["sameOperationSwaggerGroups"].append(group["id"])
    ambiguous = any(len(entry["operations"]) > 1 for entry in bound)
    if ambiguous:
        group["classification"] = "ambiguous-source-operation"
    elif not source_ops:
        group["classification"] = "emitted-operation-not-found-in-source-HTTP-graph"
    elif group["rule"] == "PutRequestResponseSchemeArm":
        op = next(op for op in source_ops if op["verb"] == "put")
        resources = request_comparison(op)
        status = "200" if "200" in group["swaggerOperations"][0]["responses"] else "201"
        compared_response_types = body_names(op, status)
        matching = [
            finding for finding in related
            if finding["family"] == "requestMismatch"
            and len(resources) == 1 and compared_response_types == set(resources)
        ]
        if matching:
            group["classification"] = "mapped-request-mismatch"
            group["mappedNativeFindingIds"] = [finding["id"] for finding in matching]
            for finding in matching:
                finding["mappedSwaggerGroups"].append(group["id"])
        elif related:
            group["classification"] = "same-operation-different-comparison"
        elif not resources:
            if any(a["group"] == "lists" for a in op["associations"]):
                group["classification"] = "missed-request-outside-lifecycle-map"
            elif op["associations"]:
                group["classification"] = "missed-request-not-selected-createOrUpdate"
            else:
                registered_responses = {
                    body["name"] for response in op["responses"]
                    for body in response["bodies"] if body and body["registeredResource"]
                }
                group["classification"] = (
                    "missed-request-registered-response-operation-absent-from-map"
                    if registered_responses else "missed-request-unregistered-response-operation"
                )
        elif not op.get("request"):
            group["classification"] = "source-emission-request-policy-difference"
        elif op["request"]["bodyKind"] != "single":
            group["classification"] = "missed-request-nonsingle-body"
        elif op["request"]["effectiveType"]["name"] in resources:
            group["classification"] = "source-canonical-request-agrees-emitted-schemas-differ"
        else:
            group["classification"] = "expected-request-warning-suppressed-or-unresolved"
    elif group["rule"] == "ConsistentResponseSchemaForPut":
        responses = group["swaggerOperations"][0]["responses"]
        same_raw = (
            responses.get("200") is not None and responses.get("201") is not None
            and responses["200"]["raw"] == responses["201"]["raw"]
        )
        group["classification"] = (
            "upstream-identity-false-positive"
            if same_raw else "missed-200-201-response-equality"
        )
    elif group["rule"] == "XmsResourceInPutResponse":
        group["classification"] = "missed-emitted-resource-extension-check"
    else:
        refs = [
            next((
                schema and schema["raw"].get("$ref")
                for status in ("200", "201", "202") if status in op["responses"]
                for schema in [op["responses"][status]]
            ), None)
            for op in group["swaggerOperations"]
        ]
        group["swaggerComparedResponseRefs"] = refs
        checked = [
            op for op in source_ops
            if any(a["group"] == "lists" or (
                a["group"] == "lifecycle" and a["kind"] in ("read", "createOrUpdate", "update")
            ) for a in op["associations"])
        ]
        group["responseTraversalContext"] = (
            "no-associated-operations" if not checked
            else "no-registered-response-candidates" if not any(op["responseCandidates"] for op in checked)
            else "canonical-response-traversal-does-not-report"
        )
        group["classification"] = (
            "missed-cross-operation-selected-ref-absent"
            if None in refs else "missed-cross-operation-distinct-response-refs"
        )
    group["nativeResponseCheckContext"] = [
        {
            "operation": op["operation"],
            "associations": op["associations"],
            "responseCandidates": op["responseCandidates"],
        }
        for op in source_ops
    ]

for finding in native_findings.values():
    if finding["mappedSwaggerGroups"]:
        finding["classification"] = "mapped-request-mismatch"
    elif not finding["selectedVersionOperations"]:
        finding["classification"] = "source-only-operation-not-in-selected-version"
    elif finding["family"] == "missingRequest":
        finding["classification"] = "additional-missing-request-policy"
    elif finding["sameOperationSwaggerGroups"]:
        finding["classification"] = "same-operation-different-comparison"
    else:
        emitted = finding["emittedBindings"]
        if len(emitted) == 1 and not ({"200", "201"} & emitted[0]["operations"][0]["responses"].keys()):
            finding["classification"] = "additional-request-check-outside-swagger-200-201-selector"
        else:
            finding["classification"] = "native-only-request-policy-or-schema-identity-unresolved"

summary = {
    "rawSwagger": len(swagger_rows),
    "checkedSwaggerInstanceGroups": len(groups),
    "nativeFindings": len(native_findings),
    "nativeFamilies": dict(collections.Counter(f["family"] for f in native_findings.values())),
    "members": [],
    "nativeClassifications": dict(collections.Counter(f["classification"] for f in native_findings.values())),
    "traceProjects": len(traces),
}
for rule in dict.fromkeys(group["rule"] for group in groups.values()):
    member = [group for group in groups.values() if group["rule"] == rule]
    summary["members"].append({
        "rule": rule, "raw": sum(len(g["rawObservationIds"]) for g in member),
        "groups": len(member),
        "classifications": dict(collections.Counter(g["classification"] for g in member)),
        "sameOperationNativeFindings": len({i for g in member for i in g["sameOperationNativeFindingIds"]}),
        "mappedNativeFindings": len({i for g in member for i in g["mappedNativeFindingIds"]}),
        "classificationRawCounts": {
            classification: sum(len(g["rawObservationIds"]) for g in member if g["classification"] == classification)
            for classification in dict.fromkeys(g["classification"] for g in member)
        },
    })
swagger_routes = {(g["project"], g["route"]) for g in groups.values()}
native_routes = {(f["project"], f["operation"]["path"]) for f in native_findings.values()}
summary["routeGrouping"] = {
    "identity": "exact frozen project sourcePath and HTTP route; methods and member checks are not separate routes",
    "swagger": len(swagger_routes), "native": len(native_routes),
    "both": len(swagger_routes & native_routes),
    "swaggerOnly": len(swagger_routes - native_routes),
    "nativeOnly": len(native_routes - swagger_routes),
}
project_groups = collections.Counter(g["project"] for g in groups.values())
project_native = collections.Counter(f["project"] for f in native_findings.values())
summary["projects"] = [
    {
        "project": project,
        "swaggerRaw": sum(len(g["rawObservationIds"]) for g in groups.values() if g["project"] == project),
        "swaggerCheckGroups": project_groups[project],
        "nativeFindings": project_native[project],
        "swaggerRoutes": sum(p == project for p, _ in swagger_routes),
        "nativeRoutes": sum(p == project for p, _ in native_routes),
        "mappedFindings": sum(
            bool(f["mappedSwaggerGroups"]) for f in native_findings.values() if f["project"] == project
        ),
    }
    for project in sorted(traces)
]
summary["routeCountDifferences"] = {
    "swaggerHigherExcess": sum(max(0, p["swaggerRoutes"] - p["nativeRoutes"]) for p in summary["projects"]),
    "nativeHigherExcess": sum(max(0, p["nativeRoutes"] - p["swaggerRoutes"]) for p in summary["projects"]),
    "absoluteDifference": sum(abs(p["nativeRoutes"] - p["swaggerRoutes"]) for p in summary["projects"]),
}
result = {
    "summary": summary, "swaggerGroups": list(groups.values()),
    "nativeFindings": list(native_findings.values()),
}
if args.output:
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
else:
    expected = json.loads((root / "instance-mapping.json").read_text(encoding="utf-8"))
    assert result == expected, "Instance assessment differs from saved evidence"
print(json.dumps({key: value for key, value in summary.items() if key != "projects"}, indent=2))

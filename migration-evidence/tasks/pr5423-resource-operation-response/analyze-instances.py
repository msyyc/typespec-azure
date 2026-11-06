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
    if finding["message"] == "ARM PUT success responses must return a resource model.":
        return "resourceIdentity"
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
        (
            body["canonicalResources"][0]
            if body.get("canonicalResources")
            else "(unregistered) " + body["name"]
        ) if "canonicalResources" in body
        else body["name"] if body["registeredResource"] else "(unregistered) " + body["name"]
        for response in operation["responses"]
        if str(response["statusCodes"]) == str(status)
        for body in response["bodies"] if body
    }


def bodies_at(operation, status):
    return [
        body
        for response in operation["responses"]
        if (
            str(response["statusCodes"]) == str(status)
            or isinstance(response["statusCodes"], dict)
            and response["statusCodes"]["start"] <= int(status) <= response["statusCodes"]["end"]
        )
        for body in response["bodies"] if body and not body.get("void")
    ]


def selected_body_status(operation):
    return next((status for status in ("200", "201") if bodies_at(operation, status)), None)


def body_key(body):
    return (
        body["name"], body["kind"],
        json.dumps(body.get("declaration", {}), sort_keys=True),
    )


def canonical_response_models(operation):
    return {
        association["resource"]
        for association in operation["associations"]
        if association.get("checkedResponseKind") in ("read", "createOrUpdate", "update", "list")
        or association["group"] == "lifecycle" and association["kind"] in ("read", "createOrUpdate", "update")
        or association["group"] == "lists"
    }


def resource_response_matches(group, finding):
    if finding["family"] not in ("resourceIdentity", "responseMismatch"):
        return False
    swagger_op = group["swaggerOperations"][0]
    status = next((s for s in ("200", "201") if swagger_op["responses"].get(s)), None)
    if status is None or swagger_op["responses"][status]["xmsResourceInHierarchy"]:
        return False
    operation = finding["operation"]
    selected = [
        op for binding in group["typeSpecSelectedBindings"]
        for op in binding["operations"] if op["verb"] == "put"
    ]
    if (
        len(selected) != 1
        or selected_body_status(operation) != status
        or selected_body_status(selected[0]) != status
        or {body_key(body) for body in bodies_at(operation, status)}
        != {body_key(body) for body in bodies_at(selected[0], status)}
    ):
        return False
    invalid_selected = {
        body_key(body) for body in bodies_at(selected[0], status)
        if body.get("nativeResource") is False
    }
    return any(
        body.get("nativeResource") is False and body_key(body) in invalid_selected
        for body in bodies_at(operation, status)
    )


def request_comparison_matches(group, finding, source_ops):
    puts = [op for op in source_ops if op["verb"] == "put"]
    if finding["family"] != "requestMismatch" or len(puts) != 1:
        return False
    selected = [
        op for binding in group["typeSpecSelectedBindings"]
        for op in binding["operations"] if op["verb"] == "put"
    ]
    if len(selected) != 1 or selected[0]["operationKey"] != puts[0]["operationKey"]:
        return False
    source_request, selected_request = puts[0].get("request"), selected[0].get("request")
    if (
        not source_request or not selected_request
        or source_request["bodyKind"] != "single" or selected_request["bodyKind"] != "single"
        or body_key(source_request["effectiveType"]) != body_key(selected_request["effectiveType"])
    ):
        return False
    resources = request_comparison(puts[0])
    status = "200" if "200" in group["swaggerOperations"][0]["responses"] else "201"
    return (
        len(resources) == 1 and body_names(puts[0], status) == set(resources)
        and {body_key(body) for body in bodies_at(puts[0], status)}
        == {body_key(body) for body in bodies_at(selected[0], status)}
    )


def response_comparison_matches(group, finding, source_ops):
    if finding["family"] != "responseMismatch":
        return False
    operation = finding["operation"]
    resources = canonical_response_models(operation)
    if len(resources) != 1:
        return False
    canonical, = resources
    selected_ops = [
        op for entry in group["typeSpecSelectedBindings"] for op in entry["operations"]
    ]
    if group["rule"] == "ConsistentResponseSchemaForPut":
        selected = [op for op in selected_ops if op["operationKey"] == operation["operationKey"]]
        if len(selected) != 1 or any(
            {body_key(body) for body in bodies_at(operation, status)}
            != {body_key(body) for body in bodies_at(selected[0], status)}
            for status in ("200", "201")
        ):
            return False
        by_status = [
            body_names(operation, status)
            for status in ("200", "201")
        ]
        return all(by_status) and any(names == {canonical} for names in by_status) and any(
            canonical not in names for names in by_status
        )
    compared = []
    for swagger_op in group["swaggerOperations"]:
        status = next((status for status in ("200", "201", "202") if status in swagger_op["responses"]), None)
        if status is None or swagger_op["responses"][status] is None:
            return False
        bound = [op for op in source_ops if op["verb"] == swagger_op["verb"]]
        selected = [op for op in selected_ops if op["verb"] == swagger_op["verb"]]
        if len(bound) != 1 or len(selected) != 1:
            return False
        names = body_names(bound[0], status)
        if {body_key(body) for body in bodies_at(bound[0], status)} != {
            body_key(body) for body in bodies_at(selected[0], status)
        }:
            return False
        if any(
            body.get("collectionItem", {}).get("name") == canonical
            for body in bodies_at(bound[0], status)
            if body.get("collectionItem")
        ):
            return False
        compared.append((bound[0], names))
    own = next((names for op, names in compared if op["operationKey"] == operation["operationKey"]), set())
    return bool(own) and canonical not in own and any(
        op["operationKey"] != operation["operationKey"] and names == {canonical}
        for op, names in compared
    )


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
native_predicates = {}
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
    configured = collections.defaultdict(list)
    for finding in native_findings.values():
        if finding["project"] == project:
            configured[(finding["finding"].get("rule"), finding["finding"]["message"],
                        finding["operation"]["operationKey"])].append(finding["id"])
    for index, predicate in enumerate(trace.get("selectedPredicates", [])):
        matches = [op for op in trace["sourceOperations"] if op["operationKey"] == predicate["operationKey"]]
        assert len(matches) == 1, (project, predicate)
        key = (predicate["rule"], predicate["message"], predicate["operationKey"])
        configured_ids = configured[key]
        identity = f"{project}:predicate:{index}"
        native_predicates[identity] = {
            "id": identity, "project": project, "family": family(predicate),
            "finding": predicate, "operation": matches[0],
            "configuredFindingIds": [configured_ids.pop(0)] if configured_ids else [],
            "mappedSwaggerGroups": [],
        }
    if "selectedPredicates" in trace:
        assert not any(configured.values()), (project, configured)

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
        matching = [
            finding for finding in related
            if request_comparison_matches(group, finding, source_ops)
        ]
        if matching:
            group["classification"] = "mapped-request-mismatch"
            group["mappedNativeFindingIds"] = [finding["id"] for finding in matching]
            for finding in matching:
                finding["mappedSwaggerGroups"].append(group["id"])
        elif any(finding["family"] != "resourceIdentity" for finding in related):
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
        if not same_raw:
            matching = [
                finding for finding in related
                if response_comparison_matches(group, finding, source_ops)
            ]
            if matching:
                group["classification"] = "mapped-response-mismatch"
                group["mappedNativeFindingIds"] = [finding["id"] for finding in matching]
                for finding in matching:
                    finding["mappedSwaggerGroups"].append(group["id"])
    elif group["rule"] == "XmsResourceInPutResponse":
        group["classification"] = "unpaired-native-resource-response-check"
        swagger_op = group["swaggerOperations"][0]
        status = next((s for s in ("200", "201") if swagger_op["responses"].get(s)), None)
        selected = [
            op for entry in selected_bound for op in entry["operations"] if op["verb"] == "put"
        ]
        matching = [
            finding for finding in related
            if resource_response_matches(group, finding)
        ]
        if matching:
            group["classification"] = "mapped-resource-response"
            group["mappedNativeFindingIds"] = [finding["id"] for finding in matching]
            for finding in matching:
                finding["mappedSwaggerGroups"].append(group["id"])
        elif len(source_ops) == len(selected) == 1 and status is not None:
            source = source_ops[0]
            source_bodies = bodies_at(source, status)
            selected_bodies = bodies_at(selected[0], status)
            if (
                source_bodies
                and {body_key(body) for body in source_bodies}
                == {body_key(body) for body in selected_bodies}
                and selected_body_status(source) == selected_body_status(selected[0]) == status
            ):
                if all(
                    body.get("nativeResource") is True
                    for body in source_bodies + selected_bodies
                ):
                    group["classification"] = "native-resource-without-emitted-marker"
                elif any(body.get("nativeResource") is False for body in source_bodies):
                    group["classification"] = (
                        "nonresource-response-not-exposed-by-resolver"
                        if source.get("resolverExposed") is False
                        else "native-resource-response-suppressed-or-unresolved"
                    )
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
        matching = [
            finding for finding in related
            if response_comparison_matches(group, finding, source_ops)
        ]
        if matching:
            group["classification"] = "mapped-response-mismatch"
            group["mappedNativeFindingIds"] = [finding["id"] for finding in matching]
            for finding in matching:
                finding["mappedSwaggerGroups"].append(group["id"])
    group["nativeResponseCheckContext"] = [
        {
            "operation": op["operation"],
            "associations": op["associations"],
            "responseCandidates": op["responseCandidates"],
        }
        for op in source_ops
    ]
    group["mappedNativePredicateIds"] = []
    if not ambiguous and source_ops and group["classification"] != "upstream-identity-false-positive":
        for predicate in native_predicates.values():
            if (
                predicate["project"] != group["project"]
                or not any(op["operationKey"] == predicate["operation"]["operationKey"] for op in source_ops)
            ):
                continue
            matches = (
                request_comparison_matches(group, predicate, source_ops)
                if group["rule"] == "PutRequestResponseSchemeArm"
                else resource_response_matches(group, predicate)
                if group["rule"] == "XmsResourceInPutResponse"
                else response_comparison_matches(group, predicate, source_ops)
            )
            if matches:
                group["mappedNativePredicateIds"].append(predicate["id"])
                predicate["mappedSwaggerGroups"].append(group["id"])
        if group["mappedNativePredicateIds"] and not group["mappedNativeFindingIds"]:
            group["classification"] = "mapped-selected-diagnostic-before-suppression"

for finding in native_findings.values():
    if finding["mappedSwaggerGroups"]:
        finding["classification"] = {
            "resourceIdentity": "mapped-resource-response",
            "responseMismatch": "mapped-response-mismatch",
        }.get(finding["family"], "mapped-request-mismatch")
    elif not finding["selectedVersionOperations"]:
        finding["classification"] = "source-only-operation-not-in-selected-version"
    elif finding["family"] == "missingRequest":
        finding["classification"] = "additional-missing-request-policy"
    elif finding["sameOperationSwaggerGroups"]:
        finding["classification"] = "same-operation-different-comparison"
    elif finding["family"] == "resourceIdentity":
        finding["classification"] = "additional-native-resource-response-policy"
    elif finding["family"] == "responseMismatch":
        finding["classification"] = "additional-canonical-response-policy"
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
    "nativePredicateFindings": len(native_predicates),
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
        "mappedNativePredicates": len({i for g in member for i in g["mappedNativePredicateIds"]}),
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
    "nativePredicates": list(native_predicates.values()),
}
if args.output:
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
else:
    expected = json.loads((root / "instance-mapping.json").read_text(encoding="utf-8"))
    assert result == expected, "Instance assessment differs from saved evidence"
print(json.dumps({key: value for key, value in summary.items() if key != "projects"}, indent=2))

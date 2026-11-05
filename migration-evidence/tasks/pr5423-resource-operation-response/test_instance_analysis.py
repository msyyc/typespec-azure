import contextlib
import io
import json
import pathlib
import runpy
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = pathlib.Path(__file__).resolve().parent
GAPS = runpy.run_path(str(ROOT / "assess-gaps.py"))
RENDER = runpy.run_path(str(ROOT / "render-instances.py"))


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


def execute(script, *arguments):
    with patch.object(sys, "argv", [str(script), *map(str, arguments)]), contextlib.redirect_stdout(io.StringIO()):
        runpy.run_path(str(script), run_name="__main__")


def operation(key, route, canonical="Resource", response="Resource"):
    model = lambda name: {"name": name, "kind": "Model", "registeredResource": name == canonical}
    return {
        "operationKey": key, "operation": key, "verb": "put", "path": route,
        "request": {"bodyKind": "single", "effectiveType": model("Input")},
        "responses": [{"statusCodes": 200, "bodies": [model(response)]}],
        "responseCandidates": [],
        "associations": [{
            "resource": canonical, "group": "lifecycle", "kind": "createOrUpdate",
            "checkedPutRequest": True,
        }],
    }


def swagger_row(identity, route, rule="PutRequestResponseSchemeArm", document="api.json"):
    return {
        "id": identity,
        "observation": {"rule": rule, "project": "p"},
        "candidates": [{
            "document": document, "route": route,
            "operations": [{
                "verb": "put", "responses": {"200": {"raw": {"$ref": "#/definitions/Resource"}}},
            }],
        }],
    }


class InstanceMappingTests(unittest.TestCase):
    def assess(self, rows, operations, findings):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            trace = {
                "project": "p", "sourceOperations": operations,
                "selectedOperations": operations, "findings": findings,
            }
            write_json(root / "swagger-bindings.json", rows)
            write_json(root / "instance-inputs.json", [trace])
            write_json(root / "native-swagger-bindings.json", [
                {"id": f"p:{index}", "candidates": []} for index, _ in enumerate(findings)
            ])
            execute(ROOT / "analyze-instances.py", "--root", root, "--output", root / "result.json")
            return json.loads((root / "result.json").read_text(encoding="utf-8"))

    def test_exact_operation_with_different_expected_model_is_not_credited(self):
        operations = [
            operation("matching", "/resources/{name}"),
            operation("coincident", "/children/{name}", canonical="Parent", response="Child"),
        ]
        findings = [{
            "operationKey": op["operationKey"],
            "message": "PUT request body must use resource model Resource. Found Input.",
        } for op in operations]
        result = self.assess(
            [swagger_row("a", operations[0]["path"]), swagger_row("b", operations[1]["path"])],
            operations, findings,
        )
        self.assertEqual(result["summary"]["members"][0]["mappedNativeFindings"], 1)
        self.assertEqual(
            [g["classification"] for g in result["swaggerGroups"]],
            ["mapped-request-mismatch", "same-operation-different-comparison"],
        )

    def test_repeated_inputs_group_but_different_member_checks_survive(self):
        route = "/resources/{name}"
        result = self.assess(
            [swagger_row("a", route), swagger_row("b", route),
             swagger_row("c", route, rule="XmsResourceInPutResponse")],
            [operation("op", route)],
            [{"operationKey": "op", "message": "PUT request body must use resource model Resource. Found Input."}],
        )
        self.assertEqual(result["summary"]["rawSwagger"], 3)
        self.assertEqual(result["summary"]["checkedSwaggerInstanceGroups"], 2)
        self.assertEqual(result["summary"]["members"][1]["sameOperationNativeFindings"], 1)
        self.assertEqual(result["summary"]["members"][1]["mappedNativeFindings"], 0)
        self.assertEqual(result["swaggerGroups"][0]["rawObservationIds"], ["a", "b"])

    def test_registration_aliases_do_not_duplicate_one_canonical_comparison(self):
        route = "/resources/{name}"
        op = operation("op", route)
        op["associations"].append(dict(op["associations"][0], group="lists", kind="create"))
        result = self.assess(
            [swagger_row("a", route)], [op],
            [{"operationKey": "op", "message": "PUT request body must use resource model Resource. Found Input."}],
        )
        self.assertEqual(result["summary"]["members"][0]["mappedNativeFindings"], 1)

    def test_ambiguous_parameter_normalization_never_credits_a_match(self):
        result = self.assess(
            [swagger_row("a", "/resources/{emitted}")],
            [operation("one", "/resources/{first}"), operation("two", "/resources/{second}")],
            [],
        )
        self.assertEqual(result["swaggerGroups"][0]["classification"], "ambiguous-source-operation")
        self.assertEqual(result["swaggerGroups"][0]["mappedNativeFindingIds"], [])

    def test_distinct_schema_contexts_at_the_same_route_are_not_deduplicated(self):
        route = "/resources/{name}"
        rows = [swagger_row("a", route), swagger_row("b", route)]
        rows[1]["candidates"][0]["operations"][0]["responses"]["200"]["raw"]["$ref"] = "#/definitions/Other"
        result = self.assess(rows, [operation("op", route)], [])
        self.assertEqual(result["summary"]["checkedSwaggerInstanceGroups"], 2)

    def test_same_response_name_without_registered_identity_is_not_credited(self):
        route = "/resources/{name}"
        op = operation("op", route)
        op["responses"][0]["bodies"][0]["registeredResource"] = False
        result = self.assess(
            [swagger_row("a", route)], [op],
            [{"operationKey": "op", "message": "PUT request body must use resource model Resource. Found Input."}],
        )
        self.assertEqual(result["swaggerGroups"][0]["classification"], "same-operation-different-comparison")
        self.assertEqual(result["summary"]["members"][0]["mappedNativeFindings"], 0)

    def test_marker_warning_maps_only_to_its_selected_missing_marker_check(self):
        route = "/resources/{name}"
        row = swagger_row("a", route, rule="XmsResourceInPutResponse")
        row["candidates"][0]["operations"][0]["responses"]["200"]["xmsResourceInHierarchy"] = False
        result = self.assess(
            [row], [operation("op", route)],
            [{"operationKey": "op", "message": "ARM PUT operations must return an Azure resource model in their 200 or 201 response."}],
        )
        self.assertEqual(result["swaggerGroups"][0]["classification"], "mapped-resource-marker")
        self.assertEqual(result["summary"]["members"][0]["mappedNativeFindings"], 1)

    def test_marker_warning_on_a_different_status_is_not_credited(self):
        route = "/resources/{name}"
        row = swagger_row("a", route, rule="XmsResourceInPutResponse")
        row["candidates"][0]["operations"][0]["responses"]["200"]["xmsResourceInHierarchy"] = False
        op = operation("op", route)
        op["responses"] = [
            {"statusCodes": 200, "bodies": [None]},
            {"statusCodes": 201, "bodies": [{"name": "Other", "kind": "Model", "registeredResource": False}]},
        ]
        result = self.assess(
            [row], [op],
            [{"operationKey": "op", "message": "ARM PUT operations must return an Azure resource model in their 200 or 201 response."}],
        )
        self.assertEqual(result["summary"]["members"][0]["mappedNativeFindings"], 0)

    def test_cross_method_warning_requires_the_other_compared_canonical_payload(self):
        route = "/resources/{name}"
        row = swagger_row("a", route, rule="PutGetPatchResponseSchema")
        row["candidates"][0]["operations"][0]["responses"]["200"]["raw"]["$ref"] = "#/definitions/Child"
        row["candidates"][0]["operations"].append({
            "verb": "get", "responses": {"200": {"raw": {"$ref": "#/definitions/Resource"}}},
        })
        put = operation("put", route, response="Child")
        get = operation("get", route)
        get["verb"] = "get"
        finding = {"operationKey": "put", "message": "[RPC 008]: PUT, GET, PATCH & LIST must return the same resource schema."}
        result = self.assess([row], [put, get], [finding])
        self.assertEqual(result["summary"]["members"][0]["mappedNativeFindings"], 1)
        for op in (put, get):
            op["associations"][0]["resource"] = "Parent"
        result = self.assess([row], [put, get], [finding])
        self.assertEqual(result["summary"]["members"][0]["mappedNativeFindings"], 0)

    def test_collection_role_warning_is_not_credited_as_a_different_resource_item(self):
        route = "/resources/{name}"
        row = swagger_row("a", route, rule="PutGetPatchResponseSchema")
        row["candidates"][0]["operations"].append({
            "verb": "get", "responses": {"200": {"raw": {
                "type": "array", "items": {"$ref": "#/definitions/Resource"},
            }}},
        })
        put = operation("put", route)
        get = operation("get", route, response="Array")
        get["verb"] = "get"
        get["responses"][0]["bodies"][0]["collectionItem"] = {
            "name": "Resource", "kind": "Model", "registeredResource": True,
        }
        result = self.assess([row], [put, get], [{
            "operationKey": "get",
            "message": "[RPC 008]: PUT, GET, PATCH & LIST must return the same resource schema.",
        }])
        self.assertEqual(result["summary"]["members"][0]["mappedNativeFindings"], 0)


class SwaggerResolutionTests(unittest.TestCase):
    def resolve(self, ambiguous=False):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            dataset = root / "dataset"
            file = "projects/p/swagger/api.json"
            ref = "../../../common.json#/definitions/Child"
            operation = {
                "operationId": "Create", "parameters": [],
                "responses": {"200": {"schema": {"$ref": ref}}},
            }
            document = {"paths": {"/resources/{name}": {"put": operation}}}
            write_json(dataset / file, document)
            if ambiguous:
                write_json(dataset / "projects/p/swagger/other.json", document)
            write_json(dataset / "common.json", {
                "definitions": {
                    "Child": {"allOf": [{"$ref": "#/definitions/Base"}]},
                    "Base": {"x-ms-azure-resource": True, "allOf": [{"$ref": "#/definitions/Child"}]},
                },
            })
            write_json(root / "observations.json", {"members": [{
                "rule": "XmsResourceInPutResponse",
                "observations": [{
                    "rule": "XmsResourceInPutResponse", "project": "p",
                    "swaggerFile": file, "validatorInputFile": file,
                    "path": ["paths", "/resources/{name}", "put"],
                }],
            }]})
            execute(
                ROOT / "analysis" / "resolve-swagger-instances.py",
                "--observations", root / "observations.json",
                "--dataset", dataset, "--output", root / "result.json",
            )
            return json.loads((root / "result.json").read_text(encoding="utf-8"))[0]

    def test_external_references_allof_and_cycles_preserve_schema_identity(self):
        result = self.resolve()
        schema = result["candidates"][0]["operations"][0]["responses"]["200"]
        self.assertEqual(schema["reference"], {"document": "common.json", "pointer": ["definitions", "Child"]})
        self.assertTrue(schema["xmsResourceInHierarchy"])

    def test_multiple_exact_documents_remain_ambiguous(self):
        self.assertEqual(self.resolve(ambiguous=True)["candidateCount"], 2)


class GapDecisionTests(unittest.TestCase):
    def test_difference_table_excludes_matching_checks_and_retains_distinct_comparisons(self):
        assessment = {"checks": [
            {"decision": "corroborated", "member": "a", "rawObservations": 1},
            {"decision": "bodyless-comparator-overreach", "member": "a", "rawObservations": 1},
            {"decision": "collection-comparator-overreach", "member": "a", "rawObservations": 2},
            {"decision": "body-policy-owner", "member": "b", "rawObservations": 1},
        ]}
        rows = RENDER["difference_rows"](assessment, "a")
        self.assertEqual(len(rows), 2)
        self.assertEqual(sum(row["checks"] for row in rows), 2)
        self.assertEqual(sum(row["raw"] for row in rows), 3)
        self.assertEqual(sum(row["checks"] for row in RENDER["difference_rows"](assessment)), 3)

    def test_each_member_difference_table_reconciles_to_its_unpaired_observations(self):
        mapping = json.loads((ROOT / "instance-mapping.json").read_text(encoding="utf-8"))
        assessment = json.loads((ROOT / "gap-assessment.json").read_text(encoding="utf-8"))
        for member in mapping["summary"]["members"]:
            with self.subTest(member=member["rule"]):
                groups = [
                    group for group in mapping["swaggerGroups"]
                    if group["rule"] == member["rule"] and not group["mappedNativeFindingIds"]
                ]
                rows = RENDER["difference_rows"](assessment, member["rule"])
                self.assertEqual(sum(row["checks"] for row in rows), len(groups))
                self.assertEqual(sum(row["raw"] for row in rows), sum(len(group["rawObservationIds"]) for group in groups))

    def group(self, identity="example", responses=None, rule="PutGetPatchResponseSchema", classification="missed-cross-operation-selected-ref-absent"):
        return {
            "id": identity, "rule": rule, "classification": classification,
            "project": "p", "route": "/resources/name", "rawObservationIds": [identity],
            "swaggerOperations": [{"verb": "put", "responses": responses or {"202": None}}],
        }

    def test_existing_empty_200_is_a_body_issue_even_when_201_has_a_model(self):
        group = self.group(responses={"200": None, "201": {"raw": {"$ref": "#/definitions/Resource"}}})
        self.assertEqual(GAPS["decision_for"](group, {}), "body-policy-owner")
        group["rule"] = "PutRequestResponseSchemeArm"
        self.assertEqual(GAPS["decision_for"](group, {}), "body-policy-owner")

    def test_borrowed_parent_read_registration_does_not_cover_syncjob_request(self):
        group = self.group(
            identity="86cde2d203ba3710", rule="PutRequestResponseSchemeArm",
            classification="same-operation-different-comparison",
        )
        self.assertEqual(GAPS["decision_for"](group, {}), "parent-canonical-association")

    def test_no_content_does_not_make_an_unknown_inline_schema_case_a_false_positive(self):
        self.assertEqual(GAPS["decision_for"](self.group(responses={"204": None}), {}), "bodyless-comparator-overreach")
        self.assertEqual(GAPS["decision_for"](self.group(), {}), "bodyless-comparator-overreach")
        omitted_204 = self.group()
        omitted_204["swaggerOperations"][0]["responses"] = {}
        omitted_204["typeSpecSelectedBindings"] = [{
            "operations": [{"verb": "put", "responses": [{"statusCodes": 204, "bodies": [None]}]}],
        }]
        self.assertEqual(GAPS["decision_for"](omitted_204, {}), "bodyless-comparator-overreach")
        with self.assertRaisesRegex(AssertionError, "Unassessed cross-method"):
            GAPS["decision_for"](self.group(responses={"200": {"raw": {"type": "object"}}}), {})

    def test_set_recovery_does_not_count_an_action_or_wrong_canonical_comparison(self):
        group = self.group(
            rule="PutRequestResponseSchemeArm",
            classification="missed-request-outside-lifecycle-map",
            responses={"200": {"raw": {"$ref": "#/definitions/Resource"}}},
        )
        self.assertEqual(GAPS["decision_for"](group, {"example": {"selectedCanonicalComparison": True}}), "recover-registered-put")
        self.assertEqual(GAPS["decision_for"](group, {"example": {"selectedCanonicalComparison": False}}), "custom-lifecycle-registration")
        group["id"] = "4f6894b5bb1a95e3"
        self.assertEqual(GAPS["decision_for"](group, {group["id"]: {"selectedCanonicalComparison": False}}), "custom-command-request")

    def test_multiple_member_checks_of_one_body_issue_remain_nonadditive(self):
        first = self.group(identity="a", responses={"200": None})
        second = self.group(identity="b", responses={"200": None}, rule="PutRequestResponseSchemeArm")
        result = GAPS["assess"]({"swaggerGroups": [first, second]}, {"registry": {"checks": []}})
        body = next(row for row in result["decisions"] if row["decision"] == "body-policy-owner")
        self.assertEqual(body["memberChecks"], 2)
        self.assertEqual(body["distinctProjectRoutes"], 1)

    def test_owner_credit_preserves_callbacks_and_does_not_double_count_contexts(self):
        first = self.group(identity="a", responses={"200": None})
        second = self.group(identity="b", responses={"200": None}, rule="PutRequestResponseSchemeArm")
        for group in (first, second):
            group["typeSpecSourceBindings"] = [{"operations": [{"operationKey": "put"}]}]
        first["classification"] = "mapped-response-mismatch"
        first["mappedNativeFindingIds"] = ["warning"]
        reports = [
            {"rule": "no-response-body", "operationKey": "put", "messageId": "default", "reportIndex": index}
            for index in (0, 1)
        ]
        probes = {"registry": {"checks": []}, "owners": {"checks": [
            {"checkId": group["id"], "project": "p", "ownerRule": "no-response-body",
             "predicateFindingsIgnoringSuppressions": reports}
            for group in (first, second)
        ]}}
        result = GAPS["assess"]({"swaggerGroups": [first, second]}, probes)
        accounting = result["coverageAccounting"]
        self.assertEqual(accounting["mappedWarningContexts"], 1)
        self.assertEqual(accounting["existingOwnerContexts"], 2)
        self.assertEqual(accounting["ownerOnlyContexts"], 1)
        self.assertEqual(accounting["overlappingMappedAndOwnerContexts"], 1)
        self.assertEqual(accounting["coveredDiagnosticContexts"], 2)
        self.assertEqual(accounting["distinctOwnerDiagnosticCallbacks"], 2)

    def test_frozen_overlay_accounts_for_every_check_without_changing_correspondence(self):
        mapping = json.loads((ROOT / "instance-mapping.json").read_text(encoding="utf-8"))
        original = json.dumps(mapping, sort_keys=True)
        probes = json.loads((ROOT / "gap-probes.json").read_text(encoding="utf-8"))
        result = GAPS["assess"](mapping, probes)
        self.assertEqual(json.dumps(mapping, sort_keys=True), original)
        self.assertEqual(
            {row["checkId"] for row in result["checks"]},
            {row["id"] for row in mapping["swaggerGroups"]},
        )
        self.assertEqual(sum(row["memberChecks"] for row in result["decisions"]), len(mapping["swaggerGroups"]))
        self.assertEqual(
            sum(row["rawObservations"] for row in result["decisions"]),
            sum(len(row["rawObservationIds"]) for row in mapping["swaggerGroups"]),
        )
        self.assertTrue(all(row["authoredSuppressions"] for row in probes["owners"]["checks"]))


if __name__ == "__main__":
    unittest.main()

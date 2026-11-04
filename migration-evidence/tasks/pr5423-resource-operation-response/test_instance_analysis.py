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


if __name__ == "__main__":
    unittest.main()

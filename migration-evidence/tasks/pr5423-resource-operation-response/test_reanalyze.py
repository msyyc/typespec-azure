import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

from reanalyze import summarize


class ProjectGroupingTests(unittest.TestCase):
    def test_cli_generates_new_summary_and_still_rejects_stale_recount(self):
        observations = {
            "projects": [{"sourcePath": "p"}],
            "native": [{"project": "p", "status": "success", "diagnostics": [], "rawDiagnostics": []}],
            "members": [],
        }
        instances = {
            "summary": {"routeGrouping": {"swagger": 0, "native": 0}, "members": []},
            "nativeFindings": [],
        }
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            for name, value in (("observations.json", observations), ("instance-mapping.json", instances)):
                (root / name).write_text(json.dumps(value), encoding="utf-8")
            command = [sys.executable, "-B", str(pathlib.Path(__file__).with_name("reanalyze.py")), "--root", str(root)]
            generated = subprocess.run(
                [*command, "--output", str(root / "summary.json")], capture_output=True, text=True,
            )
            self.assertEqual(generated.returncode, 0, generated.stderr)
            self.assertEqual(json.loads((root / "summary.json").read_text(encoding="utf-8"))["nativeRaw"], 0)
            (root / "summary.json").write_text("{}", encoding="utf-8")
            verified = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(verified.returncode, 0)
            self.assertIn("Saved-observation recount differs", verified.stderr)

    def test_assessed_summary_uses_current_correspondence_counts(self):
        diagnostic = {"rule": "native", "sourceFile": "main.tsp", "line": 1, "column": 1}
        observations = {
            "projects": [{"sourcePath": "p"}],
            "native": [{
                "project": "p", "status": "success",
                "diagnostics": [diagnostic] * 3, "rawDiagnostics": [diagnostic] * 3,
            }],
            "members": [{"rule": "first", "observations": []}],
        }
        instances = {
            "summary": {
                "routeGrouping": {"swagger": 4, "native": 2},
                "members": [{"rule": "first", "mappedNativeFindings": 2}],
            },
            "nativeFindings": [
                {"mappedSwaggerGroups": ["a"]}, {"mappedSwaggerGroups": ["b"]},
                {"mappedSwaggerGroups": []},
            ],
        }
        result = summarize(observations, instances)
        self.assertIn("4 Swagger, 2 TypeSpec", result["comparableActionableUnit"])
        self.assertIn("2 matching findings for first", result["memberNativeAttribution"])
        self.assertIn("1 shared-rule findings not credited", result["memberNativeAttribution"])

    def test_repeated_findings_and_overlapping_members_count_projects_once(self):
        projects = ["both", "swagger-only", "native-only", "neither"]
        diagnostic = {"rule": "native", "sourceFile": "main.tsp", "line": 1, "column": 1}
        observation = {"rule": "first", "project": "both", "swaggerFile": "api.json", "path": []}
        observations = {
            "projects": [{"sourcePath": project} for project in projects],
            "native": [
                {
                    "project": project,
                    "status": "success",
                    "diagnostics": [diagnostic, diagnostic] if project in ("both", "native-only") else [],
                    "rawDiagnostics": [diagnostic, diagnostic] if project in ("both", "native-only") else [],
                }
                for project in projects
            ],
            "members": [
                {"rule": "first", "observations": [observation, observation]},
                {
                    "rule": "second",
                    "observations": [
                        {**observation, "rule": "second"},
                        {**observation, "rule": "second", "project": "swagger-only"},
                    ],
                },
            ],
        }

        result = summarize(observations)
        grouped = result["projectGrouping"]
        self.assertEqual(result["swaggerRaw"], 4)
        self.assertEqual(result["nativeAligned"], 4)
        self.assertEqual(
            {key: grouped[key] for key in ("swagger", "native", "both", "swaggerOnly", "nativeOnly", "neither")},
            {"swagger": 2, "native": 2, "both": 1, "swaggerOnly": 1, "nativeOnly": 1, "neither": 1},
        )
        self.assertEqual(
            grouped["memberComparisons"],
            [
                {"rule": "first", "swagger": 1, "sharedNative": 2, "both": 1, "swaggerOnly": 0, "sharedNativeOnly": 1},
                {"rule": "second", "swagger": 2, "sharedNative": 2, "both": 1, "swaggerOnly": 1, "sharedNativeOnly": 1},
            ],
        )


if __name__ == "__main__":
    unittest.main()

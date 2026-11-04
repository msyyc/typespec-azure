import unittest

from reanalyze import summarize


class ProjectGroupingTests(unittest.TestCase):
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

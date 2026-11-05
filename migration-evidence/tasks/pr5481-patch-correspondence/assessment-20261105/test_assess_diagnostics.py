import unittest

from assess_diagnostics import annotation_category, schema_gap_category


def occurrence(*candidates):
    return {
        "classification": "same-name-different-schema",
        "sameNamedPutCandidates": len(candidates),
        "differingSchemaKeys": list(candidates),
    }


class AnnotationAssessmentTests(unittest.TestCase):
    def test_description_title_only_is_excluded(self):
        self.assertEqual(
            annotation_category([occurrence(["description", "title"])]),
            "all-occurrences-annotation-only",
        )

    def test_one_equivalent_put_candidate_is_sufficient(self):
        self.assertEqual(
            annotation_category([occurrence(["type"], ["description"])]),
            "all-occurrences-annotation-only",
        )

    def test_every_collapsed_helper_occurrence_must_have_a_candidate(self):
        self.assertEqual(
            annotation_category([
                occurrence(["description"]),
                occurrence(["x-ms-mutability"]),
            ]),
            "mixed-occurrences",
        )

    def test_repeated_annotation_only_occurrences_are_excluded(self):
        self.assertEqual(
            annotation_category([
                occurrence(["description"], ["type"]),
                occurrence(["title"]),
            ]),
            "all-occurrences-annotation-only",
        )

    def test_other_keys_are_not_assumed_harmless(self):
        for keys in (["type"], ["x-ms-mutability"], ["description", "enum"]):
            with self.subTest(keys=keys):
                self.assertEqual(
                    annotation_category([occurrence(keys)]),
                    "no-annotation-only-candidate",
                )

    def test_missing_or_inconsistent_comparison_evidence_fails_closed(self):
        bad_count = occurrence(["description"])
        bad_count["sameNamedPutCandidates"] = 2
        for occurrences in ([], [occurrence()], [occurrence([])], [bad_count]):
            with self.subTest(occurrences=occurrences):
                with self.assertRaises(ValueError):
                    annotation_category(occurrences)


def schema_occurrence(keys, *, patch_type="string", put_type="string",
                      patch_mutability=None, put_mutability=None, put_read_only=False):
    return {
        "patch": {"type": patch_type, "readOnly": False, "mutability": patch_mutability},
        "candidates": [{
            "put": {"type": put_type, "readOnly": put_read_only, "mutability": put_mutability},
            "differingKeys": keys,
        }],
    }


class SchemaGapAssessmentTests(unittest.TestCase):
    def test_documentation_and_defaults_are_not_missing_names_or_types(self):
        for keys, expected in (
            (["externalDocs"], "documentation-only-overcheck"),
            (["default", "description"], "default-only-overcheck"),
        ):
            with self.subTest(keys=keys):
                self.assertEqual(schema_gap_category([schema_occurrence(keys)]), expected)

    def test_method_appropriate_mutability_does_not_require_array_equality(self):
        self.assertEqual(schema_gap_category([schema_occurrence(
            ["x-ms-mutability"], patch_mutability=["update"],
            put_mutability=["read", "create", "update"],
        )]), "input-allowed-mutability-overcheck")

    def test_read_only_or_create_only_put_is_not_excluded_as_write_compatible(self):
        for kwargs in ({"put_read_only": True}, {"put_mutability": ["read", "create"]}):
            with self.subTest(kwargs=kwargs):
                self.assertEqual(schema_gap_category([schema_occurrence(
                    ["x-ms-mutability"], **kwargs,
                )]), "remaining-schema-difference")

    def test_all_collapsed_occurrences_need_a_qualifying_candidate(self):
        self.assertEqual(schema_gap_category([
            schema_occurrence(["description"]),
            schema_occurrence(["format"]),
        ]), "remaining-schema-difference")

    def test_an_unrelated_same_name_type_does_not_hide_a_compatible_candidate(self):
        occurrence = schema_occurrence(["type"], put_type="array", patch_type="object")
        occurrence["candidates"].extend(schema_occurrence(
            ["x-ms-mutability"], patch_type="object", put_type="object",
        )["candidates"])
        self.assertEqual(schema_gap_category([occurrence]),
                         "input-allowed-mutability-overcheck")

    def test_incompatible_json_kind_requires_every_candidate_to_conflict(self):
        self.assertEqual(schema_gap_category([
            schema_occurrence(["type"], patch_type="string", put_type="integer"),
        ]), "incompatible-json-kind")
        occurrence = schema_occurrence(["type"], patch_type="string", put_type="integer")
        occurrence["candidates"].extend(schema_occurrence(["format"])["candidates"])
        self.assertEqual(schema_gap_category([occurrence]), "remaining-schema-difference")

    def test_only_all_read_only_patch_occurrences_are_excluded_from_input_checks(self):
        readonly = schema_occurrence(["format"])
        readonly["patch"]["readOnly"] = True
        self.assertEqual(schema_gap_category([readonly]), "read-only-patch-overcheck")
        self.assertEqual(schema_gap_category([readonly, schema_occurrence(["format"])]),
                         "remaining-schema-difference")

    def test_missing_candidates_or_empty_differences_fail_closed(self):
        for occurrences in ([], [{"patch": {}, "candidates": []}],
                            [schema_occurrence([])]):
            with self.subTest(occurrences=occurrences):
                with self.assertRaises(ValueError):
                    schema_gap_category(occurrences)


if __name__ == "__main__":
    unittest.main()

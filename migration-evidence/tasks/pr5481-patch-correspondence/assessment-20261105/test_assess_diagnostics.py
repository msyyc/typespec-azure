import unittest

from assess_diagnostics import annotation_category


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


if __name__ == "__main__":
    unittest.main()

import unittest

from reconcile import bridge


def record(index, observation, indices, project="p", repeated_context=False):
    contexts = [{"warningIndices": indices}]
    if repeated_context:
        contexts.append({"warningIndices": list(indices)})
    return {
        "project": project, "diagnosticIndex": index,
        "observation": observation, "contexts": contexts,
    }


class BridgeTests(unittest.TestCase):
    def test_shared_warning_and_multiple_checks_are_distinct_effects(self):
        rows = [
            record(0, "source-reported", [0, 1], repeated_context=True),
            record(1, "mixed-source-predicates", [0, 1]),
            record(2, "body-suppressed", []),
            record(3, "source-accepts", []),
            record(4, "name-not-source-leaf", []),
        ]
        result, _, witnessed = bridge(rows, {("p", 0), ("p", 1), ("p", 2)})
        self.assertEqual(result["recordWarningAssociations"], 4)
        self.assertEqual(result["additionalAssociationsWithinRecords"], 2)
        self.assertEqual(result["repeatedAssociationsAcrossRecords"], 2)
        self.assertEqual(result["suppressedRecords"], 1)
        self.assertEqual(result["warningsOutsideJoin"], 1)
        self.assertEqual(result["netDifference"], 2)
        self.assertEqual(witnessed, {("p", 0), ("p", 1)})

    def test_distinct_diagnostic_occurrences_and_projects_are_not_collapsed(self):
        rows = [
            record(0, "source-reported", [0, 1]),
            record(0, "body-reported", [0], project="q"),
        ]
        result, _, _ = bridge(rows, {("p", 0), ("p", 1), ("q", 0)})
        self.assertEqual(result["distinctWitnessedWarnings"], 3)
        self.assertEqual(result["repeatedAssociationsAcrossRecords"], 0)
        self.assertEqual(result["netDifference"], -1)

    def test_empty_population(self):
        result, _, witnessed = bridge([], set())
        self.assertEqual(result["netDifference"], 0)
        self.assertEqual(witnessed, set())

    def test_duplicate_retained_identity_is_rejected(self):
        with self.assertRaises(ValueError):
            bridge([record(0, "source-accepts", []), record(0, "source-accepts", [])], set())

    def test_out_of_range_warning_is_rejected(self):
        with self.assertRaises(ValueError):
            bridge([record(0, "source-reported", [2])], {("p", 0)})

    def test_invalid_warning_index_is_rejected(self):
        for index in [-1, True, "0"]:
            with self.subTest(index=index), self.assertRaises(ValueError):
                bridge([record(0, "source-reported", [index])], set())

    def test_reporting_and_nonreporting_categories_are_checked(self):
        for category, indices in [
            ("source-reported", []), ("body-suppressed", [0]),
            ("source-accepts", [0]), ("unassessed", []),
        ]:
            with self.subTest(category=category), self.assertRaises(ValueError):
                bridge([record(0, category, indices)], {("p", 0)})


if __name__ == "__main__":
    unittest.main()

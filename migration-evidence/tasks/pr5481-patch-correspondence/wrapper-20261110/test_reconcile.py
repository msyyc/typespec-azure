import unittest

from reconcile import remap_decisions


def receipt(*diagnostics):
    return {"p": {"rawDiagnostics": list(diagnostics)}}


def group(indices, category="historical-versioning"):
    return {
        "project": "p",
        "warningIndices": indices,
        "category": category,
        "reason": "source evidence",
        "sourceRefs": [["main.tsp", 1, 2]],
    }


class DecisionRemappingTests(unittest.TestCase):
    def test_removed_warning_does_not_shift_the_remaining_classification(self):
        before = receipt({"message": "wrapper"}, {"message": "historical"})
        after = receipt({"message": "historical"})
        rows, removed = remap_decisions(
            [
                group([0], "typespec-empty-wrapper-overcheck"),
                group([1]),
            ],
            before,
            after,
            {("p", 0)},
        )
        self.assertEqual(rows[0]["previousWarningIndex"], 1)
        self.assertEqual(rows[0]["category"], "historical-versioning")
        self.assertEqual(removed[0]["previousWarningIndex"], 0)

    def test_identical_diagnostic_occurrences_are_not_deduplicated(self):
        value = {"message": "same"}
        rows, removed = remap_decisions(
            [group([0, 1])], receipt(value, value), receipt(value, value),
            {("p", 0), ("p", 1)},
        )
        self.assertEqual(len(rows), 2)
        self.assertEqual([row["previousWarningIndex"] for row in rows], [0, 1])
        self.assertEqual(removed, [])

    def test_new_warning_or_ambiguous_classification_is_rejected(self):
        with self.assertRaises(ValueError):
            remap_decisions(
                [group([0])], receipt({"message": "old"}),
                receipt({"message": "new"}), {("p", 0)},
            )
        value = {"message": "same"}
        with self.assertRaises(ValueError):
            remap_decisions(
                [group([0]), group([1], "writable-patch-not-put")],
                receipt(value, value), receipt(value), {("p", 0)},
            )


if __name__ == "__main__":
    unittest.main()

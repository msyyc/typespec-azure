"""Reconcile name-only observations, retaining omitted checks as policy gaps."""

import argparse
import collections
import hashlib
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
FRESH = ROOT / "refresh-20261117-names"
PREVIOUS = ROOT / "refresh-20261112-direct"
spec = importlib.util.spec_from_file_location("incidence_bridge", ROOT / "count-gap-20261106/reconcile.py")
accounting = importlib.util.module_from_spec(spec)
spec.loader.exec_module(accounting)


def load(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def identity(diagnostic):
    return json.dumps(diagnostic, sort_keys=True)


def receipts(directory):
    result = {}
    for path in sorted((directory / "runs/full-corpus").glob("native-*.json")):
        value = load(path)
        assert value["status"] == "success" and value["project"] not in result
        result[value["project"]] = value
    assert len(result) == 487
    return result


def reconcile():
    current, old = receipts(FRESH), receipts(PREVIOUS)
    assert current.keys() == old.keys()
    before = collections.Counter(
        (project, identity(warning))
        for project, receipt in old.items()
        for warning in receipt["rawDiagnostics"]
    )
    after = collections.Counter(
        (project, identity(warning))
        for project, receipt in current.items()
        for warning in receipt["rawDiagnostics"]
    )
    removed = [
        {"project": project, "diagnostic": json.loads(warning)}
        for (project, warning), count in sorted((before - after).items())
        for _ in range(count)
    ]
    added = [
        {"project": project, "diagnostic": json.loads(warning)}
        for (project, warning), count in sorted((after - before).items())
        for _ in range(count)
    ]
    assert len(removed) == 19 and not added, (removed, added)
    assert all(
        "must preserve the format and bounds of its corresponding PUT property." in row["diagnostic"]["message"]
        for row in removed
    )
    assert len({row["project"] for row in removed}) == 6
    assert sum(before.values()) == 104 and sum(after.values()) == 85
    inventory = load(FRESH / "source-attribution/inventory.json")["projects"]
    assert len(inventory) == 51
    for item in inventory:
        captured = load(FRESH / "source-attribution" / item["source"])
        native = load(FRESH / "source-attribution" / item["native"])
        assert captured["rawDiagnostics"] == native["rawDiagnostics"] == current[item["project"]]["rawDiagnostics"]
        assert captured["extractorSha256"] == hashlib.sha256((HERE / "capture-source.mjs").read_bytes()).hexdigest()
        assert captured["captureBaseSha256"] == hashlib.sha256((ROOT / "wrapper-20261110/capture-source.mjs").read_bytes()).hexdigest()
        assert captured["comparisonPolicy"] == "name-and-body-only; value compatibility not evaluated"
        assert "compatibilityModuleSha256" not in captured
    records = load(FRESH / "source-attribution/observations.json")["records"]
    previous_records = {
        (row["project"], row["diagnosticIndex"]): row
        for row in load(PREVIOUS / "source-attribution/observations.json")["records"]
    }
    warnings = {
        (project, index): diagnostic
        for project, receipt in current.items()
        for index, diagnostic in enumerate(receipt["rawDiagnostics"])
    }
    counts, _, witnessed = accounting.bridge(records, set(warnings))
    changed_records = []
    affected_records = set()
    retired_warnings = set(before - after)
    for record in records:
        previous = previous_records[record["project"], record["diagnosticIndex"]]
        previous_warnings = {
            (record["project"], identity(old[record["project"]]["rawDiagnostics"][index]))
            for context in previous["contexts"]
            for index in context["warningIndices"]
        }
        if previous_warnings & retired_warnings:
            affected_records.add((record["project"], record["diagnosticIndex"]))
        if record["observation"] != previous["observation"]:
            assert previous["observation"] in {"source-reported", "mixed-source-predicates"}
            assert record["observation"] == "source-accepts"
            assert previous_warnings and previous_warnings <= retired_warnings
            changed_records.append({
                "project": record["project"], "diagnosticIndex": record["diagnosticIndex"],
                "name": record["name"], "route": record["route"],
                "decision": "Approved omission of value/constraint comparison, NOT proven compatible or a confirmed Swagger false positive.",
            })
    assert len(changed_records) == 26
    assert affected_records == {(row["project"], row["diagnosticIndex"]) for row in changed_records}
    assert counts == {
        "retainedSwaggerRecords": 182, "configuredTypeSpecWarnings": 85,
        "acceptedOrNonInputRecords": 124, "suppressedRecords": 1,
        "reportingRecords": 57, "recordWarningAssociations": 57,
        "additionalAssociationsWithinRecords": 0, "repeatedAssociationsAcrossRecords": 3,
        "distinctWitnessedWarnings": 54, "warningsOutsideJoin": 31, "netDifference": 97,
    }, counts
    previous_assessment = load(ROOT / "direct-20261112/reconciliation.json")
    omitted = previous_assessment["omittedDeepCheckRecords"] + changed_records
    assert len({(row["project"], row["diagnosticIndex"]) for row in omitted}) == 32
    assert all(
        next(row for row in records if (row["project"], row["diagnosticIndex"]) ==
             (item["project"], item["diagnosticIndex"]))["observation"] == "source-accepts"
        for item in omitted
    )
    old_outside = {
        (row["project"], identity(row["diagnostic"])): row
        for row in previous_assessment["outsideJoinWarnings"]
    }
    outside = []
    for project, index in sorted(set(warnings) - witnessed):
        diagnostic = warnings[project, index]
        old_row = old_outside[project, identity(diagnostic)]
        outside.append({
            "project": project, "warningIndex": index, "diagnostic": diagnostic,
            "category": old_row["category"], "reason": old_row["reason"],
            "sourceRefs": old_row["sourceRefs"],
        })
    categories = dict(sorted(collections.Counter(row["category"] for row in outside).items()))
    assert categories == {"empty-patch": 1, "historical-versioning": 13, "writable-patch-not-put": 17}
    families = collections.Counter(
        "missing-name" if "does not correspond to a property" in diagnostic["message"]
        else "empty-body" if "must contain at least one property" in diagnostic["message"]
        else "missing-body" for diagnostic in warnings.values()
    )
    assert families == {"missing-name": 83, "empty-body": 1, "missing-body": 1}
    projects = []
    for project in sorted(current):
        summary, _, _ = accounting.bridge(
            [record for record in records if record["project"] == project],
            {key for key in warnings if key[0] == project},
        )
        larger = max(summary["retainedSwaggerRecords"], summary["configuredTypeSpecWarnings"])
        projects.append({
            "project": project, **summary,
            "absoluteCountDifference": abs(summary["netDifference"]),
            "relativeCountDifferenceToLargerCount": abs(summary["netDifference"]) / larger if larger else None,
        })
    directions = {
        "swaggerHigherProjects": sum(row["netDifference"] > 0 for row in projects),
        "typeSpecHigherProjects": sum(row["netDifference"] < 0 for row in projects),
        "equalCountProjects": sum(row["netDifference"] == 0 for row in projects),
        "swaggerExcess": sum(max(row["netDifference"], 0) for row in projects),
        "typeSpecExcess": sum(max(-row["netDifference"], 0) for row in projects),
        "absoluteProjectGap": sum(row["absoluteCountDifference"] for row in projects),
    }
    assert directions["swaggerExcess"] - directions["typeSpecExcess"] == counts["netDifference"]
    return {
        "candidateCommit": load(FRESH / "task.json")["candidateCommit"],
        "boundary": "Fresh final-candidate configured warnings and installed production name/body predicates. Complete diagnostic occurrence identities, no message normalization or location deduplication. Source-accepts is a predicate result, NOT proof of compatible values; the32outside-policy records remain separately classified.",
        "counts": counts,
        "semanticDisposition": {
            "checkCoveredRecords": 58, "compatibleOrNonInputRecords": 92,
            "approvedNotMigratedRecords": 32, "newlyNotMigratedRecords": 26,
            "partiallyAffectedRetainedRecords": 0,
        },
        "exactBehaviorDelta": {"before": 104, "after": 85, "removed": removed, "added": added},
        "newlyOmittedConstraintRecords": changed_records,
        "allOmittedValueRecords": omitted,
        "warningFamilies": dict(sorted(families.items())),
        "outsideJoinCategories": categories, "outsideJoinWarnings": outside,
        "all51DiagnosticArraysExactlyEqual": True,
        "retainedRoutes": {
            "swagger": len({(row["project"], row["route"]) for row in records}),
            "source": len({(row["project"], context["route"]) for row in records for context in row["contexts"]}),
        },
        "assessedCountDirections": directions,
        "relativeCountBoundary": "Absolute count difference / larger retained-Swagger or native warning count; null if both zero. Not a defect-coverage percentage.",
        "projects": projects,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = reconcile()
    output = HERE / "reconciliation.json"
    if args.check:
        assert load(output) == result
    else:
        output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"counts": result["counts"], "semanticDisposition": result["semanticDisposition"]}, indent=2))

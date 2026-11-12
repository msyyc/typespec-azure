"""Verify exact final observations and distinguish narrowed policy from compatibility."""

import argparse
import collections
import hashlib
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
FRESH = ROOT / "refresh-20261112-direct"
PREVIOUS = ROOT / "refresh-20261110-wrapper"
OLD_MESSAGE = "must have a type and constraints compatible with its corresponding PUT property."
NEW_MESSAGE = "must preserve the format and bounds of its corresponding PUT property."
spec = importlib.util.spec_from_file_location("incidence_bridge", ROOT / "count-gap-20261106/reconcile.py")
accounting = importlib.util.module_from_spec(spec)
spec.loader.exec_module(accounting)


def load(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def identity(diagnostic):
    # This explicit wording migration is the only normalization. All other fields
    # and duplicate occurrences remain part of the complete diagnostic identity.
    return json.dumps(
        {**diagnostic, "message": diagnostic["message"].replace(OLD_MESSAGE, NEW_MESSAGE)},
        sort_keys=True,
    )


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
    assert len(removed) == 4 and not added, (removed, added)
    assert all(NEW_MESSAGE in row["diagnostic"]["message"] for row in removed)
    assert sum(before.values()) == 108 and sum(after.values()) == 104
    constraints = [
        {"project": project, **warning}
        for project, receipt in current.items()
        for warning in receipt["rawDiagnostics"]
        if NEW_MESSAGE in warning["message"]
    ]
    assert len(constraints) == 19
    inventory = load(FRESH / "source-attribution/inventory.json")["projects"]
    assert len(inventory) == 51
    for item in inventory:
        captured = load(FRESH / "source-attribution" / item["source"])
        native = load(FRESH / "source-attribution" / item["native"])
        assert captured["rawDiagnostics"] == native["rawDiagnostics"] == current[item["project"]]["rawDiagnostics"]
        assert captured["extractorSha256"] == hashlib.sha256((HERE / "capture-source.mjs").read_bytes()).hexdigest()
        assert captured["captureBaseSha256"] == hashlib.sha256((ROOT / "wrapper-20261110/capture-source.mjs").read_bytes()).hexdigest()
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
    counts, edges, witnessed = accounting.bridge(records, set(warnings))
    omitted_records = []
    for record in records:
        previous = previous_records[record["project"], record["diagnosticIndex"]]
        if record["observation"] != previous["observation"]:
            assert previous["observation"] == "source-reported" and record["observation"] == "source-accepts"
            previous_warnings = {
                (record["project"], identity(old[record["project"]]["rawDiagnostics"][index]))
                for context in previous["contexts"]
                for index in context["warningIndices"]
            }
            assert previous_warnings and previous_warnings <= set(before - after)
            omitted_records.append({
                "project": record["project"], "diagnosticIndex": record["diagnosticIndex"],
                "name": record["name"], "route": record["route"],
                "decision": "Deliberately outside direct-constraint policy, not proven compatible or a Swagger false positive.",
            })
    assert len(omitted_records) == 6
    assert counts == {
        "retainedSwaggerRecords": 182, "configuredTypeSpecWarnings": 104,
        "acceptedOrNonInputRecords": 98, "suppressedRecords": 1,
        "reportingRecords": 83, "recordWarningAssociations": 85,
        "additionalAssociationsWithinRecords": 2, "repeatedAssociationsAcrossRecords": 12,
        "distinctWitnessedWarnings": 73, "warningsOutsideJoin": 31, "netDifference": 78,
    }, counts
    old_outside = load(ROOT / "wrapper-20261110/reconciliation.json")["outsideJoinWarnings"]
    classifications = {
        (row["project"], identity(row["diagnostic"])): row for row in old_outside
    }
    outside = []
    for project, index in sorted(set(warnings) - witnessed):
        diagnostic = warnings[project, index]
        old_row = classifications[project, identity(diagnostic)]
        outside.append({
            "project": project, "warningIndex": index, "diagnostic": diagnostic,
            "category": old_row["category"], "reason": old_row["reason"],
            "sourceRefs": old_row["sourceRefs"],
        })
    categories = dict(sorted(collections.Counter(row["category"] for row in outside).items()))
    assert categories == {"empty-patch": 1, "historical-versioning": 13, "writable-patch-not-put": 17}
    families = collections.Counter(
        "direct-constraint" if NEW_MESSAGE in diagnostic["message"]
        else "missing-name" if "does not correspond to a property" in diagnostic["message"]
        else "empty-body" if "must contain at least one property" in diagnostic["message"]
        else "missing-body" for diagnostic in warnings.values()
    )
    projects = []
    for project in sorted(current):
        summary, _, _ = accounting.bridge(
            [record for record in records if record["project"] == project],
            {key for key in warnings if key[0] == project},
        )
        projects.append({"project": project, **summary})
    return {
        "candidateCommit": load(FRESH / "task.json")["candidateCommit"],
        "boundary": "Fresh final-candidate configured warnings and installed production source predicates. Complete diagnostic occurrence identities, with only the explicitly recorded message migration normalized for the behavior delta. Not cross-engine historical defect equivalence.",
        "counts": counts,
        "acceptedOrNonInputBreakdown": {
            "previouslyAssessedCompatibleOrNonInput": 92,
            "deliberatelyOutsideDirectConstraintPolicy": 6,
        },
        "normalizedBehaviorDelta": {"before": 108, "after": 104, "removed": removed, "added": added},
        "retainedDirectConstraintWarnings": constraints,
        "warningFamilies": dict(sorted(families.items())),
        "outsideJoinCategories": categories,
        "outsideJoinWarnings": outside,
        "omittedDeepCheckRecords": omitted_records,
        "all51DiagnosticArraysExactlyEqual": True,
        "retainedRoutes": {
            "swagger": len({(row["project"], row["route"]) for row in records}),
            "source": len({(row["project"], ctx["route"]) for row in records for ctx in row["contexts"]}),
        },
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
    print(json.dumps(result["counts"], indent=2))

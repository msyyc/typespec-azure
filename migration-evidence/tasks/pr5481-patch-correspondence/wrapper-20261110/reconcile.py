"""Reconcile fresh observations using the existing tested incidence accounting."""

import argparse
import collections
import hashlib
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
FRESH = ROOT / "refresh-20261110-wrapper"
PREVIOUS = ROOT / "refresh-20261105-inherited"
ACCEPTED_OPAQUE_RECORDS = {
    (
        "specification/containerstorage/resource-manager/Microsoft.ContainerStorage/ContainerStorage",
        1,
    ),
    ("specification/discovery/Discovery.Management", 2),
}
spec = importlib.util.spec_from_file_location(
    "count_gap_bridge", ROOT / "count-gap-20261106/reconcile.py"
)
accounting = importlib.util.module_from_spec(spec)
spec.loader.exec_module(accounting)


def load(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def diagnostic_key(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def remap_decisions(groups, previous, current, outside_ids):
    buckets = collections.defaultdict(list)
    for group in groups:
        for index in group["warningIndices"]:
            diagnostic = previous[group["project"]]["rawDiagnostics"][index]
            identity = group["project"], diagnostic_key(diagnostic)
            buckets[identity].append((index, group))
    result = []
    for project, index in sorted(outside_ids):
        diagnostic = current[project]["rawDiagnostics"][index]
        identity = project, diagnostic_key(diagnostic)
        candidates = buckets[identity]
        if not candidates:
            raise ValueError(f"Unclassified fresh warning: {(project, index)}")
        if len({item[1]["category"] for item in candidates}) != 1:
            raise ValueError(f"Ambiguous duplicate warning classification: {identity}")
        old_index, group = candidates.pop(0)
        result.append(
            {
                "project": project,
                "warningIndex": index,
                "previousWarningIndex": old_index,
                "diagnostic": diagnostic,
                "category": group["category"],
                "reason": group["reason"],
                "sourceRefs": group["sourceRefs"],
            }
        )
    removed = [
        {
            "project": project,
            "previousWarningIndex": index,
            "diagnostic": previous[project]["rawDiagnostics"][index],
            "category": group["category"],
        }
        for (project, _), candidates in sorted(buckets.items())
        for index, group in candidates
    ]
    return result, removed


def canonical_context(value):
    if isinstance(value, list):
        return [canonical_context(item) for item in value]
    if isinstance(value, dict):
        result = {
            key: canonical_context(item)
            for key, item in value.items()
            if key not in {"warningIndices", "jsonPath"}
        }
        marker = "/node_modules/@azure-tools/typespec-azure-resource-manager/"
        if marker in result.get("sourceFile", ""):
            result["sourceFile"] = (
                "@azure-tools/typespec-azure-resource-manager/"
                + result["sourceFile"].split(marker, 1)[1]
            )
        return result
    return value


def reconcile():
    hashes = {}
    receipt_paths = {}

    def read(path):
        hashes[path.relative_to(ROOT).as_posix()] = hashlib.sha256(
            path.read_bytes()
        ).hexdigest()
        return load(path)

    def receipts(directory):
        result = {}
        for path in sorted((directory / "runs/full-corpus").glob("native-*.json")):
            receipt = read(path)
            assert receipt["status"] == "success"
            assert receipt["project"] not in result
            result[receipt["project"]] = receipt
            receipt_paths[directory.name, receipt["project"]] = path.relative_to(
                ROOT
            ).as_posix()
        assert len(result) == 487
        return result

    current = receipts(FRESH)
    previous = receipts(PREVIOUS)
    assert current.keys() == previous.keys()

    def arm_members(directory):
        artifacts = read(directory / "provenance/artifact-provenance.json")["artifacts"]
        arm = next(
            item for item in artifacts
            if item["file"].startswith("azure-tools-typespec-azure-resource-manager-")
        )
        return {item["file"]: item["sha256"] for item in arm["files"]}

    old_members, new_members = arm_members(PREVIOUS), arm_members(FRESH)
    old_library = {
        name: value for name, value in old_members.items()
        if name.startswith("package/lib/")
    }
    new_library = {
        name: value for name, value in new_members.items()
        if name.startswith("package/lib/")
    }
    assert old_library and old_library == new_library
    for name in ("arm-resource-patch-compatibility.js", "model-utils.js"):
        member = "package/dist/src/rules/" + name
        assert old_members[member] == new_members[member]
    attribution = FRESH / "source-attribution"
    records = read(attribution / "observations.json")["records"]
    old_records = {
        (row["project"], row["diagnosticIndex"]): row
        for row in read(PREVIOUS / "source-attribution/observations.json")["records"]
    }
    assert len(records) == len(old_records) == 182
    assert {
        (row["project"], row["diagnosticIndex"]) for row in records
    } == old_records.keys()
    inventory = read(attribution / "inventory.json")["projects"]
    assert len(inventory) == 51
    for item in inventory:
        source = read(attribution / item["source"])
        native = read(attribution / item["native"])
        assert (
            source["rawDiagnostics"]
            == native["rawDiagnostics"]
            == current[item["project"]]["rawDiagnostics"]
        )
    warnings = {
        (project, index): diagnostic
        for project, receipt in current.items()
        for index, diagnostic in enumerate(receipt["rawDiagnostics"])
    }
    counts, edges, witnessed = accounting.bridge(records, set(warnings))
    assert counts == {
        "retainedSwaggerRecords": 182,
        "configuredTypeSpecWarnings": 108,
        "acceptedOrNonInputRecords": 92,
        "suppressedRecords": 1,
        "reportingRecords": 89,
        "recordWarningAssociations": 91,
        "additionalAssociationsWithinRecords": 2,
        "repeatedAssociationsAcrossRecords": 14,
        "distinctWitnessedWarnings": 77,
        "warningsOutsideJoin": 31,
        "netDifference": 74,
    }, counts
    outside, removed = remap_decisions(
        read(ROOT / "count-gap-20261106/decisions.json")["groups"],
        previous,
        current,
        set(warnings) - witnessed,
    )
    for row in outside:
        row["currentReceipt"] = receipt_paths[FRESH.name, row["project"]]
    for row in removed:
        row["previousReceipt"] = receipt_paths[PREVIOUS.name, row["project"]]
    categories = dict(sorted(collections.Counter(
        row["category"] for row in outside
    ).items()))
    assert categories == {
        "empty-patch": 1,
        "historical-versioning": 13,
        "writable-patch-not-put": 17,
    }, categories
    assert len(removed) == 7
    assert all(
        row["category"] == "typespec-empty-wrapper-overcheck" for row in removed
    )
    delta = read(FRESH / "candidate-delta.json")
    assert (
        delta["beforeFindings"],
        delta["afterFindings"],
        delta["removedFindings"],
        delta["addedFindings"],
    ) == (117, 108, 9, 0)
    actual_removed = collections.Counter(
        (row["project"], diagnostic_key(diagnostic))
        for row in delta["projects"]
        for diagnostic in row["removed"]
    )
    expected_removed = collections.Counter(
        (row["project"], diagnostic_key(row["diagnostic"])) for row in removed
    )
    joined_removals = {
        (project, index)
        for project, record_index in ACCEPTED_OPAQUE_RECORDS
        for context in old_records[project, record_index]["contexts"]
        for index in context["warningIndices"]
    }
    assert len(joined_removals) == 2
    expected_removed.update(
        (project, diagnostic_key(previous[project]["rawDiagnostics"][index]))
        for project, index in joined_removals
    )
    assert actual_removed == expected_removed
    changed_contexts = []
    changed_observations = []
    for record in records:
        old = old_records[record["project"], record["diagnosticIndex"]]
        identity = record["project"], record["diagnosticIndex"]
        if identity in ACCEPTED_OPAQUE_RECORDS:
            assert old["observation"] == "source-reported"
            assert record["observation"] == "source-accepts"
            changed_observations.append({
                "project": record["project"],
                "diagnosticIndex": record["diagnosticIndex"],
                "name": record["name"],
                "previous": old["observation"],
                "current": record["observation"],
                "reason": (
                    "The matching PUT object exists at the same encoded payload path; "
                    "its flattened children no longer hide that container."
                ),
            })
        else:
            assert record["observation"] == old["observation"], identity
        if canonical_context(record["contexts"]) != canonical_context(old["contexts"]):
            changed_contexts.append(
                {
                    "project": record["project"],
                    "diagnosticIndex": record["diagnosticIndex"],
                    "observation": record["observation"],
                    "before": old["contexts"],
                    "after": record["contexts"],
                }
            )
    reviewed = read(ROOT / "inherited-20261105/assessed-contexts.json")
    reviewed_acceptances = (
        reviewed["unchangedReviewedAcceptedSchemas"]
        + reviewed["newlyReviewedAcceptedSchemas"]
    )
    reviewed_ids = {
        (row["project"], row["diagnosticIndex"]) for row in reviewed_acceptances
    }
    assert len(reviewed_ids) == 81
    assert not reviewed_ids.intersection(
        (row["project"], row["diagnosticIndex"]) for row in changed_contexts
    ), "Changed accepted predicate contexts require explicit renewed semantic review"
    assert {
        (row["project"], row["diagnosticIndex"]) for row in changed_contexts
    } == ACCEPTED_OPAQUE_RECORDS | {
        ("specification/cdn/resource-manager/Microsoft.Cdn/EdgeActions", 0)
    }
    projects = []
    for project in sorted(current):
        selected = [record for record in records if record["project"] == project]
        summary, _, _ = accounting.bridge(
            selected, {identity for identity in warnings if identity[0] == project}
        )
        projects.append({"project": project, **summary})
    for key in counts:
        assert sum(project[key] for project in projects) == counts[key], key
    by_family = collections.defaultdict(collections.Counter)
    witnesses_by_family = collections.defaultdict(set)
    for record in records:
        family = record["swaggerFamily"]
        by_family[family][record["observation"]] += 1
        witnesses_by_family[family].update(
            edges[record["project"], record["diagnosticIndex"]]
        )
    result = {
        "candidateCommit": load(FRESH / "task.json")["candidateCommit"],
        "boundary": (
            "Exact saved record-to-configured-warning incidence accounting, not "
            "cross-engine defect equivalence. Diagnostic occurrences remain distinct. "
            "Historical classifications are remapped by exact project and complete "
            "diagnostic records, never old indices, names or source position alone."
        ),
        "counts": counts,
        "outsideJoinCategories": categories,
        "outsideJoinWarnings": outside,
        "removedOverchecks": removed,
        "all51DiagnosticArraysExactlyEqual": True,
        "retainedObservations": dict(sorted(collections.Counter(
            row["observation"] for row in records
        ).items())),
        "bySwaggerFamily": {
            family: dict(observations)
            for family, observations in sorted(by_family.items())
        },
        "configuredWarningWitnessesBySwaggerFamily": {
            family: len(identities)
            for family, identities in sorted(witnesses_by_family.items())
        },
        "retainedRoutes": {
            "identity": "Frozen project path plus exact HTTP route; inspections, not defects.",
            "swaggerRoutes": len({
                (record["project"], record["route"]) for record in records
            }),
            "sourceRoutes": len({
                (record["project"], context["route"])
                for record in records
                for context in record["contexts"]
            }),
        },
        "reviewedAcceptedSchemasWithUnchangedPredicateContexts": 81,
        "unchangedArmLibraryMembers": len(new_library),
        "compatibilityAndModelUtilsUnchanged": True,
        "canonicalization": (
            "Exclude configured-warning indices and newly added jsonPath tracing; "
            "canonicalize only installed ARM package store prefixes. All other "
            "predicate/candidate/source fields remain compared."
        ),
        "changedPredicateContexts": changed_contexts,
        "changedObservations": changed_observations,
        "projects": projects,
        "directionalRetainedRecordDifferences": {
            "swaggerHigher": sum(max(0, row["netDifference"]) for row in projects),
            "typeSpecHigher": sum(max(0, -row["netDifference"]) for row in projects),
            "absoluteDifference": sum(abs(row["netDifference"]) for row in projects),
        },
        "inputByteHashes": hashes,
    }
    return result


def render_route_index():
    records = load(FRESH / "source-attribution/observations.json")["records"]
    groups = collections.defaultdict(list)
    for record in records:
        groups[record["project"], record["route"]].append(record)
    assert len(groups) == 97
    lines = [
        "# Retained PATCH-route source inspections",
        "",
        "All 182 retained Swagger records are grouped by frozen project and exact PATCH route.",
        "The 97 routes were inspected in both representations; these are not 97 matched defects.",
        "Warnings are distinct configured indices within each route's reviewed contexts.",
        "A warning can witness several records or routes: do not sum this column across rows.",
        "Dispositions classify source predicates, not historical emitted defects.",
        "",
    ]
    project = None
    for (name, route), rows in sorted(groups.items()):
        if project != name:
            project = name
            lines.extend([
                f"## `{project}`", "",
                "| Exact PATCH route | Swagger records | Source warning witnesses | Source dispositions |",
                "| --- | ---: | ---: | --- |",
            ])
        warnings = {
            index for row in rows
            for context in row["contexts"] for index in context["warningIndices"]
        }
        dispositions = ", ".join(
            f"{count} {key}" for key, count in sorted(collections.Counter(
                row["observation"] for row in rows
            ).items())
        )
        source = rows[0]["sourceFile"]
        lines.append(
            f"| `{route}` | {len(rows)} | {len(warnings)} | "
            f"[{dispositions}](../refresh-20261110-wrapper/source-attribution/{source}) |"
        )
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["write", "check"])
    arguments = parser.parse_args()
    result = reconcile()
    destination = HERE / "reconciliation.json"
    if arguments.mode == "write":
        assert not destination.exists()
        destination.write_text(
            json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n"
        )
    else:
        assert load(destination) == result
    print(json.dumps({
        key: result[key]
        for key in (
            "counts", "outsideJoinCategories",
            "directionalRetainedRecordDifferences",
        )
    }))

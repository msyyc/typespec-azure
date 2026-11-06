import argparse
import collections
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def warning_edges(records):
    edges = {}
    seen = set()
    for record in records:
        identity = (record["project"], record["diagnosticIndex"])
        if identity in seen:
            raise ValueError(f"Duplicate retained record: {identity}")
        seen.add(identity)
        indices = set()
        for context in record["contexts"]:
            for index in context["warningIndices"]:
                if type(index) is not int or index < 0:
                    raise ValueError(f"Invalid warning index: {index}")
                indices.add(index)
        edges[identity] = {(record["project"], index) for index in indices}
    return edges


def bridge(records, warning_ids):
    edges = warning_edges(records)
    witnessed = set().union(*edges.values()) if edges else set()
    if not witnessed <= warning_ids:
        raise ValueError("An attribution index is outside the configured warning universe")
    accepted = suppressed = reporters = 0
    for record, associated in zip(records, edges.values()):
        category = record["observation"]
        if category in {"source-accepts", "name-not-source-leaf"}:
            if associated:
                raise ValueError("An accepted record cannot introduce warning witnesses")
            accepted += 1
        elif category == "body-suppressed":
            if associated:
                raise ValueError("A suppressed-only record cannot introduce a configured warning")
            suppressed += 1
        elif category in {"source-reported", "mixed-source-predicates", "body-reported"}:
            if not associated:
                raise ValueError("A reporting record needs a precise configured warning witness")
            reporters += 1
        else:
            raise ValueError(f"Unassessed observation: {category}")
    incidences = sum(map(len, edges.values()))
    result = {
        "retainedSwaggerRecords": len(records),
        "configuredTypeSpecWarnings": len(warning_ids),
        "acceptedOrNonInputRecords": accepted,
        "suppressedRecords": suppressed,
        "reportingRecords": reporters,
        "recordWarningAssociations": incidences,
        "additionalAssociationsWithinRecords": incidences - reporters,
        "repeatedAssociationsAcrossRecords": incidences - len(witnessed),
        "distinctWitnessedWarnings": len(witnessed),
        "warningsOutsideJoin": len(warning_ids - witnessed),
        "netDifference": len(records) - len(warning_ids),
    }
    assert (
        accepted + suppressed + result["repeatedAssociationsAcrossRecords"]
        - result["additionalAssociationsWithinRecords"] - result["warningsOutsideJoin"]
        == result["netDifference"]
    )
    return result, edges, witnessed


def reconcile():
    full = ROOT / "refresh-20261105-inherited" / "runs" / "full-corpus"
    attribution = ROOT / "refresh-20261105-inherited" / "source-attribution"
    hashes = {}

    def load(path):
        hashes[path.relative_to(ROOT).as_posix()] = digest(path)
        return read(path)

    receipts = {}
    receipt_paths = {}
    for path in sorted(full.glob("native-*.json")):
        native = load(path)
        assert native["status"] == "success"
        assert native["project"] not in receipts
        receipts[native["project"]] = native
        receipt_paths[native["project"]] = path.relative_to(ROOT).as_posix()
    assert len(receipts) == 487
    records = load(attribution / "observations.json")["records"]
    inventory = load(attribution / "inventory.json")["projects"]
    sources = {}
    for item in inventory:
        captured = load(attribution / item["native"])
        source = load(attribution / item["source"])
        assert captured["project"] == source["project"] == item["project"]
        # Array equality, not just multiset equality, proves the saved index mapping.
        assert captured["rawDiagnostics"] == source["rawDiagnostics"] == receipts[item["project"]]["rawDiagnostics"]
        sources[item["project"]] = item["source"]
    assert len(sources) == 51
    for record in records:
        assert record["sourceFile"] == sources[record["project"]]
    warnings = {
        (project, index): warning
        for project, native in receipts.items()
        for index, warning in enumerate(native["rawDiagnostics"])
    }
    counts, edges, witnessed = bridge(records, set(warnings))
    expected = {
        "retainedSwaggerRecords": 182, "configuredTypeSpecWarnings": 117,
        "acceptedOrNonInputRecords": 90, "suppressedRecords": 1,
        "reportingRecords": 91, "recordWarningAssociations": 93,
        "additionalAssociationsWithinRecords": 2,
        "repeatedAssociationsAcrossRecords": 14,
        "distinctWitnessedWarnings": 79, "warningsOutsideJoin": 38,
        "netDifference": 65,
    }
    assert counts == expected, counts
    classifications = {}
    for group in load(HERE / "decisions.json")["groups"]:
        for index in group["warningIndices"]:
            identity = (group["project"], index)
            assert identity not in classifications
            classifications[identity] = group
    assert set(classifications) == set(warnings) - witnessed
    outside = []
    for (project, index), group in sorted(classifications.items()):
        outside.append({
            "project": project, "warningIndex": index, "diagnostic": warnings[(project, index)],
            "category": group["category"], "reason": group["reason"],
            "sourceRefs": group["sourceRefs"], "originalReceipt": receipt_paths[project],
        })
    category_counts = dict(sorted(collections.Counter(row["category"] for row in outside).items()))
    assert category_counts == {
        "empty-patch": 1, "historical-versioning": 13,
        "typespec-empty-wrapper-overcheck": 7, "writable-patch-not-put": 17,
    }
    fixtures = load(HERE / "fixtures.json")
    assert fixtures["projectCount"] == 0
    assert fixtures["candidateCommit"] == "0121903975ab45cde7d7aca37cf50ffd7f3855d3"
    assert fixtures["specsCommit"] == "2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9"
    assert len(fixtures["fixtures"]) == 4
    for fixture in fixtures["fixtures"]:
        assert fixture["native"]["status"] == "success"
        assert len(fixture["native"]["rawDiagnostics"]) == fixture["expected"]
        captured = fixture["source"]
        # Source is the authored fixture text; the execution capture is separate.
        assert isinstance(captured, str)
        observation = fixture["observation"]
        captured_bytes = (json.dumps(observation, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
        assert hashlib.sha256(captured_bytes).hexdigest() == fixture["sourceSha256"]
        assert observation["rawDiagnostics"] == fixture["native"]["rawDiagnostics"]
        for key in ["bodyModuleSha256", "compatibilityModuleSha256", "extractorSha256", "originalWorkerSha256"]:
            assert observation[key] == read(attribution / "source-0.json")[key]
        if fixture["name"] == "same-immutable-wrapper":
            pair = observation["pairs"][0]
            assert pair["patchBody"]["type"] == pair["putBody"]["type"]
            wrapper = next(leaf for leaf in pair["leaves"] if leaf["jsonName"] == "properties")
            assert wrapper["family"] == "missingProperty" and wrapper["candidates"] == []
            assert wrapper["configuredWarning"] and not wrapper["recursive"]
            assert next(leaf for leaf in pair["leaves"] if leaf["jsonName"] == "tags")["family"] is None
    source_evidence = load(HERE / "source-evidence.json")
    assert source_evidence["specsCommit"] == "2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9"
    expected_refs = {
        (group["project"], file, start, end)
        for group in read(HERE / "decisions.json")["groups"]
        for file, start, end in group["sourceRefs"]
    }
    assert {
        (item["project"], item["file"], item["start"], item["end"])
        for item in source_evidence["excerpts"]
    } == expected_refs
    projects = []
    for project in sorted(receipts):
        selected = [record for record in records if record["project"] == project]
        summary, _, _ = bridge(selected, {key for key in warnings if key[0] == project})
        if selected or summary["configuredTypeSpecWarnings"]:
            projects.append({"project": project, **summary})
    for key in counts:
        assert sum(project[key] for project in projects) == counts[key], key
    reverse = collections.defaultdict(list)
    for identity, values in edges.items():
        for value in values:
            reverse[value].append({"project": identity[0], "diagnosticIndex": identity[1]})
    repeated = [
        {"project": project, "warningIndex": index, "diagnostic": warnings[(project, index)],
         "retainedRecords": sorted(identities, key=lambda row: row["diagnosticIndex"])}
        for (project, index), identities in sorted(reverse.items()) if len(identities) > 1
    ]
    multiple = [
        {"project": project, "diagnosticIndex": index,
         "warningIndices": sorted(value[1] for value in values)}
        for (project, index), values in sorted(edges.items()) if len(values) > 1
    ]
    return {
        "scope": "Exact saved record-to-configured-warning incidence accounting, not cross-engine defect equivalence. Distinct diagnostic-array occurrences are retained even at identical locations.",
        "counts": counts, "outsideJoinCategories": category_counts,
        "all51DiagnosticArraysExactlyEqual": True,
        "outsideJoinWarnings": outside, "repeatedWarningAssociations": repeated,
        "recordsWithMultipleWarnings": multiple, "projects": projects,
        "directionalRetainedRecordDifferences": {
            "swaggerHigher": sum(max(0, p["netDifference"]) for p in projects),
            "typeSpecHigher": sum(max(0, -p["netDifference"]) for p in projects),
            "absoluteDifference": sum(abs(p["netDifference"]) for p in projects),
        },
        "inputByteHashes": hashes,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["write", "check"])
    args = parser.parse_args()
    result = reconcile()
    destination = HERE / "reconciliation.json"
    if args.mode == "write":
        destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    else:
        assert read(destination) == result, "Saved reconciliation differs from its inputs"
    print(json.dumps({"counts": result["counts"], "outsideJoinCategories": result["outsideJoinCategories"],
                      "directionalDifferences": result["directionalRetainedRecordDifferences"]}))

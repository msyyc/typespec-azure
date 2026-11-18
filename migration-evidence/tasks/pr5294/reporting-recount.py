"""Attribute saved Swagger reports to callbacks without executing either linter."""

import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def identity(diagnostic):
    return (
        diagnostic["project"],
        diagnostic.get("document", diagnostic.get("swaggerFile")),
        diagnostic["rule"],
        diagnostic["message"],
        tuple(map(str, diagnostic["path"])),
    )


def main():
    archive, output = map(Path, sys.argv[1:])
    assert not output.exists(), "Use a fresh output; do not overwrite saved evidence."
    archive_receipt = load(ROOT / "runs" / "20261102-semantic-analysis" / "archive.json")
    inventory_bytes = (archive / "archive-manifest.json").read_bytes()
    assert hashlib.sha256(inventory_bytes).hexdigest() == archive_receipt["archiveManifestSha256"]
    inventory = json.loads(inventory_bytes)
    for item in inventory["files"]:
        data = (archive / item["path"]).read_bytes()
        assert len(data) == item["bytes"]
        assert hashlib.sha256(data).hexdigest() == item["sha256"]

    receipts = [load(p) for p in sorted((archive / "swagger-traces").glob("*.json"))]
    assert len(receipts) == 136 and all(not r["errors"] for r in receipts)
    reports = sorted(
        (d for receipt in receipts for d in receipt["diagnostics"]), key=identity
    )
    originals = load(ROOT / "runs" / "20261030-94b316787" / "swagger-observations.json")
    assert Counter(map(identity, reports)) == Counter(map(identity, originals))
    assert len(reports) == len(set(map(identity, reports)))
    callbacks = [
        dict(
            finding,
            project=capture["project"],
            document=capture["document"],
            rule=capture["rule"],
            route=capture["route"],
        )
        for receipt in receipts
        for capture in receipt["captures"]
        for finding in capture["findings"]
    ]
    differences = load(
        ROOT / "runs" / "20261102-semantic-analysis" / "difference-ledger.json"
    )["differences"]
    labels = {
        (row["project"], row["route"], row["kind"], row["propertyPath"]):
        row["swaggerRemaining"]["category"]
        for row in differences
        if row.get("swaggerRemaining")
    }
    candidates = defaultdict(list)
    for index, report in enumerate(reports):
        candidates[identity(report)[:-1]].append(index)
    attributed = defaultdict(list)
    before = Counter()
    for callback in callbacks:
        key = (
            callback["project"], callback["document"], callback["rule"],
            callback["message"],
        )
        returned = tuple(map(str, callback["returnedPath"]))
        matches = [
            index
            for index in candidates[key]
            if returned[:len(reports[index]["path"])] == identity(reports[index])[-1]
        ]
        assert len(matches) == 1, (key, returned, matches)
        index = matches[0]
        category = labels.get(
            (callback["project"], callback["route"], callback["kind"], callback["propertyPath"]),
            "shared-text-key",
        )
        before[category] += 1
        attributed[index].append({
            "check": callback["kind"],
            "propertyPath": callback["propertyPath"],
            "returnedPath": callback["returnedPath"],
            "category": category,
        })
    assert len(attributed) == len(reports), "Every saved report must have a callback."

    # Independently captured prepareResults input/output validates the path association.
    control = load(archive / "reporting-control.json")
    project_reports = [d for d in reports if d["project"] == control["project"]]
    mapped_before = Counter(
        (r["rule"], tuple(map(str, r["path"])), r["message"])
        for i, r in enumerate(reports)
        if r["project"] == control["project"]
        for _ in attributed[i]
    )
    control_key = lambda d: (d["rule"], tuple(map(str, d["path"])), d["message"])
    assert mapped_before == Counter(
        control_key(d) for call in control["calls"] for d in call["before"]
    )
    assert Counter(map(control_key, project_reports)) == Counter(
        control_key(d) for call in control["calls"] for d in call["after"]
    )

    categories = {}
    records = []
    for index, report in enumerate(reports):
        findings = attributed[index]
        labels_at_report = sorted({c["category"] for c in findings})
        group = labels_at_report[0] if len(labels_at_report) == 1 else "mixed"
        totals = categories.setdefault(
            group, {"reportedDiagnostics": 0, "callbacks": 0, "byRule": Counter()}
        )
        totals["reportedDiagnostics"] += 1
        totals["callbacks"] += len(findings)
        totals["byRule"][report["rule"]] += 1
        records.append(dict(
            report, category=group, callbackCategories=labels_at_report, callbacks=findings
        ))
    for group in categories.values():
        group["byRule"] = dict(sorted(group["byRule"].items()))
        group["reportingReduction"] = group["callbacks"] - group["reportedDiagnostics"]
    expected_before = Counter({"shared-text-key": 834})
    expected_before.update(
        load(ROOT / "runs" / "20261102-semantic-analysis" / "difference-ledger.json")
        ["swaggerBeforeReportingUnshared"]
    )
    assert before == expected_before
    assert sum(c["reportedDiagnostics"] for c in categories.values()) == 975
    assert sum(c["callbacks"] for c in categories.values()) == len(callbacks) == 1057
    assert sum(c["reportingReduction"] for c in categories.values()) == 82
    check_ledger = {
        (row["project"], row["route"], row["kind"], row["propertyPath"]): row
        for row in load(archive / "analysis" / "check-path-ledger.json")
    }
    for record in records:
        if record["category"] == "mixed":
            route = record["path"][1]
            for callback in record["callbacks"]:
                row = check_ledger[
                    (record["project"], route, callback["check"], callback["propertyPath"])
                ]
                assert row["typespec"] == (
                    1 if callback["category"] == "shared-text-key" else 0
                )
    result = {
        "schemaVersion": 1,
        "mode": "Read-only attribution of saved reports; no linter, compile or emission run.",
        "evidenceBaseCommit": "87ae71cb0d3870ce9591855ff9fa3571e18695bc",
        "candidateCommit": "8a92389c9f9488035ab65c6ed3e08a49cc822f25",
        "traceCommit": "94b316787e2a19847c26986412ce254ca4da33b4",
        "archiveSha256": archive_receipt["sha256"],
        "association": (
            "Exact project/document/rule/message and reported-path ancestry of the returned "
            "callback path; exactly one saved report for every callback, no longest-prefix "
            "selection or fuzzy matching. Mixed category sets are retained, not assigned "
            "to one representative callback. This is report attribution, not defect identity."
        ),
        "verification": {
            "payloadHashes": len(inventory["files"]),
            "tracedProjects": len(receipts),
            "callbacksAssignedUniquely": len(callbacks),
            "reportsAttributed": len(reports),
            "originalReportedMultiset": "exact",
            "independentPrepareResultsControl": {
                "project": control["project"],
                "before": sum(mapped_before.values()),
                "after": len(project_reports),
                "matched": True,
            },
        },
        "categories": dict(sorted(categories.items())),
        "reports": records,
    }
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({k: v for k, v in result.items() if k != "reports"}, indent=2))


if __name__ == "__main__":
    main()

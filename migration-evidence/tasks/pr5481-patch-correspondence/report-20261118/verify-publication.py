"""Verify the report-only refresh without changing historical run inventories."""

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PREVIOUS_COMMIT = "b225b1daab93a582eecd4660667a9d8eb872c2fe"


def main(root, mode):
    original = ROOT / "names-20261117/verify-publication.py"
    source = original.read_text(encoding="utf-8")
    before = '    namespace = {"__file__": str(original), "__name__": "names_publication_verifier"}'
    assert source.count(before) == 1
    adapter = '''
    inventory_binding = '    inventory = fresh / "provenance/publication-inventory.json"'
    assert source.count(inventory_binding) == 1
    source = source.replace(
        inventory_binding,
        '    inventory = root / "report-20261118/publication-inventory.json"',
    )
'''
    source = source.replace(before, adapter + before)
    namespace = {"__file__": str(original), "__name__": "report_publication_verifier"}
    exec(compile(source, str(original), "exec"), namespace)
    namespace["main"](root.resolve(), mode)

    inventory = root / "report-20261118/publication-inventory.json"
    data = json.loads(inventory.read_text(encoding="utf-8"))
    report_scope = {
        "kind": "report-only",
        "previousEvidenceCommit": PREVIOUS_COMMIT,
        "execution": "refresh-20261117-names/task.json",
        "freshTypeSpecCompilations": 0,
        "swaggerRegenerations": 0,
    }
    if mode == "seal":
        data["reportRefresh"] = report_scope
        inventory.write_text(
            json.dumps(data, indent=2) + "\n", encoding="utf-8", newline="\n"
        )
    assert data["reportRefresh"] == report_scope
    report = (root / "migration.md").read_text(encoding="utf-8")
    headings = [line for line in report.splitlines() if line.startswith("## ")]
    assert headings == [
        "## 1. Scope",
        "## 2. Coverage",
        "## 3. Why diagnostic counts differ",
        "## 4. Function-level coverage",
        "## NOTES",
    ]
    assert "**Assessed coverage:**" in report
    summary = json.loads(
        (root / "refresh-20261117-names/staging-comparison/summary.json").read_text(
            encoding="utf-8"
        )
    )
    reconciliation = json.loads(
        (root / "names-20261117/reconciliation.json").read_text(encoding="utf-8")
    )
    counts = reconciliation["counts"]
    disposition = reconciliation["semanticDisposition"]
    outside = reconciliation["outsideJoinCategories"]
    swagger = summary["swaggerReportedDiagnostics"]
    typespec = summary["typeSpecReportedDiagnostics"]
    assert typespec == counts["configuredTypeSpecWarnings"]
    contributions = [
        swagger - counts["retainedSwaggerRecords"],
        disposition["compatibleOrNonInputRecords"],
        disposition["approvedNotMigratedRecords"],
        counts["suppressedRecords"],
        counts["repeatedAssociationsAcrossRecords"],
        -outside["historical-versioning"],
        -outside["writable-patch-not-put"],
        -outside["empty-patch"],
    ]
    assert swagger - typespec == sum(contributions)
    equation = " ".join(
        f"{'+' if value >= 0 else '-'} {abs(value):,}"
        for value in contributions[1:]
    )
    expected = (
        f"**Raw-count reconciliation: {swagger:,} - {typespec:,} = "
        f"{contributions[0]:,} {equation} = {swagger - typespec:,}.**"
    )
    assert expected in " ".join(report.split())
    print(json.dumps({"reportRefresh": report_scope, "reportContract": "verified"}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("mode", nargs="?", choices=["seal", "check"], default="check")
    arguments = parser.parse_args()
    main(arguments.root, arguments.mode)

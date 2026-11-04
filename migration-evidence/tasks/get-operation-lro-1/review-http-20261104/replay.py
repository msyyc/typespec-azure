import json
from pathlib import Path

root = Path(__file__).parent
coverage = json.loads((root / "coverage-summary.json").read_text(encoding="utf-8"))
findings = json.loads((root / "findings.json").read_text(encoding="utf-8"))
comparison = json.loads((root / "identity-comparison.json").read_text(encoding="utf-8"))
inventory = json.loads((root / "project-inventory.json").read_text(encoding="utf-8"))
assert coverage["selectedProjectCount"] == coverage["assessableProjectCount"] == len(inventory) == 487
assert not coverage["unassessedProjects"]
assert coverage["validatorRawCount"] == 4
assert coverage["nativeRawCount"] == len(findings) == 12
assert sum(item["nativeLroMetadata"] for item in findings) == 8
assert sum(bool(item["acceptedLegacyScopes"]) for item in findings) == 4
assert sum(item["inSelectedVersionHttpGraph"] for item in findings) == 8
assert sum(bool(item["paired"]) for item in findings) == 4
assert comparison["status"] == "identical"
assert comparison["unchanged"] == 12
assert not comparison["added"] and not comparison["removed"]
print("Saved-observation audit passed: 487 projects; Swagger 4; native 12; 12 unchanged identities.")
print("This audit does not rerun native compilation or establish semantic equivalence.")

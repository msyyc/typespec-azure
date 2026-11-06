import json
from pathlib import Path

root = Path(__file__).parent


def load(name):
    return json.loads((root / name).read_text(encoding="utf-8"))


coverage = load("coverage-summary.json")
inventory = load("project-inventory.json")
findings = load("findings.json")
runtime = load("runtime-verification.json")
assert coverage["selectedProjectCount"] == coverage["assessableProjectCount"] == len(inventory) == 487
assert not coverage["unassessedProjects"]
assert sum(item["validatorRawCount"] for item in inventory) == coverage["validatorRawCount"] == 4
assert sum(item["nativeRawCount"] for item in inventory) == coverage["nativeRawCount"] == 8
retained = [item for item in findings if item["reportedNow"]]
removed = [item for item in findings if not item["reportedNow"]]
assert len(retained) == 8 and len(removed) == 4
assert all(item["nativeLroMetadata"] and not item["acceptedLegacyScopes"] for item in retained)
assert sum(item["inSelectedVersionHttpGraph"] for item in retained) == 4
assert all(not item["nativeLroMetadata"] and item["acceptedLegacyScopes"] for item in removed)
assert sum(len(item["paired"]) for item in removed) == 4
assert not any(item["paired"] for item in retained)
assert runtime["status"] == "passed" and runtime["sdkRuleAbsentFromArtifactsAndRuntime"]
assert not runtime["unexpectedDifferences"]
print("Saved-observation audit passed: 487 projects; Swagger 4; ARM 8; four Legacy-only matches intentionally removed.")
print("This audit does not rerun native compilation or establish semantic equivalence.")

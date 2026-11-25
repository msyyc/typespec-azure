import argparse
import hashlib
import json
import tarfile
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--evidence-dir", type=Path, default=Path(__file__).parent)
parser.add_argument("--native-archive", type=Path)
args = parser.parse_args()


def load(name):
    return json.loads((args.evidence_dir / name).read_text(encoding="utf-8"))


coverage = load("coverage-summary.json")
inventory = load("project-inventory.json")
findings = load("findings.json")
runtime = load("runtime-verification.json")
assessment = load("assessment.json")
manifest = load("manifest.json")
assert coverage["selectedProjectCount"] == coverage["assessableProjectCount"] == len(inventory) == 487
assert not coverage["unassessedProjects"]
assert sum(item["validatorRawCount"] for item in inventory) == coverage["validatorRawCount"]
assert sum(item["nativeRawCount"] for item in inventory) == coverage["nativeRawCount"]
reported = [item for item in findings if item["reportedNow"]]
retired = [item for item in findings if not item["reportedNow"]]
assert len(reported) == coverage["nativeRawCount"]
assert len(retired) == 8
assert all(item["verb"] == "get" and item["acceptedLegacyScopes"] for item in reported)
assert all(not item["acceptedLegacyScopes"] and item["inSelectedVersionHttpGraph"] is None for item in retired)
assert len(runtime["restoredLegacyMatches"]) == 4
assert sum(len(item["paired"]) for item in runtime["restoredLegacyMatches"]) == coverage["validatorRawCount"] == 4
assert runtime["status"] == assessment["status"] == "passed"
assert runtime["sdkRulePresentAndArmRuleAbsent"]
assert manifest["candidate"]["commit"] == runtime["candidateCommit"] == assessment["candidateCommit"]
assert manifest["config"]["scope"] == "source"
assert manifest["config"]["nativeMode"] == "target-only"
assert manifest["config"]["baselinePolicy"] == "frozen-reference"
if args.native_archive:
    asset = next(item for item in load("assets.json")["assets"] if item["contents"] == "native")
    assert hashlib.sha256(args.native_archive.read_bytes()).hexdigest() == asset["sha256"]
    with tarfile.open(args.native_archive, "r:gz") as archive:
        receipts = [item for item in archive.getmembers()
                    if item.name.startswith("run/native-")
                    and item.name.removeprefix("run/native-").removesuffix(".json").isdigit()]
        assert len(receipts) == 487
        counts = {}
        for member in receipts:
            receipt = json.load(archive.extractfile(member))
            assert receipt["status"] == "success" and receipt["defaultActivation"] == "not-assessed"
            assert receipt["diagnostics"] == receipt["rawDiagnostics"]
            assert receipt["project"] not in counts
            counts[receipt["project"]] = len(receipt["rawDiagnostics"])
        assert all(counts[item["project"]] == item["nativeRawCount"] for item in inventory)
swagger_higher = sum(max(item["validatorRawCount"] - item["nativeRawCount"], 0) for item in inventory)
typespec_higher = sum(max(item["nativeRawCount"] - item["validatorRawCount"], 0) for item in inventory)
assert coverage["validatorRawCount"] - coverage["nativeRawCount"] == swagger_higher - typespec_higher
print(json.dumps({
    "status": "passed", "projects": len(inventory),
    "swaggerDiagnostics": coverage["validatorRawCount"],
    "typeSpecDiagnostics": coverage["nativeRawCount"],
    "swaggerHigherOccurrences": swagger_higher, "typeSpecHigherOccurrences": typespec_higher,
    "restoredLegacyMatches": 4, "retiredNativeOnlyTargets": len(retired),
    "savedNativeReceiptsReplayed": 487 if args.native_archive else 0,
    "limitation": "Saved-observation accounting audit; no fresh TypeSpec compilation, Swagger generation, exhaustive suppressed-diagnostic capture or semantic-equivalence decision.",
}, indent=2))

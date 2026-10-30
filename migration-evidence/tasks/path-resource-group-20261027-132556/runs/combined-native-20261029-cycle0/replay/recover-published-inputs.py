"""Recover published migration inputs in a new, task-owned checkout; never emit Swagger."""

import argparse
import hashlib
import json
import pathlib
import subprocess
import sys
import tarfile
from datetime import datetime, timezone

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--evidence-root", required=True)
parser.add_argument("--run-relative", required=True)
parser.add_argument("--recovery-root", required=True)
parser.add_argument("--node", required=True)
args = parser.parse_args()
evidence = pathlib.Path(args.evidence_root).resolve()
run = evidence / args.run_relative
root = pathlib.Path(args.recovery_root).resolve()
root.mkdir(exist_ok=False)
logs = root / "receipts"
logs.mkdir()
downloads = root / "downloads"
downloads.mkdir()
read = lambda file: json.loads(file.read_text(encoding="utf-8-sig"))
digest = lambda file: hashlib.sha256(file.read_bytes()).hexdigest()
journal = []


def command(argv, cwd=root, timeout=600):
    item = {"args": list(map(str, argv)), "started": datetime.now(timezone.utc).isoformat(), "status": "attempted"}
    journal.append(item)
    (logs / "commands.json").write_text(json.dumps(journal, indent=2) + "\n", encoding="utf-8")
    try:
        result = subprocess.run(list(map(str, argv)), cwd=cwd, capture_output=True, timeout=timeout)
        item.update(exit=result.returncode, status="passed" if result.returncode == 0 else "failed")
        (logs / f"command-{len(journal):03}.log").write_bytes(result.stdout + result.stderr)
    except Exception as error:
        item.update(status="failed", error=str(error))
        raise
    finally:
        (logs / "commands.json").write_text(json.dumps(journal, indent=2) + "\n", encoding="utf-8")
    if result.returncode:
        raise RuntimeError(f"Recovery command failed: {argv}; see command-{len(journal):03}.log")
    return result.stdout


def recover_git(directory, url, commit, filtered=False):
    directory.mkdir(exist_ok=True)
    command(["git", "init", directory])
    command(["git", "-C", directory, "remote", "add", "origin", url])
    command(["git", "-C", directory, "-c", "core.longpaths=true", "fetch", "--depth=1", *(["--filter=blob:none"] if filtered else []), "origin", commit])
    assert command(["git", "-C", directory, "rev-parse", "FETCH_HEAD"]).decode().strip() == commit
    if not filtered:
        command(["git", "-C", directory, "-c", "core.longpaths=true", "checkout", "--detach", commit])


assets = read(run / "receipts" / "assets-publication.json")
equality = read(run / "receipts" / "native-committed-source-equality.json")
descriptor = read(run / "baseline-descriptor.json")
assert assets["candidateCommit"] == equality["commit"]
for asset in assets["assets"]:
    command(["gh", "release", "download", assets["release"], "--repo", assets["repository"], "--pattern", asset["name"], "--dir", downloads])
    file = downloads / asset["name"]
    assert digest(file) == asset["sha256"] and file.stat().st_size == asset["bytes"]
inputs = root / "inputs"
inputs.mkdir()
archive = next(item for item in assets["assets"] if item["name"].endswith(".tar.gz"))
with tarfile.open(downloads / archive["name"]) as stream:
    stream.extractall(inputs, filter="data")
provenance = read(run / "receipts" / "artifact-provenance.json")
archived_provenance = read(inputs / "provenance" / "artifact-provenance.json")
assert archived_provenance["candidateContentIdentity"] == provenance["candidateContentIdentity"]
assert archived_provenance["artifacts"] == provenance["artifacts"]
package_files = 0
for artifact in provenance["artifacts"]:
    file = inputs / "packages" / artifact["file"]
    assert digest(file) == artifact["sha256"]
    with tarfile.open(file) as stream:
        actual = {item.name: hashlib.sha256(stream.extractfile(item).read()).hexdigest() for item in stream.getmembers() if item.isfile()}
    assert actual == {item["file"]: item["sha256"] for item in artifact["files"]}
    package_files += len(actual)
candidate = root / "candidate"
recover_git(candidate, "https://github.com/Azure/typespec-azure.git", equality["commit"])
for item in equality["exactTaskFilesAndDeletions"]:
    file = candidate / item["file"]
    assert file.exists() == item["exists"]
    if item["exists"]:
        assert digest(file) == item["sha256"]
core_url = command(["git", "-C", candidate, "config", "--file", ".gitmodules", "--get", "submodule.core.url"]).decode().strip()
assert "github.com/microsoft/typespec" in core_url.lower()
recover_git(candidate / "core", core_url, equality["coreCommit"])
for item in provenance["source"]["closure"]:
    relative = item["directory"].replace("\\", "/").split("$NATIVE/", 1)[1]
    assert digest(candidate / relative / "package.json") == item["manifestSha256"]
specs_commit = descriptor["source"]["commit"]
specs_ref = "refs/heads/evidence/long-running-operations-options-validator-20261022-source"
specs_url = "https://github.com/msyyc/azure-rest-api-specs.git"
assert command(["git", "ls-remote", specs_url, specs_ref]).decode().split()[0] == specs_commit
specs = root / "specs-git"
recover_git(specs, specs_url, specs_commit, filtered=True)
source_samples = [
    "specification/common-types/resource-management/v3/types.json",
    "specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/DataMigrationService.tsp",
    "specification/network/resource-manager/Microsoft.Network/Network/Network/SwapResource.tsp",
    "package.json", "pnpm-lock.yaml", "pnpm-workspace.yaml",
]
for relative in source_samples:
    file = specs / relative
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_bytes(command(["git", "-C", specs, "show", f"{specs_commit}:{relative}"]))
bundle = next(item for item in assets["assets"] if item["name"].endswith(".bundle"))
command(["git", "-C", candidate, "bundle", "verify", downloads / bundle["name"]])
tooling = root / "tooling-git"
command(["git", "clone", "--no-checkout", downloads / bundle["name"], tooling])
tooling_commit = "0c0e9f99c2d276f30653991fbb5bfe123e7bac60"
assert command(["git", "-C", tooling, "rev-parse", f"{tooling_commit}^{{commit}}"]).decode().strip() == tooling_commit
baseline_script = root / "shared_baseline.py"
baseline_script.write_bytes(command(["git", "-C", tooling, "show", f"{tooling_commit}:.github/skills/analyze-native-lint-coverage/shared_baseline.py"]))
baseline_asset = assets["baselineSeparate"]
command(["gh", "release", "download", baseline_asset["release"], "--repo", baseline_asset["repository"], "--pattern", baseline_asset["name"], "--dir", downloads])
baseline_archive = downloads / baseline_asset["name"]
assert digest(baseline_archive) == baseline_asset["sha256"]
baseline_result = json.loads(command([sys.executable, "-X", "utf8", "-B", baseline_script, "fetch", "--descriptor", (run / "baseline-descriptor.json").resolve(), "--output", root / "baseline", "--archive", baseline_archive], timeout=3600))
assert baseline_result["baselineIdentity"] == descriptor["baselineIdentity"]
command([sys.executable, run / "replay" / "reanalyze-saved-counts.py", run, logs / "saved-reanalysis.json"])
command([sys.executable, run / "replay" / "render-migration.py", run, logs / "migration-replayed.md"])
assert digest(logs / "migration-replayed.md") == digest(run / "migration.md")
command([args.node, "--test", run / "replay" / "compare-member-operation-units.test.mjs"])
counts = read(logs / "saved-reanalysis.json")
receipt = {
    "status": "passed", "evidenceCommit": command(["git", "-C", evidence, "rev-parse", "HEAD"]).decode().strip(),
    "candidateCommit": equality["commit"], "sourceIdentity": equality["sourceIdentity"],
    "testedWorkingTreeIdentity": equality["testedWorkingTreeIdentity"], "coreCommit": equality["coreCommit"],
    "assetDownloads": [{"name": item["name"], "sha256": item["sha256"], "bytes": item["bytes"], "url": item["url"]} for item in assets["assets"]],
    "packagesVerified": len(provenance["artifacts"]), "packedFilesVerified": package_files,
    "toolingCommit": tooling_commit, "toolingBundleVerified": True,
    "specsSource": {"repository": "msyyc/azure-rest-api-specs", "ref": specs_ref, "commit": specs_commit,
                    "frozenGitCommitFetched": True, "representativeInputsRecovered": source_samples,
                    "fullCheckout": False, "limitation": "Frozen source is retained by Git commit/tree with representative common-types, authored sources and root manifests recovered; no full source checkout, dependency reinstall or fresh compilation is claimed."},
    "baselineIdentity": baseline_result["baselineIdentity"], "baselineArchiveSha256": digest(baseline_archive),
    "baselineFetchVerification": "pinned shared_baseline.py completed full sealed manifest/dataset verification",
    "savedCounts": counts, "reportSha256": digest(run / "migration.md"),
    "comparisonControls": 4, "swaggerGeneration": "not-run", "fullNativeCoverageRerun": False,
    "originalWorktreeOrSessionInputsUsed": False,
    "runtime": {"python": sys.version.split()[0], "node": command([args.node, "--version"]).decode().strip()},
}
(logs / "fresh-recovery.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": "passed", "evidenceCommit": receipt["evidenceCommit"], "candidateCommit": equality["commit"], "packages": len(provenance["artifacts"]), "packedFiles": package_files, "projects": counts["assessed"], "baselineIdentity": receipt["baselineIdentity"]}))

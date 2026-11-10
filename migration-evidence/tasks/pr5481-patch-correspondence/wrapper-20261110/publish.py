"""Publish fresh candidate receipts without modifying historical observations."""

import argparse
import collections
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tarfile


ROOT = Path(__file__).resolve().parent.parent
CANDIDATE = "ade5040b62c25c8cd4eb8a0e99593f5f739c23f2"
PREVIOUS = "0121903975ab45cde7d7aca37cf50ffd7f3855d3"


def load(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def publish(local, out):
    plan = load(local / "plan.json")
    run = local / "coverage-full"
    manifest = load(run / "manifest.json")
    coverage = load(run / "coverage.json")
    recovery = None
    if manifest["status"] != "complete":
        recovery = load(local / "integrity-reconciliation.json")
        assert manifest["status"] == "running"
        assert recovery["status"] == "verified" and recovery["originalExitCode"] == -1
        assert recovery["successfulProjects"] == 487
        assert recovery["failedOrUnassessedProjects"] == 0
        assert recovery["candidateCommit"] == manifest["candidate"]["commit"]
        assert recovery["originalManifestSha256"] == digest(
            (run / "manifest.json").read_bytes()
        )
        assert recovery["originalCoverageSha256"] == digest(
            (run / "coverage.json").read_bytes()
        )
    assert manifest["candidate"]["commit"] == plan["candidateCommit"] == CANDIDATE
    assert manifest["specs"]["commit"] == plan["descriptor"]["source"]["commit"]
    assert not out.exists(), "Use a new publication directory"
    roots = [
        (plan["stagingSupplement"], "<staging-supplement>"),
        (plan["candidate"], "<candidate>"),
        (plan["specs"], "<specs>"),
        (plan["tooling"], "<tooling>"),
        (plan["baseline"], "<shared-baseline>"),
        (str(local.parent.parent), "<evidence>"),
        (str(Path.home()), "<user-profile>"),
    ]

    def sanitize(value):
        if isinstance(value, dict):
            return {key: sanitize(item) for key, item in value.items()}
        if isinstance(value, list):
            return [sanitize(item) for item in value]
        if isinstance(value, str):
            for root, replacement in roots:
                value = value.replace(root, replacement).replace(
                    root.replace("\\", "/"), replacement
                )
            assert not re.search(r"(?<![A-Za-z])[A-Za-z]:[\\/]", value), value[:250]
        return value

    def write(relative, value):
        destination = out / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not isinstance(value, str):
            value = json.dumps(sanitize(value), indent=2, ensure_ascii=True) + "\n"
        destination.write_text(
            value.replace("\r\n", "\n"), encoding="utf-8", newline="\n"
        )

    files = sorted(
        file
        for file in run.glob("native-*.json")
        if re.fullmatch(r"native-\d+\.json", file.name)
    )
    assert len(files) == 487
    receipts = [load(file) for file in files]
    assert all(receipt["status"] == "success" for receipt in receipts)
    assert len({receipt["project"] for receipt in receipts}) == 487
    transformations = []
    for file, receipt in zip(files, receipts):
        receipt["ambientDiagnostics"] = [
            item
            for item in receipt.get("ambientDiagnostics", [])
            if item.get("severity") == "error"
        ]
        receipt["publicationNote"] = (
            "All selected-rule findings, ambient errors, statuses and package receipts "
            "retained. Unrelated ambient warnings omitted; absolute roots replaced."
        )
        relative = Path("runs/full-corpus") / file.name
        write(relative, receipt)
        transformations.append(
            {
                "file": relative.as_posix(),
                "rawSha256": digest(file.read_bytes()),
                "publishedSha256": digest((out / relative).read_bytes()),
            }
        )
    for name in ("manifest.json", "coverage.json"):
        write(Path("runs/full-corpus") / name, load(run / name))
    write("provenance/receipt-transformations.json", transformations)
    write("provenance/plan.json", plan)
    if recovery is not None:
        published_recovery = {
            **recovery,
            "publishedOriginalManifestSha256": digest(
                (out / "runs/full-corpus/manifest.json").read_bytes()
            ),
            "publishedOriginalCoverageSha256": digest(
                (out / "runs/full-corpus/coverage.json").read_bytes()
            ),
        }
        write("provenance/integrity-reconciliation.json", published_recovery)
        for name in (
            "post-exit-dataset-integrity.json",
            "post-exit-source-report-integrity.json",
            "post-exit-source-report-owner.json",
        ):
            write(Path("provenance") / name, load(local / name))
    write("provenance/runtime-overrides.json", load(local / "runtime-overrides.json"))
    write("provenance/corpus-owner-receipt.json", load(local / "corpus-owner-receipt.json"))
    write("controls/injected-controls.json", load(local / "injected-controls.json"))
    for name in (
        "portable-applicable-controls.log",
        "artifact-build.log",
        "azure-pack.log",
        "core-pack.log",
        "coverage-full.command.log",
    ):
        write(
            Path("provenance") / name,
            sanitize((local / name).read_text(encoding="utf-8-sig")).rstrip("\r\n") + "\n",
        )
    artifacts = load(local / "artifact-provenance.json")
    for artifact in artifacts["artifacts"]:
        archive = local / "packages" / artifact["file"]
        assert digest(archive.read_bytes()) == artifact["sha256"]
        with tarfile.open(archive, "r:gz") as reader:
            artifact["files"] = [
                {
                    "file": member.name,
                    "sha256": digest(reader.extractfile(member).read()),
                    "bytes": member.size,
                }
                for member in reader.getmembers()
                if member.isfile()
            ]
            if artifact["file"].startswith(
                "azure-tools-typespec-azure-resource-manager-"
            ):
                for name in (
                    "arm-resource-patch-body.js",
                    "arm-resource-patch-compatibility.js",
                    "arm-resource-patch.js",
                    "model-utils.js",
                ):
                    relative = f"dist/src/rules/{name}"
                    packed = reader.extractfile("package/" + relative).read()
                    assert packed == (
                        Path(plan["candidate"])
                        / "packages/typespec-azure-resource-manager"
                        / relative
                    ).read_bytes()
                    assert packed == (
                        Path(plan["specs"])
                        / "node_modules/@azure-tools/typespec-azure-resource-manager"
                        / relative
                    ).read_bytes()
        destination = out / "artifacts/packages" / artifact["file"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(archive, destination)
    artifacts["selectedRuleBuiltPackedInstalledEquality"] = True
    write("provenance/artifact-provenance.json", artifacts)
    for file in sorted((run / "runtime-installation").iterdir()):
        write(
            Path("provenance/runtime-installation") / file.name,
            sanitize(file.read_text(encoding="utf-8-sig")),
        )
    captures = local / "source-attribution"
    inventory = load(captures / "inventory.json")
    controls = load(local / "attribution-controls/summary.json")
    assert len(inventory["projects"]) == 51
    assert len(controls) == 16 and all(row["status"] == "passed" for row in controls)
    full = {row["project"]: row["rawDiagnostics"] for row in receipts}
    capture_transformations = []

    def write_capture(relative, original):
        value = load(original)
        if "ambientDiagnostics" in value:
            value["ambientDiagnostics"] = [
                row for row in value["ambientDiagnostics"] if row["severity"] == "error"
            ]
        destination = Path("source-attribution") / relative
        write(destination, value)
        capture_transformations.append({
            "path": relative.as_posix(),
            "rawSha256": digest(original.read_bytes()),
            "publishedSha256": digest((out / destination).read_bytes()),
            "bytes": (out / destination).stat().st_size,
        })

    for item in inventory["projects"]:
        source = load(captures / item["source"])
        native = load(captures / item["native"])
        assert native["status"] == "success"
        assert source["project"] == native["project"] == item["project"]
        assert source["rawDiagnostics"] == native["rawDiagnostics"] == full[item["project"]]
        for field in ("source", "native"):
            write_capture(Path(item[field]), captures / item[field])
    for name in ("inventory.json", "observations.json"):
        write_capture(Path(name), captures / name)
    write_capture(Path("owner-receipt.json"), local / "attribution-owner-receipt.json")
    for file in sorted((local / "attribution-controls").glob("*.json")):
        if not file.name.endswith(".input.json"):
            write_capture(Path("controls") / file.name, file)
    for name in ("main.tsp", "tspconfig.yaml"):
        write(
            Path("source-attribution/controls/shared-target") / name,
            (local / "attribution-controls/shared-target" / name).read_text(encoding="utf-8"),
        )
    write(
        "source-attribution/transformations.json",
        {
            "boundary": (
                "Selected findings, targets and counts retained. Unrelated ambient "
                "warnings omitted from receipt copies; absolute roots sanitized. "
                "Suppression probes remain separate from configured warnings."
            ),
            "files": capture_transformations,
        },
    )
    previous_root = ROOT / "refresh-20261105-inherited"
    previous = [
        load(file)
        for file in (previous_root / "runs/full-corpus").glob("native-*.json")
        if re.fullmatch(r"native-\d+\.json", file.name)
    ]
    assert len(previous) == len(receipts)
    old = {receipt["project"]: receipt for receipt in previous}
    assert set(old) == {receipt["project"] for receipt in receipts}
    changes = []
    key = lambda diagnostic: json.dumps(
        diagnostic, sort_keys=True, separators=(",", ":")
    )
    for receipt in sorted(receipts, key=lambda item: item["project"]):
        before = old[receipt["project"]]["rawDiagnostics"]
        after = receipt["rawDiagnostics"]
        old_count = collections.Counter(map(key, before))
        new_count = collections.Counter(map(key, after))
        removed = [
            json.loads(value)
            for value, count in (old_count - new_count).items()
            for _ in range(count)
        ]
        added = [
            json.loads(value)
            for value, count in (new_count - old_count).items()
            for _ in range(count)
        ]
        if removed or added:
            changes.append(
                {
                    "project": receipt["project"],
                    "before": len(before),
                    "after": len(after),
                    "removed": removed,
                    "added": added,
                }
            )
    delta = {
        "previousCandidateCommit": PREVIOUS,
        "candidateCommit": CANDIDATE,
        "beforeFindings": sum(len(item["rawDiagnostics"]) for item in previous),
        "afterFindings": sum(len(item["rawDiagnostics"]) for item in receipts),
        "removedFindings": sum(len(row["removed"]) for row in changes),
        "addedFindings": sum(len(row["added"]) for row in changes),
        "projects": changes,
        "boundary": (
            "Exact source diagnostic record multiset delta on identical frozen specs; "
            "not semantic cross-engine matching."
        ),
    }
    assert (
        delta["beforeFindings"] - delta["removedFindings"] + delta["addedFindings"]
        == delta["afterFindings"]
    )
    write("candidate-delta.json", delta)
    write(
        "project-inventory.json",
        [
            {
                "project": receipt["project"],
                "status": receipt["status"],
                "findings": len(receipt["rawDiagnostics"]),
            }
            for receipt in sorted(receipts, key=lambda item: item["project"])
        ],
    )
    old_artifacts = load(
        previous_root / "provenance/artifact-provenance.json"
    )["artifacts"]
    old_members = {
        (artifact["file"], member["file"]): member["sha256"]
        for artifact in old_artifacts
        for member in artifact["files"]
    }
    new_members = {
        (artifact["file"], member["file"]): member["sha256"]
        for artifact in artifacts["artifacts"]
        for member in artifact["files"]
    }
    write(
        "closure-delta.json",
        {
            "previousCandidateCommit": PREVIOUS,
            "candidateCommit": CANDIDATE,
            "changedMembers": [
                {
                    "archive": identity[0],
                    "file": identity[1],
                    "before": old_members.get(identity),
                    "after": new_members.get(identity),
                }
                for identity in sorted(old_members.keys() | new_members.keys())
                if old_members.get(identity) != new_members.get(identity)
            ],
        },
    )
    write(
        "task.json",
        {
            "task": "pr5481-patch-correspondence-opaque-container",
            "assessment": (
                "Fresh final-candidate TypeSpec execution compared with unchanged "
                "evaluated Swagger staging observations."
            ),
            "candidateCommit": CANDIDATE,
            "coreCommit": plan["coreCommit"],
            "toolingCommit": manifest["generatorCommit"],
            "replayToolingCommit": plan["toolingCommit"],
            "toolingContentIdentity": "../wrapper-20261110/tooling-identity.json",
            "specsCommit": plan["descriptor"]["source"]["commit"],
            "baselineIdentity": plan["descriptor"]["baselineIdentity"],
            "stagingSupplementIdentity": plan["stagingSupplementIdentity"],
            "mapping": plan["mapping"],
            "outcome": {"selectedProjects": 487},
            "startedAt": manifest["startedAt"],
            "finishedAt": (
                manifest["finishedAt"] if recovery is None else recovery["finishedAt"]
            ),
            "nativeExecution": coverage["nativeExecution"],
            "originalCLIExitCode": 0 if recovery is None else recovery["originalExitCode"],
            "completion": (
                "Original CLI completed and sealed its manifest."
                if recovery is None else recovery["completion"]
            ),
            "recoveryBoundary": (
                "Fresh TypeSpec execution and saved-data replay; no Swagger regeneration "
                "or fully transitive locked regeneration claim."
            ),
        },
    )
    comparison = (ROOT / "compare-staging.py").read_text(encoding="utf-8").replace(
        '"assessment": "saved-native-observation reanalysis with fresh Swagger staging evaluation",',
        '"assessment": task.get("assessment", "saved-native-observation reanalysis"),',
    )
    complete_assertion = '    assert native_manifest["status"] == "complete"'
    assert comparison.count(complete_assertion) == 1
    comparison = comparison.replace(
        complete_assertion,
        '    if native_manifest["status"] != "complete":\n'
        '        recovery = load(native_directory.parents[1] / "provenance/integrity-reconciliation.json")\n'
        '        assert native_manifest["status"] == "running"\n'
        '        assert recovery["status"] == "verified" and recovery["originalExitCode"] == -1\n'
        '        assert recovery["successfulProjects"] == 487 and recovery["failedOrUnassessedProjects"] == 0\n'
        '        assert recovery["candidateCommit"] == native_manifest["candidate"]["commit"]\n'
        '        assert recovery["publishedOriginalManifestSha256"] == digest(native_directory / "manifest.json")\n'
        '        assert recovery["publishedOriginalCoverageSha256"] == digest(native_directory / "coverage.json")',
    )
    comparison = comparison.replace(
        "](../gap-investigation.md)", "](../../gap-investigation.md)"
    )
    write("compare-staging.py", comparison)
    subprocess.run(
        [
            sys.executable,
            "-B",
            str(out / "compare-staging.py"),
            str(out / "runs/full-corpus"),
            plan["stagingSupplement"],
            str(out / "staging-comparison"),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
    )
    summary = load(out / "staging-comparison/summary.json")
    assert summary["typeSpecReportedDiagnostics"] == delta["afterFindings"]
    assert summary["swaggerReportedDiagnostics"] == 1314
    assert not summary["failedOrUnassessedProjects"]
    print(json.dumps({key: value for key, value in delta.items() if key != "projects"}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("local", type=Path)
    parser.add_argument(
        "--output", type=Path, default=ROOT / "refresh-20261110-wrapper"
    )
    arguments = parser.parse_args()
    publish(arguments.local.resolve(), arguments.output.resolve())

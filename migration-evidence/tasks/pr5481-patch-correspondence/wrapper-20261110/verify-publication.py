"""Verify the frozen publication tree, runtime receipts and package payloads."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import tarfile
from urllib.parse import unquote


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(root, seal):
    fresh = root / "refresh-20261110-wrapper"
    inventory = fresh / "provenance/publication-inventory.json"
    candidate = "ade5040b62c25c8cd4eb8a0e99593f5f739c23f2"
    files = sorted(
        path for path in root.rglob("*") if path.is_file() and path != inventory
    )
    assert not any(path.is_symlink() for path in root.rglob("*"))
    if seal:
        inventory.write_text(
            json.dumps(
                {
                    "candidateCommit": candidate,
                    "scope": "Complete published task tree; this inventory excluded.",
                    "files": [
                        {
                            "path": path.relative_to(root).as_posix(),
                            "sha256": digest(path),
                            "bytes": path.stat().st_size,
                        }
                        for path in files
                    ],
                },
                indent=2,
            ) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    data = load(inventory)
    assert data["candidateCommit"] == candidate
    assert {path.relative_to(root).as_posix() for path in files} == {
        row["path"] for row in data["files"]
    }
    for row in data["files"]:
        file = root / row["path"]
        assert file.stat().st_size == row["bytes"], row["path"]
        assert digest(file) == row["sha256"], row["path"]
    checked_links = 0
    for name in (
        "migration.md",
        "gap-investigation.md",
        "replay.md",
        "wrapper-20261110/assessment.md",
        "wrapper-20261110/retained-route-contexts.md",
        "refresh-20261110-wrapper/staging-comparison/differences.md",
    ):
        source = root / name
        text = source.read_text(encoding="utf-8")
        for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if re.match(r"[a-z]+://", link):
                continue
            filename, _, fragment = unquote(link).partition("#")
            target = (source.parent / filename).resolve() if filename else source
            assert target.is_file(), (name, link)
            if fragment:
                target_text = target.read_text(encoding="utf-8")
                headings = re.findall(r"^#{1,6}\s+(.+)$", target_text, re.MULTILINE)
                anchors = {
                    re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-")
                    for heading in headings
                }
                anchors.update(
                    re.findall(r'<a\s+(?:id|name)="([^"]+)"', target_text)
                )
                assert fragment in anchors, (name, link)
            checked_links += 1
    provenance = load(fresh / "provenance/artifact-provenance.json")
    plan = load(fresh / "provenance/plan.json")
    task = load(fresh / "task.json")
    manifest = load(fresh / "runs/full-corpus/manifest.json")
    tooling = load(root / "wrapper-20261110/tooling-identity.json")
    assert task["toolingCommit"] == manifest["generatorCommit"]
    assert task["toolingCommit"] == tooling["actualGeneratorCommitAtRunStart"]
    assert task["replayToolingCommit"] == plan["toolingCommit"]
    assert task["replayToolingCommit"] == tooling["plannedReplayCommit"]
    assert plan["candidateCommit"] == candidate
    assert provenance["candidateCommit"] == candidate
    assert provenance["selectedRuleBuiltPackedInstalledEquality"]
    assert len(provenance["artifacts"]) == len(plan["closure"]) == 15
    closure = {item["name"]: item for item in plan["closure"]}
    entrypoints = {}
    member_hashes = {}
    member_count = 0
    for artifact in provenance["artifacts"]:
        archive = fresh / "artifacts/packages" / artifact["file"]
        assert archive.stat().st_size == artifact["bytes"]
        assert digest(archive) == artifact["sha256"]
        with tarfile.open(archive, "r:gz") as packed:
            assert {member.name for member in packed.getmembers() if member.isfile()} == {
                row["file"] for row in artifact["files"]
            }
            for row in artifact["files"]:
                value = packed.extractfile(row["file"]).read()
                assert len(value) == row["bytes"]
                assert hashlib.sha256(value).hexdigest() == row["sha256"]
                member_count += 1
            package = json.loads(packed.extractfile("package/package.json").read())
            previous_archive = (
                root / "refresh-20261105-inherited/artifacts/packages" / artifact["file"]
            )
            with tarfile.open(previous_archive, "r:gz") as previous:
                assert package == json.loads(
                    previous.extractfile("package/package.json").read()
                ), artifact["file"]
            expected = closure[package["name"]]
            assert package["version"] == expected["version"]
            members = {row["file"]: row["sha256"] for row in artifact["files"]}
            entrypoints[package["name"]] = members["package/" + expected["main"]]
            member_hashes[package["name"]] = members
    delta = load(fresh / "closure-delta.json")["changedMembers"]
    assert {
        row["file"] for row in delta
    } == {
        "package/package.json",
        "package/dist/src/rules/arm-resource-patch-body.js",
        "package/dist/src/rules/arm-resource-patch-body.js.map",
        "package/dist/src/rules/arm-resource-patch-body.d.ts.map",
    }
    receipt_count = 0
    warning_count = 0
    package_matches = 0
    for file in sorted((fresh / "runs/full-corpus").glob("native-*.json")):
        receipt = load(file)
        assert receipt["status"] == "success"
        required = {
            "@typespec/compiler",
            "@azure-tools/typespec-azure-resource-manager",
            "@azure-tools/typespec-autorest",
            "@azure-tools/typespec-azure-rulesets",
        }
        matched = set()
        for package in receipt["packages"]:
            if package["name"] in closure:
                expected = closure[package["name"]]
                assert package["version"] == expected["version"]
                assert package["sha256"] == entrypoints[package["name"]]
                matched.add(package["name"])
                package_matches += 1
        assert required <= matched, receipt["project"]
        warning_count += len(receipt["rawDiagnostics"])
        receipt_count += 1
    assert (receipt_count, warning_count) == (487, 108)
    arm = member_hashes["@azure-tools/typespec-azure-resource-manager"]
    extractor = digest(root / "wrapper-20261110/capture-source.mjs")
    original_worker = load(
        root / "refresh-20261105-inherited/source-attribution/source-0.json"
    )["originalWorkerSha256"]
    capture_inventory = load(fresh / "source-attribution/inventory.json")
    assert len(capture_inventory["projects"]) == 51
    for item in capture_inventory["projects"]:
        source = load(fresh / "source-attribution" / item["source"])
        assert source["bodyModuleSha256"] == arm[
            "package/dist/src/rules/arm-resource-patch-body.js"
        ]
        assert source["compatibilityModuleSha256"] == arm[
            "package/dist/src/rules/arm-resource-patch-compatibility.js"
        ]
        assert source["extractorSha256"] == extractor
        assert source["originalWorkerSha256"] == original_worker
    for ledger, field in (
        (fresh / "provenance/receipt-transformations.json", "file"),
        (fresh / "source-attribution/transformations.json", "path"),
    ):
        rows = load(ledger)
        prefix = fresh
        if isinstance(rows, dict):
            rows = rows["files"]
            prefix = fresh / "source-attribution"
        for row in rows:
            assert digest(prefix / row[field]) == row["publishedSha256"]
    print(json.dumps({
        "candidateCommit": candidate,
        "verifiedPublishedFiles": len(data["files"]),
        "verifiedRelativeLinks": checked_links,
        "packageArchives": len(provenance["artifacts"]),
        "verifiedArchiveMembers": member_count,
        "successfulProjects": receipt_count,
        "configuredWarnings": warning_count,
        "verifiedRuntimePackageEntrypoints": package_matches,
        "verifiedSourceCaptures": len(capture_inventory["projects"]),
    }))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("mode", nargs="?", choices=["seal", "check"], default="check")
    arguments = parser.parse_args()
    verify(arguments.root.resolve(), arguments.mode == "seal")

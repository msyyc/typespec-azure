"""Verify the current publication without relabeling historical receipts."""

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
    fresh = root / "refresh-20261112-direct"
    inventory = fresh / "provenance/publication-inventory.json"
    candidate = "f2079b23690d816ecc92a858fab2c1572e9448b5"
    files = sorted(path for path in root.rglob("*") if path.is_file() and path != inventory)
    assert not any(path.is_symlink() for path in root.rglob("*"))
    if seal:
        inventory.write_text(json.dumps({
            "candidateCommit": candidate,
            "scope": "Complete published task tree, including immutable historical evidence; this inventory excluded.",
            "files": [
                {"path": path.relative_to(root).as_posix(), "sha256": digest(path), "bytes": path.stat().st_size}
                for path in files
            ],
        }, indent=2) + "\n", encoding="utf-8", newline="\n")
    data = load(inventory)
    assert data["candidateCommit"] == candidate
    assert {path.relative_to(root).as_posix() for path in files} == {row["path"] for row in data["files"]}
    for row in data["files"]:
        file = root / row["path"]
        assert file.stat().st_size == row["bytes"] and digest(file) == row["sha256"], row["path"]
    links = 0
    for name in ("migration.md", "gap-investigation.md", "replay.md", "direct-20261112/assessment.md", "refresh-20261112-direct/staging-comparison/differences.md"):
        source = root / name
        for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", source.read_text(encoding="utf-8")):
            if re.match(r"[a-z]+://", link):
                continue
            filename, _, fragment = unquote(link).partition("#")
            target = (source.parent / filename).resolve() if filename else source
            assert target.is_file(), (name, link)
            if fragment:
                text = target.read_text(encoding="utf-8")
                headings = re.findall(r"^#{1,6}\s+(.+)$", text, re.MULTILINE)
                anchors = {re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-") for heading in headings}
                anchors.update(re.findall(r'<a\s+(?:id|name)="([^"]+)"', text))
                assert fragment in anchors, (name, link)
            links += 1
    provenance = load(fresh / "provenance/artifact-provenance.json")
    plan = load(fresh / "provenance/plan.json")
    task = load(fresh / "task.json")
    manifest = load(fresh / "runs/full-corpus/manifest.json")
    assert manifest["status"] == "complete"
    assert provenance["candidateCommit"] == task["candidateCommit"] == manifest["candidate"]["commit"] == plan["candidateCommit"] == candidate
    assert task["toolingCommit"] == manifest["generatorCommit"] == plan["toolingCommit"] == "4dda34822b8877d997b6b5ab6525b70e8379ba0d"
    assert task["coreCommit"] == plan["coreCommit"] == "e06f6b34fdad9d7f49bfc084a598b03c60684e9a"
    assert task["specsCommit"] == manifest["specs"]["commit"] == plan["descriptor"]["source"]["commit"] == "2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9"
    assert provenance["selectedRuleBuiltPackedInstalledEquality"]
    assert len(provenance["artifacts"]) == len(plan["closure"]) == 15
    closure = {item["name"]: item for item in plan["closure"]}
    entrypoints, members = {}, {}
    member_count = 0
    for artifact in provenance["artifacts"]:
        archive = fresh / "artifacts/packages" / artifact["file"]
        assert archive.stat().st_size == artifact["bytes"] and digest(archive) == artifact["sha256"]
        with tarfile.open(archive, "r:gz") as packed:
            assert {item.name for item in packed.getmembers() if item.isfile()} == {item["file"] for item in artifact["files"]}
            for item in artifact["files"]:
                value = packed.extractfile(item["file"]).read()
                assert len(value) == item["bytes"] and hashlib.sha256(value).hexdigest() == item["sha256"]
                member_count += 1
            package = json.loads(packed.extractfile("package/package.json").read())
            expected = closure[package["name"]]
            assert package["version"] == expected["version"]
            hashes = {item["file"]: item["sha256"] for item in artifact["files"]}
            entrypoints[package["name"]] = hashes["package/" + expected["main"]]
            members[package["name"]] = hashes
    receipt_count = warning_count = package_matches = 0
    for file in sorted((fresh / "runs/full-corpus").glob("native-*.json")):
        receipt = load(file)
        assert receipt["status"] == "success"
        matched = set()
        for package in receipt["packages"]:
            if package["name"] in closure:
                assert package["version"] == closure[package["name"]]["version"]
                assert package["sha256"] == entrypoints[package["name"]]
                matched.add(package["name"])
                package_matches += 1
        assert {"@typespec/compiler", "@azure-tools/typespec-azure-resource-manager", "@azure-tools/typespec-autorest", "@azure-tools/typespec-azure-rulesets"} <= matched
        warning_count += len(receipt["rawDiagnostics"])
        receipt_count += 1
    assert (receipt_count, warning_count) == (487, 104)
    arm = members["@azure-tools/typespec-azure-resource-manager"]
    captures = load(fresh / "source-attribution/inventory.json")["projects"]
    assert len(captures) == 51
    for item in captures:
        source = load(fresh / "source-attribution" / item["source"])
        assert source["bodyModuleSha256"] == arm["package/dist/src/rules/arm-resource-patch-body.js"]
        assert source["compatibilityModuleSha256"] == arm["package/dist/src/rules/arm-resource-patch-compatibility.js"]
        assert source["extractorSha256"] == digest(root / "direct-20261112/capture-source.mjs")
        assert source["captureBaseSha256"] == digest(root / "wrapper-20261110/capture-source.mjs")
        assert source["originalWorkerSha256"] == "8b912c6cee552c9c89946dbba04c5e03c286d89320175e9f332d595d05234609"
    for ledger, field in ((fresh / "provenance/receipt-transformations.json", "file"), (fresh / "source-attribution/transformations.json", "path")):
        rows = load(ledger)
        prefix = fresh
        if isinstance(rows, dict):
            rows, prefix = rows["files"], fresh / "source-attribution"
        for row in rows:
            assert digest(prefix / row[field]) == row["publishedSha256"]
    controls = load(fresh / "controls/injected-controls.json")
    assert len(controls) == 17 and all(row["receipt"]["status"] == "success" for row in controls)
    for row in controls:
        for package in row["receipt"]["packages"]:
            if package["name"] in closure:
                assert package["version"] == closure[package["name"]]["version"]
                assert package["sha256"] == entrypoints[package["name"]]
    extraction = load(fresh / "source-attribution/controls/summary.json")
    assert len(extraction) == 12 and all(row["status"] == "passed" for row in extraction)
    examples = load(fresh / "controls/documentation-examples.json")
    assert examples["documentSha256"] == "41383a8c11959a8c06b12fa4407657c697e2fe33f19f2909c8fc71c158b6eea0"
    assert {row["name"] for row in examples["receipts"]} == {"incorrect", "correct"}
    for row in examples["receipts"]:
        receipt = row["receipt"]
        assert receipt["status"] == "success"
        assert not any(item["severity"] == "error" for item in receipt["ambientDiagnostics"])
        assert len(receipt["rawDiagnostics"]) == (1 if row["name"] == "incorrect" else 0)
    portable = (fresh / "provenance/portable-applicable-controls.log").read_text(encoding="utf-8")
    assert "37 passed" in portable and "6 skipped" in portable
    print(json.dumps({
        "candidateCommit": candidate, "verifiedPublishedFiles": len(files), "verifiedRelativeLinks": links,
        "packageArchives": 15, "verifiedArchiveMembers": member_count,
        "successfulProjects": receipt_count, "configuredWarnings": warning_count,
        "verifiedRuntimePackageEntrypoints": package_matches, "verifiedSourceCaptures": len(captures),
    }))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("mode", nargs="?", choices=["seal", "check"], default="check")
    args = parser.parse_args()
    verify(args.root.resolve(), args.mode == "seal")

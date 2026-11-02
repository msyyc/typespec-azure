import hashlib
import json
import subprocess
import sys
import tarfile
from pathlib import Path


candidate, artifacts, output = map(Path, sys.argv[1:])


def digest(contents):
    return hashlib.sha256(contents).hexdigest()


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


assert not git(candidate, "status", "--porcelain"), "Candidate must be clean"
assert not git(candidate / "core", "status", "--porcelain"), "Core must be clean"
receipts = []
for archive in sorted(artifacts.glob("*.tgz")):
    with tarfile.open(archive, "r:gz") as packed:
        manifest_bytes = packed.extractfile("package/package.json").read()
        manifest = json.loads(manifest_bytes)
        name = manifest["name"]
        package_root = (
            candidate / "core" / "packages" / name.split("/")[1]
            if name.startswith("@typespec/")
            else candidate / "packages" / name.split("/")[1]
        )
        source_manifest = json.loads((package_root / "package.json").read_text())
        assert manifest["version"] == source_manifest["version"]
        files = []
        for member in packed.getmembers():
            if not member.isfile():
                assert member.isdir(), f"Unexpected nonregular archive member: {member.name}"
                continue
            relative = Path(member.name).relative_to("package")
            assert ".." not in relative.parts
            contents = packed.extractfile(member).read()
            local = package_root / relative
            if str(relative) == "package.json":
                source_kind = "Chronus workspace/catalog dependency rewrite"
            else:
                if not local.is_file() and relative.name in {"LICENSE", "LICENSE.md", "LICENSE.txt"}:
                    local = (candidate / "core" if name.startswith("@typespec/") else candidate) / relative
                assert local.is_file(), f"No candidate file for {name}: {relative}"
                assert local.read_bytes() == contents, f"Packed content mismatch: {name}/{relative}"
                source_kind = local.relative_to(candidate).as_posix()
            assert "lro-declaration" not in member.name, "Removed Core bridge leaked into artifacts"
            files.append({"file": relative.as_posix(), "sha256": digest(contents), "source": source_kind})
        for field in ("dependencies", "peerDependencies", "optionalDependencies"):
            for dependency, version in manifest.get(field, {}).items():
                assert not version.startswith(("workspace:", "catalog:")), (name, dependency, version)
        receipts.append({
            "artifact": archive.name,
            "sha256": digest(archive.read_bytes()),
            "bytes": archive.stat().st_size,
            "name": name,
            "version": manifest["version"],
            "sourceManifestSha256": digest((package_root / "package.json").read_bytes()),
            "packedManifest": manifest,
            "workspaceRuntimeDependencies": sorted({
                dependency
                for field in ("dependencies", "peerDependencies", "optionalDependencies")
                for dependency, version in source_manifest.get(field, {}).items()
                if version.startswith("workspace:")
            }),
            "files": files,
        })

names = {receipt["name"] for receipt in receipts}
assert len(receipts) == len(names) == 17, f"Expected exact 17-package closure, received {sorted(names)}"
for receipt in receipts:
    assert set(receipt["workspaceRuntimeDependencies"]) <= names, receipt["name"]

result = {
    "schemaVersion": 1,
    "candidateCommit": git(candidate, "rev-parse", "HEAD"),
    "coreCommit": git(candidate / "core", "rev-parse", "HEAD"),
    "status": "passed",
    "artifacts": receipts,
    "removedCoreBridge": "absent",
    "provenance": "Every packed ordinary file matches the selected candidate, except recorded Chronus manifest dependency rewriting. Build logs separately establish the source-to-build relationship.",
}
assert not output.exists(), "Never overwrite an audit receipt"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({
    "status": result["status"],
    "packages": len(receipts),
    "files": sum(len(receipt["files"]) for receipt in receipts),
    "candidateCommit": result["candidateCommit"],
}))

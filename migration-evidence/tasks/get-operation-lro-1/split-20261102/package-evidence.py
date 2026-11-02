import hashlib
import json
import sys
import tarfile
from pathlib import Path


root, output = map(Path, sys.argv[1:])
assert not output.exists(), "Never overwrite evidence archives"
manifest = json.loads((root / "coverage-final" / "manifest.json").read_text())
assert manifest["status"] == "complete"
output.mkdir(parents=True)
prefix = "get-operation-lro-split-" + manifest["candidate"]["commit"][:8]
groups = {
    "packages": [
        "artifacts", "package-audit.json", "build-pack.log", "pack.log",
        "pack-core-verified.log", "baseline-descriptor.json", "run-plan.json",
    ],
    "native": [
        str(path.relative_to(root))
        for path in (root / "coverage-final").iterdir()
        if path.name != "dataset"
    ],
    "controls": [
        "split-controls", "portable-controls.json", "documentation-examples.json",
        "preflight-summary.json", "inspection",
    ],
}
assets = []
for group, names in groups.items():
    archive = output / f"{prefix}-{group}.tar.gz"
    with tarfile.open(archive, "w:gz") as packed:
        for name in sorted(names):
            source = root / name
            assert source.exists() and not source.is_symlink()
            if source.is_dir():
                assert not any(path.is_symlink() for path in source.rglob("*"))
            packed.add(source, arcname=name)
    assets.append({
        "name": archive.name,
        "bytes": archive.stat().st_size,
        "sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
        "contents": names,
    })
result = {
    "schemaVersion": 1,
    "candidateCommit": manifest["candidate"]["commit"],
    "releaseRepository": "msyyc/typespec-azure",
    "releaseTag": "lintdiff-get-operation-lro-split-7e6def9b",
    "baselineDataset": "Retained separately by the descriptor-bound shared Swagger baseline asset",
    "assets": assets,
}
(output / "assets.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

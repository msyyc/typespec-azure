"""Freeze or verify explicit evidence byte hashes, including Git blob bytes."""
import hashlib
import json
import pathlib
import subprocess
import sys

root = pathlib.Path(sys.argv[1]).resolve()
mode = sys.argv[2]
inventory = root / "integrity.json"
if mode == "freeze":
    files = [
        {"file": file.relative_to(root).as_posix(), "sha256": hashlib.sha256(file.read_bytes()).hexdigest(), "bytes": file.stat().st_size}
        for file in sorted(root.rglob("*"))
        if file.is_file() and file != inventory
    ]
    inventory.write_text(json.dumps({"algorithm": "SHA-256", "scope": "All task files except this inventory itself", "files": files}, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("Frozen files:", len(files))
else:
    data = json.loads(inventory.read_text(encoding="utf-8"))
    repository = pathlib.Path(subprocess.check_output(["git", "-C", str(root), "rev-parse", "--show-toplevel"], text=True).strip()) if mode == "git" else None
    expected = {item["file"] for item in data["files"]}
    actual = {file.relative_to(root).as_posix() for file in root.rglob("*") if file.is_file() and file != inventory}
    assert actual == expected, {"missing": sorted(expected - actual), "extra": sorted(actual - expected)}
    for item in data["files"]:
        content = (root / item["file"]).read_bytes()
        assert len(content) == item["bytes"], item["file"]
        assert hashlib.sha256(content).hexdigest() == item["sha256"], item["file"]
        if mode == "git":
            git_path = (root / item["file"]).relative_to(repository).as_posix()
            blob = subprocess.check_output(["git", "-C", str(repository), "show", f"HEAD:{git_path}"])
            assert hashlib.sha256(blob).hexdigest() == item["sha256"], ("Git blob mismatch", item["file"])
    print("Verified files:", len(data["files"]), "mode:", mode)

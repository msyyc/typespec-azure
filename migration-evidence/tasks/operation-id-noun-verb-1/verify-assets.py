import argparse
import gzip
import hashlib
import json
import tarfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def read(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def verify_archive(path, expected):
    with tarfile.open(path, "r:gz") as archive:
        members = [
            member for member in archive.getmembers()
            if not (member.name == "." and member.isdir())
        ]
        actual = {member.name.removeprefix("./"): member for member in members}
        assert len(actual) == len(members), "Duplicate archive member"
        assert set(actual) == set(expected), "Archive member inventory mismatch"
        for name, identity in expected.items():
            member = actual[name]
            assert member.isfile(), name
            data = archive.extractfile(member).read()
            assert len(data) == identity["bytes"], name
            assert digest(data) == identity["sha256"], name


parser = argparse.ArgumentParser(description="Verify saved migration assets; no linter execution.")
parser.add_argument("candidate", type=Path)
parser.add_argument("run", type=Path)
parser.add_argument("tooling", type=Path)
parser.add_argument("tooling_inventory", type=Path)
args = parser.parse_args()
preparation = read("publication-preparation.json")
for path, name in [
    (args.candidate, "candidate"),
    (args.run, "run"),
    (args.tooling, "tooling"),
    (args.tooling_inventory, "toolingInventory"),
]:
    expected = preparation["assets"][name]
    data = path.read_bytes()
    assert len(data) == expected["bytes"], name
    assert digest(data) == expected["sha256"], name

candidate = read("candidate-envelope.json")
verify_archive(args.candidate, {member["file"]: member for member in candidate["members"]})
inventory = read("run-asset-inventory.json")
run_expected = {member["file"]: member for member in inventory["members"]}
inventory_bytes = (ROOT / "run-asset-inventory.json").read_bytes()
run_expected["inventory.json"] = {
    "bytes": len(inventory_bytes),
    "sha256": digest(inventory_bytes),
}
verify_archive(args.run, run_expected)
tooling = json.loads(gzip.decompress(args.tooling_inventory.read_bytes()).decode("utf-8"))
verify_archive(args.tooling, {member["file"]: member for member in tooling["members"]})
print(json.dumps({
    "status": "passed",
    "candidatePackages": len(candidate["members"]),
    "runMembers": len(run_expected),
    "toolingMembers": len(tooling["members"]),
    "scope": "Saved archive and every embedded member identity only; not a download, sealed-baseline recovery or linter rerun.",
}))

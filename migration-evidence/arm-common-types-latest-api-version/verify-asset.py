"""Verify an evidence archive and recover only its inventoried regular files."""

import argparse
import hashlib
import json
import tarfile
from pathlib import Path, PurePosixPath


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("proposal", type=Path)
    parser.add_argument("inventory", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    proposal = json.loads(args.proposal.read_text(encoding="utf-8"))
    inventory = json.loads(args.inventory.read_text(encoding="utf-8"))["files"]
    expected = {item["file"]: item for item in inventory}
    assert len(expected) == len(inventory), "Duplicate inventory member"
    assert args.archive.stat().st_size == proposal["bytes"], "Archive size mismatch"
    digest = hashlib.sha256(args.archive.read_bytes()).hexdigest()
    assert digest == proposal["sha256"], "Archive SHA-256 mismatch"
    contents = {}
    with tarfile.open(args.archive, "r:gz") as archive:
        for member in archive:
            path = PurePosixPath(member.name)
            assert (
                member.isreg()
                and not path.is_absolute()
                and ".." not in path.parts
                and "\\" not in member.name
                and ":" not in path.parts[0]
                and path.as_posix() == member.name
            ), "Unsafe archive member"
            assert member.name in expected, "Unexpected archive member"
            assert member.name not in contents, "Duplicate archive member"
            data = archive.extractfile(member).read()
            item = expected[member.name]
            assert len(data) == member.size == item["bytes"], "Member size mismatch"
            assert hashlib.sha256(data).hexdigest() == item["sha256"], "Member SHA-256 mismatch"
            contents[member.name] = data
    assert set(contents) == set(expected), "Missing archive member"
    args.output.mkdir(parents=True, exist_ok=False)
    for name, data in contents.items():
        target = args.output.joinpath(*PurePosixPath(name).parts)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    print(json.dumps({
        "status": "verified",
        "archiveSha256": digest,
        "files": len(contents),
        "payloadBytes": sum(map(len, contents.values())),
    }, indent=2))


if __name__ == "__main__":
    main()

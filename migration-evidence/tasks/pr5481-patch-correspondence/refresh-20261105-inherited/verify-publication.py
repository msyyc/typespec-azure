import hashlib
import json
import re
import sys
import tarfile
from pathlib import Path
from urllib.parse import unquote

root = Path(sys.argv[1]).resolve()
fresh = root / "refresh-20261105-inherited"
inventory = fresh / "provenance/publication-inventory.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


if len(sys.argv) > 2 and sys.argv[2] == "seal":
    files = sorted(path for path in root.rglob("*") if path.is_file() and path != inventory)
    inventory.write_text(
        json.dumps(
            {
                "candidateCommit": "0121903975ab45cde7d7aca37cf50ffd7f3855d3",
                "finalHead": "0121903975ab45cde7d7aca37cf50ffd7f3855d3",
                "scope": "Complete published task tree; this inventory excluded",
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

data = json.loads(inventory.read_text(encoding="utf-8"))
for row in data["files"]:
    path = root.joinpath(*row["path"].split("/"))
    assert path.is_file(), row["path"]
    assert path.stat().st_size == row["bytes"], row["path"]
    assert digest(path) == row["sha256"], row["path"]
actual = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file() and p != inventory}
assert actual == {row["path"] for row in data["files"]}

checked = 0
for name in (
    "migration.md", "gap-investigation.md", "replay.md", "inherited-20261105/retained-route-contexts.md", "simplification.md",
    "fix-results.md", "fix-validation.md", "corpus-examples.md",
    "semantic-evidence.md", "evidence-details.md",
    "refresh-20261105-inherited/staging-comparison/differences.md",
):
    source = root / name
    for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", source.read_text(encoding="utf-8")):
        if re.match(r"[a-z]+://", link):
            continue
        filename, _, fragment = unquote(link).partition("#")
        target = (source.parent / filename).resolve() if filename else source
        assert target.is_file(), (name, link)
        if fragment:
            headings = re.findall(r"^#{1,6}\s+(.+)$", target.read_text(encoding="utf-8"), re.MULTILINE)
            anchors = {re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-") for heading in headings}
            anchors.update(re.findall(r'<a\s+(?:id|name)="([^"]+)"', target.read_text(encoding="utf-8")))
            assert fragment in anchors, (name, link)
        checked += 1

provenance = json.loads((fresh / "provenance/artifact-provenance.json").read_text(encoding="utf-8"))
archives = list((fresh / "artifacts/packages").glob("*.tgz"))
assert len(archives) == len(provenance["artifacts"]) == 15
members = 0
for artifact in provenance["artifacts"]:
    archive = fresh / "artifacts/packages" / artifact["file"]
    assert archive.stat().st_size == artifact["bytes"]
    assert digest(archive) == artifact["sha256"]
    with tarfile.open(archive, "r:gz") as packed:
        for row in artifact["files"]:
            value = packed.extractfile(row["file"]).read()
            assert len(value) == row["bytes"], row["file"]
            assert hashlib.sha256(value).hexdigest() == row["sha256"], row["file"]
            members += 1

print(json.dumps({
    "candidateCommit": data["candidateCommit"],
    "finalHead": data["finalHead"],
    "verifiedPublishedFiles": len(data["files"]),
    "verifiedRelativeLinks": checked,
    "packageArchives": len(archives),
    "verifiedArchiveMembers": members,
}))

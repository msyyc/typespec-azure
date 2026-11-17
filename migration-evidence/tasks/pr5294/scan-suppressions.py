"""Inventory authored suppression directives, not suppressed diagnostics."""

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_SPECS = "2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9"
PATTERN = re.compile(
    r'#suppress\s+"@azure-tools/typespec-azure-resource-manager/'
    r'(arm-resource-patch|no-unsafe-patch-body-properties)"'
)


def git(specs, *args):
    return subprocess.check_output(["git", "-C", str(specs), *args])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("specs", type=Path, help="Frozen specs checkout")
    specs = parser.parse_args().specs.resolve(strict=True)
    assert git(specs, "rev-parse", "HEAD").decode().strip() == EXPECTED_SPECS
    assert not git(specs, "status", "--porcelain", "--", "specification")
    population = json.loads(
        (ROOT / "runs" / "20261030-94b316787" / "population.json").read_text(
            encoding="utf-8"
        )
    )
    projects = sorted((p["sourcePath"] for p in population), key=len, reverse=True)
    tracked = git(specs, "ls-files", "-z", "--", "specification").decode("utf-8").split("\0")
    entries = []
    for path in tracked:
        if not path.endswith(".tsp"):
            continue
        project = next((p for p in projects if path.startswith(p + "/")), None)
        if project is None:
            continue
        contents = specs.joinpath(*path.split("/")).read_bytes()
        digest = hashlib.sha256(contents).hexdigest()
        for line, text in enumerate(contents.decode("utf-8").splitlines(), start=1):
            for match in PATTERN.finditer(text):
                entries.append(
                    {
                        "project": project,
                        "sourceFile": path,
                        "line": line,
                        "rule": match.group(1),
                        "sourceFileSha256": digest,
                    }
                )
    arm = [e for e in entries if e["rule"] == "arm-resource-patch"]
    target = [e for e in entries if e["rule"] == "no-unsafe-patch-body-properties"]
    assert len(arm) == 47 and len({e["sourceFile"] for e in arm}) == 44
    assert len({e["project"] for e in arm}) == 22 and not target
    result = {
        "schemaVersion": 1,
        "specsCommit": EXPECTED_SPECS,
        "scope": "tracked .tsp files physically under the 487 selected project roots",
        "limitation": "A directive is not a captured diagnostic; imports outside these roots are not assessed.",
        "armResourcePatchDirectiveCount": len(arm),
        "armResourcePatchFileCount": len({e["sourceFile"] for e in arm}),
        "armResourcePatchProjectCount": len({e["project"] for e in arm}),
        "targetRuleDirectiveCount": len(target),
        "directives": entries,
    }
    (ROOT / "suppression-inventory.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n"
    )
    print(
        f"arm-resource-patch: {len(arm)} directives, "
        f"{result['armResourcePatchFileCount']} files, "
        f"{result['armResourcePatchProjectCount']} projects; "
        f"target-rule directives: {len(target)}"
    )


if __name__ == "__main__":
    main()

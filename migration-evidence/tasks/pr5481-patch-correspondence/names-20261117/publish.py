"""Publish the name-only candidate without rewriting historical receipts."""

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CANDIDATE = "fb7029f43ef7feaf88a8885070f4775d82e42fff"


def main(local):
    original = ROOT / "wrapper-20261110/publish.py"
    source = original.read_text(encoding="utf-8")
    replacements = {
        'CANDIDATE = "ade5040b62c25c8cd4eb8a0e99593f5f739c23f2"':
            f'CANDIDATE = "{CANDIDATE}"',
        'PREVIOUS = "0121903975ab45cde7d7aca37cf50ffd7f3855d3"':
            'PREVIOUS = "f2079b23690d816ecc92a858fab2c1572e9448b5"',
        'assert len(controls) == 16 and': 'assert len(controls) == 12 and',
        'previous_root = ROOT / "refresh-20261105-inherited"':
            'write("controls/documentation-examples.json", load(local / "documentation/summary.json"))\n'
            '    ci = load(local / "ci-build-checks.json")\n'
            '    assert ci["head"] == CANDIDATE and len(ci["builds"]) == 6\n'
            '    assert all(row["status"] == "completed" and row["conclusion"] == "success" and row["head_sha"] == CANDIDATE for row in ci["builds"])\n'
            '    write("provenance/ci-build-checks.json", ci)\n'
            '    previous_root = ROOT / "refresh-20261112-direct"',
        '"task": "pr5481-patch-correspondence-opaque-container",':
            '"task": "pr5481-writable-property-name-correspondence",',
        '"toolingContentIdentity": "../wrapper-20261110/tooling-identity.json",':
            '"toolingContentIdentity": "runs/full-corpus/manifest.json",',
        '        "portable-applicable-controls.log",':
            '        "preflight-install.log",\n'
            '        "injected-controls.log",\n'
            '        "portable-applicable-controls.log",',
        '    write("provenance/plan.json", plan)':
            '''    write("provenance/plan.json", plan)
    write("provenance/build-commands.json", {
        "candidateCommit": CANDIDATE,
        "artifactDirectory": "<evidence>/.lintdiff-local/pr5481-20261117-names/packages",
        "build": {"cwd": "<candidate>", "argv": [
            "mise", "exec", "--", "pnpm", "-r",
            "--filter", "@azure-tools/typespec-autorest...",
            "--filter", "@azure-tools/typespec-azure-rulesets...",
            "--filter", "@typespec/integration-tester...", "build",
        ]},
        "azurePack": {"cwd": "<candidate>", "argv": [
            "mise", "exec", "--", "pnpm", "exec", "chronus", "pack",
            "--pack-destination", "<artifactDirectory>",
            *["--only=" + name for name in plan["azurePackOnly"]],
        ]},
        "corePack": {"cwd": "<candidate>/core", "argv": [
            "mise", "exec", "--", "pnpm", "exec", "chronus", "pack",
            "--pack-destination", "<artifactDirectory>",
            *["--only=" + name for name in plan["corePackOnly"]],
        ]},
        "preconditions": "Clean exact candidate and core; deleted compatibility helper absent from dist; installed candidate pnpm11.10.0 via mise.",
        "sourceToPayload": "Artifact build log plus built/packed/installed selected-rule equality; all15archives retained.",
    })''',
        '                    "arm-resource-patch-compatibility.js",\n': "",
        '''    for name in ("main.tsp", "tspconfig.yaml"):
        write(
            Path("source-attribution/controls/shared-target") / name,
            (local / "attribution-controls/shared-target" / name).read_text(encoding="utf-8"),
        )
''': "",
    }
    for before, after in replacements.items():
        assert source.count(before) == 1, before
        source = source.replace(before, after)
    namespace = {"__file__": str(original), "__name__": "name_only_receipt_publisher"}
    exec(compile(source, str(original), "exec"), namespace)
    namespace["publish"](local.resolve(), ROOT / "refresh-20261117-names")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("local", type=Path)
    main(parser.parse_args().local)

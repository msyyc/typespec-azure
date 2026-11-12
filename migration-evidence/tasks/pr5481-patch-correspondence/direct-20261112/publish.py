"""Publish the direct-constraint candidate using the existing receipt publisher."""

import argparse
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def main(local):
    original = ROOT / "wrapper-20261110/publish.py"
    source = original.read_text(encoding="utf-8")
    replacements = {
        'CANDIDATE = "ade5040b62c25c8cd4eb8a0e99593f5f739c23f2"':
            'CANDIDATE = "f2079b23690d816ecc92a858fab2c1572e9448b5"',
        'PREVIOUS = "0121903975ab45cde7d7aca37cf50ffd7f3855d3"':
            'PREVIOUS = "ade5040b62c25c8cd4eb8a0e99593f5f739c23f2"',
        'assert len(controls) == 16 and': 'assert len(controls) == 12 and',
        'previous_root = ROOT / "refresh-20261105-inherited"':
            'write("controls/documentation-examples.json", load(local / "documentation/summary.json"))\n'
            '    previous_root = ROOT / "refresh-20261110-wrapper"',
        '"task": "pr5481-patch-correspondence-opaque-container",':
            '"task": "pr5481-patch-correspondence-direct-constraints",',
        '"toolingContentIdentity": "../wrapper-20261110/tooling-identity.json",':
            '"toolingContentIdentity": "runs/full-corpus/manifest.json",',
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
    namespace = {"__file__": str(original), "__name__": "direct_receipt_publisher"}
    exec(compile(source, str(original), "exec"), namespace)
    namespace["publish"](local.resolve(), ROOT / "refresh-20261112-direct")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("local", type=Path)
    main(parser.parse_args().local)

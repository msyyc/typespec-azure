"""Verify the current name-only publication using the existing complete verifier."""

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def main(root, mode):
    original = ROOT / "direct-20261112/verify-publication.py"
    source = original.read_text(encoding="utf-8")
    replacements = {
        "refresh-20261112-direct": "refresh-20261117-names",
        "f2079b23690d816ecc92a858fab2c1572e9448b5": "fb7029f43ef7feaf88a8885070f4775d82e42fff",
        "4dda34822b8877d997b6b5ab6525b70e8379ba0d": "688486d1e9a1701c34fc912c01705d098625c2a3",
        "direct-20261112/assessment.md": "names-20261117/assessment.md",
        "direct-20261112/capture-source.mjs": "names-20261117/capture-source.mjs",
        "(487, 104)": "(487, 85)",
        '        assert source["compatibilityModuleSha256"] == arm["package/dist/src/rules/arm-resource-patch-compatibility.js"]':
            '        assert source["comparisonPolicy"] == "name-and-body-only; value compatibility not evaluated"\n'
            '        assert "compatibilityModuleSha256" not in source',
        "41383a8c11959a8c06b12fa4407657c697e2fe33f19f2909c8fc71c158b6eea0":
            "a83bb3306702bd730774cb4a8ca5580ca83cd919d1a2d32130bbfa696f05196d",
        '    arm = members["@azure-tools/typespec-azure-resource-manager"]':
            '    arm = members["@azure-tools/typespec-azure-resource-manager"]\n'
            '    assert not any("arm-resource-patch-compatibility" in member for member in arm)',
    }
    for before, after in replacements.items():
        assert source.count(before) >= 1, before
        source = source.replace(before, after)
    namespace = {"__file__": str(original), "__name__": "names_publication_verifier"}
    exec(compile(source, str(original), "exec"), namespace)
    namespace["verify"](root.resolve(), mode == "seal")
    current = root / "refresh-20261117-names"
    previous = json.loads((root / "refresh-20261112-direct/provenance/artifact-provenance.json").read_text(encoding="utf-8"))
    fresh = json.loads((current / "provenance/artifact-provenance.json").read_text(encoding="utf-8"))
    def arm_members(provenance):
        artifact = next(item for item in provenance["artifacts"] if item["file"].startswith("azure-tools-typespec-azure-resource-manager-"))
        return {member["file"]: member["sha256"] for member in artifact["files"]}
    old_arm, new_arm = arm_members(previous), arm_members(fresh)
    for member in ("arm-resource-patch.js", "use-model-request-body.js", "model-utils.js"):
        assert old_arm[f"package/dist/src/rules/{member}"] == new_arm[f"package/dist/src/rules/{member}"], member
    ci = json.loads((current / "provenance/ci-build-checks.json").read_text(encoding="utf-8"))
    assert ci["head"] == fresh["candidateCommit"] and len(ci["builds"]) == 6
    assert len({row["name"] for row in ci["builds"]}) == 6
    assert all(row["status"] == "completed" and row["conclusion"] == "success" and row["head_sha"] == ci["head"] for row in ci["builds"])
    controls = json.loads((current / "controls/injected-controls.json").read_text(encoding="utf-8"))
    by_name = {item["case"]: item for item in controls}
    for name in ("omitted-string-limit", "omitted-item-limit", "omitted-numeric-limit", "omitted-format"):
        assert by_name[name]["receipt"]["rawDiagnostics"] == [], name
    suppressed = by_name["suppressed-missing-name"]
    assert '#suppress "@azure-tools/typespec-azure-resource-manager/arm-resource-patch"' in suppressed["source"]
    assert "extra?: string;" in suppressed["source"] and suppressed["receipt"]["rawDiagnostics"] == []


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("mode", nargs="?", choices=["seal", "check"], default="check")
    arguments = parser.parse_args()
    main(arguments.root, arguments.mode)

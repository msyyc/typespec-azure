import argparse
import collections
import hashlib
import json
import pathlib
import re


def read(file):
    return json.loads(file.read_text(encoding="utf-8-sig"))


def validate(package, expected):
    artifact = expected[package["name"]]
    marker = f"/node_modules/{package['name']}/"
    parts = package["entrypoint"].replace("\\", "/").rsplit(marker, 1)
    if len(parts) != 2 or package["version"] != artifact["version"]:
        raise ValueError(f"Unexpected package/version/entrypoint: {package['name']}")
    payload = {item["path"]: item["sha256"] for item in artifact["payload"]}
    if parts[1] not in payload or package.get("sha256") != payload[parts[1]]:
        raise ValueError(f"Entrypoint does not match candidate payload: {package['name']}")
    return package["name"], package["version"], parts[1], package["sha256"]


def main(args):
    assert not args.output.exists(), "Do not replace an audit receipt."
    candidate = read(args.task / "candidate.json")
    assert hashlib.sha256(args.proof.read_bytes()).hexdigest() == candidate["artifactPayloadProof"]["sha256"]
    proof = read(args.proof)
    expected = {item["name"]: item for item in proof["artifacts"]}
    assert len(expected) == 15
    files = []
    if args.run:
        manifest = read(args.run / "manifest.json")
        coverage = read(args.run / "coverage.json")
        assert manifest["status"] == "complete"
        assert coverage["selectedProjectCount"] == coverage["assessableProjectCount"] == 490
        assert coverage["unassessedProjects"] == []
        native = sorted(file for file in args.run.glob("native-*.json") if re.fullmatch(r"native-\d+\.json", file.name))
        assert len(native) == 490
        files.extend(("full490", file) for file in native)
    else:
        assert args.controls_only, "Final audit requires the complete native run."
    if args.fixtures:
        fixtures = sorted(args.fixtures.glob("*/output.json"))
        assert len(fixtures) == 12
        files.extend(("selected-fixture", file) for file in fixtures)
    for directory in args.captures:
        files.extend(("semantic-capture", file) for file in sorted(directory.glob("*.json")) if file.stem.isdigit())
    verified = collections.Counter()
    external = collections.Counter()
    receipts = collections.Counter()
    sample = None
    for role, file in files:
        receipt = read(file)
        assert receipt["status"] == "success", file
        names = {package["name"] for package in receipt["packages"]}
        assert {"@typespec/compiler", "@azure-tools/typespec-azure-resource-manager"} <= names, file
        for package in receipt["packages"]:
            if package["name"] in expected:
                verified[validate(package, expected)] += 1
                sample = package
            else:
                external[(package["name"], package.get("version"), package.get("sha256"))] += 1
        receipts[role] += 1
    assert sample is not None
    validate(sample, expected)
    try:
        validate({**sample, "sha256": "0" * 64}, expected)
    except ValueError:
        pass
    else:
        raise AssertionError("Corrupt entrypoint hash was accepted.")
    result = {
        "status": "passed",
        "scope": "Full490 recorded package receipts plus named inspected controls/captures." if args.run else "Focused existing controls/captures only; full490 audit remains pending.",
        "receiptCounts": dict(receipts),
        "verifiedEntrypoints": [
            {"name": key[0], "version": key[1], "payloadPath": key[2], "sha256": key[3], "observations": count}
            for key, count in sorted(verified.items())
        ],
        "externalMetadataNotComparedToCandidateArtifacts": [
            {"name": key[0], "version": key[1], "sha256": key[2], "observations": count}
            for key, count in sorted(external.items())
        ],
        "controls": {"matchingRecordedPayloadAccepted": True, "corruptRecordedHashRejected": True},
        "boundary": "Checks recorded entrypoint bytes against supplied artifact payloads. Does not claim all15 packages executed, full transitive freezing, all installed files rehashed, or Swagger validator execution.",
        "publication": "not-attempted",
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", required=True, type=pathlib.Path)
    parser.add_argument("--proof", required=True, type=pathlib.Path)
    parser.add_argument("--run", type=pathlib.Path)
    parser.add_argument("--controls-only", action="store_true")
    parser.add_argument("--fixtures", type=pathlib.Path)
    parser.add_argument("--captures", nargs="*", default=[], type=pathlib.Path)
    parser.add_argument("--output", required=True, type=pathlib.Path)
    main(parser.parse_args())

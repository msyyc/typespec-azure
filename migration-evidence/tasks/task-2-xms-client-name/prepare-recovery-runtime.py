"""Prepare exact-version lightweight control dependencies from published evidence."""

import argparse
import json
import pathlib
import tarfile

parser = argparse.ArgumentParser()
parser.add_argument("--artifacts", type=pathlib.Path, required=True)
parser.add_argument("--runtime", type=pathlib.Path, required=True)
args = parser.parse_args()
evidence = pathlib.Path(__file__).resolve().parent
closure = json.loads((evidence / "recovery-runtime-closure.json").read_text(encoding="utf-8"))
candidate_names = {key.rsplit("@", 1)[0] for key in closure["roots"]}
candidate_refs = {}
for archive in args.artifacts.glob("*.tgz"):
    with tarfile.open(archive) as bundle:
        manifest = json.load(bundle.extractfile("package/package.json"))
    if manifest["name"] in candidate_names:
        candidate_refs[manifest["name"]] = "file:" + str(archive.resolve())
assert set(candidate_refs) == candidate_names
versions = {}
for package in closure["packages"]:
    versions.setdefault(package["name"], []).append(package["version"])
dependencies = {name: values[0] for name, values in versions.items()}
dependencies.update(candidate_refs)
overrides = {name: values[0] for name, values in versions.items() if len(values) == 1}
overrides.update(candidate_refs)
for package in closure["packages"]:
    for name, edge in package["dependencies"].items():
        if "resolved" not in edge or name in candidate_names:
            continue
        overrides[f'{package["name"]}@{package["version"]}>{name}'] = edge["resolved"].rsplit("@", 1)[1]
args.runtime.mkdir(parents=True, exist_ok=False)
manifest = {
    "name": "task-2-xms-client-name-recovery-controls",
    "private": True,
    "packageManager": "pnpm@12.6.0",
    "dependencies": dependencies,
}
workspace = {"packages": [], "autoInstallPeers": False, "overrides": overrides}
for name, value in [("package.json", manifest), ("pnpm-workspace.yaml", workspace)]:
    (args.runtime / name).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({"runtime": str(args.runtime.resolve()), "candidatePackages": len(candidate_refs), "recordedPackages": len(closure["packages"])}))

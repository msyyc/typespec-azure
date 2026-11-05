"""Instrument the pinned coverage worker without changing diagnostics or source."""

import argparse
import concurrent.futures
import datetime
import json
import pathlib
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument("--root", type=pathlib.Path, required=True)
parser.add_argument("--tooling", type=pathlib.Path, required=True)
parser.add_argument("--output", type=pathlib.Path, required=True)
parser.add_argument("--inspector", type=pathlib.Path, required=True)
parser.add_argument("--native-run", type=pathlib.Path, required=True)
parser.add_argument("--node", type=pathlib.Path, required=True)
parser.add_argument("--pilot", action="store_true")
parser.add_argument("--projects", type=pathlib.Path)
args = parser.parse_args()
assert args.node.is_file() and args.node.is_absolute()
args.output.mkdir(parents=True, exist_ok=True)
worker_path = args.tooling / "packages/typespec-lintdiff/test/harness/native-coverage-worker.mjs"
worker_text = worker_path.read_text(encoding="utf-8")
marker = "  const location = (target) => {"
assert worker_text.count(marker) == 1
insertion = """
  const { inspectInstances } = await import(pathToFileURL(input.inspector).href);
  await inspectInstances({ program, compiler, load, project, projectDir, requireFromSpecs, outputFile });
"""
worker = args.output / "instance-worker.mjs"
worker.write_text(worker_text.replace(marker, insertion + marker), encoding="utf-8", newline="\n")
observations = json.loads((args.root / "observations.json").read_text(encoding="utf-8"))
projects = {row["project"] for m in observations["members"] for row in m["observations"]}
projects.update(row["project"] for row in observations["native"] if row["diagnostics"])
if args.projects:
    selected = set(json.loads(args.projects.read_text(encoding="utf-8")))
    assert selected and selected <= projects, "Selection must be within saved affected projects"
    projects = selected
native_run = args.native_run
inputs = []
for file in sorted(native_run.glob("native-*.input.json")):
    data = json.loads(file.read_text(encoding="utf-8"))
    if data["project"]["sourcePath"] in projects:
        data["inspector"] = str(args.inspector)
        destination = args.output / file.name
        destination.write_text(json.dumps(data), encoding="utf-8", newline="\n")
        inputs.append(destination)
assert len(inputs) == len(projects), (len(inputs), len(projects))
if args.pilot:
    inputs = [file for file in inputs if file.name == "native-11.input.json"]


def inspect(file):
    output = args.output / file.name.replace(".input.json", ".json")
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = subprocess.run(
        [str(args.node), str(worker), str(file), str(output)],
        cwd=args.tooling,
        capture_output=True,
        timeout=360,
    )
    output.with_suffix(".log").write_bytes(result.stdout + result.stderr)
    if result.returncode:
        raise RuntimeError(f"{file.name}: {result.stderr.decode(errors='replace')[-2500:]}")
    receipt = json.loads(output.read_text(encoding="utf-8"))
    assert receipt["status"] == "success", receipt
    saved = next(x for x in observations["native"] if x["project"] == receipt["project"])
    assert receipt["diagnostics"] == saved["diagnostics"], receipt["project"]
    trace = json.loads(pathlib.Path(str(output) + ".instances.json").read_text(encoding="utf-8"))
    assert [
        {k: v for k, v in d.items() if k not in ("operationKey", "targetKind")}
        for d in trace["findings"]
    ] == saved["diagnostics"], receipt["project"]
    summary = {
        "project": receipt["project"],
        "startedAt": started,
        "finishedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "findings": len(trace["findings"]),
        "sourceOperations": len(trace["sourceOperations"]),
        "selectedOperations": len(trace["selectedOperations"]),
        "savedDiagnosticEquality": True,
    }
    print(json.dumps(summary), flush=True)
    return summary


with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    summaries = list(pool.map(inspect, inputs))
(args.output / "inspection-summary.json").write_text(
    json.dumps(summaries, indent=2) + "\n", encoding="utf-8", newline="\n"
)

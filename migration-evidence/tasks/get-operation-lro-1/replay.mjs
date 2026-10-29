import assert from "node:assert/strict";
import * as fs from "node:fs";
import * as path from "node:path";
import render from "./render-report.mjs";
const [input, output] = process.argv.slice(2);
if (!input || !output) throw new Error("Usage: node replay.mjs EVIDENCE_ROOT NEW_OUTPUT_DIRECTORY");
const root = path.resolve(input),
  destination = path.resolve(output);
assert(!fs.existsSync(destination), "Never overwrite a prior replay");
const read = (name) => JSON.parse(fs.readFileSync(path.join(root, name), "utf8"));
const observations = read("observations.json"),
  task = read("task.json"),
  gaps = read("proof/gap-correspondence.json");
const validatorCounts = new Map();
for (const item of observations.validator)
  validatorCounts.set(item.project, (validatorCounts.get(item.project) ?? 0) + 1);
let validatorRawCount = 0,
  nativeRawCount = 0,
  nativeAlignedCount = 0,
  rawValidatorExcess = 0,
  rawNativeExcess = 0;
const projects = observations.native.map((item) => {
  assert.equal(item.status, "success");
  const validator = validatorCounts.get(item.project) ?? 0,
    native = item.diagnostics.length;
  validatorRawCount += validator;
  nativeRawCount += item.rawDiagnostics.length;
  nativeAlignedCount += native;
  rawValidatorExcess += Math.max(validator - native, 0);
  rawNativeExcess += Math.max(native - validator, 0);
  return { project: item.project, validator, native };
});
assert.equal(projects.length, 487);
assert.equal(new Set(projects.map((item) => item.project)).size, 487);
const counts = {
  selectedProjectCount: projects.length,
  assessableProjectCount: projects.length,
  validatorRawCount,
  nativeRawCount,
  nativeAlignedCount,
  rawValidatorExcess,
  rawNativeExcess,
};
const context = {
  ...task,
  counts,
  matched: gaps.correspondences.filter((item) => item.matched).length,
  mapped: new Set(
    gaps.correspondences.flatMap((item) =>
      item.native.map((n) => JSON.stringify([n.project, n.sourceFile, n.line, n.column])),
    ),
  ).size,
  validatorProjects: projects.filter((item) => item.validator).length,
  nativeProjects: projects.filter((item) => item.native).length,
};
fs.mkdirSync(destination, { recursive: true });
fs.writeFileSync(path.join(destination, "migration.md"), render(context));
fs.writeFileSync(
  path.join(destination, "replay-summary.json"),
  JSON.stringify(
    {
      counts,
      projects,
      limitation:
        "Saved-observation count/report reanalysis only; not fresh native execution or independent recovery.",
    },
    null,
    2,
  ) + "\n",
);
process.stdout.write(JSON.stringify(counts) + "\n");

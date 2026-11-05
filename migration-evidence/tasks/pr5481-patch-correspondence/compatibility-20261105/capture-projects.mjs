import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const [specsRepo, toolingRepo, output, fullRun] = process.argv
  .slice(2)
  .map((value) => path.resolve(value));
assert(!fs.existsSync(output), "Use a fresh extraction directory");
fs.mkdirSync(output, { recursive: true });
const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.dirname(here);
const read = (file) => JSON.parse(fs.readFileSync(file, "utf8"));
const fullReceipts = new Map(
  fs
    .readdirSync(fullRun)
    .filter((file) => /^native-\d+\.json$/.test(file))
    .map((file) => {
      const receipt = read(path.join(fullRun, file));
      assert.equal(receipt.status, "success");
      return [
        receipt.project,
        {
          receipt,
          input: read(path.join(fullRun, file.replace(".json", ".input.json"))),
        },
      ];
    }),
);
assert.equal(fullReceipts.size, 487);
const diagnosticMultiset = (diagnostics) =>
  diagnostics
    .map((diagnostic) =>
      JSON.stringify(
        Object.fromEntries(Object.entries(diagnostic).sort(([a], [b]) => a.localeCompare(b))),
      ),
    )
    .sort();
const assessment = read(path.join(root, "assessment-20261105", "results.json"));
const replay = read(path.join(root, "staging-comparison", "schema-investigation.json"));
const selected = new Map();
for (const project of assessment.projects) {
  for (const record of project.swaggerAssessments.filter(
    (record) => record.retainedAfterMetadataAssessment,
  )) {
    const operation =
      replay.inputs[record.replayInputIndex].operations[record.replayOperationIndex];
    const routes = selected.get(project.project) ?? new Set();
    routes.add(operation.path[1]);
    selected.set(project.project, routes);
  }
}
const started = Date.now();
const inventory = [];
for (const [project, routes] of [...selected].sort(([a], [b]) => a.localeCompare(b))) {
  assert(Date.now() - started < 900_000, "Attribution extraction exceeded its 900-second budget");
  const index = inventory.length;
  const input = {
    ...fullReceipts.get(project).input,
    specsRepo,
    toolingRepo,
    attributionRoutes: [...routes],
    attributionOutput: path.join(output, `source-${index}.json`),
  };
  assert.equal(input.scope, "source");
  assert.equal(input.nativeMode, "target-only");
  const inputFile = path.join(output, `input-${index}.json`);
  const nativeOutput = path.join(output, `native-${index}.json`);
  fs.writeFileSync(inputFile, JSON.stringify(input) + "\n");
  const result = spawnSync(
    process.execPath,
    [path.join(here, "source-worker.mjs"), inputFile, nativeOutput],
    {
      encoding: "utf8",
      timeout: Math.min(120_000, 900_000 - (Date.now() - started)),
      maxBuffer: 8 * 1024 * 1024,
    },
  );
  fs.writeFileSync(
    path.join(output, `worker-${index}.log`),
    `${result.stdout ?? ""}\n${result.stderr ?? ""}`,
  );
  assert.ifError(result.error);
  assert.equal(result.status, 0, `Source extraction worker ${project} failed; preserve its log`);
  const native = read(nativeOutput);
  assert.equal(native.status, "success", JSON.stringify(native));
  assert.deepEqual(
    diagnosticMultiset(native.rawDiagnostics),
    diagnosticMultiset(fullReceipts.get(project).receipt.rawDiagnostics),
    `Supplemental configured diagnostics must exactly equal the final full-population observation: ${project}`,
  );
  assert(fs.existsSync(input.attributionOutput), `Missing extraction: ${project}`);
  inventory.push({
    project,
    routes: routes.size,
    source: `source-${index}.json`,
    native: `native-${index}.json`,
  });
  console.log(`${index + 1}/${selected.size}: ${project}`);
}
fs.writeFileSync(
  path.join(output, "inventory.json"),
  JSON.stringify(
    {
      question:
        "Attribute all182retained Swagger records to exact source route/body predicates; inspect real source contracts rather than matching property names across a project.",
      boundary:
        "Supplemental discriminating source inspection, not a reduced baseline comparison or replacement for the required487project run. No Swagger emission or regeneration.",
      projects: inventory,
      elapsedSeconds: (Date.now() - started) / 1000,
      rawDiagnosticMultisetsEqualFullRun: true,
    },
    null,
    2,
  ) + "\n",
);

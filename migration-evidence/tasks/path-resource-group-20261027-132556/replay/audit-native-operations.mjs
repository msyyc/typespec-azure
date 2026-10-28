import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { pathToFileURL } from "node:url";

const [worker, templateFile, datasetDirectory, outputDirectory] =
  process.argv.slice(2);
assert(worker && templateFile && datasetDirectory && outputDirectory);
fs.mkdirSync(outputDirectory, { recursive: false });
const template = JSON.parse(fs.readFileSync(templateFile, "utf8"));
const dataset = JSON.parse(
  fs.readFileSync(path.join(datasetDirectory, "_meta.json"), "utf8"),
);
const source = fs.readFileSync(worker, "utf8");
const sourceHash = createHash("sha256").update(source).digest("hex");
const marker = "  if (errors.length > 0) {";
assert.equal(source.split(marker).length, 2);
const hook = `
  if (errors.length === 0) {
    const auditHttp = await load("@typespec/http");
    const auditVersioning = await load("@typespec/versioning");
    const auditExperimental = await import(
      pathToFileURL(requireFromSpecs.resolve("@typespec/compiler/experimental")).href
    );
    const reported = program.diagnostics.filter((item) => tspRules.includes(item.code));
    const targets = new Set(reported.map((item) => item.target));
    const record = (operation) => ({
      name: compiler.getTypeName(operation.operation),
      path: operation.path,
      verb: operation.verb,
      ...location(operation.operation),
    });
    const sourceOperations = auditHttp.getAllHttpServices(program)[0]
      .flatMap((service) => service.operations)
      .filter((operation) => targets.has(operation.operation));
    if (sourceOperations.length !== reported.length) {
      throw new Error("Every diagnostic must bind to exactly one HTTP operation by target identity.");
    }
    const observedSource = sourceOperations.map(record);
    const projected = [];
    for (const service of compiler.listServices(program)) {
      const mutators = auditVersioning.getVersioningMutators(program, service.type);
      let namespace = service.type;
      if (mutators?.kind === "versioned") {
        const selected = mutators.snapshots.find((item) => item.version.value === project.apiVersion);
        if (!selected) continue;
        namespace = auditExperimental.unsafe_mutateSubgraphWithNamespace(
          program, [selected.mutator], namespace
        ).type;
      } else if (mutators?.kind === "transient") {
        namespace = auditExperimental.unsafe_mutateSubgraphWithNamespace(
          program, [mutators.mutator], namespace
        ).type;
      }
      const [graph, graphDiagnostics] = auditHttp.getHttpService(program, namespace);
      if (graphDiagnostics.some((item) => item.severity === "error")) {
        throw new Error("Projected HTTP metadata has errors.");
      }
      for (const operation of graph.operations) {
        const lower = operation.path.toLowerCase();
        if (
          ["get", "put", "patch", "delete"].includes(operation.verb) &&
          lower.includes("/resourcegroups/") &&
          !lower.includes("/resourcegroups/{resourcegroupname}")
        ) projected.push(record(operation));
      }
    }
    fs.writeFileSync(input.auditOutput, JSON.stringify({
      kind: "instrumented-candidate-http-metadata-audit",
      project: project.sourcePath,
      apiVersion: project.apiVersion,
      sourceProgram: observedSource,
      selectedVersionViolatingOperations: projected,
      packages,
    }, null, 2) + "\\n");
  }
`;
const instrumented = source.replace(marker, hook + marker);
const instrumentedFile = path.join(outputDirectory, "instrumented-worker.mjs");
fs.writeFileSync(instrumentedFile, instrumented);
const results = [];
for (const suffix of ["/Advisor", "/DataMigration", "/Network/Network"]) {
  const selected = dataset.projects.filter((project) =>
    project.sourcePath.endsWith(suffix),
  );
  assert.equal(selected.length, 1, `Unique project for ${suffix}`);
  const name = path.posix.basename(suffix);
  const input = {
    ...template,
    project: selected[0],
    nativeMode: "target-only",
    auditOutput: path.join(outputDirectory, `${name}-operations.json`),
  };
  const inputFile = path.join(outputDirectory, `${name}-input.json`);
  const receiptFile = path.join(outputDirectory, `${name}-native.json`);
  fs.writeFileSync(inputFile, JSON.stringify(input, null, 2) + "\n");
  const run = spawnSync(
    process.execPath,
    [instrumentedFile, inputFile, receiptFile],
    {
      encoding: "utf8",
      timeout: 300_000,
      maxBuffer: 8 * 1024 * 1024,
    },
  );
  fs.writeFileSync(
    path.join(outputDirectory, `${name}.log`),
    run.stdout + run.stderr,
  );
  assert.equal(run.status, 0, `${name}: ${run.error ?? run.stderr}`);
  const receipt = JSON.parse(fs.readFileSync(receiptFile, "utf8"));
  assert.equal(receipt.status, "success", JSON.stringify(receipt));
  const audit = JSON.parse(fs.readFileSync(input.auditOutput, "utf8"));
  results.push({
    project: selected[0].sourcePath,
    apiVersion: selected[0].apiVersion,
    findings: receipt.rawDiagnostics.length,
    boundOperations: audit.sourceProgram.length,
    selectedVersionViolatingOperations:
      audit.selectedVersionViolatingOperations.length,
  });
}
assert.equal(
  createHash("sha256").update(fs.readFileSync(worker)).digest("hex"),
  sourceHash,
);
const summary = {
  originalWorkerSha256: sourceHash,
  instrumentedWorkerSha256: createHash("sha256")
    .update(instrumented)
    .digest("hex"),
  script: pathToFileURL(import.meta.filename).href,
  scope:
    "Three known affected projects only; diagnostic-to-operation bindings use object identity. Projected metadata is a separate audit, not a rerun of the linter on a projected program.",
  results,
};
fs.writeFileSync(
  path.join(outputDirectory, "summary.json"),
  JSON.stringify(summary, null, 2) + "\n",
);
process.stdout.write(JSON.stringify(summary, null, 2) + "\n");

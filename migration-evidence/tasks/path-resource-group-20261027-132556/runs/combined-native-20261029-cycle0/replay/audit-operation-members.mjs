import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { createHash } from "node:crypto";
import { spawnSync } from "node:child_process";
assert.ok(process.argv[2] && process.argv[3], "Expected run root and pinned native-coverage-worker.mjs path");
const root = path.resolve(process.argv[2]);
const worker = path.resolve(process.argv[3]);
const runDirectory = path.join(root, "coverage-full");
const dataset = JSON.parse(fs.readFileSync(path.join(runDirectory, "dataset", "_meta.json"), "utf8"));
const coverage = JSON.parse(fs.readFileSync(path.join(runDirectory, "coverage.json"), "utf8"));
assert.equal(coverage.unassessedProjects.length, 0, "Do not normalize failed population");
const auditDirectory = path.join(root, "operation-member-audit");
assert.ok(!fs.existsSync(auditDirectory), "Preserve each audit");
fs.mkdirSync(auditDirectory);
const original = fs.readFileSync(worker, "utf8");
const marker = "  if (errors.length > 0) {";
assert.equal(original.split(marker).length, 2);
const hook = `
  if (errors.length === 0 && input.auditOutput) {
    const auditHttp = await load("@typespec/http");
    const auditVersioning = await load("@typespec/versioning");
    const auditExperimental = await import(
      pathToFileURL(requireFromSpecs.resolve("@typespec/compiler/experimental")).href
    );
    const membersFor = (operation) => {
      if (!["get", "put", "patch", "delete"].includes(operation.verb)) return [];
      const lower = operation.path.toLowerCase();
      const members = [];
      if (lower.includes("/resourcegroups/") && !lower.includes("/resourcegroups/{resourcegroupname}")) members.push("PathContainsResourceGroup");
      if (lower.includes("/subscriptions/") && !lower.includes("/subscriptions/{subscriptionid}")) members.push("PathContainsSubscriptionId");
      return members;
    };
    const record = (operation) => ({
      name: compiler.getTypeName(operation.operation),
      path: operation.path, verb: operation.verb,
      members: membersFor(operation),
      ...location(operation.operation),
    });
    const reported = program.diagnostics.filter((item) => tspRules.includes(item.code));
    const targets = new Set(reported.map((item) => item.target));
    const sourceOperations = [...targets].map((target) => {
      if (target.kind !== "Operation") throw new Error("Expected authored operation target.");
      const [operation, diagnostics] = auditHttp.getHttpOperation(program, target);
      if (diagnostics.some((item) => item.severity === "error")) throw new Error("Invalid HTTP target.");
      const result = record(operation);
      const count = reported.filter((item) => item.target === target).length;
      if (result.members.length !== count) throw new Error("Member predicates must match independently actionable diagnostic multiplicity without message attribution.");
      return { ...result, diagnosticCount: count };
    });
    const projected = [];
    for (const service of compiler.listServices(program)) {
      const mutators = auditVersioning.getVersioningMutators(program, service.type);
      let namespace = service.type;
      if (mutators?.kind === "versioned") {
        const selected = mutators.snapshots.find((item) => item.version.value === project.apiVersion);
        if (!selected) throw new Error("Selected Swagger API version not found.");
        namespace = auditExperimental.unsafe_mutateSubgraphWithNamespace(program, [selected.mutator], namespace).type;
      } else if (mutators?.kind === "transient") {
        namespace = auditExperimental.unsafe_mutateSubgraphWithNamespace(program, [mutators.mutator], namespace).type;
      }
      const [graph, diagnostics] = auditHttp.getHttpService(program, namespace);
      if (diagnostics.some((item) => item.severity === "error")) throw new Error("Selected-version HTTP graph errors.");
      for (const operation of graph.operations) {
        if (membersFor(operation).length) projected.push(record(operation));
      }
    }
    fs.writeFileSync(input.auditOutput, JSON.stringify({
      project: project.sourcePath, apiVersion: project.apiVersion,
      sourceProgram: sourceOperations,
      selectedVersionViolatingOperations: projected,
      rawDiagnosticCount: reported.length,
      note: "Member association derives from exact HTTP metadata and tested predicates, never diagnostic message text. Version audit is not a projected lint rerun.",
      packages,
    }, null, 2) + "\\n");
  }
`;
const instrumented = original.replace(marker, hook + marker);
const instrumentedFile = path.join(auditDirectory, "instrumented-worker.mjs");
fs.writeFileSync(instrumentedFile, instrumented);
const selected = new Set([...coverage.validatorProjects, ...coverage.nativeProjects]);
const inputs = [];
for (const project of selected) {
  const index = dataset.projects.findIndex((item) => item.sourcePath === project);
  assert.ok(index >= 0);
  inputs.push({ name: `project-${index}`, input: JSON.parse(fs.readFileSync(path.join(runDirectory, `native-${index}.input.json`), "utf8")), fullReceipt: path.join(runDirectory, `native-${index}.json`) });
}
for (const name of ["neither", "group-only", "subscription-only", "both"]) {
  inputs.push({ name: `control-${name}`, input: JSON.parse(fs.readFileSync(path.join(root, "controls", name, "input.json"), "utf8")), fullReceipt: path.join(root, "controls", name, "output.json") });
}
const results = [];
for (const item of inputs) {
  const inputFile = path.join(auditDirectory, `${item.name}.input.json`);
  const output = path.join(auditDirectory, `${item.name}.json`);
  const auditOutput = path.join(auditDirectory, `${item.name}.operations.json`);
  fs.writeFileSync(inputFile, JSON.stringify({ ...item.input, auditOutput }, null, 2));
  const child = spawnSync(process.execPath, [instrumentedFile, inputFile, output], { encoding: "utf8", timeout: 300_000, maxBuffer: 8 * 1024 * 1024 });
  fs.writeFileSync(path.join(auditDirectory, `${item.name}.log`), (child.stdout ?? "") + (child.stderr ?? ""));
  if (child.error) throw child.error;
  assert.equal(child.status, 0, child.stderr);
  const receipt = JSON.parse(fs.readFileSync(output, "utf8"));
  const fullReceipt = JSON.parse(fs.readFileSync(item.fullReceipt, "utf8"));
  assert.equal(receipt.status, "success", JSON.stringify(receipt));
  assert.deepEqual(receipt.rawDiagnostics, fullReceipt.rawDiagnostics, "Audit must bind actual full/control findings unchanged");
  const audit = JSON.parse(fs.readFileSync(auditOutput, "utf8"));
  results.push({ name: item.name, project: receipt.project, count: receipt.rawDiagnostics.length, operations: audit.sourceProgram.length, auditOutput, receipt: output });
  console.log(JSON.stringify(results.at(-1)));
}
assert.equal(fs.readFileSync(worker, "utf8"), original);
const sha = (bytes) => createHash("sha256").update(bytes).digest("hex");
fs.writeFileSync(path.join(auditDirectory, "summary.json"), JSON.stringify({
  workerSha256: sha(original), instrumentedWorkerSha256: sha(instrumented),
  sourceUnmodified: true, results,
  scope: "Every project with any selected Swagger or TypeSpec finding, plus injected A-only/B-only/both/neither; supplementary metadata audit, not a second full corpus run.",
}, null, 2) + "\n");

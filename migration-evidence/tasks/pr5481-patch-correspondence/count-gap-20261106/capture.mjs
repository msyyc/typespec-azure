import assert from "node:assert/strict";
import { execFileSync, spawnSync } from "node:child_process";
import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";

const [originalArgument, outputArgument] = process.argv.slice(2);
const original = path.resolve(originalArgument);
const output = path.resolve(outputArgument);
assert(!fs.existsSync(output), "Preserve previous attempts; use a fresh output directory.");
fs.mkdirSync(output, { recursive: true });
const read = (file) => JSON.parse(fs.readFileSync(file, "utf8").replace(/^\uFEFF/, ""));
const sha = (file) => createHash("sha256").update(fs.readFileSync(file)).digest("hex");
const root = path.dirname(import.meta.dirname);
const plan = read(path.join(original, "plan.json"));
const full = path.join(original, "coverage-full");
const manifest = read(path.join(full, "manifest.json"));
assert.equal(manifest.candidate.commit, "0121903975ab45cde7d7aca37cf50ffd7f3855d3");
assert.equal(manifest.specs.commit, "2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9");
assert.equal(process.version, manifest.nodeVersion);
for (const [repo, revision] of [
  [plan.candidate, manifest.candidate.commit],
  [plan.specs, manifest.specs.commit],
]) {
  assert.equal(
    execFileSync("git", ["-C", repo, "rev-parse", "HEAD"], { encoding: "utf8" }).trim(),
    revision,
  );
  assert.equal(
    execFileSync("git", ["-C", repo, "status", "--porcelain"], { encoding: "utf8" }),
    "",
  );
}
assert.equal(
  sha(
    path.join(
      plan.tooling,
      "packages",
      "typespec-lintdiff",
      "test",
      "harness",
      "native-coverage-worker.mjs",
    ),
  ),
  "8b912c6cee552c9c89946dbba04c5e03c286d89320175e9f332d595d05234609",
);
const startedAt = new Date().toISOString();
const deadline = Date.now() + 120_000;
const policy = {
  question:
    "Test empty-wrapper false positives using four small isolated semantic controls while another session owns the shared corpus gate.",
  boundary:
    "Fixture-only source supplement at unchanged assessed source and installed artifacts. Reuse saved corpus receipts and pinned sources; no real-service recompilation or Swagger generation.",
  candidateCommit: manifest.candidate.commit,
  specsCommit: manifest.specs.commit,
  nodeVersion: process.version,
  startedAt,
  budgetSeconds: 120,
  expectedMinutes: "less than1",
  concurrency: 1,
  projectCount: 0,
};
fs.writeFileSync(path.join(output, "plan.json"), JSON.stringify(policy, null, 2) + "\n");
const worker = path.join(root, "inherited-20261105", "source-worker.mjs");
const run = (input, name) => {
  assert(Date.now() < deadline, "Targeted capture budget exhausted.");
  input.toolingRepo = plan.tooling;
  input.attributionOutput = path.join(output, `${name}.source.json`);
  const inputFile = path.join(output, `${name}.input.json`);
  const nativeFile = path.join(output, `${name}.native.json`);
  fs.writeFileSync(inputFile, JSON.stringify(input) + "\n", { flag: "wx" });
  const child = spawnSync(process.execPath, [worker, inputFile, nativeFile], {
    encoding: "utf8",
    timeout: Math.min(120_000, deadline - Date.now()),
    maxBuffer: 8 * 1024 * 1024,
  });
  fs.writeFileSync(
    path.join(output, `${name}.log`),
    `${child.stdout ?? ""}\n${child.stderr ?? ""}`,
  );
  assert.ifError(child.error);
  assert.equal(child.status, 0, `Preserve failed capture: ${name}`);
  const native = read(nativeFile);
  const source = read(input.attributionOutput);
  assert.equal(native.status, "success", JSON.stringify(native));
  assert.deepEqual(source.rawDiagnostics, native.rawDiagnostics);
  const originalSource = read(
    path.join(root, "refresh-20261105-inherited", "source-attribution", "source-0.json"),
  );
  for (const key of [
    "bodyModuleSha256",
    "compatibilityModuleSha256",
    "originalWorkerSha256",
    "extractorSha256",
  ]) {
    assert.equal(source[key], originalSource[key], key);
  }
  return { native, observation: source, sourceSha256: sha(input.attributionOutput) };
};
fs.symlinkSync(
  path.join(plan.specs, "node_modules"),
  path.join(output, "node_modules"),
  "junction",
);
const fixtures = [];
for (const item of [
  {
    name: "same-immutable-wrapper",
    declarations: "model P { @visibility(Lifecycle.Read, Lifecycle.Create) value?: string; }",
    put: "{ properties?: P; tags?: string; }",
    patch: "{ properties?: P; tags?: string; }",
    expected: 1,
  },
  {
    name: "same-mutable-wrapper",
    declarations: "model P { value?: string; }",
    put: "{ properties?: P; tags?: string; }",
    patch: "{ properties?: P; tags?: string; }",
    expected: 0,
  },
  {
    name: "genuine-extra-leaf",
    put: "{ common?: string; }",
    patch: "{ extra?: string; }",
    expected: 1,
  },
  {
    name: "genuine-extra-wrapper",
    declarations: "model P { @visibility(Lifecycle.Read, Lifecycle.Create) value?: string; }",
    put: "{ common?: string; }",
    patch: "{ properties?: P; }",
    expected: 1,
  },
]) {
  const directory = path.join(output, item.name);
  fs.mkdirSync(directory);
  const source = `import "@typespec/http";
import "@azure-tools/typespec-azure-resource-manager";
using TypeSpec.Http;
using Azure.ResourceManager;
@armProviderNamespace @service namespace Microsoft.CountGap;
${item.declarations ?? ""}
@route("/widgets") @put op put(@body body: ${item.put}): void;
@route("/widgets") @patch op patch(@body body: ${item.patch}): void;
`;
  fs.writeFileSync(path.join(directory, "main.tsp"), source);
  fs.writeFileSync(path.join(directory, "tspconfig.yaml"), "{}\n");
  const value = run(
    {
      specsRepo: plan.specs,
      project: { sourcePath: directory },
      validatorRule: "PatchPropertiesCorrespondToPutProperties",
      tspRules: ["@azure-tools/typespec-azure-resource-manager/arm-resource-patch"],
      scope: "source",
      nativeMode: "target-only",
    },
    item.name,
  );
  assert.equal(value.native.rawDiagnostics.length, item.expected, item.name);
  fixtures.push({ ...item, source, ...value });
  process.stdout.write(`${item.name}: ${item.expected} configured warnings\n`);
}
fs.writeFileSync(
  path.join(output, "summary.json"),
  JSON.stringify(
    {
      ...policy,
      finishedAt: new Date().toISOString(),
      fixtures,
    },
    null,
    2,
  ) + "\n",
);

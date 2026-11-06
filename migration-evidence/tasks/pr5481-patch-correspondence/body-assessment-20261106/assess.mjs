import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";

const [mode, originalArgument, outputArgument, selection] = process.argv.slice(2);
const original = path.resolve(originalArgument);
const output = path.resolve(outputArgument);
assert(["fixtures", "inventory"].includes(mode));
assert(mode === "fixtures" || selection === undefined);
assert(!fs.existsSync(output), "Use a fresh output directory; preserve previous attempts.");
fs.mkdirSync(output, { recursive: true });
const read = (file) => JSON.parse(fs.readFileSync(file, "utf8").replace(/^\uFEFF/, ""));
const sha = (value) => createHash("sha256").update(value).digest("hex");
const plan = read(path.join(original, "plan.json"));
const full = path.join(original, "coverage-full");
const baseline = read(path.join(full, "baseline.json"));
const manifest = read(path.join(full, "manifest.json"));
assert.equal(manifest.candidate.commit, "0121903975ab45cde7d7aca37cf50ffd7f3855d3");
assert.equal(manifest.specs.commit, "2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9");
assert.equal(process.version, manifest.nodeVersion);
assert.equal(baseline.projects.length, 487);
const worker = path.join(import.meta.dirname, "worker.mjs");
const startedAt = new Date().toISOString();
const budgetSeconds = mode === "fixtures" ? 600 : 2700;
const deadline = Date.now() + budgetSeconds * 1000;
const policy = {
  question:
    mode === "fixtures"
      ? "Assess every top-level shape gate, existing owning body/content-type rules, and emitted Swagger predicate behavior."
      : "Count every body-shape skip in all487frozen source projects, including routes absent from retained Swagger findings.",
  boundary:
    "Report-only supplemental assessment at unchanged source/artifacts; not a new Swagger baseline or historical-version comparison.",
  candidateCommit: manifest.candidate.commit,
  specsCommit: manifest.specs.commit,
  baselineIdentity: manifest.baselineIdentity,
  nodeVersion: process.version,
  concurrency: mode === "fixtures" ? 1 : 2,
  startedAt,
  budgetSeconds,
  expectedMinutes: mode === "fixtures" ? "1-3" : "15-25",
};
fs.writeFileSync(path.join(output, "plan.json"), JSON.stringify(policy, null, 2) + "\n");
const run = async (input, name) => {
  assert(Date.now() < deadline, "Assessment deadline reached");
  input.toolingRepo = plan.tooling;
  input.bodyOutput = path.join(output, `${name}.bodies.json`);
  const inputFile = path.join(output, `${name}.input.json`);
  const nativeFile = path.join(output, `${name}.native.json`);
  fs.writeFileSync(inputFile, JSON.stringify(input) + "\n", { flag: "wx" });
  const log = fs.openSync(path.join(output, `${name}.log`), "wx");
  try {
    await new Promise((resolve, reject) => {
      const child = spawn(process.execPath, [worker, inputFile, nativeFile], {
        stdio: ["ignore", log, log],
        timeout: Math.min(120_000, deadline - Date.now()),
      });
      child.once("error", reject);
      child.once("exit", (code, signal) =>
        code === 0 ? resolve() : reject(new Error(`${name}: exit ${code}, signal ${signal}`)),
      );
    });
  } finally {
    fs.closeSync(log);
  }
  const native = read(nativeFile);
  assert.equal(native.status, "success", JSON.stringify(native));
  assert(fs.existsSync(input.bodyOutput));
  return {
    native,
    bodies: read(input.bodyOutput),
    nativeReceiptSha256: sha(fs.readFileSync(nativeFile)),
  };
};
const rule = "@azure-tools/typespec-azure-resource-manager/arm-resource-patch";
const owner = "@azure-tools/typespec-azure-resource-manager/use-model-request-body";
const content = "@azure-tools/typespec-azure-resource-manager/use-application-json-content-type";
let results;
if (mode === "fixtures") {
  fs.symlinkSync(
    path.join(plan.specs, "node_modules"),
    path.join(output, "node_modules"),
    "junction",
  );
  const shapes = [
    ["scalar", "string", ""],
    ["array", "string[]", ""],
    ["dictionary", "Record<string>", ""],
    [
      "union",
      "First | Second",
      "model First { common?: string; } model Second { other?: string; }",
    ],
    [
      "inherited-dictionary",
      "Derived",
      "model Base is Record<string>; model Derived extends Base {}",
    ],
  ];
  const cases = [];
  for (const [name, type, declarations] of shapes) {
    cases.push({ name: `put-${name}`, declarations, put: type, patch: "{ extra?: string }" });
    cases.push({ name: `patch-${name}`, declarations, put: "{ common?: string }", patch: type });
  }
  cases.push(
    { name: "plain-compatible", put: "{ common?: string }", patch: "{ common?: string }" },
    { name: "plain-extra", put: "{ common?: string }", patch: "{ extra?: string }" },
    {
      name: "nullable-extra",
      declarations: "model Plain { common?: string; }",
      put: "Plain | null",
      patch: "{ extra?: string }",
    },
    {
      name: "property-reference-extra",
      declarations: "model Types { payload: { common?: string }; }",
      put: "Types.payload",
      patch: "{ extra?: string }",
    },
    {
      name: "nested-collection-compatible",
      put: "{ values?: Record<string>; }",
      patch: "{ values?: Record<string>; }",
    },
    {
      name: "nested-collection-incompatible",
      put: "{ values?: Record<string>; }",
      patch: "{ values?: Record<int32>; }",
    },
    {
      name: "put-multipart",
      declarations: "model Form { value: HttpPart<string>; }",
      put: "Form",
      patch: "{ extra?: string }",
      multipart: "put",
    },
    {
      name: "patch-multipart",
      declarations: "model Form { value: HttpPart<string>; }",
      put: "{ common?: string }",
      patch: "Form",
      multipart: "patch",
    },
  );
  cases.push(
    {
      name: "patch-property-reference-extra",
      declarations: "model Types { payload: { extra?: string }; }",
      put: "{ common?: string }",
      patch: "Types.payload",
    },
    {
      name: "property-reference-compatible",
      declarations: "model Types { payload: { common?: string }; }",
      put: "Types.payload",
      patch: "Types.payload",
    },
    {
      name: "plain-inherited-compatible",
      declarations: "model Base { common?: string; } model Derived extends Base {}",
      put: "Derived",
      patch: "{ common?: string }",
    },
  );
  results = [];
  const selected = selection ? new Set(selection.split(",")) : undefined;
  assert(!selected || [...selected].every((name) => cases.some((item) => item.name === name)));
  for (const item of cases.filter((item) => !selected || selected.has(item.name))) {
    const project = path.join(output, item.name);
    fs.mkdirSync(project);
    const parameter = (verb) =>
      item.multipart === verb
        ? `@header contentType: "multipart/form-data", @multipartBody body: ${item[verb]}`
        : `@body body: ${item[verb]}`;
    const source = `import "@typespec/http";
import "@azure-tools/typespec-azure-resource-manager";
using TypeSpec.Http;
using Azure.ResourceManager;
@armProviderNamespace
@service namespace Microsoft.BodyAssessment;
${item.declarations ?? ""}
@route("/widgets") @put op put(${parameter("put")}): void;
@route("/widgets") @patch op patch(${parameter("patch")}): void;
`;
    fs.writeFileSync(path.join(project, "main.tsp"), source);
    fs.writeFileSync(path.join(project, "tspconfig.yaml"), "{}\n");
    const value = await run(
      {
        specsRepo: plan.specs,
        project: { sourcePath: project },
        validatorRule: "PatchPropertiesCorrespondToPutProperties",
        tspRules: [rule, owner, content],
        scope: "source",
        nativeMode: "target-only",
        emitFixture: true,
      },
      item.name,
    );
    assert.equal(value.bodies.pairs.length, 1, item.name);
    results.push({ name: item.name, source, ...value });
    process.stdout.write(
      JSON.stringify({
        case: item.name,
        bodyCheck: value.bodies.pairs[0].bodyCheck,
        diagnostics: value.native.rawDiagnostics.map((d) => d.rule.split("/").at(-1)),
        swagger: value.bodies.swagger.map((x) => x.diagnostics.length),
        emitterErrors: value.bodies.emitterDiagnostics.filter((x) => x.severity === "error"),
      }) + "\n",
    );
  }
} else {
  results = new Array(487);
  let next = 0;
  await Promise.all(
    Array.from({ length: 2 }, async () => {
      while (next < baseline.projects.length) {
        const index = next++;
        const project = baseline.projects[index];
        const originalNative = read(path.join(full, `native-${index}.json`));
        assert.equal(originalNative.project, project.sourcePath);
        assert.equal(originalNative.status, "success");
        const value = await run(
          {
            specsRepo: plan.specs,
            project,
            validatorRule: "PatchPropertiesCorrespondToPutProperties",
            tspRules: [rule],
            scope: "source",
            nativeMode: "target-only",
          },
          `project-${index}`,
        );
        const key = (rows) =>
          rows
            .map((row) =>
              JSON.stringify(
                Object.fromEntries(Object.entries(row).sort(([a], [b]) => a.localeCompare(b))),
              ),
            )
            .sort();
        assert.deepEqual(
          key(value.native.rawDiagnostics),
          key(originalNative.rawDiagnostics),
          `Frozen configured diagnostic multiset changed: ${project.sourcePath}`,
        );
        results[index] = {
          project: project.sourcePath,
          originalReceipt: `../refresh-20261105-inherited/runs/full-corpus/native-${index}.json`,
          originalReceiptSha256: sha(fs.readFileSync(path.join(full, `native-${index}.json`))),
          nativeReceiptSha256: value.nativeReceiptSha256,
          diagnosticMultisetMatches: true,
          configuredWarnings: value.native.rawDiagnostics.length,
          ...value.bodies,
        };
        if ((index + 1) % 25 === 0)
          process.stdout.write(`${index + 1}/487 completed; ${project.sourcePath}\n`);
      }
    }),
  );
}
assert(Date.now() < deadline, "Assessment exceeded its original deadline");
const counts = {};
for (const item of results) {
  const body = item.bodies ?? item;
  for (const pair of body.pairs) counts[pair.bodyCheck] = (counts[pair.bodyCheck] ?? 0) + 1;
}
const result = {
  ...policy,
  finishedAt: new Date().toISOString(),
  elapsedSeconds: (Date.now() - Date.parse(startedAt)) / 1000,
  projects: results.length,
  bodyChecks: counts,
  results,
};
fs.writeFileSync(path.join(output, "results.json"), JSON.stringify(result, null, 2) + "\n");
process.stdout.write(
  JSON.stringify({
    projects: result.projects,
    bodyChecks: counts,
    elapsedSeconds: result.elapsedSeconds,
  }) + "\n",
);

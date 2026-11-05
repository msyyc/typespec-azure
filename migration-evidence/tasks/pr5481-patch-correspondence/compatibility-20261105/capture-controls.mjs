import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { observeContext } from "./join-contexts.mjs";

const [local, toolingRepo] = process.argv.slice(2).map((value) => path.resolve(value));
const here = path.dirname(fileURLToPath(import.meta.url));
const output = path.join(local, "attribution-controls");
assert(!fs.existsSync(output));
fs.mkdirSync(output);
const cases = [
  ["same-name-type-difference", "incompatibleProperty", true, false],
  ["compliant-subset", null, false, false],
  ["date-encoding-difference", "incompatibleProperty", true, false],
  ["default-date-encoding", null, false, false],
  ["suppressed-incompatibility", "incompatibleProperty", false, true],
  ["partial-object-reset", null, false, false],
  ["recursive-property-constraint", "incompatibleProperty", true, false],
  ["extra-leaf", "missingProperty", true, false],
  ["authored-suppression", "missingProperty", false, true],
];
const results = [];
const started = Date.now();
const timeout = () => {
  const remaining = 300_000 - (Date.now() - started);
  assert(remaining > 0, "Extraction controls exceeded their 300-second budget");
  return Math.min(120_000, remaining);
};
for (const [name, family, configuredWarning, compilerSuppressed] of cases) {
  const input = JSON.parse(
    fs.readFileSync(path.join(local, "controls", name, "input.json"), "utf8"),
  );
  input.toolingRepo = toolingRepo;
  input.attributionOutput = path.join(output, `${name}.json`);
  const file = path.join(output, `${name}.input.json`);
  const nativeOutput = path.join(output, `${name}.native.json`);
  fs.writeFileSync(file, JSON.stringify(input) + "\n");
  const result = spawnSync(
    process.execPath,
    [path.join(here, "source-worker.mjs"), file, nativeOutput],
    {
      encoding: "utf8",
      timeout: timeout(),
      maxBuffer: 8 * 1024 * 1024,
    },
  );
  fs.writeFileSync(
    path.join(output, `${name}.log`),
    `${result.stdout ?? ""}\n${result.stderr ?? ""}`,
  );
  assert.ifError(result.error);
  assert.equal(result.status, 0, `Capture control ${name} failed`);
  const receipt = JSON.parse(fs.readFileSync(input.attributionOutput, "utf8"));
  assert.equal(receipt.pairs.length, 1);
  assert.equal(receipt.pairs[0].bodyCheck, "supported");
  const violations = receipt.pairs[0].leaves.filter((leaf) => leaf.family !== null);
  if (family === null) assert.equal(violations.length, 0);
  else {
    assert.equal(violations.length, 1);
    assert.equal(violations[0].family, family);
    assert.equal(violations[0].configuredWarning, configuredWarning);
    assert.equal(violations[0].compilerSuppressed, compilerSuppressed);
  }
  results.push({ name, family, configuredWarning, compilerSuppressed, status: "passed" });
}
const collision = path.join(output, "shared-target");
fs.mkdirSync(collision);
fs.symlinkSync(
  path.join(
    JSON.parse(fs.readFileSync(path.join(local, "controls", "extra-leaf", "input.json"), "utf8"))
      .specsRepo,
    "node_modules",
  ),
  path.join(output, "node_modules"),
  "junction",
);
fs.writeFileSync(
  path.join(collision, "main.tsp"),
  `
import "@typespec/http";
import "@azure-tools/typespec-azure-resource-manager";
using TypeSpec.Http;
@service namespace Context;
model PatchBody { value?: string; }
model Accepted { value?: string; }
model Incompatible { value?: int32; }
model Missing { other?: string; }
@route("/accepted") @put op putAccepted(@body body: Accepted): void;
@route("/accepted") @patch op patchAccepted(@body body: PatchBody): void;
@route("/incompatible") @put op putIncompatible(@body body: Incompatible): void;
@route("/incompatible") @patch op patchIncompatible(@body body: PatchBody): void;
@route("/missing") @put op putMissing(@body body: Missing): void;
@route("/missing") @patch op patchMissing(@body body: PatchBody): void;
@route("/no-body") @put op putNoBody(@body body: Accepted): void;
#suppress "@azure-tools/typespec-azure-resource-manager/arm-resource-patch" "Approved body exception."
@route("/no-body") @patch op patchNoBody(): void;
@route("/empty-body") @put op putEmpty(@body body: Accepted): void;
@route("/empty-body") @patch op patchEmpty(@body body: {}): void;
`,
);
fs.writeFileSync(path.join(collision, "tspconfig.yaml"), "{}\n");
const input = JSON.parse(
  fs.readFileSync(path.join(local, "controls", "extra-leaf", "input.json"), "utf8"),
);
input.project.sourcePath = collision;
input.toolingRepo = toolingRepo;
input.attributionOutput = path.join(output, "shared-target.json");
fs.writeFileSync(path.join(collision, "input.json"), JSON.stringify(input) + "\n");
const collisionRun = spawnSync(
  process.execPath,
  [
    path.join(here, "source-worker.mjs"),
    path.join(collision, "input.json"),
    path.join(output, "shared-target.native.json"),
  ],
  {
    encoding: "utf8",
    timeout: timeout(),
    maxBuffer: 8 * 1024 * 1024,
  },
);
fs.writeFileSync(
  path.join(output, "shared-target.log"),
  `${collisionRun.stdout ?? ""}\n${collisionRun.stderr ?? ""}`,
);
assert.ifError(collisionRun.error);
assert.equal(collisionRun.status, 0);
const captured = JSON.parse(fs.readFileSync(input.attributionOutput, "utf8"));
assert.equal(
  captured.rawDiagnostics.length,
  3,
  "Two different property-message families at one shared source position plus one empty-body warning must remain distinct",
);
assert.deepEqual(
  captured.pairs
    .filter((pair) => pair.bodyCheck === "supported")
    .map((pair) => [pair.route, pair.leaves[0].family, pair.leaves[0].configuredWarning]),
  [
    ["/accepted", null, false],
    ["/incompatible", "incompatibleProperty", true],
    ["/missing", "missingProperty", true],
  ],
);
assert.deepEqual(
  captured.pairs
    .filter((pair) => pair.bodyWarning)
    .map((pair) => [
      pair.route,
      pair.bodyCheck,
      pair.bodyWarning.configuredWarning,
      pair.bodyWarning.compilerSuppressed,
    ]),
  [
    ["/no-body", "missingPatchBody", false, true],
    ["/empty-body", "emptyPatchBody", true, false],
  ],
);
results.push({ name: "shared-target-distinct-operation-and-family", status: "passed" });
assert.deepEqual(observeContext(captured, "/accepted", "value")[0].warningIndices, []);
assert.equal(observeContext(captured, "/incompatible", "value")[0].warningIndices.length, 1);
assert.equal(observeContext(captured, "/missing", "value")[0].warningIndices.length, 1);
assert.notEqual(
  observeContext(captured, "/missing", "value")[0].warningIndices[0],
  observeContext(captured, "/incompatible", "value")[0].warningIndices[0],
);
assert.equal(observeContext(captured, "/no-body", null)[0].warningIndices.length, 0);
assert.equal(observeContext(captured, "/empty-body", null)[0].warningIndices.length, 1);
assert.deepEqual(observeContext(captured, "/unknown-route", "value"), []);
assert.equal(observeContext(captured, "/missing", "other-name")[0].warningIndices.length, 0);
fs.writeFileSync(path.join(output, "summary.json"), JSON.stringify(results, null, 2) + "\n");
console.log(`${results.length} independent extraction/suppression controls passed`);

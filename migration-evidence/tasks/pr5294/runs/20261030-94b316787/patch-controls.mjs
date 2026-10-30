import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { createHash } from "node:crypto";
import * as fs from "node:fs";
import * as path from "node:path";

const [specsRepo, worker, output, mode = "configured"] = process.argv.slice(2);
assert(specsRepo && worker && output, "Expected frozen specs, worker and new output directory.");
assert(["configured", "target-only"].includes(mode));
assert(!fs.existsSync(output), "Preserve prior controls.");
fs.mkdirSync(output, { recursive: true });
fs.symlinkSync(path.join(specsRepo, "node_modules"), path.join(output, "node_modules"), "junction");
const rule = "@azure-tools/typespec-azure-resource-manager/no-unsafe-patch-body-properties";
const imports = `
import "@typespec/http";
import "@typespec/rest";
import "@typespec/versioning";
import "@azure-tools/typespec-autorest";
import "@azure-tools/typespec-azure-core";
import "@azure-tools/typespec-azure-resource-manager";
using TypeSpec.Http;
@service namespace Microsoft.PatchCoverage;
`;
const cases = [
  {
    name: "required",
    member: "PatchBodyParametersSchema",
    source: `@parameterVisibility(Lifecycle.Create) @patch
op update(@body body: { value: string; }): { value: string; };`,
    messages: ["Properties of a PATCH request body must not be required, property:value."],
  },
  {
    name: "falsy-default",
    member: "PatchBodyParametersSchema",
    source: `@patch op update(@body body: { enabled?: boolean = false; }): { enabled: boolean; };`,
    messages: ["Properties of a PATCH request body must not have default value, property:enabled."],
  },
  {
    name: "exposed-create-only",
    member: "PatchBodyParametersSchema",
    source: `@parameterVisibility(Lifecycle.Create) @patch
op update(@body body: { @visibility(Lifecycle.Create) value?: string; }): { value: string; };`,
    messages: ["PATCH request body property 'value' must include Lifecycle.Update visibility."],
  },
  {
    name: "immutable",
    member: "UnSupportedPatchProperties",
    source: `@patch op update(@body body: { location?: string; }): { location: string; };`,
    messages: [
      "PATCH request body property 'location' is immutable and must be excluded from PATCH input.",
    ],
  },
  {
    name: "layout",
    member: "ConsistentPatchProperties",
    source: `@patch op update(@body body: { extra?: string; }): { known: string; };`,
    messages: [
      "The property 'extra' in the request body either does not appear in the resource model or is nested at the wrong level.",
    ],
  },
  {
    name: "compliant",
    member: "all",
    source: `@patch op update(@body body: { properties?: { value?: string; }; }):
{ properties: { value: string; }; };`,
    messages: [],
  },
  {
    name: "excluded-create-only",
    member: "PatchBodyParametersSchema",
    source: `@patch op update(@body body: { @visibility(Lifecycle.Create) value: string = "initial"; }):
{ value: string; };`,
    messages: [],
  },
  {
    name: "identity-exemption",
    member: "PatchBodyParametersSchema",
    source: `@patch op update(@body body: { identity?: { enabled: boolean = false; }; }):
{ identity: { enabled: boolean; }; };`,
    messages: [],
  },
  {
    name: "non-patch",
    member: "all",
    source: `@post op update(@body body: { location: string = "west"; extra: string; }): {};`,
    messages: [],
  },
  {
    name: "source-suppression",
    member: "all",
    source: `model Patch {
#suppress "${rule}" "Intentional control."
enabled?: boolean = false;
}
@patch op update(@body body: Patch): { enabled: boolean; };`,
    messages: [],
  },
];
const receipts = [];
for (const test of cases) {
  const directory = path.join(output, test.name);
  fs.mkdirSync(directory);
  fs.writeFileSync(path.join(directory, "main.tsp"), imports + test.source + "\n");
  fs.writeFileSync(
    path.join(directory, "tspconfig.yaml"),
    `linter:\n  extends:\n    - "@azure-tools/typespec-azure-rulesets/resource-manager"\n`,
  );
  const input = {
    specsRepo,
    project: { sourcePath: directory, apiVersion: "2026-01-01" },
    validatorRules: [
      "PatchBodyParametersSchema",
      "ConsistentPatchProperties",
      "UnSupportedPatchProperties",
    ],
    tspRules: [rule],
    scope: "source",
    nativeMode: mode,
  };
  const inputFile = path.join(directory, "input.json");
  const resultFile = path.join(directory, "result.json");
  fs.writeFileSync(inputFile, JSON.stringify(input, null, 2));
  const child = spawnSync(process.execPath, [worker, inputFile, resultFile], {
    encoding: "utf8",
    timeout: 120_000,
  });
  fs.writeFileSync(path.join(directory, "worker.log"), child.stdout + child.stderr);
  assert.ifError(child.error);
  assert(fs.existsSync(resultFile), `Missing receipt: ${test.name}`);
  const result = JSON.parse(fs.readFileSync(resultFile, "utf8"));
  const receipt = {
    name: test.name,
    member: test.member,
    nativeMode: mode,
    expectedMessages: test.messages,
    sourceSha256: createHash("sha256")
      .update(imports + test.source + "\n")
      .digest("hex"),
    result,
  };
  receipts.push(receipt);
  fs.writeFileSync(path.join(output, "controls.json"), JSON.stringify(receipts, null, 2) + "\n");
  assert.equal(result.status, "success", JSON.stringify(result));
  assert.deepEqual(
    result.rawDiagnostics.map((d) => d.message).sort(),
    [...test.messages].sort(),
    test.name,
  );
  if (mode === "configured") {
    assert.deepEqual(
      result.defaultTargetDiagnostics,
      [],
      `Default activation changed: ${test.name}`,
    );
  } else {
    assert.equal(result.defaultActivation, "not-assessed");
    assert.equal(result.defaultTargetDiagnostics, undefined);
  }
  console.log(`PASS ${test.name}: ${test.messages.length} target diagnostics, mode=${mode}`);
}
fs.unlinkSync(path.join(output, "node_modules"));
console.log(`All ${receipts.length} injected PATCH controls passed.`);

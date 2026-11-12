import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";

const [local, specs, tooling] = process.argv.slice(2).map((value) => path.resolve(value));
const root = path.join(local, "controls");
assert(!fs.existsSync(root), "Use a fresh control directory");
fs.mkdirSync(root);
fs.symlinkSync(path.join(specs, "node_modules"), path.join(root, "node_modules"), "junction");
const rule = "@azure-tools/typespec-azure-resource-manager/arm-resource-patch";
const worker = path.join(
  tooling,
  "packages",
  "typespec-lintdiff",
  "test",
  "harness",
  "native-coverage-worker.mjs",
);
const mismatch = (name) =>
  `The property '${name}' in the PATCH body must preserve the format and bounds of its corresponding PUT property.`;
const missing = (name) =>
  `The property '${name}' in the PATCH body does not correspond to a property in the PUT body.`;
const pair = (put, patch) => `
model PutBody { ${put} }
model PatchBody { ${patch} }
@route("/widgets") @put op replace(@body body: PutBody): void;
@route("/widgets") @patch op update(@body body: PatchBody): void;`;
const constraintSource = pair("@maxLength(256) value?: string;", "value?: string;");
const cases = [
  {
    name: "missing-name",
    source: pair("name?: string;", "extra?: string;"),
    messages: [missing("extra")],
  },
  { name: "omitted-string-limit", source: constraintSource, messages: [mismatch("value")] },
  {
    name: "omitted-item-limit",
    source: pair("@minItems(1) value?: string[];", "value?: string[];"),
    messages: [mismatch("value")],
  },
  {
    name: "omitted-numeric-limit",
    source: pair("@minValue(300) @maxValue(28800) value?: int32;", "value?: int32;"),
    messages: [mismatch("value")],
  },
  {
    name: "omitted-format",
    source: '@format("arm-id") scalar Id extends string;' + pair("value?: Id;", "value?: string;"),
    messages: [mismatch("value")],
  },
  {
    name: "narrower-bounds",
    source: pair("@maxLength(256) value?: string;", "@maxLength(128) value?: string;"),
    messages: [],
  },
  {
    name: "nullable-reset",
    source: pair("@maxLength(256) value?: string;", "@maxLength(128) value?: string | null;"),
    messages: [],
  },
  {
    name: "suppressed-constraint",
    source: pair(
      "@maxLength(256) value?: string;",
      `#suppress "${rule}" "Intentional exception."\nvalue?: string;`,
    ),
    messages: [],
  },
  {
    name: "nested-contents-outside-scope",
    source:
      "model PutItem { value: string; } model PatchItem { value?: int32; }" +
      pair("items?: PutItem[];", "items?: PatchItem[];"),
    messages: [],
  },
  {
    name: "same-name-types-outside-scope",
    source: pair("value?: string;", "value?: int32;"),
    messages: [],
  },
  {
    name: "empty-patch",
    source: pair("name?: string;", ""),
    messages: ["The PATCH request body must contain at least one property."],
  },
  {
    name: "missing-patch-body",
    source:
      'model PutBody { name?: string; } @route("/widgets") @put op replace(@body body: PutBody): void; @route("/widgets") @patch op update(): void;',
    messages: ["The PATCH operation must have a request body."],
  },
  {
    name: "opaque-container",
    source:
      "model Properties { @visibility(Lifecycle.Read, Lifecycle.Create) value?: string; }" +
      pair("properties?: Properties;", "properties?: Properties;"),
    messages: [],
  },
  {
    name: "opaque-wrong-position",
    source:
      "model Properties { @visibility(Lifecycle.Read, Lifecycle.Create) value?: string; }" +
      pair("other?: { properties?: Properties; };", "properties?: Properties;"),
    messages: [missing("properties")],
  },
  {
    name: "configured-disabled",
    source: constraintSource,
    messages: [mismatch("value")],
    defaults: 0,
  },
  {
    name: "arm-all-activation",
    source: constraintSource,
    messages: [mismatch("value")],
    defaults: 1,
    preset: "@azure-tools/typespec-azure-resource-manager/all",
  },
  {
    name: "resource-manager-activation",
    source: constraintSource,
    messages: [mismatch("value")],
    defaults: 1,
    preset: "@azure-tools/typespec-azure-rulesets/resource-manager",
  },
];
const receipts = [];
for (const test of cases) {
  const directory = path.join(root, test.name);
  fs.mkdirSync(directory);
  const source = `import "@typespec/http"; import "@typespec/versioning"; import "@azure-tools/typespec-azure-resource-manager";
using TypeSpec.Http;
@service namespace Contoso;
${test.source}
`;
  fs.writeFileSync(path.join(directory, "main.tsp"), source);
  fs.writeFileSync(
    path.join(directory, "tspconfig.yaml"),
    test.preset
      ? `linter:\n  extends:\n    - '${test.preset}'\n`
      : `linter:\n  disable:\n    "${rule}": "Explicit comparison opt-in."\n`,
  );
  const input = {
    specsRepo: specs,
    project: { sourcePath: directory, apiVersion: "2026-01-01" },
    validatorRule: "PatchPropertiesCorrespondToPutProperties",
    tspRules: [rule],
    scope: "source",
    nativeMode: test.defaults === undefined ? "target-only" : "configured",
  };
  const inputFile = path.join(directory, "input.json"),
    outputFile = path.join(directory, "output.json");
  fs.writeFileSync(inputFile, JSON.stringify(input));
  const result = spawnSync(process.execPath, [worker, inputFile, outputFile], {
    encoding: "utf8",
    timeout: 120000,
    maxBuffer: 8 * 1024 * 1024,
  });
  fs.writeFileSync(
    path.join(directory, "worker.log"),
    `${result.stdout ?? ""}\n${result.stderr ?? ""}`,
  );
  assert.ifError(result.error);
  assert.equal(result.status, 0);
  const receipt = JSON.parse(fs.readFileSync(outputFile, "utf8"));
  assert.equal(receipt.status, "success", JSON.stringify(receipt));
  assert.deepEqual(
    receipt.rawDiagnostics.map((d) => d.message),
    test.messages,
  );
  assert(receipt.ambientDiagnostics.every((d) => d.severity !== "error"));
  if (test.defaults !== undefined)
    assert.equal(receipt.defaultTargetDiagnostics.length, test.defaults);
  receipts.push({ case: test.name, source, input, receipt });
  console.log(`${test.name}: passed (${test.messages.length} findings)`);
}
fs.writeFileSync(
  path.join(local, "injected-controls.json"),
  JSON.stringify(receipts, null, 2) + "\n",
);

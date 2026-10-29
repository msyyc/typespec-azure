import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";
import { pathToFileURL } from "node:url";

const specs = String.raw`$SPECS`;
const worker = String.raw`$TOOLING\packages\typespec-lintdiff\test\harness\native-coverage-worker.mjs`;
const rule = "@azure-tools/typespec-azure-resource-manager/use-scope-path-standard-name";
const root = path.join(import.meta.dirname, "controls");
assert.ok(!fs.existsSync(root), "Use fresh controls; do not overwrite receipts");
fs.mkdirSync(root);
fs.symlinkSync(path.join(specs, "node_modules"), path.join(root, "node_modules"), "junction");
const provenance = JSON.parse(fs.readFileSync(path.join(import.meta.dirname, "artifact-provenance.json"), "utf8"));
const sha = (bytes) => createHash("sha256").update(bytes).digest("hex");
const prelude = `
import "@typespec/http";
import "@typespec/rest";
import "@typespec/versioning";
import "@azure-tools/typespec-azure-core";
import "@azure-tools/typespec-azure-resource-manager";
using TypeSpec.Http;
using TypeSpec.Rest;
using Azure.ResourceManager;
@service @armProviderNamespace namespace Microsoft.Coverage;
model WidgetProperties { description?: string; }
model Widget is ProxyResource<WidgetProperties> {
  ...ResourceNameParameter<Widget>;
}
interface Operations extends Azure.ResourceManager.Operations {}
`;
function source(subscription, group, suppressed) {
  return prelude + `
model CustomBase {
  ...CommonTypes.ApiVersionParameter;
  @path @segment("subscriptions") ${subscription}: string;
  @path @segment("resourceGroups") ${group}: string;
}
@armResourceOperations interface Widgets {
  ${suppressed ? `#suppress "${rule}" "Control: reviewed scope exception."` : ""}
  read is ArmResourceRead<Widget, BaseParameters = CustomBase>;
}
`;
}
const explicitDisable = `linter:\n  disable:\n    "${rule}": "Control: comparison opt-in only."\n`;
const cases = [
  { name: "neither", subscription: "subscriptionId", group: "resourceGroupName", count: 0 },
  { name: "group-only", subscription: "subscriptionId", group: "groupName", count: 1 },
  { name: "subscription-only", subscription: "subId", group: "resourceGroupName", count: 1 },
  { name: "both", subscription: "subId", group: "groupName", count: 2 },
  { name: "configured-disabled-positive", subscription: "subId", group: "groupName", count: 2, nativeMode: "configured", defaultCount: 0 },
  { name: "configured-disabled-compliant", subscription: "subscriptionId", group: "resourceGroupName", count: 0, nativeMode: "configured", defaultCount: 0 },
  { name: "arm-all-activation", subscription: "subId", group: "groupName", count: 2, nativeMode: "configured", defaultCount: 2, config: "linter:\n  extends:\n    - '@azure-tools/typespec-azure-resource-manager/all'\n" },
  { name: "azure-ruleset-disabled", subscription: "subId", group: "groupName", count: 2, nativeMode: "configured", defaultCount: 0, config: "linter:\n  extends:\n    - '@azure-tools/typespec-azure-rulesets/resource-manager'\n" },
  { name: "one-suppression-both-checks", subscription: "subId", group: "groupName", suppressed: true, count: 0 },
];
const receipts = [];
for (const test of cases) {
  const directory = path.join(root, test.name);
  fs.mkdirSync(directory);
  fs.writeFileSync(path.join(directory, "main.tsp"), source(test.subscription, test.group, test.suppressed));
  fs.writeFileSync(path.join(directory, "tspconfig.yaml"), test.config ?? explicitDisable);
  const input = {
    specsRepo: specs,
    project: { sourcePath: directory, apiVersion: "2026-01-01" },
    validatorRule: "PathContainsResourceGroup",
    validatorRules: ["PathContainsResourceGroup", "PathContainsSubscriptionId"],
    tspRules: [rule],
    scope: "source",
    nativeMode: test.nativeMode ?? "target-only",
  };
  fs.writeFileSync(path.join(directory, "input.json"), JSON.stringify(input, null, 2));
  const output = path.join(directory, "output.json");
  const run = spawnSync(process.execPath, [worker, path.join(directory, "input.json"), output], { encoding: "utf8", timeout: 120_000 });
  fs.writeFileSync(path.join(directory, "worker.stdout.log"), run.stdout ?? "");
  fs.writeFileSync(path.join(directory, "worker.stderr.log"), run.stderr ?? "");
  if (run.error) throw run.error;
  assert.equal(run.status, 0, run.stderr);
  const receipt = JSON.parse(fs.readFileSync(output, "utf8"));
  assert.equal(receipt.status, "success", JSON.stringify(receipt));
  assert.equal(receipt.rawDiagnostics.length, test.count, JSON.stringify(receipt));
  assert.equal(receipt.diagnostics.length, test.count);
  assert.ok(receipt.ambientDiagnostics.every((item) => item.severity !== "error"));
  if (test.nativeMode === "configured") assert.equal(receipt.defaultTargetDiagnostics.length, test.defaultCount);
  else assert.equal(receipt.defaultActivation, "not-assessed");
  for (const name of ["@typespec/compiler", "@azure-tools/typespec-azure-resource-manager", "@azure-tools/typespec-autorest"]) {
    const loaded = receipt.packages.find((item) => item.name === name);
    assert.ok(loaded, `${name} actually loaded`);
    const pkg = provenance.source.closure.find((item) => item.name === name);
    const basename = `${name.replace("@", "").replace("/", "-")}-${pkg.version}.tgz`;
    const archive = provenance.artifacts.find((item) => item.file === basename);
    const main = archive.files.find((item) => item.file === `package/${pkg.main}`);
    assert.equal(loaded.sha256, main.sha256, `Actual injected artifact for ${name}`);
  }
  receipts.push({ case: test, input, receipt, sourceSha256: sha(fs.readFileSync(path.join(directory, "main.tsp"))), receiptSha256: sha(fs.readFileSync(output)) });
  console.log(JSON.stringify({ case: test.name, status: "passed", diagnostics: test.count, defaultCount: test.defaultCount ?? "not-assessed" }));
}
const require = createRequire(path.join(specs, "package.json"));
const validatorEntry = require.resolve("@microsoft.azure/openapi-validator");
const validatorRequire = createRequire(validatorEntry);
const rulesetsEntry = validatorRequire.resolve("@microsoft.azure/openapi-validator-rulesets");
const validator = await import(pathToFileURL(rulesetsEntry).href);
const registered = ["PathContainsResourceGroup", "PathContainsSubscriptionId"].map((name) => {
  const definition = validator.spectralRulesets.azARM.rules[name];
  assert.ok(definition, `Production azARM registration: ${name}`);
  const then = Array.isArray(definition.then) ? definition.then : [definition.then];
  return { name, definition, functionNames: then.map((item) => item.function?.name), functionSources: then.map((item) => String(item.function)) };
});
const result = { status: "passed", cases: receipts, productionArmRegistration: { rulesetsEntry, sha256: sha(fs.readFileSync(rulesetsEntry)), rules: registered }, sourceAndArtifacts: { candidateContentIdentity: provenance.candidateContentIdentity, artifacts: provenance.artifacts.map(({ file, sha256, bytes }) => ({ file, sha256, bytes })) } };
fs.writeFileSync(path.join(import.meta.dirname, "injected-controls.json"), JSON.stringify(result, null, 2) + "\n");
console.log(JSON.stringify({ status: "passed", controls: receipts.length, registration: registered.map((item) => item.name) }));

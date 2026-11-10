import { strict as assert } from "node:assert";
import { spawnSync } from "node:child_process";
import { mkdirSync, readFileSync, realpathSync, symlinkSync, writeFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { join, resolve } from "node:path";

const [specsRepo, worker, output] = process.argv.slice(2);
assert(specsRepo && worker && output);
mkdirSync(output, { recursive: false });
symlinkSync(join(specsRepo, "node_modules"), join(output, "node_modules"), "junction");
assert.equal(realpathSync(join(output, "node_modules")), realpathSync(join(specsRepo, "node_modules")));
const rule = "@azure-tools/typespec-azure-resource-manager/arm-common-types-version";
const prelude = `
import "@typespec/http";
import "@typespec/rest";
import "@typespec/versioning";
import "@azure-tools/typespec-azure-core";
import "@azure-tools/typespec-azure-resource-manager";
using Http;
using Rest;
using Versioning;
using Azure.ResourceManager;
`;
const versioned = (latest, suppress = false) => `
@armProviderNamespace
@versioned(Versions)
@armCommonTypesVersion("v6")
namespace Microsoft.Control;
enum Versions {
  @armCommonTypesVersion("v4")
  historical: "2024-01-01",
  ${suppress ? `#suppress "${rule}" "Intentional compatibility control."` : ""}
  @armCommonTypesVersion("${latest}")
  latest: "2025-01-01-preview",
}
`;
const cases = [
  { name: "latest-old", source: versioned("v4"), count: 1, target: "latest", message: "Use the latest ARM common-types version 'v6' instead of 'v4'." },
  { name: "historical-old-latest-current", source: versioned("v6"), count: 0 },
  { name: "missing-historical-configuration", source: `@armProviderNamespace @versioned(Versions) namespace Microsoft.Control; enum Versions { historical: "2024-01-01", @armCommonTypesVersion("v6") latest: "2025-01-01" }`, count: 1, message: "Specify the ARM common-types version using the @armCommonTypesVersion decorator on the service namespace or on each version of the service version enum." },
  { name: "unversioned-old", source: '@armProviderNamespace @armCommonTypesVersion("v4") namespace Microsoft.Control;', count: 1, message: "Use the latest ARM common-types version 'v6' instead of 'v4'." },
  { name: "authored-latest-suppression", source: versioned("v4", true), count: 0 },
  { name: "existing-resource-manager-default-policy", source: versioned("v4"), count: 1, defaultCount: 1, preset: true, message: "Use the latest ARM common-types version 'v6' instead of 'v4'." },
  { name: "target-only-positive", source: versioned("v4"), count: 1, nativeMode: "target-only", message: "Use the latest ARM common-types version 'v6' instead of 'v4'." },
  { name: "target-only-compliant", source: versioned("v6"), count: 0, nativeMode: "target-only" },
];
const results = [];
for (const item of cases) {
  const directory = join(output, item.name);
  mkdirSync(directory);
  const source = prelude + item.source;
  writeFileSync(join(directory, "main.tsp"), source);
  writeFileSync(join(directory, "tspconfig.yaml"), item.preset
    ? 'linter:\n  extends:\n    - "@azure-tools/typespec-azure-rulesets/resource-manager"\n'
    : `linter:\n  disable:\n    "${rule}": "Control: comparison explicitly enables the rule."\n`);
  const input = join(directory, "input.json"), receiptFile = join(directory, "output.json");
  writeFileSync(input, JSON.stringify({
    specsRepo, project: { sourcePath: resolve(directory), apiVersion: "2025-01-01-preview" },
    validatorRule: "LatestVersionOfCommonTypesMustBeUsed", tspRules: [rule],
    scope: "source", nativeMode: item.nativeMode ?? "configured",
  }, null, 2) + "\n");
  const child = spawnSync(process.execPath, [worker, input, receiptFile], { encoding: "utf8" });
  writeFileSync(join(directory, "worker.stdout.txt"), child.stdout ?? "");
  writeFileSync(join(directory, "worker.stderr.txt"), child.stderr ?? "");
  assert.ifError(child.error);
  assert.equal(child.status, 0, child.stderr);
  const receipt = JSON.parse(readFileSync(receiptFile, "utf8"));
  assert.equal(receipt.status, "success", receipt.error);
  assert.equal(receipt.rawDiagnostics.length, item.count, JSON.stringify(receipt.rawDiagnostics));
  assert.equal(receipt.diagnostics.length, item.count);
  if (item.message) assert.equal(receipt.rawDiagnostics[0].message, item.message);
  if (item.target) {
    const location = receipt.rawDiagnostics[0];
    assert(source.split("\n")[location.line - 1].includes(item.target), JSON.stringify(location));
  }
  if (item.nativeMode === "target-only") {
    assert.equal(receipt.defaultActivation, "not-assessed");
    assert.equal(receipt.defaultTargetDiagnostics, undefined);
  } else {
    assert.equal(receipt.defaultTargetDiagnostics.length, item.defaultCount ?? 0);
  }
  assert(receipt.packages.some(p => p.name === "@azure-tools/typespec-azure-resource-manager" && /^[a-f0-9]{64}$/.test(p.sha256)));
  results.push({ name: item.name, result: "passed", count: item.count, receipt: `${item.name}/output.json`, sourceSha256: createHash("sha256").update(source).digest("hex") });
  console.log(`${item.name}: passed (${item.count})`);
}
writeFileSync(join(output, "controls.json"), JSON.stringify({ rule, results }, null, 2) + "\n");

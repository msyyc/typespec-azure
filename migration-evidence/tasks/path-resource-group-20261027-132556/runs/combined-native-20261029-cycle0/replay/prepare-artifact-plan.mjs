import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { createHash } from "node:crypto";
const root = String.raw`$NATIVE`;
const sha = (bytes) => createHash("sha256").update(bytes).digest("hex");
const packages = new Map();
for (const directory of [path.join(root, "packages"), path.join(root, "core", "packages")]) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    const manifestFile = path.join(directory, entry.name, "package.json");
    if (!fs.existsSync(manifestFile)) continue;
    const manifest = JSON.parse(fs.readFileSync(manifestFile, "utf8"));
    packages.set(manifest.name, { manifest, directory: path.dirname(manifestFile), manifestSha256: sha(fs.readFileSync(manifestFile)) });
  }
}
const selected = new Set();
function visit(name) {
  if (selected.has(name)) return;
  const record = packages.get(name);
  assert.ok(record, `Known package ${name}`);
  assert.ok(!record.manifest.private, `Published package ${name}`);
  selected.add(name);
  for (const dependency of Object.keys({ ...record.manifest.dependencies, ...record.manifest.peerDependencies })) {
    if (packages.has(dependency)) visit(dependency);
  }
}
for (const seed of [
  "@azure-tools/typespec-azure-resource-manager",
  "@azure-tools/typespec-autorest",
  "@azure-tools/typespec-azure-rulesets",
]) visit(seed);
const closure = [...selected].sort().map((name) => {
  const { directory, manifestSha256, manifest } = packages.get(name);
  return {
    name,
    directory,
    manifestSha256,
    version: manifest.version,
    workspace: directory.startsWith(path.join(root, "core")) ? "core" : "azure",
    main: manifest.main,
    mainBuilt: typeof manifest.main !== "string" || fs.existsSync(path.join(directory, manifest.main)),
    dependencies: Object.keys({ ...manifest.dependencies, ...manifest.peerDependencies }).filter((name) => selected.has(name)),
  };
});
assert.ok(closure.every((item) => item.mainBuilt), JSON.stringify(closure.filter((item) => !item.mainBuilt)));
const baseline = String.raw`$EVIDENCE\.scope-local\swagger-arm-20261026-2cd3c5dd`;
const dataset = JSON.parse(fs.readFileSync(path.join(baseline, "dataset", "_meta.json"), "utf8"));
const index = JSON.parse(fs.readFileSync(path.join(baseline, "dataset", "validator-results.json"), "utf8"));
assert.equal(dataset.projects.length, 487);
assert.ok(dataset.projects.every((item) => item.compileStatus === "success" && item.validationStatus === "success"));
const members = ["PathContainsResourceGroup", "PathContainsSubscriptionId"].map((rule) => {
  const entry = index.rules[rule];
  if (!entry) return { rule, status: "absent-shard-requires-production-registration-proof", count: null };
  const shardFile = path.join(baseline, "dataset", entry.resultsFile);
  const shard = JSON.parse(fs.readFileSync(shardFile, "utf8"));
  assert.equal(shard.results.length, entry.count);
  return { rule, count: entry.count, shardFile, sha256: sha(fs.readFileSync(shardFile)), results: shard.results };
});
const plan = {
  candidate: root,
  closure,
  azurePackOnly: closure.filter((item) => item.workspace === "azure").map((item) => item.name),
  corePackOnly: closure.filter((item) => item.workspace === "core").map((item) => item.name),
  baselinePopulation: dataset.projects,
  baselineIndex: { sha256: sha(fs.readFileSync(path.join(baseline, "dataset", "validator-results.json"))), rulesWithFindings: Object.keys(index.rules).length, totalViolations: index.totalViolations },
  members,
};
fs.writeFileSync(path.join(import.meta.dirname, "artifact-plan-and-baseline-readout.json"), JSON.stringify(plan, null, 2) + "\n");
console.log(JSON.stringify({ closure: closure.map((item) => item.name), population: dataset.projects.length, selectedMembers: members.map(({ rule, count, status }) => ({ rule, count, status })) }, null, 2));

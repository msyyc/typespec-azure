import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { observeContext } from "../wrapper-20261110/join-contexts.mjs";

const [local, toolingRepo] = process.argv.slice(2).map((value) => path.resolve(value));
const worker = fileURLToPath(new URL("source-worker.mjs", import.meta.url));
const output = path.join(local, "attribution-controls");
assert(!fs.existsSync(output));
fs.mkdirSync(output);
const cases = [
  ["omitted-string-limit", "incompatibleProperty", true, false],
  ["omitted-item-limit", "incompatibleProperty", true, false],
  ["omitted-numeric-limit", "incompatibleProperty", true, false],
  ["omitted-format", "incompatibleProperty", true, false],
  ["narrower-bounds", null, false, false],
  ["nullable-reset", null, false, false],
  ["suppressed-constraint", "incompatibleProperty", false, true],
  ["nested-contents-outside-scope", null, false, false],
  ["same-name-types-outside-scope", null, false, false],
  ["missing-name", "missingProperty", true, false],
  ["opaque-container", null, false, false],
  ["opaque-wrong-position", "missingProperty", true, false],
];
const results = [];
for (const [name, family, configuredWarning, compilerSuppressed] of cases) {
  const input = JSON.parse(
    fs.readFileSync(path.join(local, "controls", name, "input.json"), "utf8"),
  );
  input.toolingRepo = toolingRepo;
  input.attributionOutput = path.join(output, `${name}.json`);
  const inputFile = path.join(output, `${name}.input.json`);
  fs.writeFileSync(inputFile, JSON.stringify(input) + "\n");
  const run = spawnSync(
    process.execPath,
    [worker, inputFile, path.join(output, `${name}.native.json`)],
    {
      encoding: "utf8",
      timeout: 120000,
      maxBuffer: 8 * 1024 * 1024,
    },
  );
  fs.writeFileSync(path.join(output, `${name}.log`), `${run.stdout ?? ""}\n${run.stderr ?? ""}`);
  assert.ifError(run.error);
  assert.equal(run.status, 0);
  const captured = JSON.parse(fs.readFileSync(input.attributionOutput, "utf8"));
  assert.equal(captured.pairs.length, 1);
  const violations = captured.pairs[0].leaves.filter((leaf) => leaf.family !== null);
  if (family === null) assert.equal(violations.length, 0);
  else {
    assert.equal(violations.length, 1);
    assert.equal(violations[0].family, family);
    assert.equal(violations[0].configuredWarning, configuredWarning);
    assert.equal(violations[0].compilerSuppressed, compilerSuppressed);
    const observed = observeContext(captured, captured.pairs[0].route, violations[0].jsonName);
    assert.equal(observed[0].warningIndices.length, configuredWarning ? 1 : 0);
    assert.deepEqual(observeContext(captured, "/not-an-operation", violations[0].jsonName), []);
  }
  results.push({ name, family, configuredWarning, compilerSuppressed, status: "passed" });
}
fs.writeFileSync(path.join(output, "summary.json"), JSON.stringify(results, null, 2) + "\n");
console.log(`${results.length} extraction, attribution and suppression controls passed`);

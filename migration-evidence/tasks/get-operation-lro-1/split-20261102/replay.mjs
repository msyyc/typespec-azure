import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.dirname(fileURLToPath(import.meta.url));
const coverage = JSON.parse(fs.readFileSync(path.join(root, "coverage-summary.json"), "utf8"));
const findings = JSON.parse(fs.readFileSync(path.join(root, "findings.json"), "utf8"));
const sum = (name) => coverage.projects.reduce((total, item) => total + item[name], 0);
const byRule = {};
for (const item of findings) {
  byRule[item.diagnostic.rule] = (byRule[item.diagnostic.rule] ?? 0) + 1;
  assert.equal(item.verb, "get");
  assert.equal(item.nativeLroMetadata || item.acceptedLegacyScopes.length > 0, true);
}
assert.equal(coverage.assessableProjectCount, coverage.projects.length);
assert.equal(coverage.unassessedProjects.length, 0);
assert.equal(sum("validatorRawCount"), coverage.validatorRawCount);
assert.equal(sum("nativeRawCount"), findings.length);
assert.equal(coverage.nativeRawCount, findings.length);
assert.equal(
  findings.reduce((total, item) => total + item.paired.length, 0),
  coverage.validatorRawCount,
);
const summary = {
  replay: "Saved-observation count audit, not a fresh native run or report regeneration",
  assessedProjects: coverage.projects.length,
  swaggerFindings: coverage.validatorRawCount,
  typeSpecFindings: findings.length,
  byRule,
  distinctHttpOperations: new Set(
    findings.map((item) => JSON.stringify([item.project, item.verb, item.path])),
  ).size,
  atSelectedVersionHttpLocations: findings.filter((item) => item.inSelectedVersionHttpGraph).length,
  rawSwaggerExcess: coverage.rawValidatorExcess,
  rawTypeSpecExcess: coverage.rawNativeExcess,
};
process.stdout.write(JSON.stringify(summary, null, 2) + "\n");

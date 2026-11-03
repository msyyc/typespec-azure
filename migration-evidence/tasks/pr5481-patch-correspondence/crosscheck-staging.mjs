import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";

const [tooling, baseline, supplement, task, comparison, output] = process.argv
  .slice(2)
  .map((value) => path.resolve(value));
const read = (file) => JSON.parse(fs.readFileSync(file, "utf8"));
const harness = path.join(tooling, "packages", "typespec-lintdiff", "test", "harness");
const { buildNativeCoverageReport } = await import(
  pathToFileURL(path.join(harness, "native-coverage.ts")).href
);
const { readStagingSupplement } = await import(
  pathToFileURL(path.join(harness, "staging-supplement.ts")).href
);
const rule = "PatchPropertiesCorrespondToPutProperties";
const parent = read(path.join(baseline, "baseline.json"));
const loaded = readStagingSupplement(supplement, parent, [rule]);
const native = fs
  .readdirSync(path.join(task, "runs", "full-corpus"))
  .filter((name) => /^native-\d+\.json$/.test(name))
  .map((name) => read(path.join(task, "runs", "full-corpus", name)));
for (const receipt of native) assert.deepEqual(receipt.rawDiagnostics, receipt.diagnostics);
const report = buildNativeCoverageReport(parent.projects, loaded.members.get(rule), native, [rule]);
const summary = read(path.join(comparison, "summary.json"));
const expected = read(path.join(comparison, "projects.json"));
assert.equal(loaded.identity, summary.supplementIdentity);
for (const [actual, field] of [
  ["selectedProjectCount", "selectedProjects"],
  ["assessableProjectCount", "assessableProjects"],
  ["validatorRawCount", "swaggerReportedDiagnostics"],
  ["nativeRawCount", "typeSpecReportedDiagnostics"],
  ["validatorFileIndependentCount", "swaggerDistinctProjectPaths"],
  ["nativeSourceCount", "typeSpecDistinctSourcePositions"],
  ["rawValidatorExcess", "swaggerDirectionalExcess"],
  ["rawNativeExcess", "typeSpecDirectionalExcess"],
  ["projectsWithEqualRawCounts", "equalRawCountProjects"],
  ["validatorProjects", "swaggerProjects"],
  ["nativeProjects", "typeSpecProjects"],
  ["overlapProjects", "overlapProjects"],
  ["validatorOnlyProjects", "swaggerOnlyProjects"],
  ["nativeOnlyProjects", "typeSpecOnlyProjects"],
])
  assert.deepEqual(report[actual], summary[field], actual);
assert.deepEqual(report.unassessedProjects, []);
const byProject = new Map(expected.map((row) => [row.project, row]));
for (const row of report.projects) {
  const expected = byProject.get(row.project);
  assert.equal(row.validatorRawCount, expected.swaggerReportedDiagnostics);
  assert.equal(row.nativeRawCount, expected.typeSpecReportedDiagnostics);
  assert(row.rawDifference === -expected.signedTypeSpecMinusSwagger);
}
assert(!fs.existsSync(output));
fs.writeFileSync(
  output,
  JSON.stringify(
    {
      assessment: "Independent native-coverage harness accounting over the same saved observations",
      supplementIdentity: loaded.identity,
      selectedProjects: report.selectedProjectCount,
      assessableProjects: report.assessableProjectCount,
      swaggerReportedDiagnostics: report.validatorRawCount,
      typeSpecReportedDiagnostics: report.nativeRawCount,
      swaggerDistinctProjectPaths: report.validatorFileIndependentCount,
      typeSpecDistinctSourcePositions: report.nativeSourceCount,
      swaggerDirectionalExcess: report.rawValidatorExcess,
      typeSpecDirectionalExcess: report.rawNativeExcess,
      equalRawCountProjects: report.projectsWithEqualRawCounts,
      swaggerOnlyProjects: report.validatorOnlyProjects,
      typeSpecOnlyProjects: report.nativeOnlyProjects,
      projectRowsCrosschecked: report.projects.length,
      allAssertionsPassed: true,
      nativeExecution: "not-run",
    },
    null,
    2,
  ) + "\n",
);
process.stdout.write(
  `Cross-checked ${report.projects.length} project rows and all summary fields.\n`,
);

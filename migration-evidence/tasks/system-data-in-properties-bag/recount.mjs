import assert from "node:assert/strict";
import * as fs from "node:fs";

const [inputFile, outputFile] = process.argv.slice(2);
assert(inputFile, "Usage: node recount.mjs observations.json [output.json]");
const input = JSON.parse(fs.readFileSync(inputFile, "utf8"));
const selected = new Set(input.projects.map((project) => project.sourcePath));
assert.equal(selected.size, input.projects.length, "Duplicate selected project");
const receipts = new Map(input.native.map((receipt) => [receipt.project, receipt]));
assert.equal(receipts.size, input.native.length, "Duplicate native receipt");
assert.equal(receipts.size, selected.size, "Incomplete native receipt population");
for (const project of receipts.keys()) assert(selected.has(project));
for (const finding of input.swagger) assert(selected.has(finding.project));
const sourceKey = (finding, index) =>
  finding.sourceFile !== undefined && finding.line !== undefined && finding.column !== undefined
    ? JSON.stringify([finding.rule, finding.sourceFile, finding.line, finding.column])
    : `locationless:${index}`;
const rows = [];
const failed = [];
let unassessedNativeRawCount = 0;
let unassessedValidatorRawCount = 0;
for (const project of input.projects) {
  const receipt = receipts.get(project.sourcePath);
  const swagger = input.swagger.filter((finding) => finding.project === project.sourcePath);
  if (
    project.compileStatus !== "success" ||
    project.validationStatus !== "success" ||
    receipt.status !== "success"
  ) {
    failed.push({
      project: project.sourcePath,
      reason: receipt.error ?? "Baseline project not successful",
    });
    unassessedNativeRawCount += receipt.rawDiagnostics.length;
    unassessedValidatorRawCount += swagger.length;
    continue;
  }
  const validatorFileIndependentCount = new Set(
    swagger.map((finding) => JSON.stringify([finding.rule, finding.path])),
  ).size;
  const nativeSourceCount = new Set(receipt.diagnostics.map(sourceKey)).size;
  rows.push({
    project: project.sourcePath,
    validatorRawCount: swagger.length,
    validatorFileIndependentCount,
    nativeRawCount: receipt.rawDiagnostics.length,
    nativeAlignedCount: receipt.diagnostics.length,
    nativeSourceCount,
    nativeDefaultCount: receipt.defaultTargetDiagnostics?.length ?? 0,
    rawDifference: swagger.length - receipt.diagnostics.length,
    difference: validatorFileIndependentCount - nativeSourceCount,
  });
}
const sum = (field) => rows.reduce((total, row) => total + row[field], 0);
const validatorProjects = rows
  .filter((row) => row.validatorRawCount > 0)
  .map((row) => row.project)
  .sort();
const nativeProjects = rows
  .filter((row) => row.nativeAlignedCount > 0)
  .map((row) => row.project)
  .sort();
const result = {
  selectedProjectCount: input.projects.length,
  assessableProjectCount: rows.length,
  unassessedProjects: failed.sort((left, right) => left.project.localeCompare(right.project)),
  unassessedNativeRawCount,
  unassessedValidatorRawCount,
  validatorRawCount: sum("validatorRawCount"),
  validatorFileIndependentCount: sum("validatorFileIndependentCount"),
  nativeRawCount: sum("nativeRawCount"),
  nativeAlignedCount: sum("nativeAlignedCount"),
  nativeSourceCount: sum("nativeSourceCount"),
  nativeDefaultCount: sum("nativeDefaultCount"),
  validatorProjects,
  nativeProjects,
  overlapProjects: validatorProjects.filter((project) => nativeProjects.includes(project)),
  validatorOnlyProjects: validatorProjects.filter((project) => !nativeProjects.includes(project)),
  nativeOnlyProjects: nativeProjects.filter((project) => !validatorProjects.includes(project)),
  rawValidatorExcess: rows.reduce((total, row) => total + Math.max(0, row.rawDifference), 0),
  rawNativeExcess: rows.reduce((total, row) => total + Math.max(0, -row.rawDifference), 0),
  validatorExcess: rows.reduce((total, row) => total + Math.max(0, row.difference), 0),
  nativeExcess: rows.reduce((total, row) => total + Math.max(0, -row.difference), 0),
  projectsWithEqualRawCounts: rows.filter((row) => row.rawDifference === 0).length,
  projectsWithEqualCounts: rows.filter((row) => row.difference === 0).length,
  projects: rows.sort((left, right) => left.project.localeCompare(right.project)),
  conclusion:
    "Saved-observation count reanalysis only; not fresh native execution, semantic equivalence, or a restored CLI baseline.",
};
const text = JSON.stringify(result, null, 2) + "\n";
if (outputFile) fs.writeFileSync(outputFile, text, { flag: "wx" });
else process.stdout.write(text);

import assert from "node:assert/strict";
import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const read = (file) =>
  JSON.parse(readFileSync(fileURLToPath(new URL(file, import.meta.url)), "utf8"));
const inventory = read("project-inventory.json");
const swagger = read("swagger-findings.json");
const native = read("native-results.json");
const args = process.argv.slice(2);
assert(args.length === 0 || (args.length === 1 && args[0] === "--write"));
const writeMode = args[0] === "--write";
const selected = new Set(inventory.map((p) => p.sourcePath));
const receipts = new Map(native.map((p) => [p.project, p]));
assert.equal(selected.size, inventory.length, "Duplicate selected project");
assert.equal(receipts.size, native.length, "Duplicate native project");
assert.equal(receipts.size, selected.size, "Incomplete native receipt population");
assert.equal(swagger.count, swagger.results.length, "Incorrect saved member total");
for (const project of receipts.keys()) assert(selected.has(project));
for (const finding of swagger.results) assert(selected.has(finding.project));

const rows = [];
const unassessed = [];
for (const project of inventory) {
  const receipt = receipts.get(project.sourcePath);
  assert(receipt, `Missing project: ${project.sourcePath}`);
  if (
    project.compileStatus !== "success" ||
    project.validationStatus !== "success" ||
    receipt.status !== "success"
  ) {
    unassessed.push({
      project: project.sourcePath,
      compileStatus: project.compileStatus,
      validationStatus: project.validationStatus,
      nativeStatus: receipt.status,
      error: receipt.error ?? null,
    });
    continue;
  }
  const findings = swagger.results.filter((d) => d.project === project.sourcePath);
  const rawDifference = findings.length - receipt.diagnostics.length;
  rows.push({
    project: project.sourcePath,
    apiVersion: project.apiVersion ?? null,
    swaggerRaw: findings.length,
    swaggerOccurrenceKeys: new Set(
      findings.map((d) => JSON.stringify([d.rule, d.project, d.swaggerFile, d.path])),
    ).size,
    swaggerFileIndependentKeys: new Set(
      findings.map((d) => JSON.stringify([d.rule, d.project, d.path])),
    ).size,
    typeSpecRaw: receipt.rawDiagnostics.length,
    typeSpecAligned: receipt.diagnostics.length,
    typeSpecSourceKeys: new Set(
      receipt.diagnostics.map((d, index) =>
        d.sourceFile !== undefined && d.line !== undefined && d.column !== undefined
          ? JSON.stringify([d.rule, d.project, d.sourceFile, d.line, d.column])
          : JSON.stringify([d.rule, d.project, "locationless", index]),
      ),
    ).size,
    rawDifference,
    absoluteRawDifference: Math.abs(rawDifference),
    relativeRawDifference:
      Math.abs(rawDifference) / Math.max(findings.length, receipt.diagnostics.length, 1),
  });
}
const sum = (field) => rows.reduce((total, row) => total + row[field], 0);
const swaggerProjects = rows
  .filter((p) => p.swaggerRaw > 0)
  .map((p) => p.project)
  .sort();
const typeSpecProjects = rows
  .filter((p) => p.typeSpecAligned > 0)
  .map((p) => p.project)
  .sort();
const counts = {
  selected: inventory.length,
  assessable: rows.length,
  unassessed,
  swaggerRaw: sum("swaggerRaw"),
  swaggerOccurrenceKeys: sum("swaggerOccurrenceKeys"),
  swaggerFileIndependentKeys: sum("swaggerFileIndependentKeys"),
  typeSpecRaw: sum("typeSpecRaw"),
  typeSpecAligned: sum("typeSpecAligned"),
  typeSpecSourceKeys: sum("typeSpecSourceKeys"),
  swaggerProjects,
  typeSpecProjects,
  overlapProjects: swaggerProjects.filter((p) => typeSpecProjects.includes(p)),
  swaggerOnlyProjects: swaggerProjects.filter((p) => !typeSpecProjects.includes(p)),
  typeSpecOnlyProjects: typeSpecProjects.filter((p) => !swaggerProjects.includes(p)),
  equalRawProjects: rows.filter((p) => p.rawDifference === 0).length,
  swaggerHigherProjects: rows.filter((p) => p.rawDifference > 0).length,
  typeSpecHigherProjects: rows.filter((p) => p.rawDifference < 0).length,
  swaggerExcess: rows.reduce((total, p) => total + Math.max(p.rawDifference, 0), 0),
  typeSpecExcess: rows.reduce((total, p) => total + Math.max(-p.rawDifference, 0), 0),
  totalAbsoluteDifference: sum("absoluteRawDifference"),
  relativeDenominator: "max(Swagger raw findings, TypeSpec aligned findings, 1)",
  rows,
};
if (writeMode) {
  writeFileSync(
    new URL("counts.json", import.meta.url),
    JSON.stringify(counts, null, 2) + "\n",
    "utf8",
  );
} else {
  assert.deepEqual(counts, read("counts.json"), "Saved numerical analysis does not reproduce");
}
console.log(
  JSON.stringify({
    status: writeMode ? "written" : "passed",
    selected: counts.selected,
    assessable: counts.assessable,
    swaggerRaw: counts.swaggerRaw,
    typeSpecRaw: counts.typeSpecRaw,
    scope: "Saved-observation count audit only; neither linter was rerun.",
  }),
);

import assert from "node:assert/strict";
import fs from "node:fs";

const [inputFile, outputFile] = process.argv.slice(2);
assert.ok(
  inputFile && outputFile,
  "Usage: node reanalyze-observations.mjs observations.json output.json",
);
const input = JSON.parse(fs.readFileSync(inputFile, "utf8"));
assert.equal(input.schemaVersion, 1);
const projects = new Map(input.projects.map((project) => [project.sourcePath, project]));
const native = new Map(input.native.map((receipt) => [receipt.project, receipt]));
const attributes = new Map(input.httpAttribution.map((receipt) => [receipt.project, receipt]));
assert.equal(projects.size, input.projects.length, "Duplicate selected project");
assert.equal(native.size, input.native.length, "Duplicate native project receipt");
assert.equal(attributes.size, input.httpAttribution.length, "Duplicate attribution receipt");
assert.equal(
  projects.size,
  native.size,
  "Native population must be complete, including explicit failures",
);
assert.ok(input.native.every((receipt) => projects.has(receipt.project)));
assert.ok(input.swagger.every((diagnostic) => projects.has(diagnostic.project)));
assert.ok(input.httpAttribution.every((receipt) => projects.has(receipt.project)));
const sourceKey = (diagnostic, index) =>
  diagnostic.sourceFile !== undefined &&
  diagnostic.line !== undefined &&
  diagnostic.column !== undefined
    ? JSON.stringify([diagnostic.rule, diagnostic.sourceFile, diagnostic.line, diagnostic.column])
    : `locationless:${index}`;
const wireKey = (project, method, httpPath, status) =>
  JSON.stringify([project, method, httpPath, String(status)]);
const rows = [];
const unassessed = [];
const exactUnits = [];
for (const project of projects.values()) {
  const receipt = native.get(project.sourcePath);
  assert.ok(receipt, `Missing native receipt: ${project.sourcePath}`);
  const swagger = input.swagger.filter((diagnostic) => diagnostic.project === project.sourcePath);
  if (
    project.compileStatus !== "success" ||
    project.validationStatus !== "success" ||
    receipt.status !== "success"
  ) {
    unassessed.push({
      project: project.sourcePath,
      reason:
        receipt.error ??
        `Swagger compile=${project.compileStatus}, validation=${project.validationStatus}`,
      swaggerRaw: swagger.length,
      nativeRaw: receipt.rawDiagnostics.length,
    });
    continue;
  }
  const attribution = attributes.get(project.sourcePath);
  if (attribution) {
    assert.equal(
      attribution.raw,
      receipt.rawDiagnostics.length,
      "Attribution must retain authoritative raw count",
    );
    if (attribution.attributable) {
      assert.equal(attribution.comparableCount + attribution.unrelatedCount, attribution.raw);
      assert.ok(attribution.groups.every((group) => group.attributable));
      assert.equal(
        attribution.groups.reduce((sum, group) => sum + group.rawCount, 0),
        attribution.raw,
      );
    }
  }
  const comparable =
    receipt.rawDiagnostics.length === 0
      ? 0
      : attribution?.attributable
        ? attribution.comparableCount
        : null;
  const unrelated =
    receipt.rawDiagnostics.length === 0
      ? 0
      : attribution?.attributable
        ? attribution.unrelatedCount
        : null;
  const swaggerUnits = swagger.map((diagnostic) => {
    assert.equal(diagnostic.method, "delete");
    assert.ok([200, 204].includes(diagnostic.responseStatus));
    return wireKey(
      project.sourcePath,
      diagnostic.method,
      diagnostic.httpPath,
      diagnostic.responseStatus,
    );
  });
  const nativeUnits =
    comparable === null
      ? null
      : (attribution?.groups ?? [])
          .flatMap((group) => group.comparableUnits)
          .map((unit) => wireKey(project.sourcePath, unit.method, unit.httpPath, unit.status));
  if (nativeUnits !== null) {
    assert.equal(nativeUnits.length, comparable);
    for (const unit of new Set([...swaggerUnits, ...nativeUnits])) {
      exactUnits.push({
        project: project.sourcePath,
        unit,
        swagger: swaggerUnits.filter((candidate) => candidate === unit).length,
        native: nativeUnits.filter((candidate) => candidate === unit).length,
      });
    }
  }
  const rawDifference = swagger.length - receipt.rawDiagnostics.length;
  const comparableDifference = comparable === null ? null : swagger.length - comparable;
  rows.push({
    project: project.sourcePath,
    apiVersion: project.apiVersion ?? null,
    swaggerRaw: swagger.length,
    swaggerOccurrenceKeys: new Set(
      swagger.map((diagnostic) =>
        JSON.stringify([diagnostic.rule, diagnostic.swaggerFile, diagnostic.path]),
      ),
    ).size,
    swaggerFileIndependentKeys: new Set(
      swagger.map((diagnostic) => JSON.stringify([diagnostic.rule, diagnostic.path])),
    ).size,
    swaggerWireKeys: new Set(swaggerUnits).size,
    nativeRaw: receipt.rawDiagnostics.length,
    nativeAligned: receipt.diagnostics.length,
    nativeSourceKeys: new Set(receipt.diagnostics.map(sourceKey)).size,
    nativeDefault:
      receipt.defaultActivation === "not-assessed"
        ? null
        : (receipt.defaultTargetDiagnostics?.length ?? 0),
    nativeComparable: comparable,
    nativeUnrelated: unrelated,
    nativeComparableWireKeys: nativeUnits === null ? null : new Set(nativeUnits).size,
    rawDifference,
    comparableDifference,
    comparableAbsoluteDifference:
      comparableDifference === null ? null : Math.abs(comparableDifference),
    comparableRelativeDifference:
      comparableDifference === null
        ? null
        : Math.max(swagger.length, comparable) === 0
          ? 0
          : Math.abs(comparableDifference) / Math.max(swagger.length, comparable),
  });
}
rows.sort((left, right) => left.project.localeCompare(right.project));
exactUnits.sort((left, right) => left.unit.localeCompare(right.unit));
const sum = (field) => rows.reduce((total, row) => total + row[field], 0);
const allAttributed = rows.every((row) => row.nativeComparable !== null);
const swaggerProjects = rows.filter((row) => row.swaggerRaw > 0).map((row) => row.project);
const nativeProjects = rows.filter((row) => row.nativeRaw > 0).map((row) => row.project);
const comparableProjects = rows.filter((row) => row.nativeComparable > 0).map((row) => row.project);
const result = {
  schemaVersion: 1,
  scope:
    "Saved observations only; no compiler, emitter, linter execution, or automated equivalence conclusion",
  comparisonUnit:
    "Exact project + native HTTP method + HTTP path + response status; multiplicities retained; source/latest-version alignment still requires manual evidence",
  selectedProjects: projects.size,
  assessedProjects: rows.length,
  unassessedProjects: unassessed,
  selectedSwaggerRaw: input.swagger.length,
  swaggerRaw: sum("swaggerRaw"),
  nativeRaw: sum("nativeRaw"),
  nativeAligned: sum("nativeAligned"),
  nativeDefault: rows.some((row) => row.nativeDefault === null) ? null : sum("nativeDefault"),
  swaggerOccurrenceKeys: sum("swaggerOccurrenceKeys"),
  swaggerFileIndependentKeys: sum("swaggerFileIndependentKeys"),
  nativeSourceKeys: sum("nativeSourceKeys"),
  nativeComparable: allAttributed ? sum("nativeComparable") : null,
  nativeUnrelated: allAttributed ? sum("nativeUnrelated") : null,
  unattributedProjects: rows
    .filter((row) => row.nativeComparable === null)
    .map((row) => row.project),
  rawSwaggerExcess: rows.reduce((total, row) => total + Math.max(0, row.rawDifference), 0),
  rawNativeExcess: rows.reduce((total, row) => total + Math.max(0, -row.rawDifference), 0),
  comparableSwaggerExcess: allAttributed
    ? rows.reduce((total, row) => total + Math.max(0, row.comparableDifference), 0)
    : null,
  comparableNativeExcess: allAttributed
    ? rows.reduce((total, row) => total + Math.max(0, -row.comparableDifference), 0)
    : null,
  swaggerProjects,
  nativeProjects,
  comparableProjects,
  rawSwaggerOnlyProjects: swaggerProjects.filter((project) => !nativeProjects.includes(project)),
  rawNativeOnlyProjects: nativeProjects.filter((project) => !swaggerProjects.includes(project)),
  comparableSwaggerOnlyProjects: allAttributed
    ? swaggerProjects.filter((project) => !comparableProjects.includes(project))
    : null,
  comparableNativeOnlyProjects: allAttributed
    ? comparableProjects.filter((project) => !swaggerProjects.includes(project))
    : null,
  exactUnitDifferences: exactUnits.filter((unit) => unit.swagger !== unit.native),
  exactUnitMatchingGroups: exactUnits.filter((unit) => unit.swagger === unit.native).length,
  exactUnits,
  projects: rows,
};
fs.writeFileSync(outputFile, JSON.stringify(result, null, 2) + "\n");
console.log(
  JSON.stringify({
    selected: result.selectedProjects,
    assessed: result.assessedProjects,
    failed: result.unassessedProjects.length,
    swagger: result.swaggerRaw,
    native: result.nativeRaw,
    comparable: result.nativeComparable,
    unrelated: result.nativeUnrelated,
    exactUnitDifferences: result.exactUnitDifferences.length,
  }),
);

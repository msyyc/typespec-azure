import assert from "node:assert/strict";
import * as fs from "node:fs";
import * as path from "node:path";

const [run, destination] = process.argv.slice(2);
assert.ok(run && destination, "Expected completed run and audit output directory.");
const read = (file) => JSON.parse(fs.readFileSync(path.join(run, file), "utf8"));
const manifest = read("manifest.json");
assert.ok(["complete", "incomplete"].includes(manifest.status), manifest.status);
const meta = read(path.join("dataset", "_meta.json"));
assert.equal(meta.complete, true);
const report = read("coverage.json");
assert.equal(report.members.length, 1);
const observations = report.members[0].observations;
const native = fs
  .readdirSync(run)
  .filter((name) => /^native-\d+\.json$/.test(name))
  .map(read);
assert.equal(native.length, meta.projects.length);
const byProject = new Map(native.map((item) => [item.project, item]));
assert.equal(byProject.size, native.length);
const sourceKey = (item, index) =>
  item.sourceFile === undefined
    ? JSON.stringify(["locationless", index])
    : JSON.stringify([item.rule, item.sourceFile, item.line, item.column]);
const rows = meta.projects.map((project) => {
  const result = byProject.get(project.sourcePath);
  assert.ok(result, project.sourcePath);
  const findings = observations.filter((item) => item.project === project.sourcePath);
  const assessable =
    project.compileStatus === "success" &&
    project.validationStatus === "success" &&
    result.status === "success";
  if (assessable) assert.ok(Array.isArray(result.defaultTargetDiagnostics));
  const raw = result.rawDiagnostics.length;
  const aligned = result.diagnostics.length;
  const source = new Set(result.diagnostics.map(sourceKey)).size;
  const validatorPaths = new Set(findings.map((item) => JSON.stringify([item.rule, item.path])))
    .size;
  const validatorInvocationPaths = new Set(
    findings.map((item) =>
      JSON.stringify([item.rule, item.validatorInputFile ?? item.swaggerFile, item.path]),
    ),
  ).size;
  const attributed = findings.filter((item) => item.sourceAttribution === "reported");
  const validatorReportedFilePaths = new Set(
    attributed.map((item) => JSON.stringify([item.rule, item.swaggerFile, item.path])),
  ).size;
  return {
    project: project.sourcePath,
    apiVersion: project.apiVersion ?? null,
    assessable,
    compileStatus: project.compileStatus,
    validationStatus: project.validationStatus,
    nativeStatus: result.status,
    validatorRaw: findings.length,
    validatorInvocationPaths,
    validatorReportedFilePaths,
    validatorAttributedRaw: attributed.length,
    validatorUnattributedRaw: findings.length - attributed.length,
    validatorPaths,
    nativeRaw: raw,
    nativeAligned: aligned,
    nativeSources: source,
    nativeDefault: result.defaultTargetDiagnostics?.length ?? null,
    rawDifference: assessable ? findings.length - aligned : null,
    absoluteRawDifference: assessable ? Math.abs(findings.length - aligned) : null,
    relativeRawDifference: assessable
      ? Math.max(findings.length, aligned) === 0
        ? 0
        : Math.abs(findings.length - aligned) / Math.max(findings.length, aligned)
      : null,
    locationDifference: assessable ? validatorPaths - source : null,
    compileError: project.compileError ?? null,
    validationError: project.validationError ?? null,
    nativeError: result.error ?? null,
  };
});
const assessable = rows.filter((row) => row.assessable);
const sum = (key) => assessable.reduce((total, row) => total + row[key], 0);
const vOnly = assessable
  .filter((row) => row.validatorRaw > 0 && row.nativeAligned === 0)
  .map((row) => row.project)
  .sort();
const nOnly = assessable
  .filter((row) => row.nativeAligned > 0 && row.validatorRaw === 0)
  .map((row) => row.project)
  .sort();
const audit = {
  runStatus: manifest.status,
  candidateCommit: manifest.candidate.commit,
  coreCommit: manifest.coreCommit,
  specsCommit: manifest.specs.commit,
  generatorCommit: manifest.generatorCommit,
  baselineIdentity: manifest.baselineIdentity,
  relativeGapPolicy:
    "abs(validatorRaw-nativeAligned)/max(validatorRaw,nativeAligned); both zero => 0; unassessed => null",
  fileAwarePolicy:
    "Reported document keys require explicit source attribution. Invocation keys are not exact target identities. Missing or ambiguous source remains unassigned.",
  selected: rows.length,
  assessable: assessable.length,
  unassessed: rows.length - assessable.length,
  validatorProjects: assessable.filter((row) => row.validatorRaw > 0).length,
  nativeProjects: assessable.filter((row) => row.nativeAligned > 0).length,
  overlapProjects: assessable.filter((row) => row.validatorRaw > 0 && row.nativeAligned > 0).length,
  validatorOnly: vOnly,
  nativeOnly: nOnly,
  validatorRaw: sum("validatorRaw"),
  validatorInvocationPaths: sum("validatorInvocationPaths"),
  validatorReportedFilePaths: sum("validatorReportedFilePaths"),
  validatorAttributedRaw: sum("validatorAttributedRaw"),
  validatorUnattributedRaw: sum("validatorUnattributedRaw"),
  validatorPaths: sum("validatorPaths"),
  nativeRaw: sum("nativeRaw"),
  nativeAligned: sum("nativeAligned"),
  nativeSources: sum("nativeSources"),
  nativeDefault: sum("nativeDefault"),
  rawValidatorExcess: assessable.reduce((total, row) => total + Math.max(row.rawDifference, 0), 0),
  rawNativeExcess: assessable.reduce((total, row) => total + Math.max(-row.rawDifference, 0), 0),
  locationValidatorExcess: assessable.reduce(
    (total, row) => total + Math.max(row.locationDifference, 0),
    0,
  ),
  locationNativeExcess: assessable.reduce(
    (total, row) => total + Math.max(-row.locationDifference, 0),
    0,
  ),
  equalRawProjects: assessable.filter((row) => row.rawDifference === 0).length,
  equalLocationProjects: assessable.filter((row) => row.locationDifference === 0).length,
  rows: rows.sort((a, b) => a.project.localeCompare(b.project)),
};
for (const [ours, theirs] of [
  ["selected", "selectedProjectCount"],
  ["assessable", "assessableProjectCount"],
  ["validatorRaw", "validatorRawCount"],
  ["validatorPaths", "validatorFileIndependentCount"],
  ["nativeRaw", "nativeRawCount"],
  ["nativeAligned", "nativeAlignedCount"],
  ["nativeSources", "nativeSourceCount"],
  ["nativeDefault", "nativeDefaultCount"],
  ["rawValidatorExcess", "rawValidatorExcess"],
  ["rawNativeExcess", "rawNativeExcess"],
  ["locationValidatorExcess", "validatorExcess"],
  ["locationNativeExcess", "nativeExcess"],
  ["equalRawProjects", "projectsWithEqualRawCounts"],
  ["equalLocationProjects", "projectsWithEqualCounts"],
])
  assert.equal(audit[ours], report[theirs], `${ours} != ${theirs}`);
assert.deepEqual(vOnly, [...report.validatorOnlyProjects].sort());
assert.deepEqual(nOnly, [...report.nativeOnlyProjects].sort());
fs.mkdirSync(destination, { recursive: true });
fs.writeFileSync(path.join(destination, "count-audit.json"), JSON.stringify(audit, null, 2) + "\n");
const columns = Object.keys(rows[0]).filter((key) => !key.endsWith("Error"));
const escape = (value) => `"${String(value ?? "").replaceAll('"', '""')}"`;
fs.writeFileSync(
  path.join(destination, "project-counts.csv"),
  [
    columns.map(escape).join(","),
    ...rows.map((row) => columns.map((column) => escape(row[column])).join(",")),
  ].join("\n") + "\n",
);
process.stdout.write(`${JSON.stringify({ ...audit, rows: undefined }, null, 2)}\n`);

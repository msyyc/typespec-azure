import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { createHash } from "node:crypto";
import { pathToFileURL } from "node:url";

const allowed = new Set(["get", "put", "patch", "delete"]);
export const unitKey = (unit) => JSON.stringify([unit.member, unit.project, unit.path, unit.verb]);
export function compareUnits(left, right) {
  const leftSet = new Set(left.map(unitKey));
  const rightSet = new Set(right.map(unitKey));
  assert.equal(leftSet.size, left.length, "Duplicate actionable Swagger operation/member unit");
  assert.equal(rightSet.size, right.length, "Duplicate actionable TypeSpec operation/member unit");
  return {
    swagger: left.length,
    native: right.length,
    missing: [...leftSet].filter((key) => !rightSet.has(key)).sort(),
    extra: [...rightSet].filter((key) => !leftSet.has(key)).sort(),
  };
}
export function expand(project, route, methods, members) {
  return members.flatMap((member) => methods.filter((method) => allowed.has(method)).map((verb) => ({ member, project, path: route, verb })));
}
export function analyze(root, groupingFile) {
  const read = (file) => JSON.parse(fs.readFileSync(file, "utf8"));
  const fullRun = path.join(root, "coverage-full");
  const datasetRoot = path.join(fullRun, "dataset");
  const dataset = read(path.join(datasetRoot, "_meta.json"));
  const coverage = read(path.join(fullRun, "coverage.json"));
  assert.equal(dataset.projects.length, 487);
  assert.equal(coverage.assessableProjectCount, 487);
  assert.equal(coverage.unassessedProjects.length, 0);
  const observations = coverage.members.flatMap((member) => member.observations);
  const cardinalityFile = groupingFile ?? path.resolve(root, "..", "..", "migration-evidence", "tasks", "path-resource-group-20261027-132556", "receipts", "step6-swagger-cardinality-audit.json");
  const cardinality = read(cardinalityFile);
  const identity = (item) => JSON.stringify([item.rule, item.project, item.swaggerFile, item.validatorInputFile, item.path]);
  const ordered = (items) => items.map(identity).sort();
  assert.deepEqual(ordered(cardinality.groups.flatMap((group) => group.observations)), ordered(observations), "Historical Swagger-only grouping must preserve every immutable selected observation");
  const documents = new Map();
  function document(file) {
    const absolute = path.resolve(datasetRoot, file);
    const relative = path.relative(datasetRoot, absolute);
    assert.ok(relative !== ".." && !relative.startsWith(`..${path.sep}`) && !path.isAbsolute(relative));
    if (!documents.has(file)) documents.set(file, read(absolute));
    return documents.get(file);
  }
  function refs(value, result = []) {
    if (value && typeof value === "object") {
      if (typeof value.$ref === "string") result.push(value.$ref);
      for (const child of Object.values(value)) refs(child, result);
    }
    return result;
  }
  const swaggerUnits = [];
  const swaggerGroups = [];
  for (const group of cardinality.groups) {
    assert.equal(group.candidateDocuments.length, 1, "Unique exact owning document required");
    const owner = group.candidateDocuments[0];
    const project = dataset.projects.find((item) => item.sourcePath === group.project);
    assert.equal(owner.apiVersion, project.apiVersion);
    const doc = document(owner.file);
    assert.equal(doc.info.version, project.apiVersion);
    const route = doc[group.path[0]][group.path[1]];
    assert.ok(route);
    const methods = Object.keys(route).filter((verb) => allowed.has(verb)).sort();
    assert.deepEqual(methods, owner.operations.map((item) => item.verb).sort());
    for (const occurrence of group.inputOccurrences) {
      assert.equal(occurrence.candidateReferenceChains.length, 1);
      const { document: target, chain } = occurrence.candidateReferenceChains[0];
      assert.equal(target, owner.file);
      assert.equal(chain[0], occurrence.input);
      assert.equal(chain.at(-1), owner.file);
      for (let index = 0; index + 1 < chain.length; index++) {
        assert.ok(refs(document(chain[index])).some((reference) => {
          const file = reference.split("#")[0];
          return file && !/^[a-z][a-z0-9+.-]*:/i.test(file) &&
            path.posix.normalize(path.posix.join(path.posix.dirname(chain[index]), decodeURIComponent(file))) === chain[index + 1];
        }), `Exact reference edge ${chain[index]} -> ${chain[index + 1]}`);
      }
    }
    const members = [...new Set(group.observations.map((item) => item.rule))];
    const units = expand(group.project, group.path[1], methods, members);
    swaggerUnits.push(...units);
    swaggerGroups.push({ project: group.project, path: group.path, rawCount: group.observations.length, members, owner, methods, comparableCount: units.length, observations: group.observations, referenceEvidence: group.inputOccurrences });
  }
  const summary = read(path.join(root, "operation-member-audit", "summary.json"));
  const nativeUnits = [];
  const audits = [];
  for (const item of summary.results) {
    const audit = read(path.join(root, "operation-member-audit", `${item.name}.operations.json`));
    const sourceUnits = audit.sourceProgram.flatMap((operation) => expand(item.project, operation.path, [operation.verb], operation.members));
    const projectedUnits = audit.selectedVersionViolatingOperations.flatMap((operation) => expand(item.project, operation.path, [operation.verb], operation.members));
    const selected = compareUnits(sourceUnits, projectedUnits);
    assert.deepEqual(selected.missing, [], "Source violations not represented in selected version");
    assert.deepEqual(selected.extra, [], "Selected-version violations not represented in source");
    assert.equal(sourceUnits.length, audit.rawDiagnosticCount);
    if (item.name.startsWith("project-")) nativeUnits.push(...sourceUnits);
    audits.push({ name: item.name, project: item.project, diagnosticCount: audit.rawDiagnosticCount, units: sourceUnits, selectedVersionComparison: selected, sourceProgram: audit.sourceProgram, selectedVersionViolatingOperations: audit.selectedVersionViolatingOperations });
  }
  const controls = audits.filter((item) => item.name.startsWith("control-"));
  assert.deepEqual(controls.map((item) => item.units.length), [0, 1, 1, 2]);
  const controlMembers = Object.fromEntries(controls.map((item) => [item.name, item.units.map((unit) => unit.member)]));
  assert.deepEqual(controlMembers["control-group-only"], ["PathContainsResourceGroup"]);
  assert.deepEqual(controlMembers["control-subscription-only"], ["PathContainsSubscriptionId"]);
  assert.deepEqual(controlMembers["control-both"], ["PathContainsResourceGroup", "PathContainsSubscriptionId"]);
  const rows = coverage.projects.map((row) => {
    const left = swaggerUnits.filter((unit) => unit.project === row.project);
    const right = nativeUnits.filter((unit) => unit.project === row.project);
    assert.equal(right.length, row.nativeAlignedCount, "Every full-run diagnostic must have current exact metadata binding");
    const comparable = compareUnits(left, right);
    const signedDifference = row.nativeAlignedCount - row.validatorRawCount;
    return { ...row, signedDifference, absoluteDifference: Math.abs(signedDifference), relativeDifference: Math.abs(signedDifference) / Math.max(row.nativeAlignedCount, row.validatorRawCount, 1), comparable };
  });
  const sha = (bytes) => createHash("sha256").update(bytes).digest("hex");
  const result = {
    baselineIdentity: read(path.join(fullRun, "manifest.json")).baselineIdentity,
    countingUnit: "member policy + exact project + case-preserved full HTTP path + eligible HTTP method; semantic metadata association, not message attribution",
    rawMemberNativeAttribution: "unassessed; automated raw receipts do not carry a member ID",
    normalizationControls: controlMembers,
    selectedProjects: dataset.projects.length,
    assessedProjects: rows.length,
    unassessedProjects: coverage.unassessedProjects,
    rawSwagger: coverage.validatorRawCount,
    rawNative: coverage.nativeAlignedCount,
    equalRawCountProjects: rows.filter((row) => row.absoluteDifference === 0).length,
    swaggerHigherExcess: rows.reduce((sum, row) => sum + Math.max(-row.signedDifference, 0), 0),
    nativeHigherExcess: rows.reduce((sum, row) => sum + Math.max(row.signedDifference, 0), 0),
    totalAbsoluteDifference: rows.reduce((sum, row) => sum + row.absoluteDifference, 0),
    comparable: compareUnits(swaggerUnits, nativeUnits),
    rows,
    swaggerGroups,
    audits,
    immutableSwaggerGroupingReuse: { file: cardinalityFile, sha256: sha(fs.readFileSync(cardinalityFile)), validatedAgain: "Every raw selected observation, unique owning current baseline document, selected API version, eligible method and local reference-chain edge." },
  };
  assert.equal(result.swaggerHigherExcess, coverage.rawValidatorExcess);
  assert.equal(result.nativeHigherExcess, coverage.rawNativeExcess);
  assert.equal(result.equalRawCountProjects, coverage.projectsWithEqualRawCounts);
  return result;
}
if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  const root = process.argv[2] ?? import.meta.dirname;
  const result = analyze(root, process.argv[3]);
  fs.writeFileSync(path.join(root, "combined-operation-comparison.json"), JSON.stringify(result, null, 2) + "\n");
  console.log(JSON.stringify({ rawSwagger: result.rawSwagger, rawNative: result.rawNative, projects: result.assessedProjects, comparable: result.comparable, swaggerHigherExcess: result.swaggerHigherExcess, nativeHigherExcess: result.nativeHigherExcess, totalAbsoluteDifference: result.totalAbsoluteDifference }));
}

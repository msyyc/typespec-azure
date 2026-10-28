import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";

const validatorRule = "PathContainsResourceGroup";
const nativeRule =
  "@azure-tools/typespec-azure-resource-manager/resource-group-path-parameter";
const eligible = new Set(["get", "put", "patch", "delete"]);
const key = (unit) => JSON.stringify([unit.project, unit.path, unit.verb]);
const sourceKey = (unit) =>
  JSON.stringify([unit.sourceFile, unit.line, unit.column]);
const sorted = (values) => [...values].sort();
const multiset = (values) =>
  sorted(values.map((value) => JSON.stringify(value)));

export function expandMethods(project, route, methods) {
  return methods
    .filter((verb) => eligible.has(verb))
    .map((verb) => ({ project, path: route, verb }));
}

export function compareUnits(swagger, native) {
  const left = new Set(swagger.map(key));
  const right = new Set(native.map(key));
  assert.equal(
    left.size,
    swagger.length,
    "Ambiguous Swagger operation-unit identity",
  );
  assert.equal(
    right.size,
    native.length,
    "Distinct native operations collide on path and verb",
  );
  return {
    swagger: swagger.length,
    native: native.length,
    missing: sorted([...left].filter((item) => !right.has(item))),
    extra: sorted([...right].filter((item) => !left.has(item))),
  };
}

export function analyze(
  datasetDirectory,
  observationsFile,
  cardinalityFile,
  auditDirectory,
  nativeRun,
) {
  const read = (file) => JSON.parse(fs.readFileSync(file, "utf8"));
  const dataset = read(path.join(datasetDirectory, "_meta.json"));
  const observations = read(observationsFile);
  const cardinality = read(cardinalityFile);
  assert(
    observations.observations.every((item) => item.rule === validatorRule),
  );
  assert.deepEqual(
    multiset(cardinality.groups.flatMap((group) => group.observations)),
    multiset(observations.observations),
    "Every raw Swagger observation must survive grouping",
  );
  const documents = new Map();
  function document(file) {
    const absolute = path.resolve(datasetDirectory, file);
    const relative = path.relative(datasetDirectory, absolute);
    assert(
      !path.isAbsolute(relative) &&
        relative !== ".." &&
        !relative.startsWith(`..${path.sep}`),
    );
    if (!documents.has(file)) documents.set(file, read(absolute));
    return documents.get(file);
  }
  function references(value, result = []) {
    if (value && typeof value === "object") {
      if (typeof value.$ref === "string") result.push(value.$ref);
      for (const child of Object.values(value)) references(child, result);
    }
    return result;
  }
  const swaggerUnits = [];
  for (const group of cardinality.groups) {
    assert.equal(
      group.candidateDocuments.length,
      1,
      "Exact owning Swagger document must be unique",
    );
    const owner = group.candidateDocuments[0];
    const project = dataset.projects.find(
      (item) => item.sourcePath === group.project,
    );
    assert(project);
    assert.equal(owner.apiVersion, project.apiVersion);
    const root = document(owner.file);
    assert.equal(root.info.version, project.apiVersion);
    assert.equal(group.path.length, 2);
    assert(["paths", "x-ms-paths"].includes(group.path[0]));
    const item = root[group.path[0]][group.path[1]];
    assert(item);
    const methods = Object.keys(item).filter((verb) => eligible.has(verb));
    assert.deepEqual(
      sorted(methods),
      sorted(owner.operations.map((operation) => operation.verb)),
    );
    for (const occurrence of group.inputOccurrences) {
      assert.equal(occurrence.candidateReferenceChains.length, 1);
      const { document: target, chain } =
        occurrence.candidateReferenceChains[0];
      assert.equal(target, owner.file);
      assert.equal(chain[0], occurrence.input);
      assert.equal(chain.at(-1), owner.file);
      for (let index = 0; index + 1 < chain.length; index++) {
        const reachable = references(document(chain[index])).some(
          (reference) => {
            const file = reference.split("#")[0];
            return (
              file &&
              !/^[a-z][a-z0-9+.-]*:/i.test(file) &&
              path.posix.normalize(
                path.posix.join(
                  path.posix.dirname(chain[index]),
                  decodeURIComponent(file),
                ),
              ) === chain[index + 1]
            );
          },
        );
        assert(
          reachable,
          `Missing exact local reference edge: ${chain[index]} -> ${chain[index + 1]}`,
        );
      }
    }
    swaggerUnits.push(...expandMethods(group.project, group.path[1], methods));
  }
  const summaries = read(path.join(auditDirectory, "summary.json"));
  const nativeUnits = [];
  const audits = new Map();
  for (const item of summaries.results) {
    const name = path.posix.basename(item.project);
    const audit = read(path.join(auditDirectory, `${name}-operations.json`));
    const receipt = read(path.join(auditDirectory, `${name}-native.json`));
    assert.equal(receipt.status, "success");
    assert(
      receipt.rawDiagnostics.every(
        (diagnostic) => diagnostic.rule === nativeRule,
      ),
    );
    assert.deepEqual(
      sorted(audit.sourceProgram.map(sourceKey)),
      sorted(receipt.rawDiagnostics.map(sourceKey)),
      "Each native diagnostic must retain its exact source binding",
    );
    const source = audit.sourceProgram.map((operation) => ({
      ...operation,
      project: item.project,
    }));
    const projected = audit.selectedVersionViolatingOperations.map(
      (operation) => ({ ...operation, project: item.project }),
    );
    assert.deepEqual(compareUnits(source, projected), {
      swagger: source.length,
      native: source.length,
      missing: [],
      extra: [],
    });
    nativeUnits.push(...source);
    audits.set(item.project, receipt);
  }
  const rows = [];
  for (const project of dataset.projects) {
    const rawSwagger = observations.observations.filter(
      (item) => item.project === project.sourcePath,
    ).length;
    let receipt = audits.get(project.sourcePath);
    if (nativeRun) {
      const index = dataset.projects.indexOf(project);
      receipt = read(path.join(nativeRun, `native-${index}.json`));
      assert.equal(receipt.project, project.sourcePath);
      if (receipt.status === "success" && receipt.rawDiagnostics.length > 0) {
        const auditReceipt = audits.get(project.sourcePath);
        assert(
          auditReceipt,
          `Native-only project needs its own exact operation audit: ${project.sourcePath}`,
        );
        assert.deepEqual(
          multiset(receipt.rawDiagnostics),
          multiset(auditReceipt.rawDiagnostics),
        );
      }
    }
    const assessed = receipt?.status === "success";
    const rawNative = assessed ? receipt.rawDiagnostics.length : null;
    const comparison = assessed
      ? compareUnits(
          swaggerUnits.filter((unit) => unit.project === project.sourcePath),
          nativeUnits.filter((unit) => unit.project === project.sourcePath),
        )
      : null;
    assert(!assessed || comparison.native === rawNative);
    rows.push({
      project: project.sourcePath,
      apiVersion: project.apiVersion,
      status: assessed ? "assessed" : "unassessed",
      rawSwagger,
      rawNative,
      signedDifference: assessed ? rawNative - rawSwagger : null,
      absoluteDifference: assessed ? Math.abs(rawNative - rawSwagger) : null,
      relativeDifference: assessed
        ? Math.abs(rawNative - rawSwagger) / Math.max(rawNative, rawSwagger, 1)
        : null,
      comparable: comparison,
    });
  }
  return {
    mapping: { validatorRule, nativeRule },
    countingUnit:
      "Exact project + case-preserved full HTTP path + eligible HTTP method. Source diagnostics bind to operations by object identity in the instrumented audit. Reference collapse requires a unique exact owning document and verified local reference chains.",
    attribution:
      "Derived owning-document/reference evidence does not replace original sourceDocuments or input-fallback attribution.",
    scope: nativeRun
      ? "Full saved native population with explicit unassessed rows"
      : "Supplemental three-project outlier audit; not full corpus evidence",
    selectedProjects: rows.length,
    assessedProjects: rows.filter((row) => row.status === "assessed").length,
    unassessedProjects: rows
      .filter((row) => row.status === "unassessed")
      .map((row) => row.project),
    rawSwagger: observations.observations.length,
    rawNativeAssessed: rows.reduce((sum, row) => sum + (row.rawNative ?? 0), 0),
    swaggerHigherExcess: rows.reduce(
      (sum, row) =>
        sum +
        (row.status === "assessed"
          ? Math.max(row.rawSwagger - row.rawNative, 0)
          : 0),
      0,
    ),
    nativeHigherExcess: rows.reduce(
      (sum, row) =>
        sum +
        (row.status === "assessed"
          ? Math.max(row.rawNative - row.rawSwagger, 0)
          : 0),
      0,
    ),
    comparable: compareUnits(swaggerUnits, nativeUnits),
    rows,
  };
}

if (
  process.argv[1] &&
  import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href
) {
  const [dataset, observations, cardinality, audit, output, nativeRun] =
    process.argv.slice(2);
  assert(dataset && observations && cardinality && audit && output);
  fs.writeFileSync(
    output,
    JSON.stringify(
      analyze(dataset, observations, cardinality, audit, nativeRun),
      null,
      2,
    ) + "\n",
  );
}

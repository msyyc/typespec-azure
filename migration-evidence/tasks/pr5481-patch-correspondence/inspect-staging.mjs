import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import fs from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";
import { pathToFileURL } from "node:url";

const [tooling, baseline, supplement, comparison, output] = process.argv
  .slice(2)
  .map((value) => path.resolve(value));
const read = (file) => JSON.parse(fs.readFileSync(file, "utf8"));
const sha = (bytes) => createHash("sha256").update(bytes).digest("hex");
const identity = (value) => sha(JSON.stringify(value));
const rule = "PatchPropertiesCorrespondToPutProperties";
const require = createRequire(path.join(tooling, "packages", "typespec-lintdiff", "package.json"));
const { Spectral } = require("@stoplight/spectral-core");
const {
  deleteRulesPropertiesInPayloadNotValidForSpectralRules,
} = require("@microsoft.azure/openapi-validator-rulesets");
const rulesetEntry = require.resolve("@microsoft.azure/openapi-validator-rulesets");
const rulesetRequire = createRequire(rulesetEntry);
const lodash = rulesetRequire("lodash");
const { getAllPropertiesIncludingDeeplyNestedProperties: leaves } = require(
  path.join(path.dirname(rulesetEntry), "spectral", "functions", "utils.js"),
);
const { selectStagingRules, readStagingSupplement } = await import(
  pathToFileURL(
    path.join(tooling, "packages", "typespec-lintdiff", "test", "harness", "staging-supplement.ts"),
  ).href
);
const parent = read(path.join(baseline, "baseline.json"));
const loaded = readStagingSupplement(supplement, parent, [rule]);
const rows = read(path.join(comparison, "projects.json"));
const summary = read(path.join(comparison, "summary.json"));
assert.equal(loaded.identity, summary.supplementIdentity);
assert.equal(identity(parent), summary.parentBaselineIdentity);
for (const receipt of loaded.manifest.runtime.packages) {
  let directory = path.dirname(require.resolve(receipt.name));
  while (!fs.existsSync(path.join(directory, "package.json"))) directory = path.dirname(directory);
  const metadata = read(path.join(directory, "package.json"));
  const files = [];
  function inventory(root, prefix = "") {
    for (const entry of fs.readdirSync(root, { withFileTypes: true })) {
      const relative = prefix ? `${prefix}/${entry.name}` : entry.name;
      if (entry.isDirectory()) inventory(path.join(root, entry.name), relative);
      else
        files.push({
          file: `dist/${relative}`,
          sha256: sha(fs.readFileSync(path.join(root, entry.name))),
        });
    }
  }
  inventory(path.join(directory, "dist"));
  files.sort((a, b) => a.file.localeCompare(b.file));
  files.unshift({
    file: "package.json",
    sha256: sha(fs.readFileSync(path.join(directory, "package.json"))),
  });
  assert.equal(metadata.version, receipt.version);
  assert.equal(identity(files), receipt.contentIdentity);
}
const hashes = new Map(parent.files.map((item) => [item.file.replaceAll("\\", "/"), item.sha256]));
const selected = new Map(
  rows
    .filter((row) => row.swaggerReportedDiagnostics || row.typeSpecReportedDiagnostics)
    .map((row) => [row.project, row]),
);
const results = [];
const suffix =
  " property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties.";
for (const input of loaded.manifest.inputs.filter((item) => selected.has(item.project))) {
  const file = path.join(baseline, "dataset", input.swaggerFile);
  const bytes = fs.readFileSync(file);
  assert.equal(sha(bytes), hashes.get(input.swaggerFile.replaceAll("\\", "/")));
  const ruleset = {
    rules: Object.fromEntries(
      Object.entries(selectStagingRules(loaded.manifest.rules)).map(([name, value]) => [
        name,
        { ...value },
      ]),
    ),
  };
  deleteRulesPropertiesInPayloadNotValidForSpectralRules(ruleset);
  const spectral = new Spectral();
  spectral.setRuleset(ruleset);
  const run = await spectral.runWithResolved({
    parsed: { data: JSON.parse(bytes.toString("utf8")), diagnostics: [], ast: null, lineMap: [] },
    source: file.replaceAll("\\", "/"),
    getLocationForJsonPath: () => undefined,
  });
  assert(run.results.every((item) => loaded.manifest.rules.includes(String(item.code))));
  const observed = run.results
    .filter((item) => item.code === rule)
    .map((item) => ({
      message: item.message,
      path: item.path,
      source: item.source
        ? path.relative(path.join(baseline, "dataset"), item.source).replaceAll("\\", "/")
        : input.swaggerFile,
    }));
  const expected = loaded.members
    .get(rule)
    .filter(
      (item) => item.project === input.project && item.validatorInputFile === input.swaggerFile,
    )
    .map((item) => ({ message: item.message, path: item.path, source: item.swaggerFile }));
  const key = (item) => JSON.stringify(item);
  assert.deepEqual(observed.map(key).sort(), expected.map(key).sort(), input.swaggerFile);
  const operations = [];
  for (const container of ["paths", "x-ms-paths"]) {
    for (const [url, item] of Object.entries(run.resolved[container] ?? {})) {
      if (!item || typeof item !== "object" || !item.patch || !item.put) continue;
      const bodies = (operation) =>
        (operation.parameters ?? []).filter((parameter) => parameter.in === "body");
      const patchBodies = bodies(item.patch);
      const putBodies = bodies(item.put);
      const patchLeaves = patchBodies.length ? leaves(patchBodies[0].schema, []) : [];
      const putLeaves = putBodies.length ? leaves(putBodies[0].schema, []) : [];
      assert(
        Array.isArray(patchLeaves) && Array.isArray(putLeaves),
        `${input.swaggerFile}: malformed body schema`,
      );
      const differences =
        patchBodies.length && putBodies.length
          ? lodash.differenceWith(patchLeaves, putLeaves, lodash.isEqual)
          : [];
      const predicateOccurrences = differences.map((leaf) => {
        const name = Object.keys(leaf)[0];
        const matches = putLeaves.filter((candidate) => Object.hasOwn(candidate, name));
        return {
          name,
          classification: matches.length
            ? "same-name-different-schema"
            : "leaf-name-absent-from-put",
          sameNamedPutCandidates: matches.length,
          differingSchemaKeys: matches.map((candidate) =>
            [...new Set([...Object.keys(leaf[name]), ...Object.keys(candidate[name])])]
              .filter((field) => !lodash.isEqual(leaf[name][field], candidate[name][field]))
              .sort(),
          ),
          message: name + suffix,
        };
      });
      const grouped = new Map();
      for (const occurrence of predicateOccurrences) {
        if (!grouped.has(occurrence.message)) {
          grouped.set(occurrence.message, {
            name: occurrence.name,
            classification: occurrence.classification,
            message: occurrence.message,
            predicateOccurrences: [],
          });
        }
        grouped.get(occurrence.message).predicateOccurrences.push(occurrence);
      }
      const reasons = [...grouped.values()];
      const predicted = !patchBodies.length
        ? ["Patch operations body cannot be empty."]
        : !putBodies.length
          ? ["Non empty patch body with an empty put body is not valid."]
          : reasons.map((reason) => reason.message);
      const actual = expected.filter((diagnostic) =>
        lodash.isEqual(diagnostic.path, [container, url, "patch", "parameters"]),
      );
      assert.deepEqual(
        predicted.sort(),
        actual.map((diagnostic) => diagnostic.message).sort(),
        `${input.swaggerFile}: ${url}`,
      );
      operations.push({
        path: [container, url],
        operationId: item.patch.operationId,
        patchBodyParameters: patchBodies.length,
        putBodyParameters: putBodies.length,
        patchLeafCount: patchLeaves.length,
        putLeafCount: putLeaves.length,
        patchLeafNames: patchLeaves.map((leaf) => Object.keys(leaf)[0]),
        putLeafNames: putLeaves.map((leaf) => Object.keys(leaf)[0]),
        swaggerReportedDiagnostics: actual.length,
        predicateLeafOccurrences: predicateOccurrences.length,
        reasons,
      });
    }
  }
  assert.equal(
    operations.reduce((count, item) => count + item.swaggerReportedDiagnostics, 0),
    expected.length,
  );
  results.push({ project: input.project, swaggerFile: input.swaggerFile, operations });
}
const projectResults = [...selected.values()].map((row) => {
  const inputs = results.filter((input) => input.project === row.project);
  const operations = inputs.flatMap((input) => input.operations);
  return {
    project: row.project,
    swaggerOnly: row.swaggerOnly,
    typeSpecOnly: row.typeSpecOnly,
    swaggerReportedDiagnostics: row.swaggerReportedDiagnostics,
    typeSpecReportedDiagnostics: row.typeSpecReportedDiagnostics,
    retainedSwaggerInputsInspected: inputs.length,
    pairedSwaggerOperationsInspected: operations.length,
    sameNameDifferentSchemaFindings: operations
      .flatMap((item) => item.reasons)
      .filter((item) => item.classification === "same-name-different-schema").length,
    leafNameAbsentFindings: operations
      .flatMap((item) => item.reasons)
      .filter((item) => item.classification === "leaf-name-absent-from-put").length,
    missingPatchBodyFindings: operations.filter((item) => !item.patchBodyParameters).length,
    missingPutBodyFindings: operations.filter(
      (item) => item.patchBodyParameters && !item.putBodyParameters,
    ).length,
    existingEmptyPatchBodies: operations.filter(
      (item) => item.patchBodyParameters && item.patchLeafCount === 0,
    ).length,
    predicateLeafOccurrences: operations.reduce(
      (count, item) => count + item.predicateLeafOccurrences,
      0,
    ),
    reportedLeafDiagnostics: operations.reduce((count, item) => count + item.reasons.length, 0),
    correspondence:
      "No source-target or native-diagnostic correspondence is inferred from Swagger leaf names.",
  };
});
for (const row of projectResults)
  assert.equal(
    row.sameNameDifferentSchemaFindings +
      row.leafNameAbsentFindings +
      row.missingPatchBodyFindings +
      row.missingPutBodyFindings,
    row.swaggerReportedDiagnostics,
  );
assert(!fs.existsSync(output));
fs.writeFileSync(
  output,
  JSON.stringify(
    {
      assessment:
        "Focused replay of saved emitted schemas using unchanged installed predicates; not a new native execution",
      supplementIdentity: loaded.identity,
      packages: loaded.manifest.runtime.packages,
      lodashVersion: rulesetRequire("lodash/package.json").version,
      scope:
        "All retained Swagger inputs for every project with findings on either side, including every one-sided project",
      attributionBoundary:
        "Classification establishes why the Swagger predicate reports each retained emitted leaf. It does not attribute a native diagnostic, align historical source versions, or prove a normalized cross-engine count.",
      aggregationBoundary:
        "Spectral collapses identical reported records at an operation target. Repeated helper returns with the same message are retained under predicateOccurrences, but counted once only when exact replay verifies the sealed reported diagnostics. This is not a new cross-engine normalization.",
      projects: projectResults,
      inputs: results,
    },
    null,
    2,
  ) + "\n",
);
process.stdout.write(
  JSON.stringify(
    {
      projects: projectResults.length,
      inputs: results.length,
      oneSidedProjects: projectResults.filter((item) => item.swaggerOnly || item.typeSpecOnly)
        .length,
      output,
    },
    null,
    2,
  ) + "\n",
);

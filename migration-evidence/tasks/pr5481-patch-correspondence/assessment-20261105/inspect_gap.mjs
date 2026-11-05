import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import fs from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const [tooling, baseline, supplement, output] = process.argv
  .slice(2)
  .map((value) => path.resolve(value));
const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const read = (file) => JSON.parse(fs.readFileSync(file, "utf8"));
const sha = (bytes) => createHash("sha256").update(bytes).digest("hex");
const identity = (value) => sha(JSON.stringify(value));
const replayFile = path.join(root, "staging-comparison", "schema-investigation.json");
const replay = read(replayFile);
const require = createRequire(path.join(tooling, "packages", "typespec-lintdiff", "package.json"));
const { Spectral } = require("@stoplight/spectral-core");
const {
  deleteRulesPropertiesInPayloadNotValidForSpectralRules,
} = require("@microsoft.azure/openapi-validator-rulesets");
const entry = require.resolve("@microsoft.azure/openapi-validator-rulesets");
const rulesetRequire = createRequire(entry);
const lodash = rulesetRequire("lodash");
const { getAllPropertiesIncludingDeeplyNestedProperties: leaves } = require(
  path.join(path.dirname(entry), "spectral", "functions", "utils.js"),
);
const { selectStagingRules, readStagingSupplement } = await import(
  pathToFileURL(
    path.join(tooling, "packages", "typespec-lintdiff", "test", "harness", "staging-supplement.ts"),
  ).href
);
const parent = read(path.join(baseline, "baseline.json"));
const loaded = readStagingSupplement(supplement, parent, [
  "PatchPropertiesCorrespondToPutProperties",
]);
assert.equal(loaded.identity, replay.supplementIdentity);
assert.equal(
  identity(parent),
  read(path.join(root, "refresh-20261104", "staging-comparison", "summary.json"))
    .parentBaselineIdentity,
);
for (const receipt of replay.packages) {
  let directory = path.dirname(require.resolve(receipt.name));
  while (!fs.existsSync(path.join(directory, "package.json"))) directory = path.dirname(directory);
  const files = [];
  function inventory(directory, prefix = "") {
    for (const item of fs.readdirSync(directory, { withFileTypes: true })) {
      const relative = prefix ? `${prefix}/${item.name}` : item.name;
      if (item.isDirectory()) inventory(path.join(directory, item.name), relative);
      else
        files.push({
          file: `dist/${relative}`,
          sha256: sha(fs.readFileSync(path.join(directory, item.name))),
        });
    }
  }
  inventory(path.join(directory, "dist"));
  files.sort((a, b) => a.file.localeCompare(b.file));
  files.unshift({
    file: "package.json",
    sha256: sha(fs.readFileSync(path.join(directory, "package.json"))),
  });
  assert.equal(read(path.join(directory, "package.json")).version, receipt.version);
  assert.equal(identity(files), receipt.contentIdentity);
}
assert.equal(rulesetRequire("lodash/package.json").version, replay.lodashVersion);
const hashes = new Map(parent.files.map((item) => [item.file.replaceAll("\\", "/"), item.sha256]));
const started = Date.now();
const records = [];
const schemaSummary = (schema) => ({
  type: schema.type ?? null,
  readOnly: schema.readOnly ?? false,
  mutability: schema["x-ms-mutability"] ?? null,
  ...(Object.hasOwn(schema, "default") ? { default: schema.default } : {}),
});
let inspectedInputs = 0;
for (const [inputIndex, input] of replay.inputs.entries()) {
  if (
    !input.operations.some((operation) =>
      operation.reasons.some((reason) => reason.classification === "same-name-different-schema"),
    )
  )
    continue;
  assert(Date.now() - started < 540_000, "Saved-schema inspection exceeded its 540-second budget.");
  const file = path.join(baseline, "dataset", input.swaggerFile);
  const bytes = fs.readFileSync(file);
  assert.equal(sha(bytes), hashes.get(input.swaggerFile.replaceAll("\\", "/")));
  const ruleset = {
    rules: Object.fromEntries(
      Object.entries(selectStagingRules(loaded.manifest.rules)).map(([key, value]) => [
        key,
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
  for (const [operationIndex, operation] of input.operations.entries()) {
    const [container, route] = operation.path;
    const item = run.resolved[container][route];
    const bodies = (operation) =>
      (operation.parameters ?? []).filter((parameter) => parameter.in === "body");
    const patch = bodies(item.patch);
    const put = bodies(item.put);
    assert.equal(patch.length, operation.patchBodyParameters);
    assert.equal(put.length, operation.putBodyParameters);
    if (!patch.length || !put.length) continue;
    const putLeaves = leaves(put[0].schema, []);
    const differences = lodash.differenceWith(
      leaves(patch[0].schema, []),
      putLeaves,
      lodash.isEqual,
    );
    for (const [reasonIndex, reason] of operation.reasons.entries()) {
      if (reason.classification !== "same-name-different-schema") continue;
      const occurrences = differences
        .filter((leaf) => Object.keys(leaf)[0] === reason.name)
        .map((leaf) => ({
          patch: schemaSummary(leaf[reason.name]),
          candidates: putLeaves
            .filter((candidate) => Object.hasOwn(candidate, reason.name))
            .map((candidate) => ({
              put: schemaSummary(candidate[reason.name]),
              differingKeys: [
                ...new Set([
                  ...Object.keys(leaf[reason.name]),
                  ...Object.keys(candidate[reason.name]),
                ]),
              ]
                .filter(
                  (key) => !lodash.isEqual(leaf[reason.name][key], candidate[reason.name][key]),
                )
                .sort(),
            })),
        }));
      assert.deepEqual(
        occurrences.map((occurrence) =>
          occurrence.candidates.map((candidate) => candidate.differingKeys),
        ),
        reason.predicateOccurrences.map((occurrence) => occurrence.differingSchemaKeys),
      );
      records.push({
        replayInputIndex: inputIndex,
        replayOperationIndex: operationIndex,
        replayReasonIndex: reasonIndex,
        occurrences,
      });
    }
  }
  inspectedInputs++;
}
assert.equal(
  records.length,
  replay.projects.reduce((sum, project) => sum + project.sameNameDifferentSchemaFindings, 0),
);
assert(!fs.existsSync(output), "Use a new output file; never overwrite captured evidence.");
fs.writeFileSync(
  output,
  JSON.stringify(
    {
      scope:
        "Additional type/mutability/default values for each saved same-name Swagger record; no source compilation, Swagger generation or new native diagnostics.",
      replaySha256: sha(fs.readFileSync(replayFile)),
      extractorSha256: sha(fs.readFileSync(fileURLToPath(import.meta.url))),
      parentBaselineIdentity: identity(parent),
      supplementIdentity: loaded.identity,
      packages: replay.packages,
      lodashVersion: replay.lodashVersion,
      inspectedInputs,
      records,
    },
    null,
    2,
  ) + "\n",
);
console.log(
  JSON.stringify({
    records: records.length,
    inspectedInputs,
    elapsedSeconds: (Date.now() - started) / 1000,
    output,
  }),
);

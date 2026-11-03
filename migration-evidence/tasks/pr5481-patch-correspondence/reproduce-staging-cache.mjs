import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import fs from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";

const [tooling, baseline, output] = process.argv.slice(2).map((value) => path.resolve(value));
const read = (file) => JSON.parse(fs.readFileSync(file, "utf8"));
const require = createRequire(path.join(tooling, "packages", "typespec-lintdiff", "package.json"));
const version = (name) => {
  let directory = path.dirname(require.resolve(name));
  while (!fs.existsSync(path.join(directory, "package.json"))) directory = path.dirname(directory);
  return read(path.join(directory, "package.json")).version;
};
const { Spectral } = require("@stoplight/spectral-core");
const {
  spectralRulesets,
  deleteRulesPropertiesInPayloadNotValidForSpectralRules,
} = require("@microsoft.azure/openapi-validator-rulesets");
const available = { ...spectralRulesets.azCommon.rules, ...spectralRulesets.azARM.rules };
const definitions = Object.fromEntries(
  Object.entries(available)
    .filter(([, rule]) => rule.stagingOnly)
    .map(([name, rule]) => [name, { ...rule }]),
);
const ruleset = { rules: definitions };
deleteRulesPropertiesInPayloadNotValidForSpectralRules(ruleset);
const parent = read(path.join(baseline, "baseline.json"));
const hash = (bytes) => createHash("sha256").update(bytes).digest("hex");
assert.equal(
  hash(JSON.stringify(parent)),
  "aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995",
);
const inputs = parent.projects.flatMap((project) =>
  project.swaggerFiles.map((swaggerFile) => ({ project: project.sourcePath, swaggerFile })),
);
const hashes = new Map(parent.files.map((item) => [item.file.replaceAll("\\", "/"), item.sha256]));
const results = [];
for (const mode of ["shared-resolver", "isolated-resolver"]) {
  let spectral;
  const outcomes = [];
  for (const index of [11, 12]) {
    if (!spectral || mode === "isolated-resolver") {
      spectral = new Spectral();
      spectral.setRuleset(ruleset);
    }
    const input = inputs[index];
    const file = path.join(baseline, "dataset", input.swaggerFile);
    const bytes = fs.readFileSync(file);
    assert.equal(hash(bytes), hashes.get(input.swaggerFile.replaceAll("\\", "/")));
    try {
      const diagnostics = await spectral.run({
        parsed: {
          data: JSON.parse(bytes.toString("utf8")),
          diagnostics: [],
          ast: null,
          lineMap: [],
        },
        source: file.replaceAll("\\", "/"),
        getLocationForJsonPath: () => undefined,
      });
      assert(diagnostics.every((item) => Object.hasOwn(definitions, item.code)));
      outcomes.push({ index, ...input, status: "success", diagnostics: diagnostics.length });
    } catch (error) {
      outcomes.push({
        index,
        ...input,
        status: "failed",
        error: String(error),
        stack: String(error.stack)
          .replaceAll(tooling, "$TOOLING_ROOT")
          .replaceAll(baseline, "$BASELINE"),
      });
    }
  }
  results.push({ mode, outcomes });
}
assert.equal(results[0].outcomes[0].status, "success");
assert.match(results[0].outcomes[1].error, /Maximum call stack size exceeded/);
assert(results[1].outcomes.every((item) => item.status === "success"));
assert(!fs.existsSync(output));
fs.writeFileSync(
  output,
  JSON.stringify(
    {
      assessment:
        "Real frozen-corpus regression: shared resolver fails; isolated resolvers succeed",
      parentBaselineIdentity: hash(JSON.stringify(parent)),
      rules: Object.keys(definitions).sort(),
      nodeVersion: process.version,
      rulesetsVersion: version("@microsoft.azure/openapi-validator-rulesets"),
      spectralCoreVersion: version("@stoplight/spectral-core"),
      outcomes: results,
      allAssertionsPassed: true,
    },
    null,
    2,
  ) + "\n",
);
process.stdout.write(
  "Verified shared-resolver failure and isolated-resolver success for both frozen inputs.\n",
);

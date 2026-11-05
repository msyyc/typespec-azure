import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const self = fileURLToPath(import.meta.url);
const root = path.dirname(path.dirname(self));
let source = fs.readFileSync(path.join(root, "assessment-20261105", "inspect_gap.mjs"), "utf8");
const replace = (before, after) => {
  assert.equal(source.split(before).length, 2, `Expected one extraction site: ${before}`);
  source = source.replace(before, after);
};
replace(
  "const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));",
  `const root = ${JSON.stringify(root)};`,
);
replace(
  "const records = [];",
  `const records = [];
const assessment = read(path.join(root, "assessment-20261105", "results.json"));
const selected = new Set(assessment.projects.flatMap(project =>
  project.swaggerAssessments.filter(record => record.gapCategory === "remaining-schema-difference")
    .map(record => [record.replayInputIndex, record.replayOperationIndex, record.replayReasonIndex].join("/"))));
assert.equal(selected.size, 131);
const selectedInputs = new Set([...selected].map(key => Number(key.split("/")[0])));`,
);
replace(
  `const schemaSummary = (schema) => ({
  type: schema.type ?? null,
  readOnly: schema.readOnly ?? false,
  mutability: schema["x-ms-mutability"] ?? null,
  ...(Object.hasOwn(schema, "default") ? { default: schema.default } : {}),
});`,
  `const schemaSummary = (schema, visiting = new Set()) => {
  if (schema === null || typeof schema !== "object") return schema;
  if (visiting.has(schema)) return { $recursive: true };
  visiting.add(schema);
  const result = Array.isArray(schema)
    ? schema.map(value => schemaSummary(value, visiting))
    : Object.fromEntries(Object.entries(schema)
      .filter(([key]) => !["description", "title", "externalDocs", "default", "example", "examples"].includes(key))
      .map(([key, value]) => [key, schemaSummary(value, visiting)]));
  visiting.delete(schema);
  return result;
};`,
);
replace(
  "for (const [inputIndex, input] of replay.inputs.entries()) {",
  `for (const [inputIndex, input] of replay.inputs.entries()) {
  if (!selectedInputs.has(inputIndex)) continue;`,
);
replace(
  'if (reason.classification !== "same-name-different-schema") continue;',
  `if (!selected.has([inputIndex, operationIndex, reasonIndex].join("/"))) continue;`,
);
replace(
  "replay.projects.reduce((sum, project) => sum + project.sameNameDifferentSchemaFindings, 0),",
  "selected.size,",
);
replace(
  "sha(fs.readFileSync(fileURLToPath(import.meta.url)))",
  `sha(fs.readFileSync(${JSON.stringify(self)}))`,
);
replace(
  "Additional type/mutability/default values for each saved same-name Swagger record; no source compilation, Swagger generation or new native diagnostics.",
  "Resolved schemas for all131retained same-name Swagger records. Annotation/default/example fields omitted, recursive graph boundaries explicit. Exact pinned resolver/helper comparisons verified; no source compilation, Swagger generation, semantic disposition or source-warning attribution.",
);
await import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);

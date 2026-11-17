import assert from "node:assert/strict";
import fs from "node:fs";
import { fileURLToPath } from "node:url";

const original = new URL("../wrapper-20261110/capture-source.mjs", import.meta.url);
let source = fs.readFileSync(original, "utf8");
function replace(before, after) {
  assert.equal(source.split(before).length, 2, before);
  source = source.replace(before, after);
}
replace(
  `  const compatibilityFile = path.join(
    path.dirname(bodyFile),
    "arm-resource-patch-compatibility.js",
  );
  const { createPatchPropertyCompatibility } = await import(pathToFileURL(compatibilityFile).href);
`,
  "",
);
replace(
  "          const compatible = createPatchPropertyCompatibility(program, metadata, patch, put);\n",
  "",
);
replace(
  `            const accepted = candidates.some(
              (candidate) =>
                (leaf.recursive && candidate.recursive) ||
                compatible(leaf.property, candidate.property),
            );
            const family = accepted
              ? null
              : candidates.length
                ? "incompatibleProperty"
                : "missingProperty";
            const message =
              family === "missingProperty"
                ? \`The property '\${leaf.jsonName}' in the PATCH body does not correspond to a property in the PUT body.\`
                : family === "incompatibleProperty"
                  ? \`The property '\${leaf.jsonName}' in the PATCH body must have a type and constraints compatible with its corresponding PUT property.\`
                  : null;`,
  `            const family = candidates.length > 0 ? null : "missingProperty";
            const message = family
              ? \`The property '\${leaf.jsonName}' in the PATCH body does not correspond to a property in the PUT body.\`
              : null;`,
);
replace(
  '"Installed production collector exposed without behavior changes; installed production compatibility predicate. Route grouping, overload/project filtering and finite encoded-path candidate selection match the owning listener. PUT candidate targets describe source locations, not emitted diagnostics."',
  '"Installed production collector/path lookup exposed without behavior changes. Candidate presence only: property types and constraints are not evaluated. Route grouping and project/overload filters match the listener. Acceptance is not proof of value compatibility."',
);
replace(
  "        compatibilityModuleSha256: sha(fs.readFileSync(compatibilityFile)),\n",
  '        comparisonPolicy: "name-and-body-only; value compatibility not evaluated",\n',
);
replace(
  "extractorSha256: sha(fs.readFileSync(fileURLToPath(import.meta.url))),",
  `extractorSha256: sha(fs.readFileSync(${JSON.stringify(fileURLToPath(import.meta.url))})),
        captureBaseSha256: sha(fs.readFileSync(${JSON.stringify(fileURLToPath(original))})),`,
);
export const { capture } = await import(
  `data:text/javascript;base64,${Buffer.from(source).toString("base64")}`
);

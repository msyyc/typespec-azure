import assert from "node:assert/strict";
import fs from "node:fs";
import { fileURLToPath } from "node:url";

let source = fs.readFileSync(
  new URL("../direct-20261112/capture-controls.mjs", import.meta.url),
  "utf8",
);
const worker = fileURLToPath(new URL("source-worker.mjs", import.meta.url));
const replacements = [
  [
    'const worker = fileURLToPath(new URL("source-worker.mjs", import.meta.url));',
    `const worker = ${JSON.stringify(worker)};`,
  ],
  [
    'import { observeContext } from "../wrapper-20261110/join-contexts.mjs";',
    `import { observeContext } from ${JSON.stringify(new URL("../wrapper-20261110/join-contexts.mjs", import.meta.url).href)};`,
  ],
  ['"incompatibleProperty", true, false', "null, false, false"],
  [
    '["suppressed-constraint", "incompatibleProperty", false, true]',
    '["suppressed-missing-name", "missingProperty", false, true]',
  ],
];
for (const [before, after] of replacements) {
  assert.equal(source.split(before).length - 1, before.includes("true, false") ? 4 : 1);
  source = source.replaceAll(before, after);
}
await import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);

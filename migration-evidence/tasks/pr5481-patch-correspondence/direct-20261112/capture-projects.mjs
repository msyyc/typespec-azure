import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const original = new URL("../wrapper-20261110/capture-projects.mjs", import.meta.url);
const source = fs.readFileSync(original, "utf8");
const before = "const here = path.dirname(fileURLToPath(import.meta.url));";
assert.equal(source.split(before).length, 2);
const here = path.dirname(fileURLToPath(import.meta.url));
await import(
  `data:text/javascript;base64,${Buffer.from(source.replace(before, `const here = ${JSON.stringify(here)};`)).toString("base64")}`
);

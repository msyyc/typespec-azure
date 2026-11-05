import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
const input = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const worker = path.join(
  input.toolingRepo,
  "packages",
  "typespec-lintdiff",
  "test",
  "harness",
  "native-coverage-worker.mjs",
);
let source = fs.readFileSync(worker, "utf8");
const before = 'if (scope === "source") {\n    return {';
assert.equal(source.split(before).length, 2);
const capture = pathToFileURL(
  path.join(path.dirname(fileURLToPath(import.meta.url)), "capture-source.mjs"),
).href;
source = source.replace(
  before,
  `if (scope === "source") {
    await (await import(${JSON.stringify(capture)})).capture(program, compiler, packages, input, rawDiagnostics, location);
    return {`,
);
await import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);

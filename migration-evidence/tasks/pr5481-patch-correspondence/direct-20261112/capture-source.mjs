import assert from "node:assert/strict";
import fs from "node:fs";
import { fileURLToPath } from "node:url";

const original = new URL("../wrapper-20261110/capture-source.mjs", import.meta.url);
const previous = "must have a type and constraints compatible with its corresponding PUT property.";
const current = "must preserve the format and bounds of its corresponding PUT property.";
let source = fs.readFileSync(fileURLToPath(original), "utf8");
assert.equal(source.split(previous).length, 2);
const originalHash = "extractorSha256: sha(fs.readFileSync(fileURLToPath(import.meta.url))),";
assert.equal(source.split(originalHash).length, 2);
source = source.replace(
  originalHash,
  `extractorSha256: sha(fs.readFileSync(${JSON.stringify(fileURLToPath(import.meta.url))})),
   captureBaseSha256: sha(fs.readFileSync(${JSON.stringify(fileURLToPath(original))})),`,
);
const module = await import(
  `data:text/javascript;base64,${Buffer.from(source.replace(previous, current)).toString("base64")}`
);
export const capture = module.capture;

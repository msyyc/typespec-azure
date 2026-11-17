import assert from "node:assert/strict";
import fs from "node:fs";

let source = fs.readFileSync(
  new URL("../direct-20261112/doc-examples.mjs", import.meta.url),
  "utf8",
);
const before =
  "The property 'displayName' in the PATCH body must preserve the format and bounds of its corresponding PUT property.";
assert.equal(source.split(before).length, 2);
source = source.replace(
  before,
  "The property 'extra' in the PATCH body does not correspond to a property in the PUT body.",
);
await import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);

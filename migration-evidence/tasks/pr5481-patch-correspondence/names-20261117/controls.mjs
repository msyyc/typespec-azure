import assert from "node:assert/strict";
import fs from "node:fs";

let source = fs.readFileSync(new URL("../direct-20261112/controls.mjs", import.meta.url), "utf8");
function replace(before, after, count = 1) {
  assert.equal(source.split(before).length - 1, count, before);
  source = source.replaceAll(before, after);
}
replace(
  `const mismatch = (name) =>
  \`The property '\${name}' in the PATCH body must preserve the format and bounds of its corresponding PUT property.\`;
`,
  "",
);
replace(
  `source: constraintSource,
    messages: [mismatch("value")],`,
  `source: pair("name?: string;", "extra?: string;"),
    messages: [missing("extra")],`,
  3,
);
replace('messages: [mismatch("value")]', "messages: []", 4);
replace(
  `name: "suppressed-constraint",
    source: pair(
      "@maxLength(256) value?: string;",
      \`#suppress "\${rule}" "Intentional exception."\\nvalue?: string;\`,
    ),`,
  `name: "suppressed-missing-name",
    source: pair(
      "name?: string;",
      \`#suppress "\${rule}" "Intentional exception."\\nextra?: string;\`,
    ),`,
);
await import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);

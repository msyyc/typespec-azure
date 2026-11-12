import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { createHash } from "node:crypto";
import fs from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";
import { pathToFileURL } from "node:url";

const [local, candidate, specs, tooling] = process.argv
  .slice(2)
  .map((value) => path.resolve(value));
const website = createRequire(path.join(candidate, "website", "package.json"));
const markdown = createRequire(website.resolve("@astrojs/markdown-remark"));
const { unified } = await import(pathToFileURL(markdown.resolve("unified")).href);
const { default: remarkParse } = await import(pathToFileURL(markdown.resolve("remark-parse")).href);
const document = path.join(
  candidate,
  "packages",
  "typespec-azure-resource-manager",
  "src",
  "rules",
  "arm-resource-patch.md",
);
const bytes = fs.readFileSync(document);
const tree = unified().use(remarkParse).parse(bytes.toString("utf8"));
const snippets = new Map();
let section = "";
for (const node of tree.children) {
  if (node.type === "heading" && node.depth === 2) {
    section = node.children.map((child) => child.value ?? "").join("");
  }
  if (node.type === "code" && node.lang === "tsp" && /Incorrect|Correct/.test(section)) {
    const key = section.includes("Incorrect") ? "incorrect" : "correct";
    assert(!snippets.has(key), `Ambiguous ${key} example`);
    snippets.set(key, node.value);
  }
}
assert(snippets.has("incorrect") && snippets.has("correct"));
const output = path.join(local, "documentation");
assert(!fs.existsSync(output));
fs.mkdirSync(output);
fs.symlinkSync(path.join(specs, "node_modules"), path.join(output, "node_modules"), "junction");
const rule = "@azure-tools/typespec-azure-resource-manager/arm-resource-patch";
const receipts = [];
for (const [name, source] of snippets) {
  const directory = path.join(output, name);
  fs.mkdirSync(directory);
  fs.writeFileSync(path.join(directory, "main.tsp"), source + "\n");
  fs.writeFileSync(path.join(directory, "tspconfig.yaml"), "{}\n");
  const input = {
    specsRepo: specs,
    project: { sourcePath: directory },
    tspRules: [rule],
    validatorRule: "PatchPropertiesCorrespondToPutProperties",
    scope: "source",
    nativeMode: "target-only",
  };
  const inputFile = path.join(directory, "input.json"),
    outputFile = path.join(directory, "output.json");
  fs.writeFileSync(inputFile, JSON.stringify(input) + "\n");
  const result = spawnSync(
    process.execPath,
    [
      path.join(
        tooling,
        "packages",
        "typespec-lintdiff",
        "test",
        "harness",
        "native-coverage-worker.mjs",
      ),
      inputFile,
      outputFile,
    ],
    { encoding: "utf8", timeout: 120000, maxBuffer: 8 * 1024 * 1024 },
  );
  fs.writeFileSync(
    path.join(directory, "worker.log"),
    `${result.stdout ?? ""}\n${result.stderr ?? ""}`,
  );
  assert.ifError(result.error);
  assert.equal(result.status, 0);
  const receipt = JSON.parse(fs.readFileSync(outputFile, "utf8"));
  assert.equal(receipt.status, "success", JSON.stringify(receipt));
  assert(receipt.ambientDiagnostics.every((value) => value.severity !== "error"));
  const expected =
    name === "incorrect"
      ? [
          "The property 'displayName' in the PATCH body must preserve the format and bounds of its corresponding PUT property.",
        ]
      : [];
  assert.deepEqual(
    receipt.rawDiagnostics.map((value) => value.message),
    expected,
  );
  receipts.push({ name, source, receipt });
}
fs.writeFileSync(
  path.join(output, "summary.json"),
  JSON.stringify(
    {
      document: "packages/typespec-azure-resource-manager/src/rules/arm-resource-patch.md",
      documentSha256: createHash("sha256").update(bytes).digest("hex"),
      extraction:
        "Existing website unified/remark-parse AST; unambiguous semantic Incorrect/Correct sections. One-time execution, not a bespoke Markdown parser or continuous unit-test harness.",
      setup:
        "No changes or injected imports in either published snippet. Explicit target-only registered-rule execution through the existing native worker.",
      audience:
        "ARM resource authors; ArmResourceCreateOrReplaceSync and ArmCustomPatchSync with PatchModel customization.",
      receipts,
    },
    null,
    2,
  ) + "\n",
);
console.log("Both actual published ARM examples passed their diagnostic contrast");

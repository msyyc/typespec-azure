import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { createHash } from "node:crypto";
import { execFileSync } from "node:child_process";
import { pathToFileURL } from "node:url";

const root = String.raw`$NATIVE`;
const tool = String.raw`$TOOLING\packages\typespec-lintdiff\test\harness\native-coverage.ts`;
const { snapshot, packedFileInventory } = await import(pathToFileURL(tool).href);
const sha = (bytes) => createHash("sha256").update(bytes).digest("hex");
const mode = process.argv[2];
const plan = JSON.parse(fs.readFileSync(path.join(import.meta.dirname, "artifact-plan-and-baseline-readout.json"), "utf8"));
const current = snapshot(root, true);
const approved = JSON.parse(fs.readFileSync(String.raw`$SESSION\files\scope-cycle0-content-manifest.json`, "utf8"));
assert.deepEqual(current.changedFiles, approved.files.map(({ file, sha256 }) => ({ file, sha256 })));
assert.equal(execFileSync("git", ["-C", path.join(root, "core"), "status", "--porcelain"], { encoding: "utf8" }).trim(), "");
const beforeFile = path.join(import.meta.dirname, "candidate-source-before-artifacts.json");
if (mode === "before") {
  assert.ok(!fs.existsSync(beforeFile), "Do not replace previous immutable source proof");
  fs.writeFileSync(beforeFile, JSON.stringify({ capturedAt: new Date().toISOString(), candidate: current, coreCommit: execFileSync("git", ["-C", path.join(root, "core"), "rev-parse", "HEAD"], { encoding: "utf8" }).trim(), closure: plan.closure }, null, 2) + "\n");
  console.log(JSON.stringify({ status: "captured", candidateContentIdentity: sha(JSON.stringify(current)), files: current.changedFiles.length }));
} else if (mode === "after") {
  const before = JSON.parse(fs.readFileSync(beforeFile, "utf8"));
  assert.deepEqual(current, before.candidate, "Build/pack must preserve exact tested source");
  const directory = path.join(import.meta.dirname, "packages");
  const archives = fs.readdirSync(directory).filter((file) => file.endsWith(".tgz")).sort();
  assert.equal(archives.length, plan.closure.length);
  const artifacts = archives.map((file) => {
    const bytes = fs.readFileSync(path.join(directory, file));
    const files = packedFileInventory(bytes);
    if (file.startsWith("azure-tools-typespec-azure-resource-manager-")) {
      assert.ok(files.some((item) => item.file === "package/dist/src/rules/use-scope-path-standard-name.js"));
      assert.ok(!files.some((item) => item.file.includes("/resource-group-path-parameter.")), "No obsolete generated rule remains packed");
      for (const relative of ["dist/src/rules/use-scope-path-standard-name.js", "dist/src/linter.js", "dist/src/index.js"]) {
        assert.equal(files.find((item) => item.file === `package/${relative}`)?.sha256, sha(fs.readFileSync(path.join(root, "packages", "typespec-azure-resource-manager", relative))));
      }
    }
    return { file, sha256: sha(bytes), bytes: bytes.length, files };
  });
  const receipt = { capturedAt: new Date().toISOString(), source: before, candidateContentIdentity: sha(JSON.stringify(current)), artifacts };
  fs.writeFileSync(path.join(import.meta.dirname, "artifact-provenance.json"), JSON.stringify(receipt, null, 2) + "\n");
  console.log(JSON.stringify({ status: "verified", candidateContentIdentity: receipt.candidateContentIdentity, artifacts: archives.length, bytes: artifacts.reduce((n, item) => n + item.bytes, 0) }));
} else {
  throw new Error("Expected before or after");
}

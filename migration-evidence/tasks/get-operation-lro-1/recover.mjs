import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { createHash } from "node:crypto";
import * as fs from "node:fs";
import * as path from "node:path";

const [evidenceArgument, outputArgument] = process.argv.slice(2);
assert(
  evidenceArgument && outputArgument,
  "Usage: node recover.mjs EVIDENCE_TASK_ROOT NEW_INPUT_DIRECTORY",
);
const evidence = path.resolve(evidenceArgument);
const output = path.resolve(outputArgument);
assert(output.toLowerCase().startsWith("c:\\dev\\worktrees\\"));
assert(!fs.existsSync(output), "Never overwrite an earlier recovery");
const read = (file) => JSON.parse(fs.readFileSync(file, "utf8"));
const sha = (bytes) => createHash("sha256").update(bytes).digest("hex");
const run = (command, args, options = {}) =>
  execFileSync(command, args, {
    cwd: evidence,
    maxBuffer: 128 * 1024 * 1024,
    encoding: "utf8",
    ...options,
  }).trim();
const git = (root, args, options = {}) => run("git", ["-C", root, ...args], options);
const plan = read(path.join(evidence, "recovery-plan.json"));
const publication = read(path.join(evidence, "publication.json"));
const task = read(path.join(evidence, "task.json"));
const checkout = git(evidence, ["rev-parse", "--show-toplevel"]);
const E = git(checkout, ["rev-parse", "HEAD"]);
assert.equal(git(checkout, ["status", "--porcelain"]), "");
const inventory = read(path.join(evidence, "publication-inventory.json"));
for (const item of inventory.files) {
  const actual = fs.readFileSync(path.join(evidence, item.file));
  assert.equal(actual.length, item.bytes, item.file);
  assert.equal(sha(actual), item.sha256, item.file);
  const blob = execFileSync(
    "git",
    ["-C", checkout, "show", `${E}:migration-evidence/tasks/get-operation-lro-1/${item.file}`],
    { maxBuffer: 16 * 1024 * 1024 },
  );
  assert.equal(sha(blob), item.sha256, item.file);
}
fs.mkdirSync(output, { recursive: true });
const step = (message) => process.stdout.write(`${new Date().toISOString()} ${message}\n`);
const downloads = path.join(output, "downloads");
fs.mkdirSync(downloads);
function download(repository, release, file, expected) {
  run("gh", [
    "release",
    "download",
    release,
    "--repo",
    repository,
    "--pattern",
    file,
    "--dir",
    downloads,
  ]);
  const target = path.join(downloads, file);
  const bytes = fs.readFileSync(target);
  assert.equal(bytes.length, expected.bytes, file);
  assert.equal(sha(bytes), expected.sha256, file);
  step(`Downloaded and verified ${file}`);
  return target;
}
function extract(archive, directory) {
  const members = run("tar", ["-tf", archive]).split(/\r?\n/).filter(Boolean);
  for (const member of members) {
    assert(!path.isAbsolute(member) && !/^[A-Za-z]:/.test(member));
    assert(!member.replaceAll("\\", "/").split("/").includes(".."));
  }
  fs.mkdirSync(directory, { recursive: true });
  run("tar", ["-xf", archive, "-C", directory]);
  return members.filter((member) => !member.endsWith("/")).length;
}
const candidate = path.join(output, "candidate");
const packageRoot = path.join(output, "packages");
const runtime = path.join(output, "runtime");
const sourceMembers = {};
for (const asset of publication.publishedAssets.assets) {
  const archive = download(
    publication.publishedAssets.repository,
    publication.publishedAssets.release,
    asset.file,
    asset,
  );
  const destination =
    asset.file === "candidate-source.tar"
      ? candidate
      : asset.file === "candidate-core-source.tar"
        ? path.join(candidate, "core")
        : asset.file === "candidate-packages.tar.gz"
          ? packageRoot
          : runtime;
  sourceMembers[asset.file] = extract(archive, destination);
}
const immutable = read(path.join(runtime, "attestations", "immutable-source-receipt.json"));
for (const item of immutable.sourceInventory) {
  assert.equal(sha(fs.readFileSync(path.join(candidate, item.file))), item.sha256, item.file);
}
assert.equal(immutable.sourceInventory.length, 19664);
const packed = read(path.join(evidence, "proof", "package-closure.json"));
let packedFiles = 0;
for (const item of packed.artifacts) {
  const archive = path.join(packageRoot, item.artifact);
  const bytes = fs.readFileSync(archive);
  assert.equal(bytes.length, item.bytes);
  assert.equal(sha(bytes), item.sha256);
  const destination = path.join(output, "expanded-packages", item.name.replaceAll("/", "+"));
  extract(archive, destination);
  for (const file of item.files) {
    assert.equal(
      sha(fs.readFileSync(path.join(destination, "package", file.file))),
      file.sha256,
      `${item.name}/${file.file}`,
    );
    packedFiles++;
  }
  assert.equal(
    sha(fs.readFileSync(path.join(destination, "package", "package.json"))),
    item.packedManifestSha256,
  );
}
assert.equal(packed.artifacts.length, 17);
const runtimeInventory = read(path.join(runtime, "inventory.json"));
for (const item of runtimeInventory.files) {
  assert.equal(
    sha(fs.readFileSync(path.join(runtime, item.file))),
    item.sanitizedSha256,
    item.file,
  );
}
assert.equal(
  runtimeInventory.files.filter((item) => /^run\/native-\d+\.json$/.test(item.file)).length,
  487,
);
step("All source/package/runtime members verified");
const metadataRef = "refs/recovery/baseline-metadata";
git(checkout, [
  "fetch",
  "--no-tags",
  "--depth=1",
  "--filter=blob:none",
  plan.specs.repository,
  `${plan.baseline.metadataCommit}:${metadataRef}`,
]);
const descriptor = JSON.parse(
  git(checkout, ["show", `${metadataRef}:${plan.baseline.descriptorPath}`]),
);
assert.equal(descriptor.baselineIdentity, plan.baseline.baselineIdentity);
assert.deepEqual(descriptor.archive, plan.baseline.archive);
const baselineArchive = download(
  descriptor.archive.repository,
  descriptor.archive.release,
  descriptor.archive.name,
  descriptor.archive,
);
const baselineRoot = path.join(output, "baseline");
sourceMembers.baseline = extract(baselineArchive, baselineRoot);
const baseline = read(path.join(baselineRoot, "baseline.json"));
const seal = read(path.join(baselineRoot, "manifest.json"));
assert.equal(sha(JSON.stringify(baseline)), descriptor.baselineIdentity);
assert.equal(seal.baselineIdentity, descriptor.baselineIdentity);
assert.equal(seal.status, "complete");
assert.equal(seal.nativeAssessment, "not-run");
assert.equal(baseline.projects.length, 487);
const baselineNames = new Set(baseline.files.map((item) => item.file.replaceAll("\\", "/")));
let visited = 0;
function verifyDataset(directory, prefix = "") {
  for (const item of fs.readdirSync(directory, { withFileTypes: true })) {
    const relative = prefix ? `${prefix}/${item.name}` : item.name;
    const file = path.join(directory, item.name);
    if (item.isDirectory()) verifyDataset(file, relative);
    else {
      assert(item.isFile() && baselineNames.has(relative), relative);
      visited++;
    }
  }
}
for (const [index, item] of baseline.files.entries()) {
  assert.equal(
    sha(fs.readFileSync(path.join(baselineRoot, "dataset", item.file))),
    item.sha256,
    item.file,
  );
  if (index % 10000 === 0) step(`Baseline integrity ${index}/${baseline.files.length}`);
}
verifyDataset(path.join(baselineRoot, "dataset"));
assert.equal(visited, baselineNames.size);
git(checkout, [
  "fetch",
  "--no-tags",
  "--depth=1",
  "--filter=blob:none",
  plan.native.repository,
  `${plan.native.C}:refs/recovery/native`,
]);
assert.equal(git(checkout, ["rev-parse", `${plan.native.C}^{tree}`]), plan.native.tree);
assert(git(checkout, ["ls-tree", plan.native.C, "core"]).includes(plan.native.coreCommit));
git(checkout, [
  "fetch",
  "--no-tags",
  "--depth=1",
  "--filter=blob:none",
  plan.native.coreRepository,
  `${plan.native.coreCommit}:refs/recovery/compiler`,
]);
assert.equal(git(checkout, ["rev-parse", "refs/recovery/compiler"]), plan.native.coreCommit);
const sparse = (directory, repository, commit, paths) => {
  fs.mkdirSync(directory);
  run("git", ["init", directory]);
  git(directory, ["remote", "add", "origin", repository]);
  git(directory, ["config", "core.longpaths", "true"]);
  git(directory, ["sparse-checkout", "init", "--cone"]);
  git(directory, ["sparse-checkout", "set", "--stdin"], { input: paths.join("\n") + "\n" });
  git(directory, ["fetch", "--no-tags", "--depth=1", "--filter=blob:none", "origin", commit]);
  git(directory, ["checkout", "--detach", "FETCH_HEAD"]);
  assert.equal(git(directory, ["rev-parse", "HEAD"]), commit);
};
const specsRef = JSON.parse(
  run("gh", [
    "api",
    `repos/msyyc/azure-rest-api-specs/git/ref/heads/${plan.specs.preservationRef}`,
  ]),
);
assert.equal(specsRef.object.sha, plan.specs.commit);
const specs = path.join(output, "specs");
sparse(specs, plan.specs.repository, plan.specs.commit, [
  ...new Set([
    ...baseline.projects.map((project) => project.sourcePath),
    "specification/common-types",
    "eng",
  ]),
]);
const tooling = path.join(output, "tooling");
sparse(tooling, plan.tooling.repository, plan.tooling.commit, [
  "packages/typespec-lintdiff",
  ".github/skills/analyze-native-lint-coverage",
  "eng",
]);
const sourceIdentity = read(path.join(evidence, "proof", "source-identity.json"));
for (const item of sourceIdentity.sourceFiles) {
  const blob = execFileSync("git", ["-C", checkout, "show", `${plan.native.C}:${item.file}`], {
    maxBuffer: 16 * 1024 * 1024,
  });
  assert.equal(sha(blob), item.sha256, item.file);
}
step(
  "Pinned native/compiler/specs/tooling inputs independently restored; no dependency setup or native rerun",
);
const replay = path.join(output, "saved-observation-replay");
run(process.execPath, [path.join(evidence, "replay.mjs"), evidence, replay]);
assert.equal(
  sha(fs.readFileSync(path.join(replay, "migration.md"))),
  sha(fs.readFileSync(path.join(evidence, "migration.md"))),
);
const counts = read(path.join(replay, "replay-summary.json")).counts;
assert.equal(counts.selectedProjectCount, 487);
assert.equal(counts.validatorRawCount, 4);
assert.equal(counts.nativeRawCount, 4);
assert.equal(counts.rawValidatorExcess + counts.rawNativeExcess, 0);
const receipt = {
  result: "passed",
  observedAt: new Date().toISOString(),
  recoveredEvidenceCommit: E,
  nativeC: plan.native.C,
  nativeTree: plan.native.tree,
  compilerCommit: plan.native.coreCommit,
  specsCommit: plan.specs.commit,
  toolingCommit: plan.tooling.commit,
  baselineMetadataCommit: plan.baseline.metadataCommit,
  baselineIdentity: descriptor.baselineIdentity,
  sourceMembers,
  sourceFilesVerified: immutable.sourceInventory.length,
  packageArchivesVerified: packed.artifacts.length,
  packedFilesVerified: packedFiles,
  packedManifestsVerified: packed.artifacts.length,
  baselineFilesVerified: visited,
  runtimeFilesVerified: runtimeInventory.files.length,
  publicationFilesVerified: inventory.files.length,
  exactReportSha256: sha(fs.readFileSync(path.join(replay, "migration.md"))),
  counts,
  method:
    "Fresh published evidence checkout and remotely downloaded assets/baseline/pinned Git sources. No unpublished original/session files seeded.",
  boundary:
    "Cold saved-observation reanalysis and exact report generation; no second full native487 execution or fresh dependency installation.",
  nativeRule: task.nativeRule,
};
fs.writeFileSync(
  path.join(output, "recovery-receipt.json"),
  JSON.stringify(receipt, null, 2) + "\n",
  { flag: "wx" },
);
process.stdout.write(JSON.stringify(receipt) + "\n");

import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import * as fs from "node:fs";
import { createRequire } from "node:module";
import * as path from "node:path";
import { pathToFileURL } from "node:url";

const [specsRepo, inventoryFile, countsFile, artifactFile, outputFile] = process.argv.slice(2);
const read = (file) => JSON.parse(fs.readFileSync(file, "utf8"));
const inventory = read(inventoryFile);
const counts = read(countsFile);
const artifacts = read(artifactFile);
const rule = "@azure-tools/typespec-client-generator-core/no-redundant-operation-group-name";
const packages = [];
let compiler;
async function load(name) {
  const resolved =
    compiler &&
    (await compiler.resolveModule(
      {
        realpath: fs.promises.realpath,
        stat: fs.promises.stat,
        readFile: (file) => fs.promises.readFile(file, "utf8"),
      },
      name,
      { baseDir: specsRepo, conditions: ["import"] },
    ));
  const entrypoint = fs.realpathSync(
    resolved
      ? resolved.type === "module"
        ? resolved.mainFile
        : resolved.path
      : createRequire(path.join(specsRepo, "package.json")).resolve(name),
  );
  let directory = path.dirname(entrypoint);
  while (true) {
    const manifestFile = path.join(directory, "package.json");
    if (fs.existsSync(manifestFile) && read(manifestFile).name === name) break;
    const parent = path.dirname(directory);
    assert.notEqual(parent, directory);
    directory = parent;
  }
  const member = "package/" + path.relative(directory, entrypoint).replaceAll("\\", "/");
  const artifact = artifacts.packages.find((p) => p.name === name);
  const expected = artifact.files.find((f) => f.path === member);
  const sha256 = createHash("sha256").update(fs.readFileSync(entrypoint)).digest("hex");
  assert.equal(sha256, expected.sha256, name);
  packages.push({
    name,
    version: read(path.join(directory, "package.json")).version,
    member,
    sha256,
  });
  return { module: await import(pathToFileURL(entrypoint).href), entrypoint };
}
compiler = (await load("@typespec/compiler")).module;
const tcgc = await load("@azure-tools/typespec-client-generator-core");
const http = (await load("@typespec/http")).module;
const { AllScopes } = await import(
  pathToFileURL(path.join(path.dirname(tcgc.entrypoint), "internal-utils.js")).href
);
const selected = counts.rows.filter((row) => row.rawDifference !== 0).map((row) => row.project);
const projects = [];
for (const project of selected) {
  assert(inventory.some((p) => p.sourcePath === project));
  const projectDir = path.resolve(specsRepo, project);
  const mainPath = path.join(projectDir, "main.tsp");
  const [options, configDiagnostics] = await compiler.resolveCompilerOptions(compiler.NodeHost, {
    cwd: projectDir,
    entrypoint: mainPath,
    overrides: { emit: [] },
  });
  const program = await compiler.compile(compiler.NodeHost, mainPath, {
    ...options,
    emit: [],
    noEmit: true,
    warningAsError: false,
    linterRuleSet: { enable: { [rule]: true } },
  });
  const errors = [...configDiagnostics, ...program.diagnostics].filter(
    (d) => d.severity === "error",
  );
  assert.equal(errors.length, 0, project + ": " + errors.map((d) => d.message).join("\n"));
  const context = tcgc.module.createTCGCContext(
    program,
    "@azure-tools/typespec-client-generator-core",
    { mutateNamespace: false },
  );
  const operations = [];
  for (const client of context.getClients()) {
    for (const operation of context.getOperationsForClient(client)) {
      if (compiler.isTemplateDeclaration(operation)) continue;
      const source = compiler.getSourceLocation(operation, { locateId: true });
      const position =
        source && !source.isSynthetic
          ? source.file.getLineAndCharacterOfPosition(source.pos)
          : undefined;
      const [httpOperation, diagnostics] = http.getHttpOperation(program, operation);
      operations.push({
        operation: operation.name,
        owner: client.name,
        parent: client.parent?.name ?? null,
        commonMethod: tcgc.module.getLibraryName(context, operation, AllScopes),
        sourceFile: position
          ? path.relative(projectDir, source.file.path).replaceAll("\\", "/")
          : null,
        line: position ? position.line + 1 : null,
        column: position ? position.character + 1 : null,
        path: httpOperation.path,
        verb: httpOperation.verb,
        httpDiagnostics: diagnostics.map((d) => ({
          code: d.code,
          severity: d.severity,
          message: d.message,
        })),
      });
    }
  }
  projects.push({ project, operations });
  console.log(JSON.stringify({ project, inspected: operations.length }));
}
fs.writeFileSync(
  outputFile,
  JSON.stringify(
    { scope: "Read-only semantic metadata investigation, not a corpus rerun", packages, projects },
    null,
    2,
  ) + "\n",
  "utf8",
);

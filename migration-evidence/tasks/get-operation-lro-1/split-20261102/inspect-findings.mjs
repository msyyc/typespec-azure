import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";
import { pathToFileURL } from "node:url";

const [specs, tooling, run, output] = process.argv.slice(2).map((value) => path.resolve(value));
assert(!fs.existsSync(output), "Never overwrite an investigation");
fs.mkdirSync(output, { recursive: true });
const require = createRequire(path.join(specs, "package.json"));
const load = (name) => import(pathToFileURL(require.resolve(name)).href);
const compiler = await load("@typespec/compiler");
const http = await load("@typespec/http");
const core = await load("@azure-tools/typespec-azure-core");
const openapi = await load("@typespec/openapi");
const sdkDirectory = path.dirname(require.resolve("@azure-tools/typespec-client-generator-core"));
const sdk = await import(pathToFileURL(path.join(sdkDirectory, "decorators.js")).href);
const { AllScopes } = await import(
  pathToFileURL(path.join(sdkDirectory, "internal-utils.js")).href
);
const { createTCGCContext } = await import(
  pathToFileURL(path.join(sdkDirectory, "context.js")).href
);
const manifest = JSON.parse(fs.readFileSync(path.join(run, "manifest.json"), "utf8"));
const coverage = JSON.parse(fs.readFileSync(path.join(run, "coverage.json"), "utf8"));
assert.equal(manifest.status, "complete");
const observations = coverage.members[0].observations;
const findings = [];
for (const filename of fs.readdirSync(run).filter((name) => /^native-\d+\.json$/.test(name))) {
  const receipt = JSON.parse(fs.readFileSync(path.join(run, filename), "utf8"));
  if (!receipt.rawDiagnostics.length) continue;
  const project = coverage.projects.find((item) => item.project === receipt.project);
  const directory = path.join(specs, receipt.project);
  const [options, diagnostics] = await compiler.resolveCompilerOptions(compiler.NodeHost, {
    cwd: directory,
    entrypoint: path.join(directory, "main.tsp"),
    overrides: { emit: [] },
  });
  assert(!diagnostics.some((item) => item.severity === "error"));
  const program = await compiler.compile(compiler.NodeHost, path.join(directory, "main.tsp"), {
    ...options,
    emit: [],
    noEmit: true,
    warningAsError: false,
    linterRuleSet: {},
  });
  assert(!program.diagnostics.some((item) => item.severity === "error"));
  const context = createTCGCContext(program, "@azure-tools/typespec-client-generator-core", {
    mutateNamespace: false,
  });
  const [services] = http.getAllHttpServices(program);
  const operations = services.flatMap((service) => service.operations);
  const id = (item) => JSON.stringify([item.sourceFile, item.line, item.column]);
  const location = (operation) => {
    const source = compiler.getSourceLocation(operation, { locateId: true });
    const position = source.file.getLineAndCharacterOfPosition(source.pos);
    return {
      sourceFile: path.relative(directory, source.file.path).replaceAll("\\", "/"),
      line: position.line + 1,
      column: position.character + 1,
    };
  };
  const input = path.join(output, filename.replace(".json", "-input.json"));
  const aligned = path.join(output, filename);
  fs.writeFileSync(
    input,
    JSON.stringify({
      specsRepo: specs,
      project: { sourcePath: receipt.project, apiVersion: project.apiVersion },
      validatorRule: "GetOperationMustNotBeLongRunning",
      tspRules: manifest.config.tspRules,
      nativeMode: "target-only",
      scope: "http-reachable",
    }),
  );
  const child = spawnSync(
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
      input,
      aligned,
    ],
    { encoding: "utf8", timeout: 240_000 },
  );
  assert(!child.error, child.error?.message);
  assert.equal(child.status, 0, child.stderr);
  const projected = JSON.parse(fs.readFileSync(aligned, "utf8"));
  assert.equal(projected.status, "success", JSON.stringify(projected));
  assert.deepEqual(projected.rawDiagnostics, receipt.rawDiagnostics);
  const selected = new Set(projected.diagnostics.map(id));
  const swaggerRoot = path.join(run, "dataset", "projects", receipt.project, "swagger");
  const documents = fs
    .readdirSync(swaggerRoot, { recursive: true })
    .filter((name) => name.endsWith(".json"))
    .map((name) => ({
      file: path
        .relative(path.join(run, "dataset"), path.join(swaggerRoot, name))
        .replaceAll("\\", "/"),
      document: JSON.parse(fs.readFileSync(path.join(swaggerRoot, name), "utf8")),
    }));
  for (const diagnostic of receipt.rawDiagnostics) {
    const matches = operations.filter(
      (operation) => id(location(operation.operation)) === id(diagnostic),
    );
    assert.equal(matches.length, 1, JSON.stringify(diagnostic));
    const operation = matches[0];
    const metadata = core.getLroMetadata(program, operation.operation);
    const extensions = openapi.getExtensions(program, operation.operation);
    const scopes = [
      AllScopes,
      ...Object.keys(program.stateMap(sdk.markAsLroKey).get(operation.operation) ?? {}),
    ]
      .filter((scope) => sdk.getMarkAsLro(context, operation.operation, scope))
      .map((scope) => (scope === AllScopes ? "*" : scope));
    const swagger = documents.flatMap(({ file, document }) =>
      ["paths", "x-ms-paths"].flatMap((container) => {
        const item = document[container]?.[operation.path]?.[operation.verb];
        return item
          ? [
              {
                file,
                container,
                path: operation.path,
                verb: operation.verb,
                operationId: item.operationId,
                flagPresent: Object.hasOwn(item, "x-ms-long-running-operation"),
                flag: item["x-ms-long-running-operation"],
                optionsPresent: Object.hasOwn(item, "x-ms-long-running-operation-options"),
                options: item["x-ms-long-running-operation-options"],
              },
            ]
          : [];
      }),
    );
    const paired = observations.filter(
      (item) =>
        item.project === receipt.project &&
        item.path[1] === operation.path &&
        item.path[2] === operation.verb,
    );
    findings.push({
      project: receipt.project,
      apiVersion: project.apiVersion,
      receipt: filename,
      diagnostic,
      operation: compiler.getTypeName(operation.operation),
      verb: operation.verb,
      path: operation.path,
      nativeLroMetadata: metadata !== undefined,
      acceptedLegacyScopes: scopes,
      rawFlagPresent: extensions.has("x-ms-long-running-operation"),
      rawFlag: extensions.get("x-ms-long-running-operation"),
      rawOptionsPresent: extensions.has("x-ms-long-running-operation-options"),
      rawOptions: extensions.get("x-ms-long-running-operation-options"),
      inSelectedVersionHttpGraph: selected.has(id(diagnostic)),
      swagger,
      paired,
    });
  }
  process.stdout.write(`${receipt.project}: inspected ${receipt.rawDiagnostics.length}\n`);
}
assert.equal(findings.length, coverage.nativeRawCount);
fs.writeFileSync(path.join(output, "findings.json"), JSON.stringify(findings, null, 2) + "\n");
process.stdout.write(
  JSON.stringify({
    inspected: findings.length,
    nativeMetadata: findings.filter((item) => item.nativeLroMetadata).length,
    legacy: findings.filter((item) => item.acceptedLegacyScopes.length).length,
    pairedSwagger: findings.reduce((sum, item) => sum + item.paired.length, 0),
    outsideSelectedVersion: findings.filter((item) => !item.inSelectedVersionHttpGraph).length,
  }) + "\n",
);

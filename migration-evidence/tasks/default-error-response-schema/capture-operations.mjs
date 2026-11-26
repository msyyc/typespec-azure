import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import fs from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";
import { pathToFileURL } from "node:url";

const [specs, proofPath, project, output] = process.argv.slice(2);
const requireSpecs = createRequire(path.join(specs, "package.json"));
const load = (name) => import(pathToFileURL(requireSpecs.resolve(name)).href);
const compiler = await load("@typespec/compiler");
const http = await load("@typespec/http");
const arm = await load("@azure-tools/typespec-azure-resource-manager");
const proof = JSON.parse(fs.readFileSync(proofPath));
const packages = [];
for (const name of [
  "@typespec/compiler",
  "@typespec/http",
  "@azure-tools/typespec-azure-resource-manager",
]) {
  const entrypoint = fs.realpathSync(requireSpecs.resolve(name));
  const artifact = proof.artifacts.find((item) => item.name === name);
  const payload = artifact.payload.find((item) => item.path === "dist/src/index.js");
  const sha256 = createHash("sha256").update(fs.readFileSync(entrypoint)).digest("hex");
  assert.equal(sha256, payload.sha256, name);
  packages.push({ name, version: artifact.version, entrypoint, sha256 });
}
const target = "@azure-tools/typespec-azure-resource-manager/use-standard-error";
const rule = arm.$linter.rules.find((item) => item.name === "use-standard-error");
assert.ok(rule);
const directory = path.resolve(specs, project);
const main = path.join(directory, "main.tsp");
const [options, configDiagnostics] = await compiler.resolveCompilerOptions(compiler.NodeHost, {
  cwd: directory,
  entrypoint: main,
  overrides: { emit: [] },
});
const startedAt = Date.now();
const program = await compiler.compile(compiler.NodeHost, main, {
  ...options,
  emit: [],
  noEmit: true,
  warningAsError: false,
  linterRuleSet: { enable: { [target]: true } },
});
const errors = [...configDiagnostics, ...program.diagnostics].filter(
  (item) => item.severity === "error",
);
assert.equal(
  errors.length,
  0,
  JSON.stringify(errors.map(({ code, message }) => ({ code, message }))),
);
function location(target) {
  const source = compiler.getSourceLocation(target, { locateId: true });
  if (!source || source.isSynthetic) return {};
  const point = source.file.getLineAndCharacterOfPosition(source.pos);
  return {
    sourceFile: path.relative(directory, source.file.path).replaceAll("\\", "/"),
    line: point.line + 1,
    column: point.character + 1,
  };
}
function typeName(type) {
  if (!type) return null;
  return compiler.getTypeName(type);
}
function nonNull(type) {
  if (type?.kind !== "Union") return type;
  const values = [...type.variants.values()]
    .map((item) => item.type)
    .filter((t) => !compiler.isNullType(t));
  return values.length === 1 ? nonNull(values[0]) : type;
}
function standard(type) {
  type = nonNull(type);
  return (
    (type?.kind === "Model" &&
      type.name === "ErrorResponse" &&
      type.namespace &&
      compiler.getNamespaceFullName(type.namespace) === "Azure.ResourceManager.CommonTypes") ||
    false
  );
}
function properties(type) {
  type = nonNull(type);
  if (type?.kind !== "Model") return new Map();
  return new Map(
    [...compiler.walkPropertiesInherited(type)].map((item) => [
      compiler.resolveEncodedName(program, item, "application/json"),
      item,
    ]),
  );
}
function bodyFacts(body) {
  if (!body) return { bodyKind: null, standard: false, type: null };
  const props = properties(body.type);
  const nested = properties(props.get("error")?.type);
  return {
    bodyKind: body.bodyKind,
    type: typeName(body.type),
    standard: standard(body.type),
    topLevelProperties: [...props.keys()].sort(),
    errorProperties: [...nested.keys()].sort(),
    nestedPropertyPresence: props.has("error") && nested.has("code") && nested.has("message"),
  };
}
function* leaves(type) {
  if (type.kind === "Union" && compiler.getDiscriminatedUnion(program, type)[0] === undefined) {
    for (const variant of type.variants.values()) yield* leaves(variant.type);
  } else {
    yield type;
  }
}
function sourceDirectives(operation) {
  const values = [];
  for (let node = operation.node; node; node = node.parent) {
    for (const directive of node.directives ?? []) {
      values.push({
        name: directive.target.sv,
        arguments: directive.arguments.map((arg) => arg.value ?? arg.sv),
        ...location(directive),
      });
    }
  }
  return values;
}
const operations = [];
const byTarget = new Map();
function describe(operation, resolvedHttpOperation) {
  const [httpOperation, diagnostics] = http.getHttpOperation(program, operation);
  const variants = [...leaves(operation.returnType)].map((type) => {
    const [responses, errors] = http.getResponsesForOperation(program, {
      ...operation,
      returnType: type,
    });
    return {
      type: typeName(type),
      markedError: compiler.isErrorModel(program, type),
      responseResolutionDiagnostics: errors.map(({ code, message }) => ({ code, message })),
      responses: responses.map((response) => ({
        statusCodes: response.statusCodes,
        bodies: response.responses.map(({ body }) => bodyFacts(body)),
      })),
    };
  });
  const item = {
    name: operation.name,
    fullName: [
      compiler.getNamespaceFullName(operation.namespace),
      operation.interface?.name,
      operation.name,
    ]
      .filter(Boolean)
      .join("."),
    sourceContext: compiler.getLocationContext(program, operation).type,
    sourceLibrary: compiler.getLocationContext(program, operation).metadata?.name ?? null,
    templateDeclarationOrInstance: compiler.isTemplateDeclarationOrInstance(operation),
    ...location(operation),
    authoredVerb: http.getOperationVerb(program, operation) ?? null,
    verb: (resolvedHttpOperation ?? httpOperation).verb,
    path: (resolvedHttpOperation ?? httpOperation).path,
    httpDiagnostics: diagnostics.map(({ code, message }) => ({ code, message })),
    directives: sourceDirectives(operation),
    returnType: typeName(operation.returnType),
    variants,
  };
  return item;
}
compiler.navigateProgram(program, {
  operation(operation) {
    if (compiler.getLocationContext(program, operation).type !== "project") return;
    if (compiler.isTemplateDeclarationOrInstance(operation)) return;
    const item = describe(operation);
    operations.push(item);
    byTarget.set(operation, item);
  },
});
const [httpServices, serviceDiagnostics] = http.getAllHttpServices(program);
const serviceOperations = httpServices.flatMap((service) =>
  service.operations.map((httpOperation) => describe(httpOperation.operation, httpOperation)),
);
const captured = [];
const listener = rule.create({
  program,
  options: {},
  reportDiagnostic(diagnostic) {
    if (compiler.getLocationContext(program, diagnostic.target).type !== "project") return;
    const messageId = diagnostic.messageId ?? "default";
    captured.push({
      rule: target,
      message: rule.messages[messageId],
      messageId,
      ...location(diagnostic.target),
      operation: byTarget.get(diagnostic.target) ?? null,
    });
  },
});
compiler.navigateProgram(program, listener);
const emitted = program.diagnostics
  .filter((diagnostic) => diagnostic.code === target)
  .map((diagnostic) => ({
    rule: target,
    message: diagnostic.message,
    ...location(diagnostic.target),
  }));
const identity = (item) =>
  JSON.stringify([item.rule, item.sourceFile, item.line, item.column, item.message]);
const available = new Map();
for (const item of emitted) available.set(identity(item), (available.get(identity(item)) ?? 0) + 1);
for (const item of captured) {
  const key = identity(item);
  const count = available.get(key) ?? 0;
  item.emitted = count > 0;
  if (count > 0) available.set(key, count - 1);
  else {
    item.suppressionDirectives =
      item.operation?.directives.filter(
        (directive) =>
          directive.name === "suppress" &&
          (directive.arguments[0] === target ||
            program.diagnosticCodeResolver?.resolveCode(directive.arguments[0]) === target),
      ) ?? [];
    assert.ok(item.suppressionDirectives.length > 0, "Unexplained callback/emission difference");
  }
}
assert(
  [...available.values()].every((count) => count === 0),
  "Unmatched actual emitted diagnostic",
);
fs.mkdirSync(path.dirname(output), { recursive: true });
fs.writeFileSync(
  output,
  JSON.stringify(
    {
      project,
      scope: "source program; no version projection or Swagger regeneration",
      durationMs: Date.now() - startedAt,
      nodeVersion: process.version,
      status: "success",
      rule: target,
      packages,
      emitted,
      captured,
      operations,
      serviceOperations,
      serviceDiagnostics: serviceDiagnostics.map(({ code, message }) => ({ code, message })),
    },
    null,
    2,
  ) + "\n",
);
console.log(
  JSON.stringify({
    project,
    operations: operations.length,
    emitted: emitted.length,
    captured: captured.length,
    suppressed: captured.filter((item) => !item.emitted).length,
    durationMs: Date.now() - startedAt,
  }),
);

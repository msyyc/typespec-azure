import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";
import { pathToFileURL } from "node:url";
const [inputFile, nativeFile, outputFile] = process.argv.slice(2);
const input = JSON.parse(fs.readFileSync(inputFile, "utf8"));
const native = JSON.parse(fs.readFileSync(nativeFile, "utf8"));
assert.equal(native.status, "success", "Failed native projects remain unassessed");
const requireFromSpecs = createRequire(path.join(input.specsRepo, "package.json"));
const load = async (name) => import(pathToFileURL(requireFromSpecs.resolve(name)).href);
const compiler = await load("@typespec/compiler");
const http = await load("@typespec/http");
const armEntry = requireFromSpecs.resolve("@azure-tools/typespec-azure-resource-manager");
const { isTemplatedInterfaceOperation } = await import(
  pathToFileURL(path.join(path.dirname(armEntry), "rules", "utils.js")).href
);
const projectDir = path.resolve(input.specsRepo, input.project.sourcePath);
const main = path.join(projectDir, "main.tsp");
const [options, configurationDiagnostics] = await compiler.resolveCompilerOptions(
  compiler.NodeHost,
  {
    cwd: projectDir,
    entrypoint: main,
    overrides: { emit: [] },
  },
);
const program = await compiler.compile(compiler.NodeHost, main, {
  ...options,
  emit: [],
  noEmit: true,
  warningAsError: false,
  linterRuleSet: undefined,
});
const errors = [...configurationDiagnostics, ...program.diagnostics].filter(
  (d) => d.severity === "error",
);
assert.equal(errors.length, 0, errors.map((d) => `${d.code}: ${d.message}`).join("\n"));
const key = (location) => JSON.stringify([location.sourceFile, location.line, location.column]);
const location = (target) => {
  const source = compiler.getSourceLocation(target, { locateId: true });
  if (!source || source.isSynthetic) return {};
  const position = source.file.getLineAndCharacterOfPosition(source.pos);
  return {
    sourceFile: path.relative(projectDir, source.file.path).replaceAll("\\", "/"),
    line: position.line + 1,
    column: position.character + 1,
  };
};
const operations = [];
compiler.navigateProgram(program, {
  operation(op) {
    if (compiler.isTemplateInstance(op) || isTemplatedInterfaceOperation(op)) return;
    const [operation, diagnostics] = http.getHttpOperation(program, op);
    if (operation.verb === "head") return;
    const responses = operation.responses;
    const slots = [];
    const first = responses.find(
      (response) => response.statusCodes !== 204 && response.statusCodes !== 202,
    );
    if (
      first &&
      !first.responses.every((variant) => variant.body) &&
      !(["delete", "post"].includes(operation.verb) && first.statusCodes === 200)
    ) {
      slots.push({
        category: "existing-body-required",
        status: first.statusCodes,
        comparable: false,
      });
    }
    for (const status of [200, 202, 204]) {
      if (status === 200 && operation.verb !== "delete") continue;
      const response = responses.find((item) => item.statusCodes === status);
      if (response?.responses.some((variant) => variant.body)) {
        slots.push({
          category: "body-must-be-empty",
          status,
          comparable: operation.verb === "delete" && (status === 200 || status === 204),
        });
      }
    }
    const target = location(op);
    operations.push({
      name: `${compiler.getNamespaceFullName(op.namespace)}.${op.interface ? `${op.interface.name}.` : ""}${op.name}`,
      ...target,
      key: key(target),
      method: operation.verb,
      httpPath: operation.path,
      responses: responses.map((response) => ({
        status: response.statusCodes,
        variants: response.responses.map((variant) => ({
          hasBody: !!variant.body,
          bodyKind: variant.body?.type.kind,
          bodyName: variant.body?.type.name,
        })),
      })),
      httpDiagnostics: diagnostics.map((d) => ({ code: d.code, message: d.message })),
      slots,
    });
  },
});
const groups = Object.entries(Object.groupBy(native.rawDiagnostics, key)).map(
  ([targetKey, diagnostics]) => {
    const candidates = operations.filter((op) => op.key === targetKey);
    const predicted = candidates.flatMap((op) =>
      op.slots.map((slot) => ({
        ...slot,
        operation: op.name,
        method: op.method,
        httpPath: op.httpPath,
        sourceFile: op.sourceFile,
        line: op.line,
        column: op.column,
      })),
    );
    const attributable = candidates.length === 1 && predicted.length === diagnostics.length;
    return {
      key: targetKey,
      diagnostics,
      metadataOperations: candidates,
      rawCount: diagnostics.length,
      predictedCount: predicted.length,
      attributable,
      comparableUnits: attributable ? predicted.filter((slot) => slot.comparable) : null,
      unrelatedUnits: attributable ? predicted.filter((slot) => !slot.comparable) : null,
    };
  },
);
const result = {
  project: native.project,
  policy:
    "Source-program native HTTP metadata; exact source-location join; one semantic operation/status unit; never diagnostic-message or property-name attribution. No emitter, Swagger regeneration, or source parsing.",
  metadataCompilation:
    "Same injected compiler/HTTP and project options, emit:[],noEmit:true; linterRuleSet undefined for observation only. Original saved worker diagnostics remain authoritative, including suppressions.",
  raw: native.rawDiagnostics.length,
  attributable: groups.every((group) => group.attributable),
  comparableCount: groups.every((group) => group.attributable)
    ? groups.reduce((sum, group) => sum + group.comparableUnits.length, 0)
    : null,
  unrelatedCount: groups.every((group) => group.attributable)
    ? groups.reduce((sum, group) => sum + group.unrelatedUnits.length, 0)
    : null,
  groups,
  deleteOperations: operations.filter((op) => op.method === "delete"),
};
fs.writeFileSync(outputFile, JSON.stringify(result, null, 2) + "\n");
console.log(
  JSON.stringify({
    project: result.project,
    raw: result.raw,
    attributable: result.attributable,
    comparable: result.comparableCount,
    unrelated: result.unrelatedCount,
  }),
);

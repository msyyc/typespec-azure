import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import fs from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const sha = (bytes) => createHash("sha256").update(bytes).digest("hex");

export async function capture(program, compiler, packages, input, diagnostics, location) {
  const require = createRequire(path.join(input.specsRepo, "package.json"));
  const http = await import(pathToFileURL(require.resolve("@typespec/http")).href);
  const arm = packages.find((pkg) => pkg.name === "@azure-tools/typespec-azure-resource-manager");
  assert(arm);
  const bodyFile = path.join(path.dirname(arm.entrypoint), "rules", "arm-resource-patch-body.js");
  const body = fs.readFileSync(bodyFile, "utf8");
  const exposed =
    body.replace(
      /(from\s+)(["'])([^"']+)\2/g,
      (_, prefix, quote, specifier) =>
        prefix +
        quote +
        (specifier.startsWith(".")
          ? new URL(specifier, pathToFileURL(bodyFile)).href
          : pathToFileURL(createRequire(bodyFile).resolve(specifier)).href) +
        quote,
    ) + "\nexport { collectLeafProperties, isObjectBody };\n";
  const { collectLeafProperties, isObjectBody } = await import(
    `data:text/javascript;base64,${Buffer.from(exposed).toString("base64")}`
  );
  const compatibilityFile = path.join(
    path.dirname(bodyFile),
    "arm-resource-patch-compatibility.js",
  );
  const { createPatchPropertyCompatibility } = await import(pathToFileURL(compatibilityFile).href);
  const [services] = http.getAllHttpServices(program);
  const metadata = http.createMetadataInfo(program);
  const suppressed = (target, message) => {
    const before = program.diagnostics.length;
    program.reportDiagnostic({
      code: "@azure-tools/typespec-azure-resource-manager/arm-resource-patch",
      severity: "warning",
      message,
      target,
    });
    return program.diagnostics.length === before;
  };
  const pairs = [];
  for (const service of services) {
    const byPath = new Map();
    for (const operation of service.operations) {
      if (
        compiler.getLocationContext(program, operation.operation).type !== "project" ||
        (operation.overloading && http.isOverloadSameEndpoint(operation)) ||
        !["patch", "put"].includes(operation.verb)
      )
        continue;
      const pair = byPath.get(operation.path) ?? {};
      pair[operation.verb] = operation;
      byPath.set(operation.path, pair);
    }
    for (const [route, pair] of byPath) {
      if (!pair.patch || !pair.put) continue;
      if (input.attributionRoutes && !input.attributionRoutes.includes(route)) continue;
      const { patch, put } = pair;
      const describe = (type) => ({
        type: compiler.getTypeName(type),
        kind: type.kind,
        decorators: (type.decorators ?? []).map((decorator) => decorator.decorator.name),
        ...location(type),
      });
      const describeProperty = (leaf) => ({
        jsonName: leaf.jsonName,
        property: compiler.getTypeName(leaf.property),
        type: compiler.getTypeName(leaf.property.type),
        target: location(leaf.target),
        propertySource: location(leaf.property),
        decorators: (leaf.property.decorators ?? []).map((decorator) => decorator.decorator.name),
        recursive: leaf.recursive,
      });
      const patchBody = patch.parameters.body?.type;
      const putBody = put.parameters.body?.type;
      const result = {
        route,
        patch: describe(patch.operation),
        put: describe(put.operation),
        patchBody: patchBody && describe(patchBody),
        putBody: putBody && describe(putBody),
        leaves: [],
      };
      if (!patchBody || compiler.isVoidType(patchBody)) {
        result.bodyCheck = "missingPatchBody";
      } else if (patch.parameters.body?.bodyKind !== "single" || !isObjectBody(patchBody)) {
        result.bodyCheck = "unsupportedPatchBody";
      } else {
        const patchLeaves = collectLeafProperties(program, patchBody, patch, metadata);
        if (!patchLeaves.length) {
          result.bodyCheck = "emptyPatchBody";
        } else if (
          putBody &&
          !compiler.isVoidType(putBody) &&
          (put.parameters.body?.bodyKind !== "single" || !isObjectBody(putBody))
        ) {
          result.bodyCheck = "unsupportedPutBody";
        } else {
          const putLeaves =
            putBody && !compiler.isVoidType(putBody)
              ? collectLeafProperties(program, putBody, put, metadata)
              : [];
          const compatible = createPatchPropertyCompatibility(program, metadata, patch, put);
          result.bodyCheck = "supported";
          for (const leaf of patchLeaves) {
            const candidates = putLeaves.filter(
              (candidate) => candidate.jsonName === leaf.jsonName,
            );
            const accepted = candidates.some(
              (candidate) =>
                (leaf.recursive && candidate.recursive) ||
                compatible(leaf.property, candidate.property),
            );
            const family = accepted
              ? null
              : candidates.length
                ? "incompatibleProperty"
                : "missingProperty";
            const message =
              family === "missingProperty"
                ? `The property '${leaf.jsonName}' in the PATCH body does not correspond to a property in the PUT body.`
                : family === "incompatibleProperty"
                  ? `The property '${leaf.jsonName}' in the PATCH body must have a type and constraints compatible with its corresponding PUT property.`
                  : null;
            const target = location(leaf.target);
            result.leaves.push({
              ...describeProperty(leaf),
              candidates: candidates.map(describeProperty),
              family,
              message,
              compilerSuppressed: !!family && suppressed(leaf.target, message),
              configuredWarning:
                !!family &&
                diagnostics.some(
                  (diagnostic) =>
                    diagnostic.message === message &&
                    diagnostic.sourceFile === target.sourceFile &&
                    diagnostic.line === target.line &&
                    diagnostic.column === target.column,
                ),
            });
          }
        }
      }
      if (result.bodyCheck === "missingPatchBody" || result.bodyCheck === "emptyPatchBody") {
        const message =
          result.bodyCheck === "missingPatchBody"
            ? "The PATCH operation must have a request body."
            : "The PATCH request body must contain at least one property.";
        const target = location(patch.operation);
        result.bodyWarning = {
          target,
          message,
          compilerSuppressed: suppressed(patch.operation, message),
          configuredWarning: diagnostics.some(
            (diagnostic) =>
              diagnostic.message === message &&
              diagnostic.sourceFile === target.sourceFile &&
              diagnostic.line === target.line &&
              diagnostic.column === target.column,
          ),
        };
      }
      pairs.push(result);
    }
  }
  fs.writeFileSync(
    input.attributionOutput,
    JSON.stringify(
      {
        project: input.project.sourcePath,
        scope:
          "Exact source-program HTTP operation/payload predicates before global deduplication; separate public compiler reportDiagnostic probes test authored suppression after the registered compilation. Original configured diagnostics are retained unchanged. Predicate/probe observations are not additional raw warnings or version-projected correspondence.",
        extraction:
          "Installed production collector exposed without behavior changes; installed production compatibility predicate. Route grouping, overload/project filtering and candidate selection match the owning listener.",
        bodyModuleSha256: sha(body),
        compatibilityModuleSha256: sha(fs.readFileSync(compatibilityFile)),
        extractorSha256: sha(fs.readFileSync(fileURLToPath(import.meta.url))),
        originalWorkerSha256: sha(
          fs.readFileSync(
            path.join(
              input.toolingRepo,
              "packages",
              "typespec-lintdiff",
              "test",
              "harness",
              "native-coverage-worker.mjs",
            ),
          ),
        ),
        rawDiagnostics: diagnostics,
        pairs: pairs.filter(
          (pair) => !input.attributionRoutes || input.attributionRoutes.includes(pair.route),
        ),
      },
      null,
      2,
    ) + "\n",
  );
}

import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import fs from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";
import { pathToFileURL } from "node:url";

const sha = (bytes) => createHash("sha256").update(bytes).digest("hex");

export async function capture(program, compiler, packages, input, diagnostics, location, autorest) {
  const require = createRequire(path.join(input.specsRepo, "package.json"));
  const http = await import(pathToFileURL(require.resolve("@typespec/http")).href);
  const arm = packages.find((item) => item.name === "@azure-tools/typespec-azure-resource-manager");
  assert(arm);
  const rules = path.join(path.dirname(arm.entrypoint), "rules");
  const bodyFile = path.join(rules, "arm-resource-patch-body.js");
  const bodySource = fs.readFileSync(bodyFile, "utf8");
  const exposed =
    bodySource.replace(
      /(from\s+)(["'])([^"']+)\2/g,
      (_, prefix, quote, specifier) =>
        prefix +
        quote +
        (specifier.startsWith(".")
          ? new URL(specifier, pathToFileURL(bodyFile)).href
          : pathToFileURL(createRequire(bodyFile).resolve(specifier)).href) +
        quote,
    ) + "\nexport { isObjectBody, collectLeafProperties, getOperationTarget };\n";
  const { isObjectBody, collectLeafProperties, getOperationTarget } = await import(
    `data:text/javascript;base64,${Buffer.from(exposed).toString("base64")}`
  );
  const owners = [];
  for (const [file, name] of [
    ["use-model-request-body.js", "useModelRequestBodyRule"],
    ["use-application-json-content-type.js", "useApplicationJsonContentTypeRule"],
  ]) {
    const module = await import(pathToFileURL(path.join(rules, file)).href);
    owners.push(module[name]);
  }
  const describe = (operation) => {
    const body = operation.parameters.body;
    if (!body) return { state: "absent" };
    const type = body.type;
    const indexers = [];
    for (let model = type; model?.kind === "Model"; model = model.baseModel) {
      if (model.indexer) indexers.push(compiler.getTypeName(model));
    }
    return {
      kind: type.kind,
      type: compiler.getTypeName(type),
      bodyKind: body.bodyKind,
      contentTypes: body.contentTypes,
      objectBody: isObjectBody(type),
      indexers,
      ...location(body.property ?? operation.operation),
    };
  };
  const [services] = http.getAllHttpServices(program);
  const metadata = http.createMetadataInfo(program);
  const pairs = [];
  for (const service of services) {
    const byPath = new Map();
    for (const operation of service.operations) {
      if (
        compiler.getLocationContext(program, getOperationTarget(program, operation)).type !==
          "project" ||
        (operation.overloading && http.isOverloadSameEndpoint(operation)) ||
        !["patch", "put"].includes(operation.verb)
      )
        continue;
      const pair = byPath.get(operation.path) ?? {};
      pair[operation.verb] = operation;
      byPath.set(operation.path, pair);
    }
    for (const [route, { patch, put }] of byPath) {
      if (!patch || !put) continue;
      const p = patch.parameters.body;
      const u = put.parameters.body;
      let bodyCheck;
      if (!p || compiler.isVoidType(p.type)) bodyCheck = "missingPatchBody";
      else if (p.bodyKind !== "single" || !isObjectBody(p.type)) bodyCheck = "unsupportedPatchBody";
      else if (collectLeafProperties(program, p.type, patch, metadata).length === 0)
        bodyCheck = "emptyPatchBody";
      else if (
        u &&
        !compiler.isVoidType(u.type) &&
        (u.bodyKind !== "single" || !isObjectBody(u.type))
      )
        bodyCheck = "unsupportedPutBody";
      else bodyCheck = "supported";
      const ownerPredicates = [];
      if (bodyCheck.startsWith("unsupported")) {
        for (const operation of [patch, put]) {
          for (const rule of owners) {
            rule
              .create({
                program,
                reportDiagnostic(diagnostic) {
                  ownerPredicates.push({
                    verb: operation.verb,
                    rule: `@azure-tools/typespec-azure-resource-manager/${rule.name}`,
                    messageId: diagnostic.messageId ?? "default",
                    ...location(diagnostic.target),
                  });
                },
              })
              .operation(operation.operation);
          }
        }
      }
      pairs.push({
        route,
        bodyCheck,
        patch: describe(patch),
        put: describe(put),
        ...(ownerPredicates.length ? { ownerPredicates } : {}),
      });
    }
  }
  const result = {
    project: input.project.sourcePath,
    bodyCollectorSha256: sha(bodySource),
    pairs,
    rawDiagnostics: diagnostics,
  };
  if (input.emitFixture) {
    const before = program.diagnostics.length;
    const records = await autorest.getAllServicesAtAllVersions(
      program,
      autorest.resolveAutorestOptions(program, input.project.sourcePath, {}),
    );
    const documents = records.flatMap((record) => (record.versioned ? record.versions : [record]));
    result.emitterDiagnostics = program.diagnostics.slice(before).map((diagnostic) => ({
      code: diagnostic.code,
      severity: diagnostic.severity,
      message: diagnostic.message,
    }));
    result.swagger = [];
    const predicateFile = path.join(
      path.dirname(require.resolve("@microsoft.azure/openapi-validator-rulesets")),
      "spectral",
      "functions",
      "patch-properties-correspond-to-put-properties.js",
    );
    const predicate = require(predicateFile).patchPropertiesCorrespondToPutProperties;
    result.swaggerPredicateSha256 = sha(fs.readFileSync(predicateFile));
    for (const record of documents) {
      const document = JSON.parse(JSON.stringify(record.document));
      const resolve = (value, ancestors = new Set()) => {
        if (Array.isArray(value)) return value.map((v) => resolve(v, ancestors));
        if (!value || typeof value !== "object") return value;
        if (value.$ref) {
          assert(value.$ref.startsWith("#/"), `Fixture has an external reference: ${value.$ref}`);
          assert(!ancestors.has(value.$ref), "Fixture resolver does not support cycles");
          const next = new Set(ancestors).add(value.$ref);
          const target = value.$ref
            .slice(2)
            .split("/")
            .reduce((node, key) => node[key.replaceAll("~1", "/").replaceAll("~0", "~")], document);
          assert(target);
          const { $ref, ...siblings } = value;
          return { ...resolve(target, next), ...resolve(siblings, ancestors) };
        }
        return Object.fromEntries(
          Object.entries(value).map(([k, v]) => [k, resolve(v, ancestors)]),
        );
      };
      for (const [route, item] of Object.entries(document.paths)) {
        if (!item.patch || !item.put) continue;
        const resolved = resolve(item);
        result.swagger.push({
          route,
          pathItem: resolved,
          diagnostics: predicate(resolved, null, { path: ["paths", route] }),
        });
      }
    }
  }
  fs.writeFileSync(input.bodyOutput, JSON.stringify(result) + "\n", { flag: "wx" });
}

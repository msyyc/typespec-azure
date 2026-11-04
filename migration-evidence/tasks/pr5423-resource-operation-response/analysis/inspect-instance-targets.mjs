import { writeFileSync } from "node:fs";
import * as path from "node:path";
import { pathToFileURL } from "node:url";

export async function inspectInstances({
  program,
  compiler,
  load,
  project,
  projectDir,
  requireFromSpecs,
  outputFile,
}) {
  const http = await load("@typespec/http");
  const arm = await load("@azure-tools/typespec-azure-resource-manager");
  const versioning = await load("@typespec/versioning");
  const metadata = http.createMetadataInfo(program);
  const location = (target) => {
    const source = compiler.getSourceLocation(target, { locateId: true });
    if (!source || source.isSynthetic) return {};
    const pos = source.file.getLineAndCharacterOfPosition(source.pos);
    return {
      sourceFile: path.relative(projectDir, source.file.path).replaceAll("\\", "/"),
      line: pos.line + 1,
      column: pos.character + 1,
    };
  };
  const name = (type) => type && compiler.getTypeName(type);
  const internal = (type) => {
    const ns = compiler.getNamespaceFullName(type.namespace);
    return ["TypeSpec", "Azure.ResourceManager", "Azure.Core"].some((prefix) =>
      ns.startsWith(prefix),
    );
  };
  const operationKey = (operation) => JSON.stringify([name(operation), location(operation)]);
  const associations = new Map();
  const resources = [];
  compiler.navigateProgram(program, {
    model(model) {
      if (internal(model) || !arm.getArmResource(program, model)) return;
      const operations = arm.resolveResourceOperations(program, model);
      const entries = [
        ...Object.entries(operations.lifecycle).map(([kind, value]) => ({
          group: "lifecycle",
          kind,
          value,
        })),
        ...Object.entries(operations.lists).map(([kind, value]) => ({
          group: "lists",
          kind,
          value,
        })),
      ];
      const record = { model: name(model), ...location(model), operations: [] };
      for (const { group, kind, value } of entries) {
        if (!value) continue;
        const association = {
          resource: name(model),
          group,
          kind,
          operationKey: operationKey(value.operation),
          internal: internal(value.operation),
          checkedPutRequest:
            group === "lifecycle" &&
            kind === "createOrUpdate" &&
            value.httpOperation.verb === "put" &&
            !internal(value.operation),
        };
        if (!associations.has(value.operation)) associations.set(value.operation, []);
        associations.get(value.operation).push(association);
        record.operations.push(association);
      }
      resources.push(record);
    },
  });
  const describeType = (type) =>
    type && {
      name: name(type),
      kind: type.kind,
      registeredResource: type.kind === "Model" && !!arm.getArmResource(program, type),
    };
  const describeOperation = (operation, mode) => {
    const op = operation.operation;
    const body = operation.parameters.body;
    const effective =
      body?.bodyKind === "single"
        ? metadata.getEffectivePayloadType(
            body.type,
            http.resolveRequestVisibility(program, op, operation.verb),
          )
        : undefined;
    const responseCandidates = [];
    const addCandidate = (type) => {
      if (type?.kind === "Model" && arm.getArmResource(program, type)) {
        responseCandidates.push(name(type));
      }
    };
    if (op.returnType.kind === "Model") addCandidate(op.returnType);
    else if (op.returnType.kind === "Union") {
      for (const variant of op.returnType.variants.values()) {
        if (compiler.isErrorType(variant.type) || variant.type.kind !== "Model") continue;
        const model = compiler.getEffectiveModelType(program, variant.type);
        addCandidate(model);
        for (const arg of model.templateMapper?.args ?? []) {
          if (!compiler.isType(arg) || arg.kind !== "Model") continue;
          addCandidate(arg);
          const resourceArgs = (arg.templateMapper?.args ?? []).filter(
            (item) =>
              compiler.isType(item) && item.kind === "Model" && arm.getArmResource(program, item),
          );
          if (resourceArgs.length === 1) addCandidate(resourceArgs[0]);
        }
      }
    }
    return {
      mode,
      operationKey: operationKey(op),
      operation: name(op),
      ...location(op),
      verb: operation.verb,
      path: operation.path,
      internal: internal(op),
      associations: associations.get(op) ?? [],
      request: body && {
        bodyKind: body.bodyKind,
        type: describeType(body.type),
        effectiveType: describeType(effective),
        void: compiler.isVoidType(body.type),
      },
      responseCandidates: [...new Set(responseCandidates)],
      responses: operation.responses.map((response) => ({
        statusCodes: response.statusCodes,
        type: describeType(response.type),
        bodies: response.responses.map((content) => describeType(content.body?.type)),
      })),
    };
  };
  const services = compiler.listServices(program);
  const sourceOperations = [];
  const metadataDiagnostics = [];
  for (const service of services) {
    const [graph, diagnostics] = http.getHttpService(program, service.type);
    metadataDiagnostics.push(...diagnostics.map((d) => ({ code: d.code, message: d.message })));
    sourceOperations.push(...graph.operations.map((op) => describeOperation(op, "source")));
  }
  const findings = program.diagnostics
    .filter(
      (diagnostic) =>
        diagnostic.code ===
        "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
    )
    .map((diagnostic) => ({
      rule: diagnostic.code,
      message: diagnostic.message,
      targetKind: diagnostic.target.kind,
      operationKey:
        diagnostic.target.kind === "Operation" ? operationKey(diagnostic.target) : undefined,
      ...location(diagnostic.target),
    }));
  const selectedOperations = [];
  const experimental = await import(
    pathToFileURL(requireFromSpecs.resolve("@typespec/compiler/experimental")).href
  );
  for (const service of services) {
    const mutators = versioning.getVersioningMutators(program, service.type);
    let ns = service.type;
    if (mutators?.kind === "versioned") {
      const snapshot = mutators.snapshots.find((item) => item.version.value === project.apiVersion);
      if (!snapshot) throw new Error(`Selected version ${project.apiVersion} not found`);
      ns = experimental.unsafe_mutateSubgraphWithNamespace(program, [snapshot.mutator], ns).type;
    } else if (mutators?.kind === "transient") {
      ns = experimental.unsafe_mutateSubgraphWithNamespace(program, [mutators.mutator], ns).type;
    }
    const [graph, diagnostics] = http.getHttpService(program, ns);
    metadataDiagnostics.push(...diagnostics.map((d) => ({ code: d.code, message: d.message })));
    selectedOperations.push(
      ...graph.operations.map((op) => describeOperation(op, "selected-version")),
    );
  }
  writeFileSync(
    outputFile + ".instances.json",
    JSON.stringify(
      {
        project: project.sourcePath,
        apiVersion: project.apiVersion,
        findings,
        resources,
        sourceOperations,
        selectedOperations,
        metadataDiagnostics,
      },
      null,
      2,
    ) + "\n",
  );
}

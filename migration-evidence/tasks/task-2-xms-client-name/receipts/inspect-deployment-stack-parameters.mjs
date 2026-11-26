import { createHash } from "node:crypto";
import fs from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";
import { pathToFileURL } from "node:url";

const specs = String.raw`$SPECS`;
const requireFromSpecs = createRequire(path.join(specs, "package.json"));
const compilerPath = fs.realpathSync(requireFromSpecs.resolve("@typespec/compiler"));
const compiler = await import(pathToFileURL(compilerPath).href);
const tcgcResolution = await compiler.resolveModule(
  {
    realpath: fs.promises.realpath,
    stat: fs.promises.stat,
    readFile: (file) => fs.promises.readFile(file, "utf8"),
  },
  "@azure-tools/typespec-client-generator-core",
  { baseDir: specs, conditions: ["import"] },
);
const tcgcPath = fs.realpathSync(tcgcResolution.mainFile);
const tcgc = await import(pathToFileURL(tcgcPath).href);
const project = "specification/resources/resource-manager/Microsoft.Resources/deploymentStacks";
const projectDirectory = path.join(specs, project);
const main = path.join(projectDirectory, "main.tsp");
const [options, configDiagnostics] = await compiler.resolveCompilerOptions(compiler.NodeHost, {
  cwd: projectDirectory,
  entrypoint: main,
  overrides: { emit: [] },
});
const program = await compiler.compile(compiler.NodeHost, main, {
  ...options,
  emit: [],
  noEmit: true,
});
const context = tcgc.createTCGCContext(program, "@azure-tools/typespec-client-generator-core", {
  mutateNamespace: false,
});
const properties = new Map();
const applications = new Map();
const results = [];
for (const scope of ["ResourceGroup", "Subscription", "ManagementGroup"]) {
  const interfaceName = `Microsoft.Resources.DeploymentStacks.DeploymentStacksAt${scope}`;
  const [type, diagnostics] = program.resolveTypeReference(interfaceName);
  if (diagnostics.length || type?.kind !== "Interface") {
    throw new Error(`Cannot resolve interface ${interfaceName}`);
  }
  for (const [operationName, parameterName] of [
    ["validateStack", "body"],
    ["createOrUpdate", "resource"],
  ]) {
    const operation = type.operations.get(operationName);
    const parameter = operation?.parameters.properties.get(parameterName);
    if (!parameter) throw new Error(`Missing ${interfaceName}.${operationName}.${parameterName}`);
    if (!properties.has(parameter)) properties.set(parameter, properties.size + 1);
    const decoration = [];
    for (const application of parameter.decorators) {
      if (application.definition?.name !== "@clientName") continue;
      if (!applications.has(application.node)) applications.set(application.node, applications.size + 1);
      const location = compiler.getSourceLocation(application.node ?? parameter);
      const value = application.args[0]?.value;
      decoration.push({
        applicationIdentity: applications.get(application.node),
        file: path.relative(specs, location.file.path).replaceAll("\\", "/"),
        line: location.file.text.slice(0, location.pos).split("\n").length,
        argumentEntityKind: value?.entityKind,
        value: value?.value,
        effectiveNameWithoutThisApplication: tcgc.getLibraryName(
          context,
          parameter,
          undefined,
          application,
        ),
        exactWithoutThisApplication: tcgc.isExactClientName(
          context,
          parameter,
          undefined,
          application,
        ),
      });
    }
    results.push({
      interface: interfaceName,
      operation: operationName,
      parameter: parameterName,
      propertyIdentity: properties.get(parameter),
      sourceName: parameter.name,
      effectiveName: tcgc.getLibraryName(context, parameter),
      exact: tcgc.isExactClientName(context, parameter),
      applications: decoration,
    });
  }
}
const result = {
  schemaVersion: 1,
  question: "Why are six apparently unique DeploymentStack body overrides independently ineffective?",
  scope: "One read-only saved-candidate compile; public compiler object identity and SDK counterfactual name APIs; no Program mutation, emitter or Swagger regeneration.",
  project,
  configDiagnostics: configDiagnostics.map(({ code, severity, message }) => ({ code, severity, message })),
  compilerDiagnostics: program.diagnostics.map(({ code, severity, message }) => ({ code, severity, message })),
  compiler: {
    entrypoint: compilerPath,
    sha256: createHash("sha256").update(fs.readFileSync(compilerPath)).digest("hex"),
  },
  tcgc: {
    entrypoint: tcgcPath,
    sha256: createHash("sha256").update(fs.readFileSync(tcgcPath)).digest("hex"),
  },
  results,
};
fs.writeFileSync(process.argv[2], JSON.stringify(result, undefined, 2) + "\n", "utf8");
console.log(JSON.stringify({ rows: results.length, propertyIdentities: properties.size, applicationIdentities: applications.size }));

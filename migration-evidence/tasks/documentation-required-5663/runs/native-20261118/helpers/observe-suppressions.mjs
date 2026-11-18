import { createHash } from "node:crypto";
import fs from "node:fs";
import { registerHooks } from "node:module";
import { fileURLToPath } from "node:url";

const worker = process.env.COVERAGE_NATIVE_WORKER;
if (!worker) throw new Error("Set COVERAGE_NATIVE_WORKER to the pinned worker path");
const original = fs.readFileSync(worker, "utf8");
const expectedHash = createHash("sha256").update(original).digest("hex");
const marker = '  if (scope === "source") {\n    return {';
if (original.split(marker).length !== 2)
  throw new Error("Suppression observation requires the reviewed source-scope worker shape");

// Observe the linter's diagnostic result before compiler suppression without editing its packages.
const observation = `
  if (scope === "source" && errors.length === 0) {
    const { createLinter } = await import(
      pathToFileURL(path.join(path.dirname(packages[0].entrypoint), "core", "linter.js")).href
    );
    const observer = createLinter(
      program,
      async (name) => {
        const library = await load(name);
        return library.$linter
          ? { linter: compiler.resolveLinterDefinition(name, library.$linter) }
          : undefined;
      },
      program.diagnosticCodeResolver,
    );
    const setupDiagnostics = await observer.extendRuleSet({ enable: targetOptions });
    if (setupDiagnostics.length) throw new Error("Pre-suppression observer rule activation failed");
    const observed = (await observer.lint()).diagnostics
      .filter((diagnostic) => tspRules.includes(diagnostic.code))
      .map((diagnostic) => ({
        rule: diagnostic.code,
        message: diagnostic.message,
        ...location(diagnostic.target),
      }));
    const key = (item) => JSON.stringify([
      item.rule, item.message, item.sourceFile, item.line, item.column,
    ]);
    const configured = new Map();
    for (const diagnostic of rawDiagnostics)
      configured.set(key(diagnostic), (configured.get(key(diagnostic)) ?? 0) + 1);
    const suppressed = [];
    for (const diagnostic of observed) {
      const identity = key(diagnostic);
      const remaining = configured.get(identity) ?? 0;
      if (remaining > 0) configured.set(identity, remaining - 1);
      else suppressed.push(diagnostic);
    }
    if ([...configured.values()].some((count) => count !== 0))
      throw new Error("Pre-suppression re-evaluation did not reproduce all configured findings");
    fs.writeFileSync(outputFile + ".presuppression.json", JSON.stringify({
      project: project.sourcePath,
      status: "success",
      method: "re-evaluate the exact injected mapped linter on the same compiled program before compiler suppression; configured diagnostic multiset is a required subset",
      additionalCompilation: false,
      configuredCount: rawDiagnostics.length,
      preSuppressionCount: observed.length,
      capturedSuppressedDiagnostics: suppressed,
      preSuppressionDiagnostics: observed,
    }, null, 2) + "\\n");
  }
`;
registerHooks({
  load(url, context, nextLoad) {
    const result = nextLoad(url, context);
    if (!url.startsWith("file:") || fileURLToPath(url).toLowerCase() !== worker.toLowerCase())
      return result;
    const source =
      typeof result.source === "string"
        ? result.source
        : Buffer.from(result.source).toString("utf8");
    if (createHash("sha256").update(source).digest("hex") !== expectedHash)
      throw new Error("Worker changed after observer initialization");
    return { ...result, source: source.replace(marker, observation + marker) };
  },
});

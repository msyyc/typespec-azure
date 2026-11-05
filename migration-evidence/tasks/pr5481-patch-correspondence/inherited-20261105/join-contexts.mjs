import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

export function observeContext(source, route, name) {
  return source.pairs
    .filter((pair) => pair.route === route)
    .map((pair) => {
      const leaves = name === null ? [] : pair.leaves.filter((leaf) => leaf.jsonName === name);
      const checks =
        name === null
          ? pair.bodyWarning
            ? [pair.bodyWarning]
            : []
          : leaves.filter((leaf) => leaf.family !== null);
      const warningIndices = [];
      for (const [index, diagnostic] of source.rawDiagnostics.entries()) {
        if (
          checks.some((check) => {
            const target = check.target;
            return (
              check.message === diagnostic.message &&
              target.sourceFile === diagnostic.sourceFile &&
              target.line === diagnostic.line &&
              target.column === diagnostic.column
            );
          })
        )
          warningIndices.push(index);
      }
      return {
        route,
        patch: pair.patch,
        put: pair.put,
        bodyCheck: pair.bodyCheck,
        leaves,
        ...(pair.bodyWarning ? { bodyWarning: pair.bodyWarning } : {}),
        warningIndices,
      };
    });
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const [task, captures, output] = process.argv.slice(2).map((value) => path.resolve(value));
  assert(!fs.existsSync(output));
  const read = (file) => JSON.parse(fs.readFileSync(file, "utf8"));
  const assessment = read(path.join(task, "assessment-20261105", "results.json"));
  const replay = read(path.join(task, "staging-comparison", "schema-investigation.json"));
  const inventory = read(path.join(captures, "inventory.json"));
  const sources = new Map(
    inventory.projects.map((project) => [
      project.project,
      { file: project.source, value: read(path.join(captures, project.source)) },
    ]),
  );
  const records = [];
  for (const project of assessment.projects) {
    for (const record of project.swaggerAssessments.filter(
      (record) => record.retainedAfterMetadataAssessment,
    )) {
      const input = replay.inputs[record.replayInputIndex];
      const operation = input.operations[record.replayOperationIndex];
      const source = sources.get(project.project);
      assert(source, project.project);
      const name =
        record.replayReasonIndex === null ? null : operation.reasons[record.replayReasonIndex].name;
      const contexts = observeContext(source.value, operation.path[1], name);
      let observation = "needs-inspection";
      if (!contexts.length) observation = "no-source-pair";
      else if (name === null) {
        if (contexts.every((context) => context.bodyCheck === "missingPatchBody")) {
          observation = contexts.some((context) => context.warningIndices.length)
            ? "body-reported"
            : contexts.every((context) => context.bodyWarning.compilerSuppressed)
              ? "body-suppressed"
              : "needs-inspection";
        }
      } else {
        const leaves = contexts.flatMap((context) => context.leaves);
        const violations = leaves.filter((leaf) => leaf.family !== null);
        if (!leaves.length) observation = "name-not-source-leaf";
        else if (!violations.length) observation = "source-accepts";
        else if (leaves.some((leaf) => leaf.family === null))
          observation = "mixed-source-predicates";
        else if (contexts.some((context) => context.warningIndices.length))
          observation = "source-reported";
        else if (violations.every((leaf) => leaf.compilerSuppressed))
          observation = "source-suppressed";
      }
      records.push({
        project: project.project,
        diagnosticIndex: record.diagnosticIndex,
        replayInputIndex: record.replayInputIndex,
        replayOperationIndex: record.replayOperationIndex,
        replayReasonIndex: record.replayReasonIndex,
        swaggerFamily: record.family,
        operationId: operation.operationId,
        route: operation.path[1],
        name,
        sourceFile: source.file,
        observation,
        contexts,
      });
    }
  }
  assert.equal(records.length, 182);
  const counts = {};
  for (const record of records) counts[record.observation] = (counts[record.observation] ?? 0) + 1;
  fs.writeFileSync(
    output,
    JSON.stringify(
      {
        scope:
          "Exact project/route and owning predicate/source-target observations for all182retained emitted records. This is contextual evidence, not automatic semantic disposition or one-to-one source-to-emission matching. Duplicate names/targets across contexts remain visible; only exact diagnostic indices witness configured warnings.",
        counting:
          "Records retain original reported Swagger identities. warningIndices index the entire original configured source diagnostic array in each source capture. Several records/contexts may witness one warning; distinct warning records are not collapsed by position.",
        observations: counts,
        records,
      },
      null,
      2,
    ) + "\n",
  );
  console.log(JSON.stringify(counts, null, 2));
}

import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";

const local = process.env.COVERAGE_CONTROL_OUTPUT;
const specsRepo = process.env.COVERAGE_SPECS_REPO;
const worker = process.env.COVERAGE_NATIVE_WORKER;
const rule = "@azure-tools/typespec-azure-core/documentation-required";
const root = path.join(local, "documentation-controls");
fs.mkdirSync(root);
fs.symlinkSync(path.join(specsRepo, "node_modules"), path.join(root, "node_modules"), "junction");
const fixtures = [
  {
    name: "separate-name-and-blank-families",
    source: '@doc("Widget.") model Widget { @doc("") value: string; }',
    configured: 2,
    before: 2,
    names: 1,
    blanks: 1,
  },
  {
    name: "meaningful-control",
    source:
      '@doc("Represents a widget.") model Widget { @doc("Display label for the widget.") value: string; }',
    configured: 0,
    before: 0,
  },
  {
    name: "direct-suppression-captured",
    source: `#suppress "${rule}" "Intentional control."\n@doc("Widget") model Widget {}`,
    configured: 0,
    before: 1,
  },
  {
    name: "ancestor-suppression-captured",
    source: `#suppress "${rule}" "Intentional control."\nnamespace Examples { @doc("Widget") model Widget {} }`,
    configured: 0,
    before: 1,
  },
  {
    name: "missing-doc-not-credited-to-migrated-checks",
    source: "model Widget {}",
    configured: 1,
    before: 1,
    names: 0,
    blanks: 0,
  },
  {
    name: "json-wire-name-is-not-authored-name",
    source:
      '@doc("A resource model.") model Widget { @encodedName("application/json", "wire") @doc("wire") source: string; }',
    configured: 0,
    before: 0,
  },
  {
    name: "authored-name-still-reported",
    source:
      '@doc("A resource model.") model Widget { @encodedName("application/json", "wire") @doc("source") source: string; }',
    configured: 1,
    before: 1,
    names: 1,
    blanks: 0,
  },
  {
    name: "unnamed-variant-and-enum-member",
    source:
      '@doc("States of a task.") union State { @doc("Ready.") "Ready" } @doc("Colors of a widget.") enum Color { @doc("Red") Red }',
    configured: 2,
    before: 2,
    names: 2,
    blanks: 0,
  },
];
const receipts = [];
for (const fixture of fixtures) {
  const directory = path.join(root, fixture.name);
  fs.mkdirSync(directory);
  fs.writeFileSync(
    path.join(directory, "main.tsp"),
    `import "@azure-tools/typespec-azure-core";\n${fixture.source}\n`,
  );
  fs.writeFileSync(
    path.join(directory, "tspconfig.yaml"),
    `linter:\n  disable:\n    "${rule}": "Control checks comparison activation."\n`,
  );
  for (const nativeMode of ["configured", "target-only"]) {
    const output = path.join(directory, `${nativeMode}.json`);
    const input = path.join(directory, `${nativeMode}.input.json`);
    fs.writeFileSync(
      input,
      JSON.stringify({
        specsRepo,
        project: { sourcePath: directory, apiVersion: "2026-01-01" },
        validatorRules: ["DescriptionMustNotBeNodeName", "DescriptiveDescriptionRequired"],
        tspRules: [rule],
        scope: "source",
        nativeMode,
      }),
    );
    const child = spawnSync(process.execPath, [worker, input, output], {
      encoding: "utf8",
      timeout: 120000,
    });
    assert.equal(child.status, 0, child.stderr);
    const result = JSON.parse(fs.readFileSync(output, "utf8"));
    assert.equal(result.status, "success", JSON.stringify(result));
    const observation = JSON.parse(fs.readFileSync(output + ".presuppression.json", "utf8"));
    assert.equal(result.rawDiagnostics.length, fixture.configured, fixture.name);
    assert.equal(observation.preSuppressionCount, fixture.before, fixture.name);
    assert.equal(
      observation.capturedSuppressedDiagnostics.length,
      fixture.before - fixture.configured,
    );
    if (nativeMode === "configured") assert.deepEqual(result.defaultTargetDiagnostics, []);
    if (fixture.names !== undefined)
      assert.equal(
        observation.preSuppressionDiagnostics.filter((item) =>
          item.message.startsWith("Description must not match"),
        ).length,
        fixture.names,
      );
    if (fixture.blanks !== undefined)
      assert.equal(
        observation.preSuppressionDiagnostics.filter((item) =>
          item.message.startsWith("Descriptions cannot be empty"),
        ).length,
        fixture.blanks,
      );
    receipts.push({
      fixture: fixture.name,
      nativeMode,
      source: fixture.source,
      configured: fixture.configured,
      capturedSuppressed: fixture.before - fixture.configured,
      beforeSuppression: fixture.before,
      status: "passed",
    });
  }
}
fs.writeFileSync(
  path.join(local, "documentation-control-results.json"),
  JSON.stringify(receipts, null, 2) + "\n",
);
process.stdout.write(
  `Passed ${receipts.length} injected documentation controls, including actual direct/ancestor suppressed findings and mixed-check attribution.\n`,
);

import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";

const [specs, tooling, output] = process.argv.slice(2).map((value) => path.resolve(value));
assert(specs && tooling && output);
assert(!fs.existsSync(output), "Never overwrite control evidence");
fs.mkdirSync(output, { recursive: true });
fs.symlinkSync(path.join(specs, "node_modules"), path.join(output, "node_modules"), "junction");

const arm = "@azure-tools/typespec-azure-resource-manager/no-get-lro";
const sdk = "@azure-tools/typespec-client-generator-core/no-get-lro";
const prelude = `
import "@typespec/http";
import "@typespec/openapi";
import "@azure-tools/typespec-azure-core";
import "@azure-tools/typespec-azure-resource-manager";
import "@azure-tools/typespec-client-generator-core";
using TypeSpec.Http;
using Azure.ResourceManager;
`;
const resource = `
@armProviderNamespace namespace Microsoft.Coverage;
model Widget is ProxyResource<{}> { ...ResourceNameParameter<Widget>; }
`;
const read = (decorators = "", response = "ArmAcceptedLroResponse") => `${resource}
@armResourceOperations interface Widgets {
  ${decorators}
  read is ArmResourceRead<Widget, Response = ${response}>;
}`;
const legacy = (decorators = "", scope = "") => `
@service namespace Contoso;
${decorators}
@Azure.ClientGenerator.Core.Legacy.markAsLro${scope}
@get @route("/read") op read(): { value: string; };
`;
const extension = (value) => `@TypeSpec.OpenAPI.extension("x-ms-long-running-operation", ${value})`;
const controls = [
  ["customized-get-lro", read(), [arm]],
  ["native-false-flag", read(extension("false")), [arm]],
  ["synchronous-read", read("", "ArmResponse<Widget>"), []],
  ["native-suppression", read(`#suppress "${arm}" "Approved control exception."`), []],
  ["legacy-common", legacy(), [sdk]],
  ["legacy-csharp", legacy("", '("csharp")'), [sdk]],
  ["legacy-options-scope", legacy("", '(#{scope: "javascript"})'), [sdk]],
  ["legacy-negative-scope", legacy("", '("!csharp")'), [sdk]],
  ["legacy-false-flag", legacy(extension("false")), [sdk]],
  ["extension-and-legacy", legacy(extension("true")), [sdk]],
  ["legacy-suppression", legacy(`#suppress "${sdk}" "Approved control exception."`), []],
  [
    "unmarked-get",
    '@service namespace Contoso; @get @route("/read") op read(): { value: string; };',
    [],
  ],
  ["non-get-lro", `${resource} @post @route("/start") op start(): ArmAcceptedLroResponse;`, []],
  [
    "flag-only",
    `@service namespace Contoso; ${extension("true")} @get @route("/read") op read(): { value: string; };`,
    [],
  ],
  [
    "options-only",
    `@service namespace Contoso; @TypeSpec.OpenAPI.extension("x-ms-long-running-operation-options", #{}) @get @route("/read") op read(): { value: string; };`,
    [],
  ],
  [
    "linked-get",
    `${resource}
    model Status { @Azure.Core.lroStatus status: "Succeeded" | "Failed" | "Canceled"; }
    @route("/status") @get op poll(): Status;
    @Azure.Core.pollingOperation(poll, {})
    @route("/start") @get op start(): { @statusCode statusCode: 202; };`,
    [arm],
  ],
  ["arm-all-native-get", read(), [arm], true],
];
const results = [];
try {
  for (const [name, source, expected, armAll = false] of controls) {
    for (const nativeMode of ["configured", "target-only"]) {
      const directory = path.join(output, `${name}-${nativeMode}`);
      fs.mkdirSync(directory);
      fs.writeFileSync(path.join(directory, "main.tsp"), prelude + source);
      fs.writeFileSync(
        path.join(directory, "tspconfig.yaml"),
        `linter:
  extends:
    - "${armAll ? "@azure-tools/typespec-azure-resource-manager/all" : "@azure-tools/typespec-azure-rulesets/resource-manager"}"
    - "@azure-tools/typespec-azure-rulesets/client-sdk"
`,
      );
      const input = path.join(directory, "input.json");
      const receiptPath = path.join(directory, "output.json");
      fs.writeFileSync(
        input,
        JSON.stringify({
          specsRepo: specs,
          project: { sourcePath: directory, apiVersion: "2026-01-01" },
          validatorRule: "GetOperationMustNotBeLongRunning",
          tspRules: [arm, sdk],
          scope: "source",
          nativeMode,
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
          receiptPath,
        ],
        { encoding: "utf8", timeout: 120_000 },
      );
      assert(!child.error, child.error?.message);
      assert(fs.existsSync(receiptPath), child.stderr);
      const receipt = JSON.parse(fs.readFileSync(receiptPath, "utf8"));
      assert.equal(receipt.status, "success", JSON.stringify(receipt));
      assert.equal(receipt.error, undefined);
      assert.deepEqual(
        receipt.rawDiagnostics.map((item) => item.rule).sort(),
        [...expected].sort(),
        name,
      );
      if (nativeMode === "configured") {
        assert.deepEqual(
          receipt.defaultTargetDiagnostics.map((item) => item.rule).sort(),
          armAll ? [arm] : [],
          name,
        );
      } else {
        assert.equal(receipt.defaultActivation, "not-assessed");
      }
      assert(
        receipt.packages.some(
          (item) => item.name === "@azure-tools/typespec-azure-resource-manager",
        ),
      );
      assert(
        receipt.packages.some(
          (item) => item.name === "@azure-tools/typespec-client-generator-core",
        ),
      );
      results.push({
        name,
        nativeMode,
        expected,
        actual: receipt.rawDiagnostics,
        defaultTargetDiagnostics: receipt.defaultTargetDiagnostics,
        packages: receipt.packages,
        status: "passed",
      });
      process.stdout.write(`${name} ${nativeMode}: passed\n`);
    }
  }
} finally {
  fs.unlinkSync(path.join(output, "node_modules"));
  fs.writeFileSync(
    path.join(output, "summary.json"),
    JSON.stringify(
      {
        status: results.length === controls.length * 2 ? "passed" : "incomplete",
        expected: controls.length * 2,
        passed: results.length,
        results,
      },
      null,
      2,
    ) + "\n",
  );
}

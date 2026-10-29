import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import fs from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";
import { pathToFileURL } from "node:url";

const candidate = String.raw`$NATIVE`;
const root = path.join(candidate, "packages", "typespec-azure-resource-manager");
const require = createRequire(path.join(root, "package.json"));
const load = (name) => import(pathToFileURL(require.resolve(name)).href);
const { createTester } = await load("@typespec/compiler/testing");
const { getSourceLocation } = await load("@typespec/compiler");
const { getHttpOperation } = await load("@typespec/http");
const rule = "@azure-tools/typespec-azure-resource-manager/use-scope-path-standard-name";
const setup = `
@service @armProviderNamespace namespace Microsoft.Test;
model WidgetProperties { description?: string; }
model Widget is ProxyResource<WidgetProperties> {
  ...ResourceNameParameter<Widget>;
}
interface Operations extends Azure.ResourceManager.Operations {}
`;
const tester = createTester(root, {
  libraries: [
    "@typespec/http",
    "@typespec/rest",
    "@typespec/versioning",
    "@azure-tools/typespec-azure-core",
    "@azure-tools/typespec-azure-resource-manager",
  ],
}).importLibraries().using("Http", "Rest", "Versioning", "Azure.ResourceManager");
const documents = [
  path.join(root, "src", "rules", "use-scope-path-standard-name.md"),
  path.join(candidate, "website", "src", "content", "docs", "docs", "libraries",
    "azure-resource-manager", "rules", "use-scope-path-standard-name.md"),
];
const receipts = [];
for (const document of documents) {
  const content = fs.readFileSync(document, "utf8");
  const cases = [
    { heading: "❌ Incorrect", count: 2 },
    { heading: "✅ Correct", count: 0 },
  ];
  for (const { heading, count } of cases) {
    const section = content.split(`## ${heading}\n`);
    assert.equal(section.length, 2, `Unambiguous semantic section: ${heading}`);
    const body = section[1].split("\n## ")[0];
    const snippets = [...body.matchAll(/```tsp\r?\n([\s\S]*?)```/g)];
    assert.equal(snippets.length, 1, `Unambiguous snippet in ${heading}`);
    const snippet = snippets[0][1];
    const [result, diagnostics] = await tester.compileAndDiagnose(setup + snippet, {
      compilerOptions: { linterRuleSet: { enable: { [rule]: true } } },
    });
    assert.equal(diagnostics.length, count, JSON.stringify(diagnostics.map(({ code, message }) => ({ code, message }))));
    for (const diagnostic of diagnostics) {
      assert.equal(diagnostic.code, rule);
      assert.equal(diagnostic.severity, "warning");
      assert.equal(diagnostic.target.kind, "Operation");
      assert.equal(diagnostic.target.name, "read");
      const [http, httpDiagnostics] = getHttpOperation(result.program, diagnostic.target);
      assert.equal(httpDiagnostics.length, 0);
      assert.equal(http.path, "/subscriptions/{subId}/resourceGroups/{groupName}/providers/Microsoft.Test/widgets/{widgetName}");
    }
    if (count) {
      assert.deepEqual(diagnostics.map((item) => item.message), [
        "Resource-group paths must include '/resourceGroups/{resourceGroupName}'.",
        "Subscription paths must include '/subscriptions/{subscriptionId}'.",
      ]);
    }
    receipts.push({
      document: path.relative(candidate, document),
      documentSha256: createHash("sha256").update(content).digest("hex"),
      heading,
      snippet,
      audience: "ARM resource authors",
      template: "ArmResourceRead<Widget, BaseParameters = CustomBase>",
      diagnostics: diagnostics.map(({ code, message, target }) => {
        const location = getSourceLocation(target);
        return { code, message, target: target.name, pos: location.pos, end: location.end };
      }),
    });
  }
}
const receipt = { candidate, setup, rule, documents: receipts };
fs.writeFileSync(path.join(import.meta.dirname, "documentation-examples.json"), JSON.stringify(receipt, null, 2) + "\n");
console.log(JSON.stringify({ status: "passed", documents: 2, snippets: 4, diagnostics: [2, 0, 2, 0] }));

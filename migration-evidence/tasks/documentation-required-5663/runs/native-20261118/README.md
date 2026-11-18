# November 18 frozen native comparison

## Inputs and result

Candidate: `Azure/typespec-azure@2c6596126f281d78ca06fb23afc9ef8ab37684b8`; core: `8574d5453f7bf9a07dc09bd41edac579af71d94b`; tooling: `Azure/typespec-azure@c19c77b9006f7103f4a7a79e408a929845cf113f`. Frozen specs: `Azure/azure-rest-api-specs@6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc`.

Specs are independently preserved at [msyyc/azure-rest-api-specs:evidence/shared-swagger-baseline-20261117-source](https://github.com/msyyc/azure-rest-api-specs/tree/evidence/shared-swagger-baseline-20261117-source), verified at the exact frozen SHA. No companion source or suppression changes enter the coverage runtime.

The [baseline descriptor](baseline-descriptor.json) is pinned from metadata commit `2c35e1f6a7139768b03234983ad201d8fefa4d0b` on `msyyc/azure-rest-api-specs:evidence/shared-swagger-baseline`. Its immutable baseline is `swagger-arm-20261117-6eeeaa99`, identity `7eebd1aed4f40d8305c29be3ecbf6b4ee4585db2f4b3b1b4fe5c800fac7583d8`. The shared archive has 53,558,923 bytes and SHA-256 `0331b41caeb28ef10ff3a2d023c96eed14561b357e4179b4fb537969469af20c`. All 99,960 retained dataset files/hashes and the 490-project population were verified before reuse.

The candidate uses Node v26.5.0, compiler 1.17.0, Azure Core 0.73.0 and AutoRest 0.73.2. The producer uses compiler 1.18.0; this is explicitly `frozen-reference`, not equal emission. Candidate preparation used its pnpm 11.10.0; specs/integration execution used the frozen specs' pnpm 12.6.0 and the machine-approved registry.

Both Swagger validators map to the single official `@azure-tools/typespec-azure-core/documentation-required` rule. `uninformative` belongs to DescriptionMustNotBeNodeName; `empty` belongs to DescriptiveDescriptionRequired. Existing `default` missing-doc diagnostics are audit-only exclusions. Different message families are disjoint diagnostics, not deduplicated actionable defects.

The full native run assessed 490/490 projects with no failures. [Summary](scoped-summary.json): 88,500 Swagger versus 8,387 native quality diagnostics, including 535 actually captured suppressed findings. [Project differences](per-project-counts.json), [failure inventory](failed-projects.json), [diagnostics](native-quality.jsonl), and [source witnesses](investigation.json) retain the evidence. Exact defect correspondence remains undetermined.

## Suppression observation

The standard harness honors authored suppressions. A session-only Node load hook instrumented only the reviewed source worker in memory. On each successful already-compiled program it invoked the exact injected mapped linter before compiler suppression and required every configured diagnostic to be reproduced as a multiset subset. The difference is captured suppressed diagnostics, not inferred violations or another compile. The production compiler, linter packages and tracked harness were not edited.

The [portable observer](helpers/observe-suppressions.mjs) differs from the executed helper only in its machine-specific worker-path configuration and repository formatting. [Helper provenance](helper-provenance.json) binds original/published bytes and the reviewed worker hash. Direct and ancestor suppression capture passed in both execution modes; [the eight fixture sources and 16 results](documentation-control-results.json) retain assertions. The [portable fixture driver](helpers/documentation-controls.mjs) changes path configuration, formatting and stdout logging to satisfy the repository linter; fixture sources and assertions are unchanged.

## Read saved evidence

Use the committed summary and individual diagnostics for a count audit. The standard analyzer's unfiltered mixed-rule `coverage.json` and receipts, all pre-suppression sidecars, build/pack/control logs, runtime installation manifests, and exact 20 candidate package tarballs are in the immutable [native archive](archive.json). The shared Swagger dataset is referenced by its original immutable asset, not duplicated.

Every archived text file is a portable copy with reviewed checkout prefixes replaced and UTF-8/LF serialization. `archive-inventory.json` inside the asset records both original and published hashes/bytes. Diagnostic counts, messages and project-relative targets are unchanged. Standard manifest hashes that bind original machine receipts remain original provenance; use the archive inventory for portable-file integrity.

## Reanalyze downloaded observations

Download the exact native asset identified by `archive.json`, verify size/SHA-256, extract into a new directory, then run:

```powershell
python .\helpers\reanalyze.py --run <extracted-native-archive>\full-native --output <new-analysis-directory>
```

Replace angle-bracket paths with absolute Windows paths. The helper requires all 490 receipts and all successful sidecars, checks configured/suppressed/pre-suppression accounting, excludes only existing missing-doc findings, and recomputes both directional gaps and member totals. It does not compile specs or prove defect correspondence. Compare its generated summary, project counts and quality shard with the published files. The archive's separate exclusion shard retains all 11,260 existing missing-documentation findings.

## Fully rerun the frozen comparison

Recover the exact candidate/core/tooling commits and preserved specs commit into separate clean worktrees under the selected worktrees folder. Recover and verify the shared baseline with the pinned tooling's `shared_baseline.py` and descriptor; it is a sealed Swagger-only baseline, not a completed native run. Recover the exact candidate tarballs from the native archive and verify their hashes against its preparation receipt. Build logs and [payload/source verification](artifact-source-verification.json) bind those packages to candidate source.

Select pnpm 12.6.0 for the analyzer and its integration children. Set process-local configuration to retain the approved registry and disable automatic manager changes; do not alter global registry or TLS settings. Configure the observer:

```powershell
$env:COVERAGE_NATIVE_WORKER = '<tooling>\packages\typespec-lintdiff\test\harness\native-coverage-worker.mjs'
$observer = (Get-Item -LiteralPath '.\helpers\observe-suppressions.mjs').FullName
$env:NODE_OPTIONS = '--import=' + ([System.Uri]::new($observer)).AbsoluteUri
```

Before full execution, run applicable portable controls and the selected documentation controls against the injected packages. For the latter set `COVERAGE_SPECS_REPO` to the prepared specs root and `COVERAGE_CONTROL_OUTPUT` to an existing, empty run directory created for this invocation, then execute `helpers\documentation-controls.mjs` with Node. The driver creates isolated fixtures outside frozen source and a runtime dependency junction; remove only that known junction if cleaning fixtures.

From the pinned tooling's `packages\typespec-lintdiff`, with the recovered baseline and candidate tarballs:

```powershell
node --import tsx/esm test\harness\native-coverage.ts `
  --candidate-repo <candidate> `
  --specs-repo <specs> `
  --tgz-dir <recovered-tarballs> `
  --validator-rule DescriptionMustNotBeNodeName `
  --validator-rule DescriptiveDescriptionRequired `
  --tsp-rule @azure-tools/typespec-azure-core/documentation-required `
  --scope source `
  --baseline-run <verified-shared-baseline> `
  --baseline-policy frozen-reference `
  --native-mode target-only `
  --native-budget-seconds 7200 `
  --output <new-empty-output> `
  --concurrency 2
```

No filter/limit is permitted for this population. The analyzer invokes only integration patch/install, not checkout/reset. It verifies/copies the saved Swagger data and runs native workers. Preserve nonzero results and failures rather than silently dropping projects or regenerating Swagger. Reanalyze the completed receipts with the published helper and rewrite the main and both member reports from the scoped results and investigations.

The actual full run, source/payload controls, archive download/hash/inventory recovery and remote-only saved-observation reanalysis are verified separately in publication receipts. Recovery does not claim another full 490-project recompilation. Compiler/source/emission correspondence, full-package tests, review checkpoints and external CI are separate acceptance requirements.

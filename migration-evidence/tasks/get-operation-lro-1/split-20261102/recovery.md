# Split-rule evidence and recovery

## Frozen inputs and publication

- Candidate: `Azure/typespec-azure`, commit `7e6def9b192f04147a6fb8b0929a24f5d978ab9e`, existing PR #5889. Fetch the exact source commit and initialize `core` at `780c2c6a944d2f6be276b60f890854f7a18b2955`. Do not replace the core gitlink with latest.
- Tooling: `Azure/typespec-azure`, commit `52eeec48b136f97addc10d90dcba4457a04f83a7`. Relevant tooling files were clean before execution; the run manifest also content-binds them.
- Specs: `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`, preserved in verified `msyyc/azure-rest-api-specs` branch `evidence/long-running-operations-options-validator-20261022-source`. The remote ref was verified to equal this SHA.
- Shared baseline metadata: `msyyc/azure-rest-api-specs`, commit `317e703b3e380d3b64e0dacb3a2c6fc0651de253`, descriptor `.lintdiff-baselines/swagger-arm-20261026-2cd3c5dd/baseline.json`. Discovery and immutable version descriptors agree. [Selected descriptor](baseline-descriptor.json).
- Shared baseline release: `swagger-lint-baseline-20261026-2cd3c5dd`, asset `swagger-arm-20261026-2cd3c5dd.tar.gz`, SHA-256 `0904cbd17e24ce076e7969837b85b1f5b3682e5ae25b8805b048fb506e77c1d0`, 51,932,501 bytes.
- [Split evidence release](https://github.com/msyyc/typespec-azure/releases/tag/lintdiff-get-operation-lro-split-7e6def9b). [Asset identities](assets.json) bind the package, native-result and control archives. Historical release assets are unchanged.

The shared baseline was freshly downloaded and integrity-verified. The full analyzer then independently validated/reused it and ran native workers for all 487 projects. No Swagger generation or Swagger-linter rerun occurred.

## Read saved evidence

```powershell
node .\split-20261102\replay.mjs
```

Run this from the containing task directory. It independently recomputes counts from saved project rows and exact operation evidence. It is a saved-observation count audit, not a compiler run or automatic semantic-equivalence decision.

The compact coverage report, all twelve inspected targets, preflight summary, actual documentation-example receipt, baseline descriptor and execution plan are checked in beside this file. Complete raw worker receipts, package inventories and build/control logs are release assets, not generated corpora committed to Git.

## Recover exact artifacts

Download the three named assets in `assets.json` with `gh release download --repo msyyc/typespec-azure --pattern <asset>`. Verify every byte count and SHA-256 before extraction into new directories. Never overwrite prior runs. The package archive contains all 17 exact `.tgz` files and the complete 2,951-file content audit. No removed Core bridge output is present.

The native archive excludes `dataset`: recover that input from the descriptor-bound shared Swagger baseline above. Its original `baseline.json`, manifest and complete dataset remain in the shared baseline asset. Native results retain their own manifest, coverage, runtime installation, raw worker receipts and logs.

The [publication receipt](publication.json) records upload/download verification separately from the already-passed saved count audit. Publication is incomplete while that receipt is pending. A second cold rebuild/full native compilation was not executed or claimed.

`package-evidence.py LOCAL_RUN_DIRECTORY NEW_ASSET_DIRECTORY` creates these three archive groups without replacing an existing destination. It excludes the shared dataset and rejects symlinks. A new compilation must receive a new release identity rather than overwrite these published assets.

## Rebuild, if artifacts are unavailable

Use the candidate's pinned mise tools and dependency locks. Install only missing prerequisites; avoid speculative installs.

```powershell
mise trust
mise exec -- pnpm -r --filter "@azure-tools/typespec-autorest..." --filter "@azure-tools/typespec-azure-rulesets..." --filter "@typespec/integration-tester..." build
```

Use repeated `--only=<name>` selectors for `chronus pack`. Pack the six Azure packages from the Azure workspace and the eleven `@typespec` packages from the `core` workspace. The Azure Chronus config intentionally ignores core packages. Disable pnpm's automatic dependency verification when using prepared injected runtimes: `--config.verify-deps-before-run=false`.

The exact package names, source manifests, source-matched packed files and archive hashes are retained in the package audit. `audit-artifacts.py CANDIDATE ARTIFACT_DIRECTORY NEW_AUDIT_JSON` checks them. The original build command succeeded; its following packing attempt required corrected repeated selectors. Successful final packing logs are separate. No production code repair was needed for that packaging issue.

## Recover and rerun the comparison

Use new directories outside the candidate/specs checkouts. `C:\work` below is a placeholder for your chosen worktree boundary.

```powershell
mise exec -- python -B C:\work\tooling\.github\skills\analyze-native-lint-coverage\shared_baseline.py fetch `
  --descriptor C:\work\evidence\baseline-descriptor.json `
  --output C:\work\baseline
```

Use a clean, separately writable specs checkout at the frozen source commit. Preserve the approved registry. The specs declare pnpm `12.6.0`; run the analyzer's Node entrypoint with that manager on `PATH`, not through a mismatched tooling pnpm script.

Before full execution, run the supported integration CLI's `patch` and `install` stages with the recovered tarballs. Its `install` stage restores tracked dependency files. Do not invoke `checkout`, which can reset a reusable checkout.

From the tooling checkout, run all applicable portable controls with `NATIVE_COVERAGE_SPECS_REPO` set:

```powershell
mise exec -- pnpm --config.verify-deps-before-run=false --dir packages\typespec-lintdiff exec vitest run `
  test\harness\native-coverage-worker.test.ts `
  --testNamePattern "^(?!.*evaluates injected resource-group rule)"
```

This exact candidate lacks the unrelated `resource-group-path-parameter` rule: six associated fixtures are not applicable, not passes. All 37 portable controls passed. Run `injected-controls.mjs SPECS TOOLING NEW_OUTPUT` for the additional thirty configured/target-only split controls. They verify production-preset opt-in behavior, scopes, false flags, native and SDK distinctions, overlap and suppression.

From `tooling\packages\typespec-lintdiff`, with specs pnpm on `PATH`:

```powershell
mise exec pnpm@12.6.0 -- node --import tsx/esm test\harness\native-coverage.ts `
  --candidate-repo C:\work\candidate `
  --specs-repo C:\work\specs `
  --tgz-dir C:\work\artifacts `
  --validator-rule GetOperationMustNotBeLongRunning `
  --tsp-rule @azure-tools/typespec-azure-resource-manager/no-get-lro `
  --tsp-rule @azure-tools/typespec-client-generator-core/no-get-lro `
  --scope source --baseline-policy frozen-reference --baseline-run C:\work\baseline `
  --native-mode target-only --native-budget-seconds 7200 --concurrency 2 `
  --output C:\work\new-native-run
```

Do not add a filter/limit or regenerate Swagger. Setup and baseline checks are outside the native budget. For this run, native execution took 28m25s; total setup/integrity work took substantially longer.

Run `inspect-findings.mjs SPECS TOOLING NEW_NATIVE_RUN NEW_INSPECTION_DIRECTORY` to reproduce operation-level attribution and selected-version HTTP membership. It uses the actual injected Core/SDK helpers, exact source positions, actual HTTP paths and saved Swagger operations. This is focused gap analysis after a full run, not a filtered substitute for the full population.

To regenerate `migration.md`, use the new `coverage.json`, inspected operation evidence and verified source excerpts with the same four-section report format. Keep the approved broader policy explicit, preserve all raw counts, and re-check every differing project and external-integration outcome. The reviewed prose is authored analysis; the saved count-audit script does not silently regenerate or certify it.

## External integration

Current-head run `41402813520` and pre-split run `41386057187` both fail in 64 folders. Their exact diagnostic multisets match: 754 `no-query-in-post`, 45 `use-model-request-body`, 42 `no-response-body`, and zero `no-get-lro` diagnostics. [Machine-readable comparison](integration-comparison.json).

Those existing rule implementations and Core source are unchanged by this split. The failed required check is disclosed, not reclassified as a pass or hidden by the green frozen-corpus run. No unrelated rules, suppressions or specs were changed to make CI green.

# Recovering the consolidated system-data evidence

## Three distinct recovery paths

1. **Read:** inspect [migration.md](migration.md), complete current receipts under `runs/fix5892-20261106`, [candidate.json](candidate.json) and [assets.json](assets.json). Reading does not execute either engine.
2. **Recount:** from this directory, run `node recount.mjs runs\fix5892-20261106\observations.json`. This dependency-free saved-observation reanalysis matches all 487 project rows and totals, retains failures and both excess directions, and does not prove semantic equivalence.
3. **Regenerate:** recover the pinned source/runtime/packages and shared baseline, run the controls, then execute fresh native diagnostics over all 487 frozen projects as below. The independent recovery gate reconstructed inputs; it did not perform a second full native corpus execution.

The prior recursive 0/2 run, assets and recovery instructions remain historical at [evidence commit `810d5c9`](https://github.com/msyyc/typespec-azure/tree/810d5c9565db742ce370544dea42633c5fa7c687/migration-evidence/tasks/system-data-in-properties-bag). Never use its old `no-nested-system-data` target, inactive-default controls or recursion assertions as the current contract.

## Immutable inputs

Download from the [review-fix release](https://github.com/msyyc/typespec-azure/releases/tag/systemdata-fix5892-20261106):

- `systemdata-fix5892-20261106-inputs.tar.gz`
- 47,131,353 bytes
- SHA-256 `9a1c83bcbe83fe1a0c67d7f904f50397fe0fd2eb97a8f43d7a994117f9f04a13`

Its `inputs.json` catalogs the exact source overlay and deletions relative to canonical base `0ef7decc0047a86e48c44237abc55bf0aab624b9`, 20 package archives, the tooling source archive at `402e3fb202e9a16f0a8c7dfc1b799098cfba879d`, one-time actual-package controls and the baseline descriptor. Candidate core is `microsoft/typespec` commit `f87a4e2d51c5cc0b3d995d4c7542578d55799804`. The release tag is an evidence publication marker, not a native source revision.

The shared Swagger archive remains separately published in [the specs fork release](https://github.com/msyyc/azure-rest-api-specs/releases/tag/swagger-lint-baseline-20261026-2cd3c5dd):

- `swagger-arm-20261026-2cd3c5dd.tar.gz`, 51,932,501 bytes
- SHA-256 `0904cbd17e24ce076e7969837b85b1f5b3682e5ae25b8805b048fb506e77c1d0`
- Baseline identity `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`
- Fresh discovery metadata commit `1c9d2b0e6a596754af1aa793b1906ff3c4ef2bd6`
- Frozen source `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`, preserved in `msyyc/azure-rest-api-specs` at `evidence/long-running-operations-options-validator-20261022-source`

## Independently reconstruct inputs

Use fresh task-owned directories below the chosen worktrees boundary, not the development source or a session cache.

1. Download both named assets with `gh release download --repo ... --pattern ... --dir ...`; verify byte sizes and SHA-256 before extraction.
2. Extract safely into new directories. Verify every `inputs.json` catalog entry, including package metadata names/versions and the 20 archive hashes.
3. Fetch the exact canonical candidate base and its exact core gitlink. Overlay each listed source file from `source`, verify its hash, and remove only individually listed deleted files. Do not copy unpublished development files or resolve moving `main`/`next`.
4. Recover the tooling archive and the complete frozen specs source from their pinned identities. Initialize required tooling submodules and provision only missing supported dependencies using the frozen lock and established native profile.
5. Recover the shared baseline with its supported `shared_baseline.py fetch --descriptor ... --archive ... --output ...` entrypoint and verify its entire sealed inventory. Never regenerate Swagger.

Candidate Git reconstruction begins with:

```powershell
git init --quiet <candidate>
git -C <candidate> fetch --depth 1 https://github.com/Azure/typespec-azure.git 0ef7decc0047a86e48c44237abc55bf0aab624b9
git -C <candidate> -c core.autocrlf=false checkout --detach FETCH_HEAD
git -C <candidate> submodule update --init --depth 1 core
```

Apply the exact cataloged overlay and deletions after checkout. The supported analyzer's `--candidate-working-tree true` records and verifies that snapshot; no unpublished local commit is required for reproduction.

The [new independent receipt](fresh-recovery.json) verifies the public download, remote candidate/core checkout, 33 catalog files, 15 source changes/deletions and all 20 package archives. Unchanged complete frozen baseline/specs/tooling recovery proof is retained in the [historical independent receipt](https://github.com/msyyc/typespec-azure/blob/1fc4f11b1bb31a10e123337543bb36701c065175/migration-evidence/tasks/system-data-in-properties-bag/fresh-recovery.json); the entire retained baseline was additionally verified again for this fix. This does not claim a fresh locked transitive install.

## Runtime and actual-package controls

The actual run used Node **26.13.0**, candidate/tooling pnpm **11.10.0** and specs pnpm **12.6.0**. Do not mistake a mise declaration of Node 26.5.0 for the actual executable; record `node --version`. Use the approved registry `https://packagefeedproxy.microsoft.io/npm/` through process-local `PNPM_CONFIG_REGISTRY` and the appropriate child-manager environment, not global config.

The twenty archives include seven Azure packages built from the candidate, ten compiler/library packages built from its exact core, and three unchanged external frozen pins. Verify each package name/version/hash in `inputs.json`; current prettier-plugin-typespec is 1.17.0, not historical 1.16.0.

The existing candidate `core\packages\tsp-integration\cmd\tsp-integration.js` needs its prepared dependency/build closure. Inject only the `patch` and `install` stages with exact `--repo` and `--tgz-dir`, using specs pnpm on PATH; never invoke its checkout/reset stage. Its `finally` restores workspace manifests and locks while retaining injected runtime packages.

Run the archived `run-injected-controls.mjs` with arguments `<specs> <tooling-worker> <actual-rule-Markdown> <new-output>`. The worker is `packages\typespec-lintdiff\test\harness\native-coverage-worker.mjs`; the actual rule document is `packages\typespec-azure-resource-manager\src\rules\no-reserved-resource-property.md`. Eight controls must pass. Published snippets remain excerpts; the one-time helper uses a displayed standard ARM wrapper rather than adding scaffolding to the documentation.

For all applicable portable controls, set `NATIVE_COVERAGE_SPECS_REPO` to the injected specs checkout and run from tooling:

```powershell
mise exec -- pnpm --dir packages\typespec-lintdiff exec vitest run `
  test\harness\native-coverage-worker.test.ts `
  -t '^(?!.*evaluates injected resource-group rule)'
```

This preselected profile passed 37 cases; six cases for an unrelated unmerged resource-group rule were non-applicable, not successful tests. All other portable loading, options, suppression, missing-rule and alignment cases apply.

## Fresh full-population command

Acquire the shared machine/user corpus lock atomically and exclusively before any corpus execution. Hold it through every child process and natural runner completion, recording owner/process/revision and releasing only after exit. The Windows shared location is `$env:LOCALAPPDATA\Copilot\lint-migration\corpus.lock`, not a per-run alternate.

From tooling's **`packages\typespec-lintdiff` directory**, with specs pnpm on PATH:

```powershell
mise exec pnpm@12.6.0 -- node --import tsx/esm test\harness\native-coverage.ts `
  --candidate-repo <candidate-with-verified-overlay> `
  --specs-repo <frozen-specs-runtime> `
  --tgz-dir <downloaded-verified-artifacts> `
  --validator-rule SystemDataInPropertiesBag `
  --tsp-rule @azure-tools/typespec-azure-resource-manager/no-reserved-resource-property `
  --scope source `
  --baseline-run <verified-shared-baseline> `
  --baseline-policy frozen-reference `
  --candidate-working-tree true `
  --output <new-empty-output> `
  --concurrency 2 `
  --native-budget-seconds 3600 `
  --native-mode configured
```

No filter/limit, stale native observations, new Swagger generation or Swagger-linter run is permitted. The analyzer verifies the baseline before/after reuse, freshly executes all native projects and checks final source/artifact/dataset identity. Investigate every failed/unassessed project and every meaningful difference rather than treating missing output as compliance.

The required fix run completed naturally with all 487 projects assessed, zero failures/ambient errors, Swagger 0, shared native 1 (`systemData` 1, `billingData` 0), and independent per-project recount. Both historical source/schema witnesses remain relevant, but the retired embedded-envelope warning is an authorized policy change. Regenerating counts alone cannot decide equivalence or recreate this reasoning; use [differences.md](differences.md) and refresh all four report sections plus NOTES after accepted changes.

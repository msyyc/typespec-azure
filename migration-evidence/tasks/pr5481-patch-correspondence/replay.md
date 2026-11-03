# Recovery and replay

## Read saved evidence

Use the evidence branch and task directory linked by PR #5481. Read
`migration.md`, `evidence-details.md`, `semantic-evidence.md`, the task manifest,
and the final project inventory together. The original machine analyzer's absent Swagger
shard count of zero is not an executed zero: the selected original rule was
staging-only and not evaluated in that production run. The separate
`staging-comparison` directory supplies the subsequent evaluated observations.

The shared Swagger archive is linked and checksummed in
[evidence-details.md](evidence-details.md). Recovering that archive does not
enable its disabled rule or manufacture missing observations.

## Reanalyze saved TypeSpec observations

The committed [integrity inventory](integrity.json) records every task file
except itself. From this task directory, verify recovered files and the actual
Git blob bytes before reanalysis:

```powershell
python -X utf8 -B .\verify-integrity.py . git
```

The [recovery receipt](provenance/recovery-verification.json) records an actual
fresh detached-checkout check, exact full-summary reanalysis, recovery of all
15 package tarballs from Git, and an independent 51,932,501-byte shared-baseline
download/hash round trip. It does not claim another corpus execution or a fully
transitive installation restore.

The dependency-free `reanalyze.py` reads only saved `native-<index>.json`
project receipts. It does not install dependencies, compile TypeSpec, invoke
Swagger validation, or rerun a lint.

From this directory in a fresh evidence checkout:

```powershell
python -X utf8 -B .\reanalyze.py .\runs\full-corpus > recovered-summary.json
```

PowerShell output redirection encoding varies by version. For byte comparisons,
capture Python's stdout as bytes or explicitly use UTF-8/LF. Compare parsed JSON
and the committed numerical summary; do not compare a UTF-16 redirected file's
hash to the UTF-8 publication.

Reanalysis must retain failures/unassessed projects. It must not infer Swagger
counts, cross-engine overlaps, false positives, or prevalence of the controlled
semantic examples. Message families label TypeSpec diagnostics only.

## Recover and reanalyze the staging supplement

Read [provenance/staging-publication.json](provenance/staging-publication.json).
It pins the supplement's immutable specs-fork data commit/path, manifest
identity, separate discovery commit, unchanged production descriptor hash, and
actual recovery verification. Do not recover from an unpinned moving branch or
append anything to the parent baseline.

Use an isolated data checkout of `msyyc/azure-rest-api-specs`, sparsely selecting
`.lintdiff-baselines`, at the receipt's exact data commit. Recover the production
baseline using its original descriptor/archive contract. Before any new
comparison, verify that parent and then run the new tooling's verification CLI:

```powershell
mise exec -- node --import tsx/esm test\harness\staging-supplement.ts `
  --baseline-run $verifiedSharedBaseline `
  --verify-supplement $recoveredSupplement `
  --validator-rule PatchPropertiesCorrespondToPutProperties
```

Run this from `packages\typespec-lintdiff` in the producer tooling pinned in the
receipt. Compare its returned identity with the publication receipt. It verifies
complete input population, parent/source binding, selected rules, raw/shard
inventory and hashes. A failed or partial supplement is not usable.

From the recovered task directory, with all variables set to isolated verified
paths, create a **new** reanalysis output:

```powershell
mise exec -- python -X utf8 -B .\compare-staging.py `
  .\runs\full-corpus $recoveredSupplement $newComparisonOutput
mise exec -- node --import tsx/esm .\crosscheck-staging.mjs `
  $tooling $verifiedSharedBaseline $recoveredSupplement $task `
  $newComparisonOutput $newHarnessReceipt
```

The Node loader must resolve the tooling checkout's installed `tsx` package;
if the evidence checkout has no dependencies, invoke Node through
`pnpm --dir "$tooling\packages\typespec-lintdiff" exec` and use absolute task
script paths. These commands do not install dependencies, regenerate Swagger,
compile TypeSpec, or rerun native diagnostics. Compare generated JSON with the
committed `staging-comparison` readout; differences.md is a derived presentation.

The supplementary emitted-schema investigation is a separate, bounded
validator-only replay, not native execution:

```powershell
mise exec -- node --import tsx/esm .\inspect-staging.mjs `
  $tooling $verifiedSharedBaseline $recoveredSupplement `
  $newComparisonOutput $newSchemaInvestigation
```

Generate the complete one-sided classification table from that saved inspection:

```powershell
mise exec -- python -X utf8 -B .\compare-staging.py --schema-summary `
  $newSchemaInvestigation $newOneSidedMarkdown
```

It replays every retained Swagger input for projects with findings on either
side, including every one-sided project. It checks actual package content
identities and exact selected-rule observations against the sealed supplement,
then classifies the original helper's leaf-schema differences. It does not
pair source diagnostics using property names. The report's four numbered
sections remain an authored semantic assessment; counts alone cannot regenerate
that conclusion.

`reproduce-staging-cache.mjs` accepts tooling, verified parent and a new output
path. It demonstrates the shared-resolver failure and isolated-resolver success
on the exact frozen ApiManagement/ContainerApps inputs; see
`provenance/staging-cache-regression.json`. Cancelled initial attempts are
recorded separately and are never substituted for the completed supplement.

## Regenerate a new TypeSpec execution

This is a distinct, expensive operation. Saved-observation recovery is not proof
that a complete fresh native rerun was performed.

Recover the exact candidate/core, tooling, frozen specs source, and package
artifacts identified in the provenance. Verify the preserved specs ref against
`2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`, and verify artifact byte hashes before
injection. Use isolated clean worktrees, not the original machine paths.

Build command used for the candidate closure:

```powershell
mise exec -- pnpm -r --filter '@azure-tools/typespec-autorest...' --filter '@azure-tools/typespec-azure-rulesets...' --filter '@typespec/integration-tester...' build
```

Packages were packed using the existing Chronus pack command. Supply a separate
`--only=<package>` for each package; a PowerShell array after one `--only` does
not select multiple packages. Candidate/core and tooling use pnpm 11.10.0.
The frozen specs runtime uses pnpm 12.6.0.

Invoke the candidate's existing integration CLI with **patch/install stages
only**; do not run a checkout/reset stage over the preserved source. Example,
with the variables set to verified isolated paths:

```powershell
$env:PNPM_CONFIG_REGISTRY = 'https://packagefeedproxy.microsoft.io/npm/'
mise exec pnpm@12.6.0 -- node "$candidate\core\packages\tsp-integration\cmd\tsp-integration.js" azure-specs --repo $specs --stage patch --stage install --tgz-dir $packages
```

From the exact tooling's `packages\typespec-lintdiff` directory, the full
execution used:

```powershell
mise exec pnpm@12.6.0 -- node --import tsx/esm test\harness\native-coverage.ts `
  --candidate-repo $candidate `
  --specs-repo $specs `
  --tgz-dir $packages `
  --validator-rule PatchPropertiesCorrespondToPutProperties `
  --tsp-rule '@azure-tools/typespec-azure-resource-manager/arm-resource-patch' `
  --scope source `
  --baseline-run $verifiedSharedBaseline `
  --baseline-policy frozen-reference `
  --native-mode target-only `
  --native-budget-seconds 10800 `
  --concurrency 2 `
  --output $newEmptyOutput
```

There is deliberately no project filter or limit. The budget applies to the
native execution stage, not installation or shared-baseline integrity/copy
preparation. Keep the 487-project population and any failures visible.

That historical analyzer checks the original rule's registration, but does not recognize
that its absent production shard means it was disabled. Preserve its machine
report as a receipt; use the authored not-evaluated interpretation, not its
numerical zero, in any migration decision.

For a future fresh comparison, use the new supplement-aware tooling and add
`--staging-supplement $recoveredSupplement` to the normal full native command.
It rejects the selected staging-only rule without evaluated supplemental data.
This task did not execute that fresh native path: it reused the unchanged,
content-verified native observations above.

Actual injected installation locks and package entrypoint hashes are provenance
receipts, not a fully portable transitive lock. Some runtime dependencies
resolved from ranges. A new install may not reproduce identical bytes or
findings. Do not promise identical totals without verifying that new runtime.

Rerun the selected real-linter activation/suppression controls and focused
semantic examples before drawing a new conclusion. Recheck source projection,
historical version names/types, unsupported-body boundaries, and consolidated
older rule checks. Counts alone cannot regenerate the semantic report.

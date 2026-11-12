# Verification and replay

## Current evidence

Read [migration.md](migration.md),
[the direct-constraint assessment](direct-20261112/assessment.md),
[task metadata](refresh-20261112-direct/task.json) and the
[487-project comparison](refresh-20261112-direct/staging-comparison/summary.json).
The current candidate is **`f2079b23690d816ecc92a858fab2c1572e9448b5`**:
**104 warnings, all 487 projects successful, clean CLI completion**.
Other run directories remain immutable historical evidence; their whole-tree
seals do not cover the current publication.

From this task directory, verify the current whole-task inventory, relative
links, all members of 15 archives, installed package entrypoint receipts,
51 extractor bindings, controls and authored-example receipts:

```powershell
python -B .\direct-20261112\verify-publication.py .
python -B .\direct-20261112\reconcile.py --check
```

The [inventory](refresh-20261112-direct/provenance/publication-inventory.json)
excludes only itself. This checks saved evidence, not a new compile.
Published receipts retain selected findings, ambient errors, status and runtime
packages; unrelated ambient warnings are omitted and absolute roots sanitized.
Raw/published hashes are in the
[receipt ledger](refresh-20261112-direct/provenance/receipt-transformations.json)
and [capture ledger](refresh-20261112-direct/source-attribution/transformations.json).

The reconciliation normalizes only the explicitly documented old-to-new
diagnostic suffix when computing behavioral changes. It preserves complete
diagnostic fields and duplicate occurrences, verifies all 51 ordered arrays,
and separates the six deliberately omitted records from 92 compatible/non-input
records. The raw delta remains separately available without that normalization.

## Reanalyze saved results

Recover the unchanged staging supplement through the pinned data commit/archive
in [publication provenance](provenance/staging-publication.json) and the
[original baseline instructions](evidence-details.md#original-swagger-policy-and-frozen-evidence).
Verify parent identity
`aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`
and supplement identity
`e0a2c22b857b13fa8ccf318bff1c8a6beaf367e1a1210cbc71cf7161fd86d482`.
The selected Swagger rule was evaluated in this staging supplement;
its absent production shard means **not evaluated**, not compliant.

With `$recoveredSupplement` set to the verified directory and
`$newComparisonOutput` nonexistent:

```powershell
python -B .\refresh-20261112-direct\compare-staging.py `
  .\refresh-20261112-direct\runs\full-corpus `
  $recoveredSupplement $newComparisonOutput
```

Every output byte must match the committed `staging-comparison` files.
This regenerates the comparison from downloaded observations without package
installation, TypeSpec compilation or Swagger generation.

The underlying exclusion and incidence-checking tests remain reusable:

```powershell
python -B -m unittest discover -s .\assessment-20261105 -p test_assess_diagnostics.py
python -B .\assessment-20261105\assess_diagnostics.py --check
python -B -m unittest discover -s .\count-gap-20261106 -p test_reconcile.py
```

That first assessment's TypeSpec results are historical; only its unchanged
**1,132 excluded / 182 retained Swagger records** support this comparison.
The current incidence equation is
**182 - 104 = 92 + 6 + 1 + 12 - 2 - 31 = 78**.
Scripts check observations and membership, not the authored policy decision or
unestablished cross-version defect identity.

## Actual execution

The final CLI ran **2026-11-12 03:35:24-04:14:33 UTC** and sealed a
`complete` manifest with exit code **0**, **487 successful projects** and
**104 findings**. It reused the frozen Swagger baseline and evaluated staging
supplement. All required final integrity/report stages ran inside the CLI;
no post-exit recovery or replacement native run was necessary.

The following supplemental work separately executed actual published
Incorrect/Correct snippets, 12 extraction/suppression controls and source
capture for all 51 retained-record projects. Captured diagnostic arrays equal
their full-run arrays exactly, including order. These source-predicate probes
are not substitute full runs or Swagger regeneration.

The preceding November 10 observation at `ade5040b6` had **108 findings**
and exited during finalization with its manifest still `running`.
Its [content-bound recovery receipt](refresh-20261110-wrapper/provenance/integrity-reconciliation.json)
and [dated assessment](wrapper-20261110/assessment.md) remain immutable.
That historical recovery is not this run's completion evidence; its old
whole-task inventory is not a seal of the current task tree.

## A genuinely new execution

Saved-data checks do not constitute fresh TypeSpec execution.
Recover the exact candidate/core, artifacts and runtime from the
[prepared plan](refresh-20261112-direct/provenance/plan.json).
Current source is `f2079b23690d816ecc92a858fab2c1572e9448b5`;
core is `e06f6b34fdad9d7f49bfc084a598b03c60684e9a`;
actual generator and replay tooling are both
`4dda34822b8877d997b6b5ab6525b70e8379ba0d`.
Specs remain `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`, preserved through
the recorded fetchable personal-fork source ref/canonical commit.
The inherited plan's old `toolingRevisionVerification` text is historical,
not a conflicting current generator identity.

Use isolated clean candidate/specs worktrees, verify all artifacts and the
sealed baseline/supplement, then use the existing integration runner's
**patch/install stages only**, never its checkout/reset stage on preserved
sources. The
[process-local override policy](refresh-20261112-direct/provenance/runtime-overrides.json)
retains original workspace overrides and exact candidate archives.
Substitute isolated paths for publication tokens; do not alter global
registry/configuration or silently install latest libraries. This is not a
fully transitive locked-regeneration claim.

From exact tooling `packages\typespec-lintdiff`, with **Node 26.13.0** and
the frozen specs' **pnpm 12.6.0** on PATH:

```powershell
node --import tsx/esm test\harness\native-coverage.ts `
  --candidate-repo $candidate --specs-repo $specs --tgz-dir $packages `
  --validator-rule PatchPropertiesCorrespondToPutProperties `
  --tsp-rule '@azure-tools/typespec-azure-resource-manager/arm-resource-patch' `
  --scope source --baseline-run $verifiedSharedBaseline `
  --baseline-policy frozen-reference --staging-supplement $recoveredSupplement `
  --native-mode target-only --native-budget-seconds 10800 `
  --concurrency 2 --output $newEmptyOutput
```

Keep all 487 projects, failures, suppressions and original exit/status.
A new execution needs its own concrete question and cost/budget; do not
overwrite these observations or regenerate Swagger. Run selected
violating/compliant controls first. Supplemental attribution uses
`direct-20261112\capture-controls.mjs`, `capture-projects.mjs` and the existing
`wrapper-20261110\join-contexts.mjs`.

Publication verification also replays the exact staged Git tree in a temporary
isolated archive and compares regenerated comparison files byte-for-byte.
It performs no native compilation or Swagger generation and does not claim
a second full execution.

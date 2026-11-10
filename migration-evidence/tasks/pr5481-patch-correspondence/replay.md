# Recovery and replay

## Current evidence

Read [migration.md](migration.md), [grouped decisions](gap-investigation.md),
[the current assessment](wrapper-20261110/assessment.md),
[task metadata](refresh-20261110-wrapper/task.json) and the
[487-project comparison](refresh-20261110-wrapper/staging-comparison/summary.json)
together. The current assessed candidate is
**`ade5040b62c25c8cd4eb8a0e99593f5f739c23f2`**, with **108 warnings**.
Earlier run directories remain immutable historical evidence; their whole-tree
seals do not cover this publication.

From this task directory, verify the current whole-task inventory, relative links,
every member of all 15 archives, installed package entrypoint receipts and
the 51 source-extraction bindings:

```powershell
python -B .\wrapper-20261110\verify-publication.py .
```

The [publication inventory](refresh-20261110-wrapper/provenance/publication-inventory.json)
excludes only itself. This is saved-evidence verification, not a fresh compile.
Published receipt copies omit unrelated ambient warnings and replace absolute
roots; copied logs omit terminal empty lines. Selected findings, ambient errors,
statuses and runtime-package evidence remain. Raw/published hashes are retained in the
[receipt transformation ledger](refresh-20261110-wrapper/provenance/receipt-transformations.json)
and [capture ledger](refresh-20261110-wrapper/source-attribution/transformations.json).

## Reanalyze saved results

Recover the unchanged staging supplement through the pinned data commit/archive
in [publication provenance](provenance/staging-publication.json) and the
[original baseline instructions](evidence-details.md#original-swagger-policy-and-frozen-evidence).
Verify parent identity
`aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`
and supplement identity
`e0a2c22b857b13fa8ccf318bff1c8a6beaf367e1a1210cbc71cf7161fd86d482`.
The selected Swagger rule was evaluated in this separate staging supplement;
its absent production shard means **not evaluated**, not compliant.

With `$recoveredSupplement` set to the verified directory and a new nonexistent
`$newComparisonOutput`, reproduce the current raw comparison without installing
packages, compiling TypeSpec or generating Swagger:

```powershell
python -B .\refresh-20261110-wrapper\compare-staging.py `
  .\refresh-20261110-wrapper\runs\full-corpus `
  $recoveredSupplement $newComparisonOutput
```

Compare every output byte with the committed `staging-comparison` files.
The checker refuses an existing output directory and accepts the original
`running` manifest only through its content-bound strict recovery receipt.

Recheck the immutable Swagger exclusions and current incidence accounting:

```powershell
python -B -m unittest discover -s .\assessment-20261105 -p test_assess_diagnostics.py -v
python -B .\assessment-20261105\assess_diagnostics.py --check
python -B -m unittest discover -s .\count-gap-20261106 -p test_reconcile.py -v
python -B -m unittest discover -s .\wrapper-20261110 -p test_reconcile.py -v
python -B .\wrapper-20261110\reconcile.py check
```

The first assessment's TypeSpec counts are historical; its immutable **1,132
excluded / 182 retained Swagger records** are reused. The current checker
verifies all 487 receipts, 51 exact ordered capture arrays, 81 unchanged accepted
schema contexts, the two newly accepted containers and exact diagnostic delta.
It remaps historical outside-join decisions using complete diagnostic records,
preserving duplicates. Independent project sums reproduce
**182 - 108 = 92 + 1 + 14 - 2 - 31 = 74**.
Scripts reproduce observations and membership, not the authored equivalence
decision or an API-version-aware defect identity.

The [historical body supplement](body-assessment-20261106/inventory.json)
was evaluated at `012190397` with 117 warnings; it is not a new inventory.
Its [verifier](body-assessment-20261106/verify.py) can still check those saved
observations separately. Current applicability is supported by
[unchanged classification/selection functions](wrapper-20261110/source-scope.json)
and unchanged body-policy modules in the packed closure.

## Actual execution and recovery

Native execution ran **2026-11-10 06:35:13.591-07:03:25.884 UTC**, within
the original 10,800-second budget, and completed **all 487 projects successfully**.
The CLI exited **-1** after writing every native receipt and coverage report,
before sealing its manifest. Its original status remains `running`; original
receipts/report were not overwritten. **No clean CLI pass is claimed.**

The exact Node 26.5.0 executable was observed missing afterward. The existing
mise manager restored the same version into new task-owned storage; verified
executable SHA-256:
`119d6fa70e6ae1b15b90688ab6bcc8e3a2819acea021af196895cab1843645af`.
Missing executable and process exit are observations, not proof of their cause.
No fallback runtime or global setting change was used.

Independent post-exit gates verified every one of **93,496 dataset files**,
exact path-set equality/no reparse points, source/core/spec snapshots, all
15 artifacts, baseline/supplement identities and exact reconstruction of every
official report field. The [strict recovery receipt](refresh-20261110-wrapper/provenance/integrity-reconciliation.json)
records **108 warnings, zero failed/unassessed projects and zero native reruns**,
binding the original manifest/report hashes.

All **16 extraction controls** then passed. Supplemental capture of all 51
retained-record projects produced diagnostic arrays identical to their full-run
receipts, including order. Those supplemental compiles inspect source predicates;
they are not replacement native runs or Swagger regeneration.

## A genuinely new execution

Saved-data checks do not constitute a new native run. Recover the exact
candidate/core, specs, artifacts and runtime from the
[prepared plan](refresh-20261110-wrapper/provenance/plan.json).
Specs remain `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`.
Preserve the recorded fetchable specs-fork source ref/canonical commit,
not a moving branch. Verify baseline, supplement and artifacts before installation.

The actual generator commit at run start was
`d0a802b0a67610441ee93cc7858bd874bd113697`; the prepared replay commit was
`8345f684fad330568e55e40181c3d17cd8d8db7f`. The
[tooling content-identity proof](wrapper-20261110/tooling-identity.json)
verifies identical lintdiff package tree, root dependency lock/manifest and
execution-file hashes, also unchanged at later observed HEAD `4dda3482...`.
Replay may use the content-equivalent prepared commit without relabeling the
original run's actual generator identity.

Use isolated clean candidate/specs worktrees and the supported candidate
integration runner's **patch/install stages only**, never its checkout/reset
stage over preserved sources. The process-local
[override policy](refresh-20261110-wrapper/provenance/runtime-overrides.json)
retains original workspace overrides, 15 exact archives and eight verified
Scalar versions. Substitute isolated paths for publication tokens. Do not
change shared registry/configuration or silently install latest dependencies.
This evidence is not a fully transitive portable lock.

From exact tooling `packages\typespec-lintdiff`, with recorded pnpm 12.6.0 and
Node 26.5.0 on PATH:

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

Retain all 487 projects, failures, suppressions, control applicability and
original exit/status. A genuinely new execution needs its own concrete question
and cost/budget; do not overwrite these observations or regenerate Swagger.
Run selected violating/compliant controls first. For separately budgeted source
attribution, use `wrapper-20261110\capture-controls.mjs`, `capture-projects.mjs`
and `join-contexts.mjs`. Fresh results require independent verification before
claiming identical totals.

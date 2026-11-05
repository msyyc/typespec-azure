# Recovery and replay

## Current evidence

Read [migration.md](migration.md), [the grouped assessment](gap-investigation.md),
[final task metadata](refresh-20261105-inherited/task.json) and the
[487-project comparison](refresh-20261105-inherited/staging-comparison/summary.json)
together. `refresh-20261105-inherited` is the current assessed candidate,
`0121903975ab45cde7d7aca37cf50ffd7f3855d3`. Earlier directories and their
inventories are frozen historical evidence, not current whole-task seals.

From this task directory, verify the current complete published tree, relative
links and all members of all 15 package archives:

```powershell
python -B .\refresh-20261105-inherited\verify-publication.py .
```

The current [publication inventory](refresh-20261105-inherited/provenance/publication-inventory.json)
excludes only itself. This verification is saved-evidence recovery, not another
compiler run. Runtime package receipts and source/build/packed/installed equality
are in [artifact provenance](refresh-20261105-inherited/provenance/artifact-provenance.json).

## Reanalyze saved results

Recover the immutable staging supplement using the pinned data commit and
archive instructions in [the original recovery evidence](provenance/staging-publication.json)
and [baseline details](evidence-details.md#original-swagger-policy-and-frozen-evidence).
Verify its parent identity `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`
and supplement identity `e0a2c22b857b13fa8ccf318bff1c8a6beaf367e1a1210cbc71cf7161fd86d482`.
The selected Swagger rule was evaluated in this separate staging supplement;
the production baseline's absent shard is **not evaluated**, not zero.

With `$recoveredSupplement` set to that verified directory and a new nonexistent
`$newComparisonOutput`, reproduce the current raw comparison without installing
packages, compiling TypeSpec or generating Swagger:

```powershell
python -B .\refresh-20261105-inherited\compare-staging.py `
  .\refresh-20261105-inherited\runs\full-corpus `
  $recoveredSupplement $newComparisonOutput
```

Compare every output byte with the committed `staging-comparison` files.
The script deliberately refuses to overwrite an existing output directory.
The original running manifest is accepted only with its content-bound
[strict recovery receipt](refresh-20261105-inherited/provenance/integrity-reconciliation.json),
not by treating a failed CLI as successful.

Recheck the retained-record accounting and manual acceptance membership:

```powershell
python -B -m unittest discover -s .\assessment-20261105 -p test_assess_diagnostics.py -v
python -B .\assessment-20261105\assess_diagnostics.py --check
python -B .\inherited-20261105\assess-contexts.py --check
```

The first assessment's embedded TypeSpec counts are historical; its immutable
Swagger 1,132/182 classification is reused. The final checker uses the actual
012190397 source captures and verifies the preceding 79 acceptance contexts,
allowing only package-store location canonicalization after proving all ARM
library members are unchanged. Two Oracle contracts were separately assessed.
Scripts reproduce observations/membership, not the authored equivalence decision.
They do not construct API-version-aware defect identities.

## Actual execution and recovery

The final native stage ran **2026-11-05 14:17:33.843-14:44:04.144 UTC**, within
the original 10,800-second budget. The CLI exited 255 after 134 successful
projects and produced no report. A bounded continuation ran only the remaining
353 projects through the pinned official worker and report builder; no completed
project was rerun. Two interrupted, receipt-less launches were reexecuted.
The original manifest, completed receipts and command log were not overwritten.
[Interruption](refresh-20261105-inherited/provenance/native-continuation/interruption.json),
[continuation](refresh-20261105-inherited/provenance/native-continuation/completion.json)
and [final integrity reconciliation](refresh-20261105-inherited/provenance/integrity-reconciliation.json)
retain those boundaries. **No clean CLI pass is claimed.**

The exact original Node 26.5.0 executable was observed missing. Two no-compilation
preflights rejected fallback 26.13.0; the existing mise manager restored 26.5.0
into a task-isolated tool directory without changing shared tool configuration.
[The repair receipt](refresh-20261105-inherited/provenance/pinned-node-recovery.json)
records its SHA-256. Missing executable and exit 255 are observations, not proof
of a particular deletion/crash cause.

After all workers, independent checks verified every one of **93,496 dataset
files**, exact path-set equality, no reparse points, source/core/spec snapshots,
all 15 artifact hashes, both supplement identities, and every reconstructed
official report field. All 487 projects succeeded with 117 configured warnings.
The subsequent 10 extraction controls passed and all 51 source captures matched
their full-run configured diagnostic multisets.

## A genuinely new execution

Saved-data checks are not a fresh native run. Recover the exact candidate/core,
tooling, frozen specs source, artifacts and runtime from
[the final plan](refresh-20261105-inherited/provenance/plan.json).
Specs remain `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`; preserve the recorded
specs-fork source ref or independently fetchable canonical commit, not a moving
branch. Verify the baseline/supplement and artifacts before installation.

Use isolated clean candidate/specs worktrees and the supported candidate
integration runner's **patch/install stages only**. Never run its checkout/reset
stage over a preserved source checkout. The process-local override
[policy](refresh-20261105-inherited/provenance/runtime-overrides.json)
retains all original workspace overrides, 15 exact candidate archives and eight
verified Scalar versions; substitute isolated paths for publication tokens.
Do not change a shared registry/configuration or silently use current latest
dependencies. This is not a fully transitive portable lock.

From the exact tooling's `packages\typespec-lintdiff`, with the recorded
specs package manager and exact Node runtime on PATH:

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
original exit/status. A new execution needs its own cost/budget and must not
overwrite these observations or regenerate Swagger. Run selected violating and
compliant controls before the full population. Use
`inherited-20261105\capture-controls.mjs`, `capture-projects.mjs` and
`join-contexts.mjs` only for separately budgeted source attribution; these are
supplemental source inspections, not a replacement for full verification.
Fresh runtime results must be verified before claiming identical totals.

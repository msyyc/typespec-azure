# Verification and replay

## Current evidence

Read [migration.md](migration.md),
[the name-only assessment](names-20261117/assessment.md),
[task metadata](refresh-20261117-names/task.json) and the
[487-project comparison](refresh-20261117-names/staging-comparison/summary.json).
The current candidate is **`fb7029f43ef7feaf88a8885070f4775d82e42fff`**:
**85 warnings, all 487 projects successful, clean CLI completion**.
This November 18 report-only refresh retains that exact completed execution.
Other run directories remain immutable historical evidence; their whole-tree
seals do not cover the refreshed Markdown.

From this task directory, verify the current whole-task inventory, relative
links, all members of 15 archives, installed package entrypoint receipts,
51 extractor bindings, controls and authored-example receipts:

```powershell
python -B .\report-20261118\verify-publication.py .
python -B .\names-20261117\reconcile.py --check
```

The [current inventory](report-20261118/publication-inventory.json)
excludes only itself. The
[November 17 inventory](refresh-20261117-names/provenance/publication-inventory.json)
is preserved unchanged and binds the previous report tree at evidence commit
`b225b1daab93a582eecd4660667a9d8eb872c2fe`, not this editorial refresh.
The current verifier reuses all candidate/artifact/execution checks while
binding the refreshed report and supporting note to the new inventory.
This checks saved evidence, not a new compile.
Published receipts retain selected findings, ambient errors, status and runtime
packages; unrelated ambient warnings are omitted and absolute roots sanitized.
Raw/published hashes are in the
[receipt ledger](refresh-20261117-names/provenance/receipt-transformations.json)
and [capture ledger](refresh-20261117-names/source-attribution/transformations.json).

Reconciliation compares complete diagnostic occurrence multisets **without
message normalization or location deduplication**. It checks exactly 19 removed
constraint warnings, no added warnings, all 51 ordered arrays and 26 newly omitted
retained records. The 32 total not-migrated records remain separate from the
92 legitimate accepted/non-input records; native acceptance is not proof of
value compatibility.

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
python -B .\refresh-20261117-names\compare-staging.py `
  .\refresh-20261117-names\runs\full-corpus `
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
**182 - 85 = 92 + 32 + 1 + 3 - 31 = 97**.
Scripts check observations and membership, not the authored policy decision or
unestablished cross-version defect identity.

## Actual execution

The final CLI exited **0** with **487 successful projects** and **85 findings**.
Its [manifest](refresh-20261117-names/runs/full-corpus/manifest.json)
records the exact November 17 UTC start/finish times and `complete` status;
[task metadata](refresh-20261117-names/task.json) retains the exit code. It reused
the frozen Swagger baseline and evaluated staging supplement. All required
final integrity/report stages ran inside the CLI; no post-exit recovery or
replacement native run was necessary.

Supplemental work separately executed actual published Incorrect/Correct
snippets, 12 extraction/suppression controls and source capture for all
51 retained-record projects. Captured diagnostic arrays equal their full-run
arrays exactly, including order. These source-predicate probes are not
substitute full runs or Swagger regeneration.

The November 12 observation at `f2079b236` contained **104 warnings** and retained
direct format/bounds checking. Its [dated assessment](direct-20261112/assessment.md)
remains immutable. The earlier November 10 observation at `ade5040b6`
contained **108 findings** and needed finalization recovery:
[receipt](refresh-20261110-wrapper/provenance/integrity-reconciliation.json).
Neither historical observation nor its old whole-tree seal certifies this
name-only candidate.

## A genuinely new execution

Saved-data checks do not constitute fresh TypeSpec execution.
Recover the exact candidate/core, artifacts and runtime from the
[prepared plan](refresh-20261117-names/provenance/plan.json).
Current source is `fb7029f43ef7feaf88a8885070f4775d82e42fff`;
core is `e06f6b34fdad9d7f49bfc084a598b03c60684e9a`;
actual generator and replay tooling are both
`688486d1e9a1701c34fc912c01705d098625c2a3`.
The relevant lintdiff code, root manifest and lockfile are unchanged from the
previous tooling revision, but the actual current identity is retained.
Specs remain `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`, preserved through
the recorded fetchable personal-fork source ref/canonical commit.

Use isolated clean candidate/specs worktrees, verify all artifacts and the
sealed baseline/supplement, then use the existing integration runner's
**patch/install stages only**, never its checkout/reset stage on preserved
sources. The
[process-local override policy](refresh-20261117-names/provenance/runtime-overrides.json)
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
`names-20261117\capture-controls.mjs`, `capture-projects.mjs` and the existing
`wrapper-20261110\join-contexts.mjs`.

Publication verification also replays the exact staged Git tree in a temporary
isolated archive and compares regenerated comparison files byte-for-byte.
It performs no native compilation or Swagger generation and does not claim
a second full execution.

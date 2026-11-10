# PatchPropertiesCorrespondToPutProperties migration

## 1. Conclusion and scope

The TypeSpec rule `@azure-tools/typespec-azure-resource-manager/arm-resource-patch`
migrates Swagger linter rule
[`PatchPropertiesCorrespondToPutProperties`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-properties-correspond-to-put-properties.md).
**Covered for the assessed diagnostic-driven, current-source input policy;
not full Swagger equivalence.** No observed non-versioning rule gap remains.
The TypeSpec linter intentionally avoids the Swagger linter's metadata-equality
overchecking bug. Historical names, types and operation availability remain
[deferred to #5875](https://github.com/Azure/typespec-azure/issues/5875);
unobserved inputs are not claimed exhaustively equivalent.

## 2. Actual coverage

**487 ARM projects assessed; 0 project failures or unassessed projects.**
Reported diagnostics are individual findings across the population, not projects.

| Count                                                        | Swagger linter | TypeSpec linter |
| ------------------------------------------------------------ | -------------: | --------------: |
| Raw reported diagnostics                                     |          1,314 |             108 |
| Retained PATCH routes inspected (project + exact HTTP route) |             97 |              97 |

**Assessed coverage:** **1,132 confirmed Swagger overchecks are excluded**.
All **182 retained records** are assessed: **90 are check-covered**
(89 reporting records and one authored suppression), and **92 are compatible
inputs or non-input leaves/wrappers that need no additional warning**.
Opaque containers with no Update-visible children are **covered**.

The **108 TypeSpec warnings** comprise **77 witnessed by retained-record
contexts**, **18 additional valid current-source checks to retain**, and
**13 historical/versioning warnings deferred to #5875**. No unexplained
non-versioning warning group remains. The **182 - 108 = 74** difference
reflects acceptance, suppression and reporting multiplicity, not 74 missing
checks; see [Why diagnostic counts differ](#4-why-diagnostic-counts-differ).

The 97-route row measures inspections, not matched defects. Complete
API-version-aware violation totals and coverage percentages remain **unassessed**;
the source-context assessment does not invent cross-version correspondence.

## 3. Function-level coverage

| Behavior                                                               | Result                           | Rationale                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Extra PATCH names, including nested/inherited leaves and encoded names | Covered                          | Checks effective writable inputs; [source-check evidence](gap-investigation.md#assessment-method).                                                                                                                                                 |
| Incompatible value types and supported constraints                     | Covered                          | Diagnoses incompatible wire values, collections and bounds; [evidence](gap-investigation.md#compatibility-fix), not a universal schema-subset solver.                                                                                              |
| ARM operations inherited into project interfaces                       | Covered                          | Evaluates inherited project operation pairs; [evidence](gap-investigation.md#inherited-operation-fix).                                                                                                                                             |
| Missing/empty PATCH or writable PATCH with no PUT input                | Covered                          | Checks absent and empty input; [body evidence](gap-investigation.md#missing-body-correspondence) credits authored suppression.                                                                                                                     |
| Compatible partial inputs and non-input leaves/wrappers                | Covered                          | Accepts valid input contracts rather than requiring identical emitted schemas; [accepted inputs](gap-investigation.md#why-81-schema-contexts-correctly-accept).                                                                                    |
| Same object container with no Update-visible children                  | Covered                          | Resolves the PUT container at the same encoded payload path, preserving visibility and compatibility checks; [evidence and controls](wrapper-20261110/assessment.md#opaque-object-containers).                                                     |
| Indexed request bodies encountered in evaluated services               | Covered by existing library rule | `@azure-tools/typespec-azure-resource-manager/use-model-request-body` reports both observed cases when enabled; [recorded probes](gap-investigation.md#corpus-scope-and-reproducibility). Those separate-profile warnings are not included in 108. |
| Historical names/types, availability and operation selection           | Deferred                         | Requires shared [#5875 versioning support](gap-investigation.md#versioning-boundary), outside the assessed current-source policy.                                                                                                                  |

## 4. Why diagnostic counts differ

The Swagger linter compares whole leaf schemas with
[`_.isEqual`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/patch-properties-correspond-to-put-properties.ts#L15-L70).
Documentation, defaults and harmless request/read-only metadata differences
therefore cause **1,132 false missing-property reports**. **Do not port that bug.**

The first four rows below partition all 1,314 Swagger records. The TypeSpec
column counts distinct configured warnings from the reviewed source checks,
not unrelated warnings on the same operation or proven historical counterparts.
The last three rows partition the 31 warnings outside that join; **unassessed**
means no exact Swagger counterpart is established, not zero Swagger findings.

| Difference (with evidence)                                                                                  | Swagger diagnostics | TypeSpec diagnostics for the same check | Recommended action and rationale                                                                                                        |
| ----------------------------------------------------------------------------------------------------------- | ------------------: | --------------------------------------: | --------------------------------------------------------------------------------------------------------------------------------------- |
| [Metadata/request-filtering overchecks](gap-investigation.md#assessed-diagnostic-records)                   |               1,132 |                                       0 | **Intentionally not ported:** these metadata differences are not missing inputs.                                                        |
| [Compatible inputs and non-input names](gap-investigation.md#reader-scorecard-accounting)                   |                  92 |                                       0 | **Covered acceptance:** retain partial-input and visibility behavior, not schema equality.                                              |
| [Authored suppression](gap-investigation.md#missing-body-correspondence)                                    |                   1 |                                       0 | **Covered:** Quota's implemented check is suppressed; preserve the authored decision.                                                   |
| [Reporting multiplicity](wrapper-20261110/assessment.md#record-to-warning-bridge)                           |                  89 |                                      77 | **Covered:** 91 record-warning associations include 14 repeats and two additional within-record checks. Preserve distinct checks.       |
| [Historical names/availability](count-gap-20261106/analysis.md#historical-versioning)                       |          unassessed |                                      13 | **Defer to #5875**, as requested; do not reconstruct history inside this rule.                                                          |
| [Writable PATCH inputs absent from PUT input](count-gap-20261106/analysis.md#valid-source-checks-to-retain) |          unassessed |                                      17 | **Retain the check:** spec owners should correct unintended writable declarations or confirm/document the contract.                     |
| [Empty PATCH body](gap-investigation.md#netapp-49-swagger--2-typespec)                                      |                   0 |                                       1 | **Retain the check:** Swagger misses NetApp's empty body by counting its existing body parameter; request a model/API-owner correction. |

After the 1,132 exclusions, the exact accounting is:

**182 - 108 = 92 + 1 + 14 - 2 - 31 = 74.**

These terms are accepted/non-input records, suppression, repeated associations,
additional within-record checks and outside-join warnings, respectively.

[Per-project/route evidence and the tested bridge](wrapper-20261110/assessment.md#record-to-warning-bridge)
retain both directions; opposite project differences are not cancelled.
This closes the arithmetic residual, not the deferred versioning work.

## NOTES

- **Assessment:** source
  [`ade5040b6`](https://github.com/Azure/typespec-azure/commit/ade5040b62c25c8cd4eb8a0e99593f5f739c23f2),
  [PR #5481](https://github.com/Azure/typespec-azure/pull/5481);
  [frozen population and policy](refresh-20261110-wrapper/task.json).
  TypeSpec uses the source program and authored suppressions; Swagger uses the
  unchanged evaluated staging supplement. No Swagger was regenerated.
- **Validation:** 98 rule tests and owning build/lint/format checks passed,
  alongside 31 injected controls, 37 applicable portable controls and
  16 extraction controls. Fresh evaluation removed **9 false warnings**,
  **117 -> 108**, with **0 additions**; [details](wrapper-20261110/assessment.md).
- **Counting:** all 51 capture diagnostic arrays equal their full-run arrays
  in order. The [reconciliation](wrapper-20261110/reconciliation.json) preserves
  distinct occurrences and verifies 81 unchanged accepted schema contexts.
  Retained-record directional excesses are **94 Swagger-higher / 20
  TypeSpec-higher**, absolute 114, net 74. Route inspections and source
  locations are not violation normalization.
- **Execution limitation:** all 487 projects succeeded, but the CLI exited
  during finalization. Every original post-run integrity/report gate was
  independently verified, with **no native reruns** and original receipts
  preserved. This was **not a clean CLI pass**; see
  [recovery and replay](replay.md).
- **Supporting scope:** [existing-library verification](gap-investigation.md#existing-rule-coverage-verification)
  and [broader body investigations](gap-investigation.md#top-level-body-assessment)
  remain linked. Unobserved counterexamples are not added to this diagnostic-driven
  gap inventory or declared fixed. [Tooling identity](wrapper-20261110/tooling-identity.json)
  distinguishes the actual run revision from the content-equivalent replay revision.

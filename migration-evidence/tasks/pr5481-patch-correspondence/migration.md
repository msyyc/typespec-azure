# PatchPropertiesCorrespondToPutProperties migration

## 1. Conclusion and scope

The TypeSpec rule `@azure-tools/typespec-azure-resource-manager/arm-resource-patch`
partially migrates Swagger linter
[`PatchPropertiesCorrespondToPutProperties`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-properties-correspond-to-put-properties.md).
**Covered for the assessed name/body checks and direct format/bound constraints;
not full Swagger equivalence.** General type and nested collection-value
comparisons are deliberately outside the approved simpler policy.
The TypeSpec linter avoids Swagger's metadata-equality overchecking bug.
Historical API-version evaluation remains deferred to
[#5875](https://github.com/Azure/typespec-azure/issues/5875).

## 2. Actual coverage

**487 ARM projects assessed; 0 failures or unassessed projects.**
Diagnostics count individual findings, not projects.

| Count                                                        | Swagger linter | TypeSpec linter |
| ------------------------------------------------------------ | -------------: | --------------: |
| Raw reported diagnostics                                     |          1,314 |             104 |
| Retained PATCH routes inspected (project + exact HTTP route) |             97 |              97 |

**Assessed coverage:** exclude **1,132 confirmed Swagger overchecks**.
All **182 retained records** are assessed: **84 are check-covered**
(83 reporting records and one authored suppression), **92 need no extra
current-source warning**, and **6 are not migrated under the approved narrower
policy**. Those six represent **four deep-value targets**, not six proven
service bugs. They are an explicit complexity/coverage trade-off, not false
positives hidden from the scorecard.

The **104 TypeSpec warnings** include **73 witnessed by retained records**,
**18 additional valid source checks**, and **13 historical/versioning warnings**.
The **182 - 104 = 78** difference is fully accounted for by accepted inputs,
the six omitted records, suppression and reporting multiplicity; see
[Why diagnostic counts differ](#4-why-diagnostic-counts-differ).
Route counts measure inspections, not matched defects. Complete
API-version-aware violation totals and coverage percentages remain **unassessed**.

## 3. Function-level coverage

| Behavior                                                      | Result                           | Rationale                                                                                                                                                                                             |
| ------------------------------------------------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Extra PATCH names, nested/inherited leaves and encoded names  | Covered                          | Checks effective writable inputs and inherited operation pairs; [scope](direct-20261112/assessment.md#policy-and-complexity).                                                                         |
| Format, string length, item count and numeric bounds          | Covered                          | Preserves direct PUT constraints; accepts tighter PATCH bounds and nullable/reset values; [19 observed findings](direct-20261112/assessment.md#actual-diagnostic-effect).                             |
| General types, enum values, encodings and collection contents | Not migrated                     | Deliberately omitted to avoid a recursive subset solver; four observed deep targets affect six retained records; [approved decision](direct-20261112/assessment.md#deliberately-omitted-deep-checks). |
| Missing/empty PATCH or writable PATCH with no PUT input       | Covered                          | Keeps absent/empty-input checks and authored suppression; [body evidence](gap-investigation.md#missing-body-correspondence).                                                                          |
| Partial inputs and same-position opaque containers            | Covered                          | Retains visibility and encoded-path matching; no general nested-value compatibility claim; [scope and controls](direct-20261112/assessment.md#validation-and-provenance).                             |
| Indexed request bodies encountered in evaluated services      | Covered by existing library rule | `@azure-tools/typespec-azure-resource-manager/use-model-request-body` owns these cases; [separate probes](gap-investigation.md#existing-rule-coverage-verification), not included in 104.             |
| Historical names/types and operation availability             | Deferred                         | Requires shared [#5875 support](https://github.com/Azure/typespec-azure/issues/5875), not rule-local history reconstruction.                                                                          |

## 4. Why diagnostic counts differ

Swagger compares whole leaf schemas with
[`_.isEqual`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/patch-properties-correspond-to-put-properties.ts#L15-L70).
Harmless documentation, defaults and request/read-only metadata differences
cause **1,132 false missing-property reports**. **Do not port that bug.**

The first five rows partition all 1,314 Swagger records. The TypeSpec column
counts distinct configured warnings attributed to the same source check,
not unrelated warnings on the same operation or proven historical counterparts.
The last three rows partition the 31 outside-join warnings; **unassessed**
means no exact Swagger counterpart is established, not zero findings.

| Difference (with evidence)                                                                                  | Swagger diagnostics | TypeSpec diagnostics for the same check | Recommended action and rationale                                                                                  |
| ----------------------------------------------------------------------------------------------------------- | ------------------: | --------------------------------------: | ----------------------------------------------------------------------------------------------------------------- |
| [Metadata/request-filtering overchecks](gap-investigation.md#assessed-diagnostic-records)                   |               1,132 |                                       0 | **Do not port:** confirmed Swagger bug, not missing writable inputs.                                              |
| [Compatible inputs and non-input leaves/wrappers](direct-20261112/assessment.md#record-to-warning-bridge)   |                  92 |                                       0 | **Covered acceptance:** keep legitimate partial-input and visibility behavior.                                    |
| [Deep collection/value checks](direct-20261112/assessment.md#deliberately-omitted-deep-checks)              |                   6 |                                       0 | **Not migrated, approved trade-off:** four targets need the omitted solver; no new fix planned under this policy. |
| [Authored suppression](gap-investigation.md#missing-body-correspondence)                                    |                   1 |                                       0 | **Covered:** Quota's absent-body check is intentionally suppressed.                                               |
| [Reporting multiplicity](direct-20261112/assessment.md#record-to-warning-bridge)                            |                  83 |                                      73 | **Covered:** 85 associations include 12 repeats and two additional within-record checks.                          |
| [Historical names/availability](count-gap-20261106/analysis.md#historical-versioning)                       |          unassessed |                                      13 | **Defer to #5875:** do not reconstruct API history inside this rule.                                              |
| [Writable PATCH inputs absent from PUT input](count-gap-20261106/analysis.md#valid-source-checks-to-retain) |          unassessed |                                      17 | **Retain:** model/API owners should correct unintended writable declarations or confirm the contract.             |
| [Empty PATCH body](gap-investigation.md#netapp-49-swagger--2-typespec)                                      |                   0 |                                       1 | **Retain:** Swagger counts an existing body parameter and misses the empty input; request an owner correction.    |

**182 - 104 = 92 + 6 + 1 + 12 - 2 - 31 = 78.**

The [exact per-project bridge](direct-20261112/reconciliation.json) retains
both difference directions. This explains the arithmetic without claiming
complete compatibility or retiring the deferred versioning work.

## NOTES

- **Source:** [`f2079b236`](https://github.com/Azure/typespec-azure/commit/f2079b23690d816ecc92a858fab2c1572e9448b5),
  [PR #5481](https://github.com/Azure/typespec-azure/pull/5481);
  [frozen population and policy](refresh-20261112-direct/task.json).
  Source-program checks preserve authored suppressions; Swagger reuses the
  unchanged staging supplement. No Swagger was regenerated.
- **Effect:** helper reduced **374 -> 132 lines**; all **19 direct-constraint
  findings** retained, **4 deep findings** intentionally omitted, and other
  warning families unchanged. The [assessment](direct-20261112/assessment.md)
  separates the wording-only diagnostic delta from behavior.
- **Validation:** 91 canonical rule tests, build/lint/format, 17 injected,
  37 applicable portable and 12 extraction controls passed. Both actual
  published ARM examples were compiled unchanged. All six CI Build jobs passed;
  the real merge conflict is resolved.
- **Execution:** this final run completed cleanly across all 487 projects.
  All 51 attribution arrays exactly match full-run arrays, including order.
  [Verification and replay](replay.md) distinguish current evidence from the
  historical run's finalization recovery and retain the original investigation.

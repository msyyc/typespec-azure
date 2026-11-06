# PatchPropertiesCorrespondToPutProperties migration

## 1. Conclusion and scope

The TypeSpec rule `@azure-tools/typespec-azure-resource-manager/arm-resource-patch`
migrates Swagger linter rule
[`PatchPropertiesCorrespondToPutProperties`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-properties-correspond-to-put-properties.md).
**Covered for the assessed supported current-source PUT/PATCH inputs; full
Swagger equivalence is not established.** The TypeSpec linter checks writable
property names, compatible types/constraints and missing/empty bodies. It
intentionally avoids the Swagger linter's metadata-equality overchecking bug.
Historical-version handling is
[deferred to #5875](https://github.com/Azure/typespec-azure/issues/5875);
unsupported/ambiguous top-level bodies remain unassessed.

## 2. Actual coverage

**487 ARM projects assessed; 0 project failures or unassessed projects.**
Reported diagnostics below are individual findings across that population,
not project counts.

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics |      **1,314** |         **117** |

**Assessed coverage: 0 confirmed missing non-versioning checks** remain in the
investigated supported current-source cases. **1,132 Swagger reports are
overchecks and are excluded.** All **182 remaining records** were assessed:
90 have diagnostic-check coverage (including 1 suppressed finding), 82 describe
accepted current-source shapes, 8 concern non-input leaves or wrappers, and
2 contain mixed same-named inputs whose incompatible leaves are diagnosed.

**Decision:** no additional rule change is justified by these cases. Keep the
covered checks, do not reproduce the Swagger overchecking bug, and leave
historical-version handling to #5875.

Those categories count Swagger records by source behavior, not unique matched
violations. Exact comparable violation totals and coverage percentages remain
**unassessed** without API-version-aware source-to-emission matching; the
zero confirmed gap does not include that limitation or unsupported body shapes.
See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ).

## 3. Function-level coverage

| Behavior                                                                    | Result           | Rationale                                                                                                                                                              |
| --------------------------------------------------------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Extra PATCH properties, including nested/inherited leaves and encoded names | Covered          | Checks effective request-input names; [evidence and controls](gap-investigation.md#assessment-method).                                                                 |
| Incompatible value types and supported constraints                          | Covered          | Checks serialized values, collections and length/numeric bounds; [supported predicates](gap-investigation.md#compatibility-fix), not a universal schema-subset solver. |
| ARM operations inherited into project interfaces                            | Covered          | Inherited operations are evaluated alongside authored operations; [evidence](gap-investigation.md#inherited-operation-fix).                                            |
| Missing/empty PATCH, or writable PATCH with no PUT input                    | Covered          | Checks absent and empty input; [body evidence](gap-investigation.md#missing-body-correspondence) also credits authored suppression.                                    |
| Valid partial inputs and compatible request metadata                        | Covered          | Accepts valid updates instead of requiring identical schemas; [compatible cases](gap-investigation.md#why-81-schema-contexts-correctly-accept).                        |
| Historical names/types, availability and operation selection                | Missing/deferred | Shared [#5875 work](gap-investigation.md#versioning-boundary), outside the assessed current-source policy.                                                             |
| Unsupported/ambiguous top-level bodies                                      | Unassessed       | No equivalence conclusion for these shapes; [limits](gap-investigation.md#remaining-comparison-limits-and-reproducibility).                                            |

## 4. Why diagnostic counts differ

The [Swagger implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/patch-properties-correspond-to-put-properties.ts#L15-L70)
compares whole schemas, so documentation, defaults and request metadata can
produce false missing-property reports. The TypeSpec linter checks input
compatibility instead.

The rows account for all 1,314 Swagger records. The TypeSpec column counts
established same-check findings only: **unassessed matching does not mean a
missing check**. One source warning can cover several emitted records.

| Difference (with evidence)                                                        | Swagger diagnostics | TypeSpec diagnostics for the same check | Recommended action and rationale                                                         |
| --------------------------------------------------------------------------------- | ------------------: | --------------------------------------- | ---------------------------------------------------------------------------------------- |
| [Metadata/read-only overchecks](gap-investigation.md#assessed-diagnostic-records) |               1,132 | 0 metadata-equality warnings            | **Excluded.** Do not port false positives.                                               |
| [Same-name schema differences](gap-investigation.md#schema-contexts)              |                 131 | Unassessed one-to-one matching          | **Covered in assessed scope.** Diagnose incompatible inputs; accept compatible ones.     |
| [Absent emitted names](gap-investigation.md#name-contexts)                        |                  49 | Unassessed one-to-one matching          | **Covered in assessed scope.** Keep precise leaf checks, not duplicate wrapper warnings. |
| [Absent bodies](gap-investigation.md#missing-body-correspondence)                 |                   2 | 1 reported; 1 suppressed                | **Covered.** Credit suppression without inflating the raw total of 117.                  |

[Source-only differences](gap-investigation.md#typespec-higher-projects) also
include request-input checks that Swagger misses, and
[NetApp](gap-investigation.md#netapp-49-swagger--2-typespec) demonstrates its
empty-body false negative. Keep those covered checks; NetApp's historical-name
case remains deferred. **Neither `1,314 - 117` nor `182 - 117` measures ignored
violations.**

## NOTES

- **Assessed revision and policy:** candidate
  [`012190397`](https://github.com/Azure/typespec-azure/commit/0121903975ab45cde7d7aca37cf50ffd7f3855d3)
  in [PR #5481](https://github.com/Azure/typespec-azure/pull/5481).
  [Frozen inputs and execution policy](refresh-20261105-inherited/task.json)
  identify the ARM source-program assessment and separate staging-only Swagger
  evaluation. Source-program checks are not historical-version projection.
- **Assessment details:** [record classifications](inherited-20261105/assessed-contexts.json),
  [per-route evidence](inherited-20261105/retained-route-contexts.md) and
  [complete project/target counts](refresh-20261105-inherited/staging-comparison/differences.md).
  These retain all findings in both directions; the 182-record investigation
  is not a one-to-one account of all 117 TypeSpec warnings.
- **Validation and execution:** [validation results](inherited-20261105/validation.json)
  and [local readiness review](inherited-20261105/readiness.json) retain the
  checks and their limits, without claiming a new formal GitHub A/B review.
  All 487 projects completed after the
  [documented interruption and recovery](refresh-20261105-inherited/provenance/integrity-reconciliation.json);
  this was **not a clean CLI pass**.
- **Replay and seal:** use the [sealed evidence snapshot](https://github.com/msyyc/typespec-azure/tree/f4afb7fe5398fa0778a54e13eec34326e818791a/migration-evidence/tasks/pr5481-patch-correspondence)
  and its [replay instructions](https://github.com/msyyc/typespec-azure/blob/f4afb7fe5398fa0778a54e13eec34326e818791a/migration-evidence/tasks/pr5481-patch-correspondence/replay.md).
  This report-only rewrite reuses that assessment. The original publication
  seal applies to that snapshot, not to this revised prose.

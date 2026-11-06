# PatchPropertiesCorrespondToPutProperties migration

## 1. Conclusion and scope

The TypeSpec rule `@azure-tools/typespec-azure-resource-manager/arm-resource-patch`
migrates Swagger linter rule
[`PatchPropertiesCorrespondToPutProperties`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-properties-correspond-to-put-properties.md).
**Migration is not functionally complete:** valid object bodies expressed through
model-property references bypass PATCH comparison. A separate body-shape policy
also misses inherited dictionary indexers. Both are non-versioning gaps.
Ordinary object-body checks are covered, and the TypeSpec linter intentionally
avoids the Swagger linter's metadata-equality overchecking bug.
Historical-version handling remains
[deferred to #5875](https://github.com/Azure/typespec-azure/issues/5875).

## 2. Actual coverage

**487 ARM projects assessed; 0 project failures or unassessed projects.**
Reported diagnostics are individual findings across that population, not
project counts.

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics |      **1,314** |         **117** |

**Assessed coverage:** **1,132 Swagger overchecks are excluded**. All **182
remaining records** have assessed current-source contexts: 90 have diagnostic-check
coverage (including 1 suppressed finding), 82 are accepted, 8 concern non-input
leaves or wrappers, and 2 have mixed same-named inputs with incompatible leaves
diagnosed. These are record classifications, **not 182 matched violations**.

The previously unassessed body shapes are now investigated across **1,131
PUT/PATCH pairs**. Only **2 pairs** are skipped for indexed roots; both receive
the existing body-shape warning when that rule is enabled. **Neither newly
identified gap occurs in those pairs**, but focused controls prove both are
authorable and missing. Recommend fixing the two owning checks; zero observed
corpus occurrences does not make them covered.

Exact comparable violation totals and coverage percentages remain **unassessed**:
complete API-version-aware source-to-emission matching is still unavailable.
That limitation is separate from the now-assessed body behavior.
See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ).

## 3. Function-level coverage

| Behavior                                                                       | Result                                  | Rationale                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------ | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ordinary object inputs: extra names, nested/inherited leaves and encoded names | Covered                                 | Checks effective writable leaves; [evidence](gap-investigation.md#assessment-method).                                                                                                                       |
| Compatible partial objects and supported type/constraint checks                | Covered                                 | Accepts valid updates and diagnoses incompatible values; [scope and controls](gap-investigation.md#compatibility-fix), not a universal schema-subset solver.                                                |
| Inherited ARM operations and missing/empty bodies                              | Covered                                 | Includes inherited operations and absent/empty input; [operation evidence](gap-investigation.md#inherited-operation-fix) and [body/suppression evidence](gap-investigation.md#missing-body-correspondence). |
| Object bodies referenced through model properties                              | Missing                                 | A valid `Types.payload` body is skipped instead of compared; [two violating directions and compatible control](gap-investigation.md#model-property-reference-gap).                                          |
| Inherited dictionary root policy                                               | Missing                                 | The body-shape owner checks direct indexers but not base models; [counterexamples and recommended fix](gap-investigation.md#inherited-dictionary-body-policy-gap).                                          |
| Other non-object roots and ARM multipart bodies                                | Covered by existing owners when enabled | Separate body-shape/content-type rules diagnose these inputs; [controls and real-service checks](gap-investigation.md#top-level-body-assessment). Their warnings are not included in 117.                   |
| Historical names/types, availability and operation selection                   | Missing/deferred                        | Shared [#5875 work](gap-investigation.md#versioning-boundary), outside the assessed current-source policy.                                                                                                  |

## 4. Why diagnostic counts differ

The [Swagger implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/patch-properties-correspond-to-put-properties.ts#L15-L70)
compares whole schemas. Documentation, defaults and harmless request metadata
therefore produce false missing-property reports. This **overchecking bug
accounts for 1,132 reports**, the largest explained part of the difference.

The first four rows partition all 1,314 corpus records. The last two are
**separate synthetic controls**, using the pinned Swagger predicate on actual
fixture emission, not additional corpus reports. The TypeSpec column identifies
same-check findings where established; the explicitly named body-policy row is
other-rule evidence, not part of 117. Unsupported one-to-one attribution is
not treated as zero.

| Difference (with evidence)                                                               |               Swagger diagnostics | TypeSpec diagnostics for the same check | Recommended action and rationale                                                                                                                  |
| ---------------------------------------------------------------------------------------- | --------------------------------: | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Metadata/read-only overchecks](gap-investigation.md#assessed-diagnostic-records)        |                             1,132 | 0 metadata-equality warnings            | **Excluded.** Do not port false positives.                                                                                                        |
| [Same-name schema differences](gap-investigation.md#schema-contexts)                     |                               131 | Unassessed one-to-one matching          | **Covered in assessed ordinary-object scope.** Diagnose incompatible inputs, not unequal metadata.                                                |
| [Absent emitted names](gap-investigation.md#name-contexts)                               |                                49 | Unassessed one-to-one matching          | **Covered in assessed ordinary-object scope.** Keep precise leaf checks, not duplicate wrapper warnings.                                          |
| [Absent bodies](gap-investigation.md#missing-body-correspondence)                        |                                 2 | 1 reported; 1 suppressed                | **Covered.** Credit suppression without inflating 117.                                                                                            |
| [Valid object references](gap-investigation.md#model-property-reference-gap)             |                      2 (controls) | 0 (controls)                            | **Missing; fix recommended.** Normalize references before both object classification and leaf extraction.                                         |
| [Inherited dictionary policy](gap-investigation.md#inherited-dictionary-body-policy-gap) | 1 (control; dictionary overcheck) | 0 body-policy warnings (2 controls)     | **Separate missing check; fix recommended.** Inspect inherited indexers in the existing body-shape rule; do not require declared dictionary keys. |

[TypeSpec-only findings](gap-investigation.md#typespec-higher-projects) also
include covered request-input checks that Swagger misses, including
[empty-body detection](gap-investigation.md#netapp-49-swagger--2-typespec).
Neither subtraction, `1,314 - 117` or `182 - 117`, measures ignored violations.

## NOTES

- **Assessment identity:** source
  [`012190397`](https://github.com/Azure/typespec-azure/commit/0121903975ab45cde7d7aca37cf50ffd7f3855d3),
  [PR #5481](https://github.com/Azure/typespec-azure/pull/5481);
  [frozen population and policy](refresh-20261105-inherited/task.json).
  The TypeSpec run is source-program based; the reused Swagger observations use
  the recorded staging profile. This update changes evidence, not production code.
- **Body assessment:** [complete inventory](body-assessment-20261106/inventory.json),
  [21 characterization controls](body-assessment-20261106/fixtures.json) and
  [two real-service owner checks](body-assessment-20261106/owner-probes.json).
  Of 487 projects, 368 have paired routes and 119 have none.
  Four violating controls expose the two missing behavior families; their
  successful characterization checks do not mean the production gaps are fixed.
  The 117-warning corpus enables only `arm-resource-patch`; other-rule controls
  explicitly enable their owners, without claiming default activation.
- **Validation and detail:** [body assessment results and corrections](body-assessment-20261106/validation.json),
  including 104 existing owning-package tests; [record classifications](inherited-20261105/assessed-contexts.json),
  [route evidence](inherited-20261105/retained-route-contexts.md) and
  [all project/target differences](refresh-20261105-inherited/staging-comparison/differences.md).
  The 182-record join witnesses only a subset of the 117 warnings.
- **Recovery:** the [original sealed snapshot](https://github.com/msyyc/typespec-azure/tree/f4afb7fe5398fa0778a54e13eec34326e818791a/migration-evidence/tasks/pr5481-patch-correspondence)
  and its [replay instructions](https://github.com/msyyc/typespec-azure/blob/f4afb7fe5398fa0778a54e13eec34326e818791a/migration-evidence/tasks/pr5481-patch-correspondence/replay.md)
  preserve the original assessment, including its
  [CLI interruption/recovery](refresh-20261105-inherited/provenance/integrity-reconciliation.json).
  That was not a clean CLI pass. The new source-only body inventory completed
  independently within its original budget and preserved every original
  configured diagnostic multiset. The old whole-tree seal does not cover this
  supplement; use its [offline checks and reproduction instructions](gap-investigation.md#corpus-scope-and-reproducibility).

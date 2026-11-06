# PatchPropertiesCorrespondToPutProperties migration

## 1. Conclusion and scope

The TypeSpec rule `@azure-tools/typespec-azure-resource-manager/arm-resource-patch`
migrates Swagger linter rule
[`PatchPropertiesCorrespondToPutProperties`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-properties-correspond-to-put-properties.md).
**The investigated reported cases have no confirmed missing non-versioning
check under the assessed current-source policy.** The TypeSpec linter covers
the required input checks without reproducing the Swagger linter's
metadata-equality overchecking bug.
This report concerns observed diagnostics, not exhaustive equivalence for
unobserved inputs. Historical-version handling remains
[deferred to #5875](https://github.com/Azure/typespec-azure/issues/5875).

## 2. Actual coverage

**487 ARM projects assessed; 0 project failures or unassessed projects.**
The assessed outcome is **0 confirmed uncovered current-source checks in the
investigated reported cases**. Counts below are individual diagnostic records,
not projects or matched defects.

| Count                                                                    | Swagger linter | TypeSpec linter |
| ------------------------------------------------------------------------ | -------------: | --------------: |
| Raw reported diagnostics                                                 |          1,314 |             117 |
| Retained diagnostic records after confirmed Swagger overcheck exclusions |        **182** |         **117** |

**Assessed coverage:** **1,132 Swagger reports are excluded** because whole-schema
equality falsely treats documentation, defaults, compatible request metadata or
read-only leaves as missing PATCH input. The **182 retained Swagger records**
have these assessed current-source outcomes:

| Assessed retained-record outcome                                                       | Records | Decision                                 |
| -------------------------------------------------------------------------------------- | ------: | ---------------------------------------- |
| Existing checks diagnose the relevant inputs, or an applicable suppression is authored |  **92** | Covered                                  |
| Compatible inputs or non-input leaves/wrappers                                         |  **90** | No additional warning by design          |
| A demonstrated additional non-versioning check is needed                               |   **0** | No confirmed gap in these reported cases |

The 92 include 90 check-covered records and 2 mixed-name records with
incompatible leaves diagnosed. The 90 accepted records are 82 compatible inputs
plus 8 non-input leaves/wrappers.

The TypeSpec total is unchanged: only confirmed Swagger overchecks are filtered
in the second row. Different emission/source multiplicities mean **182 versus
117 is not a remaining 65-violation gap**. These are assessed record dispositions,
not a normalization into equivalent defects.
Exact comparable violation totals and coverage percentages remain **unassessed**
without complete API-version-aware source-to-emission matching.
See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) and the
[scorecard accounting](gap-investigation.md#reader-scorecard-accounting).

## 3. Function-level coverage

| Behavior                                                               | Result                           | Rationale                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Extra PATCH names, including nested/inherited leaves and encoded names | Covered                          | Checks effective writable inputs in the reported cases; [source-check evidence](gap-investigation.md#assessment-method).                                                                                                                                     |
| Incompatible value types and supported constraints                     | Covered                          | Diagnoses incompatible wire values, collections and bounds; [evidence](gap-investigation.md#compatibility-fix), not a universal schema-subset solver.                                                                                                        |
| ARM operations inherited into project interfaces                       | Covered                          | Includes the inherited project operation pairs; [evidence](gap-investigation.md#inherited-operation-fix).                                                                                                                                                    |
| Missing/empty PATCH or writable PATCH with no PUT input                | Covered                          | Checks absent and empty input; [body evidence](gap-investigation.md#missing-body-correspondence) credits authored suppression.                                                                                                                               |
| Compatible partial inputs and non-input leaves/wrappers                | Covered                          | Does not warn merely because emitted schemas differ; [accepted inputs](gap-investigation.md#why-81-schema-contexts-correctly-accept) and [wrapper cases](gap-investigation.md#name-contexts).                                                                |
| Indexed request bodies encountered in evaluated services               | Covered by existing library rule | `@azure-tools/typespec-azure-resource-manager/use-model-request-body` reports both observed cases when enabled; [recorded real-service probes](gap-investigation.md#corpus-scope-and-reproducibility). Those separate-profile warnings are not added to 117. |
| Historical names/types, availability and operation selection           | Deferred                         | The reported historical differences belong to shared [#5875 work](gap-investigation.md#versioning-boundary), outside the assessed current-source policy.                                                                                                     |

## 4. Why diagnostic counts differ

The rows partition all **1,314 Swagger records**. The first is a confirmed
Swagger bug; the remaining rows are assessed against current-source checks,
not presumed valid historical defects. The TypeSpec column counts established
same-check findings only; unsupported one-to-one matching is not treated as zero.

| Difference (with evidence)                                                        | Swagger diagnostics | TypeSpec diagnostics for the same check | Recommended action and rationale                                                                            |
| --------------------------------------------------------------------------------- | ------------------: | --------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| [Metadata/read-only overchecks](gap-investigation.md#assessed-diagnostic-records) |               1,132 | 0 metadata-equality warnings            | **Excluded false positives.** Do not port the Swagger bug.                                                  |
| [Same-name schema differences](gap-investigation.md#schema-contexts)              |                 131 | Unassessed one-to-one matching          | **Covered in assessed scope.** Diagnose incompatible inputs; accept compatible partial values and metadata. |
| [Absent emitted names](gap-investigation.md#name-contexts)                        |                  49 | Unassessed one-to-one matching          | **Covered in assessed scope.** Keep precise input-leaf checks rather than duplicate wrapper warnings.       |
| [Absent bodies](gap-investigation.md#missing-body-correspondence)                 |                   2 | 1 reported; 1 suppressed                | **Covered.** Credit the implemented suppressed check without inflating 117.                                 |

The Swagger linter compares whole leaf schemas with
[`_.isEqual`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/patch-properties-correspond-to-put-properties.ts#L15-L70);
its 1,132 overchecks explain the largest part of the raw difference.
[TypeSpec-only reports](gap-investigation.md#typespec-higher-projects) also
include covered checks Swagger misses, such as
[empty-body detection](gap-investigation.md#netapp-49-swagger--2-typespec).
Retain those checks; historical discrepancies stay with #5875.

## NOTES

- **Assessment identity:** source
  [`012190397`](https://github.com/Azure/typespec-azure/commit/0121903975ab45cde7d7aca37cf50ffd7f3855d3),
  [PR #5481](https://github.com/Azure/typespec-azure/pull/5481);
  [frozen population and policy](refresh-20261105-inherited/task.json).
  TypeSpec is assessed as a source program; Swagger uses the recorded staging
  profile. This is a report-only refresh with no new compilation or rule change.
- **Counting boundary:** [record classifications](inherited-20261105/assessed-contexts.json)
  and [route evidence](inherited-20261105/retained-route-contexts.md) preserve
  every contributing record. The retained-record join witnesses 79 distinct
  configured warnings; the other 38 of 117 remain in the
  [complete project/target inventory](refresh-20261105-inherited/staging-comparison/differences.md).
  One source check can cover multiple emitted records; these counts do not
  establish a diagnostic matching percentage.
- **Existing-library coverage:** [implementation, tests and observed warnings](gap-investigation.md#existing-rule-coverage-verification)
  support the named existing rule. The main 117-warning profile enables only
  `arm-resource-patch`; supplementary probes explicitly enable other rules,
  without claiming default activation.
- **Scope and supporting work:** this main report follows the requested
  diagnostic-driven scope. [Broader behavioral investigations](gap-investigation.md#top-level-body-assessment)
  remain supporting evidence, not additional observed migration-gap counts
  or a claim that unobserved inputs are fully covered.
- **Validation and recovery:** [recorded validation](body-assessment-20261106/validation.json),
  the [original sealed snapshot](https://github.com/msyyc/typespec-azure/tree/f4afb7fe5398fa0778a54e13eec34326e818791a/migration-evidence/tasks/pr5481-patch-correspondence)
  and its [replay instructions](https://github.com/msyyc/typespec-azure/blob/f4afb7fe5398fa0778a54e13eec34326e818791a/migration-evidence/tasks/pr5481-patch-correspondence/replay.md)
  retain execution details. The original CLI required
  [documented interruption/recovery](refresh-20261105-inherited/provenance/integrity-reconciliation.json);
  it was not a clean CLI pass. Its seal covers the immutable snapshot, not
  revised prose. Supplementary saved-data checks are linked from the appendix.

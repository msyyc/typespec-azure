# PatchPropertiesCorrespondToPutProperties migration

## 1. Conclusion and scope

The TypeSpec rule `@azure-tools/typespec-azure-resource-manager/arm-resource-patch`
migrates Swagger linter rule
[`PatchPropertiesCorrespondToPutProperties`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-properties-correspond-to-put-properties.md).
**The assessed migration is not complete: a non-versioning empty-wrapper
overcheck still needs a TypeSpec-rule fix.** The required input checks exist,
and the TypeSpec linter intentionally avoids the Swagger linter's
metadata-equality overchecking bug. This report concerns observed diagnostics,
not exhaustive equivalence for unobserved inputs. Historical-version handling remains
[deferred to #5875](https://github.com/Azure/typespec-azure/issues/5875).

## 2. Actual coverage

**487 ARM projects assessed; 0 project failures or unassessed projects.**
Counts below are individual diagnostic records, not projects or matched defects.

| Count                                                                    | Swagger linter | TypeSpec linter |
| ------------------------------------------------------------------------ | -------------: | --------------: |
| Raw reported diagnostics                                                 |          1,314 |             117 |
| Retained diagnostic records after confirmed Swagger overcheck exclusions |        **182** |         **117** |

**Assessed coverage:** **1,132 Swagger false positives are excluded**, chiefly
metadata-equality overchecking. Of the **182 retained records**, **90** concern
compatible inputs or non-input leaves/wrappers, and **92** have implemented
checks, including one suppressed finding. These records demonstrate no
additional missing current-source check.

The **65-count difference is fully reconciled below**, not left unexplained.
It combines accepted behavior, suppression and reporting multiplicity, offset
by **38 TypeSpec warnings outside the retained-record join**. Those 38 include
**7 TypeSpec overchecks to fix**, **13 versioning cases to defer**, and
**18 valid current-source checks to retain**. Retaining those checks does not
approve the underlying service models.

Only the Swagger column is filtered in the second scorecard row; both columns
retain their own reporting units. Exact comparable violation totals and
coverage percentages remain **unassessed** without complete API-version-aware
source-to-emission matching. See
[Why diagnostic counts differ](#4-why-diagnostic-counts-differ).

## 3. Function-level coverage

| Behavior                                                               | Result                           | Rationale                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Extra PATCH names, including nested/inherited leaves and encoded names | Covered                          | Checks effective writable inputs in the reported cases; [source-check evidence](gap-investigation.md#assessment-method).                                                                                                                                     |
| Incompatible value types and supported constraints                     | Covered                          | Diagnoses incompatible wire values, collections and bounds; [evidence](gap-investigation.md#compatibility-fix), not a universal schema-subset solver.                                                                                                        |
| ARM operations inherited into project interfaces                       | Covered                          | Includes the inherited project operation pairs; [evidence](gap-investigation.md#inherited-operation-fix).                                                                                                                                                    |
| Missing/empty PATCH or writable PATCH with no PUT input                | Covered                          | Checks absent and empty input; [body evidence](gap-investigation.md#missing-body-correspondence) credits authored suppression.                                                                                                                               |
| Compatible partial inputs and non-input leaves/wrappers                | Covered                          | Does not warn merely because emitted schemas differ; [accepted inputs](gap-investigation.md#why-81-schema-contexts-correctly-accept) and [wrapper cases](gap-investigation.md#name-contexts).                                                                |
| Same object container with no Update-visible children                  | Needs fix                        | PATCH retains an opaque wrapper while PUT is flattened into children, causing false missing-property warnings; [7 observed targets and reproduced mechanism](count-gap-20261106/analysis.md#empty-wrapper-overcheck-to-fix).                                 |
| Indexed request bodies encountered in evaluated services               | Covered by existing library rule | `@azure-tools/typespec-azure-resource-manager/use-model-request-body` reports both observed cases when enabled; [recorded real-service probes](gap-investigation.md#corpus-scope-and-reproducibility). Those separate-profile warnings are not added to 117. |
| Historical names/types, availability and operation selection           | Deferred                         | The reported historical differences belong to shared [#5875 work](gap-investigation.md#versioning-boundary), outside the assessed current-source policy.                                                                                                     |

## 4. Why diagnostic counts differ

The largest raw difference is the
[**1,132 confirmed Swagger overchecks**](gap-investigation.md#assessed-diagnostic-records).
The Swagger linter compares whole leaf schemas with
[`_.isEqual`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/patch-properties-correspond-to-put-properties.ts#L15-L70);
documentation, defaults and harmless request/read-only metadata differences
therefore become false missing-property reports. **Do not port that bug.**

After those exclusions, the exact bridge is:

**182 - 117 = 90 + 1 + 14 - 2 - 38 = 65.**

| Contribution to the difference                                                                               |  Count | Assessment and action                                                                                         |
| ------------------------------------------------------------------------------------------------------------ | -----: | ------------------------------------------------------------------------------------------------------------- |
| [Compatible inputs and non-input names](gap-investigation.md#reader-scorecard-accounting)                    |    +90 | **Accept:** 82 compatible contexts and 8 non-input/flattened names need no additional current-source warning. |
| [Authored suppression](gap-investigation.md#missing-body-correspondence)                                     |     +1 | **Accept:** Quota's check is implemented and credited, but its warning is suppressed.                         |
| [Several records reuse a source warning](count-gap-20261106/analysis.md#record-to-warning-bridge)            |    +14 | **Accept the counting difference:** repeated route/declaration associations, not missing checks.              |
| [One record witnesses multiple checks](count-gap-20261106/analysis.md#record-to-warning-bridge)              |     -2 | **Preserve both checks:** two records each witness two distinct prefix-limit warnings.                        |
| [Warnings outside the retained-record join](count-gap-20261106/analysis.md#all-38-warnings-outside-the-join) |    -38 | **Assess separately:** 13 deferred + 7 overchecks to fix + 18 valid checks to retain.                         |
| **Net difference**                                                                                           | **65** | **No unexplained arithmetic residual; not 65 missed violations.**                                             |

The **38** require these different decisions:

| Observed TypeSpec warning group                                                                             | Warnings | Recommended action and rationale                                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------- | -------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Historical names/availability](count-gap-20261106/analysis.md#historical-versioning)                       |       13 | **Defer to #5875**, as requested. Do not reconstruct version history inside this rule.                                                                                                                    |
| [Empty-wrapper overchecking](count-gap-20261106/analysis.md#empty-wrapper-overcheck-to-fix)                 |        7 | **Fix `arm-resource-patch-body.ts`:** preserve the corresponding PUT object-container candidate instead of comparing PATCH's wrapper only with PUT's flattened child names. Recommended, not implemented. |
| [Writable PATCH inputs absent from PUT input](count-gap-20261106/analysis.md#valid-source-checks-to-retain) |       17 | **Retain the check.** Spec owners should correct unintended writable declarations or confirm/document the intended contract; do not disable visibility checks to equalize counts.                         |
| [Empty PATCH body](gap-investigation.md#netapp-49-swagger--2-typespec)                                      |        1 | **Retain the check.** NetApp's empty `SnapshotPatch` needs a model/API-owner correction; Swagger misses it by counting the existing body parameter.                                                       |

These are configured-warning classifications, not 38 proven historical
Swagger matches. [All individual targets, source evidence and decisions](count-gap-20261106/analysis.md)
remain linked; no warning is accepted merely because its count balances.

## NOTES

- **Assessment identity:** source
  [`012190397`](https://github.com/Azure/typespec-azure/commit/0121903975ab45cde7d7aca37cf50ffd7f3855d3),
  [PR #5481](https://github.com/Azure/typespec-azure/pull/5481);
  [frozen population and policy](refresh-20261105-inherited/task.json).
  TypeSpec is assessed as a source program; Swagger uses the recorded staging
  profile. This is a report-only refresh with four isolated fixture controls,
  no new real-service compilation and no production-rule change.
- **Counting boundary:** [record classifications](inherited-20261105/assessed-contexts.json)
  and [route evidence](inherited-20261105/retained-route-contexts.md) preserve
  every contributing record. The [tested reconciliation](count-gap-20261106/reconciliation.json)
  verifies all 51 capture arrays' index order against the 487-project run:
  91 reporting records produce 93 associations to 79 distinct warnings;
  one additional record is suppressed. Distinct warnings at one location are
  not collapsed. Retained-record project differences are **89 Swagger-higher
  versus 24 TypeSpec-higher**, absolute 113, net 65.
- **Investigation boundary:** [35 pinned source excerpts and 4 executed controls](count-gap-20261106/analysis.md#validation-and-limits)
  support the 38-warning classifications. Seven accounting tests and an offline
  replay reproduce the bridge. Per-version correspondence remains unsupported;
  complete equivalence is not claimed.
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

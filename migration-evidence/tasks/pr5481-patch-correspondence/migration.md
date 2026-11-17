# PatchPropertiesCorrespondToPutProperties migration

## 1. Conclusion and scope

`@azure-tools/typespec-azure-resource-manager/arm-resource-patch` partially
migrates Swagger linter
[`PatchPropertiesCorrespondToPutProperties`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-properties-correspond-to-put-properties.md).
**Name/body correspondence is covered; value and constraint compatibility are
deliberately not migrated.** The compatibility helper is removed without a
replacement comparator. This is the approved simplicity/coverage trade-off,
not full Swagger equivalence. Historical API-version evaluation remains
deferred to [#5875](https://github.com/Azure/typespec-azure/issues/5875).

## 2. Actual coverage

**487 ARM projects assessed; 0 failures or unassessed projects.**
The raw totals are **1,314 Swagger diagnostics / 85 TypeSpec warnings**.
After excluding **1,132 confirmed Swagger overchecks**, all **182 retained
Swagger records** have an assessed disposition:

| Retained-record disposition            | Records | Meaning                                                                                                |
| -------------------------------------- | ------: | ------------------------------------------------------------------------------------------------------ |
| Check-covered                          |      58 | 57 reporting records and one authored suppression.                                                     |
| No extra current-source warning needed |      92 | Legitimate accepted inputs or non-input leaves/wrappers, not missing native checks.                    |
| Deliberately not migrated              |      32 | 26 records lose constraint coverage in this update; six deep-value records were already outside scope. |

The 32 omitted records are **not** credited as compatible or false positives.
They remain explicit coverage loss. The **85 TypeSpec warnings** comprise
**54 witnessed by retained records**, **18 additional valid source checks** and
**13 historical/versioning findings**. Compared with the preceding candidate,
**19 constraint warnings were removed and no warnings added**.

The retained records cover **97 exact PATCH routes on each side**; inspections
are not counts of matched defects. Complete API-version-aware violation totals
and coverage percentages remain **unassessed**.

## 3. Function-level coverage

| Behavior                                                         | Result                           | Rationale                                                                                                                                                                                |
| ---------------------------------------------------------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Extra PATCH names, nested/inherited leaves and encoded names     | Covered                          | Checks effective writable inputs and inherited operation pairs; [scope](names-20261117/assessment.md#policy-and-complexity).                                                             |
| Missing/empty PATCH or writable PATCH with no PUT input          | Covered                          | Preserves body checks and authored suppression; [body evidence](gap-investigation.md#missing-body-correspondence).                                                                       |
| Partial inputs and same-position opaque containers               | Covered                          | Preserves visibility and encoded-path matching without comparing values; [controls](names-20261117/assessment.md#validation-and-provenance).                                             |
| Types, formats, bounds, enums, encodings and collection contents | Not migrated                     | Approved simplification: 19 warnings removed; 32 retained records now outside scope; [impact](names-20261117/assessment.md#deliberately-omitted-value-checks).                           |
| Indexed request bodies encountered in evaluated services         | Covered by existing library rule | `@azure-tools/typespec-azure-resource-manager/use-model-request-body` owns these cases; [separate probes](gap-investigation.md#existing-rule-coverage-verification), not included in 85. |
| Historical names/input shapes and operation availability         | Deferred                         | Requires shared [#5875 support](https://github.com/Azure/typespec-azure/issues/5875), not rule-local history reconstruction.                                                             |

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

| Difference (with evidence)                                                                                  | Swagger diagnostics | TypeSpec diagnostics for the same check | Decision                                                                                                         |
| ----------------------------------------------------------------------------------------------------------- | ------------------: | --------------------------------------: | ---------------------------------------------------------------------------------------------------------------- |
| [Metadata/request-filtering overchecks](gap-investigation.md#assessed-diagnostic-records)                   |               1,132 |                                       0 | **Do not port:** confirmed Swagger bug, not missing writable inputs.                                             |
| [Accepted inputs and non-input leaves/wrappers](names-20261117/assessment.md#record-to-warning-bridge)      |                  92 |                                       0 | **Covered acceptance:** keep legitimate partial-input and visibility behavior.                                   |
| [Value/constraint checks](names-20261117/assessment.md#deliberately-omitted-value-checks)                   |                  32 |                                       0 | **Not migrated:** approved complexity/coverage trade-off, not false positives; no fix planned under this policy. |
| [Authored suppression](gap-investigation.md#missing-body-correspondence)                                    |                   1 |                                       0 | **Covered:** Quota's absent-body check is intentionally suppressed.                                              |
| [Reporting multiplicity](names-20261117/assessment.md#record-to-warning-bridge)                             |                  57 |                                      54 | **Covered:** 57 associations include three across-record repeats; no extra within-record associations.           |
| [Historical names/availability](count-gap-20261106/analysis.md#historical-versioning)                       |          unassessed |                                      13 | **Defer to #5875:** do not reconstruct API history inside this rule.                                             |
| [Writable PATCH inputs absent from PUT input](count-gap-20261106/analysis.md#valid-source-checks-to-retain) |          unassessed |                                      17 | **Retain:** model/API owners should correct unintended writable declarations or confirm the contract.            |
| [Empty PATCH body](gap-investigation.md#netapp-49-swagger--2-typespec)                                      |                   0 |                                       1 | **Retain:** Swagger sees a body parameter but misses the empty input; request an owner correction.               |

**182 - 85 = 92 + 32 + 1 + 3 - 31 = 97.**

The [exact per-project bridge](names-20261117/reconciliation.json) preserves
both gap directions. All retained records are accounted for without calling
omitted checks compatible or retiring deferred versioning work.

## NOTES

- **Source:** [`fb7029f43`](https://github.com/Azure/typespec-azure/commit/fb7029f43ef7feaf88a8885070f4775d82e42fff),
  [PR #5481](https://github.com/Azure/typespec-azure/pull/5481);
  [frozen population and policy](refresh-20261117-names/task.json).
  The comparison explicitly enables the mapped rule while preserving authored
  suppressions. The immutable staging supplement is unchanged.
  No Swagger was regenerated.
- **Effect:** removed the entire **132-line helper** and incompatible-property
  diagnostic. **104 -> 85 warnings**, with all other warning families unchanged.
  [Assessment](names-20261117/assessment.md) lists the 19 lost warnings and their
  26 retained-record associations separately from the six previously omitted records.
- **Validation:** 76 canonical PATCH tests, clean build/lint/format, Chronus,
  17 injected, 37 applicable portable and 12 extraction controls passed.
  Both actual published ARM-template examples were compiled unchanged.
  [All six exact-head Build jobs passed](refresh-20261117-names/provenance/ci-build-checks.json).
  External integration is left unchanged as requested.
- **Execution:** the final run completed across all 487 projects. All 51
  attribution arrays exactly match full-run arrays, including order.
  [Verification and replay](replay.md) distinguish current evidence from
  immutable historical observations and their older finalization recovery.

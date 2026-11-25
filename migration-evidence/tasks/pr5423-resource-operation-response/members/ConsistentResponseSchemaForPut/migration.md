# ConsistentResponseSchemaForPut migration

## 1. Scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` is assessed against [`ConsistentResponseSchemaForPut`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-response-schema-for-put.md). Original migration linter PR: [Azure/typespec-azure#5423](https://github.com/Azure/typespec-azure/pull/5423).

## 2. Coverage

All 487 frozen projects succeeded; none failed or was unassessed. Counts are individual diagnostics attributed to this member's actual comparison, not the shared rule's full output. Captured suppressed findings are included only in the inspected affected union.

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------- | --------------- |
| Reported diagnostics | 16             | 2               |

The TypeSpec total comprises 1 corresponding configured diagnostics and 1 corresponding captured suppressed diagnostics. Other members and different canonical/source-version policies are not credited to this member. [Inclusion, exclusions and original callbacks](../../instance-correspondence.md).

**Analysis:** 1 of 16 original Swagger check contexts is diagnosed: 1 by corresponding configured diagnostics. Remaining: 15 confirmed Swagger linter false positives. Suppressed diagnostics count toward this assessment, not the configured raw total. Check contexts are not confirmed service defects; equivalent-defect coverage remains unassessed.

See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

`Raw / grouped` means individual Swagger findings / distinct check contexts (Swagger member, project, resolved document, route and schema comparison). The TypeSpec column includes corresponding captured suppressed diagnostics. Check contexts sharing a diagnostic are kept in one connected component; distinct callbacks remain distinct. This makes source/emission multiplicity and overlapping owning diagnostics countable without treating contexts as equivalent defects.

| Difference (with evidence)                                                           | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics for the same check | analysis                                                                                                                                                                  |
| ------------------------------------------------------------------------------------ | ----------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Already-diagnosed count differences](../../gap-analysis.md#corroborated-count-only) | 1 / 1                               | 2                                       | Count-only difference: repeated emitted occurrences or several distinct owning diagnostics support the same check; do not change production semantics to equalize counts. |
| [Confirmed Swagger false positive](../../gap-analysis.md#upstream-identity-bug)      | 15 / 15                             | 0                                       | Confirmed resolved-object-identity bug; intentionally do not port its false positives.                                                                                    |

**Raw-count reconciliation:** `16 - 2 = 14 = (-1) + (+15)`. The other 0 Swagger / 0 TypeSpec diagnostics belong to balanced components. Balanced totals are not an equivalence claim; opposing component/project differences remain in [the exact accounting](../../diagnostic-count-components.json) and [directional project evidence](../../project-differences.md).

## 4. Function-level coverage

| Behavior                                                       | Result                                  | analysis                                                                                                                                                                                                                          |
| -------------------------------------------------------------- | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Actual body-bearing 200/201 responses for registered resources | Covered for observed genuine difference | Canonical consistency now inspects actual HTTP success bodies, including plain nonresource models; Quota also has an existing Azure Core diagnostic. [Evidence](../../gap-analysis.md#member-consistent-response-schema-for-put). |
| Equal success schemas; absent or explicit-void bodies          | Covered / scoped exemptions             | Equal schemas do not get an object-identity false positive. This check skips absent/void bodies; separate response-body/status rules still apply. [Evidence](../../gap-analysis.md#member-consistent-response-schema-for-put).    |

## NOTES

- **Inputs:** Assessed source `d40a080dd`, core `683031f80`, specs `2cd3c5dd6`. Fresh source-program execution against retained latest-version Swagger; not universally version-aligned defects. [Provenance and recovery](../../evidence-details.md).
- **Counting:** Distinct callbacks are retained; shared diagnostics can contribute to several member notes and must not be summed. Suppression capture is not an exhaustive corpus scan. [Component accounting](../../diagnostic-count-components.json).
- **Validation:** [Assessed source and runtime gates](../../validation.json); [current head CI, separate from historical results](../../evidence-details.md#validation-and-ci).

[Pinned Swagger implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/consistent-response-schema-for-put.ts). [Shared provenance, controls, recovery and replay](../../evidence-details.md). [Exact targets](../../instance-correspondence.md).

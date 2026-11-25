# PutGetPatchResponseSchema migration

## 1. Scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` is assessed against [`PutGetPatchResponseSchema`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-get-patch-response-schema.md). Original migration linter PR: [Azure/typespec-azure#5423](https://github.com/Azure/typespec-azure/pull/5423).

## 2. Coverage

All 487 frozen projects succeeded; none failed or was unassessed. Counts are individual diagnostics attributed to this member's actual comparison, not the shared rule's full output. Captured suppressed findings are included only in the inspected affected union.

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------- | --------------- |
| Reported diagnostics | 50             | 16              |

The TypeSpec total comprises 0 corresponding configured diagnostics and 16 corresponding captured suppressed diagnostics. Other members and different canonical/source-version policies are not credited to this member. [Inclusion, exclusions and original callbacks](../../instance-correspondence.md).

**Analysis:** 16 of 36 original Swagger check contexts are diagnosed: 16 additional checks by existing owning diagnostics captured before authored suppression. Remaining: 19 proposed no-content/collection exclusions awaiting approval; 1 modeling or contract check still unresolved/deferred. Suppressed diagnostics count toward this assessment, not the configured raw total. Check contexts are not confirmed service defects; equivalent-defect coverage remains unassessed.

See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

`Raw / grouped` means individual Swagger findings / distinct check contexts (Swagger member, project, resolved document, route and schema comparison). The TypeSpec column includes corresponding captured suppressed diagnostics. Check contexts sharing a diagnostic are kept in one connected component; distinct callbacks remain distinct. This makes source/emission multiplicity and overlapping owning diagnostics countable without treating contexts as equivalent defects.

| Difference (with evidence)                                                                                         | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics for the same check | analysis                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------ | ----------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| [Empty 200: real response-body issue, not two unequal payload models](../../gap-analysis.md#body-policy-owner)     | 15 / 1                              | 1                                       | Review the authored suppression and wire contract; do not duplicate the existing response-body check.                                |
| [Swagger schema-comparison false positive / policy overreach](../../gap-analysis.md#bodyless-comparator-overreach) | 15 / 15                             | 0                                       | Recommend excluding absent-body comparisons, not inventing bodies. Status-code compliance is a separate policy; approval is pending. |
| [Swagger collection-shape comparison false positive](../../gap-analysis.md#collection-comparator-overreach)        | 4 / 4                               | 0                                       | Recommend excluding wrapper-versus-item reference equality: actual resource items agree. Approval is pending.                        |
| [Genuine PUT/GET resource-shape difference](../../gap-analysis.md#cross-method-entity-contract)                    | 1 / 1                               | 0                                       | Genuine uncovered contract difference. Confirm service intent before sharing models; defer a broad structural matcher.               |

**Raw-count reconciliation:** `50 - 16 = 34 = (+14) + (+15) + (+4) + (+1)`. The other 15 Swagger / 15 TypeSpec diagnostics belong to balanced components. Balanced totals are not an equivalence claim; opposing component/project differences remain in [the exact accounting](../../diagnostic-count-components.json) and [directional project evidence](../../project-differences.md).

## 4. Function-level coverage

| Behavior                                                   | Result                                 | analysis                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Resolved lifecycle actual success responses and list items | Covered canonical-resource policy      | Read/create/update/list associations are traversed at each resolved scope. Arrays/value envelopes supply list items; discriminated response ancestry is preserved. Unresolved LIST/PATCH-only occurrences are not checked. [Evidence](../../gap-analysis.md#member-put-get-patch-response-schema). |
| Empty 200 compared with a resource                         | Covered by existing owning diagnostics | Captured no-response-body callbacks remain diagnostic evidence despite authored suppression; schema equality must not replace body-existence policy. [Evidence](../../gap-analysis.md#member-put-get-patch-response-schema).                                                                       |
| No-content / same-item collection roles                    | Recommended intentional difference     | Comparing absent schemas or wrapper names does not establish a different resource item. Exclusions remain recommendations awaiting approval. [Evidence](../../gap-analysis.md#member-put-get-patch-response-schema).                                                                               |
| SyncJob PUT/GET shape difference                           | Missing / deferred                     | The borrowed SourceControl read association diagnoses another comparison. Confirm owner intent before sharing models; one route does not justify a recursive version/visibility-aware schema matcher. [Evidence](../../gap-analysis.md#member-put-get-patch-response-schema).                      |

## NOTES

- **Inputs:** Assessed source `d40a080dd`, core `683031f80`, specs `2cd3c5dd6`. Fresh source-program execution against retained latest-version Swagger; not universally version-aligned defects. [Provenance and recovery](../../evidence-details.md).
- **Counting:** Distinct callbacks are retained; shared diagnostics can contribute to several member notes and must not be summed. Suppression capture is not an exhaustive corpus scan. [Component accounting](../../diagnostic-count-components.json).
- **Validation:** [Assessed source and runtime gates](../../validation.json); [current head CI, separate from historical results](../../evidence-details.md#validation-and-ci).

[Pinned Swagger implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/put-get-patch-schema.ts). [Shared provenance, controls, recovery and replay](../../evidence-details.md). [Exact targets](../../instance-correspondence.md).

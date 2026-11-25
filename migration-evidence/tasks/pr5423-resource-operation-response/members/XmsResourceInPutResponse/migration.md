# XmsResourceInPutResponse migration

## 1. Scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` is assessed against [`XmsResourceInPutResponse`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/xms-resource-in-put-response.md). Original migration linter PR: [Azure/typespec-azure#5423](https://github.com/Azure/typespec-azure/pull/5423).

## 2. Coverage

All 487 frozen projects succeeded; none failed or was unassessed. Counts are individual diagnostics attributed to this member's actual comparison, not the shared rule's full output. Captured suppressed findings are included only in the inspected affected union.

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------- | --------------- |
| Reported diagnostics | 155            | 38              |

The TypeSpec total comprises 38 corresponding configured diagnostics and 0 corresponding captured suppressed diagnostics. Other members and different canonical/source-version policies are not credited to this member. [Inclusion, exclusions and original callbacks](../../instance-correspondence.md).

**Analysis:** 38 of 57 original Swagger check contexts are diagnosed: 38 by corresponding configured diagnostics. Remaining: 9 intentional TypeSpec-resource/Swagger-marker differences; 10 checks missed because the resolver omits the PUT. Suppressed diagnostics count toward this assessment, not the configured raw total. Check contexts are not confirmed service defects; equivalent-defect coverage remains unassessed.

See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

`Raw / grouped` means individual Swagger findings / distinct check contexts (Swagger member, project, resolved document, route and schema comparison). The TypeSpec column includes corresponding captured suppressed diagnostics. Check contexts sharing a diagnostic are kept in one connected component; distinct callbacks remain distinct. This makes source/emission multiplicity and overlapping owning diagnostics countable without treating contexts as equivalent defects.

| Difference (with evidence)                                                                                            | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics for the same check | analysis                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Native resource identity differs from emitted marker presence](../../gap-analysis.md#native-resource-representation) | 9 / 9                               | 0                                       | The selected body is a native resource. Marker/emission differences do not make it invalid; intentionally do not reproduce extension-level parity.     |
| [Marked PUTs on non-ARM targets are omitted by the resolver](../../gap-analysis.md#resolver-operation-gap)            | 108 / 10                            | 0                                       | Ten marked Network PUTs target models without ARM declarations. Reported in #5995; resolve the API/modeling prerequisite, not by fallback enumeration. |

**Raw-count reconciliation:** `155 - 38 = 117 = (+9) + (+108)`. The other 38 Swagger / 38 TypeSpec diagnostics belong to balanced components. Balanced totals are not an equivalence claim; opposing component/project differences remain in [the exact accounting](../../diagnostic-count-components.json) and [directional project evidence](../../project-differences.md).

## 4. Function-level coverage

| Behavior                                                 | Result                 | analysis                                                                                                                                                                                                                                                                                             |
| -------------------------------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Resolver-exposed ARM PUT, every body-bearing 200 and 201 | Covered                | Resolved resources, native resource-base ancestry, virtual and existing custom declarations are accepted. Arrays, scalars and lookalike DTOs fail. A canonical response warning avoids a duplicate resource-identity warning. [Evidence](../../gap-analysis.md#member-xms-resource-in-put-response). |
| Extension overrides and custom emission options          | Intentional difference | They neither create nor erase native resource identity. The linter does not inspect extensions or simulate emitted Swagger. [Evidence](../../gap-analysis.md#member-xms-resource-in-put-response).                                                                                                   |
| Absent/void body and non-PUT operations                  | Outside this check     | Body/status rules own absent bodies; the added resource-identity check applies only to PUT. [Evidence](../../gap-analysis.md#member-xms-resource-in-put-response).                                                                                                                                   |
| PUTs omitted by resolveArmResources                      | Missing                | Ten marked Network PUTs are absent from both resolver collections. Issue #5995 tracks the prerequisite; there is no fallback enumeration. [Evidence](../../gap-analysis.md#member-xms-resource-in-put-response).                                                                                     |

## NOTES

- **Inputs:** Assessed source `d40a080dd`, core `683031f80`, specs `2cd3c5dd6`. Fresh source-program execution against retained latest-version Swagger; not universally version-aligned defects. [Provenance and recovery](../../evidence-details.md).
- **Counting:** Distinct callbacks are retained; shared diagnostics can contribute to several member notes and must not be summed. Suppression capture is not an exhaustive corpus scan. [Component accounting](../../diagnostic-count-components.json).
- **Validation:** [Assessed source and runtime gates](../../validation.json); [current head CI, separate from historical results](../../evidence-details.md#validation-and-ci).

[Pinned Swagger implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/with-xms-resource.ts). [Shared provenance, controls, recovery and replay](../../evidence-details.md). [Exact targets](../../instance-correspondence.md).

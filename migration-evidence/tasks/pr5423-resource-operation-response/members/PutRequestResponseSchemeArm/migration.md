# PutRequestResponseSchemeArm migration

## 1. Scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` is assessed against [`PutRequestResponseSchemeArm`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-request-response-scheme-arm.md). Original migration linter PR: [Azure/typespec-azure#5423](https://github.com/Azure/typespec-azure/pull/5423).

## 2. Coverage

All 487 frozen projects succeeded; none failed or was unassessed. Counts are individual diagnostics attributed to this member's actual comparison, not the shared rule's full output. Captured suppressed findings are included only in the inspected affected union.

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------- | --------------- |
| Reported diagnostics | 212            | 153             |

The TypeSpec total comprises 144 corresponding configured diagnostics and 9 corresponding captured suppressed diagnostics. Other members and different canonical/source-version policies are not credited to this member. [Inclusion, exclusions and original callbacks](../../instance-correspondence.md).

**Analysis:** 153 of 168 original Swagger check contexts are diagnosed: 144 by corresponding configured diagnostics; 9 additional checks by existing owning diagnostics captured before authored suppression. Remaining: 15 modeling or contract checks still unresolved/deferred. Suppressed diagnostics count toward this assessment, not the configured raw total. Check contexts are not confirmed service defects; equivalent-defect coverage remains unassessed.

See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

`Raw / grouped` means individual Swagger findings / distinct check contexts (Swagger member, project, resolved document, route and schema comparison). The TypeSpec column includes corresponding captured suppressed diagnostics. Check contexts sharing a diagnostic are kept in one connected component; distinct callbacks remain distinct. This makes source/emission multiplicity and overlapping owning diagnostics countable without treating contexts as equivalent defects.

| Difference (with evidence)                                                                                             | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics for the same check | analysis                                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| [Empty 200: real response-body issue, not two unequal payload models](../../gap-analysis.md#body-policy-owner)         | 15 / 1                              | 1                                       | Review the authored suppression and wire contract; do not duplicate the existing response-body check.                                  |
| [Bulk/collection request contract, not ordinary resource replacement](../../gap-analysis.md#custom-collection-request) | 2 / 2                               | 0                                       | Unresolved bulk/item semantics. Require owner intent before enforcing ordinary resource replacement.                                   |
| [Action-like PUT contract](../../gap-analysis.md#custom-command-request)                                               | 2 / 2                               | 0                                       | Unresolved command/association contracts; do not infer canonical replacement solely from PUT.                                          |
| [Custom lifecycle registration/modeling gap](../../gap-analysis.md#custom-lifecycle-registration)                      | 3 / 3                               | 0                                       | Missing associations; three compatibility-checked repairs are in separate draft #47952, not frozen-corpus credit.                      |
| [Canonical parent differs from the actual child/result response](../../gap-analysis.md#parent-canonical-association)   | 3 / 3                               | 0                                       | Wrong parent/operation-kind association; repair modeling only after proving wire/client compatibility.                                 |
| [Deliberate polymorphism with unresolved canonical request association](../../gap-analysis.md#supported-polymorphism)  | 1 / 1                               | 0                                       | Preserve the hierarchy; establish canonical request registration. Response ancestry support does not prove derived-request acceptance. |
| [Unregistered body-bearing request/response mismatch](../../gap-analysis.md#unregistered-entity-request)               | 34 / 4                              | 0                                       | Four legacy DTO contracts lack canonical registration; review visibility/wire models rather than add recursive schema equality.        |

**Raw-count reconciliation:** `212 - 153 = 59 = (+14) + (+2) + (+2) + (+3) + (+3) + (+1) + (+34)`. The other 152 Swagger / 152 TypeSpec diagnostics belong to balanced components. Balanced totals are not an equivalence claim; opposing component/project differences remain in [the exact accounting](../../diagnostic-count-components.json) and [directional project evidence](../../project-differences.md).

## 4. Function-level coverage

| Behavior                                                    | Result                          | analysis                                                                                                                                                                                                                    |
| ----------------------------------------------------------- | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Resolved createOrUpdate PUT at each resource scope          | Covered                         | Each resolved occurrence supplies the canonical model and HTTP operation; effective request identity is checked once per operation/resource pair. [Evidence](../../gap-analysis.md#member-put-request-response-scheme-arm). |
| Missing/void request; compliant and multipart bodies        | Covered / intentional exception | Body existence is additional policy; compliant identity and multipart exemptions are controlled explicitly. [Evidence](../../gap-analysis.md#member-put-request-response-scheme-arm).                                       |
| Unregistered, command, collection or wrong-parent contracts | Partial / unresolved            | HTTP PUT alone does not establish a canonical resource. Separate compatibility-gated spec fixes are safer than a global structural comparator. [Evidence](../../gap-analysis.md#member-put-request-response-scheme-arm).    |

## NOTES

- **Inputs:** Assessed source `d40a080dd`, core `683031f80`, specs `2cd3c5dd6`. Fresh source-program execution against retained latest-version Swagger; not universally version-aligned defects. [Provenance and recovery](../../evidence-details.md).
- **Counting:** Distinct callbacks are retained; shared diagnostics can contribute to several member notes and must not be summed. Suppression capture is not an exhaustive corpus scan. [Component accounting](../../diagnostic-count-components.json).
- **Validation:** [Assessed source and runtime gates](../../validation.json); [current head CI, separate from historical results](../../evidence-details.md#validation-and-ci).

[Pinned Swagger implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/put-request-response-scheme.ts). [Shared provenance, controls, recovery and replay](../../evidence-details.md). [Exact targets](../../instance-correspondence.md).

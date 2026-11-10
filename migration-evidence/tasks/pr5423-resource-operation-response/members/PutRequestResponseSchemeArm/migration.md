# PutRequestResponseSchemeArm migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` is assessed against [`PutRequestResponseSchemeArm`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-request-response-scheme-arm.md). **Not fully equivalent. Registered create/update requests are checked against their canonical resource, but unassociated PUTs and incorrect resource associations leave request-contract gaps.**

## 2. Actual coverage

All 487 frozen projects succeeded; none failed or was unassessed. Counts are individual diagnostics, not projects. The TypeSpec total is the shared rule's full output across all four Swagger members, not this member's matched findings.

| Count                                                                 | Swagger linter | TypeSpec linter |
| --------------------------------------------------------------------- | -------------- | --------------- |
| Reported diagnostics (member / responsible rule)                      | 212            | 283             |
| Affected HTTP routes (grouped by project/route; member / shared rule) | 168            | 273             |

**Assessed coverage:** 153 of 168 original Swagger check contexts are diagnosed: 144 by corresponding configured diagnostics; 9 additional checks by existing owning diagnostics captured before authored suppression. Remaining: 15 modeling or contract checks still unresolved/deferred. Suppressed diagnostics count toward this assessment, not the configured raw total. Check contexts are not confirmed service defects; equivalent-defect coverage remains unassessed.

See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the decisions, including broader shared-rule checks.

## 3. Function-level coverage

| Behavior                                                              | Result                          | Rationale                                                                                                                                                                                                                |
| --------------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Registered createOrUpdate PUT, including retained/overwritten aliases | Covered                         | Existing resource operation registrations select the canonical model; effective request identity is checked once per operation/resource. [Evidence](../../gap-analysis.md#member-put-request-response-scheme-arm).       |
| Missing/void request; compliant and multipart bodies                  | Covered / intentional exception | Body existence is additional policy; compliant identity and multipart exemptions are controlled explicitly. [Evidence](../../gap-analysis.md#member-put-request-response-scheme-arm).                                    |
| Unregistered, command, collection or wrong-parent contracts           | Partial / unresolved            | HTTP PUT alone does not establish a canonical resource. Separate compatibility-gated spec fixes are safer than a global structural comparator. [Evidence](../../gap-analysis.md#member-put-request-response-scheme-arm). |

## 4. Why diagnostic counts differ

`Raw / grouped` means individual Swagger findings / distinct check contexts (Swagger member, project, resolved document, route and schema comparison). The TypeSpec column counts configured diagnostics attributed to that same check, not unrelated warnings on the route. Captured diagnostics before suppression are stated separately in the rationale and still count as diagnosed coverage. A diagnostic can cover several check contexts.

| Difference (with evidence)                                                                                             | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics for the same check | Recommended action and rationale                                                                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Empty 200: real response-body issue, not two unequal payload models](../../gap-analysis.md#body-policy-owner)         | 23 / 9                              | 0                                       | Covered: 9 captured owning diagnostics diagnose 9 check contexts despite authored suppression. Review the authored suppression and wire contract; do not duplicate the existing response-body check. |
| [Bulk/collection request contract, not ordinary resource replacement](../../gap-analysis.md#custom-collection-request) | 2 / 2                               | 0                                       | Unresolved bulk/item semantics. Require owner intent before enforcing ordinary resource replacement.                                                                                                 |
| [Action-like PUT contract](../../gap-analysis.md#custom-command-request)                                               | 2 / 2                               | 0                                       | Unresolved command/association contracts; do not infer canonical replacement solely from PUT.                                                                                                        |
| [Custom lifecycle registration/modeling gap](../../gap-analysis.md#custom-lifecycle-registration)                      | 3 / 3                               | 0                                       | Missing associations; three compatibility-checked repairs are in separate draft #47952, not frozen-corpus credit.                                                                                    |
| [Canonical parent differs from the actual child/result response](../../gap-analysis.md#parent-canonical-association)   | 3 / 3                               | 0                                       | Wrong parent/operation-kind association; repair modeling only after proving wire/client compatibility.                                                                                               |
| [Deliberate polymorphism with unresolved canonical request association](../../gap-analysis.md#supported-polymorphism)  | 1 / 1                               | 0                                       | Preserve the hierarchy; establish canonical request registration. Response ancestry support does not prove derived-request acceptance.                                                               |
| [Unregistered body-bearing request/response mismatch](../../gap-analysis.md#unregistered-entity-request)               | 34 / 4                              | 0                                       | Four legacy DTO contracts lack canonical registration; review visibility/wire models rather than add recursive schema equality.                                                                      |
| [Other checks from the shared TypeSpec rule](../../gap-analysis.md#typespec-only-checks)                               | 0 / 0                               | 139                                     | 39 diagnose other members; 100 are additional/different policy or population checks. Keep their individual source/body/canonical dispositions separate; none receives this member's credit.          |

## NOTES

Assessed source `779b3c409`. The TypeSpec linter is enabled in the shared ARM profile and explicitly selected for this comparison. Counts compare the source program with latest-version Swagger, not universally version-aligned defects. Each diagnosed check receives credit once, including captured diagnostics hidden by authored suppression.

[Pinned Swagger implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/put-request-response-scheme.ts). [Shared provenance, controls, recovery and replay](../../evidence-details.md). [Exact targets](../../instance-correspondence.md).

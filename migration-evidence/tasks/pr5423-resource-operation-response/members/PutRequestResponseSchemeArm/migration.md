# PutRequestResponseSchemeArm migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` is assessed against [`PutRequestResponseSchemeArm`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-request-response-scheme-arm.md). **Partial coverage. Registered createOrUpdate requests are checked, but unassociated legacy contracts and wrong canonical-resource associations remain; emitted structural equality is not generally reproduced.**

## 2. Actual coverage

All 487 frozen projects succeeded; none failed or was unassessed. Reported diagnostics are individual findings. The TypeSpec raw total is the responsible rule's full output, shared with other members where applicable; it is not this member's credited coverage.

| Count                                                                       | Swagger linter | TypeSpec linter |
| --------------------------------------------------------------------------- | -------------- | --------------- |
| Reported diagnostics (member / responsible rule)                            | 212            | 283             |
| Affected project/routes (member / responsible rule, not equivalent defects) | 168            | 273             |

**Assessed coverage:** 153 of 168 original member-check contexts are diagnosed: 144 by corresponding configured warnings; 9 additional contexts by captured owning diagnostics before authored suppression. Remaining: 15 unresolved/modeling or deferred contract contexts. Captured selected-rule and owning diagnostics count despite suppression; configured raw totals are unchanged. Contexts are not equivalent-defect counts; universal violation percentages remain unassessed.

See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the decisions, including broader shared-rule checks.

## 3. Function-level coverage

| Behavior                                                              | Result                          | Rationale                                                                                                                                                                                                                |
| --------------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Registered createOrUpdate PUT, including retained/overwritten aliases | Covered                         | Existing resource operation registrations select the canonical model; effective request identity is checked once per operation/resource. [Evidence](../../gap-analysis.md#member-put-request-response-scheme-arm).       |
| Missing/void request; compliant and multipart bodies                  | Covered / intentional exception | Body existence is additional policy; compliant identity and multipart exemptions are controlled explicitly. [Evidence](../../gap-analysis.md#member-put-request-response-scheme-arm).                                    |
| Unregistered, command, collection or wrong-parent contracts           | Partial / unresolved            | HTTP PUT alone does not establish a canonical resource. Separate compatibility-gated spec fixes are safer than a global structural comparator. [Evidence](../../gap-analysis.md#member-put-request-response-scheme-arm). |

## 4. Why diagnostic counts differ

`Raw / grouped` means reported Swagger diagnostics / distinct (member, project, resolved document, exact route, compared schema context) checks. The TypeSpec column is configured / captured-before-suppression diagnostics for the same check, including responsible existing owners. Suppression does not remove diagnostic coverage. Callbacks can cover several member contexts, so these rows are not additive defect counts.

| Difference (with evidence)                                                                                             | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics (configured / before suppression) | Decision and rationale                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Empty 200: real response-body issue, not two unequal payload models](../../gap-analysis.md#body-policy-owner)         | 23 / 9                              | 0 / 9                                                  | Covered by 9 captured owning diagnostic callbacks over 9 contexts before suppression. Diagnosed by the existing body owner before suppression; review the suppression/wire contract, not duplicate schema equality. |
| [Bulk/collection request contract, not ordinary resource replacement](../../gap-analysis.md#custom-collection-request) | 2 / 2                               | 0 / 0                                                  | Unresolved bulk/item semantics. Require owner intent before enforcing ordinary resource replacement.                                                                                                                |
| [Action-like PUT contract](../../gap-analysis.md#custom-command-request)                                               | 2 / 2                               | 0 / 0                                                  | Unresolved command/association contracts; do not infer canonical replacement solely from PUT.                                                                                                                       |
| [Custom lifecycle registration/modeling gap](../../gap-analysis.md#custom-lifecycle-registration)                      | 3 / 3                               | 0 / 0                                                  | Missing associations; three compatibility-checked repairs are in separate draft #47952, not frozen-corpus credit.                                                                                                   |
| [Canonical parent differs from the actual child/result response](../../gap-analysis.md#parent-canonical-association)   | 3 / 3                               | 0 / 0                                                  | Wrong parent/operation-kind association; repair modeling only after proving wire/client compatibility.                                                                                                              |
| [Deliberate polymorphism with unresolved canonical request association](../../gap-analysis.md#supported-polymorphism)  | 1 / 1                               | 0 / 0                                                  | Preserve the hierarchy; establish canonical request registration. Response ancestry support does not prove derived-request acceptance.                                                                              |
| [Unregistered body-bearing request/response mismatch](../../gap-analysis.md#unregistered-entity-request)               | 34 / 4                              | 0 / 0                                                  | Four legacy DTO contracts lack canonical registration; review visibility/wire models rather than add recursive schema equality.                                                                                     |
| [Other responsible-rule checks](../../gap-analysis.md#typespec-only-checks)                                            | 0 / 0                               | 139 configured                                         | 39 diagnose other members; 100 are additional/different policy or population checks. Keep their individual source/body/canonical dispositions separate; none receives this member's credit.                         |

## NOTES

Assessed source `779b3c409`; source-program versus latest-version Swagger, not universal version-aligned equivalence. The existing response rule is enabled in the shared ARM profile; its expanded native PUT guidance is intentionally enabled too. The worker explicitly enables the selected rule for comparison. Authored suppressions affect reported totals, not assessed diagnostic coverage; selected-rule and owning callbacks are credited without double-counting contexts.

[Pinned Swagger implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/put-request-response-scheme.ts). [Shared provenance, controls, recovery and replay](../../evidence-details.md). [Exact targets](../../instance-correspondence.md).

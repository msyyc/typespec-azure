# ARM resource operation response migration

## 1. Conclusion and scope

**Partial migration, not functionally equivalent.** This assessment evaluates
`@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` against
[`PutRequestResponseSchemeArm`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-request-response-scheme-arm.md),
[`ConsistentResponseSchemaForPut`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-response-schema-for-put.md),
[`XmsResourceInPutResponse`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/xms-resource-in-put-response.md)
and [`PutGetPatchResponseSchema`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-get-patch-response-schema.md).
The TypeSpec linter misses registered PUT request checks and independent resource-marker
validation; some legacy contracts also remain unresolved. **Fix the registered-request
traversal first.** Do not seek literal diagnostic parity: the Swagger linter has an
object-identity bug, and other differences involve misleading schema comparisons or
checks already implemented by other TypeSpec rules but explicitly suppressed in these specs.

## 2. Actual coverage

All **487 projects** compiled successfully; none failed or was unassessed.
Reported diagnostics are individual findings, not project counts.

| Count                                                              | Swagger linter | TypeSpec linter |
| ------------------------------------------------------------------ | -------------- | --------------- |
| Reported diagnostics                                               | 433            | 104             |
| HTTP routes referenced by findings, grouped by exact project/route | 256            | 104             |

Routes can contain several distinct checks; these counts do not measure equivalent defects.
Repeated Swagger observations, missed checks, Swagger false positives, suppressions and
source-version differences explain the gap.
See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ).

## 3. Function-level coverage

| Behavior                                     | Result                                                                                                                               |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| PUT request matches its canonical resource   | Partial: only the retained lifecycle PUT is checked; other registered PUTs are missed.                                               |
| Success responses use the same schema        | Not independently checked by this rule. Azure Core `response-schema-problem` detects the observed Quota mismatch before suppression. |
| Selected PUT response is an ARM resource     | Missing: canonical registration does not enforce the emitted `x-ms-azure-resource` marker.                                           |
| PUT/GET/PATCH/LIST return the same resource  | Limited registered-resource traversal, not general payload comparison. Legacy shape differences remain unresolved.                   |
| Canonical templates, aliases and suppression | Existing [violating/compliant controls](evidence-details.md#controls-and-validation) retained.                                       |

## 4. Why diagnostic counts differ

The 433 Swagger findings represent **277 member checks**: each retains the rule, project,
document, route and schema context. **87 checks have a corresponding TypeSpec warning**.
The remaining **190 checks** are explained below; they are not 190 proven defects.

The TypeSpec column counts only this rule's warnings for the **same comparison**.
It excludes unrelated warnings on the same operation and other rules' pre-suppression results.

| Difference and evidence                                                                       | Swagger findings / checks | TypeSpec corresponding warnings | Decision                                                                                                                                          |
| --------------------------------------------------------------------------------------------- | ------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Registered PUTs skipped by retained-map traversal](gap-analysis.md#registered-put-traversal) | 57 / 57                   | 0                               | Small rule change: enumerate existing registered operations. These are verified candidates, not measured post-fix gains.                          |
| [Empty 200 responses](gap-analysis.md#existing-policy-exceptions)                             | 53 / 25                   | 0                               | 16 route contexts already detected by `no-response-body` before explicit suppressions. Review those exceptions/specs; do not duplicate the check. |
| [Quota's different 200/201 bodies](gap-analysis.md#existing-policy-exceptions)                | 1 / 1                     | 0                               | Existing Azure Core rule detects it before explicit suppression. Review the legacy exception.                                                     |
| [Identical schemas rejected by object identity](gap-analysis.md#swagger-comparison-artifacts) | 15 / 15                   | 0                               | Confirmed Swagger bug; do not reproduce it.                                                                                                       |
| [No-content and collection-wrapper comparisons](gap-analysis.md#swagger-comparison-artifacts) | 19 / 19                   | 0                               | 15 bodyless responses and four matching-item collections are misleading schema comparisons. Recommend not porting them.                           |
| [Missing resource-marker policy](gap-analysis.md#response-resource-policy)                    | 155 / 57                  | 0                               | Design a focused check with explicit custom/action boundaries; medium complexity and unresolved policy.                                           |
| [Legacy request/response contracts](gap-analysis.md#legacy-contracts)                         | 45 / 15                   | 0                               | Review registration, DTOs and parent/child modeling before broadening the rule.                                                                   |
| [SyncJob PUT/GET shape difference](gap-analysis.md#legacy-contracts)                          | 1 / 1                     | 0                               | Confirm the service contract; defer a broad structural matcher for this observed case.                                                            |

Of the **17 other TypeSpec findings**, eight enforce missing-request policy, seven compare
a different contract, one concerns a Batch operation removed from the selected version,
and one checks a 202-only PUT outside the Swagger selector.
[All findings and exact targets](instance-correspondence.md#typespec-finding-accounting)
remain accounted for.

The recommended no-content/collection exclusions are **not approved policy retirements**.
Resource-marker and legacy-contract questions still prevent a complete migration claim.

## NOTES

Corpus: TypeSpec candidate `2d82a09`, specs `2cd3c5d`; full pins and execution policies are
in [task.json](task.json). The later PR merge `a4b87e3` did not change assessed logic
([comparison](receipts/publication-head-comparison.json)); this is not a new-head corpus run.
TypeSpec uses configured source compilation with authored suppressions; Swagger uses
latest-version output without production readme suppressions. TypeSpec severity is warning;
the Swagger rules are errors, with `ConsistentResponseSchemaForPut` staging-only.

Member evidence:
[request/response](members/PutRequestResponseSchemeArm/migration.md),
[200/201 responses](members/ConsistentResponseSchemaForPut/migration.md),
[resource marker](members/XmsResourceInPutResponse/migration.md),
[cross-operation responses](members/PutGetPatchResponseSchema/migration.md).
[Decision rationale](gap-analysis.md), [per-project inventory](instance-correspondence.md#differing-projects)
and [controls, provenance and reproduction](evidence-details.md) retain the supporting detail.

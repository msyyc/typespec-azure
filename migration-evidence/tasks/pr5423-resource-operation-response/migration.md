# ARM resource operation response migration

## 1. Conclusion and scope

**Partial migration, not functionally equivalent.** This assessment evaluates
`@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` against
[`PutRequestResponseSchemeArm`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-request-response-scheme-arm.md),
[`ConsistentResponseSchemaForPut`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-response-schema-for-put.md),
[`XmsResourceInPutResponse`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/xms-resource-in-put-response.md)
and [`PutGetPatchResponseSchema`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-get-patch-response-schema.md).
Registered createOrUpdate PUT request coverage includes legacy and overwritten aliases.
Independent response-resource policy and legacy contracts remain incomplete.
Literal diagnostic parity is inappropriate: the Swagger linter has an object-identity bug;
other differences involve misleading schema comparisons or existing TypeSpec checks
explicitly suppressed in these specs. Required CI remains failing
([CI and validation limits](evidence-details.md#external-ci-and-validation-limits)); this is not migration acceptance.

## 2. Actual coverage

All **487 projects** compiled successfully; none failed or was unassessed.
Reported diagnostics are individual findings, not project counts.

| Count                                                              | Swagger linter | TypeSpec linter |
| ------------------------------------------------------------------ | -------------- | --------------- |
| Reported diagnostics                                               | 433            | 180             |
| HTTP routes referenced by findings, grouped by exact project/route | 256            | 180             |

A route can carry multiple distinct checks; grouping does not establish equivalent defects.
Repeated Swagger observations, missing independent policies, Swagger false positives,
authored exceptions and additional source-level checks explain the remaining gap.
See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ).

## 3. Function-level coverage

| Behavior                                    | Result                                                                                                                                                      |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PUT request matches its canonical resource  | Covered for eligible registered createOrUpdate PUTs, including legacy and overwritten aliases. Custom/unregistered contracts remain outside that guarantee. |
| Success responses use the same schema       | Not independently checked by this rule. Azure Core `response-schema-problem` detects the observed Quota mismatch before suppression.                        |
| Selected PUT response is an ARM resource    | Missing: canonical registration does not enforce the emitted `x-ms-azure-resource` marker.                                                                  |
| PUT/GET/PATCH/LIST return the same resource | Existing registered-resource traversal retained; not general payload equality. Legacy shape differences remain unresolved.                                  |
| Canonical requests, aliases and exclusions  | Compliant requests remain clean; action/non-PUT, multipart and internal exclusions, deduplication and authored suppression are tested.                      |

## 4. Why diagnostic counts differ

The 433 Swagger findings represent **277 member checks**, retaining rule, project,
document, route and schema context. **144 checks have a corresponding TypeSpec warning**;
**133 remain unpaired**. They are not 133 proven defects.

The TypeSpec column below counts only this rule's warnings for the **same comparison**,
not unrelated warnings on the same operation or other rules' pre-suppression results.

| Difference and evidence                                                                  | Swagger findings / checks | TypeSpec corresponding warnings | Gap analysis and decision                                                                                     |
| ---------------------------------------------------------------------------------------- | ------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [Empty 200 responses](gap-analysis.md#existing-policy-exceptions)                        | 53 / 25                   | 0                               | Review existing no-response-body suppressions/specs; do not duplicate that check.                             |
| [Quota success-schema difference](gap-analysis.md#existing-policy-exceptions)            | 1 / 1                     | 0                               | Review the existing Azure Core rule's suppression/legacy exception; do not duplicate it in ARM.               |
| [Swagger object-identity bug](gap-analysis.md#swagger-comparison-artifacts)              | 15 / 15                   | 0                               | Confirmed false positives: do not reproduce the bug.                                                          |
| [No-content / collection-role comparisons](gap-analysis.md#swagger-comparison-artifacts) | 19 / 19                   | 0                               | Recommend not porting misleading schema comparisons; this is not approved retirement or whole-API compliance. |
| [Independent response-resource policy](gap-analysis.md#response-resource-policy)         | 155 / 57                  | 0                               | Design a focused check with custom/action boundaries; the policy remains unresolved.                          |
| [Legacy request/response contracts](gap-analysis.md#legacy-contracts)                    | 45 / 15                   | 0                               | Review registration, DTOs and parent/child modeling; do not broaden blindly to every PUT.                     |
| [SyncJob PUT/GET shape difference](gap-analysis.md#legacy-contracts)                     | 1 / 1                     | 0                               | Confirm the wire contract; prefer a targeted fix and defer a broad structural matcher.                        |

All **36 additional or different TypeSpec findings** are accounted for: Missing-request policy: 25; Same operation, different comparison: 8; Source-only version population: 2; Outside Swagger 200/201 selector: 1.
See [exact comparison accounting](instance-correspondence.md#typespec-finding-accounting)
for targets, causes and decisions. They are not credited to a different Swagger
check merely because the route matches.

Recommended no-content/collection exclusions are **not approved policy retirements**.
Resource-marker and legacy-contract questions still prevent a complete migration claim.

## NOTES

Final assessed source: `e45c2bc87`; frozen specs: `2cd3c5dd6`.
The fix preserved all 104 previous TypeSpec findings and recovered
all 57 previously identified registered-PUT comparisons:
paired member checks rose from 87 to 144,
while raw TypeSpec findings changed from 104 to 180.
Of 76 added warnings, 57 correspond to the recovered comparisons; the other 19 expose additional body-existence policy, a different canonical comparison or an older-source operation,
not additional Swagger coverage.
[Measured before/after evidence](receipts/put-traversal-before-after-20261105.json)
and [resolved example](gap-analysis.md#registered-put-traversal).

The initial corpus process terminated after 136 successful workers; the remaining 351
completed with unchanged inputs and worker. All 93,496 dataset files passed post-run
SHA-256 verification. This is a recovered full population, not a clean original CLI exit
([recovery evidence](evidence-details.md#final-source-execution-and-recovery)).

TypeSpec uses configured source compilation with authored suppressions; Swagger uses
latest-version output without production readme suppressions. This is not universal
version-aligned equivalence. TypeSpec severity is warning; the Swagger rules are errors,
with `ConsistentResponseSchemaForPut` explicitly evaluated in the staging supplement.

Member evidence:
[request/response](members/PutRequestResponseSchemeArm/migration.md),
[200/201 responses](members/ConsistentResponseSchemaForPut/migration.md),
[resource marker](members/XmsResourceInPutResponse/migration.md),
[cross-operation responses](members/PutGetPatchResponseSchema/migration.md).
[Gap analysis and decision](gap-analysis.md),
[per-project inventory](instance-correspondence.md#differing-projects),
[controls, provenance and reproduction](evidence-details.md), and
[validation limits](validation.json) retain the supporting detail.

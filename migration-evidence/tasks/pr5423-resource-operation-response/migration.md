# ARM resource operation response migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` consolidates [`PutRequestResponseSchemeArm`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-request-response-scheme-arm.md), [`ConsistentResponseSchemaForPut`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-response-schema-for-put.md), [`XmsResourceInPutResponse`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/xms-resource-in-put-response.md), [`PutGetPatchResponseSchema`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-get-patch-response-schema.md).
**Not functionally equivalent:** it checks registered ARM lifecycle resources, not arbitrary PUT operations
or PUT requests stored outside that lifecycle map by `LegacyOperations`,
and does not independently enforce exact 200/201 Swagger schema equality or emitted resource
extensions. The original staging identity-comparison bug produces false positives for identical
referenced schemas; avoiding that bug does not close the genuine plain-response gap.
Project-grouped counts are assessed below; matching findings on individual operations is not established.

## 2. Actual coverage

All 487 frozen projects were assessed successfully; zero failed or
unassessed projects. Reported diagnostics count individual findings. The assessed grouped unit is
an affected project: count each frozen `sourcePath` once when it has at least one selected finding,
regardless of repeated emissions, diagnostic count or how many Swagger members report there.

| Count                                                      | Swagger linter | TypeSpec linter |
| ---------------------------------------------------------- | -------------- | --------------- |
| Reported diagnostics                                       | 433            | 104             |
| Affected projects (grouped by frozen project `sourcePath`) | 57             | 34              |

These are assessed project counts, not normalized defect counts or a claim that both linters flag
the same operations. Registered-resource scope, source identity, source-to-emission multiplicity
and the staging bug explain identified differences; individual finding correspondence remains
unresolved. See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ).

## 3. Function-level coverage

| Behavior                                                                              | Result                                                                                       |
| ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Registered resource PUT: missing/void request or distinct effective single-body model | Covered; canonical resource identity, not emitted schema equality.                           |
| Standard ARM operation template and model alias                                       | Compliant controls accepted; aliases also have focused candidate tests.                      |
| Internal models and operations                                                        | Skipped by code inspection; no dedicated internal-operation control was run.                 |
| Custom/unregistered PUT operations                                                    | Missing; no independent HTTP-operation scan.                                                 |
| Inherited ARM-like models without registered resource identity                        | Missing; real Network ConnectionMonitorResult is not registered at this source snapshot.     |
| Registered resource PUT using LegacyOperations                                        | Missing request check: legacy decorator stores it in lists, not lifecycle.createOrUpdate.    |
| Multipart PUT request                                                                 | Excluded intentionally; no single effective-payload comparison.                              |
| Registered lifecycle response using another registered resource; list element checks  | Retained identity-based checks; not arbitrary status-by-status Swagger comparison.           |
| 200/201 exact schema equality; plain nonresource response model                       | Missing; a genuine Quota 201 mismatch remains outside this rule's checks.                    |
| Emitted x-ms-azure-resource on arbitrary PUT response                                 | Missing as an independent emitted-extension check; registration is a narrower source policy. |
| Separate model declarations with equal JSON schema                                    | Different semantics; source identity may warn even when emitted structures agree.            |
| Upstream staging object-identity bug                                                  | Not reproduced intentionally; 15 saved findings reference identical raw 200/201 schemas.     |

## 4. Why diagnostic counts differ

- [Assessed project grouping](project-differences.md#assessed-project-grouping): of 487 projects,
  32 have findings from both linters and 428 from neither. Swagger-linter-only
  25 projects; TypeSpec-linter-only 2. Thus 57 Swagger-affected projects and 34 TypeSpec-affected projects are assessed,
  with both one-sided sets retained rather than reducing the difference to a net 23.
  Swagger-higher excess is 333 findings; TypeSpec-higher excess is 4. These opposing gaps must not cancel.
- [Member and source groups](evidence-details.md#member-observation-groups): Swagger linter reports
  PutRequestResponseSchemeArm 212, ConsistentResponseSchemaForPut 16, XmsResourceInPutResponse 155, PutGetPatchResponseSchema 50.
  The shared TypeSpec total cannot be assigned to these members by message text.
- [Registered scope, legacy registration, model identity and repeated emissions](evidence-details.md#registered-scope-and-source-identity)
  explain real ApiManagement and custom AnalyticsItems restrictions. Their entire project totals
  are not asserted to be attributable to those examples.
- [Staging false positives and genuine mismatch](evidence-details.md#staging-identity-bug-and-quota-gap):
  16 Swagger findings map to 16 PUT operations; 15 use identical raw 200/201 schemas and one Quota
  operation uses distinct schemas. The TypeSpec linter does not implement that standalone equality
  test; the genuine nonresource 201 response gap remains.
- [All four TypeSpec-higher excess findings](evidence-details.md#additional-request-policy-and-version-scope)
  are independently explained: three missing-request warnings extend the original comparison policy,
  and one Batch Certificate warning comes from a source operation removed in the selected emitted version.
- [Exact diagnostic inventory](diagnostic-inventory.md) preserves every target, message and
  project count. Where no deterministic operation-level pairing is established, the disposition
  remains **unresolved**, not accepted equivalence or an inferred retirement.

## NOTES

| Swagger linter member                                                                                                                                                         | Findings | Swagger-affected projects | Also shared-TypeSpec-affected | Swagger-only projects | Semantic result          | Evidence                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------------- | ----------------------------- | --------------------- | ------------------------ | ---------------------------------------------------------------------- |
| [`PutRequestResponseSchemeArm`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-request-response-scheme-arm.md)       | 212      | 38                        | 29                            | 9                     | Partial / not equivalent | [member evidence](members/PutRequestResponseSchemeArm/migration.md)    |
| [`ConsistentResponseSchemaForPut`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-response-schema-for-put.md) | 16       | 10                        | 3                             | 7                     | Partial / not equivalent | [member evidence](members/ConsistentResponseSchemaForPut/migration.md) |
| [`XmsResourceInPutResponse`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/xms-resource-in-put-response.md)             | 155      | 14                        | 5                             | 9                     | Partial / not equivalent | [member evidence](members/XmsResourceInPutResponse/migration.md)       |
| [`PutGetPatchResponseSchema`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-get-patch-response-schema.md)           | 50       | 14                        | 8                             | 6                     | Partial / not equivalent | [member evidence](members/PutGetPatchResponseSchema/migration.md)      |

Member project intersections are assessed against the same 34 shared-TypeSpec-affected projects;
they are non-additive and do not assign TypeSpec findings to a Swagger member. Only that
finding-level attribution remains unassessed. [Grouping method and complete project sets](project-differences.md#assessed-project-grouping)
and the reproducible `projectGrouping` field in [summary.json](summary.json) retain the assessment.

`PutGetPatchResponseSchema` is included because current authored documentation maps it and the
existing lifecycle/read/update/list response logic remains in the same rule.
All originals are ARM error-severity registrations; `ConsistentResponseSchemaForPut` is staging-only.
The TypeSpec rule is a warning, registered and enabled in the `all` ruleset.
This run used `configured` mode; default-activation and suppression observations are retained
without treating suppressed/no-finding projects as proof of schema equivalence.

Candidate `2d82a09b6ce2eda8114e54bfd4df6358ec956340`; frozen specs `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`.
The current result replaces stale evidence from the deleted broad listener; historical 388
diagnostics are not current results. Baseline production and staging observations were reused
immutably, not regenerated. [Inputs, validation, limitations and recovery](evidence-details.md)
and [machine-readable summary](summary.json) retain exact identities and counts.
Migration review checkpoints and full regeneration replay were not performed by this
evidence/description-only task; this note does not claim migration acceptance.

[Verified publication and fresh-checkout recovery](receipts/publication-20261104.json) distinguish saved-observation reanalysis from full regeneration, which was not rerun.

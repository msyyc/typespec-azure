# Migration gaps: evidence and decisions

This appendix explains the differences in the [migration report](migration.md).
A **member check** retains the Swagger rule, project, document, route and schema context;
different rules can describe the same underlying issue. Corresponding TypeSpec counts refer
only to the shared rule's warning for the same comparison, not every warning on that operation.

<a id="complete-decision-partition"></a>

## Difference groups

- [Existing policy exceptions](#existing-policy-exceptions): 26 checks; review suppressions/specs, not duplicate rules.
- [Swagger comparison artifacts](#swagger-comparison-artifacts): 34 checks; avoid the identity bug and misleading comparisons.
- [Response-resource policy](#response-resource-policy): 57 checks; missing independent policy.
- [Legacy contracts](#legacy-contracts): 16 checks; targeted contract/modeling investigation.

These are all **133 unpaired Swagger member checks**. The other 144 checks match
observed TypeSpec request warnings. The
[TypeSpec finding inventory](instance-correspondence.md#typespec-finding-accounting)
separately explains all 36 additional or different TypeSpec findings.
[Per-project entries](instance-correspondence.md#differing-projects) retain exact targets,
both engines' counts, source/schema evidence and dispositions; [gap-assessment.json](gap-assessment.json)
retains the finer decisions without adding another report taxonomy.

<a id="1-best-immediate-source-change-registered-resource-operation-set"></a>

## Registered PUT traversal

**Resolved: all 57 previously identified request comparisons now have
corresponding TypeSpec warnings.** This is measured final-source correspondence, not a prediction.

The old singular lifecycle and name-keyed maps lost aliases. The existing append-only
`getArmResourceOperationList` Set retained their createOrUpdate registrations.
The [source fix](https://github.com/Azure/typespec-azure/commit/e45c2bc87e43cd76e4f32ca496985b9b9e8d9d52) enumerates
that Set inside each registered-resource listener, selects noninternal HTTP PUT
createOrUpdate operations and deduplicates Operation targets per resource.
It preserves the request predicate, canonical-resource scope and response traversal.

Of the recovered checks, 38 had been retained under lists and 19 were absent from
the maps. All 104 previous TypeSpec findings remain.
Overall raw warnings changed from 104 to 180;
paired member checks changed from 87 to 144.
These are different units: the additional warnings are not all newly paired Swagger checks.
[Measured delta and exact check IDs](receipts/put-traversal-before-after-20261105.json).

**Gap analysis and decision:** the small traversal repair was justified and is implemented.
Do not broaden to every PUT: action registrations, unregistered contracts and wrong
parent associations still require separate decisions. Focused legacy/overwritten-alias,
compliance, deduplication, exclusion and suppression regressions passed, followed by
the fresh full-population assessment.

**Resolved example:** ApiManagement `ApiContracts.createOrUpdate` accepts
`ApiCreateOrUpdateParameter` and returns canonical `ApiContract`. Before: one Swagger
finding, zero corresponding TypeSpec warnings. After: the same Swagger finding and one
corresponding requestMismatch. The source, selected response and exact warning are in
[the checked example](instance-correspondence.md#code-backed-representatives).

<a id="2-existing-owners-not-new-duplicate-schema-warnings"></a>

## Existing policy exceptions

**Swagger: 54 findings / 26 checks. TypeSpec shared rule: zero corresponding warnings.**
The existing responsible rules diagnose **all 17 distinct target operations before suppression**;
those rules emit zero configured warnings on these targets, each of which explicitly suppresses its responsible rule.
These are verified existing predicates, not observed coverage credited to the shared rule.

| Issue                       | Member checks                                             | Existing rule / evidence                                                                                                                                                                                                                   | Decision                                                                                                 |
| --------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| Empty 200 response          | 9 request + 16 cross-method checks over 16 route contexts | [ARM no-response-body](https://github.com/Azure/typespec-azure/blob/e45c2bc87e43cd76e4f32ca496985b9b9e8d9d52/packages/typespec-azure-resource-manager/src/rules/no-response-body.ts); 16/16 target predicates diagnose it                  | Review the authored exception or fix incorrect response modeling; do not add another empty-body warning. |
| Quota 200/201 bodies differ | 1                                                         | [Azure Core response-schema-problem](https://github.com/Azure/typespec-azure/blob/e45c2bc87e43cd76e4f32ca496985b9b9e8d9d52/packages/typespec-azure-core/src/rules/response-schema-multi-status-code.ts); 1/1 target predicate diagnoses it | Review the legacy success-schema exception with that rule; do not duplicate it in ARM.                   |

Empty-200 targets are Automation DscNodeConfiguration, six EventGrid PATCH operations,
four HDInsight extension PUTs, Marketplace PrivateStore, Network VipSwap,
RecoveryServicesBackup encryption configuration, and SQL DatabaseExtensions GET /
MaintenanceWindows PUT. The [probe results](gap-probes.json) retain each operation key,
predicate result and exact suppression directive/source line.

For Quota, [the source](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/CurrentQuotaLimitBase.tsp#L68-L89)
returns the quota resource at 200 and a submission-status envelope at 201, while its LRO
final result is the quota resource. Initial response consistency and final-result consistency
are different policies; `lro-response-mismatch` is not a substitute for the former.

**Tradeoff:** duplicate diagnostics would bypass deliberately suppressed policies rather
than supply missing logic. Review whether the exception is justified; do not invent response
bodies or unify models contrary to the wire contract. The body rule's general first-response/
template limitations still exist, but did not prevent its predicate from detecting these
16 exact cases.

<a id="3-swagger-findings-that-should-not-be-copied-literally"></a>

## Swagger comparison artifacts

**Swagger: 34 findings / 34 checks. TypeSpec: zero corresponding warnings.**

| Cause                                        | Checks | Evidence and decision                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Object-identity bug                          | 15     | The [staging implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/consistent-response-schema-for-put.ts) compares resolved objects with `!==` despite identical 200/201 references in the same document. Confirmed false positives; do not reproduce the bug. |
| No-content response compared to a schema     | 15     | Eleven selected bodyless 202 responses and four bodyless PATCH 204 responses are not different resource models. Recommend excluding these schema comparisons.                                                                                                                                                                                                    |
| Collection wrapper compared to an item/array | 4      | Exact emitted definition pointers prove the same item model in each case below. Recommend comparing resource items, not wrapper-reference names.                                                                                                                                                                                                                 |

The identity-bug classification uses saved references and pinned implementation, not a
newly captured resolver-object execution trace. Correct no-content semantics does not
certify the status set: a 202-only PUT can still violate the separate
[arm-put-response-codes](https://github.com/Azure/typespec-azure/blob/e45c2bc87e43cd76e4f32ca496985b9b9e8d9d52/packages/typespec-azure-resource-manager/src/rules/arm-put-response-codes.ts)
policy.

| Operation family                | Compared roles                 | Verified common item  |
| ------------------------------- | ------------------------------ | --------------------- |
| ApplicationInsights Annotations | PUT array / GET list envelope  | Annotation            |
| OperationalInsights QueryPacks  | PUT entity / GET list envelope | LogAnalyticsQueryPack |
| SQL FirewallRules               | PUT entity / GET list envelope | FirewallRule          |
| Web AppServicePlans VnetRoute   | PUT/PATCH entity / GET array   | VnetRoute             |

`collectionEvidence` in [gap-probes.json](gap-probes.json) retains the exact documents,
definition pointers and item excerpts. These are shape-role differences, not proof of
different resource items. **The 19 no-content/collection exclusions are recommendations,
not approved policy retirements or proof that the entire API design is compliant.**
Porting them literally adds misleading warnings and conflicts with existing response/list
semantics; a general raw-reference comparator is not recommended.

<a id="4-resource-extension-genuine-absent-policy-not-57-automatically-proven-defects"></a>

## Response-resource policy

**Swagger: 155 findings / 57 checks. TypeSpec: zero corresponding warnings.**

All selected response hierarchies lack `x-ms-azure-resource`, and all corresponding source
payloads are unregistered according to `getArmResource`. The current registered-resource
listener therefore cannot enforce this independent policy.

The cases mix resource-looking entities, such as Network connections and GuestConfiguration
assignments, with access-policy payloads, secrets, settings dictionaries, arrays and an unknown
payload. The check is genuinely absent, but **not all 57 cases are proven resource-definition
defects or false positives**; custom/action boundaries remain unresolved.

[Autorest emission](https://github.com/Azure/typespec-azure/blob/e45c2bc87e43cd76e4f32ca496985b9b9e8d9d52/packages/typespec-autorest/src/openapi.ts#L2249-L2275)
uses `isAzureResource` state or custom-resource options, then copies explicit extensions
which can override the marker. That state is not canonical `getArmResource` registration;
the Swagger rule also follows `allOf` and external references.

**Decision:** design a focused source-level response-resource check separately, with ARM
scope, selected-success-body behavior and explicit custom/action boundaries. Test inherited
markers, custom-resource options, extension overrides and common references. Medium complexity
is justified by the missing policy, but neither a registered-resource-only check nor an
unconditional every-PUT check solves it safely. Do not mark every DTO as a resource or add
recursive emitted-JSON equality. This gap must be addressed or explicitly narrowed before
claiming complete migration.

<a id="5-remaining-contracts-modelspec-work-before-a-global-matcher"></a>

## Legacy contracts

**Swagger: 46 findings / 16 checks. TypeSpec: zero corresponding warnings.**

The 15 request-contract checks need modeling/contract investigation:

| Checks | Cases                                                                                               | What must be established                                                                                                                                                                    |
| ------ | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 4      | Cosmos DB DatabaseAccounts/NotebookWorkspaces; SecurityInsights Actions/ThreatIntelligenceIndicator | Low-level/custom creation templates or differing resource arguments lack the required association. Use correct registration/standard templates only if emitted contracts remain unchanged.  |
| 5      | ExportConfiguration, TestJob, SyncJob, ConnectionMonitor, PacketCapture                             | Request/result DTOs differ in read-only fields, envelopes or required properties. Establish visibility and actual contract before a modeling repair. These are five checks, not 35 defects. |
| 4      | Annotations_Create, FirewallRules_Replace, WebApps_MigrateStorage, GatewayApi_CreateOrUpdate        | Bulk/collection or command inputs are not automatically ordinary resource replacement. Confirm intent instead of comparing every PUT to a parent model.                                     |
| 2      | ApiManagement PrivateEndpointConnection; RecoveryServices certificate                               | The legacy resource argument is a service/Vault parent, while the actual response is a child model. Existing parent-model warnings are not equivalent child-response checks.                |

The cross-method check is Automation SyncJob.
[PUT](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/models.tsp#L5945-L6011)
includes read-only name/type/id;
[GET](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/models.tsp#L6016-L6078)
has writable id, omits name/type and adds nested `exception`. This is a genuine shape
difference, not merely differently named aliases.

**Decision:** confirm these contracts with spec/service owners and prefer targeted modeling
fixes where wire-equivalent. If summary/detail responses are intentional, do not falsify
the spec to make them equal. A general structural matcher must handle visibility, aliases,
inheritance, unions, cycles, versions and collection roles; the current evidence does not
justify that complexity or its likely noise. These cases remain unresolved, not accepted
as equivalent.

## Evidence, boundaries and reproduction

[gap-assessment.json](gap-assessment.json) assigns every one of the 277 member checks a
decision without manufacturing correspondence credit. [gap-probes.json](gap-probes.json)
and [current execution receipt](receipts/gap-tradeoffs-20261105.json) retain the final-source
registration/owner-predicate inspection. Saved diagnostics reproduced exactly; no
suppression was removed and no Swagger was emitted.

The full final-source run is described in
[evidence-details.md](evidence-details.md#final-source-execution-and-recovery).
The older [tradeoff receipt](receipts/gap-tradeoffs-20261104.json) is historical evidence
for the pre-fix recommendation, not current warning counts.

From this task directory:

```text
python assess-gaps.py --verify
python analyze-instances.py --root .
python render-instances.py --verify
python -B -m unittest test_instance_analysis.py test_reanalyze.py
python reanalyze.py --verify-inventory
```

`analysis/collect-gap-probes.py` reconstructs probes with `--root`, `--traces`, `--plan`,
`--specs` and `--dataset`. The metadata runner requires the current `--native-run`
and an explicit `--node ABSOLUTE_PINNED_NODE`; its
`--projects PROJECTS_JSON` option is for explicitly recorded bounded investigations.
Saved-data reconstruction is not a new linter execution or full corpus regeneration.

# Gap decisions: value, ownership and implementation cost

The earlier report established correspondence but overreached by labeling almost every
unpaired check "rule update required." That was not a useful implementation recommendation.
**Keep the measured correspondence unchanged; fix worthwhile native gaps, not every literal
Swagger predicate.** No production code, spec, suppression or mapping acceptance changed in
this assessment.

## Complete decision partition

The units below are **member checks**, not distinct defects or predicted new diagnostics.
Every one of the 277 checks / 433 raw observations has exactly one decision in
[gap-assessment.json](gap-assessment.json). Different members on the same operation remain
separate. [Per-instance pages](instance-correspondence.md#differing-projects) contain the
request, response, source operation, existing diagnostic and specific disposition.

| Decision                                           | Member checks | Raw observations | Recommendation / cost                                                                                   |
| -------------------------------------------------- | ------------- | ---------------- | ------------------------------------------------------------------------------------------------------- |
| Already corroborated request comparison            | 87            | 87               | Keep existing behavior and controls.                                                                    |
| Recoverable registered PUT traversal gap           | 57            | 57               | **P1: small native change**, using the existing append-only operation Set.                              |
| Custom lifecycle registration/modeling gap         | 4             | 4                | P2: inspect custom templates/resource arguments; spec fixes must preserve emitted contracts.            |
| Confirmed upstream object-identity false positives | 15            | 15               | Do not port the bug.                                                                                    |
| Quota success-schema difference                    | 1             | 1                | Existing Azure Core owner, explicitly suppressed; do not duplicate in ARM.                              |
| Independent response-resource policy absent        | 57            | 155              | P2: focused rule/design, medium complexity; determine custom/action policy before enforcement.          |
| Empty 200 response body                            | 25            | 53               | Existing body owner, explicitly suppressed; **16 distinct project/routes**, not 25 independent defects. |
| Correctly bodyless 202/204 compared to a schema    | 15            | 15               | Recommend not porting this misleading schema comparison.                                                |
| Collection/entity/array wrapper role comparison    | 4             | 4                | Same item definition verified; recommend not porting raw wrapper-reference equality.                    |
| Bulk/collection request contracts                  | 2             | 2                | Confirm API intent; do not assume ordinary resource replacement.                                        |
| Action-like PUT contracts                          | 2             | 2                | Confirm API intent/exceptions; do not compare command input to a parent resource.                       |
| Unregistered body-bearing entity DTOs              | 5             | 35               | P2: contract/visibility/modeling review; no generic recursive Swagger comparator.                       |
| Parent canonical argument versus child response    | 2             | 2                | P2: template/spec modeling review before new warnings.                                                  |
| Genuine cross-method SyncJob shape difference      | 1             | 1                | P3: spec-owner follow-up; defer a broad structural matcher for one observed route.                      |
| **Total**                                          | **277**       | **433**          | Recommendations do not add current migration credit.                                                    |

Thus the former **175 unpaired checks + 15 upstream false positives are not 190 worthwhile
missing defects**. Fifteen are confirmed upstream identity bugs; another 19 are schema
comparison overreach for no-content/collection roles. The latter are recommendations for
intentional differences, **not approved retirements** or proof that the whole API is compliant.
The response-resource policy remains genuinely unimplemented; uncertain legacy contracts
are not relabeled false positives to improve a percentage.

## 1. Best immediate source change: registered-resource operation Set

The current request branch reads only `lifecycle.createOrUpdate` from the retained map.
However, [operations.ts](https://github.com/Azure/typespec-azure/blob/2d82a09b6ce2eda8114e54bfd4df6358ec956340/packages/typespec-azure-resource-manager/src/operations.ts#L187-L280)
already maintains `getArmResourceOperationList`, an append-only Set of operation identifiers.
[Legacy registration](https://github.com/Azure/typespec-azure/blob/2d82a09b6ce2eda8114e54bfd4df6358ec956340/packages/typespec-azure-resource-manager/src/private.decorators.ts#L920-L975)
also adds identifiers there. An overwritten singular lifecycle slot or name-keyed list entry
therefore does not necessarily require a new compiler registry or a broad PUT listener.

**Measured bounded investigation:** 14 projects, covering the 39 list-map and 23 absent-map
request checks. All saved candidate diagnostics were reproduced unchanged; no HTTP metadata
diagnostic occurred. The existing Set retains 58 of those 62 operations:

- **57** are genuine `createOrUpdate` PUT identifiers with a different effective single request
  and the canonical resource as the original selected success response: **38 list-map + 19 absent-map**.
  Their source and selected-version request/response metadata agree.
- **One** is ApiManagement `GatewayApi_CreateOrUpdate`: an `action`, with AssociationContract
  input, ApiContract output and GatewayContract parent. The source also suppresses the current
  ARM rule. Including every PUT identifier would compare the wrong contract.
- **Four** are not in any registered resource's Set: Cosmos DB DatabaseAccounts and
  NotebookWorkspaces use low-level `Foundations.ArmCreateOperation`; SecurityInsights Actions
  uses a custom creation operation, while ThreatIntelligenceIndicator creation supplies a
  different request-model template argument from its registered response resource.
  These need registration/modeling review, not a claim that the Set fixes all 62.

**Recommendation:** retain the reviewer-approved registered-model listener; enumerate that
resource's identifiers, filter `kind === "createOrUpdate"` and HTTP PUT, and reuse the existing
request helper. Deduplicate Operation targets. Do not redesign registration or silently include
actions, arbitrary PUTs or unregistered DTOs.

**Why worth doing:** 57 of the 81 unpaired request comparisons have a concrete low-complexity
path to the current semantic predicate, with no global operation scan. These are **eligible
comparisons, not 57 measured additional warnings**: production implementation, suppression
handling and final-candidate validation are still required. The current observed credit
remains 87/168, not a prospective 144/168.

**Focused implementation/test plan:** change the request traversal in
`arm-resource-operation-response.ts`; preserve response traversal unless separately justified.
Add controls for legacy/list registration, two aliases overwriting a lifecycle slot, compliant
canonical payloads, action PUT exclusion, non-PUT identifiers, multipart/internal exclusions,
deduplication and authored suppression. Run the existing narrow ARM rule tests/lint/typecheck,
then validate the changed candidate against the pinned corpus before claiming any gain.

## 2. Existing owners, not new duplicate schema warnings

### Empty 200 responses: 25 checks over 16 route contexts

Nine request-rule checks and 16 cross-method checks describe the same 16 route contexts:
Automation DscNodeConfiguration; six EventGrid PATCH operations; four HDInsight extension
PUTs; Marketplace PrivateStore; Network VipSwap; RecoveryServicesBackup encryption config;
SQL DatabaseExtensions GET and MaintenanceWindows PUT.

These are real response-body policy concerns, but there are not two unequal body models to
compare when a selected 200 has no body.
[ARM no-response-body](https://github.com/Azure/typespec-azure/blob/2d82a09b6ce2eda8114e54bfd4df6358ec956340/packages/typespec-azure-resource-manager/src/rules/no-response-body.ts)
is the appropriate existing owner. Its general implementation checks the first response
other than 202/204 and skips template operations; do not assume universal coverage from its name.

Here, we tested the **actual installed owner visitor on all 16 exact operations** with a
collector context before suppression: **16/16 produce its missing-body diagnostic**.
The unchanged configured programs produce **0/16**, and each operation has an explicit nearby
authored `#suppress ".../no-response-body"`. The saved directive, source line and operation key
are in [gap-probes.json](gap-probes.json). No suppression was removed and no diagnostics were
injected into the program.

**Recommendation:** review the legacy-contract exception/suppression with that owner, or fix
the spec if its modeled response is wrong. Do not invent a response body that the service does
not return. A new ARM schema-equality diagnostic would largely bypass an already deliberate
suppression, create noise and duplicate ownership, rather than close an absent lint predicate.
This is **verified predicate ownership, not observed corpus coverage**.

### Quota: one genuine difference, already detected by Azure Core

Quota has a resource body at 200 and a submission-status envelope at 201. This is genuinely
different schema content, not the staging rule's identity bug. But
[Azure Core response-schema-problem](https://github.com/Azure/typespec-azure/blob/2d82a09b6ce2eda8114e54bfd4df6358ec956340/packages/typespec-azure-core/src/rules/response-schema-multi-status-code.ts)
already compares effective non-error success payload identities, including plain models.

The installed visitor diagnoses the exact Quota operation before suppression (**1/1**);
configured output is **0/1**. The pinned
[operation source](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/CurrentQuotaLimitBase.tsp#L68-L89)
explicitly suppresses that owner. It also sets `FinalResult = CurrentQuotaLimitBase`.
The 201 acceptance envelope and final LRO resource are distinct concepts; the separate
`lro-response-mismatch` rule checks the latter, not literal initial-envelope equality.

**Recommendation:** use the existing Azure Core owner and review whether this documented
legacy submission response warrants its exception. Do not add a duplicate ARM check merely
to make the consolidated rule emit a warning. A one-to-many migration mapping may cite this
owner after its policy and suppression semantics are accepted; this report gives it no new
correspondence credit.

The owner experiment covered eight projects and 17 target checks, using unchanged candidate,
core and specs. **All 17 predicate findings have explicit authored suppressions; all 17
configured target counts remain zero.** This distinction materially changes the recommendation
from "missing implementation" to "existing policy/exception review."

## 3. Swagger findings that should not be copied literally

**15 confirmed staging identity false positives:** 200/201 reference the same schema in the
same document; upstream uses `!==` on resolved JavaScript objects. Retain the saved raw
references and pinned code evidence. Do not reproduce that implementation bug.

**15 no-content cross-method comparisons:** 11 involve selected bodyless 202 responses and
four involve bodyless PATCH 204. A missing schema on those statuses is expected by
`no-response-body`, not a different resource schema. Reject the schema-comparison false
positive, but separately check status policy: a 202-only PUT can still violate
[arm-put-response-codes](https://github.com/Azure/typespec-azure/blob/2d82a09b6ce2eda8114e54bfd4df6358ec956340/packages/typespec-azure-resource-manager/src/rules/arm-put-response-codes.ts).
Correct no-content semantics does not certify the operation's full ARM contract.

**Four collection comparisons:** saved Swagger was resolved to exact definition pointers,
not normalized names. Each compared payload ultimately uses the **same item definition**:

| Route/operation family          | Compared roles                 | Same item             |
| ------------------------------- | ------------------------------ | --------------------- |
| ApplicationInsights Annotations | PUT array / GET list envelope  | Annotation            |
| OperationalInsights QueryPacks  | PUT entity / GET list envelope | LogAnalyticsQueryPack |
| SQL FirewallRules               | PUT entity / GET list envelope | FirewallRule          |
| Web AppServicePlans VnetRoute   | PUT/PATCH entity / GET array   | VnetRoute             |

The exact documents, pointers and `items` excerpts are retained as `collectionEvidence` in
[gap-probes.json](gap-probes.json). Raw wrapper-reference equality overreports these role
differences. Existing `list-response-envelope` addresses list structure; do not claim that its
source ownership is freshly measured coverage here. This conclusion is about the misleading
schema comparison, not approval of every method/route design.

**Tradeoff:** reproducing these 19 comparisons adds misleading warnings and conflicts with
no-content/list semantics. Recommend documenting intentional narrower behavior rather than
adding code. Approval of that policy and any migration retirement remains outstanding.

## 4. Resource extension: genuine absent policy, not 57 automatically proven defects

All **57 selected response hierarchies** lack `x-ms-azure-resource`; every corresponding
source payload is unregistered according to `getArmResource`. Therefore this canonical
registered-resource listener cannot independently implement the original marker check.
It is a real policy gap, not made equivalent by an unrelated request warning.

However, this population mixes resource-looking entities (for example Network connections
and GuestConfiguration assignments) with access-policy payloads, secrets, settings
dictionaries, arrays and an unknown payload. **Do not mark all 57 false positives, or call
all 57 confirmed malformed resource definitions, without settling that boundary.**

[Autorest emission](https://github.com/Azure/typespec-azure/blob/2d82a09b6ce2eda8114e54bfd4df6358ec956340/packages/typespec-autorest/src/openapi.ts#L2249-L2275)
uses `isAzureResource` state or custom-resource options, then copies explicit OpenAPI
extensions, which can override the marker. `isAzureResource` reads dedicated decorator
state; it is not synonymous with canonical `getArmResource` registration. The Swagger
rule also follows `allOf` and external references.

**Recommendation:** medium-complexity, separate focused source-level response-resource
policy/design, not recursive emitted-JSON equality or a change that marks every custom DTO
as an ARM resource. Establish ARM service scope, selected 200/201 body semantics, custom/
action exceptions, inherited markers, custom-resource options, explicit extension overrides
and common external references. Reuse an existing owning decorator diagnostic only where
its actual predicate proves the same condition; `use-operation-decorator` alone does not.

**Benefit/risk:** 57 checked PUTs / 155 repeated raw findings are the investigation population,
not a validated future gain. A registered-resource-only check would miss this entire
population; an unconditional every-PUT check risks warning on intentionally nonresource
commands. This policy must be addressed or explicitly narrowed before claiming complete
four-member migration, but it should not be bolted onto this PR without focused semantics,
tests and fresh final-candidate evidence.

## 5. Remaining contracts: model/spec work before a global matcher

The request-rule's remaining **15 non-body contract checks** split exactly as follows:

- **Four registration/modeling cases:** Cosmos DB DatabaseAccounts/NotebookWorkspaces and
  SecurityInsights Actions/ThreatIntelligenceIndicator, described above. Prefer explicit
  correct registration or standard templates if wire-equivalent; do not register a request
  DTO as the response resource to silence a diagnostic.
- **Five unregistered body-bearing DTO pairs:** ApplicationInsights ExportConfiguration,
  Automation TestJob/SourceControlSyncJob, Network ConnectionMonitor/PacketCapture. There
  are five checked PUTs, not 35 separate defects. Result models add read-only fields; inputs
  and results also differ in envelope/required-property shape. These need contract,
  visibility and registration investigation, not inferred equivalence from similar names.
- **Four collection/command contracts:** Annotations_Create, FirewallRules_Replace,
  WebApps_MigrateStorage and GatewayApi_CreateOrUpdate. Item/list request roles or command
  inputs differ from ordinary single-resource replacement. Spec-owner intent matters;
  neither "definitely valid" nor "blindly compare to parent" is justified.
- **Two parent/child comparisons:** ApiManagement PrivateEndpointConnection uses a service
  resource argument but a child response; RecoveryServices certificate uses Vault but returns
  VaultCertificateResponse. Review the template/custom child operation rather than count
  the existing parent-model warning as the original child-response comparison.

The other **nine** of the original 81 unpaired request checks are empty-200 body-owner cases
already analyzed above. This partitions all 81: **57 + 15 + 9**, without inventing extra defects.
For unregistered cases, prefer targeted modeling fixes where the actual API contract permits.
A general matcher must handle visibility, read-only/write-only fields, aliases, inheritance,
unions, cycles, API versions and collection roles; its noise/maintenance cost is not justified
merely by the raw diagnostic total.

The **one genuine non-body cross-method case** is Automation SourceControlSyncJob:
[PUT model](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/models.tsp#L5945-L6011)
includes read-only name/type/id, whereas
[GET model](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/models.tsp#L6016-L6078)
has writable id, omits name/type and adds nested `exception`.
It is a real shape difference, not only different `$ref` names. Ask the spec/service owner
whether the contract should be unified; if summary versus detail is intentional, do not
falsify the spec to obtain equality. Retain this known migration gap and defer a broad
cross-operation structural matcher for one observed route.

## Evidence, boundaries and reproduction

[Execution receipt](receipts/gap-tradeoffs-20261104.json) records the bounded questions,
budgets, project sets, timings, raw trace hashes and unchanged-diagnostic checks.
The 14-project Set experiment and eight-project owner experiment are **metadata/predicate
inspections**, not another 487-project corpus or a new candidate. The original 433 Swagger /
104 selected ARM diagnostics, all 277 correspondence groups and all 104 native finding
dispositions remain unchanged. Other owners' pre-suppression predicates receive no observed
coverage credit.

PR head advanced during publication to `a4b87e3c8155f330b715c738c09e051087893fd7` by merging
main. The [head comparison](receipts/publication-head-comparison.json) shows only a separate
LRO polling rule and its registration/tests/docs changed; the assessed semantic source and
dependency manifests did not. The corpus and bounded probes remain pinned to `2d82a09`,
not presented as a fresh run of that later merge.

Saved-data checks, from this task directory:

```text
python assess-gaps.py --verify
python analyze-instances.py --root .
python render-instances.py --verify
python -m unittest test_instance_analysis.py test_reanalyze.py
python reanalyze.py --verify-inventory
```

`assess-gaps.py` applies the explicit policy overlay; it does not guess equivalent schemas.
`analysis/collect-gap-probes.py` reconstructs compact probes from the two recorded run
directories and pinned specs/dataset using `--root`, `--runs`, `--specs` and `--dataset`.
`analysis/run-instance-inspection.py --projects PROJECTS_JSON` supports each recorded
bounded selection; its other required runtime arguments are unchanged.
Fresh execution requires the pinned artifacts/runtime described in
[evidence-details.md](evidence-details.md#read-recount-and-regenerate).

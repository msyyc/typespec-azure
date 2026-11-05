# Supporting evidence and recovery

## Assessment boundary

Final assessed candidate: `e45c2bc87e43cd76e4f32ca496985b9b9e8d9d52`. Core: `a43d2ca6f2ddd4c1a1d05f2e63cd4c8a40a71b76`.
Tooling: `8345f684fad330568e55e40181c3d17cd8d8db7f`. Frozen specs: `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`.
The production fix is [PR #5423](https://github.com/Azure/typespec-azure/pull/5423);
this evidence measures its registered-PUT traversal, not complete migration acceptance.
Independent migration-review checkpoints remain outside this targeted fix.

TypeSpec uses configured source compilation with authored suppressions and explicit
mapped-rule enablement. Default activation is assessed separately. Swagger represents
the frozen producer's latest emitted version, without production readme suppressions.
Source and selected-version populations are not universally aligned, and source model
identity is not general emitted-schema structural equality.

Reported findings: Swagger **433**; TypeSpec configured raw **180**,
source-aligned **180**, default **180**.
TypeSpec severity is warning; the original Swagger registrations are ARM errors.
`ConsistentResponseSchemaForPut` is explicitly evaluated through the immutable staging
supplement, not treated as an absent production zero.

## Final-source execution and recovery

The checkpoint began `2026-11-05T05:42:42.437Z` and completed `2026-11-05T07:50:58.316Z`.
All **487 projects** succeeded; none was failed, omitted or unassessed. Selection was
the complete frozen population, no filter/limit, concurrency two. Swagger was neither
regenerated nor revalidated.

The original CLI abruptly terminated with exit255 after 136 successful workers.
There was no analyzer error or matching application crash event; the cause remains
**unknown**. Its original manifest and logs were preserved unchanged. A separate recovery
retained those same-final-source receipts byte-for-byte and ran the remaining 351 with
the unchanged official worker and exact source/artifacts/compiler/specs/configuration.
This is a **recovered full population**, not a clean original CLI exit.

An initial recovery was rejected when finalization detected unpinned Node26.13
instead of Node26.5. None of its 351 resumed receipts was accepted. The correction
reran those projects and all 17 selected controls with the verified absolute Node26.5
executable; metadata inspection used that same executable.
[Rejected attempt](receipts/runtime-drift-rejection-20261105.json) and its logs remain
in the native asset. These are preparation/recovery failures, not zero-finding projects.

Every one of the 93,496 copied dataset files passed post-execution SHA-256 verification;
source/core/specs/tooling snapshots, all 15 artifact hashes, worker/generator hashes
and original/copied staging identities were rechecked. The official exported
`buildNativeCoverageReport` enforced complete unique project membership and produced
the numerical coverage report. Completion did not merely relabel the interrupted manifest.

[Run manifest](runs/20261105-e45c2bc87/manifest.json),
[coverage](runs/20261105-e45c2bc87/coverage.json),
[interrupted manifest](receipts/interrupted-manifest-20261105.json),
[recovery](receipts/recovery-20261105.json),
[worker completion](receipts/worker-completion-20261105.json),
[dataset verification](receipts/dataset-post-verification-20261105.json), and
[post-run artifact attestation](receipts/post-run-attestation-20261105.json).

## Member observation groups

| Swagger linter                                                                          | Profile              | Raw findings | Member checks | Same-comparison TypeSpec warnings |
| --------------------------------------------------------------------------------------- | -------------------- | ------------ | ------------- | --------------------------------- |
| [`PutRequestResponseSchemeArm`](members/PutRequestResponseSchemeArm/migration.md)       | Production ARM       | 212          | 168           | 144                               |
| [`ConsistentResponseSchemaForPut`](members/ConsistentResponseSchemaForPut/migration.md) | ARM staging Spectral | 16           | 16            | 0                                 |
| [`XmsResourceInPutResponse`](members/XmsResourceInPutResponse/migration.md)             | Production ARM       | 155          | 57            | 0                                 |
| [`PutGetPatchResponseSchema`](members/PutGetPatchResponseSchema/migration.md)           | Production ARM       | 50           | 36            | 0                                 |

All four upstream rule/document links were verified at
`6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f`
([receipt](receipts/verified-upstream-links.json)). `PutGetPatchResponseSchema` remains
admitted because of the documented retained response checks, not because a request
warning on its route implements cross-method equality.

## Exact correspondence and accounting

All 433 Swagger observations resolve uniquely to 277 member checks. **144** checks
have corresponding TypeSpec warnings; **133** remain unpaired.
All **36** additional/different TypeSpec findings retain separate dispositions.
Grouping preserves `(member, project, resolved document, exact route, schema context)`;
different members and schema comparisons at one location are never deduplicated.

The current metadata-only inspection recompiled the **63-project**
union affected by either engine, concurrency two. Every saved warning reproduced
byte-for-field, with zero HTTP metadata diagnostics. All exact source/selected-version
method/route candidates and native targets remain in the compact evidence; complete
graphs, registry and owner-predicate traces are retained in the native asset.
[Inspection receipt](receipts/instance-inspection-20261105.json),
[compact input](instance-inputs.json), [Swagger bindings](swagger-bindings.json),
[TypeSpec-to-Swagger bindings](native-swagger-bindings.json), and
[assessment](instance-mapping.json).

A match requires the relevant requestMismatch, exact operation, canonical resource
and the same selected response comparison, with source/selected payload metadata
agreement. Route/name/message co-occurrence alone receives no credit.
The unchanged comparison helper/core closures and all old/new packed JavaScript
payloads were independently compared
([artifact comparison](receipts/artifact-before-after-20261105.json)).
Besides this rule, changes comprise an unrelated LRO rule and its registration/default
ruleset wiring; they do not supply coverage for this mapping.

[Per-project target evidence](instance-correspondence.md#differing-projects),
[directional counts](project-differences.md), [raw inventory](diagnostic-inventory.md),
[decisions](gap-analysis.md), and
[measured before/after delta](receipts/put-traversal-before-after-20261105.json).
Neither source location summaries nor project overlap are functional coverage percentages.

## Registered scope and source identity

[Current implementation](https://github.com/Azure/typespec-azure/blob/e45c2bc87e43cd76e4f32ca496985b9b9e8d9d52/packages/typespec-azure-resource-manager/src/rules/arm-resource-operation-response.ts)
enumerates each registered resource's operation Set for noninternal createOrUpdate PUT
requests, deduplicated per resource/Operation. Missing/void requests are additional
body-existence policy; single bodies use effective request visibility/model identity;
multipart and other operation kinds/verbs remain excluded.
Existing lifecycle/list response traversal is unchanged and narrower than general
plain-model, cross-method or 200/201 equality. Its single Model-wrapper limitation
remains demonstrated by the retained unsuccessful control; passing union controls do
not certify that wrapper case.

Network's unregistered inherited ConnectionMonitorResult and custom/parent associations
remain contract/modeling questions, not justification for a global PUT listener.
The separate Swagger bindings preserve original fallback attribution while locating
the actual referenced document; the sealed baseline was not repaired.
The response marker uses emitter `isAzureResource`/custom options/explicit extensions,
not canonical `getArmResource` registration. Existing-owner predicates diagnose the
16 empty-200 operations and Quota before their authored suppressions; configured
warnings from those owners remain zero on these targets.
[Exact causes and source/schema examples](gap-analysis.md).

## Exact source examples

These verbatim excerpts use the unchanged frozen source. The registered-request
examples below are now resolved by the measured fix, not outstanding recommendations.
Current outcomes and emitted schemas are in
[code-backed representatives](instance-correspondence.md#code-backed-representatives).

### registered-request-override

[Exact source](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/ApiContract.tsp).
Lines 19-27:

```typespec
@parentResource(ApiManagementServiceResource)
model ApiContract is Azure.ResourceManager.ProxyResource<ApiContractProperties> {
  ...ResourceNameParameter<
    Resource = ApiContract,
    KeyName = "apiId",
    SegmentName = "apis",
    NamePattern = "^[^*#&+:<>?]+$"
  >;
}
```

Lines 90-106:

```typespec
  /**
   * Creates new or updates existing specified API of the API Management service instance.
   */
  createOrUpdate is ApiContractOps.CreateOrUpdateAsync<
    ApiContract,
    Request = ApiCreateOrUpdateParameter,
    Parameters = {
      /**
       * ETag of the Entity. Not required when creating an entity, but required when updating an entity.
       */
      #suppress "@azure-tools/typespec-azure-core/casing-style" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
      @header("If-Match")
      `If-Match`?: string;
    },
    Response =
      | (ArmResponse<ApiContract> &
          ArmCombinedLroHeaders<FinalResult = ApiContract> & {
```

Lines 392-405:

```typespec
  /**
   * Creates new or updates existing specified API of the workspace in an API Management service instance.
   */
  createOrUpdate is WorkspaceApiOps.CreateOrUpdateAsync<
    ApiContract,
    Request = ApiCreateOrUpdateParameter,
    Parameters = {
      /**
       * ETag of the Entity. Not required when creating an entity, but required when updating an entity.
       */
      #suppress "@azure-tools/typespec-azure-core/casing-style" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
      @header("If-Match")
      `If-Match`?: string;
    },
```

### custom-unregistered-nonresource-response

[Exact source](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/AnalyticsItems/routes.tsp).
Lines 13-15:

```typespec
#suppress "@azure-tools/typespec-azure-resource-manager/arm-resource-interface-requires-decorator" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
interface AnalyticsItemsOperationGroup {
  /**
```

Lines 90-123:

```typespec
  /**
   * Adds or Updates a specific Analytics Item within an Application Insights component.
   */
  @route("/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}/item")
  @put
  put(
    ...ApiVersionParameter,
    ...SubscriptionIdParameter,
    ...ResourceGroupParameter,

    /**
     * The name of the Application Insights component resource.
     */
    @path
    resourceName: string,

    /**
     * Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
     */
    @path
    scopePath: ItemScopePath,

    /**
     * Flag indicating whether or not to force save an item. This allows overriding an item if it already exists.
     */
    @query("overrideItem")
    overrideItem?: boolean,

    /**
     * Properties that need to be specified to create a new item and add it to an Application Insights component.
     */
    @body
    itemProperties: ApplicationInsightsComponentAnalyticsItem,
  ): ArmResponse<ApplicationInsightsComponentAnalyticsItem>;
```

### exact-200-201-plain-response-gap

[Exact source](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/CurrentQuotaLimitBase.tsp).
Lines 39-41:

```typespec
#suppress "@azure-tools/typespec-azure-resource-manager/no-resource-delete-operation" ""
@armResourceOperations(#{ omitTags: true })
interface CurrentQuotaLimitBases {}
```

Lines 68-82:

```typespec
  #suppress "@azure-tools/typespec-azure-core/response-schema-problem" ""
  @tag("QuotaInformation")
  @Azure.Core.useFinalStateVia("original-uri")
  createOrUpdate is ArmResourceCreateOrReplaceAsync<
    CurrentQuotaLimitBase,
    QuotaPutBaseParam,
    Response =
      | ArmResourceUpdatedResponse<CurrentQuotaLimitBase>
      | ArmCreatedResponse<
          QuotaRequestSubmitResponse201,
          ExtraHeaders = ArmLroLocationHeader<FinalResult = CurrentQuotaLimitBase> &
            Azure.Core.Foundations.RetryAfterHeader
        >,
    Error = ExceptionResponse
  >;
```

### identical-external-schema-staging-false-positive

[Exact source](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/durabletask/resource-manager/Microsoft.DurableTask/DurableTask/scheduler.tsp).
Lines 12-16:

```typespec
model SchedulerPrivateLinkResource is PrivateLink;
alias PrivateLinkOperations = PrivateLinks<SchedulerPrivateLinkResource>;

model PrivateEndpointConnection is PrivateEndpointConnectionResource;
alias PrivateEndpointOperations = PrivateEndpoints<PrivateEndpointConnection>;
```

Lines 178-184:

```typespec
  @added(Versions.v2026_02_01)
  @doc("Get a private endpoint connection for the durable task scheduler")
  getPrivateEndpointConnection is PrivateEndpointOperations.Read<Scheduler>;
  @added(Versions.v2026_02_01)
  @doc("Create or update a private endpoint connection for the durable task scheduler")
  createOrUpdatePrivateEndpointConnection is PrivateEndpointOperations.CreateOrUpdateAsync<Scheduler>;
  @added(Versions.v2026_02_01)
```

### unregistered-inherited-network-resource

[Exact source](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/network/resource-manager/Microsoft.Network/Network/Network/ConnectionMonitorResult.tsp).
Lines 23-29:

```typespec
@Azure.ResourceManager.Legacy.feature(Features.networkWatcher)
@Http.Private.includeInapplicableMetadataInPayload(false)
@parentResource(NetworkWatcher)
model ConnectionMonitorResult extends TrackedResourceWithEtag {}
```

Lines 51-67:

```typespec

  /**
   * Create or update a connection monitor.
   */
  @tag("ConnectionMonitors")
  createOrUpdate is Azure.ResourceManager.Legacy.CreateOrUpdateAsync<
    ConnectionMonitorResult,
    Request = ConnectionMonitor,
    Parameters = {
      /**
       * Value indicating whether connection monitor V1 should be migrated to V2 format.
       */
      @query("migrate")
      migrate?: string;
    },
    Error = ErrorResponse
  >;
```

### additional-missing-request-policy

[Exact source](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/dns/resource-manager/Microsoft.Network/Dns/DnssecConfig.tsp).
Lines 40-49:

```typespec

  // FIXME: (ArmResourceCreateOrReplace): ArmResourceCreateOrReplaceAsync/ArmResourceCreateOrReplaceSync should have a body parameter.
  /**
   * Creates or updates the DNSSEC configuration on a DNS zone.
   */
  createOrUpdate is Azure.ResourceManager.Legacy.CreateOrReplaceAsync<
    DnssecConfig,
    Request = void,
    Parameters = {
      /**
```

### additional-missing-request-policy

[Exact source](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/security/resource-manager/Microsoft.Security/Security/ApiCollectionsAPI/ApiCollection.tsp).
Lines 55-69:

```typespec
  /**
   * Onboard an Azure API Management API to Microsoft Defender for APIs. The system will start monitoring the operations within the Azure Management API for intrusive behaviors and provide alerts for attacks that have been detected.
   */
  @summary("Onboard an Azure API Management API to Microsoft Defender for APIs")
  @tag("OnboardToD4API")
  @tag("APIMConfig")
  onboardAzureApiManagementApi is Azure.ResourceManager.Legacy.Extension.CreateOrUpdateAsync<
    serviceExternalResource,
    ApiCollection,
    Request = void,
    OptionalRequestBody = true,
    LroHeaders = ArmLroLocationHeader<FinalResult = ApiCollection> &
      Azure.Core.Foundations.RetryAfterHeader
  >;

```

### additional-missing-request-policy

[Exact source](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/management/resource-manager/Microsoft.Management/ManagementGroups/SubscriptionUnderManagementGroup.tsp).
Lines 47-59:

```typespec
  /**
   * Associates existing subscription with the management group.
   *
   */
  #suppress "@azure-tools/typespec-azure-core/no-openapi" "non-standard operations"
  #suppress "@azure-tools/typespec-azure-resource-manager/arm-put-operation-response-codes" "For backward compatibility"
  create is Azure.ResourceManager.Legacy.Extension.CreateOrReplaceSync<
    Extension.Tenant,
    SubscriptionUnderManagementGroup,
    Request = void,
    Parameters = SubscriptionUnderManagementGroupsParameters,
    Response = ArmResourceUpdatedResponse<SubscriptionUnderManagementGroup>
  >;
```

### source-versus-latest-version-removal

[Exact source](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/batch/resource-manager/Microsoft.Batch/Batch/Certificate.tsp).
Lines 63-74:

```typespec
  /**
   * Warning: This operation is deprecated and will be removed after February, 2024. Please use the [Azure KeyVault Extension](https://learn.microsoft.com/azure/batch/batch-certificate-migration-guide) instead.
   */
  #suppress "@azure-tools/typespec-azure-resource-manager/arm-put-operation-response-codes" "Legacy behavior"
  #deprecated "Removal of feature"
  @removed(Versions.v2025_06_01)
  create is Azure.ResourceManager.Legacy.CreateOrReplaceAsync<
    Certificate,
    Request = CertificateCreateOrUpdateParameters,
    Parameters = {
      /**
       * The entity state (ETag) version of the certificate to update. A value of "*" can be used to apply the operation only if the certificate already exists. If omitted, this operation will always be applied.
```

## Controls and validation

| Selected TypeSpec control                                                                    | Expected | Observed | Default | Worker  |
| -------------------------------------------------------------------------------------------- | -------- | -------- | ------- | ------- |
| [standard-template](controls/standard-template/main.tsp)                                     | 0        | 0        | 0       | success |
| [body-mismatch](controls/body-mismatch/main.tsp)                                             | 1        | 1        | 1       | success |
| [body-root-mismatch](controls/body-root-mismatch/main.tsp)                                   | 1        | 1        | 1       | success |
| [missing-request](controls/missing-request/main.tsp)                                         | 1        | 1        | 1       | success |
| [void-request](controls/void-request/main.tsp)                                               | 1        | 1        | 1       | success |
| [independent-request-response](controls/independent-request-response/main.tsp)               | 2        | 2        | 2       | success |
| [alias-compliant](controls/alias-compliant/main.tsp)                                         | 0        | 0        | 0       | success |
| [plain-success-response-gap](controls/plain-success-response-gap/main.tsp)                   | 0        | 0        | 0       | success |
| [unregistered-custom-put-gap](controls/unregistered-custom-put-gap/main.tsp)                 | 0        | 0        | 0       | success |
| [source-suppression](controls/source-suppression/main.tsp)                                   | 0        | 0        | 0       | success |
| [explicit-config-disable](controls/explicit-config-disable/main.tsp)                         | 1        | 1        | 0       | success |
| [multipart-excluded](controls/multipart-excluded/main.tsp)                                   | 0        | 0        | 0       | success |
| [registered-response-mismatch](controls/registered-response-mismatch/main.tsp)               | 1        | 1        | 1       | success |
| [custom-nonresource-response-gap](controls/custom-nonresource-response-gap/main.tsp)         | 0        | 0        | 0       | success |
| [registered-cross-operation-mismatch](controls/registered-cross-operation-mismatch/main.tsp) | 1        | 1        | 1       | success |
| [legacy-registered-request-covered](controls/legacy-registered-request-covered/main.tsp)     | 1        | 1        | 1       | success |
| [legacy-registered-request-compliant](controls/legacy-registered-request-compliant/main.tsp) | 0        | 0        | 0       | success |

All **17** exact-injected controls passed, including legacy mismatch (one warning)
and compliant legacy request (zero). The older `legacy-registered-request-gap` result
is retained **historically at 2d82a09**, not counted as a passing current zero.
The 20 original Swagger-selector fixture checks are reusable pinned semantic evidence
([results](receipts/swagger-controls-members-final.json)), not a new Swagger corpus run.

Focused candidate tests: **55 passed across four files**. The two missing-diagnostic
regressions failed before the production fix. Production build typecheck, changed-file
type-aware lint, formatting and whitespace checks passed. Portable harness controls:
**37 passed**; six unrelated absent resource-group-rule fixtures were explicitly
non-applicable, not passes. Fifteen package artifacts were built and all packed/installed
JavaScript verified against final source builds
([provenance](receipts/artifact-provenance-20261105.json)).

All **18 saved-evidence tests** passed. All **18 code-backed source excerpts**
match their exact pinned source lines; these are separate validation units.

## External CI and validation limits

The broad test tsconfig has **39 pre-existing diagnostics**. A read-only compiler-host
comparison with untouched PR HEAD reproduced identical diagnostics; neither edited
TypeScript file has an error. This is not a claim that the broad test typecheck passed.

**Azure REST API Specs CI failed** on its separate moving **605-project typespec-next**
population, which promotes warnings to errors: 845 `arm-common-types-version` and
197 `arm-resource-operation-response` diagnostics. These are not frozen-corpus counts.
The receipt records PR head, not a claim of identical merge-context code/runtime.
The pre-fix workflow required approval and did not execute; no before/after CI count
comparison exists. Do not disable existing rules, invent bodies or mass-suppress
legacy contracts to hide the failure.
[CI receipt](receipts/ci-rest-api-specs-20261105.json) and
[complete validation state](validation.json).

The **Ubuntu/Node22 build CI also failed**: one unchanged TCGC `use-correct-verb`
delete-alias test exceeded its 10-second test timeout (4,767 tests passed). The exact
local selector also exceeded its 10-second setup-hook timeout during the corpus run.
After corpus execution ended, the identical selector passed with unchanged default
timeouts on Node26.5 (one test passed). That is not a Node22 CI rerun. The tester
selects the TCGC rule, not the changed ARM rule.
No controlled baseline timing comparison or passing CI rerun is claimed.
[Build CI evidence and disposition](receipts/ci-build-20261105.json).

## Frozen input retention

Baseline metadata: `msyyc/azure-rest-api-specs`,
`evidence/shared-swagger-baseline` at `1c9d2b0e6a596754af1aa793b1906ff3c4ef2bd6`.
[Descriptor](baseline/descriptor.json); baseline identity
`aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`.
Immutable archive `swagger-arm-20261026-2cd3c5dd.tar.gz`, release
`swagger-lint-baseline-20261026-2cd3c5dd`: 51,932,501 bytes, SHA-256
`0904cbd17e24ce076e7969837b85b1f5b3682e5ae25b8805b048fb506e77c1d0`.
It retains 93,496 dataset files, 487 projects, 649 Swagger documents and 222,905
production observations. Current post-execution verification covers every dataset byte.

Staging supplement: pinned commit `feec4bab366c373380fbe1b5528faa12e7233cfe`, identity
`e0a2c22b857b13fa8ccf318bff1c8a6beaf367e1a1210cbc71cf7161fd86d482`.
Seven isolated rules, 5,360 observations, 649 successful inputs; selected member: 16.
[Descriptor](baseline/staging-descriptor.json) and [verification](baseline/staging-verification.json).
Frozen specs remain independently retained at
`msyyc/azure-rest-api-specs:evidence/long-running-operations-options-validator-20261022-source`
at `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`. Metadata, source retention and runtime injection are separate.

Policy `frozen-reference` assumes backward compatibility; it does not assert identical
emission under the current compiler. Runtime: Node v26.5.0, candidate/core pnpm 11.10.0,
specs pnpm 12.6.0, Python 3.12.13. Registry preparation failures and safe recovery
logs are retained: pnpm12 required the approved registry explicitly, then a task-local
full-metadata cache avoided a stale @scalar/types inventory. No TLS bypass, shared
cache/config edits, source downgrade or population reduction occurred.

## Read, recount and regenerate

Read this branch's main/member reports and `runs/20261105-e45c2bc87`.
Download the [native asset](native-asset.json) and immutable baseline/supplement
using their recorded identities, verifying byte sizes and SHA-256 before use.
The native asset retains 15 exact tarballs, all 487 fresh receipts/inputs, original
interruption evidence, recovery helpers/logs and full current metadata traces.

Saved-input reconstruction from this task directory:

```text
python -B -m unittest test_instance_analysis.py test_reanalyze.py
python analyze-instances.py --root .
python assess-gaps.py --verify
python render-instances.py --verify
python reanalyze.py --verify-inventory
```

These commands reanalyze saved inputs, not compile or execute linters. For a fresh
full execution, recover exact candidate/core/tooling/specs, all artifacts and the
verified baseline/supplement into isolated worktrees. Use the specs package manager
and approved registry, plus task-local metadata cache where required. Integration
patch/install must run from the candidate cwd and restore tracked workspace/lock files.
Pack Azure and core separately with repeated `--only=<package>` options; the Azure
root Chronus configuration intentionally excludes core packages.
Build, pack and injection commands/logs are retained in the native asset.

From tooling's `packages\typespec-lintdiff` directory, with the recorded runtime:

```powershell
mise exec -- node --import tsx/esm test\harness\native-coverage.ts `
  --candidate-repo $CANDIDATE_ROOT --specs-repo $SPECS_ROOT --tgz-dir $PACKAGES_ROOT `
  --validator-rule PutRequestResponseSchemeArm --validator-rule ConsistentResponseSchemaForPut `
  --validator-rule XmsResourceInPutResponse --validator-rule PutGetPatchResponseSchema `
  --tsp-rule @azure-tools/typespec-azure-resource-manager/arm-resource-operation-response `
  --scope source --baseline-run $BASELINE_ROOT --baseline-policy frozen-reference `
  --staging-supplement $STAGING_ROOT --output $FRESH_OUTPUT --concurrency 2 --native-mode configured
```

A fresh metadata pass additionally uses `analysis/run-instance-inspection.py --root
TASK_ROOT --tooling TOOLING_ROOT --output EMPTY_OUTPUT --inspector INSPECTOR
--native-run CURRENT_NATIVE_RUN --node ABSOLUTE_PINNED_NODE`. It must reproduce every saved warning exactly.
`analysis/resolve-swagger-instances.py` accepts `--observations`, `--dataset`,
`--output` and optional `--traces`. Compact and assessment helpers are retained in
the asset. No command here regenerates the shared Swagger corpus automatically.

Never reuse occupied output directories or call saved-data replay a second fresh
full run. Artifact identities and available locks do not prove complete transitive
runtime locking. A second full regeneration is **not claimed**.

## Publication and independently recovered inputs

The [previous publication receipt](receipts/publication-20261104.json) independently
recovered and verified the unchanged baseline archive, staging supplement and frozen
source retention. Those immutable-input recovery proofs remain applicable; they do
not validate the changed rule's diagnostics. Current fresh coverage and artifact
attestation above provide that evidence. Current remote asset/hash and clean saved-data
recovery/reconstruction are in the [current publication receipt](receipts/publication-20261105.json).

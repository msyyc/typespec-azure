# Supporting evidence and recovery

## Assessment boundary

This refresh evaluates exact PR head `2d82a09b6ce2eda8114e54bfd4df6358ec956340` with core
`a43d2ca6f2ddd4c1a1d05f2e63cd4c8a40a71b76`, using tooling
`662e7f405fda22e1d9c8c9c1d7664d171f80b60d`. The source and runtime were isolated;
no production files, PR body/title, skills or baseline observations were changed.
This is not migration acceptance: independent migration-review checkpoints and complete
operation-level finding attribution remain unfinished/outside this description-only request.

The full checkpoint began `2026-11-04T04:04:01.748Z` and completed
`2026-11-04T05:32:39.656Z`. Native execution: `{"startedAt": "2026-11-04T04:35:19.700Z", "finishedAt": "2026-11-04T05:13:54.468Z", "budgetExceeded": false}`.
Selection was the entire sealed population, no filter/limit, concurrency 2.
Source scope retains project source diagnostics, rather than latest-version projected diagnostics.
Swagger data represents the producer's latest emitted API version. This is a version/scope difference,
not an established normalization. All 487 projects succeeded; zero failed,
zero budget truncations and zero unassessed. Successful zero-finding projects are retained explicitly.

Configured compilation retains project configuration and source suppressions and explicitly enables
the selected rule; a separate default compilation retains default-target diagnostics.
The compiler rejects error-severity diagnostics before recording successful assessment.
The TypeSpec rule is a warning; originals are ARM error registrations. Source suppression is retained,
Swagger production readme suppressions are not applied, and staging uses explicit isolated selection.
Default findings total 104; selected configured raw findings total
104; source-aligned findings total 104.
The [source suppression](controls/source-suppression/main.tsp) and
[explicit disable](controls/explicit-config-disable/main.tsp) controls distinguish these policies.

## Member observation groups

| Original Swagger linter                                                                                                                                                       | Mode        | Raw findings | Affected projects | Implementation                                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------ | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`PutRequestResponseSchemeArm`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-request-response-scheme-arm.md)       | production  | 212          | 38                | [source](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/put-request-response-scheme.ts)        |
| [`ConsistentResponseSchemaForPut`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-response-schema-for-put.md) | stagingOnly | 16           | 10                | [source](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/consistent-response-schema-for-put.ts) |
| [`XmsResourceInPutResponse`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/xms-resource-in-put-response.md)             | production  | 155          | 14                | [source](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/with-xms-resource.ts)                  |
| [`PutGetPatchResponseSchema`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-get-patch-response-schema.md)           | production  | 50           | 14                | [source](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/put-get-patch-schema.ts)               |

All four registrations have ARM audience, no member-specific options and no RPaaS-only restriction.
The upstream code/doc links were independently resolved through the GitHub content API at
`6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f`; blob IDs and sizes are in
[the verification receipt](receipts/verified-upstream-links.json).
`PutGetPatchResponseSchema` is admitted because current native documentation lists it and existing
lifecycle/list checks remain, not because its TypeSpec attribution can be separated.

Swagger raw total 433; reported document/path keys
387 keyed by `(member, project, reported document, JSON path)`;
file-independent member/path keys 275.
TypeSpec source keys 104 keyed by
`(project, rule, source file, line, column)`. These are **different units**, not comparable actionable
defect counts. Shared-rule message-family accounting is {'request model mismatch': 96, 'missing request': 8}; these families
must not be allocated to original members. Every raw target is in
[diagnostic-inventory.md](diagnostic-inventory.md); all populations and directional excesses are in
[project-differences.md](project-differences.md) and [summary.json](summary.json).
Every one-sided/count-different project remains visible. Individual pairings without deterministic
evidence are unresolved, including same-total projects; neither name matching nor project overlap
establishes functional equivalence.
Grouping raw observations yields 387 reported document/path keys, then removing the reported-document
component yields 275 member/project/path keys. The raw-to-final reduction is 158:
Network 170 to 14 and SQL 20 to 18 account for it. Multiple raw observations can share a reported
document/path while retaining different input-document or response-schema context.
These are not normalized defects or operation counts.
Repeated saved document/path occurrences and `input-fallback` attribution must not be described
automatically as distinct emitted operations or established duplicate bugs.
The analyzer's retained `observedProjectCoveragePercent` is a project-overlap statistic, not
functional coverage, actionable parity or a migration acceptance percentage.

## Registered scope and source identity

[Current implementation](https://github.com/Azure/typespec-azure/blob/2d82a09b6ce2eda8114e54bfd4df6358ec956340/packages/typespec-azure-resource-manager/src/rules/arm-resource-operation-response.ts) listens to registered resource models, resolves their ARM
operation map and tests only the noninternal PUT in `lifecycle.createOrUpdate`.
The request comparison uses effective request-visibility payload **model identity** against the
canonical resource. It accepts aliases and skips multipart. It does not independently enumerate HTTP
PUT operations or compare every 200/201 body. Existing lifecycle/list response logic only rejects
another registered resource model in its supported return-type traversal.

**Registered legacy PUT request gap:** the [legacy operation template](https://github.com/Azure/typespec-azure/blob/2d82a09b6ce2eda8114e54bfd4df6358ec956340/packages/typespec-azure-resource-manager/lib/legacy-types/operations.tsp#L48-L84) invokes
`@legacyResourceOperation`, whose [implementation](https://github.com/Azure/typespec-azure/blob/2d82a09b6ce2eda8114e54bfd4df6358ec956340/packages/typespec-azure-resource-manager/src/private.decorators.ts#L920-L963) stores operations in `lists`,
including `createOrUpdate`. The new request-body branch reads only `lifecycle.createOrUpdate`;
legacy PUT requests therefore bypass it, although retained response checking still walks `lists`.
The [exact installed-package control](controls/legacy-registered-request-gap/result.json) has a
registered Widget with a distinct Input request and reports zero selected/default findings.
Real ApiManagement `ApiContractOps` uses this template with `Request = ApiCreateOrUpdateParameter`.
Its saved Swagger request-schema finding does not establish that the registered listener checked
this request. ApiManagement has 22 Swagger findings (19 request, 3 cross-operation) and 4 current
TypeSpec findings; this identified cause is not a claim that all 18 excess findings share one cause.

[Lifecycle registration](https://github.com/Azure/typespec-azure/blob/2d82a09b6ce2eda8114e54bfd4df6358ec956340/packages/typespec-azure-resource-manager/src/operations.ts#L187-L231) assigns a singular `operations.lifecycle[kind]`.
Multiple aliases for one resource can overwrite that slot. Separately, one source definition may
emit multiple operation/version/document occurrences; file-independent paths are not source
correspondence. Both mechanisms prevent treating raw count differences as equivalent duplicates.
The plain custom AnalyticsItems PUT is an exact source example outside registration-based coverage.

**Network inherited-resource gap:** Network has 170 saved Swagger findings
(47 request-schema,108 resource-extension,15 cross-operation), versus zero TypeSpec findings.
The [compiled registration trace](receipts/registration-inspection-354.json.registration.json)
confirms `Microsoft.Network.ConnectionMonitorResult` and `Common.NetworkWatcher` are unregistered.
The real ConnectionMonitor PUT uses `ConnectionMonitor` request and `ConnectionMonitorResult`
response; inherited `TrackedResourceWithEtag` alone does not provide canonical registration.
This proves a concrete missed request-schema case, not a causal classification of all 170 findings.

The [ApiManagement registration trace](receipts/registration-inspection-11.json.registration.json)
confirms ApiContract is registered but its PUT appears in `lists`, with no lifecycle create/update.
Its map retains only the WorkspaceApi operation for the shared `createOrUpdate` key, illustrating
both legacy registration and same-name overwrite. Two narrow instrumented recompilations preserved
exactly the same selected diagnostics as main-corpus receipts (4 and0); they are investigations,
not extra corpus projects or a second full corpus run.

**Saved attribution limit:** a Network finding's recorded `input-fallback` document is
`applicationGateway.json`, which does not contain its reported connectionMonitor route.
An independent exact-route search locates one match in `networkWatcher.json`, with the expected
request/response refs. [The full receipt](receipts/network-fallback-document-investigation.json)
preserves both the original observation and the located document; the sealed baseline was not
repaired. Document/path grouping and all other fallback observations remain attribution-limited.

The response helper also does not descend into a single `ArmResponse<Other>` Model wrapper as it
does a Union template; the retained first failed control captured that limitation before the
canonical union control was corrected. No code change was made and the narrower single-wrapper
case is not certified by the passing union check.

## Additional request policy and version scope

The [complete TypeSpec-higher investigation](receipts/native-higher-investigation.json) explains
all four higher-count projects without cancelling Swagger-higher differences:

| Project                    | Swagger linter | TypeSpec linter | Independently identified excess                                                                                   |
| -------------------------- | -------------- | --------------- | ----------------------------------------------------------------------------------------------------------------- |
| Dns                        | 0              | 1               | DnssecConfig uses `Request = void`; emitted PUT has no body                                                       |
| Security/ApiCollectionsAPI | 0              | 1               | Onboard operation uses `Request = void`; emitted PUT has no body                                                  |
| ManagementGroups           | 2              | 3               | Subscription association uses `Request = void`; emitted PUT has no body                                           |
| Batch                      | 1              | 2               | Certificate create is removed at `v2025_06_01`, absent in latest emitted paths but retained in source compilation |

`PutRequestResponseSchemeArm` skips operations with no request schema; requiring a request is an
additional TypeSpec policy, not a migrated original finding or proof of a Swagger false negative.
The Batch difference is explicitly source-versus-projection scope, not an accepted schema mismatch
in the selected latest API. Exact operation IDs, emitted paths, source excerpts and diagnostics
are retained. Per-member assignment of the remaining shared TypeSpec findings is still unassessed.

## Staging identity bug and Quota gap

The staging [implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/consistent-response-schema-for-put.ts)
uses `responseSchema !== resourceSchema`, a JavaScript object-identity test rather than structural
comparison. This is a **bug** for identical resolved schemas that occupy separate object instances.
Exact saved-data investigation maps all 16 findings, using referenced document plus JSON pointer,
to 16 unambiguous PUT operations. Fifteen have identical raw 200/201 schema references; one does not.
The false-positive classification is supported by raw document identity/schema equality and the
pinned implementation; no resolver object-identity execution trace was captured or claimed.
Definitions and external common-types attribution are preserved, not reinterpreted as operation paths.

The genuine mismatch is `Quota_CreateOrUpdate` in Reservations/Quota API `2020-10-25`.
Its 200 schema is `#/definitions/CurrentQuotaLimitBase`, while 201 is
`#/definitions/QuotaRequestSubmitResponse201`. The TypeSpec source deliberately returns canonical
resource for 200 and a plain nonresource model for 201; the current helper does not compare the latter
as a registered resource. This remains a real enforcement gap, not an accepted retirement.
The [investigation](receipts/staging-source-investigation.json) retains all 16 raw mappings;
the [summary](receipts/staging-source-investigation-summary.json) records zero unresolved mappings.
DurableTask's PrivateEndpointConnection example demonstrates identical external refs without
claiming a newly tested upstream rulesets version.

## Exact source examples

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
| [legacy-registered-request-gap](controls/legacy-registered-request-gap/main.tsp)             | 0        | 0        | 0       | success |

Sixteen controls use the exact installed compiler/ARM package closure; 13 ran before the corpus
and 3 member/gap controls during its execution. Five real emitted Swagger fixtures were additionally
checked with all four **isolated original registrations**, 20 successful selected checks including
explicit staging selection, not a corpus regeneration.
[The original selector results](receipts/swagger-controls-members-final.json) retain each finding;
common-types reference closure is included under `common-types`.

The exact candidate's ARM response suite passed **29/29** unchanged on warm rerun.
The first cold attempt passed 28 and exceeded the existing 10-second beforeEach timeout on one test;
both logs remain in the native asset. Applicable portable-worker tests passed **37**; **6**
unrelated resource-group-rule cases were explicitly non-applicable because that rule is absent
at this candidate. This is not a claim that those six tests passed.
[validation.json](validation.json) retains initial invocation/control failures and corrections.
No invalid-ref, compiler error or failed assessment was silently accepted.

Fifteen package tarballs were packed from exact built candidate/core source.
[Artifact provenance](receipts/artifact-provenance.json) verifies every packed JavaScript file against
the built closure. [Loaded listener attestation](receipts/loaded-rule-preflight.json) compares actual
installed index/linter/rule/operations/resource bytes with built candidate bytes.
The ARM artifact SHA-256 is
`a22f2b687dc958279012ccaa4b024306a2b3106385b8f3da369e14709f2e37ff`;
installed listener is `43eb31366e1d378a3c8d2c4f27a904f977206e9e42fa0cfd8fe718d4c45b8b9e`.
Post-run source/status/hash attestation is retained separately.

## Frozen input retention

- Baseline metadata repository: `msyyc/azure-rest-api-specs`, branch
  `evidence/shared-swagger-baseline`, pinned commit
  `1c9d2b0e6a596754af1aa793b1906ff3c4ef2bd6`.
- [Pinned descriptor](baseline/descriptor.json), SHA-256
  `ac511e7ff4b519619f30af811107b7f770a92a5bb56b199dfca983262dc8fd31`;
  baseline identity `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`.
- Existing immutable archive `swagger-arm-20261026-2cd3c5dd.tar.gz`,
  release `swagger-lint-baseline-20261026-2cd3c5dd`, 51,932,501 bytes,
  SHA-256 `0904cbd17e24ce076e7969837b85b1f5b3682e5ae25b8805b048fb506e77c1d0`.
- Baseline recovery/integrity verified 93,496 dataset files, 487 projects, 649 Swagger documents and
  222,905 production observations; [receipt](receipts/baseline-verification-receipt.json).
- Staging supplement pinned commit `feec4bab366c373380fbe1b5528faa12e7233cfe`,
  identity `e0a2c22b857b13fa8ccf318bff1c8a6beaf367e1a1210cbc71cf7161fd86d482`.
  Seven isolated rules / 5,360 observations / 649 successful inputs; the selected member has 16.
  [Descriptor](baseline/staging-descriptor.json) and [verification](baseline/staging-verification.json).
- Frozen specs source `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9` is independently retained by personal fork branch
  `evidence/long-running-operations-options-validator-20261022-source`; its exact SHA was verified,
  not advanced. This is separate from metadata and runtime injection.
- Policy `frozen-reference` assumes candidate backward compatibility. Historical Swagger was not
  re-emitted or shown identical under the new compiler/emitter; this limits interpretation.

Node `v26.5.0`; candidate/core pnpm `11.10.0`; frozen specs pnpm `12.6.0`;
Python `3.12.13`; mise `2026.10.12`. Actual installed paths/hashes are in sanitized run receipts.
Dependency installs were limited to missing runtime needs except one pnpm core-pack invocation
that opportunistically installed 50 core workspace projects (1,640 packages,43 downloads);
the successful log and clean tracked-state verification are retained.
Subsequent exec disabled opportunistic dependency verification. Neither version strings nor
these artifact hashes prove complete transitive dependency locking.

## Read, recount and regenerate

1. **Read:** fetch this evidence branch/commit; read the group/member reports, inventories and
   immutable run directory `runs/20261104-2d82a09b6`. Download the existing Swagger asset and
   [new native asset](native-asset.json) using their exact repository/release/asset identities;
   verify recorded byte sizes and SHA-256 values.
2. **Reanalyze saved observations:** in a clean checkout, run
   `python reanalyze.py --verify-inventory` from this task directory.
   It checks committed file hashes, independently recounts observations and compares `summary.json`.
   It does not compile, evaluate either linter, restore the baseline CLI runtime or regenerate prose.
3. **Regenerate:** fetch exact candidate/core/tooling and frozen specs source commits; recover the
   pinned shared baseline descriptor/archive and staging commit with their own integrity verification;
   recover all 15 native package artifacts from the native asset and verify hashes.
   Install only required missing dependencies with recorded pnpm/mise versions and available locks;
   where applicable use frozen-lockfile/ignore-scripts followed by explicit builds.
   Re-run semantic controls and source investigations before producing a new migration note.
   Complete transitive runtime locks are not claimed; a second full corpus regeneration was not run.

Build closure: run candidate pnpm recursive build selecting the six published Azure packages with
their dependency closure, then Chronus pack with repeated `--only` for each of the 15 packages.
The original build/pack commands and unsuccessful corrections are retained in the downloadable
native asset's preflight logs and helper scripts, with original-to-sanitized SHA-256 mapping.
Execute the analyzer from tooling's `packages\typespec-lintdiff` directory:

```powershell
mise exec -- node --import tsx/esm test\harness\native-coverage.ts `
  --candidate-repo $CANDIDATE_ROOT --specs-repo $SPECS_ROOT --tgz-dir $PACKAGES_ROOT `
  --validator-rule PutRequestResponseSchemeArm --validator-rule ConsistentResponseSchemaForPut `
  --validator-rule XmsResourceInPutResponse --validator-rule PutGetPatchResponseSchema `
  --tsp-rule @azure-tools/typespec-azure-resource-manager/arm-resource-operation-response `
  --scope source --baseline-run $BASELINE_ROOT --baseline-policy frozen-reference `
  --staging-supplement $STAGING_ROOT --output $FRESH_OUTPUT --concurrency 2 --native-mode configured
```

Never reuse an occupied output directory, regenerate the shared Swagger corpus without separate
authorization, or report a saved-data recount as a fresh linter execution.
Publication and clean remote-checkout recovery receipts are appended after actual verification.

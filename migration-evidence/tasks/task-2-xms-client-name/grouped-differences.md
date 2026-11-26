# Grouped diagnostic differences

These are all differing projects and every captured target-warning location.
Counts are individual configured diagnostic occurrences, not equivalent defects.
No warnings are normalized, paired or removed. No exhaustive corpus-wide
pre-suppression capture was made. Swagger linter counts are zero for every group.
The [independent recount](receipts/saved-observation-reanalysis.json) preserves
signed, absolute and relative differences and complete project sets.

| Project                                                                                                   | Swagger linter | TypeSpec linter | After-analysis counts                                   | Evidence                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------- | -------------: | --------------: | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `specification/advisor/resource-manager/Microsoft.Advisor/Advisor`                                        |              0 |               4 | Raw counts retained; equivalent-defect count unassessed | [advisor-body-repeat](#advisor-body-repeat), [advisor-removed-assessment](#advisor-removed-assessment), [advisor-removed-patch](#advisor-removed-patch), [advisor-removed-triage](#advisor-removed-triage) |
| `specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement`                      |              0 |               2 | Raw counts retained; equivalent-defect count unassessed | [apim-duplicate-body-renames](#apim-duplicate-body-renames)                                                                                                                                                |
| `specification/app/resource-manager/Microsoft.App/ContainerApps`                                          |              0 |               1 | Raw counts retained; equivalent-defect count unassessed | [containerapps-scoped-repeat](#containerapps-scoped-repeat)                                                                                                                                                |
| `specification/batch/resource-manager/Microsoft.Batch/Batch`                                              |              0 |               2 | Raw counts retained; equivalent-defect count unassessed | [batch-removed-certificates](#batch-removed-certificates)                                                                                                                                                  |
| `specification/billing/resource-manager/Microsoft.Billing/Billing`                                        |              0 |               2 | Raw counts retained; equivalent-defect count unassessed | [billing-shadowed-inherited-overrides](#billing-shadowed-inherited-overrides)                                                                                                                              |
| `specification/cdn/resource-manager/Microsoft.Cdn/Cdn`                                                    |              0 |               3 | Raw counts retained; equivalent-defect count unassessed | [cdn-copy-source-repeats](#cdn-copy-source-repeats)                                                                                                                                                        |
| `specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger`       |              0 |               8 | Raw counts retained; equivalent-defect count unassessed | [confidentialledger-removed-managedccf](#confidentialledger-removed-managedccf)                                                                                                                            |
| `specification/connectedcache/resource-manager/Microsoft.ConnectedCache/ConnectedCache`                   |              0 |               1 | Raw counts retained; equivalent-defect count unassessed | [connectedcache-shadowed-inline-name](#connectedcache-shadowed-inline-name)                                                                                                                                |
| `specification/consumption/resource-manager/Microsoft.Consumption/Consumption`                            |              0 |               2 | Raw counts retained; equivalent-defect count unassessed | [consumption-inherited-scope-repeat](#consumption-inherited-scope-repeat)                                                                                                                                  |
| `specification/containerservice/resource-manager/Microsoft.ContainerService/aks`                          |              0 |               4 | Raw counts retained; equivalent-defect count unassessed | [aks-body-common-repeat](#aks-body-common-repeat), [aks-duplicate-enabled](#aks-duplicate-enabled), [aks-shadowed-csharp-override](#aks-shadowed-csharp-override)                                          |
| `specification/databox/resource-manager/Microsoft.DataBox/DataBox`                                        |              0 |               2 | Raw counts retained; equivalent-defect count unassessed | [databox-duplicate-csharp](#databox-duplicate-csharp)                                                                                                                                                      |
| `specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs`                             |              0 |               2 | Raw counts retained; equivalent-defect count unassessed | [devtestlabs-duplicate-csharp](#devtestlabs-duplicate-csharp)                                                                                                                                              |
| `specification/dns/resource-manager/Microsoft.Network/Dns`                                                |              0 |               1 | Raw counts retained; equivalent-defect count unassessed | [dns-identity-name](#dns-identity-name)                                                                                                                                                                    |
| `specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration`       |              0 |               2 | Raw counts retained; equivalent-defect count unassessed | [domainregistration-duplicate-csharp](#domainregistration-duplicate-csharp)                                                                                                                                |
| `specification/frontdoor/resource-manager/Microsoft.Network/FrontDoor`                                    |              0 |               2 | Raw counts retained; equivalent-defect count unassessed | [frontdoor-inherited-java-duplicates](#frontdoor-inherited-java-duplicates)                                                                                                                                |
| `specification/help/resource-manager/Microsoft.Help/Help`                                                 |              0 |               8 | Raw counts retained; equivalent-defect count unassessed | [help-duplicate-body-applications](#help-duplicate-body-applications)                                                                                                                                      |
| `specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity`       |              0 |              10 | Raw counts retained; equivalent-defect count unassessed | [hybridconnectivity-duplicate-body-applications](#hybridconnectivity-duplicate-body-applications)                                                                                                          |
| `specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault`                                     |              0 |               1 | Raw counts retained; equivalent-defect count unassessed | [keyvault-shadowed-common-override](#keyvault-shadowed-common-override)                                                                                                                                    |
| `specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric` |              0 |              25 | Raw counts retained; equivalent-defect count unassessed | [managednetworkfabric-copy-source-repeats](#managednetworkfabric-copy-source-repeats)                                                                                                                      |
| `specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity`                            |              0 |               6 | Raw counts retained; equivalent-defect count unassessed | [managedidentity-duplicate-body-applications](#managedidentity-duplicate-body-applications)                                                                                                                |
| `specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud`                         |              0 |               2 | Raw counts retained; equivalent-defect count unassessed | [networkcloud-copy-source-repeats](#networkcloud-copy-source-repeats)                                                                                                                                      |
| `specification/oracle/resource-manager/Oracle.Database/OracleDatabase`                                    |              0 |               4 | Raw counts retained; equivalent-defect count unassessed | [oracle-duplicate-csharp](#oracle-duplicate-csharp)                                                                                                                                                        |
| `specification/postgresql/resource-manager/Microsoft.DBforPostgreSQL/PostgreSql`                          |              0 |               1 | Raw counts retained; equivalent-defect count unassessed | [postgresql-shadowed-csharp-override](#postgresql-shadowed-csharp-override)                                                                                                                                |
| `specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup` |              0 |               3 | Raw counts retained; equivalent-defect count unassessed | [recoveryservicesbackup-shadowed-csharp](#recoveryservicesbackup-shadowed-csharp)                                                                                                                          |
| `specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/OpenShiftClusters`              |              0 |               2 | Raw counts retained; equivalent-defect count unassessed | [openshift-duplicate-csharp](#openshift-duplicate-csharp)                                                                                                                                                  |
| `specification/resources/resource-manager/Microsoft.Resources/deploymentStacks`                           |              0 |               6 | Raw counts retained; equivalent-defect count unassessed | [deploymentstacks-propagated-body-applications](#deploymentstacks-propagated-body-applications)                                                                                                            |
| `specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights`             |              0 |               8 | Raw counts retained; equivalent-defect count unassessed | [securityinsights-inherited-csharp-repeats](#securityinsights-inherited-csharp-repeats)                                                                                                                    |
| `specification/sql/resource-manager/Microsoft.Sql/SQL`                                                    |              0 |               4 | Raw counts retained; equivalent-defect count unassessed | [sql-duplicate-csharp](#sql-duplicate-csharp)                                                                                                                                                              |
| `specification/storage/resource-manager/Microsoft.Storage/Storage`                                        |              0 |               7 | Raw counts retained; equivalent-defect count unassessed | [storage-duplicate-body-applications](#storage-duplicate-body-applications), [storage-duplicate-csharp](#storage-duplicate-csharp)                                                                         |
| `specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync`                            |              0 |               2 | Raw counts retained; equivalent-defect count unassessed | [storagesync-duplicate-csharp](#storagesync-duplicate-csharp)                                                                                                                                              |
| `specification/vmware/resource-manager/Microsoft.AVS/AVS`                                                 |              0 |               2 | Raw counts retained; equivalent-defect count unassessed | [avs-duplicate-body-applications](#avs-duplicate-body-applications)                                                                                                                                        |
| `specification/web/resource-manager/Microsoft.Web/AppService`                                             |              0 |              12 | Raw counts retained; equivalent-defect count unassessed | [appservice-duplicate-csharp](#appservice-duplicate-csharp), [appservice-shadowed-csharp](#appservice-shadowed-csharp)                                                                                     |

## advisor-body-repeat

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/advisor/resource-manager/Microsoft.Advisor/Advisor` / `2026-10-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 1.
- **Cause:** body-name-application-collapse.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** Existing !csharp naming and identical common repeat leave SDK naming unchanged under the retained scope precedence. Retained PUT body name is suppressionContract and has no x-ms-client-name, so the Swagger selector does not select that body object. One emitted name cannot preserve application multiplicity.

**Captured source applications**

| Source                                                                                                                                                                                                                                                            | Exact authored excerpt                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| [specification/advisor/resource-manager/Microsoft.Advisor/Advisor/client.tsp:28](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/client.tsp#L28-L36) | `@@clientName( SuppressionContracts.create::parameters.resource, "suppressionContract" );` |

**TypeSpec source and supporting declarations**

[specification/advisor/resource-manager/Microsoft.Advisor/Advisor/client.tsp:28](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/client.tsp#L28-L31)

```typespec
@@clientName(
  SuppressionContracts.create::parameters.resource,
  "suppressionContract"
);
```

[specification/advisor/resource-manager/Microsoft.Advisor/Advisor/back-compatible.tsp:68](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/back-compatible.tsp#L68-L72)

```typespec
@@clientName(
  SuppressionContracts.create::parameters.resource,
  "suppressionContract",
  "!csharp"
);
```

[specification/advisor/resource-manager/Microsoft.Advisor/Advisor/SuppressionContract.tsp:40](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/SuppressionContract.tsp#L40-L50)

```typespec
  /**
   * Enables the snoozed or dismissed attribute of a recommendation. The snoozed or dismissed attribute is referred to as a suppression. Use this API to create or update the snoozed or dismissed status of a recommendation.
   */
  #suppress "@azure-tools/typespec-azure-resource-manager/arm-put-operation-response-codes" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  #suppress "@azure-tools/typespec-azure-core/response-schema-problem" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  create is ArmResourceCreateOrReplaceSync<
    SuppressionContract,
    BaseParameters = Azure.ResourceManager.Foundations.ExtensionBaseParameters,
    Error = ArmDefaultErrorResponse | ArmNotFoundResponse,
    Response = ArmResponse<SuppressionContract>
  >;
```

**Retained Swagger or projection evidence**

`projects/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/swagger/stable/2026-10-01/openapi.json`; exact pointer segments:

```json
[
  "paths",
  "/{resourceUri}/providers/Microsoft.Advisor/recommendations/{recommendationId}/suppressions/{name}",
  "put",
  "parameters"
]
```

```json
[
  {
    "$ref": "../../../../../../../../../common-types/resource-management/v4/types.json#/parameters/ApiVersionParameter"
  },
  {
    "$ref": "#/parameters/Azure.ResourceManager.ResourceUriParameter"
  },
  {
    "name": "recommendationId",
    "in": "path",
    "description": "The recommendation ID.",
    "required": true,
    "type": "string"
  },
  {
    "name": "name",
    "in": "path",
    "description": "The name of the suppression.",
    "required": true,
    "type": "string"
  },
  {
    "name": "suppressionContract",
    "in": "body",
    "description": "The snoozed or dismissed attribute; for example, the snooze duration.",
    "required": true,
    "schema": {
      "$ref": "#/definitions/SuppressionContract"
    }
  }
]
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 1 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** SDK/spec owner may remove the redundant common application after checking retained scoped naming; no frozen-source edits in this task.

## advisor-removed-assessment

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/advisor/resource-manager/Microsoft.Advisor/Advisor` / `2026-10-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 1.
- **Cause:** older-version-source.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** AssessmentResults is removed at v2026_10_01, the selected Swagger version. The unprojected source retains the ineffective common repeat of the !csharp naming application.

**Captured source applications**

| Source                                                                                                                                                                                                                                                            | Exact authored excerpt                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| [specification/advisor/resource-manager/Microsoft.Advisor/Advisor/client.tsp:32](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/client.tsp#L32-L40) | `@@clientName(AssessmentResults.put::parameters.resource, "assessmentContract");` |

**TypeSpec source and supporting declarations**

[specification/advisor/resource-manager/Microsoft.Advisor/Advisor/client.tsp:32](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/client.tsp#L32-L32)

```typespec
@@clientName(AssessmentResults.put::parameters.resource, "assessmentContract");
```

[specification/advisor/resource-manager/Microsoft.Advisor/Advisor/back-compatible.tsp:93](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/back-compatible.tsp#L93-L97)

```typespec
@@clientName(
  AssessmentResults.put::parameters.resource,
  "assessmentContract",
  "!csharp"
);
```

[specification/advisor/resource-manager/Microsoft.Advisor/Advisor/AssessmentResult.tsp:25](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/AssessmentResult.tsp#L25-L42)

```typespec
@armResourceOperations
@removed(Versions.v2026_10_01)
interface AssessmentResults {
  /**
   * Get an existing Azure Advisor assessment.
   */
  get is ArmResourceRead<
    AssessmentResult,
    BaseParameters = Azure.ResourceManager.Foundations.SubscriptionBaseParameters
  >;

  /**
   * Create or Overwrite Azure Advisor assessment.
   */
  put is ArmResourceCreateOrReplaceSync<
    AssessmentResult,
    BaseParameters = Azure.ResourceManager.Foundations.SubscriptionBaseParameters
  >;
```

**Retained Swagger or projection evidence**

No exact selected-version Swagger object is asserted for this group.
Removed declarations are established by the quoted version decorators.
Copied declarations and SDK-only scopes are established by the exact
source-copy/application chain, not inferred emitted-name matching.

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 1 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Retain the source-profile finding and version limit; do not claim a same-version missing Swagger diagnostic.

## advisor-removed-patch

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/advisor/resource-manager/Microsoft.Advisor/Advisor` / `2026-10-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 1.
- **Cause:** older-version-source.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** Old patch operation removed at v2026_02_01_preview; selected Swagger is 2026-10-01. The newer update operation is a different authored operation and payload, not a location-only correspondence. Source warning is an ineffective common repeat of the existing !csharp override.

**Captured source applications**

| Source                                                                                                                                                                                                                                                            | Exact authored excerpt                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| [specification/advisor/resource-manager/Microsoft.Advisor/Advisor/client.tsp:21](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/client.tsp#L21-L29) | `@@clientName( ResourceRecommendationBases.patch::parameters.properties, "trackedProperties" );` |

**TypeSpec source and supporting declarations**

[specification/advisor/resource-manager/Microsoft.Advisor/Advisor/client.tsp:21](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/client.tsp#L21-L24)

```typespec
@@clientName(
  ResourceRecommendationBases.patch::parameters.properties,
  "trackedProperties"
);
```

[specification/advisor/resource-manager/Microsoft.Advisor/Advisor/back-compatible.tsp:25](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/back-compatible.tsp#L25-L29)

```typespec
@@clientName(
  ResourceRecommendationBases.patch::parameters.properties,
  "trackedProperties",
  "!csharp"
);
```

[specification/advisor/resource-manager/Microsoft.Advisor/Advisor/ResourceRecommendationBase.tsp:39](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/ResourceRecommendationBase.tsp#L39-L61)

```typespec
   * Update the tracked properties of a Recommendation.
   */
  #suppress "@azure-tools/typespec-azure-core/response-schema-problem" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  @added(Versions.v2025_05_01_preview)
  @removed(Versions.v2026_02_01_preview)
  @patch(#{ implicitOptionality: false })
  patch is ArmCustomPatchSync<
    ResourceRecommendationBase,
    PatchModel = TrackedRecommendationPropertiesPayload,
    BaseParameters = Azure.ResourceManager.Foundations.ExtensionBaseParameters,
    Error = ArmDefaultErrorResponse
  >;

  /**
   * Update the state of a Recommendation
   */
  @added(Versions.v2026_02_01_preview)
  @patch(#{ implicitOptionality: false })
  update is Extension.CustomPatchSync<
    Extension.Subscription,
    ResourceRecommendationBase,
    RecommendationPatchPayload
  >;
```

**Retained Swagger or projection evidence**

No exact selected-version Swagger object is asserted for this group.
Removed declarations are established by the quoted version decorators.
Copied declarations and SDK-only scopes are established by the exact
source-copy/application chain, not inferred emitted-name matching.

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 1 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Keep the source-profile observation; do not infer missing latest-version Swagger behavior or remove source warnings by count normalization.

## advisor-removed-triage

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/advisor/resource-manager/Microsoft.Advisor/Advisor` / `2026-10-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 1.
- **Cause:** older-version-source.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** TriageRecommendations is removed at v2026_03_01_preview; the selected Swagger is 2026-10-01. Source includes its ineffective common repeat even though the operation is not in the latest-version projection.

**Captured source applications**

| Source                                                                                                                                                                                                                                                            | Exact authored excerpt                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [specification/advisor/resource-manager/Microsoft.Advisor/Advisor/client.tsp:33](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/client.tsp#L33-L41) | `@@clientName( TriageRecommendations.rejectTriageRecommendation::parameters.body, "recommendationRejectBody" );` |

**TypeSpec source and supporting declarations**

[specification/advisor/resource-manager/Microsoft.Advisor/Advisor/client.tsp:33](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/client.tsp#L33-L36)

```typespec
@@clientName(
  TriageRecommendations.rejectTriageRecommendation::parameters.body,
  "recommendationRejectBody"
);
```

[specification/advisor/resource-manager/Microsoft.Advisor/Advisor/back-compatible.tsp:128](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/back-compatible.tsp#L128-L132)

```typespec
@@clientName(
  TriageRecommendations.rejectTriageRecommendation::parameters.body,
  "recommendationRejectBody",
  "!csharp"
);
```

[specification/advisor/resource-manager/Microsoft.Advisor/Advisor/TriageRecommendation.tsp:55](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/TriageRecommendation.tsp#L55-L62)

```typespec

#suppress "@azure-tools/typespec-azure-resource-manager/arm-resource-interface-requires-decorator" "Compatibility: preserves the legacy triage recommendation operation and action route shapes in API versions 2025-05-01-preview and 2026-02-01-preview; changing it would alter the TriageRecommendations interface."
@removed(Versions.v2026_03_01_preview)
interface TriageRecommendations {
  #suppress "@azure-tools/typespec-azure-core/no-openapi" "Compatibility: preserves the legacy GET triage recommendation wire shape in API versions 2025-05-01-preview and 2026-02-01-preview; changing it would alter the triageRecommendations_Get operation."
  #deprecated "This operation is no longer supported. The Azure Advisor triage workflow has been retired and there is no replacement API. Clients should stop calling this operation."
  @doc("Deprecated: This operation is no longer supported. The Azure Advisor triage workflow has been retired and there is no replacement API. Clients should stop calling this operation.")
  @summary("Get an existing recommendation by id for an existing Resiliency Review Id.")
```

[specification/advisor/resource-manager/Microsoft.Advisor/Advisor/TriageRecommendation.tsp:102](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/TriageRecommendation.tsp#L102-L112)

```typespec
  #suppress "@azure-tools/typespec-azure-core/no-openapi" "Compatibility: preserves the legacy reject action wire shape in API versions 2025-05-01-preview and 2026-02-01-preview; changing it would alter the triageRecommendations_RejectTriageRecommendation operation."
  #deprecated "This operation is no longer supported. The Azure Advisor triage workflow has been retired and there is no replacement API. Clients should stop calling this operation."
  @doc("Deprecated: This operation is no longer supported. The Azure Advisor triage workflow has been retired and there is no replacement API. Clients should stop calling this operation.")
  @summary("Reject existing triage recommendation by id.")
  @operationId("triageRecommendations_RejectTriageRecommendation")
  @action("reject")
  rejectTriageRecommendation is TriageRecommendationOps.ActionSync<
    TriageRecommendation,
    RecommendationRejectBody,
    OkResponse
  >;
```

**Retained Swagger or projection evidence**

No exact selected-version Swagger object is asserted for this group.
Removed declarations are established by the quoted version decorators.
Copied declarations and SDK-only scopes are established by the exact
source-copy/application chain, not inferred emitted-name matching.

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 1 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Retain the source-profile warning; any source cleanup belongs to the service owner, not a forced parity change.

## apim-duplicate-body-renames

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement` / `2025-09-01-preview`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 2.
- **Cause:** body-name-application-collapse.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** Two separately authored identical common applications target the same body property. Each application is independently removable while the other remains; two warnings are retained without actionable-defect normalization. The saved PATCH body has name parameters and no x-ms-client-name; the combined Swagger selector cannot diagnose duplicate TypeSpec applications.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                                                        | Exact authored excerpt                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/back-compatible.tsp:966](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/back-compatible.tsp#L966-L974)    | `@@clientName( ApiManagementServiceResources.quotaByCounterKeysUpdate::parameters.body, "parameters" );` |
| [specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/back-compatible.tsp:1931](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/back-compatible.tsp#L1931-L1934) | `@@clientName( ApiManagementServiceResources.quotaByCounterKeysUpdate::parameters.body, "parameters" );` |

**TypeSpec source and supporting declarations**

[specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/back-compatible.tsp:966](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/back-compatible.tsp#L966-L969)

```typespec
@@clientName(
  ApiManagementServiceResources.quotaByCounterKeysUpdate::parameters.body,
  "parameters"
);
```

[specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/back-compatible.tsp:1931](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/back-compatible.tsp#L1931-L1934)

```typespec
@@clientName(
  ApiManagementServiceResources.quotaByCounterKeysUpdate::parameters.body,
  "parameters"
);
```

[specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/ApiManagementServiceResource.tsp:479](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/ApiManagementServiceResource.tsp#L479-L490)

```typespec
   * Updates all the quota counter values specified with the existing quota counter key to a value in the specified service instance. This should be used for reset of the quota counter values.
   */
  #suppress "@azure-tools/typespec-azure-resource-manager/use-operation-decorator" "FIXME: review suppression and update justification"
  #suppress "@azure-tools/typespec-azure-resource-manager/use-api-version" "FIXME: review suppression and update justification"
  #suppress "@azure-tools/typespec-azure-resource-manager/use-interface" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  @patch(#{ implicitOptionality: false })
  @route("/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/quotas/{quotaCounterKey}")
  quotaByCounterKeysUpdate is QuotaCounterKeyOps.ActionSync<
    ApiManagementServiceResource,
    Request = QuotaCounterValueUpdateContract,
    Response = ArmResponse<QuotaCounterCollection>
  >;
```

**Retained Swagger or projection evidence**

`projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`; exact pointer segments:

```json
[
  "paths",
  "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/quotas/{quotaCounterKey}",
  "patch",
  "parameters"
]
```

```json
[
  {
    "$ref": "../../../../../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
  },
  {
    "$ref": "../../../../../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
  },
  {
    "$ref": "../../../../../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
  },
  {
    "name": "serviceName",
    "in": "path",
    "description": "The name of the API Management service.",
    "required": true,
    "type": "string",
    "minLength": 1,
    "maxLength": 50,
    "pattern": "^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$"
  },
  {
    "name": "quotaCounterKey",
    "in": "path",
    "description": "Quota counter key identifier. This is the result of expression defined in `counter-key` attribute of the quota-by-key policy. For example, if you specify `counter-key=\"boo\"` in the policy, then it\u2019s accessible by `\"boo\"` counter key. But if it\u2019s defined as `counter-key=\"@(\"b\"+\"a\")\"` then it will be accessible by `\"ba\"` key.",
    "required": true,
    "type": "string"
  },
  {
    "name": "parameters",
    "in": "body",
    "description": "The value of the quota counter to be applied to all quota counter periods.",
    "required": true,
    "schema": {
      "$ref": "#/definitions/QuotaCounterValueUpdateContract"
    }
  }
]
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 2 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Remove at most the duplicate application, retaining the meaningful remaining rename; do not recommend blindly deleting both warnings at once.

## containerapps-scoped-repeat

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/app/resource-manager/Microsoft.App/ContainerApps` / `2026-07-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 1.
- **Cause:** scope-layer-not-extension-equality.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** The C# application repeats the common ScheduledEntries override. The common case-only rename remains meaningful and is not reported. The retained property key is scheduledEntries and x-ms-client-name is ScheduledEntries; strict case-sensitive extension equality is false. The saved Swagger has no language-scope application layer.

**Captured source applications**

| Source                                                                                                                                                                                                                                                              | Exact authored excerpt                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| [specification/app/resource-manager/Microsoft.App/ContainerApps/client.tsp:1189](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/app/resource-manager/Microsoft.App/ContainerApps/client.tsp#L1189-L1197) | `@@clientName(ScheduledEntries.scheduledEntries, "ScheduledEntries", "csharp");` |

**TypeSpec source and supporting declarations**

[specification/app/resource-manager/Microsoft.App/ContainerApps/client.tsp:1189](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/app/resource-manager/Microsoft.App/ContainerApps/client.tsp#L1189-L1189)

```typespec
@@clientName(ScheduledEntries.scheduledEntries, "ScheduledEntries", "csharp");
```

[specification/app/resource-manager/Microsoft.App/ContainerApps/back-compatible.tsp:331](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/app/resource-manager/Microsoft.App/ContainerApps/back-compatible.tsp#L331-L334)

```typespec
@@doc(Operations.list, "Lists all of the available RP operations.");
@@Azure.ResourceManager.identifiers(AvailableOperations.value, #["name"]);
@@Azure.ResourceManager.identifiers(ListUsagesResult.value, #["name"]);
@@clientName(ScheduledEntries.scheduledEntries, "ScheduledEntries");
```

[specification/app/resource-manager/Microsoft.App/ContainerApps/models.tsp:3832](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/app/resource-manager/Microsoft.App/ContainerApps/models.tsp#L3832-L3839)

```typespec
model ScheduledEntries {
  /**
   * List of maintenance schedules for a managed environment.
   */
  #suppress "@azure-tools/typespec-client-generator-core/property-name-conflict" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  @identifiers(#[])
  scheduledEntries: ScheduledEntry[];
}
```

**Retained Swagger or projection evidence**

`projects/specification/app/resource-manager/Microsoft.App/ContainerApps/swagger/stable/2026-07-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "ScheduledEntries",
  "properties",
  "scheduledEntries"
]
```

```json
{
  "type": "array",
  "description": "List of maintenance schedules for a managed environment.",
  "items": {
    "$ref": "#/definitions/ScheduledEntry"
  },
  "x-ms-client-name": "ScheduledEntries",
  "x-ms-identifiers": []
}
```

`projects/specification/app/resource-manager/Microsoft.App/ContainerApps/swagger/stable/2026-07-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "ScheduledEntries",
  "properties",
  "scheduledEntries"
]
```

```json
{
  "type": "array",
  "description": "List of maintenance schedules for a managed environment.",
  "items": {
    "$ref": "#/definitions/ScheduledEntry"
  },
  "x-ms-client-name": "ScheduledEntries",
  "x-ms-identifiers": []
}
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 1 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** SDK/spec owner may remove only the redundant C# repeat, preserving the common case-only rename; do not alter rule semantics to suppress the finding.

## batch-removed-certificates

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/batch/resource-manager/Microsoft.Batch/Batch` / `2025-06-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 2.
- **Cause:** older-version-source.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** CertificateProperties and CertificateCreateOrUpdateProperties both extend CertificateBaseProperties and both augment its inherited thumbprint with the identical C# ThumbprintString spelling. All three models are removed at v2025_06_01, the selected API version. Retained Swagger contains no certificate thumbprint property.

**Captured source applications**

| Source                                                                                                                                                                                                                                                   | Exact authored excerpt                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| [specification/batch/resource-manager/Microsoft.Batch/Batch/client.tsp:130](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/batch/resource-manager/Microsoft.Batch/Batch/client.tsp#L130-L138) | `@@clientName(CertificateProperties.thumbprint, "ThumbprintString", "csharp");`                 |
| [specification/batch/resource-manager/Microsoft.Batch/Batch/client.tsp:416](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/batch/resource-manager/Microsoft.Batch/Batch/client.tsp#L416-L424) | `@@clientName( CertificateCreateOrUpdateProperties.thumbprint, "ThumbprintString", "csharp" );` |

**TypeSpec source and supporting declarations**

[specification/batch/resource-manager/Microsoft.Batch/Batch/models.tsp:1868](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/batch/resource-manager/Microsoft.Batch/Batch/models.tsp#L1868-L1870)

```typespec
@removed(Versions.v2025_06_01)
model CertificateProperties extends CertificateBaseProperties {
  /**
```

[specification/batch/resource-manager/Microsoft.Batch/Batch/models.tsp:1940](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/batch/resource-manager/Microsoft.Batch/Batch/models.tsp#L1940-L1953)

```typespec
@removed(Versions.v2025_06_01)
model CertificateBaseProperties {
  /**
   * This must match the first portion of the certificate name. Currently required to be 'SHA1'.
   */
  @summary("The algorithm of the certificate thumbprint.")
  thumbprintAlgorithm?: string;

  /**
   * This must match the thumbprint from the name.
   */
  @summary("The thumbprint of the certificate.")
  thumbprint?: string;
```

[specification/batch/resource-manager/Microsoft.Batch/Batch/models.tsp:1979](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/batch/resource-manager/Microsoft.Batch/Batch/models.tsp#L1979-L1981)

```typespec
@removed(Versions.v2025_06_01)
model CertificateCreateOrUpdateProperties extends CertificateBaseProperties {
  /**
```

**Retained Swagger or projection evidence**

No exact selected-version Swagger object is asserted for this group.
Removed declarations are established by the quoted version decorators.
Copied declarations and SDK-only scopes are established by the exact
source-copy/application chain, not inferred emitted-name matching.

Exact schema/property lookups absent from the selected Swagger:
`[["CertificateCreateOrUpdateProperties", "thumbprint"], ["CertificateProperties", "thumbprint"]]`.
An absent lookup is not a predicate-failure or correspondence claim.

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 2 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Retain both source-profile warnings. SDK/service owners may remove at most one duplicate inherited-property application after checking older-version compatibility; do not delete the meaningful remaining rename or claim same-version Swagger correspondence.

## billing-shadowed-inherited-overrides

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/billing/resource-manager/Microsoft.Billing/Billing` / `2024-04-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 2.
- **Cause:** shadowed-sdk-application.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** BillingSubscriptionAliasProperties extends BillingSubscriptionProperties. The inherited beneficiaryTenantId and customerId properties are not distinct alias declarations. Earlier alias-target C# overrides are superseded by later base-target BeneficiaryTenantId and CustomerId overrides. The exact BillingSubscriptionProperties Swagger properties contain no x-ms-client-name.

**Captured source applications**

| Source                                                                                                                                                                                                                                                               | Exact authored excerpt                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| [specification/billing/resource-manager/Microsoft.Billing/Billing/client.tsp:258](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/billing/resource-manager/Microsoft.Billing/Billing/client.tsp#L258-L266) | `@@clientName( BillingSubscriptionAliasProperties.beneficiaryTenantId, "SubscriptionAliasBeneficiaryTenantId", "csharp" );` |
| [specification/billing/resource-manager/Microsoft.Billing/Billing/client.tsp:268](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/billing/resource-manager/Microsoft.Billing/Billing/client.tsp#L268-L276) | `@@clientName( BillingSubscriptionAliasProperties.customerId, "SubscriptionAliasCustomerId", "csharp" );`                   |

**TypeSpec source and supporting declarations**

[specification/billing/resource-manager/Microsoft.Billing/Billing/models.tsp:5937](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/billing/resource-manager/Microsoft.Billing/Billing/models.tsp#L5937-L5942)

```typespec
model BillingSubscriptionAliasProperties extends BillingSubscriptionProperties {
  /**
   * The ID of the billing subscription with the subscription alias.
   */
  @visibility(Lifecycle.Read)
  billingSubscriptionId?: string;
```

[specification/billing/resource-manager/Microsoft.Billing/Billing/client.tsp:258](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/billing/resource-manager/Microsoft.Billing/Billing/client.tsp#L258-L278)

```typespec
@@clientName(
  BillingSubscriptionAliasProperties.beneficiaryTenantId,
  "SubscriptionAliasBeneficiaryTenantId",
  "csharp"
);
@@clientName(
  BillingSubscriptionAliasProperties.billingSubscriptionId,
  "SubscriptionAliasSubscriptionId",
  "csharp"
);
@@clientName(
  BillingSubscriptionAliasProperties.customerId,
  "SubscriptionAliasCustomerId",
  "csharp"
);
@@clientName(
  BillingSubscriptionProperties.beneficiaryTenantId,
  "BeneficiaryTenantId",
  "csharp"
);
@@clientName(BillingSubscriptionProperties.customerId, "CustomerId", "csharp");
```

**Retained Swagger or projection evidence**

`projects/specification/billing/resource-manager/Microsoft.Billing/Billing/swagger/stable/2024-04-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "BillingSubscriptionProperties",
  "properties",
  "beneficiaryTenantId"
]
```

```json
{
  "type": "string",
  "description": "The provisioning tenant of the subscription."
}
```

`projects/specification/billing/resource-manager/Microsoft.Billing/Billing/swagger/stable/2024-04-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "BillingSubscriptionProperties",
  "properties",
  "customerId"
]
```

```json
{
  "type": "string",
  "description": "The fully qualified ID that uniquely identifies a customer."
}
```

Exact schema/property lookups absent from the selected Swagger:
`[["BillingSubscriptionAliasProperties", "beneficiaryTenantId"], ["BillingSubscriptionAliasProperties", "customerId"]]`.
An absent lookup is not a predicate-failure or correspondence claim.

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 2 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** SDK/service owners can remove the shadowed applications, or separately review the inheritance/customization intent. Do not silently change the winning base override to force parity.

## cdn-copy-source-repeats

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/cdn/resource-manager/Microsoft.Cdn/Cdn` / `2026-10-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 3.
- **Cause:** copy-source-sdk-repeat.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** AFDDomainProperties spreads AFDDomainUpdatePropertiesParameters; AFDOriginProperties spreads AFDOriginUpdatePropertiesParameters. Each reported copy-target C# spelling is also applied to its source property with the identical scope/value. The captured no-effect checks report the copy-target applications only. Exact retained schemas preserve azureDnsZone, preValidatedCustomDomainResourceId and azureOrigin without x-ms-client-name.

**Captured source applications**

| Source                                                                                                                                                                                                                                          | Exact authored excerpt                                                                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| [specification/cdn/resource-manager/Microsoft.Cdn/Cdn/client.tsp:1459](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/client.tsp#L1459-L1467) | `@@clientName(AFDDomainProperties.azureDnsZone, "DnsZone", "csharp");`                                                  |
| [specification/cdn/resource-manager/Microsoft.Cdn/Cdn/client.tsp:1465](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/client.tsp#L1465-L1473) | `@@clientName( AFDDomainProperties.preValidatedCustomDomainResourceId, "PreValidatedCustomDomainResource", "csharp" );` |
| [specification/cdn/resource-manager/Microsoft.Cdn/Cdn/client.tsp:1475](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/client.tsp#L1475-L1483) | `@@clientName(AFDOriginProperties.azureOrigin, "Origin", "csharp");`                                                    |

**TypeSpec source and supporting declarations**

[specification/cdn/resource-manager/Microsoft.Cdn/Cdn/models.tsp:2722](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/models.tsp#L2722-L2724)

```typespec
model AFDDomainProperties {
  ...AFDDomainUpdatePropertiesParameters;
  ...AFDStateProperties;
```

[specification/cdn/resource-manager/Microsoft.Cdn/Cdn/models.tsp:3159](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/models.tsp#L3159-L3162)

```typespec
model AFDOriginProperties {
  ...AFDOriginUpdatePropertiesParameters;
  ...AFDStateProperties;
}
```

[specification/cdn/resource-manager/Microsoft.Cdn/Cdn/client.tsp:1459](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/client.tsp#L1459-L1479)

```typespec
@@clientName(AFDDomainProperties.azureDnsZone, "DnsZone", "csharp");
@@clientName(
  AFDDomainUpdatePropertiesParameters.azureDnsZone,
  "DnsZone",
  "csharp"
);
@@clientName(
  AFDDomainProperties.preValidatedCustomDomainResourceId,
  "PreValidatedCustomDomainResource",
  "csharp"
);
@@clientName(
  AFDDomainUpdatePropertiesParameters.preValidatedCustomDomainResourceId,
  "PreValidatedCustomDomainResource",
  "csharp"
);
@@clientName(AFDOriginProperties.azureOrigin, "Origin", "csharp");
@@clientName(
  AFDOriginUpdatePropertiesParameters.azureOrigin,
  "Origin",
  "csharp"
```

**Retained Swagger or projection evidence**

`projects/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/swagger/stable/2026-10-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "AFDDomainProperties",
  "properties",
  "azureDnsZone"
]
```

```json
{
  "$ref": "#/definitions/ResourceReference",
  "description": "Resource reference to the Azure DNS zone"
}
```

`projects/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/swagger/stable/2026-10-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "AFDDomainProperties",
  "properties",
  "preValidatedCustomDomainResourceId"
]
```

```json
{
  "$ref": "#/definitions/ResourceReference",
  "description": "Resource reference to the Azure resource where custom domain ownership was prevalidated"
}
```

`projects/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/swagger/stable/2026-10-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "AFDOriginProperties",
  "properties",
  "azureOrigin"
]
```

```json
{
  "$ref": "#/definitions/ResourceReference",
  "description": "Resource reference to the Azure origin resource."
}
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 3 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** SDK/service owners can remove only the reported copy-target repeats while retaining effective source-property renames. No TypeSpec rule edit is proposed.

## confidentialledger-removed-managedccf

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger` / `2026-05-22-preview`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 8.
- **Cause:** older-version-source.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** ManagedCCF and the entire ManagedCCFs interface are removed at v2026_02_23, before selected API version 2026-05-22-preview. Each of create.resource, update.properties, backup.body and restore.body has two identical unscoped ManagedCCF applications. All eight raw warnings remain source observations; selected latest-version Swagger cannot preserve removed operations.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                                                                                | Exact authored excerpt                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| [specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/back-compatible.tsp:23](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/back-compatible.tsp#L23-L31) | `@@clientName(ManagedCCFs.create::parameters.resource, "ManagedCCF");`   |
| [specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/back-compatible.tsp:38](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/back-compatible.tsp#L38-L46) | `@@clientName(ManagedCCFs.create::parameters.resource, "ManagedCCF");`   |
| [specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/back-compatible.tsp:24](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/back-compatible.tsp#L24-L32) | `@@clientName(ManagedCCFs.update::parameters.properties, "ManagedCCF");` |
| [specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/back-compatible.tsp:40](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/back-compatible.tsp#L40-L47) | `@@clientName(ManagedCCFs.update::parameters.properties, "ManagedCCF");` |
| [specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/back-compatible.tsp:25](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/back-compatible.tsp#L25-L33) | `@@clientName(ManagedCCFs.backup::parameters.body, "ManagedCCF");`       |
| [specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/back-compatible.tsp:45](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/back-compatible.tsp#L45-L47) | `@@clientName(ManagedCCFs.backup::parameters.body, "ManagedCCF");`       |
| [specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/back-compatible.tsp:26](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/back-compatible.tsp#L26-L34) | `@@clientName(ManagedCCFs.restore::parameters.body, "ManagedCCF");`      |
| [specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/back-compatible.tsp:47](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/back-compatible.tsp#L47-L47) | `@@clientName(ManagedCCFs.restore::parameters.body, "ManagedCCF");`      |

**TypeSpec source and supporting declarations**

[specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/ManagedCCF.tsp:18](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/ManagedCCF.tsp#L18-L33)

```typespec
#suppress "@azure-tools/typespec-azure-core/casing-style" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
@removed(Versions.v2026_02_23)
model ManagedCCF
  is Azure.ResourceManager.TrackedResource<ManagedCCFProperties> {
  ...ResourceNameParameter<
    Resource = ManagedCCF,
    KeyName = "appName",
    SegmentName = "managedCCFs",
    NamePattern = "^[a-zA-Z0-9]"
  >;
}

#suppress "@azure-tools/typespec-azure-core/casing-style" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
@removed(Versions.v2026_02_23)
@armResourceOperations
interface ManagedCCFs {
```

[specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/back-compatible.tsp:23](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger/back-compatible.tsp#L23-L47)

```typespec
@@clientName(ManagedCCFs.create::parameters.resource, "ManagedCCF");
@@clientName(ManagedCCFs.update::parameters.properties, "ManagedCCF");
@@clientName(ManagedCCFs.backup::parameters.body, "ManagedCCF");
@@clientName(ManagedCCFs.restore::parameters.body, "ManagedCCF");
@@clientName(checkNameAvailability::parameters.body, "nameAvailabilityRequest");
@@clientLocation(ConfidentialLedgers.get, "Ledger");
@@clientLocation(ConfidentialLedgers.create, "Ledger");
@@clientLocation(ConfidentialLedgers.update, "Ledger");
@@clientLocation(ConfidentialLedgers.delete, "Ledger");
@@clientLocation(ConfidentialLedgers.listByResourceGroup, "Ledger");
@@clientLocation(ConfidentialLedgers.listBySubscription, "Ledger");
@@clientLocation(ConfidentialLedgers.filesExport, "Ledger");
@@clientLocation(ConfidentialLedgerRestoreOps.restore, "Ledger");
@@clientLocation(ManagedCCFs.get, "ManagedCCF");
@@clientLocation(ManagedCCFs.create, "ManagedCCF");
@@clientName(ManagedCCFs.create::parameters.resource, "ManagedCCF");
@@clientLocation(ManagedCCFs.update, "ManagedCCF");
@@clientName(ManagedCCFs.update::parameters.properties, "ManagedCCF");
@@clientLocation(ManagedCCFs.delete, "ManagedCCF");
@@clientLocation(ManagedCCFs.listByResourceGroup, "ManagedCCF");
@@clientLocation(ManagedCCFs.listBySubscription, "ManagedCCF");
@@clientLocation(ManagedCCFs.backup, "ManagedCCF");
@@clientName(ManagedCCFs.backup::parameters.body, "ManagedCCF");
@@clientLocation(ManagedCCFs.restore, "ManagedCCF");
@@clientName(ManagedCCFs.restore::parameters.body, "ManagedCCF");
```

**Retained Swagger or projection evidence**

No exact selected-version Swagger object is asserted for this group.
Removed declarations are established by the quoted version decorators.
Copied declarations and SDK-only scopes are established by the exact
source-copy/application chain, not inferred emitted-name matching.

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 8 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Retain the eight source-profile warnings and version limit. If a service owner cleans duplicates, remove at most one application per target, retaining meaningful older-version names.

## connectedcache-shadowed-inline-name

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/connectedcache/resource-manager/Microsoft.ConnectedCache/ConnectedCache` / `2026-06-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 1.
- **Cause:** shadowed-sdk-application.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** AdditionalCustomerProperties.peeringDbLastUpdateDate has inline C# peeringDbLastUpdateDateValue, then client.tsp augments the same authored property with peeringDBLastUpdatedOn. The differing inline spelling is shadowed, not a meaningful final rename. The selected Swagger property has no SDK-scope application history.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                                         | Exact authored excerpt                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [specification/connectedcache/resource-manager/Microsoft.ConnectedCache/ConnectedCache/models.tsp:358](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/connectedcache/resource-manager/Microsoft.ConnectedCache/ConnectedCache/models.tsp#L358-L366) | `@Azure.ClientGenerator.Core.clientName( "peeringDbLastUpdateDateValue", "csharp" ) peeringDbLastUpdateDate?: utcDateTime;  @doc("Customer resource owner organization name.") @visibility(Lifecycle.Read) customerOrgName?: string;` |

**TypeSpec source and supporting declarations**

[specification/connectedcache/resource-manager/Microsoft.ConnectedCache/ConnectedCache/models.tsp:353](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/connectedcache/resource-manager/Microsoft.ConnectedCache/ConnectedCache/models.tsp#L353-L362)

```typespec
  @visibility(Lifecycle.Read)
  signupPhaseStatusText?: string;

  @doc("Customer resource last PeeringDB update timestamp.")
  @visibility(Lifecycle.Read)
  @Azure.ClientGenerator.Core.clientName(
    "peeringDbLastUpdateDateValue",
    "csharp"
  )
  peeringDbLastUpdateDate?: utcDateTime;
```

[specification/connectedcache/resource-manager/Microsoft.ConnectedCache/ConnectedCache/client.tsp:35](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/connectedcache/resource-manager/Microsoft.ConnectedCache/ConnectedCache/client.tsp#L35-L39)

```typespec
@@clientName(
  AdditionalCustomerProperties.peeringDbLastUpdateDate,
  "peeringDBLastUpdatedOn",
  "csharp"
);
```

**Retained Swagger or projection evidence**

`projects/specification/connectedcache/resource-manager/Microsoft.ConnectedCache/ConnectedCache/swagger/stable/2026-06-01/ConnectedCache.json`; exact pointer segments:

```json
[
  "definitions",
  "AdditionalCustomerProperties",
  "properties",
  "peeringDbLastUpdateDate"
]
```

```json
{
  "type": "string",
  "format": "date-time",
  "description": "Customer resource last PeeringDB update timestamp.",
  "readOnly": true
}
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 1 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** SDK/service owners can remove the shadowed inline application; preserve the effective augment. If the intended name differs, that is a separate SDK naming review, not a count-parity fix.

## consumption-inherited-scope-repeat

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/consumption/resource-manager/Microsoft.Consumption/Consumption` / `2026-06-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 2.
- **Cause:** inherited-sdk-repeat.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** ModernChargeSummary and LegacyChargeSummary extend ChargeSummary and do not redeclare eTag. Both Java etag augmentations repeat the Java component of ChargeSummary.eTag's java,python application. The retained exact ChargeSummary.eTag property contains no x-ms-client-name.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                    | Exact authored excerpt                                    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| [specification/consumption/resource-manager/Microsoft.Consumption/Consumption/client.tsp:16](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/consumption/resource-manager/Microsoft.Consumption/Consumption/client.tsp#L16-L24) | `@@clientName(ModernChargeSummary.eTag, "etag", "java");` |
| [specification/consumption/resource-manager/Microsoft.Consumption/Consumption/client.tsp:18](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/consumption/resource-manager/Microsoft.Consumption/Consumption/client.tsp#L18-L26) | `@@clientName(LegacyChargeSummary.eTag, "etag", "java");` |

**TypeSpec source and supporting declarations**

[specification/consumption/resource-manager/Microsoft.Consumption/Consumption/client.tsp:14](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/consumption/resource-manager/Microsoft.Consumption/Consumption/client.tsp#L14-L18)

```typespec
// Fix property name changes from lowercase to uppercase (etag -> eTag)
@@clientName(LotSummary.eTag, "etag", "java");
@@clientName(ModernChargeSummary.eTag, "etag", "java");
@@clientName(ChargeSummary.eTag, "etag", "java,python");
@@clientName(LegacyChargeSummary.eTag, "etag", "java");
```

[specification/consumption/resource-manager/Microsoft.Consumption/Consumption/models.tsp:911](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/consumption/resource-manager/Microsoft.Consumption/Consumption/models.tsp#L911-L922)

```typespec
model ChargeSummary extends Azure.ResourceManager.Foundations.ProxyResource {
  /**
   * Specifies the kind of charge summary.
   */
  kind: ChargeSummaryKind;

  /**
   * eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
   */
  eTag?: string;
}
```

[specification/consumption/resource-manager/Microsoft.Consumption/Consumption/models.tsp:4041](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/consumption/resource-manager/Microsoft.Consumption/Consumption/models.tsp#L4041-L4051)

```typespec
model LegacyChargeSummary extends ChargeSummary {
  /**
   * Properties for legacy charge summary
   */
  properties: LegacyChargeSummaryProperties;

  /**
   * Specifies the kind of charge summary.
   */
  kind: "legacy";
}
```

[specification/consumption/resource-manager/Microsoft.Consumption/Consumption/models.tsp:4106](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/consumption/resource-manager/Microsoft.Consumption/Consumption/models.tsp#L4106-L4116)

```typespec
model ModernChargeSummary extends ChargeSummary {
  /**
   * Properties for modern charge summary
   */
  properties: ModernChargeSummaryProperties;

  /**
   * Specifies the kind of charge summary.
   */
  kind: "modern";
}
```

**Retained Swagger or projection evidence**

`projects/specification/consumption/resource-manager/Microsoft.Consumption/Consumption/swagger/stable/2026-06-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "ChargeSummary",
  "properties",
  "eTag"
]
```

```json
{
  "type": "string",
  "description": "eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not."
}
```

Exact schema/property lookups absent from the selected Swagger:
`[["LegacyChargeSummary", "eTag"], ["ModernChargeSummary", "eTag"]]`.
An absent lookup is not a predicate-failure or correspondence claim.

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 2 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** SDK/service owners can remove the two inherited Java repeats while preserving the base java,python rename.

## aks-body-common-repeat

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/containerservice/resource-manager/Microsoft.ContainerService/aks` / `2026-09-02-preview`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 1.
- **Cause:** body-name-application-collapse.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** ManagedClusters.post::parameters.body has both common parameters and !csharp parameters applications. The captured warning selects the common application under actual negation-state precedence. The authored @action resolvePrivateLinkServiceId identifies the retained POST operation ResolvePrivateLinkServiceId_POST. Its body name is parameters, schema PrivateLinkResource, with no x-ms-client-name.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                                           | Exact authored excerpt                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| [specification/containerservice/resource-manager/Microsoft.ContainerService/aks/BackCompatible.tsp:145](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/BackCompatible.tsp#L145-L153) | `@@clientName(ManagedClusters.post::parameters.body, "parameters");` |

**TypeSpec source and supporting declarations**

[specification/containerservice/resource-manager/Microsoft.ContainerService/aks/BackCompatible.tsp:144](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/BackCompatible.tsp#L144-L145)

```typespec
@@clientName(ManagedClusters.post, "POST");
@@clientName(ManagedClusters.post::parameters.body, "parameters");
```

[specification/containerservice/resource-manager/Microsoft.ContainerService/aks/BackCompatible.tsp:171](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/BackCompatible.tsp#L171-L174)

```typespec
@@clientName(ManagedClusters.privateLinkResourcesList, "List", "!csharp");
@@clientName(ManagedClusters.post, "POST", "!csharp");
@@clientName(ManagedClusters.post::parameters.body, "parameters", "!csharp");
@@clientName(ManagedClusters.operationStatusResultList, "List", "!csharp");
```

[specification/containerservice/resource-manager/Microsoft.ContainerService/aks/ManagedCluster.tsp:631](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/ManagedCluster.tsp#L631-L640)

```typespec
  /**
   * Gets the private link service ID for the specified managed cluster.
   */
  @tag("resolvePrivateLinkServiceId")
  @action("resolvePrivateLinkServiceId")
  post is ArmResourceActionSync<
    ManagedCluster,
    PrivateLinkResource,
    ArmResponse<PrivateLinkResource>
  >;
```

**Retained Swagger or projection evidence**

`projects/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/swagger/preview/2026-09-02-preview/managedClusters.json`; exact pointer segments:

```json
[
  "paths",
  "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/resolvePrivateLinkServiceId",
  "post",
  "parameters"
]
```

```json
[
  {
    "name": "parameters",
    "in": "body",
    "description": "Parameters required in order to resolve a private link service ID.",
    "required": true,
    "schema": {
      "$ref": "#/definitions/PrivateLinkResource"
    }
  }
]
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 1 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** SDK/service owners can remove only the reported common repeat after confirming intended scoped names; preserve the effective remaining scope application.

## aks-duplicate-enabled

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/containerservice/resource-manager/Microsoft.ContainerService/aks` / `2026-09-02-preview`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 2.
- **Cause:** duplicate-scoped-sdk-applications.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** The same ManagedClusterAzureMonitorProfileAppMonitoringAutoInstrumentation.enabled C# IsAppMonitoringAutoInstrumentationEnabled application is authored twice. Both independently removable warnings are retained. The exact emitted enabled property does not retain source-application multiplicity.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                              | Exact authored excerpt                                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| [specification/containerservice/resource-manager/Microsoft.ContainerService/aks/client.tsp:1255](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/client.tsp#L1255-L1263) | `@@clientName( ManagedClusterAzureMonitorProfileAppMonitoringAutoInstrumentation.enabled, "IsAppMonitoringAutoInstrumentationEnabled", "csharp" );` |
| [specification/containerservice/resource-manager/Microsoft.ContainerService/aks/client.tsp:1260](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/client.tsp#L1260-L1268) | `@@clientName( ManagedClusterAzureMonitorProfileAppMonitoringAutoInstrumentation.enabled, "IsAppMonitoringAutoInstrumentationEnabled", "csharp" );` |

**TypeSpec source and supporting declarations**

[specification/containerservice/resource-manager/Microsoft.ContainerService/aks/client.tsp:1255](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/client.tsp#L1255-L1264)

```typespec
@@clientName(
  ManagedClusterAzureMonitorProfileAppMonitoringAutoInstrumentation.enabled,
  "IsAppMonitoringAutoInstrumentationEnabled",
  "csharp"
);
@@clientName(
  ManagedClusterAzureMonitorProfileAppMonitoringAutoInstrumentation.enabled,
  "IsAppMonitoringAutoInstrumentationEnabled",
  "csharp"
);
```

[specification/containerservice/resource-manager/Microsoft.ContainerService/aks/CommonModels.tsp:4161](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/CommonModels.tsp#L4161-L4168)

```typespec
@added(Versions.v2026_02_01)
model ManagedClusterAzureMonitorProfileAppMonitoringAutoInstrumentation {
  /**
   * Indicates if Application Monitoring Auto-instrumentation is enabled or not.
   */
  enabled?: boolean;
}
```

**Retained Swagger or projection evidence**

`projects/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/swagger/preview/2026-09-02-preview/managedClusters.json`; exact pointer segments:

```json
[
  "definitions",
  "ManagedClusterAzureMonitorProfileAppMonitoringAutoInstrumentation",
  "properties",
  "enabled"
]
```

```json
{
  "type": "boolean",
  "description": "Indicates if Application Monitoring Auto-instrumentation is enabled or not."
}
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 2 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Remove at most one duplicate after service-owner review. Preserve the meaningful remaining C# rename.

## aks-shadowed-csharp-override

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/containerservice/resource-manager/Microsoft.ContainerService/aks` / `2026-09-02-preview`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 1.
- **Cause:** shadowed-sdk-application.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** SysctlConfig.netIpv4IpLocalPortRange first receives NetIpv4IPLocalPortRange for C#, then a later application assigns NetIPv4IPLocalPortRange with a trailing space. The earlier override is shadowed and removable; the warning is not an endorsement of the later spelling or trailing space.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                              | Exact authored excerpt                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| [specification/containerservice/resource-manager/Microsoft.ContainerService/aks/client.tsp:1142](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/client.tsp#L1142-L1150) | `@@clientName( SysctlConfig.netIpv4IpLocalPortRange, "NetIpv4IPLocalPortRange", "csharp" );` |

**TypeSpec source and supporting declarations**

[specification/containerservice/resource-manager/Microsoft.ContainerService/aks/client.tsp:1142](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/client.tsp#L1142-L1146)

```typespec
@@clientName(
  SysctlConfig.netIpv4IpLocalPortRange,
  "NetIpv4IPLocalPortRange",
  "csharp"
);
```

[specification/containerservice/resource-manager/Microsoft.ContainerService/aks/client.tsp:1192](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/client.tsp#L1192-L1196)

```typespec
@@clientName(
  SysctlConfig.netIpv4IpLocalPortRange,
  "NetIPv4IPLocalPortRange ",
  "csharp"
);
```

**Retained Swagger or projection evidence**

`projects/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/swagger/preview/2026-09-02-preview/managedClusters.json`; exact pointer segments:

```json
[
  "definitions",
  "SysctlConfig",
  "properties",
  "netIpv4IpLocalPortRange"
]
```

```json
{
  "type": "string",
  "description": "Sysctl setting net.ipv4.ip_local_port_range."
}
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 1 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** SDK/service owners can remove the earlier shadowed application. Review the winning trailing-space spelling separately for compatibility; do not silently repair it in this migration.

## databox-duplicate-csharp

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/databox/resource-manager/Microsoft.DataBox/DataBox` / `2025-07-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 2.
- **Cause:** duplicate-scoped-sdk-applications.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** JobDetails.datacenterAddress has two identical C# DataCenterAddress applications. Both raw warnings are retained. The exact retained Swagger property lacks x-ms-client-name.

**Captured source applications**

| Source                                                                                                                                                                                                                                                               | Exact authored excerpt                                                       |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| [specification/databox/resource-manager/Microsoft.DataBox/DataBox/client.tsp:144](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/databox/resource-manager/Microsoft.DataBox/DataBox/client.tsp#L144-L152) | `@@clientName(JobDetails.datacenterAddress, "DataCenterAddress", "csharp");` |
| [specification/databox/resource-manager/Microsoft.DataBox/DataBox/client.tsp:262](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/databox/resource-manager/Microsoft.DataBox/DataBox/client.tsp#L262-L270) | `@@clientName(JobDetails.datacenterAddress, "DataCenterAddress", "csharp");` |

**TypeSpec source and supporting declarations**

[specification/databox/resource-manager/Microsoft.DataBox/DataBox/client.tsp:144](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/databox/resource-manager/Microsoft.DataBox/DataBox/client.tsp#L144-L144)

```typespec
@@clientName(JobDetails.datacenterAddress, "DataCenterAddress", "csharp");
```

[specification/databox/resource-manager/Microsoft.DataBox/DataBox/client.tsp:262](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/databox/resource-manager/Microsoft.DataBox/DataBox/client.tsp#L262-L262)

```typespec
@@clientName(JobDetails.datacenterAddress, "DataCenterAddress", "csharp");
```

**Retained Swagger or projection evidence**

`projects/specification/databox/resource-manager/Microsoft.DataBox/DataBox/swagger/stable/2025-07-01/databox.json`; exact pointer segments:

```json
[
  "definitions",
  "JobDetails",
  "properties",
  "datacenterAddress"
]
```

```json
{
  "$ref": "#/definitions/DatacenterAddressResponse",
  "description": "Datacenter address to ship to, for the given sku and storage location.",
  "readOnly": true
}
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 2 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Remove at most one duplicate after service-owner review, preserving the meaningful remaining C# name.

## devtestlabs-duplicate-csharp

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs` / `2018-09-15`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 2.
- **Cause:** duplicate-scoped-sdk-applications.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** LabVirtualMachineCreationParameterProperties.disallowPublicIpAddress has two identical C# DisallowPublicIPAddress applications. Both raw warnings are retained. The exact retained Swagger property lacks x-ms-client-name.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                     | Exact authored excerpt                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| [specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/client.tsp:391](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/client.tsp#L391-L399) | `@@clientName( LabVirtualMachineCreationParameterProperties.disallowPublicIpAddress, "DisallowPublicIPAddress", "csharp" );` |
| [specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/client.tsp:568](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/client.tsp#L568-L576) | `@@clientName( LabVirtualMachineCreationParameterProperties.disallowPublicIpAddress, "DisallowPublicIPAddress", "csharp" );` |

**TypeSpec source and supporting declarations**

[specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/client.tsp:391](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/client.tsp#L391-L395)

```typespec
@@clientName(
  LabVirtualMachineCreationParameterProperties.disallowPublicIpAddress,
  "DisallowPublicIPAddress",
  "csharp"
);
```

[specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/client.tsp:568](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/client.tsp#L568-L572)

```typespec
@@clientName(
  LabVirtualMachineCreationParameterProperties.disallowPublicIpAddress,
  "DisallowPublicIPAddress",
  "csharp"
);
```

**Retained Swagger or projection evidence**

`projects/specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/swagger/stable/2018-09-15/DTL.json`; exact pointer segments:

```json
[
  "definitions",
  "LabVirtualMachineCreationParameterProperties",
  "properties",
  "disallowPublicIpAddress"
]
```

```json
{
  "type": "boolean",
  "description": "Indicates whether the virtual machine is to be created without a public IP address.",
  "default": false
}
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 2 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Remove at most one duplicate after service-owner review, preserving the meaningful remaining C# name.

## dns-identity-name

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/dns/resource-manager/Microsoft.Network/Dns` / `2023-07-01-preview`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 1.
- **Cause:** identity-sdk-name-not-emitted-extension.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** RecordSetProperties.ARecords receives the common identical ARecords name. A separate C# DnsARecords override remains effective either way. The exact retained Swagger ARecords property has no x-ms-client-name, so it is not selected by the Swagger rule.

**Captured source applications**

| Source                                                                                                                                                                                                                                                            | Exact authored excerpt                                    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| [specification/dns/resource-manager/Microsoft.Network/Dns/back-compatible.tsp:6](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/dns/resource-manager/Microsoft.Network/Dns/back-compatible.tsp#L6-L14) | `@@clientName(RecordSetProperties.ARecords, "ARecords");` |

**TypeSpec source and supporting declarations**

[specification/dns/resource-manager/Microsoft.Network/Dns/back-compatible.tsp:6](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/dns/resource-manager/Microsoft.Network/Dns/back-compatible.tsp#L6-L6)

```typespec
@@clientName(RecordSetProperties.ARecords, "ARecords");
```

[specification/dns/resource-manager/Microsoft.Network/Dns/client.tsp:43](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/dns/resource-manager/Microsoft.Network/Dns/client.tsp#L43-L44)

```typespec
@@clientName(RecordSetProperties.ARecords, "DnsARecords", "csharp");
@@clientName(RecordSetProperties.AAAARecords, "DnsAaaaRecords", "csharp");
```

[specification/dns/resource-manager/Microsoft.Network/Dns/models.tsp:196](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/dns/resource-manager/Microsoft.Network/Dns/models.tsp#L196-L202)

```typespec

  /**
   * The list of A records in the record set.
   */
  #suppress "@azure-tools/typespec-azure-core/casing-style" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  @identifiers(#[])
  ARecords?: ARecord[];
```

**Retained Swagger or projection evidence**

`projects/specification/dns/resource-manager/Microsoft.Network/Dns/swagger/preview/2023-07-01-preview/dns.json`; exact pointer segments:

```json
[
  "definitions",
  "RecordSetProperties",
  "properties",
  "ARecords"
]
```

```json
{
  "type": "array",
  "description": "The list of A records in the record set.",
  "items": {
    "$ref": "#/definitions/ARecord"
  },
  "x-ms-identifiers": []
}
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 1 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** SDK/service owners can remove the ineffective common identity override, preserving the C# rename.

## domainregistration-duplicate-csharp

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration` / `2024-11-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 2.
- **Cause:** duplicate-scoped-sdk-applications.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** TopLevelDomainAgreementOption.forTransfer has two identical C# IsForTransfer applications. Both raw warnings are retained. The exact retained Swagger property lacks x-ms-client-name.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                                                              | Exact authored excerpt                                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| [specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration/client.tsp:55](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration/client.tsp#L55-L63) | `@@clientName( TopLevelDomainAgreementOption.forTransfer, "IsForTransfer", "csharp" );` |
| [specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration/client.tsp:83](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration/client.tsp#L83-L91) | `@@clientName( TopLevelDomainAgreementOption.forTransfer, "IsForTransfer", "csharp" );` |

**TypeSpec source and supporting declarations**

[specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration/client.tsp:55](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration/client.tsp#L55-L59)

```typespec
@@clientName(
  TopLevelDomainAgreementOption.forTransfer,
  "IsForTransfer",
  "csharp"
);
```

[specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration/client.tsp:83](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration/client.tsp#L83-L87)

```typespec
@@clientName(
  TopLevelDomainAgreementOption.forTransfer,
  "IsForTransfer",
  "csharp"
);
```

**Retained Swagger or projection evidence**

`projects/specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration/swagger/stable/2024-11-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "TopLevelDomainAgreementOption",
  "properties",
  "forTransfer"
]
```

```json
{
  "type": "boolean",
  "description": "If <code>true</code>, then the list of agreements will include agreements for domain transfer as well; otherwise, <code>false</code>."
}
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 2 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Remove at most one duplicate after service-owner review, preserving the meaningful remaining C# name.

## frontdoor-inherited-java-duplicates

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/frontdoor/resource-manager/Microsoft.Network/FrontDoor` / `2026-04-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 2.
- **Cause:** inherited-sdk-repeat.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** FrontendEndpointProperties extends FrontendEndpointUpdateParameters without redeclaring hostName. Two Java hostname augmentations address the same inherited property. Both independently removable warnings remain distinct source applications.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                    | Exact authored excerpt                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| [specification/frontdoor/resource-manager/Microsoft.Network/FrontDoor/client.tsp:32](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/frontdoor/resource-manager/Microsoft.Network/FrontDoor/client.tsp#L32-L40) | `@@clientName(FrontendEndpointUpdateParameters.hostName, "hostname", "java");` |
| [specification/frontdoor/resource-manager/Microsoft.Network/FrontDoor/client.tsp:33](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/frontdoor/resource-manager/Microsoft.Network/FrontDoor/client.tsp#L33-L41) | `@@clientName(FrontendEndpointProperties.hostName, "hostname", "java");`       |

**TypeSpec source and supporting declarations**

[specification/frontdoor/resource-manager/Microsoft.Network/FrontDoor/client.tsp:31](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/frontdoor/resource-manager/Microsoft.Network/FrontDoor/client.tsp#L31-L33)

```typespec
@@clientName(ValidateCustomDomainInput.hostName, "hostname", "java");
@@clientName(FrontendEndpointUpdateParameters.hostName, "hostname", "java");
@@clientName(FrontendEndpointProperties.hostName, "hostname", "java");
```

[specification/frontdoor/resource-manager/Microsoft.Network/FrontDoor/models.tsp:3137](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/frontdoor/resource-manager/Microsoft.Network/FrontDoor/models.tsp#L3137-L3143)

```typespec
model FrontendEndpointProperties extends FrontendEndpointUpdateParameters {
  /**
   * Resource status.
   */
  @visibility(Lifecycle.Read)
  @summary("Resource status of the Front Door or Front Door SubResource.")
  resourceState?: FrontDoorResourceState;
```

[specification/frontdoor/resource-manager/Microsoft.Network/FrontDoor/models.tsp:3237](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/frontdoor/resource-manager/Microsoft.Network/FrontDoor/models.tsp#L3237-L3242)

```typespec
model FrontendEndpointUpdateParameters {
  /**
   * The host name of the frontendEndpoint. Must be a domain name.
   */
  hostName?: string;
```

**Retained Swagger or projection evidence**

`projects/specification/frontdoor/resource-manager/Microsoft.Network/FrontDoor/swagger/stable/2026-04-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "FrontendEndpointUpdateParameters",
  "properties",
  "hostName"
]
```

```json
{
  "type": "string",
  "description": "The host name of the frontendEndpoint. Must be a domain name."
}
```

Exact schema/property lookups absent from the selected Swagger:
`[["FrontendEndpointProperties", "hostName"]]`.
An absent lookup is not a predicate-failure or correspondence claim.

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 2 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Remove at most one duplicate after service-owner review. Preserve the meaningful remaining Java rename.

## help-duplicate-body-applications

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/help/resource-manager/Microsoft.Help/Help` / `2024-03-01-preview`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 8.
- **Cause:** body-name-application-collapse.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** Four exact body targets each have two identical common applications: DiagnosticResources.create.resource diagnosticResourceRequest; SolutionResources.create.resource solutionRequestBody; SolutionResources.update.properties solutionPatchRequestBody; SimplifiedSolutionsResources.create.resource simplifiedSolutionsRequestBody. The exact retained operations have those body names and no x-ms-client-name. All eight raw warnings are retained.

**Captured source applications**

| Source                                                                                                                                                                                                                                                            | Exact authored excerpt                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp:24](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp#L24-L32) | `@@clientName( DiagnosticResources.create::parameters.resource, "diagnosticResourceRequest" );`               |
| [specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp:65](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp#L65-L73) | `@@clientName( DiagnosticResources.create::parameters.resource, "diagnosticResourceRequest" );`               |
| [specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp:33](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp#L33-L41) | `@@clientName( SolutionResources.create::parameters.resource, "solutionRequestBody" );`                       |
| [specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp:75](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp#L75-L83) | `@@clientName( SolutionResources.create::parameters.resource, "solutionRequestBody" );`                       |
| [specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp:37](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp#L37-L45) | `@@clientName( SolutionResources.update::parameters.properties, "solutionPatchRequestBody" );`                |
| [specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp:80](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp#L80-L88) | `@@clientName( SolutionResources.update::parameters.properties, "solutionPatchRequestBody" );`                |
| [specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp:46](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp#L46-L54) | `@@clientName( SimplifiedSolutionsResources.create::parameters.resource, "simplifiedSolutionsRequestBody" );` |
| [specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp:70](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp#L70-L78) | `@@clientName( SimplifiedSolutionsResources.create::parameters.resource, "simplifiedSolutionsRequestBody" );` |

**TypeSpec source and supporting declarations**

[specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp:24](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp#L24-L50)

```typespec
@@clientName(
  DiagnosticResources.create::parameters.resource,
  "diagnosticResourceRequest"
);
#suppress "@azure-tools/typespec-azure-core/no-legacy-usage" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
@@Azure.ClientGenerator.Core.Legacy.flattenProperty(
  DiagnosticResource.properties
);

@@clientName(
  SolutionResources.create::parameters.resource,
  "solutionRequestBody"
);
@@clientName(
  SolutionResources.update::parameters.properties,
  "solutionPatchRequestBody"
);
#suppress "@azure-tools/typespec-azure-core/no-legacy-usage" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
@@Azure.ClientGenerator.Core.Legacy.flattenProperty(
  SolutionResource.properties
);

@@clientName(
  SimplifiedSolutionsResources.create::parameters.resource,
  "simplifiedSolutionsRequestBody"
);
#suppress "@azure-tools/typespec-azure-core/no-legacy-usage" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
```

[specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp:65](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/help/resource-manager/Microsoft.Help/Help/back-compatible.tsp#L65-L84)

```typespec
@@clientName(
  DiagnosticResources.create::parameters.resource,
  "diagnosticResourceRequest"
);

@@clientName(
  SimplifiedSolutionsResources.create::parameters.resource,
  "simplifiedSolutionsRequestBody"
);

@@clientName(
  SolutionResources.create::parameters.resource,
  "solutionRequestBody"
);

@@clientName(
  SolutionResources.update::parameters.properties,
  "solutionPatchRequestBody"
);
@@clientName(
```

**Retained Swagger or projection evidence**

`projects/specification/help/resource-manager/Microsoft.Help/Help/swagger/preview/2024-03-01-preview/help.json`; exact pointer segments:

```json
[
  "paths",
  "/{scope}/providers/Microsoft.Help/diagnostics/{diagnosticsResourceName}",
  "put",
  "parameters"
]
```

```json
[
  {
    "name": "diagnosticResourceRequest",
    "in": "body",
    "description": "The required request body for this insightResource invocation.",
    "required": false,
    "schema": {
      "$ref": "#/definitions/DiagnosticResource"
    }
  }
]
```

`projects/specification/help/resource-manager/Microsoft.Help/Help/swagger/preview/2024-03-01-preview/help.json`; exact pointer segments:

```json
[
  "paths",
  "/{scope}/providers/Microsoft.Help/simplifiedSolutions/{simplifiedSolutionsResourceName}",
  "put",
  "parameters"
]
```

```json
[
  {
    "name": "simplifiedSolutionsRequestBody",
    "in": "body",
    "description": "The required request body for simplified Solutions resource creation.",
    "required": false,
    "schema": {
      "$ref": "#/definitions/SimplifiedSolutionsResource"
    }
  }
]
```

`projects/specification/help/resource-manager/Microsoft.Help/Help/swagger/preview/2024-03-01-preview/help.json`; exact pointer segments:

```json
[
  "paths",
  "/{scope}/providers/Microsoft.Help/solutions/{solutionResourceName}",
  "put",
  "parameters"
]
```

```json
[
  {
    "name": "solutionRequestBody",
    "in": "body",
    "description": "The required request body for this solution resource creation.",
    "required": false,
    "schema": {
      "$ref": "#/definitions/SolutionResource"
    }
  }
]
```

`projects/specification/help/resource-manager/Microsoft.Help/Help/swagger/preview/2024-03-01-preview/help.json`; exact pointer segments:

```json
[
  "paths",
  "/{scope}/providers/Microsoft.Help/solutions/{solutionResourceName}",
  "patch",
  "parameters"
]
```

```json
[
  {
    "name": "solutionPatchRequestBody",
    "in": "body",
    "description": "The required request body for updating a solution resource.",
    "required": false,
    "schema": {
      "$ref": "#/definitions/SolutionPatchRequestBody"
    }
  }
]
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 8 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Remove at most one application per exact target after service-owner review. Do not delete both meaningful rename copies simultaneously.

## hybridconnectivity-duplicate-body-applications

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity` / `2027-01-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 10.
- **Cause:** body-name-application-collapse.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** Five exact body targets have identical common applications in main.tsp and client.tsp: EndpointResources.createOrUpdate.resource and update.properties EndpointResource; EndpointResources.listManagedProxyDetails.body ManagedProxyRequest; ServiceConfigurationResources.createOrupdate.resource and update.properties ServiceConfigurationResource. The exact retained operations carry those body names without x-ms-client-name. All ten raw warnings remain source observations.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                                                              | Exact authored excerpt                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| [specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/main.tsp:47](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/main.tsp#L47-L55)     | `@@clientName( EndpointResources.createOrUpdate::parameters.resource, "EndpointResource" );`                         |
| [specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/client.tsp:32](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/client.tsp#L32-L40) | `@@clientName( EndpointResources.createOrUpdate::parameters.resource, "EndpointResource" );`                         |
| [specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/main.tsp:59](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/main.tsp#L59-L66)     | `@@clientName( EndpointResources.update::parameters.properties, "EndpointResource" );`                               |
| [specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/client.tsp:44](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/client.tsp#L44-L52) | `@@clientName( EndpointResources.update::parameters.properties, "EndpointResource" );`                               |
| [specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/main.tsp:51](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/main.tsp#L51-L59)     | `@@clientName( EndpointResources.listManagedProxyDetails::parameters.body, "ManagedProxyRequest" );`                 |
| [specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/client.tsp:36](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/client.tsp#L36-L44) | `@@clientName( EndpointResources.listManagedProxyDetails::parameters.body, "ManagedProxyRequest" );`                 |
| [specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/main.tsp:63](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/main.tsp#L63-L66)     | `@@clientName( ServiceConfigurationResources.createOrupdate::parameters.resource, "ServiceConfigurationResource" );` |
| [specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/client.tsp:48](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/client.tsp#L48-L56) | `@@clientName( ServiceConfigurationResources.createOrupdate::parameters.resource, "ServiceConfigurationResource" );` |
| [specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/main.tsp:55](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/main.tsp#L55-L63)     | `@@clientName( ServiceConfigurationResources.update::parameters.properties, "ServiceConfigurationResource" );`       |
| [specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/client.tsp:40](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/client.tsp#L40-L48) | `@@clientName( ServiceConfigurationResources.update::parameters.properties, "ServiceConfigurationResource" );`       |

**TypeSpec source and supporting declarations**

[specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/main.tsp:47](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/main.tsp#L47-L66)

```typespec
@@clientName(
  EndpointResources.createOrUpdate::parameters.resource,
  "EndpointResource"
);
@@clientName(
  EndpointResources.listManagedProxyDetails::parameters.body,
  "ManagedProxyRequest"
);
@@clientName(
  ServiceConfigurationResources.update::parameters.properties,
  "ServiceConfigurationResource"
);
@@clientName(
  EndpointResources.update::parameters.properties,
  "EndpointResource"
);
@@clientName(
  ServiceConfigurationResources.createOrupdate::parameters.resource,
  "ServiceConfigurationResource"
);
```

[specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/client.tsp:32](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/client.tsp#L32-L52)

```typespec
@@clientName(
  EndpointResources.createOrUpdate::parameters.resource,
  "EndpointResource"
);
@@clientName(
  EndpointResources.listManagedProxyDetails::parameters.body,
  "ManagedProxyRequest"
);
@@clientName(
  ServiceConfigurationResources.update::parameters.properties,
  "ServiceConfigurationResource"
);
@@clientName(
  EndpointResources.update::parameters.properties,
  "EndpointResource"
);
@@clientName(
  ServiceConfigurationResources.createOrupdate::parameters.resource,
  "ServiceConfigurationResource"
);
#suppress "@azure-tools/typespec-azure-core/no-legacy-usage" "@flattenProperty decorator is not recommended to use."
```

**Retained Swagger or projection evidence**

`projects/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/swagger/stable/2027-01-01/hybridconnectivity.json`; exact pointer segments:

```json
[
  "paths",
  "/{resourceUri}/providers/Microsoft.HybridConnectivity/endpoints/{endpointName}",
  "put",
  "parameters"
]
```

```json
[
  {
    "name": "EndpointResource",
    "in": "body",
    "description": "Endpoint details",
    "required": true,
    "schema": {
      "$ref": "#/definitions/EndpointResource"
    }
  }
]
```

`projects/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/swagger/stable/2027-01-01/hybridconnectivity.json`; exact pointer segments:

```json
[
  "paths",
  "/{resourceUri}/providers/Microsoft.HybridConnectivity/endpoints/{endpointName}",
  "patch",
  "parameters"
]
```

```json
[
  {
    "name": "EndpointResource",
    "in": "body",
    "description": "Endpoint details",
    "required": true,
    "schema": {
      "$ref": "#/definitions/EndpointResource"
    }
  }
]
```

`projects/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/swagger/stable/2027-01-01/hybridconnectivity.json`; exact pointer segments:

```json
[
  "paths",
  "/{resourceUri}/providers/Microsoft.HybridConnectivity/endpoints/{endpointName}/listManagedProxyDetails",
  "post",
  "parameters"
]
```

```json
[
  {
    "name": "ManagedProxyRequest",
    "in": "body",
    "description": "Object of type ManagedProxyRequest",
    "required": true,
    "schema": {
      "$ref": "#/definitions/ManagedProxyRequest"
    }
  }
]
```

`projects/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/swagger/stable/2027-01-01/hybridconnectivity.json`; exact pointer segments:

```json
[
  "paths",
  "/{resourceUri}/providers/Microsoft.HybridConnectivity/endpoints/{endpointName}/serviceConfigurations/{serviceConfigurationName}",
  "put",
  "parameters"
]
```

```json
[
  {
    "name": "ServiceConfigurationResource",
    "in": "body",
    "description": "Service details",
    "required": true,
    "schema": {
      "$ref": "#/definitions/ServiceConfigurationResource"
    }
  }
]
```

`projects/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/swagger/stable/2027-01-01/hybridconnectivity.json`; exact pointer segments:

```json
[
  "paths",
  "/{resourceUri}/providers/Microsoft.HybridConnectivity/endpoints/{endpointName}/serviceConfigurations/{serviceConfigurationName}",
  "patch",
  "parameters"
]
```

```json
[
  {
    "name": "ServiceConfigurationResource",
    "in": "body",
    "description": "Service details",
    "required": true,
    "schema": {
      "$ref": "#/definitions/ServiceConfigurationResourcePatch"
    }
  }
]
```

| Engine          | Observed result                                                                            |
| --------------- | ------------------------------------------------------------------------------------------ |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.            |
| TypeSpec linter | 10 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Remove at most one application per exact target after service-owner review, preserving the meaningful remaining body names.

## keyvault-shadowed-common-override

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault` / `2026-10-01-preview`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 1.
- **Cause:** shadowed-sdk-application.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** Operation.properties first receives operationProperties, then the same file applies OperationProperties to that exact target. The earlier common spelling is shadowed. Preserve strict case and do not treat different decorator text as proof of a final SDK naming effect.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                    | Exact authored excerpt                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| [specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/back-compatible.tsp:39](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/back-compatible.tsp#L39-L47) | `@@clientName(Operation.properties, "operationProperties");` |

**TypeSpec source and supporting declarations**

[specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/back-compatible.tsp:37](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/back-compatible.tsp#L37-L39)

```typespec
#suppress "@azure-tools/typespec-azure-core/no-legacy-usage" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
@@Azure.ClientGenerator.Core.Legacy.flattenProperty(Operation.properties);
@@clientName(Operation.properties, "operationProperties");
```

[specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/back-compatible.tsp:188](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/back-compatible.tsp#L188-L190)

```typespec
#suppress "@azure-tools/typespec-azure-core/no-legacy-usage" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
@@Azure.ClientGenerator.Core.Legacy.flattenProperty(Operation.properties);
@@clientName(Operation.properties, "OperationProperties");
```

[specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/models.tsp:2546](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/models.tsp#L2546-L2571)

```typespec
model Operation {
  /**
   * Operation name: {provider}/{resource}/{operation}
   */
  name?: string;

  /**
   * Display metadata associated with the operation.
   */
  display?: OperationDisplay;

  /**
   * The origin of operations.
   */
  origin?: string;

  /**
   * Properties of operation, include metric specifications.
   */
  properties?: OperationProperties;

  /**
   * Property to specify whether the action is a data action.
   */
  isDataAction?: boolean;
}
```

**Retained Swagger or projection evidence**

`projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-10-01-preview/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "Operation",
  "properties",
  "properties"
]
```

```json
{
  "$ref": "#/definitions/OperationProperties",
  "description": "Properties of operation, include metric specifications.",
  "x-ms-client-flatten": true,
  "x-ms-client-name": "OperationProperties"
}
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 1 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** SDK/service owners may remove the earlier shadowed application, preserving the winning spelling. Flattening and compatibility policy need separate review if the intended SDK name changes.

## managednetworkfabric-copy-source-repeats

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric` / `2026-01-15-preview`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 25.
- **Cause:** copy-source-sdk-repeat.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** Twenty-four Patch property applications repeat the same C# names on properties copied with model is: IpGroup, ImportRoutePolicyInformation, ExportRoutePolicyInformation, Layer3IpPrefix, RouteTargetInformation, ImportRoutePolicy, ExportRoutePolicy, ControlPlaneAclIpMatchCondition, ControlPlaneAclTtlMatchCondition and L3ExportRoutePolicy. The remaining ExternalNetworkPatchPropertiesOptionAProperties.peerASN application repeats L3OptionAProperties.peerASN copied by spread. Exact authored target/line, source-copy declaration and matching source-scope spelling are retained individually. These are source SDK application layers, not emitted extension equality.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                                                                                | Exact authored excerpt                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:1259](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L1259-L1267) | `@@clientName(IpGroupPatchProperties.ipAddressType, "IPAddressType", "csharp");`                                  |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:1260](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L1260-L1268) | `@@clientName(IpGroupPatchProperties.ipPrefixes, "IPPrefixes", "csharp");`                                        |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:1047](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L1047-L1055) | `@@clientName( ImportRoutePolicyInformationPatch.importIpv4RoutePolicyId, "ImportIPv4RoutePolicyId", "csharp" );` |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:1052](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L1052-L1060) | `@@clientName( ImportRoutePolicyInformationPatch.importIpv6RoutePolicyId, "ImportIPv6RoutePolicyId", "csharp" );` |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:1087](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L1087-L1095) | `@@clientName( ExportRoutePolicyInformationPatch.exportIpv4RoutePolicyId, "ExportIPv4RoutePolicyId", "csharp" );` |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:1092](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L1092-L1100) | `@@clientName( ExportRoutePolicyInformationPatch.exportIpv6RoutePolicyId, "ExportIPv6RoutePolicyId", "csharp" );` |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:404](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L404-L412)    | `@@clientName( Layer3IpPrefixPatchProperties.primaryIpv4Prefix, "PrimaryIPv4Prefix", "csharp" );`                 |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:409](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L409-L417)    | `@@clientName( Layer3IpPrefixPatchProperties.primaryIpv6Prefix, "PrimaryIPv6Prefix", "csharp" );`                 |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:414](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L414-L422)    | `@@clientName( Layer3IpPrefixPatchProperties.secondaryIpv4Prefix, "SecondaryIPv4Prefix", "csharp" );`             |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:419](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L419-L427)    | `@@clientName( Layer3IpPrefixPatchProperties.secondaryIpv6Prefix, "SecondaryIPv6Prefix", "csharp" );`             |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:851](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L851-L859)    | `@@clientName( RouteTargetPatchInformation.importIpv4RouteTargets, "ImportIPv4RouteTargets", "csharp" );`         |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:856](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L856-L864)    | `@@clientName( RouteTargetPatchInformation.importIpv6RouteTargets, "ImportIPv6RouteTargets", "csharp" );`         |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:841](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L841-L849)    | `@@clientName( RouteTargetPatchInformation.exportIpv4RouteTargets, "ExportIPv4RouteTargets", "csharp" );`         |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:846](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L846-L854)    | `@@clientName( RouteTargetPatchInformation.exportIpv6RouteTargets, "ExportIPv6RouteTargets", "csharp" );`         |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:1037](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L1037-L1045) | `@@clientName( ImportRoutePolicyPatch.importIpv4RoutePolicyId, "ImportIPv4RoutePolicyId", "csharp" );`            |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:1042](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L1042-L1050) | `@@clientName( ImportRoutePolicyPatch.importIpv6RoutePolicyId, "ImportIPv6RoutePolicyId", "csharp" );`            |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:1077](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L1077-L1085) | `@@clientName( ExportRoutePolicyPatch.exportIpv4RoutePolicyId, "ExportIPv4RoutePolicyId", "csharp" );`            |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:1082](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L1082-L1090) | `@@clientName( ExportRoutePolicyPatch.exportIpv6RoutePolicyId, "ExportIPv6RoutePolicyId", "csharp" );`            |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:1247](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L1247-L1255) | `@@clientName( ControlPlaneAclIpMatchConditionPatch.sourceIpPrefix, "SourceIPPrefix", "csharp" );`                |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:1252](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L1252-L1260) | `@@clientName( ControlPlaneAclIpMatchConditionPatch.destinationIpPrefix, "DestinationIPPrefix", "csharp" );`      |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:765](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L765-L773)    | `@@clientName( ControlPlaneAclTtlMatchConditionPatch.ttlValue, "TimeToLiveInHops", "csharp" );`                   |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:770](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L770-L778)    | `@@clientName( ControlPlaneAclTtlMatchConditionPatch.ttlMatchType, "TimeToLiveMatchType", "csharp" );`            |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:1107](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L1107-L1115) | `@@clientName( L3ExportRoutePolicyPatch.exportIpv4RoutePolicyId, "ExportIPv4RoutePolicyId", "csharp" );`          |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:1112](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L1112-L1120) | `@@clientName( L3ExportRoutePolicyPatch.exportIpv6RoutePolicyId, "ExportIPv6RoutePolicyId", "csharp" );`          |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:977](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L977-L985)    | `@@clientName( ExternalNetworkPatchPropertiesOptionAProperties.peerASN, "PeerAsn", "csharp" );`                   |

**TypeSpec source and supporting declarations**

[specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/common.tsp:505](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/common.tsp#L505-L505)

```typespec
model IpGroupPatchProperties is IpGroupProperties;
```

[specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/common.tsp:764](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/common.tsp#L764-L764)

```typespec
model ImportRoutePolicyInformationPatch is ImportRoutePolicyInformation;
```

[specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/common.tsp:804](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/common.tsp#L804-L804)

```typespec
model ExportRoutePolicyInformationPatch is ExportRoutePolicyInformation;
```

[specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/common.tsp:827](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/common.tsp#L827-L827)

```typespec
model Layer3IpPrefixPatchProperties is Layer3IpPrefixProperties;
```

[specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/common.tsp:912](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/common.tsp#L912-L912)

```typespec
model RouteTargetPatchInformation is RouteTargetInformation;
```

[specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/common.tsp:952](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/common.tsp#L952-L952)

```typespec
model ImportRoutePolicyPatch is ImportRoutePolicy;
```

[specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/common.tsp:992](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/common.tsp#L992-L992)

```typespec
model ExportRoutePolicyPatch is ExportRoutePolicy;
```

[specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/AccessControlList.tsp:491](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/AccessControlList.tsp#L491-L491)

```typespec
model ControlPlaneAclIpMatchConditionPatch is ControlPlanAclIpMatchCondition;
```

[specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/AccessControlList.tsp:543](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/AccessControlList.tsp#L543-L543)

```typespec
model ControlPlaneAclTtlMatchConditionPatch is ControlPlaneAclTtlMatchCondition;
```

[specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/L3IsolationDomain.tsp:210](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/L3IsolationDomain.tsp#L210-L210)

```typespec
model L3ExportRoutePolicyPatch is L3ExportRoutePolicy;
```

[specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/ExternalNetwork.tsp:282](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/ExternalNetwork.tsp#L282-L284)

```typespec
model ExternalNetworkPatchPropertiesOptionAProperties {
  ...Layer3IpPrefixPatchProperties;
  ...L3OptionAProperties;
```

[specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:379](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L379-L423)

```typespec
@@clientName(
  Layer3IpPrefixProperties.primaryIpv4Prefix,
  "PrimaryIPv4Prefix",
  "csharp"
);
@@clientName(
  Layer3IpPrefixProperties.primaryIpv6Prefix,
  "PrimaryIPv6Prefix",
  "csharp"
);
@@clientName(
  Layer3IpPrefixProperties.secondaryIpv4Prefix,
  "SecondaryIPv4Prefix",
  "csharp"
);
@@clientName(
  Layer3IpPrefixProperties.secondaryIpv6Prefix,
  "SecondaryIPv6Prefix",
  "csharp"
);
@@clientName(
  Layer3IpPrefixPatchProperties,
  "Layer3IPPrefixPatchProperties",
  "csharp"
);
@@clientName(
  Layer3IpPrefixPatchProperties.primaryIpv4Prefix,
  "PrimaryIPv4Prefix",
  "csharp"
);
@@clientName(
  Layer3IpPrefixPatchProperties.primaryIpv6Prefix,
  "PrimaryIPv6Prefix",
  "csharp"
);
@@clientName(
  Layer3IpPrefixPatchProperties.secondaryIpv4Prefix,
  "SecondaryIPv4Prefix",
  "csharp"
);
@@clientName(
  Layer3IpPrefixPatchProperties.secondaryIpv6Prefix,
  "SecondaryIPv6Prefix",
  "csharp"
);
```

[specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:755](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L755-L774)

```typespec
@@clientName(
  ControlPlaneAclTtlMatchCondition.ttlValue,
  "TimeToLiveInHops",
  "csharp"
);
@@clientName(
  ControlPlaneAclTtlMatchCondition.ttlMatchType,
  "TimeToLiveMatchType",
  "csharp"
);
@@clientName(
  ControlPlaneAclTtlMatchConditionPatch.ttlValue,
  "TimeToLiveInHops",
  "csharp"
);
@@clientName(
  ControlPlaneAclTtlMatchConditionPatch.ttlMatchType,
  "TimeToLiveMatchType",
  "csharp"
);
```

[specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:821](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L821-L860)

```typespec
@@clientName(
  RouteTargetInformation.exportIpv4RouteTargets,
  "ExportIPv4RouteTargets",
  "csharp"
);
@@clientName(
  RouteTargetInformation.exportIpv6RouteTargets,
  "ExportIPv6RouteTargets",
  "csharp"
);
@@clientName(
  RouteTargetInformation.importIpv4RouteTargets,
  "ImportIPv4RouteTargets",
  "csharp"
);
@@clientName(
  RouteTargetInformation.importIpv6RouteTargets,
  "ImportIPv6RouteTargets",
  "csharp"
);
@@clientName(
  RouteTargetPatchInformation.exportIpv4RouteTargets,
  "ExportIPv4RouteTargets",
  "csharp"
);
@@clientName(
  RouteTargetPatchInformation.exportIpv6RouteTargets,
  "ExportIPv6RouteTargets",
  "csharp"
);
@@clientName(
  RouteTargetPatchInformation.importIpv4RouteTargets,
  "ImportIPv4RouteTargets",
  "csharp"
);
@@clientName(
  RouteTargetPatchInformation.importIpv6RouteTargets,
  "ImportIPv6RouteTargets",
  "csharp"
);
```

[specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:977](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L977-L994)

```typespec
@@clientName(
  ExternalNetworkPatchPropertiesOptionAProperties.peerASN,
  "PeerAsn",
  "csharp"
);
@@clientName(
  ExternalNetworkPatchPropertiesOptionAProperties.nativeIpv4PrefixLimit,
  "NativeIPv4PrefixLimit",
  "csharp"
);
@@clientName(
  ExternalNetworkPatchPropertiesOptionAProperties.nativeIpv6PrefixLimit,
  "NativeIPv6PrefixLimit",
  "csharp"
);
@@clientName(L3OptionAProperties.peerASN, "PeerAsn", "csharp");
@@clientName(VpnOptionAProperties.peerASN, "PeerAsn", "csharp");
@@clientName(VpnOptionAPatchProperties.peerASN, "PeerAsn", "csharp");
```

[specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:1017](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L1017-L1116)

```typespec
@@clientName(
  ImportRoutePolicy.importIpv4RoutePolicyId,
  "ImportIPv4RoutePolicyId",
  "csharp"
);
@@clientName(
  ImportRoutePolicy.importIpv6RoutePolicyId,
  "ImportIPv6RoutePolicyId",
  "csharp"
);
@@clientName(
  ImportRoutePolicyInformation.importIpv4RoutePolicyId,
  "ImportIPv4RoutePolicyId",
  "csharp"
);
@@clientName(
  ImportRoutePolicyInformation.importIpv6RoutePolicyId,
  "ImportIPv6RoutePolicyId",
  "csharp"
);
@@clientName(
  ImportRoutePolicyPatch.importIpv4RoutePolicyId,
  "ImportIPv4RoutePolicyId",
  "csharp"
);
@@clientName(
  ImportRoutePolicyPatch.importIpv6RoutePolicyId,
  "ImportIPv6RoutePolicyId",
  "csharp"
);
@@clientName(
  ImportRoutePolicyInformationPatch.importIpv4RoutePolicyId,
  "ImportIPv4RoutePolicyId",
  "csharp"
);
@@clientName(
  ImportRoutePolicyInformationPatch.importIpv6RoutePolicyId,
  "ImportIPv6RoutePolicyId",
  "csharp"
);
@@clientName(
  ExportRoutePolicy.exportIpv4RoutePolicyId,
  "ExportIPv4RoutePolicyId",
  "csharp"
);
@@clientName(
  ExportRoutePolicy.exportIpv6RoutePolicyId,
  "ExportIPv6RoutePolicyId",
  "csharp"
);
@@clientName(
  ExportRoutePolicyInformation.exportIpv4RoutePolicyId,
  "ExportIPv4RoutePolicyId",
  "csharp"
);
@@clientName(
  ExportRoutePolicyInformation.exportIpv6RoutePolicyId,
  "ExportIPv6RoutePolicyId",
  "csharp"
);
@@clientName(
  ExportRoutePolicyPatch.exportIpv4RoutePolicyId,
  "ExportIPv4RoutePolicyId",
  "csharp"
);
@@clientName(
  ExportRoutePolicyPatch.exportIpv6RoutePolicyId,
  "ExportIPv6RoutePolicyId",
  "csharp"
);
@@clientName(
  ExportRoutePolicyInformationPatch.exportIpv4RoutePolicyId,
  "ExportIPv4RoutePolicyId",
  "csharp"
);
@@clientName(
  ExportRoutePolicyInformationPatch.exportIpv6RoutePolicyId,
  "ExportIPv6RoutePolicyId",
  "csharp"
);
@@clientName(
  L3ExportRoutePolicy.exportIpv4RoutePolicyId,
  "ExportIPv4RoutePolicyId",
  "csharp"
);
@@clientName(
  L3ExportRoutePolicy.exportIpv6RoutePolicyId,
  "ExportIPv6RoutePolicyId",
  "csharp"
);
@@clientName(
  L3ExportRoutePolicyPatch.exportIpv4RoutePolicyId,
  "ExportIPv4RoutePolicyId",
  "csharp"
);
@@clientName(
  L3ExportRoutePolicyPatch.exportIpv6RoutePolicyId,
  "ExportIPv6RoutePolicyId",
  "csharp"
);
```

[specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp:1237](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/client.tsp#L1237-L1260)

```typespec
@@clientName(
  ControlPlanAclIpMatchCondition.sourceIpPrefix,
  "SourceIPPrefix",
  "csharp"
);
@@clientName(
  ControlPlanAclIpMatchCondition.destinationIpPrefix,
  "DestinationIPPrefix",
  "csharp"
);
@@clientName(
  ControlPlaneAclIpMatchConditionPatch.sourceIpPrefix,
  "SourceIPPrefix",
  "csharp"
);
@@clientName(
  ControlPlaneAclIpMatchConditionPatch.destinationIpPrefix,
  "DestinationIPPrefix",
  "csharp"
);
@@clientName(IpGroupProperties.ipAddressType, "IPAddressType", "csharp");
@@clientName(IpGroupProperties.ipPrefixes, "IPPrefixes", "csharp");
@@clientName(IpGroupPatchProperties.ipAddressType, "IPAddressType", "csharp");
@@clientName(IpGroupPatchProperties.ipPrefixes, "IPPrefixes", "csharp");
```

**Retained Swagger or projection evidence**

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "ControlPlaneAclIpMatchConditionPatch",
  "properties",
  "destinationIpPrefix"
]
```

```json
{
  "type": "string",
  "description": "List of the destination IP addresses that need to be matched."
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "ControlPlaneAclIpMatchConditionPatch",
  "properties",
  "sourceIpPrefix"
]
```

```json
{
  "type": "string",
  "description": "List of the source IP addresses that need to be matched."
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "ControlPlaneAclTtlMatchConditionPatch",
  "properties",
  "ttlMatchType"
]
```

```json
{
  "$ref": "#/definitions/ControlPlaneAclTtlMatchType",
  "description": "TTL [Time To Live] match type. Example: eq | neq | gt | lt | range"
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "ControlPlaneAclTtlMatchConditionPatch",
  "properties",
  "ttlValue"
]
```

```json
{
  "type": "string",
  "description": "TTL [Time To Live] values that need to be matched."
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "ExportRoutePolicyInformationPatch",
  "properties",
  "exportIpv4RoutePolicyId"
]
```

```json
{
  "type": "string",
  "format": "arm-id",
  "description": "Export IPv4 Route Policy Id.",
  "x-ms-arm-id-details": {
    "allowedResources": [
      {
        "type": "Microsoft.ManagedNetworkFabric/routePolicies"
      }
    ]
  }
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "ExportRoutePolicyInformationPatch",
  "properties",
  "exportIpv6RoutePolicyId"
]
```

```json
{
  "type": "string",
  "format": "arm-id",
  "description": "Export IPv6 Route Policy Id.",
  "x-ms-arm-id-details": {
    "allowedResources": [
      {
        "type": "Microsoft.ManagedNetworkFabric/routePolicies"
      }
    ]
  }
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "ExportRoutePolicyPatch",
  "properties",
  "exportIpv4RoutePolicyId"
]
```

```json
{
  "type": "string",
  "format": "arm-id",
  "description": "ARM resource ID of RoutePolicy.",
  "x-ms-arm-id-details": {
    "allowedResources": [
      {
        "type": "Microsoft.ManagedNetworkFabric/routePolicies"
      }
    ]
  }
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "ExportRoutePolicyPatch",
  "properties",
  "exportIpv6RoutePolicyId"
]
```

```json
{
  "type": "string",
  "format": "arm-id",
  "description": "ARM resource ID of RoutePolicy.",
  "x-ms-arm-id-details": {
    "allowedResources": [
      {
        "type": "Microsoft.ManagedNetworkFabric/routePolicies"
      }
    ]
  }
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "ExternalNetworkPatchPropertiesOptionAProperties",
  "properties",
  "peerASN"
]
```

```json
{
  "type": "integer",
  "format": "int64",
  "description": "Peer ASN number.Example : 28",
  "minimum": 1,
  "maximum": 4294967295
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "ImportRoutePolicyInformationPatch",
  "properties",
  "importIpv4RoutePolicyId"
]
```

```json
{
  "type": "string",
  "format": "arm-id",
  "description": "Import IPv4 Route Policy Id.",
  "x-ms-arm-id-details": {
    "allowedResources": [
      {
        "type": "Microsoft.ManagedNetworkFabric/routePolicies"
      }
    ]
  }
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "ImportRoutePolicyInformationPatch",
  "properties",
  "importIpv6RoutePolicyId"
]
```

```json
{
  "type": "string",
  "format": "arm-id",
  "description": "Import IPv6 Route Policy Id.",
  "x-ms-arm-id-details": {
    "allowedResources": [
      {
        "type": "Microsoft.ManagedNetworkFabric/routePolicies"
      }
    ]
  }
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "ImportRoutePolicyPatch",
  "properties",
  "importIpv4RoutePolicyId"
]
```

```json
{
  "type": "string",
  "format": "arm-id",
  "description": "ARM resource ID of RoutePolicy.",
  "x-ms-arm-id-details": {
    "allowedResources": [
      {
        "type": "Microsoft.ManagedNetworkFabric/routePolicies"
      }
    ]
  }
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "ImportRoutePolicyPatch",
  "properties",
  "importIpv6RoutePolicyId"
]
```

```json
{
  "type": "string",
  "format": "arm-id",
  "description": "ARM resource ID of RoutePolicy.",
  "x-ms-arm-id-details": {
    "allowedResources": [
      {
        "type": "Microsoft.ManagedNetworkFabric/routePolicies"
      }
    ]
  }
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "IpGroupPatchProperties",
  "properties",
  "ipAddressType"
]
```

```json
{
  "$ref": "#/definitions/IPAddressType",
  "description": "IP Address type."
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "IpGroupPatchProperties",
  "properties",
  "ipPrefixes"
]
```

```json
{
  "type": "array",
  "description": "List of IP Prefixes.",
  "items": {
    "type": "string"
  }
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "L3ExportRoutePolicyPatch",
  "properties",
  "exportIpv4RoutePolicyId"
]
```

```json
{
  "type": "string",
  "format": "arm-id",
  "description": "ARM Resource ID of the RoutePolicy.",
  "x-ms-arm-id-details": {
    "allowedResources": [
      {
        "type": "Microsoft.ManagedNetworkFabric/routePolicies"
      }
    ]
  }
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "L3ExportRoutePolicyPatch",
  "properties",
  "exportIpv6RoutePolicyId"
]
```

```json
{
  "type": "string",
  "format": "arm-id",
  "description": "ARM Resource ID of the RoutePolicy.",
  "x-ms-arm-id-details": {
    "allowedResources": [
      {
        "type": "Microsoft.ManagedNetworkFabric/routePolicies"
      }
    ]
  }
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "Layer3IpPrefixPatchProperties",
  "properties",
  "primaryIpv4Prefix"
]
```

```json
{
  "type": "string",
  "description": "IPv4 Address Prefix."
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "Layer3IpPrefixPatchProperties",
  "properties",
  "primaryIpv6Prefix"
]
```

```json
{
  "type": "string",
  "description": "IPv6 Address Prefix."
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "Layer3IpPrefixPatchProperties",
  "properties",
  "secondaryIpv4Prefix"
]
```

```json
{
  "type": "string",
  "description": "Secondary IPv4 Address Prefix."
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "Layer3IpPrefixPatchProperties",
  "properties",
  "secondaryIpv6Prefix"
]
```

```json
{
  "type": "string",
  "description": "Secondary IPv6 Address Prefix."
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "RouteTargetPatchInformation",
  "properties",
  "exportIpv4RouteTargets"
]
```

```json
{
  "type": "array",
  "description": "Route Targets to be applied for outgoing routes into CE.",
  "items": {
    "type": "string"
  }
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "RouteTargetPatchInformation",
  "properties",
  "exportIpv6RouteTargets"
]
```

```json
{
  "type": "array",
  "description": "Route Targets to be applied for outgoing routes from CE.",
  "items": {
    "type": "string"
  }
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "RouteTargetPatchInformation",
  "properties",
  "importIpv4RouteTargets"
]
```

```json
{
  "type": "array",
  "description": "Route Targets to be applied for incoming routes into CE.",
  "items": {
    "type": "string"
  }
}
```

`projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/preview/2026-01-15-preview/managednetworkfabric.json`; exact pointer segments:

```json
[
  "definitions",
  "RouteTargetPatchInformation",
  "properties",
  "importIpv6RouteTargets"
]
```

```json
{
  "type": "array",
  "description": "Route Targets to be applied for incoming routes from CE.",
  "items": {
    "type": "string"
  }
}
```

| Engine          | Observed result                                                                            |
| --------------- | ------------------------------------------------------------------------------------------ |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.            |
| TypeSpec linter | 25 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** SDK/service owners can assess removal of the reported copy-target repeats, retaining source-property names and independent scopes. Do not infer that every customization on a copied declaration is redundant, or discard older-version source findings to equalize counts.

## managedidentity-duplicate-body-applications

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity` / `2025-05-31-preview`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 6.
- **Cause:** body-name-application-collapse.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** Identities.createOrUpdate.resource, Identities.update.properties and FederatedIdentityCredentials.createOrUpdate.resource each have identical common parameters applications in the owning source and back-compatible.tsp. Exact retained PUT/PATCH operation IDs bind each body to its source target. All body objects use parameters and have no x-ms-client-name. All six raw warnings remain distinct.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                                                              | Exact authored excerpt                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| [specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/Identity.tsp:68](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/Identity.tsp#L68-L76)                                       | `@@clientName(Identities.createOrUpdate::parameters.resource, "parameters");`                     |
| [specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/back-compatible.tsp:27](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/back-compatible.tsp#L27-L35)                         | `@@clientName(Identities.createOrUpdate::parameters.resource, "parameters");`                     |
| [specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/Identity.tsp:69](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/Identity.tsp#L69-L77)                                       | `@@clientName(Identities.update::parameters.properties, "parameters");`                           |
| [specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/back-compatible.tsp:29](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/back-compatible.tsp#L29-L37)                         | `@@clientName(Identities.update::parameters.properties, "parameters");`                           |
| [specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/FederatedIdentityCredential.tsp:75](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/FederatedIdentityCredential.tsp#L75-L83) | `@@clientName( FederatedIdentityCredentials.createOrUpdate::parameters.resource, "parameters" );` |
| [specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/back-compatible.tsp:33](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/back-compatible.tsp#L33-L40)                         | `@@clientName( FederatedIdentityCredentials.createOrUpdate::parameters.resource, "parameters" );` |

**TypeSpec source and supporting declarations**

[specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/Identity.tsp:68](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/Identity.tsp#L68-L69)

```typespec
@@clientName(Identities.createOrUpdate::parameters.resource, "parameters");
@@clientName(Identities.update::parameters.properties, "parameters");
```

[specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/FederatedIdentityCredential.tsp:75](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/FederatedIdentityCredential.tsp#L75-L78)

```typespec
@@clientName(
  FederatedIdentityCredentials.createOrUpdate::parameters.resource,
  "parameters"
);
```

[specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/back-compatible.tsp:27](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/back-compatible.tsp#L27-L36)

```typespec
@@clientName(Identities.createOrUpdate::parameters.resource, "parameters");
@@clientLocation(Identities.update, "UserAssignedIdentities");
@@clientName(Identities.update::parameters.properties, "parameters");
@@clientLocation(Identities.delete, "UserAssignedIdentities");
@@clientLocation(Identities.listByResourceGroup, "UserAssignedIdentities");
@@clientLocation(Identities.listBySubscription, "UserAssignedIdentities");
@@clientName(
  FederatedIdentityCredentials.createOrUpdate::parameters.resource,
  "parameters"
);
```

**Retained Swagger or projection evidence**

`projects/specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/swagger/preview/2025-05-31-preview/ManagedIdentity.json`; exact pointer segments:

```json
[
  "paths",
  "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{resourceName}",
  "put",
  "parameters"
]
```

```json
[
  {
    "name": "parameters",
    "in": "body",
    "description": "Parameters to create or update the identity",
    "required": true,
    "schema": {
      "$ref": "#/definitions/Identity"
    }
  }
]
```

`projects/specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/swagger/preview/2025-05-31-preview/ManagedIdentity.json`; exact pointer segments:

```json
[
  "paths",
  "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{resourceName}",
  "patch",
  "parameters"
]
```

```json
[
  {
    "name": "parameters",
    "in": "body",
    "description": "Parameters to update the identity",
    "required": true,
    "schema": {
      "$ref": "#/definitions/IdentityUpdate"
    }
  }
]
```

`projects/specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/swagger/preview/2025-05-31-preview/ManagedIdentity.json`; exact pointer segments:

```json
[
  "paths",
  "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{resourceName}/federatedIdentityCredentials/{federatedIdentityCredentialResourceName}",
  "put",
  "parameters"
]
```

```json
[
  {
    "name": "parameters",
    "in": "body",
    "description": "Parameters to create or update the federated identity credential.",
    "required": true,
    "schema": {
      "$ref": "#/definitions/FederatedIdentityCredential"
    }
  }
]
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 6 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Remove at most one duplicate per target after service-owner review, preserving the meaningful remaining body rename.

## networkcloud-copy-source-repeats

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud` / `2026-08-01-preview`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 2.
- **Cause:** copy-source-sdk-repeat.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** StorageApplianceProperties spreads StorageApplianceStatus; VolumeProperties spreads VolumeStatus. The reported copy-target C# CACertificate and AllocatedInSizeMiB applications repeat the identical spellings also applied to their source properties at client.tsp:671 and 692. Exact copy declarations and retained properties bind this source-policy difference.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                             | Exact authored excerpt                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/client.tsp:337](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/client.tsp#L337-L345) | `@@clientName( StorageApplianceProperties.caCertificate, "CACertificate", "csharp" );` |
| [specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/client.tsp:425](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/client.tsp#L425-L433) | `@@clientName(VolumeProperties.allocatedSizeMiB, "AllocatedInSizeMiB", "csharp");`     |

**TypeSpec source and supporting declarations**

[specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/storageappliances/StorageAppliance_models.tsp:161](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/storageappliances/StorageAppliance_models.tsp#L161-L169)

```typespec
model StorageApplianceProperties {
  ...StorageApplianceSpec;
  ...StorageApplianceStatus;

  /**
   * The provisioning state of the storage appliance.
   */
  @visibility(Lifecycle.Read)
  provisioningState?: StorageApplianceProvisioningState;
```

[specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/volumes/Volume_models.tsp:83](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/volumes/Volume_models.tsp#L83-L91)

```typespec
model VolumeProperties {
  ...VolumeSpec;
  ...VolumeStatus;

  /**
   * The provisioning state of the volume.
   */
  @visibility(Lifecycle.Read)
  provisioningState?: VolumeProvisioningState;
```

[specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/client.tsp:337](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/client.tsp#L337-L341)

```typespec
@@clientName(
  StorageApplianceProperties.caCertificate,
  "CACertificate",
  "csharp"
);
```

[specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/client.tsp:425](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/client.tsp#L425-L425)

```typespec
@@clientName(VolumeProperties.allocatedSizeMiB, "AllocatedInSizeMiB", "csharp");
```

[specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/client.tsp:671](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/client.tsp#L671-L671)

```typespec
@@clientName(StorageApplianceStatus.caCertificate, "CACertificate", "csharp");
```

[specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/client.tsp:691](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/client.tsp#L691-L692)

```typespec
@@clientName(VolumeSpec.sizeMiB, "AllocatedInSizeMiB", "csharp");
@@clientName(VolumeStatus.allocatedSizeMiB, "AllocatedInSizeMiB", "csharp");
```

**Retained Swagger or projection evidence**

`projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json`; exact pointer segments:

```json
[
  "definitions",
  "StorageApplianceProperties",
  "properties",
  "caCertificate"
]
```

```json
{
  "$ref": "#/definitions/CertificateInfo",
  "description": "The CA certificate information issued by the platform for connecting to TLS interfaces for the storage appliance. Callers add this certificate to their trusted CA store to allow secure communication with the storage appliance.",
  "readOnly": true
}
```

`projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json`; exact pointer segments:

```json
[
  "definitions",
  "VolumeProperties",
  "properties",
  "allocatedSizeMiB"
]
```

```json
{
  "type": "integer",
  "format": "int64",
  "description": "The allocated size of the volume in Mebibytes.",
  "minimum": 0,
  "readOnly": true
}
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 2 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** SDK/service owners may remove the reported copy-target repeats while retaining effective source-property SDK names.

## oracle-duplicate-csharp

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/oracle/resource-manager/Oracle.Database/OracleDatabase` / `2026-06-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 4.
- **Cause:** duplicate-scoped-sdk-applications.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** CloudVmClusterProperties.timeCreated has two identical C# CreatedOn applications. AutonomousDatabaseBaseProperties.dbVersion has two identical C# DBVersion applications. All four raw warnings are retained independently; source application multiplicity is not represented by emitted properties.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                       | Exact authored excerpt                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| [specification/oracle/resource-manager/Oracle.Database/OracleDatabase/client.tsp:291](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/client.tsp#L291-L299) | `@@clientName(CloudVmClusterProperties.timeCreated, "CreatedOn", "csharp");`       |
| [specification/oracle/resource-manager/Oracle.Database/OracleDatabase/client.tsp:293](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/client.tsp#L293-L301) | `@@clientName(CloudVmClusterProperties.timeCreated, "CreatedOn", "csharp");`       |
| [specification/oracle/resource-manager/Oracle.Database/OracleDatabase/client.tsp:94](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/client.tsp#L94-L102)   | `@@clientName(AutonomousDatabaseBaseProperties.dbVersion, "DBVersion", "csharp");` |
| [specification/oracle/resource-manager/Oracle.Database/OracleDatabase/client.tsp:195](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/client.tsp#L195-L203) | `@@clientName(AutonomousDatabaseBaseProperties.dbVersion, "DBVersion", "csharp");` |

**TypeSpec source and supporting declarations**

[specification/oracle/resource-manager/Oracle.Database/OracleDatabase/client.tsp:94](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/client.tsp#L94-L94)

```typespec
@@clientName(AutonomousDatabaseBaseProperties.dbVersion, "DBVersion", "csharp");
```

[specification/oracle/resource-manager/Oracle.Database/OracleDatabase/client.tsp:195](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/client.tsp#L195-L195)

```typespec
@@clientName(AutonomousDatabaseBaseProperties.dbVersion, "DBVersion", "csharp");
```

[specification/oracle/resource-manager/Oracle.Database/OracleDatabase/client.tsp:291](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/client.tsp#L291-L293)

```typespec
@@clientName(CloudVmClusterProperties.timeCreated, "CreatedOn", "csharp");
@@alternateType(CloudVmClusterProperties.timeCreated, utcDateTime, "csharp");
@@clientName(CloudVmClusterProperties.timeCreated, "CreatedOn", "csharp");
```

**Retained Swagger or projection evidence**

`projects/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/swagger/stable/2026-06-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "AutonomousDatabaseBaseProperties",
  "properties",
  "dbVersion"
]
```

```json
{
  "type": "string",
  "description": "A valid Oracle Database version for Autonomous Database.",
  "minLength": 1,
  "maxLength": 255,
  "x-ms-mutability": [
    "read",
    "create"
  ]
}
```

`projects/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/swagger/stable/2026-06-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "CloudVmClusterProperties",
  "properties",
  "timeCreated"
]
```

```json
{
  "type": "string",
  "format": "date-time",
  "description": "The date and time that the cloud VM cluster was created.",
  "readOnly": true
}
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 4 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Remove at most one duplicate per exact target after service-owner review, preserving each meaningful remaining C# name.

## postgresql-shadowed-csharp-override

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/postgresql/resource-manager/Microsoft.DBforPostgreSQL/PostgreSql` / `2026-10-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 1.
- **Cause:** shadowed-sdk-application.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** CapturedLogProperties.type first receives C# LogFileType at client.tsp:643, then the same exact target receives C# TypePropertiesType at line 765. The former spelling is shadowed, so its differing text does not imply a final SDK naming effect.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                           | Exact authored excerpt                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| [specification/postgresql/resource-manager/Microsoft.DBforPostgreSQL/PostgreSql/client.tsp:643](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/postgresql/resource-manager/Microsoft.DBforPostgreSQL/PostgreSql/client.tsp#L643-L651) | `@@clientName(CapturedLogProperties.type, "LogFileType", "csharp");` |

**TypeSpec source and supporting declarations**

[specification/postgresql/resource-manager/Microsoft.DBforPostgreSQL/PostgreSql/client.tsp:643](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/postgresql/resource-manager/Microsoft.DBforPostgreSQL/PostgreSql/client.tsp#L643-L644)

```typespec
@@clientName(CapturedLogProperties.type, "LogFileType", "csharp");
@@clientName(ValidationSummaryItem.type, "ValidationSummaryItemType", "csharp");
```

[specification/postgresql/resource-manager/Microsoft.DBforPostgreSQL/PostgreSql/client.tsp:765](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/postgresql/resource-manager/Microsoft.DBforPostgreSQL/PostgreSql/client.tsp#L765-L765)

```typespec
@@clientName(CapturedLogProperties.type, "TypePropertiesType", "csharp");
```

[specification/postgresql/resource-manager/Microsoft.DBforPostgreSQL/PostgreSql/models.tsp:1707](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/postgresql/resource-manager/Microsoft.DBforPostgreSQL/PostgreSql/models.tsp#L1707-L1735)

```typespec
model CapturedLogProperties {
  /**
   * Creation timestamp of the log file.
   */
  // FIXME: (utcDateTime) Please double check that this is the correct type for your scenario.
  createdTime?: utcDateTime;

  /**
   * Last modified timestamp of the log file.
   */
  // FIXME: (utcDateTime) Please double check that this is the correct type for your scenario.
  lastModifiedTime?: utcDateTime;

  /**
   * Size (in KB) of the log file.
   */
  sizeInKb?: int64;

  /**
   * Type of log file. Can be 'ServerLogs' or 'UpgradeLogs'.
   */
  type?: string;

  /**
   * URL to download the log file from.
   */
  url?: string;
}
```

**Retained Swagger or projection evidence**

`projects/specification/postgresql/resource-manager/Microsoft.DBforPostgreSQL/PostgreSql/swagger/stable/2026-10-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "CapturedLogProperties",
  "properties",
  "type"
]
```

```json
{
  "type": "string",
  "description": "Type of log file. Can be 'ServerLogs' or 'UpgradeLogs'."
}
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 1 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** SDK/service owners may remove the earlier shadowed application, preserving the effective winner. Any intended SDK rename is a separate compatibility decision.

## recoveryservicesbackup-shadowed-csharp

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup` / `2026-11-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 3.
- **Cause:** shadowed-sdk-application.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** AzureIaaSVMProtectedItemExtendedInfo.oldestRecoveryPointInVault, oldestRecoveryPointInArchive and newestRecoveryPointInArchive first receive PascalCase C# names without On. Later exact-target C# applications add the On suffix and supersede the earlier values. The reported earlier applications have no final SDK naming effect.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                                                                                | Exact authored excerpt                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/client.tsp:2359](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/client.tsp#L2359-L2367) | `@@clientName( AzureIaaSVMProtectedItemExtendedInfo.oldestRecoveryPointInVault, "OldestRecoveryPointInVault", "csharp" );`     |
| [specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/client.tsp:2364](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/client.tsp#L2364-L2372) | `@@clientName( AzureIaaSVMProtectedItemExtendedInfo.oldestRecoveryPointInArchive, "OldestRecoveryPointInArchive", "csharp" );` |
| [specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/client.tsp:2354](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/client.tsp#L2354-L2362) | `@@clientName( AzureIaaSVMProtectedItemExtendedInfo.newestRecoveryPointInArchive, "NewestRecoveryPointInArchive", "csharp" );` |

**TypeSpec source and supporting declarations**

[specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/client.tsp:2354](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/client.tsp#L2354-L2368)

```typespec
@@clientName(
  AzureIaaSVMProtectedItemExtendedInfo.newestRecoveryPointInArchive,
  "NewestRecoveryPointInArchive",
  "csharp"
);
@@clientName(
  AzureIaaSVMProtectedItemExtendedInfo.oldestRecoveryPointInVault,
  "OldestRecoveryPointInVault",
  "csharp"
);
@@clientName(
  AzureIaaSVMProtectedItemExtendedInfo.oldestRecoveryPointInArchive,
  "OldestRecoveryPointInArchive",
  "csharp"
);
```

[specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/client.tsp:3222](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/client.tsp#L3222-L3246)

```typespec
@@clientName(
  AzureIaaSVMProtectedItemExtendedInfo.oldestRecoveryPointInVault,
  "OldestRecoveryPointInVaultOn",
  "csharp"
);
@@clientName(
  AzureVmWorkloadProtectedItemExtendedInfo.oldestRecoveryPointInVault,
  "OldestRecoveryPointInVaultOn",
  "csharp"
);
@@clientName(
  AzureIaaSVMProtectedItemExtendedInfo.oldestRecoveryPointInArchive,
  "OldestRecoveryPointInArchiveOn",
  "csharp"
);
@@clientName(
  AzureVmWorkloadProtectedItemExtendedInfo.oldestRecoveryPointInArchive,
  "OldestRecoveryPointInArchiveOn",
  "csharp"
);
@@clientName(
  AzureIaaSVMProtectedItemExtendedInfo.newestRecoveryPointInArchive,
  "NewestRecoveryPointInArchiveOn",
  "csharp"
);
```

[specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/models.tsp:4185](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/models.tsp#L4185-L4199)

```typespec

  /**
   * The oldest backup copy available for this backup item in vault tier
   */
  oldestRecoveryPointInVault?: utcDateTime;

  /**
   * The oldest backup copy available for this backup item in archive tier
   */
  oldestRecoveryPointInArchive?: utcDateTime;

  /**
   * The latest backup copy available for this backup item in archive tier
   */
  newestRecoveryPointInArchive?: utcDateTime;
```

**Retained Swagger or projection evidence**

`projects/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/swagger/stable/2026-11-01/bms.json`; exact pointer segments:

```json
[
  "definitions",
  "AzureIaaSVMProtectedItemExtendedInfo",
  "properties",
  "newestRecoveryPointInArchive"
]
```

```json
{
  "type": "string",
  "format": "date-time",
  "description": "The latest backup copy available for this backup item in archive tier"
}
```

`projects/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/swagger/stable/2026-11-01/bms.json`; exact pointer segments:

```json
[
  "definitions",
  "AzureIaaSVMProtectedItemExtendedInfo",
  "properties",
  "oldestRecoveryPointInArchive"
]
```

```json
{
  "type": "string",
  "format": "date-time",
  "description": "The oldest backup copy available for this backup item in archive tier"
}
```

`projects/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/swagger/stable/2026-11-01/bms.json`; exact pointer segments:

```json
[
  "definitions",
  "AzureIaaSVMProtectedItemExtendedInfo",
  "properties",
  "oldestRecoveryPointInVault"
]
```

```json
{
  "type": "string",
  "format": "date-time",
  "description": "The oldest backup copy available for this backup item in vault tier"
}
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 3 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** SDK/service owners may remove the three shadowed earlier applications, preserving the effective On-suffixed names.

## openshift-duplicate-csharp

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/OpenShiftClusters` / `2025-07-25`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 2.
- **Cause:** duplicate-scoped-sdk-applications.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** NetworkProfile.preconfiguredNSG has two adjacent identical C# PreconfiguredNsg applications. Both independently removable warnings remain separate raw source observations.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                                                | Exact authored excerpt                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| [specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/OpenShiftClusters/client.tsp:61](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/OpenShiftClusters/client.tsp#L61-L69) | `@@clientName(NetworkProfile.preconfiguredNSG, "PreconfiguredNsg", "csharp");` |
| [specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/OpenShiftClusters/client.tsp:62](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/OpenShiftClusters/client.tsp#L62-L70) | `@@clientName(NetworkProfile.preconfiguredNSG, "PreconfiguredNsg", "csharp");` |

**TypeSpec source and supporting declarations**

[specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/OpenShiftClusters/client.tsp:61](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/OpenShiftClusters/client.tsp#L61-L62)

```typespec
@@clientName(NetworkProfile.preconfiguredNSG, "PreconfiguredNsg", "csharp");
@@clientName(NetworkProfile.preconfiguredNSG, "PreconfiguredNsg", "csharp");
```

**Retained Swagger or projection evidence**

`projects/specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/OpenShiftClusters/swagger/stable/2025-07-25/redhatopenshift.json`; exact pointer segments:

```json
[
  "definitions",
  "NetworkProfile",
  "properties",
  "preconfiguredNSG"
]
```

```json
{
  "$ref": "#/definitions/PreconfiguredNSG",
  "description": "Specifies whether subnets are pre-attached with an NSG"
}
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 2 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Remove at most one duplicate after service-owner review, preserving the meaningful remaining C# name.

## deploymentstacks-propagated-body-applications

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/resources/resource-manager/Microsoft.Resources/deploymentStacks` / `2025-07-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 6.
- **Cause:** body-name-application-collapse.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** Six apparently unique augment targets are operation copies of DeploymentStackCommonOps at resource-group, subscription and management-group scopes. One read-only project compile disproved the initial shared-property-object hypothesis: there are six distinct parameter objects. However, each validateStack body carries all three authored validateStack applications, and each createOrUpdate resource carries all three create applications. All use deploymentStack. The actual packed SDK resolver returns deploymentStack and unchanged exact=false after omitting any one application, on all six parameter objects. The six exact retained Swagger operation bodies use deploymentStack without x-ms-client-name.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                                | Exact authored excerpt                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| [specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/back-compat.tsp:28](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/back-compat.tsp#L28-L36) | `@@clientName( DeploymentStacksAtResourceGroup.validateStack::parameters.body, "deploymentStack" );`        |
| [specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/back-compat.tsp:32](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/back-compat.tsp#L32-L40) | `@@clientName( DeploymentStacksAtSubscription.validateStack::parameters.body, "deploymentStack" );`         |
| [specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/back-compat.tsp:36](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/back-compat.tsp#L36-L44) | `@@clientName( DeploymentStacksAtManagementGroup.validateStack::parameters.body, "deploymentStack" );`      |
| [specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/back-compat.tsp:15](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/back-compat.tsp#L15-L23) | `@@clientName( DeploymentStacksAtResourceGroup.createOrUpdate::parameters.resource, "deploymentStack" );`   |
| [specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/back-compat.tsp:19](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/back-compat.tsp#L19-L27) | `@@clientName( DeploymentStacksAtSubscription.createOrUpdate::parameters.resource, "deploymentStack" );`    |
| [specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/back-compat.tsp:23](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/back-compat.tsp#L23-L31) | `@@clientName( DeploymentStacksAtManagementGroup.createOrUpdate::parameters.resource, "deploymentStack" );` |

**Additional captured semantic evidence:** [deployment-stack-parameter-identities.json](receipts/deployment-stack-parameter-identities.json), [deployment-stack-parameter-identities.command.json](receipts/deployment-stack-parameter-identities.command.json)

**TypeSpec source and supporting declarations**

[specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/routes.tsp:17](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/routes.tsp#L17-L22)

```typespec
// Interface for all stack operations with the scoping parameterized.
// For some reason, the ArmResourceActionAsync type requires the base params extends this reflection model type.
interface DeploymentStackCommonOps<
  Scope extends Azure.ResourceManager.Foundations.SimpleResource,
  ResourceName extends valueof string = ""
> {
```

[specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/routes.tsp:37](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/routes.tsp#L37-L57)

```typespec
  /** Runs preflight validation on the Deployment stack template at the specified scope to verify its acceptance to Azure Resource Manager. */
  #suppress "@azure-tools/typespec-azure-resource-manager/arm-post-operation-response-codes" "Back compat. There's a 400 response for validation failures."
  @added(Versions.v2024_03_01)
  @action("validate")
  validateStack is Extension.ActionAsync<
    Scope,
    DeploymentStack,
    DeploymentStack,
    DeploymentStackValidateResult,
    OverrideResourceName = ResourceName,
    Error =
      | ErrorResponse
      | ValidationBadRequestResponse<DeploymentStackValidateResult>
  >;

  /** Creates or updates a Deployment stack at the specified scope. */
  createOrUpdate is Extension.CreateOrReplaceAsync<
    Scope,
    DeploymentStack,
    OverrideResourceName = ResourceName
  >;
```

[specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/routes.tsp:83](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/routes.tsp#L83-L96)

```typespec
@armResourceOperations
@tag("DeploymentStacksAtResourceGroup")
interface DeploymentStacksAtResourceGroup
  extends DeploymentStackCommonOps<Extension.ResourceGroup> {}

@armResourceOperations
@tag("DeploymentStacksAtSubscription")
interface DeploymentStacksAtSubscription
  extends DeploymentStackCommonOps<Extension.Subscription> {}

@armResourceOperations
@tag("DeploymentStacksAtManagementGroup")
interface DeploymentStacksAtManagementGroup
  extends DeploymentStackCommonOps<Extension.ManagementGroup<"managementGroupId">> {}
```

[specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/back-compat.tsp:15](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/back-compat.tsp#L15-L39)

```typespec
@@clientName(
  DeploymentStacksAtResourceGroup.createOrUpdate::parameters.resource,
  "deploymentStack"
);
@@clientName(
  DeploymentStacksAtSubscription.createOrUpdate::parameters.resource,
  "deploymentStack"
);
@@clientName(
  DeploymentStacksAtManagementGroup.createOrUpdate::parameters.resource,
  "deploymentStack"
);

@@clientName(
  DeploymentStacksAtResourceGroup.validateStack::parameters.body,
  "deploymentStack"
);
@@clientName(
  DeploymentStacksAtSubscription.validateStack::parameters.body,
  "deploymentStack"
);
@@clientName(
  DeploymentStacksAtManagementGroup.validateStack::parameters.body,
  "deploymentStack"
);
```

**Retained Swagger or projection evidence**

`projects/specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/swagger/stable/2025-07-01/deploymentStacks.json`; exact pointer segments:

```json
[
  "paths",
  "/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Resources/deploymentStacks/{deploymentStackName}",
  "put",
  "parameters"
]
```

```json
[
  {
    "name": "deploymentStack",
    "in": "body",
    "description": "Resource create parameters.",
    "required": true,
    "schema": {
      "$ref": "#/definitions/DeploymentStack"
    }
  }
]
```

`projects/specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/swagger/stable/2025-07-01/deploymentStacks.json`; exact pointer segments:

```json
[
  "paths",
  "/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Resources/deploymentStacks/{deploymentStackName}/validate",
  "post",
  "parameters"
]
```

```json
[
  {
    "name": "deploymentStack",
    "in": "body",
    "description": "The content of the action request",
    "required": true,
    "schema": {
      "$ref": "#/definitions/DeploymentStack"
    }
  }
]
```

`projects/specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/swagger/stable/2025-07-01/deploymentStacks.json`; exact pointer segments:

```json
[
  "paths",
  "/subscriptions/{subscriptionId}/providers/Microsoft.Resources/deploymentStacks/{deploymentStackName}",
  "put",
  "parameters"
]
```

```json
[
  {
    "name": "deploymentStack",
    "in": "body",
    "description": "Resource create parameters.",
    "required": true,
    "schema": {
      "$ref": "#/definitions/DeploymentStack"
    }
  }
]
```

`projects/specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/swagger/stable/2025-07-01/deploymentStacks.json`; exact pointer segments:

```json
[
  "paths",
  "/subscriptions/{subscriptionId}/providers/Microsoft.Resources/deploymentStacks/{deploymentStackName}/validate",
  "post",
  "parameters"
]
```

```json
[
  {
    "name": "deploymentStack",
    "in": "body",
    "description": "The content of the action request",
    "required": true,
    "schema": {
      "$ref": "#/definitions/DeploymentStack"
    }
  }
]
```

`projects/specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/swagger/stable/2025-07-01/deploymentStacks.json`; exact pointer segments:

```json
[
  "paths",
  "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentStacks/{deploymentStackName}",
  "put",
  "parameters"
]
```

```json
[
  {
    "name": "deploymentStack",
    "in": "body",
    "description": "Resource create parameters.",
    "required": true,
    "schema": {
      "$ref": "#/definitions/DeploymentStack"
    }
  }
]
```

`projects/specification/resources/resource-manager/Microsoft.Resources/deploymentStacks/swagger/stable/2025-07-01/deploymentStacks.json`; exact pointer segments:

```json
[
  "paths",
  "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentStacks/{deploymentStackName}/validate",
  "post",
  "parameters"
]
```

```json
[
  {
    "name": "deploymentStack",
    "in": "body",
    "description": "The content of the action request",
    "required": true,
    "schema": {
      "$ref": "#/definitions/DeploymentStack"
    }
  }
]
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 6 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** SDK/service owners may consolidate propagated applications, retaining at least one effective create and one effective validate body naming application after checking all scopes. Do not remove all six warnings together or infer that the six parameter objects are identical. No compiler or rule change is proposed from count parity.

## securityinsights-inherited-csharp-repeats

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights` / `2025-10-01-preview`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 8.
- **Cause:** inherited-sdk-repeat.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** createdDateUTC and lastUpdatedDateUTC are inherited from AlertRuleTemplatePropertiesBase. MicrosoftSecurityIncidentCreationAlertRuleTemplateProperties extends that base; MLBehaviorAnalyticsAlertRuleTemplateProperties and ThreatIntelligenceAlertRuleTemplateProperties extend AlertRuleTemplateWithMitreProperties, which extends the same base. Each inherited property has four C# applications with the same CreatedOn or LastUpdatedOn spelling. All eight warnings remain raw application counts, not eight distinct properties.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                                                        | Exact authored excerpt                                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| [specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp:727](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp#L727-L735)    | `@@clientName( MicrosoftSecurityIncidentCreationAlertRuleTemplateProperties.lastUpdatedDateUTC, "LastUpdatedOn", "csharp" );` |
| [specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp:757](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp#L757-L765)    | `@@clientName( MLBehaviorAnalyticsAlertRuleTemplateProperties.lastUpdatedDateUTC, "LastUpdatedOn", "csharp" );`               |
| [specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp:828](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp#L828-L836)    | `@@clientName( AlertRuleTemplatePropertiesBase.lastUpdatedDateUTC, "LastUpdatedOn", "csharp" );`                              |
| [specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp:1187](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp#L1187-L1195) | `@@clientName( ThreatIntelligenceAlertRuleTemplateProperties.lastUpdatedDateUTC, "LastUpdatedOn", "csharp" );`                |
| [specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp:722](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp#L722-L730)    | `@@clientName( MicrosoftSecurityIncidentCreationAlertRuleTemplateProperties.createdDateUTC, "CreatedOn", "csharp" );`         |
| [specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp:752](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp#L752-L760)    | `@@clientName( MLBehaviorAnalyticsAlertRuleTemplateProperties.createdDateUTC, "CreatedOn", "csharp" );`                       |
| [specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp:823](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp#L823-L831)    | `@@clientName( AlertRuleTemplatePropertiesBase.createdDateUTC, "CreatedOn", "csharp" );`                                      |
| [specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp:1182](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp#L1182-L1190) | `@@clientName( ThreatIntelligenceAlertRuleTemplateProperties.createdDateUTC, "CreatedOn", "csharp" );`                        |

**TypeSpec source and supporting declarations**

[specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/models.tsp:8829](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/models.tsp#L8829-L8849)

```typespec
model AlertRuleTemplatePropertiesBase {
  /**
   * The number of alert rules that were created by this template
   */
  alertRulesCreatedByTemplateCount?: int32;

  /**
   * The last time that this alert rule template has been updated.
   */
  #suppress "@azure-tools/typespec-azure-core/casing-style" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  @visibility(Lifecycle.Read)
  // FIXME: (utcDateTime) Please double check that this is the correct type for your scenario.
  lastUpdatedDateUTC?: utcDateTime;

  /**
   * The time that this alert rule template has been added.
   */
  #suppress "@azure-tools/typespec-azure-core/casing-style" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  @visibility(Lifecycle.Read)
  // FIXME: (utcDateTime) Please double check that this is the correct type for your scenario.
  createdDateUTC?: utcDateTime;
```

[specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/models.tsp:8878](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/models.tsp#L8878-L8879)

```typespec
model AlertRuleTemplateWithMitreProperties
  extends AlertRuleTemplatePropertiesBase {
```

[specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/models.tsp:9140](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/models.tsp#L9140-L9145)

```typespec
@added(Versions.v2025_10_01_preview)
model MLBehaviorAnalyticsAlertRuleTemplateProperties
  extends AlertRuleTemplateWithMitreProperties {
  /**
   * The severity for alerts created by this alert rule.
   */
```

[specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/models.tsp:9577](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/models.tsp#L9577-L9581)

```typespec
@added(Versions.v2025_10_01_preview)
model ThreatIntelligenceAlertRuleTemplateProperties
  extends AlertRuleTemplateWithMitreProperties {
  /**
   * The severity for alerts created by this alert rule.
```

[specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/models.tsp:9680](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/models.tsp#L9680-L9684)

```typespec
model MicrosoftSecurityIncidentCreationAlertRuleTemplateProperties
  extends AlertRuleTemplatePropertiesBase {
  /**
   * the alerts' displayNames on which the cases will be generated
   */
```

[specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp:722](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp#L722-L731)

```typespec
@@clientName(
  MicrosoftSecurityIncidentCreationAlertRuleTemplateProperties.createdDateUTC,
  "CreatedOn",
  "csharp"
);
@@clientName(
  MicrosoftSecurityIncidentCreationAlertRuleTemplateProperties.lastUpdatedDateUTC,
  "LastUpdatedOn",
  "csharp"
);
```

[specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp:752](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp#L752-L761)

```typespec
@@clientName(
  MLBehaviorAnalyticsAlertRuleTemplateProperties.createdDateUTC,
  "CreatedOn",
  "csharp"
);
@@clientName(
  MLBehaviorAnalyticsAlertRuleTemplateProperties.lastUpdatedDateUTC,
  "LastUpdatedOn",
  "csharp"
);
```

[specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp:823](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp#L823-L832)

```typespec
@@clientName(
  AlertRuleTemplatePropertiesBase.createdDateUTC,
  "CreatedOn",
  "csharp"
);
@@clientName(
  AlertRuleTemplatePropertiesBase.lastUpdatedDateUTC,
  "LastUpdatedOn",
  "csharp"
);
```

[specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp:1182](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/client.tsp#L1182-L1191)

```typespec
@@clientName(
  ThreatIntelligenceAlertRuleTemplateProperties.createdDateUTC,
  "CreatedOn",
  "csharp"
);
@@clientName(
  ThreatIntelligenceAlertRuleTemplateProperties.lastUpdatedDateUTC,
  "LastUpdatedOn",
  "csharp"
);
```

**Retained Swagger or projection evidence**

`projects/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/swagger/preview/2025-10-01-preview/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "AlertRuleTemplatePropertiesBase",
  "properties",
  "createdDateUTC"
]
```

```json
{
  "type": "string",
  "format": "date-time",
  "description": "The time that this alert rule template has been added.",
  "readOnly": true
}
```

`projects/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/swagger/preview/2025-10-01-preview/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "AlertRuleTemplatePropertiesBase",
  "properties",
  "lastUpdatedDateUTC"
]
```

```json
{
  "type": "string",
  "format": "date-time",
  "description": "The last time that this alert rule template has been updated.",
  "readOnly": true
}
```

Exact schema/property lookups absent from the selected Swagger:
`[["MLBehaviorAnalyticsAlertRuleTemplateProperties", "createdDateUTC"], ["MLBehaviorAnalyticsAlertRuleTemplateProperties", "lastUpdatedDateUTC"], ["MicrosoftSecurityIncidentCreationAlertRuleTemplateProperties", "createdDateUTC"], ["MicrosoftSecurityIncidentCreationAlertRuleTemplateProperties", "lastUpdatedDateUTC"], ["ThreatIntelligenceAlertRuleTemplateProperties", "createdDateUTC"], ["ThreatIntelligenceAlertRuleTemplateProperties", "lastUpdatedDateUTC"]]`.
An absent lookup is not a predicate-failure or correspondence claim.

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 8 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** SDK/service owners may consolidate repeated C# applications while retaining at least one effective CreatedOn and LastUpdatedOn rename and all independent Java scope behavior. Do not remove all warned applications together.

## sql-duplicate-csharp

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/sql/resource-manager/Microsoft.Sql/SQL` / `2026-08-01-preview`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 4.
- **Cause:** duplicate-scoped-sdk-applications.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** DatabaseColumnProperties.memoryOptimized and DatabaseTableProperties.memoryOptimized each have two identical C# IsMemoryOptimized applications. All four raw warnings remain distinct independently removable applications.

**Captured source applications**

| Source                                                                                                                                                                                                                                          | Exact authored excerpt                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| [specification/sql/resource-manager/Microsoft.Sql/SQL/client.tsp:1025](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/sql/resource-manager/Microsoft.Sql/SQL/client.tsp#L1025-L1033) | `@@clientName( DatabaseColumnProperties.memoryOptimized, "IsMemoryOptimized", "csharp" );` |
| [specification/sql/resource-manager/Microsoft.Sql/SQL/client.tsp:1435](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/sql/resource-manager/Microsoft.Sql/SQL/client.tsp#L1435-L1443) | `@@clientName( DatabaseColumnProperties.memoryOptimized, "IsMemoryOptimized", "csharp" );` |
| [specification/sql/resource-manager/Microsoft.Sql/SQL/client.tsp:1030](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/sql/resource-manager/Microsoft.Sql/SQL/client.tsp#L1030-L1038) | `@@clientName( DatabaseTableProperties.memoryOptimized, "IsMemoryOptimized", "csharp" );`  |
| [specification/sql/resource-manager/Microsoft.Sql/SQL/client.tsp:1441](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/sql/resource-manager/Microsoft.Sql/SQL/client.tsp#L1441-L1449) | `@@clientName( DatabaseTableProperties.memoryOptimized, "IsMemoryOptimized", "csharp" );`  |

**TypeSpec source and supporting declarations**

[specification/sql/resource-manager/Microsoft.Sql/SQL/client.tsp:1025](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/sql/resource-manager/Microsoft.Sql/SQL/client.tsp#L1025-L1034)

```typespec
@@clientName(
  DatabaseColumnProperties.memoryOptimized,
  "IsMemoryOptimized",
  "csharp"
);
@@clientName(
  DatabaseTableProperties.memoryOptimized,
  "IsMemoryOptimized",
  "csharp"
);
```

[specification/sql/resource-manager/Microsoft.Sql/SQL/client.tsp:1435](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/sql/resource-manager/Microsoft.Sql/SQL/client.tsp#L1435-L1445)

```typespec
@@clientName(
  DatabaseColumnProperties.memoryOptimized,
  "IsMemoryOptimized",
  "csharp"
);
@@usage(DatabaseTable, Azure.ClientGenerator.Core.Usage.input, "csharp");
@@clientName(
  DatabaseTableProperties.memoryOptimized,
  "IsMemoryOptimized",
  "csharp"
);
```

**Retained Swagger or projection evidence**

`projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/common.json`; exact pointer segments:

```json
[
  "definitions",
  "DatabaseColumnProperties",
  "properties",
  "memoryOptimized"
]
```

```json
{
  "type": "boolean",
  "description": "Whether or not the column belongs to a memory optimized table."
}
```

`projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/common.json`; exact pointer segments:

```json
[
  "definitions",
  "DatabaseTableProperties",
  "properties",
  "memoryOptimized"
]
```

```json
{
  "type": "boolean",
  "description": "Whether or not the table is memory optimized."
}
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 4 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Remove at most one duplicate per exact target after service-owner review, preserving each meaningful remaining C# name.

## storage-duplicate-body-applications

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/storage/resource-manager/Microsoft.Storage/Storage` / `2026-09-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 2.
- **Cause:** body-name-application-collapse.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** ImmutabilityPolicies.createOrUpdateImmutabilityPolicy.resource has two identical common parameters applications. Both raw warnings are retained. The exact retained operation's body name is parameters and its source application multiplicity is not represented by an emitted extension.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                 | Exact authored excerpt                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| [specification/storage/resource-manager/Microsoft.Storage/Storage/back-compatible.tsp:353](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/storage/resource-manager/Microsoft.Storage/Storage/back-compatible.tsp#L353-L361) | `@@clientName( ImmutabilityPolicies.createOrUpdateImmutabilityPolicy::parameters.resource, "parameters" );` |
| [specification/storage/resource-manager/Microsoft.Storage/Storage/back-compatible.tsp:395](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/storage/resource-manager/Microsoft.Storage/Storage/back-compatible.tsp#L395-L403) | `@@clientName( ImmutabilityPolicies.createOrUpdateImmutabilityPolicy::parameters.resource, "parameters" );` |

**TypeSpec source and supporting declarations**

[specification/storage/resource-manager/Microsoft.Storage/Storage/back-compatible.tsp:353](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/storage/resource-manager/Microsoft.Storage/Storage/back-compatible.tsp#L353-L356)

```typespec
@@clientName(
  ImmutabilityPolicies.createOrUpdateImmutabilityPolicy::parameters.resource,
  "parameters"
);
```

[specification/storage/resource-manager/Microsoft.Storage/Storage/back-compatible.tsp:395](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/storage/resource-manager/Microsoft.Storage/Storage/back-compatible.tsp#L395-L398)

```typespec
@@clientName(
  ImmutabilityPolicies.createOrUpdateImmutabilityPolicy::parameters.resource,
  "parameters"
);
```

**Retained Swagger or projection evidence**

`projects/specification/storage/resource-manager/Microsoft.Storage/Storage/swagger/stable/2026-09-01/openapi.json`; exact pointer segments:

```json
[
  "paths",
  "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName}/immutabilityPolicies/default",
  "put",
  "parameters"
]
```

```json
[
  {
    "name": "parameters",
    "in": "body",
    "description": "The ImmutabilityPolicy Properties that will be created or updated to a blob container.",
    "required": false,
    "schema": {
      "$ref": "#/definitions/ImmutabilityPolicy"
    }
  }
]
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 2 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Remove at most one duplicate after service-owner review, preserving the meaningful remaining body rename. The exact retained BlobContainers_CreateOrUpdateImmutabilityPolicy PUT body has name parameters and no x-ms-client-name.

## storage-duplicate-csharp

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/storage/resource-manager/Microsoft.Storage/Storage` / `2026-09-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 5.
- **Cause:** duplicate-scoped-sdk-applications.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** BlobServicePropertiesProperties.automaticSnapshotPolicyEnabled has three identical C# IsAutomaticSnapshotPolicyEnabled applications. ActiveDirectoryProperties.domainGuid has two identical C# ActiveDirectoryDomainGuid applications. All five independently removable warnings remain raw observations.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                  | Exact authored excerpt                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp:908](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp#L908-L916)    | `@@clientName( BlobServicePropertiesProperties.automaticSnapshotPolicyEnabled, "IsAutomaticSnapshotPolicyEnabled", "csharp" );` |
| [specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp:971](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp#L971-L979)    | `@@clientName( BlobServicePropertiesProperties.automaticSnapshotPolicyEnabled, "IsAutomaticSnapshotPolicyEnabled", "csharp" );` |
| [specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp:1295](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp#L1295-L1303) | `@@clientName( BlobServicePropertiesProperties.automaticSnapshotPolicyEnabled, "IsAutomaticSnapshotPolicyEnabled", "csharp" );` |
| [specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp:204](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp#L204-L212)    | `@@clientName( ActiveDirectoryProperties.domainGuid, "ActiveDirectoryDomainGuid", "csharp" );`                                  |
| [specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp:1288](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp#L1288-L1296) | `@@clientName( ActiveDirectoryProperties.domainGuid, "ActiveDirectoryDomainGuid", "csharp" );`                                  |

**TypeSpec source and supporting declarations**

[specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp:908](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp#L908-L912)

```typespec
@@clientName(
  BlobServicePropertiesProperties.automaticSnapshotPolicyEnabled,
  "IsAutomaticSnapshotPolicyEnabled",
  "csharp"
);
```

[specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp:971](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp#L971-L975)

```typespec
@@clientName(
  BlobServicePropertiesProperties.automaticSnapshotPolicyEnabled,
  "IsAutomaticSnapshotPolicyEnabled",
  "csharp"
);
```

[specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp:1295](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp#L1295-L1299)

```typespec
@@clientName(
  BlobServicePropertiesProperties.automaticSnapshotPolicyEnabled,
  "IsAutomaticSnapshotPolicyEnabled",
  "csharp"
);
```

[specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp:204](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp#L204-L208)

```typespec
@@clientName(
  ActiveDirectoryProperties.domainGuid,
  "ActiveDirectoryDomainGuid",
  "csharp"
);
```

[specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp:1288](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/storage/resource-manager/Microsoft.Storage/Storage/client.tsp#L1288-L1292)

```typespec
@@clientName(
  ActiveDirectoryProperties.domainGuid,
  "ActiveDirectoryDomainGuid",
  "csharp"
);
```

**Retained Swagger or projection evidence**

`projects/specification/storage/resource-manager/Microsoft.Storage/Storage/swagger/stable/2026-09-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "ActiveDirectoryProperties",
  "properties",
  "domainGuid"
]
```

```json
{
  "type": "string",
  "description": "Specifies the domain GUID. If directoryServiceOptions is set to AD (AD DS authentication), this property is required. If directoryServiceOptions is set to AADDS (Entra DS authentication), this property can be omitted. If directoryServiceOptions is set to AADKERB (Entra authentication), this property is optional; it is needed to support configuration of directory- and file-level permissions via Windows File Explorer, but is not required for authentication."
}
```

`projects/specification/storage/resource-manager/Microsoft.Storage/Storage/swagger/stable/2026-09-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "BlobServicePropertiesProperties",
  "properties",
  "automaticSnapshotPolicyEnabled"
]
```

```json
{
  "type": "boolean",
  "description": "Deprecated in favor of isVersioningEnabled property."
}
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 5 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** SDK/service owners may consolidate duplicates while retaining at least one effective application per exact target. Do not delete all warned copies together.

## storagesync-duplicate-csharp

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync` / `2025-12-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 2.
- **Cause:** duplicate-scoped-sdk-applications.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** ServerEndpointCloudTieringStatus.healthLastUpdatedTimestamp has two identical C# HealthLastUpdatedOn applications. Both raw warnings are retained independently.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                       | Exact authored excerpt                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| [specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/client.tsp:123](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/client.tsp#L123-L131) | `@@clientName( ServerEndpointCloudTieringStatus.healthLastUpdatedTimestamp, "HealthLastUpdatedOn", "csharp" );` |
| [specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/client.tsp:150](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/client.tsp#L150-L158) | `@@clientName( ServerEndpointCloudTieringStatus.healthLastUpdatedTimestamp, "HealthLastUpdatedOn", "csharp" );` |

**TypeSpec source and supporting declarations**

[specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/client.tsp:123](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/client.tsp#L123-L127)

```typespec
@@clientName(
  ServerEndpointCloudTieringStatus.healthLastUpdatedTimestamp,
  "HealthLastUpdatedOn",
  "csharp"
);
```

[specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/client.tsp:150](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/client.tsp#L150-L154)

```typespec
@@clientName(
  ServerEndpointCloudTieringStatus.healthLastUpdatedTimestamp,
  "HealthLastUpdatedOn",
  "csharp"
);
```

**Retained Swagger or projection evidence**

`projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json`; exact pointer segments:

```json
[
  "definitions",
  "ServerEndpointCloudTieringStatus",
  "properties",
  "healthLastUpdatedTimestamp"
]
```

```json
{
  "type": "string",
  "format": "date-time",
  "description": "The last updated timestamp of health state",
  "readOnly": true
}
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 2 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Remove at most one duplicate after service-owner review, preserving the meaningful remaining C# name.

## avs-duplicate-body-applications

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/vmware/resource-manager/Microsoft.AVS/AVS` / `2026-03-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 2.
- **Cause:** body-name-application-collapse.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** WorkloadNetworkDhcpConfigurations.update.properties has two identical common workloadNetworkDhcp applications. The source update is ArmCustomPatchAsync<WorkloadNetworkDhcp, WorkloadNetworkDhcp>. Exact retained PATCH operation WorkloadNetworks_UpdateDhcp has body name workloadNetworkDhcp and no x-ms-client-name. Both raw source warnings remain distinct.

**Captured source applications**

| Source                                                                                                                                                                                                                                                                                                    | Exact authored excerpt                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| [specification/vmware/resource-manager/Microsoft.AVS/AVS/workloadNetworks-dhcpConfigurations.tsp:50](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/vmware/resource-manager/Microsoft.AVS/AVS/workloadNetworks-dhcpConfigurations.tsp#L50-L58) | `@@clientName( WorkloadNetworkDhcpConfigurations.update::parameters.properties, "workloadNetworkDhcp" );` |
| [specification/vmware/resource-manager/Microsoft.AVS/AVS/workloadNetworks-dhcpConfigurations.tsp:55](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/vmware/resource-manager/Microsoft.AVS/AVS/workloadNetworks-dhcpConfigurations.tsp#L55-L63) | `@@clientName( WorkloadNetworkDhcpConfigurations.update::parameters.properties, "workloadNetworkDhcp" );` |

**TypeSpec source and supporting declarations**

[specification/vmware/resource-manager/Microsoft.AVS/AVS/workloadNetworks-dhcpConfigurations.tsp:37](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/vmware/resource-manager/Microsoft.AVS/AVS/workloadNetworks-dhcpConfigurations.tsp#L37-L39)

```typespec
  @patch(#{ implicitOptionality: false })
  update is ArmCustomPatchAsync<WorkloadNetworkDhcp, WorkloadNetworkDhcp>;
```

[specification/vmware/resource-manager/Microsoft.AVS/AVS/workloadNetworks-dhcpConfigurations.tsp:50](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/vmware/resource-manager/Microsoft.AVS/AVS/workloadNetworks-dhcpConfigurations.tsp#L50-L58)

```typespec
@@clientName(
  WorkloadNetworkDhcpConfigurations.update::parameters.properties,
  "workloadNetworkDhcp"
);

@@clientName(
  WorkloadNetworkDhcpConfigurations.update::parameters.properties,
  "workloadNetworkDhcp"
);
```

**Retained Swagger or projection evidence**

`projects/specification/vmware/resource-manager/Microsoft.AVS/AVS/swagger/stable/2026-03-01/vmware.json`; exact pointer segments:

```json
[
  "paths",
  "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/workloadNetworks/default/dhcpConfigurations/{dhcpId}",
  "patch",
  "parameters"
]
```

```json
[
  {
    "name": "workloadNetworkDhcp",
    "in": "body",
    "description": "The resource properties to be updated.",
    "required": true,
    "schema": {
      "$ref": "#/definitions/WorkloadNetworkDhcp"
    }
  }
]
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 2 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Remove at most one duplicate after service-owner review, preserving the meaningful remaining body rename.

## appservice-duplicate-csharp

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/web/resource-manager/Microsoft.Web/AppService` / `2026-09-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 10.
- **Cause:** duplicate-scoped-sdk-applications.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** Five exact properties each have two identical C# applications: AppServiceEnvironment.ipsslAddressCount IPSslAddressCount; AppServiceEnvironment.userWhitelistedIpRanges UserWhitelistedIPRanges; RemotePrivateEndpointConnectionARMResourceProperties.ipAddresses IPAddresses; FunctionAppStackProperties.preferredOs PreferredOS; SnapshotRestoreRequestProperties.overwrite CanOverwrite. All ten independently removable warnings remain raw application counts.

**Captured source applications**

| Source                                                                                                                                                                                                                                                        | Exact authored excerpt                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| [specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:5915](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L5915-L5923) | `@@clientName( AppServiceEnvironment.ipsslAddressCount, "IPSslAddressCount", "csharp" );`                    |
| [specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:7200](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L7200-L7208) | `@@clientName( AppServiceEnvironment.ipsslAddressCount, "IPSslAddressCount", "csharp" );`                    |
| [specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:6015](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L6015-L6023) | `@@clientName( AppServiceEnvironment.userWhitelistedIpRanges, "UserWhitelistedIPRanges", "csharp" );`        |
| [specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:7205](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L7205-L7213) | `@@clientName( AppServiceEnvironment.userWhitelistedIpRanges, "UserWhitelistedIPRanges", "csharp" );`        |
| [specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:4615](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L4615-L4623) | `@@clientName( RemotePrivateEndpointConnectionARMResourceProperties.ipAddresses, "IPAddresses", "csharp" );` |
| [specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:5922](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L5922-L5930) | `@@clientName( RemotePrivateEndpointConnectionARMResourceProperties.ipAddresses, "IPAddresses", "csharp" );` |
| [specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:5068](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L5068-L5076) | `@@clientName(FunctionAppStackProperties.preferredOs, "PreferredOS", "csharp");`                             |
| [specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:6021](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L6021-L6029) | `@@clientName(FunctionAppStackProperties.preferredOs, "PreferredOS", "csharp");`                             |
| [specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:4923](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L4923-L4931) | `@@clientName( SnapshotRestoreRequestProperties.overwrite, "CanOverwrite", "csharp" );`                      |
| [specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:5086](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L5086-L5094) | `@@clientName( SnapshotRestoreRequestProperties.overwrite, "CanOverwrite", "csharp" );`                      |

**TypeSpec source and supporting declarations**

[specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:5915](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L5915-L5926)

```typespec
@@clientName(
  AppServiceEnvironment.ipsslAddressCount,
  "IPSslAddressCount",
  "csharp"
);
@@clientName(EndpointDetail.ipAddress, "IPAddress", "csharp");
@@clientName(ServerFarmInstance.ipAddress, "IPAddress", "csharp");
@@clientName(
  RemotePrivateEndpointConnectionARMResourceProperties.ipAddresses,
  "IPAddresses",
  "csharp"
);
```

[specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:7200](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L7200-L7209)

```typespec
@@clientName(
  AppServiceEnvironment.ipsslAddressCount,
  "IPSslAddressCount",
  "csharp"
);
@@clientName(
  AppServiceEnvironment.userWhitelistedIpRanges,
  "UserWhitelistedIPRanges",
  "csharp"
);
```

[specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:6015](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L6015-L6021)

```typespec
@@clientName(
  AppServiceEnvironment.userWhitelistedIpRanges,
  "UserWhitelistedIPRanges",
  "csharp"
);
@@clientName(KubeEnvironmentProperties.staticIp, "StaticIP", "csharp");
@@clientName(FunctionAppStackProperties.preferredOs, "PreferredOS", "csharp");
```

[specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:4615](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L4615-L4619)

```typespec
@@clientName(
  RemotePrivateEndpointConnectionARMResourceProperties.ipAddresses,
  "IPAddresses",
  "csharp"
);
```

[specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:5068](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L5068-L5068)

```typespec
@@clientName(FunctionAppStackProperties.preferredOs, "PreferredOS", "csharp");
```

[specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:4923](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L4923-L4927)

```typespec
@@clientName(
  SnapshotRestoreRequestProperties.overwrite,
  "CanOverwrite",
  "csharp"
);
```

[specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:5086](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L5086-L5090)

```typespec
@@clientName(
  SnapshotRestoreRequestProperties.overwrite,
  "CanOverwrite",
  "csharp"
);
```

**Retained Swagger or projection evidence**

`projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-09-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "AppServiceEnvironment",
  "properties",
  "ipsslAddressCount"
]
```

```json
{
  "type": "integer",
  "format": "int32",
  "description": "Number of IP SSL addresses reserved for the App Service Environment."
}
```

`projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-09-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "AppServiceEnvironment",
  "properties",
  "userWhitelistedIpRanges"
]
```

```json
{
  "type": "array",
  "description": "User added ip ranges to whitelist on ASE db",
  "items": {
    "type": "string"
  }
}
```

`projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-09-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "FunctionAppStackProperties",
  "properties",
  "preferredOs"
]
```

```json
{
  "$ref": "#/definitions/StackPreferredOs",
  "description": "Function App stack preferred OS.",
  "readOnly": true
}
```

`projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-09-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "RemotePrivateEndpointConnectionARMResourceProperties",
  "properties",
  "ipAddresses"
]
```

```json
{
  "type": "array",
  "description": "Private IPAddresses mapped to the remote private endpoint",
  "items": {
    "type": "string"
  }
}
```

`projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-09-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "SnapshotRestoreRequestProperties",
  "properties",
  "overwrite"
]
```

```json
{
  "type": "boolean",
  "description": "If <code>true</code> the restore operation can overwrite source app; otherwise, <code>false</code>."
}
```

| Engine          | Observed result                                                                            |
| --------------- | ------------------------------------------------------------------------------------------ |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.            |
| TypeSpec linter | 10 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** Remove at most one duplicate per exact target after service-owner review, preserving each meaningful remaining C# name.

## appservice-shadowed-csharp

- **Classification:** TypeSpec-linter-only.
- **Project/API version:** `specification/web/resource-manager/Microsoft.Web/AppService` / `2026-09-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 2.
- **Cause:** shadowed-sdk-application.
- **Coverage status:** Observed no-effect SDK naming; source/emission policies differ, not literal extension-equality parity.

**Cause and evidence:** DatabaseConnectionProperties.resourceId and DatabaseConnectionPatchRequestProperties.resourceId are distinct authored properties, not inherited aliases. Each earlier C# DatabaseConnectionResourceId application is superseded by a later exact-target ResourceId application at client.tsp:6171 and 6172. Both reported earlier spellings have no final SDK naming effect.

**Captured source applications**

| Source                                                                                                                                                                                                                                                        | Exact authored excerpt                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:4569](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L4569-L4577) | `@@clientName( DatabaseConnectionProperties.resourceId, "DatabaseConnectionResourceId", "csharp" );`             |
| [specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:4574](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L4574-L4582) | `@@clientName( DatabaseConnectionPatchRequestProperties.resourceId, "DatabaseConnectionResourceId", "csharp" );` |

**TypeSpec source and supporting declarations**

[specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:4569](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L4569-L4578)

```typespec
@@clientName(
  DatabaseConnectionProperties.resourceId,
  "DatabaseConnectionResourceId",
  "csharp"
);
@@clientName(
  DatabaseConnectionPatchRequestProperties.resourceId,
  "DatabaseConnectionResourceId",
  "csharp"
);
```

[specification/web/resource-manager/Microsoft.Web/AppService/client.tsp:6171](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/client.tsp#L6171-L6176)

```typespec
@@clientName(DatabaseConnectionProperties.resourceId, "ResourceId", "csharp");
@@clientName(
  DatabaseConnectionPatchRequestProperties.resourceId,
  "ResourceId",
  "csharp"
);
```

[specification/web/resource-manager/Microsoft.Web/AppService/models.tsp:9150](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/models.tsp#L9150-L9154)

```typespec
model DatabaseConnectionProperties {
  /**
   * The resource id of the database.
   */
  resourceId: string;
```

[specification/web/resource-manager/Microsoft.Web/AppService/models.tsp:9193](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/web/resource-manager/Microsoft.Web/AppService/models.tsp#L9193-L9197)

```typespec
model DatabaseConnectionPatchRequestProperties {
  /**
   * The resource id of the database.
   */
  resourceId?: string;
```

**Retained Swagger or projection evidence**

`projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-09-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "DatabaseConnectionPatchRequestProperties",
  "properties",
  "resourceId"
]
```

```json
{
  "type": "string",
  "description": "The resource id of the database."
}
```

`projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-09-01/openapi.json`; exact pointer segments:

```json
[
  "definitions",
  "DatabaseConnectionProperties",
  "properties",
  "resourceId"
]
```

```json
{
  "type": "string",
  "description": "The resource id of the database."
}
```

| Engine          | Observed result                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| Swagger linter  | 0 selected production findings; emitted occurrence and version policy retained.           |
| TypeSpec linter | 2 configured no-effect application warning(s); source applications retained individually. |

**Gap analysis and decision:** SDK/service owners may remove the shadowed earlier applications, preserving the effective ResourceId names. Do not conflate distinct properties merely because their names and values coincide.

## Assessment limits

The captures exercise SDK no-effect checks, not literal extension equality.
Every observed source location is classified once. No unclassified count
residual remains. No missing native-contract behavior was demonstrated by
these inspected findings; this is not exhaustive SDK/data-plane coverage.
The source/latest-version population mismatch and different predicates
prevent a full-equivalence or comparable-defect-percentage conclusion.
Service and SDK owners must approve proposed spec cleanups. Reviewers retain
migration acceptance, artifact/publication review and remaining CI gates.

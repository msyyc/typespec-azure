# One-sided project source and schema examples

All ten Swagger-only projects are below, grouped by the independently investigated cause in [differences.md](differences.md). No TypeSpec-only project was observed. Source excerpts are byte-checked against the frozen Git commit, not fabricated reproducers. The API version names the baseline's selected emitted service version; the TypeSpec linter executes the unprojected source policy described in the report. The complete observations and exact path evidence are retained in the task asset; the samples below do not replace that population.

Every reference group below has exact saved-document/path attribution; the separate Network/SQL/Portal/BatchPricings missing-origin limits do not affect these ten projects. Counts describe observations, not common service-defect identities.

## AzureResilienceManagement

- **Classification:** Swagger-linter-only.
- **Status / cause:** `deprecated-location`; covered only for the approved selection/configuration boundary, not full reference-check equivalence.
- **Project / emitted API:** `specification/azureresiliencemanagement/resource-manager/Microsoft.AzureResilienceManagement/AzureResilienceManagement` / `2026-10-31-preview`.
- **Observed results:** Swagger linter **1**; TypeSpec linter **0**, with authored suppressions honored.
- **Coverage and recommended action:** Approved selection-versus-reference boundary. Latest selection is compliant; emitted deprecated LocationParameter falls back to its v5 registration. Recommend separately evaluating supported LocationResourceParameter authoring and compatibility; do not add reference traversal to this recovery.

### TypeSpec source

[`models/common/common.tsp:12-15`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/azureresiliencemanagement/resource-manager/Microsoft.AzureResilienceManagement/AzureResilienceManagement/models/common/common.tsp#L12-L15); source SHA-256 `7ad89de764041841e2146cb693c3b80ab10ee98762c28fa96a28a57c9901974f`.

```text

@service(#{ title: "Microsoft.AzureResilienceManagement" })
@armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v5)
namespace Microsoft.AzureResilienceManagement;
```

[`main.tsp:52-60`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/azureresiliencemanagement/resource-manager/Microsoft.AzureResilienceManagement/AzureResilienceManagement/main.tsp#L52-L60); source SHA-256 `d0b14a7156a9e5777f8e551b32bfef0f1540490efe652a23ffc78f1c2927a247`.

```text
  @doc("Microsoft.AzureResilienceManagement Resource Provider management API version 2026-10-01.")
  @armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v6)
  v2026_10_01: "2026-10-01",

  @doc("Microsoft.AzureResilienceManagement Resource Provider management API version 2026-10-31-preview.")
  @armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v6)
  @Azure.Core.previewVersion
  v2026_10_31_preview: "2026-10-31-preview",
}
```

### Emitted Swagger observations

**`v5/types.json`: 1 findings.** Saved document `projects/specification/azureresiliencemanagement/resource-manager/Microsoft.AzureResilienceManagement/AzureResilienceManagement/swagger/preview/2026-10-31-preview/openapi.json`; exact path `["paths", "/providers/Microsoft.AzureResilienceManagement/locations/{location}/operationStatuses/{operationId}", "get", "parameters", "1", "$ref"]`.

```json
{
  "$ref": "../../../../../../../../../common-types/resource-management/v5/types.json#/parameters/LocationParameter"
}
```

## Communication

- **Classification:** Swagger-linter-only.
- **Status / cause:** `filename-map`; covered only for the approved selection/configuration boundary, not full reference-check equivalence.
- **Project / emitted API:** `specification/communication/resource-manager/Microsoft.Communication/Communication` / `2026-03-18`.
- **Observed results:** Swagger linter **2**; TypeSpec linter **0**, with authored suppressions honored.
- **Coverage and recommended action:** Approved registry-versus-filename policy difference. Latest selection is compliant; pinned Swagger map expects v5 for a v6 file. Recommend upstream policy review before calling this a bug or changing services. No additional TypeSpec check is justified by these counts.

### TypeSpec source

[`main.tsp:34-38`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/communication/resource-manager/Microsoft.Communication/Communication/main.tsp#L34-L38); source SHA-256 `1389ffbf104728676b7ec846d415e5f6bfe79948ba04b1dd28db88d7ab7721dd`.

```text
@armProviderNamespace
@service(#{ title: "Azure Communication Services Management API" })
@versioned(Versions)
@armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v6)
namespace Microsoft.Communication;
```

### Emitted Swagger observations

**`v6/networksecurityperimeter.json`: 2 findings.** Saved document `projects/specification/communication/resource-manager/Microsoft.Communication/Communication/swagger/stable/2026-03-18/openapi.json`; exact path `["definitions", "CommunicationServiceProperties", "properties", "publicNetworkAccess", "$ref"]`.

```json
{
  "$ref": "../../../../../../../../../common-types/resource-management/v6/networksecurityperimeter.json#/definitions/PublicNetworkAccess"
}
```

## aks

- **Classification:** Swagger-linter-only.
- **Status / cause:** `filename-map`; covered only for the approved selection/configuration boundary, not full reference-check equivalence.
- **Project / emitted API:** `specification/containerservice/resource-manager/Microsoft.ContainerService/aks` / `2026-07-02-preview`.
- **Observed results:** Swagger linter **1**; TypeSpec linter **0**, with authored suppressions honored.
- **Coverage and recommended action:** Approved registry-versus-filename policy difference. Latest selection is compliant; pinned Swagger map expects v5 for a v6 file. Recommend upstream policy review before calling this a bug or changing services. No additional TypeSpec check is justified by these counts.

### TypeSpec source

[`main.tsp:50-56`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/main.tsp#L50-L56); source SHA-256 `4ef86b9b94fae71a85be1c21f346d3eebc84b1a653fc76e09059aba4d1d7cdc4`.

```text
@armProviderNamespace
@service(#{ title: "ContainerServiceClient" })
@versioned(Versions)
@armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v6)
namespace Microsoft.ContainerService;

/**
```

### Emitted Swagger observations

**`v6/managedidentitywithdelegation.json`: 1 findings.** Saved document `projects/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/swagger/preview/2026-07-02-preview/managedClusters.json`; exact path `["definitions", "ManagedClusterIdentity", "properties", "delegatedResources", "additionalProperties", "$ref"]`.

```json
{
  "$ref": "../../../../../../../../../common-types/resource-management/v6/managedidentitywithdelegation.json#/definitions/DelegatedResource"
}
```

## DocumentDB

- **Classification:** Swagger-linter-only.
- **Status / cause:** `filename-map`; covered only for the approved selection/configuration boundary, not full reference-check equivalence.
- **Project / emitted API:** `specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB` / `2026-04-01-preview`.
- **Observed results:** Swagger linter **1**; TypeSpec linter **0**, with authored suppressions honored.
- **Coverage and recommended action:** Approved registry-versus-filename policy difference. Latest selection is compliant; pinned Swagger map expects v5 for a v6 file. Recommend upstream policy review before calling this a bug or changing services. No additional TypeSpec check is justified by these counts.

### TypeSpec source

[`main.tsp:79-84`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/main.tsp#L79-L84); source SHA-256 `061e221683a13b4c383c5e7d29ab9eb676f11fe1042c65a7231f5161dfb65824`.

```text
@service(#{ title: "Cosmos DB" })
@versioned(Versions)
// FIXME: Common type version v1 is not supported for now. Set to v6.
@armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v6)
namespace Microsoft.DocumentDB;

```

### Emitted Swagger observations

**`v6/networksecurityperimeter.json`: 1 findings.** Saved document `projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json`; exact path `["definitions", "NetworkSecurityPerimeterConfiguration", "properties", "properties", "$ref"]`.

```json
{
  "$ref": "../../../../../../../../../common-types/resource-management/v6/networksecurityperimeter.json#/definitions/NetworkSecurityPerimeterConfigurationProperties"
}
```

## DatabaseWatcher

- **Classification:** Swagger-linter-only.
- **Status / cause:** `source-suppression`; covered only for the approved selection/configuration boundary, not full reference-check equivalence.
- **Project / emitted API:** `specification/databasewatcher/resource-manager/Microsoft.DatabaseWatcher/DatabaseWatcher` / `2025-01-02`.
- **Observed results:** Swagger linter **101**; TypeSpec linter **0**, with authored suppressions honored.
- **Coverage and recommended action:** Existing authored suppression, not a missing check. Historical missing configuration would take precedence by source predicate; no unsuppressed real-service execution is claimed. Recommend service-owner review of configuration/suppression independently of this recovery.

### TypeSpec source

[`watcher.tsp:13-17`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/databasewatcher/resource-manager/Microsoft.DatabaseWatcher/DatabaseWatcher/watcher.tsp#L13-L17); source SHA-256 `f8b487e68de4dc5aea05e4258cad783a21c4bfd54998d01f7836e6f2905f5079`.

```text
#suppress "@azure-tools/typespec-azure-resource-manager/arm-common-types-version" "Using invalid versions of ManagedIdentity"
@service(#{ title: "Microsoft.DatabaseWatcher" })
@versioned(Microsoft.DatabaseWatcher.Versions)
@armProviderNamespace
namespace Microsoft.DatabaseWatcher;
```

[`watcher.tsp:28-44`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/databasewatcher/resource-manager/Microsoft.DatabaseWatcher/DatabaseWatcher/watcher.tsp#L28-L44); source SHA-256 `f8b487e68de4dc5aea05e4258cad783a21c4bfd54998d01f7836e6f2905f5079`.

```text
@doc("Versions info.")
enum Versions {
  @doc("The 2023-09-01-preview version.")
  v2023_09_01_preview: "2023-09-01-preview",

  @doc("The 2024-07-17-preview version.")
  @armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v5)
  v2024_07_19_preview: "2024-07-19-preview",

  @doc("The 2024-10-01-preview version.")
  @armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v5)
  v2024_10_01_preview: "2024-10-01-preview",

  @doc("The 2025-01-02 version.")
  @armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v5)
  v2025_01_02: "2025-01-02",
}
```

### Emitted Swagger observations

**`v5/types.json`: 99 findings.** Saved document `projects/specification/databasewatcher/resource-manager/Microsoft.DatabaseWatcher/DatabaseWatcher/swagger/stable/2025-01-02/Watcher.json`; exact path `["paths", "/providers/Microsoft.DatabaseWatcher/operations", "get", "parameters", "0", "$ref"]`.

```json
{
  "$ref": "../../../../../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
}
```

**`v4/managedidentity.json`: 2 findings.** Saved document `projects/specification/databasewatcher/resource-manager/Microsoft.DatabaseWatcher/DatabaseWatcher/swagger/stable/2025-01-02/Watcher.json`; exact path `["definitions", "Watcher", "properties", "identity", "$ref"]`.

```json
{
  "$ref": "../../../../../../../../../common-types/resource-management/v4/managedidentity.json#/definitions/ManagedServiceIdentity"
}
```

## EventGrid

- **Classification:** Swagger-linter-only.
- **Status / cause:** `deprecated-location`; covered only for the approved selection/configuration boundary, not full reference-check equivalence.
- **Project / emitted API:** `specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid` / `2026-06-15-preview`.
- **Observed results:** Swagger linter **4**; TypeSpec linter **0**, with authored suppressions honored.
- **Coverage and recommended action:** Approved selection-versus-reference boundary. Latest selection is compliant; emitted deprecated LocationParameter falls back to its v5 registration. Recommend separately evaluating supported LocationResourceParameter authoring and compatibility; do not add reference traversal to this recovery.

### TypeSpec source

[`main.tsp:53-58`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/main.tsp#L53-L58); source SHA-256 `67b61e61165e60618ac2a4cb77b107e725b4927f21b5f78bf8cf810ccaef94c0`.

```text
@armProviderNamespace
@service(#{ title: "EventGridManagementClient" })
@versioned(Versions)
@armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v6)
namespace Microsoft.EventGrid;

```

### Emitted Swagger observations

**`v5/types.json`: 4 findings.** Saved document `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json`; exact path `["paths", "/subscriptions/{subscriptionId}/providers/Microsoft.EventGrid/locations/{location}/eventSubscriptions", "get", "parameters", "2", "$ref"]`.

```json
{
  "$ref": "../../../../../../../../../common-types/resource-management/v5/types.json#/parameters/LocationParameter"
}
```

## HybridCompute

- **Classification:** Swagger-linter-only.
- **Status / cause:** `deprecated-location`; covered only for the approved selection/configuration boundary, not full reference-check equivalence.
- **Project / emitted API:** `specification/hybridcompute/resource-manager/Microsoft.HybridCompute/HybridCompute` / `2026-07-15`.
- **Observed results:** Swagger linter **2**; TypeSpec linter **0**, with authored suppressions honored.
- **Coverage and recommended action:** Approved selection-versus-reference boundary. Latest selection is compliant; emitted deprecated LocationParameter falls back to its v5 registration. Recommend separately evaluating supported LocationResourceParameter authoring and compatibility; do not add reference traversal to this recovery.

### TypeSpec source

[`main.tsp:51-84`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/hybridcompute/resource-manager/Microsoft.HybridCompute/HybridCompute/main.tsp#L51-L84); source SHA-256 `bf74fa1133e62635378b897982020af49590521fc5f6292a84f2738f229fc26e`.

```text
   * The 2025-09-16-preview API version.
   */
  @useDependency(Azure.ResourceManager.CommonTypes.Versions.v3)
  @armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v3)
  v2025_09_16_preview: "2025-09-16-preview",

  /**
   * The 2026-02-12-preview API version.
   */
  @useDependency(Azure.ResourceManager.CommonTypes.Versions.v3)
  @armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v3)
  v2026_02_12_preview: "2026-02-12-preview",

  /**
   * The 2026-06-04-preview API version.
   */
  @useDependency(Azure.ResourceManager.CommonTypes.Versions.v3)
  @armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v3)
  v2026_06_04_preview: "2026-06-04-preview",

  /**
   * The 2026-06-16-preview API version.
   */
  @useDependency(Azure.ResourceManager.CommonTypes.Versions.v6)
  @armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v6)
  v2026_06_16_preview: "2026-06-16-preview",

  /**
   * The 2026-07-15 API version.
   */
  @useDependency(Azure.ResourceManager.CommonTypes.Versions.v6)
  @armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v6)
  v2026_07_15: "2026-07-15",
}
```

### Emitted Swagger observations

**`v5/types.json`: 2 findings.** Saved document `projects/specification/hybridcompute/resource-manager/Microsoft.HybridCompute/HybridCompute/swagger/stable/2026-07-15/openapi.json`; exact path `["paths", "/providers/Microsoft.HybridCompute/locations/{location}/publishers", "get", "parameters", "1", "$ref"]`.

```json
{
  "$ref": "../../../../../../../../../common-types/resource-management/v5/types.json#/parameters/LocationParameter"
}
```

## PlatformValidation

- **Classification:** Swagger-linter-only.
- **Status / cause:** `filename-map`; covered only for the approved selection/configuration boundary, not full reference-check equivalence.
- **Project / emitted API:** `specification/platformvalidation/resource-manager/Microsoft.PlatformValidation/PlatformValidation` / `2026-08-01-preview`.
- **Observed results:** Swagger linter **1**; TypeSpec linter **0**, with authored suppressions honored.
- **Coverage and recommended action:** Approved registry-versus-filename policy difference. Latest selection is compliant; pinned Swagger map expects v5 for a v6 file. Recommend upstream policy review before calling this a bug or changing services. No additional TypeSpec check is justified by these counts.

### TypeSpec source

[`main.tsp:23-30`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/platformvalidation/resource-manager/Microsoft.PlatformValidation/PlatformValidation/main.tsp#L23-L30); source SHA-256 `2d4a9175f8268562425f412d5578612d8e0ddd0a6b13e35c0a510ddf3ce7ffb5`.

```text
/** The available API versions. */
enum Versions {
  /** 2026-08-01-preview version */
  @armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v6)
  @Azure.Core.previewVersion
  v2026_08_01_preview: "2026-08-01-preview",
}
```

### Emitted Swagger observations

**`v6/mobo.json`: 1 findings.** Saved document `projects/specification/platformvalidation/resource-manager/Microsoft.PlatformValidation/PlatformValidation/swagger/preview/2026-08-01-preview/platformvalidation.json`; exact path `["definitions", "CloudValidationProperties", "properties", "managedOnBehalfOfConfiguration", "$ref"]`.

```json
{
  "$ref": "../../../../../../../../../common-types/resource-management/v6/mobo.json#/definitions/ManagedOnBehalfOfConfiguration"
}
```

## RedisEnterprise

- **Classification:** Swagger-linter-only.
- **Status / cause:** `explicit-legacy-identity`; covered only for the approved selection/configuration boundary, not full reference-check equivalence.
- **Project / emitted API:** `specification/redisenterprise/resource-manager/Microsoft.Cache/RedisEnterprise` / `2026-09-01`.
- **Observed results:** Swagger linter **2**; TypeSpec linter **0**, with authored suppressions honored.
- **Coverage and recommended action:** Approved selection-versus-reference boundary. Existing no-legacy-usage policy owns explicit legacy authoring and is suppressed here. Recommend separate compatibility review, not a duplicate payload/reference checker.

### TypeSpec source

[`main.tsp:33-38`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/redisenterprise/resource-manager/Microsoft.Cache/RedisEnterprise/main.tsp#L33-L38); source SHA-256 `318601ecb7e9b34be613c41024f1f03272c9ce56238d9bf565b7995dcd75f14b`.

```text
@armProviderNamespace
@service(#{ title: "RedisEnterpriseManagementClient" })
@versioned(Versions)
@armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v6)
namespace Microsoft.Cache;

```

[`Cluster.tsp:41-46`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/redisenterprise/resource-manager/Microsoft.Cache/RedisEnterprise/Cluster.tsp#L41-L46); source SHA-256 `c8b1a90ef224840e671d67bf138340a34bfcbf979c70adaba7cd1aa1d4a26b9c`.

```text

  /**
   * The identity of the resource.
   */
  #suppress "@azure-tools/typespec-azure-core/no-legacy-usage" "Existing usage of legacy type"
  ...Azure.ResourceManager.Legacy.ManagedServiceIdentityV4Property;
```

[`models.tsp:1148-1152`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/redisenterprise/resource-manager/Microsoft.Cache/RedisEnterprise/models.tsp#L1148-L1152); source SHA-256 `b1c0fa71c0a73ec21e73f5d17447099a985c940d0eb2e378bfd27380d540cf50`.

```text
  /**
   * The identity of the resource.
   */
  #suppress "@azure-tools/typespec-azure-core/no-legacy-usage" "Existing usage of legacy type"
  ...Azure.ResourceManager.Legacy.ManagedServiceIdentityV4Property;
```

### Emitted Swagger observations

**`v4/managedidentity.json`: 2 findings.** Saved document `projects/specification/redisenterprise/resource-manager/Microsoft.Cache/RedisEnterprise/swagger/stable/2026-09-01/redisenterprise.json`; exact path `["definitions", "Cluster", "properties", "identity", "$ref"]`.

```json
{
  "$ref": "../../../../../../../../../common-types/resource-management/v4/managedidentity.json#/definitions/ManagedServiceIdentity"
}
```

## Search

- **Classification:** Swagger-linter-only.
- **Status / cause:** `filename-map`; covered only for the approved selection/configuration boundary, not full reference-check equivalence.
- **Project / emitted API:** `specification/search/resource-manager/Microsoft.Search/Search` / `2026-09-01-preview`.
- **Observed results:** Swagger linter **2**; TypeSpec linter **0**, with authored suppressions honored.
- **Coverage and recommended action:** Approved registry-versus-filename policy difference. Latest selection is compliant; pinned Swagger map expects v5 for a v6 file. Recommend upstream policy review before calling this a bug or changing services. No additional TypeSpec check is justified by these counts.

### TypeSpec source

[`main.tsp:32-37`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/search/resource-manager/Microsoft.Search/Search/main.tsp#L32-L37); source SHA-256 `9b34d5651d446c9f5bfa0b00e26b76b58823acb5fe43a3179f96823b31b5f91b`.

```text
@armProviderNamespace
@service(#{ title: "SearchManagementClient" })
@versioned(Versions)
@armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v6)
namespace Microsoft.Search;

```

### Emitted Swagger observations

**`v6/networksecurityperimeter.json`: 2 findings.** Saved document `projects/specification/search/resource-manager/Microsoft.Search/Search/swagger/preview/2026-09-01-preview/search.json`; exact path `["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}/networkSecurityPerimeterConfigurations/{nspConfigName}", "get", "responses", "200", "schema", "$ref"]`.

```json
{
  "$ref": "../../../../../../../../../common-types/resource-management/v6/networksecurityperimeter.json#/definitions/NetworkSecurityPerimeterConfiguration"
}
```

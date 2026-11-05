# Exact operation/model correspondence

This is the target-level inventory supporting the [migration decision](migration.md) and [difference analysis](gap-analysis.md). It retains raw findings, exact comparisons and source/schema examples.

## Differing projects

This appendix accounts for **433 Swagger observations, 277 member checks and all 180 TypeSpec findings**. The summary below contains only projects with unpaired checks or additional/different TypeSpec findings, including equal-total projects with different checks. Counts on shared targets across members are non-additive.

| Project                                                                                                                                   | Swagger raw | Member checks | TypeSpec raw | Routes Swagger / TypeSpec | Credited same comparison |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------- | ------------ | ------------------------- | ------------------------ |
| [`specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement`](instances/p-6e7cc89a7ebd.md)                       | 22          | 22            | 26           | 22 / 26                   | 17                       |
| [`specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/AnalyticsItems`](instances/p-e7643f35b3aa.md) | 1           | 1             | 0            | 1 / 0                     | 0                        |
| [`specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs`](instances/p-560dd8313baf.md)  | 7           | 7             | 0            | 4 / 0                     | 0                        |
| [`specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/Favorites`](instances/p-44fd87244aab.md)      | 1           | 1             | 0            | 1 / 0                     | 0                        |
| [`specification/automation/resource-manager/Microsoft.Automation/Automation`](instances/p-49581f50dce3.md)                                | 26          | 26            | 20           | 22 / 20                   | 19                       |
| [`specification/batch/resource-manager/Microsoft.Batch/Batch`](instances/p-08262b7ca56f.md)                                               | 1           | 1             | 2            | 1 / 2                     | 1                        |
| [`specification/cdn/resource-manager/Microsoft.Cdn/Cdn`](instances/p-495bf9259924.md)                                                     | 1           | 1             | 2            | 1 / 2                     | 1                        |
| [`specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices`](instances/p-d883c2d5a2bc.md)           | 1           | 1             | 0            | 1 / 0                     | 0                        |
| [`specification/compute/resource-manager/Microsoft.Compute/Compute/Compute`](instances/p-a34772e539fc.md)                                 | 2           | 2             | 0            | 2 / 0                     | 0                        |
| [`specification/confluent/resource-manager/Microsoft.Confluent/Confluent`](instances/p-878952198171.md)                                   | 1           | 1             | 0            | 1 / 0                     | 0                        |
| [`specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry`](instances/p-9dc15a9f8ade.md)                    | 1           | 1             | 2            | 1 / 2                     | 1                        |
| [`specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB`](instances/p-d2000d5bc232.md)                                 | 33          | 33            | 31           | 33 / 31                   | 31                       |
| [`specification/datadog/resource-manager/Microsoft.Datadog/Datadog`](instances/p-8455ab1b357f.md)                                         | 1           | 1             | 0            | 1 / 0                     | 0                        |
| [`specification/dns/resource-manager/Microsoft.Network/Dns`](instances/p-c10ea5a9fd05.md)                                                 | 0           | 0             | 1            | 0 / 1                     | 0                        |
| [`specification/durabletask/resource-manager/Microsoft.DurableTask/DurableTask`](instances/p-7c23914bec5d.md)                             | 1           | 1             | 0            | 1 / 0                     | 0                        |
| [`specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid`](instances/p-da92c978c97e.md)                                   | 6           | 6             | 1            | 6 / 1                     | 0                        |
| [`specification/fileshares/resource-manager/Microsoft.FileShares/FileShares`](instances/p-f543895a6651.md)                                | 1           | 1             | 0            | 1 / 0                     | 0                        |
| [`specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments`](instances/p-313565921954.md)               | 4           | 4             | 0            | 4 / 0                     | 0                        |
| [`specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight`](instances/p-d00f78f58133.md)                                   | 9           | 9             | 2            | 5 / 2                     | 1                        |
| [`specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb`](instances/p-1a17ac3fb584.md)                                   | 2           | 2             | 1            | 2 / 1                     | 1                        |
| [`specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault`](instances/p-354fbe912752.md)                                      | 5           | 5             | 4            | 5 / 4                     | 4                        |
| [`specification/management/resource-manager/Microsoft.Management/ManagementGroups`](instances/p-71838e2726a0.md)                          | 2           | 2             | 3            | 2 / 3                     | 2                        |
| [`specification/maps/resource-manager/Microsoft.Maps/Maps`](instances/p-79b197f2d869.md)                                                  | 1           | 1             | 0            | 1 / 0                     | 0                        |
| [`specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace`](instances/p-f43db0dc1fd6.md)                             | 2           | 2             | 0            | 1 / 0                     | 0                        |
| [`specification/mysql/resource-manager/Microsoft.DBforMySQL/FlexibleServers`](instances/p-dbe559622b2b.md)                                | 1           | 1             | 1            | 1 / 1                     | 0                        |
| [`specification/network/resource-manager/Microsoft.Network/Network/Network`](instances/p-199707c82451.md)                                 | 170         | 14            | 0            | 12 / 0                    | 0                        |
| [`specification/operationalinsights/resource-manager/Microsoft.OperationalInsights/OperationalInsights`](instances/p-75b0ebe30c60.md)     | 1           | 1             | 0            | 1 / 0                     | 0                        |
| [`specification/portal/resource-manager/Microsoft.Portal/Portal`](instances/p-1e4b1f0cddaf.md)                                            | 2           | 2             | 0            | 2 / 0                     | 0                        |
| [`specification/postgresql/DBforPostgreSQL.Management`](instances/p-43a32290b79b.md)                                                      | 9           | 9             | 4            | 9 / 4                     | 0                        |
| [`specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc`](instances/p-c9e6c4ded28f.md)                     | 1           | 1             | 0            | 1 / 0                     | 0                        |
| [`specification/quota/resource-manager/Microsoft.Quota/Quota`](instances/p-50ad2767c3ed.md)                                               | 0           | 0             | 1            | 0 / 1                     | 0                        |
| [`specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices`](instances/p-551502b046ca.md)              | 2           | 2             | 1            | 1 / 1                     | 0                        |
| [`specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup`](instances/p-05203fab0aa5.md)  | 3           | 3             | 1            | 2 / 1                     | 0                        |
| [`specification/redis/resource-manager/Microsoft.Cache/Redis`](instances/p-665a329b65e9.md)                                               | 3           | 3             | 2            | 3 / 2                     | 2                        |
| [`specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota`](instances/p-e87fcbcb098a.md)                        | 1           | 1             | 0            | 1 / 0                     | 0                        |
| [`specification/resources/resource-manager/Microsoft.Resources/resources`](instances/p-82db065ff1a4.md)                                   | 2           | 2             | 0            | 2 / 0                     | 0                        |
| [`specification/security/resource-manager/Microsoft.Security/Security/ApiCollectionsAPI`](instances/p-f62fb200d40c.md)                    | 0           | 0             | 1            | 0 / 1                     | 0                        |
| [`specification/security/resource-manager/Microsoft.Security/Security/PrivateLinksAPI`](instances/p-0c954c82d021.md)                      | 1           | 1             | 0            | 1 / 0                     | 0                        |
| [`specification/security/resource-manager/Microsoft.Security/Security/SecurityOperatorsAPI`](instances/p-37638f840020.md)                 | 0           | 0             | 1            | 0 / 1                     | 0                        |
| [`specification/security/resource-manager/Microsoft.Security/Security/SecuritySolutionsAPI`](instances/p-13a3aae04c51.md)                 | 0           | 0             | 1            | 0 / 1                     | 0                        |
| [`specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights`](instances/p-3d47c51b653f.md)              | 3           | 3             | 1            | 3 / 1                     | 1                        |
| [`specification/sql/resource-manager/Microsoft.Sql/SQL`](instances/p-5941c238374d.md)                                                     | 20          | 20            | 9            | 16 / 9                    | 6                        |
| [`specification/support/resource-manager/Microsoft.Support/Support`](instances/p-fe57f17c4f29.md)                                         | 0           | 0             | 2            | 0 / 2                     | 0                        |
| [`specification/web/resource-manager/Microsoft.Web/AppService`](instances/p-618b7f706185.md)                                              | 31          | 31            | 8            | 30 / 8                    | 5                        |

## Request comparison differences

Of 168 request checks, 144 have corresponding TypeSpec warnings. The difference groups below preserve every remaining comparison; the previous traversal gap is assessed separately against the final-source results. See [registered traversal](gap-analysis.md#registered-put-traversal), [existing policy exceptions](gap-analysis.md#existing-policy-exceptions) and [legacy contracts](gap-analysis.md#legacy-contracts).

## Response comparison differences

**16 success-schema checks:** 15 Swagger identity-bug false positives and Quota's genuine difference, which the existing Azure Core rule detects before suppression. **57 resource-marker checks:** independent policy is absent. **36 cross-method checks:** 15 no-content comparisons, four matching-item collection comparisons, 16 empty-200 cases detected by the existing body rule before suppression, and one genuine SyncJob shape difference. The shared ARM rule emits no corresponding response-family warning. [Evidence and decisions](gap-analysis.md#difference-groups).

## Identity and attribution

Each raw observation is resolved against the immutable Swagger dataset by exact route and explicit operation ID, or by exact referenced schema document and JSON pointer for staging schema targets. All 433 have one candidate. Grouping retains `(member, project, resolved document, exact route, request/response schema context)`; it never merges different member checks or distinct schema contexts. PUT/GET/PATCH is one path-level method bundle, not three invented violations.

The result is 168 + 16 + 57 + 36 = **277** member checks. Network's 170 raw observations resolve to 14 checks (three request, ten extension, one cross-method), accounting for all 156 repeated observations. Location-only JSON-path keys are not operation identities: schema-target locations can identify different invoking operations. The separate location summaries remain in [summary.json](summary.json).

These checks reference 256 distinct project/routes and 307 participating method/route identities. All 328 source bindings across the member checks, and all 328 selected-version bindings, are unique exact method/route matches. No fuzzy matching or parameter normalization was needed. Original fallback documents and validator inputs remain unchanged; the separately resolved document is explicit in every group.

All 144 credited cases use the same operation, a different effective request model and the canonical resource as the original selected response body. Their source and selected-version request/response metadata agree. **This corroborates these observed request-resource mismatches; it does not prove structural schema equality and source-model identity are universally equivalent, or that correcting the source will necessarily eliminate every emitted-schema difference.**

Routes overlap at 154 (102 Swagger-only, 26 TypeSpec-only), but only 144 findings receive comparison credit. Route co-occurrence is explicitly not coverage. The complete raw IDs and full schema contexts are in [Swagger bindings](swagger-bindings.json), [native-to-Swagger bindings](native-swagger-bindings.json) and [assessment](instance-mapping.json).

Per-project route-grouped excesses are 91 Swagger-higher and 15 TypeSpec-higher, absolute difference 106. This is distinct from raw-finding excesses of 268 and 15. Opposing project differences do not cancel in either unit.

## TypeSpec finding accounting

The shared linter reports **154 requestMismatch + 26 missingRequest + 0 response-family findings**. 144 findings correspond to selected Swagger comparisons; all 36 additional or different findings appear individually below.

Missing-request warnings enforce an additional body-existence policy. A source-only operation absent in the selected version is a population difference, not a new selected-version defect. A PUT without 200/201 is outside the original request rule's registration selector. Same-operation warnings comparing another canonical resource or selected body do not receive comparison credit. Any unresolved schema-identity classification remains unresolved until its linked source/schema evidence explains it; totals alone are never correspondence.

| Additional comparison / cause        | Swagger corresponding findings | TypeSpec findings | Gap analysis and decision                                                                                                                                               |
| ------------------------------------ | ------------------------------ | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Missing-request policy               | 0                              | 25                | Additional body-existence check, skipped by the Swagger selector. Review the wire contract/exception; do not invent a body to equalize counts.                          |
| Same operation, different comparison | 0                              | 8                 | Canonical parent or selected success body differs from the original comparator. Review resource association/contract; route co-occurrence receives no migration credit. |
| Source-only version population       | 0                              | 2                 | Retain the source warning; use supported version-aligned comparison for selected-version parity, not a rule suppression.                                                |
| Outside Swagger 200/201 selector     | 0                              | 1                 | The registered request policy is broader. Keep this finding separate from migrated 200/201 comparisons; review the independent status-set contract.                     |

The zero column means no selected Swagger finding for that same comparison, not no Swagger warning on the route.

| TypeSpec operation / source                                                                                                                                                                                                                                                                                                       | Family            | Disposition                                                 | Credited Swagger check IDs                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------------------------------------------------- | ----------------------------------------- |
| [Microsoft.ApiManagement.AccessInformationContracts.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/AccessInformationContract.tsp#L91)                                                     | `requestMismatch` | `mapped-request-mismatch`                                   | [`6d6f81e97257180a`](#s-6d6f81e97257180a) |
| [Microsoft.ApiManagement.ApiContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/ApiContract.tsp#L93)                                                                         | `requestMismatch` | `mapped-request-mismatch`                                   | [`d6c6d92c9a0f4dc9`](#s-d6c6d92c9a0f4dc9) |
| [Microsoft.ApiManagement.CertificateContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/CertificateContract.tsp#L97)                                                         | `requestMismatch` | `mapped-request-mismatch`                                   | [`07a4fba5ab458883`](#s-07a4fba5ab458883) |
| [Microsoft.ApiManagement.EmailTemplateContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/EmailTemplateContract.tsp#L89)                                                     | `requestMismatch` | `mapped-request-mismatch`                                   | [`5bc868e33cb12f58`](#s-5bc868e33cb12f58) |
| [Microsoft.ApiManagement.GroupContracts.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/GroupContract.tsp#L334)                                                                            | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.ApiManagement.GroupContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/GroupContract.tsp#L188)                                                                    | `requestMismatch` | `mapped-request-mismatch`                                   | [`a24e9f05205ca77e`](#s-a24e9f05205ca77e) |
| [Microsoft.ApiManagement.IdentityProviderContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/IdentityProviderContract.tsp#L62)                                               | `requestMismatch` | `mapped-request-mismatch`                                   | [`16bb019f51c54666`](#s-16bb019f51c54666) |
| [Microsoft.ApiManagement.NamedValueContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NamedValueContract.tsp#L91)                                                           | `requestMismatch` | `mapped-request-mismatch`                                   | [`4074356758b8b55a`](#s-4074356758b8b55a) |
| [Microsoft.ApiManagement.NotificationContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NotificationContract.tsp#L233)                                                      | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/PrivateEndpointConnection.tsp#L29)                                             | `requestMismatch` | `same-operation-different-comparison`                       | (none)                                    |
| [Microsoft.ApiManagement.SubscriptionContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/SubscriptionContract.tsp#L91)                                                       | `requestMismatch` | `mapped-request-mismatch`                                   | [`9bd66fb3b423b668`](#s-9bd66fb3b423b668) |
| [Microsoft.ApiManagement.Tag.assignToApi](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagContract.tsp#L223)                                                                                    | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.ApiManagement.TagContractOperation.assignToProduct](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagContract.tsp#L350)                                                               | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.ApiManagement.TagContractOperationGroup.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagContract.tsp#L453)                                                           | `requestMismatch` | `mapped-request-mismatch`                                   | [`c24f5593e4c0444c`](#s-c24f5593e4c0444c) |
| [Microsoft.ApiManagement.TagContracts.assignToOperation](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagContract.tsp#L110)                                                                     | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.ApiManagement.TagDescriptionContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagDescriptionContract.tsp#L102)                                                  | `requestMismatch` | `mapped-request-mismatch`                                   | [`a0043bfa2f35690b`](#s-a0043bfa2f35690b) |
| [Microsoft.ApiManagement.UserContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/UserContract.tsp#L61)                                                                       | `requestMismatch` | `mapped-request-mismatch`                                   | [`abb6d8ec653be75b`](#s-abb6d8ec653be75b) |
| [Microsoft.ApiManagement.WorkspaceApi.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/ApiContract.tsp#L395)                                                                        | `requestMismatch` | `mapped-request-mismatch`                                   | [`f480a1873a8a46d6`](#s-f480a1873a8a46d6) |
| [Microsoft.ApiManagement.WorkspaceCertificate.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/CertificateContract.tsp#L273)                                                        | `requestMismatch` | `mapped-request-mismatch`                                   | [`4fe374080228c379`](#s-4fe374080228c379) |
| [Microsoft.ApiManagement.WorkspaceGroup.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/GroupContract.tsp#L438)                                                                    | `requestMismatch` | `mapped-request-mismatch`                                   | [`aab9a5c4285f75fb`](#s-aab9a5c4285f75fb) |
| [Microsoft.ApiManagement.WorkspaceNamedValue.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NamedValueContract.tsp#L306)                                                          | `requestMismatch` | `mapped-request-mismatch`                                   | [`e76bb208f825a268`](#s-e76bb208f825a268) |
| [Microsoft.ApiManagement.WorkspaceNotification.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NotificationContract.tsp#L424)                                                      | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientEmailCreateOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NotificationContract.tsp#L538)                   | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientUserCreateOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NotificationContract.tsp#L485)                    | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.ApiManagement.WorkspaceSubscription.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/SubscriptionContract.tsp#L403)                                                      | `requestMismatch` | `mapped-request-mismatch`                                   | [`ddf45b716631a01b`](#s-ddf45b716631a01b) |
| [Microsoft.ApiManagement.WorkspaceTag.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagContract.tsp#L628)                                                                        | `requestMismatch` | `mapped-request-mismatch`                                   | [`ea5b75fffe317a54`](#s-ea5b75fffe317a54) |
| [Microsoft.Attestation.AttestationProviders.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/attestation/resource-manager/Microsoft.Attestation/Attestation/AttestationProvider.tsp#L61)                                                                         | `requestMismatch` | `mapped-request-mismatch`                                   | [`9c84623c7997c7e8`](#s-9c84623c7997c7e8) |
| [Microsoft.AttributeNamespaces.AccessReviewDefaultSettingsOperationGroup.put](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/AccessReviewDefaultSettings.tsp#L62)                    | `requestMismatch` | `mapped-request-mismatch`                                   | [`2eb48d6c239daee9`](#s-2eb48d6c239daee9) |
| [Microsoft.AttributeNamespaces.AccessReviewHistoryDefinitions.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/AccessReviewHistoryDefinition.tsp#L65)                          | `requestMismatch` | `mapped-request-mismatch`                                   | [`0039d3e2e8604534`](#s-0039d3e2e8604534) |
| [Microsoft.AttributeNamespaces.AccessReviewInstances.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/AccessReviewInstance.tsp#L72)                                            | `requestMismatch` | `mapped-request-mismatch`                                   | [`85f4458dae5f772c`](#s-85f4458dae5f772c) |
| [Microsoft.AttributeNamespaces.AccessReviewScheduleDefinitions.createOrUpdateById](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/AccessReviewScheduleDefinition.tsp#L84)            | `requestMismatch` | `mapped-request-mismatch`                                   | [`b5ef44d92176b2c4`](#s-b5ef44d92176b2c4) |
| [Microsoft.AttributeNamespaces.ScopeAccessReviewDefaultSettings.put](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/AccessReviewDefaultSettings.tsp#L107)                            | `requestMismatch` | `mapped-request-mismatch`                                   | [`22c2dd3e8b4a25fd`](#s-22c2dd3e8b4a25fd) |
| [Microsoft.AttributeNamespaces.ScopeAccessReviewHistoryDefinitions.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/AccessReviewHistoryDefinition.tsp#L173)                    | `requestMismatch` | `mapped-request-mismatch`                                   | [`6b3a035269cdee71`](#s-6b3a035269cdee71) |
| [Microsoft.AttributeNamespaces.ScopeAccessReviewInstances.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/AccessReviewInstance.tsp#L224)                                      | `requestMismatch` | `mapped-request-mismatch`                                   | [`441d5618033269e7`](#s-441d5618033269e7) |
| [Microsoft.AttributeNamespaces.ScopeAccessReviewScheduleDefinitions.createOrUpdateById](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/AccessReviewScheduleDefinition.tsp#L169)      | `requestMismatch` | `mapped-request-mismatch`                                   | [`4972a9ee4dfdd4ae`](#s-4972a9ee4dfdd4ae) |
| [Microsoft.RoleAssignment.RoleAssignments.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/RoleAssignment/RoleAssignment.tsp#L161)                                                          | `requestMismatch` | `mapped-request-mismatch`                                   | [`9c317d438b4a5f71`](#s-9c317d438b4a5f71) |
| [Microsoft.RoleAssignment.RoleAssignmentsByIdOperations.createById](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/RoleAssignment/RoleAssignment.tsp#L309)                                        | `requestMismatch` | `mapped-request-mismatch`                                   | [`b13069e2bfb91132`](#s-b13069e2bfb91132) |
| [Microsoft.Automation.AutomationAccounts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/AutomationAccount.tsp#L76)                                                                         | `requestMismatch` | `mapped-request-mismatch`                                   | [`db520c522579a0ff`](#s-db520c522579a0ff) |
| [Microsoft.Automation.Certificates.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Certificate.tsp#L43)                                                                                     | `requestMismatch` | `mapped-request-mismatch`                                   | [`2ee09847cc1ea272`](#s-2ee09847cc1ea272) |
| [Microsoft.Automation.ConnectionTypes.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/ConnectionType.tsp#L44)                                                                               | `requestMismatch` | `mapped-request-mismatch`                                   | [`8c696c8d8a3847e6`](#s-8c696c8d8a3847e6) |
| [Microsoft.Automation.Connections.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Connection.tsp#L42)                                                                                       | `requestMismatch` | `mapped-request-mismatch`                                   | [`6c42af6ba5bf267b`](#s-6c42af6ba5bf267b) |
| [Microsoft.Automation.Credentials.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Credential.tsp#L42)                                                                                       | `requestMismatch` | `mapped-request-mismatch`                                   | [`701d9778f09f2bce`](#s-701d9778f09f2bce) |
| [Microsoft.Automation.DscConfigurations.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/DscConfiguration.tsp#L49)                                                                           | `requestMismatch` | `mapped-request-mismatch`                                   | [`30747121ec0c0631`](#s-30747121ec0c0631) |
| [Microsoft.Automation.DscNodeConfigurations.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/DscNodeConfiguration.tsp#L45)                                                                   | `requestMismatch` | `same-operation-different-comparison`                       | (none)                                    |
| [Microsoft.Automation.HybridRunbookWorkerGroups.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/HybridRunbookWorkerGroup.tsp#L44)                                                                   | `requestMismatch` | `mapped-request-mismatch`                                   | [`c700a5800790bded`](#s-c700a5800790bded) |
| [Microsoft.Automation.HybridRunbookWorkers.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/HybridRunbookWorker.tsp#L43)                                                                             | `requestMismatch` | `mapped-request-mismatch`                                   | [`292f816b17f7d7b1`](#s-292f816b17f7d7b1) |
| [Microsoft.Automation.JobSchedules.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/JobSchedule.tsp#L44)                                                                                             | `requestMismatch` | `mapped-request-mismatch`                                   | [`7ae44ff3ae6d7f4f`](#s-7ae44ff3ae6d7f4f) |
| [Microsoft.Automation.Jobs.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Job.tsp#L54)                                                                                                             | `requestMismatch` | `mapped-request-mismatch`                                   | [`ed051c77ccddb09c`](#s-ed051c77ccddb09c) |
| [Microsoft.Automation.Modules.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Module.tsp#L71)                                                                                               | `requestMismatch` | `mapped-request-mismatch`                                   | [`c7ced7c3b979f1c9`](#s-c7ced7c3b979f1c9) |
| [Microsoft.Automation.Packages.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Package.tsp#L42)                                                                                             | `requestMismatch` | `mapped-request-mismatch`                                   | [`1a6a16a376d63d73`](#s-1a6a16a376d63d73) |
| [Microsoft.Automation.Python2Package.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Module.tsp#L223)                                                                                       | `requestMismatch` | `mapped-request-mismatch`                                   | [`345af9cecebe896b`](#s-345af9cecebe896b) |
| [Microsoft.Automation.Python3Package.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Module.tsp#L291)                                                                                       | `requestMismatch` | `mapped-request-mismatch`                                   | [`7b2dd73598a4c620`](#s-7b2dd73598a4c620) |
| [Microsoft.Automation.Runbooks.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Runbook.tsp#L65)                                                                                             | `requestMismatch` | `mapped-request-mismatch`                                   | [`62212bf10d0eb1ee`](#s-62212bf10d0eb1ee) |
| [Microsoft.Automation.Schedules.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Schedule.tsp#L43)                                                                                           | `requestMismatch` | `mapped-request-mismatch`                                   | [`b6e8e0ed0ffa0a7e`](#s-b6e8e0ed0ffa0a7e) |
| [Microsoft.Automation.SourceControls.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/SourceControl.tsp#L55)                                                                                 | `requestMismatch` | `mapped-request-mismatch`                                   | [`a5926ec404279bda`](#s-a5926ec404279bda) |
| [Microsoft.Automation.Variables.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Variable.tsp#L42)                                                                                           | `requestMismatch` | `mapped-request-mismatch`                                   | [`824155ae51a4294c`](#s-824155ae51a4294c) |
| [Microsoft.Automation.Webhooks.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Webhook.tsp#L42)                                                                                             | `requestMismatch` | `mapped-request-mismatch`                                   | [`28f094b6475664fd`](#s-28f094b6475664fd) |
| [Microsoft.Batch.BatchAccounts.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/batch/resource-manager/Microsoft.Batch/Batch/BatchAccount.tsp#L44)                                                                                                               | `requestMismatch` | `mapped-request-mismatch`                                   | [`26cefb8c076b5dda`](#s-26cefb8c076b5dda) |
| [Microsoft.Batch.Certificates.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/batch/resource-manager/Microsoft.Batch/Batch/Certificate.tsp#L69)                                                                                                                 | `requestMismatch` | `source-only-operation-not-in-selected-version`             | (none)                                    |
| [Microsoft.Billing.PartnerTransfers.initiate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/billing/resource-manager/Microsoft.Billing/Billing/PartnerTransferDetails.tsp#L52)                                                                                        | `requestMismatch` | `mapped-request-mismatch`                                   | [`3c56ad68fe60248e`](#s-3c56ad68fe60248e) |
| [Microsoft.Billing.Transfers.initiate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/billing/resource-manager/Microsoft.Billing/Billing/TransferDetails.tsp#L50)                                                                                                      | `requestMismatch` | `mapped-request-mismatch`                                   | [`fc900d8332d940cc`](#s-fc900d8332d940cc) |
| [Microsoft.BillingBenefits.ReservationOrderAliasResponses.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits/ReservationOrderAliasResponse.tsp#L54)                                     | `requestMismatch` | `mapped-request-mismatch`                                   | [`27f2841e3a69a04c`](#s-27f2841e3a69a04c) |
| [Microsoft.Cdn.CustomDomains.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/CustomDomain.tsp#L41)                                                                                                                       | `requestMismatch` | `mapped-request-mismatch`                                   | [`b8c23f8be92990e5`](#s-b8c23f8be92990e5) |
| [Microsoft.Cdn.RuleSets.createV1](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/RuleSet.tsp#L43)                                                                                                                               | `missingRequest`  | `source-only-operation-not-in-selected-version`             | (none)                                    |
| [Microsoft.ContainerRegistry.ArchiveVersions.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/ArchiveVersion.tsp#L84)                                                                    | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.ContainerRegistry.Webhooks.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/Webhook.tsp#L36)                                                                                  | `requestMismatch` | `mapped-request-mismatch`                                   | [`32e3c2def02f5a05`](#s-32e3c2def02f5a05) |
| [Microsoft.DocumentDB.CassandraKeyspaceGetResultsOperationGroup.createUpdateCassandraKeyspace](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/CassandraKeyspaceGetResults.tsp#L54)                          | `requestMismatch` | `mapped-request-mismatch`                                   | [`0f2d9f17cb87c7cf`](#s-0f2d9f17cb87c7cf) |
| [Microsoft.DocumentDB.CassandraResources.updateCassandraKeyspaceThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L649)                                           | `requestMismatch` | `mapped-request-mismatch`                                   | [`1143ed1af0d6a699`](#s-1143ed1af0d6a699) |
| [Microsoft.DocumentDB.CassandraResourcesThroughputSettingsGetResultsOperationGroup.updateCassandraTableThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L739)    | `requestMismatch` | `mapped-request-mismatch`                                   | [`ac6f0249cbe35516`](#s-ac6f0249cbe35516) |
| [Microsoft.DocumentDB.CassandraTableGetResultsOperationGroup.createUpdateCassandraTable](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/CassandraTableGetResults.tsp#L54)                                   | `requestMismatch` | `mapped-request-mismatch`                                   | [`50be0c4a42ffcc8c`](#s-50be0c4a42ffcc8c) |
| [Microsoft.DocumentDB.CassandraViewGetResultsOperationGroup.createUpdateCassandraView](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/CassandraViewGetResults.tsp#L58)                                      | `requestMismatch` | `mapped-request-mismatch`                                   | [`0999b8017d3a3ca3`](#s-0999b8017d3a3ca3) |
| [Microsoft.DocumentDB.ClientEncryptionKeyGetResultsOperationGroup.createUpdateClientEncryptionKey](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ClientEncryptionKeyGetResults.tsp#L40)                    | `requestMismatch` | `mapped-request-mismatch`                                   | [`1791c6f4e0e03cdd`](#s-1791c6f4e0e03cdd) |
| [Microsoft.DocumentDB.DataTransferJobs.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/DataTransferJobGetResults.tsp#L44)                                                                            | `requestMismatch` | `mapped-request-mismatch`                                   | [`44196ad97da9b599`](#s-44196ad97da9b599) |
| [Microsoft.DocumentDB.GraphResources.createUpdateGraph](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/GraphResourceGetResults.tsp#L58)                                                                     | `requestMismatch` | `mapped-request-mismatch`                                   | [`ccc457dafd55a252`](#s-ccc457dafd55a252) |
| [Microsoft.DocumentDB.GremlinDatabaseGetResultsOperationGroup.createUpdateGremlinDatabase](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/GremlinDatabaseGetResults.tsp#L54)                                | `requestMismatch` | `mapped-request-mismatch`                                   | [`6d73bab3d240dfe7`](#s-6d73bab3d240dfe7) |
| [Microsoft.DocumentDB.GremlinGraphGetResultsOperationGroup.createUpdateGremlinGraph](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/GremlinGraphGetResults.tsp#L54)                                         | `requestMismatch` | `mapped-request-mismatch`                                   | [`5a150435e0bf9c1c`](#s-5a150435e0bf9c1c) |
| [Microsoft.DocumentDB.GremlinResources.updateGremlinDatabaseThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L912)                                               | `requestMismatch` | `mapped-request-mismatch`                                   | [`673f2765007e9573`](#s-673f2765007e9573) |
| [Microsoft.DocumentDB.GremlinResourcesThroughputSettingsGetResultsOperationGroup.updateGremlinGraphThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L1002)       | `requestMismatch` | `mapped-request-mismatch`                                   | [`dc8068c9a16a3e6c`](#s-dc8068c9a16a3e6c) |
| [Microsoft.DocumentDB.MongoDBCollectionGetResultsOperationGroup.createUpdateMongoDBCollection](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/MongoDBCollectionGetResults.tsp#L58)                          | `requestMismatch` | `mapped-request-mismatch`                                   | [`67f350ba602a1e77`](#s-67f350ba602a1e77) |
| [Microsoft.DocumentDB.MongoDBDatabaseGetResultsOperationGroup.createUpdateMongoDBDatabase](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/MongoDBDatabaseGetResults.tsp#L59)                                | `requestMismatch` | `mapped-request-mismatch`                                   | [`2b8d5ec39f8e6396`](#s-2b8d5ec39f8e6396) |
| [Microsoft.DocumentDB.MongoDBResources.updateMongoDBDatabaseThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L323)                                               | `requestMismatch` | `mapped-request-mismatch`                                   | [`cd0334886a62fa92`](#s-cd0334886a62fa92) |
| [Microsoft.DocumentDB.MongoDBResourcesThroughputSettingsGetResultsOperationGroup.updateMongoDBCollectionThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L449)   | `requestMismatch` | `mapped-request-mismatch`                                   | [`eccb6e3257fb494e`](#s-eccb6e3257fb494e) |
| [Microsoft.DocumentDB.MongoRoleDefinitionGetResultsOperationGroup.createUpdateMongoRoleDefinition](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/MongoRoleDefinitionGetResults.tsp#L42)                    | `requestMismatch` | `mapped-request-mismatch`                                   | [`6cb87d2527f170dc`](#s-6cb87d2527f170dc) |
| [Microsoft.DocumentDB.MongoUserDefinitionGetResultsOperationGroup.createUpdateMongoUserDefinition](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/MongoUserDefinitionGetResults.tsp#L42)                    | `requestMismatch` | `mapped-request-mismatch`                                   | [`9da6aee26c1efe75`](#s-9da6aee26c1efe75) |
| [Microsoft.DocumentDB.ServiceResources.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ServiceResource.tsp#L47)                                                                                      | `requestMismatch` | `mapped-request-mismatch`                                   | [`5e8b88329bc7b1a1`](#s-5e8b88329bc7b1a1) |
| [Microsoft.DocumentDB.SqlContainerGetResultsOperationGroup.createUpdateSqlContainer](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/SqlContainerGetResults.tsp#L56)                                         | `requestMismatch` | `mapped-request-mismatch`                                   | [`b6ece0a02adea3f4`](#s-b6ece0a02adea3f4) |
| [Microsoft.DocumentDB.SqlResources.createUpdateSqlDatabase](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/SqlDatabaseGetResults.tsp#L56)                                                                   | `requestMismatch` | `mapped-request-mismatch`                                   | [`96312c7f7482dee6`](#s-96312c7f7482dee6) |
| [Microsoft.DocumentDB.SqlResourcesThroughputSettingsGetResultsOperationGroup.updateSqlContainerThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L211)            | `requestMismatch` | `mapped-request-mismatch`                                   | [`6aca430f0e23eff2`](#s-6aca430f0e23eff2) |
| [Microsoft.DocumentDB.SqlRoleAssignmentGetResultsOperationGroup.createUpdateSqlRoleAssignment](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/SqlRoleAssignmentGetResults.tsp#L42)                          | `requestMismatch` | `mapped-request-mismatch`                                   | [`f641eeeeb54bb1b8`](#s-f641eeeeb54bb1b8) |
| [Microsoft.DocumentDB.SqlRoleDefinitionGetResultsOperationGroup.createUpdateSqlRoleDefinition](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/SqlRoleDefinitionGetResults.tsp#L42)                          | `requestMismatch` | `mapped-request-mismatch`                                   | [`c7633b5ddecf0ded`](#s-c7633b5ddecf0ded) |
| [Microsoft.DocumentDB.SqlStoredProcedureGetResultsOperationGroup.createUpdateSqlStoredProcedure](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/SqlStoredProcedureGetResults.tsp#L55)                       | `requestMismatch` | `mapped-request-mismatch`                                   | [`8912a41b13e3d2a4`](#s-8912a41b13e3d2a4) |
| [Microsoft.DocumentDB.SqlTriggerGetResultsOperationGroup.createUpdateSqlTrigger](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/SqlTriggerGetResults.tsp#L55)                                               | `requestMismatch` | `mapped-request-mismatch`                                   | [`4750b61aaceacad3`](#s-4750b61aaceacad3) |
| [Microsoft.DocumentDB.SqlUserDefinedFunctionGetResultsOperationGroup.createUpdateSqlUserDefinedFunction](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/SqlUserDefinedFunctionGetResults.tsp#L55)           | `requestMismatch` | `mapped-request-mismatch`                                   | [`07ac7618e0649bfa`](#s-07ac7618e0649bfa) |
| [Microsoft.DocumentDB.TableGetResultsOperationGroup.createUpdateTable](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/TableGetResults.tsp#L54)                                                              | `requestMismatch` | `mapped-request-mismatch`                                   | [`70eb76d13df9cb4a`](#s-70eb76d13df9cb4a) |
| [Microsoft.DocumentDB.TableResources.updateTableThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L566)                                                           | `requestMismatch` | `mapped-request-mismatch`                                   | [`9d0e513b8b2001e3`](#s-9d0e513b8b2001e3) |
| [Microsoft.DocumentDB.ThroughputSettingsGetResultsOperationGroup.updateSqlDatabaseThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L90)                          | `requestMismatch` | `mapped-request-mismatch`                                   | [`930b038191c584c7`](#s-930b038191c584c7) |
| [Microsoft.DocumentDB.ViewCassandraResourcesThroughputSettingsGetResultsOperationGroup.updateCassandraViewThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L829) | `requestMismatch` | `mapped-request-mismatch`                                   | [`265aa27b73887877`](#s-265aa27b73887877) |
| [Microsoft.DataFactory.PrivateEndpointConnectionResources.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/datafactory/resource-manager/Microsoft.DataFactory/DataFactory/PrivateEndpointConnectionResource.tsp#L54)                                     | `requestMismatch` | `mapped-request-mismatch`                                   | [`f4b6d787dec42d61`](#s-f4b6d787dec42d61) |
| [Microsoft.Network.DnssecConfigs.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/dns/resource-manager/Microsoft.Network/Dns/DnssecConfig.tsp#L45)                                                                                                       | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.AAD.OuContainers.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/domainservices/resource-manager/Microsoft.AAD/DomainServices/OuContainer.tsp#L58)                                                                                                   | `requestMismatch` | `mapped-request-mismatch`                                   | [`a8fe35091a27ad02`](#s-a8fe35091a27ad02) |
| [Microsoft.EventGrid.DomainTopics.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/DomainTopic.tsp#L41)                                                                                         | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.HDInsight.Clusters.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/Cluster.tsp#L50)                                                                                                         | `requestMismatch` | `mapped-request-mismatch`                                   | [`c4bcc152bcc2531b`](#s-c4bcc152bcc2531b) |
| [Microsoft.HDInsight.Extensions.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/routes.tsp#L278)                                                                                                       | `requestMismatch` | `same-operation-different-comparison`                       | (none)                                    |
| [Microsoft.HealthcareApis.PrivateEndpointConnectionDescriptions.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis/PrivateEndpointConnectionDescription.tsp#L69)                   | `requestMismatch` | `mapped-request-mismatch`                                   | [`1eade2d50db1582c`](#s-1eade2d50db1582c) |
| [Microsoft.HorizonDb.HorizonDbAdministrators.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb/routes.tsp#L245)                                                                                  | `requestMismatch` | `mapped-request-mismatch`                                   | [`b0f7e5d05992ba29`](#s-b0f7e5d05992ba29) |
| [Microsoft.Devices.EventHubConsumerGroupInfos.createEventHubConsumerGroup](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/iothub/resource-manager/Microsoft.Devices/IoTHub/EventHubConsumerGroupInfo.tsp#L69)                                                          | `requestMismatch` | `mapped-request-mismatch`                                   | [`ae4b3b99a94936b7`](#s-ae4b3b99a94936b7) |
| [Microsoft.KeyVault.Keys.createIfNotExist](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/Key.tsp#L79)                                                                                                           | `requestMismatch` | `mapped-request-mismatch`                                   | [`f1556d52484cec77`](#s-f1556d52484cec77) |
| [Microsoft.KeyVault.ManagedHsmKeys.createIfNotExist](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/ManagedHsmKey.tsp#L77)                                                                                       | `requestMismatch` | `mapped-request-mismatch`                                   | [`d06c8a5fb5f17afe`](#s-d06c8a5fb5f17afe) |
| [Microsoft.KeyVault.Secrets.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/Secret.tsp#L54)                                                                                                       | `requestMismatch` | `mapped-request-mismatch`                                   | [`298528f12f334db4`](#s-298528f12f334db4) |
| [Microsoft.KeyVault.Vaults.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/Vault.tsp#L77)                                                                                                         | `requestMismatch` | `mapped-request-mismatch`                                   | [`3aad4a135b0bb0b0`](#s-3aad4a135b0bb0b0) |
| [Microsoft.Management.HierarchySettingsOperationGroup.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/management/resource-manager/Microsoft.Management/ManagementGroups/HierarchySettings.tsp#L42)                                                      | `requestMismatch` | `mapped-request-mismatch`                                   | [`126288d94fda2339`](#s-126288d94fda2339) |
| [Microsoft.Management.ManagementGroups.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/management/resource-manager/Microsoft.Management/ManagementGroups/ManagementGroup.tsp#L81)                                                                       | `requestMismatch` | `mapped-request-mismatch`                                   | [`b1a1905f0462b79f`](#s-b1a1905f0462b79f) |
| [Microsoft.Management.SubscriptionUnderManagementGroups.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/management/resource-manager/Microsoft.Management/ManagementGroups/SubscriptionUnderManagementGroup.tsp#L53)                                             | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.DBforMySQL.Backups.put](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/mysql/resource-manager/Microsoft.DBforMySQL/FlexibleServers/ServerBackup.tsp#L43)                                                                                                    | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Nginx.NginxPlus.NginxConfigurationResponses.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/nginx/resource-manager/Nginx.NginxPlus/NginxPlus/NginxConfigurationResponse.tsp#L38)                                                                       | `requestMismatch` | `mapped-request-mismatch`                                   | [`99a575bc062d01ad`](#s-99a575bc062d01ad) |
| [Nginx.NginxPlus.NginxDeploymentApiKeyResponses.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/nginx/resource-manager/Nginx.NginxPlus/NginxPlus/NginxDeploymentApiKeyResponse.tsp#L38)                                                                 | `requestMismatch` | `mapped-request-mismatch`                                   | [`4c27ca3deee1ed60`](#s-4c27ca3deee1ed60) |
| [Microsoft.DBforPostgreSQL.AdministratorMicrosoftEntras.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/postgresql/DBforPostgreSQL.Management/AdministratorMicrosoftEntra.tsp#L43)                                                                      | `requestMismatch` | `same-operation-different-comparison`                       | (none)                                    |
| [Microsoft.DBforPostgreSQL.BackupAutomaticAndOnDemands.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/postgresql/DBforPostgreSQL.Management/BackupAutomaticAndOnDemand.tsp#L41)                                                                                | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.DBforPostgreSQL.Configurations.put](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/postgresql/DBforPostgreSQL.Management/Configuration.tsp#L43)                                                                                                             | `requestMismatch` | `same-operation-different-comparison`                       | (none)                                    |
| [Microsoft.DBforPostgreSQL.DbAgents.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/postgresql/DBforPostgreSQL.Management/routes.tsp#L184)                                                                                                              | `requestMismatch` | `additional-request-check-outside-swagger-200-201-selector` | (none)                                    |
| [Microsoft.Quota.GroupQuotaSubscriptionIds.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/quota/resource-manager/Microsoft.Quota/Quota/GroupQuotaSubscriptionId.tsp#L81)                                                                               | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.RecoveryServices.Vaults.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices/Vault.tsp#L215)                                                                                | `requestMismatch` | `same-operation-different-comparison`                       | (none)                                    |
| [Microsoft.RecoveryServices.BackupResourceEncryptionConfigs.update](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/BackupResourceEncryptionConfigExtendedResource.tsp#L74)   | `requestMismatch` | `same-operation-different-comparison`                       | (none)                                    |
| [Microsoft.RecoveryServices.Alerts.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/Alert.tsp#L47)                                                                         | `requestMismatch` | `mapped-request-mismatch`                                   | [`3c1e17ac0515bb56`](#s-3c1e17ac0515bb56) |
| [Microsoft.RecoveryServices.Fabrics.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/Fabric.tsp#L87)                                                                       | `requestMismatch` | `mapped-request-mismatch`                                   | [`8dafe16a2ac4742a`](#s-8dafe16a2ac4742a) |
| [Microsoft.RecoveryServices.MigrationItems.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/MigrationItem.tsp#L51)                                                         | `requestMismatch` | `mapped-request-mismatch`                                   | [`5da833899a6ca8b2`](#s-5da833899a6ca8b2) |
| [Microsoft.RecoveryServices.NetworkMappings.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/NetworkMapping.tsp#L48)                                                       | `requestMismatch` | `mapped-request-mismatch`                                   | [`c5f7e94acda9528b`](#s-c5f7e94acda9528b) |
| [Microsoft.RecoveryServices.Policies.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/Policy.tsp#L46)                                                                      | `requestMismatch` | `mapped-request-mismatch`                                   | [`2967e7ab465b206e`](#s-2967e7ab465b206e) |
| [Microsoft.RecoveryServices.ProtectionContainerMappings.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/ProtectionContainerMapping.tsp#L48)                               | `requestMismatch` | `mapped-request-mismatch`                                   | [`d4aba7de8272b75a`](#s-d4aba7de8272b75a) |
| [Microsoft.RecoveryServices.ProtectionContainers.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/ProtectionContainer.tsp#L90)                                             | `requestMismatch` | `mapped-request-mismatch`                                   | [`b8222c99a4d012f0`](#s-b8222c99a4d012f0) |
| [Microsoft.RecoveryServices.RecoveryPlans.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/RecoveryPlan.tsp#L50)                                                           | `requestMismatch` | `mapped-request-mismatch`                                   | [`bab564cfa3acb771`](#s-bab564cfa3acb771) |
| [Microsoft.RecoveryServices.RecoveryServicesProviders.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/RecoveryServicesProvider.tsp#L58)                                   | `requestMismatch` | `mapped-request-mismatch`                                   | [`b5e12b9d313dedda`](#s-b5e12b9d313dedda) |
| [Microsoft.RecoveryServices.ReplicationProtectedItems.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/ReplicationProtectedItem.tsp#L95)                                   | `requestMismatch` | `mapped-request-mismatch`                                   | [`9186ed7d0ea7376a`](#s-9186ed7d0ea7376a) |
| [Microsoft.RecoveryServices.ReplicationProtectionIntents.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/ReplicationProtectionIntent.tsp#L47)                             | `requestMismatch` | `mapped-request-mismatch`                                   | [`d210db784e52df68`](#s-d210db784e52df68) |
| [Microsoft.RecoveryServices.StorageClassificationMappings.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/StorageClassificationMapping.tsp#L48)                           | `requestMismatch` | `mapped-request-mismatch`                                   | [`2e4017ed3d656c1e`](#s-2e4017ed3d656c1e) |
| [Microsoft.RecoveryServices.VCenters.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/VCenter.tsp#L49)                                                                     | `requestMismatch` | `mapped-request-mismatch`                                   | [`d102de4d81cbd3ff`](#s-d102de4d81cbd3ff) |
| [Microsoft.RecoveryServices.VaultSettings.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/VaultSetting.tsp#L65)                                                           | `requestMismatch` | `mapped-request-mismatch`                                   | [`1d9ac6271df17676`](#s-1d9ac6271df17676) |
| [Microsoft.Cache.LinkedServer.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/redis/resource-manager/Microsoft.Cache/Redis/RedisLinkedServerWithProperties.tsp#L63)                                                                                             | `requestMismatch` | `mapped-request-mismatch`                                   | [`4c6b8f698e11f401`](#s-4c6b8f698e11f401) |
| [Microsoft.Cache.RedisResources.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/redis/resource-manager/Microsoft.Cache/Redis/RedisResource.tsp#L60)                                                                                                             | `requestMismatch` | `mapped-request-mismatch`                                   | [`ee92b9b2ca843418`](#s-ee92b9b2ca843418) |
| [Reservations.ReservationOrderResponses.purchase](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Reservations/ReservationOrderResponse.tsp#L58)                                                          | `requestMismatch` | `mapped-request-mismatch`                                   | [`25128fd566ec6cae`](#s-25128fd566ec6cae) |
| [Microsoft.Resources.DeploymentExtendedManagementGroup.createOrUpdateAtManagementGroupScope](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/resources/resource-manager/Microsoft.Resources/deployments/DeploymentExtended.tsp#L462)                                    | `requestMismatch` | `mapped-request-mismatch`                                   | [`2539debec2183c88`](#s-2539debec2183c88) |
| [Microsoft.Resources.DeploymentExtendedOperationGroup.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/resources/resource-manager/Microsoft.Resources/deployments/DeploymentExtended.tsp#L846)                                                           | `requestMismatch` | `mapped-request-mismatch`                                   | [`3970ba63ac56b905`](#s-3970ba63ac56b905) |
| [Microsoft.Resources.DeploymentExtendedSubscriptionGroup.createOrUpdateAtSubscriptionScope](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/resources/resource-manager/Microsoft.Resources/deployments/DeploymentExtended.tsp#L654)                                     | `requestMismatch` | `mapped-request-mismatch`                                   | [`bcf447708adda74f`](#s-bcf447708adda74f) |
| [Microsoft.Resources.Deployments.createOrUpdateAtScope](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/resources/resource-manager/Microsoft.Resources/deployments/DeploymentExtended.tsp#L85)                                                                          | `requestMismatch` | `mapped-request-mismatch`                                   | [`cd90eaafa6e1243a`](#s-cd90eaafa6e1243a) |
| [Microsoft.Resources.DeploymentsExtendedTenant.createOrUpdateAtTenantScope](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/resources/resource-manager/Microsoft.Resources/deployments/DeploymentExtended.tsp#L264)                                                     | `requestMismatch` | `mapped-request-mismatch`                                   | [`b65884ae28978e52`](#s-b65884ae28978e52) |
| [ApiCollectionsAPI.ApiCollections.onboardAzureApiManagementApi](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/security/resource-manager/Microsoft.Security/Security/ApiCollectionsAPI/ApiCollection.tsp#L61)                                                          | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [AssessmentAPI.SecurityAssessmentResponses.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/security/resource-manager/Microsoft.Security/Security/AssessmentAPI/SecurityAssessmentResponse.tsp#L56)                                                      | `requestMismatch` | `mapped-request-mismatch`                                   | [`9ab25f6672013381`](#s-9ab25f6672013381) |
| [SecurityOperatorsAPI.SecurityOperators.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/security/resource-manager/Microsoft.Security/Security/SecurityOperatorsAPI/SecurityOperator.tsp#L78)                                                            | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [SecuritySolutionsAPI.ServerVulnerabilityAssessments.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/security/resource-manager/Microsoft.Security/Security/SecuritySolutionsAPI/ServerVulnerabilityAssessment.tsp#L93)                                  | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [SensitivitySettingsAPI.GetSensitivitySettingsResponses.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/security/resource-manager/Microsoft.Security/Security/SensitivitySettingsAPI/GetSensitivitySettingsResponse.tsp#L48)                            | `requestMismatch` | `mapped-request-mismatch`                                   | [`8fcc4fed76afe960`](#s-8fcc4fed76afe960) |
| [SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentBaselineRules.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI/RuleResults.tsp#L87)                       | `requestMismatch` | `mapped-request-mismatch`                                   | [`5855bd5b6e6f7223`](#s-5855bd5b6e6f7223) |
| [Microsoft.SecurityInsights.EntityQueries.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/EntityQuery.tsp#L88)                                                            | `requestMismatch` | `mapped-request-mismatch`                                   | [`bc51ed864cff2a1f`](#s-bc51ed864cff2a1f) |
| [Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentBaselineSets.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/sql/resource-manager/Microsoft.Sql/SQL/DatabaseSqlVulnerabilityAssessmentBaselineSet.tsp#L81)                                             | `requestMismatch` | `mapped-request-mismatch`                                   | [`25eb7ac0f78cc6ed`](#s-25eb7ac0f78cc6ed) |
| [Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentRuleBaselines.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/sql/resource-manager/Microsoft.Sql/SQL/DatabaseSqlVulnerabilityAssessmentRuleBaseline.tsp#L84)                                           | `requestMismatch` | `mapped-request-mismatch`                                   | [`64d8a1df7c00e65a`](#s-64d8a1df7c00e65a) |
| [Microsoft.Sql.ImportExportExtensionsOperationResults.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/sql/resource-manager/Microsoft.Sql/SQL/ImportExportExtensionsOperationResult.tsp#L50)                                                             | `requestMismatch` | `mapped-request-mismatch`                                   | [`7970e6692438c123`](#s-7970e6692438c123) |
| [Microsoft.Sql.JobExecutions.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/sql/resource-manager/Microsoft.Sql/SQL/JobExecution.tsp#L76)                                                                                                               | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.Sql.ManagedServerDnsAliases.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/sql/resource-manager/Microsoft.Sql/SQL/ManagedServerDnsAlias.tsp#L43)                                                                                            | `requestMismatch` | `mapped-request-mismatch`                                   | [`46dff1947112b2f2`](#s-46dff1947112b2f2) |
| [Microsoft.Sql.OutboundFirewallRules.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/sql/resource-manager/Microsoft.Sql/SQL/OutboundFirewallRule.tsp#L43)                                                                                               | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.Sql.ServerDnsAliases.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/sql/resource-manager/Microsoft.Sql/SQL/ServerDnsAlias.tsp#L43)                                                                                                          | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.Sql.SqlVulnerabilityAssessmentBaseline.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/sql/resource-manager/Microsoft.Sql/SQL/DatabaseSqlVulnerabilityAssessmentBaselineSet.tsp#L146)                                                        | `requestMismatch` | `mapped-request-mismatch`                                   | [`e672e41cbcb1cdde`](#s-e672e41cbcb1cdde) |
| [Microsoft.Sql.SqlVulnerabilityAssessmentRuleBaseline.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/sql/resource-manager/Microsoft.Sql/SQL/DatabaseSqlVulnerabilityAssessmentRuleBaseline.tsp#L159)                                                   | `requestMismatch` | `mapped-request-mismatch`                                   | [`85b0d6fa43cfaf1a`](#s-85b0d6fa43cfaf1a) |
| [Microsoft.Storage.StorageAccounts.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/storage/resource-manager/Microsoft.Storage/Storage/StorageAccount.tsp#L111)                                                                                                  | `requestMismatch` | `mapped-request-mismatch`                                   | [`fe9a0a8beddfb98f`](#s-fe9a0a8beddfb98f) |
| [Microsoft.StorageSync.CloudEndpoints.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/CloudEndpoint.tsp#L55)                                                                                     | `requestMismatch` | `mapped-request-mismatch`                                   | [`c66d4b452c9ef375`](#s-c66d4b452c9ef375) |
| [Microsoft.StorageSync.RegisteredServers.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/RegisteredServer.tsp#L54)                                                                               | `requestMismatch` | `mapped-request-mismatch`                                   | [`2fd98161d8adcfd3`](#s-2fd98161d8adcfd3) |
| [Microsoft.StorageSync.ServerEndpoints.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/ServerEndpoint.tsp#L53)                                                                                   | `requestMismatch` | `mapped-request-mismatch`                                   | [`5347141e830697b7`](#s-5347141e830697b7) |
| [Microsoft.StorageSync.StorageSyncServices.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/StorageSyncService.tsp#L52)                                                                           | `requestMismatch` | `mapped-request-mismatch`                                   | [`a93ba334f29ff387`](#s-a93ba334f29ff387) |
| [Microsoft.StorageSync.SyncGroups.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/SyncGroup.tsp#L51)                                                                                             | `requestMismatch` | `mapped-request-mismatch`                                   | [`9beeadcf7b7fa3a0`](#s-9beeadcf7b7fa3a0) |
| [Microsoft.Subscription.GetTenantPolicyResponses.addUpdatePolicyForTenant](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/GetTenantPolicyResponse.tsp#L43)                                           | `requestMismatch` | `mapped-request-mismatch`                                   | [`9fb05cc3244469f8`](#s-9fb05cc3244469f8) |
| [Microsoft.Subscription.SubscriptionAliasResponses.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/SubscriptionAliasResponse.tsp#L40)                                                         | `requestMismatch` | `mapped-request-mismatch`                                   | [`e61cca263ccff3b7`](#s-e61cca263ccff3b7) |
| [Microsoft.Subscription.TargetDirectoryResults.putTargetDirectory](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/TargetDirectoryResult.tsp#L51)                                                     | `requestMismatch` | `mapped-request-mismatch`                                   | [`09326584113e2a3a`](#s-09326584113e2a3a) |
| [Microsoft.Support.FileWorkspaces.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/support/resource-manager/Microsoft.Support/Support/FileWorkspaceDetails.tsp#L54)                                                                                              | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.Support.FileWorkspacesNoSubscription.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/support/resource-manager/Microsoft.Support/Support/FileWorkspaceDetails.tsp#L87)                                                                                | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.Web.FunctionEnvelopeOperationGroup.createOrUpdateFunctionSecretSlot](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/FunctionEnvelope.tsp#L350)                                                                | `requestMismatch` | `same-operation-different-comparison`                       | (none)                                    |
| [Microsoft.Web.InstanceMSDeployStatusOperationGroup.createInstanceMSDeployOperationSlot](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/MSDeployStatus.tsp#L324)                                                         | `requestMismatch` | `mapped-request-mismatch`                                   | [`e1629ee96cac1c89`](#s-e1629ee96cac1c89) |
| [Microsoft.Web.MSDeployStatusOperationGroup.createInstanceMSDeployOperation](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/MSDeployStatus.tsp#L161)                                                                     | `requestMismatch` | `mapped-request-mismatch`                                   | [`1dfddeaf18be16cd`](#s-1dfddeaf18be16cd) |
| [Microsoft.Web.MSDeployStatusSlotOperationGroup.createMSDeployOperationSlot](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/MSDeployStatus.tsp#L239)                                                                     | `requestMismatch` | `mapped-request-mismatch`                                   | [`93a320df959a9968`](#s-93a320df959a9968) |
| [Microsoft.Web.MSDeployStatuses.createMSDeployOperation](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/MSDeployStatus.tsp#L82)                                                                                          | `requestMismatch` | `mapped-request-mismatch`                                   | [`4cd8762330aa680c`](#s-4cd8762330aa680c) |
| [Microsoft.Web.SiteExtensionInfoOperationGroup.installSiteExtensionSlot](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/SiteExtensionInfo.tsp#L165)                                                                      | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.Web.SiteExtensionInfos.installSiteExtension](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/SiteExtensionInfo.tsp#L77)                                                                                        | `missingRequest`  | `additional-missing-request-policy`                         | (none)                                    |
| [Microsoft.Web.StaticSiteCustomDomainOverviewARMResources.createOrUpdateStaticSiteCustomDomain](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/StaticSiteCustomDomainOverviewARMResource.tsp#L54)                        | `requestMismatch` | `mapped-request-mismatch`                                   | [`e5d6f2c465883792`](#s-e5d6f2c465883792) |

## Per-project target differences

Use the project links in [Differing projects](#differing-projects) for every original target, corresponding TypeSpec operation/model and disposition. Project pages keep the evidence small enough to render on GitHub. All 277 check groups remain in the machine-readable assessment.

## Matching request targets

These 144 controls are listed separately from differences. Each has one original raw finding and one TypeSpec requestMismatch on the same PUT, with the selected source response equal to the canonical resource. The full output retains the exact request, resource, status-specific bodies, source line and diagnostic.

| Check ID / source                                                                                                                                                                                                                                                                                                                                                                   | Swagger operation / request                                                                                                            | Canonical selected response                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| <a id="s-d6c6d92c9a0f4dc9"></a>`d6c6d92c9a0f4dc9` [Microsoft.ApiManagement.ApiContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/ApiContract.tsp#L93)                                                                         | `Api_CreateOrUpdate` / `Microsoft.ApiManagement.ApiCreateOrUpdateParameter`                                                            | `Microsoft.ApiManagement.ApiContract`                           |
| <a id="s-a0043bfa2f35690b"></a>`a0043bfa2f35690b` [Microsoft.ApiManagement.TagDescriptionContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagDescriptionContract.tsp#L102)                                                  | `ApiTagDescription_CreateOrUpdate` / `Microsoft.ApiManagement.TagDescriptionCreateParameters`                                          | `Microsoft.ApiManagement.TagDescriptionContract`                |
| <a id="s-07a4fba5ab458883"></a>`07a4fba5ab458883` [Microsoft.ApiManagement.CertificateContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/CertificateContract.tsp#L97)                                                         | `Certificate_CreateOrUpdate` / `Microsoft.ApiManagement.CertificateCreateOrUpdateParameters`                                           | `Microsoft.ApiManagement.CertificateContract`                   |
| <a id="s-a24e9f05205ca77e"></a>`a24e9f05205ca77e` [Microsoft.ApiManagement.GroupContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/GroupContract.tsp#L188)                                                                    | `Group_CreateOrUpdate` / `Microsoft.ApiManagement.GroupCreateParameters`                                                               | `Microsoft.ApiManagement.GroupContract`                         |
| <a id="s-16bb019f51c54666"></a>`16bb019f51c54666` [Microsoft.ApiManagement.IdentityProviderContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/IdentityProviderContract.tsp#L62)                                               | `IdentityProvider_CreateOrUpdate` / `Microsoft.ApiManagement.IdentityProviderCreateContract`                                           | `Microsoft.ApiManagement.IdentityProviderContract`              |
| <a id="s-4074356758b8b55a"></a>`4074356758b8b55a` [Microsoft.ApiManagement.NamedValueContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NamedValueContract.tsp#L91)                                                           | `NamedValue_CreateOrUpdate` / `Microsoft.ApiManagement.NamedValueCreateContract`                                                       | `Microsoft.ApiManagement.NamedValueContract`                    |
| <a id="s-9bd66fb3b423b668"></a>`9bd66fb3b423b668` [Microsoft.ApiManagement.SubscriptionContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/SubscriptionContract.tsp#L91)                                                       | `Subscription_CreateOrUpdate` / `Microsoft.ApiManagement.SubscriptionCreateParameters`                                                 | `Microsoft.ApiManagement.SubscriptionContract`                  |
| <a id="s-c24f5593e4c0444c"></a>`c24f5593e4c0444c` [Microsoft.ApiManagement.TagContractOperationGroup.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagContract.tsp#L453)                                                           | `Tag_CreateOrUpdate` / `Microsoft.ApiManagement.TagCreateUpdateParameters`                                                             | `Microsoft.ApiManagement.TagContract`                           |
| <a id="s-5bc868e33cb12f58"></a>`5bc868e33cb12f58` [Microsoft.ApiManagement.EmailTemplateContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/EmailTemplateContract.tsp#L89)                                                     | `EmailTemplate_CreateOrUpdate` / `Microsoft.ApiManagement.EmailTemplateUpdateParameters`                                               | `Microsoft.ApiManagement.EmailTemplateContract`                 |
| <a id="s-6d6f81e97257180a"></a>`6d6f81e97257180a` [Microsoft.ApiManagement.AccessInformationContracts.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/AccessInformationContract.tsp#L91)                                                     | `TenantAccess_Create` / `Microsoft.ApiManagement.AccessInformationCreateParameters`                                                    | `Microsoft.ApiManagement.AccessInformationContract`             |
| <a id="s-abb6d8ec653be75b"></a>`abb6d8ec653be75b` [Microsoft.ApiManagement.UserContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/UserContract.tsp#L61)                                                                       | `User_CreateOrUpdate` / `Microsoft.ApiManagement.UserCreateParameters`                                                                 | `Microsoft.ApiManagement.UserContract`                          |
| <a id="s-f480a1873a8a46d6"></a>`f480a1873a8a46d6` [Microsoft.ApiManagement.WorkspaceApi.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/ApiContract.tsp#L395)                                                                        | `WorkspaceApi_CreateOrUpdate` / `Microsoft.ApiManagement.ApiCreateOrUpdateParameter`                                                   | `Microsoft.ApiManagement.ApiContract`                           |
| <a id="s-4fe374080228c379"></a>`4fe374080228c379` [Microsoft.ApiManagement.WorkspaceCertificate.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/CertificateContract.tsp#L273)                                                        | `WorkspaceCertificate_CreateOrUpdate` / `Microsoft.ApiManagement.CertificateCreateOrUpdateParameters`                                  | `Microsoft.ApiManagement.CertificateContract`                   |
| <a id="s-aab9a5c4285f75fb"></a>`aab9a5c4285f75fb` [Microsoft.ApiManagement.WorkspaceGroup.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/GroupContract.tsp#L438)                                                                    | `WorkspaceGroup_CreateOrUpdate` / `Microsoft.ApiManagement.GroupCreateParameters`                                                      | `Microsoft.ApiManagement.GroupContract`                         |
| <a id="s-e76bb208f825a268"></a>`e76bb208f825a268` [Microsoft.ApiManagement.WorkspaceNamedValue.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NamedValueContract.tsp#L306)                                                          | `WorkspaceNamedValue_CreateOrUpdate` / `Microsoft.ApiManagement.NamedValueCreateContract`                                              | `Microsoft.ApiManagement.NamedValueContract`                    |
| <a id="s-ddf45b716631a01b"></a>`ddf45b716631a01b` [Microsoft.ApiManagement.WorkspaceSubscription.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/SubscriptionContract.tsp#L403)                                                      | `WorkspaceSubscription_CreateOrUpdate` / `Microsoft.ApiManagement.SubscriptionCreateParameters`                                        | `Microsoft.ApiManagement.SubscriptionContract`                  |
| <a id="s-ea5b75fffe317a54"></a>`ea5b75fffe317a54` [Microsoft.ApiManagement.WorkspaceTag.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagContract.tsp#L628)                                                                        | `WorkspaceTag_CreateOrUpdate` / `Microsoft.ApiManagement.TagCreateUpdateParameters`                                                    | `Microsoft.ApiManagement.TagContract`                           |
| <a id="s-9c84623c7997c7e8"></a>`9c84623c7997c7e8` [Microsoft.Attestation.AttestationProviders.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/attestation/resource-manager/Microsoft.Attestation/Attestation/AttestationProvider.tsp#L61)                                                                         | `AttestationProviders_Create` / `Microsoft.Attestation.AttestationServiceCreationParams`                                               | `Microsoft.Attestation.AttestationProvider`                     |
| <a id="s-0039d3e2e8604534"></a>`0039d3e2e8604534` [Microsoft.AttributeNamespaces.AccessReviewHistoryDefinitions.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/AccessReviewHistoryDefinition.tsp#L65)                          | `AccessReviewHistoryDefinition_Create` / `Microsoft.AttributeNamespaces.AccessReviewHistoryDefinitionProperties`                       | `Microsoft.AttributeNamespaces.AccessReviewHistoryDefinition`   |
| <a id="s-b5ef44d92176b2c4"></a>`b5ef44d92176b2c4` [Microsoft.AttributeNamespaces.AccessReviewScheduleDefinitions.createOrUpdateById](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/AccessReviewScheduleDefinition.tsp#L84)            | `AccessReviewScheduleDefinitions_CreateOrUpdateById` / `Microsoft.AttributeNamespaces.AccessReviewScheduleDefinitionProperties`        | `Microsoft.AttributeNamespaces.AccessReviewScheduleDefinition`  |
| <a id="s-85f4458dae5f772c"></a>`85f4458dae5f772c` [Microsoft.AttributeNamespaces.AccessReviewInstances.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/AccessReviewInstance.tsp#L72)                                            | `AccessReviewInstances_Create` / `Microsoft.AttributeNamespaces.AccessReviewInstanceProperties`                                        | `Microsoft.AttributeNamespaces.AccessReviewInstance`            |
| <a id="s-2eb48d6c239daee9"></a>`2eb48d6c239daee9` [Microsoft.AttributeNamespaces.AccessReviewDefaultSettingsOperationGroup.put](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/AccessReviewDefaultSettings.tsp#L62)                    | `AccessReviewDefaultSettings_Put` / `Microsoft.AttributeNamespaces.AccessReviewScheduleSettings`                                       | `Microsoft.AttributeNamespaces.AccessReviewDefaultSettings`     |
| <a id="s-6b3a035269cdee71"></a>`6b3a035269cdee71` [Microsoft.AttributeNamespaces.ScopeAccessReviewHistoryDefinitions.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/AccessReviewHistoryDefinition.tsp#L173)                    | `ScopeAccessReviewHistoryDefinition_Create` / `Microsoft.AttributeNamespaces.AccessReviewHistoryDefinitionProperties`                  | `Microsoft.AttributeNamespaces.AccessReviewHistoryDefinition`   |
| <a id="s-4972a9ee4dfdd4ae"></a>`4972a9ee4dfdd4ae` [Microsoft.AttributeNamespaces.ScopeAccessReviewScheduleDefinitions.createOrUpdateById](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/AccessReviewScheduleDefinition.tsp#L169)      | `ScopeAccessReviewScheduleDefinitions_CreateOrUpdateById` / `Microsoft.AttributeNamespaces.AccessReviewScheduleDefinitionProperties`   | `Microsoft.AttributeNamespaces.AccessReviewScheduleDefinition`  |
| <a id="s-441d5618033269e7"></a>`441d5618033269e7` [Microsoft.AttributeNamespaces.ScopeAccessReviewInstances.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/AccessReviewInstance.tsp#L224)                                      | `ScopeAccessReviewInstances_Create` / `Microsoft.AttributeNamespaces.AccessReviewInstanceProperties`                                   | `Microsoft.AttributeNamespaces.AccessReviewInstance`            |
| <a id="s-22c2dd3e8b4a25fd"></a>`22c2dd3e8b4a25fd` [Microsoft.AttributeNamespaces.ScopeAccessReviewDefaultSettings.put](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/AccessReviewDefaultSettings.tsp#L107)                            | `ScopeAccessReviewDefaultSettings_Put` / `Microsoft.AttributeNamespaces.AccessReviewScheduleSettings`                                  | `Microsoft.AttributeNamespaces.AccessReviewDefaultSettings`     |
| <a id="s-b13069e2bfb91132"></a>`b13069e2bfb91132` [Microsoft.RoleAssignment.RoleAssignmentsByIdOperations.createById](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/RoleAssignment/RoleAssignment.tsp#L309)                                        | `RoleAssignments_CreateById` / `Microsoft.RoleAssignment.RoleAssignmentCreateParameters`                                               | `Microsoft.RoleAssignment.RoleAssignment`                       |
| <a id="s-9c317d438b4a5f71"></a>`9c317d438b4a5f71` [Microsoft.RoleAssignment.RoleAssignments.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/RoleAssignment/RoleAssignment.tsp#L161)                                                          | `RoleAssignments_Create` / `Microsoft.RoleAssignment.RoleAssignmentCreateParameters`                                                   | `Microsoft.RoleAssignment.RoleAssignment`                       |
| <a id="s-db520c522579a0ff"></a>`db520c522579a0ff` [Microsoft.Automation.AutomationAccounts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/AutomationAccount.tsp#L76)                                                                         | `AutomationAccount_CreateOrUpdate` / `Microsoft.Automation.AutomationAccountCreateOrUpdateParameters`                                  | `Microsoft.Automation.AutomationAccount`                        |
| <a id="s-2ee09847cc1ea272"></a>`2ee09847cc1ea272` [Microsoft.Automation.Certificates.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Certificate.tsp#L43)                                                                                     | `Certificate_CreateOrUpdate` / `Microsoft.Automation.CertificateCreateOrUpdateParameters`                                              | `Microsoft.Automation.Certificate`                              |
| <a id="s-30747121ec0c0631"></a>`30747121ec0c0631` [Microsoft.Automation.DscConfigurations.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/DscConfiguration.tsp#L49)                                                                           | `DscConfiguration_CreateOrUpdate` / `Microsoft.Automation.DscConfigurationCreateOrUpdateParameters`                                    | `Microsoft.Automation.DscConfiguration`                         |
| <a id="s-8c696c8d8a3847e6"></a>`8c696c8d8a3847e6` [Microsoft.Automation.ConnectionTypes.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/ConnectionType.tsp#L44)                                                                               | `ConnectionType_CreateOrUpdate` / `Microsoft.Automation.ConnectionTypeCreateOrUpdateParameters`                                        | `Microsoft.Automation.ConnectionType`                           |
| <a id="s-6c42af6ba5bf267b"></a>`6c42af6ba5bf267b` [Microsoft.Automation.Connections.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Connection.tsp#L42)                                                                                       | `Connection_CreateOrUpdate` / `Microsoft.Automation.ConnectionCreateOrUpdateParameters`                                                | `Microsoft.Automation.Connection`                               |
| <a id="s-701d9778f09f2bce"></a>`701d9778f09f2bce` [Microsoft.Automation.Credentials.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Credential.tsp#L42)                                                                                       | `Credential_CreateOrUpdate` / `Microsoft.Automation.CredentialCreateOrUpdateParameters`                                                | `Microsoft.Automation.Credential`                               |
| <a id="s-c700a5800790bded"></a>`c700a5800790bded` [Microsoft.Automation.HybridRunbookWorkerGroups.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/HybridRunbookWorkerGroup.tsp#L44)                                                                   | `HybridRunbookWorkerGroup_Create` / `Microsoft.Automation.HybridRunbookWorkerGroupCreateOrUpdateParameters`                            | `Microsoft.Automation.HybridRunbookWorkerGroup`                 |
| <a id="s-292f816b17f7d7b1"></a>`292f816b17f7d7b1` [Microsoft.Automation.HybridRunbookWorkers.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/HybridRunbookWorker.tsp#L43)                                                                             | `HybridRunbookWorkers_Create` / `Microsoft.Automation.HybridRunbookWorkerCreateParameters`                                             | `Microsoft.Automation.HybridRunbookWorker`                      |
| <a id="s-7ae44ff3ae6d7f4f"></a>`7ae44ff3ae6d7f4f` [Microsoft.Automation.JobSchedules.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/JobSchedule.tsp#L44)                                                                                             | `JobSchedule_Create` / `Microsoft.Automation.JobScheduleCreateParameters`                                                              | `Microsoft.Automation.JobSchedule`                              |
| <a id="s-ed051c77ccddb09c"></a>`ed051c77ccddb09c` [Microsoft.Automation.Jobs.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Job.tsp#L54)                                                                                                             | `Job_Create` / `Microsoft.Automation.JobCreateParameters`                                                                              | `Microsoft.Automation.Job`                                      |
| <a id="s-c7ced7c3b979f1c9"></a>`c7ced7c3b979f1c9` [Microsoft.Automation.Modules.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Module.tsp#L71)                                                                                               | `Module_CreateOrUpdate` / `Microsoft.Automation.ModuleCreateOrUpdateParameters`                                                        | `Microsoft.Automation.Module`                                   |
| <a id="s-345af9cecebe896b"></a>`345af9cecebe896b` [Microsoft.Automation.Python2Package.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Module.tsp#L223)                                                                                       | `Python2Package_CreateOrUpdate` / `Microsoft.Automation.PythonPackageCreateParameters`                                                 | `Microsoft.Automation.Module`                                   |
| <a id="s-7b2dd73598a4c620"></a>`7b2dd73598a4c620` [Microsoft.Automation.Python3Package.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Module.tsp#L291)                                                                                       | `Python3Package_CreateOrUpdate` / `Microsoft.Automation.PythonPackageCreateParameters`                                                 | `Microsoft.Automation.Module`                                   |
| <a id="s-62212bf10d0eb1ee"></a>`62212bf10d0eb1ee` [Microsoft.Automation.Runbooks.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Runbook.tsp#L65)                                                                                             | `Runbook_CreateOrUpdate` / `Microsoft.Automation.RunbookCreateOrUpdateParameters`                                                      | `Microsoft.Automation.Runbook`                                  |
| <a id="s-1a6a16a376d63d73"></a>`1a6a16a376d63d73` [Microsoft.Automation.Packages.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Package.tsp#L42)                                                                                             | `Package_CreateOrUpdate` / `Microsoft.Automation.PackageCreateOrUpdateParameters`                                                      | `Microsoft.Automation.Package`                                  |
| <a id="s-b6e8e0ed0ffa0a7e"></a>`b6e8e0ed0ffa0a7e` [Microsoft.Automation.Schedules.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Schedule.tsp#L43)                                                                                           | `Schedule_CreateOrUpdate` / `Microsoft.Automation.ScheduleCreateOrUpdateParameters`                                                    | `Microsoft.Automation.Schedule`                                 |
| <a id="s-a5926ec404279bda"></a>`a5926ec404279bda` [Microsoft.Automation.SourceControls.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/SourceControl.tsp#L55)                                                                                 | `SourceControl_CreateOrUpdate` / `Microsoft.Automation.SourceControlCreateOrUpdateParameters`                                          | `Microsoft.Automation.SourceControl`                            |
| <a id="s-824155ae51a4294c"></a>`824155ae51a4294c` [Microsoft.Automation.Variables.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Variable.tsp#L42)                                                                                           | `Variable_CreateOrUpdate` / `Microsoft.Automation.VariableCreateOrUpdateParameters`                                                    | `Microsoft.Automation.Variable`                                 |
| <a id="s-28f094b6475664fd"></a>`28f094b6475664fd` [Microsoft.Automation.Webhooks.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/Webhook.tsp#L42)                                                                                             | `Webhook_CreateOrUpdate` / `Microsoft.Automation.WebhookCreateOrUpdateParameters`                                                      | `Microsoft.Automation.Webhook`                                  |
| <a id="s-26cefb8c076b5dda"></a>`26cefb8c076b5dda` [Microsoft.Batch.BatchAccounts.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/batch/resource-manager/Microsoft.Batch/Batch/BatchAccount.tsp#L44)                                                                                                               | `BatchAccount_Create` / `Microsoft.Batch.BatchAccountCreateParameters`                                                                 | `Microsoft.Batch.BatchAccount`                                  |
| <a id="s-3c56ad68fe60248e"></a>`3c56ad68fe60248e` [Microsoft.Billing.PartnerTransfers.initiate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/billing/resource-manager/Microsoft.Billing/Billing/PartnerTransferDetails.tsp#L52)                                                                                        | `PartnerTransfers_Initiate` / `Microsoft.Billing.PartnerInitiateTransferRequest`                                                       | `Microsoft.Billing.PartnerTransferDetails`                      |
| <a id="s-fc900d8332d940cc"></a>`fc900d8332d940cc` [Microsoft.Billing.Transfers.initiate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/billing/resource-manager/Microsoft.Billing/Billing/TransferDetails.tsp#L50)                                                                                                      | `Transfers_Initiate` / `Microsoft.Billing.InitiateTransferRequest`                                                                     | `Microsoft.Billing.TransferDetails`                             |
| <a id="s-27f2841e3a69a04c"></a>`27f2841e3a69a04c` [Microsoft.BillingBenefits.ReservationOrderAliasResponses.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits/ReservationOrderAliasResponse.tsp#L54)                                     | `ReservationOrderAlias_Create` / `Microsoft.BillingBenefits.ReservationOrderAliasRequest`                                              | `Microsoft.BillingBenefits.ReservationOrderAliasResponse`       |
| <a id="s-b8c23f8be92990e5"></a>`b8c23f8be92990e5` [Microsoft.Cdn.CustomDomains.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/CustomDomain.tsp#L41)                                                                                                                       | `CustomDomains_Create` / `Microsoft.Cdn.CustomDomainParameters`                                                                        | `Microsoft.Cdn.CustomDomain`                                    |
| <a id="s-32e3c2def02f5a05"></a>`32e3c2def02f5a05` [Microsoft.ContainerRegistry.Webhooks.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/Webhook.tsp#L36)                                                                                  | `Webhooks_Create` / `Microsoft.ContainerRegistry.WebhookCreateParameters`                                                              | `Microsoft.ContainerRegistry.Webhook`                           |
| <a id="s-0f2d9f17cb87c7cf"></a>`0f2d9f17cb87c7cf` [Microsoft.DocumentDB.CassandraKeyspaceGetResultsOperationGroup.createUpdateCassandraKeyspace](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/CassandraKeyspaceGetResults.tsp#L54)                          | `CassandraResources_CreateUpdateCassandraKeyspace` / `Microsoft.DocumentDB.CassandraKeyspaceCreateUpdateParameters`                    | `Microsoft.DocumentDB.CassandraKeyspaceGetResults`              |
| <a id="s-50be0c4a42ffcc8c"></a>`50be0c4a42ffcc8c` [Microsoft.DocumentDB.CassandraTableGetResultsOperationGroup.createUpdateCassandraTable](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/CassandraTableGetResults.tsp#L54)                                   | `CassandraResources_CreateUpdateCassandraTable` / `Microsoft.DocumentDB.CassandraTableCreateUpdateParameters`                          | `Microsoft.DocumentDB.CassandraTableGetResults`                 |
| <a id="s-ac6f0249cbe35516"></a>`ac6f0249cbe35516` [Microsoft.DocumentDB.CassandraResourcesThroughputSettingsGetResultsOperationGroup.updateCassandraTableThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L739)    | `CassandraResources_UpdateCassandraTableThroughput` / `Microsoft.DocumentDB.ThroughputSettingsUpdateParameters`                        | `Microsoft.DocumentDB.ThroughputSettingsGetResults`             |
| <a id="s-1143ed1af0d6a699"></a>`1143ed1af0d6a699` [Microsoft.DocumentDB.CassandraResources.updateCassandraKeyspaceThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L649)                                           | `CassandraResources_UpdateCassandraKeyspaceThroughput` / `Microsoft.DocumentDB.ThroughputSettingsUpdateParameters`                     | `Microsoft.DocumentDB.ThroughputSettingsGetResults`             |
| <a id="s-0999b8017d3a3ca3"></a>`0999b8017d3a3ca3` [Microsoft.DocumentDB.CassandraViewGetResultsOperationGroup.createUpdateCassandraView](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/CassandraViewGetResults.tsp#L58)                                      | `CassandraResources_CreateUpdateCassandraView` / `Microsoft.DocumentDB.CassandraViewCreateUpdateParameters`                            | `Microsoft.DocumentDB.CassandraViewGetResults`                  |
| <a id="s-265aa27b73887877"></a>`265aa27b73887877` [Microsoft.DocumentDB.ViewCassandraResourcesThroughputSettingsGetResultsOperationGroup.updateCassandraViewThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L829) | `CassandraResources_UpdateCassandraViewThroughput` / `Microsoft.DocumentDB.ThroughputSettingsUpdateParameters`                         | `Microsoft.DocumentDB.ThroughputSettingsGetResults`             |
| <a id="s-44196ad97da9b599"></a>`44196ad97da9b599` [Microsoft.DocumentDB.DataTransferJobs.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/DataTransferJobGetResults.tsp#L44)                                                                            | `DataTransferJobs_Create` / `Microsoft.DocumentDB.CreateJobRequest`                                                                    | `Microsoft.DocumentDB.DataTransferJobGetResults`                |
| <a id="s-ccc457dafd55a252"></a>`ccc457dafd55a252` [Microsoft.DocumentDB.GraphResources.createUpdateGraph](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/GraphResourceGetResults.tsp#L58)                                                                     | `GraphResources_CreateUpdateGraph` / `Microsoft.DocumentDB.GraphResourceCreateUpdateParameters`                                        | `Microsoft.DocumentDB.GraphResourceGetResults`                  |
| <a id="s-6d73bab3d240dfe7"></a>`6d73bab3d240dfe7` [Microsoft.DocumentDB.GremlinDatabaseGetResultsOperationGroup.createUpdateGremlinDatabase](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/GremlinDatabaseGetResults.tsp#L54)                                | `GremlinResources_CreateUpdateGremlinDatabase` / `Microsoft.DocumentDB.GremlinDatabaseCreateUpdateParameters`                          | `Microsoft.DocumentDB.GremlinDatabaseGetResults`                |
| <a id="s-5a150435e0bf9c1c"></a>`5a150435e0bf9c1c` [Microsoft.DocumentDB.GremlinGraphGetResultsOperationGroup.createUpdateGremlinGraph](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/GremlinGraphGetResults.tsp#L54)                                         | `GremlinResources_CreateUpdateGremlinGraph` / `Microsoft.DocumentDB.GremlinGraphCreateUpdateParameters`                                | `Microsoft.DocumentDB.GremlinGraphGetResults`                   |
| <a id="s-dc8068c9a16a3e6c"></a>`dc8068c9a16a3e6c` [Microsoft.DocumentDB.GremlinResourcesThroughputSettingsGetResultsOperationGroup.updateGremlinGraphThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L1002)       | `GremlinResources_UpdateGremlinGraphThroughput` / `Microsoft.DocumentDB.ThroughputSettingsUpdateParameters`                            | `Microsoft.DocumentDB.ThroughputSettingsGetResults`             |
| <a id="s-673f2765007e9573"></a>`673f2765007e9573` [Microsoft.DocumentDB.GremlinResources.updateGremlinDatabaseThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L912)                                               | `GremlinResources_UpdateGremlinDatabaseThroughput` / `Microsoft.DocumentDB.ThroughputSettingsUpdateParameters`                         | `Microsoft.DocumentDB.ThroughputSettingsGetResults`             |
| <a id="s-2b8d5ec39f8e6396"></a>`2b8d5ec39f8e6396` [Microsoft.DocumentDB.MongoDBDatabaseGetResultsOperationGroup.createUpdateMongoDBDatabase](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/MongoDBDatabaseGetResults.tsp#L59)                                | `MongoDBResources_CreateUpdateMongoDBDatabase` / `Microsoft.DocumentDB.MongoDBDatabaseCreateUpdateParameters`                          | `Microsoft.DocumentDB.MongoDBDatabaseGetResults`                |
| <a id="s-67f350ba602a1e77"></a>`67f350ba602a1e77` [Microsoft.DocumentDB.MongoDBCollectionGetResultsOperationGroup.createUpdateMongoDBCollection](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/MongoDBCollectionGetResults.tsp#L58)                          | `MongoDBResources_CreateUpdateMongoDBCollection` / `Microsoft.DocumentDB.MongoDBCollectionCreateUpdateParameters`                      | `Microsoft.DocumentDB.MongoDBCollectionGetResults`              |
| <a id="s-eccb6e3257fb494e"></a>`eccb6e3257fb494e` [Microsoft.DocumentDB.MongoDBResourcesThroughputSettingsGetResultsOperationGroup.updateMongoDBCollectionThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L449)   | `MongoDBResources_UpdateMongoDBCollectionThroughput` / `Microsoft.DocumentDB.ThroughputSettingsUpdateParameters`                       | `Microsoft.DocumentDB.ThroughputSettingsGetResults`             |
| <a id="s-cd0334886a62fa92"></a>`cd0334886a62fa92` [Microsoft.DocumentDB.MongoDBResources.updateMongoDBDatabaseThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L323)                                               | `MongoDBResources_UpdateMongoDBDatabaseThroughput` / `Microsoft.DocumentDB.ThroughputSettingsUpdateParameters`                         | `Microsoft.DocumentDB.ThroughputSettingsGetResults`             |
| <a id="s-6cb87d2527f170dc"></a>`6cb87d2527f170dc` [Microsoft.DocumentDB.MongoRoleDefinitionGetResultsOperationGroup.createUpdateMongoRoleDefinition](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/MongoRoleDefinitionGetResults.tsp#L42)                    | `MongoDBResources_CreateUpdateMongoRoleDefinition` / `Microsoft.DocumentDB.MongoRoleDefinitionCreateUpdateParameters`                  | `Microsoft.DocumentDB.MongoRoleDefinitionGetResults`            |
| <a id="s-9da6aee26c1efe75"></a>`9da6aee26c1efe75` [Microsoft.DocumentDB.MongoUserDefinitionGetResultsOperationGroup.createUpdateMongoUserDefinition](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/MongoUserDefinitionGetResults.tsp#L42)                    | `MongoDBResources_CreateUpdateMongoUserDefinition` / `Microsoft.DocumentDB.MongoUserDefinitionCreateUpdateParameters`                  | `Microsoft.DocumentDB.MongoUserDefinitionGetResults`            |
| <a id="s-5e8b88329bc7b1a1"></a>`5e8b88329bc7b1a1` [Microsoft.DocumentDB.ServiceResources.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ServiceResource.tsp#L47)                                                                                      | `Service_Create` / `Microsoft.DocumentDB.ServiceResourceCreateUpdateParameters`                                                        | `Microsoft.DocumentDB.ServiceResource`                          |
| <a id="s-96312c7f7482dee6"></a>`96312c7f7482dee6` [Microsoft.DocumentDB.SqlResources.createUpdateSqlDatabase](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/SqlDatabaseGetResults.tsp#L56)                                                                   | `SqlResources_CreateUpdateSqlDatabase` / `Microsoft.DocumentDB.SqlDatabaseCreateUpdateParameters`                                      | `Microsoft.DocumentDB.SqlDatabaseGetResults`                    |
| <a id="s-1791c6f4e0e03cdd"></a>`1791c6f4e0e03cdd` [Microsoft.DocumentDB.ClientEncryptionKeyGetResultsOperationGroup.createUpdateClientEncryptionKey](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ClientEncryptionKeyGetResults.tsp#L40)                    | `SqlResources_CreateUpdateClientEncryptionKey` / `Microsoft.DocumentDB.ClientEncryptionKeyCreateUpdateParameters`                      | `Microsoft.DocumentDB.ClientEncryptionKeyGetResults`            |
| <a id="s-b6ece0a02adea3f4"></a>`b6ece0a02adea3f4` [Microsoft.DocumentDB.SqlContainerGetResultsOperationGroup.createUpdateSqlContainer](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/SqlContainerGetResults.tsp#L56)                                         | `SqlResources_CreateUpdateSqlContainer` / `Microsoft.DocumentDB.SqlContainerCreateUpdateParameters`                                    | `Microsoft.DocumentDB.SqlContainerGetResults`                   |
| <a id="s-8912a41b13e3d2a4"></a>`8912a41b13e3d2a4` [Microsoft.DocumentDB.SqlStoredProcedureGetResultsOperationGroup.createUpdateSqlStoredProcedure](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/SqlStoredProcedureGetResults.tsp#L55)                       | `SqlResources_CreateUpdateSqlStoredProcedure` / `Microsoft.DocumentDB.SqlStoredProcedureCreateUpdateParameters`                        | `Microsoft.DocumentDB.SqlStoredProcedureGetResults`             |
| <a id="s-6aca430f0e23eff2"></a>`6aca430f0e23eff2` [Microsoft.DocumentDB.SqlResourcesThroughputSettingsGetResultsOperationGroup.updateSqlContainerThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L211)            | `SqlResources_UpdateSqlContainerThroughput` / `Microsoft.DocumentDB.ThroughputSettingsUpdateParameters`                                | `Microsoft.DocumentDB.ThroughputSettingsGetResults`             |
| <a id="s-4750b61aaceacad3"></a>`4750b61aaceacad3` [Microsoft.DocumentDB.SqlTriggerGetResultsOperationGroup.createUpdateSqlTrigger](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/SqlTriggerGetResults.tsp#L55)                                               | `SqlResources_CreateUpdateSqlTrigger` / `Microsoft.DocumentDB.SqlTriggerCreateUpdateParameters`                                        | `Microsoft.DocumentDB.SqlTriggerGetResults`                     |
| <a id="s-07ac7618e0649bfa"></a>`07ac7618e0649bfa` [Microsoft.DocumentDB.SqlUserDefinedFunctionGetResultsOperationGroup.createUpdateSqlUserDefinedFunction](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/SqlUserDefinedFunctionGetResults.tsp#L55)           | `SqlResources_CreateUpdateSqlUserDefinedFunction` / `Microsoft.DocumentDB.SqlUserDefinedFunctionCreateUpdateParameters`                | `Microsoft.DocumentDB.SqlUserDefinedFunctionGetResults`         |
| <a id="s-930b038191c584c7"></a>`930b038191c584c7` [Microsoft.DocumentDB.ThroughputSettingsGetResultsOperationGroup.updateSqlDatabaseThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L90)                          | `SqlResources_UpdateSqlDatabaseThroughput` / `Microsoft.DocumentDB.ThroughputSettingsUpdateParameters`                                 | `Microsoft.DocumentDB.ThroughputSettingsGetResults`             |
| <a id="s-f641eeeeb54bb1b8"></a>`f641eeeeb54bb1b8` [Microsoft.DocumentDB.SqlRoleAssignmentGetResultsOperationGroup.createUpdateSqlRoleAssignment](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/SqlRoleAssignmentGetResults.tsp#L42)                          | `SqlResources_CreateUpdateSqlRoleAssignment` / `Microsoft.DocumentDB.SqlRoleAssignmentCreateUpdateParameters`                          | `Microsoft.DocumentDB.SqlRoleAssignmentGetResults`              |
| <a id="s-c7633b5ddecf0ded"></a>`c7633b5ddecf0ded` [Microsoft.DocumentDB.SqlRoleDefinitionGetResultsOperationGroup.createUpdateSqlRoleDefinition](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/SqlRoleDefinitionGetResults.tsp#L42)                          | `SqlResources_CreateUpdateSqlRoleDefinition` / `Microsoft.DocumentDB.SqlRoleDefinitionCreateUpdateParameters`                          | `Microsoft.DocumentDB.SqlRoleDefinitionGetResults`              |
| <a id="s-70eb76d13df9cb4a"></a>`70eb76d13df9cb4a` [Microsoft.DocumentDB.TableGetResultsOperationGroup.createUpdateTable](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/TableGetResults.tsp#L54)                                                              | `TableResources_CreateUpdateTable` / `Microsoft.DocumentDB.TableCreateUpdateParameters`                                                | `Microsoft.DocumentDB.TableGetResults`                          |
| <a id="s-9d0e513b8b2001e3"></a>`9d0e513b8b2001e3` [Microsoft.DocumentDB.TableResources.updateTableThroughput](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/ThroughputSettingsGetResults.tsp#L566)                                                           | `TableResources_UpdateTableThroughput` / `Microsoft.DocumentDB.ThroughputSettingsUpdateParameters`                                     | `Microsoft.DocumentDB.ThroughputSettingsGetResults`             |
| <a id="s-f4b6d787dec42d61"></a>`f4b6d787dec42d61` [Microsoft.DataFactory.PrivateEndpointConnectionResources.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/datafactory/resource-manager/Microsoft.DataFactory/DataFactory/PrivateEndpointConnectionResource.tsp#L54)                                     | `PrivateEndpointConnection_CreateOrUpdate` / `Microsoft.DataFactory.PrivateLinkConnectionApprovalRequestResource`                      | `Microsoft.DataFactory.PrivateEndpointConnectionResource`       |
| <a id="s-a8fe35091a27ad02"></a>`a8fe35091a27ad02` [Microsoft.AAD.OuContainers.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/domainservices/resource-manager/Microsoft.AAD/DomainServices/OuContainer.tsp#L58)                                                                                                   | `OuContainer_Create` / `Microsoft.AAD.ContainerAccount`                                                                                | `Microsoft.AAD.OuContainer`                                     |
| <a id="s-c4bcc152bcc2531b"></a>`c4bcc152bcc2531b` [Microsoft.HDInsight.Clusters.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/Cluster.tsp#L50)                                                                                                         | `Clusters_Create` / `Microsoft.HDInsight.ClusterCreateParametersExtended`                                                              | `Microsoft.HDInsight.Cluster`                                   |
| <a id="s-1eade2d50db1582c"></a>`1eade2d50db1582c` [Microsoft.HealthcareApis.PrivateEndpointConnectionDescriptions.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis/PrivateEndpointConnectionDescription.tsp#L69)                   | `PrivateEndpointConnections_CreateOrUpdate` / `Azure.ResourceManager.CommonTypes.PrivateEndpointConnection`                            | `Microsoft.HealthcareApis.PrivateEndpointConnectionDescription` |
| <a id="s-b0f7e5d05992ba29"></a>`b0f7e5d05992ba29` [Microsoft.HorizonDb.HorizonDbAdministrators.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb/routes.tsp#L245)                                                                                  | `HorizonDbAdministrators_CreateOrUpdate` / `Microsoft.HorizonDb.HorizonDbAdministratorAdd`                                             | `Microsoft.HorizonDb.HorizonDbAdministrator`                    |
| <a id="s-ae4b3b99a94936b7"></a>`ae4b3b99a94936b7` [Microsoft.Devices.EventHubConsumerGroupInfos.createEventHubConsumerGroup](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/iothub/resource-manager/Microsoft.Devices/IoTHub/EventHubConsumerGroupInfo.tsp#L69)                                                          | `IotHubResource_CreateEventHubConsumerGroup` / `Microsoft.Devices.EventHubConsumerGroupBodyDescription`                                | `Microsoft.Devices.EventHubConsumerGroupInfo`                   |
| <a id="s-d06c8a5fb5f17afe"></a>`d06c8a5fb5f17afe` [Microsoft.KeyVault.ManagedHsmKeys.createIfNotExist](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/ManagedHsmKey.tsp#L77)                                                                                       | `ManagedHsmKeys_CreateIfNotExist` / `Microsoft.KeyVault.ManagedHsmKeyCreateParameters`                                                 | `Microsoft.KeyVault.ManagedHsmKey`                              |
| <a id="s-3aad4a135b0bb0b0"></a>`3aad4a135b0bb0b0` [Microsoft.KeyVault.Vaults.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/Vault.tsp#L77)                                                                                                         | `Vaults_CreateOrUpdate` / `Microsoft.KeyVault.VaultCreateOrUpdateParameters`                                                           | `Microsoft.KeyVault.Vault`                                      |
| <a id="s-f1556d52484cec77"></a>`f1556d52484cec77` [Microsoft.KeyVault.Keys.createIfNotExist](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/Key.tsp#L79)                                                                                                           | `Keys_CreateIfNotExist` / `Microsoft.KeyVault.KeyCreateParameters`                                                                     | `Microsoft.KeyVault.Key`                                        |
| <a id="s-298528f12f334db4"></a>`298528f12f334db4` [Microsoft.KeyVault.Secrets.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/Secret.tsp#L54)                                                                                                       | `Secrets_CreateOrUpdate` / `Microsoft.KeyVault.SecretCreateOrUpdateParameters`                                                         | `Microsoft.KeyVault.Secret`                                     |
| <a id="s-b1a1905f0462b79f"></a>`b1a1905f0462b79f` [Microsoft.Management.ManagementGroups.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/management/resource-manager/Microsoft.Management/ManagementGroups/ManagementGroup.tsp#L81)                                                                       | `ManagementGroups_CreateOrUpdate` / `Microsoft.Management.CreateManagementGroupRequest`                                                | `Microsoft.Management.ManagementGroup`                          |
| <a id="s-126288d94fda2339"></a>`126288d94fda2339` [Microsoft.Management.HierarchySettingsOperationGroup.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/management/resource-manager/Microsoft.Management/ManagementGroups/HierarchySettings.tsp#L42)                                                      | `HierarchySettings_CreateOrUpdate` / `Microsoft.Management.CreateOrUpdateSettingsRequest`                                              | `Microsoft.Management.HierarchySettings`                        |
| <a id="s-4c27ca3deee1ed60"></a>`4c27ca3deee1ed60` [Nginx.NginxPlus.NginxDeploymentApiKeyResponses.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/nginx/resource-manager/Nginx.NginxPlus/NginxPlus/NginxDeploymentApiKeyResponse.tsp#L38)                                                                 | `ApiKeys_CreateOrUpdate` / `Nginx.NginxPlus.NginxDeploymentApiKeyRequest`                                                              | `Nginx.NginxPlus.NginxDeploymentApiKeyResponse`                 |
| <a id="s-99a575bc062d01ad"></a>`99a575bc062d01ad` [Nginx.NginxPlus.NginxConfigurationResponses.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/nginx/resource-manager/Nginx.NginxPlus/NginxPlus/NginxConfigurationResponse.tsp#L38)                                                                       | `Configurations_CreateOrUpdate` / `Nginx.NginxPlus.NginxConfigurationRequest`                                                          | `Nginx.NginxPlus.NginxConfigurationResponse`                    |
| <a id="s-3c1e17ac0515bb56"></a>`3c1e17ac0515bb56` [Microsoft.RecoveryServices.Alerts.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/Alert.tsp#L47)                                                                         | `ReplicationAlertSettings_Create` / `Microsoft.RecoveryServices.ConfigureAlertRequest`                                                 | `Microsoft.RecoveryServices.Alert`                              |
| <a id="s-8dafe16a2ac4742a"></a>`8dafe16a2ac4742a` [Microsoft.RecoveryServices.Fabrics.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/Fabric.tsp#L87)                                                                       | `ReplicationFabrics_Create` / `Microsoft.RecoveryServices.FabricCreationInput`                                                         | `Microsoft.RecoveryServices.Fabric`                             |
| <a id="s-c5f7e94acda9528b"></a>`c5f7e94acda9528b` [Microsoft.RecoveryServices.NetworkMappings.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/NetworkMapping.tsp#L48)                                                       | `ReplicationNetworkMappings_Create` / `Microsoft.RecoveryServices.CreateNetworkMappingInput`                                           | `Microsoft.RecoveryServices.NetworkMapping`                     |
| <a id="s-b8222c99a4d012f0"></a>`b8222c99a4d012f0` [Microsoft.RecoveryServices.ProtectionContainers.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/ProtectionContainer.tsp#L90)                                             | `ReplicationProtectionContainers_Create` / `Microsoft.RecoveryServices.CreateProtectionContainerInput`                                 | `Microsoft.RecoveryServices.ProtectionContainer`                |
| <a id="s-5da833899a6ca8b2"></a>`5da833899a6ca8b2` [Microsoft.RecoveryServices.MigrationItems.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/MigrationItem.tsp#L51)                                                         | `ReplicationMigrationItems_Create` / `Microsoft.RecoveryServices.EnableMigrationInput`                                                 | `Microsoft.RecoveryServices.MigrationItem`                      |
| <a id="s-9186ed7d0ea7376a"></a>`9186ed7d0ea7376a` [Microsoft.RecoveryServices.ReplicationProtectedItems.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/ReplicationProtectedItem.tsp#L95)                                   | `ReplicationProtectedItems_Create` / `Microsoft.RecoveryServices.EnableProtectionInput`                                                | `Microsoft.RecoveryServices.ReplicationProtectedItem`           |
| <a id="s-d4aba7de8272b75a"></a>`d4aba7de8272b75a` [Microsoft.RecoveryServices.ProtectionContainerMappings.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/ProtectionContainerMapping.tsp#L48)                               | `ReplicationProtectionContainerMappings_Create` / `Microsoft.RecoveryServices.CreateProtectionContainerMappingInput`                   | `Microsoft.RecoveryServices.ProtectionContainerMapping`         |
| <a id="s-b5e12b9d313dedda"></a>`b5e12b9d313dedda` [Microsoft.RecoveryServices.RecoveryServicesProviders.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/RecoveryServicesProvider.tsp#L58)                                   | `ReplicationRecoveryServicesProviders_Create` / `Microsoft.RecoveryServices.AddRecoveryServicesProviderInput`                          | `Microsoft.RecoveryServices.RecoveryServicesProvider`           |
| <a id="s-2e4017ed3d656c1e"></a>`2e4017ed3d656c1e` [Microsoft.RecoveryServices.StorageClassificationMappings.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/StorageClassificationMapping.tsp#L48)                           | `ReplicationStorageClassificationMappings_Create` / `Microsoft.RecoveryServices.StorageClassificationMappingInput`                     | `Microsoft.RecoveryServices.StorageClassificationMapping`       |
| <a id="s-d102de4d81cbd3ff"></a>`d102de4d81cbd3ff` [Microsoft.RecoveryServices.VCenters.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/VCenter.tsp#L49)                                                                     | `ReplicationvCenters_Create` / `Microsoft.RecoveryServices.AddVCenterRequest`                                                          | `Microsoft.RecoveryServices.VCenter`                            |
| <a id="s-2967e7ab465b206e"></a>`2967e7ab465b206e` [Microsoft.RecoveryServices.Policies.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/Policy.tsp#L46)                                                                      | `ReplicationPolicies_Create` / `Microsoft.RecoveryServices.CreatePolicyInput`                                                          | `Microsoft.RecoveryServices.Policy`                             |
| <a id="s-d210db784e52df68"></a>`d210db784e52df68` [Microsoft.RecoveryServices.ReplicationProtectionIntents.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/ReplicationProtectionIntent.tsp#L47)                             | `ReplicationProtectionIntents_Create` / `Microsoft.RecoveryServices.CreateProtectionIntentInput`                                       | `Microsoft.RecoveryServices.ReplicationProtectionIntent`        |
| <a id="s-bab564cfa3acb771"></a>`bab564cfa3acb771` [Microsoft.RecoveryServices.RecoveryPlans.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/RecoveryPlan.tsp#L50)                                                           | `ReplicationRecoveryPlans_Create` / `Microsoft.RecoveryServices.CreateRecoveryPlanInput`                                               | `Microsoft.RecoveryServices.RecoveryPlan`                       |
| <a id="s-1d9ac6271df17676"></a>`1d9ac6271df17676` [Microsoft.RecoveryServices.VaultSettings.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/VaultSetting.tsp#L65)                                                           | `ReplicationVaultSetting_Create` / `Microsoft.RecoveryServices.VaultSettingCreationInput`                                              | `Microsoft.RecoveryServices.VaultSetting`                       |
| <a id="s-ee92b9b2ca843418"></a>`ee92b9b2ca843418` [Microsoft.Cache.RedisResources.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/redis/resource-manager/Microsoft.Cache/Redis/RedisResource.tsp#L60)                                                                                                             | `Redis_Create` / `Microsoft.Cache.RedisCreateParameters`                                                                               | `Microsoft.Cache.RedisResource`                                 |
| <a id="s-4c6b8f698e11f401"></a>`4c6b8f698e11f401` [Microsoft.Cache.LinkedServer.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/redis/resource-manager/Microsoft.Cache/Redis/RedisLinkedServerWithProperties.tsp#L63)                                                                                             | `LinkedServer_Create` / `Microsoft.Cache.RedisLinkedServerCreateParameters`                                                            | `Microsoft.Cache.RedisLinkedServerWithProperties`               |
| <a id="s-25128fd566ec6cae"></a>`25128fd566ec6cae` [Reservations.ReservationOrderResponses.purchase](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Reservations/ReservationOrderResponse.tsp#L58)                                                          | `ReservationOrder_Purchase` / `Reservations.PurchaseRequest`                                                                           | `Reservations.ReservationOrderResponse`                         |
| <a id="s-2539debec2183c88"></a>`2539debec2183c88` [Microsoft.Resources.DeploymentExtendedManagementGroup.createOrUpdateAtManagementGroupScope](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/resources/resource-manager/Microsoft.Resources/deployments/DeploymentExtended.tsp#L462)                                    | `Deployments_CreateOrUpdateAtManagementGroupScope` / `Microsoft.Resources.ScopedDeployment`                                            | `Microsoft.Resources.DeploymentExtended`                        |
| <a id="s-b65884ae28978e52"></a>`b65884ae28978e52` [Microsoft.Resources.DeploymentsExtendedTenant.createOrUpdateAtTenantScope](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/resources/resource-manager/Microsoft.Resources/deployments/DeploymentExtended.tsp#L264)                                                     | `Deployments_CreateOrUpdateAtTenantScope` / `Microsoft.Resources.ScopedDeployment`                                                     | `Microsoft.Resources.DeploymentExtended`                        |
| <a id="s-bcf447708adda74f"></a>`bcf447708adda74f` [Microsoft.Resources.DeploymentExtendedSubscriptionGroup.createOrUpdateAtSubscriptionScope](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/resources/resource-manager/Microsoft.Resources/deployments/DeploymentExtended.tsp#L654)                                     | `Deployments_CreateOrUpdateAtSubscriptionScope` / `Microsoft.Resources.Deployment`                                                     | `Microsoft.Resources.DeploymentExtended`                        |
| <a id="s-3970ba63ac56b905"></a>`3970ba63ac56b905` [Microsoft.Resources.DeploymentExtendedOperationGroup.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/resources/resource-manager/Microsoft.Resources/deployments/DeploymentExtended.tsp#L846)                                                           | `Deployments_CreateOrUpdate` / `Microsoft.Resources.Deployment`                                                                        | `Microsoft.Resources.DeploymentExtended`                        |
| <a id="s-cd90eaafa6e1243a"></a>`cd90eaafa6e1243a` [Microsoft.Resources.Deployments.createOrUpdateAtScope](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/resources/resource-manager/Microsoft.Resources/deployments/DeploymentExtended.tsp#L85)                                                                          | `Deployments_CreateOrUpdateAtScope` / `Microsoft.Resources.Deployment`                                                                 | `Microsoft.Resources.DeploymentExtended`                        |
| <a id="s-9ab25f6672013381"></a>`9ab25f6672013381` [AssessmentAPI.SecurityAssessmentResponses.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/security/resource-manager/Microsoft.Security/Security/AssessmentAPI/SecurityAssessmentResponse.tsp#L56)                                                      | `Assessments_CreateOrUpdate` / `AssessmentAPI.SecurityAssessment`                                                                      | `AssessmentAPI.SecurityAssessmentResponse`                      |
| <a id="s-8fcc4fed76afe960"></a>`8fcc4fed76afe960` [SensitivitySettingsAPI.GetSensitivitySettingsResponses.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/security/resource-manager/Microsoft.Security/Security/SensitivitySettingsAPI/GetSensitivitySettingsResponse.tsp#L48)                            | `SensitivitySettings_CreateOrUpdate` / `SensitivitySettingsAPI.UpdateSensitivitySettingsRequest`                                       | `SensitivitySettingsAPI.GetSensitivitySettingsResponse`         |
| <a id="s-5855bd5b6e6f7223"></a>`5855bd5b6e6f7223` [SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentBaselineRules.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI/RuleResults.tsp#L87)                       | `SqlVulnerabilityAssessmentBaselineRules_CreateOrUpdate` / `SqlVulnerabilityAssessmentsAPI.RuleResultsInput`                           | `SqlVulnerabilityAssessmentsAPI.RuleResults`                    |
| <a id="s-bc51ed864cff2a1f"></a>`bc51ed864cff2a1f` [Microsoft.SecurityInsights.EntityQueries.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/EntityQuery.tsp#L88)                                                            | `EntityQueries_CreateOrUpdate` / `Microsoft.SecurityInsights.CustomEntityQuery`                                                        | `Microsoft.SecurityInsights.EntityQuery`                        |
| <a id="s-46dff1947112b2f2"></a>`46dff1947112b2f2` [Microsoft.Sql.ManagedServerDnsAliases.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/sql/resource-manager/Microsoft.Sql/SQL/ManagedServerDnsAlias.tsp#L43)                                                                                            | `ManagedServerDnsAliases_CreateOrUpdate` / `Microsoft.Sql.ManagedServerDnsAliasCreation`                                               | `Microsoft.Sql.ManagedServerDnsAlias`                           |
| <a id="s-7970e6692438c123"></a>`7970e6692438c123` [Microsoft.Sql.ImportExportExtensionsOperationResults.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/sql/resource-manager/Microsoft.Sql/SQL/ImportExportExtensionsOperationResult.tsp#L50)                                                             | `DatabaseExtensions_CreateOrUpdate` / `Microsoft.Sql.DatabaseExtensions`                                                               | `Microsoft.Sql.ImportExportExtensionsOperationResult`           |
| <a id="s-25eb7ac0f78cc6ed"></a>`25eb7ac0f78cc6ed` [Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentBaselineSets.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/sql/resource-manager/Microsoft.Sql/SQL/DatabaseSqlVulnerabilityAssessmentBaselineSet.tsp#L81)                                             | `DatabaseSqlVulnerabilityAssessmentBaselines_CreateOrUpdate` / `Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentRuleBaselineListInput` | `Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentBaselineSet`   |
| <a id="s-64d8a1df7c00e65a"></a>`64d8a1df7c00e65a` [Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentRuleBaselines.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/sql/resource-manager/Microsoft.Sql/SQL/DatabaseSqlVulnerabilityAssessmentRuleBaseline.tsp#L84)                                           | `DatabaseSqlVulnerabilityAssessmentRuleBaselines_CreateOrUpdate` / `Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentRuleBaselineInput` | `Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentRuleBaseline`  |
| <a id="s-e672e41cbcb1cdde"></a>`e672e41cbcb1cdde` [Microsoft.Sql.SqlVulnerabilityAssessmentBaseline.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/sql/resource-manager/Microsoft.Sql/SQL/DatabaseSqlVulnerabilityAssessmentBaselineSet.tsp#L146)                                                        | `SqlVulnerabilityAssessmentBaselines_CreateOrUpdate` / `Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentRuleBaselineListInput`         | `Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentBaselineSet`   |
| <a id="s-85b0d6fa43cfaf1a"></a>`85b0d6fa43cfaf1a` [Microsoft.Sql.SqlVulnerabilityAssessmentRuleBaseline.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/sql/resource-manager/Microsoft.Sql/SQL/DatabaseSqlVulnerabilityAssessmentRuleBaseline.tsp#L159)                                                   | `SqlVulnerabilityAssessmentRuleBaseline_CreateOrUpdate` / `Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentRuleBaselineInput`          | `Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentRuleBaseline`  |
| <a id="s-fe9a0a8beddfb98f"></a>`fe9a0a8beddfb98f` [Microsoft.Storage.StorageAccounts.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/storage/resource-manager/Microsoft.Storage/Storage/StorageAccount.tsp#L111)                                                                                                  | `StorageAccounts_Create` / `Microsoft.Storage.StorageAccountCreateParameters`                                                          | `Microsoft.Storage.StorageAccount`                              |
| <a id="s-a93ba334f29ff387"></a>`a93ba334f29ff387` [Microsoft.StorageSync.StorageSyncServices.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/StorageSyncService.tsp#L52)                                                                           | `StorageSyncServices_Create` / `Microsoft.StorageSync.StorageSyncServiceCreateParameters`                                              | `Microsoft.StorageSync.StorageSyncService`                      |
| <a id="s-2fd98161d8adcfd3"></a>`2fd98161d8adcfd3` [Microsoft.StorageSync.RegisteredServers.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/RegisteredServer.tsp#L54)                                                                               | `RegisteredServers_Create` / `Microsoft.StorageSync.RegisteredServerCreateParameters`                                                  | `Microsoft.StorageSync.RegisteredServer`                        |
| <a id="s-9beeadcf7b7fa3a0"></a>`9beeadcf7b7fa3a0` [Microsoft.StorageSync.SyncGroups.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/SyncGroup.tsp#L51)                                                                                             | `SyncGroups_Create` / `Microsoft.StorageSync.SyncGroupCreateParameters`                                                                | `Microsoft.StorageSync.SyncGroup`                               |
| <a id="s-c66d4b452c9ef375"></a>`c66d4b452c9ef375` [Microsoft.StorageSync.CloudEndpoints.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/CloudEndpoint.tsp#L55)                                                                                     | `CloudEndpoints_Create` / `Microsoft.StorageSync.CloudEndpointCreateParameters`                                                        | `Microsoft.StorageSync.CloudEndpoint`                           |
| <a id="s-5347141e830697b7"></a>`5347141e830697b7` [Microsoft.StorageSync.ServerEndpoints.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/ServerEndpoint.tsp#L53)                                                                                   | `ServerEndpoints_Create` / `Microsoft.StorageSync.ServerEndpointCreateParameters`                                                      | `Microsoft.StorageSync.ServerEndpoint`                          |
| <a id="s-e61cca263ccff3b7"></a>`e61cca263ccff3b7` [Microsoft.Subscription.SubscriptionAliasResponses.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/SubscriptionAliasResponse.tsp#L40)                                                         | `Alias_Create` / `Microsoft.Subscription.PutAliasRequest`                                                                              | `Microsoft.Subscription.SubscriptionAliasResponse`              |
| <a id="s-9fb05cc3244469f8"></a>`9fb05cc3244469f8` [Microsoft.Subscription.GetTenantPolicyResponses.addUpdatePolicyForTenant](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/GetTenantPolicyResponse.tsp#L43)                                           | `SubscriptionPolicy_AddUpdatePolicyForTenant` / `Microsoft.Subscription.PutTenantPolicyRequestProperties`                              | `Microsoft.Subscription.GetTenantPolicyResponse`                |
| <a id="s-09326584113e2a3a"></a>`09326584113e2a3a` [Microsoft.Subscription.TargetDirectoryResults.putTargetDirectory](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/TargetDirectoryResult.tsp#L51)                                                     | `Subscriptions_PutTargetDirectory` / `Microsoft.Subscription.TargetDirectoryRequest`                                                   | `Microsoft.Subscription.TargetDirectoryResult`                  |
| <a id="s-4cd8762330aa680c"></a>`4cd8762330aa680c` [Microsoft.Web.MSDeployStatuses.createMSDeployOperation](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/MSDeployStatus.tsp#L82)                                                                                          | `WebApps_CreateMSDeployOperation` / `Microsoft.Web.MSDeploy`                                                                           | `Microsoft.Web.MSDeployStatus`                                  |
| <a id="s-1dfddeaf18be16cd"></a>`1dfddeaf18be16cd` [Microsoft.Web.MSDeployStatusOperationGroup.createInstanceMSDeployOperation](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/MSDeployStatus.tsp#L161)                                                                     | `WebApps_CreateInstanceMSDeployOperation` / `Microsoft.Web.MSDeploy`                                                                   | `Microsoft.Web.MSDeployStatus`                                  |
| <a id="s-93a320df959a9968"></a>`93a320df959a9968` [Microsoft.Web.MSDeployStatusSlotOperationGroup.createMSDeployOperationSlot](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/MSDeployStatus.tsp#L239)                                                                     | `WebApps_CreateMSDeployOperationSlot` / `Microsoft.Web.MSDeploy`                                                                       | `Microsoft.Web.MSDeployStatus`                                  |
| <a id="s-e1629ee96cac1c89"></a>`e1629ee96cac1c89` [Microsoft.Web.InstanceMSDeployStatusOperationGroup.createInstanceMSDeployOperationSlot](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/MSDeployStatus.tsp#L324)                                                         | `WebApps_CreateInstanceMSDeployOperationSlot` / `Microsoft.Web.MSDeploy`                                                               | `Microsoft.Web.MSDeployStatus`                                  |
| <a id="s-e5d6f2c465883792"></a>`e5d6f2c465883792` [Microsoft.Web.StaticSiteCustomDomainOverviewARMResources.createOrUpdateStaticSiteCustomDomain](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/StaticSiteCustomDomainOverviewARMResource.tsp#L54)                        | `StaticSites_CreateOrUpdateStaticSiteCustomDomain` / `Microsoft.Web.StaticSiteCustomDomainRequestPropertiesARMResource`                | `Microsoft.Web.StaticSiteCustomDomainOverviewARMResource`       |

## Code-backed representatives

These are verbatim excerpts of the pinned authored source, not invented or standalone compiling fixtures. The per-target entries above retain all other instances; existing broader controls and examples remain in [evidence-details.md](evidence-details.md#exact-source-examples).

### Resolved: registered PUT absent from retained operation map

**Project/API version:** `specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement` / `2025-09-01-preview`.
**Source:** [Microsoft.ApiManagement.ApiContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/ApiContract.tsp#L93), lines 91-123.

**TypeSpec source**

```typespec
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
            /**
             * Current entity state version. Should be treated as opaque and used to make conditional HTTP requests.
             */
            @header("ETag")
            eTag: string;
          })
      | (ArmResourceCreatedResponse<
          ApiContract,
          LroHeaders = ArmCombinedLroHeaders<FinalResult = ApiContract>
        > & {
          /**
           * Current entity state version. Should be treated as opaque and used to make conditional HTTP requests.
           */
          @header("ETag")
          eTag: string;
        })
  >;
```

**Emitted Swagger schema excerpt / version-scope evidence**

```json
{
  "put": {
    "operationId": "Api_CreateOrUpdate",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/ApiContract"
        }
      },
      "201": {
        "schema": {
          "$ref": "#/definitions/ApiContract"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/ApiCreateOrUpdateParameter"
        }
      }
    ]
  }
}
```

**Observed comparison / disposition:** The singular retained map loses this operation, but the append-only registered-resource operation Set retains its createOrUpdate identifier and canonical selected response. The implemented fix applies the existing request predicate through that Set, without a broad PUT listener or registry redesign. Swagger remains at 1 raw observation; the final-source TypeSpec run now reports 1 corresponding requestMismatch, compared with 0 before the fix.

### Resolved: PUT stored under lists rather than lifecycle.createOrUpdate

**Project/API version:** `specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement` / `2025-09-01-preview`.
**Source:** [Microsoft.ApiManagement.TagDescriptionContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagDescriptionContract.tsp#L102), lines 100-128.

**TypeSpec source**

```typespec
   * Create/Update tag description in scope of the Api.
   */
  createOrUpdate is TagDescriptionContractsOps.CreateOrUpdateSync<
    TagDescriptionContract,
    Request = TagDescriptionCreateParameters,
    Parameters = {
      /**
       * ETag of the Entity. Not required when creating an entity, but required when updating an entity.
       */
      #suppress "@azure-tools/typespec-azure-core/casing-style" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
      @header("If-Match")
      `If-Match`?: string;
    },
    Response =
      | (ArmResponse<TagDescriptionContract> & {
          /**
           * Current entity state version. Should be treated as opaque and used to make conditional HTTP requests.
           */
          @header("ETag")
          eTag: string;
        })
      | (ArmCreatedResponse<TagDescriptionContract> & {
          /**
           * Current entity state version. Should be treated as opaque and used to make conditional HTTP requests.
           */
          @header("ETag")
          eTag: string;
        })
  >;
```

**Emitted Swagger schema excerpt / version-scope evidence**

```json
{
  "put": {
    "operationId": "ApiTagDescription_CreateOrUpdate",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/TagDescriptionContract"
        }
      },
      "201": {
        "schema": {
          "$ref": "#/definitions/TagDescriptionContract"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/TagDescriptionCreateParameters"
        }
      }
    ]
  }
}
```

**Observed comparison / disposition:** The legacy PUT is retained under lists and also in the registered-resource operation Set as createOrUpdate. The implemented Set-based request traversal reaches it while preserving action, compliant, multipart and suppression controls. Swagger remains at 1 raw observation; the final-source TypeSpec run now reports 1 corresponding requestMismatch, compared with 0 before the fix.

### New warning compares FunctionEnvelope to a KeyInfo wire contract

**Project/API version:** `specification/web/resource-manager/Microsoft.Web/AppService` / `2026-07-15`.
**Source:** [Microsoft.Web.FunctionEnvelopeOperationGroup.createOrUpdateFunctionSecretSlot](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/FunctionEnvelope.tsp#L350-L355), lines 350-355.

**TypeSpec source**

```typespec
  createOrUpdateFunctionSecretSlot is FunctionEnvelopeSlotOperationGroupOps.CreateOrUpdateAsync<
    FunctionEnvelope,
    Request = KeyInfo,
    Response = ArmResponse<KeyInfo> | ArmResourceCreatedSyncResponse<KeyInfo>,
    OverrideErrorType = DefaultErrorResponse
  >;
```

**Emitted Swagger schema excerpt / version-scope evidence**

```json
{
  "put": {
    "operationId": "WebApps_CreateOrUpdateFunctionSecretSlot",
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/KeyInfo"
        }
      }
    ],
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/KeyInfo"
        }
      },
      "201": {
        "schema": {
          "$ref": "#/definitions/KeyInfo"
        }
      }
    }
  }
}
```

**Observed comparison / disposition:** The Swagger request/response member reports zero: both payloads reference KeyInfo. Its XmsResourceInPutResponse finding is a separate missing-marker check. The final-source TypeSpec run adds one requestMismatch comparing KeyInfo to the registered FunctionEnvelope argument, not to the actual response. This warning is neither request/response correspondence nor marker coverage. Review the legacy resource association with the service owner before a wire-equivalent modeling correction; do not change the KeyInfo contract or weaken the shared predicate merely to equalize counts.

### New source-only warning on a removed operation sharing the replacement route

**Project/API version:** `specification/cdn/resource-manager/Microsoft.Cdn/Cdn` / `2026-08-01-preview`.
**Source:** [Microsoft.Cdn.RuleSets.createV1 and its replacement](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/RuleSet.tsp#L39-L59), lines 39-48.

**TypeSpec source**

```typespec
  @removed(Versions.v2025_12_01)
  @renamedFrom(Versions.v2025_12_01, "create")
  @sharedRoute
  @put
  createV1 is Azure.ResourceManager.Legacy.CreateOrUpdateAsync<
    RuleSet,
    void,
    Response = ArmResponse<RuleSet> | ArmCreatedResponse<RuleSet>,
    Error = ErrorResponse
  >;
```

**Emitted Swagger schema excerpt / version-scope evidence**

```json
{
  "put": {
    "operationId": "RuleSets_Create",
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/RuleSet"
        }
      }
    ],
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/RuleSet"
        }
      },
      "201": {
        "schema": {
          "$ref": "#/definitions/RuleSet"
        }
      }
    }
  }
}
```

**Observed comparison / disposition:** The final-source TypeSpec run adds one missingRequest on createV1, removed at 2025-12-01. It has no selected-version operation counterpart. The current Swagger reuses that route for create, added at 2025-12-01 with an optional RuleSet body; its payload is not the old void request. Thus no selected-version Swagger comparison exists for createV1, even though a replacement operation occupies the same route. Retain the source warning and use version-aligned comparison for selected-version parity; do not infer identity from the route or suppress the warning to balance counts.

### Matched request and canonical response resource

**Project/API version:** `specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement` / `2025-09-01-preview`.
**Source:** [Microsoft.ApiManagement.IdentityProviderContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/IdentityProviderContract.tsp#L62), lines 60-88.

**TypeSpec source**

```typespec
   * Creates or Updates the IdentityProvider configuration.
   */
  createOrUpdate is Azure.ResourceManager.Legacy.CreateOrUpdateSync<
    IdentityProviderContract,
    Request = IdentityProviderCreateContract,
    Parameters = {
      /**
       * ETag of the Entity. Not required when creating an entity, but required when updating an entity.
       */
      #suppress "@azure-tools/typespec-azure-core/casing-style" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
      @header("If-Match")
      `If-Match`?: string;
    },
    Response =
      | (ArmResponse<IdentityProviderContract> & {
          /**
           * Current entity state version. Should be treated as opaque and used to make conditional HTTP requests.
           */
          @header("ETag")
          eTag?: string;
        })
      | (ArmResourceCreatedSyncResponse<IdentityProviderContract> & {
          /**
           * Current entity state version. Should be treated as opaque and used to make conditional HTTP requests.
           */
          @header("ETag")
          eTag?: string;
        })
  >;
```

**Emitted Swagger schema excerpt / version-scope evidence**

```json
{
  "put": {
    "operationId": "IdentityProvider_CreateOrUpdate",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/IdentityProviderContract"
        }
      },
      "201": {
        "schema": {
          "$ref": "#/definitions/IdentityProviderContract"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/IdentityProviderCreateContract"
        }
      }
    ]
  }
}
```

**Observed comparison / disposition:** Swagger reports one request-schema finding. TypeSpec reports requestMismatch on the same PUT; its canonical resource is the selected response body. No rule change is needed for this observed pairing, but this is not universal structural-equivalence proof.

### Warning on the same operation compares a different contract

**Project/API version:** `specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement` / `2025-09-01-preview`.
**Source:** [Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/PrivateEndpointConnection.tsp#L29), lines 27-44.

**TypeSpec source**

```typespec
   */
  #suppress "@azure-tools/typespec-azure-resource-manager/arm-put-operation-response-codes" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  createOrUpdate is Azure.ResourceManager.Legacy.CreateOrUpdateAsync<
    ApiManagementServiceResource,
    Request = PrivateEndpointConnectionRequest,
    Response =
      | ArmResourceUpdatedResponse<Azure.ResourceManager.CommonTypes.PrivateEndpointConnection>
      | ArmAcceptedLroResponse<LroHeaders = ArmLroLocationHeader<FinalResult = PrivateEndpointConnection> &
          Azure.Core.Foundations.RetryAfterHeader>,
    Parameters = {
      /**
       * API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
       */
      @path
      @segment("privateEndpointConnections")
      privateEndpointConnectionName: string;
    }
  >;
```

**Emitted Swagger schema excerpt / version-scope evidence**

```json
{
  "put": {
    "operationId": "PrivateEndpointConnection_CreateOrUpdate",
    "responses": {
      "200": {
        "schema": {
          "$ref": "../../../../../../../../../common-types/resource-management/v5/privatelinks.json#/definitions/PrivateEndpointConnection"
        }
      },
      "202": {}
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/PrivateEndpointConnectionRequest"
        }
      }
    ]
  }
}
```

**Observed comparison / disposition:** The current warning compares PrivateEndpointConnectionRequest to the parent ApiManagementServiceResource, while the actual 200 body is CommonTypes.PrivateEndpointConnection. Review the legacy template's parent/child modeling before adding an equality warning or changing source contracts. The existing warning is not equivalent coverage. Swagger: 1 raw observation; TypeSpec: 1 same-operation finding, 0 credited.

### Unassociated PUT with no registered response model

**Project/API version:** `specification/network/resource-manager/Microsoft.Network/Network/Network` / `2026-03-01`.
**Source:** [Microsoft.Network.ConnectionMonitorResults.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/network/resource-manager/Microsoft.Network/Network/Network/ConnectionMonitorResult.tsp#L56), lines 54-67.

**TypeSpec source**

```typespec
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

**Emitted Swagger schema excerpt / version-scope evidence**

```json
{
  "put": {
    "operationId": "ConnectionMonitors_CreateOrUpdate",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/ConnectionMonitorResult"
        }
      },
      "201": {
        "schema": {
          "$ref": "#/definitions/ConnectionMonitorResult"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/ConnectionMonitor"
        }
      }
    ]
  }
}
```

**Observed comparison / disposition:** ConnectionMonitor and ConnectionMonitorResult are different body-bearing DTOs, but inheritance from an ARM-shaped base does not establish a registered canonical resource. Review the legacy contract, read-only result fields and model registration; do not broaden the resource listener to every PUT or introduce recursive emitted-schema equality for this case. Sixteen repeated raw observations represent one checked PUT. TypeSpec: 0 corresponding findings.

### Canonical request is accepted while selected 200 has no schema

**Project/API version:** `specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace` / `2025-01-01`.
**Source:** [Microsoft.Marketplace.PrivateStores.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace/PrivateStore.tsp#L43), lines 41-49.

**TypeSpec source**

```typespec
  #suppress "@azure-tools/typespec-azure-resource-manager/arm-put-operation-response-codes" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  #suppress "@azure-tools/typespec-azure-resource-manager/no-response-body" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  createOrUpdate is Azure.ResourceManager.Legacy.CreateOrReplaceSync<
    PrivateStore,
    BaseParameters = Azure.ResourceManager.Foundations.TenantBaseParameters,
    Response = OkResponse,
    Error = ErrorResponse,
    OptionalRequestBody = true
  >;
```

**Emitted Swagger schema excerpt / version-scope evidence**

```json
{
  "put": {
    "operationId": "PrivateStore_CreateOrUpdate",
    "responses": {
      "200": {}
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/PrivateStore"
        }
      }
    ]
  }
}
```

**Observed comparison / disposition:** The canonical request is valid for this rule; the selected 200 is empty. The existing no-response-body visitor diagnoses this exact operation when evaluated before suppression, and the source explicitly suppresses that owner. Review that suppression or repair the modeled/wire response, rather than adding a second schema-equality warning. Swagger: 1 raw observation; TypeSpec shared rule: 0 corresponding findings.

### Upstream staging object-identity false positive

**Project/API version:** `specification/durabletask/resource-manager/Microsoft.DurableTask/DurableTask` / `2026-05-01-preview`.
**Source:** [Microsoft.DurableTask.Schedulers.createOrUpdatePrivateEndpointConnection](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/durabletask/resource-manager/Microsoft.DurableTask/DurableTask/scheduler.tsp#L183), lines 181-183.

**TypeSpec source**

```typespec
  @added(Versions.v2026_02_01)
  @doc("Create or update a private endpoint connection for the durable task scheduler")
  createOrUpdatePrivateEndpointConnection is PrivateEndpointOperations.CreateOrUpdateAsync<Scheduler>;
```

**Emitted Swagger schema excerpt / version-scope evidence**

```json
{
  "put": {
    "operationId": "Schedulers_CreateOrUpdatePrivateEndpointConnection",
    "responses": {
      "200": {
        "schema": {
          "$ref": "../../../../../../../../../common-types/resource-management/v6/privatelinks.json#/definitions/PrivateEndpointConnection"
        }
      },
      "201": {
        "schema": {
          "$ref": "../../../../../../../../../common-types/resource-management/v6/privatelinks.json#/definitions/PrivateEndpointConnection"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "../../../../../../../../../common-types/resource-management/v6/privatelinks.json#/definitions/PrivateEndpointConnection"
        }
      }
    ]
  }
}
```

**Observed comparison / disposition:** Raw 200 and 201 references are identical in the same invoking document. The original uses !== on resolved JavaScript objects, not structural equality. This classification uses saved references and pinned code, not a newly captured resolver-object execution trace. No TypeSpec rule update required: intentionally do not reproduce the upstream identity bug. Swagger: 1 raw observation(s); TypeSpec: 0 same-operation finding(s), 0 credited.

### Genuine plain-response 200/201 mismatch

**Project/API version:** `specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota` / `2020-10-25`.
**Source:** [Quota.CurrentQuotaLimitBases.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/CurrentQuotaLimitBase.tsp#L71), lines 69-82.

**TypeSpec source**

```typespec
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

**Emitted Swagger schema excerpt / version-scope evidence**

```json
{
  "put": {
    "operationId": "Quota_CreateOrUpdate",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/CurrentQuotaLimitBase"
        }
      },
      "201": {
        "schema": {
          "$ref": "#/definitions/QuotaRequestSubmitResponse201"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/CurrentQuotaLimitBase"
        }
      }
    ]
  }
}
```

**Observed comparison / disposition:** Quota intentionally returns the quota resource at 200 and a submission-status envelope at 201, with the final LRO result separately set to the quota resource. The existing Azure Core response-schema-problem visitor detects the initial-payload difference before its explicit authored suppression. Recommend reviewing the legacy exception with that owner, not duplicating it in the ARM rule. Swagger: 1 raw observation; shared ARM rule: 0 corresponding findings.

### Selected PUT response lacks resource extension

**Project/API version:** `specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/AnalyticsItems` / `2015-05-01`.
**Source:** [AnalyticsItems.AnalyticsItemsOperationGroup.put](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/AnalyticsItems/routes.tsp#L95), lines 93-123.

**TypeSpec source**

```typespec
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

**Emitted Swagger schema excerpt / version-scope evidence**

```json
{
  "put": {
    "operationId": "AnalyticsItems_Put",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/ApplicationInsightsComponentAnalyticsItem"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/ApplicationInsightsComponentAnalyticsItem"
        }
      }
    ]
  }
}
```

**Observed comparison / disposition:** The selected AnalyticsItem lacks the emitted resource marker and is not a registered ARM resource. This is a missing independent policy, not proof that marking every custom PUT payload as a resource is correct. Recommend a separate source-level response-resource design with explicit custom/action boundaries and emitter-marker controls, rather than overloading canonical-resource identity. Swagger: 1 raw observation; TypeSpec: 0 corresponding findings.

### Cross-operation comparison includes an absent selected response reference

**Project/API version:** `specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement` / `2025-09-01-preview`.
**Source:** [Microsoft.ApiManagement.DelegationSettings.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/PortalDelegationSettings.tsp#L67), lines 65-78.

**TypeSpec source**

```typespec
  #suppress "@azure-tools/typespec-azure-resource-manager/arm-put-operation-response-codes" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  #deprecated "deprecated"
  createOrUpdate is ArmResourceCreateOrReplaceSync<
    PortalDelegationSettings,
    Parameters = {
      /**
       * ETag of the Entity. Not required when creating an entity, but required when updating an entity.
       */
      #suppress "@azure-tools/typespec-azure-core/casing-style" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
      @header("If-Match")
      `If-Match`?: string;
    },
    Response = ArmResourceUpdatedResponse<PortalDelegationSettings>
  >;
```

**Emitted Swagger schema excerpt / version-scope evidence**

```json
{
  "put": {
    "operationId": "DelegationSettings_CreateOrUpdate",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/PortalDelegationSettings"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/PortalDelegationSettings"
        }
      }
    ]
  },
  "get": {
    "operationId": "DelegationSettings_Get",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/PortalDelegationSettings"
        }
      }
    }
  },
  "patch": {
    "operationId": "DelegationSettings_Update",
    "responses": {},
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/PortalDelegationSettings"
        }
      }
    ]
  }
}
```

**Observed comparison / disposition:** DelegationSettings returns a resource for PUT/GET and correctly has no body at PATCH 204. Comparing its absent PATCH schema to that resource is a Swagger schema-comparison false positive, not evidence of a different resource model. Recommend not porting this comparison; no whole-operation compliance, approved retirement or new migration credit is claimed.

### Cross-operation comparison has distinct selected references

**Project/API version:** `specification/automation/resource-manager/Microsoft.Automation/Automation` / `2024-10-23`.
**Source:** [Microsoft.Automation.SourceControls.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/SourceControl.tsp#L105), lines 103-116.

**TypeSpec source**

```typespec
  @OpenAPI.externalDocs("http://aka.ms/azureautomationsdk/sourcecontrolsyncjoboperations")
  @put
  create is ArmResourceRead<
    SourceControl,
    BaseParameters = Azure.ResourceManager.Foundations.DefaultBaseParameters<SourceControl>,
    Response = ArmResourceCreatedSyncResponse<SourceControlSyncJob>,
    Parameters = SourceControlSyncJobIdParameter & {
      /**
       * The parameters supplied to the create source control sync job operation.
       */
      @body
      parameters: SourceControlSyncJobCreateParameters;
    }
  >;
```

**Emitted Swagger schema excerpt / version-scope evidence**

```json
{
  "put": {
    "operationId": "SourceControlSyncJob_Create",
    "responses": {
      "201": {
        "schema": {
          "$ref": "#/definitions/SourceControlSyncJob"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/SourceControlSyncJobCreateParameters"
        }
      }
    ]
  },
  "get": {
    "operationId": "SourceControlSyncJob_Get",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/SourceControlSyncJobById"
        }
      }
    }
  }
}
```

**Observed comparison / disposition:** SourceControlSyncJob and SourceControlSyncJobById genuinely differ: the PUT response includes read-only name/type/id, whereas GET has writable id, omits name/type and adds nested exception. Request spec-owner confirmation of the wire contract before sharing models. One observed route does not justify a general recursive cross-operation comparator; retain this as a known gap, not an alias false positive. Swagger: 1 raw observation; TypeSpec: 0 corresponding findings.

### Same PUT warning, but original selects empty 200 instead of 201

**Project/API version:** `specification/automation/resource-manager/Microsoft.Automation/Automation` / `2024-10-23`.
**Source:** [Microsoft.Automation.DscNodeConfigurations.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/DscNodeConfiguration.tsp#L45), lines 43-55.

**TypeSpec source**

```typespec
  #suppress "@azure-tools/typespec-azure-core/no-openapi" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  @OpenAPI.externalDocs("http://aka.ms/azureautomationsdk/dscnodeconfigurations")
  createOrUpdate is Azure.ResourceManager.Legacy.CreateOrUpdateAsync<
    DscNodeConfiguration,
    Request = DscNodeConfigurationCreateOrUpdateParameters,
    Response =
      | OkResponse
      | ArmResourceCreatedResponse<
          DscNodeConfiguration,
          ArmLroLocationHeader<FinalResult = DscNodeConfiguration> &
            Azure.Core.Foundations.RetryAfterHeader
        >
  >;
```

**Emitted Swagger schema excerpt / version-scope evidence**

```json
{
  "put": {
    "operationId": "DscNodeConfiguration_CreateOrUpdate",
    "responses": {
      "200": {},
      "201": {
        "schema": {
          "$ref": "#/definitions/DscNodeConfiguration"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/DscNodeConfigurationCreateOrUpdateParameters"
        }
      }
    ]
  }
}
```

**Observed comparison / disposition:** Swagger selects the empty 200, while this rule compares the request to the 201 resource; those findings are not equivalent. The existing no-response-body predicate separately diagnoses the empty 200 before the source's explicit suppression. Review the body-owner suppression/contract rather than adding status-specific equality solely for parity.

### additional-missing-request-policy

**Project/API version:** `specification/dns/resource-manager/Microsoft.Network/Dns` / `2023-07-01-preview`.
**Source:** [Microsoft.Network.DnssecConfigs.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/dns/resource-manager/Microsoft.Network/Dns/DnssecConfig.tsp#L45), lines 43-66.

**TypeSpec source**

```typespec
   * Creates or updates the DNSSEC configuration on a DNS zone.
   */
  createOrUpdate is Azure.ResourceManager.Legacy.CreateOrReplaceAsync<
    DnssecConfig,
    Request = void,
    Parameters = {
      /**
       * The etag of the DNSSEC configuration. Omit this value to always overwrite the DNSSEC configuration. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes.
       */
      #suppress "@azure-tools/typespec-azure-core/casing-style" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
      @header("If-Match")
      IfMatch?: string;

      /**
       * Set to '*' to allow this DNSSEC configuration to be created, but to prevent updating existing DNSSEC configuration. Other values will be ignored.
       */
      #suppress "@azure-tools/typespec-azure-core/casing-style" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
      @header("If-None-Match")
      IfNoneMatch?: string;
    },
    LroHeaders = ArmLroLocationHeader<FinalResult = DnssecConfig> &
      Azure.Core.Foundations.RetryAfterHeader,
    Error = CloudError
  >;
```

**Emitted Swagger schema excerpt / version-scope evidence**

```json
{
  "put": {
    "operationId": "DnssecConfigs_CreateOrUpdate",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/DnssecConfig"
        }
      },
      "201": {
        "schema": {
          "$ref": "#/definitions/DnssecConfig"
        }
      }
    }
  }
}
```

**Observed comparison / disposition:** The original skips missing request schemas; the TypeSpec linter reports missingRequest for void. This is additional policy, not member coverage. No TypeSpec rule change is required to explain the gap.

### source-only-operation-not-in-selected-version

**Project/API version:** `specification/batch/resource-manager/Microsoft.Batch/Batch` / `2025-06-01`.
**Source:** [Microsoft.Batch.Certificates.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/batch/resource-manager/Microsoft.Batch/Batch/Certificate.tsp#L69), lines 67-95.

**TypeSpec source**

```typespec
  #deprecated "Removal of feature"
  @removed(Versions.v2025_06_01)
  create is Azure.ResourceManager.Legacy.CreateOrReplaceAsync<
    Certificate,
    Request = CertificateCreateOrUpdateParameters,
    Parameters = {
      /**
       * The entity state (ETag) version of the certificate to update. A value of "*" can be used to apply the operation only if the certificate already exists. If omitted, this operation will always be applied.
       */
      #suppress "@azure-tools/typespec-azure-core/casing-style" "Legacy casing"
      @header("If-Match")
      `If-Match`?: string;

      /**
       * Set to '*' to allow a new certificate to be created, but to prevent updating an existing certificate. Other values will be ignored.
       */
      #suppress "@azure-tools/typespec-azure-core/casing-style" "Legacy casing"
      @header("If-None-Match")
      `If-None-Match`?: string;
    },
    Response = ArmResourceUpdatedResponse<Certificate> & {
      /**
       * The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Match or If-None-Match headers.
       */
      @header("ETag")
      etag?: string;
    },
    Error = CloudError
  >;
```

**Emitted Swagger schema excerpt / version-scope evidence**

```json
{
  "selectedApiVersion": "2025-06-01",
  "operationAbsentFromSelectedSwagger": true
}
```

**Observed comparison / disposition:** Batch Certificate is removed in the selected version and absent from Swagger. TypeSpec source compilation still reports requestMismatch. No emitted schema exists to compare; align projection rather than change the rule.

### additional-request-check-outside-swagger-200-201-selector

**Project/API version:** `specification/postgresql/DBforPostgreSQL.Management` / `2026-07-01-preview`.
**Source:** [Microsoft.DBforPostgreSQL.DbAgents.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/postgresql/DBforPostgreSQL.Management/routes.tsp#L184), lines 182-188.

**TypeSpec source**

```typespec
  @Azure.Core.useFinalStateVia("azure-async-operation")
  @put
  createOrUpdate is Legacy.CreateOrReplaceAsync<
    DbAgent,
    Request = DbAgentForUpdate,
    Response = DbAgentAcceptedResponse
  >;
```

**Emitted Swagger schema excerpt / version-scope evidence**

```json
{
  "put": {
    "operationId": "DBAgent_CreateOrUpdate",
    "responses": {
      "202": {
        "schema": {
          "$ref": "#/definitions/DbAgent"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/DbAgentForUpdate"
        }
      }
    ]
  }
}
```

**Observed comparison / disposition:** DbAgent has only a 202 success response. The original registration selects existing 200/201 responses, so it never invokes the request-comparison function here. TypeSpec requestMismatch is additional selector coverage; no rule change is required merely to explain it.

### Collection PUT resource versus GET list wrapper

**Project/API version:** `specification/sql/resource-manager/Microsoft.Sql/SQL` / `2026-08-01-preview`.
**Source:** [Microsoft.Sql.Servers.replace](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/sql/resource-manager/Microsoft.Sql/SQL/Server.tsp#L161), lines 160-165.

**TypeSpec source**

```typespec
  @Azure.ResourceManager.Legacy.feature(Features.FirewallRules)
  replace is ArmResourceActionSync<
    Server,
    FirewallRuleList,
    ArmResponse<FirewallRule> | AcceptedResponse
  >;
```

**Emitted Swagger schema excerpt / version-scope evidence**

```json
{
  "put": {
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/FirewallRule"
        }
      },
      "202": {}
    }
  },
  "get": {
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/FirewallRuleListResult"
        }
      }
    }
  }
}
```

**Observed comparison / disposition:** The collection PUT returns FirewallRule, while GET returns FirewallRuleListResult whose value array contains that exact same emitted FirewallRule definition. Different wrapper roles do not demonstrate different resource item models. Recommend not porting raw reference-name equality here; this is a reasoned policy recommendation, not approved retirement or migration credit.

## Reproduction and limits

The metadata-only inspection recompiled the 63-project union affected by either engine, concurrency two. All 63 succeeded, every saved finding was reproduced byte-for-field, and HTTP metadata produced zero diagnostics. The inspection did not modify specs or linter source and did not emit Swagger. The 424 no-finding projects remain in the successful 487-project corpus; they did not need another metadata compilation.

[Execution receipt](receipts/instance-inspection-20261105.json) retains timings, full-graph hashes/counts and equality checks. [Compact metadata](instance-inputs.json) retains every relevant operation and version counterpart without duplicating unrelated HTTP graphs. The [inspector](analysis/inspect-instance-targets.mjs) copies the candidate's actual response traversal, and the [runner](analysis/run-instance-inspection.py) injects it into the pinned worker without changing diagnostic selection.

Saved-evidence verification: `python analyze-instances.py --root .`, `python -m unittest test_instance_analysis.py test_reanalyze.py`, and `python reanalyze.py --verify-inventory`. `python render-instances.py --verify` checks the generated appendix/member prose, ignoring formatter whitespace; integrity.json verifies exact saved bytes. Fresh metadata reproduction additionally requires the pinned runtime/artifacts and original worker inputs documented in [evidence-details.md](evidence-details.md#read-recount-and-regenerate). The resolver accepts `--observations`, `--dataset`, `--output` and optional `--traces`; no CLI invocation regenerates Swagger.

The [migration report](migration.md) states the conclusion; [gap-analysis.md](gap-analysis.md) explains the recommended fixes, policy exceptions and unresolved contracts. This inventory does not turn unpaired findings into proven defects or prospective fixes into observed coverage.

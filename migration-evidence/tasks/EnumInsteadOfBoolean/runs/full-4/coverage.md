# Native TypeSpec coverage analysis

Validators: `EnumInsteadOfBoolean`
Native rules: `@azure-tools/typespec-azure-core/no-boolean`
Scope: `boolean-http`; partial: false.

**This is observed coverage, not an automatic equivalence decision.**
Primary counting unit: sum of raw member validator occurrences versus aligned native diagnostics, counted once.
Member-native attribution is unavailable. Test every member's semantics, including members with no observations.
Cross-validator overlap is not normalized. Equal source locations do not establish one actionable grouped violation.
JSON paths and source locations are different identity domains. One-sided projects and outliers require investigation.
Aligned diagnostics are source diagnostics filtered by locations in the selected-version HTTP graph, not a rerun of arbitrary rule predicates on a projected program.

| Measure | Value |
| --- | ---: |
| Selected / assessable projects | 487 / 487 |
| Unassessed projects | 0 |
| Validator / native / overlap projects | 313 / 312 / 312 |
| Observed validator-project coverage | 99.68051118210862 |
| Validator raw / file-independent paths | 8338 / 4269 |
| Native raw / aligned / source targets | 4823 / 4680 / 4174 |
| Native findings under project defaults | 0 |
| Validator excess / native excess | 95 / 0 |
| Raw validator excess / raw native excess (primary) | 4037 / 379 |

## Member observations (not member-native coverage)

- EnumInsteadOfBoolean: 8338 raw observations; completeness not determined.

## One-sided projects

- Validator only: `specification/security/resource-manager/Microsoft.Security/Security/BatchPricingsAPI`

## Unassessed projects


## Diagnostic outliers

| Project | Validator raw | Native aligned | Raw difference | Validator paths | Native targets | Location difference |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| specification/sql/resource-manager/Microsoft.Sql/SQL | 2224 | 157 | 2067 | 134 | 134 | 0 |
| specification/network/resource-manager/Microsoft.Network/Network/Network | 2190 | 258 | 1932 | 214 | 211 | 3 |
| specification/billing/resource-manager/Microsoft.Billing/Billing | 75 | 145 | -70 | 75 | 75 | 0 |
| specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup | 54 | 101 | -47 | 54 | 54 | 0 |
| specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization | 63 | 100 | -37 | 63 | 63 | 0 |
| specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement | 96 | 126 | -30 | 96 | 96 | 0 |
| specification/compute/resource-manager/Microsoft.Compute/Compute/Compute | 148 | 178 | -30 | 148 | 148 | 0 |
| specification/web/resource-manager/Microsoft.Web/AppService | 256 | 286 | -30 | 256 | 256 | 0 |
| specification/resources/resource-manager/Microsoft.Resources/deploymentStacks | 3 | 27 | -24 | 3 | 3 | 0 |
| specification/containerservice/resource-manager/Microsoft.ContainerService/aks | 100 | 112 | -12 | 100 | 100 | 0 |
| specification/education/resource-manager/Microsoft.Education/Education | 10 | 20 | -10 | 10 | 10 | 0 |
| specification/oracle/resource-manager/Oracle.Database/OracleDatabase | 66 | 75 | -9 | 66 | 61 | 5 |
| specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration | 74 | 83 | -9 | 74 | 74 | 0 |
| specification/marketplacecatalog/resource-manager/Microsoft.Marketplace/Products | 46 | 52 | -6 | 46 | 39 | 7 |
| specification/deviceprovisioningservices/resource-manager/Microsoft.Devices/DeviceProvisioningServices | 12 | 18 | -6 | 12 | 12 | 0 |
| specification/monitor/resource-manager/Microsoft.Insights/Insights/MetricsApi | 10 | 16 | -6 | 10 | 10 | 0 |
| specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices | 37 | 42 | -5 | 37 | 36 | 1 |
| specification/compute/resource-manager/Microsoft.Compute/Bulkactions | 52 | 57 | -5 | 52 | 51 | 1 |
| specification/alertsmanagement/resource-manager/Microsoft.AlertsManagement/AlertsManagement | 6 | 11 | -5 | 6 | 6 | 0 |
| specification/iotoperationsmq/resource-manager/Microsoft.IoTOperationsMQ/IoTOperationsMQ | 22 | 18 | 4 | 22 | 15 | 7 |
| specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/fluxConfigurations | 20 | 16 | 4 | 20 | 15 | 5 |
| specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/WorkbooksApi | 3 | 7 | -4 | 3 | 3 | 0 |
| specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices | 63 | 60 | 3 | 63 | 50 | 13 |
| specification/purestorage/resource-manager/PureStorage.Block/PureStorageBlock | 13 | 10 | 3 | 13 | 10 | 3 |
| specification/servicelinker/resource-manager/Microsoft.ServiceLinker/ServiceLinker | 4 | 1 | 3 | 4 | 1 | 3 |
| specification/chaos/resource-manager/Microsoft.Chaos/Chaos | 5 | 8 | -3 | 5 | 4 | 1 |
| specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery | 17 | 20 | -3 | 17 | 17 | 0 |
| specification/datafactory/resource-manager/Microsoft.DataFactory/DataFactory | 30 | 33 | -3 | 30 | 30 | 0 |
| specification/edge/resource-manager/Microsoft.Edge/configurationmanager | 4 | 7 | -3 | 4 | 4 | 0 |
| specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights | 69 | 67 | 2 | 69 | 61 | 8 |
| specification/azureresiliencemanagement/resource-manager/Microsoft.AzureResilienceManagement/AzureResilienceManagement | 8 | 6 | 2 | 8 | 6 | 2 |
| specification/botservice/resource-manager/Microsoft.BotService/BotService | 47 | 45 | 2 | 47 | 45 | 2 |
| specification/providerhub/resource-manager/Microsoft.ProviderHub/ProviderHub | 38 | 36 | 2 | 38 | 36 | 2 |
| specification/sovereign/resource-manager/Microsoft.Sovereign/Sovereign | 4 | 2 | 2 | 4 | 2 | 2 |
| specification/security/resource-manager/Microsoft.Security/Security/BatchPricingsAPI | 2 | 0 | 2 | 1 | 0 | 1 |
| specification/computebulkactions/ComputeBulkActions.Management | 42 | 44 | -2 | 42 | 42 | 0 |
| specification/databricks/resource-manager/Microsoft.Databricks/Databricks | 9 | 11 | -2 | 9 | 9 | 0 |
| specification/elastic/resource-manager/Microsoft.Elastic/Elastic | 9 | 11 | -2 | 9 | 9 | 0 |
| specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/extensionTypes | 5 | 7 | -2 | 5 | 5 | 0 |
| specification/management/resource-manager/Microsoft.Management/ManagementGroups | 4 | 6 | -2 | 4 | 4 | 0 |
| specification/portal/resource-manager/Microsoft.Portal/Portal | 3 | 1 | 2 | 1 | 1 | 0 |
| specification/recoveryservicesdatareplication/resource-manager/Microsoft.DataReplication/DataReplication | 36 | 38 | -2 | 36 | 36 | 0 |
| specification/operationalinsights/resource-manager/Microsoft.OperationalInsights/OperationalInsights | 27 | 26 | 1 | 27 | 21 | 6 |
| specification/automation/resource-manager/Microsoft.Automation/Automation | 52 | 51 | 1 | 52 | 51 | 1 |
| specification/communitytraining/resource-manager/Microsoft.Community/Community | 4 | 3 | 1 | 4 | 3 | 1 |
| specification/hybridaks/resource-manager/Microsoft.HybridContainerService/HybridContainerService | 9 | 10 | -1 | 9 | 8 | 1 |
| specification/liftrmongodb/resource-manager/MongoDB.Atlas/MongoDBAtlas | 2 | 1 | 1 | 2 | 1 | 1 |
| specification/mission/resource-manager/Microsoft.Mission/Mission | 4 | 5 | -1 | 4 | 3 | 1 |
| specification/netapp/resource-manager/Microsoft.NetApp/NetApp | 54 | 55 | -1 | 54 | 53 | 1 |
| specification/purview/resource-manager/Microsoft.Purview/Purview | 5 | 4 | 1 | 5 | 4 | 1 |
| specification/search/resource-manager/Microsoft.Search/Search | 2 | 1 | 1 | 2 | 1 | 1 |
| specification/splitio/SplitIO.Experimentation.Management | 2 | 1 | 1 | 2 | 1 | 1 |
| specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/Favorites | 2 | 3 | -1 | 2 | 2 | 0 |
| specification/commerce/resource-manager/Microsoft.Commerce/Commerce | 2 | 3 | -1 | 2 | 2 | 0 |
| specification/containerinstance/resource-manager/Microsoft.ContainerInstance/ContainerInstance | 11 | 12 | -1 | 11 | 11 | 0 |
| specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration | 17 | 18 | -1 | 17 | 17 | 0 |
| specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/extensions | 4 | 5 | -1 | 4 | 4 | 0 |
| specification/monitor/resource-manager/Microsoft.Insights/Insights/DataCollectionApi | 6 | 7 | -1 | 6 | 6 | 0 |
| specification/peering/resource-manager/Microsoft.Peering/Peering | 6 | 7 | -1 | 6 | 6 | 0 |
| specification/compute/resource-manager/Microsoft.Compute/Recommender | 4 | 4 | 0 | 4 | 2 | 2 |
| specification/computeschedule/resource-manager/Microsoft.ComputeSchedule/ComputeSchedule | 46 | 46 | 0 | 46 | 44 | 2 |
| specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry | 7 | 7 | 0 | 7 | 5 | 2 |
| specification/manufacturingplatform/Manufacturingplatform.Management | 7 | 7 | 0 | 7 | 5 | 2 |
| specification/apicenter/resource-manager/Microsoft.ApiCenter/ApiCenter | 4 | 4 | 0 | 4 | 3 | 1 |
| specification/cdn/resource-manager/Microsoft.Cdn/Cdn | 44 | 44 | 0 | 44 | 43 | 1 |
| specification/containerservice/resource-manager/Microsoft.ContainerService/aimanager | 3 | 3 | 0 | 3 | 2 | 1 |
| specification/dataprotection/resource-manager/Microsoft.DataProtection/DataProtection | 20 | 20 | 0 | 20 | 19 | 1 |
| specification/portalservices/resource-manager/Microsoft.PortalServices/copilotSettings | 2 | 2 | 0 | 2 | 1 | 1 |
| specification/programmableconnectivity/ProgrammableConnectivity.Management | 3 | 3 | 0 | 3 | 2 | 1 |

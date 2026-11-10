# Retained PATCH-route source inspections

All 182 retained Swagger records are grouped by frozen project and exact PATCH route.
The 97 routes were inspected in both representations; these are not 97 matched defects.
Warnings are distinct configured indices within each route's reviewed contexts.
A warning can witness several records or routes: do not sum this column across rows.
Dispositions classify source predicates, not historical emitted defects.

## `specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement`

| Exact PATCH route                                                                                                                                                                | Swagger records | Source warning witnesses | Source dispositions                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}`                                        |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-0.json)  |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/loggers/{loggerId}`                                  |               1 |                        1 | [1 source-reported](../refresh-20261110-wrapper/source-attribution/source-0.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/namedValues/{namedValueId}`                          |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-0.json)  |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/subscriptions/{sid}`                                 |               3 |                        3 | [3 source-reported](../refresh-20261110-wrapper/source-attribution/source-0.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/apis/{apiId}`               |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-0.json)  |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/loggers/{loggerId}`         |               1 |                        1 | [1 source-reported](../refresh-20261110-wrapper/source-attribution/source-0.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/namedValues/{namedValueId}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-0.json)  |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/subscriptions/{sid}`        |               3 |                        3 | [3 source-reported](../refresh-20261110-wrapper/source-attribution/source-0.json) |

## `specification/app/resource-manager/Microsoft.App/ContainerApps`

| Exact PATCH route                                                                                           | Swagger records | Source warning witnesses | Source dispositions                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/jobs/{jobName}` |               3 |                        2 | [1 source-accepts, 2 source-reported](../refresh-20261110-wrapper/source-attribution/source-1.json) |

## `specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/WorkbooksApi`

| Exact PATCH route                                                                                                          | Swagger records | Source warning witnesses | Source dispositions                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/workbooks/{resourceName}` |               3 |                        1 | [2 source-accepts, 1 source-reported](../refresh-20261110-wrapper/source-attribution/source-2.json) |

## `specification/automation/resource-manager/Microsoft.Automation/Automation`

| Exact PATCH route                                                                                                                                                                 | Swagger records | Source warning witnesses | Source dispositions                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/schedules/{scheduleName}`           |               1 |                        1 | [1 source-reported](../refresh-20261110-wrapper/source-attribution/source-3.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}` |               3 |                        3 | [3 source-reported](../refresh-20261110-wrapper/source-attribution/source-3.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/watchers/{watcherName}`             |               1 |                        1 | [1 source-reported](../refresh-20261110-wrapper/source-attribution/source-3.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/webhooks/{webhookName}`             |               1 |                        1 | [1 source-reported](../refresh-20261110-wrapper/source-attribution/source-3.json) |

## `specification/azure-kusto/resource-manager/Microsoft.Kusto/Kusto`

| Exact PATCH route                                                                                                     | Swagger records | Source warning witnesses | Source dispositions                                                              |
| --------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | -------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-4.json) |

## `specification/azurearcdata/resource-manager/Microsoft.AzureArcData/AzureArcData`

| Exact PATCH route                                                                                                                                | Swagger records | Source warning witnesses | Source dispositions                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureArcData/sqlServerInstances/{sqlServerInstanceName}` |               3 |                        3 | [3 source-reported](../refresh-20261110-wrapper/source-attribution/source-5.json) |

## `specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCI`

| Exact PATCH route                                                                                                                                          | Swagger records | Source warning witnesses | Source dispositions                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/clusters/{clusterName}/arcSettings/{arcSettingName}` |               1 |                        1 | [1 source-reported](../refresh-20261110-wrapper/source-attribution/source-6.json) |

## `specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM`

| Exact PATCH route                                                                  | Swagger records | Source warning witnesses | Source dispositions                                                              |
| ---------------------------------------------------------------------------------- | --------------: | -----------------------: | -------------------------------------------------------------------------------- |
| `/{resourceUri}/providers/Microsoft.AzureStackHCI/virtualMachineInstances/default` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-7.json) |

## `specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits`

| Exact PATCH route                                                                                                                                   | Swagger records | Source warning witnesses | Source dispositions                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BillingBenefits/conditionalCredits/{conditionalCreditName}` |               2 |                        2 | [2 source-reported](../refresh-20261110-wrapper/source-attribution/source-8.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BillingBenefits/maccs/{maccName}`                           |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-8.json)  |

## `specification/cdn/resource-manager/Microsoft.Cdn/EdgeActions`

| Exact PATCH route                                                                                                         | Swagger records | Source warning witnesses | Source dispositions                                                              |
| ------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | -------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/edgeActions/{edgeActionName}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-9.json) |

## `specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices`

| Exact PATCH route                                                                                                                                                                    | Swagger records | Source warning witnesses | Source dispositions                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/costControls/{costControlName}`                     |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-10.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/projects/{projectName}/workbenches/{workbenchName}` |               2 |                        0 | [2 source-accepts](../refresh-20261110-wrapper/source-attribution/source-10.json) |

## `specification/compute/resource-manager/Microsoft.Compute/Compute/Compute`

| Exact PATCH route                                                                                                                         | Swagger records | Source warning witnesses | Source dispositions                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-11.json) |

## `specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/RegistryTasks`

| Exact PATCH route                                                                                                                                           | Swagger records | Source warning witnesses | Source dispositions                                                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | ---------------------------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/taskRuns/{taskRunName}` |               1 |                        1 | [1 source-reported](../refresh-20261110-wrapper/source-attribution/source-12.json)                   |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName}`       |               3 |                        1 | [2 source-accepts, 1 source-reported](../refresh-20261110-wrapper/source-attribution/source-12.json) |

## `specification/containerservice/resource-manager/Microsoft.ContainerService/fleet`

| Exact PATCH route                                                                                                                                                     | Swagger records | Source warning witnesses | Source dispositions                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/fleets/{fleetName}/managedNamespaces/{managedNamespaceName}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-13.json) |

## `specification/containerstorage/resource-manager/Microsoft.ContainerStorage/ContainerStorage`

| Exact PATCH route                                                                                                          | Swagger records | Source warning witnesses | Source dispositions                                                               |
| -------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerStorage/pools/{poolName}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-14.json) |

## `specification/databox/resource-manager/Microsoft.DataBox/DataBox`

| Exact PATCH route                                                                                               | Swagger records | Source warning witnesses | Source dispositions                                                                |
| --------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | ---------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName}` |               3 |                        3 | [3 source-reported](../refresh-20261110-wrapper/source-attribution/source-15.json) |

## `specification/datafactory/resource-manager/Microsoft.DataFactory/DataFactory`

| Exact PATCH route                                                                                                                                                         | Swagger records | Source warning witnesses | Source dispositions                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | ---------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}` |               2 |                        2 | [2 source-reported](../refresh-20261110-wrapper/source-attribution/source-16.json) |

## `specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization`

| Exact PATCH route                                                                                                                                                                      | Swagger records | Source warning witnesses | Source dispositions                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/appAttachPackages/{appAttachPackageName}`                                |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-17.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/applicationGroups/{applicationGroupName}/applications/{applicationName}` |               2 |                        0 | [2 source-accepts](../refresh-20261110-wrapper/source-attribution/source-17.json) |

## `specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry`

| Exact PATCH route                                                                                                                                                           | Swagger records | Source warning witnesses | Source dispositions                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/namespaces/{namespaceName}/devices/{deviceName}`                     |               3 |                        0 | [3 source-accepts](../refresh-20261110-wrapper/source-attribution/source-18.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/namespaces/{namespaceName}/discoveredDevices/{discoveredDeviceName}` |               2 |                        0 | [2 source-accepts](../refresh-20261110-wrapper/source-attribution/source-18.json) |

## `specification/discovery/Discovery.Management`

| Exact PATCH route                                                                                                                           | Swagger records | Source warning witnesses | Source dispositions                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Discovery/storageContainers/{storageContainerName}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-19.json) |

## `specification/dynatrace/resource-manager/Dynatrace.Observability/DynatraceObservability`

| Exact PATCH route                                                                                                             | Swagger records | Source warning witnesses | Source dispositions                                                               |
| ----------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Dynatrace.Observability/monitors/{monitorName}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-20.json) |

## `specification/elasticsan/resource-manager/Microsoft.ElasticSan/ElasticSan`

| Exact PATCH route                                                                                                                                               | Swagger records | Source warning witnesses | Source dispositions                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ElasticSan/elasticSans/{elasticSanName}`                                |               5 |                        0 | [5 source-accepts](../refresh-20261110-wrapper/source-attribution/source-21.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ElasticSan/elasticSans/{elasticSanName}/volumegroups/{volumeGroupName}` |               2 |                        0 | [2 source-accepts](../refresh-20261110-wrapper/source-attribution/source-21.json) |

## `specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight`

| Exact PATCH route                                                                                                         | Swagger records | Source warning witnesses | Source dispositions                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-22.json) |

## `specification/hybridcompute/resource-manager/Microsoft.HybridCompute/HybridCompute`

| Exact PATCH route                                                                                                                                                  | Swagger records | Source warning witnesses | Source dispositions                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{machineName}`                                      |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-23.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{machineName}/licenseProfiles/{licenseProfileName}` |               2 |                        0 | [2 source-accepts](../refresh-20261110-wrapper/source-attribution/source-23.json) |

## `specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity`

| Exact PATCH route                                                                                                                                        | Swagger records | Source warning witnesses | Source dispositions                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridConnectivity/publicCloudConnectors/{publicCloudConnector}` |               2 |                        0 | [2 source-accepts](../refresh-20261110-wrapper/source-attribution/source-24.json) |

## `specification/informatica/resource-manager/Informatica.DataManagement/Informatica`

| Exact PATCH route                                                                                                                          | Swagger records | Source warning witnesses | Source dispositions                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------ | --------------: | -----------------------: | --------------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Informatica.DataManagement/organizations/{organizationName}` |               1 |                        0 | [1 name-not-source-leaf](../refresh-20261110-wrapper/source-attribution/source-25.json) |

## `specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/extensions`

| Exact PATCH route                                                                                                                                                                                     | Swagger records | Source warning witnesses | Source dispositions                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/extensions/{extensionName}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-26.json) |

## `specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/fluxConfigurations`

| Exact PATCH route                                                                                                                                                                                                     | Swagger records | Source warning witnesses | Source dispositions                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/fluxConfigurations/{fluxConfigurationName}` |               5 |                        0 | [5 source-accepts](../refresh-20261110-wrapper/source-attribution/source-27.json) |

## `specification/kubernetesruntime/resource-manager/Microsoft.KubernetesRuntime/KubernetesRuntime`

| Exact PATCH route                                                                        | Swagger records | Source warning witnesses | Source dispositions                                                                 |
| ---------------------------------------------------------------------------------------- | --------------: | -----------------------: | ----------------------------------------------------------------------------------- |
| `/{resourceUri}/providers/Microsoft.KubernetesRuntime/storageClasses/{storageClassName}` |              12 |                       12 | [12 source-reported](../refresh-20261110-wrapper/source-attribution/source-28.json) |

## `specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices`

| Exact PATCH route                                                                                                                                                                                       | Swagger records | Source warning witnesses | Source dispositions                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/registries/{registryName}`                                                              |               2 |                        0 | [1 name-not-source-leaf, 1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-29.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/batchEndpoints/{endpointName}`                               |               2 |                        1 | [1 source-accepts, 1 source-reported](../refresh-20261110-wrapper/source-attribution/source-29.json)      |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/batchEndpoints/{endpointName}/deployments/{deploymentName}`  |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-29.json)                         |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName}`                                      |               3 |                        3 | [3 source-reported](../refresh-20261110-wrapper/source-attribution/source-29.json)                        |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/onlineEndpoints/{endpointName}`                              |               2 |                        1 | [1 source-accepts, 1 source-reported](../refresh-20261110-wrapper/source-attribution/source-29.json)      |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/onlineEndpoints/{endpointName}/deployments/{deploymentName}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-29.json)                         |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/serverlessEndpoints/{name}`                                  |               2 |                        1 | [1 source-accepts, 1 source-reported](../refresh-20261110-wrapper/source-attribution/source-29.json)      |

## `specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric`

| Exact PATCH route                                                                                                                                                                                                 | Swagger records | Source warning witnesses | Source dispositions                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | ------------------------------------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/accessControlLists/{accessControlListName}`                                                          |               3 |                        2 | [1 source-accepts, 2 source-reported](../refresh-20261110-wrapper/source-attribution/source-30.json)          |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}`                                                          |               3 |                        3 | [2 mixed-source-predicates, 1 source-reported](../refresh-20261110-wrapper/source-attribution/source-30.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/externalNetworks/{externalNetworkName}`                   |               2 |                        2 | [1 name-not-source-leaf, 1 source-reported](../refresh-20261110-wrapper/source-attribution/source-30.json)    |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/internalNetworks/{internalNetworkName}`                   |               5 |                        5 | [1 name-not-source-leaf, 4 source-reported](../refresh-20261110-wrapper/source-attribution/source-30.json)    |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}`                                                                  |               1 |                        0 | [1 name-not-source-leaf](../refresh-20261110-wrapper/source-attribution/source-30.json)                       |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}/networkToNetworkInterconnects/{networkToNetworkInterconnectName}` |               2 |                        1 | [1 name-not-source-leaf, 1 source-reported](../refresh-20261110-wrapper/source-attribution/source-30.json)    |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkMonitors/{networkMonitorName}`                                                                |               1 |                        1 | [1 source-reported](../refresh-20261110-wrapper/source-attribution/source-30.json)                            |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkTapRules/{networkTapRuleName}`                                                                |               2 |                        2 | [2 source-reported](../refresh-20261110-wrapper/source-attribution/source-30.json)                            |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkTaps/{networkTapName}`                                                                        |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-30.json)                             |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/routePolicies/{routePolicyName}`                                                                     |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-30.json)                             |

## `specification/management/resource-manager/Microsoft.Management/ManagementGroups`

| Exact PATCH route                                            | Swagger records | Source warning witnesses | Source dispositions                                                                                  |
| ------------------------------------------------------------ | --------------: | -----------------------: | ---------------------------------------------------------------------------------------------------- |
| `/providers/Microsoft.Management/managementGroups/{groupId}` |               2 |                        1 | [1 source-accepts, 1 source-reported](../refresh-20261110-wrapper/source-attribution/source-31.json) |

## `specification/mission/resource-manager/Microsoft.Mission/Mission`

| Exact PATCH route                                                                                                                     | Swagger records | Source warning witnesses | Source dispositions                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/communities/{communityName}`          |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-32.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/virtualEnclaves/{virtualEnclaveName}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-32.json) |

## `specification/netapp/resource-manager/Microsoft.NetApp/NetApp`

| Exact PATCH route                                                                                                                                                                               | Swagger records | Source warning witnesses | Source dispositions                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}`                                           |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-33.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}`                      |               2 |                        0 | [2 source-accepts](../refresh-20261110-wrapper/source-attribution/source-33.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/buckets/{bucketName}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-33.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/snapshotPolicies/{snapshotPolicyName}`                              |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-33.json) |

## `specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud`

| Exact PATCH route                                                                                                                                                           | Swagger records | Source warning witnesses | Source dispositions                                                                                  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | ---------------------------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusters/{clusterName}`                                                |               4 |                        1 | [3 source-accepts, 1 source-reported](../refresh-20261110-wrapper/source-attribution/source-34.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/kubernetesClusters/{kubernetesClusterName}`                            |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-34.json)                    |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/kubernetesClusters/{kubernetesClusterName}/agentPools/{agentPoolName}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-34.json)                    |

## `specification/oracle/resource-manager/Oracle.Database/OracleDatabase`

| Exact PATCH route                                                                                                                           | Swagger records | Source warning witnesses | Source dispositions                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/autonomousDatabases/{autonomousdatabasename}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-35.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/dbSystems/{dbSystemName}`                     |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-35.json) |

## `specification/postgresql/DBforPostgreSQL.Management`

| Exact PATCH route                                                                                                                     | Swagger records | Source warning witnesses | Source dispositions                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}` |               4 |                        0 | [1 name-not-source-leaf, 3 source-accepts](../refresh-20261110-wrapper/source-attribution/source-36.json) |

## `specification/providerhub/resource-manager/Microsoft.ProviderHub/ProviderHub`

| Exact PATCH route                                                                                                                                         | Swagger records | Source warning witnesses | Source dispositions                                                              |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | -------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ProviderHub/providerMonitorSettings/{providerMonitorSettingName}` |               1 |                        1 | [1 body-reported](../refresh-20261110-wrapper/source-attribution/source-37.json) |

## `specification/quota/resource-manager/Microsoft.Quota/Quota`

| Exact PATCH route                                                                                                                                            | Swagger records | Source warning witnesses | Source dispositions                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------: | -----------------------: | --------------------------------------------------------------------------------------- |
| `/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Quota/groupQuotas/{groupQuotaName}`                                |               1 |                        0 | [1 name-not-source-leaf](../refresh-20261110-wrapper/source-attribution/source-38.json) |
| `/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Quota/groupQuotas/{groupQuotaName}/subscriptions/{subscriptionId}` |               1 |                        0 | [1 body-suppressed](../refresh-20261110-wrapper/source-attribution/source-38.json)      |

## `specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices`

| Exact PATCH route                                                                                                            | Swagger records | Source warning witnesses | Source dispositions                                                               |
| ---------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-39.json) |

## `specification/recoveryservicesdatareplication/resource-manager/Microsoft.DataReplication/DataReplication`

| Exact PATCH route                                                                                                                      | Swagger records | Source warning witnesses | Source dispositions                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataReplication/replicationVaults/{vaultName}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-40.json) |

## `specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery`

| Exact PATCH route                                                                                                                                                                                                                                                                 | Swagger records | Source warning witnesses | Source dispositions                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | ---------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}` |               9 |                        9 | [9 source-reported](../refresh-20261110-wrapper/source-attribution/source-41.json) |

## `specification/resources/resource-manager/Microsoft.Resources/resources`

| Exact PATCH route                                                    | Swagger records | Source warning witnesses | Source dispositions                                                                |
| -------------------------------------------------------------------- | --------------: | -----------------------: | ---------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}` |               1 |                        1 | [1 source-reported](../refresh-20261110-wrapper/source-attribution/source-42.json) |
| `/{scope}/providers/Microsoft.Resources/tags/default`                |               1 |                        1 | [1 source-reported](../refresh-20261110-wrapper/source-attribution/source-42.json) |

## `specification/scvmm/resource-manager/Microsoft.ScVmm/ScVmm`

| Exact PATCH route                                                          | Swagger records | Source warning witnesses | Source dispositions                                                               |
| -------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/{resourceUri}/providers/Microsoft.ScVmm/virtualMachineInstances/default` |               2 |                        0 | [2 source-accepts](../refresh-20261110-wrapper/source-attribution/source-43.json) |

## `specification/servicebus/resource-manager/Microsoft.ServiceBus/ServiceBus`

| Exact PATCH route                                                                                                              | Swagger records | Source warning witnesses | Source dispositions                                                               |
| ------------------------------------------------------------------------------------------------------------------------------ | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-44.json) |

## `specification/sphere/resource-manager/Microsoft.AzureSphere/AzureSphere`

| Exact PATCH route                                                                                                                                                                                      | Swagger records | Source warning witnesses | Source dispositions                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------: | -----------------------: | ---------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureSphere/catalogs/{catalogName}/products/{productName}/deviceGroups/{deviceGroupName}/devices/{deviceName}` |               1 |                        1 | [1 source-reported](../refresh-20261110-wrapper/source-attribution/source-45.json) |

## `specification/storagecache/resource-manager/Microsoft.StorageCache/StorageCache`

| Exact PATCH route                                                                                                                                                           | Swagger records | Source warning witnesses | Source dispositions                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageCache/amlFilesystems/{amlFilesystemName}/autoExportJobs/{autoExportJobName}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-46.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageCache/amlFilesystems/{amlFilesystemName}/autoImportJobs/{autoImportJobName}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-46.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageCache/amlFilesystems/{amlFilesystemName}/importJobs/{importJobName}`         |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-46.json) |

## `specification/storagediscovery/resource-manager/Microsoft.StorageDiscovery/StorageDiscovery`

| Exact PATCH route                                                                                                                                                    | Swagger records | Source warning witnesses | Source dispositions                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | --------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageDiscovery/storageDiscoveryWorkspaces/{storageDiscoveryWorkspaceName}` |               1 |                        0 | [1 source-accepts](../refresh-20261110-wrapper/source-attribution/source-47.json) |

## `specification/support/resource-manager/Microsoft.Support/Support`

| Exact PATCH route                                                                                | Swagger records | Source warning witnesses | Source dispositions                                                                |
| ------------------------------------------------------------------------------------------------ | --------------: | -----------------------: | ---------------------------------------------------------------------------------- |
| `/providers/Microsoft.Support/supportTickets/{supportTicketName}`                                |               1 |                        1 | [1 source-reported](../refresh-20261110-wrapper/source-attribution/source-48.json) |
| `/subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}` |               1 |                        1 | [1 source-reported](../refresh-20261110-wrapper/source-attribution/source-48.json) |

## `specification/vmware/resource-manager/Microsoft.AVS/AVS`

| Exact PATCH route                                                                                                                                                                            | Swagger records | Source warning witnesses | Source dispositions                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | ---------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/clusters/{clusterName}/placementPolicies/{placementPolicyName}` |               4 |                        4 | [4 source-reported](../refresh-20261110-wrapper/source-attribution/source-49.json) |

## `specification/web/resource-manager/Microsoft.Web/AppService`

| Exact PATCH route                                                                                                                                     | Swagger records | Source warning witnesses | Source dispositions                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | --------------: | -----------------------: | ---------------------------------------------------------------------------------- |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name}`                                      |               2 |                        2 | [2 source-reported](../refresh-20261110-wrapper/source-attribution/source-50.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/certificates/{certificateName}`              |               2 |                        2 | [2 source-reported](../refresh-20261110-wrapper/source-attribution/source-50.json) |
| `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/certificates/{certificateName}` |               2 |                        2 | [2 source-reported](../refresh-20261110-wrapper/source-attribution/source-50.json) |

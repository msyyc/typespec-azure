# Complete TypeSpec diagnostic inventory

Swagger linter result for every group below: **not evaluated (staging-only)**.
These are not established TypeSpec-only groups or cross-engine count gaps.
All 487 project statuses, including the 445 without selected-rule findings,
are retained in [project-inventory.json](project-inventory.json).
The raw total is 214 diagnostics across 42 projects; no failed projects.

See [corpus-examples.md](corpus-examples.md) for investigated examples and
unresolved validity/attribution limits. Different messages at one source
position remain separate findings. No whole-corpus valid/false-positive
classification has been performed.

## specification/devcenter/resource-manager/Microsoft.DevCenter/DevCenter

Swagger linter: **not evaluated**. TypeSpec linter: **90** reported diagnostics.

| Source target       | TypeSpec diagnostic                                                                                                      |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `models.tsp:688:3`  | The property 'identityType' in the PATCH body does not correspond to a property in the PUT body.                         |
| `models.tsp:688:3`  | The property 'userAssignedIdentityResourceId' in the PATCH body does not correspond to a property in the PUT body.       |
| `models.tsp:688:3`  | The property 'federatedClientId' in the PATCH body does not correspond to a property in the PUT body.                    |
| `models.tsp:688:3`  | The property 'delegatedIdentityClientId' in the PATCH body does not correspond to a property in the PUT body.            |
| `models.tsp:688:3`  | The property 'keyEncryptionKeyUrl' in the PATCH body does not correspond to a property in the PUT body.                  |
| `models.tsp:673:3`  | The property 'displayName' in the PATCH body does not correspond to a property in the PUT body.                          |
| `models.tsp:694:3`  | The property 'catalogItemSyncEnableStatus' in the PATCH body does not correspond to a property in the PUT body.          |
| `models.tsp:722:3`  | The property 'microsoftHostedNetworkEnableStatus' in the PATCH body does not correspond to a property in the PUT body.   |
| `models.tsp:728:3`  | The property 'installAzureMonitorAgentEnableStatus' in the PATCH body does not correspond to a property in the PUT body. |
| `models.tsp:768:3`  | The property 'devboxDisksEncryptionEnableStatus' in the PATCH body does not correspond to a property in the PUT body.    |
| `models.tsp:772:3`  | The property 'keyEncryptionKeyUrl' in the PATCH body does not correspond to a property in the PUT body.                  |
| `models.tsp:784:3`  | The property 'userAssignedIdentityResourceId' in the PATCH body does not correspond to a property in the PUT body.       |
| `models.tsp:810:3`  | The property 'resourcePolicies' in the PATCH body does not correspond to a property in the PUT body.                     |
| `models.tsp:813:3`  | The property 'scopes' in the PATCH body does not correspond to a property in the PUT body.                               |
| `models.tsp:858:3`  | The property 'devCenterId' in the PATCH body does not correspond to a property in the PUT body.                          |
| `models.tsp:861:3`  | The property 'description' in the PATCH body does not correspond to a property in the PUT body.                          |
| `models.tsp:865:3`  | The property 'maxDevBoxesPerUser' in the PATCH body does not correspond to a property in the PUT body.                   |
| `models.tsp:868:3`  | The property 'displayName' in the PATCH body does not correspond to a property in the PUT body.                          |
| `models.tsp:902:3`  | The property 'catalogItemSyncTypes' in the PATCH body does not correspond to a property in the PUT body.                 |
| `models.tsp:909:3`  | The property 'identities' in the PATCH body does not correspond to a property in the PUT body.                           |
| `models.tsp:912:3`  | The property 'userCustomizationsEnableStatus' in the PATCH body does not correspond to a property in the PUT body.       |
| `models.tsp:928:3`  | The property 'deleteMode' in the PATCH body does not correspond to a property in the PUT body.                           |
| `models.tsp:931:3`  | The property 'inactiveThreshold' in the PATCH body does not correspond to a property in the PUT body.                    |
| `models.tsp:934:3`  | The property 'gracePeriod' in the PATCH body does not correspond to a property in the PUT body.                          |
| `models.tsp:956:3`  | The property 'azureAiServicesMode' in the PATCH body does not correspond to a property in the PUT body.                  |
| `models.tsp:962:3`  | The property 'serverlessGpuSessionsMode' in the PATCH body does not correspond to a property in the PUT body.            |
| `models.tsp:966:3`  | The property 'maxConcurrentSessionsPerProject' in the PATCH body does not correspond to a property in the PUT body.      |
| `models.tsp:972:3`  | The property 'workspaceStorageMode' in the PATCH body does not correspond to a property in the PUT body.                 |
| `models.tsp:1255:3` | The property 'uri' in the PATCH body does not correspond to a property in the PUT body.                                  |
| `models.tsp:1258:3` | The property 'branch' in the PATCH body does not correspond to a property in the PUT body.                               |
| `models.tsp:1261:3` | The property 'secretIdentifier' in the PATCH body does not correspond to a property in the PUT body.                     |
| `models.tsp:1264:3` | The property 'path' in the PATCH body does not correspond to a property in the PUT body.                                 |
| `models.tsp:1240:3` | The property 'syncType' in the PATCH body does not correspond to a property in the PUT body.                             |
| `models.tsp:1249:3` | The property 'tags' in the PATCH body does not correspond to a property in the PUT body.                                 |
| `models.tsp:1526:3` | The property 'displayName' in the PATCH body does not correspond to a property in the PUT body.                          |
| `models.tsp:1573:3` | The property 'deploymentTargetId' in the PATCH body does not correspond to a property in the PUT body.                   |
| `models.tsp:1576:3` | The property 'displayName' in the PATCH body does not correspond to a property in the PUT body.                          |
| `models.tsp:1579:3` | The property 'status' in the PATCH body does not correspond to a property in the PUT body.                               |
| `models.tsp:1593:3` | The property 'roles' in the PATCH body does not correspond to a property in the PUT body.                                |
| `models.tsp:1586:3` | The property 'userRoleAssignments' in the PATCH body does not correspond to a property in the PUT body.                  |
| `models.tsp:1668:3` | The property 'id' in the PATCH body does not correspond to a property in the PUT body.                                   |
| `models.tsp:1681:3` | The property 'name' in the PATCH body does not correspond to a property in the PUT body.                                 |
| `models.tsp:1681:3` | The property 'tier' in the PATCH body does not correspond to a property in the PUT body.                                 |
| `models.tsp:1681:3` | The property 'size' in the PATCH body does not correspond to a property in the PUT body.                                 |
| `models.tsp:1681:3` | The property 'family' in the PATCH body does not correspond to a property in the PUT body.                               |
| `models.tsp:1681:3` | The property 'capacity' in the PATCH body does not correspond to a property in the PUT body.                             |
| `models.tsp:1684:3` | The property 'osStorageType' in the PATCH body does not correspond to a property in the PUT body.                        |
| `models.tsp:1687:3` | The property 'hibernateSupport' in the PATCH body does not correspond to a property in the PUT body.                     |
| `models.tsp:2064:3` | The property 'devBoxDefinitionType' in the PATCH body does not correspond to a property in the PUT body.                 |
| `models.tsp:2067:3` | The property 'devBoxDefinitionName' in the PATCH body does not correspond to a property in the PUT body.                 |
| `models.tsp:2112:3` | The property 'name' in the PATCH body does not correspond to a property in the PUT body.                                 |
| `models.tsp:2112:3` | The property 'tier' in the PATCH body does not correspond to a property in the PUT body.                                 |
| `models.tsp:2112:3` | The property 'size' in the PATCH body does not correspond to a property in the PUT body.                                 |
| `models.tsp:2112:3` | The property 'family' in the PATCH body does not correspond to a property in the PUT body.                               |
| `models.tsp:2112:3` | The property 'capacity' in the PATCH body does not correspond to a property in the PUT body.                             |
| `models.tsp:2073:3` | The property 'networkConnectionName' in the PATCH body does not correspond to a property in the PUT body.                |
| `models.tsp:2076:3` | The property 'licenseType' in the PATCH body does not correspond to a property in the PUT body.                          |
| `models.tsp:2079:3` | The property 'localAdministrator' in the PATCH body does not correspond to a property in the PUT body.                   |
| `models.tsp:2122:3` | The property 'status' in the PATCH body does not correspond to a property in the PUT body.                               |
| `models.tsp:2125:3` | The property 'gracePeriodMinutes' in the PATCH body does not correspond to a property in the PUT body.                   |
| `models.tsp:2131:3` | The property 'status' in the PATCH body does not correspond to a property in the PUT body.                               |
| `models.tsp:2134:3` | The property 'gracePeriodMinutes' in the PATCH body does not correspond to a property in the PUT body.                   |
| `models.tsp:2088:3` | The property 'singleSignOnStatus' in the PATCH body does not correspond to a property in the PUT body.                   |
| `models.tsp:2091:3` | The property 'displayName' in the PATCH body does not correspond to a property in the PUT body.                          |
| `models.tsp:2094:3` | The property 'virtualNetworkType' in the PATCH body does not correspond to a property in the PUT body.                   |
| `models.tsp:2097:3` | The property 'managedVirtualNetworkRegions' in the PATCH body does not correspond to a property in the PUT body.         |
| `models.tsp:2140:3` | The property 'keepAwakeEnableStatus' in the PATCH body does not correspond to a property in the PUT body.                |
| `models.tsp:2143:3` | The property 'autoStartEnableStatus' in the PATCH body does not correspond to a property in the PUT body.                |
| `models.tsp:2146:3` | The property 'defaultTimeZone' in the PATCH body does not correspond to a property in the PUT body.                      |
| `models.tsp:2149:3` | The property 'defaultStartTimeHour' in the PATCH body does not correspond to a property in the PUT body.                 |
| `models.tsp:2152:3` | The property 'defaultEndTimeHour' in the PATCH body does not correspond to a property in the PUT body.                   |
| `models.tsp:2155:3` | The property 'defaultDaysOfWeek' in the PATCH body does not correspond to a property in the PUT body.                    |
| `models.tsp:2158:3` | The property 'daysOfWeekLimit' in the PATCH body does not correspond to a property in the PUT body.                      |
| `models.tsp:2103:3` | The property 'devBoxTunnelEnableStatus' in the PATCH body does not correspond to a property in the PUT body.             |
| `models.tsp:747:3`  | The property 'tags' in the PATCH body does not correspond to a property in the PUT body.                                 |
| `models.tsp:2181:3` | The property 'type' in the PATCH body does not correspond to a property in the PUT body.                                 |
| `models.tsp:2184:3` | The property 'frequency' in the PATCH body does not correspond to a property in the PUT body.                            |
| `models.tsp:2187:3` | The property 'time' in the PATCH body does not correspond to a property in the PUT body.                                 |
| `models.tsp:2190:3` | The property 'timeZone' in the PATCH body does not correspond to a property in the PUT body.                             |
| `models.tsp:2193:3` | The property 'state' in the PATCH body does not correspond to a property in the PUT body.                                |
| `models.tsp:1086:3` | The property 'statusModifiable' in the PATCH body does not correspond to a property in the PUT body.                     |
| `models.tsp:1089:3` | The property 'valuesModifiable' in the PATCH body does not correspond to a property in the PUT body.                     |
| `models.tsp:1092:3` | The property 'defaultStatus' in the PATCH body does not correspond to a property in the PUT body.                        |
| `models.tsp:1095:3` | The property 'defaultValues' in the PATCH body does not correspond to a property in the PUT body.                        |
| `models.tsp:941:3`  | The property 'deleteMode' in the PATCH body does not correspond to a property in the PUT body.                           |
| `models.tsp:944:3`  | The property 'inactiveThreshold' in the PATCH body does not correspond to a property in the PUT body.                    |
| `models.tsp:947:3`  | The property 'gracePeriod' in the PATCH body does not correspond to a property in the PUT body.                          |
| `models.tsp:950:3`  | The property 'cancelOnConnectEnableStatus' in the PATCH body does not correspond to a property in the PUT body.          |
| `models.tsp:896:3`  | The property 'assignedGroups' in the PATCH body does not correspond to a property in the PUT body.                       |
| `models.tsp:1244:3` | The property 'autoImageBuildEnableStatus' in the PATCH body does not correspond to a property in the PUT body.           |

## specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric

Swagger linter: **not evaluated**. TypeSpec linter: **13** reported diagnostics.

| Source target                                   | TypeSpec diagnostic                                                                                                      |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `models/InternalNetwork.tsp:324:3`              | The property 'connectedIPv4SubnetsDeprecated' in the PATCH body does not correspond to a property in the PUT body.       |
| `models/InternalNetwork.tsp:338:3`              | The property 'connectedIPv6SubnetsDeprecated' in the PATCH body does not correspond to a property in the PUT body.       |
| `models/NetworkFabric.tsp:403:3`                | The property 'primaryIpv6Prefix' in the PATCH body does not correspond to a property in the PUT body.                    |
| `models/NetworkToNetworkInterconnect.tsp:333:3` | The property 'ipv4RoutesDeprecated' in the PATCH body does not correspond to a property in the PUT body.                 |
| `models/NetworkToNetworkInterconnect.tsp:345:3` | The property 'ipv6RoutesDeprecated' in the PATCH body does not correspond to a property in the PUT body.                 |
| `models/NetworkTapRule.tsp:225:3`               | The property 'dynamicMatchConfigurationsDeprecated' in the PATCH body does not correspond to a property in the PUT body. |
| `models/L3IsolationDomain.tsp:100:3`            | The property 'ipv4RoutesDeprecated' in the PATCH body does not correspond to a property in the PUT body.                 |
| `models/L3IsolationDomain.tsp:112:3`            | The property 'ipv6RoutesDeprecated' in the PATCH body does not correspond to a property in the PUT body.                 |
| `models/InternalNetwork.tsp:613:3`              | The property 'neighborIpExclusionsDeprecated' in the PATCH body does not correspond to a property in the PUT body.       |
| `models/common.tsp:1085:3`                      | The property 'prefixLimitsDeprecated' in the PATCH body does not correspond to a property in the PUT body.               |
| `models/common.tsp:1110:3`                      | The property 'prefixLimitsDeprecated' in the PATCH body does not correspond to a property in the PUT body.               |
| `models/NetworkInterface.tsp:89:3`              | The property 'description' in the PATCH body does not correspond to a property in the PUT body.                          |
| `models/NetworkToNetworkInterconnect.tsp:262:3` | The property 'prefixLimitsDeprecated' in the PATCH body does not correspond to a property in the PUT body.               |

## specification/kubernetesruntime/resource-manager/Microsoft.KubernetesRuntime/KubernetesRuntime

Swagger linter: **not evaluated**. TypeSpec linter: **12** reported diagnostics.

| Source target            | TypeSpec diagnostic                                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------------------------------- |
| `storageclass.tsp:174:3` | The property 'backingStorageClassName' in the PATCH body does not correspond to a property in the PUT body. |
| `storageclass.tsp:183:3` | The property 'azureStorageAccountName' in the PATCH body does not correspond to a property in the PUT body. |
| `storageclass.tsp:187:3` | The property 'azureStorageAccountKey' in the PATCH body does not correspond to a property in the PUT body.  |
| `storageclass.tsp:207:3` | The property 'server' in the PATCH body does not correspond to a property in the PUT body.                  |
| `storageclass.tsp:210:3` | The property 'share' in the PATCH body does not correspond to a property in the PUT body.                   |
| `storageclass.tsp:213:3` | The property 'subDir' in the PATCH body does not correspond to a property in the PUT body.                  |
| `storageclass.tsp:216:3` | The property 'mountPermissions' in the PATCH body does not correspond to a property in the PUT body.        |
| `storageclass.tsp:219:3` | The property 'onDelete' in the PATCH body does not correspond to a property in the PUT body.                |
| `storageclass.tsp:228:3` | The property 'source' in the PATCH body does not correspond to a property in the PUT body.                  |
| `storageclass.tsp:234:3` | The property 'username' in the PATCH body does not correspond to a property in the PUT body.                |
| `storageclass.tsp:238:3` | The property 'password' in the PATCH body does not correspond to a property in the PUT body.                |
| `storageclass.tsp:241:3` | The property 'domain' in the PATCH body does not correspond to a property in the PUT body.                  |

## specification/automation/resource-manager/Microsoft.Automation/Automation

Swagger linter: **not evaluated**. TypeSpec linter: **9** reported diagnostics.

| Source target       | TypeSpec diagnostic                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------ |
| `models.tsp:5200:3` | The property 'createdBy' in the PATCH body does not correspond to a property in the PUT body.          |
| `models.tsp:5200:3` | The property 'createdByType' in the PATCH body does not correspond to a property in the PUT body.      |
| `models.tsp:5200:3` | The property 'createdAt' in the PATCH body does not correspond to a property in the PUT body.          |
| `models.tsp:5200:3` | The property 'lastModifiedBy' in the PATCH body does not correspond to a property in the PUT body.     |
| `models.tsp:5200:3` | The property 'lastModifiedByType' in the PATCH body does not correspond to a property in the PUT body. |
| `models.tsp:5200:3` | The property 'lastModifiedAt' in the PATCH body does not correspond to a property in the PUT body.     |
| `models.tsp:5423:3` | The property 'isEnabled' in the PATCH body does not correspond to a property in the PUT body.          |
| `models.tsp:6349:3` | The property 'name' in the PATCH body does not correspond to a property in the PUT body.               |
| `models.tsp:6519:3` | The property 'description' in the PATCH body does not correspond to a property in the PUT body.        |

## specification/cdn/resource-manager/Microsoft.Cdn/Cdn

Swagger linter: **not evaluated**. TypeSpec linter: **9** reported diagnostics.

| Source target       | TypeSpec diagnostic                                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `models.tsp:3131:3` | The property 'probePath' in the PATCH body does not correspond to a property in the PUT body.                                             |
| `models.tsp:3136:3` | The property 'probeRequestType' in the PATCH body does not correspond to a property in the PUT body.                                      |
| `models.tsp:3141:3` | The property 'probeProtocol' in the PATCH body does not correspond to a property in the PUT body.                                         |
| `models.tsp:3148:3` | The property 'probeIntervalInSeconds' in the PATCH body does not correspond to a property in the PUT body.                                |
| `models.tsp:4995:3` | The property 'origins' in the PATCH body does not correspond to a property in the PUT body.                                               |
| `models.tsp:5002:3` | The property 'trafficRestorationTimeToHealedOrNewEndpointsInMinutes' in the PATCH body does not correspond to a property in the PUT body. |
| `models.tsp:4553:3` | The property 'responseBasedDetectedErrorTypes' in the PATCH body does not correspond to a property in the PUT body.                       |
| `models.tsp:4560:3` | The property 'responseBasedFailoverThresholdPercentage' in the PATCH body does not correspond to a property in the PUT body.              |
| `models.tsp:4566:3` | The property 'httpErrorRanges' in the PATCH body does not correspond to a property in the PUT body.                                       |

## specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery

Swagger linter: **not evaluated**. TypeSpec linter: **9** reported diagnostics.

| Source target       | TypeSpec diagnostic                                                                                                |
| ------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `models.tsp:3352:3` | The property 'recoveryAzureVMName' in the PATCH body does not correspond to a property in the PUT body.            |
| `models.tsp:3358:3` | The property 'recoveryAzureVMSize' in the PATCH body does not correspond to a property in the PUT body.            |
| `models.tsp:3363:3` | The property 'selectedRecoveryAzureNetworkId' in the PATCH body does not correspond to a property in the PUT body. |
| `models.tsp:3368:3` | The property 'selectedTfoAzureNetworkId' in the PATCH body does not correspond to a property in the PUT body.      |
| `models.tsp:3373:3` | The property 'selectedSourceNicId' in the PATCH body does not correspond to a property in the PUT body.            |
| `models.tsp:3378:3` | The property 'enableRdpOnTargetOption' in the PATCH body does not correspond to a property in the PUT body.        |
| `models.tsp:3384:3` | The property 'vmNics' in the PATCH body does not correspond to a property in the PUT body.                         |
| `models.tsp:3389:3` | The property 'licenseType' in the PATCH body does not correspond to a property in the PUT body.                    |
| `models.tsp:3394:3` | The property 'recoveryAvailabilitySetId' in the PATCH body does not correspond to a property in the PUT body.      |

## specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud

Swagger linter: **not evaluated**. TypeSpec linter: **8** reported diagnostics.

| Source target                                     | TypeSpec diagnostic                                                                                                  |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `clusters/Cluster_models.tsp:1580:3`              | The property 'aggregatorOrSingleRackDefinition' in the PATCH body does not correspond to a property in the PUT body. |
| `clusters/Cluster_models.tsp:1596:3`              | The property 'clusterServicePrincipal' in the PATCH body does not correspond to a property in the PUT body.          |
| `clusters/Cluster_models.tsp:1607:3`              | The property 'computeDeploymentThreshold' in the PATCH body does not correspond to a property in the PUT body.       |
| `clusters/Cluster_models.tsp:1620:3`              | The property 'runtimeProtectionConfiguration' in the PATCH body does not correspond to a property in the PUT body.   |
| `clusters/Cluster_models.tsp:1626:3`              | The property 'secretArchive' in the PATCH body does not correspond to a property in the PUT body.                    |
| `clusters/Cluster_models.tsp:1637:3`              | The property 'updateStrategy' in the PATCH body does not correspond to a property in the PUT body.                   |
| `virtualmachines/VirtualMachine_models.tsp:439:3` | The property 'vmImageRepositoryCredentials' in the PATCH body does not correspond to a property in the PUT body.     |
| `virtualmachines/Console_models.tsp:182:3`        | The property 'sshPublicKey' in the PATCH body does not correspond to a property in the PUT body.                     |

## specification/servicefabric/resource-manager/Microsoft.ServiceFabric/ServiceFabric

Swagger linter: **not evaluated**. TypeSpec linter: **6** reported diagnostics.

| Source target     | TypeSpec diagnostic                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------ |
| `models.tsp:87:3` | The property 'createdBy' in the PATCH body does not correspond to a property in the PUT body.          |
| `models.tsp:87:3` | The property 'createdByType' in the PATCH body does not correspond to a property in the PUT body.      |
| `models.tsp:87:3` | The property 'createdAt' in the PATCH body does not correspond to a property in the PUT body.          |
| `models.tsp:87:3` | The property 'lastModifiedBy' in the PATCH body does not correspond to a property in the PUT body.     |
| `models.tsp:87:3` | The property 'lastModifiedByType' in the PATCH body does not correspond to a property in the PUT body. |
| `models.tsp:87:3` | The property 'lastModifiedAt' in the PATCH body does not correspond to a property in the PUT body.     |

## specification/app/resource-manager/Microsoft.App/ContainerApps

Swagger linter: **not evaluated**. TypeSpec linter: **4** reported diagnostics.

| Source target       | TypeSpec diagnostic                                                                                     |
| ------------------- | ------------------------------------------------------------------------------------------------------- |
| `models.tsp:2711:3` | The property 'vnetConfiguration' in the PATCH body does not correspond to a property in the PUT body.   |
| `models.tsp:4324:3` | The property 'outboundIpAddresses' in the PATCH body does not correspond to a property in the PUT body. |
| `models.tsp:4329:3` | The property 'eventStreamEndpoint' in the PATCH body does not correspond to a property in the PUT body. |
| `models.tsp:7037:3` | The property 'networking' in the PATCH body does not correspond to a property in the PUT body.          |

## specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices

Swagger linter: **not evaluated**. TypeSpec linter: **4** reported diagnostics.

| Source target       | TypeSpec diagnostic                                                                                             |
| ------------------- | --------------------------------------------------------------------------------------------------------------- |
| `models.tsp:4311:3` | The property 'maxNodeCount' in the PATCH body does not correspond to a property in the PUT body.                |
| `models.tsp:4316:3` | The property 'minNodeCount' in the PATCH body does not correspond to a property in the PUT body.                |
| `models.tsp:4321:3` | The property 'nodeIdleTimeBeforeScaleDown' in the PATCH body does not correspond to a property in the PUT body. |
| `models.tsp:8082:3` | The property 'identity' in the PATCH body does not correspond to a property in the PUT body.                    |

## specification/vmware/resource-manager/Microsoft.AVS/AVS

Swagger linter: **not evaluated**. TypeSpec linter: **4** reported diagnostics.

| Source target                 | TypeSpec diagnostic                                                                                        |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `placementPolicies.tsp:159:3` | The property 'vmMembers' in the PATCH body does not correspond to a property in the PUT body.              |
| `placementPolicies.tsp:162:3` | The property 'hostMembers' in the PATCH body does not correspond to a property in the PUT body.            |
| `placementPolicies.tsp:165:3` | The property 'affinityStrength' in the PATCH body does not correspond to a property in the PUT body.       |
| `placementPolicies.tsp:168:3` | The property 'azureHybridBenefitType' in the PATCH body does not correspond to a property in the PUT body. |

## specification/azurearcdata/resource-manager/Microsoft.AzureArcData/AzureArcData

Swagger linter: **not evaluated**. TypeSpec linter: **3** reported diagnostics.

| Source target       | TypeSpec diagnostic                                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `models.tsp:4012:3` | The property 'isMicrosoftPkiCertTrustConfigured' in the PATCH body does not correspond to a property in the PUT body. |
| `models.tsp:4017:3` | The property 'isDigiCertPkiCertTrustConfigured' in the PATCH body does not correspond to a property in the PUT body.  |
| `models.tsp:4023:3` | The property 'maxServerMemoryMB' in the PATCH body does not correspond to a property in the PUT body.                 |

## specification/databox/resource-manager/Microsoft.DataBox/DataBox

Swagger linter: **not evaluated**. TypeSpec linter: **3** reported diagnostics.

| Source target       | TypeSpec diagnostic                                                                                      |
| ------------------- | -------------------------------------------------------------------------------------------------------- |
| `models.tsp:2480:3` | The property 'carrierAccountNumber' in the PATCH body does not correspond to a property in the PUT body. |
| `models.tsp:2485:3` | The property 'carrierName' in the PATCH body does not correspond to a property in the PUT body.          |
| `models.tsp:2490:3` | The property 'trackingId' in the PATCH body does not correspond to a property in the PUT body.           |

## specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement

Swagger linter: **not evaluated**. TypeSpec linter: **2** reported diagnostics.

| Source target        | TypeSpec diagnostic                                                                                |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| `models.tsp:10095:3` | The property 'expirationDate' in the PATCH body does not correspond to a property in the PUT body. |
| `models.tsp:10124:3` | The property 'stateComment' in the PATCH body does not correspond to a property in the PUT body.   |

## specification/applink/AppLink.Management

Swagger linter: **not evaluated**. TypeSpec linter: **2** reported diagnostics.

| Source target             | TypeSpec diagnostic                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| `applinkmember.tsp:29:3`  | The property 'metadata' in the PATCH body does not correspond to a property in the PUT body.       |
| `applinkmember.tsp:118:3` | The property 'privateConnect' in the PATCH body does not correspond to a property in the PUT body. |

## specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits

Swagger linter: **not evaluated**. TypeSpec linter: **2** reported diagnostics.

| Source target       | TypeSpec diagnostic                                                                                   |
| ------------------- | ----------------------------------------------------------------------------------------------------- |
| `models.tsp:3237:3` | The property 'allowContributors' in the PATCH body does not correspond to a property in the PUT body. |
| `models.tsp:3242:3` | The property 'milestones' in the PATCH body does not correspond to a property in the PUT body.        |

## specification/datafactory/resource-manager/Microsoft.DataFactory/DataFactory

Swagger linter: **not evaluated**. TypeSpec linter: **2** reported diagnostics.

| Source target       | TypeSpec diagnostic                                                                                   |
| ------------------- | ----------------------------------------------------------------------------------------------------- |
| `models.tsp:3986:3` | The property 'autoUpdate' in the PATCH body does not correspond to a property in the PUT body.        |
| `models.tsp:3991:3` | The property 'updateDelayOffset' in the PATCH body does not correspond to a property in the PUT body. |

## specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry

Swagger linter: **not evaluated**. TypeSpec linter: **2** reported diagnostics.

| Source target        | TypeSpec diagnostic                                                                                                   |
| -------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `ns_policy.tsp:66:3` | The property 'certificateAuthorityConfiguration' in the PATCH body does not correspond to a property in the PUT body. |
| `ns_policy.tsp:94:3` | The property 'bringYourOwnRoot' in the PATCH body does not correspond to a property in the PUT body.                  |

## specification/discovery/Discovery.Management

Swagger linter: **not evaluated**. TypeSpec linter: **2** reported diagnostics.

| Source target                                                     | TypeSpec diagnostic                                                                            |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `../Discovery.Workspace.Management/ChatModelDeployments.tsp:63:3` | The property 'properties' in the PATCH body does not correspond to a property in the PUT body. |
| `storageContainer.tsp:114:3`                                      | The property 'properties' in the PATCH body does not correspond to a property in the PUT body. |

## specification/informatica/resource-manager/Informatica.DataManagement/Informatica

Swagger linter: **not evaluated**. TypeSpec linter: **2** reported diagnostics.

| Source target    | TypeSpec diagnostic                                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------------------------------- |
| `main.tsp:739:3` | The property 'informaticaOrganizationProperties' in the PATCH body does not correspond to a property in the PUT body. |
| `main.tsp:751:3` | The property 'existingResourceId' in the PATCH body does not correspond to a property in the PUT body.                |

## specification/managedoperations/ManagedOps.Management

Swagger linter: **not evaluated**. TypeSpec linter: **2** reported diagnostics.

| Source target          | TypeSpec diagnostic                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------------------------ |
| `managedOps.tsp:348:3` | The property 'defenderForServers' in the PATCH body does not correspond to a property in the PUT body. |
| `managedOps.tsp:352:3` | The property 'defenderCspm' in the PATCH body does not correspond to a property in the PUT body.       |

## specification/netapp/resource-manager/Microsoft.NetApp/NetApp

Swagger linter: **not evaluated**. TypeSpec linter: **2** reported diagnostics.

| Source target        | TypeSpec diagnostic                                                                                        |
| -------------------- | ---------------------------------------------------------------------------------------------------------- |
| `Volume.tsp:1361:3`  | The property 'usageThreshold20250901' in the PATCH body does not correspond to a property in the PUT body. |
| `Snapshot.tsp:116:3` | The PATCH request body must contain at least one property.                                                 |

## specification/powerbidedicated/resource-manager/Microsoft.PowerBIdedicated/PowerBIDedicated

Swagger linter: **not evaluated**. TypeSpec linter: **2** reported diagnostics.

| Source target      | TypeSpec diagnostic                                                                         |
| ------------------ | ------------------------------------------------------------------------------------------- |
| `models.tsp:207:3` | The property 'members' in the PATCH body does not correspond to a property in the PUT body. |
| `models.tsp:185:3` | The property 'mode' in the PATCH body does not correspond to a property in the PUT body.    |

## specification/resources/resource-manager/Microsoft.Resources/resources

Swagger linter: **not evaluated**. TypeSpec linter: **2** reported diagnostics.

| Source target       | TypeSpec diagnostic                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------- |
| `models.tsp:868:3`  | The property 'name' in the PATCH body does not correspond to a property in the PUT body.      |
| `models.tsp:1032:3` | The property 'operation' in the PATCH body does not correspond to a property in the PUT body. |

## specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/WorkbooksApi

Swagger linter: **not evaluated**. TypeSpec linter: **1** reported diagnostics.

| Source target      | TypeSpec diagnostic                                                                          |
| ------------------ | -------------------------------------------------------------------------------------------- |
| `models.tsp:254:3` | The property 'revision' in the PATCH body does not correspond to a property in the PUT body. |

## specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCI

Swagger linter: **not evaluated**. TypeSpec linter: **1** reported diagnostics.

| Source target       | TypeSpec diagnostic                                                                      |
| ------------------- | ---------------------------------------------------------------------------------------- |
| `models.tsp:2010:3` | The property 'tags' in the PATCH body does not correspond to a property in the PUT body. |

## specification/billingtrust/resource-manager/Microsoft.BillingTrust/BillingTrust

Swagger linter: **not evaluated**. TypeSpec linter: **1** reported diagnostics.

| Source target    | TypeSpec diagnostic                                                                      |
| ---------------- | ---------------------------------------------------------------------------------------- |
| `main.tsp:324:3` | The property 'kind' in the PATCH body does not correspond to a property in the PUT body. |

## specification/codesigning/resource-manager/Microsoft.CodeSigning/CodeSigning

Swagger linter: **not evaluated**. TypeSpec linter: **1** reported diagnostics.

| Source target      | TypeSpec diagnostic                                                                     |
| ------------------ | --------------------------------------------------------------------------------------- |
| `models.tsp:162:3` | The property 'sku' in the PATCH body does not correspond to a property in the PUT body. |

## specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/RegistryTasks

Swagger linter: **not evaluated**. TypeSpec linter: **1** reported diagnostics.

| Source target      | TypeSpec diagnostic                                                                      |
| ------------------ | ---------------------------------------------------------------------------------------- |
| `models.tsp:936:3` | The property 'tags' in the PATCH body does not correspond to a property in the PUT body. |

## specification/containerstorage/resource-manager/Microsoft.ContainerStorage/ContainerStorage

Swagger linter: **not evaluated**. TypeSpec linter: **1** reported diagnostics.

| Source target    | TypeSpec diagnostic                                                                            |
| ---------------- | ---------------------------------------------------------------------------------------------- |
| `pool.tsp:106:3` | The property 'elasticSan' in the PATCH body does not correspond to a property in the PUT body. |

## specification/databasefleetmanager/resource-manager/Microsoft.DatabaseFleetManager/DatabaseFleetManager

Swagger linter: **not evaluated**. TypeSpec linter: **1** reported diagnostics.

| Source target      | TypeSpec diagnostic                                                                            |
| ------------------ | ---------------------------------------------------------------------------------------------- |
| `models.tsp:340:3` | The property 'properties' in the PATCH body does not correspond to a property in the PUT body. |

## specification/databoxedge/resource-manager/Microsoft.DataBoxEdge/DataBoxEdge

Swagger linter: **not evaluated**. TypeSpec linter: **1** reported diagnostics.

| Source target       | TypeSpec diagnostic                                                                    |
| ------------------- | -------------------------------------------------------------------------------------- |
| `models.tsp:1717:3` | The property 'id' in the PATCH body does not correspond to a property in the PUT body. |

## specification/dnsresolver/resource-manager/Microsoft.Network/DnsResolver

Swagger linter: **not evaluated**. TypeSpec linter: **1** reported diagnostics.

| Source target      | TypeSpec diagnostic                                                                                        |
| ------------------ | ---------------------------------------------------------------------------------------------------------- |
| `models.tsp:612:3` | The property 'dnsResolverDomainLists' in the PATCH body does not correspond to a property in the PUT body. |

## specification/github-network/resource-manager/GitHub.Network/GitHubNetwork

Swagger linter: **not evaluated**. TypeSpec linter: **1** reported diagnostics.

| Source target                      | TypeSpec diagnostic                                                                            |
| ---------------------------------- | ---------------------------------------------------------------------------------------------- |
| `NetworkSettingsResource.tsp:37:3` | The property 'properties' in the PATCH body does not correspond to a property in the PUT body. |

## specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault

Swagger linter: **not evaluated**. TypeSpec linter: **1** reported diagnostics.

| Source target       | TypeSpec diagnostic                                                                                         |
| ------------------- | ----------------------------------------------------------------------------------------------------------- |
| `models.tsp:1463:3` | The property 'enableRbacAuthorization' in the PATCH body does not correspond to a property in the PUT body. |

## specification/management/resource-manager/Microsoft.Management/ManagementGroups

Swagger linter: **not evaluated**. TypeSpec linter: **1** reported diagnostics.

| Source target      | TypeSpec diagnostic                                                                               |
| ------------------ | ------------------------------------------------------------------------------------------------- |
| `models.tsp:602:3` | The property 'parentGroupId' in the PATCH body does not correspond to a property in the PUT body. |

## specification/migrate/resource-manager/Microsoft.OffAzure/OffAzure

Swagger linter: **not evaluated**. TypeSpec linter: **1** reported diagnostics.

| Source target       | TypeSpec diagnostic                                                                                   |
| ------------------- | ----------------------------------------------------------------------------------------------------- |
| `models.tsp:7737:3` | The property 'provisioningState' in the PATCH body does not correspond to a property in the PUT body. |

## specification/providerhub/resource-manager/Microsoft.ProviderHub/ProviderHub

Swagger linter: **not evaluated**. TypeSpec linter: **1** reported diagnostics.

| Source target                     | TypeSpec diagnostic                           |
| --------------------------------- | --------------------------------------------- |
| `ProviderMonitorSetting.tsp:42:3` | The PATCH operation must have a request body. |

## specification/sphere/resource-manager/Microsoft.AzureSphere/AzureSphere

Swagger linter: **not evaluated**. TypeSpec linter: **1** reported diagnostics.

| Source target      | TypeSpec diagnostic                                                                               |
| ------------------ | ------------------------------------------------------------------------------------------------- |
| `models.tsp:795:3` | The property 'deviceGroupId' in the PATCH body does not correspond to a property in the PUT body. |

## specification/sql/resource-manager/Microsoft.Sql/SQL

Swagger linter: **not evaluated**. TypeSpec linter: **1** reported diagnostics.

| Source target        | TypeSpec diagnostic                                                                            |
| -------------------- | ---------------------------------------------------------------------------------------------- |
| `models.tsp:11853:3` | The property 'properties' in the PATCH body does not correspond to a property in the PUT body. |

## specification/support/resource-manager/Microsoft.Support/Support

Swagger linter: **not evaluated**. TypeSpec linter: **1** reported diagnostics.

| Source target      | TypeSpec diagnostic                                                                        |
| ------------------ | ------------------------------------------------------------------------------------------ |
| `models.tsp:791:3` | The property 'status' in the PATCH body does not correspond to a property in the PUT body. |

## specification/web/resource-manager/Microsoft.Web/AppService

Swagger linter: **not evaluated**. TypeSpec linter: **1** reported diagnostics.

| Source target       | TypeSpec diagnostic                                                                                            |
| ------------------- | -------------------------------------------------------------------------------------------------------------- |
| `models.tsp:6560:3` | The property 'containerAppsConfiguration' in the PATCH body does not correspond to a property in the PUT body. |

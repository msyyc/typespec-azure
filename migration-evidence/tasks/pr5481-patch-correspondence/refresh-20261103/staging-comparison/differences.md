# Complete raw-count difference inventory

Swagger and TypeSpec rows below are separate identity domains, not paired
diagnostics. Grouping identical target/message records preserves raw
multiplicity; it is not semantic deduplication. Schema/visibility/version
investigations and their limits are in [gap-investigation.md](../gap-investigation.md).

| Project | Swagger linter | TypeSpec linter | TypeSpec minus Swagger | Absolute gap | Relative gap |
| --- | ---: | ---: | ---: | ---: | ---: |
| [specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric](#difference-0) | 93 | 13 | -80 | 80 | 86.02% |
| [specification/web/resource-manager/Microsoft.Web/AppService](#difference-1) | 53 | 1 | -52 | 52 | 98.11% |
| [specification/netapp/resource-manager/Microsoft.NetApp/NetApp](#difference-2) | 49 | 2 | -47 | 47 | 95.92% |
| [specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement](#difference-3) | 41 | 2 | -39 | 39 | 95.12% |
| [specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery](#difference-4) | 36 | 0 | -36 | 36 | 100.00% |
| [specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid](#difference-5) | 34 | 0 | -34 | 34 | 100.00% |
| [specification/compute/resource-manager/Microsoft.Compute/Compute/Compute](#difference-6) | 30 | 0 | -30 | 30 | 100.00% |
| [specification/mission/resource-manager/Microsoft.Mission/Mission](#difference-7) | 26 | 0 | -26 | 26 | 100.00% |
| [specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud](#difference-8) | 34 | 8 | -26 | 26 | 76.47% |
| [specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM](#difference-9) | 21 | 0 | -21 | 21 | 100.00% |
| [specification/postgresql/DBforPostgreSQL.Management](#difference-10) | 21 | 0 | -21 | 21 | 100.00% |
| [specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices](#difference-11) | 21 | 3 | -18 | 18 | 85.71% |
| [specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization](#difference-12) | 16 | 0 | -16 | 16 | 100.00% |
| [specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry](#difference-13) | 18 | 2 | -16 | 16 | 88.89% |
| [specification/recoveryservicesdatareplication/resource-manager/Microsoft.DataReplication/DataReplication](#difference-14) | 14 | 0 | -14 | 14 | 100.00% |
| [specification/devcenter/resource-manager/Microsoft.DevCenter/DevCenter](#difference-15) | 13 | 0 | -13 | 13 | 100.00% |
| [specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs](#difference-16) | 13 | 0 | -13 | 13 | 100.00% |
| [specification/storage/resource-manager/Microsoft.Storage/Storage](#difference-17) | 13 | 0 | -13 | 13 | 100.00% |
| [specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits](#difference-18) | 14 | 2 | -12 | 12 | 85.71% |
| [specification/iotoperationsmq/resource-manager/Microsoft.IoTOperationsMQ/IoTOperationsMQ](#difference-19) | 12 | 0 | -12 | 12 | 100.00% |
| [specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/fluxConfigurations](#difference-20) | 12 | 0 | -12 | 12 | 100.00% |
| [specification/oracle/resource-manager/Oracle.Database/OracleDatabase](#difference-21) | 12 | 0 | -12 | 12 | 100.00% |
| [specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry](#difference-22) | 11 | 0 | -11 | 11 | 100.00% |
| [specification/dnsresolver/resource-manager/Microsoft.Network/DnsResolver](#difference-23) | 12 | 1 | -11 | 11 | 91.67% |
| [specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc](#difference-24) | 10 | 0 | -10 | 10 | 100.00% |
| [specification/containerinstance/resource-manager/Microsoft.ContainerInstance/ContainerInstance](#difference-25) | 9 | 0 | -9 | 9 | 100.00% |
| [specification/hybridcompute/resource-manager/Microsoft.HybridCompute/HybridCompute](#difference-26) | 9 | 0 | -9 | 9 | 100.00% |
| [specification/azurearcdata/resource-manager/Microsoft.AzureArcData/AzureArcData](#difference-27) | 11 | 3 | -8 | 8 | 72.73% |
| [specification/certificateregistration/resource-manager/Microsoft.CertificateRegistration/CertificateRegistration](#difference-28) | 8 | 0 | -8 | 8 | 100.00% |
| [specification/discovery/Discovery.Management](#difference-29) | 10 | 2 | -8 | 8 | 80.00% |
| [specification/elasticsan/resource-manager/Microsoft.ElasticSan/ElasticSan](#difference-30) | 8 | 0 | -8 | 8 | 100.00% |
| [specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault](#difference-31) | 9 | 1 | -8 | 8 | 88.89% |
| [specification/storagecache/resource-manager/Microsoft.StorageCache/StorageCache](#difference-32) | 8 | 0 | -8 | 8 | 100.00% |
| [specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb](#difference-33) | 7 | 0 | -7 | 7 | 100.00% |
| [specification/network/resource-manager/Microsoft.Network/Network/Network](#difference-34) | 7 | 0 | -7 | 7 | 100.00% |
| [specification/scvmm/resource-manager/Microsoft.ScVmm/ScVmm](#difference-35) | 7 | 0 | -7 | 7 | 100.00% |
| [specification/servicefabric/resource-manager/Microsoft.ServiceFabric/ServiceFabric](#difference-36) | 13 | 6 | -7 | 7 | 53.85% |
| [specification/sql/resource-manager/Microsoft.Sql/SQL](#difference-37) | 8 | 1 | -7 | 7 | 87.50% |
| [specification/app/resource-manager/Microsoft.App/ContainerApps](#difference-38) | 10 | 4 | -6 | 6 | 60.00% |
| [specification/azuredatatransfer/resource-manager/Microsoft.AzureDataTransfer/AzureDataTransfer](#difference-39) | 6 | 0 | -6 | 6 | 100.00% |
| [specification/containerservice/resource-manager/Microsoft.ContainerService/aks](#difference-40) | 6 | 0 | -6 | 6 | 100.00% |
| [specification/dashboard/resource-manager/Microsoft.Dashboard/Dashboard](#difference-41) | 6 | 0 | -6 | 6 | 100.00% |
| [specification/edge/resource-manager/Microsoft.Edge/configurationmanager](#difference-42) | 6 | 0 | -6 | 6 | 100.00% |
| [specification/servicefabricmanagedclusters/resource-manager/Microsoft.ServiceFabric/ServiceFabricManagedClusters](#difference-43) | 6 | 0 | -6 | 6 | 100.00% |
| [specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/RegistryTasks](#difference-44) | 6 | 1 | -5 | 5 | 83.33% |
| [specification/containerservice/resource-manager/Microsoft.ContainerService/fleet](#difference-45) | 5 | 0 | -5 | 5 | 100.00% |
| [specification/dynatrace/resource-manager/Dynatrace.Observability/DynatraceObservability](#difference-46) | 5 | 0 | -5 | 5 | 100.00% |
| [specification/fileshares/resource-manager/Microsoft.FileShares/FileShares](#difference-47) | 5 | 0 | -5 | 5 | 100.00% |
| [specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis](#difference-48) | 5 | 0 | -5 | 5 | 100.00% |
| [specification/playwrighttesting/PlaywrightTesting.Management](#difference-49) | 5 | 0 | -5 | 5 | 100.00% |
| [specification/support/resource-manager/Microsoft.Support/Support](#difference-50) | 6 | 1 | -5 | 5 | 83.33% |
| [specification/agricultureplatform/AgriculturePlatform.Management](#difference-51) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCI](#difference-52) | 5 | 1 | -4 | 4 | 80.00% |
| [specification/cdn/resource-manager/Microsoft.Cdn/Cdn](#difference-53) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/cdn/resource-manager/Microsoft.Cdn/EdgeActions](#difference-54) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices](#difference-55) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/communication/resource-manager/Microsoft.Communication/Communication](#difference-56) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeDisk](#difference-57) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/compute/resource-manager/Microsoft.Compute/WorkloadManager](#difference-58) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/connectedcache/resource-manager/Microsoft.ConnectedCache/ConnectedCache](#difference-59) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration](#difference-60) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/hybridkubernetes/resource-manager/Microsoft.Kubernetes/HybridKubernetes](#difference-61) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/loadtestservice/resource-manager/Microsoft.LoadTestService/playwright](#difference-62) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/manufacturingplatform/Manufacturingplatform.Management](#difference-63) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/migrate/resource-manager/Microsoft.OffAzure/OffAzure](#difference-64) | 5 | 1 | -4 | 4 | 80.00% |
| [specification/monitor/resource-manager/Microsoft.Insights/Insights/DataCollectionApi](#difference-65) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/monitor/resource-manager/Microsoft.Insights/Insights/MetricAlertApi](#difference-66) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/operationalinsights/resource-manager/Microsoft.OperationalInsights/OperationalInsights](#difference-67) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/hcpopenshiftclusters](#difference-68) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/resources/resource-manager/Microsoft.Resources/deploymentScripts](#difference-69) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/servicenetworking/resource-manager/Microsoft.ServiceNetworking/ServiceNetworking](#difference-70) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/splitio/SplitIO.Experimentation.Management](#difference-71) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync](#difference-72) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/workloads/resource-manager/Microsoft.Workloads/SAPVirtualInstance](#difference-73) | 4 | 0 | -4 | 4 | 100.00% |
| [specification/apimanagement/resource-manager/Microsoft.ApiManagement/AIGateway](#difference-74) | 3 | 0 | -3 | 3 | 100.00% |
| [specification/appconfiguration/resource-manager/Microsoft.AppConfiguration/AppConfiguration](#difference-75) | 3 | 0 | -3 | 3 | 100.00% |
| [specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/WorkbooksApi](#difference-76) | 4 | 1 | -3 | 3 | 75.00% |
| [specification/azure-kusto/resource-manager/Microsoft.Kusto/Kusto](#difference-77) | 3 | 0 | -3 | 3 | 100.00% |
| [specification/azurefleet/resource-manager/Microsoft.AzureFleet/AzureFleet](#difference-78) | 3 | 0 | -3 | 3 | 100.00% |
| [specification/azurelargeinstance/resource-manager/Microsoft.AzureLargeInstance/AzureLargeInstance](#difference-79) | 3 | 0 | -3 | 3 | 100.00% |
| [specification/azureresiliencemanagement/resource-manager/Microsoft.AzureResilienceManagement/AzureResilienceManagement](#difference-80) | 3 | 0 | -3 | 3 | 100.00% |
| [specification/chaos/resource-manager/Microsoft.Chaos/Chaos](#difference-81) | 3 | 0 | -3 | 3 | 100.00% |
| [specification/datadog/resource-manager/Microsoft.Datadog/Datadog](#difference-82) | 3 | 0 | -3 | 3 | 100.00% |
| [specification/fist/resource-manager/Microsoft.IoTFirmwareDefense/IoTFirmwareDefense](#difference-83) | 3 | 0 | -3 | 3 | 100.00% |
| [specification/hardwaresecuritymodules/resource-manager/Microsoft.HardwareSecurityModules/HardwareSecurityModules](#difference-84) | 3 | 0 | -3 | 3 | 100.00% |
| [specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity](#difference-85) | 3 | 0 | -3 | 3 | 100.00% |
| [specification/iotoperationsdataprocessor/resource-manager/Microsoft.IoTOperationsDataProcessor/IoTOperationsDataProcessor](#difference-86) | 3 | 0 | -3 | 3 | 100.00% |
| [specification/iotoperationsorchestrator/resource-manager/Microsoft.IoTOperationsOrchestrator/IoTOperationsOrchestrator](#difference-87) | 3 | 0 | -3 | 3 | 100.00% |
| [specification/monitoringservice/resource-manager/Microsoft.Monitor/Agents](#difference-88) | 3 | 0 | -3 | 3 | 100.00% |
| [specification/purestorage/resource-manager/PureStorage.Block/PureStorageBlock](#difference-89) | 3 | 0 | -3 | 3 | 100.00% |
| [specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices](#difference-90) | 3 | 0 | -3 | 3 | 100.00% |
| [specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery](#difference-91) | 12 | 9 | -3 | 3 | 25.00% |
| [specification/storagediscovery/resource-manager/Microsoft.StorageDiscovery/StorageDiscovery](#difference-92) | 3 | 0 | -3 | 3 | 100.00% |
| [specification/storagemover/resource-manager/Microsoft.StorageMover/StorageMover](#difference-93) | 3 | 0 | -3 | 3 | 100.00% |
| [specification/alertsmanagement/resource-manager/Microsoft.AlertsManagement/AlertProcessingRules](#difference-94) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/alertsmanagement/resource-manager/Microsoft.AlertsManagement/PrometheusRuleGroups](#difference-95) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/anyscale/resource-manager/Anyscale.Platform/platform](#difference-96) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/app/resource-manager/Microsoft.App/SreAgent](#difference-97) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/automation/resource-manager/Microsoft.Automation/Automation](#difference-98) | 11 | 9 | -2 | 2 | 18.18% |
| [specification/azuredependencymap/resource-manager/Microsoft.DependencyMap/DependencyMap](#difference-99) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/databricks/resource-manager/Microsoft.Databricks/Databricks](#difference-100) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration](#difference-101) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/dataprotection/resource-manager/Microsoft.DataProtection/DataProtection](#difference-102) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/dell/resource-manager/Dell.Storage/DellStorage](#difference-103) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/developerhub/resource-manager/Microsoft.DevHub/DeveloperHub](#difference-104) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/edgeorder/resource-manager/Microsoft.EdgeOrder/EdgeOrder](#difference-105) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/ews/resource-manager/Microsoft.SecretSyncController/SecretSyncController](#difference-106) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/extendedlocation/resource-manager/Microsoft.ExtendedLocation/CustomLocations](#difference-107) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/healthbot/resource-manager/Microsoft.HealthBot/HealthBot](#difference-108) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/healthdataaiservices/resource-manager/Microsoft.HealthDataAIServices/HealthDataAIServices](#difference-109) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/informatica/resource-manager/Informatica.DataManagement/Informatica](#difference-110) | 4 | 2 | -2 | 2 | 50.00% |
| [specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/extensions](#difference-111) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/liftrarize/resource-manager/ArizeAi.ObservabilityEval/ObservabilityEval](#difference-112) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/liftrcommvault/Commvault.ContentStore.Management](#difference-113) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/liftrhyperexecute/resource-manager/LambdaTest.HyperExecute/HyperExecute](#difference-114) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/liftrmongodb/resource-manager/MongoDB.Atlas/MongoDBAtlas](#difference-115) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/liftrpinecone/resource-manager/Pinecone.VectorDb/PineconeVectorDb](#difference-116) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/liftrweightsandbiases/resource-manager/Microsoft.WeightsAndBiases/WeightsAndBiases](#difference-117) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/maps/resource-manager/Microsoft.Maps/Maps](#difference-118) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/monitor/resource-manager/Microsoft.Insights/Insights/ActionGroupsApi](#difference-119) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/monitor/resource-manager/Microsoft.Insights/Insights/TenantActionGroups](#difference-120) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/mysql/resource-manager/Microsoft.DBforMySQL/FlexibleServers](#difference-121) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/napster/Napster.CompanionAPI.Management](#difference-122) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/notificationhubs/resource-manager/Microsoft.NotificationHubs/NotificationHubs](#difference-123) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/onlineexperimentation/resource-manager/Microsoft.OnlineExperimentation/OnlineExperimentation](#difference-124) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/orbitalplanetarycomputer/Orbital.Management](#difference-125) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/paloaltonetworks/resource-manager/PaloAltoNetworks.Cloudngfw/Cloudngfw](#difference-126) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/peering/resource-manager/Microsoft.Peering/Peering](#difference-127) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/platformvalidation/resource-manager/Microsoft.PlatformValidation/PlatformValidation](#difference-128) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/powerbidedicated/resource-manager/Microsoft.PowerBIdedicated/PowerBIDedicated](#difference-129) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/powerplatform/resource-manager/Microsoft.PowerPlatform/PowerPlatform](#difference-130) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/privatetrafficmanager/resource-manager/Microsoft.Network/PrivateTrafficManager](#difference-131) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/programmableconnectivity/ProgrammableConnectivity.Management](#difference-132) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/quota/resource-manager/Microsoft.Quota/Quota](#difference-133) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/relay/resource-manager/Microsoft.Relay/Relay](#difference-134) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/search/resource-manager/Microsoft.Search/Search](#difference-135) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/security/resource-manager/Microsoft.Security/Security/ServiceEntitlementSettingsAPI](#difference-136) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/servicebus/resource-manager/Microsoft.ServiceBus/ServiceBus](#difference-137) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/solutions/resource-manager/Microsoft.Solutions/Solutions](#difference-138) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/sovereign/resource-manager/Microsoft.Sovereign/Sovereign](#difference-139) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/sqlvirtualmachine/resource-manager/Microsoft.SqlVirtualMachine/SqlVirtualMachine](#difference-140) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/standbypool/resource-manager/Microsoft.StandbyPool/StandbyPool](#difference-141) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/vmware/resource-manager/Microsoft.AVS/AVS](#difference-142) | 6 | 4 | -2 | 2 | 33.33% |
| [specification/workloads/resource-manager/Microsoft.Workloads/SAPDiscoverySites](#difference-143) | 2 | 0 | -2 | 2 | 100.00% |
| [specification/alertsmanagement/resource-manager/Microsoft.AlertsManagement/TenantActivityLogAlerts](#difference-144) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/apicenter/resource-manager/Microsoft.ApiCenter/ApiCenter](#difference-145) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/WorkbookTemplatesApi](#difference-146) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/applink/AppLink.Management](#difference-147) | 3 | 2 | -1 | 1 | 33.33% |
| [specification/awsconnector/AccessAnalyzerAnalyzer.Management](#difference-148) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/AcmCertificateSummary.Management](#difference-149) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/ApiGatewayRestApi.Management](#difference-150) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/ApiGatewayStage.Management](#difference-151) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/AppSyncGraphqlApi.Management](#difference-152) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/AutoScalingAutoScalingGroup.Management](#difference-153) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/CloudFormationStack.Management](#difference-154) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/CloudFormationStackSet.Management](#difference-155) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/CloudFrontDistribution.Management](#difference-156) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/CloudTrailTrail.Management](#difference-157) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/CloudWatchAlarm.Management](#difference-158) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/CodeBuildProject.Management](#difference-159) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/CodeBuildSourceCredentialsInfo.Management](#difference-160) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/ConfigServiceConfigurationRecorder.Management](#difference-161) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/ConfigServiceConfigurationRecorderStatus.Management](#difference-162) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/ConfigServiceDeliveryChannel.Management](#difference-163) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/DatabaseMigrationServiceReplicationInstance.Management](#difference-164) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/DaxCluster.Management](#difference-165) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/DynamoDBContinuousBackupsDescription.Management](#difference-166) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/DynamoDBTable.Management](#difference-167) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Ec2AccountAttribute.Management](#difference-168) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Ec2Address.Management](#difference-169) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Ec2FlowLog.Management](#difference-170) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Ec2Image.Management](#difference-171) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Ec2InstanceStatus.Management](#difference-172) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Ec2Ipam.Management](#difference-173) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Ec2KeyPair.Management](#difference-174) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Ec2NetworkAcl.Management](#difference-175) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Ec2NetworkInterface.Management](#difference-176) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Ec2RouteTable.Management](#difference-177) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Ec2SecurityGroup.Management](#difference-178) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Ec2Snapshot.Management](#difference-179) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Ec2Subnet.Management](#difference-180) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Ec2VPCEndpoint.Management](#difference-181) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Ec2VPCPeeringConnection.Management](#difference-182) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Ec2Volume.Management](#difference-183) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Ec2Vpc.Management](#difference-184) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/EcrImageDetail.Management](#difference-185) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/EcrRepository.Management](#difference-186) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/EcsCluster.Management](#difference-187) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/EcsService.Management](#difference-188) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/EcsTaskDefinition.Management](#difference-189) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/EfsFileSystem.Management](#difference-190) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/EfsMountTarget.Management](#difference-191) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/EksNodegroup.Management](#difference-192) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/ElasticBeanstalkApplication.Management](#difference-193) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/ElasticBeanstalkConfigurationTemplate.Management](#difference-194) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/ElasticBeanstalkEnvironment.Management](#difference-195) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/ElasticLoadBalancingV2Listener.Management](#difference-196) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/ElasticLoadBalancingV2LoadBalancer.Management](#difference-197) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/ElasticLoadBalancingV2TargetGroup.Management](#difference-198) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/ElasticLoadBalancingv2TargetHealthDescription.Management](#difference-199) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/EmrCluster.Management](#difference-200) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/GuardDutyDetector.Management](#difference-201) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/IamAccessKeyLastUsed.Management](#difference-202) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/IamAccessKeyMetadata.Management](#difference-203) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/IamGroup.Management](#difference-204) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/IamInstanceProfile.Management](#difference-205) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/IamMFADevice.Management](#difference-206) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/IamPasswordPolicy.Management](#difference-207) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/IamPolicyVersion.Management](#difference-208) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/IamRole.Management](#difference-209) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/IamServerCertificate.Management](#difference-210) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/IamVirtualMFADevice.Management](#difference-211) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/KmsAlias.Management](#difference-212) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/KmsKey.Management](#difference-213) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/LambdaFunction.Management](#difference-214) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/LambdaFunctionCodeLocation.Management](#difference-215) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/LightsailBucket.Management](#difference-216) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/LightsailInstance.Management](#difference-217) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/LogsLogGroup.Management](#difference-218) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/LogsLogStream.Management](#difference-219) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/LogsMetricFilter.Management](#difference-220) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/LogsSubscriptionFilter.Management](#difference-221) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Macie2JobSummary.Management](#difference-222) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/MacieAllowList.Management](#difference-223) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/NetworkFirewallFirewall.Management](#difference-224) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/NetworkFirewallFirewallPolicy.Management](#difference-225) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/NetworkFirewallRuleGroup.Management](#difference-226) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/OpenSearchDomainStatus.Management](#difference-227) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/OrganizationsAccount.Management](#difference-228) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/OrganizationsOrganization.Management](#difference-229) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/RdsDBCluster.Management](#difference-230) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/RdsDBInstance.Management](#difference-231) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/RdsDBSnapshot.Management](#difference-232) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/RdsDBSnapshotAttributesResult.Management](#difference-233) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/RdsEventSubscription.Management](#difference-234) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/RdsExportTask.Management](#difference-235) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/RedshiftCluster.Management](#difference-236) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/RedshiftClusterParameterGroup.Management](#difference-237) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Route53DomainsDomainSummary.Management](#difference-238) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Route53HostedZone.Management](#difference-239) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Route53ResourceRecordSet.Management](#difference-240) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/S3AccessControlPolicy.Management](#difference-241) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/S3AccessPoint.Management](#difference-242) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/S3Bucket.Management](#difference-243) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/S3BucketPolicy.Management](#difference-244) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/S3ControlMultiRegionAccessPointPolicyDocument.Management](#difference-245) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/SageMakerApp.Management](#difference-246) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/SageMakerNotebookInstanceSummary.Management](#difference-247) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/SecretsManagerResourcePolicy.Management](#difference-248) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/SecretsManagerSecret.Management](#difference-249) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/SnsSubscription.Management](#difference-250) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/SnsTopic.Management](#difference-251) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/SqsQueue.Management](#difference-252) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/SsmInstanceInformation.Management](#difference-253) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/SsmParameter.Management](#difference-254) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/SsmResourceComplianceSummaryItem.Management](#difference-255) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/WafWebACLSummary.Management](#difference-256) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/awsconnector/Wafv2LoggingConfiguration.Management](#difference-257) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/billingtrust/resource-manager/Microsoft.BillingTrust/BillingTrust](#difference-258) | 0 | 1 | 1 | 1 | 100.00% |
| [specification/cloudhealth/resource-manager/Microsoft.CloudHealth/CloudHealth](#difference-259) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/communitytraining/resource-manager/Microsoft.Community/Community](#difference-260) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/compute/resource-manager/Microsoft.Compute/Bulkactions](#difference-261) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/computeschedule/resource-manager/Microsoft.ComputeSchedule/ComputeSchedule](#difference-262) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/confluent/resource-manager/Microsoft.Confluent/Confluent](#difference-263) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/containerservice/resource-manager/Microsoft.ContainerService/aimanager](#difference-264) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/containerservice/resource-manager/Microsoft.ContainerService/nodecustomization](#difference-265) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/containerservice/resource-manager/Microsoft.ContainerService/preparedimagespecification](#difference-266) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/containerstorage/resource-manager/Microsoft.ContainerStorage/ContainerStorage](#difference-267) | 2 | 1 | -1 | 1 | 50.00% |
| [specification/contosowidgetmanager/Contoso.Management](#difference-268) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB](#difference-269) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/databasewatcher/resource-manager/Microsoft.DatabaseWatcher/DatabaseWatcher](#difference-270) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/databox/resource-manager/Microsoft.DataBox/DataBox](#difference-271) | 4 | 3 | -1 | 1 | 25.00% |
| [specification/databoxedge/resource-manager/Microsoft.DataBoxEdge/DataBoxEdge](#difference-272) | 2 | 1 | -1 | 1 | 50.00% |
| [specification/deviceprovisioningservices/resource-manager/Microsoft.Devices/DeviceProvisioningServices](#difference-273) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/deviceupdate/resource-manager/Microsoft.DeviceUpdate/DuDeviceRegistry](#difference-274) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/devopsinfrastructure/resource-manager/Microsoft.DevOpsInfrastructure/DevOpsInfrastructure](#difference-275) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/dns/resource-manager/Microsoft.Network/Dns](#difference-276) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/durabletask/resource-manager/Microsoft.DurableTask/DurableTask](#difference-277) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/edge/resource-manager/Microsoft.Edge/configurations](#difference-278) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/edge/resource-manager/Microsoft.Edge/disconnectedOperations](#difference-279) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/elastic/resource-manager/Microsoft.Elastic/Elastic](#difference-280) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/fabric/resource-manager/Microsoft.Fabric/Fabric](#difference-281) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/frontdoor/resource-manager/Microsoft.Network/FrontDoor](#difference-282) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/gcpconnector/resource-manager/Microsoft.GcpConnector/BigQueryDataset](#difference-283) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/gcpconnector/resource-manager/Microsoft.GcpConnector/CloudFunction](#difference-284) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/gcpconnector/resource-manager/Microsoft.GcpConnector/SQLAdminInstances](#difference-285) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/gcpconnector/resource-manager/Microsoft.GcpConnector/StorageBucket](#difference-286) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/hanaonazure/resource-manager/Microsoft.HanaOnAzure/HanaOnAzure](#difference-287) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight](#difference-288) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/hybridaks/resource-manager/Microsoft.HybridContainerService/HybridContainerService](#difference-289) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/imagebuilder/resource-manager/Microsoft.VirtualMachineImages/ImageBuilder](#difference-290) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/iothub/resource-manager/Microsoft.Devices/IoTHub](#difference-291) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/iotoperations/resource-manager/Microsoft.IoTOperations/IoTOperations](#difference-292) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/privateLinkScopes](#difference-293) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/liftrastronomer/resource-manager/Astronomer.Astro/AstronomerAstro](#difference-294) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/liftrqumulo/resource-manager/Qumulo.Storage/QumuloStorage](#difference-295) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/loadtestservice/resource-manager/Microsoft.LoadTestService/loadtesting](#difference-296) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/logic/resource-manager/Microsoft.Logic/Logic](#difference-297) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/management/resource-manager/Microsoft.Management/ManagementGroups](#difference-298) | 2 | 1 | -1 | 1 | 50.00% |
| [specification/migrate/resource-manager/Microsoft.Migrate/AssessmentProjects](#difference-299) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/mongocluster/resource-manager/Microsoft.DocumentDB/MongoCluster](#difference-300) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/monitor/resource-manager/Microsoft.Insights/Insights/ActivityLogAlertsApi](#difference-301) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/monitor/resource-manager/Microsoft.Insights/Insights/AutoScaleApi](#difference-302) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/monitor/resource-manager/Microsoft.Insights/Insights/LogProfilesApi](#difference-303) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/monitor/resource-manager/Microsoft.Insights/Insights/PrivateLinkScopesApi](#difference-304) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/monitor/resource-manager/Microsoft.Insights/Insights/ScheduledQueryRuleApi](#difference-305) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/monitoringservice/resource-manager/Microsoft.Monitor/Accounts](#difference-306) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/monitoringservice/resource-manager/Microsoft.Monitor/PipelineGroups](#difference-307) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity](#difference-308) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/newrelic/resource-manager/NewRelic.Observability/NewRelicObservability](#difference-309) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/nginx/resource-manager/Nginx.NginxPlus/NginxPlus](#difference-310) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/portal/resource-manager/Microsoft.Portal/Portal](#difference-311) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/programenrollment/resource-manager/Microsoft.ProgramEnrollment/ProgramEnrollment](#difference-312) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/purview/resource-manager/Microsoft.Purview/Purview](#difference-313) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/quantum/resource-manager/Microsoft.Quantum/Quantum](#difference-314) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/OpenShiftClusters](#difference-315) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/redisenterprise/resource-manager/Microsoft.Cache/RedisEnterprise](#difference-316) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/resourceconnector/resource-manager/Microsoft.ResourceConnector/ResourceConnector](#difference-317) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/resourcegraph/resource-manager/Microsoft.ResourceGraph/ResourceGraph/GraphQueryApi](#difference-318) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/resources/resource-manager/Microsoft.Resources/resources](#difference-319) | 3 | 2 | -1 | 1 | 33.33% |
| [specification/security/resource-manager/Microsoft.Security/Security/AutomationsAPI](#difference-320) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/security/resource-manager/Microsoft.Security/Security/IoTSecurityAPI](#difference-321) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/security/resource-manager/Microsoft.Security/Security/PrivateLinksAPI](#difference-322) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/security/resource-manager/Microsoft.Security/Security/ServiceEntitlementsAPI](#difference-323) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/sphere/resource-manager/Microsoft.AzureSphere/AzureSphere](#difference-324) | 2 | 1 | -1 | 1 | 50.00% |
| [specification/storageactions/resource-manager/Microsoft.StorageActions/StorageActions](#difference-325) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/verifiedid/resource-manager/Microsoft.VerifiedId/VerifiedId](#difference-326) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/widget/resource-manager/Microsoft.Widget/Widget](#difference-327) | 1 | 0 | -1 | 1 | 100.00% |
| [specification/workloads/resource-manager/Microsoft.Workloads/monitors](#difference-328) | 1 | 0 | -1 | 1 | 100.00% |

Relative gap uses `abs(TypeSpec - Swagger) / max(TypeSpec, Swagger, 1)`.
All exact observations, including equal-count and zero-count projects,
are retained in [projects.json](projects.json). Matching totals do not
prove matching defects. Unsupported common-unit counts remain unassessed.

<a id="difference-0"></a>
## specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric

Reported diagnostics: Swagger **93**, TypeSpec **13**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/accessControlLists/{accessControlListName}","patch","parameters"]` | controlPlaneAclConfiguration property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/accessControlLists/{accessControlListName}","patch","parameters"]` | defaultAction property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/accessControlLists/{accessControlListName}","patch","parameters"]` | dynamicMatchConfigurations property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/accessControlLists/{accessControlListName}","patch","parameters"]` | enableCount property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/accessControlLists/{accessControlListName}","patch","parameters"]` | matchConfigurations property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/accessControlLists/{accessControlListName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/internetGatewayRules/{internetGatewayRuleName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/internetGateways/{internetGatewayName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/ipCommunities/{ipCommunityName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/ipExtendedCommunities/{ipExtendedCommunityName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/ipPrefixes/{ipPrefixName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l2IsolationDomains/{l2IsolationDomainName}","patch","parameters"]` | extendedVlan property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l2IsolationDomains/{l2IsolationDomainName}","patch","parameters"]` | mtu property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l2IsolationDomains/{l2IsolationDomainName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l2IsolationDomains/{l2IsolationDomainName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}","patch","parameters"]` | exportPolicies property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}","patch","parameters"]` | ipv4Routes property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}","patch","parameters"]` | ipv6Routes property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}","patch","parameters"]` | redistributeConnectedSubnets property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}","patch","parameters"]` | redistributeStaticRoutes property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/externalNetworks/{externalNetworkName}","patch","parameters"]` | administrativeState property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/externalNetworks/{externalNetworkName}","patch","parameters"]` | configurationState property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/externalNetworks/{externalNetworkName}","patch","parameters"]` | intervalInMilliSeconds property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/externalNetworks/{externalNetworkName}","patch","parameters"]` | mtu property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/externalNetworks/{externalNetworkName}","patch","parameters"]` | multiplier property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/externalNetworks/{externalNetworkName}","patch","parameters"]` | prefixLimits property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/externalNetworks/{externalNetworkName}","patch","parameters"]` | v4OverV6BgpSession property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/externalNetworks/{externalNetworkName}","patch","parameters"]` | v6OverV4BgpSession property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/internalNetworks/{internalNetworkName}","patch","parameters"]` | administrativeState property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/internalNetworks/{internalNetworkName}","patch","parameters"]` | allowAS property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/internalNetworks/{internalNetworkName}","patch","parameters"]` | connectedIPv4Subnets property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/internalNetworks/{internalNetworkName}","patch","parameters"]` | connectedIPv6Subnets property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/internalNetworks/{internalNetworkName}","patch","parameters"]` | intervalInMilliSeconds property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/internalNetworks/{internalNetworkName}","patch","parameters"]` | isMonitoringEnabled property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/internalNetworks/{internalNetworkName}","patch","parameters"]` | mtu property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/internalNetworks/{internalNetworkName}","patch","parameters"]` | multiplier property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/internalNetworks/{internalNetworkName}","patch","parameters"]` | neighborIpExclusions property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/internalNetworks/{internalNetworkName}","patch","parameters"]` | prefixLimits property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/internalNetworks/{internalNetworkName}","patch","parameters"]` | v4OverV6BgpSession property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/internalNetworks/{internalNetworkName}","patch","parameters"]` | v6OverV4BgpSession property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/neighborGroups/{neighborGroupName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/neighborGroups/{neighborGroupName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkBootstrapDevices/{networkBootstrapDeviceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkBootstrapDevices/{networkBootstrapDeviceName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkDevices/{networkDeviceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkDevices/{networkDeviceName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkDevices/{networkDeviceName}/networkInterfaces/{networkInterfaceName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabricControllers/{networkFabricControllerName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabricControllers/{networkFabricControllerName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}","patch","parameters"]` | administrativeState property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}","patch","parameters"]` | intervalInMilliSeconds property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}","patch","parameters"]` | ipv6Prefix property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}","patch","parameters"]` | mtu property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}","patch","parameters"]` | multiplier property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}","patch","parameters"]` | nniDerivedUniqueRdConfigurationState property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}","patch","parameters"]` | qosConfigurationState property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}","patch","parameters"]` | trustedIpPrefixes property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}","patch","parameters"]` | uniqueRdConfigurationState property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}/networkToNetworkInterconnects/{networkToNetworkInterconnectName}","patch","parameters"]` | administrativeState property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}/networkToNetworkInterconnects/{networkToNetworkInterconnectName}","patch","parameters"]` | configurationState property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}/networkToNetworkInterconnects/{networkToNetworkInterconnectName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}/networkToNetworkInterconnects/{networkToNetworkInterconnectName}","patch","parameters"]` | intervalInMilliSeconds property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}/networkToNetworkInterconnects/{networkToNetworkInterconnectName}","patch","parameters"]` | mtu property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}/networkToNetworkInterconnects/{networkToNetworkInterconnectName}","patch","parameters"]` | multiplier property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}/networkToNetworkInterconnects/{networkToNetworkInterconnectName}","patch","parameters"]` | prefixLimits property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}/networkToNetworkInterconnects/{networkToNetworkInterconnectName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkMonitors/{networkMonitorName}","patch","parameters"]` | exportPolicies property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkMonitors/{networkMonitorName}","patch","parameters"]` | exportPolicy property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkMonitors/{networkMonitorName}","patch","parameters"]` | keepaliveIdleTime property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkMonitors/{networkMonitorName}","patch","parameters"]` | monitoredAddressFamilies property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkMonitors/{networkMonitorName}","patch","parameters"]` | probeCount property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkMonitors/{networkMonitorName}","patch","parameters"]` | probeInterval property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkMonitors/{networkMonitorName}","patch","parameters"]` | stationPort property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkMonitors/{networkMonitorName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkPacketBrokers/{networkPacketBrokerName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkPacketBrokers/{networkPacketBrokerName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkRacks/{networkRackName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkTapRules/{networkTapRuleName}","patch","parameters"]` | dynamicMatchConfigurations property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkTapRules/{networkTapRuleName}","patch","parameters"]` | enableCount property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkTapRules/{networkTapRuleName}","patch","parameters"]` | matchConfigurations property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkTapRules/{networkTapRuleName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkTapRules/{networkTapRuleName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkTaps/{networkTapName}","patch","parameters"]` | destinations property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkTaps/{networkTapName}","patch","parameters"]` | pollingType property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkTaps/{networkTapName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkTaps/{networkTapName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/routePolicies/{routePolicyName}","patch","parameters"]` | defaultAction property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/routePolicies/{routePolicyName}","patch","parameters"]` | statements property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/swagger/stable/2025-07-15/managednetworkfabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/routePolicies/{routePolicyName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models/InternalNetwork.tsp:324:3` | The property 'connectedIPv4SubnetsDeprecated' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models/InternalNetwork.tsp:338:3` | The property 'connectedIPv6SubnetsDeprecated' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models/InternalNetwork.tsp:613:3` | The property 'neighborIpExclusionsDeprecated' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models/L3IsolationDomain.tsp:100:3` | The property 'ipv4RoutesDeprecated' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models/L3IsolationDomain.tsp:112:3` | The property 'ipv6RoutesDeprecated' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models/NetworkFabric.tsp:403:3` | The property 'primaryIpv6Prefix' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models/NetworkInterface.tsp:89:3` | The property 'description' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models/NetworkTapRule.tsp:225:3` | The property 'dynamicMatchConfigurationsDeprecated' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models/NetworkToNetworkInterconnect.tsp:262:3` | The property 'prefixLimitsDeprecated' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models/NetworkToNetworkInterconnect.tsp:333:3` | The property 'ipv4RoutesDeprecated' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models/NetworkToNetworkInterconnect.tsp:345:3` | The property 'ipv6RoutesDeprecated' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models/common.tsp:1085:3` | The property 'prefixLimitsDeprecated' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models/common.tsp:1110:3` | The property 'prefixLimitsDeprecated' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-1"></a>
## specification/web/resource-manager/Microsoft.Web/AppService

Reported diagnostics: Swagger **53**, TypeSpec **1**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/aigateways/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name}","patch","parameters"]` | keyVaultId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name}","patch","parameters"]` | keyVaultSecretName property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name}","patch","parameters"]` | kind property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name}","patch","parameters"]` | password property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name}","patch","parameters"]` | serverFarmId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/kubeEnvironments/{name}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/kubeEnvironments/{name}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/kubeEnvironments/{name}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}","patch","parameters"]` | hyperV property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}","patch","parameters"]` | isXenon property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}","patch","parameters"]` | kind property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}","patch","parameters"]` | perSiteScaling property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}","patch","parameters"]` | reserved property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}","patch","parameters"]` | zoneRedundant property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}","patch","parameters"]` | clientAffinityEnabled property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}","patch","parameters"]` | hostNamesDisabled property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/certificates/{certificateName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/certificates/{certificateName}","patch","parameters"]` | keyVaultId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/certificates/{certificateName}","patch","parameters"]` | keyVaultSecretName property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/certificates/{certificateName}","patch","parameters"]` | kind property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/certificates/{certificateName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/certificates/{certificateName}","patch","parameters"]` | password property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/certificates/{certificateName}","patch","parameters"]` | serverFarmId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/certificates/{certificateName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/premieraddons/{premierAddOnName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/premieraddons/{premierAddOnName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/premieraddons/{premierAddOnName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}","patch","parameters"]` | clientAffinityEnabled property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}","patch","parameters"]` | hostNamesDisabled property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/certificates/{certificateName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/certificates/{certificateName}","patch","parameters"]` | keyVaultId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/certificates/{certificateName}","patch","parameters"]` | keyVaultSecretName property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/certificates/{certificateName}","patch","parameters"]` | kind property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/certificates/{certificateName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/certificates/{certificateName}","patch","parameters"]` | password property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/certificates/{certificateName}","patch","parameters"]` | serverFarmId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/certificates/{certificateName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons/{premierAddOnName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons/{premierAddOnName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons/{premierAddOnName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/staticSites/{name}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/staticSites/{name}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/staticSites/{name}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:6560:3` | The property 'containerAppsConfiguration' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-2"></a>
## specification/netapp/resource-manager/Microsoft.NetApp/NetApp

Reported diagnostics: Swagger **49**, TypeSpec **2**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/activeDirectoryConfigs/{activeDirectoryConfigName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/activeDirectoryConfigs/{activeDirectoryConfigName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/elasticAccounts/{accountName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/elasticAccounts/{accountName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/elasticAccounts/{accountName}/elasticBackupPolicies/{backupPolicyName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/elasticAccounts/{accountName}/elasticBackupVaults/{backupVaultName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/elasticAccounts/{accountName}/elasticCapacityPools/{poolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/elasticAccounts/{accountName}/elasticCapacityPools/{poolName}/elasticVolumes/{volumeName}","patch","parameters"]` | smbEncryption property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/elasticAccounts/{accountName}/elasticCapacityPools/{poolName}/elasticVolumes/{volumeName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/elasticAccounts/{accountName}/elasticSnapshotPolicies/{snapshotPolicyName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}","patch","parameters"]` | bindAuthenticationLevel property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}","patch","parameters"]` | secureLdapType property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/backupPolicies/{backupPolicyName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/backupPolicies/{backupPolicyName}","patch","parameters"]` | location property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/backupPolicies/{backupPolicyName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/backupPolicies/{backupPolicyName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/backupPolicies/{backupPolicyName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/backupVaults/{backupVaultName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}","patch","parameters"]` | coolAccess property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}","patch","parameters"]` | location property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}","patch","parameters"]` | qosType property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}","patch","parameters"]` | size property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/caches/{cacheName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}","patch","parameters"]` | coolAccess property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}","patch","parameters"]` | defaultGroupQuotaInKiBs property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}","patch","parameters"]` | defaultUserQuotaInKiBs property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}","patch","parameters"]` | isDefaultQuotaEnabled property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}","patch","parameters"]` | location property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}","patch","parameters"]` | serviceLevel property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}","patch","parameters"]` | snapshotDirectoryVisible property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}","patch","parameters"]` | throughputMibps property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}","patch","parameters"]` | usageThreshold property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/buckets/{bucketName}","patch","parameters"]` | permissions property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/subvolumes/{subvolumeName}","patch","parameters"]` | path property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/volumeQuotaRules/{volumeQuotaRuleName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/snapshotPolicies/{snapshotPolicyName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/snapshotPolicies/{snapshotPolicyName}","patch","parameters"]` | location property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/snapshotPolicies/{snapshotPolicyName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/snapshotPolicies/{snapshotPolicyName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/swagger/preview/2026-06-15-preview/netapp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/snapshotPolicies/{snapshotPolicyName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `Snapshot.tsp:116:3` | The PATCH request body must contain at least one property. | 1 |
| TypeSpec linter | `Volume.tsp:1361:3` | The property 'usageThreshold20250901' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-3"></a>
## specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement

Reported diagnostics: Swagger **41**, TypeSpec **2**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/gateways/{gatewayName}","patch","parameters"]` | etag property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/gateways/{gatewayName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/gateways/{gatewayName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/gateways/{gatewayName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/gateways/{gatewayName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}","patch","parameters"]` | etag property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}","patch","parameters"]` | zones property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}","patch","parameters"]` | displayName property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}","patch","parameters"]` | serviceUrl property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}","patch","parameters"]` | method property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/backends/{backendId}","patch","parameters"]` | url property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/identityProviders/{identityProviderName}","patch","parameters"]` | clientSecret property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/loggers/{loggerId}","patch","parameters"]` | credentials property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/loggers/{loggerId}","patch","parameters"]` | description property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/namedValues/{namedValueId}","patch","parameters"]` | value property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/subscriptions/{sid}","patch","parameters"]` | displayName property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/subscriptions/{sid}","patch","parameters"]` | expirationDate property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/subscriptions/{sid}","patch","parameters"]` | ownerId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/subscriptions/{sid}","patch","parameters"]` | primaryKey property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/subscriptions/{sid}","patch","parameters"]` | scope property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/subscriptions/{sid}","patch","parameters"]` | secondaryKey property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/subscriptions/{sid}","patch","parameters"]` | stateComment property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/users/{userId}","patch","parameters"]` | password property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/apis/{apiId}","patch","parameters"]` | displayName property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/apis/{apiId}","patch","parameters"]` | serviceUrl property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/apis/{apiId}/operations/{operationId}","patch","parameters"]` | method property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/backends/{backendId}","patch","parameters"]` | url property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/loggers/{loggerId}","patch","parameters"]` | credentials property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/loggers/{loggerId}","patch","parameters"]` | description property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/namedValues/{namedValueId}","patch","parameters"]` | value property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/subscriptions/{sid}","patch","parameters"]` | displayName property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/subscriptions/{sid}","patch","parameters"]` | expirationDate property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/subscriptions/{sid}","patch","parameters"]` | ownerId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/subscriptions/{sid}","patch","parameters"]` | primaryKey property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/subscriptions/{sid}","patch","parameters"]` | scope property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/subscriptions/{sid}","patch","parameters"]` | secondaryKey property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/subscriptions/{sid}","patch","parameters"]` | stateComment property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:10095:3` | The property 'expirationDate' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:10124:3` | The property 'stateComment' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-4"></a>
## specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery

Reported diagnostics: Swagger **36**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}/versions/{galleryImageVersionName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}/versions/{galleryImageVersionName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}/versions/{galleryImageVersionName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}/versions/{galleryImageVersionName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/inVMAccessControlProfiles/{inVMAccessControlProfileName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/inVMAccessControlProfiles/{inVMAccessControlProfileName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/inVMAccessControlProfiles/{inVMAccessControlProfileName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/inVMAccessControlProfiles/{inVMAccessControlProfileName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/inVMAccessControlProfiles/{inVMAccessControlProfileName}/versions/{inVMAccessControlProfileVersionName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/inVMAccessControlProfiles/{inVMAccessControlProfileName}/versions/{inVMAccessControlProfileVersionName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/inVMAccessControlProfiles/{inVMAccessControlProfileName}/versions/{inVMAccessControlProfileVersionName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/inVMAccessControlProfiles/{inVMAccessControlProfileName}/versions/{inVMAccessControlProfileVersionName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/scripts/{galleryScriptName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/scripts/{galleryScriptName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/scripts/{galleryScriptName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/scripts/{galleryScriptName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/scripts/{galleryScriptName}/versions/{galleryScriptVersionName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/scripts/{galleryScriptName}/versions/{galleryScriptVersionName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/scripts/{galleryScriptName}/versions/{galleryScriptVersionName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeGallery/swagger/stable/2026-03-03/GalleryRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/scripts/{galleryScriptName}/versions/{galleryScriptVersionName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-5"></a>
## specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid

Reported diagnostics: Swagger **34**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}","patch","parameters"]` | autoCreateTopicWithFirstSubscription property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}","patch","parameters"]` | autoDeleteTopicWithLastSubscription property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}","patch","parameters"]` | disableLocalAuth property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}","patch","parameters"]` | publicNetworkAccess property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/eventSubscriptions/{eventSubscriptionName}","patch","parameters"]` | eventDeliverySchema property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/eventSubscriptions/{eventSubscriptionName}","patch","parameters"]` | expirationTimeUtc property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/topics/{topicName}/eventSubscriptions/{eventSubscriptionName}","patch","parameters"]` | eventDeliverySchema property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/topics/{topicName}/eventSubscriptions/{eventSubscriptionName}","patch","parameters"]` | expirationTimeUtc property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/namespaces/{namespaceName}","patch","parameters"]` | customDomains property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/namespaces/{namespaceName}","patch","parameters"]` | routeTopicResourceId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/namespaces/{namespaceName}","patch","parameters"]` | state property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/namespaces/{namespaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerConfigurations/default","patch","parameters"]` | defaultMaximumExpirationTimeInDays property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerConfigurations/default","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerDestinations/{partnerDestinationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerNamespaces/{partnerNamespaceName}","patch","parameters"]` | disableLocalAuth property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerNamespaces/{partnerNamespaceName}","patch","parameters"]` | publicNetworkAccess property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerNamespaces/{partnerNamespaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerNamespaces/{partnerNamespaceName}/channels/{channelName}","patch","parameters"]` | expirationTimeIfNotActivatedUtc property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerRegistrations/{partnerRegistrationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerTopics/{partnerTopicName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerTopics/{partnerTopicName}/eventSubscriptions/{eventSubscriptionName}","patch","parameters"]` | eventDeliverySchema property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerTopics/{partnerTopicName}/eventSubscriptions/{eventSubscriptionName}","patch","parameters"]` | expirationTimeUtc property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/systemTopics/{systemTopicName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/systemTopics/{systemTopicName}/eventSubscriptions/{eventSubscriptionName}","patch","parameters"]` | eventDeliverySchema property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/systemTopics/{systemTopicName}/eventSubscriptions/{eventSubscriptionName}","patch","parameters"]` | expirationTimeUtc property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}","patch","parameters"]` | disableLocalAuth property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}","patch","parameters"]` | publicNetworkAccess property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}/eventSubscriptions/{eventSubscriptionName}","patch","parameters"]` | eventDeliverySchema property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}/eventSubscriptions/{eventSubscriptionName}","patch","parameters"]` | expirationTimeUtc property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{eventSubscriptionName}","patch","parameters"]` | eventDeliverySchema property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json: ["paths","/{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{eventSubscriptionName}","patch","parameters"]` | expirationTimeUtc property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-6"></a>
## specification/compute/resource-manager/Microsoft.Compute/Compute/Compute

Reported diagnostics: Swagger **30**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}/capacityReservations/{capacityReservationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}","patch","parameters"]` | zones property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}/hosts/{hostName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/images/{imageName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/interconnectBlocks/{interconnectBlockName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/proximityPlacementGroups/{proximityPlacementGroupName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/restorePointCollections/{restorePointCollectionName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/sshPublicKeys/{sshPublicKeyName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}","patch","parameters"]` | customData property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}","patch","parameters"]` | dataDisks property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}","patch","parameters"]` | diskSizeGB property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}","patch","parameters"]` | licenseType property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}","patch","parameters"]` | networkInterfaceConfigurations property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}","patch","parameters"]` | secrets property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}","patch","parameters"]` | userData property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}","patch","parameters"]` | vhdContainers property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}","patch","parameters"]` | zones property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/diagnosticRunCommands/{runCommandName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/runCommands/{runCommandName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}","patch","parameters"]` | zones property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/diagnosticRunCommands/{runCommandName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/extensions/{vmExtensionName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/runCommands/{runCommandName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-7"></a>
## specification/mission/resource-manager/Microsoft.Mission/Mission

Reported diagnostics: Swagger **26**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/communities/{communityName}","patch","parameters"]` | destinationType property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/communities/{communityName}","patch","parameters"]` | diagnosticDestinations property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/communities/{communityName}","patch","parameters"]` | firewallSku property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/communities/{communityName}","patch","parameters"]` | justification property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/communities/{communityName}","patch","parameters"]` | mode property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/communities/{communityName}","patch","parameters"]` | principals property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/communities/{communityName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/communities/{communityName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/communities/{communityName}/communityEndpoints/{communityEndpointName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/communities/{communityName}/dedicatedHubs/{dedicatedHubName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/communities/{communityName}/transitHubs/{transitHubName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/enclaveConnections/{enclaveConnectionName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/virtualEnclaves/{virtualEnclaveName}","patch","parameters"]` | bastionEnabled property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/virtualEnclaves/{virtualEnclaveName}","patch","parameters"]` | destinationType property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/virtualEnclaves/{virtualEnclaveName}","patch","parameters"]` | diagnosticDestination property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/virtualEnclaves/{virtualEnclaveName}","patch","parameters"]` | diagnosticDestinations property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/virtualEnclaves/{virtualEnclaveName}","patch","parameters"]` | justification property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/virtualEnclaves/{virtualEnclaveName}","patch","parameters"]` | mode property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/virtualEnclaves/{virtualEnclaveName}","patch","parameters"]` | principals property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/virtualEnclaves/{virtualEnclaveName}","patch","parameters"]` | rbacInheritance property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/virtualEnclaves/{virtualEnclaveName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/virtualEnclaves/{virtualEnclaveName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/virtualEnclaves/{virtualEnclaveName}","patch","parameters"]` | workloadResourceVisibility property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/virtualEnclaves/{virtualEnclaveName}/enclaveEndpoints/{enclaveEndpointName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Mission/virtualEnclaves/{virtualEnclaveName}/workloads/{workloadName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mission/resource-manager/Microsoft.Mission/Mission/swagger/stable/2026-04-01/openapi.json: ["paths","/{resourceUri}/providers/Microsoft.Mission/approvals/{approvalName}","patch","parameters"]` | approvalStatus property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-8"></a>
## specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud

Reported diagnostics: Swagger **34**, TypeSpec **8**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/accessBridges/{accessBridgeName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/bareMetalMachines/{bareMetalMachineName}","patch","parameters"]` | machineDetails property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/bareMetalMachines/{bareMetalMachineName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/cloudServicesNetworks/{cloudServicesNetworkName}","patch","parameters"]` | enableDefaultEgressEndpoints property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/cloudServicesNetworks/{cloudServicesNetworkName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusterManagers/{clusterManagerName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusters/{clusterName}","patch","parameters"]` | bareMetalMachineConfigurationData property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusters/{clusterName}","patch","parameters"]` | clusterLocation property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusters/{clusterName}","patch","parameters"]` | computeRackDefinitions property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusters/{clusterName}","patch","parameters"]` | containerScan property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusters/{clusterName}","patch","parameters"]` | definitionUpdateMode property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusters/{clusterName}","patch","parameters"]` | enforcementLevel property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusters/{clusterName}","patch","parameters"]` | storageApplianceConfigurationData property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusters/{clusterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusters/{clusterName}","patch","parameters"]` | useKeyVault property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusters/{clusterName}","patch","parameters"]` | waitTimeMinutes property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusters/{clusterName}/bareMetalMachineKeySets/{bareMetalMachineKeySetName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusters/{clusterName}/bmcKeySets/{bmcKeySetName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusters/{clusterName}/metricsConfigurations/{metricsConfigurationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/kubernetesClusters/{kubernetesClusterName}","patch","parameters"]` | sshPublicKeys property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/kubernetesClusters/{kubernetesClusterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/kubernetesClusters/{kubernetesClusterName}/agentPools/{agentPoolName}","patch","parameters"]` | sshPublicKeys property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/kubernetesClusters/{kubernetesClusterName}/agentPools/{agentPoolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/kubernetesClusters/{kubernetesClusterName}/features/{featureName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/kubernetesVersions/{kubernetesVersionName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/l2Networks/{l2NetworkName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/l3Networks/{l3NetworkName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/racks/{rackName}","patch","parameters"]` | rackSerialNumber property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/racks/{rackName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/storageAppliances/{storageApplianceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/trunkedNetworks/{trunkedNetworkName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/virtualMachines/{virtualMachineName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/virtualMachines/{virtualMachineName}/consoles/{consoleName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud/swagger/preview/2026-08-01-preview/networkcloud.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/volumes/{volumeName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `clusters/Cluster_models.tsp:1580:3` | The property 'aggregatorOrSingleRackDefinition' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `clusters/Cluster_models.tsp:1596:3` | The property 'clusterServicePrincipal' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `clusters/Cluster_models.tsp:1607:3` | The property 'computeDeploymentThreshold' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `clusters/Cluster_models.tsp:1620:3` | The property 'runtimeProtectionConfiguration' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `clusters/Cluster_models.tsp:1626:3` | The property 'secretArchive' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `clusters/Cluster_models.tsp:1637:3` | The property 'updateStrategy' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `virtualmachines/Console_models.tsp:182:3` | The property 'sshPublicKey' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `virtualmachines/VirtualMachine_models.tsp:439:3` | The property 'vmImageRepositoryCredentials' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-9"></a>
## specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM

Reported diagnostics: Swagger **21**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/galleryImages/{galleryImageName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/loadBalancers/{loadBalancerName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/logicalNetworks/{logicalNetworkName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/marketplaceGalleryImages/{marketplaceGalleryImageName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/natGateways/{natGatewayName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/networkInterfaces/{networkInterfaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/networkSecurityGroups/{networkSecurityGroupName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/publicIPAddresses/{publicIPAddressName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/snapshots/{snapshotName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/storageContainers/{storageContainerName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/virtualHardDisks/{virtualHardDiskName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/virtualNetworks/{virtualNetworkName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/{resourceUri}/providers/Microsoft.AzureStackHCI/virtualMachineInstances/default","patch","parameters"]` | computerName property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/{resourceUri}/providers/Microsoft.AzureStackHCI/virtualMachineInstances/default","patch","parameters"]` | dataDisks property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/{resourceUri}/providers/Microsoft.AzureStackHCI/virtualMachineInstances/default","patch","parameters"]` | principalId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/{resourceUri}/providers/Microsoft.AzureStackHCI/virtualMachineInstances/default","patch","parameters"]` | provisionVMAgent property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/{resourceUri}/providers/Microsoft.AzureStackHCI/virtualMachineInstances/default","patch","parameters"]` | provisionVMConfigAgent property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/{resourceUri}/providers/Microsoft.AzureStackHCI/virtualMachineInstances/default","patch","parameters"]` | tenantId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/{resourceUri}/providers/Microsoft.AzureStackHCI/virtualMachineInstances/default","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/{resourceUri}/providers/Microsoft.AzureStackHCI/virtualMachineInstances/default","patch","parameters"]` | virtualMachineGPUs property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCIVM/swagger/preview/2026-04-01-preview/stackhcivm.json: ["paths","/{resourceUri}/providers/Microsoft.AzureStackHCI/virtualMachineInstances/default","patch","parameters"]` | vmSize property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-10"></a>
## specification/postgresql/DBforPostgreSQL.Management

Reported diagnostics: Swagger **21**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}","patch","parameters"]` | administratorLogin property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}","patch","parameters"]` | administratorLoginPassword property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}","patch","parameters"]` | availabilityZone property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}","patch","parameters"]` | backupRetentionDays property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}","patch","parameters"]` | createMode property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}","patch","parameters"]` | customWindow property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}","patch","parameters"]` | dayOfWeek property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}","patch","parameters"]` | fipsMode property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}","patch","parameters"]` | geoRedundantBackup property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}","patch","parameters"]` | mode property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}","patch","parameters"]` | passwordAuth property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}","patch","parameters"]` | sourceServerResourceId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}","patch","parameters"]` | startHour property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}","patch","parameters"]` | startMinute property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}","patch","parameters"]` | tenantId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/migrations/{migrationName}","patch","parameters"]` | sourceServerPassword property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/migrations/{migrationName}","patch","parameters"]` | sourceServerUsername property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/migrations/{migrationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/migrations/{migrationName}","patch","parameters"]` | targetServerPassword property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/migrations/{migrationName}","patch","parameters"]` | targetServerUsername property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-11"></a>
## specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices

Reported diagnostics: Swagger **21**, TypeSpec **3**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/registries/{registryName}","patch","parameters"]` | identity property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/registries/{registryName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/registries/{registryName}","patch","parameters"]` | size property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/registries/{registryName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}","patch","parameters"]` | keyIdentifier property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/batchEndpoints/{endpointName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/batchEndpoints/{endpointName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/batchEndpoints/{endpointName}/deployments/{deploymentName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName}","patch","parameters"]` | maxNodeCount property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName}","patch","parameters"]` | minNodeCount property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName}","patch","parameters"]` | nodeIdleTimeBeforeScaleDown property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/onlineEndpoints/{endpointName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/onlineEndpoints/{endpointName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/onlineEndpoints/{endpointName}/deployments/{deploymentName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/onlineEndpoints/{endpointName}/deployments/{deploymentName}","patch","parameters"]` | size property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/onlineEndpoints/{endpointName}/deployments/{deploymentName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/serverlessEndpoints/{name}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/serverlessEndpoints/{name}","patch","parameters"]` | size property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/serverlessEndpoints/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/serverlessEndpoints/{name}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:4311:3` | The property 'maxNodeCount' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:4316:3` | The property 'minNodeCount' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:4321:3` | The property 'nodeIdleTimeBeforeScaleDown' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-12"></a>
## specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization

Reported diagnostics: Swagger **16**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization/swagger/preview/2026-04-01-preview/desktopvirtualization.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/appAttachPackages/{appAttachPackageName}","patch","parameters"]` | hostPoolReferences property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization/swagger/preview/2026-04-01-preview/desktopvirtualization.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/appAttachPackages/{appAttachPackageName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization/swagger/preview/2026-04-01-preview/desktopvirtualization.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/applicationGroups/{applicationGroupName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization/swagger/preview/2026-04-01-preview/desktopvirtualization.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/applicationGroups/{applicationGroupName}/applications/{applicationName}","patch","parameters"]` | msixPackageApplicationId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization/swagger/preview/2026-04-01-preview/desktopvirtualization.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/applicationGroups/{applicationGroupName}/applications/{applicationName}","patch","parameters"]` | msixPackageFamilyName property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization/swagger/preview/2026-04-01-preview/desktopvirtualization.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/hostPools/{hostPoolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization/swagger/preview/2026-04-01-preview/desktopvirtualization.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/hostPools/{hostPoolName}/msixPackages/{msixPackageFullName}","patch","parameters"]` | displayName property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization/swagger/preview/2026-04-01-preview/desktopvirtualization.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/hostPools/{hostPoolName}/msixPackages/{msixPackageFullName}","patch","parameters"]` | isActive property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization/swagger/preview/2026-04-01-preview/desktopvirtualization.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/hostPools/{hostPoolName}/msixPackages/{msixPackageFullName}","patch","parameters"]` | isRegularRegistration property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization/swagger/preview/2026-04-01-preview/desktopvirtualization.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/hostPools/{hostPoolName}/sessionHostConfigurations/default","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization/swagger/preview/2026-04-01-preview/desktopvirtualization.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/hostPools/{hostPoolName}/sessionHostManagements/default","patch","parameters"]` | logOffMessage property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization/swagger/preview/2026-04-01-preview/desktopvirtualization.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/scalingPlans/{scalingPlanName}","patch","parameters"]` | schedules property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization/swagger/preview/2026-04-01-preview/desktopvirtualization.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/scalingPlans/{scalingPlanName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization/swagger/preview/2026-04-01-preview/desktopvirtualization.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/scalingPlans/{scalingPlanName}/pooledSchedules/{scalingPlanScheduleName}","patch","parameters"]` | scalingMethod property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization/swagger/preview/2026-04-01-preview/desktopvirtualization.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/workspaces/{workspaceName}","patch","parameters"]` | applicationGroupReferences property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization/swagger/preview/2026-04-01-preview/desktopvirtualization.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/workspaces/{workspaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-13"></a>
## specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry

Reported diagnostics: Swagger **18**, TypeSpec **2**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry/swagger/preview/2026-11-02-preview/deviceregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/assetEndpointProfiles/{assetEndpointProfileName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry/swagger/preview/2026-11-02-preview/deviceregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/assets/{assetName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry/swagger/preview/2026-11-02-preview/deviceregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/namespaces/{namespaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry/swagger/preview/2026-11-02-preview/deviceregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/namespaces/{namespaceName}/assets/{assetName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry/swagger/preview/2026-11-02-preview/deviceregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/namespaces/{namespaceName}/certificateAuthorities/{certificateAuthorityName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry/swagger/preview/2026-11-02-preview/deviceregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/namespaces/{namespaceName}/devices/{deviceName}","patch","parameters"]` | assigned property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry/swagger/preview/2026-11-02-preview/deviceregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/namespaces/{namespaceName}/devices/{deviceName}","patch","parameters"]` | enabled property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry/swagger/preview/2026-11-02-preview/deviceregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/namespaces/{namespaceName}/devices/{deviceName}","patch","parameters"]` | inbound property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry/swagger/preview/2026-11-02-preview/deviceregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/namespaces/{namespaceName}/devices/{deviceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry/swagger/preview/2026-11-02-preview/deviceregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/namespaces/{namespaceName}/devices/{deviceName}","patch","parameters"]` | unassigned property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry/swagger/preview/2026-11-02-preview/deviceregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/namespaces/{namespaceName}/discoveredAssets/{discoveredAssetName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry/swagger/preview/2026-11-02-preview/deviceregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/namespaces/{namespaceName}/discoveredDevices/{discoveredDeviceName}","patch","parameters"]` | assigned property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry/swagger/preview/2026-11-02-preview/deviceregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/namespaces/{namespaceName}/discoveredDevices/{discoveredDeviceName}","patch","parameters"]` | inbound property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry/swagger/preview/2026-11-02-preview/deviceregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/namespaces/{namespaceName}/discoveredDevices/{discoveredDeviceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry/swagger/preview/2026-11-02-preview/deviceregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/namespaces/{namespaceName}/groups/{groupName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry/swagger/preview/2026-11-02-preview/deviceregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/namespaces/{namespaceName}/jobs/{jobName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry/swagger/preview/2026-11-02-preview/deviceregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/namespaces/{namespaceName}/registryDevices/{registryDeviceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/deviceregistry/resource-manager/Microsoft.DeviceRegistry/DeviceRegistry/swagger/preview/2026-11-02-preview/deviceregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceRegistry/schemaRegistries/{schemaRegistryName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `ns_policy.tsp:66:3` | The property 'certificateAuthorityConfiguration' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `ns_policy.tsp:94:3` | The property 'bringYourOwnRoot' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-14"></a>
## specification/recoveryservicesdatareplication/resource-manager/Microsoft.DataReplication/DataReplication

Reported diagnostics: Swagger **14**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/recoveryservicesdatareplication/resource-manager/Microsoft.DataReplication/DataReplication/swagger/stable/2026-05-01/recoveryservicesdatareplication.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataReplication/replicationFabrics/{fabricName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicesdatareplication/resource-manager/Microsoft.DataReplication/DataReplication/swagger/stable/2026-05-01/recoveryservicesdatareplication.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataReplication/replicationFabrics/{fabricName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicesdatareplication/resource-manager/Microsoft.DataReplication/DataReplication/swagger/stable/2026-05-01/recoveryservicesdatareplication.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataReplication/replicationFabrics/{fabricName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicesdatareplication/resource-manager/Microsoft.DataReplication/DataReplication/swagger/stable/2026-05-01/recoveryservicesdatareplication.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataReplication/replicationFabrics/{fabricName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicesdatareplication/resource-manager/Microsoft.DataReplication/DataReplication/swagger/stable/2026-05-01/recoveryservicesdatareplication.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataReplication/replicationVaults/{vaultName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicesdatareplication/resource-manager/Microsoft.DataReplication/DataReplication/swagger/stable/2026-05-01/recoveryservicesdatareplication.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataReplication/replicationVaults/{vaultName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicesdatareplication/resource-manager/Microsoft.DataReplication/DataReplication/swagger/stable/2026-05-01/recoveryservicesdatareplication.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataReplication/replicationVaults/{vaultName}","patch","parameters"]` | principalId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicesdatareplication/resource-manager/Microsoft.DataReplication/DataReplication/swagger/stable/2026-05-01/recoveryservicesdatareplication.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataReplication/replicationVaults/{vaultName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicesdatareplication/resource-manager/Microsoft.DataReplication/DataReplication/swagger/stable/2026-05-01/recoveryservicesdatareplication.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataReplication/replicationVaults/{vaultName}","patch","parameters"]` | tenantId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicesdatareplication/resource-manager/Microsoft.DataReplication/DataReplication/swagger/stable/2026-05-01/recoveryservicesdatareplication.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataReplication/replicationVaults/{vaultName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicesdatareplication/resource-manager/Microsoft.DataReplication/DataReplication/swagger/stable/2026-05-01/recoveryservicesdatareplication.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataReplication/replicationVaults/{vaultName}/protectedItems/{protectedItemName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicesdatareplication/resource-manager/Microsoft.DataReplication/DataReplication/swagger/stable/2026-05-01/recoveryservicesdatareplication.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataReplication/replicationVaults/{vaultName}/protectedItems/{protectedItemName}","patch","parameters"]` | instanceType property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicesdatareplication/resource-manager/Microsoft.DataReplication/DataReplication/swagger/stable/2026-05-01/recoveryservicesdatareplication.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataReplication/replicationVaults/{vaultName}/protectedItems/{protectedItemName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicesdatareplication/resource-manager/Microsoft.DataReplication/DataReplication/swagger/stable/2026-05-01/recoveryservicesdatareplication.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataReplication/replicationVaults/{vaultName}/protectedItems/{protectedItemName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-15"></a>
## specification/devcenter/resource-manager/Microsoft.DevCenter/DevCenter

Reported diagnostics: Swagger **13**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/devcenter/resource-manager/Microsoft.DevCenter/DevCenter/swagger/preview/2026-01-01-preview/DevCenterRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/devcenters/{devCenterName}","patch","parameters"]` | location property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devcenter/resource-manager/Microsoft.DevCenter/DevCenter/swagger/preview/2026-01-01-preview/DevCenterRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/devcenters/{devCenterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devcenter/resource-manager/Microsoft.DevCenter/DevCenter/swagger/preview/2026-01-01-preview/DevCenterRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/devcenters/{devCenterName}/devboxdefinitions/{devBoxDefinitionName}","patch","parameters"]` | location property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devcenter/resource-manager/Microsoft.DevCenter/DevCenter/swagger/preview/2026-01-01-preview/DevCenterRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/devcenters/{devCenterName}/devboxdefinitions/{devBoxDefinitionName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devcenter/resource-manager/Microsoft.DevCenter/DevCenter/swagger/preview/2026-01-01-preview/DevCenterRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/devcenters/{devCenterName}/encryptionSets/{encryptionSetName}","patch","parameters"]` | location property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devcenter/resource-manager/Microsoft.DevCenter/DevCenter/swagger/preview/2026-01-01-preview/DevCenterRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/devcenters/{devCenterName}/encryptionSets/{encryptionSetName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devcenter/resource-manager/Microsoft.DevCenter/DevCenter/swagger/preview/2026-01-01-preview/DevCenterRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/networkConnections/{networkConnectionName}","patch","parameters"]` | location property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devcenter/resource-manager/Microsoft.DevCenter/DevCenter/swagger/preview/2026-01-01-preview/DevCenterRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/networkConnections/{networkConnectionName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devcenter/resource-manager/Microsoft.DevCenter/DevCenter/swagger/preview/2026-01-01-preview/DevCenterRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/projects/{projectName}","patch","parameters"]` | location property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devcenter/resource-manager/Microsoft.DevCenter/DevCenter/swagger/preview/2026-01-01-preview/DevCenterRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/projects/{projectName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devcenter/resource-manager/Microsoft.DevCenter/DevCenter/swagger/preview/2026-01-01-preview/DevCenterRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/projects/{projectName}/environmentTypes/{environmentTypeName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devcenter/resource-manager/Microsoft.DevCenter/DevCenter/swagger/preview/2026-01-01-preview/DevCenterRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/projects/{projectName}/pools/{poolName}","patch","parameters"]` | location property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devcenter/resource-manager/Microsoft.DevCenter/DevCenter/swagger/preview/2026-01-01-preview/DevCenterRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/projects/{projectName}/pools/{poolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-16"></a>
## specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs

Reported diagnostics: Swagger **13**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/swagger/stable/2018-09-15/DTL.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/swagger/stable/2018-09-15/DTL.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/customimages/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/swagger/stable/2018-09-15/DTL.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/notificationchannels/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/swagger/stable/2018-09-15/DTL.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/schedules/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/swagger/stable/2018-09-15/DTL.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/swagger/stable/2018-09-15/DTL.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/disks/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/swagger/stable/2018-09-15/DTL.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/environments/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/swagger/stable/2018-09-15/DTL.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/secrets/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/swagger/stable/2018-09-15/DTL.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/swagger/stable/2018-09-15/DTL.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines/{virtualMachineName}/schedules/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/swagger/stable/2018-09-15/DTL.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualnetworks/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/swagger/stable/2018-09-15/DTL.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs/swagger/stable/2018-09-15/DTL.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/schedules/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-17"></a>
## specification/storage/resource-manager/Microsoft.Storage/Storage

Reported diagnostics: Swagger **13**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/storage/resource-manager/Microsoft.Storage/Storage/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/contextCaches/{contextCacheName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storage/resource-manager/Microsoft.Storage/Storage/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/contextCaches/{contextCacheName}/contextCacheContainers/{contextCacheContainerName}","patch","parameters"]` | timeToLive property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storage/resource-manager/Microsoft.Storage/Storage/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}","patch","parameters"]` | supportsHttpsTrafficOnly property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storage/resource-manager/Microsoft.Storage/Storage/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storage/resource-manager/Microsoft.Storage/Storage/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobAccessPointConfigurations/{blobAccessPointConfigurationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storage/resource-manager/Microsoft.Storage/Storage/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/connectors/{connectorName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storage/resource-manager/Microsoft.Storage/Storage/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/dataShares/{dataShareName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storage/resource-manager/Microsoft.Storage/Storage/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/storageTaskAssignments/{storageTaskAssignmentName}","patch","parameters"]` | endBy property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storage/resource-manager/Microsoft.Storage/Storage/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/storageTaskAssignments/{storageTaskAssignmentName}","patch","parameters"]` | interval property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storage/resource-manager/Microsoft.Storage/Storage/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/storageTaskAssignments/{storageTaskAssignmentName}","patch","parameters"]` | prefix property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storage/resource-manager/Microsoft.Storage/Storage/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/storageTaskAssignments/{storageTaskAssignmentName}","patch","parameters"]` | startFrom property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storage/resource-manager/Microsoft.Storage/Storage/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/storageTaskAssignments/{storageTaskAssignmentName}","patch","parameters"]` | startOn property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storage/resource-manager/Microsoft.Storage/Storage/swagger/stable/2026-09-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/storageTaskAssignments/{storageTaskAssignmentName}","patch","parameters"]` | taskId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-18"></a>
## specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits

Reported diagnostics: Swagger **14**, TypeSpec **2**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits/swagger/stable/2026-06-01/billingbenefits.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BillingBenefits/conditionalCredits/{conditionalCreditName}","patch","parameters"]` | allowContributors property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits/swagger/stable/2026-06-01/billingbenefits.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BillingBenefits/conditionalCredits/{conditionalCreditName}","patch","parameters"]` | endAt property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits/swagger/stable/2026-06-01/billingbenefits.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BillingBenefits/conditionalCredits/{conditionalCreditName}","patch","parameters"]` | milestones property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits/swagger/stable/2026-06-01/billingbenefits.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BillingBenefits/conditionalCredits/{conditionalCreditName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits/swagger/stable/2026-06-01/billingbenefits.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BillingBenefits/credits/{creditName}","patch","parameters"]` | breakdown property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits/swagger/stable/2026-06-01/billingbenefits.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BillingBenefits/credits/{creditName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits/swagger/stable/2026-06-01/billingbenefits.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BillingBenefits/credits/{creditName}/sources/{sourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits/swagger/stable/2026-06-01/billingbenefits.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BillingBenefits/discounts/{discountName}","patch","parameters"]` | displayName property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits/swagger/stable/2026-06-01/billingbenefits.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BillingBenefits/discounts/{discountName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits/swagger/stable/2026-06-01/billingbenefits.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BillingBenefits/freeServices/{freeServiceName}","patch","parameters"]` | endAt property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits/swagger/stable/2026-06-01/billingbenefits.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BillingBenefits/freeServices/{freeServiceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits/swagger/stable/2026-06-01/billingbenefits.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BillingBenefits/maccs/{maccName}","patch","parameters"]` | milestones property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits/swagger/stable/2026-06-01/billingbenefits.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BillingBenefits/maccs/{maccName}","patch","parameters"]` | status property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits/swagger/stable/2026-06-01/billingbenefits.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BillingBenefits/maccs/{maccName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:3237:3` | The property 'allowContributors' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:3242:3` | The property 'milestones' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-19"></a>
## specification/iotoperationsmq/resource-manager/Microsoft.IoTOperationsMQ/IoTOperationsMQ

Reported diagnostics: Swagger **12**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/iotoperationsmq/resource-manager/Microsoft.IoTOperationsMQ/IoTOperationsMQ/swagger/preview/2023-10-04-preview/iotoperationsmq.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTOperationsMQ/mq/{mqName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/iotoperationsmq/resource-manager/Microsoft.IoTOperationsMQ/IoTOperationsMQ/swagger/preview/2023-10-04-preview/iotoperationsmq.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTOperationsMQ/mq/{mqName}/broker/{brokerName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/iotoperationsmq/resource-manager/Microsoft.IoTOperationsMQ/IoTOperationsMQ/swagger/preview/2023-10-04-preview/iotoperationsmq.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTOperationsMQ/mq/{mqName}/broker/{brokerName}/authentication/{authenticationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/iotoperationsmq/resource-manager/Microsoft.IoTOperationsMQ/IoTOperationsMQ/swagger/preview/2023-10-04-preview/iotoperationsmq.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTOperationsMQ/mq/{mqName}/broker/{brokerName}/authorization/{authorizationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/iotoperationsmq/resource-manager/Microsoft.IoTOperationsMQ/IoTOperationsMQ/swagger/preview/2023-10-04-preview/iotoperationsmq.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTOperationsMQ/mq/{mqName}/broker/{brokerName}/listener/{listenerName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/iotoperationsmq/resource-manager/Microsoft.IoTOperationsMQ/IoTOperationsMQ/swagger/preview/2023-10-04-preview/iotoperationsmq.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTOperationsMQ/mq/{mqName}/dataLakeConnector/{dataLakeConnectorName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/iotoperationsmq/resource-manager/Microsoft.IoTOperationsMQ/IoTOperationsMQ/swagger/preview/2023-10-04-preview/iotoperationsmq.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTOperationsMQ/mq/{mqName}/dataLakeConnector/{dataLakeConnectorName}/topicMap/{topicMapName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/iotoperationsmq/resource-manager/Microsoft.IoTOperationsMQ/IoTOperationsMQ/swagger/preview/2023-10-04-preview/iotoperationsmq.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTOperationsMQ/mq/{mqName}/diagnosticService/{diagnosticServiceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/iotoperationsmq/resource-manager/Microsoft.IoTOperationsMQ/IoTOperationsMQ/swagger/preview/2023-10-04-preview/iotoperationsmq.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTOperationsMQ/mq/{mqName}/kafkaConnector/{kafkaConnectorName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/iotoperationsmq/resource-manager/Microsoft.IoTOperationsMQ/IoTOperationsMQ/swagger/preview/2023-10-04-preview/iotoperationsmq.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTOperationsMQ/mq/{mqName}/kafkaConnector/{kafkaConnectorName}/topicMap/{topicMapName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/iotoperationsmq/resource-manager/Microsoft.IoTOperationsMQ/IoTOperationsMQ/swagger/preview/2023-10-04-preview/iotoperationsmq.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTOperationsMQ/mq/{mqName}/mqttBridgeConnector/{mqttBridgeConnectorName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/iotoperationsmq/resource-manager/Microsoft.IoTOperationsMQ/IoTOperationsMQ/swagger/preview/2023-10-04-preview/iotoperationsmq.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTOperationsMQ/mq/{mqName}/mqttBridgeConnector/{mqttBridgeConnectorName}/topicMap/{topicMapName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-20"></a>
## specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/fluxConfigurations

Reported diagnostics: Swagger **12**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/fluxConfigurations/swagger/stable/2025-04-01/fluxconfiguration.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/fluxConfigurations/{fluxConfigurationName}","patch","parameters"]` | bucketName property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/fluxConfigurations/swagger/stable/2025-04-01/fluxconfiguration.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/fluxConfigurations/{fluxConfigurationName}","patch","parameters"]` | clientCertificate property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/fluxConfigurations/swagger/stable/2025-04-01/fluxconfiguration.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/fluxConfigurations/{fluxConfigurationName}","patch","parameters"]` | clientCertificateSendChain property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/fluxConfigurations/swagger/stable/2025-04-01/fluxconfiguration.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/fluxConfigurations/{fluxConfigurationName}","patch","parameters"]` | configurationProtectedSettings property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/fluxConfigurations/swagger/stable/2025-04-01/fluxconfiguration.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/fluxConfigurations/{fluxConfigurationName}","patch","parameters"]` | insecure property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/fluxConfigurations/swagger/stable/2025-04-01/fluxconfiguration.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/fluxConfigurations/{fluxConfigurationName}","patch","parameters"]` | kustomizations property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/fluxConfigurations/swagger/stable/2025-04-01/fluxconfiguration.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/fluxConfigurations/{fluxConfigurationName}","patch","parameters"]` | matchOidcIdentity property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/fluxConfigurations/swagger/stable/2025-04-01/fluxconfiguration.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/fluxConfigurations/{fluxConfigurationName}","patch","parameters"]` | sourceKind property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/fluxConfigurations/swagger/stable/2025-04-01/fluxconfiguration.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/fluxConfigurations/{fluxConfigurationName}","patch","parameters"]` | suspend property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/fluxConfigurations/swagger/stable/2025-04-01/fluxconfiguration.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/fluxConfigurations/{fluxConfigurationName}","patch","parameters"]` | syncIntervalInSeconds property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/fluxConfigurations/swagger/stable/2025-04-01/fluxconfiguration.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/fluxConfigurations/{fluxConfigurationName}","patch","parameters"]` | timeoutInSeconds property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/fluxConfigurations/swagger/stable/2025-04-01/fluxconfiguration.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/fluxConfigurations/{fluxConfigurationName}","patch","parameters"]` | url property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-21"></a>
## specification/oracle/resource-manager/Oracle.Database/OracleDatabase

Reported diagnostics: Swagger **12**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/swagger/stable/2026-06-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/autonomousDatabases/{autonomousdatabasename}","patch","parameters"]` | scheduledOperationsList property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/swagger/stable/2026-06-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/autonomousDatabases/{autonomousdatabasename}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/swagger/stable/2026-06-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/cloudExadataInfrastructures/{cloudexadatainfrastructurename}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/swagger/stable/2026-06-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/cloudVmClusters/{cloudvmclustername}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/swagger/stable/2026-06-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/dbSystems/{dbSystemName}","patch","parameters"]` | source property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/swagger/stable/2026-06-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/dbSystems/{dbSystemName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/swagger/stable/2026-06-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/exadbVmClusters/{exadbVmClusterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/swagger/stable/2026-06-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/exascaleDbStorageVaults/{exascaleDbStorageVaultName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/swagger/stable/2026-06-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/goldenGateConnections/{goldenGateConnectionName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/swagger/stable/2026-06-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/goldenGateDeployments/{goldenGateDeploymentName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/swagger/stable/2026-06-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/networkAnchors/{networkAnchorName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/swagger/stable/2026-06-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/resourceAnchors/{resourceAnchorName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-22"></a>
## specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry

Reported diagnostics: Swagger **11**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}","patch","parameters"]` | adminUserEnabled property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}","patch","parameters"]` | anonymousPullEnabled property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}","patch","parameters"]` | networkRuleBypassAllowedForTasks property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}","patch","parameters"]` | publicNetworkAccess property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}","patch","parameters"]` | roleAssignmentMode property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}","patch","parameters"]` | writableCacheRepos property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/cacheRules/{cacheRuleName}","patch","parameters"]` | credentialSetResourceId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/replications/{replicationName}","patch","parameters"]` | regionEndpointEnabled property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/replications/{replicationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/scopeMaps/{scopeMapName}","patch","parameters"]` | actions property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-23"></a>
## specification/dnsresolver/resource-manager/Microsoft.Network/DnsResolver

Reported diagnostics: Swagger **12**, TypeSpec **1**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/dnsresolver/resource-manager/Microsoft.Network/DnsResolver/swagger/preview/2025-10-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsForwardingRulesets/{dnsForwardingRulesetName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dnsresolver/resource-manager/Microsoft.Network/DnsResolver/swagger/preview/2025-10-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsForwardingRulesets/{dnsForwardingRulesetName}/forwardingRules/{forwardingRuleName}","patch","parameters"]` | forwardingRuleState property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dnsresolver/resource-manager/Microsoft.Network/DnsResolver/swagger/preview/2025-10-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsResolverDomainLists/{dnsResolverDomainListName}","patch","parameters"]` | domains property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dnsresolver/resource-manager/Microsoft.Network/DnsResolver/swagger/preview/2025-10-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsResolverDomainLists/{dnsResolverDomainListName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dnsresolver/resource-manager/Microsoft.Network/DnsResolver/swagger/preview/2025-10-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsResolverPolicies/{dnsResolverPolicyName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dnsresolver/resource-manager/Microsoft.Network/DnsResolver/swagger/preview/2025-10-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsResolverPolicies/{dnsResolverPolicyName}/dnsSecurityRules/{dnsSecurityRuleName}","patch","parameters"]` | dnsResolverDomainLists property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dnsresolver/resource-manager/Microsoft.Network/DnsResolver/swagger/preview/2025-10-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsResolverPolicies/{dnsResolverPolicyName}/dnsSecurityRules/{dnsSecurityRuleName}","patch","parameters"]` | managedDomainLists property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dnsresolver/resource-manager/Microsoft.Network/DnsResolver/swagger/preview/2025-10-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsResolverPolicies/{dnsResolverPolicyName}/dnsSecurityRules/{dnsSecurityRuleName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dnsresolver/resource-manager/Microsoft.Network/DnsResolver/swagger/preview/2025-10-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsResolverPolicies/{dnsResolverPolicyName}/virtualNetworkLinks/{dnsResolverPolicyVirtualNetworkLinkName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dnsresolver/resource-manager/Microsoft.Network/DnsResolver/swagger/preview/2025-10-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsResolvers/{dnsResolverName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dnsresolver/resource-manager/Microsoft.Network/DnsResolver/swagger/preview/2025-10-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsResolvers/{dnsResolverName}/inboundEndpoints/{inboundEndpointName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dnsresolver/resource-manager/Microsoft.Network/DnsResolver/swagger/preview/2025-10-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsResolvers/{dnsResolverName}/outboundEndpoints/{outboundEndpointName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:612:3` | The property 'dnsResolverDomainLists' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-24"></a>
## specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc

Reported diagnostics: Swagger **10**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc/swagger/preview/2023-03-02-preview/postgresqlhsc.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/serverGroupsv2/{clusterName}","patch","parameters"]` | administratorLoginPassword property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc/swagger/preview/2023-03-02-preview/postgresqlhsc.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/serverGroupsv2/{clusterName}","patch","parameters"]` | coordinatorServerEdition property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc/swagger/preview/2023-03-02-preview/postgresqlhsc.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/serverGroupsv2/{clusterName}","patch","parameters"]` | coordinatorStorageQuotaInMb property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc/swagger/preview/2023-03-02-preview/postgresqlhsc.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/serverGroupsv2/{clusterName}","patch","parameters"]` | coordinatorVCores property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc/swagger/preview/2023-03-02-preview/postgresqlhsc.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/serverGroupsv2/{clusterName}","patch","parameters"]` | nodeCount property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc/swagger/preview/2023-03-02-preview/postgresqlhsc.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/serverGroupsv2/{clusterName}","patch","parameters"]` | nodeEnablePublicIpAccess property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc/swagger/preview/2023-03-02-preview/postgresqlhsc.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/serverGroupsv2/{clusterName}","patch","parameters"]` | nodeServerEdition property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc/swagger/preview/2023-03-02-preview/postgresqlhsc.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/serverGroupsv2/{clusterName}","patch","parameters"]` | nodeStorageQuotaInMb property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc/swagger/preview/2023-03-02-preview/postgresqlhsc.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/serverGroupsv2/{clusterName}","patch","parameters"]` | nodeVCores property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc/swagger/preview/2023-03-02-preview/postgresqlhsc.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/serverGroupsv2/{clusterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-25"></a>
## specification/containerinstance/resource-manager/Microsoft.ContainerInstance/ContainerInstance

Reported diagnostics: Swagger **9**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/containerinstance/resource-manager/Microsoft.ContainerInstance/ContainerInstance/swagger/preview/2026-09-01-preview/containerInstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/aiAgentsGroups/{aiAgentsGroupName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerinstance/resource-manager/Microsoft.ContainerInstance/ContainerInstance/swagger/preview/2026-09-01-preview/containerInstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerinstance/resource-manager/Microsoft.ContainerInstance/ContainerInstance/swagger/preview/2026-09-01-preview/containerInstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}","patch","parameters"]` | location property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerinstance/resource-manager/Microsoft.ContainerInstance/ContainerInstance/swagger/preview/2026-09-01-preview/containerInstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerinstance/resource-manager/Microsoft.ContainerInstance/ContainerInstance/swagger/preview/2026-09-01-preview/containerInstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerinstance/resource-manager/Microsoft.ContainerInstance/ContainerInstance/swagger/preview/2026-09-01-preview/containerInstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}","patch","parameters"]` | zones property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerinstance/resource-manager/Microsoft.ContainerInstance/ContainerInstance/swagger/preview/2026-09-01-preview/containerInstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/managedVirtualNodePools/{managedVirtualNodePoolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerinstance/resource-manager/Microsoft.ContainerInstance/ContainerInstance/swagger/preview/2026-09-01-preview/containerInstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/ngroups/{ngroupsName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerinstance/resource-manager/Microsoft.ContainerInstance/ContainerInstance/swagger/preview/2026-09-01-preview/containerInstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/ngroups/{ngroupsName}","patch","parameters"]` | zones property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-26"></a>
## specification/hybridcompute/resource-manager/Microsoft.HybridCompute/HybridCompute

Reported diagnostics: Swagger **9**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/hybridcompute/resource-manager/Microsoft.HybridCompute/HybridCompute/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/gateways/{gatewayName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/hybridcompute/resource-manager/Microsoft.HybridCompute/HybridCompute/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/licenses/{licenseName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/hybridcompute/resource-manager/Microsoft.HybridCompute/HybridCompute/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{machineName}","patch","parameters"]` | identityKeyStore property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/hybridcompute/resource-manager/Microsoft.HybridCompute/HybridCompute/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{machineName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/hybridcompute/resource-manager/Microsoft.HybridCompute/HybridCompute/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{machineName}/extensions/{extensionName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/hybridcompute/resource-manager/Microsoft.HybridCompute/HybridCompute/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{machineName}/licenseProfiles/{licenseProfileName}","patch","parameters"]` | productFeatures property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/hybridcompute/resource-manager/Microsoft.HybridCompute/HybridCompute/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{machineName}/licenseProfiles/{licenseProfileName}","patch","parameters"]` | subscriptionStatus property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/hybridcompute/resource-manager/Microsoft.HybridCompute/HybridCompute/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{machineName}/licenseProfiles/{licenseProfileName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/hybridcompute/resource-manager/Microsoft.HybridCompute/HybridCompute/swagger/stable/2026-07-15/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/privateLinkScopes/{scopeName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-27"></a>
## specification/azurearcdata/resource-manager/Microsoft.AzureArcData/AzureArcData

Reported diagnostics: Swagger **11**, TypeSpec **3**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/azurearcdata/resource-manager/Microsoft.AzureArcData/AzureArcData/swagger/preview/2026-03-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureArcData/dataControllers/{dataControllerName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurearcdata/resource-manager/Microsoft.AzureArcData/AzureArcData/swagger/preview/2026-03-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureArcData/postgresInstances/{postgresInstanceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurearcdata/resource-manager/Microsoft.AzureArcData/AzureArcData/swagger/preview/2026-03-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureArcData/sqlManagedInstances/{sqlManagedInstanceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurearcdata/resource-manager/Microsoft.AzureArcData/AzureArcData/swagger/preview/2026-03-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureArcData/sqlServerEsuLicenses/{sqlServerEsuLicenseName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurearcdata/resource-manager/Microsoft.AzureArcData/AzureArcData/swagger/preview/2026-03-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureArcData/sqlServerInstances/{sqlServerInstanceName}","patch","parameters"]` | isDigiCertPkiCertTrustConfigured property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurearcdata/resource-manager/Microsoft.AzureArcData/AzureArcData/swagger/preview/2026-03-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureArcData/sqlServerInstances/{sqlServerInstanceName}","patch","parameters"]` | isMicrosoftPkiCertTrustConfigured property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurearcdata/resource-manager/Microsoft.AzureArcData/AzureArcData/swagger/preview/2026-03-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureArcData/sqlServerInstances/{sqlServerInstanceName}","patch","parameters"]` | maxServerMemoryMB property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurearcdata/resource-manager/Microsoft.AzureArcData/AzureArcData/swagger/preview/2026-03-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureArcData/sqlServerInstances/{sqlServerInstanceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurearcdata/resource-manager/Microsoft.AzureArcData/AzureArcData/swagger/preview/2026-03-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureArcData/sqlServerInstances/{sqlServerInstanceName}/availabilityGroups/{availabilityGroupName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurearcdata/resource-manager/Microsoft.AzureArcData/AzureArcData/swagger/preview/2026-03-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureArcData/sqlServerInstances/{sqlServerInstanceName}/databases/{databaseName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurearcdata/resource-manager/Microsoft.AzureArcData/AzureArcData/swagger/preview/2026-03-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureArcData/sqlServerLicenses/{sqlServerLicenseName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:4012:3` | The property 'isMicrosoftPkiCertTrustConfigured' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:4017:3` | The property 'isDigiCertPkiCertTrustConfigured' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:4023:3` | The property 'maxServerMemoryMB' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-28"></a>
## specification/certificateregistration/resource-manager/Microsoft.CertificateRegistration/CertificateRegistration

Reported diagnostics: Swagger **8**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/certificateregistration/resource-manager/Microsoft.CertificateRegistration/CertificateRegistration/swagger/stable/2024-11-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/certificateregistration/resource-manager/Microsoft.CertificateRegistration/CertificateRegistration/swagger/stable/2024-11-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}","patch","parameters"]` | kind property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/certificateregistration/resource-manager/Microsoft.CertificateRegistration/CertificateRegistration/swagger/stable/2024-11-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/certificateregistration/resource-manager/Microsoft.CertificateRegistration/CertificateRegistration/swagger/stable/2024-11-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/certificateregistration/resource-manager/Microsoft.CertificateRegistration/CertificateRegistration/swagger/stable/2024-11-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/certificateregistration/resource-manager/Microsoft.CertificateRegistration/CertificateRegistration/swagger/stable/2024-11-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name}","patch","parameters"]` | kind property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/certificateregistration/resource-manager/Microsoft.CertificateRegistration/CertificateRegistration/swagger/stable/2024-11-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/certificateregistration/resource-manager/Microsoft.CertificateRegistration/CertificateRegistration/swagger/stable/2024-11-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-29"></a>
## specification/discovery/Discovery.Management

Reported diagnostics: Swagger **10**, TypeSpec **2**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/discovery/Discovery.Management/swagger/resource-manager/Microsoft.Discovery/stable/2026-06-01/discovery.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Discovery/bookshelves/{bookshelfName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/discovery/Discovery.Management/swagger/resource-manager/Microsoft.Discovery/stable/2026-06-01/discovery.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Discovery/storageContainers/{storageContainerName}","patch","parameters"]` | properties property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/discovery/Discovery.Management/swagger/resource-manager/Microsoft.Discovery/stable/2026-06-01/discovery.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Discovery/storageContainers/{storageContainerName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/discovery/Discovery.Management/swagger/resource-manager/Microsoft.Discovery/stable/2026-06-01/discovery.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Discovery/storageContainers/{storageContainerName}/storageAssets/{storageAssetName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/discovery/Discovery.Management/swagger/resource-manager/Microsoft.Discovery/stable/2026-06-01/discovery.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Discovery/supercomputers/{supercomputerName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/discovery/Discovery.Management/swagger/resource-manager/Microsoft.Discovery/stable/2026-06-01/discovery.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Discovery/supercomputers/{supercomputerName}/nodePools/{nodePoolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/discovery/Discovery.Management/swagger/resource-manager/Microsoft.Discovery/stable/2026-06-01/discovery.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Discovery/tools/{toolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/discovery/Discovery.Management/swagger/resource-manager/Microsoft.Discovery/stable/2026-06-01/discovery.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Discovery/workspaces/{workspaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/discovery/Discovery.Management/swagger/resource-manager/Microsoft.Discovery/stable/2026-06-01/discovery.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Discovery/workspaces/{workspaceName}/chatModelDeployments/{chatModelDeploymentName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/discovery/Discovery.Management/swagger/resource-manager/Microsoft.Discovery/stable/2026-06-01/discovery.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Discovery/workspaces/{workspaceName}/projects/{projectName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `../Discovery.Workspace.Management/ChatModelDeployments.tsp:63:3` | The property 'properties' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `storageContainer.tsp:114:3` | The property 'properties' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-30"></a>
## specification/elasticsan/resource-manager/Microsoft.ElasticSan/ElasticSan

Reported diagnostics: Swagger **8**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/elasticsan/resource-manager/Microsoft.ElasticSan/ElasticSan/swagger/preview/2026-05-01-preview/elasticsan.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ElasticSan/elasticSans/{elasticSanName}","patch","parameters"]` | baseSizeTiB property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/elasticsan/resource-manager/Microsoft.ElasticSan/ElasticSan/swagger/preview/2026-05-01-preview/elasticsan.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ElasticSan/elasticSans/{elasticSanName}","patch","parameters"]` | extendedCapacitySizeTiB property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/elasticsan/resource-manager/Microsoft.ElasticSan/ElasticSan/swagger/preview/2026-05-01-preview/elasticsan.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ElasticSan/elasticSans/{elasticSanName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/elasticsan/resource-manager/Microsoft.ElasticSan/ElasticSan/swagger/preview/2026-05-01-preview/elasticsan.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ElasticSan/elasticSans/{elasticSanName}","patch","parameters"]` | totalIops property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/elasticsan/resource-manager/Microsoft.ElasticSan/ElasticSan/swagger/preview/2026-05-01-preview/elasticsan.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ElasticSan/elasticSans/{elasticSanName}","patch","parameters"]` | totalMBps property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/elasticsan/resource-manager/Microsoft.ElasticSan/ElasticSan/swagger/preview/2026-05-01-preview/elasticsan.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ElasticSan/elasticSans/{elasticSanName}","patch","parameters"]` | totalSizeTiB property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/elasticsan/resource-manager/Microsoft.ElasticSan/ElasticSan/swagger/preview/2026-05-01-preview/elasticsan.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ElasticSan/elasticSans/{elasticSanName}/volumegroups/{volumeGroupName}","patch","parameters"]` | reservedIops property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/elasticsan/resource-manager/Microsoft.ElasticSan/ElasticSan/swagger/preview/2026-05-01-preview/elasticsan.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ElasticSan/elasticSans/{elasticSanName}/volumegroups/{volumeGroupName}","patch","parameters"]` | reservedMBps property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-31"></a>
## specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault

Reported diagnostics: Swagger **9**, TypeSpec **1**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}","patch","parameters"]` | accessPolicies property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}","patch","parameters"]` | enableRbacAuthorization property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}","patch","parameters"]` | enableSoftDelete property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}","patch","parameters"]` | enabledForDeployment property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}","patch","parameters"]` | enabledForDiskEncryption property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}","patch","parameters"]` | enabledForTemplateDeployment property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}","patch","parameters"]` | publicNetworkAccess property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}","patch","parameters"]` | softDeleteRetentionInDays property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/secrets/{secretName}","patch","parameters"]` | value property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:1463:3` | The property 'enableRbacAuthorization' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-32"></a>
## specification/storagecache/resource-manager/Microsoft.StorageCache/StorageCache

Reported diagnostics: Swagger **8**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/storagecache/resource-manager/Microsoft.StorageCache/StorageCache/swagger/stable/2026-08-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageCache/amlFilesystems/{amlFilesystemName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storagecache/resource-manager/Microsoft.StorageCache/StorageCache/swagger/stable/2026-08-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageCache/amlFilesystems/{amlFilesystemName}/autoExportJobs/{autoExportJobName}","patch","parameters"]` | adminStatus property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storagecache/resource-manager/Microsoft.StorageCache/StorageCache/swagger/stable/2026-08-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageCache/amlFilesystems/{amlFilesystemName}/autoExportJobs/{autoExportJobName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storagecache/resource-manager/Microsoft.StorageCache/StorageCache/swagger/stable/2026-08-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageCache/amlFilesystems/{amlFilesystemName}/autoImportJobs/{autoImportJobName}","patch","parameters"]` | adminStatus property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storagecache/resource-manager/Microsoft.StorageCache/StorageCache/swagger/stable/2026-08-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageCache/amlFilesystems/{amlFilesystemName}/autoImportJobs/{autoImportJobName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storagecache/resource-manager/Microsoft.StorageCache/StorageCache/swagger/stable/2026-08-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageCache/amlFilesystems/{amlFilesystemName}/expansionJobs/{expansionJobName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storagecache/resource-manager/Microsoft.StorageCache/StorageCache/swagger/stable/2026-08-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageCache/amlFilesystems/{amlFilesystemName}/importJobs/{importJobName}","patch","parameters"]` | adminStatus property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storagecache/resource-manager/Microsoft.StorageCache/StorageCache/swagger/stable/2026-08-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageCache/amlFilesystems/{amlFilesystemName}/importJobs/{importJobName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-33"></a>
## specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb

Reported diagnostics: Swagger **7**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb/swagger/preview/2026-05-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HorizonDb/clusters/{clusterName}","patch","parameters"]` | administratorLoginPassword property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb/swagger/preview/2026-05-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HorizonDb/clusters/{clusterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb/swagger/preview/2026-05-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HorizonDb/clusters/{clusterName}","patch","parameters"]` | vCores property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb/swagger/preview/2026-05-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HorizonDb/parameterGroups/{parameterGroupName}","patch","parameters"]` | applyImmediately property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb/swagger/preview/2026-05-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HorizonDb/parameterGroups/{parameterGroupName}","patch","parameters"]` | description property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb/swagger/preview/2026-05-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HorizonDb/parameterGroups/{parameterGroupName}","patch","parameters"]` | parameters property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb/swagger/preview/2026-05-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HorizonDb/parameterGroups/{parameterGroupName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-34"></a>
## specification/network/resource-manager/Microsoft.Network/Network/Network

Reported diagnostics: Swagger **7**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkSecurityPerimeter.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityPerimeters/{networkSecurityPerimeterName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkSecurityPerimeter.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityPerimeters/{networkSecurityPerimeterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkManagers/{networkManagerName}/ipamPools/{poolName}","patch","parameters"]` | maxAllocationSize property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkManagers/{networkManagerName}/ipamPools/{poolName}","patch","parameters"]` | minAllocationSize property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkManagers/{networkManagerName}/ipamPools/{poolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkManagers/{networkManagerName}/verifierWorkspaces/{workspaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-35"></a>
## specification/scvmm/resource-manager/Microsoft.ScVmm/ScVmm

Reported diagnostics: Swagger **7**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/scvmm/resource-manager/Microsoft.ScVmm/ScVmm/swagger/stable/2025-03-13/scvmm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ScVmm/availabilitySets/{availabilitySetResourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/scvmm/resource-manager/Microsoft.ScVmm/ScVmm/swagger/stable/2025-03-13/scvmm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ScVmm/clouds/{cloudResourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/scvmm/resource-manager/Microsoft.ScVmm/ScVmm/swagger/stable/2025-03-13/scvmm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ScVmm/virtualMachineTemplates/{virtualMachineTemplateName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/scvmm/resource-manager/Microsoft.ScVmm/ScVmm/swagger/stable/2025-03-13/scvmm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ScVmm/virtualNetworks/{virtualNetworkName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/scvmm/resource-manager/Microsoft.ScVmm/ScVmm/swagger/stable/2025-03-13/scvmm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ScVmm/vmmServers/{vmmServerName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/scvmm/resource-manager/Microsoft.ScVmm/ScVmm/swagger/stable/2025-03-13/scvmm.json: ["paths","/{resourceUri}/providers/Microsoft.ScVmm/virtualMachineInstances/default","patch","parameters"]` | disks property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/scvmm/resource-manager/Microsoft.ScVmm/ScVmm/swagger/stable/2025-03-13/scvmm.json: ["paths","/{resourceUri}/providers/Microsoft.ScVmm/virtualMachineInstances/default","patch","parameters"]` | networkInterfaces property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-36"></a>
## specification/servicefabric/resource-manager/Microsoft.ServiceFabric/ServiceFabric

Reported diagnostics: Swagger **13**, TypeSpec **6**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/servicefabric/resource-manager/Microsoft.ServiceFabric/ServiceFabric/swagger/preview/2026-03-01-preview/servicefabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}","patch","parameters"]` | clientCertificateCommonNames property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicefabric/resource-manager/Microsoft.ServiceFabric/ServiceFabric/swagger/preview/2026-03-01-preview/servicefabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}","patch","parameters"]` | clientCertificateThumbprints property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicefabric/resource-manager/Microsoft.ServiceFabric/ServiceFabric/swagger/preview/2026-03-01-preview/servicefabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}","patch","parameters"]` | fabricSettings property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicefabric/resource-manager/Microsoft.ServiceFabric/ServiceFabric/swagger/preview/2026-03-01-preview/servicefabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}","patch","parameters"]` | nodeTypes property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicefabric/resource-manager/Microsoft.ServiceFabric/ServiceFabric/swagger/preview/2026-03-01-preview/servicefabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicefabric/resource-manager/Microsoft.ServiceFabric/ServiceFabric/swagger/preview/2026-03-01-preview/servicefabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}","patch","parameters"]` | upgradePauseEndTimestampUtc property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicefabric/resource-manager/Microsoft.ServiceFabric/ServiceFabric/swagger/preview/2026-03-01-preview/servicefabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}","patch","parameters"]` | upgradePauseStartTimestampUtc property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicefabric/resource-manager/Microsoft.ServiceFabric/ServiceFabric/swagger/preview/2026-03-01-preview/servicefabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicefabric/resource-manager/Microsoft.ServiceFabric/ServiceFabric/swagger/preview/2026-03-01-preview/servicefabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicefabric/resource-manager/Microsoft.ServiceFabric/ServiceFabric/swagger/preview/2026-03-01-preview/servicefabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicefabric/resource-manager/Microsoft.ServiceFabric/ServiceFabric/swagger/preview/2026-03-01-preview/servicefabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName}/services/{serviceName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicefabric/resource-manager/Microsoft.ServiceFabric/ServiceFabric/swagger/preview/2026-03-01-preview/servicefabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName}/services/{serviceName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicefabric/resource-manager/Microsoft.ServiceFabric/ServiceFabric/swagger/preview/2026-03-01-preview/servicefabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName}/services/{serviceName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:87:3` | The property 'createdAt' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:87:3` | The property 'createdBy' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:87:3` | The property 'createdByType' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:87:3` | The property 'lastModifiedAt' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:87:3` | The property 'lastModifiedBy' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:87:3` | The property 'lastModifiedByType' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-37"></a>
## specification/sql/resource-manager/Microsoft.Sql/SQL

Reported diagnostics: Swagger **8**, TypeSpec **1**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/databases.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/elasticPools.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/instancePools.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/instancePools/{instancePoolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/jobAgents.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/managedDatabases.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/managedInstances.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/servers.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/virtualClusters.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/virtualClusters/{virtualClusterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:11853:3` | The property 'properties' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-38"></a>
## specification/app/resource-manager/Microsoft.App/ContainerApps

Reported diagnostics: Swagger **10**, TypeSpec **4**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/app/resource-manager/Microsoft.App/ContainerApps/swagger/stable/2026-07-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/connectedEnvironments/{connectedEnvironmentName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/app/resource-manager/Microsoft.App/ContainerApps/swagger/stable/2026-07-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/connectedEnvironments/{connectedEnvironmentName}/certificates/{certificateName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/app/resource-manager/Microsoft.App/ContainerApps/swagger/stable/2026-07-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/jobs/{jobName}","patch","parameters"]` | environmentId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/app/resource-manager/Microsoft.App/ContainerApps/swagger/stable/2026-07-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/jobs/{jobName}","patch","parameters"]` | eventStreamEndpoint property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/app/resource-manager/Microsoft.App/ContainerApps/swagger/stable/2026-07-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/jobs/{jobName}","patch","parameters"]` | outboundIpAddresses property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/app/resource-manager/Microsoft.App/ContainerApps/swagger/stable/2026-07-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/jobs/{jobName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/app/resource-manager/Microsoft.App/ContainerApps/swagger/stable/2026-07-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/managedEnvironments/{environmentName}/certificates/{certificateName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/app/resource-manager/Microsoft.App/ContainerApps/swagger/stable/2026-07-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/managedEnvironments/{environmentName}/managedCertificates/{managedCertificateName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/app/resource-manager/Microsoft.App/ContainerApps/swagger/stable/2026-07-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/sandboxGroups/{sandboxGroupName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/app/resource-manager/Microsoft.App/ContainerApps/swagger/stable/2026-07-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/sessionPools/{sessionPoolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:2711:3` | The property 'vnetConfiguration' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:4324:3` | The property 'outboundIpAddresses' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:4329:3` | The property 'eventStreamEndpoint' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:7037:3` | The property 'networking' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-39"></a>
## specification/azuredatatransfer/resource-manager/Microsoft.AzureDataTransfer/AzureDataTransfer

Reported diagnostics: Swagger **6**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/azuredatatransfer/resource-manager/Microsoft.AzureDataTransfer/AzureDataTransfer/swagger/preview/2026-02-06-preview/azuredatatransfer.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureDataTransfer/connections/{connectionName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azuredatatransfer/resource-manager/Microsoft.AzureDataTransfer/AzureDataTransfer/swagger/preview/2026-02-06-preview/azuredatatransfer.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureDataTransfer/connections/{connectionName}/flows/{flowName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azuredatatransfer/resource-manager/Microsoft.AzureDataTransfer/AzureDataTransfer/swagger/preview/2026-02-06-preview/azuredatatransfer.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureDataTransfer/pipelines/{pipelineName}","patch","parameters"]` | flowTypes property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azuredatatransfer/resource-manager/Microsoft.AzureDataTransfer/AzureDataTransfer/swagger/preview/2026-02-06-preview/azuredatatransfer.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureDataTransfer/pipelines/{pipelineName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azuredatatransfer/resource-manager/Microsoft.AzureDataTransfer/AzureDataTransfer/swagger/preview/2026-02-06-preview/azuredatatransfer.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureDataTransfer/pipelines/{pipelineName}/flowProfiles/{flowProfileName}","patch","parameters"]` | description property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azuredatatransfer/resource-manager/Microsoft.AzureDataTransfer/AzureDataTransfer/swagger/preview/2026-02-06-preview/azuredatatransfer.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureDataTransfer/pipelines/{pipelineName}/flowProfiles/{flowProfileName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-40"></a>
## specification/containerservice/resource-manager/Microsoft.ContainerService/aks

Reported diagnostics: Swagger **6**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/swagger/preview/2026-07-02-preview/managedClusters.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/maintenanceWindows/{maintenanceWindowName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/swagger/preview/2026-07-02-preview/managedClusters.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/swagger/preview/2026-07-02-preview/managedClusters.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/agentPools/{agentPoolName}","patch","parameters"]` | count property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/swagger/preview/2026-07-02-preview/managedClusters.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/managedNamespaces/{managedNamespaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/swagger/preview/2026-07-02-preview/managedClusters.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedclustersnapshots/{resourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/swagger/preview/2026-07-02-preview/managedClusters.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/snapshots/{resourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-41"></a>
## specification/dashboard/resource-manager/Microsoft.Dashboard/Dashboard

Reported diagnostics: Swagger **6**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/dashboard/resource-manager/Microsoft.Dashboard/Dashboard/swagger/preview/2025-09-01-preview/grafana.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Dashboard/dashboards/{dashboardName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dashboard/resource-manager/Microsoft.Dashboard/Dashboard/swagger/preview/2025-09-01-preview/grafana.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Dashboard/grafana/{workspaceName}","patch","parameters"]` | grafanaPlugins property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dashboard/resource-manager/Microsoft.Dashboard/Dashboard/swagger/preview/2025-09-01-preview/grafana.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Dashboard/grafana/{workspaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dashboard/resource-manager/Microsoft.Dashboard/Dashboard/swagger/preview/2025-09-01-preview/grafana.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Dashboard/grafana/{workspaceName}/integrationFabrics/{integrationFabricName}","patch","parameters"]` | scenarios property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dashboard/resource-manager/Microsoft.Dashboard/Dashboard/swagger/preview/2025-09-01-preview/grafana.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Dashboard/grafana/{workspaceName}/integrationFabrics/{integrationFabricName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dashboard/resource-manager/Microsoft.Dashboard/Dashboard/swagger/preview/2025-09-01-preview/grafana.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Dashboard/grafana/{workspaceName}/managedPrivateEndpoints/{managedPrivateEndpointName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-42"></a>
## specification/edge/resource-manager/Microsoft.Edge/configurationmanager

Reported diagnostics: Swagger **6**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/edge/resource-manager/Microsoft.Edge/configurationmanager/swagger/stable/2026-06-01/configurationmanager.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Edge/configTemplates/{configTemplateName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/edge/resource-manager/Microsoft.Edge/configurationmanager/swagger/stable/2026-06-01/configurationmanager.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Edge/contexts/{contextName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/edge/resource-manager/Microsoft.Edge/configurationmanager/swagger/stable/2026-06-01/configurationmanager.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Edge/diagnostics/{diagnosticName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/edge/resource-manager/Microsoft.Edge/configurationmanager/swagger/stable/2026-06-01/configurationmanager.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Edge/schemas/{schemaName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/edge/resource-manager/Microsoft.Edge/configurationmanager/swagger/stable/2026-06-01/configurationmanager.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Edge/solutionTemplates/{solutionTemplateName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/edge/resource-manager/Microsoft.Edge/configurationmanager/swagger/stable/2026-06-01/configurationmanager.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Edge/targets/{targetName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-43"></a>
## specification/servicefabricmanagedclusters/resource-manager/Microsoft.ServiceFabric/ServiceFabricManagedClusters

Reported diagnostics: Swagger **6**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/servicefabricmanagedclusters/resource-manager/Microsoft.ServiceFabric/ServiceFabricManagedClusters/swagger/preview/2026-05-01-preview/servicefabricmanagedclusters.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/managedClusters/{clusterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicefabricmanagedclusters/resource-manager/Microsoft.ServiceFabric/ServiceFabricManagedClusters/swagger/preview/2026-05-01-preview/servicefabricmanagedclusters.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/managedClusters/{clusterName}/applicationTypes/{applicationTypeName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicefabricmanagedclusters/resource-manager/Microsoft.ServiceFabric/ServiceFabricManagedClusters/swagger/preview/2026-05-01-preview/servicefabricmanagedclusters.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/managedClusters/{clusterName}/applicationTypes/{applicationTypeName}/versions/{version}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicefabricmanagedclusters/resource-manager/Microsoft.ServiceFabric/ServiceFabricManagedClusters/swagger/preview/2026-05-01-preview/servicefabricmanagedclusters.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/managedClusters/{clusterName}/applications/{applicationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicefabricmanagedclusters/resource-manager/Microsoft.ServiceFabric/ServiceFabricManagedClusters/swagger/preview/2026-05-01-preview/servicefabricmanagedclusters.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/managedClusters/{clusterName}/applications/{applicationName}/services/{serviceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicefabricmanagedclusters/resource-manager/Microsoft.ServiceFabric/ServiceFabricManagedClusters/swagger/preview/2026-05-01-preview/servicefabricmanagedclusters.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/managedClusters/{clusterName}/nodeTypes/{nodeTypeName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-44"></a>
## specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/RegistryTasks

Reported diagnostics: Swagger **6**, TypeSpec **1**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/RegistryTasks/swagger/preview/2025-03-01-preview/containerregistry_build.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/agentPools/{agentPoolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/RegistryTasks/swagger/preview/2025-03-01-preview/containerregistry_build.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/taskRuns/{taskRunName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/RegistryTasks/swagger/preview/2025-03-01-preview/containerregistry_build.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName}","patch","parameters"]` | sourceTriggers property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/RegistryTasks/swagger/preview/2025-03-01-preview/containerregistry_build.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/RegistryTasks/swagger/preview/2025-03-01-preview/containerregistry_build.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName}","patch","parameters"]` | timeout property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/RegistryTasks/swagger/preview/2025-03-01-preview/containerregistry_build.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName}","patch","parameters"]` | timerTriggers property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:936:3` | The property 'tags' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-45"></a>
## specification/containerservice/resource-manager/Microsoft.ContainerService/fleet

Reported diagnostics: Swagger **5**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/containerservice/resource-manager/Microsoft.ContainerService/fleet/swagger/preview/2026-06-02-preview/fleets.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/fleets/{fleetName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerservice/resource-manager/Microsoft.ContainerService/fleet/swagger/preview/2026-06-02-preview/fleets.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/fleets/{fleetName}/managedNamespaces/{managedNamespaceName}","patch","parameters"]` | clusterNames property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerservice/resource-manager/Microsoft.ContainerService/fleet/swagger/preview/2026-06-02-preview/fleets.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/fleets/{fleetName}/managedNamespaces/{managedNamespaceName}","patch","parameters"]` | clusterSelectorTerms property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerservice/resource-manager/Microsoft.ContainerService/fleet/swagger/preview/2026-06-02-preview/fleets.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/fleets/{fleetName}/managedNamespaces/{managedNamespaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerservice/resource-manager/Microsoft.ContainerService/fleet/swagger/preview/2026-06-02-preview/fleets.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/fleets/{fleetName}/managedNamespaces/{managedNamespaceName}","patch","parameters"]` | tolerations property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-46"></a>
## specification/dynatrace/resource-manager/Dynatrace.Observability/DynatraceObservability

Reported diagnostics: Swagger **5**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/dynatrace/resource-manager/Dynatrace.Observability/DynatraceObservability/swagger/stable/2024-04-24/dynatrace.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Dynatrace.Observability/monitors/{monitorName}","patch","parameters"]` | principalId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dynatrace/resource-manager/Dynatrace.Observability/DynatraceObservability/swagger/stable/2024-04-24/dynatrace.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Dynatrace.Observability/monitors/{monitorName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dynatrace/resource-manager/Dynatrace.Observability/DynatraceObservability/swagger/stable/2024-04-24/dynatrace.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Dynatrace.Observability/monitors/{monitorName}","patch","parameters"]` | tenantId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dynatrace/resource-manager/Dynatrace.Observability/DynatraceObservability/swagger/stable/2024-04-24/dynatrace.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Dynatrace.Observability/monitors/{monitorName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dynatrace/resource-manager/Dynatrace.Observability/DynatraceObservability/swagger/stable/2024-04-24/dynatrace.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Dynatrace.Observability/monitors/{monitorName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-47"></a>
## specification/fileshares/resource-manager/Microsoft.FileShares/FileShares

Reported diagnostics: Swagger **5**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/fileshares/resource-manager/Microsoft.FileShares/FileShares/swagger/stable/2026-06-01/fileshares.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.FileShares/fileShares/{resourceName}","patch","parameters"]` | provisionedIOPerSec property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/fileshares/resource-manager/Microsoft.FileShares/FileShares/swagger/stable/2026-06-01/fileshares.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.FileShares/fileShares/{resourceName}","patch","parameters"]` | provisionedStorageGiB property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/fileshares/resource-manager/Microsoft.FileShares/FileShares/swagger/stable/2026-06-01/fileshares.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.FileShares/fileShares/{resourceName}","patch","parameters"]` | provisionedThroughputMiBPerSec property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/fileshares/resource-manager/Microsoft.FileShares/FileShares/swagger/stable/2026-06-01/fileshares.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.FileShares/fileShares/{resourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/fileshares/resource-manager/Microsoft.FileShares/FileShares/swagger/stable/2026-06-01/fileshares.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.FileShares/fileShares/{resourceName}/fileShareSnapshots/{name}","patch","parameters"]` | metadata property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-48"></a>
## specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis

Reported diagnostics: Swagger **5**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis/swagger/preview/2025-04-01-preview/healthcare-apis.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/services/{resourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis/swagger/preview/2025-04-01-preview/healthcare-apis.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis/swagger/preview/2025-04-01-preview/healthcare-apis.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}/dicomservices/{dicomServiceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis/swagger/preview/2025-04-01-preview/healthcare-apis.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}/fhirservices/{fhirServiceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis/swagger/preview/2025-04-01-preview/healthcare-apis.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}/iotconnectors/{iotConnectorName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-49"></a>
## specification/playwrighttesting/PlaywrightTesting.Management

Reported diagnostics: Swagger **5**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/playwrighttesting/PlaywrightTesting.Management/swagger/resource-manager/Microsoft.AzurePlaywrightService/stable/2024-12-01/playwrighttesting.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzurePlaywrightService/accounts/{accountName}","patch","parameters"]` | localAuth property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/playwrighttesting/PlaywrightTesting.Management/swagger/resource-manager/Microsoft.AzurePlaywrightService/stable/2024-12-01/playwrighttesting.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzurePlaywrightService/accounts/{accountName}","patch","parameters"]` | regionalAffinity property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/playwrighttesting/PlaywrightTesting.Management/swagger/resource-manager/Microsoft.AzurePlaywrightService/stable/2024-12-01/playwrighttesting.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzurePlaywrightService/accounts/{accountName}","patch","parameters"]` | reporting property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/playwrighttesting/PlaywrightTesting.Management/swagger/resource-manager/Microsoft.AzurePlaywrightService/stable/2024-12-01/playwrighttesting.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzurePlaywrightService/accounts/{accountName}","patch","parameters"]` | scalableExecution property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/playwrighttesting/PlaywrightTesting.Management/swagger/resource-manager/Microsoft.AzurePlaywrightService/stable/2024-12-01/playwrighttesting.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzurePlaywrightService/accounts/{accountName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-50"></a>
## specification/support/resource-manager/Microsoft.Support/Support

Reported diagnostics: Swagger **6**, TypeSpec **1**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/support/resource-manager/Microsoft.Support/Support/swagger/preview/2025-06-01-preview/support.json: ["paths","/providers/Microsoft.Support/supportTickets/{supportTicketName}","patch","parameters"]` | additionalEmailAddresses property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/support/resource-manager/Microsoft.Support/Support/swagger/preview/2025-06-01-preview/support.json: ["paths","/providers/Microsoft.Support/supportTickets/{supportTicketName}","patch","parameters"]` | preferredSupportLanguage property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/support/resource-manager/Microsoft.Support/Support/swagger/preview/2025-06-01-preview/support.json: ["paths","/providers/Microsoft.Support/supportTickets/{supportTicketName}","patch","parameters"]` | status property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/support/resource-manager/Microsoft.Support/Support/swagger/preview/2025-06-01-preview/support.json: ["paths","/subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}","patch","parameters"]` | additionalEmailAddresses property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/support/resource-manager/Microsoft.Support/Support/swagger/preview/2025-06-01-preview/support.json: ["paths","/subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}","patch","parameters"]` | preferredSupportLanguage property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/support/resource-manager/Microsoft.Support/Support/swagger/preview/2025-06-01-preview/support.json: ["paths","/subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}","patch","parameters"]` | status property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:791:3` | The property 'status' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-51"></a>
## specification/agricultureplatform/AgriculturePlatform.Management

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/agricultureplatform/AgriculturePlatform.Management/swagger/resource-manager/Microsoft.AgriculturePlatform/preview/2024-06-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AgriculturePlatform/agriServices/{agriServiceResourceName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/agricultureplatform/AgriculturePlatform.Management/swagger/resource-manager/Microsoft.AgriculturePlatform/preview/2024-06-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AgriculturePlatform/agriServices/{agriServiceResourceName}","patch","parameters"]` | size property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/agricultureplatform/AgriculturePlatform.Management/swagger/resource-manager/Microsoft.AgriculturePlatform/preview/2024-06-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AgriculturePlatform/agriServices/{agriServiceResourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/agricultureplatform/AgriculturePlatform.Management/swagger/resource-manager/Microsoft.AgriculturePlatform/preview/2024-06-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AgriculturePlatform/agriServices/{agriServiceResourceName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-52"></a>
## specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCI

Reported diagnostics: Swagger **5**, TypeSpec **1**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCI/swagger/preview/2026-10-15-preview/hci.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/clusters/{clusterName}","patch","parameters"]` | cloudManagementEndpoint property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCI/swagger/preview/2026-10-15-preview/hci.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/clusters/{clusterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCI/swagger/preview/2026-10-15-preview/hci.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/clusters/{clusterName}/arcSettings/{arcSettingName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCI/swagger/preview/2026-10-15-preview/hci.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/devicePools/{devicePoolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurestackhci/resource-manager/Microsoft.AzureStackHCI/StackHCI/swagger/preview/2026-10-15-preview/hci.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/edgeMachines/{edgeMachineName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:2010:3` | The property 'tags' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-53"></a>
## specification/cdn/resource-manager/Microsoft.Cdn/Cdn

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/swagger/preview/2026-08-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/cdnWebApplicationFirewallPolicies/{policyName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/swagger/preview/2026-08-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/swagger/preview/2026-08-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/afdEndpoints/{endpointName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/swagger/preview/2026-08-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-54"></a>
## specification/cdn/resource-manager/Microsoft.Cdn/EdgeActions

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/cdn/resource-manager/Microsoft.Cdn/EdgeActions/swagger/stable/2026-10-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/edgeActions/{edgeActionName}","patch","parameters"]` | properties property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/cdn/resource-manager/Microsoft.Cdn/EdgeActions/swagger/stable/2026-10-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/edgeActions/{edgeActionName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/cdn/resource-manager/Microsoft.Cdn/EdgeActions/swagger/stable/2026-10-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/edgeActions/{edgeActionName}/executionFilters/{executionFilter}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/cdn/resource-manager/Microsoft.Cdn/EdgeActions/swagger/stable/2026-10-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/edgeActions/{edgeActionName}/versions/{version}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-55"></a>
## specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices/swagger/preview/2026-09-15-preview/cognitiveservices.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/costControls/{costControlName}","patch","parameters"]` | displayName property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices/swagger/preview/2026-09-15-preview/cognitiveservices.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/costControls/{costControlName}","patch","parameters"]` | rules property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices/swagger/preview/2026-09-15-preview/cognitiveservices.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/projects/{projectName}/workbenches/{workbenchName}","patch","parameters"]` | gpuCount property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices/swagger/preview/2026-09-15-preview/cognitiveservices.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/projects/{projectName}/workbenches/{workbenchName}","patch","parameters"]` | instanceType property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-56"></a>
## specification/communication/resource-manager/Microsoft.Communication/Communication

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/communication/resource-manager/Microsoft.Communication/Communication/swagger/stable/2026-03-18/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Communication/communicationServices/{communicationServiceName}","patch","parameters"]` | disableLocalAuth property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/communication/resource-manager/Microsoft.Communication/Communication/swagger/stable/2026-03-18/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Communication/communicationServices/{communicationServiceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/communication/resource-manager/Microsoft.Communication/Communication/swagger/stable/2026-03-18/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Communication/emailServices/{emailServiceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/communication/resource-manager/Microsoft.Communication/Communication/swagger/stable/2026-03-18/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Communication/emailServices/{emailServiceName}/domains/{domainName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-57"></a>
## specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeDisk

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeDisk/swagger/stable/2026-03-02/DiskRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskAccesses/{diskAccessName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeDisk/swagger/stable/2026-03-02/DiskRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeDisk/swagger/stable/2026-03-02/DiskRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/disks/{diskName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Compute/ComputeDisk/swagger/stable/2026-03-02/DiskRP.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/snapshots/{snapshotName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-58"></a>
## specification/compute/resource-manager/Microsoft.Compute/WorkloadManager

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/WorkloadManager/swagger/preview/2026-11-01-preview/WorkloadManager.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/workloadSpaces/{spaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/WorkloadManager/swagger/preview/2026-11-01-preview/WorkloadManager.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/workloadSpaces/{spaceName}/capabilities/{capabilityName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/WorkloadManager/swagger/preview/2026-11-01-preview/WorkloadManager.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/workloadSpaces/{spaceName}/runtimeBindings/{bindingName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/WorkloadManager/swagger/preview/2026-11-01-preview/WorkloadManager.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/workloadSpaces/{spaceName}/runtimeLinks/{linkName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-59"></a>
## specification/connectedcache/resource-manager/Microsoft.ConnectedCache/ConnectedCache

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/connectedcache/resource-manager/Microsoft.ConnectedCache/ConnectedCache/swagger/stable/2026-06-01/ConnectedCache.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ConnectedCache/enterpriseMccCustomers/{customerResourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/connectedcache/resource-manager/Microsoft.ConnectedCache/ConnectedCache/swagger/stable/2026-06-01/ConnectedCache.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ConnectedCache/enterpriseMccCustomers/{customerResourceName}/enterpriseMccCacheNodes/{cacheNodeResourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/connectedcache/resource-manager/Microsoft.ConnectedCache/ConnectedCache/swagger/stable/2026-06-01/ConnectedCache.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ConnectedCache/ispCustomers/{customerResourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/connectedcache/resource-manager/Microsoft.ConnectedCache/ConnectedCache/swagger/stable/2026-06-01/ConnectedCache.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ConnectedCache/ispCustomers/{customerResourceName}/ispCacheNodes/{cacheNodeResourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-60"></a>
## specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration/swagger/stable/2024-11-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration/swagger/stable/2024-11-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName}","patch","parameters"]` | kind property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration/swagger/stable/2024-11-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration/swagger/stable/2024-11-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-61"></a>
## specification/hybridkubernetes/resource-manager/Microsoft.Kubernetes/HybridKubernetes

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/hybridkubernetes/resource-manager/Microsoft.Kubernetes/HybridKubernetes/swagger/stable/2026-05-01/connectedClusters.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kubernetes/connectedClusters/{clusterName}","patch","parameters"]` | azureHybridBenefit property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/hybridkubernetes/resource-manager/Microsoft.Kubernetes/HybridKubernetes/swagger/stable/2026-05-01/connectedClusters.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kubernetes/connectedClusters/{clusterName}","patch","parameters"]` | distribution property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/hybridkubernetes/resource-manager/Microsoft.Kubernetes/HybridKubernetes/swagger/stable/2026-05-01/connectedClusters.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kubernetes/connectedClusters/{clusterName}","patch","parameters"]` | distributionVersion property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/hybridkubernetes/resource-manager/Microsoft.Kubernetes/HybridKubernetes/swagger/stable/2026-05-01/connectedClusters.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kubernetes/connectedClusters/{clusterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-62"></a>
## specification/loadtestservice/resource-manager/Microsoft.LoadTestService/playwright

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/loadtestservice/resource-manager/Microsoft.LoadTestService/playwright/swagger/preview/2026-08-01-preview/playwright.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LoadTestService/playwrightWorkspaces/{playwrightWorkspaceName}","patch","parameters"]` | localAuth property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/loadtestservice/resource-manager/Microsoft.LoadTestService/playwright/swagger/preview/2026-08-01-preview/playwright.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LoadTestService/playwrightWorkspaces/{playwrightWorkspaceName}","patch","parameters"]` | regionalAffinity property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/loadtestservice/resource-manager/Microsoft.LoadTestService/playwright/swagger/preview/2026-08-01-preview/playwright.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LoadTestService/playwrightWorkspaces/{playwrightWorkspaceName}","patch","parameters"]` | reporting property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/loadtestservice/resource-manager/Microsoft.LoadTestService/playwright/swagger/preview/2026-08-01-preview/playwright.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LoadTestService/playwrightWorkspaces/{playwrightWorkspaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-63"></a>
## specification/manufacturingplatform/Manufacturingplatform.Management

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/manufacturingplatform/Manufacturingplatform.Management/swagger/resource-manager/Microsoft.ManufacturingPlatform/stable/2025-03-01/manufacturingplatform.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManufacturingPlatform/manufacturingDataServices/{mdsResourceName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/manufacturingplatform/Manufacturingplatform.Management/swagger/resource-manager/Microsoft.ManufacturingPlatform/stable/2025-03-01/manufacturingplatform.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManufacturingPlatform/manufacturingDataServices/{mdsResourceName}","patch","parameters"]` | size property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/manufacturingplatform/Manufacturingplatform.Management/swagger/resource-manager/Microsoft.ManufacturingPlatform/stable/2025-03-01/manufacturingplatform.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManufacturingPlatform/manufacturingDataServices/{mdsResourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/manufacturingplatform/Manufacturingplatform.Management/swagger/resource-manager/Microsoft.ManufacturingPlatform/stable/2025-03-01/manufacturingplatform.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManufacturingPlatform/manufacturingDataServices/{mdsResourceName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-64"></a>
## specification/migrate/resource-manager/Microsoft.OffAzure/OffAzure

Reported diagnostics: Swagger **5**, TypeSpec **1**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/migrate/resource-manager/Microsoft.OffAzure/OffAzure/swagger/preview/2024-12-01-preview/offazure-migrate.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OffAzure/hypervSites/{siteName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/migrate/resource-manager/Microsoft.OffAzure/OffAzure/swagger/preview/2024-12-01-preview/offazure-migrate.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OffAzure/importSites/{siteName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/migrate/resource-manager/Microsoft.OffAzure/OffAzure/swagger/preview/2024-12-01-preview/offazure-migrate.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OffAzure/masterSites/{siteName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/migrate/resource-manager/Microsoft.OffAzure/OffAzure/swagger/preview/2024-12-01-preview/offazure-migrate.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OffAzure/serverSites/{siteName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/migrate/resource-manager/Microsoft.OffAzure/OffAzure/swagger/preview/2024-12-01-preview/offazure-migrate.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OffAzure/vmwareSites/{siteName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:7737:3` | The property 'provisioningState' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-65"></a>
## specification/monitor/resource-manager/Microsoft.Insights/Insights/DataCollectionApi

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/monitor/resource-manager/Microsoft.Insights/Insights/DataCollectionApi/swagger/stable/2024-03-11/dataCollection.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/dataCollectionEndpoints/{dataCollectionEndpointName}","patch","parameters"]` | identity property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/monitor/resource-manager/Microsoft.Insights/Insights/DataCollectionApi/swagger/stable/2024-03-11/dataCollection.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/dataCollectionEndpoints/{dataCollectionEndpointName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/monitor/resource-manager/Microsoft.Insights/Insights/DataCollectionApi/swagger/stable/2024-03-11/dataCollection.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/dataCollectionRules/{dataCollectionRuleName}","patch","parameters"]` | identity property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/monitor/resource-manager/Microsoft.Insights/Insights/DataCollectionApi/swagger/stable/2024-03-11/dataCollection.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/dataCollectionRules/{dataCollectionRuleName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-66"></a>
## specification/monitor/resource-manager/Microsoft.Insights/Insights/MetricAlertApi

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/monitor/resource-manager/Microsoft.Insights/Insights/MetricAlertApi/swagger/stable/2026-01-01/metricAlert.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/metricAlerts/{ruleName}","patch","parameters"]` | scopes property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/monitor/resource-manager/Microsoft.Insights/Insights/MetricAlertApi/swagger/stable/2026-01-01/metricAlert.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/metricAlerts/{ruleName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/monitor/resource-manager/Microsoft.Insights/Insights/MetricAlertApi/swagger/stable/2026-01-01/metricAlert.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/metricAlerts/{ruleName}","patch","parameters"]` | targetResourceRegion property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/monitor/resource-manager/Microsoft.Insights/Insights/MetricAlertApi/swagger/stable/2026-01-01/metricAlert.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/metricAlerts/{ruleName}","patch","parameters"]` | targetResourceType property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-67"></a>
## specification/operationalinsights/resource-manager/Microsoft.OperationalInsights/OperationalInsights

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/operationalinsights/resource-manager/Microsoft.OperationalInsights/OperationalInsights/swagger/stable/2026-03-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/clusters/{clusterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/operationalinsights/resource-manager/Microsoft.OperationalInsights/OperationalInsights/swagger/stable/2026-03-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/queryPacks/{queryPackName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/operationalinsights/resource-manager/Microsoft.OperationalInsights/OperationalInsights/swagger/stable/2026-03-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}","patch","parameters"]` | etag property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/operationalinsights/resource-manager/Microsoft.OperationalInsights/OperationalInsights/swagger/stable/2026-03-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-68"></a>
## specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/hcpopenshiftclusters

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/hcpopenshiftclusters/swagger/preview/2026-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RedHatOpenShift/hcpOpenShiftClusters/{hcpOpenShiftClusterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/hcpopenshiftclusters/swagger/preview/2026-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RedHatOpenShift/hcpOpenShiftClusters/{hcpOpenShiftClusterName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/hcpopenshiftclusters/swagger/preview/2026-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RedHatOpenShift/hcpOpenShiftClusters/{hcpOpenShiftClusterName}/nodePools/{nodePoolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/hcpopenshiftclusters/swagger/preview/2026-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RedHatOpenShift/hcpOpenShiftClusters/{hcpOpenShiftClusterName}/nodePools/{nodePoolName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-69"></a>
## specification/resources/resource-manager/Microsoft.Resources/deploymentScripts

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/resources/resource-manager/Microsoft.Resources/deploymentScripts/swagger/stable/2023-08-01/deploymentScripts.json: ["paths","/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/resources/resource-manager/Microsoft.Resources/deploymentScripts/swagger/stable/2023-08-01/deploymentScripts.json: ["paths","/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/resources/resource-manager/Microsoft.Resources/deploymentScripts/swagger/stable/2023-08-01/deploymentScripts.json: ["paths","/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/resources/resource-manager/Microsoft.Resources/deploymentScripts/swagger/stable/2023-08-01/deploymentScripts.json: ["paths","/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName}","patch","parameters"]` | type property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-70"></a>
## specification/servicenetworking/resource-manager/Microsoft.ServiceNetworking/ServiceNetworking

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/servicenetworking/resource-manager/Microsoft.ServiceNetworking/ServiceNetworking/swagger/stable/2026-03-01/TrafficController.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceNetworking/trafficControllers/{trafficControllerName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicenetworking/resource-manager/Microsoft.ServiceNetworking/ServiceNetworking/swagger/stable/2026-03-01/TrafficController.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceNetworking/trafficControllers/{trafficControllerName}/associations/{associationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicenetworking/resource-manager/Microsoft.ServiceNetworking/ServiceNetworking/swagger/stable/2026-03-01/TrafficController.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceNetworking/trafficControllers/{trafficControllerName}/frontends/{frontendName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicenetworking/resource-manager/Microsoft.ServiceNetworking/ServiceNetworking/swagger/stable/2026-03-01/TrafficController.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceNetworking/trafficControllers/{trafficControllerName}/securityPolicies/{securityPolicyName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-71"></a>
## specification/splitio/SplitIO.Experimentation.Management

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/splitio/SplitIO.Experimentation.Management/swagger/resource-manager/SplitIO.Experimentation/preview/2024-07-01-preview/splitio.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/SplitIO.Experimentation/experimentationWorkspaces/{workspaceName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/splitio/SplitIO.Experimentation.Management/swagger/resource-manager/SplitIO.Experimentation/preview/2024-07-01-preview/splitio.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/SplitIO.Experimentation/experimentationWorkspaces/{workspaceName}","patch","parameters"]` | size property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/splitio/SplitIO.Experimentation.Management/swagger/resource-manager/SplitIO.Experimentation/preview/2024-07-01-preview/splitio.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/SplitIO.Experimentation/experimentationWorkspaces/{workspaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/splitio/SplitIO.Experimentation.Management/swagger/resource-manager/SplitIO.Experimentation/preview/2024-07-01-preview/splitio.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/SplitIO.Experimentation/experimentationWorkspaces/{workspaceName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-72"></a>
## specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/registeredServers/{serverId}","patch","parameters"]` | applicationId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/serverEndpoints/{serverEndpointName}","patch","parameters"]` | tierFilesOlderThanDays property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/serverEndpoints/{serverEndpointName}","patch","parameters"]` | volumeFreeSpacePercent property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-73"></a>
## specification/workloads/resource-manager/Microsoft.Workloads/SAPVirtualInstance

Reported diagnostics: Swagger **4**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/workloads/resource-manager/Microsoft.Workloads/SAPVirtualInstance/swagger/stable/2024-09-01/SAPVirtualInstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Workloads/sapVirtualInstances/{sapVirtualInstanceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/workloads/resource-manager/Microsoft.Workloads/SAPVirtualInstance/swagger/stable/2024-09-01/SAPVirtualInstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Workloads/sapVirtualInstances/{sapVirtualInstanceName}/applicationInstances/{applicationInstanceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/workloads/resource-manager/Microsoft.Workloads/SAPVirtualInstance/swagger/stable/2024-09-01/SAPVirtualInstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Workloads/sapVirtualInstances/{sapVirtualInstanceName}/centralInstances/{centralInstanceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/workloads/resource-manager/Microsoft.Workloads/SAPVirtualInstance/swagger/stable/2024-09-01/SAPVirtualInstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Workloads/sapVirtualInstances/{sapVirtualInstanceName}/databaseInstances/{databaseInstanceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-74"></a>
## specification/apimanagement/resource-manager/Microsoft.ApiManagement/AIGateway

Reported diagnostics: Swagger **3**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/AIGateway/swagger/preview/2026-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/aigateways/{aiGatewayName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/AIGateway/swagger/preview/2026-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/aigateways/{aiGatewayName}","patch","parameters"]` | size property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/AIGateway/swagger/preview/2026-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/aigateways/{aiGatewayName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-75"></a>
## specification/appconfiguration/resource-manager/Microsoft.AppConfiguration/AppConfiguration

Reported diagnostics: Swagger **3**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/appconfiguration/resource-manager/Microsoft.AppConfiguration/AppConfiguration/swagger/preview/2025-08-01-preview/appconfiguration.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}","patch","parameters"]` | disableLocalAuth property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/appconfiguration/resource-manager/Microsoft.AppConfiguration/AppConfiguration/swagger/preview/2025-08-01-preview/appconfiguration.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}","patch","parameters"]` | enablePurgeProtection property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/appconfiguration/resource-manager/Microsoft.AppConfiguration/AppConfiguration/swagger/preview/2025-08-01-preview/appconfiguration.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-76"></a>
## specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/WorkbooksApi

Reported diagnostics: Swagger **4**, TypeSpec **1**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/WorkbooksApi/swagger/stable/2023-06-01/workbooks_API.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/workbooks/{resourceName}","patch","parameters"]` | kind property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/WorkbooksApi/swagger/stable/2023-06-01/workbooks_API.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/workbooks/{resourceName}","patch","parameters"]` | revision property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/WorkbooksApi/swagger/stable/2023-06-01/workbooks_API.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/workbooks/{resourceName}","patch","parameters"]` | serializedData property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/WorkbooksApi/swagger/stable/2023-06-01/workbooks_API.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/workbooks/{resourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:254:3` | The property 'revision' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-77"></a>
## specification/azure-kusto/resource-manager/Microsoft.Kusto/Kusto

Reported diagnostics: Swagger **3**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/azure-kusto/resource-manager/Microsoft.Kusto/Kusto/swagger/stable/2025-02-14/kusto.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}","patch","parameters"]` | location property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azure-kusto/resource-manager/Microsoft.Kusto/Kusto/swagger/stable/2025-02-14/kusto.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azure-kusto/resource-manager/Microsoft.Kusto/Kusto/swagger/stable/2025-02-14/kusto.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}","patch","parameters"]` | zones property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-78"></a>
## specification/azurefleet/resource-manager/Microsoft.AzureFleet/AzureFleet

Reported diagnostics: Swagger **3**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/azurefleet/resource-manager/Microsoft.AzureFleet/AzureFleet/swagger/stable/2026-08-01/azurefleet.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureFleet/fleets/{fleetName}","patch","parameters"]` | product property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurefleet/resource-manager/Microsoft.AzureFleet/AzureFleet/swagger/stable/2026-08-01/azurefleet.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureFleet/fleets/{fleetName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurefleet/resource-manager/Microsoft.AzureFleet/AzureFleet/swagger/stable/2026-08-01/azurefleet.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureFleet/fleets/{fleetName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-79"></a>
## specification/azurelargeinstance/resource-manager/Microsoft.AzureLargeInstance/AzureLargeInstance

Reported diagnostics: Swagger **3**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/azurelargeinstance/resource-manager/Microsoft.AzureLargeInstance/AzureLargeInstance/swagger/preview/2024-08-01-preview/azurelargeinstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureLargeInstance/azureLargeInstances/{azureLargeInstanceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurelargeinstance/resource-manager/Microsoft.AzureLargeInstance/AzureLargeInstance/swagger/preview/2024-08-01-preview/azurelargeinstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureLargeInstance/azureLargeStorageInstances/{azureLargeStorageInstanceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azurelargeinstance/resource-manager/Microsoft.AzureLargeInstance/AzureLargeInstance/swagger/preview/2024-08-01-preview/azurelargeinstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureLargeInstance/azureLargeStorageInstances/{azureLargeStorageInstanceName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-80"></a>
## specification/azureresiliencemanagement/resource-manager/Microsoft.AzureResilienceManagement/AzureResilienceManagement

Reported diagnostics: Swagger **3**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/azureresiliencemanagement/resource-manager/Microsoft.AzureResilienceManagement/AzureResilienceManagement/swagger/preview/2026-10-31-preview/openapi.json: ["paths","/providers/Microsoft.Management/serviceGroups/{serviceGroupName}/providers/Microsoft.AzureResilienceManagement/drills/{drillName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azureresiliencemanagement/resource-manager/Microsoft.AzureResilienceManagement/AzureResilienceManagement/swagger/preview/2026-10-31-preview/openapi.json: ["paths","/providers/Microsoft.Management/serviceGroups/{serviceGroupName}/providers/Microsoft.AzureResilienceManagement/recoveryPlans/{recoveryPlanName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azureresiliencemanagement/resource-manager/Microsoft.AzureResilienceManagement/AzureResilienceManagement/swagger/preview/2026-10-31-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureResilienceManagement/usagePlans/{usagePlanName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-81"></a>
## specification/chaos/resource-manager/Microsoft.Chaos/Chaos

Reported diagnostics: Swagger **3**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/chaos/resource-manager/Microsoft.Chaos/Chaos/swagger/preview/2026-08-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Chaos/experiments/{experimentName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/chaos/resource-manager/Microsoft.Chaos/Chaos/swagger/preview/2026-08-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Chaos/privateAccesses/{privateAccessName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/chaos/resource-manager/Microsoft.Chaos/Chaos/swagger/preview/2026-08-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Chaos/workspaces/{workspaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-82"></a>
## specification/datadog/resource-manager/Microsoft.Datadog/Datadog

Reported diagnostics: Swagger **3**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/datadog/resource-manager/Microsoft.Datadog/Datadog/swagger/preview/2025-12-26-preview/datadog.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Datadog/monitors/{monitorName}","patch","parameters"]` | cspm property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/datadog/resource-manager/Microsoft.Datadog/Datadog/swagger/preview/2025-12-26-preview/datadog.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Datadog/monitors/{monitorName}","patch","parameters"]` | resourceCollection property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/datadog/resource-manager/Microsoft.Datadog/Datadog/swagger/preview/2025-12-26-preview/datadog.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Datadog/monitors/{monitorName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-83"></a>
## specification/fist/resource-manager/Microsoft.IoTFirmwareDefense/IoTFirmwareDefense

Reported diagnostics: Swagger **3**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/fist/resource-manager/Microsoft.IoTFirmwareDefense/IoTFirmwareDefense/swagger/preview/2026-06-01-preview/iotfirmwaredefense.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTFirmwareDefense/workspaces/{workspaceName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/fist/resource-manager/Microsoft.IoTFirmwareDefense/IoTFirmwareDefense/swagger/preview/2026-06-01-preview/iotfirmwaredefense.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTFirmwareDefense/workspaces/{workspaceName}","patch","parameters"]` | size property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/fist/resource-manager/Microsoft.IoTFirmwareDefense/IoTFirmwareDefense/swagger/preview/2026-06-01-preview/iotfirmwaredefense.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTFirmwareDefense/workspaces/{workspaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-84"></a>
## specification/hardwaresecuritymodules/resource-manager/Microsoft.HardwareSecurityModules/HardwareSecurityModules

Reported diagnostics: Swagger **3**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/hardwaresecuritymodules/resource-manager/Microsoft.HardwareSecurityModules/HardwareSecurityModules/swagger/preview/2025-12-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HardwareSecurityModules/cloudHsmClusters/{cloudHsmClusterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/hardwaresecuritymodules/resource-manager/Microsoft.HardwareSecurityModules/HardwareSecurityModules/swagger/preview/2025-12-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HardwareSecurityModules/dedicatedHSMs/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/hardwaresecuritymodules/resource-manager/Microsoft.HardwareSecurityModules/HardwareSecurityModules/swagger/preview/2025-12-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HardwareSecurityModules/paymentHsmClusters/{paymentHsmClusterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-85"></a>
## specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity

Reported diagnostics: Swagger **3**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/swagger/stable/2027-01-01/hybridconnectivity.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridConnectivity/publicCloudConnectors/{publicCloudConnector}","patch","parameters"]` | excludedFolderIds property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/swagger/stable/2027-01-01/hybridconnectivity.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridConnectivity/publicCloudConnectors/{publicCloudConnector}","patch","parameters"]` | excludedProjectNumbers property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity/swagger/stable/2027-01-01/hybridconnectivity.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridConnectivity/publicCloudConnectors/{publicCloudConnector}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-86"></a>
## specification/iotoperationsdataprocessor/resource-manager/Microsoft.IoTOperationsDataProcessor/IoTOperationsDataProcessor

Reported diagnostics: Swagger **3**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/iotoperationsdataprocessor/resource-manager/Microsoft.IoTOperationsDataProcessor/IoTOperationsDataProcessor/swagger/preview/2023-10-04-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTOperationsDataProcessor/instances/{instanceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/iotoperationsdataprocessor/resource-manager/Microsoft.IoTOperationsDataProcessor/IoTOperationsDataProcessor/swagger/preview/2023-10-04-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTOperationsDataProcessor/instances/{instanceName}/datasets/{datasetName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/iotoperationsdataprocessor/resource-manager/Microsoft.IoTOperationsDataProcessor/IoTOperationsDataProcessor/swagger/preview/2023-10-04-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTOperationsDataProcessor/instances/{instanceName}/pipelines/{pipelineName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-87"></a>
## specification/iotoperationsorchestrator/resource-manager/Microsoft.IoTOperationsOrchestrator/IoTOperationsOrchestrator

Reported diagnostics: Swagger **3**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/iotoperationsorchestrator/resource-manager/Microsoft.IoTOperationsOrchestrator/IoTOperationsOrchestrator/swagger/preview/2023-10-04-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTOperationsOrchestrator/instances/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/iotoperationsorchestrator/resource-manager/Microsoft.IoTOperationsOrchestrator/IoTOperationsOrchestrator/swagger/preview/2023-10-04-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTOperationsOrchestrator/solutions/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/iotoperationsorchestrator/resource-manager/Microsoft.IoTOperationsOrchestrator/IoTOperationsOrchestrator/swagger/preview/2023-10-04-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTOperationsOrchestrator/targets/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-88"></a>
## specification/monitoringservice/resource-manager/Microsoft.Monitor/Agents

Reported diagnostics: Swagger **3**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/monitoringservice/resource-manager/Microsoft.Monitor/Agents/swagger/preview/2026-05-01-preview/agents.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Monitor/observabilityAgents/{observabilityAgentName}","patch","parameters"]` | enabled property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/monitoringservice/resource-manager/Microsoft.Monitor/Agents/swagger/preview/2026-05-01-preview/agents.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Monitor/observabilityAgents/{observabilityAgentName}","patch","parameters"]` | monitoringAccountId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/monitoringservice/resource-manager/Microsoft.Monitor/Agents/swagger/preview/2026-05-01-preview/agents.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Monitor/observabilityAgents/{observabilityAgentName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-89"></a>
## specification/purestorage/resource-manager/PureStorage.Block/PureStorageBlock

Reported diagnostics: Swagger **3**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/purestorage/resource-manager/PureStorage.Block/PureStorageBlock/swagger/preview/2026-05-01-preview/purestorage.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/PureStorage.Block/reservations/{reservationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/purestorage/resource-manager/PureStorage.Block/PureStorageBlock/swagger/preview/2026-05-01-preview/purestorage.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/PureStorage.Block/storagePools/{storagePoolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/purestorage/resource-manager/PureStorage.Block/PureStorageBlock/swagger/preview/2026-05-01-preview/purestorage.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/PureStorage.Block/storagePools/{storagePoolName}/volumeGroups/{volumeGroupName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-90"></a>
## specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices

Reported diagnostics: Swagger **3**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices/swagger/preview/2026-08-31-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}","patch","parameters"]` | etag property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices/swagger/preview/2026-08-31-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}","patch","parameters"]` | location property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices/swagger/preview/2026-08-31-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-91"></a>
## specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery

Reported diagnostics: Swagger **12**, TypeSpec **9**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationNetworks/{networkName}/replicationNetworkMappings/{networkMappingName}","patch","parameters"]` | recoveryFabricName property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}","patch","parameters"]` | enableRdpOnTargetOption property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}","patch","parameters"]` | licenseType property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}","patch","parameters"]` | recoveryAvailabilitySetId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}","patch","parameters"]` | recoveryAzureVMName property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}","patch","parameters"]` | recoveryAzureVMSize property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}","patch","parameters"]` | selectedRecoveryAzureNetworkId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}","patch","parameters"]` | selectedSourceNicId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}","patch","parameters"]` | selectedTfoAzureNetworkId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}","patch","parameters"]` | vmNics property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationvCenters/{vcenterName}","patch","parameters"]` | processServerId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationvCenters/{vcenterName}","patch","parameters"]` | runAsAccountId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:3352:3` | The property 'recoveryAzureVMName' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:3358:3` | The property 'recoveryAzureVMSize' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:3363:3` | The property 'selectedRecoveryAzureNetworkId' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:3368:3` | The property 'selectedTfoAzureNetworkId' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:3373:3` | The property 'selectedSourceNicId' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:3378:3` | The property 'enableRdpOnTargetOption' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:3384:3` | The property 'vmNics' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:3389:3` | The property 'licenseType' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:3394:3` | The property 'recoveryAvailabilitySetId' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-92"></a>
## specification/storagediscovery/resource-manager/Microsoft.StorageDiscovery/StorageDiscovery

Reported diagnostics: Swagger **3**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/storagediscovery/resource-manager/Microsoft.StorageDiscovery/StorageDiscovery/swagger/preview/2026-10-01-preview/storageDiscoveryWorkspace.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageDiscovery/storageDiscoveryWorkspaces/{storageDiscoveryWorkspaceName}","patch","parameters"]` | prefixConfigurations property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storagediscovery/resource-manager/Microsoft.StorageDiscovery/StorageDiscovery/swagger/preview/2026-10-01-preview/storageDiscoveryWorkspace.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageDiscovery/storageDiscoveryWorkspaces/{storageDiscoveryWorkspaceName}","patch","parameters"]` | sku property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storagediscovery/resource-manager/Microsoft.StorageDiscovery/StorageDiscovery/swagger/preview/2026-10-01-preview/storageDiscoveryWorkspace.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageDiscovery/storageDiscoveryWorkspaces/{storageDiscoveryWorkspaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-93"></a>
## specification/storagemover/resource-manager/Microsoft.StorageMover/StorageMover

Reported diagnostics: Swagger **3**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/storagemover/resource-manager/Microsoft.StorageMover/StorageMover/swagger/stable/2026-05-01/storagemover.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageMover/storageMovers/{storageMoverName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storagemover/resource-manager/Microsoft.StorageMover/StorageMover/swagger/stable/2026-05-01/storagemover.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageMover/storageMovers/{storageMoverName}/projects/{projectName}/jobDefinitions/{jobDefinitionName}","patch","parameters"]` | dataIntegrityValidation property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/storagemover/resource-manager/Microsoft.StorageMover/StorageMover/swagger/stable/2026-05-01/storagemover.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageMover/storageMovers/{storageMoverName}/projects/{projectName}/jobDefinitions/{jobDefinitionName}","patch","parameters"]` | description property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-94"></a>
## specification/alertsmanagement/resource-manager/Microsoft.AlertsManagement/AlertProcessingRules

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/alertsmanagement/resource-manager/Microsoft.AlertsManagement/AlertProcessingRules/swagger/stable/2021-08-08/AlertProcessingRules.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AlertsManagement/actionRules/{alertProcessingRuleName}","patch","parameters"]` | enabled property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/alertsmanagement/resource-manager/Microsoft.AlertsManagement/AlertProcessingRules/swagger/stable/2021-08-08/AlertProcessingRules.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AlertsManagement/actionRules/{alertProcessingRuleName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-95"></a>
## specification/alertsmanagement/resource-manager/Microsoft.AlertsManagement/PrometheusRuleGroups

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/alertsmanagement/resource-manager/Microsoft.AlertsManagement/PrometheusRuleGroups/swagger/stable/2023-03-01/PrometheusRuleGroups.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AlertsManagement/prometheusRuleGroups/{ruleGroupName}","patch","parameters"]` | enabled property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/alertsmanagement/resource-manager/Microsoft.AlertsManagement/PrometheusRuleGroups/swagger/stable/2023-03-01/PrometheusRuleGroups.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AlertsManagement/prometheusRuleGroups/{ruleGroupName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-96"></a>
## specification/anyscale/resource-manager/Anyscale.Platform/platform

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/anyscale/resource-manager/Anyscale.Platform/platform/swagger/stable/2026-09-01/anyscale.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Anyscale.Platform/clouds/{cloudName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/anyscale/resource-manager/Anyscale.Platform/platform/swagger/stable/2026-09-01/anyscale.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Anyscale.Platform/clouds/{cloudName}/cloudResources/{cloudResourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-97"></a>
## specification/app/resource-manager/Microsoft.App/SreAgent

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/app/resource-manager/Microsoft.App/SreAgent/swagger/stable/2026-01-01/sreagent.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/agents/{agentName}","patch","parameters"]` | initialSponsorGroupId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/app/resource-manager/Microsoft.App/SreAgent/swagger/stable/2026-01-01/sreagent.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/agents/{agentName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-98"></a>
## specification/automation/resource-manager/Microsoft.Automation/Automation

Reported diagnostics: Swagger **11**, TypeSpec **9**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/connections/{connectionName}","patch","parameters"]` | fieldDefinitionValues property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/modules/{moduleName}","patch","parameters"]` | location property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/modules/{moduleName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/schedules/{scheduleName}","patch","parameters"]` | isEnabled property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}","patch","parameters"]` | autoSync property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}","patch","parameters"]` | branch property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}","patch","parameters"]` | description property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}","patch","parameters"]` | folderPath property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/watchers/{watcherName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/webhooks/{webhookName}","patch","parameters"]` | description property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:5200:3` | The property 'createdAt' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:5200:3` | The property 'createdBy' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:5200:3` | The property 'createdByType' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:5200:3` | The property 'lastModifiedAt' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:5200:3` | The property 'lastModifiedBy' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:5200:3` | The property 'lastModifiedByType' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:5423:3` | The property 'isEnabled' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:6349:3` | The property 'name' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:6519:3` | The property 'description' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-99"></a>
## specification/azuredependencymap/resource-manager/Microsoft.DependencyMap/DependencyMap

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/azuredependencymap/resource-manager/Microsoft.DependencyMap/DependencyMap/swagger/preview/2025-07-01-preview/dependencyMap.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DependencyMap/maps/{mapName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/azuredependencymap/resource-manager/Microsoft.DependencyMap/DependencyMap/swagger/preview/2025-07-01-preview/dependencyMap.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DependencyMap/maps/{mapName}/discoverySources/{sourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-100"></a>
## specification/databricks/resource-manager/Microsoft.Databricks/Databricks

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/databricks/resource-manager/Microsoft.Databricks/Databricks/swagger/stable/2026-01-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Databricks/accessConnectors/{connectorName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/databricks/resource-manager/Microsoft.Databricks/Databricks/swagger/stable/2026-01-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Databricks/workspaces/{workspaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-101"></a>
## specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataMigration/migrationServices/{migrationServiceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/swagger/preview/2025-09-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataMigration/sqlMigrationServices/{sqlMigrationServiceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-102"></a>
## specification/dataprotection/resource-manager/Microsoft.DataProtection/DataProtection

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/dataprotection/resource-manager/Microsoft.DataProtection/DataProtection/swagger/stable/2026-07-01/dataprotection.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataProtection/backupVaults/{vaultName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dataprotection/resource-manager/Microsoft.DataProtection/DataProtection/swagger/stable/2026-07-01/dataprotection.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataProtection/resourceGuards/{resourceGuardsName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-103"></a>
## specification/dell/resource-manager/Dell.Storage/DellStorage

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/dell/resource-manager/Dell.Storage/DellStorage/swagger/preview/2025-03-21-preview/Dell.Storage.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Dell.Storage/filesystems/{filesystemName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/dell/resource-manager/Dell.Storage/DellStorage/swagger/preview/2025-03-21-preview/Dell.Storage.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Dell.Storage/filesystems/{filesystemName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-104"></a>
## specification/developerhub/resource-manager/Microsoft.DevHub/DeveloperHub

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/developerhub/resource-manager/Microsoft.DevHub/DeveloperHub/swagger/preview/2025-03-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevHub/iacProfiles/{iacProfileName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/developerhub/resource-manager/Microsoft.DevHub/DeveloperHub/swagger/preview/2025-03-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevHub/workflows/{workflowName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-105"></a>
## specification/edgeorder/resource-manager/Microsoft.EdgeOrder/EdgeOrder

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/edgeorder/resource-manager/Microsoft.EdgeOrder/EdgeOrder/swagger/stable/2024-02-01/edgeorder.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EdgeOrder/addresses/{addressName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/edgeorder/resource-manager/Microsoft.EdgeOrder/EdgeOrder/swagger/stable/2024-02-01/edgeorder.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EdgeOrder/orderItems/{orderItemName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-106"></a>
## specification/ews/resource-manager/Microsoft.SecretSyncController/SecretSyncController

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/ews/resource-manager/Microsoft.SecretSyncController/SecretSyncController/swagger/preview/2026-09-25-preview/secretsynccontroller.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SecretSyncController/azureKeyVaultSecretProviderClasses/{azureKeyVaultSecretProviderClassName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/ews/resource-manager/Microsoft.SecretSyncController/SecretSyncController/swagger/preview/2026-09-25-preview/secretsynccontroller.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SecretSyncController/secretSyncs/{secretSyncName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-107"></a>
## specification/extendedlocation/resource-manager/Microsoft.ExtendedLocation/CustomLocations

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/extendedlocation/resource-manager/Microsoft.ExtendedLocation/CustomLocations/swagger/preview/2021-08-31-preview/customlocations.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ExtendedLocation/customLocations/{resourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/extendedlocation/resource-manager/Microsoft.ExtendedLocation/CustomLocations/swagger/preview/2021-08-31-preview/customlocations.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ExtendedLocation/customLocations/{resourceName}/resourceSyncRules/{childResourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-108"></a>
## specification/healthbot/resource-manager/Microsoft.HealthBot/HealthBot

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/healthbot/resource-manager/Microsoft.HealthBot/HealthBot/swagger/stable/2025-11-01/healthbot.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthBot/healthBots/{botName}","patch","parameters"]` | location property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/healthbot/resource-manager/Microsoft.HealthBot/HealthBot/swagger/stable/2025-11-01/healthbot.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthBot/healthBots/{botName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-109"></a>
## specification/healthdataaiservices/resource-manager/Microsoft.HealthDataAIServices/HealthDataAIServices

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/healthdataaiservices/resource-manager/Microsoft.HealthDataAIServices/HealthDataAIServices/swagger/stable/2024-09-20/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthDataAIServices/deidServices/{deidServiceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/healthdataaiservices/resource-manager/Microsoft.HealthDataAIServices/HealthDataAIServices/swagger/stable/2024-09-20/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthDataAIServices/deidServices/{deidServiceName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-110"></a>
## specification/informatica/resource-manager/Informatica.DataManagement/Informatica

Reported diagnostics: Swagger **4**, TypeSpec **2**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/informatica/resource-manager/Informatica.DataManagement/Informatica/swagger/stable/2025-11-27/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Informatica.DataManagement/organizations/{organizationName}","patch","parameters"]` | properties property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/informatica/resource-manager/Informatica.DataManagement/Informatica/swagger/stable/2025-11-27/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Informatica.DataManagement/organizations/{organizationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/informatica/resource-manager/Informatica.DataManagement/Informatica/swagger/stable/2025-11-27/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Informatica.DataManagement/organizations/{organizationName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/informatica/resource-manager/Informatica.DataManagement/Informatica/swagger/stable/2025-11-27/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Informatica.DataManagement/organizations/{organizationName}/serverlessRuntimes/{serverlessRuntimeName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `main.tsp:739:3` | The property 'informaticaOrganizationProperties' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `main.tsp:751:3` | The property 'existingResourceId' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-111"></a>
## specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/extensions

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/extensions/swagger/stable/2025-03-01/extensions.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/extensions/{extensionName}","patch","parameters"]` | configurationProtectedSettings property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/extensions/swagger/stable/2025-03-01/extensions.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/extensions/{extensionName}","patch","parameters"]` | version property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-112"></a>
## specification/liftrarize/resource-manager/ArizeAi.ObservabilityEval/ObservabilityEval

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/liftrarize/resource-manager/ArizeAi.ObservabilityEval/ObservabilityEval/swagger/preview/2024-10-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/ArizeAi.ObservabilityEval/organizations/{organizationname}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/liftrarize/resource-manager/ArizeAi.ObservabilityEval/ObservabilityEval/swagger/preview/2024-10-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/ArizeAi.ObservabilityEval/organizations/{organizationname}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-113"></a>
## specification/liftrcommvault/Commvault.ContentStore.Management

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/liftrcommvault/Commvault.ContentStore.Management/swagger/resource-manager/Commvault.ContentStore/stable/2026-09-30/commvault.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Commvault.ContentStore/cloudAccounts/{cloudAccountName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/liftrcommvault/Commvault.ContentStore.Management/swagger/resource-manager/Commvault.ContentStore/stable/2026-09-30/commvault.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Commvault.ContentStore/cloudAccounts/{cloudAccountName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-114"></a>
## specification/liftrhyperexecute/resource-manager/LambdaTest.HyperExecute/HyperExecute

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/liftrhyperexecute/resource-manager/LambdaTest.HyperExecute/HyperExecute/swagger/preview/2024-02-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/LambdaTest.HyperExecute/organizations/{organizationname}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/liftrhyperexecute/resource-manager/LambdaTest.HyperExecute/HyperExecute/swagger/preview/2024-02-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/LambdaTest.HyperExecute/organizations/{organizationname}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-115"></a>
## specification/liftrmongodb/resource-manager/MongoDB.Atlas/MongoDBAtlas

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/liftrmongodb/resource-manager/MongoDB.Atlas/MongoDBAtlas/swagger/preview/2026-03-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/MongoDB.Atlas/organizations/{organizationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/liftrmongodb/resource-manager/MongoDB.Atlas/MongoDBAtlas/swagger/preview/2026-03-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/MongoDB.Atlas/organizations/{organizationName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-116"></a>
## specification/liftrpinecone/resource-manager/Pinecone.VectorDb/PineconeVectorDb

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/liftrpinecone/resource-manager/Pinecone.VectorDb/PineconeVectorDb/swagger/preview/2024-10-22-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Pinecone.VectorDb/organizations/{organizationname}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/liftrpinecone/resource-manager/Pinecone.VectorDb/PineconeVectorDb/swagger/preview/2024-10-22-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Pinecone.VectorDb/organizations/{organizationname}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-117"></a>
## specification/liftrweightsandbiases/resource-manager/Microsoft.WeightsAndBiases/WeightsAndBiases

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/liftrweightsandbiases/resource-manager/Microsoft.WeightsAndBiases/WeightsAndBiases/swagger/preview/2024-09-18-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WeightsAndBiases/instances/{instancename}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/liftrweightsandbiases/resource-manager/Microsoft.WeightsAndBiases/WeightsAndBiases/swagger/preview/2024-09-18-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WeightsAndBiases/instances/{instancename}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-118"></a>
## specification/maps/resource-manager/Microsoft.Maps/Maps

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/maps/resource-manager/Microsoft.Maps/Maps/swagger/preview/2025-10-01-preview/maps-management.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Maps/accounts/{accountName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/maps/resource-manager/Microsoft.Maps/Maps/swagger/preview/2025-10-01-preview/maps-management.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Maps/accounts/{accountName}/creators/{creatorName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-119"></a>
## specification/monitor/resource-manager/Microsoft.Insights/Insights/ActionGroupsApi

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/monitor/resource-manager/Microsoft.Insights/Insights/ActionGroupsApi/swagger/preview/2024-10-01-preview/actionGroups.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/actionGroups/{actionGroupName}","patch","parameters"]` | enabled property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/monitor/resource-manager/Microsoft.Insights/Insights/ActionGroupsApi/swagger/preview/2024-10-01-preview/actionGroups.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/actionGroups/{actionGroupName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-120"></a>
## specification/monitor/resource-manager/Microsoft.Insights/Insights/TenantActionGroups

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/monitor/resource-manager/Microsoft.Insights/Insights/TenantActionGroups/swagger/preview/2023-05-01-preview/tenantActionGroups.json: ["paths","/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Insights/tenantActionGroups/{tenantActionGroupName}","patch","parameters"]` | enabled property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/monitor/resource-manager/Microsoft.Insights/Insights/TenantActionGroups/swagger/preview/2023-05-01-preview/tenantActionGroups.json: ["paths","/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Insights/tenantActionGroups/{tenantActionGroupName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-121"></a>
## specification/mysql/resource-manager/Microsoft.DBforMySQL/FlexibleServers

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/mysql/resource-manager/Microsoft.DBforMySQL/FlexibleServers/swagger/preview/2025-12-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/flexibleServers/{serverName}","patch","parameters"]` | administratorLoginPassword property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/mysql/resource-manager/Microsoft.DBforMySQL/FlexibleServers/swagger/preview/2025-12-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/flexibleServers/{serverName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-122"></a>
## specification/napster/Napster.CompanionAPI.Management

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/napster/Napster.CompanionAPI.Management/swagger/resource-manager/Napster.CompanionAPI/stable/2026-08-11/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Napster.CompanionAPI/organizations/{organizationname}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/napster/Napster.CompanionAPI.Management/swagger/resource-manager/Napster.CompanionAPI/stable/2026-08-11/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Napster.CompanionAPI/organizations/{organizationname}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-123"></a>
## specification/notificationhubs/resource-manager/Microsoft.NotificationHubs/NotificationHubs

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/notificationhubs/resource-manager/Microsoft.NotificationHubs/NotificationHubs/swagger/preview/2023-10-01-preview/notificationhubs.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/notificationhubs/resource-manager/Microsoft.NotificationHubs/NotificationHubs/swagger/preview/2023-10-01-preview/notificationhubs.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-124"></a>
## specification/onlineexperimentation/resource-manager/Microsoft.OnlineExperimentation/OnlineExperimentation

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/onlineexperimentation/resource-manager/Microsoft.OnlineExperimentation/OnlineExperimentation/swagger/preview/2025-08-01-preview/OnlineExperimentationWorkspace.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OnlineExperimentation/workspaces/{workspaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/onlineexperimentation/resource-manager/Microsoft.OnlineExperimentation/OnlineExperimentation/swagger/preview/2025-08-01-preview/OnlineExperimentationWorkspace.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OnlineExperimentation/workspaces/{workspaceName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-125"></a>
## specification/orbitalplanetarycomputer/Orbital.Management

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/orbitalplanetarycomputer/Orbital.Management/swagger/resource-manager/Microsoft.Orbital/stable/2026-04-15/planetarycomputer.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Orbital/geoCatalogs/{catalogName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/orbitalplanetarycomputer/Orbital.Management/swagger/resource-manager/Microsoft.Orbital/stable/2026-04-15/planetarycomputer.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Orbital/geoCatalogs/{catalogName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-126"></a>
## specification/paloaltonetworks/resource-manager/PaloAltoNetworks.Cloudngfw/Cloudngfw

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/paloaltonetworks/resource-manager/PaloAltoNetworks.Cloudngfw/Cloudngfw/swagger/preview/2026-08-27-preview/PaloAltoNetworks.Cloudngfw.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/PaloAltoNetworks.Cloudngfw/firewalls/{firewallName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/paloaltonetworks/resource-manager/PaloAltoNetworks.Cloudngfw/Cloudngfw/swagger/preview/2026-08-27-preview/PaloAltoNetworks.Cloudngfw.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/PaloAltoNetworks.Cloudngfw/localRulestacks/{localRulestackName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-127"></a>
## specification/peering/resource-manager/Microsoft.Peering/Peering

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/peering/resource-manager/Microsoft.Peering/Peering/swagger/stable/2025-05-01/peering.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/peering/resource-manager/Microsoft.Peering/Peering/swagger/stable/2025-05-01/peering.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-128"></a>
## specification/platformvalidation/resource-manager/Microsoft.PlatformValidation/PlatformValidation

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/platformvalidation/resource-manager/Microsoft.PlatformValidation/PlatformValidation/swagger/preview/2026-08-01-preview/platformvalidation.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PlatformValidation/cloudValidations/{cloudValidationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/platformvalidation/resource-manager/Microsoft.PlatformValidation/PlatformValidation/swagger/preview/2026-08-01-preview/platformvalidation.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PlatformValidation/cloudValidations/{cloudValidationName}/validationExecutionPlans/{validationExecutionPlanName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-129"></a>
## specification/powerbidedicated/resource-manager/Microsoft.PowerBIdedicated/PowerBIDedicated

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/powerbidedicated/resource-manager/Microsoft.PowerBIdedicated/PowerBIDedicated/swagger/stable/2021-01-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBIDedicated/autoScaleVCores/{vcoreName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/powerbidedicated/resource-manager/Microsoft.PowerBIdedicated/PowerBIDedicated/swagger/stable/2021-01-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBIDedicated/capacities/{dedicatedCapacityName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-130"></a>
## specification/powerplatform/resource-manager/Microsoft.PowerPlatform/PowerPlatform

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/powerplatform/resource-manager/Microsoft.PowerPlatform/PowerPlatform/swagger/preview/2020-10-30-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerPlatform/accounts/{accountName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/powerplatform/resource-manager/Microsoft.PowerPlatform/PowerPlatform/swagger/preview/2020-10-30-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerPlatform/enterprisePolicies/{enterprisePolicyName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-131"></a>
## specification/privatetrafficmanager/resource-manager/Microsoft.Network/PrivateTrafficManager

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/privatetrafficmanager/resource-manager/Microsoft.Network/PrivateTrafficManager/swagger/preview/2026-10-01-preview/privateTrafficManager.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateTrafficManagerProfiles/{privateTrafficManagerProfileName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/privatetrafficmanager/resource-manager/Microsoft.Network/PrivateTrafficManager/swagger/preview/2026-10-01-preview/privateTrafficManager.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/topologyMaps/{topologyMapName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-132"></a>
## specification/programmableconnectivity/ProgrammableConnectivity.Management

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/programmableconnectivity/ProgrammableConnectivity.Management/swagger/resource-manager/Microsoft.ProgrammableConnectivity/preview/2025-03-30-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ProgrammableConnectivity/gateways/{gatewayName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/programmableconnectivity/ProgrammableConnectivity.Management/swagger/resource-manager/Microsoft.ProgrammableConnectivity/preview/2025-03-30-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ProgrammableConnectivity/operatorApiConnections/{operatorApiConnectionName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-133"></a>
## specification/quota/resource-manager/Microsoft.Quota/Quota

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/quota/resource-manager/Microsoft.Quota/Quota/swagger/preview/2026-09-01-preview/openapi.json: ["paths","/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Quota/groupQuotas/{groupQuotaName}","patch","parameters"]` | properties property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/quota/resource-manager/Microsoft.Quota/Quota/swagger/preview/2026-09-01-preview/openapi.json: ["paths","/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Quota/groupQuotas/{groupQuotaName}/subscriptions/{subscriptionId}","patch","parameters"]` | Patch operations body cannot be empty. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-134"></a>
## specification/relay/resource-manager/Microsoft.Relay/Relay

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/relay/resource-manager/Microsoft.Relay/Relay/swagger/preview/2026-07-01-preview/relay.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/clusters/{clusterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/relay/resource-manager/Microsoft.Relay/Relay/swagger/preview/2026-07-01-preview/relay.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-135"></a>
## specification/search/resource-manager/Microsoft.Search/Search

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/search/resource-manager/Microsoft.Search/Search/swagger/preview/2026-09-01-preview/search.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}","patch","parameters"]` | location property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/search/resource-manager/Microsoft.Search/Search/swagger/preview/2026-09-01-preview/search.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-136"></a>
## specification/security/resource-manager/Microsoft.Security/Security/ServiceEntitlementSettingsAPI

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/security/resource-manager/Microsoft.Security/Security/ServiceEntitlementSettingsAPI/swagger/preview/2026-09-16-preview/serviceEntitlementSettings.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/serviceEntitlementSettings/{serviceEntitlementSettingName}","patch","parameters"]` | isDefault property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/security/resource-manager/Microsoft.Security/Security/ServiceEntitlementSettingsAPI/swagger/preview/2026-09-16-preview/serviceEntitlementSettings.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/serviceEntitlementSettings/{serviceEntitlementSettingName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-137"></a>
## specification/servicebus/resource-manager/Microsoft.ServiceBus/ServiceBus

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/servicebus/resource-manager/Microsoft.ServiceBus/ServiceBus/swagger/preview/2026-07-01-preview/servicebus.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}","patch","parameters"]` | location property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/servicebus/resource-manager/Microsoft.ServiceBus/ServiceBus/swagger/preview/2026-07-01-preview/servicebus.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-138"></a>
## specification/solutions/resource-manager/Microsoft.Solutions/Solutions

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/solutions/resource-manager/Microsoft.Solutions/Solutions/swagger/preview/2023-12-01-preview/managedapplications.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/applicationDefinitions/{applicationDefinitionName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/solutions/resource-manager/Microsoft.Solutions/Solutions/swagger/preview/2023-12-01-preview/managedapplications.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/jitRequests/{jitRequestName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-139"></a>
## specification/sovereign/resource-manager/Microsoft.Sovereign/Sovereign

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/sovereign/resource-manager/Microsoft.Sovereign/Sovereign/swagger/preview/2025-02-27-preview/sovereign.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sovereign/landingZoneAccounts/{landingZoneAccountName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/sovereign/resource-manager/Microsoft.Sovereign/Sovereign/swagger/preview/2025-02-27-preview/sovereign.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sovereign/landingZoneAccounts/{landingZoneAccountName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-140"></a>
## specification/sqlvirtualmachine/resource-manager/Microsoft.SqlVirtualMachine/SqlVirtualMachine

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/sqlvirtualmachine/resource-manager/Microsoft.SqlVirtualMachine/SqlVirtualMachine/swagger/stable/2023-10-01/sqlvm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SqlVirtualMachine/sqlVirtualMachineGroups/{sqlVirtualMachineGroupName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/sqlvirtualmachine/resource-manager/Microsoft.SqlVirtualMachine/SqlVirtualMachine/swagger/stable/2023-10-01/sqlvm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SqlVirtualMachine/sqlVirtualMachines/{sqlVirtualMachineName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-141"></a>
## specification/standbypool/resource-manager/Microsoft.StandbyPool/StandbyPool

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/standbypool/resource-manager/Microsoft.StandbyPool/StandbyPool/swagger/stable/2026-04-01/standbypool.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StandbyPool/standbyContainerGroupPools/{standbyContainerGroupPoolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/standbypool/resource-manager/Microsoft.StandbyPool/StandbyPool/swagger/stable/2026-04-01/standbypool.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StandbyPool/standbyVirtualMachinePools/{standbyVirtualMachinePoolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-142"></a>
## specification/vmware/resource-manager/Microsoft.AVS/AVS

Reported diagnostics: Swagger **6**, TypeSpec **4**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/vmware/resource-manager/Microsoft.AVS/AVS/swagger/stable/2026-03-01/vmware.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}","patch","parameters"]` | internet property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/vmware/resource-manager/Microsoft.AVS/AVS/swagger/stable/2026-03-01/vmware.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/vmware/resource-manager/Microsoft.AVS/AVS/swagger/stable/2026-03-01/vmware.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/clusters/{clusterName}/placementPolicies/{placementPolicyName}","patch","parameters"]` | affinityStrength property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/vmware/resource-manager/Microsoft.AVS/AVS/swagger/stable/2026-03-01/vmware.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/clusters/{clusterName}/placementPolicies/{placementPolicyName}","patch","parameters"]` | azureHybridBenefitType property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/vmware/resource-manager/Microsoft.AVS/AVS/swagger/stable/2026-03-01/vmware.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/clusters/{clusterName}/placementPolicies/{placementPolicyName}","patch","parameters"]` | hostMembers property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/vmware/resource-manager/Microsoft.AVS/AVS/swagger/stable/2026-03-01/vmware.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/clusters/{clusterName}/placementPolicies/{placementPolicyName}","patch","parameters"]` | vmMembers property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `placementPolicies.tsp:159:3` | The property 'vmMembers' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `placementPolicies.tsp:162:3` | The property 'hostMembers' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `placementPolicies.tsp:165:3` | The property 'affinityStrength' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `placementPolicies.tsp:168:3` | The property 'azureHybridBenefitType' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-143"></a>
## specification/workloads/resource-manager/Microsoft.Workloads/SAPDiscoverySites

Reported diagnostics: Swagger **2**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/workloads/resource-manager/Microsoft.Workloads/SAPDiscoverySites/swagger/preview/2023-10-01-preview/SAPDiscoverySites.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Workloads/sapDiscoverySites/{sapDiscoverySiteName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/workloads/resource-manager/Microsoft.Workloads/SAPDiscoverySites/swagger/preview/2023-10-01-preview/SAPDiscoverySites.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Workloads/sapDiscoverySites/{sapDiscoverySiteName}/sapInstances/{sapInstanceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-144"></a>
## specification/alertsmanagement/resource-manager/Microsoft.AlertsManagement/TenantActivityLogAlerts

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/alertsmanagement/resource-manager/Microsoft.AlertsManagement/TenantActivityLogAlerts/swagger/preview/2023-04-01-preview/TenantActivityLogAlerts.json: ["paths","/providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.AlertsManagement/tenantActivityLogAlerts/{alertRuleName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-145"></a>
## specification/apicenter/resource-manager/Microsoft.ApiCenter/ApiCenter

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/apicenter/resource-manager/Microsoft.ApiCenter/ApiCenter/swagger/preview/2024-06-01-preview/apicenter.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiCenter/services/{serviceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-146"></a>
## specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/WorkbookTemplatesApi

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/WorkbookTemplatesApi/swagger/stable/2020-11-20/workbookTemplates_API.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/workbooktemplates/{resourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-147"></a>
## specification/applink/AppLink.Management

Reported diagnostics: Swagger **3**, TypeSpec **2**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/applink/AppLink.Management/swagger/resource-manager/Microsoft.AppLink/preview/2026-08-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppLink/appLinks/{appLinkName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/applink/AppLink.Management/swagger/resource-manager/Microsoft.AppLink/preview/2026-08-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppLink/appLinks/{appLinkName}","patch","parameters"]` | userAssignedIdentities property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/applink/AppLink.Management/swagger/resource-manager/Microsoft.AppLink/preview/2026-08-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppLink/appLinks/{appLinkName}/appLinkMembers/{appLinkMemberName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `applinkmember.tsp:29:3` | The property 'metadata' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `applinkmember.tsp:118:3` | The property 'privateConnect' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-148"></a>
## specification/awsconnector/AccessAnalyzerAnalyzer.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/AccessAnalyzerAnalyzer.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/accessAnalyzerAnalyzer.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/accessAnalyzerAnalyzers/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-149"></a>
## specification/awsconnector/AcmCertificateSummary.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/AcmCertificateSummary.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/acmCertificateSummary.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/acmCertificateSummaries/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-150"></a>
## specification/awsconnector/ApiGatewayRestApi.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/ApiGatewayRestApi.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/apiGatewayRestApi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/apiGatewayRestApis/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-151"></a>
## specification/awsconnector/ApiGatewayStage.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/ApiGatewayStage.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/apiGatewayStage.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/apiGatewayStages/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-152"></a>
## specification/awsconnector/AppSyncGraphqlApi.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/AppSyncGraphqlApi.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/appSyncGraphqlApi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/appSyncGraphqlApis/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-153"></a>
## specification/awsconnector/AutoScalingAutoScalingGroup.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/AutoScalingAutoScalingGroup.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/autoScalingAutoScalingGroup.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/autoScalingAutoScalingGroups/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-154"></a>
## specification/awsconnector/CloudFormationStack.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/CloudFormationStack.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/cloudFormationStack.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/cloudFormationStacks/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-155"></a>
## specification/awsconnector/CloudFormationStackSet.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/CloudFormationStackSet.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/cloudFormationStackSet.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/cloudFormationStackSets/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-156"></a>
## specification/awsconnector/CloudFrontDistribution.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/CloudFrontDistribution.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/cloudFrontDistribution.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/cloudFrontDistributions/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-157"></a>
## specification/awsconnector/CloudTrailTrail.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/CloudTrailTrail.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/cloudTrailTrail.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/cloudTrailTrails/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-158"></a>
## specification/awsconnector/CloudWatchAlarm.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/CloudWatchAlarm.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/cloudWatchAlarm.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/cloudWatchAlarms/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-159"></a>
## specification/awsconnector/CodeBuildProject.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/CodeBuildProject.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/codeBuildProject.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/codeBuildProjects/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-160"></a>
## specification/awsconnector/CodeBuildSourceCredentialsInfo.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/CodeBuildSourceCredentialsInfo.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/codeBuildSourceCredentialsInfo.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/codeBuildSourceCredentialsInfos/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-161"></a>
## specification/awsconnector/ConfigServiceConfigurationRecorder.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/ConfigServiceConfigurationRecorder.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/configServiceConfigurationRecorder.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/configServiceConfigurationRecorders/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-162"></a>
## specification/awsconnector/ConfigServiceConfigurationRecorderStatus.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/ConfigServiceConfigurationRecorderStatus.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/configServiceConfigurationRecorderStatus.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/configServiceConfigurationRecorderStatuses/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-163"></a>
## specification/awsconnector/ConfigServiceDeliveryChannel.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/ConfigServiceDeliveryChannel.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/configServiceDeliveryChannel.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/configServiceDeliveryChannels/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-164"></a>
## specification/awsconnector/DatabaseMigrationServiceReplicationInstance.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/DatabaseMigrationServiceReplicationInstance.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/databaseMigrationServiceReplicationInstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/databaseMigrationServiceReplicationInstances/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-165"></a>
## specification/awsconnector/DaxCluster.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/DaxCluster.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/daxCluster.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/daxClusters/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-166"></a>
## specification/awsconnector/DynamoDBContinuousBackupsDescription.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/DynamoDBContinuousBackupsDescription.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/dynamoDBContinuousBackupsDescription.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/dynamoDBContinuousBackupsDescriptions/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-167"></a>
## specification/awsconnector/DynamoDBTable.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/DynamoDBTable.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/dynamoDBTable.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/dynamoDBTables/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-168"></a>
## specification/awsconnector/Ec2AccountAttribute.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Ec2AccountAttribute.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ec2AccountAttribute.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ec2AccountAttributes/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-169"></a>
## specification/awsconnector/Ec2Address.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Ec2Address.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ec2Address.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ec2Addresses/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-170"></a>
## specification/awsconnector/Ec2FlowLog.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Ec2FlowLog.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ec2FlowLog.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ec2FlowLogs/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-171"></a>
## specification/awsconnector/Ec2Image.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Ec2Image.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ec2Image.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ec2Images/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-172"></a>
## specification/awsconnector/Ec2InstanceStatus.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Ec2InstanceStatus.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ec2InstanceStatus.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ec2InstanceStatuses/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-173"></a>
## specification/awsconnector/Ec2Ipam.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Ec2Ipam.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ec2Ipam.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ec2Ipams/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-174"></a>
## specification/awsconnector/Ec2KeyPair.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Ec2KeyPair.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ec2KeyPair.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ec2KeyPairs/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-175"></a>
## specification/awsconnector/Ec2NetworkAcl.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Ec2NetworkAcl.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ec2NetworkAcl.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ec2NetworkAcls/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-176"></a>
## specification/awsconnector/Ec2NetworkInterface.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Ec2NetworkInterface.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ec2NetworkInterface.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ec2NetworkInterfaces/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-177"></a>
## specification/awsconnector/Ec2RouteTable.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Ec2RouteTable.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ec2RouteTable.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ec2RouteTables/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-178"></a>
## specification/awsconnector/Ec2SecurityGroup.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Ec2SecurityGroup.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ec2SecurityGroup.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ec2SecurityGroups/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-179"></a>
## specification/awsconnector/Ec2Snapshot.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Ec2Snapshot.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ec2Snapshot.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ec2Snapshots/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-180"></a>
## specification/awsconnector/Ec2Subnet.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Ec2Subnet.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ec2Subnet.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ec2Subnets/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-181"></a>
## specification/awsconnector/Ec2VPCEndpoint.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Ec2VPCEndpoint.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ec2VPCEndpoint.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ec2VPCEndpoints/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-182"></a>
## specification/awsconnector/Ec2VPCPeeringConnection.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Ec2VPCPeeringConnection.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ec2VPCPeeringConnection.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ec2VPCPeeringConnections/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-183"></a>
## specification/awsconnector/Ec2Volume.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Ec2Volume.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ec2Volume.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ec2Volumes/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-184"></a>
## specification/awsconnector/Ec2Vpc.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Ec2Vpc.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ec2Vpc.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ec2Vpcs/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-185"></a>
## specification/awsconnector/EcrImageDetail.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/EcrImageDetail.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ecrImageDetail.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ecrImageDetails/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-186"></a>
## specification/awsconnector/EcrRepository.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/EcrRepository.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ecrRepository.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ecrRepositories/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-187"></a>
## specification/awsconnector/EcsCluster.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/EcsCluster.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ecsCluster.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ecsClusters/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-188"></a>
## specification/awsconnector/EcsService.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/EcsService.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ecsService.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ecsServices/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-189"></a>
## specification/awsconnector/EcsTaskDefinition.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/EcsTaskDefinition.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ecsTaskDefinition.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ecsTaskDefinitions/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-190"></a>
## specification/awsconnector/EfsFileSystem.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/EfsFileSystem.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/efsFileSystem.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/efsFileSystems/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-191"></a>
## specification/awsconnector/EfsMountTarget.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/EfsMountTarget.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/efsMountTarget.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/efsMountTargets/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-192"></a>
## specification/awsconnector/EksNodegroup.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/EksNodegroup.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/eksNodegroup.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/eksNodegroups/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-193"></a>
## specification/awsconnector/ElasticBeanstalkApplication.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/ElasticBeanstalkApplication.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/elasticBeanstalkApplication.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/elasticBeanstalkApplications/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-194"></a>
## specification/awsconnector/ElasticBeanstalkConfigurationTemplate.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/ElasticBeanstalkConfigurationTemplate.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/elasticBeanstalkConfigurationTemplate.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/elasticBeanstalkConfigurationTemplates/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-195"></a>
## specification/awsconnector/ElasticBeanstalkEnvironment.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/ElasticBeanstalkEnvironment.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/elasticBeanstalkEnvironment.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/elasticBeanstalkEnvironments/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-196"></a>
## specification/awsconnector/ElasticLoadBalancingV2Listener.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/ElasticLoadBalancingV2Listener.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/elasticLoadBalancingV2Listener.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/elasticLoadBalancingV2Listeners/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-197"></a>
## specification/awsconnector/ElasticLoadBalancingV2LoadBalancer.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/ElasticLoadBalancingV2LoadBalancer.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/elasticLoadBalancingV2LoadBalancer.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/elasticLoadBalancingV2LoadBalancers/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-198"></a>
## specification/awsconnector/ElasticLoadBalancingV2TargetGroup.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/ElasticLoadBalancingV2TargetGroup.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/elasticLoadBalancingV2TargetGroup.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/elasticLoadBalancingV2TargetGroups/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-199"></a>
## specification/awsconnector/ElasticLoadBalancingv2TargetHealthDescription.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/ElasticLoadBalancingv2TargetHealthDescription.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/elasticLoadBalancingV2TargetHealthDescription.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/elasticLoadBalancingV2TargetHealthDescriptions/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-200"></a>
## specification/awsconnector/EmrCluster.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/EmrCluster.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/emrCluster.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/emrClusters/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-201"></a>
## specification/awsconnector/GuardDutyDetector.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/GuardDutyDetector.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/guardDutyDetector.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/guardDutyDetectors/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-202"></a>
## specification/awsconnector/IamAccessKeyLastUsed.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/IamAccessKeyLastUsed.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/iamAccessKeyLastUsed.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/iamAccessKeyLastUseds/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-203"></a>
## specification/awsconnector/IamAccessKeyMetadata.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/IamAccessKeyMetadata.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/iamAccessKeyMetadata.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/iamAccessKeyMetadata/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-204"></a>
## specification/awsconnector/IamGroup.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/IamGroup.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/iamGroup.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/iamGroups/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-205"></a>
## specification/awsconnector/IamInstanceProfile.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/IamInstanceProfile.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/iamInstanceProfile.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/iamInstanceProfiles/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-206"></a>
## specification/awsconnector/IamMFADevice.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/IamMFADevice.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/iamMFADevice.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/iamMFADevices/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-207"></a>
## specification/awsconnector/IamPasswordPolicy.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/IamPasswordPolicy.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/iamPasswordPolicy.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/iamPasswordPolicies/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-208"></a>
## specification/awsconnector/IamPolicyVersion.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/IamPolicyVersion.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/iamPolicyVersion.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/iamPolicyVersions/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-209"></a>
## specification/awsconnector/IamRole.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/IamRole.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/iamRole.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/iamRoles/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-210"></a>
## specification/awsconnector/IamServerCertificate.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/IamServerCertificate.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/iamServerCertificate.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/iamServerCertificates/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-211"></a>
## specification/awsconnector/IamVirtualMFADevice.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/IamVirtualMFADevice.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/iamVirtualMFADevice.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/iamVirtualMFADevices/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-212"></a>
## specification/awsconnector/KmsAlias.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/KmsAlias.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/kmsAlias.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/kmsAliases/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-213"></a>
## specification/awsconnector/KmsKey.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/KmsKey.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/kmsKey.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/kmsKeys/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-214"></a>
## specification/awsconnector/LambdaFunction.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/LambdaFunction.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/lambdaFunction.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/lambdaFunctions/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-215"></a>
## specification/awsconnector/LambdaFunctionCodeLocation.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/LambdaFunctionCodeLocation.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/lambdaFunctionCodeLocation.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/lambdaFunctionCodeLocations/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-216"></a>
## specification/awsconnector/LightsailBucket.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/LightsailBucket.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/lightsailBucket.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/lightsailBuckets/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-217"></a>
## specification/awsconnector/LightsailInstance.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/LightsailInstance.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/lightsailInstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/lightsailInstances/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-218"></a>
## specification/awsconnector/LogsLogGroup.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/LogsLogGroup.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/logsLogGroup.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/logsLogGroups/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-219"></a>
## specification/awsconnector/LogsLogStream.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/LogsLogStream.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/logsLogStream.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/logsLogStreams/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-220"></a>
## specification/awsconnector/LogsMetricFilter.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/LogsMetricFilter.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/logsMetricFilter.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/logsMetricFilters/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-221"></a>
## specification/awsconnector/LogsSubscriptionFilter.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/LogsSubscriptionFilter.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/logsSubscriptionFilter.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/logsSubscriptionFilters/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-222"></a>
## specification/awsconnector/Macie2JobSummary.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Macie2JobSummary.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/macie2JobSummary.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/macie2JobSummaries/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-223"></a>
## specification/awsconnector/MacieAllowList.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/MacieAllowList.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/macieAllowList.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/macieAllowLists/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-224"></a>
## specification/awsconnector/NetworkFirewallFirewall.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/NetworkFirewallFirewall.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/networkFirewallFirewall.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/networkFirewallFirewalls/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-225"></a>
## specification/awsconnector/NetworkFirewallFirewallPolicy.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/NetworkFirewallFirewallPolicy.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/networkFirewallFirewallPolicy.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/networkFirewallFirewallPolicies/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-226"></a>
## specification/awsconnector/NetworkFirewallRuleGroup.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/NetworkFirewallRuleGroup.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/networkFirewallRuleGroup.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/networkFirewallRuleGroups/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-227"></a>
## specification/awsconnector/OpenSearchDomainStatus.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/OpenSearchDomainStatus.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/openSearchDomainStatus.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/openSearchDomainStatuses/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-228"></a>
## specification/awsconnector/OrganizationsAccount.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/OrganizationsAccount.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/organizationsAccount.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/organizationsAccounts/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-229"></a>
## specification/awsconnector/OrganizationsOrganization.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/OrganizationsOrganization.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/organizationsOrganization.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/organizationsOrganizations/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-230"></a>
## specification/awsconnector/RdsDBCluster.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/RdsDBCluster.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/rdsDBCluster.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/rdsDBClusters/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-231"></a>
## specification/awsconnector/RdsDBInstance.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/RdsDBInstance.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/rdsDBInstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/rdsDBInstances/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-232"></a>
## specification/awsconnector/RdsDBSnapshot.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/RdsDBSnapshot.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/rdsDBSnapshot.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/rdsDBSnapshots/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-233"></a>
## specification/awsconnector/RdsDBSnapshotAttributesResult.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/RdsDBSnapshotAttributesResult.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/rdsDBSnapshotAttributesResult.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/rdsDBSnapshotAttributesResults/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-234"></a>
## specification/awsconnector/RdsEventSubscription.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/RdsEventSubscription.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/rdsEventSubscription.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/rdsEventSubscriptions/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-235"></a>
## specification/awsconnector/RdsExportTask.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/RdsExportTask.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/rdsExportTask.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/rdsExportTasks/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-236"></a>
## specification/awsconnector/RedshiftCluster.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/RedshiftCluster.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/redshiftCluster.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/redshiftClusters/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-237"></a>
## specification/awsconnector/RedshiftClusterParameterGroup.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/RedshiftClusterParameterGroup.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/redshiftClusterParameterGroup.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/redshiftClusterParameterGroups/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-238"></a>
## specification/awsconnector/Route53DomainsDomainSummary.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Route53DomainsDomainSummary.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/route53DomainsDomainSummary.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/route53DomainsDomainSummaries/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-239"></a>
## specification/awsconnector/Route53HostedZone.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Route53HostedZone.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/route53HostedZone.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/route53HostedZones/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-240"></a>
## specification/awsconnector/Route53ResourceRecordSet.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Route53ResourceRecordSet.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/route53ResourceRecordSet.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/route53ResourceRecordSets/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-241"></a>
## specification/awsconnector/S3AccessControlPolicy.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/S3AccessControlPolicy.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/s3AccessControlPolicy.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/s3AccessControlPolicies/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-242"></a>
## specification/awsconnector/S3AccessPoint.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/S3AccessPoint.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/s3AccessPoint.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/s3AccessPoints/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-243"></a>
## specification/awsconnector/S3Bucket.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/S3Bucket.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/s3Bucket.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/s3Buckets/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-244"></a>
## specification/awsconnector/S3BucketPolicy.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/S3BucketPolicy.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/s3BucketPolicy.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/s3BucketPolicies/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-245"></a>
## specification/awsconnector/S3ControlMultiRegionAccessPointPolicyDocument.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/S3ControlMultiRegionAccessPointPolicyDocument.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/s3ControlMultiRegionAccessPointPolicyDocument.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/s3ControlMultiRegionAccessPointPolicyDocuments/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-246"></a>
## specification/awsconnector/SageMakerApp.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/SageMakerApp.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/sageMakerApp.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/sageMakerApps/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-247"></a>
## specification/awsconnector/SageMakerNotebookInstanceSummary.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/SageMakerNotebookInstanceSummary.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/sageMakerNotebookInstanceSummary.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/sageMakerNotebookInstanceSummaries/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-248"></a>
## specification/awsconnector/SecretsManagerResourcePolicy.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/SecretsManagerResourcePolicy.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/secretsManagerResourcePolicy.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/secretsManagerResourcePolicies/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-249"></a>
## specification/awsconnector/SecretsManagerSecret.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/SecretsManagerSecret.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/secretsManagerSecret.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/secretsManagerSecrets/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-250"></a>
## specification/awsconnector/SnsSubscription.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/SnsSubscription.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/snsSubscription.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/snsSubscriptions/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-251"></a>
## specification/awsconnector/SnsTopic.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/SnsTopic.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/snsTopic.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/snsTopics/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-252"></a>
## specification/awsconnector/SqsQueue.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/SqsQueue.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/sqsQueue.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/sqsQueues/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-253"></a>
## specification/awsconnector/SsmInstanceInformation.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/SsmInstanceInformation.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ssmInstanceInformation.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ssmInstanceInformations/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-254"></a>
## specification/awsconnector/SsmParameter.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/SsmParameter.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ssmParameter.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ssmParameters/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-255"></a>
## specification/awsconnector/SsmResourceComplianceSummaryItem.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/SsmResourceComplianceSummaryItem.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/ssmResourceComplianceSummaryItem.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/ssmResourceComplianceSummaryItems/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-256"></a>
## specification/awsconnector/WafWebACLSummary.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/WafWebACLSummary.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/wafWebACLSummary.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/wafWebACLSummaries/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-257"></a>
## specification/awsconnector/Wafv2LoggingConfiguration.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/awsconnector/Wafv2LoggingConfiguration.Management/swagger/resource-manager/Microsoft.AwsConnector/stable/2024-12-01/wafv2LoggingConfiguration.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AwsConnector/wafv2LoggingConfigurations/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-258"></a>
## specification/billingtrust/resource-manager/Microsoft.BillingTrust/BillingTrust

Reported diagnostics: Swagger **0**, TypeSpec **1**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| TypeSpec linter | `main.tsp:324:3` | The property 'kind' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-259"></a>
## specification/cloudhealth/resource-manager/Microsoft.CloudHealth/CloudHealth

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/cloudhealth/resource-manager/Microsoft.CloudHealth/CloudHealth/swagger/stable/2026-11-01/cloudhealth.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CloudHealth/healthmodels/{healthModelName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-260"></a>
## specification/communitytraining/resource-manager/Microsoft.Community/Community

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/communitytraining/resource-manager/Microsoft.Community/Community/swagger/stable/2023-11-01/CommunityTrainings.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Community/communityTrainings/{communityTrainingName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-261"></a>
## specification/compute/resource-manager/Microsoft.Compute/Bulkactions

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/compute/resource-manager/Microsoft.Compute/Bulkactions/swagger/preview/2026-10-06-preview/Bulkactions.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/scheduledActions/{scheduledActionName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-262"></a>
## specification/computeschedule/resource-manager/Microsoft.ComputeSchedule/ComputeSchedule

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/computeschedule/resource-manager/Microsoft.ComputeSchedule/ComputeSchedule/swagger/preview/2026-04-15-preview/computeschedule.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ComputeSchedule/scheduledActions/{scheduledActionName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-263"></a>
## specification/confluent/resource-manager/Microsoft.Confluent/Confluent

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/confluent/resource-manager/Microsoft.Confluent/Confluent/swagger/preview/2026-06-02-preview/confluent.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Confluent/organizations/{organizationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-264"></a>
## specification/containerservice/resource-manager/Microsoft.ContainerService/aimanager

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/containerservice/resource-manager/Microsoft.ContainerService/aimanager/swagger/preview/2026-09-02-preview/aimanagers.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/aiManagers/{aiManagerName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-265"></a>
## specification/containerservice/resource-manager/Microsoft.ContainerService/nodecustomization

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/containerservice/resource-manager/Microsoft.ContainerService/nodecustomization/swagger/preview/2025-09-02-preview/nodecustomization.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/nodeCustomizations/{nodeCustomizationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-266"></a>
## specification/containerservice/resource-manager/Microsoft.ContainerService/preparedimagespecification

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/containerservice/resource-manager/Microsoft.ContainerService/preparedimagespecification/swagger/preview/2026-05-02-preview/preparedimagespecification.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/preparedImageSpecifications/{preparedImageSpecificationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-267"></a>
## specification/containerstorage/resource-manager/Microsoft.ContainerStorage/ContainerStorage

Reported diagnostics: Swagger **2**, TypeSpec **1**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/containerstorage/resource-manager/Microsoft.ContainerStorage/ContainerStorage/swagger/preview/2023-07-01-preview/containerstorage.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerStorage/pools/{poolName}","patch","parameters"]` | elasticSan property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/containerstorage/resource-manager/Microsoft.ContainerStorage/ContainerStorage/swagger/preview/2023-07-01-preview/containerstorage.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerStorage/pools/{poolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `pool.tsp:106:3` | The property 'elasticSan' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-268"></a>
## specification/contosowidgetmanager/Contoso.Management

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/contosowidgetmanager/Contoso.Management/swagger/resource-manager/Microsoft.Contoso/stable/2021-11-01/contoso.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Contoso/employees/{employeeName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-269"></a>
## specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/fleets/{fleetName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-270"></a>
## specification/databasewatcher/resource-manager/Microsoft.DatabaseWatcher/DatabaseWatcher

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/databasewatcher/resource-manager/Microsoft.DatabaseWatcher/DatabaseWatcher/swagger/stable/2025-01-02/Watcher.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DatabaseWatcher/watchers/{watcherName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-271"></a>
## specification/databox/resource-manager/Microsoft.DataBox/DataBox

Reported diagnostics: Swagger **4**, TypeSpec **3**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/databox/resource-manager/Microsoft.DataBox/DataBox/swagger/stable/2025-07-01/databox.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName}","patch","parameters"]` | carrierAccountNumber property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/databox/resource-manager/Microsoft.DataBox/DataBox/swagger/stable/2025-07-01/databox.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName}","patch","parameters"]` | carrierName property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/databox/resource-manager/Microsoft.DataBox/DataBox/swagger/stable/2025-07-01/databox.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/databox/resource-manager/Microsoft.DataBox/DataBox/swagger/stable/2025-07-01/databox.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName}","patch","parameters"]` | trackingId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:2480:3` | The property 'carrierAccountNumber' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:2485:3` | The property 'carrierName' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:2490:3` | The property 'trackingId' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-272"></a>
## specification/databoxedge/resource-manager/Microsoft.DataBoxEdge/DataBoxEdge

Reported diagnostics: Swagger **2**, TypeSpec **1**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/databoxedge/resource-manager/Microsoft.DataBoxEdge/DataBoxEdge/swagger/stable/2023-12-01/databoxedge.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}","patch","parameters"]` | id property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/databoxedge/resource-manager/Microsoft.DataBoxEdge/DataBoxEdge/swagger/stable/2023-12-01/databoxedge.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:1717:3` | The property 'id' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-273"></a>
## specification/deviceprovisioningservices/resource-manager/Microsoft.Devices/DeviceProvisioningServices

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/deviceprovisioningservices/resource-manager/Microsoft.Devices/DeviceProvisioningServices/swagger/stable/2026-11-01/iotdps.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-274"></a>
## specification/deviceupdate/resource-manager/Microsoft.DeviceUpdate/DuDeviceRegistry

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/deviceupdate/resource-manager/Microsoft.DeviceUpdate/DuDeviceRegistry/swagger/DuDeviceRegistry/preview/2026-11-02-preview/dudeviceupdate.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DeviceUpdate/updateInstances/{updateInstanceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-275"></a>
## specification/devopsinfrastructure/resource-manager/Microsoft.DevOpsInfrastructure/DevOpsInfrastructure

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/devopsinfrastructure/resource-manager/Microsoft.DevOpsInfrastructure/DevOpsInfrastructure/swagger/preview/2026-07-03-preview/devopsinfrastructure.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevOpsInfrastructure/pools/{poolName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-276"></a>
## specification/dns/resource-manager/Microsoft.Network/Dns

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/dns/resource-manager/Microsoft.Network/Dns/swagger/preview/2023-07-01-preview/dns.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-277"></a>
## specification/durabletask/resource-manager/Microsoft.DurableTask/DurableTask

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/durabletask/resource-manager/Microsoft.DurableTask/DurableTask/swagger/preview/2026-05-01-preview/durabletask.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DurableTask/schedulers/{schedulerName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-278"></a>
## specification/edge/resource-manager/Microsoft.Edge/configurations

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/edge/resource-manager/Microsoft.Edge/configurations/swagger/stable/2026-06-01/configurations.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Edge/configurations/{configurationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-279"></a>
## specification/edge/resource-manager/Microsoft.Edge/disconnectedOperations

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/edge/resource-manager/Microsoft.Edge/disconnectedOperations/swagger/stable/2026-03-15/disconnectedOperations.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Edge/disconnectedOperations/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-280"></a>
## specification/elastic/resource-manager/Microsoft.Elastic/Elastic

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/elastic/resource-manager/Microsoft.Elastic/Elastic/swagger/preview/2026-03-15-preview/elastic.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Elastic/monitors/{monitorName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-281"></a>
## specification/fabric/resource-manager/Microsoft.Fabric/Fabric

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/fabric/resource-manager/Microsoft.Fabric/Fabric/swagger/preview/2026-09-01-preview/fabric.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric/capacities/{capacityName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-282"></a>
## specification/frontdoor/resource-manager/Microsoft.Network/FrontDoor

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/frontdoor/resource-manager/Microsoft.Network/FrontDoor/swagger/stable/2026-04-01/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName}/Experiments/{experimentName}","patch","parameters"]` | description property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-283"></a>
## specification/gcpconnector/resource-manager/Microsoft.GcpConnector/BigQueryDataset

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/gcpconnector/resource-manager/Microsoft.GcpConnector/BigQueryDataset/swagger/stable/2027-01-01/bigQueryDataset.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.GcpConnector/bigQueryDatasets/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-284"></a>
## specification/gcpconnector/resource-manager/Microsoft.GcpConnector/CloudFunction

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/gcpconnector/resource-manager/Microsoft.GcpConnector/CloudFunction/swagger/stable/2027-01-01/cloudFunction.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.GcpConnector/cloudFunctions/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-285"></a>
## specification/gcpconnector/resource-manager/Microsoft.GcpConnector/SQLAdminInstances

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/gcpconnector/resource-manager/Microsoft.GcpConnector/SQLAdminInstances/swagger/stable/2027-01-01/sqlAdminInstance.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.GcpConnector/sqlAdminInstances/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-286"></a>
## specification/gcpconnector/resource-manager/Microsoft.GcpConnector/StorageBucket

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/gcpconnector/resource-manager/Microsoft.GcpConnector/StorageBucket/swagger/stable/2027-01-01/storageBucket.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.GcpConnector/storageBuckets/{name}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-287"></a>
## specification/hanaonazure/resource-manager/Microsoft.HanaOnAzure/HanaOnAzure

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/hanaonazure/resource-manager/Microsoft.HanaOnAzure/HanaOnAzure/swagger/preview/2020-02-07-preview/hanaonazure.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/sapMonitors/{sapMonitorName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-288"></a>
## specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-289"></a>
## specification/hybridaks/resource-manager/Microsoft.HybridContainerService/HybridContainerService

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/hybridaks/resource-manager/Microsoft.HybridContainerService/HybridContainerService/swagger/preview/2026-04-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridContainerService/virtualNetworks/{virtualNetworkName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-290"></a>
## specification/imagebuilder/resource-manager/Microsoft.VirtualMachineImages/ImageBuilder

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/imagebuilder/resource-manager/Microsoft.VirtualMachineImages/ImageBuilder/swagger/stable/2025-10-01/imagebuilder.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-291"></a>
## specification/iothub/resource-manager/Microsoft.Devices/IoTHub

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/iothub/resource-manager/Microsoft.Devices/IoTHub/swagger/preview/2026-10-01-preview/iothub.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-292"></a>
## specification/iotoperations/resource-manager/Microsoft.IoTOperations/IoTOperations

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/iotoperations/resource-manager/Microsoft.IoTOperations/IoTOperations/swagger/preview/2026-11-01-preview/iotoperations.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTOperations/instances/{instanceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-293"></a>
## specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/privateLinkScopes

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/privateLinkScopes/swagger/preview/2024-11-01-preview/privateLinkScopes.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KubernetesConfiguration/privateLinkScopes/{scopeName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-294"></a>
## specification/liftrastronomer/resource-manager/Astronomer.Astro/AstronomerAstro

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/liftrastronomer/resource-manager/Astronomer.Astro/AstronomerAstro/swagger/preview/2024-08-27-preview/astronomer.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Astronomer.Astro/organizations/{organizationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-295"></a>
## specification/liftrqumulo/resource-manager/Qumulo.Storage/QumuloStorage

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/liftrqumulo/resource-manager/Qumulo.Storage/QumuloStorage/swagger/stable/2026-04-16/Qumulo.Storage.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Qumulo.Storage/fileSystems/{fileSystemName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-296"></a>
## specification/loadtestservice/resource-manager/Microsoft.LoadTestService/loadtesting

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/loadtestservice/resource-manager/Microsoft.LoadTestService/loadtesting/swagger/preview/2024-12-01-preview/loadtestservice.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LoadTestService/loadTests/{loadTestName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-297"></a>
## specification/logic/resource-manager/Microsoft.Logic/Logic

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/logic/resource-manager/Microsoft.Logic/Logic/swagger/preview/2026-04-01-preview/automationproject.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/automationProjects/{automationProjectName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-298"></a>
## specification/management/resource-manager/Microsoft.Management/ManagementGroups

Reported diagnostics: Swagger **2**, TypeSpec **1**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/management/resource-manager/Microsoft.Management/ManagementGroups/swagger/stable/2023-04-01/management.json: ["paths","/providers/Microsoft.Management/managementGroups/{groupId}","patch","parameters"]` | displayName property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/management/resource-manager/Microsoft.Management/ManagementGroups/swagger/stable/2023-04-01/management.json: ["paths","/providers/Microsoft.Management/managementGroups/{groupId}","patch","parameters"]` | parentGroupId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:602:3` | The property 'parentGroupId' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-299"></a>
## specification/migrate/resource-manager/Microsoft.Migrate/AssessmentProjects

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/migrate/resource-manager/Microsoft.Migrate/AssessmentProjects/swagger/preview/2024-03-03-preview/assessmentProjects.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-300"></a>
## specification/mongocluster/resource-manager/Microsoft.DocumentDB/MongoCluster

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/mongocluster/resource-manager/Microsoft.DocumentDB/MongoCluster/swagger/preview/2026-06-15-preview/mongoCluster.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/mongoClusters/{mongoClusterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-301"></a>
## specification/monitor/resource-manager/Microsoft.Insights/Insights/ActivityLogAlertsApi

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/monitor/resource-manager/Microsoft.Insights/Insights/ActivityLogAlertsApi/swagger/preview/2023-01-01-preview/activityLogAlerts.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/activityLogAlerts/{activityLogAlertName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-302"></a>
## specification/monitor/resource-manager/Microsoft.Insights/Insights/AutoScaleApi

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/monitor/resource-manager/Microsoft.Insights/Insights/AutoScaleApi/swagger/stable/2022-10-01/autoScale.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/autoscalesettings/{autoscaleSettingName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-303"></a>
## specification/monitor/resource-manager/Microsoft.Insights/Insights/LogProfilesApi

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/monitor/resource-manager/Microsoft.Insights/Insights/LogProfilesApi/swagger/stable/2016-03-01/logProfiles.json: ["paths","/subscriptions/{subscriptionId}/providers/Microsoft.Insights/logprofiles/{logProfileName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-304"></a>
## specification/monitor/resource-manager/Microsoft.Insights/Insights/PrivateLinkScopesApi

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/monitor/resource-manager/Microsoft.Insights/Insights/PrivateLinkScopesApi/swagger/preview/2023-06-01-preview/privateLinkScopes.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-305"></a>
## specification/monitor/resource-manager/Microsoft.Insights/Insights/ScheduledQueryRuleApi

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/monitor/resource-manager/Microsoft.Insights/Insights/ScheduledQueryRuleApi/swagger/preview/2025-01-01-preview/scheduledQueryRule.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/scheduledQueryRules/{ruleName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-306"></a>
## specification/monitoringservice/resource-manager/Microsoft.Monitor/Accounts

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/monitoringservice/resource-manager/Microsoft.Monitor/Accounts/swagger/preview/2026-09-03-preview/azuremonitorworkspace.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Monitor/accounts/{azureMonitorWorkspaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-307"></a>
## specification/monitoringservice/resource-manager/Microsoft.Monitor/PipelineGroups

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/monitoringservice/resource-manager/Microsoft.Monitor/PipelineGroups/swagger/stable/2026-04-01/pipelineGroups.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Monitor/pipelineGroups/{pipelineGroupName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-308"></a>
## specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity/swagger/preview/2025-05-31-preview/ManagedIdentity.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{resourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-309"></a>
## specification/newrelic/resource-manager/NewRelic.Observability/NewRelicObservability

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/newrelic/resource-manager/NewRelic.Observability/NewRelicObservability/swagger/stable/2026-06-01/NewRelic.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/NewRelic.Observability/monitors/{monitorName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-310"></a>
## specification/nginx/resource-manager/Nginx.NginxPlus/NginxPlus

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/nginx/resource-manager/Nginx.NginxPlus/NginxPlus/swagger/stable/2025-11-01/swagger.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Nginx.NginxPlus/nginxDeployments/{deploymentName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-311"></a>
## specification/portal/resource-manager/Microsoft.Portal/Portal

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/portal/resource-manager/Microsoft.Portal/Portal/swagger/stable/2026-04-01/portal.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-312"></a>
## specification/programenrollment/resource-manager/Microsoft.ProgramEnrollment/ProgramEnrollment

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/programenrollment/resource-manager/Microsoft.ProgramEnrollment/ProgramEnrollment/swagger/preview/2026-03-01-preview/openapi.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ProgramEnrollment/eduEnrollments/{enrollmentName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-313"></a>
## specification/purview/resource-manager/Microsoft.Purview/Purview

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/purview/resource-manager/Microsoft.Purview/Purview/swagger/preview/2024-04-01-preview/purview.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-314"></a>
## specification/quantum/resource-manager/Microsoft.Quantum/Quantum

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/quantum/resource-manager/Microsoft.Quantum/Quantum/swagger/preview/2026-06-15-preview/quantum.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Quantum/workspaces/{workspaceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-315"></a>
## specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/OpenShiftClusters

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/OpenShiftClusters/swagger/stable/2025-07-25/redhatopenshift.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RedHatOpenShift/openShiftClusters/{resourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-316"></a>
## specification/redisenterprise/resource-manager/Microsoft.Cache/RedisEnterprise

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/redisenterprise/resource-manager/Microsoft.Cache/RedisEnterprise/swagger/stable/2026-09-01/redisenterprise.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/redisEnterprise/{clusterName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-317"></a>
## specification/resourceconnector/resource-manager/Microsoft.ResourceConnector/ResourceConnector

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/resourceconnector/resource-manager/Microsoft.ResourceConnector/ResourceConnector/swagger/preview/2025-03-01-preview/appliances.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ResourceConnector/appliances/{resourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-318"></a>
## specification/resourcegraph/resource-manager/Microsoft.ResourceGraph/ResourceGraph/GraphQueryApi

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/resourcegraph/resource-manager/Microsoft.ResourceGraph/ResourceGraph/GraphQueryApi/swagger/stable/2024-04-01/graphquery.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ResourceGraph/queries/{resourceName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-319"></a>
## specification/resources/resource-manager/Microsoft.Resources/resources

Reported diagnostics: Swagger **3**, TypeSpec **2**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/resources/resource-manager/Microsoft.Resources/resources/swagger/stable/2025-04-01/resources.json: ["paths","/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}","patch","parameters"]` | name property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/resources/resource-manager/Microsoft.Resources/resources/swagger/stable/2025-04-01/resources.json: ["paths","/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/resources/resource-manager/Microsoft.Resources/resources/swagger/stable/2025-04-01/resources.json: ["paths","/{scope}/providers/Microsoft.Resources/tags/default","patch","parameters"]` | operation property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:868:3` | The property 'name' in the PATCH body does not correspond to a property in the PUT body. | 1 |
| TypeSpec linter | `models.tsp:1032:3` | The property 'operation' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-320"></a>
## specification/security/resource-manager/Microsoft.Security/Security/AutomationsAPI

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/security/resource-manager/Microsoft.Security/Security/AutomationsAPI/swagger/preview/2023-12-01-preview/security-Automations.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/automations/{automationName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-321"></a>
## specification/security/resource-manager/Microsoft.Security/Security/IoTSecurityAPI

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/security/resource-manager/Microsoft.Security/Security/IoTSecurityAPI/swagger/stable/2019-08-01/security-IoTSecurity.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-322"></a>
## specification/security/resource-manager/Microsoft.Security/Security/PrivateLinksAPI

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/security/resource-manager/Microsoft.Security/Security/PrivateLinksAPI/swagger/stable/2026-01-01/privateLinks.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/privateLinks/{privateLinkName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-323"></a>
## specification/security/resource-manager/Microsoft.Security/Security/ServiceEntitlementsAPI

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/security/resource-manager/Microsoft.Security/Security/ServiceEntitlementsAPI/swagger/preview/2026-09-01-preview/serviceEntitlements.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/serviceEntitlements/{serviceEntitlementName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-324"></a>
## specification/sphere/resource-manager/Microsoft.AzureSphere/AzureSphere

Reported diagnostics: Swagger **2**, TypeSpec **1**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/sphere/resource-manager/Microsoft.AzureSphere/AzureSphere/swagger/stable/2024-04-01/azuresphere.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureSphere/catalogs/{catalogName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| Swagger linter | `projects/specification/sphere/resource-manager/Microsoft.AzureSphere/AzureSphere/swagger/stable/2024-04-01/azuresphere.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureSphere/catalogs/{catalogName}/products/{productName}/deviceGroups/{deviceGroupName}/devices/{deviceName}","patch","parameters"]` | deviceGroupId property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |
| TypeSpec linter | `models.tsp:795:3` | The property 'deviceGroupId' in the PATCH body does not correspond to a property in the PUT body. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-325"></a>
## specification/storageactions/resource-manager/Microsoft.StorageActions/StorageActions

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/storageactions/resource-manager/Microsoft.StorageActions/StorageActions/swagger/stable/2026-03-01/storageactions.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageActions/storageTasks/{storageTaskName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-326"></a>
## specification/verifiedid/resource-manager/Microsoft.VerifiedId/VerifiedId

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/verifiedid/resource-manager/Microsoft.VerifiedId/VerifiedId/swagger/preview/2024-01-26-preview/verifiedid.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VerifiedId/authorities/{authorityName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-327"></a>
## specification/widget/resource-manager/Microsoft.Widget/Widget

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/widget/resource-manager/Microsoft.Widget/Widget/swagger/preview/2024-10-01-preview/widget.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Widget/employees/{employeeName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

<a id="difference-328"></a>
## specification/workloads/resource-manager/Microsoft.Workloads/monitors

Reported diagnostics: Swagger **1**, TypeSpec **0**.
The complete groups below account for both counts independently.

| Engine | Exact diagnostic target | Message | Raw count |
| --- | --- | --- | ---: |
| Swagger linter | `projects/specification/workloads/resource-manager/Microsoft.Workloads/monitors/swagger/preview/2024-02-01-preview/monitors.json: ["paths","/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Workloads/monitors/{monitorName}","patch","parameters"]` | tags property in patch body is not present in the corresponding put body. A patch request body must only contain properties present in the corresponding put request body, and must contain at least one of the properties. | 1 |

**Attribution boundary:** these raw source/latest-emitted observations
do not establish a common-operation count or exact cross-engine
correspondence. Any residual not established by the linked investigation
remains unresolved; no production-rule change is inferred from totals.

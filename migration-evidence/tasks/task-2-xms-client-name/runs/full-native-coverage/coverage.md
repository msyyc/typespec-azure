# Native TypeSpec coverage analysis

Validators: `XmsClientName`
Native rules: `@azure-tools/typespec-client-generator-core/no-redundant-client-name`
Scope: `source`; partial: false.

**This is observed coverage, not an automatic equivalence decision.**
Primary counting unit: sum of raw member validator occurrences versus aligned native diagnostics, counted once.
Member-native attribution is unavailable. Test every member's semantics, including members with no observations.
Cross-validator overlap is not normalized. Equal source locations do not establish one actionable grouped violation.
JSON paths and source locations are different identity domains. One-sided projects and outliers require investigation.
Source diagnostics include all declared versions; Swagger uses the latest emitted API version.

| Measure                                            |           Value |
| -------------------------------------------------- | --------------: |
| Selected / assessable projects                     |       490 / 490 |
| Unassessed projects                                |               0 |
| Validator / native / overlap projects              |      0 / 32 / 0 |
| Observed validator-project coverage                |             N/A |
| Validator raw / file-independent paths             |           0 / 0 |
| Native raw / aligned / source targets              | 141 / 141 / 141 |
| Native findings under project defaults             |    not assessed |
| Validator excess / native excess                   |         0 / 141 |
| Raw validator excess / raw native excess (primary) |         0 / 141 |

## Member observations (not member-native coverage)

- XmsClientName: 0 raw observations; completeness not determined.

## One-sided projects

- Native only: `specification/advisor/resource-manager/Microsoft.Advisor/Advisor`
- Native only: `specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement`
- Native only: `specification/app/resource-manager/Microsoft.App/ContainerApps`
- Native only: `specification/batch/resource-manager/Microsoft.Batch/Batch`
- Native only: `specification/billing/resource-manager/Microsoft.Billing/Billing`
- Native only: `specification/cdn/resource-manager/Microsoft.Cdn/Cdn`
- Native only: `specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger`
- Native only: `specification/connectedcache/resource-manager/Microsoft.ConnectedCache/ConnectedCache`
- Native only: `specification/consumption/resource-manager/Microsoft.Consumption/Consumption`
- Native only: `specification/containerservice/resource-manager/Microsoft.ContainerService/aks`
- Native only: `specification/databox/resource-manager/Microsoft.DataBox/DataBox`
- Native only: `specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs`
- Native only: `specification/dns/resource-manager/Microsoft.Network/Dns`
- Native only: `specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration`
- Native only: `specification/frontdoor/resource-manager/Microsoft.Network/FrontDoor`
- Native only: `specification/help/resource-manager/Microsoft.Help/Help`
- Native only: `specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity`
- Native only: `specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault`
- Native only: `specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric`
- Native only: `specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity`
- Native only: `specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud`
- Native only: `specification/oracle/resource-manager/Oracle.Database/OracleDatabase`
- Native only: `specification/postgresql/resource-manager/Microsoft.DBforPostgreSQL/PostgreSql`
- Native only: `specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup`
- Native only: `specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/OpenShiftClusters`
- Native only: `specification/resources/resource-manager/Microsoft.Resources/deploymentStacks`
- Native only: `specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights`
- Native only: `specification/sql/resource-manager/Microsoft.Sql/SQL`
- Native only: `specification/storage/resource-manager/Microsoft.Storage/Storage`
- Native only: `specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync`
- Native only: `specification/vmware/resource-manager/Microsoft.AVS/AVS`
- Native only: `specification/web/resource-manager/Microsoft.Web/AppService`

## Unassessed projects

## Diagnostic outliers

| Project                                                                                                 | Validator raw | Native aligned | Raw difference | Validator paths | Native targets | Location difference |
| ------------------------------------------------------------------------------------------------------- | ------------: | -------------: | -------------: | --------------: | -------------: | ------------------: |
| specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric |             0 |             25 |            -25 |               0 |             25 |                 -25 |
| specification/web/resource-manager/Microsoft.Web/AppService                                             |             0 |             12 |            -12 |               0 |             12 |                 -12 |
| specification/hybridconnectivity/resource-manager/Microsoft.HybridConnectivity/HybridConnectivity       |             0 |             10 |            -10 |               0 |             10 |                 -10 |
| specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/ConfidentialLedger       |             0 |              8 |             -8 |               0 |              8 |                  -8 |
| specification/help/resource-manager/Microsoft.Help/Help                                                 |             0 |              8 |             -8 |               0 |              8 |                  -8 |
| specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights             |             0 |              8 |             -8 |               0 |              8 |                  -8 |
| specification/storage/resource-manager/Microsoft.Storage/Storage                                        |             0 |              7 |             -7 |               0 |              7 |                  -7 |
| specification/msi/resource-manager/Microsoft.ManagedIdentity/ManagedIdentity                            |             0 |              6 |             -6 |               0 |              6 |                  -6 |
| specification/resources/resource-manager/Microsoft.Resources/deploymentStacks                           |             0 |              6 |             -6 |               0 |              6 |                  -6 |
| specification/advisor/resource-manager/Microsoft.Advisor/Advisor                                        |             0 |              4 |             -4 |               0 |              4 |                  -4 |
| specification/containerservice/resource-manager/Microsoft.ContainerService/aks                          |             0 |              4 |             -4 |               0 |              4 |                  -4 |
| specification/oracle/resource-manager/Oracle.Database/OracleDatabase                                    |             0 |              4 |             -4 |               0 |              4 |                  -4 |
| specification/sql/resource-manager/Microsoft.Sql/SQL                                                    |             0 |              4 |             -4 |               0 |              4 |                  -4 |
| specification/cdn/resource-manager/Microsoft.Cdn/Cdn                                                    |             0 |              3 |             -3 |               0 |              3 |                  -3 |
| specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup |             0 |              3 |             -3 |               0 |              3 |                  -3 |
| specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement                      |             0 |              2 |             -2 |               0 |              2 |                  -2 |
| specification/batch/resource-manager/Microsoft.Batch/Batch                                              |             0 |              2 |             -2 |               0 |              2 |                  -2 |
| specification/billing/resource-manager/Microsoft.Billing/Billing                                        |             0 |              2 |             -2 |               0 |              2 |                  -2 |
| specification/consumption/resource-manager/Microsoft.Consumption/Consumption                            |             0 |              2 |             -2 |               0 |              2 |                  -2 |
| specification/databox/resource-manager/Microsoft.DataBox/DataBox                                        |             0 |              2 |             -2 |               0 |              2 |                  -2 |
| specification/devtestlabs/resource-manager/Microsoft.DevTestLab/DevTestLabs                             |             0 |              2 |             -2 |               0 |              2 |                  -2 |
| specification/domainregistration/resource-manager/Microsoft.DomainRegistration/DomainRegistration       |             0 |              2 |             -2 |               0 |              2 |                  -2 |
| specification/frontdoor/resource-manager/Microsoft.Network/FrontDoor                                    |             0 |              2 |             -2 |               0 |              2 |                  -2 |
| specification/networkcloud/resource-manager/Microsoft.NetworkCloud/NetworkCloud                         |             0 |              2 |             -2 |               0 |              2 |                  -2 |
| specification/redhatopenshift/resource-manager/Microsoft.RedHatOpenShift/OpenShiftClusters              |             0 |              2 |             -2 |               0 |              2 |                  -2 |
| specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync                            |             0 |              2 |             -2 |               0 |              2 |                  -2 |
| specification/vmware/resource-manager/Microsoft.AVS/AVS                                                 |             0 |              2 |             -2 |               0 |              2 |                  -2 |
| specification/app/resource-manager/Microsoft.App/ContainerApps                                          |             0 |              1 |             -1 |               0 |              1 |                  -1 |
| specification/connectedcache/resource-manager/Microsoft.ConnectedCache/ConnectedCache                   |             0 |              1 |             -1 |               0 |              1 |                  -1 |
| specification/dns/resource-manager/Microsoft.Network/Dns                                                |             0 |              1 |             -1 |               0 |              1 |                  -1 |
| specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault                                     |             0 |              1 |             -1 |               0 |              1 |                  -1 |
| specification/postgresql/resource-manager/Microsoft.DBforPostgreSQL/PostgreSql                          |             0 |              1 |             -1 |               0 |              1 |                  -1 |

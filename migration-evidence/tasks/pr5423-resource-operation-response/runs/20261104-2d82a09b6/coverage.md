Swagger staging supplement: `e0a2c22b857b13fa8ccf318bff1c8a6beaf367e1a1210cbc71cf7161fd86d482` (explicit ARM/common Spectral staging; production observations remain separate).

# Native TypeSpec coverage analysis

Validators: `PutRequestResponseSchemeArm`, `ConsistentResponseSchemaForPut`, `XmsResourceInPutResponse`, `PutGetPatchResponseSchema`
Native rules: `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response`
Scope: `source`; partial: false.

**This is observed coverage, not an automatic equivalence decision.**
Primary counting unit: sum of raw member validator occurrences versus aligned native diagnostics, counted once.
Member-native attribution is unavailable. Test every member's semantics, including members with no observations.
Cross-validator overlap is not normalized. Equal source locations do not establish one actionable grouped violation.
JSON paths and source locations are different identity domains. One-sided projects and outliers require investigation.
Source diagnostics include all declared versions; Swagger uses the latest emitted API version.

| Measure                                            |             Value |
| -------------------------------------------------- | ----------------: |
| Selected / assessable projects                     |         487 / 487 |
| Unassessed projects                                |                 0 |
| Validator / native / overlap projects              |      57 / 34 / 32 |
| Observed validator-project coverage                | 56.14035087719298 |
| Validator raw / file-independent paths             |         433 / 275 |
| Native raw / aligned / source targets              |   104 / 104 / 104 |
| Native findings under project defaults             |               104 |
| Validator excess / native excess                   |           175 / 4 |
| Raw validator excess / raw native excess (primary) |           333 / 4 |

## Member observations (not member-native coverage)

- PutRequestResponseSchemeArm: 212 raw observations; completeness not determined.
- ConsistentResponseSchemaForPut: 16 raw observations; completeness not determined.
- XmsResourceInPutResponse: 155 raw observations; completeness not determined.
- PutGetPatchResponseSchema: 50 raw observations; completeness not determined.

## One-sided projects

- Validator only: `specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/AnalyticsItems`
- Validator only: `specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs`
- Validator only: `specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/Favorites`
- Validator only: `specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview`
- Validator only: `specification/authorization/resource-manager/Microsoft.Authorization/Authorization/RoleAssignment`
- Validator only: `specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices`
- Validator only: `specification/compute/resource-manager/Microsoft.Compute/Compute/Compute`
- Validator only: `specification/confluent/resource-manager/Microsoft.Confluent/Confluent`
- Validator only: `specification/datadog/resource-manager/Microsoft.Datadog/Datadog`
- Validator only: `specification/durabletask/resource-manager/Microsoft.DurableTask/DurableTask`
- Validator only: `specification/fileshares/resource-manager/Microsoft.FileShares/FileShares`
- Validator only: `specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments`
- Validator only: `specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis`
- Validator only: `specification/maps/resource-manager/Microsoft.Maps/Maps`
- Validator only: `specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace`
- Validator only: `specification/network/resource-manager/Microsoft.Network/Network/Network`
- Validator only: `specification/operationalinsights/resource-manager/Microsoft.OperationalInsights/OperationalInsights`
- Validator only: `specification/portal/resource-manager/Microsoft.Portal/Portal`
- Validator only: `specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc`
- Validator only: `specification/redis/resource-manager/Microsoft.Cache/Redis`
- Validator only: `specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota`
- Validator only: `specification/resources/resource-manager/Microsoft.Resources/resources`
- Validator only: `specification/security/resource-manager/Microsoft.Security/Security/PrivateLinksAPI`
- Validator only: `specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI`
- Validator only: `specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights`
- Native only: `specification/dns/resource-manager/Microsoft.Network/Dns`
- Native only: `specification/security/resource-manager/Microsoft.Security/Security/ApiCollectionsAPI`

## Unassessed projects

## Diagnostic outliers

| Project                                                                                                  | Validator raw | Native aligned | Raw difference | Validator paths | Native targets | Location difference |
| -------------------------------------------------------------------------------------------------------- | ------------: | -------------: | -------------: | --------------: | -------------: | ------------------: |
| specification/network/resource-manager/Microsoft.Network/Network/Network                                 |           170 |              0 |            170 |              14 |              0 |                  14 |
| specification/web/resource-manager/Microsoft.Web/AppService                                              |            31 |              1 |             30 |              31 |              1 |                  30 |
| specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement                       |            22 |              4 |             18 |              22 |              4 |                  18 |
| specification/sql/resource-manager/Microsoft.Sql/SQL                                                     |            20 |              4 |             16 |              18 |              4 |                  14 |
| specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB                                 |            33 |             21 |             12 |              33 |             21 |                  12 |
| specification/automation/resource-manager/Microsoft.Automation/Automation                                |            26 |             17 |              9 |              26 |             17 |                   9 |
| specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview          |             8 |              0 |              8 |               8 |              0 |                   8 |
| specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight                                   |             9 |              1 |              8 |               9 |              1 |                   8 |
| specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs  |             7 |              0 |              7 |               7 |              0 |                   7 |
| specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid                                   |             6 |              1 |              5 |               6 |              1 |                   5 |
| specification/postgresql/DBforPostgreSQL.Management                                                      |             9 |              4 |              5 |               9 |              4 |                   5 |
| specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments               |             4 |              0 |              4 |               4 |              0 |                   4 |
| specification/resources/resource-manager/Microsoft.Resources/deployments                                 |             5 |              1 |              4 |               5 |              1 |                   4 |
| specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault                                      |             5 |              2 |              3 |               5 |              2 |                   3 |
| specification/redis/resource-manager/Microsoft.Cache/Redis                                               |             3 |              0 |              3 |               3 |              0 |                   3 |
| specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights              |             3 |              0 |              3 |               3 |              0 |                   3 |
| specification/authorization/resource-manager/Microsoft.Authorization/Authorization/RoleAssignment        |             2 |              0 |              2 |               2 |              0 |                   2 |
| specification/compute/resource-manager/Microsoft.Compute/Compute/Compute                                 |             2 |              0 |              2 |               2 |              0 |                   2 |
| specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace                             |             2 |              0 |              2 |               2 |              0 |                   2 |
| specification/portal/resource-manager/Microsoft.Portal/Portal                                            |             2 |              0 |              2 |               2 |              0 |                   2 |
| specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup  |             3 |              1 |              2 |               3 |              1 |                   2 |
| specification/resources/resource-manager/Microsoft.Resources/resources                                   |             2 |              0 |              2 |               2 |              0 |                   2 |
| specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/AnalyticsItems |             1 |              0 |              1 |               1 |              0 |                   1 |
| specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/Favorites      |             1 |              0 |              1 |               1 |              0 |                   1 |
| specification/batch/resource-manager/Microsoft.Batch/Batch                                               |             1 |              2 |             -1 |               1 |              2 |                  -1 |
| specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices           |             1 |              0 |              1 |               1 |              0 |                   1 |
| specification/confluent/resource-manager/Microsoft.Confluent/Confluent                                   |             1 |              0 |              1 |               1 |              0 |                   1 |
| specification/datadog/resource-manager/Microsoft.Datadog/Datadog                                         |             1 |              0 |              1 |               1 |              0 |                   1 |
| specification/dns/resource-manager/Microsoft.Network/Dns                                                 |             0 |              1 |             -1 |               0 |              1 |                  -1 |
| specification/durabletask/resource-manager/Microsoft.DurableTask/DurableTask                             |             1 |              0 |              1 |               1 |              0 |                   1 |
| specification/fileshares/resource-manager/Microsoft.FileShares/FileShares                                |             1 |              0 |              1 |               1 |              0 |                   1 |
| specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis                    |             1 |              0 |              1 |               1 |              0 |                   1 |
| specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb                                   |             2 |              1 |              1 |               2 |              1 |                   1 |
| specification/management/resource-manager/Microsoft.Management/ManagementGroups                          |             2 |              3 |             -1 |               2 |              3 |                  -1 |
| specification/maps/resource-manager/Microsoft.Maps/Maps                                                  |             1 |              0 |              1 |               1 |              0 |                   1 |
| specification/operationalinsights/resource-manager/Microsoft.OperationalInsights/OperationalInsights     |             1 |              0 |              1 |               1 |              0 |                   1 |
| specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc                     |             1 |              0 |              1 |               1 |              0 |                   1 |
| specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices              |             2 |              1 |              1 |               2 |              1 |                   1 |
| specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota                        |             1 |              0 |              1 |               1 |              0 |                   1 |
| specification/security/resource-manager/Microsoft.Security/Security/ApiCollectionsAPI                    |             0 |              1 |             -1 |               0 |              1 |                  -1 |
| specification/security/resource-manager/Microsoft.Security/Security/PrivateLinksAPI                      |             1 |              0 |              1 |               1 |              0 |                   1 |
| specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI       |             1 |              0 |              1 |               1 |              0 |                   1 |

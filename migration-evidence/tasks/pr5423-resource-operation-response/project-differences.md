# Complete directional project inventory

## Assessed project grouping

The common counting unit is an affected project, identified by its exact `sourcePath` in the
frozen 487-project inventory. The Swagger side unions the affected-project sets of all four
selected members; the TypeSpec side uses the shared rule's retained `diagnostics` array.
Multiple findings, emitted documents and members in the same project count once on each side.
No finding is removed from the raw inventories.

| Project group                | Count |
| ---------------------------- | ----- |
| Swagger linter has findings  | 57    |
| TypeSpec linter has findings | 34    |
| Both linters have findings   | 32    |
| Swagger linter only          | 25    |
| TypeSpec linter only         | 2     |
| Neither linter has findings  | 428   |
| Entire assessed population   | 487   |

The sets partition the population: `32 + 25 + 2 + 428 = 487`.
The affected counts reconstruct as `32 + 25 = 57` and `32 + 2 = 34`.
These numbers assess project-level occurrence, not operation correspondence or equivalent defects.
Swagger uses saved latest-version emission; TypeSpec uses source scope with authored suppressions.
Both execution policies are unchanged from the recorded corpus.

### Member project comparisons

| Swagger member                 | Swagger-affected | Shared TypeSpec-affected | Both | Swagger-only | Shared TypeSpec-only |
| ------------------------------ | ---------------- | ------------------------ | ---- | ------------ | -------------------- |
| PutRequestResponseSchemeArm    | 38               | 34                       | 29   | 9            | 5                    |
| ConsistentResponseSchemaForPut | 10               | 34                       | 3    | 7            | 31                   |
| XmsResourceInPutResponse       | 14               | 34                       | 5    | 9            | 29                   |
| PutGetPatchResponseSchema      | 14               | 34                       | 8    | 6            | 26                   |

Each row compares that member's project set with the same shared TypeSpec set.
These are assessed intersections, not per-member TypeSpec finding attribution. Rows overlap and
must not be added together. The exact combined sets remain in `summary.json` as `swaggerProjects`,
`nativeProjects`, `overlapProjects`, `swaggerOnlyProjects` and `nativeOnlyProjects`.
Each member's exact set can be reproduced from its retained `observations.json`.

Run `python reanalyze.py --verify-inventory` to independently rebuild the grouped counts from
`observations.json` and compare them with `summary.json`; `python -m unittest test_reanalyze`
checks duplicate findings and overlapping member populations. No compiler or linter rerun is involved.
[Assessment provenance and independent recount](receipts/project-grouping-20261104.json) bind this
update to the unchanged saved observations and candidate.

## Raw diagnostic differences

All projects with unequal raw counts are retained below. Same-total projects remain in the full
diagnostic inventory, `summary.json` and `observations.json`; equal totals do not establish semantic
identity or functional equivalence. They are not presented as known differences without pairing evidence.

| Project                                                                                                                 | Swagger | TypeSpec | TypeSpec minus Swagger | Disposition                                     |
| ----------------------------------------------------------------------------------------------------------------------- | ------- | -------- | ---------------------- | ----------------------------------------------- |
| [specification/network/resource-manager/Microsoft.Network/Network/Network](#project-0)                                  | 170     | 0        | -170                   | Swagger-linter-only                             |
| [specification/web/resource-manager/Microsoft.Web/AppService](#project-1)                                               | 31      | 1        | -30                    | count-only / semantic correspondence unassessed |
| [specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement](#project-2)                        | 22      | 4        | -18                    | count-only / semantic correspondence unassessed |
| [specification/sql/resource-manager/Microsoft.Sql/SQL](#project-3)                                                      | 20      | 4        | -16                    | count-only / semantic correspondence unassessed |
| [specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB](#project-4)                                  | 33      | 21       | -12                    | count-only / semantic correspondence unassessed |
| [specification/automation/resource-manager/Microsoft.Automation/Automation](#project-5)                                 | 26      | 17       | -9                     | count-only / semantic correspondence unassessed |
| [specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview](#project-6)           | 8       | 0        | -8                     | Swagger-linter-only                             |
| [specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight](#project-7)                                    | 9       | 1        | -8                     | count-only / semantic correspondence unassessed |
| [specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs](#project-8)   | 7       | 0        | -7                     | Swagger-linter-only                             |
| [specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid](#project-9)                                    | 6       | 1        | -5                     | count-only / semantic correspondence unassessed |
| [specification/postgresql/DBforPostgreSQL.Management](#project-10)                                                      | 9       | 4        | -5                     | count-only / semantic correspondence unassessed |
| [specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments](#project-11)               | 4       | 0        | -4                     | Swagger-linter-only                             |
| [specification/resources/resource-manager/Microsoft.Resources/deployments](#project-12)                                 | 5       | 1        | -4                     | count-only / semantic correspondence unassessed |
| [specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault](#project-13)                                      | 5       | 2        | -3                     | count-only / semantic correspondence unassessed |
| [specification/redis/resource-manager/Microsoft.Cache/Redis](#project-14)                                               | 3       | 0        | -3                     | Swagger-linter-only                             |
| [specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights](#project-15)              | 3       | 0        | -3                     | Swagger-linter-only                             |
| [specification/authorization/resource-manager/Microsoft.Authorization/Authorization/RoleAssignment](#project-16)        | 2       | 0        | -2                     | Swagger-linter-only                             |
| [specification/compute/resource-manager/Microsoft.Compute/Compute/Compute](#project-17)                                 | 2       | 0        | -2                     | Swagger-linter-only                             |
| [specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace](#project-18)                             | 2       | 0        | -2                     | Swagger-linter-only                             |
| [specification/portal/resource-manager/Microsoft.Portal/Portal](#project-19)                                            | 2       | 0        | -2                     | Swagger-linter-only                             |
| [specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup](#project-20)  | 3       | 1        | -2                     | count-only / semantic correspondence unassessed |
| [specification/resources/resource-manager/Microsoft.Resources/resources](#project-21)                                   | 2       | 0        | -2                     | Swagger-linter-only                             |
| [specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/AnalyticsItems](#project-22) | 1       | 0        | -1                     | Swagger-linter-only                             |
| [specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/Favorites](#project-23)      | 1       | 0        | -1                     | Swagger-linter-only                             |
| [specification/batch/resource-manager/Microsoft.Batch/Batch](#project-24)                                               | 1       | 2        | 1                      | count-only / semantic correspondence unassessed |
| [specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices](#project-25)           | 1       | 0        | -1                     | Swagger-linter-only                             |
| [specification/confluent/resource-manager/Microsoft.Confluent/Confluent](#project-26)                                   | 1       | 0        | -1                     | Swagger-linter-only                             |
| [specification/datadog/resource-manager/Microsoft.Datadog/Datadog](#project-27)                                         | 1       | 0        | -1                     | Swagger-linter-only                             |
| [specification/dns/resource-manager/Microsoft.Network/Dns](#project-28)                                                 | 0       | 1        | 1                      | TypeSpec-linter-only                            |
| [specification/durabletask/resource-manager/Microsoft.DurableTask/DurableTask](#project-29)                             | 1       | 0        | -1                     | Swagger-linter-only                             |
| [specification/fileshares/resource-manager/Microsoft.FileShares/FileShares](#project-30)                                | 1       | 0        | -1                     | Swagger-linter-only                             |
| [specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis](#project-31)                    | 1       | 0        | -1                     | Swagger-linter-only                             |
| [specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb](#project-32)                                   | 2       | 1        | -1                     | count-only / semantic correspondence unassessed |
| [specification/management/resource-manager/Microsoft.Management/ManagementGroups](#project-33)                          | 2       | 3        | 1                      | count-only / semantic correspondence unassessed |
| [specification/maps/resource-manager/Microsoft.Maps/Maps](#project-34)                                                  | 1       | 0        | -1                     | Swagger-linter-only                             |
| [specification/operationalinsights/resource-manager/Microsoft.OperationalInsights/OperationalInsights](#project-35)     | 1       | 0        | -1                     | Swagger-linter-only                             |
| [specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc](#project-36)                     | 1       | 0        | -1                     | Swagger-linter-only                             |
| [specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices](#project-37)              | 2       | 1        | -1                     | count-only / semantic correspondence unassessed |
| [specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota](#project-38)                        | 1       | 0        | -1                     | Swagger-linter-only                             |
| [specification/security/resource-manager/Microsoft.Security/Security/ApiCollectionsAPI](#project-39)                    | 0       | 1        | 1                      | TypeSpec-linter-only                            |
| [specification/security/resource-manager/Microsoft.Security/Security/PrivateLinksAPI](#project-40)                      | 1       | 0        | -1                     | Swagger-linter-only                             |
| [specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI](#project-41)       | 1       | 0        | -1                     | Swagger-linter-only                             |

<a id="project-0"></a>

## specification/network/resource-manager/Microsoft.Network/Network/Network

- API version: `2026-03-01`.
- Swagger linter: 170; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 47, 'XmsResourceInPutResponse': 108, 'PutGetPatchResponseSchema': 15}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-1"></a>

## specification/web/resource-manager/Microsoft.Web/AppService

- API version: `2026-07-15`.
- Swagger linter: 31; TypeSpec linter: 1 aligned /
  1 raw / 1 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 6, 'XmsResourceInPutResponse': 24, 'PutGetPatchResponseSchema': 1}.
- Disposition: count-only / semantic correspondence unassessed. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-2"></a>

## specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement

- API version: `2025-09-01-preview`.
- Swagger linter: 22; TypeSpec linter: 4 aligned /
  4 raw / 4 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 19, 'PutGetPatchResponseSchema': 3}.
- Disposition: count-only / semantic correspondence unassessed. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-3"></a>

## specification/sql/resource-manager/Microsoft.Sql/SQL

- API version: `2026-08-01-preview`.
- Swagger linter: 20; TypeSpec linter: 4 aligned /
  4 raw / 4 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 8, 'ConsistentResponseSchemaForPut': 6, 'XmsResourceInPutResponse': 3, 'PutGetPatchResponseSchema': 3}.
- Disposition: count-only / semantic correspondence unassessed. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-4"></a>

## specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB

- API version: `2026-04-01-preview`.
- Swagger linter: 33; TypeSpec linter: 21 aligned /
  21 raw / 21 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 33}.
- Disposition: count-only / semantic correspondence unassessed. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-5"></a>

## specification/automation/resource-manager/Microsoft.Automation/Automation

- API version: `2024-10-23`.
- Swagger linter: 26; TypeSpec linter: 17 aligned /
  17 raw / 17 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 22, 'XmsResourceInPutResponse': 2, 'PutGetPatchResponseSchema': 2}.
- Disposition: count-only / semantic correspondence unassessed. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-6"></a>

## specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview

- API version: `2021-12-01-preview`.
- Swagger linter: 8; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 8}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-7"></a>

## specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight

- API version: `2025-01-15-preview`.
- Swagger linter: 9; TypeSpec linter: 1 aligned /
  1 raw / 1 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 5, 'PutGetPatchResponseSchema': 4}.
- Disposition: count-only / semantic correspondence unassessed. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-8"></a>

## specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs

- API version: `2015-05-01`.
- Swagger linter: 7; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 2, 'XmsResourceInPutResponse': 4, 'PutGetPatchResponseSchema': 1}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-9"></a>

## specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid

- API version: `2026-06-15-preview`.
- Swagger linter: 6; TypeSpec linter: 1 aligned /
  1 raw / 1 default-target findings.
- Swagger member counts: {'PutGetPatchResponseSchema': 6}.
- Disposition: count-only / semantic correspondence unassessed. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-10"></a>

## specification/postgresql/DBforPostgreSQL.Management

- API version: `2026-07-01-preview`.
- Swagger linter: 9; TypeSpec linter: 4 aligned /
  4 raw / 4 default-target findings.
- Swagger member counts: {'PutGetPatchResponseSchema': 9}.
- Disposition: count-only / semantic correspondence unassessed. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-11"></a>

## specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments

- API version: `2024-04-05`.
- Swagger linter: 4; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'XmsResourceInPutResponse': 4}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-12"></a>

## specification/resources/resource-manager/Microsoft.Resources/deployments

- API version: `2026-06-01`.
- Swagger linter: 5; TypeSpec linter: 1 aligned /
  1 raw / 1 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 5}.
- Disposition: count-only / semantic correspondence unassessed. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-13"></a>

## specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault

- API version: `2026-06-01-preview`.
- Swagger linter: 5; TypeSpec linter: 2 aligned /
  2 raw / 2 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 4, 'XmsResourceInPutResponse': 1}.
- Disposition: count-only / semantic correspondence unassessed. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-14"></a>

## specification/redis/resource-manager/Microsoft.Cache/Redis

- API version: `2025-08-01-preview`.
- Swagger linter: 3; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 2, 'ConsistentResponseSchemaForPut': 1}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-15"></a>

## specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights

- API version: `2025-10-01-preview`.
- Swagger linter: 3; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 3}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-16"></a>

## specification/authorization/resource-manager/Microsoft.Authorization/Authorization/RoleAssignment

- API version: `2022-04-01`.
- Swagger linter: 2; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 2}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-17"></a>

## specification/compute/resource-manager/Microsoft.Compute/Compute/Compute

- API version: `2026-04-01`.
- Swagger linter: 2; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'XmsResourceInPutResponse': 2}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-18"></a>

## specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace

- API version: `2025-01-01`.
- Swagger linter: 2; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 1, 'PutGetPatchResponseSchema': 1}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-19"></a>

## specification/portal/resource-manager/Microsoft.Portal/Portal

- API version: `2026-04-01`.
- Swagger linter: 2; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'ConsistentResponseSchemaForPut': 2}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-20"></a>

## specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup

- API version: `2026-10-01`.
- Swagger linter: 3; TypeSpec linter: 1 aligned /
  1 raw / 1 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 1, 'PutGetPatchResponseSchema': 2}.
- Disposition: count-only / semantic correspondence unassessed. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-21"></a>

## specification/resources/resource-manager/Microsoft.Resources/resources

- API version: `2025-04-01`.
- Swagger linter: 2; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'XmsResourceInPutResponse': 2}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-22"></a>

## specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/AnalyticsItems

- API version: `2015-05-01`.
- Swagger linter: 1; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'XmsResourceInPutResponse': 1}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-23"></a>

## specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/Favorites

- API version: `2015-05-01`.
- Swagger linter: 1; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'XmsResourceInPutResponse': 1}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-24"></a>

## specification/batch/resource-manager/Microsoft.Batch/Batch

- API version: `2025-06-01`.
- Swagger linter: 1; TypeSpec linter: 2 aligned /
  2 raw / 2 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 1}.
- Disposition: count-only / semantic correspondence unassessed. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-25"></a>

## specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices

- API version: `2026-09-15-preview`.
- Swagger linter: 1; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'PutGetPatchResponseSchema': 1}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-26"></a>

## specification/confluent/resource-manager/Microsoft.Confluent/Confluent

- API version: `2026-06-02-preview`.
- Swagger linter: 1; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'XmsResourceInPutResponse': 1}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-27"></a>

## specification/datadog/resource-manager/Microsoft.Datadog/Datadog

- API version: `2025-12-26-preview`.
- Swagger linter: 1; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'XmsResourceInPutResponse': 1}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-28"></a>

## specification/dns/resource-manager/Microsoft.Network/Dns

- API version: `2023-07-01-preview`.
- Swagger linter: 0; TypeSpec linter: 1 aligned /
  1 raw / 1 default-target findings.
- Swagger member counts: {}.
- Disposition: TypeSpec-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-29"></a>

## specification/durabletask/resource-manager/Microsoft.DurableTask/DurableTask

- API version: `2026-05-01-preview`.
- Swagger linter: 1; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'ConsistentResponseSchemaForPut': 1}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-30"></a>

## specification/fileshares/resource-manager/Microsoft.FileShares/FileShares

- API version: `2026-06-01`.
- Swagger linter: 1; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'PutGetPatchResponseSchema': 1}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-31"></a>

## specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis

- API version: `2025-04-01-preview`.
- Swagger linter: 1; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 1}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-32"></a>

## specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb

- API version: `2026-05-01-preview`.
- Swagger linter: 2; TypeSpec linter: 1 aligned /
  1 raw / 1 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 1, 'ConsistentResponseSchemaForPut': 1}.
- Disposition: count-only / semantic correspondence unassessed. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-33"></a>

## specification/management/resource-manager/Microsoft.Management/ManagementGroups

- API version: `2023-04-01`.
- Swagger linter: 2; TypeSpec linter: 3 aligned /
  3 raw / 3 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 2}.
- Disposition: count-only / semantic correspondence unassessed. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-34"></a>

## specification/maps/resource-manager/Microsoft.Maps/Maps

- API version: `2025-10-01-preview`.
- Swagger linter: 1; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'ConsistentResponseSchemaForPut': 1}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-35"></a>

## specification/operationalinsights/resource-manager/Microsoft.OperationalInsights/OperationalInsights

- API version: `2026-03-01`.
- Swagger linter: 1; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'PutGetPatchResponseSchema': 1}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-36"></a>

## specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc

- API version: `2023-03-02-preview`.
- Swagger linter: 1; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'ConsistentResponseSchemaForPut': 1}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-37"></a>

## specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices

- API version: `2026-08-31-preview`.
- Swagger linter: 2; TypeSpec linter: 1 aligned /
  1 raw / 1 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 1, 'XmsResourceInPutResponse': 1}.
- Disposition: count-only / semantic correspondence unassessed. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-38"></a>

## specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota

- API version: `2020-10-25`.
- Swagger linter: 1; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'ConsistentResponseSchemaForPut': 1}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-39"></a>

## specification/security/resource-manager/Microsoft.Security/Security/ApiCollectionsAPI

- API version: `2023-11-15`.
- Swagger linter: 0; TypeSpec linter: 1 aligned /
  1 raw / 1 default-target findings.
- Swagger member counts: {}.
- Disposition: TypeSpec-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-40"></a>

## specification/security/resource-manager/Microsoft.Security/Security/PrivateLinksAPI

- API version: `2026-01-01`.
- Swagger linter: 1; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'ConsistentResponseSchemaForPut': 1}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

<a id="project-41"></a>

## specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI

- API version: `2026-04-01-preview`.
- Swagger linter: 1; TypeSpec linter: 0 aligned /
  0 raw / 0 default-target findings.
- Swagger member counts: {'PutRequestResponseSchemeArm': 1}.
- Disposition: Swagger-linter-only. Exact findings are in the [inventory](diagnostic-inventory.md).
  No operation-level correspondence or accepted retirement is inferred from project-level totals.
  Known code-backed causes are linked in [supporting analysis](evidence-details.md);
  remaining individual pairings are unresolved.

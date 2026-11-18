# Native TypeSpec coverage analysis

Validators: `AvoidAnonymousTypes`
Native rules: `@azure-tools/typespec-azure-core/no-unnamed-types`
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
| Validator / native / overlap projects              |         9 / 5 / 4 |
| Observed validator-project coverage                | 44.44444444444444 |
| Validator raw / file-independent paths             |           32 / 14 |
| Native raw / aligned / source targets              |         6 / 6 / 6 |
| Native findings under project defaults             |      not assessed |
| Validator excess / native excess                   |             9 / 1 |
| Raw validator excess / raw native excess (primary) |            27 / 1 |

## Member observations (not member-native coverage)

- AvoidAnonymousTypes: 32 raw observations; completeness not determined.

## One-sided projects

- Validator only: `specification/datafactory/resource-manager/Microsoft.DataFactory/DataFactory`
- Validator only: `specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration`
- Validator only: `specification/impact/resource-manager/Microsoft.Impact/Impact`
- Validator only: `specification/resources/resource-manager/Microsoft.Resources/deployments`
- Validator only: `specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights`
- Native only: `specification/extendedlocation/resource-manager/Microsoft.ExtendedLocation/CustomLocations`

## Unassessed projects

## Diagnostic outliers

| Project                                                                                     | Validator raw | Native aligned | Raw difference | Validator paths | Native targets | Location difference |
| ------------------------------------------------------------------------------------------- | ------------: | -------------: | -------------: | --------------: | -------------: | ------------------: |
| specification/network/resource-manager/Microsoft.Network/Network/Network                    |            21 |              2 |             19 |               3 |              2 |                   1 |
| specification/datafactory/resource-manager/Microsoft.DataFactory/DataFactory                |             2 |              0 |              2 |               2 |              0 |                   2 |
| specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights |             2 |              0 |              2 |               2 |              0 |                   2 |
| specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration          |             1 |              0 |              1 |               1 |              0 |                   1 |
| specification/extendedlocation/resource-manager/Microsoft.ExtendedLocation/CustomLocations  |             0 |              1 |             -1 |               0 |              1 |                  -1 |
| specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight                      |             2 |              1 |              1 |               2 |              1 |                   1 |
| specification/impact/resource-manager/Microsoft.Impact/Impact                               |             1 |              0 |              1 |               1 |              0 |                   1 |
| specification/resources/resource-manager/Microsoft.Resources/deployments                    |             1 |              0 |              1 |               1 |              0 |                   1 |

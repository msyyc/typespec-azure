# Operation/check correspondence

This appendix separates the four intentionally retired Swagger violations from the eight retained native-protocol findings. Full source locations, metadata and saved Swagger attribution are in [findings.json](findings.json); `reportedNow` distinguishes current findings from investigated former targets.

## Retired Legacy-only matches

| Project        | Operation                                                                         | Swagger warnings | ARM warnings |
| -------------- | --------------------------------------------------------------------------------- | ---------------: | -----------: |
| CostManagement | `Microsoft.CostManagement.GenerateDetailedCostReportOperationResults.get`         |                1 |            0 |
| CostManagement | `Microsoft.CostManagement.GenerateCostDetailsReport.getOperationResults`          |                1 |            0 |
| AppService     | `Microsoft.Web.CsmDeploymentStatuses.getProductionSiteDeploymentStatus`           |                1 |            0 |
| AppService     | `Microsoft.Web.CsmDeploymentStatusOperationGroup.getSlotSiteDeploymentStatusSlot` |                1 |            0 |

Each operation still has accepted common Legacy scope `"*"` and no Azure Core LRO metadata in the current runtime. An authored raw LRO flag is absent; the corresponding saved emitted Swagger flag is **true**. Legacy emission, not a source-authored extension, explains the Swagger warning. The inspection retains exact validator input, attributed source document, JSON path, HTTP verb and diagnostic identity rather than matching by name or count.

These are real detection losses relative to the Swagger linter, accepted as a narrower compatibility policy. No other retained ARM finding substitutes for them. The removed findings' selected-version graph field is `null`: they are inspected historical targets, not current diagnostics classified as version-excluded.

## Retained native-protocol GET findings

| Project                | Operation                                                                                | Selected-version HTTP graph |
| ---------------------- | ---------------------------------------------------------------------------------------- | --------------------------- |
| BotService             | `Microsoft.BotService.OperationResultsOperationGroup.get`                                | Yes                         |
| Maps                   | `Microsoft.Maps.OperationResultOperationGroup.get`                                       | Yes                         |
| RecoveryServicesBackup | `Microsoft.RecoveryServices.RecoveryPointOperationResultsFromCrossTenantVault.get`       | No                          |
| RecoveryServicesBackup | `Microsoft.RecoveryServices.ProtectedItemOperationResultsFromCrossTenantVault.get`       | No                          |
| RecoveryServicesBackup | `Microsoft.RecoveryServices.ValidateOperationResultFromCrossTenantVault.get`             | No                          |
| RecoveryServicesBackup | `Microsoft.RecoveryServices.CrossTenantVaultCredentialOperationResults.get`              | No                          |
| RecoveryServicesBackup | `Microsoft.RecoveryServices.RecoveryPointsExtendedInfo.getRPExtendedInfoOperationResult` | Yes                         |
| AppService             | `Microsoft.Web.StaticSitesAsyncOperations.getOperationResult`                            | Yes                         |

All eight are HTTP GETs with native Core LRO metadata and no accepted Legacy scope. Their operation identities, authored diagnostic locations, metadata and saved Swagger correspondence are unchanged from the prior joint-rule run. None corresponds to an original Swagger violation.

Four warnings concern source versions outside the Swagger baseline's selected version. The other four are native source/protocol warnings, not matches for the four retired Legacy warnings. The selected-version graph inspection checks membership; it does not rerun arbitrary predicates on a projected program.

## Directional differences and policy

At the project-total level, Swagger excess is 3 and TypeSpec excess is 7: AppService's 2-versus-1 total cancels one unrelated finding numerically. At the operation/check level, all four Swagger observations and all eight TypeSpec observations are unmatched. This is why neither 4-versus-8 raw totals nor 4-versus-4 selected-version totals establish equivalent enforcement.

The new SDK regression expresses the shared changed behavior minimally: an accepted Legacy-only GET compiles under SDK `all`, remains an SDK LRO, and has no Core metadata. Its pre-change failure is specifically the removed SDK warning. Existing native ARM cases and the injected controls cover the contrasting native GET behavior, non-GET/synchronous cases, service boundaries, suppression and activation. Raw extension-only declarations remain unsupported rather than being reclassified by a new LRO detector.

All 487 projects succeeded. There are no unassessed projects or unexplained count changes; the deliberate retirement and broader native-source findings account for the differences. This disposition supports the accepted narrower guidance, not full Swagger-rule equivalence.

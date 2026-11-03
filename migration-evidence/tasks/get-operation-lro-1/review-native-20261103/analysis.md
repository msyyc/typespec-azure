# Native-only rule difference investigation

The fresh `8a1c96bef` run compiled all 487 frozen ARM projects. All twelve findings
were inspected through the injected current compiler, HTTP, Core and SDK helpers.
Exact diagnostic identities, operation metadata and saved Swagger attribution
match the earlier investigation. The source examples below use the same frozen
specs commit, `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`.

[Current structured findings](findings.json) retain each actual operation, HTTP
path/method, authored location, selected-version membership, native metadata,
accepted Legacy scopes and matching saved Swagger occurrences. No fuzzy or
name-based correspondence is used.

## BotService

Swagger reports 0; ARM reports 1. The
[source GET](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/botservice/resource-manager/Microsoft.BotService/BotService/routes.tsp#L82-L107),
`OperationResultsOperationGroup.get`, returns an
`ArmAcceptedLroResponse` with an `ArmLroLocationHeader` and `RetryAfterHeader`.
The existing Core helper recognizes native LRO metadata.

Saved operation `OperationResults_Get` has a 202 response with Location and
Retry-After headers, but neither LRO extension. The operation remains in the
selected-version HTTP graph. This is an intentional native-policy difference,
not a failed project or evidence that the result GET initiates work.

## Maps

Swagger reports 0; ARM reports 1. The
[source GET](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/maps/resource-manager/Microsoft.Maps/Maps/routes.tsp#L14-L36),
`OperationResultOperationGroup.get`, returns
`OkResponse | (ArmAcceptedResponse & ArmLroLocationHeader) | ErrorResponse`.
The accepted-response/location combination supplies native LRO metadata.

Saved operation `OperationResult_Get` has neither LRO extension. The source and
selected-version HTTP graphs contain the same GET. The additional warning follows
the approved native policy.

## RecoveryServicesBackup

Swagger reports 0; ARM reports 5 at selected API version `2026-10-01`.

| Source operation                                              | Source definition                                                                                                                                                                                                                                                 | Selected HTTP graph |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| `RecoveryPointOperationResultsFromCrossTenantVault.get`       | [Definition](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/CrossTenantVaultMappingResource.tsp#L476-L500)   | Absent              |
| `ProtectedItemOperationResultsFromCrossTenantVault.get`       | [Definition](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/CrossTenantVaultMappingResource.tsp#L586-L610)   | Absent              |
| `ValidateOperationResultFromCrossTenantVault.get`             | [Definition](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/CrossTenantVaultMappingResource.tsp#L817-L844)   | Absent              |
| `CrossTenantVaultCredentialOperationResults.get`              | [Definition](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/CrossTenantVaultMappingResource.tsp#L1025-L1052) | Absent              |
| `RecoveryPointsExtendedInfo.getRPExtendedInfoOperationResult` | [Definition](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/routes.tsp#L813-L860)                            | Present             |

All five GETs have native LRO metadata. The four cross-tenant declarations have
`@added(Versions.v2026_08_31_preview)` and
`@removed(Versions.v2026_10_01)`. Fresh `http-reachable` workers confirm their
absence from the selected graph. The source-wide run intentionally retains them;
there is no corresponding selected-version Swagger operation to compare.

The fifth operation appears in saved `bms.json` as
`RecoveryPoints_GetRPExtendedInfoOperationResult`, without either LRO extension.
Its accepted-response/location metadata explains the remaining warning.

## AppService

Swagger reports 2; TypeSpec reports 3. Two accepted common Legacy declarations
match the true flags for `WebApps_GetProductionSiteDeploymentStatus` and
`WebApps_GetSlotSiteDeploymentStatusSlot`. They produce two SDK warnings.

The additional
[source GET](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/StaticSitesAsyncOperations.tsp#L40-L66),
`StaticSitesAsyncOperations.getOperationResult`, returns an `ArmResponse`,
`ArmAcceptedLroResponse` or `DefaultErrorResponse`. It remains in the selected
graph and has native LRO metadata. Saved operation
`StaticSitesAsyncOperations_GetOperationResult` has neither LRO extension.
ARM therefore adds one warning under the approved broader policy.

## Matching findings and semantic limits

CostManagement contributes two Swagger and two SDK findings. Together with
AppService's two SDK findings, all four saved Swagger occurrences correspond
exactly to four current HTTP operations. All eight ARM findings have native
metadata and no raw LRO flag/options. There are twelve distinct HTTP operations
and no ARM/SDK overlap on this corpus.

The 34 fresh injected controls use the current native-only policy. A synchronous
GET with only a raw flag or options produces no native warning. An accepted
Legacy marker plus a raw true flag produces only the SDK warning. The historical
two-warning extension/Legacy overlap expectation is superseded.

Both raw excess sums remain explicit: Swagger 0, TypeSpec 8. Four projects differ;
483 have equal raw counts, including 482 with no findings. Relative differences
against zero Swagger findings are undefined, not an acceptance waiver.

Eight source findings remain at selected-version HTTP locations. This is
location alignment, not arbitrary predicate reevaluation after projection.
Neither equal historical totals nor this ARM corpus establish general emitted
document equivalence or coverage of SDK policies outside the ARM audience.

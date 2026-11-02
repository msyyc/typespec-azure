# Split-rule difference investigation

## Difference summary

| Project                                           | Swagger / TypeSpec | Cause                                                                         | Disposition                                        |
| ------------------------------------------------- | -----------------: | ----------------------------------------------------------------------------- | -------------------------------------------------- |
| [BotService](#botservice)                         |              0 / 1 | Recognized result GET; emitted operation has no LRO extensions                | Intentional broader policy                         |
| [Maps](#maps)                                     |              0 / 1 | Recognized result GET; emitted operation has no LRO extensions                | Intentional broader policy                         |
| [RecoveryServicesBackup](#recoveryservicesbackup) |              0 / 5 | One emitted result GET; four operations absent from the selected version      | Intentional broader policy plus version population |
| [AppService](#appservice)                         |              2 / 3 | Two matched SDK declarations and one recognized result GET without extensions | Intentional broader policy                         |

No TypeSpec rule update is required. The user explicitly approved warning for every checked GET recognized by the existing helper, including polling/result endpoints. These differences are not evidence that the extra GETs initiate new work.

The [structured investigation](findings.json) accounts for all 12 findings. Each diagnostic was bound to exactly one actual HTTP operation using its exact authored source location, then compared by actual path/method with saved Swagger observations. This is not name-based or fuzzy matching. Every ARM-only finding has native LRO metadata, no accepted Legacy marker and no raw LRO flag/options. Every TCGC finding has an accepted common Legacy marker and maps to one saved true-flag Swagger occurrence.

## BotService

**Classification:** TypeSpec-linter-only; intentional. API version `2023-09-15-preview`.

The [source operation](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/botservice/resource-manager/Microsoft.BotService/BotService/routes.tsp#L82-L107) is
`Microsoft.BotService.OperationResultsOperationGroup.get`, GET
`/subscriptions/{subscriptionId}/providers/Microsoft.BotService/operationresults/{operationResultId}`.
Its actual response includes:

```typespec
    | ArmAcceptedLroResponse<LroHeaders = ArmLroLocationHeader<FinalResult = OperationResultsDescription> &
        Azure.Core.Foundations.RetryAfterHeader>
```

The saved `botservice.json` operation `OperationResults_Get` has neither LRO extension. Its actual response excerpt is:

```json
{
  "202": {
    "description": "Resource operation accepted.",
    "headers": {
      "Location": {
        "type": "string",
        "description": "The Location header contains the URL where the status of the long running operation can be checked."
      },
      "Retry-After": {
        "type": "integer",
        "format": "int32",
        "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
      }
    }
  }
}
```

| Engine          | Observed result                                            |
| --------------- | ---------------------------------------------------------- |
| Swagger linter  | 0: neither checked LRO extension exists                    |
| TypeSpec linter | 1 ARM warning: existing helper returns native LRO metadata |

The source and selected-version HTTP graphs both contain this operation. This is a semantic-policy difference, not a missing or failed project.

## Maps

**Classification:** TypeSpec-linter-only; intentional. API version `2025-10-01-preview`.

The [source](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/maps/resource-manager/Microsoft.Maps/Maps/routes.tsp#L14-L36) operation
`Microsoft.Maps.OperationResultOperationGroup.get` returns:

```typespec
  ): OkResponse | (ArmAcceptedResponse & ArmLroLocationHeader) | ErrorResponse;
```

Its GET path is `/subscriptions/{subscriptionId}/providers/Microsoft.Maps/locations/{location}/operationResults/{operationId}`.
Saved operation `OperationResult_Get` has neither LRO extension. Swagger reports 0; ARM reports 1. The existing helper recognizes this accepted-response/location combination. Like BotService, it remains in the selected HTTP graph. The same verified cause applies; no TypeSpec rule change is required.

## RecoveryServicesBackup

**Classification:** TypeSpec-linter-only; intentional policy plus version population. Selected API version `2026-10-01`.

| Exact source operation                                        | Source                                                                                                                                                                                                                                                           | Selected HTTP graph | Swagger / TypeSpec |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | -----------------: |
| `RecoveryPointOperationResultsFromCrossTenantVault.get`       | [line 490](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/CrossTenantVaultMappingResource.tsp#L476-L500)    | Absent              |              0 / 1 |
| `ProtectedItemOperationResultsFromCrossTenantVault.get`       | [line 602](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/CrossTenantVaultMappingResource.tsp#L586-L610)    | Absent              |              0 / 1 |
| `ValidateOperationResultFromCrossTenantVault.get`             | [line 833](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/CrossTenantVaultMappingResource.tsp#L817-L844)    | Absent              |              0 / 1 |
| `CrossTenantVaultCredentialOperationResults.get`              | [line 1042](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/CrossTenantVaultMappingResource.tsp#L1025-L1052) | Absent              |              0 / 1 |
| `RecoveryPointsExtendedInfo.getRPExtendedInfoOperationResult` | [line 821](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/routes.tsp#L813-L860)                             | Present             |              0 / 1 |

All five are GETs with native LRO metadata. The four cross-tenant declarations have the actual version boundary:

```typespec
@added(Versions.v2026_08_31_preview)
@removed(Versions.v2026_10_01)
```

For example:

```typespec
  get is RecoveryPointOperationResultsFromCrossTenantVaultOps.Read<
    RecoveryPointResource,
    Response =
      | ArmResponse<BulkRestoreRecoveryPointsResponse>
      | ArmAcceptedResponse<
          "Accepted",
          ArmLroLocationHeader & Azure.Core.Foundations.RetryAfterHeader
        >
  >;
```

The fresh supported `http-reachable` worker confirms all four are absent from the selected graph. No corresponding selected-version Swagger operation exists, so there is no meaningful Swagger schema excerpt for those four. They remain valid findings under the chosen source-wide policy; they are not subtracted from the 12 reported findings.

The fifth operation is present in saved `bms.json` as `RecoveryPoints_GetRPExtendedInfoOperationResult`, without either LRO extension. Its result response follows the same recognized accepted-response/location pattern as BotService. Thus the project difference is exactly four source/version additions plus one broader-policy addition, not an unexplained five-warning gap.

## AppService

**Classification:** count-only; intentional broader policy. API version `2026-07-15`.

The two `CsmDeploymentStatus.tsp` findings correspond exactly to the saved true flags for `WebApps_GetProductionSiteDeploymentStatus` and `WebApps_GetSlotSiteDeploymentStatusSlot`. Both are accepted common Legacy declarations and now belong to TCGC, not ARM.

The additional [source operation](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/StaticSitesAsyncOperations.tsp#L40-L66), `StaticSitesAsyncOperations.getOperationResult`, returns:

```typespec
    | ArmResponse<Azure.ResourceManager.CommonTypes.Resource>
    | ArmAcceptedLroResponse
    | DefaultErrorResponse;
```

Its GET path is `/subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/staticSitesOperationResults/{operationId}`.
Saved operation `StaticSitesAsyncOperations_GetOperationResult` has neither LRO extension. The selected graph contains it; the existing helper recognizes native LRO metadata. Swagger reports 0 and ARM reports 1 for this group, in addition to the two matched SDK groups. Project totals are therefore 2 / 3.

## Matching controls and counting limits

CostManagement has two Swagger findings and two TCGC findings, with no count difference. Together with the two AppService SDK findings, all four saved occurrences map exactly to four current HTTP operations. Their full paths, source positions, actual saved operation IDs and accepted marker states are in `findings.json`.

There are 12 distinct `(project, method, path)` operations and 12 source targets. No two rules overlap on this corpus. Separate injected overlap controls do produce two rule-specific diagnostics for one operation with both an accepted Legacy declaration and an explicit true extension. Counts are not silently deduplicated.

Raw signed difference is Swagger minus TypeSpec. Four projects differ: `-1`, `-1`, `-5`, `-1`; both directional excess sums are 0 / 8. Relative differences against zero Swagger findings are undefined, not a percentage-based acceptance waiver. The other 483 projects have equal raw counts, including 482 with no findings.

The alignment result contains eight source findings at selected-version HTTP locations. This is the existing location-alignment profile, not reevaluation of arbitrary predicates after projection. The original source result remains the primary result. General emitted-document equivalence and audiences outside this frozen production ARM corpus are not claimed.

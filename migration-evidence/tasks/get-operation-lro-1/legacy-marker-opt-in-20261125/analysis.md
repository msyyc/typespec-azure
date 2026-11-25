# Accepted Legacy GET-marker assessment with client-SDK opt-in

## Differences summary

There are no differing current projects or diagnostic groups: Swagger linter 4, TypeSpec linter 4; signed, absolute and relative count differences are zero. Both directional project excesses and the unexplained residual are zero. No normalization or deduplication is applied. Matching controls and correspondence are separate below, not artificial difference rows.

The change from automatic client-SDK activation to opt-in is a user-authorized policy change, not a disappearance of target-only coverage. The four original Swagger findings are still reported when the rule is explicitly enabled. Full-population default activation is unassessed.

## Current correspondence

| Project / selected version    | Source operation                                                                  | Swagger diagnostics | TypeSpec diagnostics |
| ----------------------------- | --------------------------------------------------------------------------------- | ------------------: | -------------------: |
| CostManagement / `2026-06-01` | `Microsoft.CostManagement.GenerateDetailedCostReportOperationResults.get`         |                   1 |                    1 |
| CostManagement / `2026-06-01` | `Microsoft.CostManagement.GenerateCostDetailsReport.getOperationResults`          |                   1 |                    1 |
| AppService / `2026-07-15`     | `Microsoft.Web.CsmDeploymentStatuses.getProductionSiteDeploymentStatus`           |                   1 |                    1 |
| AppService / `2026-07-15`     | `Microsoft.Web.CsmDeploymentStatusOperationGroup.getSlotSiteDeploymentStatusSlot` |                   1 |                    1 |

[findings.json](findings.json) carries exact source locations, saved Swagger file/JSON paths, HTTP paths/verbs, scopes and selected-version membership. All four have accepted common scope, no Core protocol metadata or authored raw flag/options, and saved emitted `x-ms-long-running-operation: true`. Each matches one distinct occurrence and source target, not merely an operation name or count.

### Retained restored-gap example: accepted Legacy GET

- **Classification:** former Swagger-linter-only.
- **Status:** fixed for the accepted-marker scope when enabled.
- **Project/API version:** CostManagement / `2026-06-01`.
- **Source:** `GenerateDetailedCostReportOperationResult.tsp:34`, [frozen declaration](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cost-management/resource-manager/Microsoft.CostManagement/CostManagement/GenerateDetailedCostReportOperationResult.tsp#L26-L42).

**TypeSpec source**

```typespec
interface GenerateDetailedCostReportOperationResults {
  @Azure.ClientGenerator.Core.Legacy.markAsLro
  get is Extension.Read<
    Extension.ScopeParameter,
    GenerateDetailedCostReportOperationResult,
    Response = ArmResponse<GenerateDetailedCostReportOperationResult> | ArmAcceptedResponse,
    Error = ErrorResponse
  >;
}
```

**Saved OpenAPI fields** from the GET object at `/{scope}/providers/Microsoft.CostManagement/operationResults/{operationId}`:

```json
{
  "operationId": "GenerateDetailedCostReportOperationResults_Get",
  "x-ms-long-running-operation": true
}
```

| Engine          | Observed result                                                                  |
| --------------- | -------------------------------------------------------------------------------- |
| Swagger linter  | One `GetOperationMustNotBeLongRunning` occurrence at the LRO flag.               |
| TypeSpec linter | One SDK `no-get-lro` warning at the authored operation with explicit enablement. |

**Explanation:** The accepted Legacy marker explains the historical emitted flag. The former ARM metadata-only predicate missed this violation; the current accepted-marker check detects it without generating SDK clients.

**Coverage status:** All four real matches share this cause, with their distinct identities retained. AppService's concrete template-derived declarations are independently represented.

**analysis:** Retain the accepted-marker predicate and canonical common/scoped/template controls. [The later user request](https://github.com/Azure/typespec-azure/pull/5889#discussion_r4692400008) disables only the client-SDK preset default. The observed corpus deliberately enables the check; it is not evidence of automatic default warning delivery.

## Native-only boundary

The eight [historical native-protocol targets](../arm-only-20261106/analysis.md#retained-native-protocol-get-findings) have zero current warnings and no accepted Legacy marker. Their current membership is `null`, not `false`: without a current warning there is no current selected-version alignment claim. The historical selected-version/source-version distinction remains in that ledger.

| Former operation                                                                         | Current Swagger diagnostics | Current TypeSpec diagnostics |
| ---------------------------------------------------------------------------------------- | --------------------------: | ---------------------------: |
| `Microsoft.BotService.OperationResultsOperationGroup.get`                                |                           0 |                            0 |
| `Microsoft.Maps.OperationResultOperationGroup.get`                                       |                           0 |                            0 |
| `Microsoft.RecoveryServices.RecoveryPointOperationResultsFromCrossTenantVault.get`       |                           0 |                            0 |
| `Microsoft.RecoveryServices.ProtectedItemOperationResultsFromCrossTenantVault.get`       |                           0 |                            0 |
| `Microsoft.RecoveryServices.ValidateOperationResultFromCrossTenantVault.get`             |                           0 |                            0 |
| `Microsoft.RecoveryServices.CrossTenantVaultCredentialOperationResults.get`              |                           0 |                            0 |
| `Microsoft.RecoveryServices.RecoveryPointsExtendedInfo.getRPExtendedInfoOperationResult` |                           0 |                            0 |
| `Microsoft.Web.StaticSitesAsyncOperations.getOperationResult`                            |                           0 |                            0 |

Four historical selected-version GETs have no saved LRO flag/options; four other source-version targets have no selected-version Swagger operation. They are not missing occurrences of the original Swagger property check.

**Coverage status:** Outside this user-selected rule. No native-only GET-LRO detector is implemented.

**analysis:** Preserve the narrower accepted-marker contract and do not credit these eight warnings as migrated Swagger coverage. The user explicitly excluded a follow-up issue; none is created. The previous [accepted-marker cycle](../legacy-marker-20261125/analysis.md#native-only-boundary) retains the same boundary as historical evidence.

## Raw-extension boundary

The selected public control authors:

```typespec
@TypeSpec.OpenAPI.extension("x-ms-long-running-operation", true)
@get
@route("/read")
op read(): {
  value: string;
};
```

It runs inside `@service namespace Contoso`. The separate options-only control uses `@TypeSpec.OpenAPI.extension("x-ms-long-running-operation-options", #{})`, with no Legacy marker.

| Engine          | Evidence                                                                                                                                                                                                                                                                                                           |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Swagger linter  | The pinned [property-check implementation](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/packages/rulesets/src/spectral/az-arm.ts) checks LRO properties on GET. This is code evidence; these controls were not newly emitted and run through the Swagger linter. |
| TypeSpec linter | Zero target warnings for both raw-only controls in configured and target-only executions.                                                                                                                                                                                                                          |

**Coverage status:** Missing from this predicate. None of the four observed Swagger findings is raw-only. That absence does not prove structural prevention or exhaustive substitute coverage.

**analysis:** Keep the original property-check limitation visible. No owning-rule coverage is counted without attributed captured diagnostics, and no future in-scope unmatched finding may be excluded merely to align totals. The user chose marker-only enforcement; this does not retire the broader Swagger property requirement or establish complete equivalence.

## Counting and suppression

The full comparison explicitly enables only the target rule. Configured target warnings: 4; included warnings: 4; excluded current warning identities: empty; additional corresponding suppressed diagnostics captured: empty. The worker honors suppressions but does not capture suppressed callbacks, so exhaustive suppression-inclusive coverage for other owning checks remains unassessed.

All four matching operations actually report an unsuppressed warning. Their existing `no-legacy-usage`, `lro-location-header`, `no-response-body` or `mark-as-lro-ineffective` pragmas are source evidence, not captured unsuppressed runs of those other checks. They do not suppress the new warning.

Canonical/injected suppression controls prove that a justified suppression of this rule preserves SDK LRO generation; suppressing a different Legacy diagnostic does not erase it. These fixture diagnostics are not extra suppressed corpus findings.

Raw Swagger occurrence identity retains rule/project/file/JSON path; file-independent summaries retain rule/project/JSON path. TypeSpec identity retains rule/project/source/line/column. Four observations are distinct under each applicable summary, without collapsing distinct checks. The exact correspondence in [findings.json](findings.json), complete project totals and [assessment/exclusion ledger](assessment.json) remain authoritative; saved replay independently regroups every project.

## Controls and activation

- SDK canonical rule: 17 cases, retaining accepted/common/scoped/repeated markers, empty scope, exact targets, concrete templates, service/helper boundaries, native-only and rejected markers, non-GET controls, suppression and SDK generation.
- SDK suite: 2,074 passed, two intentional skips; 115 test files passed with a 30-second test budget. Central ruleset suite: 22 passed.
- Injected controls: 37 applicable portable passes, six unrelated resource-group fixtures excluded before execution; 25 selected public fixtures in two modes, all 50 passed.
- Client-SDK registers `no-get-lro: false` per [comment 11](https://github.com/Azure/typespec-azure/pull/5889#discussion_r4692400008). Actual configured controls report no default target warning; explicit target enablement and SDK `all` retain warnings. ARM/data-plane/C# presets remain inactive.
- [Comment 12](https://github.com/Azure/typespec-azure/pull/5889#discussion_r4692414105) is addressed by making the existing ruleset registration changeset internal. The SDK feature changeset remains.
- Invalid-target controls retain the existing warning and ignored state; ineffective native-marker controls retain the existing error. Passing controls assert those outcomes rather than universally error-free compilation.

See [validation](validation.json), [controls](controls-summary.json), [runtime verification](runtime-verification.json), and [assets/recovery](recovery.md). Historical external coverage-category reports are not the immutable population/method used here.

## Assessment and remaining uncertainty

The fresh assessed source `c67b521` and Core `123e997` report all four observed accepted-Legacy Swagger findings. No current one-sided project, unpaired warning or uncovered production regression emerged. The later `4c1a337` head merges only unrelated documentation-agent/spelling changes; every assessed package payload still matches that source, without relabeling the run.

This supports the selected accepted-marker check and explicit opt-in policy, not complete Swagger property-level equivalence. Raw-only behavior and suppression-inclusive substitute coverage remain limited/unassessed as stated. Broader migration acceptance belongs to reviewers.

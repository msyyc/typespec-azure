# Accepted Legacy GET-marker assessment

## Differences summary

There are no current differing projects or unmatched observations: Swagger 4, TypeSpec 4; both directional project excesses, absolute difference and signed residual are zero. This is an observed marker-coverage result, not complete Swagger-rule equivalence. No normalization is applied.

The two former real gaps are restored: CostManagement 2/0 becomes 2/2, and AppService's two Legacy targets 2/0 become 2/2. Historical native-only findings are intentionally removed under the user's narrower marker-only scope. The raw-extension property boundary remains a semantic limitation, not a newly observed one-sided corpus finding.

## Current correspondence

| Project / selected version    | Source operation                                                                  | Swagger diagnostics | TypeSpec diagnostics |
| ----------------------------- | --------------------------------------------------------------------------------- | ------------------: | -------------------: |
| CostManagement / `2026-06-01` | `Microsoft.CostManagement.GenerateDetailedCostReportOperationResults.get`         |                   1 |                    1 |
| CostManagement / `2026-06-01` | `Microsoft.CostManagement.GenerateCostDetailsReport.getOperationResults`          |                   1 |                    1 |
| AppService / `2026-07-15`     | `Microsoft.Web.CsmDeploymentStatuses.getProductionSiteDeploymentStatus`           |                   1 |                    1 |
| AppService / `2026-07-15`     | `Microsoft.Web.CsmDeploymentStatusOperationGroup.getSlotSiteDeploymentStatusSlot` |                   1 |                    1 |

Use [findings.json](findings.json) for the authoritative version/path/location fields. Each record carries the source declaration, HTTP method/path, current warning, accepted common scope, Core protocol metadata, selected-version membership and complete saved Swagger input/document/JSON-path occurrence.

All four have common Legacy scope, no Core protocol metadata, no authored raw LRO flag/options, and a saved emitted `x-ms-long-running-operation: true`. All four warnings remain in the selected-version HTTP graph. Each maps to one distinct Swagger occurrence and one distinct source location; no operation-name-only or fuzzy matching is used.

### Restored gap example: accepted Legacy GET

- **Classification:** former Swagger-linter-only.
- **Status:** fixed for the accepted-marker scope.
- **Project/API version:** CostManagement / `2026-06-01`.
- **Source:** `GenerateDetailedCostReportOperationResult.tsp:34`, [frozen declaration](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cost-management/resource-manager/Microsoft.CostManagement/CostManagement/GenerateDetailedCostReportOperationResult.tsp#L26-L42).

Relevant authored declaration:

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

Selected fields from the actual saved GET object at `/{scope}/providers/Microsoft.CostManagement/operationResults/{operationId}`:

```json
{
  "operationId": "GenerateDetailedCostReportOperationResults_Get",
  "x-ms-long-running-operation": true
}
```

| Engine          | Observed result                                                             |
| --------------- | --------------------------------------------------------------------------- |
| Swagger linter  | One `GetOperationMustNotBeLongRunning` occurrence at the LRO flag property. |
| TypeSpec linter | One SDK `no-get-lro` warning on the authored `get` operation.               |

**Explanation:** The accepted Legacy marker explains the historical emitted flag; there is no source-authored extension or native protocol metadata to classify instead. The former ARM-only predicate missed this actual Swagger violation.

**Coverage status:** All four real occurrences share this accepted-common-marker cause. AppService uses the same marker on concrete template-derived GET declarations; those identities are separately retained, not deduplicated.

**Gap analysis and decision:** Adopt TCGC ownership and the explicitly authorized accepted-marker predicate, without generating SDK clients or inventing an LRO status pattern. Canonical common/scoped/template regressions and contrasting unmarked/non-GET cases cover the changed behavior.

## Native-only boundary

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

All eight have native protocol metadata and no accepted Legacy marker in the current inspection. Four were in the historical selected-version HTTP graph and four belonged to other source versions. Their current membership field is **null**, not false: they are historical targets without a current warning to align.

The four selected-version saved GETs do not carry LRO flags/options. The other four have no selected-version Swagger operation to compare. The [historical ledger](../arm-only-20261106/analysis.md#retained-native-protocol-get-findings) preserves the original membership evidence.

**Gap analysis and decision:** Native-only enforcement is outside the latest user-authorized rule, not migrated Swagger coverage. The eight former ARM warnings are absent, rather than substituted for the four Legacy matches. No follow-up issue is created.

## Raw-extension boundary

The final public `flag-only` control authors this exact operation under `@service namespace Contoso`:

```typespec
@TypeSpec.OpenAPI.extension("x-ms-long-running-operation", true)
@get
@route("/read")
op read(): {
  value: string;
};
```

The `options-only` control instead authors `@TypeSpec.OpenAPI.extension("x-ms-long-running-operation-options", #{})`, also without a Legacy marker.

| Engine          | Evidence                                                                                                                                                                                                                                                                                                      |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Swagger linter  | The pinned [implementation](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/packages/rulesets/src/spectral/az-arm.ts) checks LRO extension properties on GET. This is implementation evidence; these controls were not newly emitted and validated as Swagger. |
| TypeSpec linter | Zero target warnings in configured and target-only controls for both raw-only declarations.                                                                                                                                                                                                                   |

**Coverage status:** Missing from the new predicate. No raw-only occurrence is observed among the four assessed Swagger findings; that does not establish structural prevention or universal existing-rule coverage.

**Gap analysis and decision:** Keep this limitation explicit. Existing configuration-dependent OpenAPI-extension guidance is not counted as captured substitute coverage here. The user selected marker-only enforcement; do not add a detector, normalize away a future unmatched occurrence or declare full extension parity from the current totals.

## Suppression accounting

The full worker honors source suppressions but has no suppressed-diagnostic callback/capture. Thus the configured target total is 4, the included current total is 4, excluded current diagnostics are empty, and additional corresponding suppressed diagnostics captured are empty. Exhaustive suppression-inclusive totals for other owning checks remain unassessed.

Each of the four matched targets actually emitted its new warning. Existing source pragmas cover such checks as `no-legacy-usage`, `lro-location-header`, `no-response-body` and, on one CostManagement target, `mark-as-lro-ineffective`. They are not new-rule suppressions and do not remove the observed warnings. Source inspection explains these pragmas; it is not counted as an observed unsuppressed execution of those owning checks.

Canonical and injected tests separately establish that suppressing the new rule removes its warning, while suppressing a different Legacy diagnostic does not. The canonical SDK-generation case retains an SDK `lro` with the justified new-rule suppression. These are controls, not extra suppressed corpus findings.

## Controls and regressions

- Canonical SDK rule: 17 cases, plus existing Legacy/package interactions in the full SDK suite. Tests cover exact authored target identity, concrete template-derived operations, explicit/global service boundaries, scoped/repeated markers, comma-only empty scope, native-only and invalid/ineffective boundaries, non-GETs and suppression.
- SDK suite: 1,970 passed and two skipped, with one startup timeout; the isolated retry passed. Combined unique tested cases: 1,971 passed, two skipped.
- Central ruleset suite: 20 passed. Owning `all` and client-SDK activation are tested through real registered execution; ARM/data-plane/C# presets remain inactive.
- Portable injected harness: 37 passed, six unrelated resource-group fixtures excluded before execution. Selected public controls: 25 fixtures in two modes, all 50 passed.
- Invalid-target controls retain the existing **warning** and ignored marker; native-ineffective controls retain the existing **error** and rejected marker. Control success asserts the intended result, not universal error-free compilation.
- Empty-scope regression fixed the predicate before the final corpus: an empty key does not denote an effective SDK language. Exclusion arrays are not marker values. Existing parsing/state precedence is reused, not reimplemented.
- Two selected-driver failures and one missing registry `next` closure failure are archived. These were preparation assumptions, not production regressions; no production edit followed the final corpus.

See [validation](validation.json), [controls](controls-summary.json), [runtime verification](runtime-verification.json), and the archived raw logs/fixtures. Historical external coverage-category reports are not the population or methodology used for this immutable-baseline comparison.

## Scoped conclusion

The final run restores all four observed Legacy-caused Swagger findings and intentionally excludes the eight former native-only source warnings. Every current project/diagnostic difference is accounted for, with no uncovered production regression found. This supports the selected accepted-marker guideline and its activation/suppression contract, not complete Swagger property-level equivalence. Broader migration acceptance remains a reviewer decision.

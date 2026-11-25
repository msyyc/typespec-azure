# Resolver refresh: changed targets and coverage impact

The chosen `resolveArmResources` traversal reduces configured TypeSpec linter findings from 283 to 267. There are 16 removed diagnostics in 11 projects and no added targets. The removed findings are canonical-resource comparisons on 15 GETs and 1 POST, outside the four Swagger linters' assessed checks. They were already excluded from the previous attributed total; no corresponding original diagnostic is lost.

Fresh attribution and owning callbacks still give **433 Swagger / 200 TypeSpec diagnostics**, covering **208 of 277 check contexts**. The scoped raw gap remains **233**. The unfiltered gap increases by 16; this does not create 16 new missing original checks. [Exact current accounting](diagnostic-count-components.json), [fresh owner evidence](gap-probes.json), [full target delta](receipts/resolver-20261125-comparison.json).

| Resolver effect                                                  | Removed TypeSpec diagnostics | analysis                                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Action rather than a canonical resource list                     | 1                            | The old registration argument selected a canonical parent/resource comparison; the resolver supplies no eligible read/create/update/list association here. Keep the agreed resolver-only boundary, not a legacy fallback. This is not a claim that every underlying model or operation contract is compliant. |
| Operation absent from resolved resource and provider collections | 8                            | The old registration argument selected a canonical parent/resource comparison; the resolver supplies no eligible read/create/update/list association here. Keep the agreed resolver-only boundary, not a legacy fallback. This is not a claim that every underlying model or operation contract is compliant. |
| Provider operation without a canonical resource association      | 7                            | The old registration argument selected a canonical parent/resource comparison; the resolver supplies no eligible read/create/update/list association here. Keep the agreed resolver-only boundary, not a legacy fallback. This is not a claim that every underlying model or operation contract is compliant. |

The generic LIST/PATCH-only limitation remains a real traversal boundary ([#5994](https://github.com/Azure/typespec-azure/issues/5994)). The retained 10 non-resource PUT contexts / 108 Swagger findings remain a separate resolver prerequisite ([#5995](https://github.com/Azure/typespec-azure/issues/5995)). The 9 marker-policy contexts and unresolved request/cross-method contracts remain unchanged. No general structural matcher, extension-presence policy or custom-marker tightening was added.

## Every removed target

| Project / source operation                                                                                                                                                                                                                                                                                                                                                                                                                                  | Previous / current TypeSpec | Resolver effect                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ---------------------------------------------------------------- |
| `specification/automation/resource-manager/Microsoft.Automation/Automation` / [Microsoft.Automation.AutomationAccounts.listFieldsByType](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/AutomationAccount.tsp#L314)                                                                                                                  | 1 / 0                       | Operation absent from resolved resource and provider collections |
| `specification/automation/resource-manager/Microsoft.Automation/Automation` / [Microsoft.Automation.DscNodes.getContent](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/DscNode.tsp#L143)                                                                                                                                            | 1 / 0                       | Operation absent from resolved resource and provider collections |
| `specification/dataprotection/resource-manager/Microsoft.DataProtection/DataProtection` / [Microsoft.DataProtection.BackupVaultResources.exportJobsOperationResultGet](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/dataprotection/resource-manager/Microsoft.DataProtection/DataProtection/BackupVaultResource.tsp#L209)                                                                      | 1 / 0                       | Operation absent from resolved resource and provider collections |
| `specification/devopsinfrastructure/resource-manager/Microsoft.DevOpsInfrastructure/DevOpsInfrastructure` / [Microsoft.DevOpsInfrastructure.SubscriptionUsages.usages](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/devopsinfrastructure/resource-manager/Microsoft.DevOpsInfrastructure/DevOpsInfrastructure/main.tsp#L833)                                                                   | 1 / 0                       | Provider operation without a canonical resource association      |
| `specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight` / [Microsoft.HDInsight.ScriptActions.getExecutionAsyncOperationStatus](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/routes.tsp#L399)                                                                                                                         | 1 / 0                       | Operation absent from resolved resource and provider collections |
| `specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight` / [Microsoft.HDInsight.VirtualMachines.getAsyncOperationStatus](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/routes.tsp#L498)                                                                                                                                | 1 / 0                       | Operation absent from resolved resource and provider collections |
| `specification/loadtestservice/resource-manager/Microsoft.LoadTestService/loadtesting` / [Microsoft.LoadTestService.LoadTests.outboundNetworkDependenciesEndpoints](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/loadtestservice/resource-manager/Microsoft.LoadTestService/loadtesting/routes.tsp#L63)                                                                                        | 1 / 0                       | Action rather than a canonical resource list                     |
| `specification/marketplacecatalog/resource-manager/Microsoft.Marketplace/Products` / [Microsoft.Marketplace.ProductList.listByBillingAccount](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/marketplacecatalog/resource-manager/Microsoft.Marketplace/Products/main.tsp#L118)                                                                                                                   | 1 / 0                       | Provider operation without a canonical resource association      |
| `specification/marketplacecatalog/resource-manager/Microsoft.Marketplace/Products` / [Microsoft.Marketplace.ProductList.listByBillingProfile](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/marketplacecatalog/resource-manager/Microsoft.Marketplace/Products/main.tsp#L157)                                                                                                                   | 1 / 0                       | Provider operation without a canonical resource association      |
| `specification/marketplacecatalog/resource-manager/Microsoft.Marketplace/Products` / [Microsoft.Marketplace.ProductList.listBySubscription](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/marketplacecatalog/resource-manager/Microsoft.Marketplace/Products/main.tsp#L83)                                                                                                                      | 1 / 0                       | Provider operation without a canonical resource association      |
| `specification/monitor/resource-manager/Microsoft.Insights/Insights/MetricAlertApi` / [MetricAlertApi.MetricAlertResources.list](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/monitor/resource-manager/Microsoft.Insights/Insights/MetricAlertApi/MetricAlertResource.tsp#L130)                                                                                                                | 1 / 0                       | Provider operation without a canonical resource association      |
| `specification/monitor/resource-manager/Microsoft.Insights/Insights/MetricAlertApi` / [MetricAlertApi.MetricAlertResources.listByName](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/monitor/resource-manager/Microsoft.Insights/Insights/MetricAlertApi/MetricAlertResource.tsp#L149)                                                                                                          | 1 / 0                       | Provider operation without a canonical resource association      |
| `specification/operationalinsights/resource-manager/Microsoft.OperationalInsights/OperationalInsights` / [Microsoft.OperationalInsights.Workspaces.schemaGet](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/operationalinsights/resource-manager/Microsoft.OperationalInsights/OperationalInsights/Workspace.tsp#L321)                                                                          | 1 / 0                       | Provider operation without a canonical resource association      |
| `specification/privatedns/resource-manager/Microsoft.Network/PrivateDns` / [Microsoft.Network.RecordSets.listByType](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/privatedns/resource-manager/Microsoft.Network/PrivateDns/RecordSet.tsp#L157)                                                                                                                                                 | 1 / 0                       | Operation absent from resolved resource and provider collections |
| `specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup` / [Microsoft.RecoveryServices.ExportJobsOperationResults.get](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/JobResource.tsp#L155)                                                           | 1 / 0                       | Operation absent from resolved resource and provider collections |
| `specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI` / [SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentSettingsOperationGroup.getScanOperationResult](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI/SqlVulnerabilityAssessmentSettings.tsp#L176) | 1 / 0                       | Operation absent from resolved resource and provider collections |

## Code-backed representatives

### Action rather than a canonical resource list

**Classification:** TypeSpec-only count change. **Status:** resolver-only contract followed; underlying authoring/model correctness is not inferred from an absent warning.

**Project/source:** `specification/loadtestservice/resource-manager/Microsoft.LoadTestService/loadtesting` / `routes.tsp`, lines 59-68.

```typespec
  #suppress "@azure-tools/typespec-azure-core/no-openapi" "OperationID already published."
  @operationId("LoadTests_ListOutboundNetworkDependenciesEndpoints")
  @doc("Lists the endpoints that agents may call as part of load testing.")
  @list
  outboundNetworkDependenciesEndpoints is CustomOperations.ArmResourceActionSyncCustomGet<
    LoadTestResource,
    void,
    PagedOutboundEnvironmentEndpoint
  >;
}
```

**Frozen emitted response / route evidence:**

```json
[
  {
    "document": "projects/specification/loadtestservice/resource-manager/Microsoft.LoadTestService/loadtesting/swagger/preview/2024-12-01-preview/loadtestservice.json",
    "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LoadTestService/loadTests/{loadTestName}/outboundNetworkDependenciesEndpoints",
    "operations": [
      {
        "verb": "get",
        "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LoadTestService/loadTests/{loadTestName}/outboundNetworkDependenciesEndpoints",
        "operationId": "LoadTests_ListOutboundNetworkDependenciesEndpoints",
        "request": null,
        "responses": {
          "200": {
            "raw": {
              "$ref": "#/definitions/PagedOutboundEnvironmentEndpoint"
            },
            "reference": {
              "document": "projects/specification/loadtestservice/resource-manager/Microsoft.LoadTestService/loadtesting/swagger/preview/2024-12-01-preview/loadtestservice.json",
              "pointer": ["definitions", "PagedOutboundEnvironmentEndpoint"]
            },
            "topLevelResolvedSchemaSha256": "4a1cdd906d3a96d1166f67e270ff53ce6d422a5f30adb4ea6a3be62e0e44280c",
            "xmsResourceInHierarchy": false
          }
        }
      }
    ]
  }
]
```

| Engine          | Observed result                                                         |
| --------------- | ----------------------------------------------------------------------- |
| Swagger linter  | No finding from the four original comparisons on this operation target. |
| TypeSpec linter | Previous canonical comparison: 1. Current configured comparison: 0.     |

**Cause and coverage status:** Action rather than a canonical resource list. The original resource registration argument is not an eligible resolved canonical comparison.

**analysis:** Preserve the API direction agreed in #6053; do not infer a canonical resource from a verb or add legacy enumeration to retain these counts. Review the operation's actual parent/result/list role if an authoring correction is desired. This is separate from the original Swagger check coverage.

### Operation absent from resolved resource and provider collections

**Classification:** TypeSpec-only count change. **Status:** resolver-only contract followed; underlying authoring/model correctness is not inferred from an absent warning.

**Project/source:** `specification/automation/resource-manager/Microsoft.Automation/Automation` / `AutomationAccount.tsp`, lines 308-327.

```typespec
  #suppress "@azure-tools/typespec-azure-core/no-openapi" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  @tag("ObjectDataTypes")
  @OpenAPI.externalDocs("http://aka.ms/azureautomationsdk/objectdatatypeoperations")
  @list
  @get
  @action("fields")
  listFieldsByType is ArmResourceRead<
    AutomationAccount,
    BaseParameters = Azure.ResourceManager.Foundations.DefaultBaseParameters<AutomationAccount>,
    Response = ArmResponse<TypeFieldListResult>,
    Parameters = {
      /**
       * The name of type.
       */
      @path
      @segment("objectDataTypes")
      typeName: string;
    }
  >;

```

**Frozen emitted response / route evidence:**

```json
[
  {
    "document": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
    "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/objectDataTypes/{typeName}/fields",
    "operations": [
      {
        "verb": "get",
        "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/objectDataTypes/{typeName}/fields",
        "operationId": "ObjectDataTypes_ListFieldsByType",
        "request": null,
        "responses": {
          "200": {
            "raw": {
              "$ref": "#/definitions/TypeFieldListResult"
            },
            "reference": {
              "document": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
              "pointer": ["definitions", "TypeFieldListResult"]
            },
            "topLevelResolvedSchemaSha256": "0fb5e07da501322bf4dfea0be6028d932e8ca31073c733ffe4b655002953eb6e",
            "xmsResourceInHierarchy": false
          }
        }
      }
    ]
  }
]
```

| Engine          | Observed result                                                         |
| --------------- | ----------------------------------------------------------------------- |
| Swagger linter  | No finding from the four original comparisons on this operation target. |
| TypeSpec linter | Previous canonical comparison: 1. Current configured comparison: 0.     |

**Cause and coverage status:** Operation absent from resolved resource and provider collections. The original resource registration argument is not an eligible resolved canonical comparison.

**analysis:** Preserve the API direction agreed in #6053; do not infer a canonical resource from a verb or add legacy enumeration to retain these counts. Review the operation's actual parent/result/list role if an authoring correction is desired. This is separate from the original Swagger check coverage.

### Provider operation without a canonical resource association

**Classification:** TypeSpec-only count change. **Status:** resolver-only contract followed; underlying authoring/model correctness is not inferred from an absent warning.

**Project/source:** `specification/devopsinfrastructure/resource-manager/Microsoft.DevOpsInfrastructure/DevOpsInfrastructure` / `main.tsp`, lines 825-840.

```typespec
interface SubscriptionUsages {
  #suppress "@azure-tools/typespec-azure-resource-manager/arm-resource-invalid-action-verb" "Actions must be HTTP Post operations."
  @action
  @armProviderNameValue
  @get
  @armResourceList(Location)
  @doc("List Quota resources by subscription ID")
  @list
  usages(
    ...SubscriptionIdParameter,
    ...Azure.ResourceManager.Foundations.DefaultProviderNamespace,
    ...LocationResourceParameter,
    ...ApiVersionParameter,
  ): ArmResponse<Page<Quota>> | ErrorResponse;
}
```

**Frozen emitted response / route evidence:**

```json
[
  {
    "document": "projects/specification/devopsinfrastructure/resource-manager/Microsoft.DevOpsInfrastructure/DevOpsInfrastructure/swagger/preview/2026-07-03-preview/devopsinfrastructure.json",
    "route": "/subscriptions/{subscriptionId}/providers/Microsoft.DevOpsInfrastructure/locations/{location}/usages",
    "operations": [
      {
        "verb": "get",
        "route": "/subscriptions/{subscriptionId}/providers/Microsoft.DevOpsInfrastructure/locations/{location}/usages",
        "operationId": "SubscriptionUsages_Usages",
        "request": null,
        "responses": {
          "200": {
            "raw": {
              "$ref": "#/definitions/PagedQuota"
            },
            "reference": {
              "document": "projects/specification/devopsinfrastructure/resource-manager/Microsoft.DevOpsInfrastructure/DevOpsInfrastructure/swagger/preview/2026-07-03-preview/devopsinfrastructure.json",
              "pointer": ["definitions", "PagedQuota"]
            },
            "topLevelResolvedSchemaSha256": "ffb38c7054f0f335601924135edd61536c81e7965579cbc63ff7cfa696df200c",
            "xmsResourceInHierarchy": false
          }
        }
      }
    ]
  }
]
```

| Engine          | Observed result                                                         |
| --------------- | ----------------------------------------------------------------------- |
| Swagger linter  | No finding from the four original comparisons on this operation target. |
| TypeSpec linter | Previous canonical comparison: 1. Current configured comparison: 0.     |

**Cause and coverage status:** Provider operation without a canonical resource association. The original resource registration argument is not an eligible resolved canonical comparison.

**analysis:** Preserve the API direction agreed in #6053; do not infer a canonical resource from a verb or add legacy enumeration to retain these counts. Review the operation's actual parent/result/list role if an authoring correction is desired. This is separate from the original Swagger check coverage.

# specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI

[All project differences](../instance-correspondence.md#differing-projects).

<a id="s-5855bd5b6e6f7223"></a>

## PutRequestResponseSchemeArm: 5855bd5b6e6f7223

**Route/document:** `/{resourceId}/providers/Microsoft.Security/sqlVulnerabilityAssessments/default/baselineRules/{ruleId}`; `projects/specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI/swagger/preview/2026-04-01-preview/security-SqlVulnerabilityAssessments.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/{resourceId}/providers/Microsoft.Security/sqlVulnerabilityAssessments/default/baselineRules/{ruleId}",
      "operationId": "SqlVulnerabilityAssessmentBaselineRules_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/RuleResultsInput"
        },
        "reference": {
          "document": "projects/specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI/swagger/preview/2026-04-01-preview/security-SqlVulnerabilityAssessments.json",
          "pointer": ["definitions", "RuleResultsInput"]
        },
        "topLevelResolvedSchemaSha256": "ae31bf16637a1637a2f42f11bb780312e60cefca6bdd0a9a46b79a8123423eff",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/RuleResults"
          },
          "reference": {
            "document": "projects/specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI/swagger/preview/2026-04-01-preview/security-SqlVulnerabilityAssessments.json",
            "pointer": ["definitions", "RuleResults"]
          },
          "topLevelResolvedSchemaSha256": "26bbe1d5774c80402baed2425b646860b0f02de9730f87d758a7d3ba1c9cac30",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/RuleResults"
          },
          "reference": {
            "document": "projects/specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI/swagger/preview/2026-04-01-preview/security-SqlVulnerabilityAssessments.json",
            "pointer": ["definitions", "RuleResults"]
          },
          "topLevelResolvedSchemaSha256": "26bbe1d5774c80402baed2425b646860b0f02de9730f87d758a7d3ba1c9cac30",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentBaselineRules.createOrUpdate",
      "sourceFile": "RuleResults.tsp",
      "line": 87,
      "verb": "put",
      "path": "/{resourceId}/providers/Microsoft.Security/sqlVulnerabilityAssessments/default/baselineRules/{ruleId}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "SqlVulnerabilityAssessmentsAPI.RuleResultsInput",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "SqlVulnerabilityAssessmentsAPI.RuleResultsInput",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "SqlVulnerabilityAssessmentsAPI.RuleResultsInput",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "SqlVulnerabilityAssessmentsAPI.RuleResultsInput",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "SqlVulnerabilityAssessmentsAPI.RuleResults",
          "group": "lists",
          "kind": "createOrUpdate",
          "operationKey": "[\"SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentBaselineRules.createOrUpdate\",{\"sourceFile\":\"RuleResults.tsp\",\"line\":87,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<SqlVulnerabilityAssessmentsAPI.RuleResults>",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<SqlVulnerabilityAssessmentsAPI.RuleResults>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "SqlVulnerabilityAssessmentsAPI.RuleResults",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "SqlVulnerabilityAssessmentsAPI.RuleResults",
                  "discriminated": false
                },
                {
                  "name": "Azure.ResourceManager.CommonTypes.ExtensionResource",
                  "discriminated": false
                },
                {
                  "name": "Azure.ResourceManager.CommonTypes.Resource",
                  "discriminated": false
                }
              ],
              "effectiveModel": "SqlVulnerabilityAssessmentsAPI.RuleResults"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<SqlVulnerabilityAssessmentsAPI.RuleResults>",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<SqlVulnerabilityAssessmentsAPI.RuleResults>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "SqlVulnerabilityAssessmentsAPI.RuleResults",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "SqlVulnerabilityAssessmentsAPI.RuleResults",
                  "discriminated": false
                },
                {
                  "name": "Azure.ResourceManager.CommonTypes.ExtensionResource",
                  "discriminated": false
                },
                {
                  "name": "Azure.ResourceManager.CommonTypes.Resource",
                  "discriminated": false
                }
              ],
              "effectiveModel": "SqlVulnerabilityAssessmentsAPI.RuleResults"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Common.CloudError",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Common.CloudError",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Common.CloudError",
              "kind": "Model",
              "registeredResource": false,
              "void": false,
              "lineage": [
                {
                  "name": "Common.CloudError",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Common.CloudError"
            }
          ]
        }
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentBaselineRules.createOrUpdate\",{\"sourceFile\":\"RuleResults.tsp\",\"line\":87,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI:0"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:185"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

## Additional comparison: SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentSettingsOperationGroup.getScanOperationResult

[SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentSettingsOperationGroup.getScanOperationResult](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI/SqlVulnerabilityAssessmentSettings.tsp#L176); **additional-canonical-response-policy**.

```json
{
  "diagnostic": {
    "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
    "message": "[RPC 008]: PUT, GET, PATCH & LIST must return the same resource schema.",
    "targetKind": "Operation",
    "operationKey": "[\"SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentSettingsOperationGroup.getScanOperationResult\",{\"sourceFile\":\"SqlVulnerabilityAssessmentSettings.tsp\",\"line\":176,\"column\":3}]",
    "sourceFile": "SqlVulnerabilityAssessmentSettings.tsp",
    "line": 176,
    "column": 3
  },
  "operation": {
    "operation": "SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentSettingsOperationGroup.getScanOperationResult",
    "sourceFile": "SqlVulnerabilityAssessmentSettings.tsp",
    "line": 176,
    "verb": "get",
    "path": "/{resourceId}/providers/Microsoft.Security/sqlVulnerabilityAssessments/default/scans/scanOperationResults/{operationId}",
    "associations": [
      {
        "resource": "SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentSettings",
        "group": "lists",
        "kind": "getScanOperationResult",
        "operationKey": "[\"SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentSettingsOperationGroup.getScanOperationResult\",{\"sourceFile\":\"SqlVulnerabilityAssessmentSettings.tsp\",\"line\":176,\"column\":3}]",
        "internal": false,
        "checkedResponseKind": "read",
        "checkedPutRequest": false
      }
    ],
    "responses": [
      {
        "statusCodes": 200,
        "type": {
          "name": "Azure.ResourceManager.ArmResponse<SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentScanOperationResult>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResponse<SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentScanOperationResult>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentScanOperationResult",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentScanOperationResult",
                "discriminated": false
              },
              {
                "name": "Azure.ResourceManager.CommonTypes.Resource",
                "discriminated": false
              }
            ],
            "effectiveModel": "SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentScanOperationResult"
          }
        ]
      },
      {
        "statusCodes": "*",
        "type": {
          "name": "Common.CloudError",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Common.CloudError",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Common.CloudError",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Common.CloudError",
                "discriminated": false
              }
            ],
            "effectiveModel": "Common.CloudError"
          }
        ]
      }
    ]
  },
  "selectedVersionOperationIdentities": [
    "[\"SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentSettingsOperationGroup.getScanOperationResult\",{\"sourceFile\":\"SqlVulnerabilityAssessmentSettings.tsp\",\"line\":176,\"column\":3}]"
  ],
  "emittedBindings": [
    {
      "document": "projects/specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI/swagger/preview/2026-04-01-preview/security-SqlVulnerabilityAssessments.json",
      "route": "/{resourceId}/providers/Microsoft.Security/sqlVulnerabilityAssessments/default/scans/scanOperationResults/{operationId}",
      "operations": [
        {
          "verb": "get",
          "route": "/{resourceId}/providers/Microsoft.Security/sqlVulnerabilityAssessments/default/scans/scanOperationResults/{operationId}",
          "operationId": "SqlVulnerabilityAssessmentScans_GetScanOperationResult",
          "request": null,
          "responses": {
            "200": {
              "raw": {
                "$ref": "#/definitions/SqlVulnerabilityAssessmentScanOperationResult"
              },
              "reference": {
                "document": "projects/specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI/swagger/preview/2026-04-01-preview/security-SqlVulnerabilityAssessments.json",
                "pointer": ["definitions", "SqlVulnerabilityAssessmentScanOperationResult"]
              },
              "topLevelResolvedSchemaSha256": "d6dc819c2101024f0ba326d60c6614299f106efb18582e51a8b42bf088617878",
              "xmsResourceInHierarchy": true
            }
          }
        }
      ]
    }
  ]
}
```

**Gap analysis and decision:** Review the authored canonical resource and actual success body. Parent/child, command, polling-result and collection-role associations are not automatically original cross-method comparisons; prefer wire-compatible spec fixes over weakening the rule.

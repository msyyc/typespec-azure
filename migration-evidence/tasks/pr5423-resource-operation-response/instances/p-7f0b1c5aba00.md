# specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI

[All project differences](../instance-correspondence.md#differing-projects).

<a id="s-5855bd5b6e6f7223"></a>

## PutRequestResponseSchemeArm: 5855bd5b6e6f7223

**Route/document:** `/{resourceId}/providers/Microsoft.Security/sqlVulnerabilityAssessments/default/baselineRules/{ruleId}`; `projects/specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI/swagger/preview/2026-04-01-preview/security-SqlVulnerabilityAssessments.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 corresponding selected callbacks before suppression; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

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
          "declaration": {
            "sourceFile": "models.tsp",
            "line": 192,
            "column": 7
          },
          "registeredResource": false,
          "resolvedResource": false,
          "canonicalResources": [],
          "nativeResource": false,
          "nativeResourceDeclarations": [
            {
              "model": "SqlVulnerabilityAssessmentsAPI.RuleResultsInput",
              "registered": false,
              "resolved": false,
              "resourceBase": false,
              "customDeclaration": false,
              "virtualDeclaration": false
            }
          ],
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
          "declaration": {
            "sourceFile": "models.tsp",
            "line": 192,
            "column": 7
          },
          "registeredResource": false,
          "resolvedResource": false,
          "canonicalResources": [],
          "nativeResource": false,
          "nativeResourceDeclarations": [
            {
              "model": "SqlVulnerabilityAssessmentsAPI.RuleResultsInput",
              "registered": false,
              "resolved": false,
              "resourceBase": false,
              "customDeclaration": false,
              "virtualDeclaration": false
            }
          ],
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
          "resourceInstancePath": "/{resourceId}/providers/Microsoft.Security/sqlVulnerabilityAssessments/default/baselineRules/{ruleId}",
          "scope": "Scope",
          "group": "lifecycle",
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
            "declaration": {
              "sourceFile": "../../../../../../node_modules/.pnpm/@azure-tools+typespec-azure_d9e44c01360e3f74ee605d4aa55553ab/node_modules/@azure-tools/typespec-azure-resource-manager/lib/responses.tsp",
              "line": 317,
              "column": 7
            },
            "registeredResource": false,
            "resolvedResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Azure.ResourceManager.ArmResourceUpdatedResponse<SqlVulnerabilityAssessmentsAPI.RuleResults>",
                "registered": false,
                "resolved": false,
                "resourceBase": false,
                "customDeclaration": false,
                "virtualDeclaration": false
              }
            ],
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
              "declaration": {
                "sourceFile": "RuleResults.tsp",
                "line": 22,
                "column": 7
              },
              "registeredResource": true,
              "resolvedResource": true,
              "canonicalResources": ["SqlVulnerabilityAssessmentsAPI.RuleResults"],
              "nativeResource": true,
              "nativeResourceDeclarations": [
                {
                  "model": "SqlVulnerabilityAssessmentsAPI.RuleResults",
                  "registered": true,
                  "resolved": true,
                  "resourceBase": false,
                  "customDeclaration": false,
                  "virtualDeclaration": false
                },
                {
                  "model": "Azure.ResourceManager.CommonTypes.ExtensionResource",
                  "registered": false,
                  "resolved": false,
                  "resourceBase": false,
                  "customDeclaration": false,
                  "virtualDeclaration": false
                },
                {
                  "model": "Azure.ResourceManager.CommonTypes.Resource",
                  "registered": false,
                  "resolved": false,
                  "resourceBase": true,
                  "customDeclaration": false,
                  "virtualDeclaration": false
                }
              ],
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
            "declaration": {
              "sourceFile": "../../../../../../node_modules/.pnpm/@azure-tools+typespec-azure_d9e44c01360e3f74ee605d4aa55553ab/node_modules/@azure-tools/typespec-azure-resource-manager/lib/responses.tsp",
              "line": 363,
              "column": 7
            },
            "registeredResource": false,
            "resolvedResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<SqlVulnerabilityAssessmentsAPI.RuleResults>",
                "registered": false,
                "resolved": false,
                "resourceBase": false,
                "customDeclaration": false,
                "virtualDeclaration": false
              }
            ],
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
              "declaration": {
                "sourceFile": "RuleResults.tsp",
                "line": 22,
                "column": 7
              },
              "registeredResource": true,
              "resolvedResource": true,
              "canonicalResources": ["SqlVulnerabilityAssessmentsAPI.RuleResults"],
              "nativeResource": true,
              "nativeResourceDeclarations": [
                {
                  "model": "SqlVulnerabilityAssessmentsAPI.RuleResults",
                  "registered": true,
                  "resolved": true,
                  "resourceBase": false,
                  "customDeclaration": false,
                  "virtualDeclaration": false
                },
                {
                  "model": "Azure.ResourceManager.CommonTypes.ExtensionResource",
                  "registered": false,
                  "resolved": false,
                  "resourceBase": false,
                  "customDeclaration": false,
                  "virtualDeclaration": false
                },
                {
                  "model": "Azure.ResourceManager.CommonTypes.Resource",
                  "registered": false,
                  "resolved": false,
                  "resourceBase": true,
                  "customDeclaration": false,
                  "virtualDeclaration": false
                }
              ],
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
            "declaration": {
              "sourceFile": "../Common/main.tsp",
              "line": 60,
              "column": 7
            },
            "registeredResource": false,
            "resolvedResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Common.CloudError",
                "registered": false,
                "resolved": false,
                "resourceBase": false,
                "customDeclaration": false,
                "virtualDeclaration": false
              }
            ],
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
              "declaration": {
                "sourceFile": "../Common/main.tsp",
                "line": 60,
                "column": 7
              },
              "registeredResource": false,
              "resolvedResource": false,
              "canonicalResources": [],
              "nativeResource": false,
              "nativeResourceDeclarations": [
                {
                  "model": "Common.CloudError",
                  "registered": false,
                  "resolved": false,
                  "resourceBase": false,
                  "customDeclaration": false,
                  "virtualDeclaration": false
                }
              ],
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
      ],
      "resolverExposed": true,
      "projectOwned": true,
      "inInterface": true,
      "armNamespace": true
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentBaselineRules.createOrUpdate\",{\"sourceFile\":\"RuleResults.tsp\",\"line\":87,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI:0"
  ],
  "mappedNativePredicateIds": [
    "specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI:predicate:0"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:185"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

# specification/devopsinfrastructure/resource-manager/Microsoft.DevOpsInfrastructure/DevOpsInfrastructure

[All project differences](../instance-correspondence.md#differing-projects).

## Additional comparison: Microsoft.DevOpsInfrastructure.SubscriptionUsages.usages

[Microsoft.DevOpsInfrastructure.SubscriptionUsages.usages](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/devopsinfrastructure/resource-manager/Microsoft.DevOpsInfrastructure/DevOpsInfrastructure/main.tsp#L833); **additional-canonical-response-policy**.

```json
{
  "diagnostic": {
    "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
    "message": "[RPC 008]: PUT, GET, PATCH & LIST must return the same resource schema.",
    "targetKind": "Operation",
    "operationKey": "[\"Microsoft.DevOpsInfrastructure.SubscriptionUsages.usages\",{\"sourceFile\":\"main.tsp\",\"line\":833,\"column\":3}]",
    "sourceFile": "main.tsp",
    "line": 833,
    "column": 3
  },
  "operation": {
    "operation": "Microsoft.DevOpsInfrastructure.SubscriptionUsages.usages",
    "sourceFile": "main.tsp",
    "line": 833,
    "verb": "get",
    "path": "/subscriptions/{subscriptionId}/providers/Microsoft.DevOpsInfrastructure/locations/{location}/usages",
    "associations": [
      {
        "resource": "Microsoft.DevOpsInfrastructure.Location",
        "group": "lists",
        "kind": "usages",
        "operationKey": "[\"Microsoft.DevOpsInfrastructure.SubscriptionUsages.usages\",{\"sourceFile\":\"main.tsp\",\"line\":833,\"column\":3}]",
        "internal": false,
        "checkedResponseKind": "list",
        "checkedPutRequest": false
      }
    ],
    "responses": [
      {
        "statusCodes": 200,
        "type": {
          "name": "Azure.ResourceManager.ArmResponse<Azure.Core.Page<Microsoft.DevOpsInfrastructure.Quota>>",
          "kind": "Model",
          "declaration": {
            "sourceFile": "../../../../../node_modules/.pnpm/@azure-tools+typespec-azure_4e16f6958b689539320f5d6f4fdd0da2/node_modules/@azure-tools/typespec-azure-resource-manager/lib/responses.tsp",
            "line": 19,
            "column": 7
          },
          "registeredResource": false,
          "canonicalResources": [],
          "nativeResource": false,
          "nativeResourceDeclarations": [
            {
              "model": "Azure.ResourceManager.ArmResponse<Azure.Core.Page<Microsoft.DevOpsInfrastructure.Quota>>",
              "registered": false,
              "resourceBase": false,
              "customDeclaration": false
            }
          ],
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResponse<Azure.Core.Page<Microsoft.DevOpsInfrastructure.Quota>>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Azure.Core.Page<Microsoft.DevOpsInfrastructure.Quota>",
            "kind": "Model",
            "declaration": {
              "sourceFile": "../../../../../node_modules/.pnpm/@azure-tools+typespec-azure_5a4f63133f252f0fd542cb267e49f496/node_modules/@azure-tools/typespec-azure-core/lib/models.tsp",
              "line": 16,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Azure.Core.Page<Microsoft.DevOpsInfrastructure.Quota>",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Azure.Core.Page<Microsoft.DevOpsInfrastructure.Quota>",
                "discriminated": false
              }
            ],
            "effectiveModel": "Azure.Core.Page<Microsoft.DevOpsInfrastructure.Quota>",
            "collectionItem": {
              "name": "Microsoft.DevOpsInfrastructure.Quota",
              "kind": "Model",
              "declaration": {
                "sourceFile": "main.tsp",
                "line": 843,
                "column": 7
              },
              "registeredResource": false,
              "canonicalResources": [],
              "nativeResource": false,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.DevOpsInfrastructure.Quota",
                  "registered": false,
                  "resourceBase": false,
                  "customDeclaration": false
                }
              ],
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.DevOpsInfrastructure.Quota",
                  "discriminated": false
                }
              ]
            }
          }
        ]
      },
      {
        "statusCodes": "*",
        "type": {
          "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
          "kind": "Model",
          "declaration": {
            "sourceFile": "../../../../../node_modules/.pnpm/@azure-tools+typespec-azure_4e16f6958b689539320f5d6f4fdd0da2/node_modules/@azure-tools/typespec-azure-resource-manager/lib/common-types/types.tsp",
            "line": 290,
            "column": 7
          },
          "registeredResource": false,
          "canonicalResources": [],
          "nativeResource": false,
          "nativeResourceDeclarations": [
            {
              "model": "Azure.ResourceManager.CommonTypes.ErrorResponse",
              "registered": false,
              "resourceBase": false,
              "customDeclaration": false
            }
          ],
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "declaration": {
              "sourceFile": "../../../../../node_modules/.pnpm/@azure-tools+typespec-azure_4e16f6958b689539320f5d6f4fdd0da2/node_modules/@azure-tools/typespec-azure-resource-manager/lib/common-types/types.tsp",
              "line": 290,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Azure.ResourceManager.CommonTypes.ErrorResponse",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
                "discriminated": false
              }
            ],
            "effectiveModel": "Azure.ResourceManager.CommonTypes.ErrorResponse"
          }
        ]
      }
    ],
    "resolverExposed": false,
    "projectOwned": true,
    "inInterface": true,
    "armNamespace": true
  },
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.DevOpsInfrastructure.SubscriptionUsages.usages\",{\"sourceFile\":\"main.tsp\",\"line\":833,\"column\":3}]"
  ],
  "emittedBindings": [
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
}
```

**Gap analysis and decision:** Review the authored canonical resource and actual success body. Parent/child, command, polling-result and collection-role associations are not automatically original cross-method comparisons; prefer wire-compatible spec fixes over weakening the rule.

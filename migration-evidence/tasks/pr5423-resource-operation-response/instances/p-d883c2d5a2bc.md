# specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices

[All project differences](../instance-correspondence.md#differing-projects).

<a id="s-147374c72a96fb47"></a>

## PutGetPatchResponseSchema: 147374c72a96fb47

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/computes/{computeName}`; `projects/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices/swagger/preview/2026-09-15-preview/cognitiveservices.json`.

**Observed:** 1 Swagger raw / 1 member check; 0 corresponding configured TypeSpec warnings; 0 corresponding selected callbacks before suppression; 0 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** recommended-non-porting-not-approved. **Classification:** missed-cross-operation-selected-ref-absent.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/computes/{computeName}",
      "operationId": "Computes_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/Compute"
        },
        "reference": {
          "document": "projects/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices/swagger/preview/2026-09-15-preview/cognitiveservices.json",
          "pointer": ["definitions", "Compute"]
        },
        "topLevelResolvedSchemaSha256": "c32a470f6a32233c7fd796a4e28634a587894d6dbc2266cf013582520f50a738",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "202": null
      }
    },
    {
      "verb": "get",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/computes/{computeName}",
      "operationId": "Computes_Get",
      "request": null,
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/Compute"
          },
          "reference": {
            "document": "projects/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices/swagger/preview/2026-09-15-preview/cognitiveservices.json",
            "pointer": ["definitions", "Compute"]
          },
          "topLevelResolvedSchemaSha256": "c32a470f6a32233c7fd796a4e28634a587894d6dbc2266cf013582520f50a738",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.CognitiveServices.Computes.createOrUpdate",
      "sourceFile": "Compute.tsp",
      "line": 91,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/computes/{computeName}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.CognitiveServices.Compute",
          "kind": "Model",
          "declaration": {
            "sourceFile": "Compute.tsp",
            "line": 29,
            "column": 7
          },
          "registeredResource": true,
          "canonicalResources": ["Microsoft.CognitiveServices.Compute"],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.CognitiveServices.Compute",
              "registered": true,
              "resourceBase": false,
              "customDeclaration": false
            },
            {
              "model": "Azure.ResourceManager.CommonTypes.ProxyResource",
              "registered": false,
              "resourceBase": false,
              "customDeclaration": false
            },
            {
              "model": "Azure.ResourceManager.CommonTypes.Resource",
              "registered": false,
              "resourceBase": true,
              "customDeclaration": false
            }
          ],
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.CognitiveServices.Compute",
              "discriminated": false
            },
            {
              "name": "Azure.ResourceManager.CommonTypes.ProxyResource",
              "discriminated": false
            },
            {
              "name": "Azure.ResourceManager.CommonTypes.Resource",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.CognitiveServices.Compute",
          "kind": "Model",
          "declaration": {
            "sourceFile": "Compute.tsp",
            "line": 29,
            "column": 7
          },
          "registeredResource": true,
          "canonicalResources": ["Microsoft.CognitiveServices.Compute"],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.CognitiveServices.Compute",
              "registered": true,
              "resourceBase": false,
              "customDeclaration": false
            },
            {
              "model": "Azure.ResourceManager.CommonTypes.ProxyResource",
              "registered": false,
              "resourceBase": false,
              "customDeclaration": false
            },
            {
              "model": "Azure.ResourceManager.CommonTypes.Resource",
              "registered": false,
              "resourceBase": true,
              "customDeclaration": false
            }
          ],
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.CognitiveServices.Compute",
              "discriminated": false
            },
            {
              "name": "Azure.ResourceManager.CommonTypes.ProxyResource",
              "discriminated": false
            },
            {
              "name": "Azure.ResourceManager.CommonTypes.Resource",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.CognitiveServices.Compute",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.CognitiveServices.Computes.createOrUpdate\",{\"sourceFile\":\"Compute.tsp\",\"line\":91,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 202,
          "type": {
            "name": "Azure.ResourceManager.ArmAcceptedLroResponse<\"Resource creation accepted.\", Azure.ResourceManager.ArmCombinedLroHeaders<Azure.ResourceManager.ArmOperationStatus<never, Azure.ResourceManager.ResourceProvisioningState>, Microsoft.CognitiveServices.Compute, TypeSpec.Rest.ResourceLocation, string>>",
            "kind": "Model",
            "declaration": {
              "sourceFile": "../../../../../node_modules/.pnpm/@azure-tools+typespec-azure_4e16f6958b689539320f5d6f4fdd0da2/node_modules/@azure-tools/typespec-azure-resource-manager/lib/responses.tsp",
              "line": 132,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Azure.ResourceManager.ArmAcceptedLroResponse<\"Resource creation accepted.\", Azure.ResourceManager.ArmCombinedLroHeaders<Azure.ResourceManager.ArmOperationStatus<never, Azure.ResourceManager.ResourceProvisioningState>, Microsoft.CognitiveServices.Compute, TypeSpec.Rest.ResourceLocation, string>>",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmAcceptedLroResponse<\"Resource creation accepted.\", Azure.ResourceManager.ArmCombinedLroHeaders<Azure.ResourceManager.ArmOperationStatus<never, Azure.ResourceManager.ResourceProvisioningState>, Microsoft.CognitiveServices.Compute, TypeSpec.Rest.ResourceLocation, string>>",
                "discriminated": false
              }
            ]
          },
          "bodies": [null]
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
      "resolverExposed": true,
      "projectOwned": true,
      "inInterface": true,
      "armNamespace": true
    },
    {
      "operation": "Microsoft.CognitiveServices.Computes.get",
      "sourceFile": "Compute.tsp",
      "line": 84,
      "verb": "get",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/computes/{computeName}",
      "associations": [
        {
          "resource": "Microsoft.CognitiveServices.Compute",
          "group": "lifecycle",
          "kind": "read",
          "operationKey": "[\"Microsoft.CognitiveServices.Computes.get\",{\"sourceFile\":\"Compute.tsp\",\"line\":84,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "read",
          "checkedPutRequest": false
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "Azure.ResourceManager.ArmResponse<Microsoft.CognitiveServices.Compute>",
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
                "model": "Azure.ResourceManager.ArmResponse<Microsoft.CognitiveServices.Compute>",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResponse<Microsoft.CognitiveServices.Compute>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.CognitiveServices.Compute",
              "kind": "Model",
              "declaration": {
                "sourceFile": "Compute.tsp",
                "line": 29,
                "column": 7
              },
              "registeredResource": true,
              "canonicalResources": ["Microsoft.CognitiveServices.Compute"],
              "nativeResource": true,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.CognitiveServices.Compute",
                  "registered": true,
                  "resourceBase": false,
                  "customDeclaration": false
                },
                {
                  "model": "Azure.ResourceManager.CommonTypes.ProxyResource",
                  "registered": false,
                  "resourceBase": false,
                  "customDeclaration": false
                },
                {
                  "model": "Azure.ResourceManager.CommonTypes.Resource",
                  "registered": false,
                  "resourceBase": true,
                  "customDeclaration": false
                }
              ],
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.CognitiveServices.Compute",
                  "discriminated": false
                },
                {
                  "name": "Azure.ResourceManager.CommonTypes.ProxyResource",
                  "discriminated": false
                },
                {
                  "name": "Azure.ResourceManager.CommonTypes.Resource",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Microsoft.CognitiveServices.Compute"
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
      "resolverExposed": true,
      "projectOwned": true,
      "inInterface": true,
      "armNamespace": true
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.CognitiveServices.Computes.createOrUpdate\",{\"sourceFile\":\"Compute.tsp\",\"line\":91,\"column\":3}]",
    "[\"Microsoft.CognitiveServices.Computes.get\",{\"sourceFile\":\"Compute.tsp\",\"line\":84,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [],
  "mappedNativePredicateIds": [],
  "ownerReports": [],
  "rawObservationIds": ["PutGetPatchResponseSchema:6"]
}
```

**Gap analysis and decision:** The comparison treats a correctly bodyless 202 or 204 as an unequal resource schema. Do not invent a response body or add a resource-schema warning merely to match that result. This does not establish that the operation's status set is ARM-compliant: arm-put-response-codes owns that separate question. This is a recommended intentional difference, not approved retirement or existing migration credit.

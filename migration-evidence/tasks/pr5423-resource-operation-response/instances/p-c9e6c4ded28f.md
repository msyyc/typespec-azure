# specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc

[All project differences](../instance-correspondence.md#differing-projects).

<a id="s-3b8448268bb7dcd2"></a>

## ConsistentResponseSchemaForPut: 3b8448268bb7dcd2

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/serverGroupsv2/{clusterName}/privateEndpointConnections/{privateEndpointConnectionName}`; `projects/specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc/swagger/preview/2023-03-02-preview/postgresqlhsc.json`.

**Observed:** 1 Swagger raw / 1 member check; 0 corresponding configured TypeSpec warnings; 0 corresponding selected callbacks before suppression; 0 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** confirmed-upstream-false-positive. **Classification:** upstream-identity-false-positive.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/serverGroupsv2/{clusterName}/privateEndpointConnections/{privateEndpointConnectionName}",
      "operationId": "PrivateEndpointConnections_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "../../../../../../../../../common-types/resource-management/v4/privatelinks.json#/definitions/PrivateEndpointConnection"
        },
        "reference": {
          "document": "common-types/resource-management/v4/privatelinks.json",
          "pointer": ["definitions", "PrivateEndpointConnection"]
        },
        "topLevelResolvedSchemaSha256": "ca39c48c7fcfad8c52d9868df1b7669be57a41677cb7e54584c075ddc2972f08",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "../../../../../../../../../common-types/resource-management/v4/privatelinks.json#/definitions/PrivateEndpointConnection"
          },
          "reference": {
            "document": "common-types/resource-management/v4/privatelinks.json",
            "pointer": ["definitions", "PrivateEndpointConnection"]
          },
          "topLevelResolvedSchemaSha256": "ca39c48c7fcfad8c52d9868df1b7669be57a41677cb7e54584c075ddc2972f08",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "../../../../../../../../../common-types/resource-management/v4/privatelinks.json#/definitions/PrivateEndpointConnection"
          },
          "reference": {
            "document": "common-types/resource-management/v4/privatelinks.json",
            "pointer": ["definitions", "PrivateEndpointConnection"]
          },
          "topLevelResolvedSchemaSha256": "ca39c48c7fcfad8c52d9868df1b7669be57a41677cb7e54584c075ddc2972f08",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.DBforPostgreSQL.PrivateEndpointConnections.createOrUpdate",
      "sourceFile": "PrivateEndpointConnection.tsp",
      "line": 27,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/serverGroupsv2/{clusterName}/privateEndpointConnections/{privateEndpointConnectionName}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.DBforPostgreSQL.PrivateEndpointConnection",
          "kind": "Model",
          "declaration": {
            "sourceFile": "PrivateEndpointConnection.tsp",
            "line": 13,
            "column": 7
          },
          "registeredResource": true,
          "canonicalResources": ["Microsoft.DBforPostgreSQL.PrivateEndpointConnection"],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.DBforPostgreSQL.PrivateEndpointConnection",
              "registered": true,
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
              "name": "Microsoft.DBforPostgreSQL.PrivateEndpointConnection",
              "discriminated": false
            },
            {
              "name": "Azure.ResourceManager.CommonTypes.Resource",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.DBforPostgreSQL.PrivateEndpointConnection",
          "kind": "Model",
          "declaration": {
            "sourceFile": "PrivateEndpointConnection.tsp",
            "line": 13,
            "column": 7
          },
          "registeredResource": true,
          "canonicalResources": ["Microsoft.DBforPostgreSQL.PrivateEndpointConnection"],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.DBforPostgreSQL.PrivateEndpointConnection",
              "registered": true,
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
              "name": "Microsoft.DBforPostgreSQL.PrivateEndpointConnection",
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
          "resource": "Microsoft.DBforPostgreSQL.PrivateEndpointConnection",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.DBforPostgreSQL.PrivateEndpointConnections.createOrUpdate\",{\"sourceFile\":\"PrivateEndpointConnection.tsp\",\"line\":27,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.DBforPostgreSQL.PrivateEndpointConnection>",
            "kind": "Model",
            "declaration": {
              "sourceFile": "../../../../../node_modules/.pnpm/@azure-tools+typespec-azure_4e16f6958b689539320f5d6f4fdd0da2/node_modules/@azure-tools/typespec-azure-resource-manager/lib/responses.tsp",
              "line": 317,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.DBforPostgreSQL.PrivateEndpointConnection>",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.DBforPostgreSQL.PrivateEndpointConnection>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.DBforPostgreSQL.PrivateEndpointConnection",
              "kind": "Model",
              "declaration": {
                "sourceFile": "PrivateEndpointConnection.tsp",
                "line": 13,
                "column": 7
              },
              "registeredResource": true,
              "canonicalResources": ["Microsoft.DBforPostgreSQL.PrivateEndpointConnection"],
              "nativeResource": true,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.DBforPostgreSQL.PrivateEndpointConnection",
                  "registered": true,
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
                  "name": "Microsoft.DBforPostgreSQL.PrivateEndpointConnection",
                  "discriminated": false
                },
                {
                  "name": "Azure.ResourceManager.CommonTypes.Resource",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Microsoft.DBforPostgreSQL.PrivateEndpointConnection"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceCreatedResponse<Microsoft.DBforPostgreSQL.PrivateEndpointConnection, { azureAsyncOperation: string, location: string }>",
            "kind": "Model",
            "declaration": {
              "sourceFile": "../../../../../node_modules/.pnpm/@azure-tools+typespec-azure_4e16f6958b689539320f5d6f4fdd0da2/node_modules/@azure-tools/typespec-azure-resource-manager/lib/responses.tsp",
              "line": 337,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Azure.ResourceManager.ArmResourceCreatedResponse<Microsoft.DBforPostgreSQL.PrivateEndpointConnection, { azureAsyncOperation: string, location: string }>",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceCreatedResponse<Microsoft.DBforPostgreSQL.PrivateEndpointConnection, { azureAsyncOperation: string, location: string }>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.DBforPostgreSQL.PrivateEndpointConnection",
              "kind": "Model",
              "declaration": {
                "sourceFile": "PrivateEndpointConnection.tsp",
                "line": 13,
                "column": 7
              },
              "registeredResource": true,
              "canonicalResources": ["Microsoft.DBforPostgreSQL.PrivateEndpointConnection"],
              "nativeResource": true,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.DBforPostgreSQL.PrivateEndpointConnection",
                  "registered": true,
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
                  "name": "Microsoft.DBforPostgreSQL.PrivateEndpointConnection",
                  "discriminated": false
                },
                {
                  "name": "Azure.ResourceManager.CommonTypes.Resource",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Microsoft.DBforPostgreSQL.PrivateEndpointConnection"
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
    "[\"Microsoft.DBforPostgreSQL.PrivateEndpointConnections.createOrUpdate\",{\"sourceFile\":\"PrivateEndpointConnection.tsp\",\"line\":27,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [],
  "mappedNativePredicateIds": [],
  "ownerReports": [],
  "rawObservationIds": ["ConsistentResponseSchemaForPut:6"]
}
```

**Gap analysis and decision:** Identical 200/201 references were compared by resolved JavaScript object identity. Do not reproduce this bug or count its absence as a missing useful diagnostic.

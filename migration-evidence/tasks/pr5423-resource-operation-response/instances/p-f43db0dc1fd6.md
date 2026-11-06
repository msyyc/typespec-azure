# specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace

[All project differences](../instance-correspondence.md#differing-projects).

<a id="s-dcb16038cea11cc9"></a>

## PutGetPatchResponseSchema: dcb16038cea11cc9

**Route/document:** `/providers/Microsoft.Marketplace/privateStores/{privateStoreId}`; `projects/specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace/swagger/stable/2025-01-01/Marketplace.json`.

**Observed:** 1 Swagger raw / 1 member check; 0 corresponding configured TypeSpec warnings; 0 corresponding selected callbacks before suppression; 0 same-operation findings (not automatically credited); 1 captured owning callbacks before suppression.

**Coverage status:** existing-owner-diagnostic-before-suppression. **Classification:** missed-cross-operation-selected-ref-absent.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/providers/Microsoft.Marketplace/privateStores/{privateStoreId}",
      "operationId": "PrivateStore_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/PrivateStore"
        },
        "reference": {
          "document": "projects/specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace/swagger/stable/2025-01-01/Marketplace.json",
          "pointer": ["definitions", "PrivateStore"]
        },
        "topLevelResolvedSchemaSha256": "75b87691af50259c47e25ebb9cf372bc1d9063f7318afa2834ab25db9594a697",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "200": null
      }
    },
    {
      "verb": "get",
      "route": "/providers/Microsoft.Marketplace/privateStores/{privateStoreId}",
      "operationId": "PrivateStore_Get",
      "request": null,
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/PrivateStore"
          },
          "reference": {
            "document": "projects/specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace/swagger/stable/2025-01-01/Marketplace.json",
            "pointer": ["definitions", "PrivateStore"]
          },
          "topLevelResolvedSchemaSha256": "75b87691af50259c47e25ebb9cf372bc1d9063f7318afa2834ab25db9594a697",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.Marketplace.PrivateStores.createOrUpdate",
      "sourceFile": "PrivateStore.tsp",
      "line": 43,
      "verb": "put",
      "path": "/providers/Microsoft.Marketplace/privateStores/{privateStoreId}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.Marketplace.PrivateStore",
          "kind": "Model",
          "declaration": {
            "sourceFile": "PrivateStore.tsp",
            "line": 17,
            "column": 7
          },
          "registeredResource": true,
          "canonicalResources": ["Microsoft.Marketplace.PrivateStore"],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.Marketplace.PrivateStore",
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
              "name": "Microsoft.Marketplace.PrivateStore",
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
          "name": "Microsoft.Marketplace.PrivateStore",
          "kind": "Model",
          "declaration": {
            "sourceFile": "PrivateStore.tsp",
            "line": 17,
            "column": 7
          },
          "registeredResource": true,
          "canonicalResources": ["Microsoft.Marketplace.PrivateStore"],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.Marketplace.PrivateStore",
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
              "name": "Microsoft.Marketplace.PrivateStore",
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
          "resource": "Microsoft.Marketplace.PrivateStore",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.Marketplace.PrivateStores.createOrUpdate\",{\"sourceFile\":\"PrivateStore.tsp\",\"line\":43,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "TypeSpec.Http.OkResponse",
            "kind": "Model",
            "declaration": {
              "sourceFile": "../../../../../node_modules/.pnpm/@typespec+http@file+..+evid_b09bef7b56e9aff619bebdb6a4fdcce9/node_modules/@typespec/http/lib/main.tsp",
              "line": 54,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "TypeSpec.Http.OkResponse",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "TypeSpec.Http.OkResponse",
                "discriminated": false
              }
            ]
          },
          "bodies": [null]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Microsoft.Marketplace.ErrorResponse",
            "kind": "Model",
            "declaration": {
              "sourceFile": "models.tsp",
              "line": 291,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Microsoft.Marketplace.ErrorResponse",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.Marketplace.ErrorResponse",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.Marketplace.ErrorResponse",
              "kind": "Model",
              "declaration": {
                "sourceFile": "models.tsp",
                "line": 291,
                "column": 7
              },
              "registeredResource": false,
              "canonicalResources": [],
              "nativeResource": false,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.Marketplace.ErrorResponse",
                  "registered": false,
                  "resourceBase": false,
                  "customDeclaration": false
                }
              ],
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.Marketplace.ErrorResponse",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Microsoft.Marketplace.ErrorResponse"
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
      "operation": "Microsoft.Marketplace.PrivateStores.get",
      "sourceFile": "PrivateStore.tsp",
      "line": 32,
      "verb": "get",
      "path": "/providers/Microsoft.Marketplace/privateStores/{privateStoreId}",
      "associations": [
        {
          "resource": "Microsoft.Marketplace.PrivateStore",
          "group": "lifecycle",
          "kind": "read",
          "operationKey": "[\"Microsoft.Marketplace.PrivateStores.get\",{\"sourceFile\":\"PrivateStore.tsp\",\"line\":32,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "read",
          "checkedPutRequest": false
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "Azure.ResourceManager.ArmResponse<Microsoft.Marketplace.PrivateStore>",
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
                "model": "Azure.ResourceManager.ArmResponse<Microsoft.Marketplace.PrivateStore>",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResponse<Microsoft.Marketplace.PrivateStore>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.Marketplace.PrivateStore",
              "kind": "Model",
              "declaration": {
                "sourceFile": "PrivateStore.tsp",
                "line": 17,
                "column": 7
              },
              "registeredResource": true,
              "canonicalResources": ["Microsoft.Marketplace.PrivateStore"],
              "nativeResource": true,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.Marketplace.PrivateStore",
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
                  "name": "Microsoft.Marketplace.PrivateStore",
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
              "effectiveModel": "Microsoft.Marketplace.PrivateStore"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Microsoft.Marketplace.ErrorResponse",
            "kind": "Model",
            "declaration": {
              "sourceFile": "models.tsp",
              "line": 291,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Microsoft.Marketplace.ErrorResponse",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.Marketplace.ErrorResponse",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.Marketplace.ErrorResponse",
              "kind": "Model",
              "declaration": {
                "sourceFile": "models.tsp",
                "line": 291,
                "column": 7
              },
              "registeredResource": false,
              "canonicalResources": [],
              "nativeResource": false,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.Marketplace.ErrorResponse",
                  "registered": false,
                  "resourceBase": false,
                  "customDeclaration": false
                }
              ],
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.Marketplace.ErrorResponse",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Microsoft.Marketplace.ErrorResponse"
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
    "[\"Microsoft.Marketplace.PrivateStores.createOrUpdate\",{\"sourceFile\":\"PrivateStore.tsp\",\"line\":43,\"column\":3}]",
    "[\"Microsoft.Marketplace.PrivateStores.get\",{\"sourceFile\":\"PrivateStore.tsp\",\"line\":32,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [],
  "mappedNativePredicateIds": [],
  "ownerReports": [
    {
      "project": "specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace",
      "reportIndex": 0,
      "rule": "no-response-body",
      "messageId": "default",
      "operationKey": "[\"Microsoft.Marketplace.PrivateStores.createOrUpdate\",{\"sourceFile\":\"PrivateStore.tsp\",\"line\":43,\"column\":3}]",
      "sourceFile": "PrivateStore.tsp",
      "line": 43,
      "column": 3
    }
  ],
  "rawObservationIds": ["PutGetPatchResponseSchema:18"]
}
```

**Gap analysis and decision:** Keep schema consistency separate from response existence. Review no-response-body and authored suppressions, and repair the spec only against the actual wire contract. Its current implementation checks the first ordinary response and skips some template operations; source ownership alone is not measured coverage. The focused owner-predicate results are linked in gap-analysis.md.

<a id="s-e6c42278fc611fee"></a>

## PutRequestResponseSchemeArm: e6c42278fc611fee

**Route/document:** `/providers/Microsoft.Marketplace/privateStores/{privateStoreId}`; `projects/specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace/swagger/stable/2025-01-01/Marketplace.json`.

**Observed:** 1 Swagger raw / 1 member check; 0 corresponding configured TypeSpec warnings; 0 corresponding selected callbacks before suppression; 0 same-operation findings (not automatically credited); 1 captured owning callbacks before suppression.

**Coverage status:** existing-owner-diagnostic-before-suppression. **Classification:** source-canonical-request-agrees-emitted-schemas-differ.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/providers/Microsoft.Marketplace/privateStores/{privateStoreId}",
      "operationId": "PrivateStore_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/PrivateStore"
        },
        "reference": {
          "document": "projects/specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace/swagger/stable/2025-01-01/Marketplace.json",
          "pointer": ["definitions", "PrivateStore"]
        },
        "topLevelResolvedSchemaSha256": "75b87691af50259c47e25ebb9cf372bc1d9063f7318afa2834ab25db9594a697",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "200": null
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.Marketplace.PrivateStores.createOrUpdate",
      "sourceFile": "PrivateStore.tsp",
      "line": 43,
      "verb": "put",
      "path": "/providers/Microsoft.Marketplace/privateStores/{privateStoreId}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.Marketplace.PrivateStore",
          "kind": "Model",
          "declaration": {
            "sourceFile": "PrivateStore.tsp",
            "line": 17,
            "column": 7
          },
          "registeredResource": true,
          "canonicalResources": ["Microsoft.Marketplace.PrivateStore"],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.Marketplace.PrivateStore",
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
              "name": "Microsoft.Marketplace.PrivateStore",
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
          "name": "Microsoft.Marketplace.PrivateStore",
          "kind": "Model",
          "declaration": {
            "sourceFile": "PrivateStore.tsp",
            "line": 17,
            "column": 7
          },
          "registeredResource": true,
          "canonicalResources": ["Microsoft.Marketplace.PrivateStore"],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.Marketplace.PrivateStore",
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
              "name": "Microsoft.Marketplace.PrivateStore",
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
          "resource": "Microsoft.Marketplace.PrivateStore",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.Marketplace.PrivateStores.createOrUpdate\",{\"sourceFile\":\"PrivateStore.tsp\",\"line\":43,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "TypeSpec.Http.OkResponse",
            "kind": "Model",
            "declaration": {
              "sourceFile": "../../../../../node_modules/.pnpm/@typespec+http@file+..+evid_b09bef7b56e9aff619bebdb6a4fdcce9/node_modules/@typespec/http/lib/main.tsp",
              "line": 54,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "TypeSpec.Http.OkResponse",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "TypeSpec.Http.OkResponse",
                "discriminated": false
              }
            ]
          },
          "bodies": [null]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Microsoft.Marketplace.ErrorResponse",
            "kind": "Model",
            "declaration": {
              "sourceFile": "models.tsp",
              "line": 291,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Microsoft.Marketplace.ErrorResponse",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.Marketplace.ErrorResponse",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.Marketplace.ErrorResponse",
              "kind": "Model",
              "declaration": {
                "sourceFile": "models.tsp",
                "line": 291,
                "column": 7
              },
              "registeredResource": false,
              "canonicalResources": [],
              "nativeResource": false,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.Marketplace.ErrorResponse",
                  "registered": false,
                  "resourceBase": false,
                  "customDeclaration": false
                }
              ],
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.Marketplace.ErrorResponse",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Microsoft.Marketplace.ErrorResponse"
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
    "[\"Microsoft.Marketplace.PrivateStores.createOrUpdate\",{\"sourceFile\":\"PrivateStore.tsp\",\"line\":43,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [],
  "mappedNativePredicateIds": [],
  "ownerReports": [
    {
      "project": "specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace",
      "reportIndex": 0,
      "rule": "no-response-body",
      "messageId": "default",
      "operationKey": "[\"Microsoft.Marketplace.PrivateStores.createOrUpdate\",{\"sourceFile\":\"PrivateStore.tsp\",\"line\":43,\"column\":3}]",
      "sourceFile": "PrivateStore.tsp",
      "line": 43,
      "column": 3
    }
  ],
  "rawObservationIds": ["PutRequestResponseSchemeArm:109"]
}
```

**Gap analysis and decision:** Keep schema consistency separate from response existence. Review no-response-body and authored suppressions, and repair the spec only against the actual wire contract. Its current implementation checks the first ordinary response and skips some template operations; source ownership alone is not measured coverage. The focused owner-predicate results are linked in gap-analysis.md.

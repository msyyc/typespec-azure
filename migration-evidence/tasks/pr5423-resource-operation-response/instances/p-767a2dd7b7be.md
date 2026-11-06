# specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync

[All project differences](../instance-correspondence.md#differing-projects).

<a id="s-a93ba334f29ff387"></a>

## PutRequestResponseSchemeArm: a93ba334f29ff387

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}`; `projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 corresponding selected callbacks before suppression; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}",
      "operationId": "StorageSyncServices_Create",
      "request": {
        "raw": {
          "$ref": "#/definitions/StorageSyncServiceCreateParameters"
        },
        "reference": {
          "document": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
          "pointer": ["definitions", "StorageSyncServiceCreateParameters"]
        },
        "topLevelResolvedSchemaSha256": "772354ec246c18af4ab0096ba9f345d2ec66ea9f083c1f6a063168810e6585aa",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/StorageSyncService"
          },
          "reference": {
            "document": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
            "pointer": ["definitions", "StorageSyncService"]
          },
          "topLevelResolvedSchemaSha256": "430cbcb8be977229f0e5cba6eb5070dc72d87f95b9263811a647cd9afcc10784",
          "xmsResourceInHierarchy": true
        },
        "202": null
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.StorageSync.StorageSyncServices.create",
      "sourceFile": "StorageSyncService.tsp",
      "line": 52,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.StorageSync.StorageSyncServiceCreateParameters",
          "kind": "Model",
          "declaration": {
            "sourceFile": "models.tsp",
            "line": 608,
            "column": 7
          },
          "registeredResource": false,
          "canonicalResources": [],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.StorageSync.StorageSyncServiceCreateParameters",
              "registered": false,
              "resourceBase": false,
              "customDeclaration": false
            },
            {
              "model": "Azure.ResourceManager.CommonTypes.TrackedResource",
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
              "name": "Microsoft.StorageSync.StorageSyncServiceCreateParameters",
              "discriminated": false
            },
            {
              "name": "Azure.ResourceManager.CommonTypes.TrackedResource",
              "discriminated": false
            },
            {
              "name": "Azure.ResourceManager.CommonTypes.Resource",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.StorageSync.StorageSyncServiceCreateParameters",
          "kind": "Model",
          "declaration": {
            "sourceFile": "models.tsp",
            "line": 608,
            "column": 7
          },
          "registeredResource": false,
          "canonicalResources": [],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.StorageSync.StorageSyncServiceCreateParameters",
              "registered": false,
              "resourceBase": false,
              "customDeclaration": false
            },
            {
              "model": "Azure.ResourceManager.CommonTypes.TrackedResource",
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
              "name": "Microsoft.StorageSync.StorageSyncServiceCreateParameters",
              "discriminated": false
            },
            {
              "name": "Azure.ResourceManager.CommonTypes.TrackedResource",
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
          "resource": "Microsoft.StorageSync.StorageSyncService",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.StorageSync.StorageSyncServices.create\",{\"sourceFile\":\"StorageSyncService.tsp\",\"line\":52,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.StorageSync.StorageSyncService>",
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
                "model": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.StorageSync.StorageSyncService>",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.StorageSync.StorageSyncService>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.StorageSync.StorageSyncService",
              "kind": "Model",
              "declaration": {
                "sourceFile": "StorageSyncService.tsp",
                "line": 16,
                "column": 7
              },
              "registeredResource": true,
              "canonicalResources": ["Microsoft.StorageSync.StorageSyncService"],
              "nativeResource": true,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.StorageSync.StorageSyncService",
                  "registered": true,
                  "resourceBase": false,
                  "customDeclaration": false
                },
                {
                  "model": "Azure.ResourceManager.CommonTypes.TrackedResource",
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
                  "name": "Microsoft.StorageSync.StorageSyncService",
                  "discriminated": false
                },
                {
                  "name": "Azure.ResourceManager.CommonTypes.TrackedResource",
                  "discriminated": false
                },
                {
                  "name": "Azure.ResourceManager.CommonTypes.Resource",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Microsoft.StorageSync.StorageSyncService"
            }
          ]
        },
        {
          "statusCodes": 202,
          "type": {
            "name": "{ statusCode: 202, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, retryAfter: int32, xMsCorrelationRequestId: string, xMsRequestId: string }",
            "kind": "Model",
            "declaration": {
              "sourceFile": "StorageSyncService.tsp",
              "line": 57,
              "column": 9
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "{ statusCode: 202, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, retryAfter: int32, xMsCorrelationRequestId: string, xMsRequestId: string }",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 202, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, retryAfter: int32, xMsCorrelationRequestId: string, xMsRequestId: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [null]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Microsoft.StorageSync.StorageSyncError",
            "kind": "Model",
            "declaration": {
              "sourceFile": "models.tsp",
              "line": 449,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Microsoft.StorageSync.StorageSyncError",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.StorageSync.StorageSyncError",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.StorageSync.StorageSyncError",
              "kind": "Model",
              "declaration": {
                "sourceFile": "models.tsp",
                "line": 449,
                "column": 7
              },
              "registeredResource": false,
              "canonicalResources": [],
              "nativeResource": false,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.StorageSync.StorageSyncError",
                  "registered": false,
                  "resourceBase": false,
                  "customDeclaration": false
                }
              ],
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.StorageSync.StorageSyncError",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Microsoft.StorageSync.StorageSyncError"
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
    "[\"Microsoft.StorageSync.StorageSyncServices.create\",{\"sourceFile\":\"StorageSyncService.tsp\",\"line\":52,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync:0"
  ],
  "mappedNativePredicateIds": [
    "specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync:predicate:0"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:198"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-2fd98161d8adcfd3"></a>

## PutRequestResponseSchemeArm: 2fd98161d8adcfd3

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/registeredServers/{serverId}`; `projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 corresponding selected callbacks before suppression; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/registeredServers/{serverId}",
      "operationId": "RegisteredServers_Create",
      "request": {
        "raw": {
          "$ref": "#/definitions/RegisteredServerCreateParameters"
        },
        "reference": {
          "document": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
          "pointer": ["definitions", "RegisteredServerCreateParameters"]
        },
        "topLevelResolvedSchemaSha256": "9023f3c81db7fcb1fb3456b1cd4521d2cd0a6408e08e64cf3e40192f34906232",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/RegisteredServer"
          },
          "reference": {
            "document": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
            "pointer": ["definitions", "RegisteredServer"]
          },
          "topLevelResolvedSchemaSha256": "4c49771587849d2ca5735428db4e3438d154d0b8f2a98dbd96d4ef8a0dae5aaa",
          "xmsResourceInHierarchy": true
        },
        "202": null
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.StorageSync.RegisteredServers.create",
      "sourceFile": "RegisteredServer.tsp",
      "line": 54,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/registeredServers/{serverId}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.StorageSync.RegisteredServerCreateParameters",
          "kind": "Model",
          "declaration": {
            "sourceFile": "models.tsp",
            "line": 2490,
            "column": 7
          },
          "registeredResource": false,
          "canonicalResources": [],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.StorageSync.RegisteredServerCreateParameters",
              "registered": false,
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
              "name": "Microsoft.StorageSync.RegisteredServerCreateParameters",
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
          "name": "Microsoft.StorageSync.RegisteredServerCreateParameters",
          "kind": "Model",
          "declaration": {
            "sourceFile": "models.tsp",
            "line": 2490,
            "column": 7
          },
          "registeredResource": false,
          "canonicalResources": [],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.StorageSync.RegisteredServerCreateParameters",
              "registered": false,
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
              "name": "Microsoft.StorageSync.RegisteredServerCreateParameters",
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
          "resource": "Microsoft.StorageSync.RegisteredServer",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.StorageSync.RegisteredServers.create\",{\"sourceFile\":\"RegisteredServer.tsp\",\"line\":54,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.StorageSync.RegisteredServer, xMsCorrelationRequestId: string, xMsRequestId: string }",
            "kind": "Model",
            "declaration": {
              "sourceFile": "RegisteredServer.tsp",
              "line": 58,
              "column": 9
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "{ statusCode: 200, body: Microsoft.StorageSync.RegisteredServer, xMsCorrelationRequestId: string, xMsRequestId: string }",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.StorageSync.RegisteredServer, xMsCorrelationRequestId: string, xMsRequestId: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.StorageSync.RegisteredServer",
              "kind": "Model",
              "declaration": {
                "sourceFile": "RegisteredServer.tsp",
                "line": 18,
                "column": 7
              },
              "registeredResource": true,
              "canonicalResources": ["Microsoft.StorageSync.RegisteredServer"],
              "nativeResource": true,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.StorageSync.RegisteredServer",
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
                  "name": "Microsoft.StorageSync.RegisteredServer",
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
              "effectiveModel": "Microsoft.StorageSync.RegisteredServer"
            }
          ]
        },
        {
          "statusCodes": 202,
          "type": {
            "name": "{ statusCode: 202, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, retryAfter: int32, xMsCorrelationRequestId: string, xMsRequestId: string }",
            "kind": "Model",
            "declaration": {
              "sourceFile": "RegisteredServer.tsp",
              "line": 67,
              "column": 9
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "{ statusCode: 202, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, retryAfter: int32, xMsCorrelationRequestId: string, xMsRequestId: string }",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 202, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, retryAfter: int32, xMsCorrelationRequestId: string, xMsRequestId: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [null]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Microsoft.StorageSync.StorageSyncError",
            "kind": "Model",
            "declaration": {
              "sourceFile": "models.tsp",
              "line": 449,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Microsoft.StorageSync.StorageSyncError",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.StorageSync.StorageSyncError",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.StorageSync.StorageSyncError",
              "kind": "Model",
              "declaration": {
                "sourceFile": "models.tsp",
                "line": 449,
                "column": 7
              },
              "registeredResource": false,
              "canonicalResources": [],
              "nativeResource": false,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.StorageSync.StorageSyncError",
                  "registered": false,
                  "resourceBase": false,
                  "customDeclaration": false
                }
              ],
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.StorageSync.StorageSyncError",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Microsoft.StorageSync.StorageSyncError"
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
    "[\"Microsoft.StorageSync.RegisteredServers.create\",{\"sourceFile\":\"RegisteredServer.tsp\",\"line\":54,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync:4"
  ],
  "mappedNativePredicateIds": [
    "specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync:predicate:4"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:199"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-9beeadcf7b7fa3a0"></a>

## PutRequestResponseSchemeArm: 9beeadcf7b7fa3a0

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}`; `projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 corresponding selected callbacks before suppression; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}",
      "operationId": "SyncGroups_Create",
      "request": {
        "raw": {
          "$ref": "#/definitions/SyncGroupCreateParameters"
        },
        "reference": {
          "document": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
          "pointer": ["definitions", "SyncGroupCreateParameters"]
        },
        "topLevelResolvedSchemaSha256": "93935836a1d27476aafff16789aad2e077c5f69d87ba0fed3e8c69aef1ac47ba",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/SyncGroup"
          },
          "reference": {
            "document": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
            "pointer": ["definitions", "SyncGroup"]
          },
          "topLevelResolvedSchemaSha256": "f47e5912758decc5504cba2ba652d900c92e2c31cde3aeaaf283c63609fca7ba",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.StorageSync.SyncGroups.create",
      "sourceFile": "SyncGroup.tsp",
      "line": 51,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.StorageSync.SyncGroupCreateParameters",
          "kind": "Model",
          "declaration": {
            "sourceFile": "models.tsp",
            "line": 784,
            "column": 7
          },
          "registeredResource": false,
          "canonicalResources": [],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.StorageSync.SyncGroupCreateParameters",
              "registered": false,
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
              "name": "Microsoft.StorageSync.SyncGroupCreateParameters",
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
          "name": "Microsoft.StorageSync.SyncGroupCreateParameters",
          "kind": "Model",
          "declaration": {
            "sourceFile": "models.tsp",
            "line": 784,
            "column": 7
          },
          "registeredResource": false,
          "canonicalResources": [],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.StorageSync.SyncGroupCreateParameters",
              "registered": false,
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
              "name": "Microsoft.StorageSync.SyncGroupCreateParameters",
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
          "resource": "Microsoft.StorageSync.SyncGroup",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.StorageSync.SyncGroups.create\",{\"sourceFile\":\"SyncGroup.tsp\",\"line\":51,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.StorageSync.SyncGroup, xMsCorrelationRequestId: string, xMsRequestId: string }",
            "kind": "Model",
            "declaration": {
              "sourceFile": "SyncGroup.tsp",
              "line": 54,
              "column": 16
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "{ statusCode: 200, body: Microsoft.StorageSync.SyncGroup, xMsCorrelationRequestId: string, xMsRequestId: string }",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.StorageSync.SyncGroup, xMsCorrelationRequestId: string, xMsRequestId: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.StorageSync.SyncGroup",
              "kind": "Model",
              "declaration": {
                "sourceFile": "SyncGroup.tsp",
                "line": 18,
                "column": 7
              },
              "registeredResource": true,
              "canonicalResources": ["Microsoft.StorageSync.SyncGroup"],
              "nativeResource": true,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.StorageSync.SyncGroup",
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
                  "name": "Microsoft.StorageSync.SyncGroup",
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
              "effectiveModel": "Microsoft.StorageSync.SyncGroup"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Microsoft.StorageSync.StorageSyncError",
            "kind": "Model",
            "declaration": {
              "sourceFile": "models.tsp",
              "line": 449,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Microsoft.StorageSync.StorageSyncError",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.StorageSync.StorageSyncError",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.StorageSync.StorageSyncError",
              "kind": "Model",
              "declaration": {
                "sourceFile": "models.tsp",
                "line": 449,
                "column": 7
              },
              "registeredResource": false,
              "canonicalResources": [],
              "nativeResource": false,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.StorageSync.StorageSyncError",
                  "registered": false,
                  "resourceBase": false,
                  "customDeclaration": false
                }
              ],
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.StorageSync.StorageSyncError",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Microsoft.StorageSync.StorageSyncError"
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
    "[\"Microsoft.StorageSync.SyncGroups.create\",{\"sourceFile\":\"SyncGroup.tsp\",\"line\":51,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync:1"
  ],
  "mappedNativePredicateIds": [
    "specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync:predicate:1"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:200"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-c66d4b452c9ef375"></a>

## PutRequestResponseSchemeArm: c66d4b452c9ef375

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}`; `projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 corresponding selected callbacks before suppression; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}",
      "operationId": "CloudEndpoints_Create",
      "request": {
        "raw": {
          "$ref": "#/definitions/CloudEndpointCreateParameters"
        },
        "reference": {
          "document": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
          "pointer": ["definitions", "CloudEndpointCreateParameters"]
        },
        "topLevelResolvedSchemaSha256": "4418e75bfbb1ccf137b3efc5151a4072c663b87ef4043f89fca59f191f315fc9",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/CloudEndpoint"
          },
          "reference": {
            "document": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
            "pointer": ["definitions", "CloudEndpoint"]
          },
          "topLevelResolvedSchemaSha256": "8af50280514d4503ed4afcd554ab5482ecd946d4f58b10498e89af76d5c5b450",
          "xmsResourceInHierarchy": true
        },
        "202": null
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.StorageSync.CloudEndpoints.create",
      "sourceFile": "CloudEndpoint.tsp",
      "line": 55,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.StorageSync.CloudEndpointCreateParameters",
          "kind": "Model",
          "declaration": {
            "sourceFile": "models.tsp",
            "line": 797,
            "column": 7
          },
          "registeredResource": false,
          "canonicalResources": [],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.StorageSync.CloudEndpointCreateParameters",
              "registered": false,
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
              "name": "Microsoft.StorageSync.CloudEndpointCreateParameters",
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
          "name": "Microsoft.StorageSync.CloudEndpointCreateParameters",
          "kind": "Model",
          "declaration": {
            "sourceFile": "models.tsp",
            "line": 797,
            "column": 7
          },
          "registeredResource": false,
          "canonicalResources": [],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.StorageSync.CloudEndpointCreateParameters",
              "registered": false,
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
              "name": "Microsoft.StorageSync.CloudEndpointCreateParameters",
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
          "resource": "Microsoft.StorageSync.CloudEndpoint",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.StorageSync.CloudEndpoints.create\",{\"sourceFile\":\"CloudEndpoint.tsp\",\"line\":55,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.StorageSync.CloudEndpoint, xMsCorrelationRequestId: string, xMsRequestId: string }",
            "kind": "Model",
            "declaration": {
              "sourceFile": "CloudEndpoint.tsp",
              "line": 59,
              "column": 9
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "{ statusCode: 200, body: Microsoft.StorageSync.CloudEndpoint, xMsCorrelationRequestId: string, xMsRequestId: string }",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.StorageSync.CloudEndpoint, xMsCorrelationRequestId: string, xMsRequestId: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.StorageSync.CloudEndpoint",
              "kind": "Model",
              "declaration": {
                "sourceFile": "CloudEndpoint.tsp",
                "line": 20,
                "column": 7
              },
              "registeredResource": true,
              "canonicalResources": ["Microsoft.StorageSync.CloudEndpoint"],
              "nativeResource": true,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.StorageSync.CloudEndpoint",
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
                  "name": "Microsoft.StorageSync.CloudEndpoint",
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
              "effectiveModel": "Microsoft.StorageSync.CloudEndpoint"
            }
          ]
        },
        {
          "statusCodes": 202,
          "type": {
            "name": "{ statusCode: 202, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, retryAfter: int32, xMsCorrelationRequestId: string, xMsRequestId: string }",
            "kind": "Model",
            "declaration": {
              "sourceFile": "CloudEndpoint.tsp",
              "line": 68,
              "column": 9
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "{ statusCode: 202, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, retryAfter: int32, xMsCorrelationRequestId: string, xMsRequestId: string }",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 202, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, retryAfter: int32, xMsCorrelationRequestId: string, xMsRequestId: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [null]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Microsoft.StorageSync.StorageSyncError",
            "kind": "Model",
            "declaration": {
              "sourceFile": "models.tsp",
              "line": 449,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Microsoft.StorageSync.StorageSyncError",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.StorageSync.StorageSyncError",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.StorageSync.StorageSyncError",
              "kind": "Model",
              "declaration": {
                "sourceFile": "models.tsp",
                "line": 449,
                "column": 7
              },
              "registeredResource": false,
              "canonicalResources": [],
              "nativeResource": false,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.StorageSync.StorageSyncError",
                  "registered": false,
                  "resourceBase": false,
                  "customDeclaration": false
                }
              ],
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.StorageSync.StorageSyncError",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Microsoft.StorageSync.StorageSyncError"
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
    "[\"Microsoft.StorageSync.CloudEndpoints.create\",{\"sourceFile\":\"CloudEndpoint.tsp\",\"line\":55,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync:2"
  ],
  "mappedNativePredicateIds": [
    "specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync:predicate:2"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:201"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-5347141e830697b7"></a>

## PutRequestResponseSchemeArm: 5347141e830697b7

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/serverEndpoints/{serverEndpointName}`; `projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 corresponding selected callbacks before suppression; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/serverEndpoints/{serverEndpointName}",
      "operationId": "ServerEndpoints_Create",
      "request": {
        "raw": {
          "$ref": "#/definitions/ServerEndpointCreateParameters"
        },
        "reference": {
          "document": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
          "pointer": ["definitions", "ServerEndpointCreateParameters"]
        },
        "topLevelResolvedSchemaSha256": "f0d7e663b5cc3d4977b70085d98bde43ca809ffcf5268b0d9343443c28518a41",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/ServerEndpoint"
          },
          "reference": {
            "document": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
            "pointer": ["definitions", "ServerEndpoint"]
          },
          "topLevelResolvedSchemaSha256": "679641829292b7272c9e5cc0daf3cbfa625bcb443ab18abdd6f35c04d0df69f6",
          "xmsResourceInHierarchy": true
        },
        "202": null
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.StorageSync.ServerEndpoints.create",
      "sourceFile": "ServerEndpoint.tsp",
      "line": 53,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/serverEndpoints/{serverEndpointName}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.StorageSync.ServerEndpointCreateParameters",
          "kind": "Model",
          "declaration": {
            "sourceFile": "models.tsp",
            "line": 1298,
            "column": 7
          },
          "registeredResource": false,
          "canonicalResources": [],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.StorageSync.ServerEndpointCreateParameters",
              "registered": false,
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
              "name": "Microsoft.StorageSync.ServerEndpointCreateParameters",
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
          "name": "Microsoft.StorageSync.ServerEndpointCreateParameters",
          "kind": "Model",
          "declaration": {
            "sourceFile": "models.tsp",
            "line": 1298,
            "column": 7
          },
          "registeredResource": false,
          "canonicalResources": [],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.StorageSync.ServerEndpointCreateParameters",
              "registered": false,
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
              "name": "Microsoft.StorageSync.ServerEndpointCreateParameters",
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
          "resource": "Microsoft.StorageSync.ServerEndpoint",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.StorageSync.ServerEndpoints.create\",{\"sourceFile\":\"ServerEndpoint.tsp\",\"line\":53,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.StorageSync.ServerEndpoint, xMsCorrelationRequestId: string, xMsRequestId: string }",
            "kind": "Model",
            "declaration": {
              "sourceFile": "ServerEndpoint.tsp",
              "line": 57,
              "column": 9
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "{ statusCode: 200, body: Microsoft.StorageSync.ServerEndpoint, xMsCorrelationRequestId: string, xMsRequestId: string }",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.StorageSync.ServerEndpoint, xMsCorrelationRequestId: string, xMsRequestId: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.StorageSync.ServerEndpoint",
              "kind": "Model",
              "declaration": {
                "sourceFile": "ServerEndpoint.tsp",
                "line": 18,
                "column": 7
              },
              "registeredResource": true,
              "canonicalResources": ["Microsoft.StorageSync.ServerEndpoint"],
              "nativeResource": true,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.StorageSync.ServerEndpoint",
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
                  "name": "Microsoft.StorageSync.ServerEndpoint",
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
              "effectiveModel": "Microsoft.StorageSync.ServerEndpoint"
            }
          ]
        },
        {
          "statusCodes": 202,
          "type": {
            "name": "{ statusCode: 202, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, retryAfter: int32, xMsCorrelationRequestId: string, xMsRequestId: string }",
            "kind": "Model",
            "declaration": {
              "sourceFile": "ServerEndpoint.tsp",
              "line": 66,
              "column": 9
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "{ statusCode: 202, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, retryAfter: int32, xMsCorrelationRequestId: string, xMsRequestId: string }",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 202, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, retryAfter: int32, xMsCorrelationRequestId: string, xMsRequestId: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [null]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Microsoft.StorageSync.StorageSyncError",
            "kind": "Model",
            "declaration": {
              "sourceFile": "models.tsp",
              "line": 449,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Microsoft.StorageSync.StorageSyncError",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.StorageSync.StorageSyncError",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.StorageSync.StorageSyncError",
              "kind": "Model",
              "declaration": {
                "sourceFile": "models.tsp",
                "line": 449,
                "column": 7
              },
              "registeredResource": false,
              "canonicalResources": [],
              "nativeResource": false,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.StorageSync.StorageSyncError",
                  "registered": false,
                  "resourceBase": false,
                  "customDeclaration": false
                }
              ],
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.StorageSync.StorageSyncError",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Microsoft.StorageSync.StorageSyncError"
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
    "[\"Microsoft.StorageSync.ServerEndpoints.create\",{\"sourceFile\":\"ServerEndpoint.tsp\",\"line\":53,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync:3"
  ],
  "mappedNativePredicateIds": [
    "specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync:predicate:3"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:202"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

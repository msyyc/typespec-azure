# specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota

[All project differences](../instance-correspondence.md#differing-projects).

<a id="s-272fe9a097875b9c"></a>

## ConsistentResponseSchemaForPut: 272fe9a097875b9c

**Route/document:** `/subscriptions/{subscriptionId}/providers/Microsoft.Capacity/resourceProviders/{providerId}/locations/{location}/serviceLimits/{resourceName}`; `projects/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/swagger/stable/2020-10-25/quota.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 corresponding selected callbacks before suppression; 1 same-operation findings (not automatically credited); 1 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-response-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/providers/Microsoft.Capacity/resourceProviders/{providerId}/locations/{location}/serviceLimits/{resourceName}",
      "operationId": "Quota_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/CurrentQuotaLimitBase"
        },
        "reference": {
          "document": "projects/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/swagger/stable/2020-10-25/quota.json",
          "pointer": ["definitions", "CurrentQuotaLimitBase"]
        },
        "topLevelResolvedSchemaSha256": "b51dfdff1e37f688177d4e69a5146529eb97d9da670a043d029e739acf0fc806",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/CurrentQuotaLimitBase"
          },
          "reference": {
            "document": "projects/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/swagger/stable/2020-10-25/quota.json",
            "pointer": ["definitions", "CurrentQuotaLimitBase"]
          },
          "topLevelResolvedSchemaSha256": "b51dfdff1e37f688177d4e69a5146529eb97d9da670a043d029e739acf0fc806",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/QuotaRequestSubmitResponse201"
          },
          "reference": {
            "document": "projects/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/swagger/stable/2020-10-25/quota.json",
            "pointer": ["definitions", "QuotaRequestSubmitResponse201"]
          },
          "topLevelResolvedSchemaSha256": "b3323ea2fc45d9bc626a10f4c9353bbf457ec2e43a40e639d33bf61ccb173751",
          "xmsResourceInHierarchy": false
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Quota.CurrentQuotaLimitBases.createOrUpdate",
      "sourceFile": "CurrentQuotaLimitBase.tsp",
      "line": 71,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/providers/Microsoft.Capacity/resourceProviders/{providerId}/locations/{location}/serviceLimits/{resourceName}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Quota.CurrentQuotaLimitBase",
          "kind": "Model",
          "declaration": {
            "sourceFile": "CurrentQuotaLimitBase.tsp",
            "line": 17,
            "column": 7
          },
          "registeredResource": true,
          "canonicalResources": ["Quota.CurrentQuotaLimitBase"],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Quota.CurrentQuotaLimitBase",
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
              "name": "Quota.CurrentQuotaLimitBase",
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
          "name": "Quota.CurrentQuotaLimitBase",
          "kind": "Model",
          "declaration": {
            "sourceFile": "CurrentQuotaLimitBase.tsp",
            "line": 17,
            "column": 7
          },
          "registeredResource": true,
          "canonicalResources": ["Quota.CurrentQuotaLimitBase"],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Quota.CurrentQuotaLimitBase",
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
              "name": "Quota.CurrentQuotaLimitBase",
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
          "resource": "Quota.CurrentQuotaLimitBase",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Quota.CurrentQuotaLimitBases.createOrUpdate\",{\"sourceFile\":\"CurrentQuotaLimitBase.tsp\",\"line\":71,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Quota.CurrentQuotaLimitBase>",
            "kind": "Model",
            "declaration": {
              "sourceFile": "../../../../../../node_modules/.pnpm/@azure-tools+typespec-azure_4e16f6958b689539320f5d6f4fdd0da2/node_modules/@azure-tools/typespec-azure-resource-manager/lib/responses.tsp",
              "line": 317,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Azure.ResourceManager.ArmResourceUpdatedResponse<Quota.CurrentQuotaLimitBase>",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Quota.CurrentQuotaLimitBase>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Quota.CurrentQuotaLimitBase",
              "kind": "Model",
              "declaration": {
                "sourceFile": "CurrentQuotaLimitBase.tsp",
                "line": 17,
                "column": 7
              },
              "registeredResource": true,
              "canonicalResources": ["Quota.CurrentQuotaLimitBase"],
              "nativeResource": true,
              "nativeResourceDeclarations": [
                {
                  "model": "Quota.CurrentQuotaLimitBase",
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
                  "name": "Quota.CurrentQuotaLimitBase",
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
              "effectiveModel": "Quota.CurrentQuotaLimitBase"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "Azure.ResourceManager.ArmCreatedResponse<Quota.QuotaRequestSubmitResponse201, { location: string, retryAfter: int32 }>",
            "kind": "Model",
            "declaration": {
              "sourceFile": "../../../../../../node_modules/.pnpm/@azure-tools+typespec-azure_4e16f6958b689539320f5d6f4fdd0da2/node_modules/@azure-tools/typespec-azure-resource-manager/lib/responses.tsp",
              "line": 42,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Azure.ResourceManager.ArmCreatedResponse<Quota.QuotaRequestSubmitResponse201, { location: string, retryAfter: int32 }>",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmCreatedResponse<Quota.QuotaRequestSubmitResponse201, { location: string, retryAfter: int32 }>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Quota.QuotaRequestSubmitResponse201",
              "kind": "Model",
              "declaration": {
                "sourceFile": "models.tsp",
                "line": 230,
                "column": 7
              },
              "registeredResource": false,
              "canonicalResources": [],
              "nativeResource": false,
              "nativeResourceDeclarations": [
                {
                  "model": "Quota.QuotaRequestSubmitResponse201",
                  "registered": false,
                  "resourceBase": false,
                  "customDeclaration": false
                }
              ],
              "void": false,
              "lineage": [
                {
                  "name": "Quota.QuotaRequestSubmitResponse201",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Quota.QuotaRequestSubmitResponse201"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Quota.ExceptionResponse",
            "kind": "Model",
            "declaration": {
              "sourceFile": "models.tsp",
              "line": 181,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Quota.ExceptionResponse",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Quota.ExceptionResponse",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Quota.ExceptionResponse",
              "kind": "Model",
              "declaration": {
                "sourceFile": "models.tsp",
                "line": 181,
                "column": 7
              },
              "registeredResource": false,
              "canonicalResources": [],
              "nativeResource": false,
              "nativeResourceDeclarations": [
                {
                  "model": "Quota.ExceptionResponse",
                  "registered": false,
                  "resourceBase": false,
                  "customDeclaration": false
                }
              ],
              "void": false,
              "lineage": [
                {
                  "name": "Quota.ExceptionResponse",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Quota.ExceptionResponse"
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
    "[\"Quota.CurrentQuotaLimitBases.createOrUpdate\",{\"sourceFile\":\"CurrentQuotaLimitBase.tsp\",\"line\":71,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota:0"
  ],
  "mappedNativePredicateIds": [
    "specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota:predicate:0"
  ],
  "ownerReports": [
    {
      "project": "specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota",
      "reportIndex": 0,
      "rule": "response-schema-problem",
      "messageId": "multipleSuccessSchemas",
      "operationKey": "[\"Quota.CurrentQuotaLimitBases.createOrUpdate\",{\"sourceFile\":\"CurrentQuotaLimitBase.tsp\",\"line\":71,\"column\":3}]",
      "sourceFile": "CurrentQuotaLimitBase.tsp",
      "line": 71,
      "column": 3
    }
  ],
  "rawObservationIds": ["ConsistentResponseSchemaForPut:8"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

## Additional comparison: Quota.CurrentQuotaLimitBases.update

[Quota.CurrentQuotaLimitBases.update](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/CurrentQuotaLimitBase.tsp#L95); **additional-canonical-response-policy**.

```json
{
  "diagnostic": {
    "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
    "message": "[RPC 008]: PUT, GET, PATCH & LIST must return the same resource schema.",
    "targetKind": "Operation",
    "operationKey": "[\"Quota.CurrentQuotaLimitBases.update\",{\"sourceFile\":\"CurrentQuotaLimitBase.tsp\",\"line\":95,\"column\":3}]",
    "sourceFile": "CurrentQuotaLimitBase.tsp",
    "line": 95,
    "column": 3
  },
  "operation": {
    "operation": "Quota.CurrentQuotaLimitBases.update",
    "sourceFile": "CurrentQuotaLimitBase.tsp",
    "line": 95,
    "verb": "patch",
    "path": "/subscriptions/{subscriptionId}/providers/Microsoft.Capacity/resourceProviders/{providerId}/locations/{location}/serviceLimits/{resourceName}",
    "request": {
      "bodyKind": "single",
      "type": {
        "name": "Quota.CurrentQuotaLimitBase",
        "kind": "Model",
        "declaration": {
          "sourceFile": "CurrentQuotaLimitBase.tsp",
          "line": 17,
          "column": 7
        },
        "registeredResource": true,
        "canonicalResources": ["Quota.CurrentQuotaLimitBase"],
        "nativeResource": true,
        "nativeResourceDeclarations": [
          {
            "model": "Quota.CurrentQuotaLimitBase",
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
            "name": "Quota.CurrentQuotaLimitBase",
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
        "name": "Quota.CurrentQuotaLimitBase",
        "kind": "Model",
        "declaration": {
          "sourceFile": "CurrentQuotaLimitBase.tsp",
          "line": 17,
          "column": 7
        },
        "registeredResource": true,
        "canonicalResources": ["Quota.CurrentQuotaLimitBase"],
        "nativeResource": true,
        "nativeResourceDeclarations": [
          {
            "model": "Quota.CurrentQuotaLimitBase",
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
            "name": "Quota.CurrentQuotaLimitBase",
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
        "resource": "Quota.CurrentQuotaLimitBase",
        "group": "lifecycle",
        "kind": "update",
        "operationKey": "[\"Quota.CurrentQuotaLimitBases.update\",{\"sourceFile\":\"CurrentQuotaLimitBase.tsp\",\"line\":95,\"column\":3}]",
        "internal": false,
        "checkedResponseKind": "update",
        "checkedPutRequest": false
      }
    ],
    "responses": [
      {
        "statusCodes": 200,
        "type": {
          "name": "Azure.ResourceManager.ArmResponse<Quota.CurrentQuotaLimitBase>",
          "kind": "Model",
          "declaration": {
            "sourceFile": "../../../../../../node_modules/.pnpm/@azure-tools+typespec-azure_4e16f6958b689539320f5d6f4fdd0da2/node_modules/@azure-tools/typespec-azure-resource-manager/lib/responses.tsp",
            "line": 19,
            "column": 7
          },
          "registeredResource": false,
          "canonicalResources": [],
          "nativeResource": false,
          "nativeResourceDeclarations": [
            {
              "model": "Azure.ResourceManager.ArmResponse<Quota.CurrentQuotaLimitBase>",
              "registered": false,
              "resourceBase": false,
              "customDeclaration": false
            }
          ],
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResponse<Quota.CurrentQuotaLimitBase>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Quota.CurrentQuotaLimitBase",
            "kind": "Model",
            "declaration": {
              "sourceFile": "CurrentQuotaLimitBase.tsp",
              "line": 17,
              "column": 7
            },
            "registeredResource": true,
            "canonicalResources": ["Quota.CurrentQuotaLimitBase"],
            "nativeResource": true,
            "nativeResourceDeclarations": [
              {
                "model": "Quota.CurrentQuotaLimitBase",
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
                "name": "Quota.CurrentQuotaLimitBase",
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
            "effectiveModel": "Quota.CurrentQuotaLimitBase"
          }
        ]
      },
      {
        "statusCodes": 201,
        "type": {
          "name": "Azure.ResourceManager.ArmCreatedResponse<Quota.QuotaRequestSubmitResponse201, { location: string, retryAfter: int32 }>",
          "kind": "Model",
          "declaration": {
            "sourceFile": "../../../../../../node_modules/.pnpm/@azure-tools+typespec-azure_4e16f6958b689539320f5d6f4fdd0da2/node_modules/@azure-tools/typespec-azure-resource-manager/lib/responses.tsp",
            "line": 42,
            "column": 7
          },
          "registeredResource": false,
          "canonicalResources": [],
          "nativeResource": false,
          "nativeResourceDeclarations": [
            {
              "model": "Azure.ResourceManager.ArmCreatedResponse<Quota.QuotaRequestSubmitResponse201, { location: string, retryAfter: int32 }>",
              "registered": false,
              "resourceBase": false,
              "customDeclaration": false
            }
          ],
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmCreatedResponse<Quota.QuotaRequestSubmitResponse201, { location: string, retryAfter: int32 }>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Quota.QuotaRequestSubmitResponse201",
            "kind": "Model",
            "declaration": {
              "sourceFile": "models.tsp",
              "line": 230,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Quota.QuotaRequestSubmitResponse201",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Quota.QuotaRequestSubmitResponse201",
                "discriminated": false
              }
            ],
            "effectiveModel": "Quota.QuotaRequestSubmitResponse201"
          }
        ]
      },
      {
        "statusCodes": "*",
        "type": {
          "name": "Quota.ExceptionResponse",
          "kind": "Model",
          "declaration": {
            "sourceFile": "models.tsp",
            "line": 181,
            "column": 7
          },
          "registeredResource": false,
          "canonicalResources": [],
          "nativeResource": false,
          "nativeResourceDeclarations": [
            {
              "model": "Quota.ExceptionResponse",
              "registered": false,
              "resourceBase": false,
              "customDeclaration": false
            }
          ],
          "void": false,
          "lineage": [
            {
              "name": "Quota.ExceptionResponse",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Quota.ExceptionResponse",
            "kind": "Model",
            "declaration": {
              "sourceFile": "models.tsp",
              "line": 181,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Quota.ExceptionResponse",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Quota.ExceptionResponse",
                "discriminated": false
              }
            ],
            "effectiveModel": "Quota.ExceptionResponse"
          }
        ]
      }
    ],
    "resolverExposed": true,
    "projectOwned": true,
    "inInterface": true,
    "armNamespace": true
  },
  "selectedVersionOperationIdentities": [
    "[\"Quota.CurrentQuotaLimitBases.update\",{\"sourceFile\":\"CurrentQuotaLimitBase.tsp\",\"line\":95,\"column\":3}]"
  ],
  "emittedBindings": [
    {
      "document": "projects/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/swagger/stable/2020-10-25/quota.json",
      "route": "/subscriptions/{subscriptionId}/providers/Microsoft.Capacity/resourceProviders/{providerId}/locations/{location}/serviceLimits/{resourceName}",
      "operations": [
        {
          "verb": "patch",
          "route": "/subscriptions/{subscriptionId}/providers/Microsoft.Capacity/resourceProviders/{providerId}/locations/{location}/serviceLimits/{resourceName}",
          "operationId": "Quota_Update",
          "request": {
            "raw": {
              "$ref": "#/definitions/CurrentQuotaLimitBase"
            },
            "reference": {
              "document": "projects/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/swagger/stable/2020-10-25/quota.json",
              "pointer": ["definitions", "CurrentQuotaLimitBase"]
            },
            "topLevelResolvedSchemaSha256": "b51dfdff1e37f688177d4e69a5146529eb97d9da670a043d029e739acf0fc806",
            "xmsResourceInHierarchy": true
          },
          "responses": {
            "200": {
              "raw": {
                "$ref": "#/definitions/CurrentQuotaLimitBase"
              },
              "reference": {
                "document": "projects/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/swagger/stable/2020-10-25/quota.json",
                "pointer": ["definitions", "CurrentQuotaLimitBase"]
              },
              "topLevelResolvedSchemaSha256": "b51dfdff1e37f688177d4e69a5146529eb97d9da670a043d029e739acf0fc806",
              "xmsResourceInHierarchy": true
            },
            "201": {
              "raw": {
                "$ref": "#/definitions/QuotaRequestSubmitResponse201"
              },
              "reference": {
                "document": "projects/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/swagger/stable/2020-10-25/quota.json",
                "pointer": ["definitions", "QuotaRequestSubmitResponse201"]
              },
              "topLevelResolvedSchemaSha256": "b3323ea2fc45d9bc626a10f4c9353bbf457ec2e43a40e639d33bf61ccb173751",
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

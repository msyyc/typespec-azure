# specification/portal/resource-manager/Microsoft.Portal/Portal

[All project differences](../instance-correspondence.md#differing-projects).

<a id="s-84a4cb24142840d5"></a>

## ConsistentResponseSchemaForPut: 84a4cb24142840d5

**Route/document:** `/providers/Microsoft.Portal/tenantConfigurations/{configurationName}`; `projects/specification/portal/resource-manager/Microsoft.Portal/Portal/swagger/stable/2026-04-01/tenantConfiguration.json`.

**Observed:** 1 Swagger raw / 1 member check; 0 corresponding configured TypeSpec warnings; 0 corresponding selected callbacks before suppression; 0 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** confirmed-upstream-false-positive. **Classification:** upstream-identity-false-positive.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/providers/Microsoft.Portal/tenantConfigurations/{configurationName}",
      "operationId": "TenantConfigurations_Create",
      "request": {
        "raw": {
          "$ref": "./common.json#/definitions/Configuration"
        },
        "reference": {
          "document": "projects/specification/portal/resource-manager/Microsoft.Portal/Portal/swagger/stable/2026-04-01/common.json",
          "pointer": ["definitions", "Configuration"]
        },
        "topLevelResolvedSchemaSha256": "258e9e2a15a433c3fb78e3fb0f57bb02a6ea69ea47fda27ff43f76951b235dba",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "./common.json#/definitions/Configuration"
          },
          "reference": {
            "document": "projects/specification/portal/resource-manager/Microsoft.Portal/Portal/swagger/stable/2026-04-01/common.json",
            "pointer": ["definitions", "Configuration"]
          },
          "topLevelResolvedSchemaSha256": "258e9e2a15a433c3fb78e3fb0f57bb02a6ea69ea47fda27ff43f76951b235dba",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "./common.json#/definitions/Configuration"
          },
          "reference": {
            "document": "projects/specification/portal/resource-manager/Microsoft.Portal/Portal/swagger/stable/2026-04-01/common.json",
            "pointer": ["definitions", "Configuration"]
          },
          "topLevelResolvedSchemaSha256": "258e9e2a15a433c3fb78e3fb0f57bb02a6ea69ea47fda27ff43f76951b235dba",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.Portal.TenantConfigurations.create",
      "sourceFile": "TenantConfiguration.tsp",
      "line": 48,
      "verb": "put",
      "path": "/providers/Microsoft.Portal/tenantConfigurations/{configurationName}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.Portal.Configuration",
          "kind": "Model",
          "declaration": {
            "sourceFile": "TenantConfiguration.tsp",
            "line": 27,
            "column": 7
          },
          "registeredResource": true,
          "canonicalResources": ["Microsoft.Portal.Configuration"],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.Portal.Configuration",
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
              "name": "Microsoft.Portal.Configuration",
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
          "name": "Microsoft.Portal.Configuration",
          "kind": "Model",
          "declaration": {
            "sourceFile": "TenantConfiguration.tsp",
            "line": 27,
            "column": 7
          },
          "registeredResource": true,
          "canonicalResources": ["Microsoft.Portal.Configuration"],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.Portal.Configuration",
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
              "name": "Microsoft.Portal.Configuration",
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
          "resource": "Microsoft.Portal.Configuration",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.Portal.TenantConfigurations.create\",{\"sourceFile\":\"TenantConfiguration.tsp\",\"line\":48,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.Portal.Configuration>",
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
                "model": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.Portal.Configuration>",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.Portal.Configuration>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.Portal.Configuration",
              "kind": "Model",
              "declaration": {
                "sourceFile": "TenantConfiguration.tsp",
                "line": 27,
                "column": 7
              },
              "registeredResource": true,
              "canonicalResources": ["Microsoft.Portal.Configuration"],
              "nativeResource": true,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.Portal.Configuration",
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
                  "name": "Microsoft.Portal.Configuration",
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
              "effectiveModel": "Microsoft.Portal.Configuration"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.Portal.Configuration>",
            "kind": "Model",
            "declaration": {
              "sourceFile": "../../../../../node_modules/.pnpm/@azure-tools+typespec-azure_4e16f6958b689539320f5d6f4fdd0da2/node_modules/@azure-tools/typespec-azure-resource-manager/lib/responses.tsp",
              "line": 363,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.Portal.Configuration>",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.Portal.Configuration>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.Portal.Configuration",
              "kind": "Model",
              "declaration": {
                "sourceFile": "TenantConfiguration.tsp",
                "line": 27,
                "column": 7
              },
              "registeredResource": true,
              "canonicalResources": ["Microsoft.Portal.Configuration"],
              "nativeResource": true,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.Portal.Configuration",
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
                  "name": "Microsoft.Portal.Configuration",
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
              "effectiveModel": "Microsoft.Portal.Configuration"
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
    "[\"Microsoft.Portal.TenantConfigurations.create\",{\"sourceFile\":\"TenantConfiguration.tsp\",\"line\":48,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [],
  "mappedNativePredicateIds": [],
  "ownerReports": [],
  "rawObservationIds": ["ConsistentResponseSchemaForPut:5"]
}
```

**Gap analysis and decision:** Identical 200/201 references were compared by resolved JavaScript object identity. Do not reproduce this bug or count its absence as a missing useful diagnostic.

<a id="s-20e9f2df566de610"></a>

## ConsistentResponseSchemaForPut: 20e9f2df566de610

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName}`; `projects/specification/portal/resource-manager/Microsoft.Portal/Portal/swagger/stable/2026-04-01/portal.json`.

**Observed:** 1 Swagger raw / 1 member check; 0 corresponding configured TypeSpec warnings; 0 corresponding selected callbacks before suppression; 0 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** confirmed-upstream-false-positive. **Classification:** upstream-identity-false-positive.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName}",
      "operationId": "Dashboards_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "./common.json#/definitions/Dashboard"
        },
        "reference": {
          "document": "projects/specification/portal/resource-manager/Microsoft.Portal/Portal/swagger/stable/2026-04-01/common.json",
          "pointer": ["definitions", "Dashboard"]
        },
        "topLevelResolvedSchemaSha256": "5aa0bac07846a5e785c9c4a7c461666b020d99ee0f036eaaab730edd4b21d02d",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "./common.json#/definitions/Dashboard"
          },
          "reference": {
            "document": "projects/specification/portal/resource-manager/Microsoft.Portal/Portal/swagger/stable/2026-04-01/common.json",
            "pointer": ["definitions", "Dashboard"]
          },
          "topLevelResolvedSchemaSha256": "5aa0bac07846a5e785c9c4a7c461666b020d99ee0f036eaaab730edd4b21d02d",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "./common.json#/definitions/Dashboard"
          },
          "reference": {
            "document": "projects/specification/portal/resource-manager/Microsoft.Portal/Portal/swagger/stable/2026-04-01/common.json",
            "pointer": ["definitions", "Dashboard"]
          },
          "topLevelResolvedSchemaSha256": "5aa0bac07846a5e785c9c4a7c461666b020d99ee0f036eaaab730edd4b21d02d",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.Portal.Dashboards.createOrUpdate",
      "sourceFile": "Dashboard.tsp",
      "line": 35,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.Portal.Dashboard",
          "kind": "Model",
          "declaration": {
            "sourceFile": "Dashboard.tsp",
            "line": 19,
            "column": 7
          },
          "registeredResource": true,
          "canonicalResources": ["Microsoft.Portal.Dashboard"],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.Portal.Dashboard",
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
              "name": "Microsoft.Portal.Dashboard",
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
          "name": "Microsoft.Portal.Dashboard",
          "kind": "Model",
          "declaration": {
            "sourceFile": "Dashboard.tsp",
            "line": 19,
            "column": 7
          },
          "registeredResource": true,
          "canonicalResources": ["Microsoft.Portal.Dashboard"],
          "nativeResource": true,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.Portal.Dashboard",
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
              "name": "Microsoft.Portal.Dashboard",
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
          "resource": "Microsoft.Portal.Dashboard",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.Portal.Dashboards.createOrUpdate\",{\"sourceFile\":\"Dashboard.tsp\",\"line\":35,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.Portal.Dashboard>",
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
                "model": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.Portal.Dashboard>",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.Portal.Dashboard>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.Portal.Dashboard",
              "kind": "Model",
              "declaration": {
                "sourceFile": "Dashboard.tsp",
                "line": 19,
                "column": 7
              },
              "registeredResource": true,
              "canonicalResources": ["Microsoft.Portal.Dashboard"],
              "nativeResource": true,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.Portal.Dashboard",
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
                  "name": "Microsoft.Portal.Dashboard",
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
              "effectiveModel": "Microsoft.Portal.Dashboard"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.Portal.Dashboard>",
            "kind": "Model",
            "declaration": {
              "sourceFile": "../../../../../node_modules/.pnpm/@azure-tools+typespec-azure_4e16f6958b689539320f5d6f4fdd0da2/node_modules/@azure-tools/typespec-azure-resource-manager/lib/responses.tsp",
              "line": 363,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.Portal.Dashboard>",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.Portal.Dashboard>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.Portal.Dashboard",
              "kind": "Model",
              "declaration": {
                "sourceFile": "Dashboard.tsp",
                "line": 19,
                "column": 7
              },
              "registeredResource": true,
              "canonicalResources": ["Microsoft.Portal.Dashboard"],
              "nativeResource": true,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.Portal.Dashboard",
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
                  "name": "Microsoft.Portal.Dashboard",
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
              "effectiveModel": "Microsoft.Portal.Dashboard"
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
    "[\"Microsoft.Portal.Dashboards.createOrUpdate\",{\"sourceFile\":\"Dashboard.tsp\",\"line\":35,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [],
  "mappedNativePredicateIds": [],
  "ownerReports": [],
  "rawObservationIds": ["ConsistentResponseSchemaForPut:4"]
}
```

**Gap analysis and decision:** Identical 200/201 references were compared by resolved JavaScript object identity. Do not reproduce this bug or count its absence as a missing useful diagnostic.

# specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry

[All project differences](../instance-correspondence.md#differing-projects).

<a id="s-32e3c2def02f5a05"></a>

## PutRequestResponseSchemeArm: 32e3c2def02f5a05

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/webhooks/{webhookName}`; `projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 corresponding selected callbacks before suppression; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/webhooks/{webhookName}",
      "operationId": "Webhooks_Create",
      "request": {
        "raw": {
          "$ref": "#/definitions/WebhookCreateParameters"
        },
        "reference": {
          "document": "projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json",
          "pointer": ["definitions", "WebhookCreateParameters"]
        },
        "topLevelResolvedSchemaSha256": "ce3b545a484c4c0094163b4e0e2030c76fd91463dbf6fb8008504b6940e037f5",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/Webhook"
          },
          "reference": {
            "document": "projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json",
            "pointer": ["definitions", "Webhook"]
          },
          "topLevelResolvedSchemaSha256": "8b97962c6eb801b42a5f1730348b2f3a24e559569591e05e58161ac4798cca9b",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/Webhook"
          },
          "reference": {
            "document": "projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json",
            "pointer": ["definitions", "Webhook"]
          },
          "topLevelResolvedSchemaSha256": "8b97962c6eb801b42a5f1730348b2f3a24e559569591e05e58161ac4798cca9b",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ContainerRegistry.Webhooks.create",
      "sourceFile": "Webhook.tsp",
      "line": 36,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/webhooks/{webhookName}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ContainerRegistry.WebhookCreateParameters",
          "kind": "Model",
          "declaration": {
            "sourceFile": "Webhook.models.tsp",
            "line": 58,
            "column": 7
          },
          "registeredResource": false,
          "canonicalResources": [],
          "nativeResource": false,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.ContainerRegistry.WebhookCreateParameters",
              "registered": false,
              "resourceBase": false,
              "customDeclaration": false
            }
          ],
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ContainerRegistry.WebhookCreateParameters",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.ContainerRegistry.WebhookCreateParameters",
          "kind": "Model",
          "declaration": {
            "sourceFile": "Webhook.models.tsp",
            "line": 58,
            "column": 7
          },
          "registeredResource": false,
          "canonicalResources": [],
          "nativeResource": false,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.ContainerRegistry.WebhookCreateParameters",
              "registered": false,
              "resourceBase": false,
              "customDeclaration": false
            }
          ],
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ContainerRegistry.WebhookCreateParameters",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.ContainerRegistry.Webhook",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ContainerRegistry.Webhooks.create\",{\"sourceFile\":\"Webhook.tsp\",\"line\":36,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ContainerRegistry.Webhook>",
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
                "model": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ContainerRegistry.Webhook>",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ContainerRegistry.Webhook>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ContainerRegistry.Webhook",
              "kind": "Model",
              "declaration": {
                "sourceFile": "Webhook.tsp",
                "line": 17,
                "column": 7
              },
              "registeredResource": true,
              "canonicalResources": ["Microsoft.ContainerRegistry.Webhook"],
              "nativeResource": true,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.ContainerRegistry.Webhook",
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
                  "name": "Microsoft.ContainerRegistry.Webhook",
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
              "effectiveModel": "Microsoft.ContainerRegistry.Webhook"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceCreatedResponse<Microsoft.ContainerRegistry.Webhook, { azureAsyncOperation: string, retryAfter: int32 }>",
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
                "model": "Azure.ResourceManager.ArmResourceCreatedResponse<Microsoft.ContainerRegistry.Webhook, { azureAsyncOperation: string, retryAfter: int32 }>",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceCreatedResponse<Microsoft.ContainerRegistry.Webhook, { azureAsyncOperation: string, retryAfter: int32 }>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ContainerRegistry.Webhook",
              "kind": "Model",
              "declaration": {
                "sourceFile": "Webhook.tsp",
                "line": 17,
                "column": 7
              },
              "registeredResource": true,
              "canonicalResources": ["Microsoft.ContainerRegistry.Webhook"],
              "nativeResource": true,
              "nativeResourceDeclarations": [
                {
                  "model": "Microsoft.ContainerRegistry.Webhook",
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
                  "name": "Microsoft.ContainerRegistry.Webhook",
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
              "effectiveModel": "Microsoft.ContainerRegistry.Webhook"
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
    "[\"Microsoft.ContainerRegistry.Webhooks.create\",{\"sourceFile\":\"Webhook.tsp\",\"line\":36,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry:1"
  ],
  "mappedNativePredicateIds": [
    "specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry:predicate:1"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:59"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

## Additional comparison: Microsoft.ContainerRegistry.ArchiveVersions.create

[Microsoft.ContainerRegistry.ArchiveVersions.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/ArchiveVersion.tsp#L84); **additional-missing-request-policy**.

```json
{
  "diagnostic": {
    "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
    "message": "ARM PUT operations must have a request body.",
    "targetKind": "Operation",
    "operationKey": "[\"Microsoft.ContainerRegistry.ArchiveVersions.create\",{\"sourceFile\":\"ArchiveVersion.tsp\",\"line\":84,\"column\":3}]",
    "sourceFile": "ArchiveVersion.tsp",
    "line": 84,
    "column": 3
  },
  "operation": {
    "operation": "Microsoft.ContainerRegistry.ArchiveVersions.create",
    "sourceFile": "ArchiveVersion.tsp",
    "line": 84,
    "verb": "put",
    "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/packages/{packageType}/archives/{archiveName}/versions/{archiveVersionName}",
    "request": {
      "bodyKind": "single",
      "type": {
        "name": "void",
        "kind": "Intrinsic",
        "declaration": {},
        "registeredResource": false,
        "canonicalResources": [],
        "nativeResource": false,
        "nativeResourceDeclarations": [],
        "void": true,
        "lineage": []
      },
      "effectiveType": {
        "name": "void",
        "kind": "Intrinsic",
        "declaration": {},
        "registeredResource": false,
        "canonicalResources": [],
        "nativeResource": false,
        "nativeResourceDeclarations": [],
        "void": true,
        "lineage": []
      },
      "void": true
    },
    "associations": [
      {
        "resource": "Microsoft.ContainerRegistry.ArchiveVersion",
        "group": "lists",
        "kind": "create",
        "operationKey": "[\"Microsoft.ContainerRegistry.ArchiveVersions.create\",{\"sourceFile\":\"ArchiveVersion.tsp\",\"line\":84,\"column\":3}]",
        "internal": false,
        "checkedResponseKind": "createOrUpdate",
        "checkedPutRequest": true
      }
    ],
    "responses": [
      {
        "statusCodes": 200,
        "type": {
          "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ContainerRegistry.ArchiveVersion>",
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
              "model": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ContainerRegistry.ArchiveVersion>",
              "registered": false,
              "resourceBase": false,
              "customDeclaration": false
            }
          ],
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ContainerRegistry.ArchiveVersion>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ContainerRegistry.ArchiveVersion",
            "kind": "Model",
            "declaration": {
              "sourceFile": "ArchiveVersion.tsp",
              "line": 63,
              "column": 7
            },
            "registeredResource": true,
            "canonicalResources": ["Microsoft.ContainerRegistry.ArchiveVersion"],
            "nativeResource": true,
            "nativeResourceDeclarations": [
              {
                "model": "Microsoft.ContainerRegistry.ArchiveVersion",
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
                "name": "Microsoft.ContainerRegistry.ArchiveVersion",
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
            "effectiveModel": "Microsoft.ContainerRegistry.ArchiveVersion"
          }
        ]
      },
      {
        "statusCodes": 201,
        "type": {
          "name": "Azure.ResourceManager.ArmResourceCreatedResponse<Microsoft.ContainerRegistry.ArchiveVersion, { azureAsyncOperation: string, retryAfter: int32 }>",
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
              "model": "Azure.ResourceManager.ArmResourceCreatedResponse<Microsoft.ContainerRegistry.ArchiveVersion, { azureAsyncOperation: string, retryAfter: int32 }>",
              "registered": false,
              "resourceBase": false,
              "customDeclaration": false
            }
          ],
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResourceCreatedResponse<Microsoft.ContainerRegistry.ArchiveVersion, { azureAsyncOperation: string, retryAfter: int32 }>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ContainerRegistry.ArchiveVersion",
            "kind": "Model",
            "declaration": {
              "sourceFile": "ArchiveVersion.tsp",
              "line": 63,
              "column": 7
            },
            "registeredResource": true,
            "canonicalResources": ["Microsoft.ContainerRegistry.ArchiveVersion"],
            "nativeResource": true,
            "nativeResourceDeclarations": [
              {
                "model": "Microsoft.ContainerRegistry.ArchiveVersion",
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
                "name": "Microsoft.ContainerRegistry.ArchiveVersion",
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
            "effectiveModel": "Microsoft.ContainerRegistry.ArchiveVersion"
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
  },
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ContainerRegistry.ArchiveVersions.create\",{\"sourceFile\":\"ArchiveVersion.tsp\",\"line\":84,\"column\":3}]"
  ],
  "emittedBindings": [
    {
      "document": "projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/packages/{packageType}/archives/{archiveName}/versions/{archiveVersionName}",
      "operations": [
        {
          "verb": "put",
          "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/packages/{packageType}/archives/{archiveName}/versions/{archiveVersionName}",
          "operationId": "ArchiveVersions_Create",
          "request": null,
          "responses": {
            "200": {
              "raw": {
                "$ref": "#/definitions/ArchiveVersion"
              },
              "reference": {
                "document": "projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json",
                "pointer": ["definitions", "ArchiveVersion"]
              },
              "topLevelResolvedSchemaSha256": "e8cb7a0109c6acae3fb0b2f65377eefbc04a93692b4a9ad50ab70c773b6b3d46",
              "xmsResourceInHierarchy": true
            },
            "201": {
              "raw": {
                "$ref": "#/definitions/ArchiveVersion"
              },
              "reference": {
                "document": "projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json",
                "pointer": ["definitions", "ArchiveVersion"]
              },
              "topLevelResolvedSchemaSha256": "e8cb7a0109c6acae3fb0b2f65377eefbc04a93692b4a9ad50ab70c773b6b3d46",
              "xmsResourceInHierarchy": true
            }
          }
        }
      ]
    }
  ]
}
```

**Gap analysis and decision:** Additional body-existence policy; the Swagger selector skips missing bodies. Review the wire contract rather than inventing a request for count parity.

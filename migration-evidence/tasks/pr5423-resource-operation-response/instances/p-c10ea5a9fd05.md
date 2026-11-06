# specification/dns/resource-manager/Microsoft.Network/Dns

[All project differences](../instance-correspondence.md#differing-projects).

## Additional comparison: Microsoft.Network.DnssecConfigs.createOrUpdate

[Microsoft.Network.DnssecConfigs.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/dns/resource-manager/Microsoft.Network/Dns/DnssecConfig.tsp#L45); **additional-missing-request-policy**.

```json
{
  "diagnostic": {
    "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
    "message": "ARM PUT operations must have a request body.",
    "targetKind": "Operation",
    "operationKey": "[\"Microsoft.Network.DnssecConfigs.createOrUpdate\",{\"sourceFile\":\"DnssecConfig.tsp\",\"line\":45,\"column\":3}]",
    "sourceFile": "DnssecConfig.tsp",
    "line": 45,
    "column": 3
  },
  "operation": {
    "operation": "Microsoft.Network.DnssecConfigs.createOrUpdate",
    "sourceFile": "DnssecConfig.tsp",
    "line": 45,
    "verb": "put",
    "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/dnssecConfigs/default",
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
        "resource": "Microsoft.Network.DnssecConfig",
        "group": "lifecycle",
        "kind": "createOrUpdate",
        "operationKey": "[\"Microsoft.Network.DnssecConfigs.createOrUpdate\",{\"sourceFile\":\"DnssecConfig.tsp\",\"line\":45,\"column\":3}]",
        "internal": false,
        "checkedResponseKind": "createOrUpdate",
        "checkedPutRequest": true
      }
    ],
    "responses": [
      {
        "statusCodes": 200,
        "type": {
          "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.Network.DnssecConfig>",
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
              "model": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.Network.DnssecConfig>",
              "registered": false,
              "resourceBase": false,
              "customDeclaration": false
            }
          ],
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.Network.DnssecConfig>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.Network.DnssecConfig",
            "kind": "Model",
            "declaration": {
              "sourceFile": "DnssecConfig.tsp",
              "line": 19,
              "column": 7
            },
            "registeredResource": true,
            "canonicalResources": ["Microsoft.Network.DnssecConfig"],
            "nativeResource": true,
            "nativeResourceDeclarations": [
              {
                "model": "Microsoft.Network.DnssecConfig",
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
                "name": "Microsoft.Network.DnssecConfig",
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
            "effectiveModel": "Microsoft.Network.DnssecConfig"
          }
        ]
      },
      {
        "statusCodes": 201,
        "type": {
          "name": "Azure.ResourceManager.ArmResourceCreatedResponse<Microsoft.Network.DnssecConfig, { location: string, retryAfter: int32 }>",
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
              "model": "Azure.ResourceManager.ArmResourceCreatedResponse<Microsoft.Network.DnssecConfig, { location: string, retryAfter: int32 }>",
              "registered": false,
              "resourceBase": false,
              "customDeclaration": false
            }
          ],
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResourceCreatedResponse<Microsoft.Network.DnssecConfig, { location: string, retryAfter: int32 }>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.Network.DnssecConfig",
            "kind": "Model",
            "declaration": {
              "sourceFile": "DnssecConfig.tsp",
              "line": 19,
              "column": 7
            },
            "registeredResource": true,
            "canonicalResources": ["Microsoft.Network.DnssecConfig"],
            "nativeResource": true,
            "nativeResourceDeclarations": [
              {
                "model": "Microsoft.Network.DnssecConfig",
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
                "name": "Microsoft.Network.DnssecConfig",
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
            "effectiveModel": "Microsoft.Network.DnssecConfig"
          }
        ]
      },
      {
        "statusCodes": "*",
        "type": {
          "name": "Microsoft.Network.CloudError",
          "kind": "Model",
          "declaration": {
            "sourceFile": "models.tsp",
            "line": 125,
            "column": 7
          },
          "registeredResource": false,
          "canonicalResources": [],
          "nativeResource": false,
          "nativeResourceDeclarations": [
            {
              "model": "Microsoft.Network.CloudError",
              "registered": false,
              "resourceBase": false,
              "customDeclaration": false
            }
          ],
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.Network.CloudError",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.Network.CloudError",
            "kind": "Model",
            "declaration": {
              "sourceFile": "models.tsp",
              "line": 125,
              "column": 7
            },
            "registeredResource": false,
            "canonicalResources": [],
            "nativeResource": false,
            "nativeResourceDeclarations": [
              {
                "model": "Microsoft.Network.CloudError",
                "registered": false,
                "resourceBase": false,
                "customDeclaration": false
              }
            ],
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.Network.CloudError",
                "discriminated": false
              }
            ],
            "effectiveModel": "Microsoft.Network.CloudError"
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
    "[\"Microsoft.Network.DnssecConfigs.createOrUpdate\",{\"sourceFile\":\"DnssecConfig.tsp\",\"line\":45,\"column\":3}]"
  ],
  "emittedBindings": [
    {
      "document": "projects/specification/dns/resource-manager/Microsoft.Network/Dns/swagger/preview/2023-07-01-preview/dns.json",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/dnssecConfigs/default",
      "operations": [
        {
          "verb": "put",
          "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/dnssecConfigs/default",
          "operationId": "DnssecConfigs_CreateOrUpdate",
          "request": null,
          "responses": {
            "200": {
              "raw": {
                "$ref": "#/definitions/DnssecConfig"
              },
              "reference": {
                "document": "projects/specification/dns/resource-manager/Microsoft.Network/Dns/swagger/preview/2023-07-01-preview/dns.json",
                "pointer": ["definitions", "DnssecConfig"]
              },
              "topLevelResolvedSchemaSha256": "20d71a11afa416dcaf693ec729b4b688654001fc1e71534097876d6855964bbb",
              "xmsResourceInHierarchy": true
            },
            "201": {
              "raw": {
                "$ref": "#/definitions/DnssecConfig"
              },
              "reference": {
                "document": "projects/specification/dns/resource-manager/Microsoft.Network/Dns/swagger/preview/2023-07-01-preview/dns.json",
                "pointer": ["definitions", "DnssecConfig"]
              },
              "topLevelResolvedSchemaSha256": "20d71a11afa416dcaf693ec729b4b688654001fc1e71534097876d6855964bbb",
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

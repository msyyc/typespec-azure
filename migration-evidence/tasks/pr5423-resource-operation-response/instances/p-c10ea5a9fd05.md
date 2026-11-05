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
        "registeredResource": false,
        "void": true,
        "lineage": []
      },
      "effectiveType": {
        "name": "void",
        "kind": "Intrinsic",
        "registeredResource": false,
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
          "registeredResource": false,
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
            "registeredResource": true,
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
          "registeredResource": false,
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
            "registeredResource": true,
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
          "registeredResource": false,
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
            "registeredResource": false,
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
    ]
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

# specification/domainservices/resource-manager/Microsoft.AAD/DomainServices

[All project differences](../instance-correspondence.md#differing-projects).

<a id="s-a8fe35091a27ad02"></a>

## PutRequestResponseSchemeArm: a8fe35091a27ad02

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AAD/domainServices/{domainServiceName}/ouContainer/{ouContainerName}`; `projects/specification/domainservices/resource-manager/Microsoft.AAD/DomainServices/swagger/preview/2026-08-31-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AAD/domainServices/{domainServiceName}/ouContainer/{ouContainerName}",
      "operationId": "OuContainer_Create",
      "request": {
        "raw": {
          "$ref": "#/definitions/ContainerAccount"
        },
        "reference": {
          "document": "projects/specification/domainservices/resource-manager/Microsoft.AAD/DomainServices/swagger/preview/2026-08-31-preview/openapi.json",
          "pointer": ["definitions", "ContainerAccount"]
        },
        "topLevelResolvedSchemaSha256": "2110526e5caa8ab50117d29e3a152bedd8eec2c5ee5ce5b93c873c1512178b96",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/OuContainer"
          },
          "reference": {
            "document": "projects/specification/domainservices/resource-manager/Microsoft.AAD/DomainServices/swagger/preview/2026-08-31-preview/openapi.json",
            "pointer": ["definitions", "OuContainer"]
          },
          "topLevelResolvedSchemaSha256": "2e089de284b2542638c0aa9217ae9b6eeb2d16f99b150841d086578b71971b27",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/OuContainer"
          },
          "reference": {
            "document": "projects/specification/domainservices/resource-manager/Microsoft.AAD/DomainServices/swagger/preview/2026-08-31-preview/openapi.json",
            "pointer": ["definitions", "OuContainer"]
          },
          "topLevelResolvedSchemaSha256": "2e089de284b2542638c0aa9217ae9b6eeb2d16f99b150841d086578b71971b27",
          "xmsResourceInHierarchy": true
        },
        "202": {
          "raw": {
            "$ref": "#/definitions/OuContainer"
          },
          "reference": {
            "document": "projects/specification/domainservices/resource-manager/Microsoft.AAD/DomainServices/swagger/preview/2026-08-31-preview/openapi.json",
            "pointer": ["definitions", "OuContainer"]
          },
          "topLevelResolvedSchemaSha256": "2e089de284b2542638c0aa9217ae9b6eeb2d16f99b150841d086578b71971b27",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.AAD.OuContainers.create",
      "sourceFile": "OuContainer.tsp",
      "line": 58,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AAD/domainServices/{domainServiceName}/ouContainer/{ouContainerName}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.AAD.ContainerAccount",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.AAD.ContainerAccount",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.AAD.ContainerAccount",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.AAD.ContainerAccount",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.AAD.OuContainer",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.AAD.OuContainers.create\",{\"sourceFile\":\"OuContainer.tsp\",\"line\":58,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.AAD.OuContainer>",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.AAD.OuContainer>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.AAD.OuContainer",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.AAD.OuContainer",
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
              "effectiveModel": "Microsoft.AAD.OuContainer"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceCreatedResponse<Microsoft.AAD.OuContainer, { location: string, retryAfter: int32 }>",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceCreatedResponse<Microsoft.AAD.OuContainer, { location: string, retryAfter: int32 }>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.AAD.OuContainer",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.AAD.OuContainer",
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
              "effectiveModel": "Microsoft.AAD.OuContainer"
            }
          ]
        },
        {
          "statusCodes": 202,
          "type": {
            "name": "{ statusCode: 202, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, retryAfter: int32, _: Microsoft.AAD.OuContainer }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 202, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, retryAfter: int32, _: Microsoft.AAD.OuContainer }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.AAD.OuContainer",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.AAD.OuContainer",
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
              "effectiveModel": "Microsoft.AAD.OuContainer"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Microsoft.AAD.CloudError",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.AAD.CloudError",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.AAD.CloudError",
              "kind": "Model",
              "registeredResource": false,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.AAD.CloudError",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Microsoft.AAD.CloudError"
            }
          ]
        }
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.AAD.OuContainers.create\",{\"sourceFile\":\"OuContainer.tsp\",\"line\":58,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/domainservices/resource-manager/Microsoft.AAD/DomainServices:0"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:94"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

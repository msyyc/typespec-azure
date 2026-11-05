# specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis

[All project differences](../instance-correspondence.md#differing-projects).

<a id="s-1eade2d50db1582c"></a>

## PutRequestResponseSchemeArm: 1eade2d50db1582c

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/services/{resourceName}/privateEndpointConnections/{privateEndpointConnectionName}`; `projects/specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis/swagger/preview/2025-04-01-preview/healthcare-apis.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/services/{resourceName}/privateEndpointConnections/{privateEndpointConnectionName}",
      "operationId": "PrivateEndpointConnections_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "../../../../../../../../../common-types/resource-management/v3/privatelinks.json#/definitions/PrivateEndpointConnection"
        },
        "reference": {
          "document": "common-types/resource-management/v3/privatelinks.json",
          "pointer": ["definitions", "PrivateEndpointConnection"]
        },
        "topLevelResolvedSchemaSha256": "8a39d4d7921fb05f241bb162785366a5acc1b3d93ffd4e1c8f09324388bb0cc6",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/PrivateEndpointConnectionDescription"
          },
          "reference": {
            "document": "projects/specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis/swagger/preview/2025-04-01-preview/healthcare-apis.json",
            "pointer": ["definitions", "PrivateEndpointConnectionDescription"]
          },
          "topLevelResolvedSchemaSha256": "dd4e738b997b5b594e5a00fe6b02f13d9d686cd9f202e7a6d0d7e41d61225ccb",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.HealthcareApis.PrivateEndpointConnectionDescriptions.createOrUpdate",
      "sourceFile": "PrivateEndpointConnectionDescription.tsp",
      "line": 69,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/services/{resourceName}/privateEndpointConnections/{privateEndpointConnectionName}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Azure.ResourceManager.CommonTypes.PrivateEndpointConnection",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.CommonTypes.PrivateEndpointConnection",
              "discriminated": false
            },
            {
              "name": "Azure.ResourceManager.CommonTypes.Resource",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Azure.ResourceManager.CommonTypes.PrivateEndpointConnection",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.CommonTypes.PrivateEndpointConnection",
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
          "resource": "Microsoft.HealthcareApis.PrivateEndpointConnectionDescription",
          "group": "registry",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.HealthcareApis.PrivateEndpointConnectionDescriptions.createOrUpdate\",{\"sourceFile\":\"PrivateEndpointConnectionDescription.tsp\",\"line\":69,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.HealthcareApis.PrivateEndpointConnectionDescription, location: string, retryAfter: int32 }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.HealthcareApis.PrivateEndpointConnectionDescription, location: string, retryAfter: int32 }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.HealthcareApis.PrivateEndpointConnectionDescription",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.HealthcareApis.PrivateEndpointConnectionDescription",
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
              "effectiveModel": "Microsoft.HealthcareApis.PrivateEndpointConnectionDescription"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Microsoft.HealthcareApis.ErrorDetails",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.HealthcareApis.ErrorDetails",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.HealthcareApis.ErrorDetails",
              "kind": "Model",
              "registeredResource": false,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.HealthcareApis.ErrorDetails",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Microsoft.HealthcareApis.ErrorDetails"
            }
          ]
        }
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.HealthcareApis.PrivateEndpointConnectionDescriptions.createOrUpdate\",{\"sourceFile\":\"PrivateEndpointConnectionDescription.tsp\",\"line\":69,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis:0"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:100"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

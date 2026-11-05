# specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement

[All project differences](../instance-correspondence.md#differing-projects).

<a id="s-d6c6d92c9a0f4dc9"></a>

## PutRequestResponseSchemeArm: d6c6d92c9a0f4dc9

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}",
      "operationId": "Api_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/ApiCreateOrUpdateParameter"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "ApiCreateOrUpdateParameter"]
        },
        "topLevelResolvedSchemaSha256": "363605794ce5370a178f9ed0d30b028292c451ca4d96ed2df4ea97d35343ef03",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/ApiContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "ApiContract"]
          },
          "topLevelResolvedSchemaSha256": "a5dcb74389d6fd3f5b41c9be3b1847f5a22cbc55ec5ae8ba1f8abb27a871eff3",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/ApiContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "ApiContract"]
          },
          "topLevelResolvedSchemaSha256": "a5dcb74389d6fd3f5b41c9be3b1847f5a22cbc55ec5ae8ba1f8abb27a871eff3",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.ApiContracts.createOrUpdate",
      "sourceFile": "ApiContract.tsp",
      "line": 93,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.ApiCreateOrUpdateParameter",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.ApiCreateOrUpdateParameter",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.ApiManagement.ApiCreateOrUpdateParameter",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.ApiCreateOrUpdateParameter",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.ApiManagement.ApiContract",
          "group": "registry",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.ApiContracts.createOrUpdate\",{\"sourceFile\":\"ApiContract.tsp\",\"line\":93,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.ApiManagement.ApiContract, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.ApiManagement.ApiContract, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.ApiContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.ApiContract",
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
              "effectiveModel": "Microsoft.ApiManagement.ApiContract"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "{ statusCode: 201, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, body: Microsoft.ApiManagement.ApiContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 201, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, body: Microsoft.ApiManagement.ApiContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.ApiContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.ApiContract",
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
              "effectiveModel": "Microsoft.ApiManagement.ApiContract"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.ApiContracts.createOrUpdate\",{\"sourceFile\":\"ApiContract.tsp\",\"line\":93,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement:0"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:0"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-a0043bfa2f35690b"></a>

## PutRequestResponseSchemeArm: a0043bfa2f35690b

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/tagDescriptions/{tagDescriptionId}`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/tagDescriptions/{tagDescriptionId}",
      "operationId": "ApiTagDescription_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/TagDescriptionCreateParameters"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "TagDescriptionCreateParameters"]
        },
        "topLevelResolvedSchemaSha256": "9c0cb49ed5c5e448a07c79805376082884f3f13e0acbf54542f05554bdc9a986",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/TagDescriptionContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "TagDescriptionContract"]
          },
          "topLevelResolvedSchemaSha256": "4d8cb28b326ff5d4e2d2faf013368db0b1ef964f7cfae31ec2390e578598dda8",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/TagDescriptionContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "TagDescriptionContract"]
          },
          "topLevelResolvedSchemaSha256": "4d8cb28b326ff5d4e2d2faf013368db0b1ef964f7cfae31ec2390e578598dda8",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.TagDescriptionContracts.createOrUpdate",
      "sourceFile": "TagDescriptionContract.tsp",
      "line": 102,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/tagDescriptions/{tagDescriptionId}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.TagDescriptionCreateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.TagDescriptionCreateParameters",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.ApiManagement.TagDescriptionCreateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.TagDescriptionCreateParameters",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.ApiManagement.TagDescriptionContract",
          "group": "lists",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.TagDescriptionContracts.createOrUpdate\",{\"sourceFile\":\"TagDescriptionContract.tsp\",\"line\":102,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.ApiManagement.TagDescriptionContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.ApiManagement.TagDescriptionContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.TagDescriptionContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.TagDescriptionContract",
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
              "effectiveModel": "Microsoft.ApiManagement.TagDescriptionContract"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "{ statusCode: 201, retryAfter: int32, body: Microsoft.ApiManagement.TagDescriptionContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 201, retryAfter: int32, body: Microsoft.ApiManagement.TagDescriptionContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.TagDescriptionContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.TagDescriptionContract",
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
              "effectiveModel": "Microsoft.ApiManagement.TagDescriptionContract"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.TagDescriptionContracts.createOrUpdate\",{\"sourceFile\":\"TagDescriptionContract.tsp\",\"line\":102,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement:9"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:1"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-07a4fba5ab458883"></a>

## PutRequestResponseSchemeArm: 07a4fba5ab458883

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/certificates/{certificateId}`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/certificates/{certificateId}",
      "operationId": "Certificate_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/CertificateCreateOrUpdateParameters"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "CertificateCreateOrUpdateParameters"]
        },
        "topLevelResolvedSchemaSha256": "7af06c99db4f6c497a09278c2a736f7f716de8a4d6226f0d4ed89d8c729969eb",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/CertificateContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "CertificateContract"]
          },
          "topLevelResolvedSchemaSha256": "a3a0b842e4c4b9e2d06e0c8d2eb6decc0a08c994c491718e26f8e15f59956cff",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/CertificateContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "CertificateContract"]
          },
          "topLevelResolvedSchemaSha256": "a3a0b842e4c4b9e2d06e0c8d2eb6decc0a08c994c491718e26f8e15f59956cff",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.CertificateContracts.createOrUpdate",
      "sourceFile": "CertificateContract.tsp",
      "line": 97,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/certificates/{certificateId}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.CertificateCreateOrUpdateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.CertificateCreateOrUpdateParameters",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.ApiManagement.CertificateCreateOrUpdateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.CertificateCreateOrUpdateParameters",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.ApiManagement.CertificateContract",
          "group": "registry",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.CertificateContracts.createOrUpdate\",{\"sourceFile\":\"CertificateContract.tsp\",\"line\":97,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.ApiManagement.CertificateContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.ApiManagement.CertificateContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.CertificateContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.CertificateContract",
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
              "effectiveModel": "Microsoft.ApiManagement.CertificateContract"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "{ statusCode: 201, body: Microsoft.ApiManagement.CertificateContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 201, body: Microsoft.ApiManagement.CertificateContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.CertificateContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.CertificateContract",
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
              "effectiveModel": "Microsoft.ApiManagement.CertificateContract"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.CertificateContracts.createOrUpdate\",{\"sourceFile\":\"CertificateContract.tsp\",\"line\":97,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement:10"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:2"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-4f6894b5bb1a95e3"></a>

## PutRequestResponseSchemeArm: 4f6894b5bb1a95e3

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/gateways/{gatewayId}/apis/{apiId}`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 0 corresponding configured TypeSpec warnings; 0 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** unpaired-required-investigation-or-modeling. **Classification:** missed-request-outside-lifecycle-map.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/gateways/{gatewayId}/apis/{apiId}",
      "operationId": "GatewayApi_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/AssociationContract"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "AssociationContract"]
        },
        "topLevelResolvedSchemaSha256": "c75d4d19d10c66b594cf9796278689071f772965d934455e095e5cdaeef895fd",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/ApiContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "ApiContract"]
          },
          "topLevelResolvedSchemaSha256": "a5dcb74389d6fd3f5b41c9be3b1847f5a22cbc55ec5ae8ba1f8abb27a871eff3",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/ApiContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "ApiContract"]
          },
          "topLevelResolvedSchemaSha256": "a5dcb74389d6fd3f5b41c9be3b1847f5a22cbc55ec5ae8ba1f8abb27a871eff3",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.GatewayContracts.gatewayApiCreateOrUpdate",
      "sourceFile": "GatewayContract.tsp",
      "line": 320,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/gateways/{gatewayId}/apis/{apiId}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.AssociationContract",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.AssociationContract",
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
          "name": "Microsoft.ApiManagement.AssociationContract",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.AssociationContract",
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
          "resource": "Microsoft.ApiManagement.GatewayContract",
          "group": "lists",
          "kind": "gatewayApiCreateOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.GatewayContracts.gatewayApiCreateOrUpdate\",{\"sourceFile\":\"GatewayContract.tsp\",\"line\":320,\"column\":3}]",
          "internal": false,
          "checkedPutRequest": false
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "Azure.ResourceManager.ArmResponse<Microsoft.ApiManagement.ApiContract>",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResponse<Microsoft.ApiManagement.ApiContract>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.ApiContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.ApiContract",
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
              "effectiveModel": "Microsoft.ApiManagement.ApiContract"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.ApiContract>",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.ApiContract>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.ApiContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.ApiContract",
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
              "effectiveModel": "Microsoft.ApiManagement.ApiContract"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.GatewayContracts.gatewayApiCreateOrUpdate\",{\"sourceFile\":\"GatewayContract.tsp\",\"line\":320,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:3"]
}
```

**Gap analysis and decision:** Gateway API association and storage migration use command/association inputs rather than the parent resource model. GatewayApi is registered as action, has a different ApiContract response and explicitly suppresses the current ARM rule. Do not compare its input to the Gateway parent simply because its verb is PUT. Review API design and justified exceptions separately rather than widening this resource listener.

<a id="s-a24e9f05205ca77e"></a>

## PutRequestResponseSchemeArm: a24e9f05205ca77e

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/groups/{groupId}`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/groups/{groupId}",
      "operationId": "Group_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/GroupCreateParameters"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "GroupCreateParameters"]
        },
        "topLevelResolvedSchemaSha256": "15b2324645f4d9e2302640f032b43b5e17bfba1eafe43ab46059fec1c71b8687",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/GroupContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "GroupContract"]
          },
          "topLevelResolvedSchemaSha256": "71477ed63f310d12c08eb6ba518429cd169eeaa2ad808f4aaa89e6c77eec84a4",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/GroupContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "GroupContract"]
          },
          "topLevelResolvedSchemaSha256": "71477ed63f310d12c08eb6ba518429cd169eeaa2ad808f4aaa89e6c77eec84a4",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.GroupContracts.createOrUpdate",
      "sourceFile": "GroupContract.tsp",
      "line": 188,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/groups/{groupId}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.GroupCreateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.GroupCreateParameters",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.ApiManagement.GroupCreateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.GroupCreateParameters",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.ApiManagement.GroupContract",
          "group": "registry",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.GroupContracts.createOrUpdate\",{\"sourceFile\":\"GroupContract.tsp\",\"line\":188,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.ApiManagement.GroupContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.ApiManagement.GroupContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.GroupContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.GroupContract",
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
              "effectiveModel": "Microsoft.ApiManagement.GroupContract"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "{ statusCode: 201, retryAfter: int32, body: Microsoft.ApiManagement.GroupContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 201, retryAfter: int32, body: Microsoft.ApiManagement.GroupContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.GroupContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.GroupContract",
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
              "effectiveModel": "Microsoft.ApiManagement.GroupContract"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.GroupContracts.createOrUpdate\",{\"sourceFile\":\"GroupContract.tsp\",\"line\":188,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement:13"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:4"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-16bb019f51c54666"></a>

## PutRequestResponseSchemeArm: 16bb019f51c54666

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/identityProviders/{identityProviderName}`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/identityProviders/{identityProviderName}",
      "operationId": "IdentityProvider_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/IdentityProviderCreateContract"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "IdentityProviderCreateContract"]
        },
        "topLevelResolvedSchemaSha256": "fee055e105411534b714116546e0fc8e7f0f8f44894675e9cd66fd64908c430a",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/IdentityProviderContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "IdentityProviderContract"]
          },
          "topLevelResolvedSchemaSha256": "752c4e97fed2eb4a968413b88c612a6cba26058aefcd9e60f3d782ba4e959f11",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/IdentityProviderContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "IdentityProviderContract"]
          },
          "topLevelResolvedSchemaSha256": "752c4e97fed2eb4a968413b88c612a6cba26058aefcd9e60f3d782ba4e959f11",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.IdentityProviderContracts.createOrUpdate",
      "sourceFile": "IdentityProviderContract.tsp",
      "line": 62,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/identityProviders/{identityProviderName}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.IdentityProviderCreateContract",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.IdentityProviderCreateContract",
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
          "name": "Microsoft.ApiManagement.IdentityProviderCreateContract",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.IdentityProviderCreateContract",
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
          "resource": "Microsoft.ApiManagement.IdentityProviderContract",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.IdentityProviderContracts.createOrUpdate\",{\"sourceFile\":\"IdentityProviderContract.tsp\",\"line\":62,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.ApiManagement.IdentityProviderContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.ApiManagement.IdentityProviderContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.IdentityProviderContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.IdentityProviderContract",
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
              "effectiveModel": "Microsoft.ApiManagement.IdentityProviderContract"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "{ statusCode: 201, body: Microsoft.ApiManagement.IdentityProviderContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 201, body: Microsoft.ApiManagement.IdentityProviderContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.IdentityProviderContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.IdentityProviderContract",
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
              "effectiveModel": "Microsoft.ApiManagement.IdentityProviderContract"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.IdentityProviderContracts.createOrUpdate\",{\"sourceFile\":\"IdentityProviderContract.tsp\",\"line\":62,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement:18"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:5"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-4074356758b8b55a"></a>

## PutRequestResponseSchemeArm: 4074356758b8b55a

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/namedValues/{namedValueId}`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/namedValues/{namedValueId}",
      "operationId": "NamedValue_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/NamedValueCreateContract"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "NamedValueCreateContract"]
        },
        "topLevelResolvedSchemaSha256": "c62c8ddb5d21bb8970a1262e4c9ee44e990bd4cee515955f19d317028149cdbd",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/NamedValueContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "NamedValueContract"]
          },
          "topLevelResolvedSchemaSha256": "b77d1f749674db0eaa88fd588704564590c491b5b7694bc359cc5aade8eb1d1c",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/NamedValueContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "NamedValueContract"]
          },
          "topLevelResolvedSchemaSha256": "b77d1f749674db0eaa88fd588704564590c491b5b7694bc359cc5aade8eb1d1c",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.NamedValueContracts.createOrUpdate",
      "sourceFile": "NamedValueContract.tsp",
      "line": 91,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/namedValues/{namedValueId}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.NamedValueCreateContract",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.NamedValueCreateContract",
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
          "name": "Microsoft.ApiManagement.NamedValueCreateContract",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.NamedValueCreateContract",
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
          "resource": "Microsoft.ApiManagement.NamedValueContract",
          "group": "registry",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.NamedValueContracts.createOrUpdate\",{\"sourceFile\":\"NamedValueContract.tsp\",\"line\":91,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.ApiManagement.NamedValueContract, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.ApiManagement.NamedValueContract, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.NamedValueContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.NamedValueContract",
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
              "effectiveModel": "Microsoft.ApiManagement.NamedValueContract"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "{ statusCode: 201, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, body: Microsoft.ApiManagement.NamedValueContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 201, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, body: Microsoft.ApiManagement.NamedValueContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.NamedValueContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.NamedValueContract",
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
              "effectiveModel": "Microsoft.ApiManagement.NamedValueContract"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.NamedValueContracts.createOrUpdate\",{\"sourceFile\":\"NamedValueContract.tsp\",\"line\":91,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement:19"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:6"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-e7a795042777d9cf"></a>

## PutGetPatchResponseSchema: e7a795042777d9cf

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/delegation`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 0 corresponding configured TypeSpec warnings; 0 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** recommended-non-porting-not-approved. **Classification:** missed-cross-operation-selected-ref-absent.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/delegation",
      "operationId": "DelegationSettings_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/PortalDelegationSettings"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "PortalDelegationSettings"]
        },
        "topLevelResolvedSchemaSha256": "f8b5aca2019b38741e106b6f6d93dc5ec8b0f6e32f010e6f28b6c80c83a0ed4f",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/PortalDelegationSettings"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "PortalDelegationSettings"]
          },
          "topLevelResolvedSchemaSha256": "f8b5aca2019b38741e106b6f6d93dc5ec8b0f6e32f010e6f28b6c80c83a0ed4f",
          "xmsResourceInHierarchy": true
        }
      }
    },
    {
      "verb": "get",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/delegation",
      "operationId": "DelegationSettings_Get",
      "request": null,
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/PortalDelegationSettings"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "PortalDelegationSettings"]
          },
          "topLevelResolvedSchemaSha256": "f8b5aca2019b38741e106b6f6d93dc5ec8b0f6e32f010e6f28b6c80c83a0ed4f",
          "xmsResourceInHierarchy": true
        }
      }
    },
    {
      "verb": "patch",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/delegation",
      "operationId": "DelegationSettings_Update",
      "request": {
        "raw": {
          "$ref": "#/definitions/PortalDelegationSettings"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "PortalDelegationSettings"]
        },
        "topLevelResolvedSchemaSha256": "f8b5aca2019b38741e106b6f6d93dc5ec8b0f6e32f010e6f28b6c80c83a0ed4f",
        "xmsResourceInHierarchy": true
      },
      "responses": {}
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.DelegationSettings.createOrUpdate",
      "sourceFile": "PortalDelegationSettings.tsp",
      "line": 67,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/delegation",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.PortalDelegationSettings",
          "kind": "Model",
          "registeredResource": true,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.PortalDelegationSettings",
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
          "name": "Microsoft.ApiManagement.PortalDelegationSettings",
          "kind": "Model",
          "registeredResource": true,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.PortalDelegationSettings",
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
          "resource": "Microsoft.ApiManagement.PortalDelegationSettings",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.DelegationSettings.createOrUpdate\",{\"sourceFile\":\"PortalDelegationSettings.tsp\",\"line\":67,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ApiManagement.PortalDelegationSettings>",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ApiManagement.PortalDelegationSettings>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.PortalDelegationSettings",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.PortalDelegationSettings",
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
              "effectiveModel": "Microsoft.ApiManagement.PortalDelegationSettings"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    },
    {
      "operation": "Microsoft.ApiManagement.DelegationSettings.get",
      "sourceFile": "PortalDelegationSettings.tsp",
      "line": 36,
      "verb": "get",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/delegation",
      "associations": [
        {
          "resource": "Microsoft.ApiManagement.PortalDelegationSettings",
          "group": "lifecycle",
          "kind": "read",
          "operationKey": "[\"Microsoft.ApiManagement.DelegationSettings.get\",{\"sourceFile\":\"PortalDelegationSettings.tsp\",\"line\":36,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "read",
          "checkedPutRequest": false
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.ApiManagement.PortalDelegationSettings, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.ApiManagement.PortalDelegationSettings, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.PortalDelegationSettings",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.PortalDelegationSettings",
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
              "effectiveModel": "Microsoft.ApiManagement.PortalDelegationSettings"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    },
    {
      "operation": "Microsoft.ApiManagement.DelegationSettings.update",
      "sourceFile": "PortalDelegationSettings.tsp",
      "line": 85,
      "verb": "patch",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/delegation",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.PortalDelegationSettings",
          "kind": "Model",
          "registeredResource": true,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.PortalDelegationSettings",
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
          "name": "Microsoft.ApiManagement.PortalDelegationSettings",
          "kind": "Model",
          "registeredResource": true,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.PortalDelegationSettings",
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
          "resource": "Microsoft.ApiManagement.PortalDelegationSettings",
          "group": "lifecycle",
          "kind": "update",
          "operationKey": "[\"Microsoft.ApiManagement.DelegationSettings.update\",{\"sourceFile\":\"PortalDelegationSettings.tsp\",\"line\":85,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "update",
          "checkedPutRequest": false
        }
      ],
      "responses": [
        {
          "statusCodes": 204,
          "type": {
            "name": "Azure.ResourceManager.ArmNoContentResponse<\"Operation completed successfully.\">",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmNoContentResponse<\"Operation completed successfully.\">",
                "discriminated": false
              }
            ]
          },
          "bodies": [null]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.DelegationSettings.createOrUpdate\",{\"sourceFile\":\"PortalDelegationSettings.tsp\",\"line\":67,\"column\":3}]",
    "[\"Microsoft.ApiManagement.DelegationSettings.get\",{\"sourceFile\":\"PortalDelegationSettings.tsp\",\"line\":36,\"column\":3}]",
    "[\"Microsoft.ApiManagement.DelegationSettings.update\",{\"sourceFile\":\"PortalDelegationSettings.tsp\",\"line\":85,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [],
  "ownerReports": [],
  "rawObservationIds": ["PutGetPatchResponseSchema:0"]
}
```

**Gap analysis and decision:** The comparison treats a correctly bodyless 202 or 204 as an unequal resource schema. Do not invent a response body or add a resource-schema warning merely to match that result. This does not establish that the operation's status set is ARM-compliant: arm-put-response-codes owns that separate question. This is a recommended intentional difference, not approved retirement or existing migration credit.

<a id="s-e0504c2667af2c28"></a>

## PutGetPatchResponseSchema: e0504c2667af2c28

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signin`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 0 corresponding configured TypeSpec warnings; 0 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** recommended-non-porting-not-approved. **Classification:** missed-cross-operation-selected-ref-absent.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signin",
      "operationId": "SignInSettings_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/PortalSigninSettings"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "PortalSigninSettings"]
        },
        "topLevelResolvedSchemaSha256": "652a78e3d1698ba569dece0962600d6c08ea8b56d0dfa14f4d642fe0ce6c89eb",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/PortalSigninSettings"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "PortalSigninSettings"]
          },
          "topLevelResolvedSchemaSha256": "652a78e3d1698ba569dece0962600d6c08ea8b56d0dfa14f4d642fe0ce6c89eb",
          "xmsResourceInHierarchy": true
        }
      }
    },
    {
      "verb": "get",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signin",
      "operationId": "SignInSettings_Get",
      "request": null,
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/PortalSigninSettings"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "PortalSigninSettings"]
          },
          "topLevelResolvedSchemaSha256": "652a78e3d1698ba569dece0962600d6c08ea8b56d0dfa14f4d642fe0ce6c89eb",
          "xmsResourceInHierarchy": true
        }
      }
    },
    {
      "verb": "patch",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signin",
      "operationId": "SignInSettings_Update",
      "request": {
        "raw": {
          "$ref": "#/definitions/PortalSigninSettings"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "PortalSigninSettings"]
        },
        "topLevelResolvedSchemaSha256": "652a78e3d1698ba569dece0962600d6c08ea8b56d0dfa14f4d642fe0ce6c89eb",
        "xmsResourceInHierarchy": true
      },
      "responses": {}
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.SignInSettings.createOrUpdate",
      "sourceFile": "PortalSigninSettings.tsp",
      "line": 67,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signin",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.PortalSigninSettings",
          "kind": "Model",
          "registeredResource": true,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.PortalSigninSettings",
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
          "name": "Microsoft.ApiManagement.PortalSigninSettings",
          "kind": "Model",
          "registeredResource": true,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.PortalSigninSettings",
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
          "resource": "Microsoft.ApiManagement.PortalSigninSettings",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.SignInSettings.createOrUpdate\",{\"sourceFile\":\"PortalSigninSettings.tsp\",\"line\":67,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ApiManagement.PortalSigninSettings>",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ApiManagement.PortalSigninSettings>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.PortalSigninSettings",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.PortalSigninSettings",
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
              "effectiveModel": "Microsoft.ApiManagement.PortalSigninSettings"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    },
    {
      "operation": "Microsoft.ApiManagement.SignInSettings.get",
      "sourceFile": "PortalSigninSettings.tsp",
      "line": 36,
      "verb": "get",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signin",
      "associations": [
        {
          "resource": "Microsoft.ApiManagement.PortalSigninSettings",
          "group": "lifecycle",
          "kind": "read",
          "operationKey": "[\"Microsoft.ApiManagement.SignInSettings.get\",{\"sourceFile\":\"PortalSigninSettings.tsp\",\"line\":36,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "read",
          "checkedPutRequest": false
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.ApiManagement.PortalSigninSettings, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.ApiManagement.PortalSigninSettings, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.PortalSigninSettings",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.PortalSigninSettings",
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
              "effectiveModel": "Microsoft.ApiManagement.PortalSigninSettings"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    },
    {
      "operation": "Microsoft.ApiManagement.SignInSettings.update",
      "sourceFile": "PortalSigninSettings.tsp",
      "line": 85,
      "verb": "patch",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signin",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.PortalSigninSettings",
          "kind": "Model",
          "registeredResource": true,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.PortalSigninSettings",
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
          "name": "Microsoft.ApiManagement.PortalSigninSettings",
          "kind": "Model",
          "registeredResource": true,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.PortalSigninSettings",
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
          "resource": "Microsoft.ApiManagement.PortalSigninSettings",
          "group": "lifecycle",
          "kind": "update",
          "operationKey": "[\"Microsoft.ApiManagement.SignInSettings.update\",{\"sourceFile\":\"PortalSigninSettings.tsp\",\"line\":85,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "update",
          "checkedPutRequest": false
        }
      ],
      "responses": [
        {
          "statusCodes": 204,
          "type": {
            "name": "Azure.ResourceManager.ArmNoContentResponse<\"Operation completed successfully.\">",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmNoContentResponse<\"Operation completed successfully.\">",
                "discriminated": false
              }
            ]
          },
          "bodies": [null]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.SignInSettings.createOrUpdate\",{\"sourceFile\":\"PortalSigninSettings.tsp\",\"line\":67,\"column\":3}]",
    "[\"Microsoft.ApiManagement.SignInSettings.get\",{\"sourceFile\":\"PortalSigninSettings.tsp\",\"line\":36,\"column\":3}]",
    "[\"Microsoft.ApiManagement.SignInSettings.update\",{\"sourceFile\":\"PortalSigninSettings.tsp\",\"line\":85,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [],
  "ownerReports": [],
  "rawObservationIds": ["PutGetPatchResponseSchema:1"]
}
```

**Gap analysis and decision:** The comparison treats a correctly bodyless 202 or 204 as an unequal resource schema. Do not invent a response body or add a resource-schema warning merely to match that result. This does not establish that the operation's status set is ARM-compliant: arm-put-response-codes owns that separate question. This is a recommended intentional difference, not approved retirement or existing migration credit.

<a id="s-86196a233810a562"></a>

## PutGetPatchResponseSchema: 86196a233810a562

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signup`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 0 corresponding configured TypeSpec warnings; 0 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** recommended-non-porting-not-approved. **Classification:** missed-cross-operation-selected-ref-absent.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signup",
      "operationId": "SignUpSettings_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/PortalSignupSettings"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "PortalSignupSettings"]
        },
        "topLevelResolvedSchemaSha256": "3e2d80aa07c389afe12a623c2ae8b247295d51eda3577d593a1097704dbb020b",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/PortalSignupSettings"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "PortalSignupSettings"]
          },
          "topLevelResolvedSchemaSha256": "3e2d80aa07c389afe12a623c2ae8b247295d51eda3577d593a1097704dbb020b",
          "xmsResourceInHierarchy": true
        }
      }
    },
    {
      "verb": "get",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signup",
      "operationId": "SignUpSettings_Get",
      "request": null,
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/PortalSignupSettings"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "PortalSignupSettings"]
          },
          "topLevelResolvedSchemaSha256": "3e2d80aa07c389afe12a623c2ae8b247295d51eda3577d593a1097704dbb020b",
          "xmsResourceInHierarchy": true
        }
      }
    },
    {
      "verb": "patch",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signup",
      "operationId": "SignUpSettings_Update",
      "request": {
        "raw": {
          "$ref": "#/definitions/PortalSignupSettings"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "PortalSignupSettings"]
        },
        "topLevelResolvedSchemaSha256": "3e2d80aa07c389afe12a623c2ae8b247295d51eda3577d593a1097704dbb020b",
        "xmsResourceInHierarchy": true
      },
      "responses": {}
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.SignUpSettings.createOrUpdate",
      "sourceFile": "PortalSignupSettings.tsp",
      "line": 67,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signup",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.PortalSignupSettings",
          "kind": "Model",
          "registeredResource": true,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.PortalSignupSettings",
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
          "name": "Microsoft.ApiManagement.PortalSignupSettings",
          "kind": "Model",
          "registeredResource": true,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.PortalSignupSettings",
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
          "resource": "Microsoft.ApiManagement.PortalSignupSettings",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.SignUpSettings.createOrUpdate\",{\"sourceFile\":\"PortalSignupSettings.tsp\",\"line\":67,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ApiManagement.PortalSignupSettings>",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ApiManagement.PortalSignupSettings>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.PortalSignupSettings",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.PortalSignupSettings",
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
              "effectiveModel": "Microsoft.ApiManagement.PortalSignupSettings"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    },
    {
      "operation": "Microsoft.ApiManagement.SignUpSettings.get",
      "sourceFile": "PortalSignupSettings.tsp",
      "line": 36,
      "verb": "get",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signup",
      "associations": [
        {
          "resource": "Microsoft.ApiManagement.PortalSignupSettings",
          "group": "lifecycle",
          "kind": "read",
          "operationKey": "[\"Microsoft.ApiManagement.SignUpSettings.get\",{\"sourceFile\":\"PortalSignupSettings.tsp\",\"line\":36,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "read",
          "checkedPutRequest": false
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.ApiManagement.PortalSignupSettings, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.ApiManagement.PortalSignupSettings, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.PortalSignupSettings",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.PortalSignupSettings",
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
              "effectiveModel": "Microsoft.ApiManagement.PortalSignupSettings"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    },
    {
      "operation": "Microsoft.ApiManagement.SignUpSettings.update",
      "sourceFile": "PortalSignupSettings.tsp",
      "line": 85,
      "verb": "patch",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signup",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.PortalSignupSettings",
          "kind": "Model",
          "registeredResource": true,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.PortalSignupSettings",
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
          "name": "Microsoft.ApiManagement.PortalSignupSettings",
          "kind": "Model",
          "registeredResource": true,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.PortalSignupSettings",
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
          "resource": "Microsoft.ApiManagement.PortalSignupSettings",
          "group": "lifecycle",
          "kind": "update",
          "operationKey": "[\"Microsoft.ApiManagement.SignUpSettings.update\",{\"sourceFile\":\"PortalSignupSettings.tsp\",\"line\":85,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "update",
          "checkedPutRequest": false
        }
      ],
      "responses": [
        {
          "statusCodes": 204,
          "type": {
            "name": "Azure.ResourceManager.ArmNoContentResponse<\"Operation completed successfully.\">",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmNoContentResponse<\"Operation completed successfully.\">",
                "discriminated": false
              }
            ]
          },
          "bodies": [null]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.SignUpSettings.createOrUpdate\",{\"sourceFile\":\"PortalSignupSettings.tsp\",\"line\":67,\"column\":3}]",
    "[\"Microsoft.ApiManagement.SignUpSettings.get\",{\"sourceFile\":\"PortalSignupSettings.tsp\",\"line\":36,\"column\":3}]",
    "[\"Microsoft.ApiManagement.SignUpSettings.update\",{\"sourceFile\":\"PortalSignupSettings.tsp\",\"line\":85,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [],
  "ownerReports": [],
  "rawObservationIds": ["PutGetPatchResponseSchema:2"]
}
```

**Gap analysis and decision:** The comparison treats a correctly bodyless 202 or 204 as an unequal resource schema. Do not invent a response body or add a resource-schema warning merely to match that result. This does not establish that the operation's status set is ARM-compliant: arm-put-response-codes owns that separate question. This is a recommended intentional difference, not approved retirement or existing migration credit.

<a id="s-9eca5628f4dd299e"></a>

## PutRequestResponseSchemeArm: 9eca5628f4dd299e

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/privateEndpointConnections/{privateEndpointConnectionName}`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 0 corresponding configured TypeSpec warnings; 2 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** unpaired-required-investigation-or-modeling. **Classification:** same-operation-different-comparison.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/privateEndpointConnections/{privateEndpointConnectionName}",
      "operationId": "PrivateEndpointConnection_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/PrivateEndpointConnectionRequest"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "PrivateEndpointConnectionRequest"]
        },
        "topLevelResolvedSchemaSha256": "8d06d27e4977a7598c6af81e5eda9a79a02f437aad43f29a94148711b442e8c8",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "../../../../../../../../../common-types/resource-management/v5/privatelinks.json#/definitions/PrivateEndpointConnection"
          },
          "reference": {
            "document": "common-types/resource-management/v5/privatelinks.json",
            "pointer": ["definitions", "PrivateEndpointConnection"]
          },
          "topLevelResolvedSchemaSha256": "1bb5749af0cd09d5f1ab36343be59e60b1cb653ee1e10886d2ae9150137f47a1",
          "xmsResourceInHierarchy": true
        },
        "202": null
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate",
      "sourceFile": "PrivateEndpointConnection.tsp",
      "line": 29,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/privateEndpointConnections/{privateEndpointConnectionName}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.PrivateEndpointConnectionRequest",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.PrivateEndpointConnectionRequest",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.ApiManagement.PrivateEndpointConnectionRequest",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.PrivateEndpointConnectionRequest",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.ApiManagement.ApiManagementServiceResource",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate\",{\"sourceFile\":\"PrivateEndpointConnection.tsp\",\"line\":29,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Azure.ResourceManager.CommonTypes.PrivateEndpointConnection>",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Azure.ResourceManager.CommonTypes.PrivateEndpointConnection>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
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
              ],
              "effectiveModel": "Azure.ResourceManager.CommonTypes.PrivateEndpointConnection"
            }
          ]
        },
        {
          "statusCodes": 202,
          "type": {
            "name": "Azure.ResourceManager.ArmAcceptedLroResponse<\"Resource operation accepted.\", { location: string, retryAfter: int32 }>",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmAcceptedLroResponse<\"Resource operation accepted.\", { location: string, retryAfter: int32 }>",
                "discriminated": false
              }
            ]
          },
          "bodies": [null]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate\",{\"sourceFile\":\"PrivateEndpointConnection.tsp\",\"line\":29,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:7"]
}
```

**Gap analysis and decision:** ApiManagement PrivateEndpointConnection uses ApiManagementServiceResource as the legacy resource argument; RecoveryServices certificate uses Vault but returns VaultCertificateResponse. The complete registered-alias graph also exposes SyncJob.create as a read association of SourceControl, not an eligible create/update association for the SyncJob result. Existing canonical warnings compare to the parent, not the original request/result or SyncJob PUT/GET pair. Review child-resource/custom-operation modeling and preserve wire behavior; an extra equality warning is not the first fix.

<a id="s-9bd66fb3b423b668"></a>

## PutRequestResponseSchemeArm: 9bd66fb3b423b668

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/subscriptions/{sid}`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/subscriptions/{sid}",
      "operationId": "Subscription_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/SubscriptionCreateParameters"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "SubscriptionCreateParameters"]
        },
        "topLevelResolvedSchemaSha256": "ea0c399d65674bb359d158dd4afd4359a25b0f78bc6585bbe5d16cddad83c220",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/SubscriptionContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "SubscriptionContract"]
          },
          "topLevelResolvedSchemaSha256": "460212c8c487380e32d5102d80a4ce36a045a8a693153f465cffdd4755f185d7",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/SubscriptionContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "SubscriptionContract"]
          },
          "topLevelResolvedSchemaSha256": "460212c8c487380e32d5102d80a4ce36a045a8a693153f465cffdd4755f185d7",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.SubscriptionContracts.createOrUpdate",
      "sourceFile": "SubscriptionContract.tsp",
      "line": 91,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/subscriptions/{sid}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.SubscriptionCreateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.SubscriptionCreateParameters",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.ApiManagement.SubscriptionCreateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.SubscriptionCreateParameters",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.ApiManagement.SubscriptionContract",
          "group": "registry",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.SubscriptionContracts.createOrUpdate\",{\"sourceFile\":\"SubscriptionContract.tsp\",\"line\":91,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.ApiManagement.SubscriptionContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.ApiManagement.SubscriptionContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.SubscriptionContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.SubscriptionContract",
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
              "effectiveModel": "Microsoft.ApiManagement.SubscriptionContract"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "{ statusCode: 201, body: Microsoft.ApiManagement.SubscriptionContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 201, body: Microsoft.ApiManagement.SubscriptionContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.SubscriptionContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.SubscriptionContract",
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
              "effectiveModel": "Microsoft.ApiManagement.SubscriptionContract"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.SubscriptionContracts.createOrUpdate\",{\"sourceFile\":\"SubscriptionContract.tsp\",\"line\":91,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement:27"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:8"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-c24f5593e4c0444c"></a>

## PutRequestResponseSchemeArm: c24f5593e4c0444c

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tags/{tagId}`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tags/{tagId}",
      "operationId": "Tag_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/TagCreateUpdateParameters"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "TagCreateUpdateParameters"]
        },
        "topLevelResolvedSchemaSha256": "ac72a890bc7841bbd32f1f0ece88cb3e8f3b606d15d84239d5ca07e8b0d5ed83",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/TagContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "TagContract"]
          },
          "topLevelResolvedSchemaSha256": "8c5621162c1786bd4226fb9f358895e32f6ddec800ace060c2c7f6ccacdf8de9",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/TagContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "TagContract"]
          },
          "topLevelResolvedSchemaSha256": "8c5621162c1786bd4226fb9f358895e32f6ddec800ace060c2c7f6ccacdf8de9",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.TagContractOperationGroup.createOrUpdate",
      "sourceFile": "TagContract.tsp",
      "line": 453,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tags/{tagId}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.TagCreateUpdateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.TagCreateUpdateParameters",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.ApiManagement.TagCreateUpdateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.TagCreateUpdateParameters",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.ApiManagement.TagContract",
          "group": "registry",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.TagContractOperationGroup.createOrUpdate\",{\"sourceFile\":\"TagContract.tsp\",\"line\":453,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.ApiManagement.TagContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.ApiManagement.TagContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.TagContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.TagContract",
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
              "effectiveModel": "Microsoft.ApiManagement.TagContract"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "{ statusCode: 201, body: Microsoft.ApiManagement.TagContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 201, body: Microsoft.ApiManagement.TagContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.TagContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.TagContract",
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
              "effectiveModel": "Microsoft.ApiManagement.TagContract"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.TagContractOperationGroup.createOrUpdate\",{\"sourceFile\":\"TagContract.tsp\",\"line\":453,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement:7"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:9"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-5bc868e33cb12f58"></a>

## PutRequestResponseSchemeArm: 5bc868e33cb12f58

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/templates/{templateName}`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/templates/{templateName}",
      "operationId": "EmailTemplate_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/EmailTemplateUpdateParameters"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "EmailTemplateUpdateParameters"]
        },
        "topLevelResolvedSchemaSha256": "6887ea9fd29794e31a4cef0ee8a5a844d9aeb5597b1a7322114c355c21a528a1",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/EmailTemplateContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "EmailTemplateContract"]
          },
          "topLevelResolvedSchemaSha256": "1a8596ee48f68e601d993e131404eb9be2e896cf655803e443e168356b06a1bf",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/EmailTemplateContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "EmailTemplateContract"]
          },
          "topLevelResolvedSchemaSha256": "1a8596ee48f68e601d993e131404eb9be2e896cf655803e443e168356b06a1bf",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.EmailTemplateContracts.createOrUpdate",
      "sourceFile": "EmailTemplateContract.tsp",
      "line": 89,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/templates/{templateName}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.EmailTemplateUpdateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.EmailTemplateUpdateParameters",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.ApiManagement.EmailTemplateUpdateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.EmailTemplateUpdateParameters",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.ApiManagement.EmailTemplateContract",
          "group": "lists",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.EmailTemplateContracts.createOrUpdate\",{\"sourceFile\":\"EmailTemplateContract.tsp\",\"line\":89,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ApiManagement.EmailTemplateContract>",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ApiManagement.EmailTemplateContract>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.EmailTemplateContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.EmailTemplateContract",
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
              "effectiveModel": "Microsoft.ApiManagement.EmailTemplateContract"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.EmailTemplateContract>",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.EmailTemplateContract>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.EmailTemplateContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.EmailTemplateContract",
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
              "effectiveModel": "Microsoft.ApiManagement.EmailTemplateContract"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.EmailTemplateContracts.createOrUpdate\",{\"sourceFile\":\"EmailTemplateContract.tsp\",\"line\":89,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement:12"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:10"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-6d6f81e97257180a"></a>

## PutRequestResponseSchemeArm: 6d6f81e97257180a

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tenant/{accessName}`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tenant/{accessName}",
      "operationId": "TenantAccess_Create",
      "request": {
        "raw": {
          "$ref": "#/definitions/AccessInformationCreateParameters"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "AccessInformationCreateParameters"]
        },
        "topLevelResolvedSchemaSha256": "ecf3acf2d0dd0cdc95f1d31a130ff79bee779993fb529f83b9c1853d3af7defe",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/AccessInformationContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "AccessInformationContract"]
          },
          "topLevelResolvedSchemaSha256": "d7270e069ed86c2e47541f8f5a6311c0b03fd123b9f37685f24833cd8ae49e5b",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.AccessInformationContracts.create",
      "sourceFile": "AccessInformationContract.tsp",
      "line": 91,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tenant/{accessName}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.AccessInformationCreateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.AccessInformationCreateParameters",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.ApiManagement.AccessInformationCreateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.AccessInformationCreateParameters",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.ApiManagement.AccessInformationContract",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.AccessInformationContracts.create\",{\"sourceFile\":\"AccessInformationContract.tsp\",\"line\":91,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.ApiManagement.AccessInformationContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.ApiManagement.AccessInformationContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.AccessInformationContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.AccessInformationContract",
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
              "effectiveModel": "Microsoft.ApiManagement.AccessInformationContract"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.AccessInformationContracts.create\",{\"sourceFile\":\"AccessInformationContract.tsp\",\"line\":91,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement:29"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:11"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-abb6d8ec653be75b"></a>

## PutRequestResponseSchemeArm: abb6d8ec653be75b

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/users/{userId}`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/users/{userId}",
      "operationId": "User_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/UserCreateParameters"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "UserCreateParameters"]
        },
        "topLevelResolvedSchemaSha256": "0b787a73aa40e2dc1e537856e50be7089a13b52e9863292543ea9ab5586ff99b",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/UserContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "UserContract"]
          },
          "topLevelResolvedSchemaSha256": "d1f93637aecd965e7d1bad8ae73a30fc5ec7b3218a1d2ecd62ff0171ffdb5cef",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/UserContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "UserContract"]
          },
          "topLevelResolvedSchemaSha256": "d1f93637aecd965e7d1bad8ae73a30fc5ec7b3218a1d2ecd62ff0171ffdb5cef",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.UserContracts.createOrUpdate",
      "sourceFile": "UserContract.tsp",
      "line": 61,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/users/{userId}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.UserCreateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.UserCreateParameters",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.ApiManagement.UserCreateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.UserCreateParameters",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.ApiManagement.UserContract",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.UserContracts.createOrUpdate\",{\"sourceFile\":\"UserContract.tsp\",\"line\":61,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.ApiManagement.UserContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.ApiManagement.UserContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.UserContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.UserContract",
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
              "effectiveModel": "Microsoft.ApiManagement.UserContract"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "{ statusCode: 201, retryAfter: int32, body: Microsoft.ApiManagement.UserContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 201, retryAfter: int32, body: Microsoft.ApiManagement.UserContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.UserContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.UserContract",
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
              "effectiveModel": "Microsoft.ApiManagement.UserContract"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.UserContracts.createOrUpdate\",{\"sourceFile\":\"UserContract.tsp\",\"line\":61,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement:17"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:12"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-f480a1873a8a46d6"></a>

## PutRequestResponseSchemeArm: f480a1873a8a46d6

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/apis/{apiId}`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/apis/{apiId}",
      "operationId": "WorkspaceApi_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/ApiCreateOrUpdateParameter"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "ApiCreateOrUpdateParameter"]
        },
        "topLevelResolvedSchemaSha256": "363605794ce5370a178f9ed0d30b028292c451ca4d96ed2df4ea97d35343ef03",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/ApiContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "ApiContract"]
          },
          "topLevelResolvedSchemaSha256": "a5dcb74389d6fd3f5b41c9be3b1847f5a22cbc55ec5ae8ba1f8abb27a871eff3",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/ApiContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "ApiContract"]
          },
          "topLevelResolvedSchemaSha256": "a5dcb74389d6fd3f5b41c9be3b1847f5a22cbc55ec5ae8ba1f8abb27a871eff3",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.WorkspaceApi.createOrUpdate",
      "sourceFile": "ApiContract.tsp",
      "line": 395,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/apis/{apiId}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.ApiCreateOrUpdateParameter",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.ApiCreateOrUpdateParameter",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.ApiManagement.ApiCreateOrUpdateParameter",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.ApiCreateOrUpdateParameter",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.ApiManagement.ApiContract",
          "group": "lists",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.WorkspaceApi.createOrUpdate\",{\"sourceFile\":\"ApiContract.tsp\",\"line\":395,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.ApiManagement.ApiContract, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.ApiManagement.ApiContract, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.ApiContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.ApiContract",
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
              "effectiveModel": "Microsoft.ApiManagement.ApiContract"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "{ statusCode: 201, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, body: Microsoft.ApiManagement.ApiContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 201, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, body: Microsoft.ApiManagement.ApiContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.ApiContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.ApiContract",
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
              "effectiveModel": "Microsoft.ApiManagement.ApiContract"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.WorkspaceApi.createOrUpdate\",{\"sourceFile\":\"ApiContract.tsp\",\"line\":395,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement:1"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:13"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-4fe374080228c379"></a>

## PutRequestResponseSchemeArm: 4fe374080228c379

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/certificates/{certificateId}`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/certificates/{certificateId}",
      "operationId": "WorkspaceCertificate_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/CertificateCreateOrUpdateParameters"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "CertificateCreateOrUpdateParameters"]
        },
        "topLevelResolvedSchemaSha256": "7af06c99db4f6c497a09278c2a736f7f716de8a4d6226f0d4ed89d8c729969eb",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/CertificateContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "CertificateContract"]
          },
          "topLevelResolvedSchemaSha256": "a3a0b842e4c4b9e2d06e0c8d2eb6decc0a08c994c491718e26f8e15f59956cff",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/CertificateContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "CertificateContract"]
          },
          "topLevelResolvedSchemaSha256": "a3a0b842e4c4b9e2d06e0c8d2eb6decc0a08c994c491718e26f8e15f59956cff",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.WorkspaceCertificate.createOrUpdate",
      "sourceFile": "CertificateContract.tsp",
      "line": 273,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/certificates/{certificateId}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.CertificateCreateOrUpdateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.CertificateCreateOrUpdateParameters",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.ApiManagement.CertificateCreateOrUpdateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.CertificateCreateOrUpdateParameters",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.ApiManagement.CertificateContract",
          "group": "lists",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.WorkspaceCertificate.createOrUpdate\",{\"sourceFile\":\"CertificateContract.tsp\",\"line\":273,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.ApiManagement.CertificateContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.ApiManagement.CertificateContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.CertificateContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.CertificateContract",
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
              "effectiveModel": "Microsoft.ApiManagement.CertificateContract"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "{ statusCode: 201, body: Microsoft.ApiManagement.CertificateContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 201, body: Microsoft.ApiManagement.CertificateContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.CertificateContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.CertificateContract",
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
              "effectiveModel": "Microsoft.ApiManagement.CertificateContract"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.WorkspaceCertificate.createOrUpdate\",{\"sourceFile\":\"CertificateContract.tsp\",\"line\":273,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement:11"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:14"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-aab9a5c4285f75fb"></a>

## PutRequestResponseSchemeArm: aab9a5c4285f75fb

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/groups/{groupId}`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/groups/{groupId}",
      "operationId": "WorkspaceGroup_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/GroupCreateParameters"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "GroupCreateParameters"]
        },
        "topLevelResolvedSchemaSha256": "15b2324645f4d9e2302640f032b43b5e17bfba1eafe43ab46059fec1c71b8687",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/GroupContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "GroupContract"]
          },
          "topLevelResolvedSchemaSha256": "71477ed63f310d12c08eb6ba518429cd169eeaa2ad808f4aaa89e6c77eec84a4",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/GroupContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "GroupContract"]
          },
          "topLevelResolvedSchemaSha256": "71477ed63f310d12c08eb6ba518429cd169eeaa2ad808f4aaa89e6c77eec84a4",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.WorkspaceGroup.createOrUpdate",
      "sourceFile": "GroupContract.tsp",
      "line": 438,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/groups/{groupId}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.GroupCreateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.GroupCreateParameters",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.ApiManagement.GroupCreateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.GroupCreateParameters",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.ApiManagement.GroupContract",
          "group": "lists",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.WorkspaceGroup.createOrUpdate\",{\"sourceFile\":\"GroupContract.tsp\",\"line\":438,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.ApiManagement.GroupContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.ApiManagement.GroupContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.GroupContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.GroupContract",
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
              "effectiveModel": "Microsoft.ApiManagement.GroupContract"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "{ statusCode: 201, body: Microsoft.ApiManagement.GroupContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 201, body: Microsoft.ApiManagement.GroupContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.GroupContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.GroupContract",
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
              "effectiveModel": "Microsoft.ApiManagement.GroupContract"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.WorkspaceGroup.createOrUpdate\",{\"sourceFile\":\"GroupContract.tsp\",\"line\":438,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement:16"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:15"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-e76bb208f825a268"></a>

## PutRequestResponseSchemeArm: e76bb208f825a268

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/namedValues/{namedValueId}`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/namedValues/{namedValueId}",
      "operationId": "WorkspaceNamedValue_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/NamedValueCreateContract"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "NamedValueCreateContract"]
        },
        "topLevelResolvedSchemaSha256": "c62c8ddb5d21bb8970a1262e4c9ee44e990bd4cee515955f19d317028149cdbd",
        "xmsResourceInHierarchy": true
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/NamedValueContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "NamedValueContract"]
          },
          "topLevelResolvedSchemaSha256": "b77d1f749674db0eaa88fd588704564590c491b5b7694bc359cc5aade8eb1d1c",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/NamedValueContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "NamedValueContract"]
          },
          "topLevelResolvedSchemaSha256": "b77d1f749674db0eaa88fd588704564590c491b5b7694bc359cc5aade8eb1d1c",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.WorkspaceNamedValue.createOrUpdate",
      "sourceFile": "NamedValueContract.tsp",
      "line": 306,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/namedValues/{namedValueId}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.NamedValueCreateContract",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.NamedValueCreateContract",
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
          "name": "Microsoft.ApiManagement.NamedValueCreateContract",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.NamedValueCreateContract",
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
          "resource": "Microsoft.ApiManagement.NamedValueContract",
          "group": "lists",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.WorkspaceNamedValue.createOrUpdate\",{\"sourceFile\":\"NamedValueContract.tsp\",\"line\":306,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.ApiManagement.NamedValueContract, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.ApiManagement.NamedValueContract, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.NamedValueContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.NamedValueContract",
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
              "effectiveModel": "Microsoft.ApiManagement.NamedValueContract"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "{ statusCode: 201, retryAfter: int32, body: Microsoft.ApiManagement.NamedValueContract, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 201, retryAfter: int32, body: Microsoft.ApiManagement.NamedValueContract, azureAsyncOperation: TypeSpec.Rest.ResourceLocation, location: string, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.NamedValueContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.NamedValueContract",
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
              "effectiveModel": "Microsoft.ApiManagement.NamedValueContract"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.WorkspaceNamedValue.createOrUpdate\",{\"sourceFile\":\"NamedValueContract.tsp\",\"line\":306,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement:20"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:16"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-ddf45b716631a01b"></a>

## PutRequestResponseSchemeArm: ddf45b716631a01b

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/subscriptions/{sid}`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/subscriptions/{sid}",
      "operationId": "WorkspaceSubscription_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/SubscriptionCreateParameters"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "SubscriptionCreateParameters"]
        },
        "topLevelResolvedSchemaSha256": "ea0c399d65674bb359d158dd4afd4359a25b0f78bc6585bbe5d16cddad83c220",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/SubscriptionContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "SubscriptionContract"]
          },
          "topLevelResolvedSchemaSha256": "460212c8c487380e32d5102d80a4ce36a045a8a693153f465cffdd4755f185d7",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/SubscriptionContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "SubscriptionContract"]
          },
          "topLevelResolvedSchemaSha256": "460212c8c487380e32d5102d80a4ce36a045a8a693153f465cffdd4755f185d7",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.WorkspaceSubscription.createOrUpdate",
      "sourceFile": "SubscriptionContract.tsp",
      "line": 403,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/subscriptions/{sid}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.SubscriptionCreateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.SubscriptionCreateParameters",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.ApiManagement.SubscriptionCreateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.SubscriptionCreateParameters",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.ApiManagement.SubscriptionContract",
          "group": "lists",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.WorkspaceSubscription.createOrUpdate\",{\"sourceFile\":\"SubscriptionContract.tsp\",\"line\":403,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.ApiManagement.SubscriptionContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.ApiManagement.SubscriptionContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.SubscriptionContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.SubscriptionContract",
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
              "effectiveModel": "Microsoft.ApiManagement.SubscriptionContract"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "{ statusCode: 201, body: Microsoft.ApiManagement.SubscriptionContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 201, body: Microsoft.ApiManagement.SubscriptionContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.SubscriptionContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.SubscriptionContract",
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
              "effectiveModel": "Microsoft.ApiManagement.SubscriptionContract"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.WorkspaceSubscription.createOrUpdate\",{\"sourceFile\":\"SubscriptionContract.tsp\",\"line\":403,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement:28"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:17"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-ea5b75fffe317a54"></a>

## PutRequestResponseSchemeArm: ea5b75fffe317a54

**Route/document:** `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/tags/{tagId}`; `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/tags/{tagId}",
      "operationId": "WorkspaceTag_CreateOrUpdate",
      "request": {
        "raw": {
          "$ref": "#/definitions/TagCreateUpdateParameters"
        },
        "reference": {
          "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
          "pointer": ["definitions", "TagCreateUpdateParameters"]
        },
        "topLevelResolvedSchemaSha256": "ac72a890bc7841bbd32f1f0ece88cb3e8f3b606d15d84239d5ca07e8b0d5ed83",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/TagContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "TagContract"]
          },
          "topLevelResolvedSchemaSha256": "8c5621162c1786bd4226fb9f358895e32f6ddec800ace060c2c7f6ccacdf8de9",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/TagContract"
          },
          "reference": {
            "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
            "pointer": ["definitions", "TagContract"]
          },
          "topLevelResolvedSchemaSha256": "8c5621162c1786bd4226fb9f358895e32f6ddec800ace060c2c7f6ccacdf8de9",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.ApiManagement.WorkspaceTag.createOrUpdate",
      "sourceFile": "TagContract.tsp",
      "line": 628,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/tags/{tagId}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.ApiManagement.TagCreateUpdateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.TagCreateUpdateParameters",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.ApiManagement.TagCreateUpdateParameters",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.ApiManagement.TagCreateUpdateParameters",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.ApiManagement.TagContract",
          "group": "lists",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.ApiManagement.WorkspaceTag.createOrUpdate\",{\"sourceFile\":\"TagContract.tsp\",\"line\":628,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "{ statusCode: 200, body: Microsoft.ApiManagement.TagContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 200, body: Microsoft.ApiManagement.TagContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.TagContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.TagContract",
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
              "effectiveModel": "Microsoft.ApiManagement.TagContract"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "{ statusCode: 201, body: Microsoft.ApiManagement.TagContract, eTag: string }",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "{ statusCode: 201, body: Microsoft.ApiManagement.TagContract, eTag: string }",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.ApiManagement.TagContract",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.ApiManagement.TagContract",
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
              "effectiveModel": "Microsoft.ApiManagement.TagContract"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
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
              "registeredResource": false,
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
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.WorkspaceTag.createOrUpdate\",{\"sourceFile\":\"TagContract.tsp\",\"line\":628,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement:8"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:18"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

## Additional comparison: Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate

[Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/PrivateEndpointConnection.tsp#L29); **same-operation-different-comparison**.

```json
{
  "diagnostic": {
    "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
    "message": "PUT request body must use resource model Microsoft.ApiManagement.ApiManagementServiceResource. Found Microsoft.ApiManagement.PrivateEndpointConnectionRequest.",
    "targetKind": "Operation",
    "operationKey": "[\"Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate\",{\"sourceFile\":\"PrivateEndpointConnection.tsp\",\"line\":29,\"column\":3}]",
    "sourceFile": "PrivateEndpointConnection.tsp",
    "line": 29,
    "column": 3
  },
  "operation": {
    "operation": "Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate",
    "sourceFile": "PrivateEndpointConnection.tsp",
    "line": 29,
    "verb": "put",
    "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/privateEndpointConnections/{privateEndpointConnectionName}",
    "request": {
      "bodyKind": "single",
      "type": {
        "name": "Microsoft.ApiManagement.PrivateEndpointConnectionRequest",
        "kind": "Model",
        "registeredResource": false,
        "void": false,
        "lineage": [
          {
            "name": "Microsoft.ApiManagement.PrivateEndpointConnectionRequest",
            "discriminated": false
          }
        ]
      },
      "effectiveType": {
        "name": "Microsoft.ApiManagement.PrivateEndpointConnectionRequest",
        "kind": "Model",
        "registeredResource": false,
        "void": false,
        "lineage": [
          {
            "name": "Microsoft.ApiManagement.PrivateEndpointConnectionRequest",
            "discriminated": false
          }
        ]
      },
      "void": false
    },
    "associations": [
      {
        "resource": "Microsoft.ApiManagement.ApiManagementServiceResource",
        "group": "lifecycle",
        "kind": "createOrUpdate",
        "operationKey": "[\"Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate\",{\"sourceFile\":\"PrivateEndpointConnection.tsp\",\"line\":29,\"column\":3}]",
        "internal": false,
        "checkedResponseKind": "createOrUpdate",
        "checkedPutRequest": true
      }
    ],
    "responses": [
      {
        "statusCodes": 200,
        "type": {
          "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Azure.ResourceManager.CommonTypes.PrivateEndpointConnection>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Azure.ResourceManager.CommonTypes.PrivateEndpointConnection>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
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
            ],
            "effectiveModel": "Azure.ResourceManager.CommonTypes.PrivateEndpointConnection"
          }
        ]
      },
      {
        "statusCodes": 202,
        "type": {
          "name": "Azure.ResourceManager.ArmAcceptedLroResponse<\"Resource operation accepted.\", { location: string, retryAfter: int32 }>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmAcceptedLroResponse<\"Resource operation accepted.\", { location: string, retryAfter: int32 }>",
              "discriminated": false
            }
          ]
        },
        "bodies": [null]
      },
      {
        "statusCodes": "*",
        "type": {
          "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
          "kind": "Model",
          "registeredResource": false,
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
            "registeredResource": false,
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
    ]
  },
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate\",{\"sourceFile\":\"PrivateEndpointConnection.tsp\",\"line\":29,\"column\":3}]"
  ],
  "emittedBindings": [
    {
      "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/privateEndpointConnections/{privateEndpointConnectionName}",
      "operations": [
        {
          "verb": "put",
          "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/privateEndpointConnections/{privateEndpointConnectionName}",
          "operationId": "PrivateEndpointConnection_CreateOrUpdate",
          "request": {
            "raw": {
              "$ref": "#/definitions/PrivateEndpointConnectionRequest"
            },
            "reference": {
              "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
              "pointer": ["definitions", "PrivateEndpointConnectionRequest"]
            },
            "topLevelResolvedSchemaSha256": "8d06d27e4977a7598c6af81e5eda9a79a02f437aad43f29a94148711b442e8c8",
            "xmsResourceInHierarchy": false
          },
          "responses": {
            "200": {
              "raw": {
                "$ref": "../../../../../../../../../common-types/resource-management/v5/privatelinks.json#/definitions/PrivateEndpointConnection"
              },
              "reference": {
                "document": "common-types/resource-management/v5/privatelinks.json",
                "pointer": ["definitions", "PrivateEndpointConnection"]
              },
              "topLevelResolvedSchemaSha256": "1bb5749af0cd09d5f1ab36343be59e60b1cb653ee1e10886d2ae9150137f47a1",
              "xmsResourceInHierarchy": true
            },
            "202": null
          }
        }
      ]
    }
  ]
}
```

**Gap analysis and decision:** Review the canonical association or selected status/body. A real warning on the route receives no credit for a different comparison.

## Additional comparison: Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate

[Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/PrivateEndpointConnection.tsp#L29); **same-operation-different-comparison**.

```json
{
  "diagnostic": {
    "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
    "message": "[RPC 008]: PUT, GET, PATCH & LIST must return the same resource schema.",
    "targetKind": "Operation",
    "operationKey": "[\"Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate\",{\"sourceFile\":\"PrivateEndpointConnection.tsp\",\"line\":29,\"column\":3}]",
    "sourceFile": "PrivateEndpointConnection.tsp",
    "line": 29,
    "column": 3
  },
  "operation": {
    "operation": "Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate",
    "sourceFile": "PrivateEndpointConnection.tsp",
    "line": 29,
    "verb": "put",
    "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/privateEndpointConnections/{privateEndpointConnectionName}",
    "request": {
      "bodyKind": "single",
      "type": {
        "name": "Microsoft.ApiManagement.PrivateEndpointConnectionRequest",
        "kind": "Model",
        "registeredResource": false,
        "void": false,
        "lineage": [
          {
            "name": "Microsoft.ApiManagement.PrivateEndpointConnectionRequest",
            "discriminated": false
          }
        ]
      },
      "effectiveType": {
        "name": "Microsoft.ApiManagement.PrivateEndpointConnectionRequest",
        "kind": "Model",
        "registeredResource": false,
        "void": false,
        "lineage": [
          {
            "name": "Microsoft.ApiManagement.PrivateEndpointConnectionRequest",
            "discriminated": false
          }
        ]
      },
      "void": false
    },
    "associations": [
      {
        "resource": "Microsoft.ApiManagement.ApiManagementServiceResource",
        "group": "lifecycle",
        "kind": "createOrUpdate",
        "operationKey": "[\"Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate\",{\"sourceFile\":\"PrivateEndpointConnection.tsp\",\"line\":29,\"column\":3}]",
        "internal": false,
        "checkedResponseKind": "createOrUpdate",
        "checkedPutRequest": true
      }
    ],
    "responses": [
      {
        "statusCodes": 200,
        "type": {
          "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Azure.ResourceManager.CommonTypes.PrivateEndpointConnection>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Azure.ResourceManager.CommonTypes.PrivateEndpointConnection>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
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
            ],
            "effectiveModel": "Azure.ResourceManager.CommonTypes.PrivateEndpointConnection"
          }
        ]
      },
      {
        "statusCodes": 202,
        "type": {
          "name": "Azure.ResourceManager.ArmAcceptedLroResponse<\"Resource operation accepted.\", { location: string, retryAfter: int32 }>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmAcceptedLroResponse<\"Resource operation accepted.\", { location: string, retryAfter: int32 }>",
              "discriminated": false
            }
          ]
        },
        "bodies": [null]
      },
      {
        "statusCodes": "*",
        "type": {
          "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
          "kind": "Model",
          "registeredResource": false,
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
            "registeredResource": false,
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
    ]
  },
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate\",{\"sourceFile\":\"PrivateEndpointConnection.tsp\",\"line\":29,\"column\":3}]"
  ],
  "emittedBindings": [
    {
      "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/privateEndpointConnections/{privateEndpointConnectionName}",
      "operations": [
        {
          "verb": "put",
          "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/privateEndpointConnections/{privateEndpointConnectionName}",
          "operationId": "PrivateEndpointConnection_CreateOrUpdate",
          "request": {
            "raw": {
              "$ref": "#/definitions/PrivateEndpointConnectionRequest"
            },
            "reference": {
              "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
              "pointer": ["definitions", "PrivateEndpointConnectionRequest"]
            },
            "topLevelResolvedSchemaSha256": "8d06d27e4977a7598c6af81e5eda9a79a02f437aad43f29a94148711b442e8c8",
            "xmsResourceInHierarchy": false
          },
          "responses": {
            "200": {
              "raw": {
                "$ref": "../../../../../../../../../common-types/resource-management/v5/privatelinks.json#/definitions/PrivateEndpointConnection"
              },
              "reference": {
                "document": "common-types/resource-management/v5/privatelinks.json",
                "pointer": ["definitions", "PrivateEndpointConnection"]
              },
              "topLevelResolvedSchemaSha256": "1bb5749af0cd09d5f1ab36343be59e60b1cb653ee1e10886d2ae9150137f47a1",
              "xmsResourceInHierarchy": true
            },
            "202": null
          }
        }
      ]
    }
  ]
}
```

**Gap analysis and decision:** Review the canonical association or selected status/body. A real warning on the route receives no credit for a different comparison.

## Additional comparison: Microsoft.ApiManagement.Tag.assignToApi

[Microsoft.ApiManagement.Tag.assignToApi](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagContract.tsp#L223); **additional-missing-request-policy**.

```json
{
  "diagnostic": {
    "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
    "message": "ARM PUT operations must have a request body.",
    "targetKind": "Operation",
    "operationKey": "[\"Microsoft.ApiManagement.Tag.assignToApi\",{\"sourceFile\":\"TagContract.tsp\",\"line\":223,\"column\":3}]",
    "sourceFile": "TagContract.tsp",
    "line": 223,
    "column": 3
  },
  "operation": {
    "operation": "Microsoft.ApiManagement.Tag.assignToApi",
    "sourceFile": "TagContract.tsp",
    "line": 223,
    "verb": "put",
    "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/tags/{tagId}",
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
        "resource": "Microsoft.ApiManagement.TagContract",
        "group": "lists",
        "kind": "assignToApi",
        "operationKey": "[\"Microsoft.ApiManagement.Tag.assignToApi\",{\"sourceFile\":\"TagContract.tsp\",\"line\":223,\"column\":3}]",
        "internal": false,
        "checkedResponseKind": "createOrUpdate",
        "checkedPutRequest": true
      }
    ],
    "responses": [
      {
        "statusCodes": 200,
        "type": {
          "name": "{ statusCode: 200, body: Microsoft.ApiManagement.TagContract, eTag: string }",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "{ statusCode: 200, body: Microsoft.ApiManagement.TagContract, eTag: string }",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.TagContract",
            "kind": "Model",
            "registeredResource": true,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.TagContract",
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
            "effectiveModel": "Microsoft.ApiManagement.TagContract"
          }
        ]
      },
      {
        "statusCodes": 201,
        "type": {
          "name": "{ statusCode: 201, body: Microsoft.ApiManagement.TagContract, eTag: string }",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "{ statusCode: 201, body: Microsoft.ApiManagement.TagContract, eTag: string }",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.TagContract",
            "kind": "Model",
            "registeredResource": true,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.TagContract",
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
            "effectiveModel": "Microsoft.ApiManagement.TagContract"
          }
        ]
      },
      {
        "statusCodes": "*",
        "type": {
          "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
          "kind": "Model",
          "registeredResource": false,
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
            "registeredResource": false,
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
    ]
  },
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.Tag.assignToApi\",{\"sourceFile\":\"TagContract.tsp\",\"line\":223,\"column\":3}]"
  ],
  "emittedBindings": [
    {
      "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/tags/{tagId}",
      "operations": [
        {
          "verb": "put",
          "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/tags/{tagId}",
          "operationId": "Tag_AssignToApi",
          "request": null,
          "responses": {
            "200": {
              "raw": {
                "$ref": "#/definitions/TagContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "TagContract"]
              },
              "topLevelResolvedSchemaSha256": "8c5621162c1786bd4226fb9f358895e32f6ddec800ace060c2c7f6ccacdf8de9",
              "xmsResourceInHierarchy": true
            },
            "201": {
              "raw": {
                "$ref": "#/definitions/TagContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "TagContract"]
              },
              "topLevelResolvedSchemaSha256": "8c5621162c1786bd4226fb9f358895e32f6ddec800ace060c2c7f6ccacdf8de9",
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

## Additional comparison: Microsoft.ApiManagement.TagContracts.assignToOperation

[Microsoft.ApiManagement.TagContracts.assignToOperation](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagContract.tsp#L110); **additional-missing-request-policy**.

```json
{
  "diagnostic": {
    "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
    "message": "ARM PUT operations must have a request body.",
    "targetKind": "Operation",
    "operationKey": "[\"Microsoft.ApiManagement.TagContracts.assignToOperation\",{\"sourceFile\":\"TagContract.tsp\",\"line\":110,\"column\":3}]",
    "sourceFile": "TagContract.tsp",
    "line": 110,
    "column": 3
  },
  "operation": {
    "operation": "Microsoft.ApiManagement.TagContracts.assignToOperation",
    "sourceFile": "TagContract.tsp",
    "line": 110,
    "verb": "put",
    "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}/tags/{tagId}",
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
        "resource": "Microsoft.ApiManagement.TagContract",
        "group": "lists",
        "kind": "assignToOperation",
        "operationKey": "[\"Microsoft.ApiManagement.TagContracts.assignToOperation\",{\"sourceFile\":\"TagContract.tsp\",\"line\":110,\"column\":3}]",
        "internal": false,
        "checkedResponseKind": "createOrUpdate",
        "checkedPutRequest": true
      }
    ],
    "responses": [
      {
        "statusCodes": 200,
        "type": {
          "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ApiManagement.TagContract>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ApiManagement.TagContract>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.TagContract",
            "kind": "Model",
            "registeredResource": true,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.TagContract",
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
            "effectiveModel": "Microsoft.ApiManagement.TagContract"
          }
        ]
      },
      {
        "statusCodes": 201,
        "type": {
          "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.TagContract>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.TagContract>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.TagContract",
            "kind": "Model",
            "registeredResource": true,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.TagContract",
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
            "effectiveModel": "Microsoft.ApiManagement.TagContract"
          }
        ]
      },
      {
        "statusCodes": "*",
        "type": {
          "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
          "kind": "Model",
          "registeredResource": false,
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
            "registeredResource": false,
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
    ]
  },
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.TagContracts.assignToOperation\",{\"sourceFile\":\"TagContract.tsp\",\"line\":110,\"column\":3}]"
  ],
  "emittedBindings": [
    {
      "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}/tags/{tagId}",
      "operations": [
        {
          "verb": "put",
          "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}/tags/{tagId}",
          "operationId": "Tag_AssignToOperation",
          "request": null,
          "responses": {
            "200": {
              "raw": {
                "$ref": "#/definitions/TagContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "TagContract"]
              },
              "topLevelResolvedSchemaSha256": "8c5621162c1786bd4226fb9f358895e32f6ddec800ace060c2c7f6ccacdf8de9",
              "xmsResourceInHierarchy": true
            },
            "201": {
              "raw": {
                "$ref": "#/definitions/TagContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "TagContract"]
              },
              "topLevelResolvedSchemaSha256": "8c5621162c1786bd4226fb9f358895e32f6ddec800ace060c2c7f6ccacdf8de9",
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

## Additional comparison: Microsoft.ApiManagement.TagContractOperation.assignToProduct

[Microsoft.ApiManagement.TagContractOperation.assignToProduct](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagContract.tsp#L350); **additional-missing-request-policy**.

```json
{
  "diagnostic": {
    "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
    "message": "ARM PUT operations must have a request body.",
    "targetKind": "Operation",
    "operationKey": "[\"Microsoft.ApiManagement.TagContractOperation.assignToProduct\",{\"sourceFile\":\"TagContract.tsp\",\"line\":350,\"column\":3}]",
    "sourceFile": "TagContract.tsp",
    "line": 350,
    "column": 3
  },
  "operation": {
    "operation": "Microsoft.ApiManagement.TagContractOperation.assignToProduct",
    "sourceFile": "TagContract.tsp",
    "line": 350,
    "verb": "put",
    "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/tags/{tagId}",
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
        "resource": "Microsoft.ApiManagement.TagContract",
        "group": "lists",
        "kind": "assignToProduct",
        "operationKey": "[\"Microsoft.ApiManagement.TagContractOperation.assignToProduct\",{\"sourceFile\":\"TagContract.tsp\",\"line\":350,\"column\":3}]",
        "internal": false,
        "checkedResponseKind": "createOrUpdate",
        "checkedPutRequest": true
      }
    ],
    "responses": [
      {
        "statusCodes": 200,
        "type": {
          "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ApiManagement.TagContract>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ApiManagement.TagContract>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.TagContract",
            "kind": "Model",
            "registeredResource": true,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.TagContract",
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
            "effectiveModel": "Microsoft.ApiManagement.TagContract"
          }
        ]
      },
      {
        "statusCodes": 201,
        "type": {
          "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.TagContract>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.TagContract>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.TagContract",
            "kind": "Model",
            "registeredResource": true,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.TagContract",
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
            "effectiveModel": "Microsoft.ApiManagement.TagContract"
          }
        ]
      },
      {
        "statusCodes": "*",
        "type": {
          "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
          "kind": "Model",
          "registeredResource": false,
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
            "registeredResource": false,
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
    ]
  },
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.TagContractOperation.assignToProduct\",{\"sourceFile\":\"TagContract.tsp\",\"line\":350,\"column\":3}]"
  ],
  "emittedBindings": [
    {
      "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/tags/{tagId}",
      "operations": [
        {
          "verb": "put",
          "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/tags/{tagId}",
          "operationId": "Tag_AssignToProduct",
          "request": null,
          "responses": {
            "200": {
              "raw": {
                "$ref": "#/definitions/TagContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "TagContract"]
              },
              "topLevelResolvedSchemaSha256": "8c5621162c1786bd4226fb9f358895e32f6ddec800ace060c2c7f6ccacdf8de9",
              "xmsResourceInHierarchy": true
            },
            "201": {
              "raw": {
                "$ref": "#/definitions/TagContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "TagContract"]
              },
              "topLevelResolvedSchemaSha256": "8c5621162c1786bd4226fb9f358895e32f6ddec800ace060c2c7f6ccacdf8de9",
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

## Additional comparison: Microsoft.ApiManagement.GroupContracts.create

[Microsoft.ApiManagement.GroupContracts.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/GroupContract.tsp#L334); **additional-missing-request-policy**.

```json
{
  "diagnostic": {
    "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
    "message": "ARM PUT operations must have a request body.",
    "targetKind": "Operation",
    "operationKey": "[\"Microsoft.ApiManagement.GroupContracts.create\",{\"sourceFile\":\"GroupContract.tsp\",\"line\":334,\"column\":3}]",
    "sourceFile": "GroupContract.tsp",
    "line": 334,
    "column": 3
  },
  "operation": {
    "operation": "Microsoft.ApiManagement.GroupContracts.create",
    "sourceFile": "GroupContract.tsp",
    "line": 334,
    "verb": "put",
    "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/groups/{groupId}/users/{userId}",
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
        "resource": "Microsoft.ApiManagement.GroupContract",
        "group": "registry",
        "kind": "createOrUpdate",
        "operationKey": "[\"Microsoft.ApiManagement.GroupContracts.create\",{\"sourceFile\":\"GroupContract.tsp\",\"line\":334,\"column\":3}]",
        "internal": false,
        "checkedResponseKind": "createOrUpdate",
        "checkedPutRequest": true
      }
    ],
    "responses": [
      {
        "statusCodes": 200,
        "type": {
          "name": "Azure.ResourceManager.ArmResponse<Microsoft.ApiManagement.UserContract>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResponse<Microsoft.ApiManagement.UserContract>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.UserContract",
            "kind": "Model",
            "registeredResource": true,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.UserContract",
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
            "effectiveModel": "Microsoft.ApiManagement.UserContract"
          }
        ]
      },
      {
        "statusCodes": 201,
        "type": {
          "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.UserContract>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.UserContract>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.UserContract",
            "kind": "Model",
            "registeredResource": true,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.UserContract",
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
            "effectiveModel": "Microsoft.ApiManagement.UserContract"
          }
        ]
      },
      {
        "statusCodes": "*",
        "type": {
          "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
          "kind": "Model",
          "registeredResource": false,
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
            "registeredResource": false,
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
    ]
  },
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.GroupContracts.create\",{\"sourceFile\":\"GroupContract.tsp\",\"line\":334,\"column\":3}]"
  ],
  "emittedBindings": [
    {
      "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/groups/{groupId}/users/{userId}",
      "operations": [
        {
          "verb": "put",
          "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/groups/{groupId}/users/{userId}",
          "operationId": "GroupUser_Create",
          "request": null,
          "responses": {
            "200": {
              "raw": {
                "$ref": "#/definitions/UserContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "UserContract"]
              },
              "topLevelResolvedSchemaSha256": "d1f93637aecd965e7d1bad8ae73a30fc5ec7b3218a1d2ecd62ff0171ffdb5cef",
              "xmsResourceInHierarchy": true
            },
            "201": {
              "raw": {
                "$ref": "#/definitions/UserContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "UserContract"]
              },
              "topLevelResolvedSchemaSha256": "d1f93637aecd965e7d1bad8ae73a30fc5ec7b3218a1d2ecd62ff0171ffdb5cef",
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

## Additional comparison: Microsoft.ApiManagement.GroupContracts.create

[Microsoft.ApiManagement.GroupContracts.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/GroupContract.tsp#L334); **additional-canonical-response-policy**.

```json
{
  "diagnostic": {
    "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
    "message": "[RPC 008]: PUT, GET, PATCH & LIST must return the same resource schema.",
    "targetKind": "Operation",
    "operationKey": "[\"Microsoft.ApiManagement.GroupContracts.create\",{\"sourceFile\":\"GroupContract.tsp\",\"line\":334,\"column\":3}]",
    "sourceFile": "GroupContract.tsp",
    "line": 334,
    "column": 3
  },
  "operation": {
    "operation": "Microsoft.ApiManagement.GroupContracts.create",
    "sourceFile": "GroupContract.tsp",
    "line": 334,
    "verb": "put",
    "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/groups/{groupId}/users/{userId}",
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
        "resource": "Microsoft.ApiManagement.GroupContract",
        "group": "registry",
        "kind": "createOrUpdate",
        "operationKey": "[\"Microsoft.ApiManagement.GroupContracts.create\",{\"sourceFile\":\"GroupContract.tsp\",\"line\":334,\"column\":3}]",
        "internal": false,
        "checkedResponseKind": "createOrUpdate",
        "checkedPutRequest": true
      }
    ],
    "responses": [
      {
        "statusCodes": 200,
        "type": {
          "name": "Azure.ResourceManager.ArmResponse<Microsoft.ApiManagement.UserContract>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResponse<Microsoft.ApiManagement.UserContract>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.UserContract",
            "kind": "Model",
            "registeredResource": true,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.UserContract",
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
            "effectiveModel": "Microsoft.ApiManagement.UserContract"
          }
        ]
      },
      {
        "statusCodes": 201,
        "type": {
          "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.UserContract>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.UserContract>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.UserContract",
            "kind": "Model",
            "registeredResource": true,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.UserContract",
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
            "effectiveModel": "Microsoft.ApiManagement.UserContract"
          }
        ]
      },
      {
        "statusCodes": "*",
        "type": {
          "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
          "kind": "Model",
          "registeredResource": false,
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
            "registeredResource": false,
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
    ]
  },
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.GroupContracts.create\",{\"sourceFile\":\"GroupContract.tsp\",\"line\":334,\"column\":3}]"
  ],
  "emittedBindings": [
    {
      "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/groups/{groupId}/users/{userId}",
      "operations": [
        {
          "verb": "put",
          "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/groups/{groupId}/users/{userId}",
          "operationId": "GroupUser_Create",
          "request": null,
          "responses": {
            "200": {
              "raw": {
                "$ref": "#/definitions/UserContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "UserContract"]
              },
              "topLevelResolvedSchemaSha256": "d1f93637aecd965e7d1bad8ae73a30fc5ec7b3218a1d2ecd62ff0171ffdb5cef",
              "xmsResourceInHierarchy": true
            },
            "201": {
              "raw": {
                "$ref": "#/definitions/UserContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "UserContract"]
              },
              "topLevelResolvedSchemaSha256": "d1f93637aecd965e7d1bad8ae73a30fc5ec7b3218a1d2ecd62ff0171ffdb5cef",
              "xmsResourceInHierarchy": true
            }
          }
        }
      ]
    }
  ]
}
```

**Gap analysis and decision:** Review the authored canonical resource and actual success body. Parent/child, command, polling-result and collection-role associations are not automatically original cross-method comparisons; prefer wire-compatible spec fixes over weakening the rule.

## Additional comparison: Microsoft.ApiManagement.NotificationContracts.createOrUpdate

[Microsoft.ApiManagement.NotificationContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NotificationContract.tsp#L233); **additional-missing-request-policy**.

```json
{
  "diagnostic": {
    "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
    "message": "ARM PUT operations must have a request body.",
    "targetKind": "Operation",
    "operationKey": "[\"Microsoft.ApiManagement.NotificationContracts.createOrUpdate\",{\"sourceFile\":\"NotificationContract.tsp\",\"line\":233,\"column\":3}]",
    "sourceFile": "NotificationContract.tsp",
    "line": 233,
    "column": 3
  },
  "operation": {
    "operation": "Microsoft.ApiManagement.NotificationContracts.createOrUpdate",
    "sourceFile": "NotificationContract.tsp",
    "line": 233,
    "verb": "put",
    "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/notifications/{notificationName}",
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
        "resource": "Microsoft.ApiManagement.NotificationContract",
        "group": "registry",
        "kind": "createOrUpdate",
        "operationKey": "[\"Microsoft.ApiManagement.NotificationContracts.createOrUpdate\",{\"sourceFile\":\"NotificationContract.tsp\",\"line\":233,\"column\":3}]",
        "internal": false,
        "checkedResponseKind": "createOrUpdate",
        "checkedPutRequest": true
      }
    ],
    "responses": [
      {
        "statusCodes": 200,
        "type": {
          "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ApiManagement.NotificationContract>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ApiManagement.NotificationContract>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.NotificationContract",
            "kind": "Model",
            "registeredResource": true,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.NotificationContract",
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
            "effectiveModel": "Microsoft.ApiManagement.NotificationContract"
          }
        ]
      },
      {
        "statusCodes": "*",
        "type": {
          "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
          "kind": "Model",
          "registeredResource": false,
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
            "registeredResource": false,
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
    ]
  },
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.NotificationContracts.createOrUpdate\",{\"sourceFile\":\"NotificationContract.tsp\",\"line\":233,\"column\":3}]"
  ],
  "emittedBindings": [
    {
      "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/notifications/{notificationName}",
      "operations": [
        {
          "verb": "put",
          "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/notifications/{notificationName}",
          "operationId": "Notification_CreateOrUpdate",
          "request": null,
          "responses": {
            "200": {
              "raw": {
                "$ref": "#/definitions/NotificationContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "NotificationContract"]
              },
              "topLevelResolvedSchemaSha256": "d1f19949a57831ec8dea73e4ea9b081e49be4eaaf8ce893f1917748f04a4ff38",
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

## Additional comparison: Microsoft.ApiManagement.WorkspaceNotification.createOrUpdate

[Microsoft.ApiManagement.WorkspaceNotification.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NotificationContract.tsp#L424); **additional-missing-request-policy**.

```json
{
  "diagnostic": {
    "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
    "message": "ARM PUT operations must have a request body.",
    "targetKind": "Operation",
    "operationKey": "[\"Microsoft.ApiManagement.WorkspaceNotification.createOrUpdate\",{\"sourceFile\":\"NotificationContract.tsp\",\"line\":424,\"column\":3}]",
    "sourceFile": "NotificationContract.tsp",
    "line": 424,
    "column": 3
  },
  "operation": {
    "operation": "Microsoft.ApiManagement.WorkspaceNotification.createOrUpdate",
    "sourceFile": "NotificationContract.tsp",
    "line": 424,
    "verb": "put",
    "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/notifications/{notificationName}",
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
        "resource": "Microsoft.ApiManagement.NotificationContract",
        "group": "lists",
        "kind": "createOrUpdate",
        "operationKey": "[\"Microsoft.ApiManagement.WorkspaceNotification.createOrUpdate\",{\"sourceFile\":\"NotificationContract.tsp\",\"line\":424,\"column\":3}]",
        "internal": false,
        "checkedResponseKind": "createOrUpdate",
        "checkedPutRequest": true
      }
    ],
    "responses": [
      {
        "statusCodes": 200,
        "type": {
          "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ApiManagement.NotificationContract>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.ApiManagement.NotificationContract>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.NotificationContract",
            "kind": "Model",
            "registeredResource": true,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.NotificationContract",
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
            "effectiveModel": "Microsoft.ApiManagement.NotificationContract"
          }
        ]
      },
      {
        "statusCodes": "*",
        "type": {
          "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
          "kind": "Model",
          "registeredResource": false,
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
            "registeredResource": false,
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
    ]
  },
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.WorkspaceNotification.createOrUpdate\",{\"sourceFile\":\"NotificationContract.tsp\",\"line\":424,\"column\":3}]"
  ],
  "emittedBindings": [
    {
      "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/notifications/{notificationName}",
      "operations": [
        {
          "verb": "put",
          "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/notifications/{notificationName}",
          "operationId": "WorkspaceNotification_CreateOrUpdate",
          "request": null,
          "responses": {
            "200": {
              "raw": {
                "$ref": "#/definitions/NotificationContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "NotificationContract"]
              },
              "topLevelResolvedSchemaSha256": "d1f19949a57831ec8dea73e4ea9b081e49be4eaaf8ce893f1917748f04a4ff38",
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

## Additional comparison: Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientUserCreateOrUpdate

[Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientUserCreateOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NotificationContract.tsp#L485); **additional-missing-request-policy**.

```json
{
  "diagnostic": {
    "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
    "message": "ARM PUT operations must have a request body.",
    "targetKind": "Operation",
    "operationKey": "[\"Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientUserCreateOrUpdate\",{\"sourceFile\":\"NotificationContract.tsp\",\"line\":485,\"column\":3}]",
    "sourceFile": "NotificationContract.tsp",
    "line": 485,
    "column": 3
  },
  "operation": {
    "operation": "Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientUserCreateOrUpdate",
    "sourceFile": "NotificationContract.tsp",
    "line": 485,
    "verb": "put",
    "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/notifications/{notificationName}/recipientUsers/{userId}",
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
        "resource": "Microsoft.ApiManagement.NotificationContract",
        "group": "lists",
        "kind": "workspaceNotificationRecipientUserCreateOrUpdate",
        "operationKey": "[\"Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientUserCreateOrUpdate\",{\"sourceFile\":\"NotificationContract.tsp\",\"line\":485,\"column\":3}]",
        "internal": false,
        "checkedResponseKind": "createOrUpdate",
        "checkedPutRequest": true
      }
    ],
    "responses": [
      {
        "statusCodes": 200,
        "type": {
          "name": "Azure.ResourceManager.ArmResponse<Microsoft.ApiManagement.RecipientUserContract>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResponse<Microsoft.ApiManagement.RecipientUserContract>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.RecipientUserContract",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.RecipientUserContract",
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
            "effectiveModel": "Microsoft.ApiManagement.RecipientUserContract"
          }
        ]
      },
      {
        "statusCodes": 201,
        "type": {
          "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.RecipientUserContract>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.RecipientUserContract>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.RecipientUserContract",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.RecipientUserContract",
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
            "effectiveModel": "Microsoft.ApiManagement.RecipientUserContract"
          }
        ]
      },
      {
        "statusCodes": "*",
        "type": {
          "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
          "kind": "Model",
          "registeredResource": false,
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
            "registeredResource": false,
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
    ]
  },
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientUserCreateOrUpdate\",{\"sourceFile\":\"NotificationContract.tsp\",\"line\":485,\"column\":3}]"
  ],
  "emittedBindings": [
    {
      "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/notifications/{notificationName}/recipientUsers/{userId}",
      "operations": [
        {
          "verb": "put",
          "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/notifications/{notificationName}/recipientUsers/{userId}",
          "operationId": "WorkspaceNotificationRecipientUser_CreateOrUpdate",
          "request": null,
          "responses": {
            "200": {
              "raw": {
                "$ref": "#/definitions/RecipientUserContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "RecipientUserContract"]
              },
              "topLevelResolvedSchemaSha256": "ee0d46327fab65346f95afd6545812d879919a86b13cd7eef53ad355dc0eda9c",
              "xmsResourceInHierarchy": true
            },
            "201": {
              "raw": {
                "$ref": "#/definitions/RecipientUserContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "RecipientUserContract"]
              },
              "topLevelResolvedSchemaSha256": "ee0d46327fab65346f95afd6545812d879919a86b13cd7eef53ad355dc0eda9c",
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

## Additional comparison: Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientUserCreateOrUpdate

[Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientUserCreateOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NotificationContract.tsp#L485); **additional-canonical-response-policy**.

```json
{
  "diagnostic": {
    "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
    "message": "[RPC 008]: PUT, GET, PATCH & LIST must return the same resource schema.",
    "targetKind": "Operation",
    "operationKey": "[\"Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientUserCreateOrUpdate\",{\"sourceFile\":\"NotificationContract.tsp\",\"line\":485,\"column\":3}]",
    "sourceFile": "NotificationContract.tsp",
    "line": 485,
    "column": 3
  },
  "operation": {
    "operation": "Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientUserCreateOrUpdate",
    "sourceFile": "NotificationContract.tsp",
    "line": 485,
    "verb": "put",
    "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/notifications/{notificationName}/recipientUsers/{userId}",
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
        "resource": "Microsoft.ApiManagement.NotificationContract",
        "group": "lists",
        "kind": "workspaceNotificationRecipientUserCreateOrUpdate",
        "operationKey": "[\"Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientUserCreateOrUpdate\",{\"sourceFile\":\"NotificationContract.tsp\",\"line\":485,\"column\":3}]",
        "internal": false,
        "checkedResponseKind": "createOrUpdate",
        "checkedPutRequest": true
      }
    ],
    "responses": [
      {
        "statusCodes": 200,
        "type": {
          "name": "Azure.ResourceManager.ArmResponse<Microsoft.ApiManagement.RecipientUserContract>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResponse<Microsoft.ApiManagement.RecipientUserContract>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.RecipientUserContract",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.RecipientUserContract",
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
            "effectiveModel": "Microsoft.ApiManagement.RecipientUserContract"
          }
        ]
      },
      {
        "statusCodes": 201,
        "type": {
          "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.RecipientUserContract>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.RecipientUserContract>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.RecipientUserContract",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.RecipientUserContract",
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
            "effectiveModel": "Microsoft.ApiManagement.RecipientUserContract"
          }
        ]
      },
      {
        "statusCodes": "*",
        "type": {
          "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
          "kind": "Model",
          "registeredResource": false,
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
            "registeredResource": false,
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
    ]
  },
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientUserCreateOrUpdate\",{\"sourceFile\":\"NotificationContract.tsp\",\"line\":485,\"column\":3}]"
  ],
  "emittedBindings": [
    {
      "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/notifications/{notificationName}/recipientUsers/{userId}",
      "operations": [
        {
          "verb": "put",
          "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/notifications/{notificationName}/recipientUsers/{userId}",
          "operationId": "WorkspaceNotificationRecipientUser_CreateOrUpdate",
          "request": null,
          "responses": {
            "200": {
              "raw": {
                "$ref": "#/definitions/RecipientUserContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "RecipientUserContract"]
              },
              "topLevelResolvedSchemaSha256": "ee0d46327fab65346f95afd6545812d879919a86b13cd7eef53ad355dc0eda9c",
              "xmsResourceInHierarchy": true
            },
            "201": {
              "raw": {
                "$ref": "#/definitions/RecipientUserContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "RecipientUserContract"]
              },
              "topLevelResolvedSchemaSha256": "ee0d46327fab65346f95afd6545812d879919a86b13cd7eef53ad355dc0eda9c",
              "xmsResourceInHierarchy": true
            }
          }
        }
      ]
    }
  ]
}
```

**Gap analysis and decision:** Review the authored canonical resource and actual success body. Parent/child, command, polling-result and collection-role associations are not automatically original cross-method comparisons; prefer wire-compatible spec fixes over weakening the rule.

## Additional comparison: Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientEmailCreateOrUpdate

[Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientEmailCreateOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NotificationContract.tsp#L538); **additional-missing-request-policy**.

```json
{
  "diagnostic": {
    "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
    "message": "ARM PUT operations must have a request body.",
    "targetKind": "Operation",
    "operationKey": "[\"Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientEmailCreateOrUpdate\",{\"sourceFile\":\"NotificationContract.tsp\",\"line\":538,\"column\":3}]",
    "sourceFile": "NotificationContract.tsp",
    "line": 538,
    "column": 3
  },
  "operation": {
    "operation": "Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientEmailCreateOrUpdate",
    "sourceFile": "NotificationContract.tsp",
    "line": 538,
    "verb": "put",
    "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/notifications/{notificationName}/recipientEmails/{email}",
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
        "resource": "Microsoft.ApiManagement.NotificationContract",
        "group": "lists",
        "kind": "workspaceNotificationRecipientEmailCreateOrUpdate",
        "operationKey": "[\"Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientEmailCreateOrUpdate\",{\"sourceFile\":\"NotificationContract.tsp\",\"line\":538,\"column\":3}]",
        "internal": false,
        "checkedResponseKind": "createOrUpdate",
        "checkedPutRequest": true
      }
    ],
    "responses": [
      {
        "statusCodes": 200,
        "type": {
          "name": "Azure.ResourceManager.ArmResponse<Microsoft.ApiManagement.RecipientEmailContract>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResponse<Microsoft.ApiManagement.RecipientEmailContract>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.RecipientEmailContract",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.RecipientEmailContract",
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
            "effectiveModel": "Microsoft.ApiManagement.RecipientEmailContract"
          }
        ]
      },
      {
        "statusCodes": 201,
        "type": {
          "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.RecipientEmailContract>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.RecipientEmailContract>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.RecipientEmailContract",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.RecipientEmailContract",
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
            "effectiveModel": "Microsoft.ApiManagement.RecipientEmailContract"
          }
        ]
      },
      {
        "statusCodes": "*",
        "type": {
          "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
          "kind": "Model",
          "registeredResource": false,
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
            "registeredResource": false,
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
    ]
  },
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientEmailCreateOrUpdate\",{\"sourceFile\":\"NotificationContract.tsp\",\"line\":538,\"column\":3}]"
  ],
  "emittedBindings": [
    {
      "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/notifications/{notificationName}/recipientEmails/{email}",
      "operations": [
        {
          "verb": "put",
          "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/notifications/{notificationName}/recipientEmails/{email}",
          "operationId": "WorkspaceNotificationRecipientEmail_CreateOrUpdate",
          "request": null,
          "responses": {
            "200": {
              "raw": {
                "$ref": "#/definitions/RecipientEmailContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "RecipientEmailContract"]
              },
              "topLevelResolvedSchemaSha256": "48f97a4302c99c3457e5192fed746eaae34cf2c134fb74328af8dddfc67428d3",
              "xmsResourceInHierarchy": true
            },
            "201": {
              "raw": {
                "$ref": "#/definitions/RecipientEmailContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "RecipientEmailContract"]
              },
              "topLevelResolvedSchemaSha256": "48f97a4302c99c3457e5192fed746eaae34cf2c134fb74328af8dddfc67428d3",
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

## Additional comparison: Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientEmailCreateOrUpdate

[Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientEmailCreateOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NotificationContract.tsp#L538); **additional-canonical-response-policy**.

```json
{
  "diagnostic": {
    "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
    "message": "[RPC 008]: PUT, GET, PATCH & LIST must return the same resource schema.",
    "targetKind": "Operation",
    "operationKey": "[\"Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientEmailCreateOrUpdate\",{\"sourceFile\":\"NotificationContract.tsp\",\"line\":538,\"column\":3}]",
    "sourceFile": "NotificationContract.tsp",
    "line": 538,
    "column": 3
  },
  "operation": {
    "operation": "Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientEmailCreateOrUpdate",
    "sourceFile": "NotificationContract.tsp",
    "line": 538,
    "verb": "put",
    "path": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/notifications/{notificationName}/recipientEmails/{email}",
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
        "resource": "Microsoft.ApiManagement.NotificationContract",
        "group": "lists",
        "kind": "workspaceNotificationRecipientEmailCreateOrUpdate",
        "operationKey": "[\"Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientEmailCreateOrUpdate\",{\"sourceFile\":\"NotificationContract.tsp\",\"line\":538,\"column\":3}]",
        "internal": false,
        "checkedResponseKind": "createOrUpdate",
        "checkedPutRequest": true
      }
    ],
    "responses": [
      {
        "statusCodes": 200,
        "type": {
          "name": "Azure.ResourceManager.ArmResponse<Microsoft.ApiManagement.RecipientEmailContract>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResponse<Microsoft.ApiManagement.RecipientEmailContract>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.RecipientEmailContract",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.RecipientEmailContract",
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
            "effectiveModel": "Microsoft.ApiManagement.RecipientEmailContract"
          }
        ]
      },
      {
        "statusCodes": 201,
        "type": {
          "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.RecipientEmailContract>",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Azure.ResourceManager.ArmResourceCreatedSyncResponse<Microsoft.ApiManagement.RecipientEmailContract>",
              "discriminated": false
            }
          ]
        },
        "bodies": [
          {
            "name": "Microsoft.ApiManagement.RecipientEmailContract",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Microsoft.ApiManagement.RecipientEmailContract",
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
            "effectiveModel": "Microsoft.ApiManagement.RecipientEmailContract"
          }
        ]
      },
      {
        "statusCodes": "*",
        "type": {
          "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
          "kind": "Model",
          "registeredResource": false,
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
            "registeredResource": false,
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
    ]
  },
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientEmailCreateOrUpdate\",{\"sourceFile\":\"NotificationContract.tsp\",\"line\":538,\"column\":3}]"
  ],
  "emittedBindings": [
    {
      "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
      "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/notifications/{notificationName}/recipientEmails/{email}",
      "operations": [
        {
          "verb": "put",
          "route": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/notifications/{notificationName}/recipientEmails/{email}",
          "operationId": "WorkspaceNotificationRecipientEmail_CreateOrUpdate",
          "request": null,
          "responses": {
            "200": {
              "raw": {
                "$ref": "#/definitions/RecipientEmailContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "RecipientEmailContract"]
              },
              "topLevelResolvedSchemaSha256": "48f97a4302c99c3457e5192fed746eaae34cf2c134fb74328af8dddfc67428d3",
              "xmsResourceInHierarchy": true
            },
            "201": {
              "raw": {
                "$ref": "#/definitions/RecipientEmailContract"
              },
              "reference": {
                "document": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
                "pointer": ["definitions", "RecipientEmailContract"]
              },
              "topLevelResolvedSchemaSha256": "48f97a4302c99c3457e5192fed746eaae34cf2c134fb74328af8dddfc67428d3",
              "xmsResourceInHierarchy": true
            }
          }
        }
      ]
    }
  ]
}
```

**Gap analysis and decision:** Review the authored canonical resource and actual success body. Parent/child, command, polling-result and collection-role associations are not automatically original cross-method comparisons; prefer wire-compatible spec fixes over weakening the rule.

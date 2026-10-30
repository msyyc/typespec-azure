# Saved fixture diagnostic differences

These are immutable saved observations, not freshly executed fixtures.
Swagger snapshots use each fixture's selected member; the TypeSpec snapshot
uses the combined rule. Distinct categories are retained, never deduplicated
by property name, path or source location. No aligned corpus equivalence
or per-member TypeSpec attribution follows from these totals.

All 51 saved fixtures: 44 selected Swagger findings and 57 combined TypeSpec
findings. Of 24 unequal fixture groups, eight are Swagger-higher (12 excess)
and 16 TypeSpec-higher (25 excess); absolute difference 37, net difference 13.
The 27 equal-count fixtures remain in [the complete observations](historical-fixtures.json);
equal totals do not prove corresponding diagnostics.

| Differing fixture                                                                                                                         | Swagger | TypeSpec |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------: | -------: |
| [ConsistentPatchProperties/inherited-encoded-discriminator-patch](#consistentpatchproperties-inherited-encoded-discriminator-patch)       |       0 |        1 |
| [ConsistentPatchProperties/inherited-encoded-discriminator-response](#consistentpatchproperties-inherited-encoded-discriminator-response) |       1 |        0 |
| [ConsistentPatchProperties/never-resource-override](#consistentpatchproperties-never-resource-override)                                   |       0 |        1 |
| [ConsistentPatchProperties/scoped-get-fallback](#consistentpatchproperties-scoped-get-fallback)                                           |       0 |        1 |
| [ConsistentPatchProperties/scoped-patch-operation](#consistentpatchproperties-scoped-patch-operation)                                     |       0 |        1 |
| [ConsistentPatchProperties/scoped-property](#consistentpatchproperties-scoped-property)                                                   |       0 |        1 |
| [ConsistentPatchProperties/scoped-response-property](#consistentpatchproperties-scoped-response-property)                                 |       1 |        0 |
| [ConsistentPatchProperties/synthesized-discriminator](#consistentpatchproperties-synthesized-discriminator)                               |       1 |        0 |
| [PatchBodyParametersSchema/array-replacement-elements](#patchbodyparametersschema-array-replacement-elements)                             |       0 |        2 |
| [PatchBodyParametersSchema/create-only-patch-property](#patchbodyparametersschema-create-only-patch-property)                             |       1 |        0 |
| [PatchBodyParametersSchema/create-visibility-override](#patchbodyparametersschema-create-visibility-override)                             |       4 |        1 |
| [PatchBodyParametersSchema/default-patch-property](#patchbodyparametersschema-default-patch-property)                                     |       1 |        8 |
| [PatchBodyParametersSchema/discriminator-required-patch-property](#patchbodyparametersschema-discriminator-required-patch-property)       |       3 |        4 |
| [PatchBodyParametersSchema/encoded-identity-compliant](#patchbodyparametersschema-encoded-identity-compliant)                             |       0 |        1 |
| [PatchBodyParametersSchema/encoded-non-identity-violating](#patchbodyparametersschema-encoded-non-identity-violating)                     |       2 |        3 |
| [PatchBodyParametersSchema/native-discriminator-compliant](#patchbodyparametersschema-native-discriminator-compliant)                     |       3 |        0 |
| [PatchBodyParametersSchema/native-visibility-compliant](#patchbodyparametersschema-native-visibility-compliant)                           |       4 |        3 |
| [PatchBodyParametersSchema/nullable-body-required-property](#patchbodyparametersschema-nullable-body-required-property)                   |       1 |        2 |
| [PatchBodyParametersSchema/nullable-model-required-property](#patchbodyparametersschema-nullable-model-required-property)                 |       1 |        2 |
| [UnSupportedPatchProperties/encoded-inherited-properties](#unsupportedpatchproperties-encoded-inherited-properties)                       |       3 |        5 |
| [UnSupportedPatchProperties/explicit-create-immutable-input](#unsupportedpatchproperties-explicit-create-immutable-input)                 |       0 |        2 |
| [UnSupportedPatchProperties/patch-with-id-name](#unsupportedpatchproperties-patch-with-id-name)                                           |       3 |        4 |
| [UnSupportedPatchProperties/patch-with-location-provisioning-state](#unsupportedpatchproperties-patch-with-location-provisioning-state)   |       2 |        3 |
| [UnSupportedPatchProperties/readonly-ref-validator-discrepancy](#unsupportedpatchproperties-readonly-ref-validator-discrepancy)           |       1 |        0 |

For cause/disposition, see [layout/emission](evidence-details.md#layout-and-emission),
[safety/counting](evidence-details.md#safety-and-counting), and
[visibility/immutable input](evidence-details.md#visibility-and-immutable-input).
Policy differences and combined categories explain saved fixture differences;
they are not fixes to implement or complete explanations of production gaps.

## ConsistentPatchProperties inherited-encoded-discriminator-patch

Reported findings: Swagger **0**, TypeSpec **1**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                                                                        | Target                                                             |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| Swagger  | No selected findings                                                                                                                                                                             | Not applicable                                                     |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'details.kind.extra' in the request body either does not appear in the resource model or is nested at the wrong level. | Authored semantic target; no location serialized in saved snapshot |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/inherited-encoded-discriminator-patch/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/inherited-encoded-discriminator-patch/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/inherited-encoded-discriminator-patch/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/inherited-encoded-discriminator-patch/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using Azure.ResourceManager;

@armProviderNamespace
@service(#{ title: "Inherited encoded PATCH discriminator" })
namespace Microsoft.TestService;

/** Authored payload inherited by the discriminated model. */
model Base {
  /** Object represented as kind in the JSON payload. */
  @encodedName("application/json", "kind")
  payload?: {
    /** Property missing from the scalar resource kind. */
    extra?: string;
  };
}

/** Discriminator metadata must not replace the inherited authored object. */
@discriminator("kind")
model Details extends Base {}

interface Operations extends Azure.ResourceManager.Operations {}

/** Update the resource. */
@route("/widgets")
@patch
op update(
  /** Update body. */
  @body body: {
    /** Update details. */
    details?: Details;
  },
): {
  /** Resource details. */
  details?: {
    /** Scalar kind. */
    kind?: string;
  };
};
```

```json
{
  "paths": {
    "/providers/Microsoft.TestService/operations": {
      "get": {
        "operationId": "Operations_List",
        "tags": ["Operations"],
        "description": "List the operations for the provider",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/ApiVersionParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v3/types.json#/definitions/OperationListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v3/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/widgets": {
      "patch": {
        "operationId": "Update",
        "description": "Update the resource.",
        "parameters": [
          {
            "name": "body",
            "in": "body",
            "description": "Update body.",
            "required": true,
            "schema": {
              "type": "object",
              "properties": {
                "details": {
                  "$ref": "#/definitions/Details",
                  "description": "Update details."
                }
              }
            }
          }
        ],
        "responses": {
          "200": {
            "description": "The request has succeeded.",
            "schema": {
              "type": "object",
              "properties": {
                "details": {
                  "type": "object",
                  "description": "Resource details.",
                  "properties": {
                    "kind": {
                      "type": "string",
                      "description": "Scalar kind."
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  "definitions": {
    "Base": {
      "type": "object",
      "description": "Authored payload inherited by the discriminated model.",
      "properties": {
        "kind": {
          "type": "object",
          "description": "Object represented as kind in the JSON payload.",
          "properties": {
            "extra": {
              "type": "string",
              "description": "Property missing from the scalar resource kind."
            }
          },
          "x-ms-client-name": "payload"
        }
      }
    },
    "Details": {
      "type": "object",
      "description": "Discriminator metadata must not replace the inherited authored object.",
      "properties": {
        "kind": {
          "type": "string",
          "description": "Discriminator property for Details."
        }
      },
      "discriminator": "kind",
      "required": ["kind"],
      "allOf": [
        {
          "$ref": "#/definitions/Base"
        }
      ]
    }
  }
}
```

</details>

## ConsistentPatchProperties inherited-encoded-discriminator-response

Reported findings: Swagger **1**, TypeSpec **0**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                           | Target                                                      |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Swagger  | `ConsistentPatchProperties`: The property 'details.kind.extra' in the request body either not apppear in the resource model or has the wrong level. | ["paths", "/widgets", "patch", "parameters", "0", "schema"] |
| TypeSpec | No selected findings                                                                                                                                | Not applicable                                              |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/inherited-encoded-discriminator-response/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/inherited-encoded-discriminator-response/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/inherited-encoded-discriminator-response/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/inherited-encoded-discriminator-response/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using Azure.ResourceManager;

@armProviderNamespace
@service(#{ title: "Inherited encoded response discriminator" })
namespace Microsoft.TestService;

/** Authored payload inherited by the discriminated model. */
model Base {
  /** Object represented as kind in the JSON payload. */
  @encodedName("application/json", "kind")
  payload?: {
    /** Writable resource property. */
    extra?: string;
  };
}

/** Discriminator metadata must not replace the inherited authored object. */
@discriminator("kind")
model Details extends Base {}

interface Operations extends Azure.ResourceManager.Operations {}

/** Update the resource. */
@route("/widgets")
@patch
op update(
  /** Update body. */
  @body body: {
    /** Update details. */
    details?: {
      /** Object-valued kind. */
      kind?: {
        /** Updated property. */
        extra?: string;
      };
    };
  },
): {
  /** Resource details. */
  details?: Details;
};
```

```json
{
  "paths": {
    "/providers/Microsoft.TestService/operations": {
      "get": {
        "operationId": "Operations_List",
        "tags": ["Operations"],
        "description": "List the operations for the provider",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/ApiVersionParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v3/types.json#/definitions/OperationListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v3/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/widgets": {
      "patch": {
        "operationId": "Update",
        "description": "Update the resource.",
        "parameters": [
          {
            "name": "body",
            "in": "body",
            "description": "Update body.",
            "required": true,
            "schema": {
              "type": "object",
              "properties": {
                "details": {
                  "type": "object",
                  "description": "Update details.",
                  "properties": {
                    "kind": {
                      "type": "object",
                      "description": "Object-valued kind.",
                      "properties": {
                        "extra": {
                          "type": "string",
                          "description": "Updated property."
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        ],
        "responses": {
          "200": {
            "description": "The request has succeeded.",
            "schema": {
              "type": "object",
              "properties": {
                "details": {
                  "$ref": "#/definitions/Details",
                  "description": "Resource details."
                }
              }
            }
          }
        }
      }
    }
  },
  "definitions": {
    "Base": {
      "type": "object",
      "description": "Authored payload inherited by the discriminated model.",
      "properties": {
        "kind": {
          "type": "object",
          "description": "Object represented as kind in the JSON payload.",
          "properties": {
            "extra": {
              "type": "string",
              "description": "Writable resource property."
            }
          },
          "x-ms-client-name": "payload"
        }
      }
    },
    "Details": {
      "type": "object",
      "description": "Discriminator metadata must not replace the inherited authored object.",
      "properties": {
        "kind": {
          "type": "string",
          "description": "Discriminator property for Details."
        }
      },
      "discriminator": "kind",
      "required": ["kind"],
      "allOf": [
        {
          "$ref": "#/definitions/Base"
        }
      ]
    }
  }
}
```

</details>

## ConsistentPatchProperties never-resource-override

Reported findings: Swagger **0**, TypeSpec **1**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                                                           | Target                                                             |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Swagger  | No selected findings                                                                                                                                                                | Not applicable                                                     |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'extra' in the request body either does not appear in the resource model or is nested at the wrong level. | Authored semantic target; no location serialized in saved snapshot |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/never-resource-override/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/never-resource-override/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/never-resource-override/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/never-resource-override/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using Azure.ResourceManager;

@armProviderNamespace
@service(#{ title: "Inherited resource override" })
namespace Microsoft.TestService;

/** Shared resource properties. */
model Base {
  /** Property removed by the resource model. */
  extra?: string;

  /** Resource name. */
  name?: string;
}

/** Resource excludes the inherited extra property. */
model Resource extends Base {
  extra?: never;
}

/** Update tries to write the excluded property. */
model Update {
  /** Excluded resource property. */
  extra?: string;
}

interface Operations extends Azure.ResourceManager.Operations {}

/** Update the resource. */
@route("/widgets")
@patch
op update(
  /** Update body. */
  @body body: Update,
): Resource;
```

```json
{
  "paths": {
    "/providers/Microsoft.TestService/operations": {
      "get": {
        "operationId": "Operations_List",
        "tags": ["Operations"],
        "description": "List the operations for the provider",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/ApiVersionParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v3/types.json#/definitions/OperationListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v3/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/widgets": {
      "patch": {
        "operationId": "Update",
        "description": "Update the resource.",
        "parameters": [
          {
            "name": "body",
            "in": "body",
            "description": "Update body.",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Update"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "The request has succeeded.",
            "schema": {
              "$ref": "#/definitions/Resource"
            }
          }
        }
      }
    }
  },
  "definitions": {
    "Base": {
      "type": "object",
      "description": "Shared resource properties.",
      "properties": {
        "extra": {
          "type": "string",
          "description": "Property removed by the resource model."
        },
        "name": {
          "type": "string",
          "description": "Resource name."
        }
      }
    },
    "Resource": {
      "type": "object",
      "description": "Resource excludes the inherited extra property.",
      "allOf": [
        {
          "$ref": "#/definitions/Base"
        }
      ]
    },
    "Update": {
      "type": "object",
      "description": "Update tries to write the excluded property.",
      "properties": {
        "extra": {
          "type": "string",
          "description": "Excluded resource property."
        }
      }
    }
  }
}
```

</details>

## ConsistentPatchProperties scoped-get-fallback

Reported findings: Swagger **0**, TypeSpec **1**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                                                                 | Target                                                             |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Swagger  | No selected findings                                                                                                                                                                      | Not applicable                                                     |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'displayName' in the request body either does not appear in the resource model or is nested at the wrong level. | Authored semantic target; no location serialized in saved snapshot |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/scoped-get-fallback/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/scoped-get-fallback/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/scoped-get-fallback/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/scoped-get-fallback/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";
import "@azure-tools/typespec-client-generator-core";

using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.Versioning;
using Azure.ClientGenerator.Core;
using Azure.ResourceManager;

@armProviderNamespace
@service(#{ title: "Test Service" })
@versioned(Versions)
@armCommonTypesVersion(CommonTypes.Versions.v6)
namespace Microsoft.TestService;

enum Versions {
  @useDependency(Azure.ResourceManager.CommonTypes.Versions.v6)
  v2024_01_01: "2024-01-01",
}

model Widget is ProxyResource<WidgetProperties> {
  @key("widgetName")
  @segment("widgets")
  @doc("The name of the widget")
  @path
  name: string;
}

@doc("Widget resource properties.")
model WidgetProperties {
  @doc("Display name")
  displayName?: string;
}

@doc("PATCH body with a property at the wrong level.")
model WidgetPatchBody {
  @doc("Display name at the top level")
  displayName?: string;
}

model WidgetResponse {
  @statusCode statusCode: 200;
  @body body: Widget;
}

model AcceptedResponse {
  @statusCode statusCode: 202;
}

interface Operations extends Azure.ResourceManager.Operations {}

@route("/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}")
interface CustomWidgetOperations {
  @get
  @scope("csharp")
  read(...ResourceInstanceParameters<Widget>): WidgetResponse | ErrorResponse;

  @patch
  update(...ResourceInstanceParameters<Widget>, @body body: WidgetPatchBody):
    | AcceptedResponse
    | ErrorResponse;
}
```

```json
{
  "paths": {
    "/providers/Microsoft.TestService/operations": {
      "get": {
        "operationId": "Operations_List",
        "tags": ["Operations"],
        "description": "List the operations for the provider",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ApiVersionParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/OperationListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}/{provider}": {
      "patch": {
        "operationId": "CustomWidgetOperations_Update",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "provider",
            "in": "path",
            "description": "The provider namespace for the resource.",
            "required": true,
            "type": "string",
            "enum": ["Microsoft.TestService"],
            "x-ms-enum": {
              "modelAsString": false
            }
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string"
          },
          {
            "name": "body",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/WidgetPatchBody"
            }
          }
        ],
        "responses": {
          "202": {
            "description": "The request has been accepted for processing, but processing has not yet completed."
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/ErrorResponse"
            }
          }
        }
      }
    }
  },
  "definitions": {
    "AcceptedResponse": {
      "type": "object"
    },
    "Widget": {
      "type": "object",
      "description": "Concrete proxy resource types can be created by aliasing this type using a specific property type.",
      "properties": {
        "properties": {
          "$ref": "#/definitions/WidgetProperties",
          "description": "The resource-specific properties for this resource."
        }
      },
      "allOf": [
        {
          "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/ProxyResource"
        }
      ]
    },
    "WidgetPatchBody": {
      "type": "object",
      "description": "PATCH body with a property at the wrong level.",
      "properties": {
        "displayName": {
          "type": "string",
          "description": "Display name at the top level"
        }
      }
    },
    "WidgetProperties": {
      "type": "object",
      "description": "Widget resource properties.",
      "properties": {
        "displayName": {
          "type": "string",
          "description": "Display name"
        }
      }
    },
    "WidgetResponse": {
      "type": "object",
      "properties": {
        "body": {
          "$ref": "#/definitions/Widget"
        }
      },
      "required": ["body"]
    }
  }
}
```

</details>

## ConsistentPatchProperties scoped-patch-operation

Reported findings: Swagger **0**, TypeSpec **1**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                                                           | Target                                                             |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Swagger  | No selected findings                                                                                                                                                                | Not applicable                                                     |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'extra' in the request body either does not appear in the resource model or is nested at the wrong level. | Authored semantic target; no location serialized in saved snapshot |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/scoped-patch-operation/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/scoped-patch-operation/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/scoped-patch-operation/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/scoped-patch-operation/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";
import "@azure-tools/typespec-client-generator-core";

using TypeSpec.Http;
using Azure.ClientGenerator.Core;
using Azure.ResourceManager;

@armProviderNamespace
@service(#{ title: "Scoped PATCH comparison" })
namespace Microsoft.TestService;

/** Resource returned by the service. */
model Widget {
  /** Resource name. */
  name?: string;
}

/** Native update body with an extra property. */
model WidgetUpdate {
  /** Property absent from the resource. */
  extra?: string;
}

interface Operations extends Azure.ResourceManager.Operations {}

/** Read the widget. */
@route("/widgets")
@get
op read(): Widget;

/** Update the widget in the native HTTP contract, but not AutoRest output. */
@route("/widgets")
@patch
@scope("csharp")
op update(
  /** Update body. */
  @body body: WidgetUpdate,
): Widget;
```

```json
{
  "paths": {
    "/providers/Microsoft.TestService/operations": {
      "get": {
        "operationId": "Operations_List",
        "tags": ["Operations"],
        "description": "List the operations for the provider",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/ApiVersionParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v3/types.json#/definitions/OperationListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v3/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/widgets": {
      "get": {
        "operationId": "Read",
        "description": "Read the widget.",
        "parameters": [],
        "responses": {
          "200": {
            "description": "The request has succeeded.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          }
        }
      }
    }
  },
  "definitions": {
    "Widget": {
      "type": "object",
      "description": "Resource returned by the service.",
      "properties": {
        "name": {
          "type": "string",
          "description": "Resource name."
        }
      }
    },
    "WidgetUpdate": {
      "type": "object",
      "description": "Native update body with an extra property.",
      "properties": {
        "extra": {
          "type": "string",
          "description": "Property absent from the resource."
        }
      }
    }
  }
}
```

</details>

## ConsistentPatchProperties scoped-property

Reported findings: Swagger **0**, TypeSpec **1**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                                                                           | Target                                                             |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Swagger  | No selected findings                                                                                                                                                                                | Not applicable                                                     |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'properties.clientOnly' in the request body either does not appear in the resource model or is nested at the wrong level. | Authored semantic target; no location serialized in saved snapshot |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/scoped-property/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/scoped-property/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/scoped-property/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/scoped-property/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";
import "@azure-tools/typespec-client-generator-core";

using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.Versioning;
using Azure.ClientGenerator.Core;
using Azure.ResourceManager;

@armProviderNamespace
@service(#{ title: "Test Service" })
@versioned(Versions)
@armCommonTypesVersion(CommonTypes.Versions.v6)
namespace Microsoft.TestService;

enum Versions {
  @useDependency(Azure.ResourceManager.CommonTypes.Versions.v6)
  v2024_01_01: "2024-01-01",
}

model Widget is ProxyResource<WidgetProperties> {
  @key("widgetName")
  @segment("widgets")
  @doc("The name of the widget")
  @path
  name: string;
}

@doc("Widget resource properties.")
model WidgetProperties {
  @doc("Display name")
  displayName?: string;
}

@doc("PATCH properties.")
model WidgetPatchProperties {
  @doc("A property emitted only for C#")
  @scope("csharp")
  clientOnly?: string;
}

@doc("PATCH body.")
model WidgetPatchBody {
  @doc("Resource properties to update")
  properties?: WidgetPatchProperties;
}

interface Operations extends Azure.ResourceManager.Operations {}

@armResourceOperations
interface Widgets {
  get is ArmResourceRead<Widget>;
  createOrUpdate is ArmResourceCreateOrReplaceAsync<Widget>;
  delete is ArmResourceDeleteWithoutOkAsync<Widget>;
  listByResourceGroup is ArmResourceListByParent<Widget>;
  listBySubscription is ArmListBySubscription<Widget>;

  @patch
  @armResourceUpdate(Widget)
  update(...ResourceInstanceParameters<Widget>, @body body: WidgetPatchBody):
    | ArmResponse<Widget>
    | ErrorResponse;
}
```

```json
{
  "paths": {
    "/providers/Microsoft.TestService/operations": {
      "get": {
        "operationId": "Operations_List",
        "tags": ["Operations"],
        "description": "List the operations for the provider",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ApiVersionParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/OperationListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/providers/Microsoft.TestService/widgets": {
      "get": {
        "operationId": "Widgets_ListBySubscription",
        "tags": ["Widgets"],
        "description": "List Widget resources by subscription ID",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/SubscriptionIdParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/WidgetListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets": {
      "get": {
        "operationId": "Widgets_ListByResourceGroup",
        "tags": ["Widgets"],
        "description": "List Widget resources by resource group",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ResourceGroupNameParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/WidgetListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}": {
      "get": {
        "operationId": "Widgets_Get",
        "tags": ["Widgets"],
        "description": "Get a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "put": {
        "operationId": "Widgets_CreateOrUpdate",
        "tags": ["Widgets"],
        "description": "Create a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string"
          },
          {
            "name": "resource",
            "in": "body",
            "description": "Resource create parameters.",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Resource 'Widget' update operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "201": {
            "description": "Resource 'Widget' create operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            },
            "headers": {
              "Azure-AsyncOperation": {
                "type": "string",
                "description": "A link to the status monitor"
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "azure-async-operation"
        },
        "x-ms-long-running-operation": true
      },
      "patch": {
        "operationId": "Widgets_Update",
        "tags": ["Widgets"],
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string"
          },
          {
            "name": "body",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/WidgetPatchBody"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "delete": {
        "operationId": "Widgets_Delete",
        "tags": ["Widgets"],
        "description": "Delete a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "202": {
            "description": "Resource deletion accepted.",
            "headers": {
              "Location": {
                "type": "string",
                "description": "The Location header contains the URL where the status of the long running operation can be checked."
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "204": {
            "description": "Resource does not exist."
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "location"
        },
        "x-ms-long-running-operation": true
      }
    }
  },
  "definitions": {
    "Widget": {
      "type": "object",
      "description": "Concrete proxy resource types can be created by aliasing this type using a specific property type.",
      "properties": {
        "properties": {
          "$ref": "#/definitions/WidgetProperties",
          "description": "The resource-specific properties for this resource."
        }
      },
      "allOf": [
        {
          "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/ProxyResource"
        }
      ]
    },
    "WidgetListResult": {
      "type": "object",
      "description": "The response of a Widget list operation.",
      "properties": {
        "value": {
          "type": "array",
          "description": "The Widget items on this page",
          "items": {
            "$ref": "#/definitions/Widget"
          }
        },
        "nextLink": {
          "type": "string",
          "format": "uri",
          "description": "The link to the next page of items"
        }
      },
      "required": ["value"]
    },
    "WidgetPatchBody": {
      "type": "object",
      "description": "PATCH body.",
      "properties": {
        "properties": {
          "$ref": "#/definitions/WidgetPatchProperties",
          "description": "Resource properties to update"
        }
      }
    },
    "WidgetPatchProperties": {
      "type": "object",
      "description": "PATCH properties."
    },
    "WidgetProperties": {
      "type": "object",
      "description": "Widget resource properties.",
      "properties": {
        "displayName": {
          "type": "string",
          "description": "Display name"
        }
      }
    }
  }
}
```

</details>

## ConsistentPatchProperties scoped-response-property

Reported findings: Swagger **1**, TypeSpec **0**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                    | Target                                                      |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Swagger  | `ConsistentPatchProperties`: The property 'description' in the request body either not apppear in the resource model or has the wrong level. | ["paths", "/widgets", "patch", "parameters", "0", "schema"] |
| TypeSpec | No selected findings                                                                                                                         | Not applicable                                              |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/scoped-response-property/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/scoped-response-property/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/scoped-response-property/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/scoped-response-property/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";
import "@azure-tools/typespec-client-generator-core";

using TypeSpec.Http;
using Azure.ClientGenerator.Core;
using Azure.ResourceManager;

@armProviderNamespace
@service(#{ title: "Scoped response comparison" })
namespace Microsoft.TestService;

/** Resource with a property available in the native model only. */
model Widget {
  /** Resource name. */
  name?: string;

  /** Property omitted from AutoRest output. */
  @scope("csharp")
  description?: string;
}

/** Native update body is a same-level subset of Widget. */
model WidgetUpdate {
  /** Updated description. */
  description?: string;
}

interface Operations extends Azure.ResourceManager.Operations {}

/** Update the widget. */
@route("/widgets")
@patch
op update(
  /** Update body. */
  @body body: WidgetUpdate,
): Widget;
```

```json
{
  "paths": {
    "/providers/Microsoft.TestService/operations": {
      "get": {
        "operationId": "Operations_List",
        "tags": ["Operations"],
        "description": "List the operations for the provider",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/ApiVersionParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v3/types.json#/definitions/OperationListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v3/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/widgets": {
      "patch": {
        "operationId": "Update",
        "description": "Update the widget.",
        "parameters": [
          {
            "name": "body",
            "in": "body",
            "description": "Update body.",
            "required": true,
            "schema": {
              "$ref": "#/definitions/WidgetUpdate"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "The request has succeeded.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          }
        }
      }
    }
  },
  "definitions": {
    "Widget": {
      "type": "object",
      "description": "Resource with a property available in the native model only.",
      "properties": {
        "name": {
          "type": "string",
          "description": "Resource name."
        }
      }
    },
    "WidgetUpdate": {
      "type": "object",
      "description": "Native update body is a same-level subset of Widget.",
      "properties": {
        "description": {
          "type": "string",
          "description": "Updated description."
        }
      }
    }
  }
}
```

</details>

## ConsistentPatchProperties synthesized-discriminator

Reported findings: Swagger **1**, TypeSpec **0**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                                | Target                                                                                                                                                                     |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Swagger  | `ConsistentPatchProperties`: The property 'properties.details.kind' in the request body either not apppear in the resource model or has the wrong level. | ["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}", "patch", "parameters", "4", "schema"] |
| TypeSpec | No selected findings                                                                                                                                     | Not applicable                                                                                                                                                             |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/synthesized-discriminator/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/synthesized-discriminator/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/synthesized-discriminator/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/synthesized-discriminator/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.Versioning;
using Azure.ResourceManager;

@armProviderNamespace
@service(#{ title: "Test Service" })
@versioned(Versions)
@armCommonTypesVersion(CommonTypes.Versions.v6)
namespace Microsoft.TestService;

enum Versions {
  @useDependency(Azure.ResourceManager.CommonTypes.Versions.v6)
  v2024_01_01: "2024-01-01",
}

model Widget is ProxyResource<WidgetProperties> {
  @key("widgetName")
  @segment("widgets")
  @doc("The name of the widget")
  @path
  name: string;
}

@doc("Widget resource properties.")
model WidgetProperties {
  @doc("Resource details")
  details?: ResourceDetails;
}

@doc("Response details without a discriminator.")
model ResourceDetails {}

@doc("PATCH properties.")
model WidgetPatchProperties {
  @doc("PATCH details")
  details?: PatchDetails;
}

@doc("PATCH details whose discriminator property is synthesized by AutoRest.")
@discriminator("kind")
model PatchDetails {}

@doc("PATCH body.")
model WidgetPatchBody {
  @doc("Resource properties to update")
  properties?: WidgetPatchProperties;
}

interface Operations extends Azure.ResourceManager.Operations {}

@armResourceOperations
interface Widgets {
  get is ArmResourceRead<Widget>;
  createOrUpdate is ArmResourceCreateOrReplaceAsync<Widget>;
  delete is ArmResourceDeleteWithoutOkAsync<Widget>;
  listByResourceGroup is ArmResourceListByParent<Widget>;
  listBySubscription is ArmListBySubscription<Widget>;

  @patch
  @armResourceUpdate(Widget)
  update(...ResourceInstanceParameters<Widget>, @body body: WidgetPatchBody):
    | ArmResponse<Widget>
    | ErrorResponse;
}
```

```json
{
  "paths": {
    "/providers/Microsoft.TestService/operations": {
      "get": {
        "operationId": "Operations_List",
        "tags": ["Operations"],
        "description": "List the operations for the provider",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ApiVersionParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/OperationListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/providers/Microsoft.TestService/widgets": {
      "get": {
        "operationId": "Widgets_ListBySubscription",
        "tags": ["Widgets"],
        "description": "List Widget resources by subscription ID",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/SubscriptionIdParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/WidgetListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets": {
      "get": {
        "operationId": "Widgets_ListByResourceGroup",
        "tags": ["Widgets"],
        "description": "List Widget resources by resource group",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ResourceGroupNameParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/WidgetListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}": {
      "get": {
        "operationId": "Widgets_Get",
        "tags": ["Widgets"],
        "description": "Get a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "put": {
        "operationId": "Widgets_CreateOrUpdate",
        "tags": ["Widgets"],
        "description": "Create a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string"
          },
          {
            "name": "resource",
            "in": "body",
            "description": "Resource create parameters.",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Resource 'Widget' update operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "201": {
            "description": "Resource 'Widget' create operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            },
            "headers": {
              "Azure-AsyncOperation": {
                "type": "string",
                "description": "A link to the status monitor"
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "azure-async-operation"
        },
        "x-ms-long-running-operation": true
      },
      "patch": {
        "operationId": "Widgets_Update",
        "tags": ["Widgets"],
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string"
          },
          {
            "name": "body",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/WidgetPatchBody"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "delete": {
        "operationId": "Widgets_Delete",
        "tags": ["Widgets"],
        "description": "Delete a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v6/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "202": {
            "description": "Resource deletion accepted.",
            "headers": {
              "Location": {
                "type": "string",
                "description": "The Location header contains the URL where the status of the long running operation can be checked."
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "204": {
            "description": "Resource does not exist."
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "location"
        },
        "x-ms-long-running-operation": true
      }
    }
  },
  "definitions": {
    "PatchDetails": {
      "type": "object",
      "description": "PATCH details whose discriminator property is synthesized by AutoRest.",
      "properties": {
        "kind": {
          "type": "string",
          "description": "Discriminator property for PatchDetails."
        }
      },
      "discriminator": "kind",
      "required": ["kind"]
    },
    "ResourceDetails": {
      "type": "object",
      "description": "Response details without a discriminator."
    },
    "Widget": {
      "type": "object",
      "description": "Concrete proxy resource types can be created by aliasing this type using a specific property type.",
      "properties": {
        "properties": {
          "$ref": "#/definitions/WidgetProperties",
          "description": "The resource-specific properties for this resource."
        }
      },
      "allOf": [
        {
          "$ref": "../../../../../common-types/resource-management/v6/types.json#/definitions/ProxyResource"
        }
      ]
    },
    "WidgetListResult": {
      "type": "object",
      "description": "The response of a Widget list operation.",
      "properties": {
        "value": {
          "type": "array",
          "description": "The Widget items on this page",
          "items": {
            "$ref": "#/definitions/Widget"
          }
        },
        "nextLink": {
          "type": "string",
          "format": "uri",
          "description": "The link to the next page of items"
        }
      },
      "required": ["value"]
    },
    "WidgetPatchBody": {
      "type": "object",
      "description": "PATCH body.",
      "properties": {
        "properties": {
          "$ref": "#/definitions/WidgetPatchProperties",
          "description": "Resource properties to update"
        }
      }
    },
    "WidgetPatchProperties": {
      "type": "object",
      "description": "PATCH properties.",
      "properties": {
        "details": {
          "$ref": "#/definitions/PatchDetails",
          "description": "PATCH details"
        }
      }
    },
    "WidgetProperties": {
      "type": "object",
      "description": "Widget resource properties.",
      "properties": {
        "details": {
          "$ref": "#/definitions/ResourceDetails",
          "description": "Resource details"
        }
      }
    }
  }
}
```

</details>

## PatchBodyParametersSchema array-replacement-elements

Reported findings: Swagger **0**, TypeSpec **2**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                                                                   | Target                                                             |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Swagger  | No selected findings                                                                                                                                                                        | Not applicable                                                     |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: Properties of a PATCH request body must not have default value, property:items[].enabled.                                      | Authored semantic target; no location serialized in saved snapshot |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'items[].extra' in the request body either does not appear in the resource model or is nested at the wrong level. | Authored semantic target; no location serialized in saved snapshot |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/array-replacement-elements/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/array-replacement-elements/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/array-replacement-elements/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/array-replacement-elements/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using Azure.ResourceManager;

@armProviderNamespace
@service
namespace Microsoft.TestService;

model Element {
  id: string;
  enabled?: boolean = false;
  extra?: string;
}

@patch
@route("/widgets")
op update(
  @body body: {
    items?: Element[];
  },
): {
  items: {
    id: string;
    enabled: boolean;
  }[];
};
```

```json
{
  "paths": {
    "/widgets": {
      "patch": {
        "operationId": "Update",
        "parameters": [
          {
            "name": "body",
            "in": "body",
            "required": true,
            "schema": {
              "type": "object",
              "properties": {
                "items": {
                  "type": "array",
                  "items": {
                    "$ref": "#/definitions/Element"
                  }
                }
              }
            }
          }
        ],
        "responses": {
          "200": {
            "description": "The request has succeeded.",
            "schema": {
              "type": "object",
              "properties": {
                "items": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "string"
                      },
                      "enabled": {
                        "type": "boolean"
                      }
                    },
                    "required": ["id", "enabled"]
                  }
                }
              },
              "required": ["items"]
            }
          }
        }
      }
    }
  },
  "definitions": {
    "Element": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "enabled": {
          "type": "boolean",
          "default": false
        },
        "extra": {
          "type": "string"
        }
      },
      "required": ["id"]
    }
  }
}
```

</details>

## PatchBodyParametersSchema create-only-patch-property

Reported findings: Swagger **1**, TypeSpec **0**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                     | Target                                                                                                                                                                                                 |
| -------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not be x-ms-mutability: ["create"], property:createOnly. | ["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}", "patch", "parameters", "4", "schema", "properties", "properties"] |
| TypeSpec | No selected findings                                                                                                          | Not applicable                                                                                                                                                                                         |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/create-only-patch-property/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/create-only-patch-property/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/create-only-patch-property/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/create-only-patch-property/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.Versioning;
using Azure.ResourceManager;

@armProviderNamespace
@service(#{ title: "Test Service" })
@versioned(Versions)
@armCommonTypesVersion(CommonTypes.Versions.v5)
namespace Microsoft.TestService;

enum Versions {
  @useDependency(Azure.ResourceManager.CommonTypes.Versions.v5)
  v2024_01_01: "2024-01-01",
}

model Widget is TrackedResource<WidgetProperties> {
  @key("widgetName")
  @segment("widgets")
  @doc("The name of the widget")
  @path
  @pattern("^[a-zA-Z0-9_-]+$")
  name: string;
}

@doc("Widget resource properties.")
model WidgetProperties {
  @doc("Description of the widget")
  description?: string;

  @doc("Resource provisioning state")
  @visibility(Lifecycle.Read)
  provisioningState?: ResourceProvisioningState;
}

@doc("Patch envelope for widget.")
model WidgetPatchBody {
  @doc("Resource properties with a create-only field")
  properties?: WidgetPatchProperties;
}

@doc("Patch properties with a create-only property.")
model WidgetPatchProperties {
  @doc("Create-only property excluded from native PATCH input but retained by schema sharing")
  @visibility(Lifecycle.Create)
  createOnly?: string;
}

interface Operations extends Azure.ResourceManager.Operations {}

@armResourceOperations
interface Widgets {
  get is ArmResourceRead<Widget>;
  createOrUpdate is ArmResourceCreateOrReplaceAsync<Widget>;
  delete is ArmResourceDeleteWithoutOkAsync<Widget>;

  @doc("Update widget")
  @patch
  @armResourceUpdate(Widget)
  update(
    ...ResourceInstanceParameters<Widget>,
    @doc("The request body") @body body: WidgetPatchBody,
  ): ArmResponse<Widget> | ErrorResponse;
}
```

```json
{
  "paths": {
    "/providers/Microsoft.TestService/operations": {
      "get": {
        "operationId": "Operations_List",
        "tags": ["Operations"],
        "description": "List the operations for the provider",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/OperationListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}": {
      "get": {
        "operationId": "Widgets_Get",
        "tags": ["Widgets"],
        "description": "Get a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "put": {
        "operationId": "Widgets_CreateOrUpdate",
        "tags": ["Widgets"],
        "description": "Create a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          },
          {
            "name": "resource",
            "in": "body",
            "description": "Resource create parameters.",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Resource 'Widget' update operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "201": {
            "description": "Resource 'Widget' create operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            },
            "headers": {
              "Azure-AsyncOperation": {
                "type": "string",
                "description": "A link to the status monitor"
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "azure-async-operation"
        },
        "x-ms-long-running-operation": true
      },
      "patch": {
        "operationId": "Widgets_Update",
        "tags": ["Widgets"],
        "description": "Update widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          },
          {
            "name": "body",
            "in": "body",
            "description": "The request body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/WidgetPatchBody"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "delete": {
        "operationId": "Widgets_Delete",
        "tags": ["Widgets"],
        "description": "Delete a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          }
        ],
        "responses": {
          "202": {
            "description": "Resource deletion accepted.",
            "headers": {
              "Location": {
                "type": "string",
                "description": "The Location header contains the URL where the status of the long running operation can be checked."
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "204": {
            "description": "Resource does not exist."
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "location"
        },
        "x-ms-long-running-operation": true
      }
    }
  },
  "definitions": {
    "Azure.ResourceManager.ResourceProvisioningState": {
      "type": "string",
      "description": "The provisioning state of a resource type.",
      "enum": ["Succeeded", "Failed", "Canceled"],
      "x-ms-enum": {
        "name": "ResourceProvisioningState",
        "modelAsString": true,
        "values": [
          {
            "name": "Succeeded",
            "value": "Succeeded",
            "description": "Resource has been created."
          },
          {
            "name": "Failed",
            "value": "Failed",
            "description": "Resource creation failed."
          },
          {
            "name": "Canceled",
            "value": "Canceled",
            "description": "Resource creation was canceled."
          }
        ]
      }
    },
    "Widget": {
      "type": "object",
      "description": "Concrete tracked resource types can be created by aliasing this type using a specific property type.",
      "properties": {
        "properties": {
          "$ref": "#/definitions/WidgetProperties",
          "description": "The resource-specific properties for this resource."
        }
      },
      "allOf": [
        {
          "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/TrackedResource"
        }
      ]
    },
    "WidgetPatchBody": {
      "type": "object",
      "description": "Patch envelope for widget.",
      "properties": {
        "properties": {
          "$ref": "#/definitions/WidgetPatchProperties",
          "description": "Resource properties with a create-only field"
        }
      }
    },
    "WidgetPatchProperties": {
      "type": "object",
      "description": "Patch properties with a create-only property.",
      "properties": {
        "createOnly": {
          "type": "string",
          "description": "Create-only property excluded from native PATCH input but retained by schema sharing",
          "x-ms-mutability": ["create"]
        }
      }
    },
    "WidgetProperties": {
      "type": "object",
      "description": "Widget resource properties.",
      "properties": {
        "description": {
          "type": "string",
          "description": "Description of the widget"
        },
        "provisioningState": {
          "$ref": "#/definitions/Azure.ResourceManager.ResourceProvisioningState",
          "description": "Resource provisioning state",
          "readOnly": true
        }
      }
    }
  }
}
```

</details>

## PatchBodyParametersSchema create-visibility-override

Reported findings: Swagger **4**, TypeSpec **1**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                      | Target                                                             |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not have default value, property:id.                                      | ["paths", "/widgets", "patch", "parameters", "0", "schema"]        |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not be required, property:id.                                             | ["paths", "/widgets", "patch", "parameters", "0", "schema"]        |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not be x-ms-mutability: ["create"], property:createdBy.                   | ["paths", "/widgets", "patch", "parameters", "0", "schema"]        |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not be required, property:name.                                           | ["paths", "/widgets", "patch", "parameters", "0", "schema"]        |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: PATCH request body property 'createdBy' must include Lifecycle.Update visibility. | Authored semantic target; no location serialized in saved snapshot |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/create-visibility-override/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/create-visibility-override/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/create-visibility-override/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/create-visibility-override/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using Azure.ResourceManager;

@armProviderNamespace
@service
namespace Microsoft.TestService;

model PatchBody {
  @visibility(Lifecycle.Read)
  id: string = "server";

  @visibility(Lifecycle.Create)
  createdBy?: string;

  @visibility(Lifecycle.Update)
  name: string;
}

@route("/widgets")
@parameterVisibility(Lifecycle.Create)
@patch
op update(@body body: PatchBody): void;
```

```json
{
  "paths": {
    "/widgets": {
      "patch": {
        "operationId": "Update",
        "parameters": [
          {
            "name": "body",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/PatchBody"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "There is no content to send for this request, but the headers may be useful. "
          }
        }
      }
    }
  },
  "definitions": {
    "PatchBody": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "default": "server",
          "readOnly": true
        },
        "createdBy": {
          "type": "string",
          "x-ms-mutability": ["create"]
        },
        "name": {
          "type": "string",
          "x-ms-mutability": ["update"]
        }
      },
      "required": ["id", "name"]
    }
  }
}
```

</details>

## PatchBodyParametersSchema default-patch-property

Reported findings: Swagger **1**, TypeSpec **8**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                                                                        | Target                                                                                                                                                                                                 |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not have default value, property:mode.                                                                                      | ["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}", "patch", "parameters", "4", "schema", "properties", "properties"] |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: Properties of a PATCH request body must not have default value, property:properties.mode.                                           | Authored semantic target; no location serialized in saved snapshot                                                                                                                                     |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'properties.mode' in the request body either does not appear in the resource model or is nested at the wrong level.    | Authored semantic target; no location serialized in saved snapshot                                                                                                                                     |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: Properties of a PATCH request body must not have default value, property:properties.enabled.                                        | Authored semantic target; no location serialized in saved snapshot                                                                                                                                     |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'properties.enabled' in the request body either does not appear in the resource model or is nested at the wrong level. | Authored semantic target; no location serialized in saved snapshot                                                                                                                                     |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: Properties of a PATCH request body must not have default value, property:properties.count.                                          | Authored semantic target; no location serialized in saved snapshot                                                                                                                                     |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'properties.count' in the request body either does not appear in the resource model or is nested at the wrong level.   | Authored semantic target; no location serialized in saved snapshot                                                                                                                                     |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: Properties of a PATCH request body must not have default value, property:properties.label.                                          | Authored semantic target; no location serialized in saved snapshot                                                                                                                                     |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'properties.label' in the request body either does not appear in the resource model or is nested at the wrong level.   | Authored semantic target; no location serialized in saved snapshot                                                                                                                                     |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/default-patch-property/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/default-patch-property/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/default-patch-property/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/default-patch-property/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.Versioning;
using Azure.ResourceManager;

@armProviderNamespace
@service(#{ title: "Test Service" })
@versioned(Versions)
@armCommonTypesVersion(CommonTypes.Versions.v5)
namespace Microsoft.TestService;

enum Versions {
  @useDependency(Azure.ResourceManager.CommonTypes.Versions.v5)
  v2024_01_01: "2024-01-01",
}

model Widget is TrackedResource<WidgetProperties> {
  @key("widgetName")
  @segment("widgets")
  @doc("The name of the widget")
  @path
  @pattern("^[a-zA-Z0-9_-]+$")
  name: string;
}

@doc("Widget resource properties.")
model WidgetProperties {
  @doc("Description of the widget")
  description?: string;

  @doc("Resource provisioning state")
  @visibility(Lifecycle.Read)
  provisioningState?: ResourceProvisioningState;
}

@doc("Patch envelope for widget.")
model WidgetPatchBody {
  @doc("Resource properties with a defaulted field")
  properties?: WidgetPatchProperties;
}

@doc("Patch properties with a defaulted property.")
model WidgetPatchProperties {
  @doc("Mode default in patch body -- violates rule")
  mode?: string = "enabled";

  @doc("Falsy boolean default in patch body -- violates rule")
  enabled?: boolean = false;

  @doc("Falsy numeric default in patch body -- violates rule")
  count?: int32 = 0;

  @doc("Falsy string default in patch body -- violates rule")
  label?: string = "";
}

interface Operations extends Azure.ResourceManager.Operations {}

@armResourceOperations
interface Widgets {
  get is ArmResourceRead<Widget>;
  createOrUpdate is ArmResourceCreateOrReplaceAsync<Widget>;
  delete is ArmResourceDeleteWithoutOkAsync<Widget>;

  @doc("Update widget")
  @patch
  @armResourceUpdate(Widget)
  update(
    ...ResourceInstanceParameters<Widget>,
    @doc("The request body") @body body: WidgetPatchBody,
  ): ArmResponse<Widget> | ErrorResponse;
}
```

```json
{
  "paths": {
    "/providers/Microsoft.TestService/operations": {
      "get": {
        "operationId": "Operations_List",
        "tags": ["Operations"],
        "description": "List the operations for the provider",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/OperationListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}": {
      "get": {
        "operationId": "Widgets_Get",
        "tags": ["Widgets"],
        "description": "Get a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "put": {
        "operationId": "Widgets_CreateOrUpdate",
        "tags": ["Widgets"],
        "description": "Create a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          },
          {
            "name": "resource",
            "in": "body",
            "description": "Resource create parameters.",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Resource 'Widget' update operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "201": {
            "description": "Resource 'Widget' create operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            },
            "headers": {
              "Azure-AsyncOperation": {
                "type": "string",
                "description": "A link to the status monitor"
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "azure-async-operation"
        },
        "x-ms-long-running-operation": true
      },
      "patch": {
        "operationId": "Widgets_Update",
        "tags": ["Widgets"],
        "description": "Update widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          },
          {
            "name": "body",
            "in": "body",
            "description": "The request body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/WidgetPatchBody"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "delete": {
        "operationId": "Widgets_Delete",
        "tags": ["Widgets"],
        "description": "Delete a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          }
        ],
        "responses": {
          "202": {
            "description": "Resource deletion accepted.",
            "headers": {
              "Location": {
                "type": "string",
                "description": "The Location header contains the URL where the status of the long running operation can be checked."
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "204": {
            "description": "Resource does not exist."
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "location"
        },
        "x-ms-long-running-operation": true
      }
    }
  },
  "definitions": {
    "Azure.ResourceManager.ResourceProvisioningState": {
      "type": "string",
      "description": "The provisioning state of a resource type.",
      "enum": ["Succeeded", "Failed", "Canceled"],
      "x-ms-enum": {
        "name": "ResourceProvisioningState",
        "modelAsString": true,
        "values": [
          {
            "name": "Succeeded",
            "value": "Succeeded",
            "description": "Resource has been created."
          },
          {
            "name": "Failed",
            "value": "Failed",
            "description": "Resource creation failed."
          },
          {
            "name": "Canceled",
            "value": "Canceled",
            "description": "Resource creation was canceled."
          }
        ]
      }
    },
    "Widget": {
      "type": "object",
      "description": "Concrete tracked resource types can be created by aliasing this type using a specific property type.",
      "properties": {
        "properties": {
          "$ref": "#/definitions/WidgetProperties",
          "description": "The resource-specific properties for this resource."
        }
      },
      "allOf": [
        {
          "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/TrackedResource"
        }
      ]
    },
    "WidgetPatchBody": {
      "type": "object",
      "description": "Patch envelope for widget.",
      "properties": {
        "properties": {
          "$ref": "#/definitions/WidgetPatchProperties",
          "description": "Resource properties with a defaulted field"
        }
      }
    },
    "WidgetPatchProperties": {
      "type": "object",
      "description": "Patch properties with a defaulted property.",
      "properties": {
        "mode": {
          "type": "string",
          "description": "Mode default in patch body -- violates rule",
          "default": "enabled"
        },
        "enabled": {
          "type": "boolean",
          "description": "Falsy boolean default in patch body -- violates rule",
          "default": false
        },
        "count": {
          "type": "integer",
          "format": "int32",
          "description": "Falsy numeric default in patch body -- violates rule",
          "default": 0
        },
        "label": {
          "type": "string",
          "description": "Falsy string default in patch body -- violates rule",
          "default": ""
        }
      }
    },
    "WidgetProperties": {
      "type": "object",
      "description": "Widget resource properties.",
      "properties": {
        "description": {
          "type": "string",
          "description": "Description of the widget"
        },
        "provisioningState": {
          "$ref": "#/definitions/Azure.ResourceManager.ResourceProvisioningState",
          "description": "Resource provisioning state",
          "readOnly": true
        }
      }
    }
  }
}
```

</details>

## PatchBodyParametersSchema discriminator-required-patch-property

Reported findings: Swagger **3**, TypeSpec **4**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                                                                                 | Target                                                                                                                                                                                                             |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not be required, property:kind.                                                                                                      | ["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}", "patch", "parameters", "4", "schema", "properties", "inheritedDiscriminator"] |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not be required, property:kind.                                                                                                      | ["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}", "patch", "parameters", "4", "schema", "properties", "optional"]               |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not be required, property:kind.                                                                                                      | ["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}", "patch", "parameters", "4", "schema", "properties", "synthesized"]            |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'optional.kind' in the request body either does not appear in the resource model or is nested at the wrong level.               | Authored semantic target; no location serialized in saved snapshot                                                                                                                                                 |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'synthesized' in the request body either does not appear in the resource model or is nested at the wrong level.                 | Authored semantic target; no location serialized in saved snapshot                                                                                                                                                 |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: Properties of a PATCH request body must not be required, property:inheritedDiscriminator.kind.                                               | Authored semantic target; no location serialized in saved snapshot                                                                                                                                                 |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'inheritedDiscriminator.kind' in the request body either does not appear in the resource model or is nested at the wrong level. | Authored semantic target; no location serialized in saved snapshot                                                                                                                                                 |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/discriminator-required-patch-property/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/discriminator-required-patch-property/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/discriminator-required-patch-property/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/discriminator-required-patch-property/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.Versioning;
using Azure.ResourceManager;

@armProviderNamespace
@service(#{ title: "Test Service" })
@versioned(Versions)
@armCommonTypesVersion(CommonTypes.Versions.v5)
namespace Microsoft.TestService;

enum Versions {
  @useDependency(Azure.ResourceManager.CommonTypes.Versions.v5)
  v2024_01_01: "2024-01-01",
}

@discriminator("kind")
model OptionalDiscriminator {
  @doc("An authored optional discriminator emitted as required")
  kind?: string;
}

@discriminator("kind")
model SynthesizedDiscriminator {}

@discriminator("kind")
model BaseSynthesizedDiscriminator {}

model DerivedDiscriminator extends BaseSynthesizedDiscriminator {
  @doc("An inherited discriminator value emitted as required")
  kind: "derived";
}

model Widget is TrackedResource<WidgetProperties> {
  @key("widgetName")
  @segment("widgets")
  @doc("The name of the widget")
  @path
  @pattern("^[a-zA-Z0-9_-]+$")
  name: string;
}

@doc("Widget resource properties.")
model WidgetProperties {
  @doc("Description of the widget")
  description?: string;

  @doc("Resource provisioning state")
  @visibility(Lifecycle.Read)
  provisioningState?: ResourceProvisioningState;
}

@doc("Patch envelope for widget.")
model WidgetPatchBody {
  @doc("A model with an authored optional discriminator")
  optional?: OptionalDiscriminator;

  @doc("A model whose discriminator is synthesized by Autorest")
  synthesized?: SynthesizedDiscriminator;

  @doc("A derived model with an inherited discriminator declaration")
  inheritedDiscriminator?: DerivedDiscriminator;
}

interface Operations extends Azure.ResourceManager.Operations {}

@armResourceOperations
interface Widgets {
  get is ArmResourceRead<Widget>;
  createOrUpdate is ArmResourceCreateOrReplaceAsync<Widget>;
  delete is ArmResourceDeleteWithoutOkAsync<Widget>;

  @doc("Update widget")
  @patch
  @armResourceUpdate(Widget)
  update(
    ...ResourceInstanceParameters<Widget>,
    @doc("The request body") @body body: WidgetPatchBody,
  ): ArmResponse<Widget> | ErrorResponse;
}
```

```json
{
  "paths": {
    "/providers/Microsoft.TestService/operations": {
      "get": {
        "operationId": "Operations_List",
        "tags": ["Operations"],
        "description": "List the operations for the provider",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/OperationListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}": {
      "get": {
        "operationId": "Widgets_Get",
        "tags": ["Widgets"],
        "description": "Get a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "put": {
        "operationId": "Widgets_CreateOrUpdate",
        "tags": ["Widgets"],
        "description": "Create a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          },
          {
            "name": "resource",
            "in": "body",
            "description": "Resource create parameters.",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Resource 'Widget' update operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "201": {
            "description": "Resource 'Widget' create operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            },
            "headers": {
              "Azure-AsyncOperation": {
                "type": "string",
                "description": "A link to the status monitor"
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "azure-async-operation"
        },
        "x-ms-long-running-operation": true
      },
      "patch": {
        "operationId": "Widgets_Update",
        "tags": ["Widgets"],
        "description": "Update widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          },
          {
            "name": "body",
            "in": "body",
            "description": "The request body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/WidgetPatchBody"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "delete": {
        "operationId": "Widgets_Delete",
        "tags": ["Widgets"],
        "description": "Delete a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          }
        ],
        "responses": {
          "202": {
            "description": "Resource deletion accepted.",
            "headers": {
              "Location": {
                "type": "string",
                "description": "The Location header contains the URL where the status of the long running operation can be checked."
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "204": {
            "description": "Resource does not exist."
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "location"
        },
        "x-ms-long-running-operation": true
      }
    }
  },
  "definitions": {
    "Azure.ResourceManager.ResourceProvisioningState": {
      "type": "string",
      "description": "The provisioning state of a resource type.",
      "enum": ["Succeeded", "Failed", "Canceled"],
      "x-ms-enum": {
        "name": "ResourceProvisioningState",
        "modelAsString": true,
        "values": [
          {
            "name": "Succeeded",
            "value": "Succeeded",
            "description": "Resource has been created."
          },
          {
            "name": "Failed",
            "value": "Failed",
            "description": "Resource creation failed."
          },
          {
            "name": "Canceled",
            "value": "Canceled",
            "description": "Resource creation was canceled."
          }
        ]
      }
    },
    "BaseSynthesizedDiscriminator": {
      "type": "object",
      "properties": {
        "kind": {
          "type": "string",
          "description": "Discriminator property for BaseSynthesizedDiscriminator."
        }
      },
      "discriminator": "kind",
      "required": ["kind"]
    },
    "DerivedDiscriminator": {
      "type": "object",
      "allOf": [
        {
          "$ref": "#/definitions/BaseSynthesizedDiscriminator"
        }
      ],
      "x-ms-discriminator-value": "derived"
    },
    "OptionalDiscriminator": {
      "type": "object",
      "properties": {
        "kind": {
          "type": "string",
          "description": "An authored optional discriminator emitted as required"
        }
      },
      "discriminator": "kind",
      "required": ["kind"]
    },
    "SynthesizedDiscriminator": {
      "type": "object",
      "properties": {
        "kind": {
          "type": "string",
          "description": "Discriminator property for SynthesizedDiscriminator."
        }
      },
      "discriminator": "kind",
      "required": ["kind"]
    },
    "Widget": {
      "type": "object",
      "description": "Concrete tracked resource types can be created by aliasing this type using a specific property type.",
      "properties": {
        "properties": {
          "$ref": "#/definitions/WidgetProperties",
          "description": "The resource-specific properties for this resource."
        }
      },
      "allOf": [
        {
          "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/TrackedResource"
        }
      ]
    },
    "WidgetPatchBody": {
      "type": "object",
      "description": "Patch envelope for widget.",
      "properties": {
        "optional": {
          "$ref": "#/definitions/OptionalDiscriminator",
          "description": "A model with an authored optional discriminator"
        },
        "synthesized": {
          "$ref": "#/definitions/SynthesizedDiscriminator",
          "description": "A model whose discriminator is synthesized by Autorest"
        },
        "inheritedDiscriminator": {
          "$ref": "#/definitions/DerivedDiscriminator",
          "description": "A derived model with an inherited discriminator declaration"
        }
      }
    },
    "WidgetProperties": {
      "type": "object",
      "description": "Widget resource properties.",
      "properties": {
        "description": {
          "type": "string",
          "description": "Description of the widget"
        },
        "provisioningState": {
          "$ref": "#/definitions/Azure.ResourceManager.ResourceProvisioningState",
          "description": "Resource provisioning state",
          "readOnly": true
        }
      }
    }
  }
}
```

</details>

## PatchBodyParametersSchema encoded-identity-compliant

Reported findings: Swagger **0**, TypeSpec **1**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                                                                          | Target                                                             |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Swagger  | No selected findings                                                                                                                                                                               | Not applicable                                                     |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'identity.principalId' in the request body either does not appear in the resource model or is nested at the wrong level. | Authored semantic target; no location serialized in saved snapshot |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/encoded-identity-compliant/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/encoded-identity-compliant/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/encoded-identity-compliant/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/encoded-identity-compliant/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.Versioning;
using Azure.ResourceManager;

@armProviderNamespace
@service(#{ title: "Test Service" })
@versioned(Versions)
@armCommonTypesVersion(CommonTypes.Versions.v5)
namespace Microsoft.TestService;

enum Versions {
  @useDependency(Azure.ResourceManager.CommonTypes.Versions.v5)
  v2024_01_01: "2024-01-01",
}

model Widget is TrackedResource<WidgetProperties> {
  @key("widgetName")
  @segment("widgets")
  @doc("The name of the widget")
  @path
  @pattern("^[a-zA-Z0-9_-]+$")
  name: string;
}

@doc("Widget resource properties.")
model WidgetProperties {
  @doc("Description of the widget")
  description?: string;
}

@doc("Custom identity model.")
model CustomIdentity {
  @doc("Required identity field that Swagger skips under top-level identity")
  principalId: string;
}

@doc("Patch envelope for widget.")
model WidgetPatchBody {
  @doc("Encoded top-level identity is skipped by the Swagger rule")
  @encodedName("application/json", "identity")
  customIdentity: CustomIdentity;
}

interface Operations extends Azure.ResourceManager.Operations {}

@armResourceOperations
interface Widgets {
  get is ArmResourceRead<Widget>;
  createOrUpdate is ArmResourceCreateOrReplaceAsync<Widget>;
  delete is ArmResourceDeleteWithoutOkAsync<Widget>;

  @doc("Update widget")
  @patch
  @armResourceUpdate(Widget)
  update(
    ...ResourceInstanceParameters<Widget>,
    @doc("The request body") @body body: WidgetPatchBody,
  ): ArmResponse<Widget> | ErrorResponse;
}
```

```json
{
  "paths": {
    "/providers/Microsoft.TestService/operations": {
      "get": {
        "operationId": "Operations_List",
        "tags": ["Operations"],
        "description": "List the operations for the provider",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/OperationListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}": {
      "get": {
        "operationId": "Widgets_Get",
        "tags": ["Widgets"],
        "description": "Get a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "put": {
        "operationId": "Widgets_CreateOrUpdate",
        "tags": ["Widgets"],
        "description": "Create a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          },
          {
            "name": "resource",
            "in": "body",
            "description": "Resource create parameters.",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Resource 'Widget' update operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "201": {
            "description": "Resource 'Widget' create operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            },
            "headers": {
              "Azure-AsyncOperation": {
                "type": "string",
                "description": "A link to the status monitor"
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "azure-async-operation"
        },
        "x-ms-long-running-operation": true
      },
      "patch": {
        "operationId": "Widgets_Update",
        "tags": ["Widgets"],
        "description": "Update widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          },
          {
            "name": "body",
            "in": "body",
            "description": "The request body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/WidgetPatchBody"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "delete": {
        "operationId": "Widgets_Delete",
        "tags": ["Widgets"],
        "description": "Delete a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          }
        ],
        "responses": {
          "202": {
            "description": "Resource deletion accepted.",
            "headers": {
              "Location": {
                "type": "string",
                "description": "The Location header contains the URL where the status of the long running operation can be checked."
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "204": {
            "description": "Resource does not exist."
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "location"
        },
        "x-ms-long-running-operation": true
      }
    }
  },
  "definitions": {
    "CustomIdentity": {
      "type": "object",
      "description": "Custom identity model.",
      "properties": {
        "principalId": {
          "type": "string",
          "description": "Required identity field that Swagger skips under top-level identity"
        }
      },
      "required": ["principalId"]
    },
    "Widget": {
      "type": "object",
      "description": "Concrete tracked resource types can be created by aliasing this type using a specific property type.",
      "properties": {
        "properties": {
          "$ref": "#/definitions/WidgetProperties",
          "description": "The resource-specific properties for this resource."
        }
      },
      "allOf": [
        {
          "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/TrackedResource"
        }
      ]
    },
    "WidgetPatchBody": {
      "type": "object",
      "description": "Patch envelope for widget.",
      "properties": {
        "identity": {
          "$ref": "#/definitions/CustomIdentity",
          "description": "Encoded top-level identity is skipped by the Swagger rule",
          "x-ms-client-name": "customIdentity"
        }
      },
      "required": ["identity"]
    },
    "WidgetProperties": {
      "type": "object",
      "description": "Widget resource properties.",
      "properties": {
        "description": {
          "type": "string",
          "description": "Description of the widget"
        }
      }
    }
  }
}
```

</details>

## PatchBodyParametersSchema encoded-non-identity-violating

Reported findings: Swagger **2**, TypeSpec **3**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                                                                                | Target                                                                                                                                                                                                     |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not be required, property:principalId.                                                                                              | ["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}", "patch", "parameters", "4", "schema", "properties", "customIdentity"] |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not be required, property:customIdentity.                                                                                           | ["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}", "patch", "parameters", "4", "schema"]                                 |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: Properties of a PATCH request body must not be required, property:customIdentity.                                                           | Authored semantic target; no location serialized in saved snapshot                                                                                                                                         |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: Properties of a PATCH request body must not be required, property:customIdentity.principalId.                                               | Authored semantic target; no location serialized in saved snapshot                                                                                                                                         |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'customIdentity.principalId' in the request body either does not appear in the resource model or is nested at the wrong level. | Authored semantic target; no location serialized in saved snapshot                                                                                                                                         |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/encoded-non-identity-violating/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/encoded-non-identity-violating/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/encoded-non-identity-violating/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/encoded-non-identity-violating/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.Versioning;
using Azure.ResourceManager;

@armProviderNamespace
@service(#{ title: "Test Service" })
@versioned(Versions)
@armCommonTypesVersion(CommonTypes.Versions.v5)
namespace Microsoft.TestService;

enum Versions {
  @useDependency(Azure.ResourceManager.CommonTypes.Versions.v5)
  v2024_01_01: "2024-01-01",
}

model Widget is TrackedResource<WidgetProperties> {
  @key("widgetName")
  @segment("widgets")
  @doc("The name of the widget")
  @path
  @pattern("^[a-zA-Z0-9_-]+$")
  name: string;
}

@doc("Widget resource properties.")
model WidgetProperties {
  @doc("Description of the widget")
  description?: string;
}

@doc("Custom identity model.")
model CustomIdentity {
  @doc("Required property in emitted non-identity envelope — violates rule")
  principalId: string;
}

@doc("Patch envelope for widget.")
model WidgetPatchBody {
  @doc("Authored identity encoded away from identity is checked by the Swagger rule")
  @encodedName("application/json", "customIdentity")
  identity: CustomIdentity;
}

interface Operations extends Azure.ResourceManager.Operations {}

@armResourceOperations
interface Widgets {
  get is ArmResourceRead<Widget>;
  createOrUpdate is ArmResourceCreateOrReplaceAsync<Widget>;
  delete is ArmResourceDeleteWithoutOkAsync<Widget>;

  @doc("Update widget")
  @patch
  @armResourceUpdate(Widget)
  update(
    ...ResourceInstanceParameters<Widget>,
    @doc("The request body") @body body: WidgetPatchBody,
  ): ArmResponse<Widget> | ErrorResponse;
}
```

```json
{
  "paths": {
    "/providers/Microsoft.TestService/operations": {
      "get": {
        "operationId": "Operations_List",
        "tags": ["Operations"],
        "description": "List the operations for the provider",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/OperationListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}": {
      "get": {
        "operationId": "Widgets_Get",
        "tags": ["Widgets"],
        "description": "Get a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "put": {
        "operationId": "Widgets_CreateOrUpdate",
        "tags": ["Widgets"],
        "description": "Create a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          },
          {
            "name": "resource",
            "in": "body",
            "description": "Resource create parameters.",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Resource 'Widget' update operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "201": {
            "description": "Resource 'Widget' create operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            },
            "headers": {
              "Azure-AsyncOperation": {
                "type": "string",
                "description": "A link to the status monitor"
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "azure-async-operation"
        },
        "x-ms-long-running-operation": true
      },
      "patch": {
        "operationId": "Widgets_Update",
        "tags": ["Widgets"],
        "description": "Update widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          },
          {
            "name": "body",
            "in": "body",
            "description": "The request body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/WidgetPatchBody"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "delete": {
        "operationId": "Widgets_Delete",
        "tags": ["Widgets"],
        "description": "Delete a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          }
        ],
        "responses": {
          "202": {
            "description": "Resource deletion accepted.",
            "headers": {
              "Location": {
                "type": "string",
                "description": "The Location header contains the URL where the status of the long running operation can be checked."
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "204": {
            "description": "Resource does not exist."
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "location"
        },
        "x-ms-long-running-operation": true
      }
    }
  },
  "definitions": {
    "CustomIdentity": {
      "type": "object",
      "description": "Custom identity model.",
      "properties": {
        "principalId": {
          "type": "string",
          "description": "Required property in emitted non-identity envelope \u2014 violates rule"
        }
      },
      "required": ["principalId"]
    },
    "Widget": {
      "type": "object",
      "description": "Concrete tracked resource types can be created by aliasing this type using a specific property type.",
      "properties": {
        "properties": {
          "$ref": "#/definitions/WidgetProperties",
          "description": "The resource-specific properties for this resource."
        }
      },
      "allOf": [
        {
          "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/TrackedResource"
        }
      ]
    },
    "WidgetPatchBody": {
      "type": "object",
      "description": "Patch envelope for widget.",
      "properties": {
        "customIdentity": {
          "$ref": "#/definitions/CustomIdentity",
          "description": "Authored identity encoded away from identity is checked by the Swagger rule",
          "x-ms-client-name": "identity"
        }
      },
      "required": ["customIdentity"]
    },
    "WidgetProperties": {
      "type": "object",
      "description": "Widget resource properties.",
      "properties": {
        "description": {
          "type": "string",
          "description": "Description of the widget"
        }
      }
    }
  }
}
```

</details>

## PatchBodyParametersSchema native-discriminator-compliant

Reported findings: Swagger **3**, TypeSpec **0**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                            | Target                                                                                |
| -------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not be required, property:kind. | ["paths", "/widgets", "patch", "parameters", "0", "schema", "properties", "absent"]   |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not be required, property:kind. | ["paths", "/widgets", "patch", "parameters", "0", "schema", "properties", "excluded"] |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not be required, property:kind. | ["paths", "/widgets", "patch", "parameters", "0", "schema", "properties", "optional"] |
| TypeSpec | No selected findings                                                                                 | Not applicable                                                                        |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/native-discriminator-compliant/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/native-discriminator-compliant/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/native-discriminator-compliant/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/native-discriminator-compliant/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using Azure.ResourceManager;

@armProviderNamespace
@service
namespace Microsoft.TestService;

@discriminator("kind")
model AbsentDiscriminator {}

@discriminator("kind")
model OptionalDiscriminator {
  kind?: string;
}

@discriminator("kind")
model ExcludedDiscriminator {
  @visibility(Lifecycle.Read)
  kind: string;

  name?: string;
}

model PatchBody {
  absent?: AbsentDiscriminator;
  optional?: OptionalDiscriminator;
  excluded?: ExcludedDiscriminator;
}

@route("/widgets")
@patch
op update(@body body: PatchBody): void;
```

```json
{
  "paths": {
    "/widgets": {
      "patch": {
        "operationId": "Update",
        "parameters": [
          {
            "name": "body",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/PatchBody"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "There is no content to send for this request, but the headers may be useful. "
          }
        }
      }
    }
  },
  "definitions": {
    "AbsentDiscriminator": {
      "type": "object",
      "properties": {
        "kind": {
          "type": "string",
          "description": "Discriminator property for AbsentDiscriminator."
        }
      },
      "discriminator": "kind",
      "required": ["kind"]
    },
    "ExcludedDiscriminator": {
      "type": "object",
      "properties": {
        "kind": {
          "type": "string",
          "readOnly": true
        },
        "name": {
          "type": "string"
        }
      },
      "discriminator": "kind",
      "required": ["kind"]
    },
    "OptionalDiscriminator": {
      "type": "object",
      "properties": {
        "kind": {
          "type": "string"
        }
      },
      "discriminator": "kind",
      "required": ["kind"]
    },
    "PatchBody": {
      "type": "object",
      "properties": {
        "absent": {
          "$ref": "#/definitions/AbsentDiscriminator"
        },
        "optional": {
          "$ref": "#/definitions/OptionalDiscriminator"
        },
        "excluded": {
          "$ref": "#/definitions/ExcludedDiscriminator"
        }
      }
    }
  }
}
```

</details>

## PatchBodyParametersSchema native-visibility-compliant

Reported findings: Swagger **4**, TypeSpec **3**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                           | Target                                                             |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not have default value, property:id.                                           | ["paths", "/defaults", "patch", "parameters", "0", "schema"]       |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not be required, property:id.                                                  | ["paths", "/defaults", "patch", "parameters", "0", "schema"]       |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not be required, property:id.                                                  | ["paths", "/widgets", "patch", "parameters", "0", "schema"]        |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not be x-ms-mutability: ["create"], property:createdBy.                        | ["paths", "/widgets", "patch", "parameters", "0", "schema"]        |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: PATCH request body property 'name' is immutable and must be excluded from PATCH input. | Authored semantic target; no location serialized in saved snapshot |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: PATCH request body property 'name' is immutable and must be excluded from PATCH input. | Authored semantic target; no location serialized in saved snapshot |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: PATCH request body property 'name' is immutable and must be excluded from PATCH input. | Authored semantic target; no location serialized in saved snapshot |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/native-visibility-compliant/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/native-visibility-compliant/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/native-visibility-compliant/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/native-visibility-compliant/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using Azure.ResourceManager;

@armProviderNamespace
@service
namespace Microsoft.TestService;

model PatchBody {
  @visibility(Lifecycle.Read)
  id: string;

  @visibility(Lifecycle.Create)
  createdBy?: string;

  name?: string;
}

model AugmentedPatchBody {
  ...PatchBody;

  @visibility(Lifecycle.Read, Lifecycle.Query)
  unrelated?: string;
}

model DefaultPatchBody {
  @visibility(Lifecycle.Read)
  id: string = "server";

  name?: string;
}

@route("/widgets")
@patch
op update(@body body: PatchBody): void;

@route("/augmented")
@patch
op updateAugmented(@body body: AugmentedPatchBody): void;

@route("/defaults")
@patch
op updateDefaults(@body body: DefaultPatchBody): void;
```

```json
{
  "paths": {
    "/augmented": {
      "patch": {
        "operationId": "UpdateAugmented",
        "parameters": [
          {
            "name": "body",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/AugmentedPatchBody"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "There is no content to send for this request, but the headers may be useful. "
          }
        }
      }
    },
    "/defaults": {
      "patch": {
        "operationId": "UpdateDefaults",
        "parameters": [
          {
            "name": "body",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/DefaultPatchBody"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "There is no content to send for this request, but the headers may be useful. "
          }
        }
      }
    },
    "/widgets": {
      "patch": {
        "operationId": "Update",
        "parameters": [
          {
            "name": "body",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/PatchBody"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "There is no content to send for this request, but the headers may be useful. "
          }
        }
      }
    }
  },
  "definitions": {
    "AugmentedPatchBody": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        }
      }
    },
    "DefaultPatchBody": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "default": "server",
          "readOnly": true
        },
        "name": {
          "type": "string"
        }
      },
      "required": ["id"]
    },
    "PatchBody": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "readOnly": true
        },
        "createdBy": {
          "type": "string",
          "x-ms-mutability": ["create"]
        },
        "name": {
          "type": "string"
        }
      },
      "required": ["id"]
    }
  }
}
```

</details>

## PatchBodyParametersSchema nullable-body-required-property

Reported findings: Swagger **1**, TypeSpec **2**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                                                                  | Target                                                                                                                                                                     |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not be required, property:requiredProp.                                                                               | ["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}", "patch", "parameters", "4", "schema"] |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: Properties of a PATCH request body must not be required, property:requiredProp.                                               | Authored semantic target; no location serialized in saved snapshot                                                                                                         |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'requiredProp' in the request body either does not appear in the resource model or is nested at the wrong level. | Authored semantic target; no location serialized in saved snapshot                                                                                                         |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/nullable-body-required-property/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/nullable-body-required-property/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/nullable-body-required-property/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/nullable-body-required-property/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.Versioning;
using Azure.ResourceManager;

@armProviderNamespace
@service(#{ title: "Test Service" })
@versioned(Versions)
@armCommonTypesVersion(CommonTypes.Versions.v5)
namespace Microsoft.TestService;

enum Versions {
  @useDependency(Azure.ResourceManager.CommonTypes.Versions.v5)
  v2024_01_01: "2024-01-01",
}

model Widget is TrackedResource<WidgetProperties> {
  @key("widgetName")
  @segment("widgets")
  @doc("The name of the widget")
  @path
  @pattern("^[a-zA-Z0-9_-]+$")
  name: string;
}

@doc("Widget resource properties.")
model WidgetProperties {
  @doc("Description of the widget")
  description?: string;
}

@doc("Patch envelope for widget.")
model WidgetPatchBody {
  @doc("Required property in patch body — violates rule")
  requiredProp: string;
}

interface Operations extends Azure.ResourceManager.Operations {}

@armResourceOperations
interface Widgets {
  get is ArmResourceRead<Widget>;
  createOrUpdate is ArmResourceCreateOrReplaceAsync<Widget>;
  delete is ArmResourceDeleteWithoutOkAsync<Widget>;

  @doc("Update widget")
  @patch
  @armResourceUpdate(Widget)
  update(
    ...ResourceInstanceParameters<Widget>,
    @doc("Nullable request body") @body body: WidgetPatchBody | null,
  ): ArmResponse<Widget> | ErrorResponse;
}
```

```json
{
  "paths": {
    "/providers/Microsoft.TestService/operations": {
      "get": {
        "operationId": "Operations_List",
        "tags": ["Operations"],
        "description": "List the operations for the provider",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/OperationListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}": {
      "get": {
        "operationId": "Widgets_Get",
        "tags": ["Widgets"],
        "description": "Get a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "put": {
        "operationId": "Widgets_CreateOrUpdate",
        "tags": ["Widgets"],
        "description": "Create a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          },
          {
            "name": "resource",
            "in": "body",
            "description": "Resource create parameters.",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Resource 'Widget' update operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "201": {
            "description": "Resource 'Widget' create operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            },
            "headers": {
              "Azure-AsyncOperation": {
                "type": "string",
                "description": "A link to the status monitor"
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "azure-async-operation"
        },
        "x-ms-long-running-operation": true
      },
      "patch": {
        "operationId": "Widgets_Update",
        "tags": ["Widgets"],
        "description": "Update widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          },
          {
            "name": "body",
            "in": "body",
            "description": "Nullable request body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/WidgetPatchBody",
              "x-nullable": true
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "delete": {
        "operationId": "Widgets_Delete",
        "tags": ["Widgets"],
        "description": "Delete a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          }
        ],
        "responses": {
          "202": {
            "description": "Resource deletion accepted.",
            "headers": {
              "Location": {
                "type": "string",
                "description": "The Location header contains the URL where the status of the long running operation can be checked."
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "204": {
            "description": "Resource does not exist."
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "location"
        },
        "x-ms-long-running-operation": true
      }
    }
  },
  "definitions": {
    "Widget": {
      "type": "object",
      "description": "Concrete tracked resource types can be created by aliasing this type using a specific property type.",
      "properties": {
        "properties": {
          "$ref": "#/definitions/WidgetProperties",
          "description": "The resource-specific properties for this resource."
        }
      },
      "allOf": [
        {
          "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/TrackedResource"
        }
      ]
    },
    "WidgetPatchBody": {
      "type": "object",
      "description": "Patch envelope for widget.",
      "properties": {
        "requiredProp": {
          "type": "string",
          "description": "Required property in patch body \u2014 violates rule"
        }
      },
      "required": ["requiredProp"]
    },
    "WidgetProperties": {
      "type": "object",
      "description": "Widget resource properties.",
      "properties": {
        "description": {
          "type": "string",
          "description": "Description of the widget"
        }
      }
    }
  }
}
```

</details>

## PatchBodyParametersSchema nullable-model-required-property

Reported findings: Swagger **1**, TypeSpec **2**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                                                                          | Target                                                                                                                                                                                              |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Swagger  | `PatchBodyParametersSchema`: Properties of a PATCH request body must not be required, property:requiredProp.                                                                                       | ["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}", "patch", "parameters", "4", "schema", "properties", "details"] |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: Properties of a PATCH request body must not be required, property:details.requiredProp.                                               | Authored semantic target; no location serialized in saved snapshot                                                                                                                                  |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'details.requiredProp' in the request body either does not appear in the resource model or is nested at the wrong level. | Authored semantic target; no location serialized in saved snapshot                                                                                                                                  |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/nullable-model-required-property/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/nullable-model-required-property/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/nullable-model-required-property/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/nullable-model-required-property/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.Versioning;
using Azure.ResourceManager;

@armProviderNamespace
@service(#{ title: "Test Service" })
@versioned(Versions)
@armCommonTypesVersion(CommonTypes.Versions.v5)
namespace Microsoft.TestService;

enum Versions {
  @useDependency(Azure.ResourceManager.CommonTypes.Versions.v5)
  v2024_01_01: "2024-01-01",
}

model Widget is TrackedResource<WidgetProperties> {
  @key("widgetName")
  @segment("widgets")
  @path
  name: string;
}

model WidgetProperties {}

model WidgetPatchBody {
  details?: WidgetPatchDetails | null;
}

model WidgetPatchDetails {
  requiredProp: string;
}

interface Operations extends Azure.ResourceManager.Operations {}

@armResourceOperations
interface Widgets {
  get is ArmResourceRead<Widget>;
  createOrUpdate is ArmResourceCreateOrReplaceAsync<Widget>;
  delete is ArmResourceDeleteWithoutOkAsync<Widget>;

  @patch
  @armResourceUpdate(Widget)
  update(...ResourceInstanceParameters<Widget>, @body body: WidgetPatchBody):
    | ArmResponse<Widget>
    | ErrorResponse;
}
```

```json
{
  "paths": {
    "/providers/Microsoft.TestService/operations": {
      "get": {
        "operationId": "Operations_List",
        "tags": ["Operations"],
        "description": "List the operations for the provider",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/OperationListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}": {
      "get": {
        "operationId": "Widgets_Get",
        "tags": ["Widgets"],
        "description": "Get a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "put": {
        "operationId": "Widgets_CreateOrUpdate",
        "tags": ["Widgets"],
        "description": "Create a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "required": true,
            "type": "string"
          },
          {
            "name": "resource",
            "in": "body",
            "description": "Resource create parameters.",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Resource 'Widget' update operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "201": {
            "description": "Resource 'Widget' create operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            },
            "headers": {
              "Azure-AsyncOperation": {
                "type": "string",
                "description": "A link to the status monitor"
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "azure-async-operation"
        },
        "x-ms-long-running-operation": true
      },
      "patch": {
        "operationId": "Widgets_Update",
        "tags": ["Widgets"],
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "required": true,
            "type": "string"
          },
          {
            "name": "body",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/WidgetPatchBody"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "delete": {
        "operationId": "Widgets_Delete",
        "tags": ["Widgets"],
        "description": "Delete a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "202": {
            "description": "Resource deletion accepted.",
            "headers": {
              "Location": {
                "type": "string",
                "description": "The Location header contains the URL where the status of the long running operation can be checked."
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "204": {
            "description": "Resource does not exist."
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "location"
        },
        "x-ms-long-running-operation": true
      }
    }
  },
  "definitions": {
    "Widget": {
      "type": "object",
      "description": "Concrete tracked resource types can be created by aliasing this type using a specific property type.",
      "properties": {
        "properties": {
          "$ref": "#/definitions/WidgetProperties",
          "description": "The resource-specific properties for this resource."
        }
      },
      "allOf": [
        {
          "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/TrackedResource"
        }
      ]
    },
    "WidgetPatchBody": {
      "type": "object",
      "properties": {
        "details": {
          "$ref": "#/definitions/WidgetPatchDetails",
          "x-nullable": true
        }
      }
    },
    "WidgetPatchDetails": {
      "type": "object",
      "properties": {
        "requiredProp": {
          "type": "string"
        }
      },
      "required": ["requiredProp"]
    },
    "WidgetProperties": {
      "type": "object"
    }
  }
}
```

</details>

## UnSupportedPatchProperties encoded-inherited-properties

Reported findings: Swagger **3**, TypeSpec **5**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                                                                                                                                            | Target                                                                                                                                                           |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Swagger  | `UnSupportedPatchProperties`: Mark the top-level property "name", specified in the patch operation body, as readOnly or immutable. You could also choose to remove it from the request payload of the Patch operation. This property is not patchable.               | ["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}", "patch", "parameters", "4"] |
| Swagger  | `UnSupportedPatchProperties`: Mark the top-level property "location", specified in the patch operation body, as readOnly or immutable. You could also choose to remove it from the request payload of the Patch operation. This property is not patchable.           | ["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}", "patch", "parameters", "4"] |
| Swagger  | `UnSupportedPatchProperties`: Mark the property "properties.provisioningState", specified in the patch operation body, as readOnly or immutable. You could also choose to remove it from the request payload of the Patch operation. This property is not patchable. | ["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}", "patch", "parameters", "4"] |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: PATCH request body property 'location' is immutable and must be excluded from PATCH input.                                                                                                              | Authored semantic target; no location serialized in saved snapshot                                                                                               |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: PATCH request body property 'properties.provisioningState' is immutable and must be excluded from PATCH input.                                                                                          | Authored semantic target; no location serialized in saved snapshot                                                                                               |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'properties.provisioningState' in the request body either does not appear in the resource model or is nested at the wrong level.                                                           | Authored semantic target; no location serialized in saved snapshot                                                                                               |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: PATCH request body property 'name' is immutable and must be excluded from PATCH input.                                                                                                                  | Authored semantic target; no location serialized in saved snapshot                                                                                               |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'name' in the request body either does not appear in the resource model or is nested at the wrong level.                                                                                   | Authored semantic target; no location serialized in saved snapshot                                                                                               |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/encoded-inherited-properties/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/encoded-inherited-properties/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/encoded-inherited-properties/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/encoded-inherited-properties/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.Versioning;
using Azure.ResourceManager;

@armProviderNamespace
@service(#{ title: "Test Service" })
@versioned(Versions)
@armCommonTypesVersion(CommonTypes.Versions.v5)
namespace Microsoft.TestService;

enum Versions {
  @useDependency(Azure.ResourceManager.CommonTypes.Versions.v5)
  v2024_01_01: "2024-01-01",
}

model Widget is TrackedResource<WidgetProperties> {
  @key("widgetName")
  @segment("widgets")
  @doc("The name of the widget")
  @path
  @pattern("^[a-zA-Z0-9_-]+$")
  name: string;
}

model WidgetProperties {
  description?: string;
}

model PatchBase {
  @encodedName("application/json", "name")
  resourceName?: string;
}

model WidgetPatch extends PatchBase {
  @encodedName("application/json", "location")
  region?: string;

  properties?: WidgetPatchProperties;
}

model PatchPropertiesBase {
  @encodedName("application/json", "provisioningState")
  state?: ResourceProvisioningState;
}

model WidgetPatchProperties extends PatchPropertiesBase {
  description?: string;
}

interface Operations extends Azure.ResourceManager.Operations {}

@armResourceOperations
interface Widgets {
  get is ArmResourceRead<Widget>;
  createOrUpdate is ArmResourceCreateOrReplaceAsync<Widget>;

  @patch
  @armResourceUpdate(Widget)
  update(...ResourceInstanceParameters<Widget>, @body body: WidgetPatch):
    | ArmResponse<Widget>
    | ErrorResponse;

  delete is ArmResourceDeleteWithoutOkAsync<Widget>;
}
```

```json
{
  "paths": {
    "/providers/Microsoft.TestService/operations": {
      "get": {
        "operationId": "Operations_List",
        "tags": ["Operations"],
        "description": "List the operations for the provider",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/OperationListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}": {
      "get": {
        "operationId": "Widgets_Get",
        "tags": ["Widgets"],
        "description": "Get a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "put": {
        "operationId": "Widgets_CreateOrUpdate",
        "tags": ["Widgets"],
        "description": "Create a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          },
          {
            "name": "resource",
            "in": "body",
            "description": "Resource create parameters.",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Resource 'Widget' update operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "201": {
            "description": "Resource 'Widget' create operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            },
            "headers": {
              "Azure-AsyncOperation": {
                "type": "string",
                "description": "A link to the status monitor"
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "azure-async-operation"
        },
        "x-ms-long-running-operation": true
      },
      "patch": {
        "operationId": "Widgets_Update",
        "tags": ["Widgets"],
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          },
          {
            "name": "body",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/WidgetPatch"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "delete": {
        "operationId": "Widgets_Delete",
        "tags": ["Widgets"],
        "description": "Delete a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          }
        ],
        "responses": {
          "202": {
            "description": "Resource deletion accepted.",
            "headers": {
              "Location": {
                "type": "string",
                "description": "The Location header contains the URL where the status of the long running operation can be checked."
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "204": {
            "description": "Resource does not exist."
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "location"
        },
        "x-ms-long-running-operation": true
      }
    }
  },
  "definitions": {
    "Azure.ResourceManager.ResourceProvisioningState": {
      "type": "string",
      "description": "The provisioning state of a resource type.",
      "enum": ["Succeeded", "Failed", "Canceled"],
      "x-ms-enum": {
        "name": "ResourceProvisioningState",
        "modelAsString": true,
        "values": [
          {
            "name": "Succeeded",
            "value": "Succeeded",
            "description": "Resource has been created."
          },
          {
            "name": "Failed",
            "value": "Failed",
            "description": "Resource creation failed."
          },
          {
            "name": "Canceled",
            "value": "Canceled",
            "description": "Resource creation was canceled."
          }
        ]
      }
    },
    "PatchBase": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "x-ms-client-name": "resourceName"
        }
      }
    },
    "PatchPropertiesBase": {
      "type": "object",
      "properties": {
        "provisioningState": {
          "$ref": "#/definitions/Azure.ResourceManager.ResourceProvisioningState",
          "x-ms-client-name": "state"
        }
      }
    },
    "Widget": {
      "type": "object",
      "description": "Concrete tracked resource types can be created by aliasing this type using a specific property type.",
      "properties": {
        "properties": {
          "$ref": "#/definitions/WidgetProperties",
          "description": "The resource-specific properties for this resource."
        }
      },
      "allOf": [
        {
          "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/TrackedResource"
        }
      ]
    },
    "WidgetPatch": {
      "type": "object",
      "properties": {
        "location": {
          "type": "string",
          "x-ms-client-name": "region"
        },
        "properties": {
          "$ref": "#/definitions/WidgetPatchProperties"
        }
      },
      "allOf": [
        {
          "$ref": "#/definitions/PatchBase"
        }
      ]
    },
    "WidgetPatchProperties": {
      "type": "object",
      "properties": {
        "description": {
          "type": "string"
        }
      },
      "allOf": [
        {
          "$ref": "#/definitions/PatchPropertiesBase"
        }
      ]
    },
    "WidgetProperties": {
      "type": "object",
      "properties": {
        "description": {
          "type": "string"
        }
      }
    }
  }
}
```

</details>

## UnSupportedPatchProperties explicit-create-immutable-input

Reported findings: Swagger **0**, TypeSpec **2**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                               | Target                                                             |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Swagger  | No selected findings                                                                                                                                    | Not applicable                                                     |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: PATCH request body property 'location' is immutable and must be excluded from PATCH input. | Authored semantic target; no location serialized in saved snapshot |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: PATCH request body property 'location' must include Lifecycle.Update visibility.           | Authored semantic target; no location serialized in saved snapshot |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/explicit-create-immutable-input/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/explicit-create-immutable-input/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/explicit-create-immutable-input/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/explicit-create-immutable-input/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using Azure.ResourceManager;

@armProviderNamespace
@service
namespace Microsoft.TestService;

@parameterVisibility(Lifecycle.Create)
@patch
@route("/widgets")
op update(
  @body body: {
    @visibility(Lifecycle.Create) location?: string;
  },
): void;
```

```json
{
  "paths": {
    "/widgets": {
      "patch": {
        "operationId": "Update",
        "parameters": [
          {
            "name": "body",
            "in": "body",
            "required": true,
            "schema": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "x-ms-mutability": ["create"]
                }
              }
            }
          }
        ],
        "responses": {
          "204": {
            "description": "There is no content to send for this request, but the headers may be useful. "
          }
        }
      }
    }
  },
  "definitions": {}
}
```

</details>

## UnSupportedPatchProperties patch-with-id-name

Reported findings: Swagger **3**, TypeSpec **4**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                                                                                                                              | Target                                                                                                                                                           |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Swagger  | `UnSupportedPatchProperties`: Mark the top-level property "id", specified in the patch operation body, as readOnly or immutable. You could also choose to remove it from the request payload of the Patch operation. This property is not patchable.   | ["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}", "patch", "parameters", "4"] |
| Swagger  | `UnSupportedPatchProperties`: Mark the top-level property "name", specified in the patch operation body, as readOnly or immutable. You could also choose to remove it from the request payload of the Patch operation. This property is not patchable. | ["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}", "patch", "parameters", "4"] |
| Swagger  | `UnSupportedPatchProperties`: Mark the top-level property "type", specified in the patch operation body, as readOnly or immutable. You could also choose to remove it from the request payload of the Patch operation. This property is not patchable. | ["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}", "patch", "parameters", "4"] |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: PATCH request body property 'id' is immutable and must be excluded from PATCH input.                                                                                                      | Authored semantic target; no location serialized in saved snapshot                                                                                               |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: PATCH request body property 'name' is immutable and must be excluded from PATCH input.                                                                                                    | Authored semantic target; no location serialized in saved snapshot                                                                                               |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'name' in the request body either does not appear in the resource model or is nested at the wrong level.                                                                     | Authored semantic target; no location serialized in saved snapshot                                                                                               |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: PATCH request body property 'type' is immutable and must be excluded from PATCH input.                                                                                                    | Authored semantic target; no location serialized in saved snapshot                                                                                               |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/patch-with-id-name/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/patch-with-id-name/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/patch-with-id-name/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/patch-with-id-name/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.Versioning;
using Azure.ResourceManager;

@armProviderNamespace
@service(#{ title: "Test Service" })
@versioned(Versions)
namespace Microsoft.TestService;

enum Versions {
  @useDependency(Azure.ResourceManager.CommonTypes.Versions.v5)
  @armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v3)
  v2024_01_01: "2024-01-01",
}

/** A test widget resource. */
model Widget is TrackedResource<WidgetProperties> {
  @key("widgetName")
  @segment("widgets")
  @doc("The name of the widget")
  @pattern("^[a-zA-Z0-9-]{3,24}$")
  @path
  name: string;
}

/** Widget properties. */
model WidgetProperties {
  /** Description of the widget. */
  description?: string;

  /** The provisioning state of the widget. */
  @visibility(Lifecycle.Read)
  provisioningState?: ProvisioningState;
}

/** The provisioning state of a resource. */
union ProvisioningState {
  string,
  ResourceProvisioningState,
}

interface Operations extends Azure.ResourceManager.Operations {}

/** Custom patch body with unsupported properties. */
model WidgetPatch {
  /** Resource ID - should not be in PATCH. */
  id?: string;

  /** Resource name - should not be in PATCH. */
  name?: string;

  /** Resource type - should not be in PATCH. */
  type?: string;

  /** Tags. */
  #suppress "@azure-tools/typespec-azure-resource-manager/arm-no-record" "Record needed for tags in PATCH body"
  tags?: Record<string>;
}

@armResourceOperations
interface Widgets {
  get is ArmResourceRead<Widget>;
  createOrUpdate is ArmResourceCreateOrReplaceAsync<Widget>;

  /** Update widget. */
  @patch
  @armResourceUpdate(Widget)
  update(
    ...ResourceInstanceParameters<Widget>,
    @doc("The widget patch body.") @body body: WidgetPatch,
  ): ArmResponse<Widget> | ErrorResponse;

  delete is ArmResourceDeleteWithoutOkAsync<Widget>;
  listByResourceGroup is ArmResourceListByParent<Widget>;
  listBySubscription is ArmListBySubscription<Widget>;
}
```

```json
{
  "paths": {
    "/providers/Microsoft.TestService/operations": {
      "get": {
        "operationId": "Operations_List",
        "tags": ["Operations"],
        "description": "List the operations for the provider",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/ApiVersionParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v3/types.json#/definitions/OperationListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v3/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/providers/Microsoft.TestService/widgets": {
      "get": {
        "operationId": "Widgets_ListBySubscription",
        "tags": ["Widgets"],
        "description": "List Widget resources by subscription ID",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/SubscriptionIdParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/WidgetListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v3/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets": {
      "get": {
        "operationId": "Widgets_ListByResourceGroup",
        "tags": ["Widgets"],
        "description": "List Widget resources by resource group",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/ResourceGroupNameParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/WidgetListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v3/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}": {
      "get": {
        "operationId": "Widgets_Get",
        "tags": ["Widgets"],
        "description": "Get a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9-]{3,24}$"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v3/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "put": {
        "operationId": "Widgets_CreateOrUpdate",
        "tags": ["Widgets"],
        "description": "Create a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9-]{3,24}$"
          },
          {
            "name": "resource",
            "in": "body",
            "description": "Resource create parameters.",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Resource 'Widget' update operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "201": {
            "description": "Resource 'Widget' create operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            },
            "headers": {
              "Azure-AsyncOperation": {
                "type": "string",
                "description": "A link to the status monitor"
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v3/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "azure-async-operation"
        },
        "x-ms-long-running-operation": true
      },
      "patch": {
        "operationId": "Widgets_Update",
        "tags": ["Widgets"],
        "description": "Update widget.",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9-]{3,24}$"
          },
          {
            "name": "body",
            "in": "body",
            "description": "The widget patch body.",
            "required": true,
            "schema": {
              "$ref": "#/definitions/WidgetPatch"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v3/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "delete": {
        "operationId": "Widgets_Delete",
        "tags": ["Widgets"],
        "description": "Delete a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v3/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9-]{3,24}$"
          }
        ],
        "responses": {
          "202": {
            "description": "Resource deletion accepted.",
            "headers": {
              "Location": {
                "type": "string",
                "description": "The Location header contains the URL where the status of the long running operation can be checked."
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "204": {
            "description": "Resource does not exist."
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v3/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "location"
        },
        "x-ms-long-running-operation": true
      }
    }
  },
  "definitions": {
    "ProvisioningState": {
      "type": "string",
      "description": "The provisioning state of a resource.",
      "enum": ["Succeeded", "Failed", "Canceled"],
      "x-ms-enum": {
        "name": "ProvisioningState",
        "modelAsString": true,
        "values": [
          {
            "name": "Succeeded",
            "value": "Succeeded",
            "description": "Resource has been created."
          },
          {
            "name": "Failed",
            "value": "Failed",
            "description": "Resource creation failed."
          },
          {
            "name": "Canceled",
            "value": "Canceled",
            "description": "Resource creation was canceled."
          }
        ]
      }
    },
    "Widget": {
      "type": "object",
      "description": "A test widget resource.",
      "properties": {
        "properties": {
          "$ref": "#/definitions/WidgetProperties",
          "description": "The resource-specific properties for this resource."
        }
      },
      "allOf": [
        {
          "$ref": "../../../../../common-types/resource-management/v3/types.json#/definitions/TrackedResource"
        }
      ]
    },
    "WidgetListResult": {
      "type": "object",
      "description": "The response of a Widget list operation.",
      "properties": {
        "value": {
          "type": "array",
          "description": "The Widget items on this page",
          "items": {
            "$ref": "#/definitions/Widget"
          }
        },
        "nextLink": {
          "type": "string",
          "format": "uri",
          "description": "The link to the next page of items"
        }
      },
      "required": ["value"]
    },
    "WidgetPatch": {
      "type": "object",
      "description": "Custom patch body with unsupported properties.",
      "properties": {
        "id": {
          "type": "string",
          "description": "Resource ID - should not be in PATCH."
        },
        "name": {
          "type": "string",
          "description": "Resource name - should not be in PATCH."
        },
        "type": {
          "type": "string",
          "description": "Resource type - should not be in PATCH."
        },
        "tags": {
          "type": "object",
          "description": "Tags.",
          "additionalProperties": {
            "type": "string"
          }
        }
      }
    },
    "WidgetProperties": {
      "type": "object",
      "description": "Widget properties.",
      "properties": {
        "description": {
          "type": "string",
          "description": "Description of the widget."
        },
        "provisioningState": {
          "$ref": "#/definitions/ProvisioningState",
          "description": "The provisioning state of the widget.",
          "readOnly": true
        }
      }
    }
  }
}
```

</details>

## UnSupportedPatchProperties patch-with-location-provisioning-state

Reported findings: Swagger **2**, TypeSpec **3**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                                                                                                                                            | Target                                                                                                                                                           |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Swagger  | `UnSupportedPatchProperties`: Mark the top-level property "location", specified in the patch operation body, as readOnly or immutable. You could also choose to remove it from the request payload of the Patch operation. This property is not patchable.           | ["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}", "patch", "parameters", "4"] |
| Swagger  | `UnSupportedPatchProperties`: Mark the property "properties.provisioningState", specified in the patch operation body, as readOnly or immutable. You could also choose to remove it from the request payload of the Patch operation. This property is not patchable. | ["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}", "patch", "parameters", "4"] |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: PATCH request body property 'location' is immutable and must be excluded from PATCH input.                                                                                                              | Authored semantic target; no location serialized in saved snapshot                                                                                               |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: PATCH request body property 'properties.provisioningState' is immutable and must be excluded from PATCH input.                                                                                          | Authored semantic target; no location serialized in saved snapshot                                                                                               |
| TypeSpec | `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`: The property 'properties.provisioningState' in the request body either does not appear in the resource model or is nested at the wrong level.                                                           | Authored semantic target; no location serialized in saved snapshot                                                                                               |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/patch-with-location-provisioning-state/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/patch-with-location-provisioning-state/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/patch-with-location-provisioning-state/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/patch-with-location-provisioning-state/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.Versioning;
using Azure.ResourceManager;

@armProviderNamespace
@service(#{ title: "Test Service" })
@versioned(Versions)
@armCommonTypesVersion(CommonTypes.Versions.v5)
namespace Microsoft.TestService;

enum Versions {
  @useDependency(Azure.ResourceManager.CommonTypes.Versions.v5)
  v2024_01_01: "2024-01-01",
}

model Widget is TrackedResource<WidgetProperties> {
  @key("widgetName")
  @segment("widgets")
  @doc("The name of the widget")
  @path
  @pattern("^[a-zA-Z0-9_-]+$")
  name: string;
}

model WidgetProperties {
  description?: string;
}

model WidgetPatch {
  location?: string;
  properties?: WidgetPatchProperties;
}

model WidgetPatchProperties {
  provisioningState?: ResourceProvisioningState;
  description?: string;
}

interface Operations extends Azure.ResourceManager.Operations {}

@armResourceOperations
interface Widgets {
  get is ArmResourceRead<Widget>;
  createOrUpdate is ArmResourceCreateOrReplaceAsync<Widget>;

  @patch
  @armResourceUpdate(Widget)
  update(...ResourceInstanceParameters<Widget>, @body body: WidgetPatch | null):
    | ArmResponse<Widget>
    | ErrorResponse;

  delete is ArmResourceDeleteWithoutOkAsync<Widget>;
}
```

```json
{
  "paths": {
    "/providers/Microsoft.TestService/operations": {
      "get": {
        "operationId": "Operations_List",
        "tags": ["Operations"],
        "description": "List the operations for the provider",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/OperationListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}": {
      "get": {
        "operationId": "Widgets_Get",
        "tags": ["Widgets"],
        "description": "Get a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "put": {
        "operationId": "Widgets_CreateOrUpdate",
        "tags": ["Widgets"],
        "description": "Create a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          },
          {
            "name": "resource",
            "in": "body",
            "description": "Resource create parameters.",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Resource 'Widget' update operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "201": {
            "description": "Resource 'Widget' create operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            },
            "headers": {
              "Azure-AsyncOperation": {
                "type": "string",
                "description": "A link to the status monitor"
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "azure-async-operation"
        },
        "x-ms-long-running-operation": true
      },
      "patch": {
        "operationId": "Widgets_Update",
        "tags": ["Widgets"],
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          },
          {
            "name": "body",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/WidgetPatch",
              "x-nullable": true
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "delete": {
        "operationId": "Widgets_Delete",
        "tags": ["Widgets"],
        "description": "Delete a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          }
        ],
        "responses": {
          "202": {
            "description": "Resource deletion accepted.",
            "headers": {
              "Location": {
                "type": "string",
                "description": "The Location header contains the URL where the status of the long running operation can be checked."
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "204": {
            "description": "Resource does not exist."
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "location"
        },
        "x-ms-long-running-operation": true
      }
    }
  },
  "definitions": {
    "Azure.ResourceManager.ResourceProvisioningState": {
      "type": "string",
      "description": "The provisioning state of a resource type.",
      "enum": ["Succeeded", "Failed", "Canceled"],
      "x-ms-enum": {
        "name": "ResourceProvisioningState",
        "modelAsString": true,
        "values": [
          {
            "name": "Succeeded",
            "value": "Succeeded",
            "description": "Resource has been created."
          },
          {
            "name": "Failed",
            "value": "Failed",
            "description": "Resource creation failed."
          },
          {
            "name": "Canceled",
            "value": "Canceled",
            "description": "Resource creation was canceled."
          }
        ]
      }
    },
    "Widget": {
      "type": "object",
      "description": "Concrete tracked resource types can be created by aliasing this type using a specific property type.",
      "properties": {
        "properties": {
          "$ref": "#/definitions/WidgetProperties",
          "description": "The resource-specific properties for this resource."
        }
      },
      "allOf": [
        {
          "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/TrackedResource"
        }
      ]
    },
    "WidgetPatch": {
      "type": "object",
      "properties": {
        "location": {
          "type": "string"
        },
        "properties": {
          "$ref": "#/definitions/WidgetPatchProperties"
        }
      }
    },
    "WidgetPatchProperties": {
      "type": "object",
      "properties": {
        "provisioningState": {
          "$ref": "#/definitions/Azure.ResourceManager.ResourceProvisioningState"
        },
        "description": {
          "type": "string"
        }
      }
    },
    "WidgetProperties": {
      "type": "object",
      "properties": {
        "description": {
          "type": "string"
        }
      }
    }
  }
}
```

</details>

## UnSupportedPatchProperties readonly-ref-validator-discrepancy

Reported findings: Swagger **1**, TypeSpec **0**.
Common normalized unit: **unassessed**. No fixture-level net count is
used to cancel an opposing difference.

| Engine   | Exact reported diagnostic                                                                                                                                                                                                                                            | Target                                                                                                                                                           |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Swagger  | `UnSupportedPatchProperties`: Mark the property "properties.provisioningState", specified in the patch operation body, as readOnly or immutable. You could also choose to remove it from the request payload of the Patch operation. This property is not patchable. | ["paths", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}", "patch", "parameters", "4"] |
| TypeSpec | No selected findings                                                                                                                                                                                                                                                 | Not applicable                                                                                                                                                   |

[Original source](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/readonly-ref-validator-discrepancy/main.tsp),
[emitted Swagger](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/readonly-ref-validator-discrepancy/output.json),
[Swagger receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/readonly-ref-validator-discrepancy/validator-diagnostics.json),
[TypeSpec receipt](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/readonly-ref-validator-discrepancy/tsp-diagnostics.json).

<details>
<summary>Verified authored source and emitted schema (saved snapshot)</summary>

```typespec
import "../../lib/imports.tsp";

using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.Versioning;
using Azure.ResourceManager;

@armProviderNamespace
@service(#{ title: "Test Service" })
@versioned(Versions)
@armCommonTypesVersion(CommonTypes.Versions.v5)
namespace Microsoft.TestService;

enum Versions {
  @useDependency(Azure.ResourceManager.CommonTypes.Versions.v5)
  v2024_01_01: "2024-01-01",
}

model Widget is TrackedResource<WidgetProperties> {
  @key("widgetName")
  @segment("widgets")
  @doc("The name of the widget")
  @path
  @pattern("^[a-zA-Z0-9_-]+$")
  name: string;
}

model WidgetProperties {
  description?: string;
}

model WidgetPatch {
  properties?: WidgetPatchProperties;
}

model WidgetPatchProperties {
  @visibility(Lifecycle.Read)
  provisioningState?: ResourceProvisioningState;

  description?: string;
}

interface Operations extends Azure.ResourceManager.Operations {}

@armResourceOperations
interface Widgets {
  get is ArmResourceRead<Widget>;
  createOrUpdate is ArmResourceCreateOrReplaceAsync<Widget>;

  @patch
  @armResourceUpdate(Widget)
  update(...ResourceInstanceParameters<Widget>, @body body: WidgetPatch):
    | ArmResponse<Widget>
    | ErrorResponse;

  delete is ArmResourceDeleteWithoutOkAsync<Widget>;
}
```

```json
{
  "paths": {
    "/providers/Microsoft.TestService/operations": {
      "get": {
        "operationId": "Operations_List",
        "tags": ["Operations"],
        "description": "List the operations for the provider",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/OperationListResult"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-pageable": {
          "nextLinkName": "nextLink"
        }
      }
    },
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}": {
      "get": {
        "operationId": "Widgets_Get",
        "tags": ["Widgets"],
        "description": "Get a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "put": {
        "operationId": "Widgets_CreateOrUpdate",
        "tags": ["Widgets"],
        "description": "Create a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          },
          {
            "name": "resource",
            "in": "body",
            "description": "Resource create parameters.",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Resource 'Widget' update operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "201": {
            "description": "Resource 'Widget' create operation succeeded",
            "schema": {
              "$ref": "#/definitions/Widget"
            },
            "headers": {
              "Azure-AsyncOperation": {
                "type": "string",
                "description": "A link to the status monitor"
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "azure-async-operation"
        },
        "x-ms-long-running-operation": true
      },
      "patch": {
        "operationId": "Widgets_Update",
        "tags": ["Widgets"],
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          },
          {
            "name": "body",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/WidgetPatch"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Azure operation completed successfully.",
            "schema": {
              "$ref": "#/definitions/Widget"
            }
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        }
      },
      "delete": {
        "operationId": "Widgets_Delete",
        "tags": ["Widgets"],
        "description": "Delete a Widget",
        "parameters": [
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ApiVersionParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/SubscriptionIdParameter"
          },
          {
            "$ref": "../../../../../common-types/resource-management/v5/types.json#/parameters/ResourceGroupNameParameter"
          },
          {
            "name": "widgetName",
            "in": "path",
            "description": "The name of the widget",
            "required": true,
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          }
        ],
        "responses": {
          "202": {
            "description": "Resource deletion accepted.",
            "headers": {
              "Location": {
                "type": "string",
                "description": "The Location header contains the URL where the status of the long running operation can be checked."
              },
              "Retry-After": {
                "type": "integer",
                "format": "int32",
                "description": "The Retry-After header can indicate how long the client should wait before polling the operation status."
              }
            }
          },
          "204": {
            "description": "Resource does not exist."
          },
          "default": {
            "description": "An unexpected error response.",
            "schema": {
              "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/ErrorResponse"
            }
          }
        },
        "x-ms-long-running-operation-options": {
          "final-state-via": "location"
        },
        "x-ms-long-running-operation": true
      }
    }
  },
  "definitions": {
    "Azure.ResourceManager.ResourceProvisioningState": {
      "type": "string",
      "description": "The provisioning state of a resource type.",
      "enum": ["Succeeded", "Failed", "Canceled"],
      "x-ms-enum": {
        "name": "ResourceProvisioningState",
        "modelAsString": true,
        "values": [
          {
            "name": "Succeeded",
            "value": "Succeeded",
            "description": "Resource has been created."
          },
          {
            "name": "Failed",
            "value": "Failed",
            "description": "Resource creation failed."
          },
          {
            "name": "Canceled",
            "value": "Canceled",
            "description": "Resource creation was canceled."
          }
        ]
      }
    },
    "Widget": {
      "type": "object",
      "description": "Concrete tracked resource types can be created by aliasing this type using a specific property type.",
      "properties": {
        "properties": {
          "$ref": "#/definitions/WidgetProperties",
          "description": "The resource-specific properties for this resource."
        }
      },
      "allOf": [
        {
          "$ref": "../../../../../common-types/resource-management/v5/types.json#/definitions/TrackedResource"
        }
      ]
    },
    "WidgetPatch": {
      "type": "object",
      "properties": {
        "properties": {
          "$ref": "#/definitions/WidgetPatchProperties"
        }
      }
    },
    "WidgetPatchProperties": {
      "type": "object",
      "properties": {
        "provisioningState": {
          "$ref": "#/definitions/Azure.ResourceManager.ResourceProvisioningState",
          "readOnly": true
        },
        "description": {
          "type": "string"
        }
      }
    },
    "WidgetProperties": {
      "type": "object",
      "properties": {
        "description": {
          "type": "string"
        }
      }
    }
  }
}
```

</details>


import "@typespec/http";
import "@typespec/rest";
import "@typespec/versioning";
import "@typespec/openapi";
import "@azure-tools/typespec-autorest";
import "@azure-tools/typespec-azure-resource-manager";
using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.Versioning;
using Azure.ResourceManager;

  @service namespace Controls;
  @OpenAPI.defaultResponse model Fallback { code: string; }
  @error model Standard {
    @statusCode status: 400;
    @body body: CommonTypes.ErrorResponse;
  }
  @route("/mixed") @get op mixed(): Fallback | Standard;

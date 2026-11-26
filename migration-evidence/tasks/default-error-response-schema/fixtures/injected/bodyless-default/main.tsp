
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
@error
@OpenAPI.defaultResponse
model Bodyless {
  @statusCode status: 500;
}
@route("/bodyless") @get op bodyless(): Bodyless;

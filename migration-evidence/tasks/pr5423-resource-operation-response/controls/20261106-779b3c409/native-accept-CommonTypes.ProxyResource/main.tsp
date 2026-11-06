
import "@typespec/http";
import "@typespec/rest";
import "@typespec/openapi";
import "@azure-tools/typespec-azure-core";
import "@azure-tools/typespec-azure-resource-manager";
using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.OpenAPI;
using Azure.ResourceManager;
@service @armProviderNamespace namespace Microsoft.Coverage;
model Widget is ProxyResource<{}> { ...ResourceNameParameter<Widget>; }
model Other is ProxyResource<{}> { ...ResourceNameParameter<Other>; }
model Input { value?: string; }
model Lookalike { ...Widget; }

interface Custom {

  @put @route("/providers/Microsoft.Coverage/custom/{customName}")
  replace(@path customName: string, @body body: Input): CommonTypes.ProxyResource;
}

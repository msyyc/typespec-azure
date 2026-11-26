
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

@armProviderNamespace
@armCommonTypesVersion(CommonTypes.Versions.v5)
namespace Microsoft.Contoso;
model Widget is ProxyResource<{}> {
  ...ResourceNameParameter<Widget>;
}

@error model CustomError { code: string; message: string; }
@armResourceOperations interface Widgets {
  restart is ArmResourceActionAsync<Widget, void, void, Error = CustomError>;
}

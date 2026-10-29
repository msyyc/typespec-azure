
import "@typespec/http";
import "@typespec/rest";
import "@typespec/versioning";
import "@azure-tools/typespec-azure-core";
import "@azure-tools/typespec-azure-resource-manager";
using TypeSpec.Http;
using TypeSpec.Rest;
using Azure.ResourceManager;
@service @armProviderNamespace namespace Microsoft.Coverage;
model WidgetProperties { description?: string; }
model Widget is ProxyResource<WidgetProperties> {
  ...ResourceNameParameter<Widget>;
}
interface Operations extends Azure.ResourceManager.Operations {}

model CustomBase {
  ...CommonTypes.ApiVersionParameter;
  @path @segment("subscriptions") subId: string;
  @path @segment("resourceGroups") resourceGroupName: string;
}
@armResourceOperations interface Widgets {
  
  read is ArmResourceRead<Widget, BaseParameters = CustomBase>;
}

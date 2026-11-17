import "@typespec/http";
import "@typespec/rest";
import "@typespec/versioning";
import "@azure-tools/typespec-azure-core";
import "@azure-tools/typespec-azure-resource-manager";
using TypeSpec.Http;
using Azure.Core;
using Azure.ResourceManager;
@service
namespace Contoso;
model Widget {
  value: string;
}
model Result<T> {
  value: T;
}

#suppress "@azure-tools/typespec-azure-core/no-unnamed-types" "Preserve the existing response contract."
@get @route("/suppressed") op suppressed(): Record<string>;
@get @route("/reported") op reported(): Record<string>;
@get @route("/anonymous") op anonymous(): {
  value: string;
};

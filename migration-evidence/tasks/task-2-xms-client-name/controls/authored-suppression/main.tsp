import "@typespec/http";
import "@azure-tools/typespec-client-generator-core";
using TypeSpec.Http;
using Azure.ClientGenerator.Core;
@service namespace NativeControls;
model Widget {
#suppress "@azure-tools/typespec-client-generator-core/no-redundant-client-name" "Intentional control."
@clientName("name") name: string; }

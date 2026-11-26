import "@typespec/http";
import "@azure-tools/typespec-client-generator-core";
using TypeSpec.Http;
using Azure.ClientGenerator.Core;
@service namespace NativeControls;
model Widget { @clientName("name") @friendlyName("other") name: string; @clientName("other") @friendlyName("other") second: string; @clientName(exact("other")) @friendlyName("other") third: string; }

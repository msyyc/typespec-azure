import "@typespec/http";
import "@azure-tools/typespec-client-generator-core";
using TypeSpec.Http;
using Azure.ClientGenerator.Core;
@service namespace NativeControls;
model Widget { @clientName("other", "python") @clientName("other") name: string; @clientName("second", "python") @clientName("different") second: string; }

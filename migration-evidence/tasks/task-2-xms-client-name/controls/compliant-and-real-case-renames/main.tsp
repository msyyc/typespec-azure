import "@typespec/http";
import "@azure-tools/typespec-client-generator-core";
using TypeSpec.Http;
using Azure.ClientGenerator.Core;
@service namespace NativeControls;
model Widget { plain: string; @clientName("different") renamed: string; @clientName("Name") name: string; }

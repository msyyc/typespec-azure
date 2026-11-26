import "@typespec/http";
import "@azure-tools/typespec-client-generator-core";
using TypeSpec.Http;
using Azure.ClientGenerator.Core;
@service namespace NativeControls;
model Source { @clientName("renamed") @friendlyName("renamed") original: string; } model Result { @friendlyName("{name}", Source.original) value: string; } @get op read(): Result;

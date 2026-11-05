import "@typespec/http";
import "@azure-tools/typespec-client-generator-core";
using TypeSpec.Http;
using Azure.ClientGenerator.Core;
@service namespace Test {}
@client({service: Test}) namespace RootClient {
  @client({name:"Items"}) @clientName("Paths") interface Other {
    @get @route("/paths") op listPaths(): string;
  }
}

import "@typespec/http";
import "@azure-tools/typespec-client-generator-core";
using TypeSpec.Http;
@service namespace Controls;
interface Paths {

  @get @route("/paths") op list(): string;
}

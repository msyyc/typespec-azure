import "@typespec/http";
import "@azure-tools/typespec-client-generator-core";
using TypeSpec.Http;
@service namespace Controls;
interface Paths {
  #suppress "@azure-tools/typespec-client-generator-core/no-redundant-operation-group-name" "Intentional installed control."
  @get @route("/paths") op listPaths(): string;
}

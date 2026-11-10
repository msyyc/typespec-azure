# CustomLocations compatibility proposal

## Completed CI evidence

[External Integration / Azure REST API Specs](https://github.com/Azure/typespec-azure/actions/runs/42774292159/job/129689064694) completed with **failure** on November 10, 2026. It exercised linter head [`3a08c00ff9daca0ed6eb44ce043d424a90d78ab9`](https://github.com/Azure/typespec-azure/commit/3a08c00ff9daca0ed6eb44ce043d424a90d78ab9), with compiler submodule `8574d5453f7bf9a07dc09bd41edac579af71d94b`. The validation summary was **604 passing / one failing project out of 605**. The failed project reported exactly one diagnostic occurrence:

`@azure-tools/typespec-azure-core/no-unnamed-types`: `Anonymous model should be defined as a named model declaration.`

Its source target was `specification/extendedlocation/resource-manager/Microsoft.ExtendedLocation/CustomLocations/client.tsp:158:5`, the anonymous response of `resourceSyncRulesUpdate`. See the [sanitized CI excerpt](ci-excerpt.txt) and [machine-readable attribution](compatibility.json). The full captured CLI log is retained locally with SHA-256 `1308aadd111135888d814b21a915b20727a4833f5e4625519025d744f710a998`; it is not republished because it contains runner paths and unrelated setup output.

The [suite configuration](https://github.com/Azure/typespec-azure/blob/3a08c00ff9daca0ed6eb44ce043d424a90d78ab9/.typespec-integration/config.yaml) selects `Azure/azure-rest-api-specs:typespec-next`, discovers `specification/**/tspconfig.yaml`, excludes `specification/ai-foundry/data-plane/Foundry/**`, and runs `client.tsp --no-emit` before `main.tsp` when present. The [runner](https://github.com/microsoft/typespec/blob/8574d5453f7bf9a07dc09bd41edac579af71d94b/packages/tsp-integration/src/validate.ts) stops a project at its first failing entrypoint. The [compile command](https://github.com/microsoft/typespec/blob/8574d5453f7bf9a07dc09bd41edac579af71d94b/packages/tsp-integration/src/package-manager.ts) supplies `--warn-as-error`, which promotes this warning to an error. For the failed service, the reported `client.tsp` target and entrypoint order identify the client compile as the failing entrypoint; no successful `main.tsp` run for that service is inferred.

## Consumer revision and source reconciliation

The integration checkout log records `typespec-next` checkout from `07:21:56Z` to `07:22:30Z`, **but does not print the consumer checkout SHA**. There are no retained run artifacts containing that checkout identity. Therefore the exact tested consumer commit is **not independently recorded**, and this report does not substitute today's branch tip for it.

The consumer proposal is pinned separately to fetched base [`06472951865696fb06a0e36ece718d62bf4edc33`](https://github.com/Azure/azure-rest-api-specs/commit/06472951865696fb06a0e36ece718d62bf4edc33). That was the observed `typespec-next` head before the monitored job completed, and the commit-history query bounded to the checkout end also returns it (commit time `00:15:58Z`). These are corroborating branch-history observations, not proof emitted by the CI checkout.

The diagnostic target itself is reconciled directly: the complete model text printed at CI lines 158-163 matches the same lines in [the fetched base's client file](https://github.com/Azure/azure-rest-api-specs/blob/06472951865696fb06a0e36ece718d62bf4edc33/specification/extendedlocation/resource-manager/Microsoft.ExtendedLocation/CustomLocations/client.tsp#L133-L164). Its base Git blob is `b4ccfba338d15b4e98ce7f056e25001c7df74275`. The operation name, JavaScript override binding, parameter context and existing suppressions are present at that base. No source drift or pre-existing naming suppression was found at this target. The proposal does not claim whole-checkout identity or replay verification.

## Why this warning is caused by PR #5551

Compared with main [`4184cf254ea0420446ebe9bc3b978b2da342ca76`](https://github.com/Azure/typespec-azure/commit/4184cf254ea0420446ebe9bc3b978b2da342ca76), the [changed rule](https://github.com/Azure/typespec-azure/blob/3a08c00ff9daca0ed6eb44ce043d424a90d78ab9/packages/typespec-azure-core/src/rules/no-unnamed-types.ts#L99-L133) adds the implicit-response traversal. Existing property/request checks, the diagnostic code/message and ruleset activation remain unchanged.

The client operation's return union contains:

```typespec
{
  statusCode: 200;
  body: Microsoft.ExtendedLocation.resourceSyncRule;
  azureAsyncOperation: string;
  retryAfter: int32;
}
```

None of these properties has `@statusCode`, `@body` or `@header`, so HTTP semantics treat the expression as a nonempty implicit payload. Its property types are named/scalar, not anonymous property models diagnosed by the unchanged path. The old operation visitor excluded the top-level return union from union warnings but did not check this model. The new response path recovers the original anonymous declaration and adds it to `invalidModels`. This establishes causality for the captured warning rather than inferring it from a reused diagnostic code.

The service's [configuration](https://github.com/Azure/azure-rest-api-specs/blob/06472951865696fb06a0e36ece718d62bf4edc33/specification/extendedlocation/resource-manager/Microsoft.ExtendedLocation/CustomLocations/tspconfig.yaml) extends the resource-manager and client-sdk presets. The existing naming rule is enabled; no service-level disabling of it was found. The SDK override is deliberately not excluded by the compiler/HTTP naming rule. This is a confirmed compatibility diagnostic, not a demonstrated false positive requiring a linter fix.

## Attribution and edit count

| Classification                                                                      | Raw diagnostic occurrences | Unique source targets | Proposed edits |
| ----------------------------------------------------------------------------------- | -------------------------: | --------------------: | -------------: |
| Confirmed PR-caused compatibility warning                                           |                          1 |                     1 |              1 |
| Unrelated/pre-existing compile/lint diagnostic occurrences in failed-project output |                          0 |                     0 |              0 |
| Confirmed linter false positives                                                    |                          0 |                     0 |              0 |
| Stale or unresolved diagnostic targets                                              |                          0 |                     0 |              0 |

Deduplication identity is source file + original model target + diagnostic code + message. The one occurrence requires one authored suppression, not one annotation per entrypoint or property. The missing full consumer checkout SHA remains a provenance limitation; it is not hidden in the zero unresolved-target count. Runner/action deprecation warnings are infrastructure annotations and are not candidates for TypeSpec suppression.

## Suppression scope

Add exactly this directive to the existing suppression group immediately before `op resourceSyncRulesUpdate`:

```typespec
#suppress "@azure-tools/typespec-azure-core/no-unnamed-types" "Preserve the existing JavaScript resourceSyncRulesUpdate response shape for backward compatibility."
```

The [compiler's suppression traversal](https://github.com/microsoft/typespec/blob/8574d5453f7bf9a07dc09bd41edac579af71d94b/packages/compiler/src/core/suppression-tracking.ts#L199-L216) walks from the diagnosed model through its ancestors; the [suppression code fix](https://github.com/microsoft/typespec/blob/8574d5453f7bf9a07dc09bd41edac579af71d94b/packages/compiler/src/core/compiler-code-fixes/suppress.codefix.ts#L117-L143) likewise selects a supported enclosing declaration for model/union/signature expressions. Thus operation scope is the supported narrow declaration scope for this model expression, not a namespace-wide bypass.

Preserve all existing suppressions and every API/SDK declaration. Do not name/restructure the model, add HTTP decorators, change common types, dependencies, lockfiles, generated Swagger or CI configuration. Only this confirmed target is proposed; no new warnings are extrapolated from source inspection.

## Validation and readiness

This is a **CI-derived, suppression-only proposal**, not a green-CI or landing outcome. No local consumer compilation, build, tests, lint, formatting, integration, emission or dependency installation was run. Inspection is limited to the captured CI evidence, pinned source/configuration, compiler suppression semantics and the complete one-line diff.

The original linter CI remains failed until independently addressed. Publishing a companion does not validate it or establish rollout readiness. No CI rerun, additional CI monitoring, automatic merge or linter implementation change is part of this proposal.

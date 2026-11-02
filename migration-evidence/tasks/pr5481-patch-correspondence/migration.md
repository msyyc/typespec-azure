# PatchPropertiesCorrespondToPutProperties migration

## 1. Conclusion and scope

The TypeSpec linter
`@azure-tools/typespec-azure-resource-manager/arm-resource-patch` is **not
functionally equivalent** to Swagger linter
[`PatchPropertiesCorrespondToPutProperties`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-properties-correspond-to-put-properties.md).
It compares writable JSON leaf **names**, not whole leaf schemas, so incompatible
same-name types can pass. Empty PATCH/missing PUT behavior, historical shape
handling, traversal, activation, and diagnostic identity also differ. Controlled
examples demonstrate inheritance and historical-shape false-positive mechanisms.
**Full Swagger/TypeSpec corpus parity remains unassessed:** the original rule was
staging-only and did not execute in the shared production Swagger baseline.

## 2. Actual coverage

The fresh TypeSpec execution assessed the complete frozen **487-project ARM
corpus**, without a filter or limit: 487 compiled successfully, **0 failed or
unassessed**. Findings occurred in 42 projects. Reported diagnostics are individual
findings, not project counts.

| Count                | Swagger linter                   | TypeSpec linter |
| -------------------- | -------------------------------- | --------------- |
| Reported diagnostics | **Not evaluated (staging-only)** | **214**         |

No supported cross-engine common-unit count or project overlap is available.
The absent Swagger shard must not be interpreted as zero. See the
[complete project inventory](project-inventory.json),
[all diagnostic targets and messages](diagnostic-inventory.md), and
[saved-observation summary](coverage-summary.json).

## 3. Function-level coverage

| Behavior                                                | Result                                                                                                             |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Extra PATCH JSON leaf; compliant subset                 | Covered by executed TypeSpec controls: 1 / 0 findings.                                                             |
| Same name, incompatible type or unequal schema metadata | **Different:** TypeSpec accepts it; Swagger's schema-equality predicate can report it.                             |
| Absent PATCH body                                       | Covered; both predicates reject it.                                                                                |
| Existing empty PATCH object                             | **Different:** TypeSpec rejects it; Swagger's body-parameter count check accepts it when PUT has a body.           |
| Missing PUT body                                        | **Different:** Swagger reports it; TypeSpec skips correspondence after checking PATCH.                             |
| Nested/inherited writable properties                    | **Partial:** a controlled derived-read-only/inherited-writable shape produces a TypeSpec traversal false positive. |
| Version availability versus historical names/types      | **Partial:** added/removed availability is handled; historical rename/type-shape controls produce false positives. |
| Encoded names, visibility, unauthored discriminators    | Source-aware TypeSpec policy differs from comparing emitted schemas; not full emission parity.                     |
| Unsupported top-level bodies                            | TypeSpec skips arrays, dictionaries, ambiguous unions, and other unsupported shapes.                               |
| Occurrence identity and activation                      | Different source-target deduplication and broader warning activation versus staging-only Swagger errors.           |

[Semantic examples and evidence labels](semantic-evidence.md) distinguish
executed controls, existing tests, and source inspection. They do not establish
production prevalence.

## 4. Why diagnostic counts differ

A measured cross-engine count gap **cannot be calculated** because the selected
Swagger linter did not run. The 214 TypeSpec findings comprise **212 missing
JSON-leaf-name**, **1 empty PATCH body**, and **1 missing PATCH body** diagnostics;
these are not proven TypeSpec-only findings.

The [grouped corpus evidence](corpus-examples.md) links the 90-finding DevCenter
outlier to an inheritance-asymmetry investigation, shows historical-name context
in the 13-finding Managed Network Fabric project, and records the NetApp empty
body, ProviderHub absent body, and Automation shared-location examples.
Controlled schema/type, body-policy, projection, and deduplication differences
are detailed in the [semantic appendix](semantic-evidence.md); all project and
diagnostic records remain available. Neither every finding's validity nor
Swagger correspondence is inferred from these examples.

## NOTES

- Assessed current PR head: `7baca4db3d7824c24c30961c50c3f47a6df8d958`.
  This task updates evidence and the PR description, not rule behavior.
  [Rule-change disposition and limitations](evidence-details.md#rule-change-disposition).
- Frozen specs: `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`;
  shared baseline `swagger-arm-20261026-2cd3c5dd`, metadata commit
  `317e703b3e380d3b64e0dacb3a2c6fc0651de253`.
  All 649 retained Swagger logs explicitly disable the original staging-only
  rule. [Pinned sources and runtime provenance](evidence-details.md).
- TypeSpec policy: all-source versions, selected rule explicitly enabled in
  `target-only` mode, authored suppressions retained. This is not a projection
  aligned with the historical latest-emitted Swagger selection.
  Separate controls verify suppression and actual ruleset activation.
- Raw TypeSpec diagnostics: 214; distinct project/location/message records: 214.
  The analyzer's 192 source positions merge different leaf messages and are
  **not** 192 equivalent operations or a normalized Swagger comparison.
  Older resource-subset/tags/body checks coexist under this TypeSpec rule code;
  the observed full-corpus messages here are the paired-helper families.
- Eight fresh injected real-linter controls passed. Applicable portable harness
  controls: 37 passed / 6 unrelated absent-rule cases explicitly skipped;
  the initial six failures remain disclosed. Additional semantic controls use
  the helper directly and do not test the entire suppression pipeline.
- [Evidence details](evidence-details.md),
  [real-service examples](corpus-examples.md), and
  [recovery/reanalysis instructions](replay.md) retain provenance, complete
  observations, validation boundaries, and source retention. Saved-data
  recovery is distinct from a full rerun; fully locked transitive regeneration
  is not claimed.
- [Independent local review](provenance/local-review.json) found no blocking
  publication issues. [Fresh-checkout recovery](provenance/recovery-verification.json)
  verified saved-data reanalysis, package bytes, and the shared-baseline asset;
  it did not repeat the corpus execution.

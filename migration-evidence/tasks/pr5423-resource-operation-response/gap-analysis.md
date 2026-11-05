# Gap analysis and decision

This appendix separates measured diagnostic coverage, semantic cause and recommended action. Recommendations are not approved policy retirements. [Migration conclusion](migration.md).

## Difference groups

`Raw / grouped` means reported Swagger diagnostics / distinct (member, project, resolved document, exact route, compared schema context) checks. The TypeSpec column counts only configured diagnostics attributed to that same comparison, not unrelated warnings on the route or callbacks hidden by authored suppression. Captured owning diagnostics are nevertheless credited in Assessed coverage and identified below.

| Difference (with evidence)                                                                                       | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics for the same check | Recommended action and rationale                                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------- | ----------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Empty 200: real response-body issue, not two unequal payload models](gap-analysis.md#body-policy-owner)         | 53 / 25                             | 0                                       | Covered by 16 captured owning diagnostic callbacks over 25 contexts before suppression. Diagnosed by the existing body owner before suppression; review the suppression/wire contract, not duplicate schema equality.                                      |
| [Swagger schema-comparison false positive / policy overreach](gap-analysis.md#bodyless-comparator-overreach)     | 15 / 15                             | 0                                       | Recommend excluding absent-body comparisons, not inventing bodies. Status-code compliance is a separate policy; approval is pending.                                                                                                                       |
| [Swagger collection-shape comparison false positive](gap-analysis.md#collection-comparator-overreach)            | 4 / 4                               | 0                                       | Recommend excluding wrapper-versus-item reference equality: actual resource items agree. Approval is pending.                                                                                                                                              |
| [Genuine PUT/GET resource-shape difference](gap-analysis.md#cross-method-entity-contract)                        | 1 / 1                               | 0                                       | Genuine uncovered contract difference. Confirm service intent before sharing models; defer a broad structural matcher.                                                                                                                                     |
| [Bulk/collection request contract, not ordinary resource replacement](gap-analysis.md#custom-collection-request) | 2 / 2                               | 0                                       | Unresolved bulk/item semantics. Require owner intent before enforcing ordinary resource replacement.                                                                                                                                                       |
| [Action-like PUT contract](gap-analysis.md#custom-command-request)                                               | 2 / 2                               | 0                                       | Unresolved command/association contracts; do not infer canonical replacement solely from PUT.                                                                                                                                                              |
| [Custom lifecycle registration/modeling gap](gap-analysis.md#custom-lifecycle-registration)                      | 3 / 3                               | 0                                       | Missing associations; three compatibility-checked repairs are in separate draft #47952, not frozen-corpus credit.                                                                                                                                          |
| [Canonical parent differs from the actual child/result response](gap-analysis.md#parent-canonical-association)   | 3 / 3                               | 0                                       | Wrong parent/operation-kind association; repair modeling only after proving wire/client compatibility.                                                                                                                                                     |
| [Deliberate polymorphism with unresolved canonical request association](gap-analysis.md#supported-polymorphism)  | 1 / 1                               | 0                                       | Preserve the hierarchy; establish canonical request registration. Response ancestry support does not prove derived-request acceptance.                                                                                                                     |
| [Unregistered body-bearing request/response mismatch](gap-analysis.md#unregistered-entity-request)               | 34 / 4                              | 0                                       | Four legacy DTO contracts lack canonical registration; review visibility/wire models rather than add recursive schema equality.                                                                                                                            |
| [Confirmed Swagger false positive](gap-analysis.md#upstream-identity-bug)                                        | 15 / 15                             | 0                                       | Confirmed resolved-object-identity bug; intentionally do not port its false positives.                                                                                                                                                                     |
| [Repeated reference invocations: put-resource-marker](gap-analysis.md#repeated-invocations)                      | 108 / 10                            | 10                                      | Count-only difference: preserve all invocations, but compare each exact member/schema context once. No production fix is needed.                                                                                                                           |
| [additional-canonical-response-policy](gap-analysis.md#typespec-only-checks)                                     | 0 / 0                               | 57                                      | Review the authored canonical resource and actual success body. Parent/child, command, polling-result and collection-role associations are not automatically original cross-method comparisons; prefer wire-compatible spec fixes over weakening the rule. |
| [additional-missing-request-policy](gap-analysis.md#typespec-only-checks)                                        | 0 / 0                               | 25                                      | Additional body-existence policy; the Swagger selector skips missing bodies. Review the wire contract rather than inventing a request for count parity.                                                                                                    |
| [additional-request-check-outside-swagger-200-201-selector](gap-analysis.md#typespec-only-checks)                | 0 / 0                               | 1                                       | Keep broader registered-request enforcement separate from the Swagger 200/201 selector.                                                                                                                                                                    |
| [same-operation-different-comparison](gap-analysis.md#typespec-only-checks)                                      | 0 / 0                               | 16                                      | Review the canonical association or selected status/body. A real warning on the route receives no credit for a different comparison.                                                                                                                       |
| [source-only-operation-not-in-selected-version](gap-analysis.md#typespec-only-checks)                            | 0 / 0                               | 4                                       | Retain source diagnostics and use supported version alignment for selected-version parity; do not suppress them to equalize totals.                                                                                                                        |

<a id="custom-lifecycle-registration"></a>

## Custom lifecycle registration/modeling gap

**Observed counts:** 3 Swagger raw / 3 member checks; 0 corresponding configured TypeSpec warnings. 0 captured owning diagnostic callbacks across 0 contexts before suppression.

**Coverage status:** unpaired-required-investigation-or-modeling.

**Cause, tradeoff and recommendation:** The PUT is absent from every registered resource's operation Set, despite a registered selected response. Review the low-level/custom template or its resource argument before adding explicit lifecycle registration. Verify emitted paths, operation IDs and wire schemas do not change; do not infer a canonical model from HTTP PUT alone. The separate three-decorator follow-up is Azure/azure-rest-api-specs#47952; its modified specs are not frozen-corpus coverage.

**Exact targets:** [a867f0b3a5246c71](instances/p-d2000d5bc232.md#s-a867f0b3a5246c71), [c399b6820a7911f4](instances/p-d2000d5bc232.md#s-c399b6820a7911f4), [f6f798cbc04b8634](instances/p-3d47c51b653f.md#s-f6f798cbc04b8634).

<a id="upstream-identity-bug"></a>

## Confirmed Swagger false positive

**Observed counts:** 15 Swagger raw / 15 member checks; 0 corresponding configured TypeSpec warnings. 0 captured owning diagnostic callbacks across 0 contexts before suppression.

**Coverage status:** confirmed-upstream-false-positive.

**Cause, tradeoff and recommendation:** Identical 200/201 references were compared by resolved JavaScript object identity. Do not reproduce this bug or count its absence as a missing useful diagnostic.

**Exact targets:** [b303b55475326bb1](instances/p-7c23914bec5d.md#s-b303b55475326bb1), [bd490485059e25dc](instances/p-1a17ac3fb584.md#s-bd490485059e25dc), [97862fe9352dc17d](instances/p-79b197f2d869.md#s-97862fe9352dc17d), [2687614a0ca6982e](instances/p-dbe559622b2b.md#s-2687614a0ca6982e), [20e9f2df566de610](instances/p-1e4b1f0cddaf.md#s-20e9f2df566de610), [84a4cb24142840d5](instances/p-1e4b1f0cddaf.md#s-84a4cb24142840d5), [3b8448268bb7dcd2](instances/p-c9e6c4ded28f.md#s-3b8448268bb7dcd2), [83adcf1aa2217d40](instances/p-665a329b65e9.md#s-83adcf1aa2217d40), [af6929bc1496914c](instances/p-0c954c82d021.md#s-af6929bc1496914c), [a970dca734af2a1e](instances/p-5941c238374d.md#s-a970dca734af2a1e), [d3f84100c93be405](instances/p-5941c238374d.md#s-d3f84100c93be405), [97ad659f49330ad9](instances/p-5941c238374d.md#s-97ad659f49330ad9), [c640094a903a8d9c](instances/p-5941c238374d.md#s-c640094a903a8d9c), [dbe6352c95eaaccb](instances/p-5941c238374d.md#s-dbe6352c95eaaccb), [e6a7d82dc4f453e8](instances/p-5941c238374d.md#s-e6a7d82dc4f453e8).

[Pinned implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/consistent-response-schema-for-put.ts): the result uses `!==` on resolved objects. Saved 200/201 references are identical in the same invoking document; no new resolver-object execution trace or newer upstream version was tested.

<a id="body-policy-owner"></a>

## Empty 200: real response-body issue, not two unequal payload models

**Observed counts:** 53 Swagger raw / 25 member checks; 0 corresponding configured TypeSpec warnings. 16 captured owning diagnostic callbacks across 25 contexts before suppression.

**Coverage status:** existing-owner-diagnostic-before-suppression.

**Cause, tradeoff and recommendation:** Keep schema consistency separate from response existence. Review no-response-body and authored suppressions, and repair the spec only against the actual wire contract. Its current implementation checks the first ordinary response and skips some template operations; source ownership alone is not measured coverage. The focused owner-predicate results are linked in gap-analysis.md.

**Exact targets:** [55f8c13b76ee23c3](instances/p-49581f50dce3.md#s-55f8c13b76ee23c3), [924247bbd9d61c2a](instances/p-d00f78f58133.md#s-924247bbd9d61c2a), [df021fee65ceae2f](instances/p-d00f78f58133.md#s-df021fee65ceae2f), [90c4b2c0c5193e8c](instances/p-d00f78f58133.md#s-90c4b2c0c5193e8c), [7fb97154f9ce23e5](instances/p-d00f78f58133.md#s-7fb97154f9ce23e5), [e6c42278fc611fee](instances/p-f43db0dc1fd6.md#s-e6c42278fc611fee), [90d6e26b20d2c935](instances/p-199707c82451.md#s-90d6e26b20d2c935), [2142b3573d5c8b43](instances/p-05203fab0aa5.md#s-2142b3573d5c8b43), [2cdfd153d5e916bb](instances/p-5941c238374d.md#s-2cdfd153d5e916bb), [3d653a84a1dea976](instances/p-49581f50dce3.md#s-3d653a84a1dea976), [685ef4b7fabbea0b](instances/p-da92c978c97e.md#s-685ef4b7fabbea0b), [9896c2b7172bc816](instances/p-da92c978c97e.md#s-9896c2b7172bc816), [2a485a015bc860db](instances/p-da92c978c97e.md#s-2a485a015bc860db), [37b4c877ee656026](instances/p-da92c978c97e.md#s-37b4c877ee656026), [df82f85c0059c07a](instances/p-da92c978c97e.md#s-df82f85c0059c07a), [445b8c82abe957ef](instances/p-da92c978c97e.md#s-445b8c82abe957ef), [7c49ac5c4bbb614d](instances/p-d00f78f58133.md#s-7c49ac5c4bbb614d), [44242262fca7602e](instances/p-d00f78f58133.md#s-44242262fca7602e), [a62af5b7649f1939](instances/p-d00f78f58133.md#s-a62af5b7649f1939), [dbb40f8beb5c7df1](instances/p-d00f78f58133.md#s-dbb40f8beb5c7df1), [dcb16038cea11cc9](instances/p-f43db0dc1fd6.md#s-dcb16038cea11cc9), [327922905ec9a60a](instances/p-199707c82451.md#s-327922905ec9a60a), [433e4303e6f36989](instances/p-05203fab0aa5.md#s-433e4303e6f36989), [1c595ce8051358dc](instances/p-5941c238374d.md#s-1c595ce8051358dc), [aa4aed8cc87b6761](instances/p-5941c238374d.md#s-aa4aed8cc87b6761).

<a id="bodyless-comparator-overreach"></a>

## Swagger schema-comparison false positive / policy overreach

**Observed counts:** 15 Swagger raw / 15 member checks; 0 corresponding configured TypeSpec warnings. 0 captured owning diagnostic callbacks across 0 contexts before suppression.

**Coverage status:** recommended-non-porting-not-approved.

**Cause, tradeoff and recommendation:** The comparison treats a correctly bodyless 202 or 204 as an unequal resource schema. Do not invent a response body or add a resource-schema warning merely to match that result. This does not establish that the operation's status set is ARM-compliant: arm-put-response-codes owns that separate question. This is a recommended intentional difference, not approved retirement or existing migration credit.

**Exact targets:** [e7a795042777d9cf](instances/p-6e7cc89a7ebd.md#s-e7a795042777d9cf), [e0504c2667af2c28](instances/p-6e7cc89a7ebd.md#s-e0504c2667af2c28), [86196a233810a562](instances/p-6e7cc89a7ebd.md#s-86196a233810a562), [147374c72a96fb47](instances/p-d883c2d5a2bc.md#s-147374c72a96fb47), [6fcb2ff88314e6da](instances/p-f543895a6651.md#s-6fcb2ff88314e6da), [6e59a8aafa900ec0](instances/p-43a32290b79b.md#s-6e59a8aafa900ec0), [7ee14429ae268362](instances/p-43a32290b79b.md#s-7ee14429ae268362), [d8943102fff456a3](instances/p-43a32290b79b.md#s-d8943102fff456a3), [71f3e9931e02ce3d](instances/p-43a32290b79b.md#s-71f3e9931e02ce3d), [71bebd7a6b39537e](instances/p-43a32290b79b.md#s-71bebd7a6b39537e), [25609454b7338515](instances/p-43a32290b79b.md#s-25609454b7338515), [b0cdaa08e24ed658](instances/p-43a32290b79b.md#s-b0cdaa08e24ed658), [8c82cbe71f357f18](instances/p-43a32290b79b.md#s-8c82cbe71f357f18), [47818b29f17a39b3](instances/p-43a32290b79b.md#s-47818b29f17a39b3), [90675c396d5e87a2](instances/p-05203fab0aa5.md#s-90675c396d5e87a2).

<a id="collection-comparator-overreach"></a>

## Swagger collection-shape comparison false positive

**Observed counts:** 4 Swagger raw / 4 member checks; 0 corresponding configured TypeSpec warnings. 0 captured owning diagnostic callbacks across 0 contexts before suppression.

**Coverage status:** recommended-non-porting-not-approved.

**Cause, tradeoff and recommendation:** The compared payloads are an entity/array/list-envelope role difference, not evidence of different resource item models. The saved schemas show matching item identity. Keep list envelope/item validation separate; do not compare wrapper reference names across collection and item-like methods. This recommendation is not approved retirement or existing migration credit.

**Exact targets:** [a4753c8793120f98](instances/p-560dd8313baf.md#s-a4753c8793120f98), [932685760e4abb70](instances/p-75b0ebe30c60.md#s-932685760e4abb70), [96597104b5cfbfbf](instances/p-5941c238374d.md#s-96597104b5cfbfbf), [2d6708f576319f69](instances/p-618b7f706185.md#s-2d6708f576319f69).

<a id="custom-collection-request"></a>

## Bulk/collection request contract, not ordinary resource replacement

**Observed counts:** 2 Swagger raw / 2 member checks; 0 corresponding configured TypeSpec warnings. 0 captured owning diagnostic callbacks across 0 contexts before suppression.

**Coverage status:** unpaired-required-investigation-or-modeling.

**Cause, tradeoff and recommendation:** Annotations creates an item but returns an array; FirewallRules_Replace supplies a list to a collection operation. These shapes are not automatically equivalent, but HTTP PUT alone does not establish a single-resource replacement contract. Require spec-owner intent before extending the canonical-resource rule; do not claim these are confirmed compliant APIs.

**Exact targets:** [43582b9e61743914](instances/p-560dd8313baf.md#s-43582b9e61743914), [e44a5097b4b0fd88](instances/p-5941c238374d.md#s-e44a5097b4b0fd88).

<a id="custom-command-request"></a>

## Action-like PUT contract

**Observed counts:** 2 Swagger raw / 2 member checks; 0 corresponding configured TypeSpec warnings. 0 captured owning diagnostic callbacks across 0 contexts before suppression.

**Coverage status:** unpaired-required-investigation-or-modeling.

**Cause, tradeoff and recommendation:** Gateway API association and storage migration use command/association inputs rather than the parent resource model. GatewayApi is registered as action, has a different ApiContract response and explicitly suppresses the current ARM rule. Do not compare its input to the Gateway parent simply because its verb is PUT. Review API design and justified exceptions separately rather than widening this resource listener.

**Exact targets:** [4f6894b5bb1a95e3](instances/p-6e7cc89a7ebd.md#s-4f6894b5bb1a95e3), [7375fbc9fd2cdf33](instances/p-618b7f706185.md#s-7375fbc9fd2cdf33).

<a id="unregistered-entity-request"></a>

## Unregistered body-bearing request/response mismatch

**Observed counts:** 34 Swagger raw / 4 member checks; 0 corresponding configured TypeSpec warnings. 0 captured owning diagnostic callbacks across 0 contexts before suppression.

**Coverage status:** unpaired-required-investigation-or-modeling.

**Cause, tradeoff and recommendation:** The differing request and response are observable, but no registered canonical resource is established. ExportConfiguration, TestJob, ConnectionMonitor and PacketCapture need owner review of read-only fields, visibility and actual contract before a modeling repair. These are four checked PUTs, not their repeated raw finding total. Do not add a generic recursive schema comparator for these legacy DTOs.

**Exact targets:** [571ef2a8440d26f5](instances/p-560dd8313baf.md#s-571ef2a8440d26f5), [519e41ba16bd20e7](instances/p-49581f50dce3.md#s-519e41ba16bd20e7), [4886ec579aad3049](instances/p-199707c82451.md#s-4886ec579aad3049), [b9045e5e0128dbbd](instances/p-199707c82451.md#s-b9045e5e0128dbbd).

<a id="parent-canonical-association"></a>

## Canonical parent differs from the actual child/result response

**Observed counts:** 3 Swagger raw / 3 member checks; 0 corresponding configured TypeSpec warnings. 0 captured owning diagnostic callbacks across 0 contexts before suppression.

**Coverage status:** unpaired-required-investigation-or-modeling.

**Cause, tradeoff and recommendation:** ApiManagement PrivateEndpointConnection uses ApiManagementServiceResource as the legacy resource argument; RecoveryServices certificate uses Vault but returns VaultCertificateResponse. The complete registered-alias graph also exposes SyncJob.create as a read association of SourceControl, not an eligible create/update association for the SyncJob result. Existing canonical warnings compare to the parent, not the original request/result or SyncJob PUT/GET pair. Review child-resource/custom-operation modeling and preserve wire behavior; an extra equality warning is not the first fix.

**Exact targets:** [9eca5628f4dd299e](instances/p-6e7cc89a7ebd.md#s-9eca5628f4dd299e), [86cde2d203ba3710](instances/p-49581f50dce3.md#s-86cde2d203ba3710), [e7c4ffbd689792f0](instances/p-551502b046ca.md#s-e7c4ffbd689792f0).

<a id="cross-method-entity-contract"></a>

## Genuine PUT/GET resource-shape difference

**Observed counts:** 1 Swagger raw / 1 member checks; 0 corresponding configured TypeSpec warnings. 0 captured owning diagnostic callbacks across 0 contexts before suppression.

**Coverage status:** unpaired-required-investigation-or-modeling.

**Cause, tradeoff and recommendation:** SyncJob's PUT response has read-only name/type/id; GET has writable id, omits name/type, and adds nested exception. These are not merely differently named aliases. Establish whether the wire contract should share a model; do not rewrite the spec if the service intentionally returns a summary versus detail. One observed route does not justify a general recursive, version/visibility-aware cross-operation structural comparator.

**Exact targets:** [e3d27963b9f80e88](instances/p-49581f50dce3.md#s-e3d27963b9f80e88).

<a id="supported-polymorphism"></a>

## Deliberate polymorphism with unresolved canonical request association

**Observed counts:** 1 Swagger raw / 1 member checks; 0 corresponding configured TypeSpec warnings. 0 captured owning diagnostic callbacks across 0 contexts before suppression.

**Coverage status:** polymorphic-contract-with-unassessed-request-association.

**Cause, tradeoff and recommendation:** ThreatIntelligenceIndicatorModel derives from the kind-discriminated ThreatIntelligenceInformation response base. The generic response predicate accepts discriminated ancestor/descendant resources, but the request predicate still requires effective identity with the declared canonical resource. The frozen PUT is unassociated, so its absent request warning is not observed request-polymorphism acceptance. Preserve the intended hierarchy and establish the canonical resource before changing registration; do not claim corresponding warning parity or rewrite the DTOs merely to satisfy strict identity.

**Exact targets:** [4de3358332155e13](instances/p-3d47c51b653f.md#s-4de3358332155e13).

<a id="repeated-invocations"></a>

## Repeated reference invocations

The same referenced operation/schema can be diagnosed while validating different invoking documents. All raw input/reported-document identities are retained; only exact same-member/schema contexts are grouped. This is counting multiplicity, not a production-rule defect or normalization of different violations.

| Member / project                                                                                                                     | Swagger raw | Grouped mapped contexts | TypeSpec corresponding warnings |
| ------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ----------------------- | ------------------------------- |
| XmsResourceInPutResponse / [`specification/network/resource-manager/Microsoft.Network/Network/Network`](instances/p-199707c82451.md) | 108         | 10                      | 10                              |

<a id="member-put-request-response-scheme-arm"></a>

## PutRequestResponseSchemeArm: implemented policy and remaining boundary

153 of 168 original member-check contexts are diagnosed: 144 by corresponding configured warnings; 9 additional contexts by captured owning diagnostics before authored suppression. Remaining: 15 unresolved/modeling or deferred contract contexts. Captured owning diagnostics receive credit despite suppression, without changing configured raw totals. Contexts are not equivalent-defect counts; universal violation percentages remain unassessed.

[Member assessment](members/PutRequestResponseSchemeArm/migration.md). Exact source/body/status/canonical metadata and warning IDs are retained for both matching and differing targets.

<a id="member-consistent-response-schema-for-put"></a>

## ConsistentResponseSchemaForPut: implemented policy and remaining boundary

1 of 16 original member-check contexts are diagnosed: 1 by corresponding configured warnings. Remaining: 15 confirmed Swagger false-positive contexts. 1 mapped context(s) also have captured owning diagnostics; coverage counts each once. Captured owning diagnostics receive credit despite suppression, without changing configured raw totals. Contexts are not equivalent-defect counts; universal violation percentages remain unassessed.

[Member assessment](members/ConsistentResponseSchemaForPut/migration.md). Exact source/body/status/canonical metadata and warning IDs are retained for both matching and differing targets.

<a id="member-xms-resource-in-put-response"></a>

## XmsResourceInPutResponse: implemented policy and remaining boundary

57 of 57 original member-check contexts are diagnosed: 57 by corresponding configured warnings. Captured owning diagnostics receive credit despite suppression, without changing configured raw totals. Contexts are not equivalent-defect counts; universal violation percentages remain unassessed.

[Member assessment](members/XmsResourceInPutResponse/migration.md). Exact source/body/status/canonical metadata and warning IDs are retained for both matching and differing targets.

<a id="member-put-get-patch-response-schema"></a>

## PutGetPatchResponseSchema: implemented policy and remaining boundary

16 of 36 original member-check contexts are diagnosed: 16 additional contexts by captured owning diagnostics before authored suppression. Remaining: 19 recommended comparison exclusions awaiting approval; 1 unresolved/modeling or deferred contract contexts. Captured owning diagnostics receive credit despite suppression, without changing configured raw totals. Contexts are not equivalent-defect counts; universal violation percentages remain unassessed.

[Member assessment](members/PutGetPatchResponseSchema/migration.md). Exact source/body/status/canonical metadata and warning IDs are retained for both matching and differing targets.

## TypeSpec-only checks

These counts have no attributed selected Swagger finding for the same comparison. A route may still have an unrelated Swagger warning. Canonical response policy compares against the authored resource, not necessarily another method's body. This explains additional diagnostics but does not prove every association is correct.

| Classification                                            | TypeSpec raw | Gap analysis and decision                                                                                                                                                                                                                                  |
| --------------------------------------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| additional-canonical-response-policy                      | 57           | Review the authored canonical resource and actual success body. Parent/child, command, polling-result and collection-role associations are not automatically original cross-method comparisons; prefer wire-compatible spec fixes over weakening the rule. |
| additional-missing-request-policy                         | 25           | Additional body-existence policy; the Swagger selector skips missing bodies. Review the wire contract rather than inventing a request for count parity.                                                                                                    |
| additional-request-check-outside-swagger-200-201-selector | 1            | Keep broader registered-request enforcement separate from the Swagger 200/201 selector.                                                                                                                                                                    |
| same-operation-different-comparison                       | 16           | Review the canonical association or selected status/body. A real warning on the route receives no credit for a different comparison.                                                                                                                       |
| source-only-operation-not-in-selected-version             | 4            | Retain source diagnostics and use supported version alignment for selected-version parity; do not suppress them to equalize totals.                                                                                                                        |

Every extra diagnostic is listed with its message, actual response and canonical association in [the exact inventory](instance-correspondence.md#typespec-finding-accounting), including one-sided projects.

## Compatibility-gated spec follow-ups

[Draft #47952](https://github.com/Azure/azure-rest-api-specs/pull/47952) adds only three missing create/update associations. Registry probes changed as intended; five all-version OpenAPI outputs are byte-identical. Ten public TCGC outputs differ only in the source-version fingerprint. Full SDK generation was not run and public TCGC omits internal `__raw`, so specialized ARM SDK neutrality is not proven. [Receipt](receipts/spec-followup-compatibility-20261105.json).

API Management's parent-resource argument also controls paths; a simple argument swap is not wire-neutral. The RecoveryServices certificate contract has no established canonical child resource. SyncJob has an actual PUT/GET difference (read-only name/type/id versus writable id, missing name/type and added exception). ThreatIntel's response ancestry is supported, but its frozen PUT is unassociated and request identity remains strict: absence of a warning is not evidence that a registered derived request is accepted. These remain explicit owner/modeling decisions, not broad-linter special cases.

## Code-backed representatives

Excerpts are verbatim pinned authored source and saved Swagger, not invented compiling examples. Resolved gaps retain their original example and current observed disposition.

<a id="example-0"></a>

### Resolved: registered PUT absent from retained operation map

**Project/API version:** `specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement` / `2025-09-01-preview`. **Source:** [Microsoft.ApiManagement.ApiContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/ApiContract.tsp#L93), lines 91-123.

```typespec
   * Creates new or updates existing specified API of the API Management service instance.
   */
  createOrUpdate is ApiContractOps.CreateOrUpdateAsync<
    ApiContract,
    Request = ApiCreateOrUpdateParameter,
    Parameters = {
      /**
       * ETag of the Entity. Not required when creating an entity, but required when updating an entity.
       */
      #suppress "@azure-tools/typespec-azure-core/casing-style" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
      @header("If-Match")
      `If-Match`?: string;
    },
    Response =
      | (ArmResponse<ApiContract> &
          ArmCombinedLroHeaders<FinalResult = ApiContract> & {
            /**
             * Current entity state version. Should be treated as opaque and used to make conditional HTTP requests.
             */
            @header("ETag")
            eTag: string;
          })
      | (ArmResourceCreatedResponse<
          ApiContract,
          LroHeaders = ArmCombinedLroHeaders<FinalResult = ApiContract>
        > & {
          /**
           * Current entity state version. Should be treated as opaque and used to make conditional HTTP requests.
           */
          @header("ETag")
          eTag: string;
        })
  >;
```

```json
{
  "put": {
    "operationId": "Api_CreateOrUpdate",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/ApiContract"
        }
      },
      "201": {
        "schema": {
          "$ref": "#/definitions/ApiContract"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/ApiCreateOrUpdateParameter"
        }
      }
    ]
  }
}
```

**Observed comparison / gap analysis and decision:** The singular retained map loses this operation, but the append-only registered-resource operation Set retains its createOrUpdate identifier and canonical selected response. The implemented fix applies the existing request predicate through that Set, without a broad PUT listener or registry redesign. Swagger remains at 1 raw observation; the final-source TypeSpec run now reports 1 corresponding requestMismatch, compared with 0 before the fix.

<a id="example-1"></a>

### Resolved: PUT stored under lists rather than lifecycle.createOrUpdate

**Project/API version:** `specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement` / `2025-09-01-preview`. **Source:** [Microsoft.ApiManagement.TagDescriptionContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagDescriptionContract.tsp#L102), lines 100-128.

```typespec
   * Create/Update tag description in scope of the Api.
   */
  createOrUpdate is TagDescriptionContractsOps.CreateOrUpdateSync<
    TagDescriptionContract,
    Request = TagDescriptionCreateParameters,
    Parameters = {
      /**
       * ETag of the Entity. Not required when creating an entity, but required when updating an entity.
       */
      #suppress "@azure-tools/typespec-azure-core/casing-style" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
      @header("If-Match")
      `If-Match`?: string;
    },
    Response =
      | (ArmResponse<TagDescriptionContract> & {
          /**
           * Current entity state version. Should be treated as opaque and used to make conditional HTTP requests.
           */
          @header("ETag")
          eTag: string;
        })
      | (ArmCreatedResponse<TagDescriptionContract> & {
          /**
           * Current entity state version. Should be treated as opaque and used to make conditional HTTP requests.
           */
          @header("ETag")
          eTag: string;
        })
  >;
```

```json
{
  "put": {
    "operationId": "ApiTagDescription_CreateOrUpdate",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/TagDescriptionContract"
        }
      },
      "201": {
        "schema": {
          "$ref": "#/definitions/TagDescriptionContract"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/TagDescriptionCreateParameters"
        }
      }
    ]
  }
}
```

**Observed comparison / gap analysis and decision:** The legacy PUT is retained under lists and also in the registered-resource operation Set as createOrUpdate. The implemented Set-based request traversal reaches it while preserving action, compliant, multipart and suppression controls. Swagger remains at 1 raw observation; the final-source TypeSpec run now reports 1 corresponding requestMismatch, compared with 0 before the fix.

<a id="example-2"></a>

### New warning compares FunctionEnvelope to a KeyInfo wire contract

**Project/API version:** `specification/web/resource-manager/Microsoft.Web/AppService` / `2026-07-15`. **Source:** [Microsoft.Web.FunctionEnvelopeOperationGroup.createOrUpdateFunctionSecretSlot](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/FunctionEnvelope.tsp#L350-L355), lines 350-355.

```typespec
  createOrUpdateFunctionSecretSlot is FunctionEnvelopeSlotOperationGroupOps.CreateOrUpdateAsync<
    FunctionEnvelope,
    Request = KeyInfo,
    Response = ArmResponse<KeyInfo> | ArmResourceCreatedSyncResponse<KeyInfo>,
    OverrideErrorType = DefaultErrorResponse
  >;
```

```json
{
  "put": {
    "operationId": "WebApps_CreateOrUpdateFunctionSecretSlot",
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/KeyInfo"
        }
      }
    ],
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/KeyInfo"
        }
      },
      "201": {
        "schema": {
          "$ref": "#/definitions/KeyInfo"
        }
      }
    }
  }
}
```

**Observed comparison / gap analysis and decision:** The Swagger request/response member reports zero: both payloads reference KeyInfo. Canonical request and response warnings compare that contract with the registered FunctionEnvelope parent; they are not request/response or marker correspondence. The dedicated marker rule independently diagnoses the missing marker on KeyInfo. Review the legacy resource association with the service owner before a wire-equivalent modeling correction; do not change the KeyInfo wire contract or weaken the shared predicate merely to equalize counts.

<a id="example-3"></a>

### New source-only warning on a removed operation sharing the replacement route

**Project/API version:** `specification/cdn/resource-manager/Microsoft.Cdn/Cdn` / `2026-08-01-preview`. **Source:** [Microsoft.Cdn.RuleSets.createV1 and its replacement](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/RuleSet.tsp#L39-L59), lines 39-48.

```typespec
  @removed(Versions.v2025_12_01)
  @renamedFrom(Versions.v2025_12_01, "create")
  @sharedRoute
  @put
  createV1 is Azure.ResourceManager.Legacy.CreateOrUpdateAsync<
    RuleSet,
    void,
    Response = ArmResponse<RuleSet> | ArmCreatedResponse<RuleSet>,
    Error = ErrorResponse
  >;
```

```json
{
  "put": {
    "operationId": "RuleSets_Create",
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/RuleSet"
        }
      }
    ],
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/RuleSet"
        }
      },
      "201": {
        "schema": {
          "$ref": "#/definitions/RuleSet"
        }
      }
    }
  }
}
```

**Observed comparison / gap analysis and decision:** The final-source TypeSpec run adds one missingRequest on createV1, removed at 2025-12-01. It has no selected-version operation counterpart. The current Swagger reuses that route for create, added at 2025-12-01 with an optional RuleSet body; its payload is not the old void request. Thus no selected-version Swagger comparison exists for createV1, even though a replacement operation occupies the same route. Retain the source warning and use version-aligned comparison for selected-version parity; do not infer identity from the route or suppress the warning to balance counts.

<a id="example-4"></a>

### Matched request and canonical response resource

**Project/API version:** `specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement` / `2025-09-01-preview`. **Source:** [Microsoft.ApiManagement.IdentityProviderContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/IdentityProviderContract.tsp#L62), lines 60-88.

```typespec
   * Creates or Updates the IdentityProvider configuration.
   */
  createOrUpdate is Azure.ResourceManager.Legacy.CreateOrUpdateSync<
    IdentityProviderContract,
    Request = IdentityProviderCreateContract,
    Parameters = {
      /**
       * ETag of the Entity. Not required when creating an entity, but required when updating an entity.
       */
      #suppress "@azure-tools/typespec-azure-core/casing-style" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
      @header("If-Match")
      `If-Match`?: string;
    },
    Response =
      | (ArmResponse<IdentityProviderContract> & {
          /**
           * Current entity state version. Should be treated as opaque and used to make conditional HTTP requests.
           */
          @header("ETag")
          eTag?: string;
        })
      | (ArmResourceCreatedSyncResponse<IdentityProviderContract> & {
          /**
           * Current entity state version. Should be treated as opaque and used to make conditional HTTP requests.
           */
          @header("ETag")
          eTag?: string;
        })
  >;
```

```json
{
  "put": {
    "operationId": "IdentityProvider_CreateOrUpdate",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/IdentityProviderContract"
        }
      },
      "201": {
        "schema": {
          "$ref": "#/definitions/IdentityProviderContract"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/IdentityProviderCreateContract"
        }
      }
    ]
  }
}
```

**Observed comparison / gap analysis and decision:** Swagger reports one request-schema finding. TypeSpec reports requestMismatch on the same PUT; its canonical resource is the selected response body. No rule change is needed for this observed pairing, but this is not universal structural-equivalence proof.

<a id="example-5"></a>

### Warning on the same operation compares a different contract

**Project/API version:** `specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement` / `2025-09-01-preview`. **Source:** [Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/PrivateEndpointConnection.tsp#L29), lines 27-44.

```typespec
   */
  #suppress "@azure-tools/typespec-azure-resource-manager/arm-put-operation-response-codes" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  createOrUpdate is Azure.ResourceManager.Legacy.CreateOrUpdateAsync<
    ApiManagementServiceResource,
    Request = PrivateEndpointConnectionRequest,
    Response =
      | ArmResourceUpdatedResponse<Azure.ResourceManager.CommonTypes.PrivateEndpointConnection>
      | ArmAcceptedLroResponse<LroHeaders = ArmLroLocationHeader<FinalResult = PrivateEndpointConnection> &
          Azure.Core.Foundations.RetryAfterHeader>,
    Parameters = {
      /**
       * API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
       */
      @path
      @segment("privateEndpointConnections")
      privateEndpointConnectionName: string;
    }
  >;
```

```json
{
  "put": {
    "operationId": "PrivateEndpointConnection_CreateOrUpdate",
    "responses": {
      "200": {
        "schema": {
          "$ref": "../../../../../../../../../common-types/resource-management/v5/privatelinks.json#/definitions/PrivateEndpointConnection"
        }
      },
      "202": {}
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/PrivateEndpointConnectionRequest"
        }
      }
    ]
  }
}
```

**Observed comparison / gap analysis and decision:** The request warning compares PrivateEndpointConnectionRequest to the parent ApiManagementServiceResource, while the actual 200 body is CommonTypes.PrivateEndpointConnection. The response warning also compares to that parent, not the original request/child-response pair. Neither receives correspondence credit for this member. A simple resource argument swap changes route parameters, and inherited registration survives an added child decorator. Keep this as compatibility-gated template/spec-owner work rather than a blanket equality change.

<a id="example-6"></a>

### Unassociated PUT with no registered response model

**Project/API version:** `specification/network/resource-manager/Microsoft.Network/Network/Network` / `2026-03-01`. **Source:** [Microsoft.Network.ConnectionMonitorResults.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/network/resource-manager/Microsoft.Network/Network/Network/ConnectionMonitorResult.tsp#L56), lines 54-67.

```typespec
   */
  @tag("ConnectionMonitors")
  createOrUpdate is Azure.ResourceManager.Legacy.CreateOrUpdateAsync<
    ConnectionMonitorResult,
    Request = ConnectionMonitor,
    Parameters = {
      /**
       * Value indicating whether connection monitor V1 should be migrated to V2 format.
       */
      @query("migrate")
      migrate?: string;
    },
    Error = ErrorResponse
  >;
```

```json
{
  "put": {
    "operationId": "ConnectionMonitors_CreateOrUpdate",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/ConnectionMonitorResult"
        }
      },
      "201": {
        "schema": {
          "$ref": "#/definitions/ConnectionMonitorResult"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/ConnectionMonitor"
        }
      }
    ]
  }
}
```

**Observed comparison / gap analysis and decision:** ConnectionMonitor and ConnectionMonitorResult are different body-bearing DTOs, but inheritance from an ARM-shaped base does not establish a registered canonical resource. Review the legacy contract, read-only result fields and model registration; do not broaden the resource listener to every PUT or introduce recursive emitted-schema equality for this case. Sixteen repeated raw observations represent one checked PUT. TypeSpec: 0 corresponding findings.

<a id="example-7"></a>

### Canonical request is accepted while selected 200 has no schema

**Project/API version:** `specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace` / `2025-01-01`. **Source:** [Microsoft.Marketplace.PrivateStores.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace/PrivateStore.tsp#L43), lines 41-49.

```typespec
  #suppress "@azure-tools/typespec-azure-resource-manager/arm-put-operation-response-codes" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  #suppress "@azure-tools/typespec-azure-resource-manager/no-response-body" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  createOrUpdate is Azure.ResourceManager.Legacy.CreateOrReplaceSync<
    PrivateStore,
    BaseParameters = Azure.ResourceManager.Foundations.TenantBaseParameters,
    Response = OkResponse,
    Error = ErrorResponse,
    OptionalRequestBody = true
  >;
```

```json
{
  "put": {
    "operationId": "PrivateStore_CreateOrUpdate",
    "responses": {
      "200": {}
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/PrivateStore"
        }
      }
    ]
  }
}
```

**Observed comparison / gap analysis and decision:** The canonical request is valid for this rule; the selected 200 is empty. The existing no-response-body visitor diagnoses this exact operation when evaluated before suppression, and the source explicitly suppresses that owner. Review that suppression or repair the modeled/wire response, rather than adding a second schema-equality warning. Swagger: 1 raw observation; TypeSpec shared rule: 0 corresponding findings.

<a id="example-8"></a>

### Upstream staging object-identity false positive

**Project/API version:** `specification/durabletask/resource-manager/Microsoft.DurableTask/DurableTask` / `2026-05-01-preview`. **Source:** [Microsoft.DurableTask.Schedulers.createOrUpdatePrivateEndpointConnection](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/durabletask/resource-manager/Microsoft.DurableTask/DurableTask/scheduler.tsp#L183), lines 181-183.

```typespec
  @added(Versions.v2026_02_01)
  @doc("Create or update a private endpoint connection for the durable task scheduler")
  createOrUpdatePrivateEndpointConnection is PrivateEndpointOperations.CreateOrUpdateAsync<Scheduler>;
```

```json
{
  "put": {
    "operationId": "Schedulers_CreateOrUpdatePrivateEndpointConnection",
    "responses": {
      "200": {
        "schema": {
          "$ref": "../../../../../../../../../common-types/resource-management/v6/privatelinks.json#/definitions/PrivateEndpointConnection"
        }
      },
      "201": {
        "schema": {
          "$ref": "../../../../../../../../../common-types/resource-management/v6/privatelinks.json#/definitions/PrivateEndpointConnection"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "../../../../../../../../../common-types/resource-management/v6/privatelinks.json#/definitions/PrivateEndpointConnection"
        }
      }
    ]
  }
}
```

**Observed comparison / gap analysis and decision:** Raw 200 and 201 references are identical in the same invoking document. The original uses !== on resolved JavaScript objects, not structural equality. This classification uses saved references and pinned code, not a newly captured resolver-object execution trace. No TypeSpec rule update required: intentionally do not reproduce the upstream identity bug. Swagger: 1 raw observation(s); TypeSpec: 0 same-operation finding(s), 0 credited.

<a id="example-9"></a>

### Genuine plain-response 200/201 mismatch

**Project/API version:** `specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota` / `2020-10-25`. **Source:** [Quota.CurrentQuotaLimitBases.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/CurrentQuotaLimitBase.tsp#L71), lines 69-82.

```typespec
  @tag("QuotaInformation")
  @Azure.Core.useFinalStateVia("original-uri")
  createOrUpdate is ArmResourceCreateOrReplaceAsync<
    CurrentQuotaLimitBase,
    QuotaPutBaseParam,
    Response =
      | ArmResourceUpdatedResponse<CurrentQuotaLimitBase>
      | ArmCreatedResponse<
          QuotaRequestSubmitResponse201,
          ExtraHeaders = ArmLroLocationHeader<FinalResult = CurrentQuotaLimitBase> &
            Azure.Core.Foundations.RetryAfterHeader
        >,
    Error = ExceptionResponse
  >;
```

```json
{
  "put": {
    "operationId": "Quota_CreateOrUpdate",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/CurrentQuotaLimitBase"
        }
      },
      "201": {
        "schema": {
          "$ref": "#/definitions/QuotaRequestSubmitResponse201"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/CurrentQuotaLimitBase"
        }
      }
    ]
  }
}
```

**Observed comparison / gap analysis and decision:** Quota intentionally returns the quota resource at 200 and a submission-status envelope at 201, with the final LRO result separately set to the quota resource. The generic actual-success-body fix now diagnoses the noncanonical 201 body. Azure Core response-schema-problem also reports the initial-payload difference in the captured pre-suppression callback. Credit this original context once in the covered union, retain both diagnostic receipts, and review the legacy initial-envelope policy with the service owner.

<a id="example-10"></a>

### Selected PUT response lacks resource extension

**Project/API version:** `specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/AnalyticsItems` / `2015-05-01`. **Source:** [AnalyticsItems.AnalyticsItemsOperationGroup.put](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/AnalyticsItems/routes.tsp#L95), lines 93-123.

```typespec
  @route("/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}/item")
  @put
  put(
    ...ApiVersionParameter,
    ...SubscriptionIdParameter,
    ...ResourceGroupParameter,

    /**
     * The name of the Application Insights component resource.
     */
    @path
    resourceName: string,

    /**
     * Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
     */
    @path
    scopePath: ItemScopePath,

    /**
     * Flag indicating whether or not to force save an item. This allows overriding an item if it already exists.
     */
    @query("overrideItem")
    overrideItem?: boolean,

    /**
     * Properties that need to be specified to create a new item and add it to an Application Insights component.
     */
    @body
    itemProperties: ApplicationInsightsComponentAnalyticsItem,
  ): ArmResponse<ApplicationInsightsComponentAnalyticsItem>;
```

```json
{
  "put": {
    "operationId": "AnalyticsItems_Put",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/ApplicationInsightsComponentAnalyticsItem"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/ApplicationInsightsComponentAnalyticsItem"
        }
      }
    ]
  }
}
```

**Observed comparison / gap analysis and decision:** The selected AnalyticsItem lacks the emitted resource marker and is not a registered ARM resource. The dedicated opt-in arm-put-response-resource rule now reports the same selected PUT response independently of canonical registration: one Swagger check and one corresponding TypeSpec marker warning. This establishes marker-policy correspondence, not proof that every custom PUT payload should be remodeled as a resource. Keep any justified custom/action exception explicit.

<a id="example-11"></a>

### Cross-operation comparison includes an absent selected response reference

**Project/API version:** `specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement` / `2025-09-01-preview`. **Source:** [Microsoft.ApiManagement.DelegationSettings.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/PortalDelegationSettings.tsp#L67), lines 65-78.

```typespec
  #suppress "@azure-tools/typespec-azure-resource-manager/arm-put-operation-response-codes" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  #deprecated "deprecated"
  createOrUpdate is ArmResourceCreateOrReplaceSync<
    PortalDelegationSettings,
    Parameters = {
      /**
       * ETag of the Entity. Not required when creating an entity, but required when updating an entity.
       */
      #suppress "@azure-tools/typespec-azure-core/casing-style" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
      @header("If-Match")
      `If-Match`?: string;
    },
    Response = ArmResourceUpdatedResponse<PortalDelegationSettings>
  >;
```

```json
{
  "put": {
    "operationId": "DelegationSettings_CreateOrUpdate",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/PortalDelegationSettings"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/PortalDelegationSettings"
        }
      }
    ]
  },
  "get": {
    "operationId": "DelegationSettings_Get",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/PortalDelegationSettings"
        }
      }
    }
  },
  "patch": {
    "operationId": "DelegationSettings_Update",
    "responses": {},
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/PortalDelegationSettings"
        }
      }
    ]
  }
}
```

**Observed comparison / gap analysis and decision:** DelegationSettings returns a resource for PUT/GET and correctly has no body at PATCH 204. Comparing its absent PATCH schema to that resource is a Swagger schema-comparison false positive, not evidence of a different resource model. Recommend not porting this comparison; no whole-operation compliance, approved retirement or new migration credit is claimed.

<a id="example-12"></a>

### Cross-operation comparison has distinct selected references

**Project/API version:** `specification/automation/resource-manager/Microsoft.Automation/Automation` / `2024-10-23`. **Source:** [Microsoft.Automation.SourceControls.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/SourceControl.tsp#L105), lines 103-116.

```typespec
  @OpenAPI.externalDocs("http://aka.ms/azureautomationsdk/sourcecontrolsyncjoboperations")
  @put
  create is ArmResourceRead<
    SourceControl,
    BaseParameters = Azure.ResourceManager.Foundations.DefaultBaseParameters<SourceControl>,
    Response = ArmResourceCreatedSyncResponse<SourceControlSyncJob>,
    Parameters = SourceControlSyncJobIdParameter & {
      /**
       * The parameters supplied to the create source control sync job operation.
       */
      @body
      parameters: SourceControlSyncJobCreateParameters;
    }
  >;
```

```json
{
  "put": {
    "operationId": "SourceControlSyncJob_Create",
    "responses": {
      "201": {
        "schema": {
          "$ref": "#/definitions/SourceControlSyncJob"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/SourceControlSyncJobCreateParameters"
        }
      }
    ]
  },
  "get": {
    "operationId": "SourceControlSyncJob_Get",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/SourceControlSyncJobById"
        }
      }
    }
  }
}
```

**Observed comparison / gap analysis and decision:** SourceControlSyncJob and SourceControlSyncJobById genuinely differ: the PUT response includes read-only name/type/id, whereas GET has writable id, omits name/type and adds nested exception. Request spec-owner confirmation of the wire contract before sharing models. One observed route does not justify a general recursive cross-operation comparator; retain this as a known gap, not an alias false positive. Swagger: 1 raw observation; TypeSpec: 0 corresponding findings.

<a id="example-13"></a>

### Same PUT warning, but original selects empty 200 instead of 201

**Project/API version:** `specification/automation/resource-manager/Microsoft.Automation/Automation` / `2024-10-23`. **Source:** [Microsoft.Automation.DscNodeConfigurations.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/DscNodeConfiguration.tsp#L45), lines 43-55.

```typespec
  #suppress "@azure-tools/typespec-azure-core/no-openapi" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  @OpenAPI.externalDocs("http://aka.ms/azureautomationsdk/dscnodeconfigurations")
  createOrUpdate is Azure.ResourceManager.Legacy.CreateOrUpdateAsync<
    DscNodeConfiguration,
    Request = DscNodeConfigurationCreateOrUpdateParameters,
    Response =
      | OkResponse
      | ArmResourceCreatedResponse<
          DscNodeConfiguration,
          ArmLroLocationHeader<FinalResult = DscNodeConfiguration> &
            Azure.Core.Foundations.RetryAfterHeader
        >
  >;
```

```json
{
  "put": {
    "operationId": "DscNodeConfiguration_CreateOrUpdate",
    "responses": {
      "200": {},
      "201": {
        "schema": {
          "$ref": "#/definitions/DscNodeConfiguration"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/DscNodeConfigurationCreateOrUpdateParameters"
        }
      }
    ]
  }
}
```

**Observed comparison / gap analysis and decision:** Swagger selects the empty 200, while this rule compares the request to the 201 resource; those findings are not equivalent. The existing no-response-body predicate separately diagnoses the empty 200 before the source's explicit suppression. Review the body-owner suppression/contract rather than adding status-specific equality solely for parity.

<a id="example-14"></a>

### additional-missing-request-policy

**Project/API version:** `specification/dns/resource-manager/Microsoft.Network/Dns` / `2023-07-01-preview`. **Source:** [Microsoft.Network.DnssecConfigs.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/dns/resource-manager/Microsoft.Network/Dns/DnssecConfig.tsp#L45), lines 43-66.

```typespec
   * Creates or updates the DNSSEC configuration on a DNS zone.
   */
  createOrUpdate is Azure.ResourceManager.Legacy.CreateOrReplaceAsync<
    DnssecConfig,
    Request = void,
    Parameters = {
      /**
       * The etag of the DNSSEC configuration. Omit this value to always overwrite the DNSSEC configuration. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes.
       */
      #suppress "@azure-tools/typespec-azure-core/casing-style" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
      @header("If-Match")
      IfMatch?: string;

      /**
       * Set to '*' to allow this DNSSEC configuration to be created, but to prevent updating existing DNSSEC configuration. Other values will be ignored.
       */
      #suppress "@azure-tools/typespec-azure-core/casing-style" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
      @header("If-None-Match")
      IfNoneMatch?: string;
    },
    LroHeaders = ArmLroLocationHeader<FinalResult = DnssecConfig> &
      Azure.Core.Foundations.RetryAfterHeader,
    Error = CloudError
  >;
```

```json
{
  "put": {
    "operationId": "DnssecConfigs_CreateOrUpdate",
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/DnssecConfig"
        }
      },
      "201": {
        "schema": {
          "$ref": "#/definitions/DnssecConfig"
        }
      }
    }
  }
}
```

**Observed comparison / gap analysis and decision:** The original skips missing request schemas; the TypeSpec linter reports missingRequest for void. This is additional policy, not member coverage. No TypeSpec rule change is required to explain the gap.

<a id="example-15"></a>

### source-only-operation-not-in-selected-version

**Project/API version:** `specification/batch/resource-manager/Microsoft.Batch/Batch` / `2025-06-01`. **Source:** [Microsoft.Batch.Certificates.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/batch/resource-manager/Microsoft.Batch/Batch/Certificate.tsp#L69), lines 67-95.

```typespec
  #deprecated "Removal of feature"
  @removed(Versions.v2025_06_01)
  create is Azure.ResourceManager.Legacy.CreateOrReplaceAsync<
    Certificate,
    Request = CertificateCreateOrUpdateParameters,
    Parameters = {
      /**
       * The entity state (ETag) version of the certificate to update. A value of "*" can be used to apply the operation only if the certificate already exists. If omitted, this operation will always be applied.
       */
      #suppress "@azure-tools/typespec-azure-core/casing-style" "Legacy casing"
      @header("If-Match")
      `If-Match`?: string;

      /**
       * Set to '*' to allow a new certificate to be created, but to prevent updating an existing certificate. Other values will be ignored.
       */
      #suppress "@azure-tools/typespec-azure-core/casing-style" "Legacy casing"
      @header("If-None-Match")
      `If-None-Match`?: string;
    },
    Response = ArmResourceUpdatedResponse<Certificate> & {
      /**
       * The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Match or If-None-Match headers.
       */
      @header("ETag")
      etag?: string;
    },
    Error = CloudError
  >;
```

```json
{
  "selectedApiVersion": "2025-06-01",
  "operationAbsentFromSelectedSwagger": true
}
```

**Observed comparison / gap analysis and decision:** Batch Certificate is removed in the selected version and absent from Swagger. TypeSpec source compilation still reports requestMismatch. No emitted schema exists to compare; align projection rather than change the rule.

<a id="example-16"></a>

### additional-request-check-outside-swagger-200-201-selector

**Project/API version:** `specification/postgresql/DBforPostgreSQL.Management` / `2026-07-01-preview`. **Source:** [Microsoft.DBforPostgreSQL.DbAgents.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/postgresql/DBforPostgreSQL.Management/routes.tsp#L184), lines 182-188.

```typespec
  @Azure.Core.useFinalStateVia("azure-async-operation")
  @put
  createOrUpdate is Legacy.CreateOrReplaceAsync<
    DbAgent,
    Request = DbAgentForUpdate,
    Response = DbAgentAcceptedResponse
  >;
```

```json
{
  "put": {
    "operationId": "DBAgent_CreateOrUpdate",
    "responses": {
      "202": {
        "schema": {
          "$ref": "#/definitions/DbAgent"
        }
      }
    },
    "parameters": [
      {
        "in": "body",
        "schema": {
          "$ref": "#/definitions/DbAgentForUpdate"
        }
      }
    ]
  }
}
```

**Observed comparison / gap analysis and decision:** DbAgent has only a 202 success response. The original registration selects existing 200/201 responses, so it never invokes the request-comparison function here. TypeSpec requestMismatch is additional selector coverage; no rule change is required merely to explain it.

<a id="example-17"></a>

### Collection PUT resource versus GET list wrapper

**Project/API version:** `specification/sql/resource-manager/Microsoft.Sql/SQL` / `2026-08-01-preview`. **Source:** [Microsoft.Sql.Servers.replace](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/sql/resource-manager/Microsoft.Sql/SQL/Server.tsp#L161), lines 160-165.

```typespec
  @Azure.ResourceManager.Legacy.feature(Features.FirewallRules)
  replace is ArmResourceActionSync<
    Server,
    FirewallRuleList,
    ArmResponse<FirewallRule> | AcceptedResponse
  >;
```

```json
{
  "put": {
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/FirewallRule"
        }
      },
      "202": {}
    }
  },
  "get": {
    "responses": {
      "200": {
        "schema": {
          "$ref": "#/definitions/FirewallRuleListResult"
        }
      }
    }
  }
}
```

**Observed comparison / gap analysis and decision:** The collection PUT returns FirewallRule, while GET returns FirewallRuleListResult whose value array contains that exact same emitted FirewallRule definition. Different wrapper roles do not demonstrate different resource item models. Recommend not porting raw reference-name equality here; this is a reasoned policy recommendation, not approved retirement or migration credit.

<a id="example-18"></a>

### Missing custom create/update registration

**Project/API version:** `specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB` / `2026-04-01-preview`. **Source:** https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/DatabaseAccountGetResults.tsp#L54, lines 54-64.

```typespec
  /**
   * Creates or updates an Azure Cosmos DB database account. The "Update" method is preferred when performing updates on an account.
   */
  @put
  createOrUpdate is Azure.ResourceManager.Foundations.ArmCreateOperation<
    ResourceInstanceParameters<DatabaseAccountGetResults>,
    DatabaseAccountCreateUpdateParameters,
    Response = ArmResponse<DatabaseAccountGetResults> &
      ArmLroLocationHeader<FinalResult = DatabaseAccountGetResults>,
    ErrorResponse = Azure.ResourceManager.CommonTypes.ErrorResponse
  >;
```

```json
{
  "put": {
    "operationId": "DatabaseAccounts_CreateOrUpdate",
    "request": {
      "$ref": "#/definitions/DatabaseAccountCreateUpdateParameters"
    },
    "responses": {
      "200": {
        "$ref": "#/definitions/DatabaseAccountGetResults"
      }
    }
  }
}
```

**Observed comparison / gap analysis and decision:** The low-level ArmCreateOperation has the canonical response but no armResourceCreateOrUpdate association. The frozen request/response comparison has no corresponding request warning. Draft #47952 adds exactly that decorator (also NotebookWorkspaces and ActionResponses); registry probes change while saved OpenAPI stays byte-identical. Those authored fixes are separate from, and receive no credit in, this frozen assessment. Public TCGC compatibility is checked, but full/specialized SDK neutrality is not proven.

<a id="example-19"></a>

### Discriminated response ancestry is not request acceptance

**Project/API version:** `specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights` / `2025-10-01-preview`. **Source:** https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/ThreatIntelligenceInformation.tsp#L16, lines 16-62.

```typespec
 */
#suppress "@azure-tools/typespec-azure-core/no-legacy-usage" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
@discriminator("kind")
@parentResource(ThreatIntelligenceMain)
model ThreatIntelligenceInformation
  is Azure.ResourceManager.Legacy.DiscriminatedProxyResource<ThreatIntelligenceResourceInnerKind> {
  ...ResourceNameParameter<
    Resource = ThreatIntelligenceInformation,
    KeyName = "name",
    SegmentName = "indicators",
    NamePattern = ""
  >;

  /**
   * Etag of the azure resource
   */
  #suppress "@azure-tools/typespec-azure-resource-manager/arm-resource-invalid-envelope-property" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  etag?: string;
}

@armResourceOperations(#{ omitTags: true })
interface ThreatIntelligenceInformationOperations {
  /**
   * View a threat intelligence indicator by name.
   */
  @tag("ThreatIntelligence")
  get is Extension.Read<
    OperationalInsights,
    ThreatIntelligenceInformation,
    Error = CloudError,
    OverrideResourceName = "SecurityInsightsThreatIntelligenceIndicator"
  >;

  /**
   * Update a threat Intelligence indicator.
   */
  @tag("ThreatIntelligence")
  create is Extension.CreateOrReplaceSync<
    OperationalInsights,
    ThreatIntelligenceIndicatorModel,
    Response =
      | ArmResourceUpdatedResponse<ThreatIntelligenceInformation>
      | ArmResourceCreatedSyncResponse<ThreatIntelligenceInformation>,
    Error = CloudError,
    OverrideResourceName = "SecurityInsightsThreatIntelligenceIndicator"
  >;
```

```json
{
  "put": {
    "operationId": "ThreatIntelligenceIndicator_Create",
    "request": {
      "$ref": "#/definitions/ThreatIntelligenceIndicatorModel"
    },
    "responses": {
      "200": {
        "$ref": "#/definitions/ThreatIntelligenceInformation"
      },
      "201": {
        "$ref": "#/definitions/ThreatIntelligenceInformation"
      }
    }
  }
}
```

**Observed comparison / gap analysis and decision:** The kind-discriminated ThreatIntelligenceInformation base is the response; the request ThreatIntelligenceIndicatorModel extends that base (models.tsp:7677 at the same frozen revision). There is no eligible create/update association in the frozen registry. The response rule supports discriminated ancestry, but request identity is strict; no request warning here does not prove a registered derived request would be accepted. Preserve the hierarchy and establish owner-approved canonical registration instead of rewriting DTOs for equality.

<a id="example-20"></a>

### Borrowed parent read template does not cover SyncJob equality

**Project/API version:** `specification/automation/resource-manager/Microsoft.Automation/Automation` / `2024-10-23`. **Source:** https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/SourceControl.tsp#L99, lines 99-130.

```typespec
   * Creates the sync job for a source control.
   */
  #suppress "@azure-tools/typespec-azure-core/no-openapi" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  @tag("SourceControlSyncJob")
  @OpenAPI.externalDocs("http://aka.ms/azureautomationsdk/sourcecontrolsyncjoboperations")
  @put
  create is ArmResourceRead<
    SourceControl,
    BaseParameters = Azure.ResourceManager.Foundations.DefaultBaseParameters<SourceControl>,
    Response = ArmResourceCreatedSyncResponse<SourceControlSyncJob>,
    Parameters = SourceControlSyncJobIdParameter & {
      /**
       * The parameters supplied to the create source control sync job operation.
       */
      @body
      parameters: SourceControlSyncJobCreateParameters;
    }
  >;

  /**
   * Retrieve the source control sync job identified by job id.
   */
  #suppress "@azure-tools/typespec-azure-core/no-openapi" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  @tag("SourceControlSyncJob")
  @OpenAPI.externalDocs("http://aka.ms/azureautomationsdk/sourcecontrolsyncjoboperations")
  @get
  sourceControlSyncJobGet is ArmResourceRead<
    SourceControl,
    BaseParameters = Azure.ResourceManager.Foundations.DefaultBaseParameters<SourceControl>,
    Response = ArmResponse<SourceControlSyncJobById>,
    Parameters = SourceControlSyncJobIdParameter
  >;
```

```json
{
  "put": {
    "operationId": "SourceControlSyncJob_Create",
    "request": {
      "$ref": "#/definitions/SourceControlSyncJobCreateParameters"
    },
    "responses": {
      "201": {
        "$ref": "#/definitions/SourceControlSyncJob"
      }
    }
  }
}
```

**Observed comparison / gap analysis and decision:** Both SyncJob methods borrow ArmResourceRead<SourceControl>, and PUT overrides its verb and request body. The complete registered-alias graph now exposes that parent read association: it does not establish create/update request checking for SyncJob. RPC008 compares each result with SourceControl, not PUT's SourceControlSyncJob with GET's SourceControlSyncJobById, so neither original comparison receives credit from that warning. The separate marker check is credited independently. Require a wire/client-compatible operation/resource modeling decision; do not confuse this wrong-parent warning with a fix for the genuine SyncJob PUT/GET shape difference.

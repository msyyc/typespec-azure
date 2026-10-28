# DeleteResponseBodyEmpty migration

## 1. Conclusion and scope

The TypeSpec rule `@azure-tools/typespec-azure-resource-manager/no-response-body`
migrates Swagger linter rule
[`DeleteResponseBodyEmpty`](https://github.com/Azure/azure-openapi-validator/blob/18a7944e7fc3155e8ef1498665465ed5f455f54a/docs/delete-response-body-empty.md).
The assessed DELETE `200`/`204` response-body semantics match. Every observed
count difference is explained by authored suppressions, client-only source
operations, or the TypeSpec rule's existing `202` check; no further production
rule change is indicated. **Native draft PR
[#5866](https://github.com/Azure/typespec-azure/pull/5866) and portable evidence
are published. Both independent review checkpoints passed at the exact tested
native source; all required CI checks passed.**

## 2. Actual coverage

All 487 selected projects were assessed, with no unassessed projects.
Reported diagnostics are individual findings across that population, not project counts.

| Count                                                     | Swagger linter | TypeSpec linter |
| --------------------------------------------------------- | -------------: | --------------: |
| Reported diagnostics                                      |             45 |              33 |
| After analysis: DELETE `200`/`204` source findings        |             45 |              32 |
| After analysis: exact common HTTP operation/status groups |             30 |              30 |

The last row is the intersection established by exact project, HTTP method,
case-sensitive path, and response status, retaining multiplicities. It is not
a replacement for the raw totals or a claim that suppressed findings vanished.
The remaining 15 Swagger findings are explicitly suppressed in TypeSpec;
two additional TypeSpec DELETE findings belong to client-only operations.
The other TypeSpec finding checks a `202` POST response.
See the [complete investigation](evidence-details.md) and
[machine-readable reconciliation](runs/native-full487-run1/reconciliation.json).

## 3. Function-level coverage

| Behavior                                                         | Result                                                |
| ---------------------------------------------------------------- | ----------------------------------------------------- |
| Supported synchronous DELETE template override with a `200` body | Covered                                               |
| Explicit `@body`, `@bodyRoot`, and implicit response payload     | Covered                                               |
| Body-bearing `204`, including after a bodyless `200`             | Covered                                               |
| Two violating statuses on one operation                          | Two operation-targeted diagnostics                    |
| Standard DELETE defaults and headers-only responses              | Compliant                                             |
| Authored source suppression                                      | Retained                                              |
| Existing `202`, non-DELETE `200`, and HEAD behavior              | Preserved, except correction of the early-return hole |
| Exact emitted Swagger/source count equality                      | Not expected; all differences investigated            |

## 4. Why diagnostic counts differ

| Difference group                                                                 | Swagger linter | TypeSpec linter | Explanation                                              |
| -------------------------------------------------------------------------------- | -------------: | --------------: | -------------------------------------------------------- |
| [Device Provisioning Services](evidence-details.md#device-provisioning-services) |              1 |               0 | Existing operation-level suppression                     |
| [IoT Hub](evidence-details.md#iot-hub)                                           |              2 |               0 | Existing suppressions on both DELETE operations          |
| [Security Insights](evidence-details.md#security-insights)                       |              2 |               0 | One suppression covers DELETE `200` and `204`            |
| [App Service](evidence-details.md#app-service)                                   |             10 |               0 | Five suppressed operations, two statuses each            |
| [AKS](evidence-details.md#aks)                                                   |              0 |               1 | Existing POST `202` policy, outside this Swagger mapping |
| [Policy](evidence-details.md#policy)                                             |              1 |               2 | One extra source-only client DELETE operation            |
| [Search](evidence-details.md#search)                                             |              1 |               2 | One extra source-only client DELETE customization        |

Raw directional differences are 15 Swagger-higher and three TypeSpec-higher
findings, not merely a net difference of 12. The complete comparison retains
all 487 projects and all 45/33 reported findings.

## NOTES

- Specs commit: `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`.
- Candidate snapshot: `8da43e29ab015a9cee850006a791e9a7483eebb1`,
  tree `8072a4306a1402df20a2b5c7e0139dddfcf44069`.
- Published native candidate:
  [`8ccd925220ca8a92cdbc4c7ec06bb656c4f831ab`](https://github.com/Azure/typespec-azure/commit/8ccd925220ca8a92cdbc4c7ec06bb656c4f831ab).
  Its Git tree exactly equals the clean tested snapshot tree.
- Core commit: `ea154bb3228988d8d6f179dabd8a51d36bcfccc4`.
- Shared baseline: `swagger-arm-20261026-2cd3c5dd`; metadata commit
  `317e703b3e380d3b64e0dacb3a2c6fc0651de253`.
  The metadata commit is not the tested specs commit.
- Comparison uses the explicit `frozen-reference` policy: current-main
  compiler/libraries are assumed backward-compatible with the frozen source.
  No Swagger was regenerated. The baseline was integrity-verified separately.
- Swagger policy is production ARM, resolved DELETE `200`/`204` response schemas.
  The TypeSpec rule remains a warning with its existing ARM ruleset enablement;
  Swagger reports an error. The TypeSpec rule reports once per violating status
  on the authored operation and has broader existing success-response checks.
- Source-mode native diagnostics include client customizations and retain source
  suppressions; Swagger is the saved latest emitted service version.
  No API-version mismatch was needed to explain the observed differences.
- Raw affected-project sets are Swagger 21, TypeSpec 18, overlap 17.
  Four Swagger-only projects and one TypeSpec-only project are explained above.
  Raw source-location and file-independent Swagger-path totals are 33 and 45,
  respectively; they are not interchangeable identity domains.
- Validation receipts record 22 focused rule cases, 657 ARM package tests,
  eight ruleset tests, four actual documentation snippet compilations, and
  11 passing injected rule/attribution controls. A supplemental 43-case harness
  run passed 37 cases and failed six unrelated resource-group-rule cases because
  that other rule is absent from the pinned candidate. It is not a full passing suite.
- All 33 saved native findings were deterministically attributed using exact
  source keys and native HTTP metadata. A focused metadata-only investigation
  covered the 18 diagnostic-bearing and four Swagger-only projects; it did not
  rerun the full lint corpus or emit Swagger.
- [Portable provenance](runs/native-full487-run1/provenance.json),
  [complete saved observations](runs/native-full487-run1/observations.json),
  and [recovery configuration](runs/native-full487-run1/reproduction.json)
  distinguish saved-observation reanalysis from a new native execution.
  Actual loaded package hashes are retained; this is not a sealed transitive runtime.
- The missing duplicate Azure Examples package-root schema is a user-waived
  packaging limitation. Its actual imported `dist/schema/dist/ExamplesYaml.json`
  exists. A preexisting unused compiler `.d.ts` export typo is also retained;
  all 17 selected packages have their actual runtime/TypeSpec entrypoints.
  Failed broad package audits are not relabeled as passing.
- [Fresh-checkout recovery](runs/native-full487-run1/recovery-receipt.json)
  verified every published payload hash, reproduced all 487 projects exactly,
  downloaded and verified all 17 candidate artifacts and the frozen Swagger
  archive, and verified the retained source ref and remote native/core identities.
  This did not repeat native execution or reconstruct a sealed transitive runtime.
- [Review checkpoint receipts](runs/native-full487-run1/review-checkpoints.json)
  record separate development and release-readiness local reviews plus fresh
  Balanced GitHub reviews
  [A](https://github.com/Azure/typespec-azure/pull/5866#pullrequestreview-5685111899)
  and
  [B](https://github.com/Azure/typespec-azure/pull/5866#pullrequestreview-5685417626).
  Each GitHub checkpoint completed in one round with zero review-specific
  comments and zero unresolved threads, independently verified by the
  coordinator at the unchanged native commit. No review fix or semantic repair
  was needed. All required CI checks, including the final Gate, passed.
- [Exact-source validation](runs/native-full487-run1/validation.json) retains
  the seven source hashes, test cases, actual documentation examples, command
  outcomes, original receipt hashes, and disclosed supplemental failures.
- The original implementation agent encountered a model-service
  organization-access `401`; the coordinator resumed the verified
  explicit-target binding without retrying that worker or resetting any
  recovery allowance.

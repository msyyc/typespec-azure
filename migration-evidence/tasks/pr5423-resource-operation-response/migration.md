# ARM resource operation response migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response`
consolidates [`PutRequestResponseSchemeArm`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-request-response-scheme-arm.md),
[`ConsistentResponseSchemaForPut`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-response-schema-for-put.md),
[`XmsResourceInPutResponse`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/xms-resource-in-put-response.md)
and [`PutGetPatchResponseSchema`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-get-patch-response-schema.md).
**Partially effective, not functionally equivalent.** The recommended immediate change is small:
the existing registered-resource operation Set exposes **57 further canonical request comparisons**
without restoring a broad PUT listener. Conversely, do not copy Swagger false positives or add
duplicate warnings for existing explicitly suppressed native policies. Quota and all 16 empty-200
route cases already trigger the appropriate existing owner predicate before suppression.
The independent resource-marker policy and remaining legacy contracts still need explicit decisions.
See the [gap decisions and implementation tradeoffs](gap-analysis.md); no production change or
prospective coverage gain is claimed here.

## 2. Actual coverage

All 487 frozen projects succeeded, with zero failed or unassessed projects.
Reported diagnostics are individual findings, not project counts.
The common grouped unit below is an exact `(project sourcePath, HTTP route)` referenced by a finding:
one route may have several member checks or several participating methods.

| Count                                                    | Swagger linter | TypeSpec linter |
| -------------------------------------------------------- | -------------- | --------------- |
| Reported diagnostics                                     | 433            | 104             |
| HTTP routes referenced by findings (project/exact route) | 256            | 104             |

These are route counts, not equivalent-defect counts. Exact tracing separates matching request
comparisons from absent checks, unrelated warnings on the same operation, upstream false positives,
repeated observations and source-version differences.
See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) and the
[complete operation/model correspondence](instance-correspondence.md).

## 3. Function-level coverage

| Behavior                                                                     | Result                                                                                                                                |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Registered lifecycle PUT request uses a different effective resource model   | Partial: 87 corroborated instances; no claim that model identity universally equals emitted-schema equality.                          |
| PUT stored under `lists`, or absent from the retained resource operation map | Missing request comparisons; registration alone does not establish coverage.                                                          |
| Missing/void PUT request                                                     | Additional TypeSpec policy, not a migrated finding from these four members.                                                           |
| Arbitrary 200/201 response equality, including a plain nonresource response  | Not in this ARM rule; Quota's genuine difference already triggers Azure Core response-schema-problem before its authored suppression. |
| `x-ms-azure-resource` in the selected PUT response hierarchy                 | Missing as an independent check.                                                                                                      |
| PUT/GET/PATCH selected response `$ref` comparison                            | Not equivalent: canonical registered-resource traversal does not check the same status/body/reference predicate.                      |
| Standard templates and resource aliases; suppression handling                | Existing compliant/violation controls retained; no linter disabled or new suppression added.                                          |
| Staging object-identity bug                                                  | Correctly not reproduced; identical references are not genuine schema mismatches.                                                     |

## 4. Why diagnostic counts differ

**Unpaired does not mean "add a new warning."** Every check now has an evidence-backed
[disposition](gap-assessment.json), including whether source changes are worthwhile:

| Assessed cause                                                            | Member checks | Recommendation / coverage-versus-cost                                                                                                                                  |
| ------------------------------------------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Existing corresponding request comparison                                 | 87            | Keep existing behavior.                                                                                                                                                |
| Registered PUTs recoverable via the existing operation Set                | 57            | **P1: small native traversal fix**; 38 legacy/list + 19 absent-map cases, not a global PUT scan.                                                                       |
| Upstream identity bug                                                     | 15            | Confirmed false positives; do not port.                                                                                                                                |
| Correctly bodyless 202/204 compared to a resource schema                  | 15            | Schema-comparison overreach; recommend not porting; status validity is separate.                                                                                       |
| Entity/array/list-envelope role differences                               | 4             | Same item definition verified; recommend not porting wrapper-reference equality.                                                                                       |
| Empty 200 responses                                                       | 25            | 16 route contexts; existing no-response-body predicate diagnoses all 16 before explicit authored suppressions. Review those exceptions/specs, not duplicate ARM logic. |
| Quota 200/201 resource versus submission envelope                         | 1             | Existing Azure Core predicate diagnoses it before explicit suppression; review the legacy exception, not add a duplicate rule.                                         |
| Missing independent response-resource policy                              | 57            | Medium-complexity focused rule/design; clarify custom/action scope. Not 57 automatically proven resource defects or future gains.                                      |
| Custom registration, legacy DTOs, commands/bulk and parent/child modeling | 15            | Targeted spec/template/contract review; a general structural matcher adds complexity and noise.                                                                        |
| Genuine SyncJob PUT/GET shape difference                                  | 1             | Spec-owner follow-up; defer a broad recursive matcher for one observed route.                                                                                          |
| **Total**                                                                 | **277**       | Counts remain member checks, not unique defects or post-fix diagnostics.                                                                                               |

The former blanket "rule update required" conclusions are withdrawn. The 19 no-content/collection
differences are **recommended**, not approved policy retirements. The 57 recovery candidates were
verified on 14 projects, and the 17 existing-owner predicates on eight projects; all saved diagnostics
reproduced unchanged. The configured owner counts remain zero because the exact operations explicitly
suppress those owners. This is predicate evidence, **not new observed migration credit**.
The [detailed analysis](gap-analysis.md) explains the five Set-recovery exceptions, exact source
owners, suppressions, uncertain contracts, alternatives rejected and focused implementation/tests.

The 433 observations resolve to **277 distinct member checks**: identity retains member, project,
resolved Swagger document, exact route and request/response schema context. A path-level comparison
remains one check over its method bundle; different members at the same route are not duplicates.

| Swagger member                                                                        | Raw findings | Distinct checks      | TypeSpec findings mapped to the same comparison | Unpaired checks                                 |
| ------------------------------------------------------------------------------------- | ------------ | -------------------- | ----------------------------------------------- | ----------------------------------------------- |
| [PutRequestResponseSchemeArm](members/PutRequestResponseSchemeArm/migration.md)       | 212          | 168 PUTs             | 87                                              | 81                                              |
| [ConsistentResponseSchemaForPut](members/ConsistentResponseSchemaForPut/migration.md) | 16           | 16 PUTs              | 0                                               | 1 genuine mismatch; 15 upstream false positives |
| [XmsResourceInPutResponse](members/XmsResourceInPutResponse/migration.md)             | 155          | 57 PUTs              | 0                                               | 57                                              |
| [PutGetPatchResponseSchema](members/PutGetPatchResponseSchema/migration.md)           | 50           | 36 route comparisons | 0                                               | 36                                              |

- [Request-check differences](instance-correspondence.md#request-comparison-differences):
  39 PUTs are stored in `lists`; 23 have registered responses but no retained operation association;
  12 have neither an association nor a registered response; five have warnings comparing different
  models/status bodies; two have the canonical request but an empty selected 200 response.
  The other 87 have the same PUT, effective request and canonical response-resource comparison.
- [Response-check differences](instance-correspondence.md#response-comparison-differences):
  all 57 extension checks are absent; Quota's distinct 200/201 bodies are not compared.
  Of 36 cross-operation checks, 33 compare a missing selected `$ref` against another response
  and three compare distinct references. A request warning on the route does not cover either check.
  Semantic assessment partitions those 36 into **15 no-content comparisons + four collection
  comparisons + 16 existing-body-owner cases + one genuine shape difference**; the old 33/3
  reference distinction is not an implementation priority.
- [All TypeSpec findings](instance-correspondence.md#typespec-finding-accounting):
  96 request mismatches split into 87 mapped, seven coincident but different comparisons,
  one removed Batch source operation and one 202-only PUT outside the Swagger selector.
  Eight missing-request warnings are additional policy. There are **zero response-family findings**.
  All 104 are accounted for; the 17 not credited above are not silently discarded.
- [Repeated inputs and attribution](instance-correspondence.md#identity-and-attribution):
  exact document/route/schema resolution groups Network's 170 observations into 14 checks.
  This is a count-only reduction, not missing coverage. Original fallback attributions remain immutable.
- [Per-project and per-instance inventory](instance-correspondence.md#differing-projects)
  preserves every difference and both directions, including equal raw totals with different semantics.
  Project sets remain 57 Swagger-affected / 34 TypeSpec-affected, with 32 in both, 25 Swagger-only
  and two TypeSpec-only. Raw directional excesses remain 333 / 4 and must not cancel.

## NOTES

All 433 Swagger findings have one exact emitted operation/route context.
The 59 affected projects were recompiled only for metadata: every saved diagnostic was reproduced
unchanged, with no metadata failures. All 328 method/route bindings are unique and exact in both
source and selected-version HTTP graphs; no parameter normalization or fuzzy matching was needed.
The 87 credited cases also have unchanged request/response metadata in the selected version.
This closes the earlier reporting-attribution gap; it does not make the migration complete.

The TypeSpec rule is a warning, enabled in `all`; the four ARM Swagger registrations are errors,
with `ConsistentResponseSchemaForPut` staging-only. Configured source compilation retains authored
suppressions; Swagger uses frozen latest-version output without production readme suppressions.
Source and emitted-version policies remain distinct, explicitly accounted for rather than normalized away.
At the common project/route unit, Swagger-higher excess is 156 routes and TypeSpec-higher excess
is four (absolute difference 160); the net difference must not cancel opposite project gaps.

Candidate `2d82a09b6ce2eda8114e54bfd4df6358ec956340`; frozen specs
`2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`. No production linter changes were made for this assessment.
The existing 487-project corpus and immutable Swagger baseline were reused; this was not another
full corpus run or Swagger regeneration.

At publication, PR head `a4b87e3c8155f330b715c738c09e051087893fd7` had merged main.
The [complete head comparison](receipts/publication-head-comparison.json) changes a separate
LRO polling rule and its wiring/tests/docs, not the assessed response rule, supporting registration,
existing owner predicates, emitter or dependencies. The semantic analysis therefore still applies;
the corpus remains explicitly pinned to `2d82a09`, **not relabeled as an execution of the new head**.

[Decision evidence and bounded experiments](gap-analysis.md),
[Inputs, controls, code-backed examples and recovery](evidence-details.md),
[exact instance inputs/results](instance-mapping.json),
[metadata execution receipt](receipts/instance-inspection-20261104.json),
[project grouping](project-differences.md#assessed-project-grouping) and
[reproducible summary](summary.json) retain the evidence.
Run `python analyze-instances.py --root .` and `python reanalyze.py --verify-inventory`
to verify saved-evidence reconstruction; neither command reruns a linter.
Independent migration review and complete runtime regeneration remain outside this evidence task;
the report does not claim migration acceptance.

# ARM PATCH property migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/no-unsafe-patch-body-properties`
consolidates the Swagger linters
[PatchBodyParametersSchema](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-body-parameters-schema.md),
[ConsistentPatchProperties](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-patch-properties.md), and
[UnSupportedPatchProperties](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/un-supported-patch-properties.md)
into native ARM PATCH validation. Coverage is not fully equivalent to the Swagger checks.

## 2. Actual coverage

Fresh TypeSpec diagnostics were recollected on November 2, 2026 at
`8a92389c9f9488035ab65c6ed3e08a49cc822f25` for **487 selected,
487 assessable projects; zero compilation/worker failures or exclusions**.
The verified shared baseline supplies 649 saved Swagger files and their findings;
Swagger was not regenerated. Reported diagnostics are individual findings,
not project counts.

| Count                                            | Swagger linter | TypeSpec linter |
| ------------------------------------------------ | -------------: | --------------: |
| Fresh comparison, reported diagnostics           |            975 |           1,337 |
| Affected PATCH routes (grouped by project/route) |            304 |             321 |

The gap reflects differences in effective PATCH input, authored versus emitted schemas, additional default/array checks, reporting granularity, and source/version scope. Grouping findings by route does not eliminate these differences or establish equivalent coverage. See [detailed analysis](detailed-analysis.md) for the breakdown and remaining parity boundaries.

The Swagger total is **715 + 150 + 110** for the three original rules.
The combined TypeSpec total is counted once. The common unit is **one
`(project, exact case-sensitive PATCH route)`**, preserving parameter names:
277 shared, 27 Swagger-only and 44 TypeSpec-only. This is a coarse affected-route
count, **not distinct defects, version-aligned operations or required fixes**.
The earlier direct observation at `94b316787` attributes TypeSpec findings to
required/default/visibility (914), layout (361) and immutable (62) implementation
families; it does not pair those findings with individual Swagger defects.
The new run reproduced every prior raw and aligned diagnostic exactly,
including project, rule, message, authored location and duplicate multiplicity:
**zero changed projects, zero added or removed findings**. Family and route
attribution below is retained analysis of those reproduced observations,
not a claim that callback instrumentation was rerun on the new implementation.
[Exact comparison](runs/20261102-8a92389c9/diagnostic-differences.json).
[Detailed accounting and limitations](detailed-analysis.md#counting-levels).

## 3. Function-level coverage

| Behavior and compliant control                                                                                      | Result                                                                                             |
| ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Required PATCH input and defaults; optional, default-free input accepted                                            | Covered; all defaults include falsy values missed by Swagger's truthiness check                    |
| Ordinary Read/Create-only input excluded; explicitly exposed non-Update input checked                               | Covered native policy; intentionally differs from emitted mutability/schema sharing                |
| Immutable root `id`, `name`, `type`, `location` and `properties.provisioningState`; unrelated nested names accepted | Covered; Update visibility never makes those paths mutable                                         |
| Partial encoded JSON layout, including inherited overrides, nullable models and missing nested leaves               | Covered; not type assignability and not emitted `allOf`/synthetic-discriminator equivalence        |
| Explicit resource association; PATCH/GET 200/201 precedence; safety without a comparison resource                   | Covered; standard ARM PATCH templates use explicit association                                     |
| Top-level encoded case-insensitive `identity` safety exemption                                                      | Covered; layout comparison is deliberately not exempt                                              |
| Array replacement elements                                                                                          | Extended: required descendants allowed; defaults, visibility and supported item layout checked     |
| Open resource records                                                                                               | Covered named keys and named-member layouts; record indexer values not recursively expanded        |
| Request multi-model unions, tuples and multipart/native File transport                                              | Outside traversal; no exhaustive Swagger-parity claim                                              |
| Unsupported resource unions                                                                                         | Descendant layout skipped; independent safety and supported siblings retained                      |
| Ambiguous preferred response bodies                                                                                 | Layout declined; independent safety retained; no lower-priority response/GET substitution          |
| GET fallback without a containing service                                                                           | No namespace-local discovery; standalone safety and ordinary same-service GET remain covered       |
| Native and derived File models                                                                                      | Whole transport models excluded, including authored overrides                                      |
| Resource member visibility and duplicate encoded names                                                              | Native all-visibility layout; conflicting encoded members decline descendant layout conservatively |
| Associated-resource `name` filtering and emitted optional/default-free PATCH fields                                 | Observed 12 and 9 additional findings; exact emitted-layout parity is not established              |

See [behavior evidence and member notes](evidence-details.md#member-evidence).
Compiler-invalid discriminator/File constructions are not counted as linter
coverage. SDK-scope fixture behavior is source-side evidence, not proof that the
official package tests a client-generator integration.

## 4. Why diagnostic counts differ

The selected Swagger functions return **1,057 checks**, but Spectral reports
**975** after collapsing 82 occurrences (75 required, seven default) by its
reported-path/message fingerprint. Distinct full property paths are retained;
975 is not silently replaced or individually paired with arbitrarily chosen
callbacks. [Captured reporting control](detailed-analysis.md#reporting-stage-collapse).

Before that reporting collapse, **834 occurrences share a project/route/check/
property-path-text key**. This is an accounting intersection, not proof of
identical underlying defects. The remaining **223 Swagger / 503 TypeSpec**
observations are exhaustively accounted for below:

| Differing check/path group                           | Swagger / TypeSpec | Cause and disposition                                                                                                                                                                                                                                                                 |
| ---------------------------------------------------- | -----------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Effective PATCH input exclusions                     |            165 / 0 | Read/Create-only fields or excluded ancestors; no repair justified for excluding them. [Evidence](detailed-analysis.md#effective-input-and-synthetic-fields)                                                                                                                          |
| Emitted-only discriminator; optional candidate field |       5 / 0; 1 / 0 | Five synthetic discriminators and CommunityTraining's optional `sku.name`; not missing authored required checks. [Evidence](detailed-analysis.md#effective-input-and-synthetic-fields)                                                                                                |
| Parent/leaf layout regions                           |           52 / 175 | Swagger stops at absent parent branches; TypeSpec reports leaf paths. Related prefixes are not normalized into identical defects. [Evidence](detailed-analysis.md#parent-and-leaf-accounting)                                                                                         |
| Falsy defaults and array traversal                   |            0 / 207 | 128 falsy defaults, 65 other array defaults and 14 array-layout findings, with overlap removed only from this category accounting. [Evidence](detailed-analysis.md#defaults-and-arrays)                                                                                               |
| Recursive Informatica request                        |             0 / 24 | Captured unresolved recursive `$ref` reaches `getProperties` with no children; an analysis-only cycle-breaking control exposes two missing branches. [Evidence](detailed-analysis.md#recursive-reference-boundary)                                                                    |
| Source/version/client-only and operation populations |             0 / 76 | Removed declarations, 34 Search client-only findings, three additional same-route source-operation occurrences and seven findings without an identical saved PATCH route. [Evidence](detailed-analysis.md#source-and-operation-populations)                                           |
| Resource-name and emitted PATCH representation       |             0 / 21 | Twelve associated-resource `name` payload-filter findings; nine NetApp required/default findings absent from its optional/default-free saved request. Count mechanisms are established; parity policy remains open. [Evidence](detailed-analysis.md#representation-policy-boundaries) |

All **83 unequal-count projects** and every exact target are retained in the
[fresh difference inventory](fresh-differences.md). The **102 Swagger excess
findings** and **464 TypeSpec excess findings** must not cancel into the net
**+362**; absolute per-project difference is **566**. There are also 404 equal-count
projects, whose equal totals do not prove correspondence. Four equal-count
projects have different check/path observations. The new
[87-project semantic difference ledger](detailed-differences.md) includes those
four as well as all 83 raw-count differences. Count mechanisms are now explicit;
this does not certify same-version semantic equivalence or approve the
representation-policy differences. No source changes were made to equalize results.

## 5. Review-fix validation and scope changes

The four admitted review requests were implemented together in
[`8a92389c9`](https://github.com/msyyc/typespec-azure/commit/8a92389c9f9488035ab65c6ed3e08a49cc822f25).
Response ambiguity now uses one selected body and one traversal; namespace-local
GET discovery and bespoke derived-File override handling were removed; resource
comparison uses native all-visibility metadata instead of a Read-or-writable
projection. Effective PATCH input filtering, explicit-body/item metadata,
record/indexer handling and template-instance exclusions remain.

These are intentional supported-scope changes, **not globally function-equivalent
refactoring**: synthetic ambiguous layouts, no-service GET discovery,
derived-File overrides and Query-only comparison cases can produce fewer
warnings. A small encoded-name ambiguity guard prevents a demonstrated false
`missing(wire.good)` when a Query member shadows an inherited Read member;
independent required checks and unrelated missing siblings remain reported.
The canonical suite also verifies that an ambiguous PATCH 200 does not substitute
a usable 201. Existing ordering and safety controls cover the other changes.

One final full-population run after stable production changes passed; no
per-comment corpus runs or Swagger regeneration were performed. The exact
487-project diagnostic multisets are unchanged from October 30, establishing
**no observed corpus regression**, not universal equivalence. There were no
changed corpus cases requiring additional extracted fixtures.
The [validation receipt](runs/20261102-8a92389c9/local-validation.json) maps all
four report IDs to executed canonical cases.

## NOTES

- Assessed PR: [Azure/typespec-azure#5294](https://github.com/Azure/typespec-azure/pull/5294),
  tested source head `8a92389c9f9488035ab65c6ed3e08a49cc822f25`,
  core `cefb035e7721a6fdcb6de605b5f469b93055a880`.
  [Implementation](https://github.com/msyyc/typespec-azure/blob/8a92389c9f9488035ab65c6ed3e08a49cc822f25/packages/typespec-azure-resource-manager/src/rules/no-unsafe-patch-body-properties.ts),
  [tests](https://github.com/msyyc/typespec-azure/blob/8a92389c9f9488035ab65c6ed3e08a49cc822f25/packages/typespec-azure-resource-manager/test/rules/no-unsafe-patch-body-properties.test.ts),
  [public contract](https://github.com/msyyc/typespec-azure/blob/8a92389c9f9488035ab65c6ed3e08a49cc822f25/packages/typespec-azure-resource-manager/src/rules/no-unsafe-patch-body-properties.md).
- Fresh ARM build, root `pnpm format` and `pnpm lint` passed.
  **757 distinct owning ARM tests validated**, including all **112 canonical
  PATCH tests**: 755 initially passed, and both initial timeout cases
  passed a focused retry after concurrent dependency restoration ended.
  **20/20 injected PATCH controls** passed across configured and target-only
  modes. Applicable portable controls: **37 passed**; six unrelated
  `resource-group-path-parameter` fixtures were explicitly excluded up front,
  not counted as passing. The historical October suite had 758/113 tests and
  six explicit generic-control failures; those receipts remain unchanged.
  [Current controls](runs/20261102-8a92389c9/controls.json).
- Frozen specs: `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`.
  Baseline metadata: `317e703b3e380d3b64e0dacb3a2c6fc0651de253`;
  baseline identity `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`.
  Metadata commit and tested specs commit are different.
  [Pinned descriptor](runs/20261030-94b316787/selected-descriptor.json).
- Policy: `scope: source`, no filter/limit, `frozen-reference`, target-only,
  concurrency 2, native budget 7,200 seconds. Native execution took about
  26 minutes; setup, full baseline copying/hash verification and final integrity
  checks were additional. Saved Swagger is a historical reference, not newly
  re-emitted or proven identical under the candidate's changed runtime.
- Project guardrails: Swagger findings in 121 projects, TypeSpec findings in 128,
  overlap 113, Swagger-only 8, TypeSpec-only 15. Raw-count direction:
  Swagger higher in 27 projects, TypeSpec higher in 56. Conservative location
  summaries are 431 Swagger paths and 935 TypeSpec source locations; these are
  different identity domains, not normalized actionable counts.
- November 2 analysis observed all 136 projects with findings on either side:
  all 1,337 TypeSpec findings reproduced with exact source/message multisets;
  selected Spectral replay reproduced all 975 retained Swagger reports by
  project/document/rule/message. Both had zero failures. Source applicability
  inspections covered all 223 unmatched Swagger checks in 48 projects.
  These are bounded semantic investigations of retained inputs, not new Swagger
  generation or a replacement for the October 30 full-population run.
  [Receipts and reproduction](detailed-analysis.md#reproducibility).
- Loaded compiler `1.17.0`, ARM `0.73.0`, AutoRest emitter `0.73.2`,
  Node `26.5.0`, specs pnpm `12.6.0`.
  [Actual loaded package hashes](runs/20261102-8a92389c9/loaded-packages.json)
  matched the packed candidate artifacts in every successful worker.
- Audience: explicitly enabled ARM analysis; the TypeSpec linter is a warning,
  registered but disabled in the shared resource-manager ruleset. It does not
  automatically distinguish ARM from data-plane services in a mixed program.
  Other PATCH rules and their overlapping diagnostics remain unchanged.
- The target-only corpus run did not execute configured/default activation:
  those findings remain null/unassessed for all 487 projects, not zero.
  The ten separately configured PATCH controls verify default disablement.
- Member notes: [required/default/visibility](members/PatchBodyParametersSchema/migration.md),
  [layout](members/ConsistentPatchProperties/migration.md),
  [immutable properties](members/UnSupportedPatchProperties/migration.md).
  [Historical fixtures](fixture-differences.md) and their older 468-project
  corpus remain historical; aggregate changes across different populations
  are not measured regressions.
- [Provenance, durable assets and recovery](fresh-evidence.md).
  Source preservation uses the verified existing specs-fork ref at the exact
  frozen SHA. Reading/recounting saved observations is distinct from rerunning
  native diagnostics. This revision updates only the native PR's implementation
  and evidence; no original lintdiff-source repair, Swagger generation,
  enablement change or thread resolution was performed.

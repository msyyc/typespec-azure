# ARM PATCH property migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/no-unsafe-patch-body-properties`
consolidates the Swagger linters
[PatchBodyParametersSchema](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-body-parameters-schema.md),
[ConsistentPatchProperties](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-patch-properties.md), and
[UnSupportedPatchProperties](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/un-supported-patch-properties.md).
**This is an intentional native semantic consolidation, not full functional
equivalence to Swagger. Current-head corpus coverage remains unassessed.**
Focused tests establish the implemented behaviors, but historical corpus
differences include unresolved attribution and within-project residuals.
This reporting-only update records differences; it does not repair either
implementation or adopt the latest review's proposed simplifications.

## 2. Actual coverage

The available full corpus is historical: 468 attempted projects, 462 successfully
compiled, six failed and excluded from both sides. It evaluated the earlier
consolidated source, not the current PR head. Reported diagnostics are individual
findings, not project counts; member rows must not reuse the combined TypeSpec
total as their own coverage.

| Count                                                          | Swagger linter | TypeSpec linter |
| -------------------------------------------------------------- | -------------: | --------------: |
| Historical corpus reported diagnostics, three members combined |            961 |           1,258 |
| Current PR head, full-corpus reported diagnostics              |     Unassessed |      Unassessed |

No supported common actionable unit has been established for the differing
historical totals; no after-analysis normalized total is asserted.
The [historical member rows and population limits](evidence-details.md#historical-corpus)
are distinct from the **113/113 current-head focused tests**. Those tests are
behavior controls, not a production diagnostic count.

## 3. Function-level coverage

| Behavior and compliant control                                                                                      | Result                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Required PATCH input and defaults; optional, default-free input accepted                                            | Covered; all defaults include falsy values missed by Swagger's truthiness check                |
| Ordinary Read/Create-only input excluded; explicitly exposed non-Update input checked                               | Covered native policy; intentionally differs from emitted mutability/schema sharing            |
| Immutable root `id`, `name`, `type`, `location` and `properties.provisioningState`; unrelated nested names accepted | Covered; Update visibility never makes those paths mutable                                     |
| Partial encoded JSON layout, including inherited overrides, nullable models and missing nested leaves               | Covered; not type assignability and not emitted `allOf`/synthetic-discriminator equivalence    |
| Explicit resource association; PATCH/GET 200/201 precedence; safety without a comparison resource                   | Covered; standard ARM PATCH templates use explicit association                                 |
| Top-level encoded case-insensitive `identity` safety exemption                                                      | Covered; layout comparison is deliberately not exempt                                          |
| Array replacement elements                                                                                          | Extended: required descendants allowed; defaults, visibility and supported item layout checked |
| Open resource records                                                                                               | Covered named keys and named-member layouts; record indexer values not recursively expanded    |
| Request multi-model unions, tuples and multipart/native File transport                                              | Outside traversal; no exhaustive Swagger-parity claim                                          |
| Unsupported resource unions                                                                                         | Descendant layout skipped; independent safety and supported siblings retained                  |
| Ambiguous response candidates, no-service GET fallback, derived File overrides, response visibility                 | Current behavior tested; scope/design remains under review                                     |

See [behavior evidence and member notes](evidence-details.md#member-evidence).
Compiler-invalid discriminator/File constructions are not counted as linter
coverage. SDK-scope fixture behavior is source-side evidence, not proof that the
official package tests a client-generator integration.

## 4. Why diagnostic counts differ

| Differing diagnostic group                                                 | Observed Swagger / TypeSpec findings | Cause and disposition                                                                                                                                                                                                  |
| -------------------------------------------------------------------------- | -----------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Historical layout category                                                 |                            151 / 302 | Authored shape, emission/scope and array differences; Informatica and other within-project residuals remain unresolved. [Evidence](evidence-details.md#layout-and-emission)                                            |
| Historical immutable category                                              |                             107 / 59 | Effective request input versus emitted annotations/reference resolution; no blanket current-head equivalence claim. [Evidence](evidence-details.md#visibility-and-immutable-input)                                     |
| Historical required/default/non-Update categories                          |                            703 / 897 | Falsy defaults, excluded input, discriminator optionality, arrays and distinct checks; ProgrammableConnectivity attribution and residual counts remain unresolved. [Evidence](evidence-details.md#safety-and-counting) |
| Saved array fixture, selected Swagger member versus combined TypeSpec rule |                                0 / 2 | Default `items[].enabled` and missing `items[].extra`; required replacement-item `id` is accepted. [Example](evidence-details.md#array-extension)                                                                      |
| Saved explicitly exposed Create-only immutable fixture                     |                                0 / 2 | TypeSpec diagnoses immutable `location` and missing Update visibility independently. [Example](evidence-details.md#explicit-visibility-override)                                                                       |
| Latest review's proposed simplifications                                   |                   No post-change run | Could remove currently tested diagnostics; changes are not applied, approved retirements or measured corpus regressions. [Analysis](evidence-details.md#latest-review-and-regression-boundary)                         |

The historical net difference is **+297 TypeSpec findings**, not a match after
normalization. Opposing per-project gaps cannot be reconstructed from aggregate
rows and must not cancel. Every unequal saved fixture is listed with its exact
targets in the [fixture difference appendix](fixture-differences.md); equal
counts alone do not prove semantic correspondence.

## NOTES

- Assessed PR: [Azure/typespec-azure#5294](https://github.com/Azure/typespec-azure/pull/5294),
  source head `94b316787e2a19847c26986412ce254ca4da33b4`,
  core `cefb035e7721a6fdcb6de605b5f469b93055a880`.
  [Implementation](https://github.com/msyyc/typespec-azure/blob/94b316787e2a19847c26986412ce254ca4da33b4/packages/typespec-azure-resource-manager/src/rules/no-unsafe-patch-body-properties.ts),
  [tests](https://github.com/msyyc/typespec-azure/blob/94b316787e2a19847c26986412ce254ca4da33b4/packages/typespec-azure-resource-manager/test/rules/no-unsafe-patch-body-properties.test.ts),
  [public contract](https://github.com/msyyc/typespec-azure/blob/94b316787e2a19847c26986412ce254ca4da33b4/packages/typespec-azure-resource-manager/src/rules/no-unsafe-patch-body-properties.md).
- Assessment date: October 30, 2026. Fresh focused tests: 113 passed, zero
  failures/skips. [Portable result receipt](focused-tests.json). Historical
  758-test ARM validation and builds belong to the October 29 fix, not a new
  full-package run for this report.
- Historical specs: `f6b53f105b95da05276530a0754a1c71b4f16397`.
  Historical consolidation evidence: `0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3`.
  Later source repair: `19a9d339ad4cdaf6f777bd44f78c61e2def6e118`
  ([#5820](https://github.com/Azure/typespec-azure/pull/5820)).
  Current destination fixes intentionally diverge from that source; the old
  source/destination traversal-equivalence claim no longer applies.
- Audience: explicitly enabled ARM analysis; the TypeSpec linter is a warning,
  registered but disabled in the shared resource-manager ruleset. It does not
  automatically distinguish ARM from data-plane services in a mixed program.
  Other PATCH rules and their overlapping diagnostics remain unchanged.
- [Member notes](evidence-details.md#member-evidence), [51 saved fixture observations](historical-fixtures.json),
  [source-to-test mapping and recovery](evidence-details.md#recovery-and-validation).
  Saved fixture counts use each fixture's selected Swagger member versus the
  combined TypeSpec rule; they are not an aligned production benchmark.
- No new Swagger generation, shared-baseline consumption, full-corpus execution,
  source repair, default enablement change, review reply or thread resolution
  was performed. Full-corpus and unresolved-gap gates remain open; this report
  does not certify migration/release readiness.

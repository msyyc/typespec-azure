# OperationIdNounVerb migration

## 1. Conclusion and scope

The TypeSpec linter
`@azure-tools/typespec-client-generator-core/no-redundant-operation-group-name`
migrates the naming intent of
[`OperationIdNounVerb`](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/docs/operation-id-noun-verb.md).
**It covers the approved common-SDK naming policy, but is not functionally
equivalent to checking serialized operation IDs.** Common client ownership,
common `@clientName` overrides, literal names and emitter-specific overrides
intentionally differ. This comparison assesses ARM source programs against saved
latest-version Swagger, not version-projected or data-plane corpus parity.

## 2. Actual coverage

All 487 selected projects were assessed; none failed or remained unassessed.
Reported diagnostics are total individual findings, not project counts.

| Count                                             | Swagger linter | TypeSpec linter |
| ------------------------------------------------- | -------------- | --------------- |
| Reported diagnostics                              | 265            | 123             |
| Common actionable unit across the complete corpus | Unassessed     | Unassessed      |

The fresh S3/a43 run reproduced every historical native project status, raw
diagnostic and aligned diagnostic exactly. Its retained Swagger member
observations also match the immutable frozen baseline exactly. Repeated Swagger
observations account for the largest difference. Common-method casing, explicit
operation IDs and AutoRest-only client relocation account for the other
differences. No full-corpus normalization is claimed.

## 3. Function-level coverage

| Behavior                                                                   | Result                                        |
| -------------------------------------------------------------------------- | --------------------------------------------- |
| Group noun repeated in a common method, including singular/plural forms    | Covered; one warning per authored operation   |
| Common `@clientName` overriding explicit `@client({name})`                 | Covered by focused and installed 1/0 controls |
| Distinct methods, case-sensitive near matches and empty normalized noun    | Compliant controls passed                     |
| Actual immediate subclient ownership, common name overrides and relocation | Covered                                       |
| Root clients, unowned operations and unrelated ancestor groups             | Exempt, with controls                         |
| Language-scoped names, explicit operation IDs and AutoRest casing          | Intentionally outside common-SDK policy       |
| Literal punctuation and full group names                                   | Covered without regex or underscore parsing   |
| ARM and data-plane standard operation templates                            | Violating/compliant native controls passed    |
| Authored suppression and recommended-preset nonactivation                  | Actual installed controls passed              |

## 4. Why diagnostic counts differ

| Project               | Swagger / TypeSpec findings | Cause and disposition                                                                                                                                                                                                                                              |
| --------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Billing               | 5 / 4                       | Serialization capitalizes a common lowercase method. [Casing evidence](evidence-details.md#gap-example-method-casing-introduced-by-serialization); no TypeSpec rule update required.                                                                               |
| DesktopVirtualization | 0 / 1                       | An explicit ID hides the common method's repeated group noun. [Override evidence](evidence-details.md#gap-example-explicit-operation-id-hides-a-common-sdk-repetition); intentional common-SDK coverage.                                                           |
| FileShares            | 0 / 4                       | Four explicit IDs hide four common-method repetitions. [Exact operations](evidence-details.md#same-cause-fileshares-explicit-operation-ids); intentional common-SDK coverage.                                                                                      |
| Network               | 154 / 11                    | Repeated saved observations at 11 exact route/verb targets. [Grouped evidence and attribution limits](evidence-details.md#network-reference-and-attribution-evidence); the 143 fallback attributions remain unavailable and are not treated as normalized defects. |
| Network/Vmss          | 5 / 3                       | Two AutoRest-only relocations use shorter groups than the actual common owners. [Ownership evidence](evidence-details.md#gap-example-autorest-only-operation-group-relocation); intentional common-SDK boundary.                                                   |
| Resources             | 4 / 3                       | Serialized casing adds one finding; three operations correspond, including two source-backed parameter-rename bridges. [Resources evidence](evidence-details.md#gap-example-resources-casing-and-explicit-route-bridges); no rule update required.                 |

## NOTES

- [Supporting evidence](evidence-details.md), [complete grouped targets](grouped-targets.md)
  and [all-project counts](counts.json) retain the full accounting. Swagger
  findings occur in 35 projects, TypeSpec findings in 37, with overlap 35 and no
  Swagger-only project. The two TypeSpec-only projects are explained above.
- Directional raw excesses are 147 Swagger and 5 TypeSpec; absolute difference
  is 152. There are 481 equal-count projects. These are not equivalent-defect
  counts. Conservative Swagger occurrence/file-independent keys are 210/122;
  TypeSpec source keys are 123.
- [Inputs](inputs.json) pin S3/T3, main, core, artifacts, tooling and the frozen
  baseline. Policy is `source`, `target-only`, `frozen-reference`, with no
  filter, limit or Swagger regeneration. Corpus default activation was not
  assessed; independent installed controls passed. The warning remains disabled
  in recommended presets.
- [Validation](validation.json) records 109 owning-package test files, 1,890
  passing tests and two unchanged skips, 31 focused tests, 14 rulesets tests,
  five compiled documentation controls, seven installed naming controls and 37
  applicable portable controls. Six predeclared unrelated portable cases are
  skips, not passes. The original timeout cause remains **UNPROVEN**.
- Historical E1/release1 remain immutable. [Publication preparation](publication-preparation.json)
  records locally verified cycle0-3 candidate/run assets and explicit reuse of
  the two release1 tooling assets. Native C2
  `54cc4d9ddb386ee4d7ce1f09d25ea13963d6150a` publishes exact tree T3.
  Evidence E2/release3, download recovery, checkpoint A2 and independent
  checkpoint B remain pending. All C2 checks completed. Six Ubuntu/Windows
  Node 22/24/26 builds, format, lint, website, change/version/common-types
  checks, CodeQL, end-to-end checks and language integrations passed. Automatic
  C2 ExternalIntegration run
  [41958140410](https://github.com/Azure/typespec-azure/actions/runs/41958140410)
  completed 211 passed and 394 failed of 605, so it is not green. All 394
  failures are classified as the unrelated ARM common-types-version v6 versus
  v5 requirement; none mention the target naming rule. No matching-base rerun
  or proof is claimed. PackageSize job `41958140431` separately failed on an
  unrelated Maven Central HTTP 429 and was not retried.

# DescriptiveDescriptionRequired migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-core/documentation-required` implements the supplied-content intent of [DescriptiveDescriptionRequired](https://github.com/Azure/azure-openapi-validator/blob/main/docs/descriptive-description-required.md). **Executable Swagger parity is intentionally partial:** the Swagger selector's truthy-value test has a false-negative bug that skips empty strings even though its function can reject them; the TypeSpec linter rejects explicit empty metadata. Source declarations without emitted counterparts also remain in scope. Current consolidated-rule corpus coverage remains unassessed.

## 2. Actual coverage

The historical run attempted 468 ARM projects at the frozen specs revision; 462 compiled successfully and six were excluded. Reported findings are individual diagnostics, not project counts.

| Count                                                       | Swagger linter | TypeSpec linter |
| ----------------------------------------------------------- | -------------- | --------------- |
| Historical successful-project raw diagnostics               | 0              | 5               |
| Current consolidated-rule corpus diagnostics for this check | Unassessed     | Unassessed      |

**Assessed coverage:** all five findings in three successful projects were investigated. Four match emitted `description: ""` fields that the Swagger selector skips; one is empty effective documentation on an inherited property whose description is omitted by the emitter. All five belong to selected latest API versions, not older-only declarations. This explains the historical five-finding difference but establishes no coverage percentage with a zero Swagger denominator. Twenty-seven Network warnings from a compiler-invalid project remain excluded from this table (the full TypeSpec shard has 32), and the current combined-rule corpus has not been measured.

See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) and the [complete pinned investigation](https://github.com/Azure/typespec-azure/blob/72ab22394704fce1a1555c879ff7335da8debf42/packages/typespec-lintdiff/test/fixtures/DescriptiveDescriptionRequired/migration.md).

## 3. Function-level coverage

All rows use the [official implementation and canonical fixture mapping](../../evidence-details.md#implementation-and-fixture-mapping), including violating examples and nonblank/absent-metadata controls. These are source-policy checks, not current corpus prevalence measurements.

| Behavior                                                                                 | Result                      | Rationale                                                                                                                                                                                         |
| ---------------------------------------------------------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Explicit empty or whitespace-only metadata                                               | Covered in recorded tests   | The official `empty` diagnostic uses trimmed compiler documentation, including Unicode whitespace. Missing docs remain a separate check.                                                          |
| Missing metadata and meaningful supplied descriptions                                    | Covered in recorded tests   | Undefined docs are not blank-content violations; nonblank text is accepted unless independently uninformative. [Combined controls](../../evidence-details.md#implementation-and-fixture-mapping). |
| Properties, parameters, members, variants, and inline/instantiated declarations          | Covered in recorded tests   | Exact authored property/member locations and instance cases remain in the canonical public-rule suite.                                                                                            |
| Explicit blank docs on namespace/interface/scalar and version/discriminator declarations | Covered in recorded tests   | Exemptions from requiring missing docs do not exempt explicitly blank metadata. Uninstantiated template docs unavailable from the compiler remain outside coverage.                               |
| Enum-member traversal                                                                    | Covered in recorded tests   | The current compiler emits `enumMember`; the official rule uses it. The original source's manual-loop rationale applied to an older closure and is not a current requirement.                     |
| Empty fields skipped by the Swagger selector                                             | Intentional extra coverage  | The source policy rejects the supplied blank value rather than reproducing the selector false negative.                                                                                           |
| Generated descriptions without an authored metadata target                               | Outside source-policy scope | The TypeSpec linter does not reconstruct generated response/authentication documentation or emitted-only fields.                                                                                  |

## 4. Why diagnostic counts differ

The [pinned report](https://github.com/Azure/typespec-azure/blob/72ab22394704fce1a1555c879ff7335da8debf42/packages/typespec-lintdiff/test/fixtures/DescriptiveDescriptionRequired/migration.md) traces all five successful-project findings:

- DataProtection's `findRestorableTimeRanges` has one emitted empty description.
- RecoveryServicesBackup has three explicitly empty model descriptions.
- ResourceHealth augments `AvailabilityStatus.name` with `@@doc(..., "")`; the effective inherited property documentation is empty, while emission omits the description.

The first four produce zero Swagger findings because `$..[?(@object() && @.description)].description` excludes empty strings. The [selector evidence](../../evidence-details.md#swagger-selector-evidence) distinguishes the captured installed-rule false-negative bug from current source inspection. The fifth produces zero because no emitted description field is selected. Preserve the TypeSpec blank checks; copying these selection/emission omissions would weaken the authoring policy.

Network supplies 27 additional raw warnings at five source identities but fails HTTP compilation. Keep them visible in the raw population, not in the successful-project comparison. Do not infer parity or successful compilation from warning counts.

## NOTES

- The [group report](../../migration.md) and [evidence details](../../evidence-details.md) distinguish this `empty` check from existing missing-documentation `default` diagnostics and the other member's `uninformative` diagnostics.
- Original lintdiff source: `72ab22394704fce1a1555c879ff7335da8debf42`, delivered through [#5672](https://github.com/Azure/typespec-azure/pull/5672); incorporated promotion [#5674](https://github.com/Azure/typespec-azure/pull/5674) is superseded by #5663.
- Historical run: specs `f6b53f105b95da05276530a0754a1c71b4f16397`, analysis generated October 12, 2026. The original report binds its uncommitted source draft by SHA-256, records the 468-project population, and retains the exact fixture and compiler exclusions. Its 22 source predicate tests and four strict comparison fixtures are historical, not present-day official suite totals.
- The original report's supplemental noise audit was unusable because its caller omitted local-linter activation. Required fixture validation supplied activation; do not treat the supplemental audit as passing equivalence evidence.
- The separate [CI-derived compatibility proposal](../../companion/causality.md) covers only `uninformative` name-check messages, not this member's `empty` findings. Its consumer annotations do not modify linter implementation or enablement, and local consumer validation was intentionally not run.
- This publication does not rerun coverage, recreate Swagger, or alter linter source, registration or dependencies. No current-source corpus, green-CI or merge-readiness claim follows from the historical counts.

# DescriptiveDescriptionRequired migration

## 1. Scope

The TypeSpec linter `@azure-tools/typespec-azure-core/documentation-required` is assessed against [DescriptiveDescriptionRequired](https://github.com/Azure/azure-openapi-validator/blob/main/docs/descriptive-description-required.md). Original migration linter PR: [Azure/typespec-azure#5663](https://github.com/Azure/typespec-azure/pull/5663).

## 2. Coverage

The official rule's blank-check corpus has not been measured at the assessed revision. The separate historical run attempted **468 ARM projects**, with **462 successful compilations and 6 exclusions**.

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------- | --------------- |
| Reported diagnostics | Unassessed     | Unassessed      |

The scorecard concerns the original Swagger blank-content check, not missing-documentation `default` warnings or name-check `uninformative` warnings. The historical configured-only counts were **0 Swagger / 5 TypeSpec**. Source suppressions were honored, but additional suppressed diagnostics were not separately captured; they remain unassessed, not zero.

**Analysis:** All five recorded TypeSpec findings in three successful projects were investigated and belong to selected latest API versions. Four have emitted `description: ""` fields that the Swagger selector skips; the fifth is empty inherited-property documentation omitted on emission. This explains that historical configured difference, not a current corpus total or a coverage percentage with a zero Swagger denominator.

See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ) and [the combined assessment](../../migration.md).

## 3. Why diagnostic counts differ

The official rule's net gap is **unassessed**. The following table accounts for all five configured diagnostics in the historical successful-project comparison; uncaptured suppressed additions are not included in that historical snapshot.

| Difference (with evidence)                                                                                                                                                                                                               | Swagger diagnostics | TypeSpec diagnostics for the same check | analysis                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Empty emitted descriptions skipped by the selector](../../evidence-details.md#swagger-selector-evidence)                                                                                                                                | 0                   | 4 configured                            | DataProtection's `findRestorableTimeRanges` contributes one field and RecoveryServicesBackup contributes three model descriptions. The truthy selector skips all four empty strings, a confirmed false-negative bug. Retain the TypeSpec blank checks rather than reproduce it. |
| [Empty inherited-property documentation omitted on emission](https://github.com/Azure/typespec-azure/blob/72ab22394704fce1a1555c879ff7335da8debf42/packages/typespec-lintdiff/test/fixtures/DescriptiveDescriptionRequired/migration.md) | 0                   | 1 configured                            | ResourceHealth augments `AvailabilityStatus.name` with `@@doc(..., "")`; effective documentation is empty but emission omits the field. Retain the source check instead of inferring meaningful documentation from output absence.                                              |

**Raw-count reconciliation:** **`0 - 5 = (0 - 4) + (0 - 1) = -5`** for the historical configured snapshot. The [captured installed-rule behavior](../../evidence-details.md#swagger-selector-evidence) is distinct from later source inspection of `$..[?(@object() && @.description)].description`.

The full historical TypeSpec shard has **32 findings = 5 successful-project findings + 27 Network findings** from a compiler-invalid project. Those 27 findings occur at five source identities and remain excluded from the successful-project comparison; warning counts do not establish successful compilation. The original investigation retains their raw population. No suppression-inclusive or official-rule difference can be inferred from this historical arithmetic.

## 4. Function-level coverage

These source-policy checks use the [official implementation and canonical fixture mapping](../../evidence-details.md#implementation-and-fixture-mapping), including violating and compliant controls; they are not current corpus prevalence measurements.

| Behavior                                                                                 | Result                            | analysis                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Explicit empty or whitespace-only metadata                                               | Covered in recorded tests         | The official `empty` diagnostic uses trimmed compiler documentation, including Unicode whitespace. Missing docs remain a separate check.                                                          |
| Missing metadata and meaningful supplied descriptions                                    | Covered in recorded tests         | Undefined docs are not blank-content violations; nonblank text is accepted unless independently uninformative. [Combined controls](../../evidence-details.md#implementation-and-fixture-mapping). |
| Properties, parameters, members, variants and inline/instantiated declarations           | Covered in recorded tests         | Exact authored property/member locations and instance cases remain in the canonical public-rule suite.                                                                                            |
| Explicit blank docs on namespace/interface/scalar and version/discriminator declarations | Covered in recorded tests         | Missing-doc exemptions do not exempt explicitly blank metadata. Uninstantiated template docs unavailable from the compiler remain outside coverage.                                               |
| Enum-member traversal                                                                    | Covered in recorded tests         | The assessed compiler emits `enumMember`; the official rule uses it. The original source's manual-loop approach belonged to an older closure.                                                     |
| Empty fields skipped by the Swagger selector                                             | Additional source-policy coverage | The source check rejects supplied blank metadata rather than reproducing the selector false negative.                                                                                             |
| Generated descriptions without an authored metadata target                               | Outside source policy             | The TypeSpec linter does not reconstruct generated response/authentication documentation or emitted-only fields.                                                                                  |

## NOTES

- **Inputs:** [Frozen identities](../../evidence-details.md#frozen-identities) retain official source/compiler and specs pins. Historical source `72ab22394704fce1a1555c879ff7335da8debf42` was delivered through [Azure/typespec-azure#5672](https://github.com/Azure/typespec-azure/pull/5672); incorporated promotion [Azure/typespec-azure#5674](https://github.com/Azure/typespec-azure/pull/5674) is superseded by #5663. This is report-only reuse, not a new run.
- **Historical evidence:** The [immutable investigation](https://github.com/Azure/typespec-azure/blob/72ab22394704fce1a1555c879ff7335da8debf42/packages/typespec-lintdiff/test/fixtures/DescriptiveDescriptionRequired/migration.md) retains the October 12, 2026 analysis, source fingerprint, 22 predicate tests, four strict fixtures and compiler exclusions. Its supplemental noise audit omitted local-linter activation and is not passing equivalence evidence; required fixture validation supplied activation.
- **Validation and compatibility:** [Official validation limits](../../evidence-details.md#validation-and-release-readiness) remain separate from the historical run. The [CI-derived proposal](../../companion/causality.md) concerns only `uninformative`, not this member's `empty` findings. No local consumer validation, current corpus run or green-CI claim is made.

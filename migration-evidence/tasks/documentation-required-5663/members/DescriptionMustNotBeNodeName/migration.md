# DescriptionMustNotBeNodeName migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-core/documentation-required` implements the authored-documentation intent of [DescriptionMustNotBeNodeName](https://github.com/Azure/azure-openapi-validator/blob/main/docs/description-must-not-be-node-name.md). **Exact executable Swagger equivalence is partial.** The official policy deliberately uses authored ordinary-property names instead of JSON serialization names, and does not reconstruct generated names or repeated reference occurrences. Historical corpus evidence supports the earlier lintdiff implementation; current official-rule corpus coverage remains unassessed.

## 2. Actual coverage

The historical investigation attempted 468 ARM projects and compared 462 successful compilations, excluding six HTTP compiler failures. Findings below are individual diagnostics, not project counts.

| Count                                         | Swagger linter | TypeSpec linter |
| --------------------------------------------- | -------------- | --------------- |
| Historical successful-project raw diagnostics | 70,815         | 7,523           |
| Current official-rule corpus diagnostics      | Unassessed     | Unassessed      |

**Assessed coverage:** all 105 Swagger-affected successful projects overlap the 143 TypeSpec-affected projects. The historical selected-version investigation removes 22 findings and one project, retaining 7,501 findings in 142 projects. The investigated causes of the remaining differences are source-only declarations, client compatibility types, naming differences, and erased parameters; this does not establish a universal violation identity. Comparable violation totals and coverage percentages are **unassessed**. The official authored-name change has focused unit evidence, not a refreshed corpus measurement.

See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the differences and their [detailed historical evidence](https://github.com/Azure/typespec-azure/blob/3753a319f32f3926005536029f9ff32b94f3c905/packages/typespec-lintdiff/test/fixtures/DescriptionMustNotBeNodeName/migration.md).

## 3. Function-level coverage

All rows use the [official implementation and canonical fixture mapping](../../evidence-details.md#implementation-and-fixture-mapping), including violating examples and meaningful-documentation controls. These are source-policy checks, not current corpus prevalence measurements.

| Behavior                                                                        | Result                             | Rationale                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Trim, period removal, case-insensitive name equality, placeholder `description` | Covered in recorded tests          | The official rule applies normalization and targets offending semantic declarations; meaningful text and punctuation-only controls remain. [Current mapping](../../evidence-details.md#implementation-and-fixture-mapping). |
| Enum members, named union variants, unnamed string values, ordinary keys        | Covered in recorded tests          | Explicit target cases avoid the former blanket key exemption and missing member checks; other unnamed variants receive placeholder checks only.                                                                             |
| Authored operation names and effective GET/POST verbs                           | Covered in recorded tests          | Both source names and HTTP verbs are considered; inferred and explicitly declared verbs have contrasting controls.                                                                                                          |
| HTTP path/query/header and multipart names                                      | Covered in recorded tests          | Wire metadata has precedence, unnamed parts fall back to source names, and repeated parts unwrap their outer array.                                                                                                         |
| Ordinary JSON-renamed properties                                                | Intentional policy difference      | The current rule compares authored names. The old lintdiff fixtures' JSON-name compliance/violation outcomes are historical and are not claimed as current parity.                                                          |
| Status-code property name repetition                                            | Exempt                             | Name checks skip status-code properties; explicit blank documentation is still checked separately.                                                                                                                          |
| Emitted-only names, references, unused-source filtering                         | Outside the source-policy boundary | The rule does not depend on an emitter or restrict checks to emitted reachability. [Scope differences](../../evidence-details.md#historical-name-check-differences) remain visible.                                         |

## 4. Why diagnostic counts differ

The full retained historical shards contain 86,264 Swagger findings and 8,499 TypeSpec findings, including compiler-invalid projects. Excluding those projects yields 70,815 and 7,523. Selected-version attribution further retains 7,501 TypeSpec findings; these populations must not be mixed.

The [historical investigation](https://github.com/Azure/typespec-azure/blob/3753a319f32f3926005536029f9ff32b94f3c905/packages/typespec-lintdiff/test/fixtures/DescriptionMustNotBeNodeName/migration.md) records 86,255 enum-metadata occurrences among all 86,264 Swagger findings. SQL repeats 34 ColumnDataType members across reference roots: 3,740 reported occurrences across 110 files. AlertsManagement has 76 definition findings plus 124 inline copies, compared with 76 source targets. These counts describe emission multiplicity, not thousands of independent authored defects.

The 38 unprojected TypeSpec-only projects become 37 after selected-version attribution; the original report preserves the complete project list and six cause categories. IoTOperations has two additional un-emitted version-enum members: excluding those for an emitted-version-only comparison gives 7,499 findings in 141 projects, but production continues to check explicit source docs. No new reachability filter is recommended.

The official ordinary-property adaptation is a separate, reviewed policy difference. `@encodedName("application/json", "wire-name")` does not change the author's node-name comparison. Keep that policy rather than restoring the historical JSON-name resolver solely for Swagger parity. Its corpus delta is unassessed.

## NOTES

- Current implementation/test identities and commands are in the [group evidence details](../../evidence-details.md). The group report is the [combined assessment](../../migration.md).
- Original lintdiff source: `3753a319f32f3926005536029f9ff32b94f3c905`, originally delivered through [#5662](https://github.com/Azure/typespec-azure/pull/5662). The historical report records its actual pre-commit content fingerprint, specs pin, harness, source suppressions, reference resolution, and selected-version attribution procedure.
- Historical source validation: 47 predicate tests, 15 strict comparison fixtures, and the 468-project run with six exclusions. These are not current official-rule test totals. The [immutable original report](https://github.com/Azure/typespec-azure/blob/3753a319f32f3926005536029f9ff32b94f3c905/packages/typespec-lintdiff/test/fixtures/DescriptionMustNotBeNodeName/migration.md) retains outliers, controls, repair evidence, supplemental audit failures, and explicit limits.
- No new corpus run, Swagger regeneration, source repair, or TypeSpec linter change was performed for this report-only refresh. Current-head corpus equivalence is not asserted.

# DescriptionMustNotBeNodeName migration

## 1. Scope

The TypeSpec linter `@azure-tools/typespec-azure-core/documentation-required` is assessed against [DescriptionMustNotBeNodeName](https://github.com/Azure/azure-openapi-validator/blob/main/docs/description-must-not-be-node-name.md). Original migration linter PR: [Azure/typespec-azure#5663](https://github.com/Azure/typespec-azure/pull/5663).

## 2. Coverage

The official rule's name-check corpus has not been measured at the assessed revision. The separate historical lintdiff run attempted **468 ARM projects** and compared **462 successful compilations**, excluding six compiler-invalid projects.

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------- | --------------- |
| Reported diagnostics | Unassessed     | Unassessed      |

The scorecard concerns the official rule's original Swagger name check, not existing missing-documentation or blank-content warnings. Historical configured findings were **70,815 Swagger / 7,523 TypeSpec**; additional suppressed findings were not captured and remain unassessed. These earlier counts cannot be relabeled as a current suppression-inclusive total.

**Analysis:** All 105 Swagger-affected successful projects were among 143 TypeSpec-affected projects. Selected-version attribution retained 7,501 TypeSpec findings in 142 projects, but project overlap and version attribution do not establish matched defects or a coverage percentage. The official authored-name adaptation has focused unit evidence, not a refreshed corpus measurement.

See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ) for the historical arithmetic and [the combined report](../../migration.md) for the two-check scope.

## 3. Why diagnostic counts differ

The current official-rule gap is **unassessed**. The historical configured-only successful-project difference is **`70,815 - 7,523 = 63,292`**. The [pinned investigation](https://github.com/Azure/typespec-azure/blob/3753a319f32f3926005536029f9ff32b94f3c905/packages/typespec-lintdiff/test/fixtures/DescriptionMustNotBeNodeName/migration.md) records the following causes, not a complete diagnostic-by-diagnostic partition of that difference:

- **Repeated emission and reference roots:** SQL accounts for 64,724 raw findings, including 3,740 ColumnDataType occurrences across 110 files for 34 file-independent member paths and 34 authored members. AlertsManagement has 76 definition findings plus 124 inline copies versus 76 source targets. These are source/emission multiplicities, not a common raw diagnostic identity. [Historical examples](../../evidence-details.md#historical-name-check-differences).
- **Source/version population:** 38 unprojected TypeSpec-only projects become 37 after selected-version attribution removes 22 findings, leaving 7,501. Removing two additional un-emitted IoTOperations version-enum members would leave 7,499 in 141 projects, but production continues to check explicit source docs. No new reachability filter is proposed.
- **Naming and authoring differences:** The original witnesses include unused/imported source declarations, client compatibility types, removed/later-version declarations, namespace-qualified schema names, template-renamed keys and constant parameters erased during emission. Preserve those distinctions rather than infer universal source/output correspondence.
- **Official ordinary-property adaptation:** The official rule compares authored names under `@encodedName("application/json", "wire-name")`, unlike the historical JSON-name resolver. Retain the reviewed policy and regression; its corpus delta is unassessed. [Authorized adaptations](../../evidence-details.md#authorized-policy-adaptations).

The full historical shards contain 86,264 Swagger and 8,499 TypeSpec findings, including the six excluded projects. Excluding their **15,449 Swagger and 976 TypeSpec findings** gives the successful-project counts above. The original report also records 86,255 enum-metadata occurrences in the full Swagger shard. None of these larger-population figures is substituted for a successful-project or current official total.

**Reconciliation limit:** The historical net difference of 63,292 is known, but its full per-cause allocation and a collision-resistant cross-engine correspondence remain unassessed. Do not interpret that number as missing TypeSpec checks, subtract example subsets as if they were disjoint, or count 34 authored members as 34 captured diagnostics without diagnostic evidence. The official rule's net gap and suppressed additions cannot be calculated from these saved aggregate observations.

## 4. Function-level coverage

These are source-policy checks supported by the [official implementation and canonical fixture mapping](../../evidence-details.md#implementation-and-fixture-mapping), not current corpus prevalence measurements.

| Behavior                                                                           | Result                     | analysis                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------- | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Trim, period removal, case-insensitive name equality and placeholder `description` | Covered in recorded tests  | Normalization targets offending semantic declarations; meaningful text and punctuation-only controls remain. [Current mapping](../../evidence-details.md#implementation-and-fixture-mapping). |
| Enum members, named union variants, unnamed string values and ordinary keys        | Covered in recorded tests  | Exact target cases retain member checks; other unnamed variants receive placeholder checks only.                                                                                              |
| Authored operation names and effective GET/POST verbs                              | Covered in recorded tests  | Source names and HTTP verbs are considered; inferred and explicitly declared verbs have contrasting controls.                                                                                 |
| HTTP path/query/header and multipart names                                         | Covered in recorded tests  | Wire metadata has precedence, unnamed parts fall back to source names, and repeated parts unwrap their outer array.                                                                           |
| Ordinary JSON-renamed properties                                                   | Reviewed policy difference | The official rule compares authored names; historical JSON-name fixture outcomes are not current parity claims.                                                                               |
| Status-code property name repetition                                               | Exempt                     | Name checks skip status-code properties; explicit blank documentation is checked separately.                                                                                                  |
| Emitted-only names, references and unused-source filtering                         | Outside source policy      | The rule does not depend on an emitter or restrict checks to emitted reachability. [Scope differences](../../evidence-details.md#historical-name-check-differences).                          |

## NOTES

- **Inputs:** Official source/compiler and specs identities are in [frozen identities](../../evidence-details.md#frozen-identities). The historical source is `3753a319f32f3926005536029f9ff32b94f3c905`, originally delivered through [Azure/typespec-azure#5662](https://github.com/Azure/typespec-azure/pull/5662). No new corpus run or source change is claimed.
- **Historical evidence:** The [immutable investigation](https://github.com/Azure/typespec-azure/blob/3753a319f32f3926005536029f9ff32b94f3c905/packages/typespec-lintdiff/test/fixtures/DescriptionMustNotBeNodeName/migration.md) retains 47 predicate tests, 15 strict fixtures, source fingerprints, suppressions, exact project witnesses and audit/replay limits. These are source-phase totals, not official-rule test totals.
- **Official validation and separate CI:** [Recorded validation](../../evidence-details.md#validation-and-release-readiness) is distinct from corpus coverage. The [compatibility proposal](../../companion/causality.md) retains 10,697 observed occurrences and 7,901 proposed suppression targets in 219 files, with an unknown tested consumer SHA and no local consumer validation. It is not a Swagger comparison or a green-CI claim.

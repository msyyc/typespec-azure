# DescriptiveDescriptionRequired migration

## 1. Scope

The TypeSpec linter `@azure-tools/typespec-azure-core/documentation-required` is assessed against [DescriptiveDescriptionRequired](https://github.com/Azure/azure-openapi-validator/blob/main/docs/descriptive-description-required.md). Original migration linter PR: [Azure/typespec-azure#5663](https://github.com/Azure/typespec-azure/pull/5663).

## 2. Coverage

The November 18 official-rule run assessed **all 490 frozen ARM projects**, with **zero failures or exclusions**.

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------- | --------------- |
| Reported diagnostics | 0              | 32              |

TypeSpec has **zero configured + 32 captured suppressed** `empty` diagnostics. These are actual findings observed before compiler suppression on every successful program, not predictions. The name-check and existing missing-documentation families are excluded. [Scoped accounting](../../runs/native-20261118/scoped-summary.json) and [quality diagnostic shard](../../runs/native-20261118/native-quality.jsonl) preserve the distinction.

**Assessed coverage:** Blank findings occur in **four projects at 10 source locations**: DataProtection 1, Network 27 at five locations, RecoveryServicesBackup 3, and ResourceHealth 1. The Swagger rule is registered in the production common Spectral ruleset; its zero is evaluated absence of findings, not an omitted/staging-only rule.

**Analysis:** Injected controls distinguish missing, meaningful and explicitly blank documentation. Four native findings have traced emitted empty descriptions that the truthy Swagger selector skips; ResourceHealth's augmented empty documentation is not emitted. Network's 27 semantic findings now belong to successful programs, but their finer template/emission correspondence remains unassessed. Zero Swagger findings do not provide a meaningful coverage-percentage denominator. See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

Every native value below includes captured suppressed diagnostics, even though configured execution reports none.

| Difference (with evidence)                                                                                       | Swagger diagnostics | TypeSpec diagnostics for the same check | analysis                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------- | ------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Empty emitted descriptions skipped by the selector](../../evidence-details.md#current-blank-witnesses)          | 0                   | 4                                       | DataProtection's findRestorableTimeRanges operation and three RecoveryServicesBackup model definitions have actual `description: ""` fields in the saved selected-version Swagger. The selector's truthy precondition skips them: retain the native check rather than reproduce this false negative. |
| [Empty inherited-property documentation absent from emission](../../evidence-details.md#current-blank-witnesses) | 0                   | 1                                       | ResourceHealth applies `@@doc(AvailabilityStatus.name, "")`; the native diagnostic points to the inherited property source. No empty description field is present in that project's saved Swagger. This is source-policy coverage, not meaningful docs inferred from output absence.                 |
| [Network semantic instances at five source locations](../../runs/native-20261118/investigation.json)             | 0                   | 27                                      | Counts are 1 + 1 + 10 + 6 + 9. Two empty emitted parameter descriptions are inventoried, but no exact mapping from all semantic instances is established. Source locations and repeated template instances must not be collapsed into five diagnostics or assigned an invented cause.                |

**Raw-count reconciliation:** **`0 - 32 = (0 - 4) + (0 - 1) + (0 - 27) = -32`**. Four projects have a native directional excess of 32; the other 486 are equal. The residual **27 findings have unresolved exact template/emission attribution**, not unmeasured diagnostic totals.

The previous configured-only successful-project snapshot contained five findings and excluded Network's 27 because that historical compilation failed. The new frozen population compiles successfully, and all 32 findings are captured despite current source suppressions. The shared baseline was not regenerated; source and producer/candidate emission closures remain distinct.

## 4. Function-level coverage

| Behavior                                                        | Result                                                   | analysis                                                                                                                                                                                                                         |
| --------------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Explicit empty or whitespace-only metadata                      | Verified canonical/injected controls and corpus findings | The official check uses trimmed compiler documentation, including explicit metadata on otherwise missing-doc-exempt declarations. [Validation](../../evidence-details.md#current-run-validation).                                |
| Missing docs and meaningful supplied text                       | Verified compliant/discriminating controls               | Missing docs are a separate family; they are not credited as blank violations.                                                                                                                                                   |
| Properties, parameters, members and semantic/template instances | Covered by canonical tests and captured targets          | Individual findings retain multiplicity even where source locations coincide; uninstantiated metadata unavailable from the compiler is outside coverage.                                                                         |
| Enum-member traversal and exempt declarations                   | Covered by canonical tests                               | The pinned compiler emits `enumMember`; no legacy manual member loop is required. [Fixture mapping](../../evidence-details.md#implementation-and-fixture-mapping).                                                               |
| Direct/ancestor source suppression                              | Exhaustively captured for this successful corpus         | The observer uses the same program and exact injected mapped linter, with configured multiset reconciliation and no additional compilation. [Method and controls](../../runs/native-20261118/README.md#suppression-observation). |
| Empty fields skipped by Swagger                                 | Additional source-policy coverage                        | Retain the native blank check; production registration and saved fields support the selector explanation.                                                                                                                        |
| Generated-only fields and complete source/output correspondence | Outside source policy / partially unresolved             | Network's 27-instance correspondence is not promoted to full equivalence or a confirmed missing native check.                                                                                                                    |

## NOTES

- **Inputs and recovery:** Official head `2c6596126f281d78ca06fb23afc9ef8ab37684b8`, core `8574d5453f7bf9a07dc09bd41edac579af71d94b`, specs `6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc`; [new native-run and immutable-baseline replay](../../runs/native-20261118/README.md).
- **Historical sources:** [Original investigation at 72ab2239](https://github.com/Azure/typespec-azure/blob/72ab22394704fce1a1555c879ff7335da8debf42/packages/typespec-lintdiff/test/fixtures/DescriptiveDescriptionRequired/migration.md) retains the prior configured snapshot. Incorporated [promotion #5674](https://github.com/Azure/typespec-azure/pull/5674) remains superseded by #5663; no historical counts are added to the new run.
- **Validation and compatibility:** [Current validation](../../evidence-details.md#current-run-validation) is separate from unchanged [companion #48090](https://github.com/Azure/azure-rest-api-specs/pull/48090), which concerns only name checks. No companion refresh or green-CI claim is made.

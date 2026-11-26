# DefaultErrorResponseSchema migration

## 1. Scope

The TypeSpec linter
`@azure-tools/typespec-azure-resource-manager/use-standard-error` is assessed
against Swagger linter
[`DefaultErrorResponseSchema`](https://github.com/Azure/azure-openapi-validator/blob/405e6f094fa8280e05af23327845f6202a8edc65/docs/default-error-response-schema.md).
The existing TypeSpec linter was introduced in
[Azure/typespec-azure#5451](https://github.com/Azure/typespec-azure/pull/5451).

## 2. Coverage

All 490 frozen ARM projects were assessed successfully; none failed or remain
unassessed. The comparison uses unprojected TypeSpec source and retained
latest-version Swagger, not aligned version/reachability populations.

Reported diagnostics are individual default-payload findings. The TypeSpec total
is 5,119 selected-rule diagnostics minus 450 missing-marked-response checks and
40 explicit-only payload checks. No corresponding suppressed diagnostics were
captured in the 144 inspected projects. Suppression inspection is not exhaustive
across all 490 projects.

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------- | --------------- |
| Reported diagnostics | 762            | 4,629           |

**Analysis:** **Assessed coverage:** The 762 Swagger observations occupy 273
project/path/method contexts. Captured structural-default diagnostics correspond
to 268 contexts; five inherited library operations are not linted. The TypeSpec
linter also reports 4,248 custom defaults whose corresponding retained schemas
have the required properties, plus 113 source-only operations. HEAD exemptions
and unmarked malformed defaults remain material limits. These are not
equivalent-defect counts or a coverage percentage.

The scoped project sets contain 18 overlapping projects, one Swagger-only
project and 110 TypeSpec-only projects.
[Detailed accounting and scope limits](evidence-details.md#full-population-accounting)
explain these sets and every differing group. See
[Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

Grouped Swagger contexts below use exact project, path and HTTP method.
Grouping preserves raw observations; it does not normalize equivalent defects.
Both columns retain the section 2 diagnostic and suppression scope.

| Difference (with evidence)                                                                                | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics for the same check | analysis                                                                                                                                                  |
| --------------------------------------------------------------------------------------------------------- | ----------------------------------- | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Network input-associated repetition](evidence-details.md#repeated-input-associated-swagger-observations) | 528 / 39                            | 39                                      | The malformed defaults are recognized. Retain 489 additional observations; ambiguous originating files are not invented.                                  |
| [Inherited provider operations](evidence-details.md#inherited-library-operations-are-not-lint-targets)    | 5 / 5                               | 0                                       | Missing coverage. An owning-rule extension needs owner approval and project-owned reporting targets.                                                      |
| [Stricter standard-model identity](evidence-details.md#full-population-accounting)                        | 0 / —                               | 4,248                                   | Required properties exist in the saved defaults, but the custom models still warn. Prefer standard models only when API compatibility permits.            |
| [SDK override declarations](residual-evidence.md#sdk-overrides)                                           | 0 / —                               | 46                                      | Captured source customizations are outside the service HTTP graph. Retain these source-scope diagnostics rather than calling them emitted API defects.    |
| [Declarations unavailable in the selected version](residual-evidence.md#version-availability)             | 0 / —                               | 67                                      | Authored availability annotations and version-enum order explain the source/latest-version population difference. This is not a projected TypeSpec rerun. |

Another 229 authored contexts have one diagnostic from each linter and cancel.
The [source-backed path investigation](residual-evidence.md#explicit-path-representations)
places 17 initially unmatched paths within the 4,248 stricter defaults; it does
not add diagnostics or normalize counts.

**Raw-count reconciliation:** **762 - 4,629 = 489 + 5 - 4,248 - 46 - 67 =
-3,867**. Per-project Swagger-higher excess is 4; TypeSpec-higher excess is 3,871.
Their absolute sum is 3,875. Opposing differences are retained in the
[complete project accounting](project-accounting.csv) and
[differing model/project groups](difference-groups.md).

## 4. Function-level coverage

| Behavior                                                             | Result                             | analysis                                                                                                                                |
| -------------------------------------------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Existing default lacks a schema, nested `error`, `code` or `message` | Covered for linted marked defaults | [Discriminating controls and real findings](evidence-details.md#predicate-and-member-matrix) establish this bounded behavior.           |
| Standard error response and supported aliases                        | Compliant                          | The owning tests, injected ARM-template control and actual final correct documentation example pass.                                    |
| Custom default has all required properties                           | Stricter TypeSpec policy           | Standard model identity is still required. Structural similarity alone does not satisfy this rule.                                      |
| Inherited library operation has a malformed default                  | Missing coverage                   | Five real cases remain. Existing template use does not prevent custom error overrides.                                                  |
| HEAD or unmarked malformed default                                   | Missing Swagger scope              | [Controls](evidence-details.md#predicate-and-member-matrix) verify these limits. No exemption removal or policy retirement is approved. |
| Authored suppression                                                 | Honored                            | Positive, compliant and suppressed controls capture emitted/callback counts of `1/1`, `0/0` and `0/1`.                                  |

## NOTES

- **Inputs:** [Candidate snapshot and 15-package closure](candidate.json);
  [pinned specs, tooling and shared baseline](inputs.json). This is a fresh
  490-project TypeSpec run. Frozen-reference reuse does not prove identical
  current Swagger emission.
- **Counting:** [Assessment](assessment.json), [exclusion ledger and recovery assets](assets.json)
  and [source-path/population evidence](residual-evidence.md) preserve raw,
  scoped and conservative location counts. No equivalent-defect normalization
  or exhaustive suppression-inclusive corpus total is claimed.
- **Fixture sources:** 22 source files remain byte-exact. Two display derivatives
  remove terminal whitespace only; [recover their exact executed originals](evidence-details.md#tested-fixture-bytes-and-publication-derivatives)
  from base64 and verify the recorded hashes. The display derivatives were not executed.
- **Validation:** [Focused tests and documentation checks pass](validation.json).
  The earlier broad run failed with seven ordinary-test and nine hook timeouts;
  999 tests passed. The user prospectively replaced that broad gate with focused
  affected checks. [Final local review accepted partial guidance](task.json); durable publication and GitHub checkpoints remain pending.
  [Companion evidence is pending](companion-evidence.json), not green consumer CI.

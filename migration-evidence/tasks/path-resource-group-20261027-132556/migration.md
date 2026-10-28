# PathContainsResourceGroup migration

## 1. Conclusion and scope

The TypeSpec rule
`@azure-tools/typespec-azure-resource-manager/resource-group-path-parameter`
migrates Swagger linter rule
[`PathContainsResourceGroup`](https://github.com/Azure/azure-openapi-validator/blob/18a7944e7fc3155e8ef1498665465ed5f455f54a/docs/path-contains-resource-group.md).
**The migrated rule is functionally equivalent to the original Swagger linter
for the assessed ARM path policy.**

## 2. Actual coverage

All **487 projects** were assessed, with no failures.
Reported diagnostics means the total number of individual linter findings,
not the number of projects. Both linters report findings in **three projects**.

| Count                                    | Swagger linter | TypeSpec linter |
| ---------------------------------------- | -------------: | --------------: |
| Reported diagnostics                     |             43 |              31 |
| After analysis: affected HTTP operations |             31 |              31 |

Analysis shows that both linters identify the **same 31 operations**, with no
missing or extra operations. The reported counts remain 43 and 31; the second
row compares the affected operations rather than changing those raw counts.

## 3. Function-level coverage

Tests establish matching behavior for the following checks and compliant cases.

| Behavior                   | Result                                                                                                 |
| -------------------------- | ------------------------------------------------------------------------------------------------------ |
| HTTP methods               | GET, PUT, PATCH and DELETE checked; POST and HEAD excluded                                             |
| ARM templates              | Incorrect custom base parameters detected; standard and correctly retained parameters accepted         |
| Resource-group paths       | Missing, incorrect and literal parameters detected; original case and path-matching behavior preserved |
| Serialized parameter names | Both directions of `@path` name overrides checked                                                      |
| Eligible operations        | Non-ARM services excluded; mixed services and concrete generic operations/interfaces tested            |
| Activation and suppression | Explicit activation, inherited options and authored suppression tested; default remains disabled       |

## 4. Why diagnostic counts differ

The differences come from how findings are counted, not missing rule behavior:

- **[DataMigration](evidence-details.md#datamigration-method-multiplicity):**
  11 Swagger linter diagnostics describe paths containing 26 affected operations.
  The TypeSpec linter reports those 26 operations individually.
- **[Network](evidence-details.md#network-reference-multiplicity):**
  30 Swagger linter diagnostics repeat findings through referenced documents.
  The two affected paths contain the same three operations reported by the
  TypeSpec linter.

[Advisor](evidence-details.md#advisor-direct-route) already agrees at two
diagnostics and two affected operations for each linter. No unexplained
differences remain.

## 5. Example: incorrect and correct parameter names

**Incorrect custom base:** The resource-group parameter is named `groupName`
instead of `resourceGroupName`.

```typespec
model CustomBase {
  ...CommonTypes.ApiVersionParameter;
  ...CommonTypes.SubscriptionIdParameter;
  @path @segment("resourceGroups") groupName: string;
}
```

Using this base in `ArmResourceRead<Widget, BaseParameters = CustomBase>` produces
one TypeSpec linter warning.

**Correct standard template:** `ArmResourceRead<Widget>` retains the standard
`resourceGroupName` parameter and produces no warning. Both documentation
snippets compile without errors.

## NOTES

- **Comparison scope:** Production Azure Resource Manager (ARM), OpenAPI 2.0,
  using the [frozen inputs](evidence-details.md#frozen-inputs). The Swagger linter
  uses the latest emitted API version; the TypeSpec linter uses the source
  program. A separate selected-version HTTP audit verifies every affected
  operation; it does not rerun the TypeSpec linter on a projected program.
  Compiler/library versions differ from the Swagger baseline producer. Targeted
  path evidence supports this comparison; byte-identical Swagger and equivalence
  for untested specs or policies are not claimed.
- **Counting details:** The
  [per-project audit](receipts/step8-operation-comparison-full.json) compares
  exact project, full path and HTTP method, with verified reference chains.
  Raw Swagger-linter-higher and TypeSpec-linter-higher differences are 27 and 15;
  they do not cancel. The [comparison method](evidence-details.md#comparison-method)
  retains location counts, source-attribution limits and eight comparison
  controls. The [automatic report](runs/full-native-01/coverage.md) leaves
  equivalence undetermined; the conclusion above comes from the semantic tests
  and operation-level investigation, not matching totals alone.
- **Severity and activation:** The Swagger linter reports errors; the TypeSpec
  linter reports warnings and is disabled by default. Coverage explicitly
  enabled the TypeSpec linter. Default activation was not measured by the corpus
  run; separate tests cover registration, activation and suppression.
  Enabling the TypeSpec linter by default remains a separate policy decision.
- **Validation:** 25 rule cases, five registration checks, 671 ARM package tests,
  nine ruleset tests, 37 installed-package controls, 75 harness tests and eight
  comparison controls passed. These are test counts, not a coverage percentage.
  The [validation details](evidence-details.md#validation) retain earlier failed
  attempts, 32 unrelated tooling typecheck errors, and the full 80-minute run
  timing. A full tooling typecheck pass is not claimed.
- **Recovery:** [Saved-evidence replay](receipts/fresh-replay.json) reproduced
  the 487-project results. It was not a complete compiler/emitter rerun.
  [Recovery instructions](evidence-details.md#recovery-and-replay) retain the
  inputs and commands. This revision changes report presentation only; no
  coverage data or rule implementation was changed or rerun.

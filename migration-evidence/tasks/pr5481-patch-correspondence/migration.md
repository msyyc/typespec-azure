# PatchPropertiesCorrespondToPutProperties migration

## 1. Scope

The TypeSpec linter
`@azure-tools/typespec-azure-resource-manager/arm-resource-patch` is assessed
against Swagger linter
[`PatchPropertiesCorrespondToPutProperties`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-properties-correspond-to-put-properties.md).
Original migration linter PR: [Azure/typespec-azure#5481](https://github.com/Azure/typespec-azure/pull/5481).

## 2. Coverage

**487 ARM projects evaluated; 0 failed or unassessed project executions.**
The table counts individual diagnostic occurrences, not equivalent defects.
It retains all configured name/body findings, including TypeSpec-only checks.
No captured suppressed diagnostic is added: Quota's suppression evidence is a
separate compiler probe, not a captured linter callback. Suppression inspection
covers the 51 retained-record projects, not an exhaustive pre-suppression corpus.
Separate body-policy probes are outside this correspondence-check profile;
[counting boundaries](names-20261117/assessment.md#report-counting-boundaries).

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics |          1,314 |              85 |

**Analysis:** **Assessed coverage:** excluding **1,132 confirmed Swagger
overchecks** leaves **182 records**: **58 check-covered** (57 reporting records
and one suppression-probed body check), **92 legitimate accepted/non-input
records**, and **32 deliberately not migrated value/constraint records**.
Those 32 are coverage loss, not false positives; removing constraint comparison
lost 19 TypeSpec warnings. The 85 remaining warnings include 54 witnessed by
retained records, 18 additional valid source checks and 13 historical/versioning
findings whose API-version counterparts remain unassessed.

Name/body correspondence is implemented, not value compatibility.
Historical evaluation remains deferred to
[#5875](https://github.com/Azure/typespec-azure/issues/5875).
The retained records cover 97 exact PATCH routes on each side; complete
API-version-aware violation totals and comparable-defect coverage percentages
remain **unassessed**. See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

Swagger compares whole leaf schemas with
[`_.isEqual`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/patch-properties-correspond-to-put-properties.ts#L15-L70).
Harmless documentation, defaults and request/read-only metadata differences
cause 1,132 false missing-property reports, not absent writable inputs.

The first five rows partition all 1,314 Swagger occurrences. The TypeSpec
column counts distinct configured diagnostics for the same source check.
The last three rows partition the 31 findings outside the retained-record join;
**unassessed** means no exact Swagger counterpart is established, not zero.
This is the same diagnostic/suppression policy as section 2.

| Difference (with evidence)                                                                                     | Swagger diagnostics | TypeSpec diagnostics for the same check | analysis                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------- | ------------------: | --------------------------------------: | ------------------------------------------------------------------------------------------------------------------------ |
| [Metadata/request-filtering overchecks](gap-investigation.md#assessed-diagnostic-records)                      |               1,132 |                                       0 | **Do not port:** confirmed Swagger bug, not missing writable inputs.                                                     |
| [Accepted inputs and non-input leaves/wrappers](names-20261117/assessment.md#record-to-warning-bridge)         |                  92 |                                       0 | **Covered acceptance:** keep legitimate partial-input and visibility behavior.                                           |
| [Value/constraint checks](names-20261117/assessment.md#gap-example-deliberately-omitted-constraint-comparison) |                  32 |                                       0 | **Not migrated:** user-approved simplicity/coverage trade-off; no restoration proposed under this policy.                |
| [Authored suppression](names-20261117/assessment.md#report-counting-boundaries)                                |                   1 |                                       0 | **Check covered, capture limited:** Quota's compiler probe confirms suppression; it is not an added captured diagnostic. |
| [Reporting multiplicity](names-20261117/assessment.md#record-to-warning-bridge)                                |                  57 |                                      54 | **Covered:** 57 associations include three across-record repeats; no extra within-record associations.                   |
| [Historical names/availability](count-gap-20261106/analysis.md#historical-versioning)                          |          unassessed |                                      13 | **Deferred/unassessed comparison:** retain the observed source warnings; shared #5875 support is still missing.          |
| [Writable PATCH inputs absent from PUT input](count-gap-20261106/analysis.md#valid-source-checks-to-retain)    |          unassessed |                                      17 | **Retain:** model/API owners should correct unintended writable declarations or confirm the contract.                    |
| [Empty PATCH body](gap-investigation.md#netapp-49-swagger--2-typespec)                                         |                   0 |                                       1 | **Retain:** Swagger sees a body parameter but misses the empty input; request an owner correction.                       |

**Raw-count reconciliation: 1,314 - 85 = 1,132 + 92 + 32 + 1 + 3 - 13 - 17 - 1 = 1,229.**
After the 1,132 confirmed overchecks, the retained-count gap is
**182 - 85 = 97**. There is no unexplained arithmetic residual; historical
semantic correspondence is still unassessed.

The [complete raw project/target inventory](refresh-20261117-names/staging-comparison/differences.md)
and [retained-record project bridges](names-20261117/reconciliation.json)
preserve both directions; opposing differences must not be cancelled into
equivalence. [Grouped assessment and examples](names-20261117/assessment.md)
explain the coverage and proposed actions, not just the totals.

## 4. Function-level coverage

| Behavior                                                         | Result                          | analysis                                                                                                                                                                                                                                                             |
| ---------------------------------------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Extra PATCH names, nested/inherited leaves and encoded names     | Covered                         | Effective writable inputs and inherited operation pairs are checked; [scope and tests](names-20261117/assessment.md#policy-and-complexity).                                                                                                                          |
| Missing/empty PATCH or writable PATCH with no PUT input          | Covered                         | Retain body checks; Quota has probe-only suppression evidence, not an unsuppressed finding; [body evidence](gap-investigation.md#missing-body-correspondence).                                                                                                       |
| Partial inputs and same-position opaque containers               | Covered                         | Compliant controls preserve visibility and encoded-path matching, without checking values; [controls](names-20261117/assessment.md#validation-and-provenance).                                                                                                       |
| Types, formats, bounds, enums, encodings and collection contents | Not migrated                    | User-approved removal loses 19 warnings; 32 retained records remain uncovered; [observed example and impact](names-20261117/assessment.md#gap-example-deliberately-omitted-constraint-comparison).                                                                   |
| Indexed request bodies encountered in evaluated services         | Existing body-policy owner      | `@azure-tools/typespec-azure-resource-manager/use-model-request-body` reports both targeted real-service cases under its separate profile; [probes and limits](gap-investigation.md#existing-rule-coverage-verification). Not additional correspondence diagnostics. |
| Historical names/input shapes and operation availability         | Deferred; comparison unassessed | Shared [#5875 support](https://github.com/Azure/typespec-azure/issues/5875) remains missing; do not reconstruct history locally or credit the deferral as coverage.                                                                                                  |

## NOTES

- **Inputs:** assessed source [`fb7029f43`](https://github.com/Azure/typespec-azure/commit/fb7029f43ef7feaf88a8885070f4775d82e42fff),
  specs `2cd3c5dd6`, core `e06f6b34f` and tooling `688486d1e`;
  [pinned closure, population and execution](refresh-20261117-names/task.json).
  This November 18 report-only refresh reuses the completed November 17 run;
  no new TypeSpec execution or Swagger generation is claimed.
- **Counting evidence:** [record dispositions, full diagnostic identities and both project directions](names-20261117/reconciliation.json);
  [configured observations and exclusion ledger](replay.md#reanalyze-saved-results).
  Predicate/probe evidence is not substituted for captured diagnostics.
- **Validation:** at `fb7029f43`, 76 PATCH tests, clean build/lint/format,
  Chronus, 17 injected, 37 applicable portable and 12 extraction controls,
  both actual ARM-template snippets and
  [all six exact-head Build jobs](refresh-20261117-names/provenance/ci-build-checks.json)
  passed. External Integration was failing and intentionally left unchanged,
  not credited as passing. [Detailed receipts and report-only verification](replay.md).

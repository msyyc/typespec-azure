# PatchPropertiesCorrespondToPutProperties migration

## 1. Scope

The TypeSpec linter
`@azure-tools/typespec-azure-resource-manager/arm-resource-patch` is assessed
against Swagger linter
[`PatchPropertiesCorrespondToPutProperties`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-properties-correspond-to-put-properties.md).
Original migration linter PR: [Azure/typespec-azure#5481](https://github.com/Azure/typespec-azure/pull/5481).

## 2. Coverage

**All 487 ARM project executions succeeded; 0 failed or unrun projects.**
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

**Analysis:** **Assessed coverage:** the original **182 retained Swagger
records** comprise **58 check-covered** (57 reporting records and one
suppression-probed body check), **91 accepted/non-leaf targets**, **one
Informatica wrapper with two related inner-property warnings**, and **32
deliberately not migrated value/constraint records**. Those 32 are coverage
loss, not false positives; removing constraint comparison lost 19 warnings.
The original schema-only assessment excluded another 1,132 Swagger records;
one of them, DataBoxEdge's `id`, shares a genuine TypeSpec warning target and
is shown separately below, without adding another Swagger diagnostic.

The 85 TypeSpec warnings include 54 witnessed by the original retained-record
join, 17 further input-membership checks, one empty-body check and 13 warnings
on declarations removed in the selected Swagger API versions.

Name/body correspondence is implemented, not value compatibility.
Historical evaluation remains deferred to
[#5875](https://github.com/Azure/typespec-azure/issues/5875).
The retained records cover 97 exact PATCH routes on each side. All-version
violation totals and comparable-defect coverage percentages have not been
evaluated; the observed diagnostic counts below are established.
See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

Swagger compares whole leaf schemas with
[`_.isEqual`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/patch-properties-correspond-to-put-properties.ts#L15-L70).
The frozen schema-only assessment excluded 1,132 metadata/request-schema
findings. DataBoxEdge contributes one of those records but also has a genuine
TypeSpec input-membership finding on the same target. Informatica contributes
one of the original 92 accepted/non-leaf records and has two related inner
warnings. Moving these two Swagger records into explicit rows leaves
**1,131 other overchecks and 91 accepted/non-leaf targets**.

Every Swagger and TypeSpec diagnostic is counted once in this table, using
section 2's inclusion/suppression policy. DataBoxEdge's same target has different
triggers; Informatica's wrapper and inner findings have different granularity.
These are observed diagnostic groups, not claims of equivalent defects.
The [group evidence](names-20261117/assessment.md#explicit-frozen-run-groups)
also explains why the historical row is **0 / 13** for the selected API versions.

| Difference (with evidence)                                                                                                               | Swagger diagnostics | TypeSpec diagnostics for the same check | analysis                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------: | --------------------------------------: | ------------------------------------------------------------------------------------------------------------------------------------------- |
| [Other metadata/request-filtering overchecks](gap-investigation.md#assessed-diagnostic-records)                                          |               1,131 |                                       0 | **Do not port:** excludes the DataBoxEdge record shown separately below.                                                                    |
| [Accepted inputs and non-leaf targets](names-20261117/assessment.md#explicit-frozen-run-groups)                                          |                  91 |                                       0 | **Covered acceptance/non-leaf targets:** excludes Informatica's wrapper shown separately below.                                             |
| [Value/constraint checks](names-20261117/assessment.md#gap-example-deliberately-omitted-constraint-comparison)                           |                  32 |                                       0 | **Not migrated:** user-approved simplicity/coverage trade-off; no restoration proposed under this policy.                                   |
| [Authored suppression](names-20261117/assessment.md#report-counting-boundaries)                                                          |                   1 |                                       0 | **Check covered, capture limited:** Quota's compiler probe confirms suppression; it is not an added captured diagnostic.                    |
| [Reporting multiplicity](names-20261117/assessment.md#record-to-warning-bridge)                                                          |                  57 |                                      54 | **Covered:** 57 associations include three across-record repeats; no extra within-record associations.                                      |
| [Historical declarations absent from selected API versions](names-20261117/assessment.md#historical-declarations-0-swagger--13-typespec) |                   0 |                                      13 | **Version-selection difference:** all 13 declarations were removed at the selected versions; #5875 remains deferred.                        |
| [Additional writable PATCH inputs](names-20261117/assessment.md#additional-input-membership-groups)                                      |                   0 |                                      14 | **Retain:** Automation 6, ServiceFabric 6, BillingTrust 1 and OffAzure 1; owner correction or contract confirmation needed.                 |
| [DataBoxEdge `edgeProfile.subscription.id`](names-20261117/assessment.md#databoxedge-1-swagger--1-typespec)                              |                   1 |                                       1 | **Same target, different triggers:** Swagger compares descriptions; TypeSpec rejects a writable PATCH input under a Read-only PUT ancestor. |
| [Informatica organization body](names-20261117/assessment.md#informatica-1-swagger--2-typespec)                                          |                   1 |                                       2 | **Different granularity:** one outer `properties` warning versus two inner-property warnings; retain the precise checks.                    |
| [Empty PATCH body](gap-investigation.md#netapp-49-swagger--2-typespec)                                                                   |                   0 |                                       1 | **Retain:** Swagger sees a body parameter but misses the empty input; request an owner correction.                                          |

**Raw-count reconciliation: 1,314 - 85 = 1,131 + 91 + 32 + 1 + 3 - 13 - 14 + 0 - 1 - 1 = 1,229.**
DataBoxEdge contributes zero to the gap; Informatica contributes minus one.
The original retained-record bridge remains **182 - 85 = 97**.
No diagnostic is added or discarded by this regrouping.

The [complete raw project/target inventory](refresh-20261117-names/staging-comparison/differences.md)
and [retained-record project bridges](names-20261117/reconciliation.json)
preserve both directions; opposing differences must not be cancelled into
equivalence. [Grouped assessment and examples](names-20261117/assessment.md)
explain the coverage and proposed actions, not just the totals.

## 4. Function-level coverage

| Behavior                                                         | Result                     | analysis                                                                                                                                                                                                                                                             |
| ---------------------------------------------------------------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Extra PATCH names, nested/inherited leaves and encoded names     | Covered                    | Effective writable inputs and inherited operation pairs are checked; [scope and tests](names-20261117/assessment.md#policy-and-complexity).                                                                                                                          |
| Missing/empty PATCH or writable PATCH with no PUT input          | Covered                    | Retain body checks; Quota has probe-only suppression evidence, not an unsuppressed finding; [body evidence](gap-investigation.md#missing-body-correspondence).                                                                                                       |
| Partial inputs and same-position opaque containers               | Covered                    | Compliant controls preserve visibility and encoded-path matching, without checking values; [controls](names-20261117/assessment.md#validation-and-provenance).                                                                                                       |
| Types, formats, bounds, enums, encodings and collection contents | Not migrated               | User-approved removal loses 19 warnings; 32 retained records remain uncovered; [observed example and impact](names-20261117/assessment.md#gap-example-deliberately-omitted-constraint-comparison).                                                                   |
| Indexed request bodies encountered in evaluated services         | Existing body-policy owner | `@azure-tools/typespec-azure-resource-manager/use-model-request-body` reports both targeted real-service cases under its separate profile; [probes and limits](gap-investigation.md#existing-rule-coverage-verification). Not additional correspondence diagnostics. |
| Historical names/input shapes and operation availability         | Deferred                   | The 13 observed source targets are absent from the selected Swagger versions. Shared [#5875 support](https://github.com/Azure/typespec-azure/issues/5875) is still needed for all-version evaluation; the zero is not proof of historical coverage.                  |

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
  passed. The recorded External Integration job failed; the separate consumer
  proposal below is not credited as passing CI.
  [Detailed receipts and report-only verification](replay.md).
- **Companion suppression proposal:** draft
  [Azure/azure-rest-api-specs#48325](https://github.com/Azure/azure-rest-api-specs/pull/48325)
  preserves existing PATCH contracts using 62 annotations across 25 files.
  [CI causality, pins, full attribution and exclusions](companion-20261118/analysis.md)
  account for 73 raw / 72 distinct confirmed compatibility findings; 13 unresolved
  historical-versioning findings remain unsuppressed. The consumer CI SHA is
  history-reconstructed with verbatim source checks, not directly logged.
  No local consumer validation or Swagger generation was run; this is a proposal,
  not a green-CI or landing outcome. The 1,314 / 85 coverage counts above remain
  the original frozen assessment, not post-suppression measurements.

- **Private consumer proposal:** published; details retained privately. This is
  an inspection-only proposal, not a passing-CI or landing outcome.

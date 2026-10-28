# PathContainsResourceGroup migration

## 1. Conclusion and scope

The opt-in ARM rule
`@azure-tools/typespec-azure-resource-manager/resource-group-path-parameter`
detects the original resource-group path problem on supported native operations,
including standard ARM templates with custom base parameters. The full comparison
assessed **487 projects without failures**. Both engines identified the same three
projects. All **31 comparable HTTP operation units match**, without missing or
extra units.

**No TypeSpec rule update is required by these results.** The implementation
matches the audited ARM path policy. This is a scoped functional-equivalence
conclusion, not proof for every future spec, API version, or execution policy.
The [automatic report](runs/full-native-01/coverage.md) correctly retains
`equivalence: not-determined`.

The comparison uses production ARM/OAS2 Swagger from the
[frozen baseline](evidence-details.md#frozen-inputs), and explicitly enabled native
linting on the same frozen specs with the candidate compiler/library closure.
Swagger selects the latest emitted version; native collection uses the source
program. A separate selected-version HTTP audit checks every affected operation.
It is **not** a projected-linter rerun. Original Swagger severity is error; native
severity is warning. Native defaults remain disabled and default activation was
not measured by the target-only corpus run.

## 2. Actual coverage

| Measure                                                | Observed result |
| ------------------------------------------------------ | --------------: |
| Selected / assessed / failed or unassessed projects    |   487 / 487 / 0 |
| Swagger / native / overlapping affected projects       |       3 / 3 / 3 |
| Swagger-only / native-only projects                    |           0 / 0 |
| Raw Swagger / raw and aligned native findings          |         43 / 31 |
| File-independent Swagger paths / native source targets |         15 / 31 |
| Comparable Swagger / native operation units            |         31 / 31 |
| Missing / extra comparable units                       |           0 / 0 |

Raw records, JSON paths, source targets, and HTTP operations are different units.
Raw diagnostic correspondence is not one-to-one. The comparable unit is the exact
project, case-preserved full path, and eligible HTTP method. Native diagnostics
bind to operation objects; reference collapse requires a unique exact Swagger
owner and verified local reference chains. Eight controls reject missing methods,
wrong-but-equal totals, ambiguous owners, and path/project collisions.

See the [full per-project audit](receipts/step8-operation-comparison-full.json)
and [normalization method](evidence-details.md#comparison-method).
Neither project overlap nor ratios between raw counts measure functional coverage.

## 3. Function-level coverage

The six audited behavior families below are covered. This denominator describes
the reviewed contract, not all possible TypeSpec programs or production prevalence.

| Audited family                    | Evidence and status                                                                                           |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Eligible CRUD operations          | Covered: GET, PUT, PATCH, DELETE; POST and HEAD compliant exclusions                                          |
| Standard and custom ARM templates | Covered: wrong/literal custom bases fail; default and retained standard parameters pass                       |
| Full-path predicate               | Covered: missing/wrong/literal parameters, case-insensitivity, canonical occurrence, segment-prefix exclusion |
| Serialized path identity          | Covered: both directions of `@path` name overrides                                                            |
| Audience and authored targets     | Covered: non-ARM exclusion, mixed services, concrete generic operations/interfaces, per-operation reporting   |
| Activation and suppression        | Covered: disabled registration/rulesets, explicit activation, inherited options, authored suppression         |

The native suite has 25 rule cases and five registration checks. Broader evidence
includes 671 ARM package tests, nine ruleset tests, 37 injected-package controls,
75 harness tests, and eight comparison controls. These counts are not weighted
behavior percentages. [Validation receipts and limits](evidence-details.md#validation)
retain failed drafts and disclosed unrelated typecheck errors.

## 4. Why diagnostic counts differ

| Project / cause                                                                                       | Raw Swagger / native | Comparable units | Disposition                                        |
| ----------------------------------------------------------------------------------------------------- | -------------------: | ---------------: | -------------------------------------------------- |
| [Advisor: ordinary wrong parameter](evidence-details.md#advisor-direct-route)                         |                2 / 2 |            2 / 2 | Same two operations                                |
| [DataMigration: several methods per path](evidence-details.md#datamigration-method-multiplicity)      |              11 / 26 |          26 / 26 | One Swagger path finding covers several operations |
| [Network: repeated reference-linked observations](evidence-details.md#network-reference-multiplicity) |               30 / 3 |            3 / 3 | Two exact paths cover three operations             |

Raw Swagger-higher excess is **27**; native-higher excess is **15**. Total absolute
difference is **42**, not the net difference of 12. Raw counts agree in 485
projects, including the 484 projects with no findings. Comparable counts agree
in all 487 projects. There are no unexplained operation-unit residuals.
Network retains 28 `input-fallback` observations and two reported observations.
Ownership inferred for fallback records remains derived, not reported provenance.

## 5. Examples and required action

The verified standard-template example replaces the usual resource-group base:

```typespec
model CustomBase {
  ...CommonTypes.ApiVersionParameter;
  ...CommonTypes.SubscriptionIdParameter;
  @path @segment("resourceGroups") groupName: string;
}
```

Using this base in `ArmResourceRead<Widget, BaseParameters = CustomBase>` produces
one native warning. Using `ArmResourceRead<Widget>` produces none. Both actual
documentation snippets compile without errors. Real
[DataMigration](evidence-details.md#datamigration-method-multiplicity) and
[Network](evidence-details.md#network-reference-multiplicity) examples show why
raw count equality would be misleading.

No additional production rule or fixture change is indicated. Enablement remains
an explicit policy choice, not an automatic migration side effect. Exact input
recovery and saved-observation reanalysis are documented in
[replay instructions](evidence-details.md#recovery-and-replay); a complete fresh
compiler/emitter rerun is distinct from that replay and is not claimed.

A fresh published-evidence checkout verified all 524 receipt hashes, downloaded
and restored all 40 input assets, and reproduced the complete 487-project report
exactly. The [replay receipt](receipts/fresh-replay.json) records the verified
historical archive and the 12 documents extracted for numerical replay only.

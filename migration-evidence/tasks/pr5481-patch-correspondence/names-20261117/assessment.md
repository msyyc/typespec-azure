# Name-only PATCH correspondence

## Policy and complexity

The approved update removes the entire 132-line
`arm-resource-patch-compatibility.ts` helper and its incompatible-property
diagnostic. PUT leaf inventory is now a set of writable encoded names.
There is no replacement comparator or compiler-assignability check.

`@azure-tools/typespec-azure-resource-manager/arm-resource-patch` retains paired
endpoint/body checks, inherited operations, request visibility, encoded names,
finite same-position lookup for opaque object containers, recursive termination,
diagnostic deduplication and its original ARM resource-model/tags checks.
Rule identity, severity and default activation are unchanged.

Matching names do **not** prove value compatibility. Types, formats, bounds,
enum values, encodings and nested collection contents are outside the approved
scope. This is intentionally partial migration, not full Swagger equivalence.

## Actual diagnostic effect

The final candidate is
[`fb7029f43`](https://github.com/Azure/typespec-azure/commit/fb7029f43ef7feaf88a8885070f4775d82e42fff).
The fresh full-population observation covers all **487 projects**:
**104 -> 85 warnings**, exactly **19 removed, 0 added**. The surviving findings
are **83 missing-name**, **one empty-body** and **one missing-body** warning.
All surviving complete diagnostic records match the preceding candidate,
including their locations and duplicate occurrences.

| Removed check             | Warnings | Projects                                             |
| ------------------------- | -------: | ---------------------------------------------------- |
| String-length constraints |        6 | API Management (2), Automation (3), NetworkCloud (1) |
| Minimum item count        |       10 | ManagedNetworkFabric                                 |
| Numeric bounds            |        1 | RegistryTasks                                        |
| ARM resource-ID format    |        2 | AppService                                           |

These are deliberately lost checks, not newly confirmed false positives.
The [raw diagnostic delta](../refresh-20261117-names/candidate-delta.json)
and [reconciliation](reconciliation.json) preserve every occurrence.

## Deliberately omitted value checks

The 19 removed warnings supported **26 retained Swagger records**. Together with
the **six previously omitted deep-value records**, this leaves **32 records
outside the approved policy**. The six old records are unchanged; they are not
six additional removed warnings in this update.

The [newly omitted record list](reconciliation.json) identifies each project,
diagnostic index, route and reported name. Its `allOmittedValueRecords` also
retains the preceding six records. None of these 32 is credited as compatible
or reclassified as a Swagger false positive merely because the native predicate
now accepts its names.

## Record-to-warning bridge

The immutable Swagger observations still contain **1,314 diagnostics**.
The previous source investigation confirmed **1,132 metadata/request overchecks**;
the remaining **182 records** are all assessed:

| Disposition                                             | Retained records | Distinct configured warnings |
| ------------------------------------------------------- | ---------------: | ---------------------------: |
| Reporting name/body checks                              |               57 |                           54 |
| Authored suppression                                    |                1 |                            0 |
| Legitimate accepted inputs or non-input leaves/wrappers |               92 |                            0 |
| Deliberately not migrated value/constraint checks       |               32 |                            0 |
| Total                                                   |              182 |                           54 |

The 57 reporting records have **57 warning associations**, with **three
across-record repeats** and **no extra within-record associations**.
There are **31 warnings outside that join**: 17 valid writable-PATCH-not-PUT,
one valid empty-body check and 13 historical/versioning findings deferred to
[#5875](https://github.com/Azure/typespec-azure/issues/5875).
Their exact diagnostic identities and prior source classifications are
preserved, not rematched by property name or message text.

**182 - 85 = 92 + 32 + 1 + 3 - 31 = 97.**

All [per-project bridges](reconciliation.json) remain available, including both
gap directions. Source inspection covers 97 exact retained routes on each side;
route counts are not counts of proven equivalent defects.

At project level, **39 have more retained Swagger records**, **six have more
TypeSpec warnings** and **442 have equal counts**. The directional excesses are
**110 / 13**, giving a **97 net difference** but **123 absolute project gap**.
Signed, absolute and relative count differences are retained for every project;
these are not defect-coverage percentages.

## Report counting boundaries

The November 18 report refresh reuses the same November 17 execution and source
identity. Its scorecard contains **1,314 original Swagger diagnostic occurrences
and 85 configured TypeSpec diagnostic occurrences**, without normalization.
All 85 findings are name/body checks in the assessed source-input policy;
none is removed just because its historical counterpart is unestablished.
The original ARM resource-model/tags checks contribute no additional diagnostic
family to these 85. The 13 historical-name/availability findings stay in the
observed total, with historical correspondence unassessed under #5875.

**Suppression evidence is not a captured diagnostic total.** In the 51
retained-record projects, the extractor found Quota's absent-body predicate
and separately called the public compiler's `program.reportDiagnostic` with a
constructed diagnostic. The compiler suppressed that probe. The
[current source capture](../refresh-20261117-names/source-attribution/source-38.json)
records `compilerSuppressed: true`, `configuredWarning: false` and no warning
index. This establishes implemented check/suppression behavior, not an actual
registered-linter callback capture. Thus the report adds **zero captured
suppressed diagnostics**, not an invented 86th finding. An exhaustive
suppression-inclusive total across all 487 projects is **unassessed**.
The one suppression-probed record remains part of the 58 check-covered records,
not part of the 57 reporting records.

The separate
[`use-model-request-body` probes](../body-assessment-20261106/owner-probes.json)
explicitly enable that additional rule and observe two targeted real-service
body-shape warnings. They diagnose indexed ARM request roots, not property
correspondence or suppressed instances of this Swagger check, so they are
not added to the 85. Other ambient/probe findings and synthetic controls are
likewise not corpus correspondence diagnostics. See the
[exact profiles and sources](../gap-investigation.md#corpus-scope-and-reproducibility).

The main report's raw-count equation is
**1,314 - 85 = 1,132 + 92 + 32 + 1 + 3 - 13 - 17 - 1 = 1,229**.
The terms respectively identify confirmed overchecks, legitimate accepted/
non-input records, deliberately omitted checks, the suppression-probed record,
repeated record-to-warning associations, historical source findings, valid
additional input-membership findings and the valid additional empty-body finding.
There is no arithmetic residual; that does not resolve historical semantics.
The [complete raw differing-project/target inventory](../refresh-20261117-names/staging-comparison/differences.md)
and [182-record/project reconciliation](reconciliation.json) preserve individual
occurrences, opposing directions, signed/absolute/relative gaps and exact targets.

### Gap example: deliberately omitted constraint comparison

- **Classification:** Swagger-linter-only; **status:** user-approved policy difference.
- **Project/source:** API Management, `LoggerContractProperties` and
  `LoggerUpdateParameters` in pinned
  [`models.tsp`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/models.tsp#L7634-L7686).
  The source-input run does not select an API version; the original emitted
  operation/version identities remain in the linked Swagger inventory.

**TypeSpec source excerpts**

```typespec
// PUT: LoggerContractProperties
@maxLength(256)
description?: string;

// PATCH: LoggerUpdateParameters
description?: string;
```

The [saved resolved Swagger leaves](../compatibility-20261105/retained-schemas.json)
are `{"type":"string","maxLength":256}` and `{"type":"string"}`.

| Engine          | Observed result                                                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Swagger linter  | 2 records, for Logger and WorkspaceLogger, because the whole same-named schemas differ.                                                                 |
| TypeSpec linter | 0 warnings for this constraint check at `fb7029f43`; the single shared warning at `models.tsp:7686:3` is present in the exact removed-diagnostic delta. |

**Explanation:** the name-only policy does not compare `maxLength`, so values
longer than 256 are no longer checked. The
[exact delta](../refresh-20261117-names/candidate-delta.json) and
[26 newly omitted record identities](reconciliation.json) distinguish the
19 removed warnings from their 26 record associations; six other deep-value
records were already omitted.

**Coverage status:** this is deliberate missing value coverage, not a harmless
metadata difference or compatible contract.

**Gap analysis and decision:** the user approved removing value/constraint
comparison to reduce complexity. No restoration is proposed under that policy;
reviewers retain the broader migration-acceptance decision. Existing
[metadata/request examples](../gap-investigation.md#assessed-diagnostic-records),
[accepted-shape examples](../gap-investigation.md#why-81-schema-contexts-correctly-accept),
[historical source examples](../count-gap-20261106/analysis.md#historical-versioning),
[valid additional input checks](../count-gap-20261106/analysis.md#valid-source-checks-to-retain)
and [the empty-body source/schema trace](../gap-investigation.md#netapp-49-swagger--2-typespec)
explain the other material causes. Their dated executions are not relabeled
as new runs; only the unchanged source predicates/count classifications are reused.

## Validation and provenance

| Acceptance claim                                                      | Layer and evidence                                                                                                                                                          |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Same names are accepted despite different types/formats/bounds        | Canonical `patch-operations.test.ts`, `checks names without comparing property constraints or value types`; expected-red before removal, now green.                         |
| Name/body/path/visibility/inherited-operation behavior remains intact | The same canonical suite, 76 passing tests; no relocated or second per-rule suite.                                                                                          |
| Actual registered execution, opt-in and presets remain unchanged      | Injected receipts `configured-disabled`, `arm-all-activation`, `resource-manager-activation` in [17 controls](../refresh-20261117-names/controls/injected-controls.json).   |
| Authored suppression still hides a real missing-name violation        | Injected `missing-name` / `suppressed-missing-name` pair plus [extraction/suppression probes](../refresh-20261117-names/source-attribution/controls/summary.json).          |
| Published ARM examples retain their diagnostic contrast               | [Actual authored-document receipts](../refresh-20261117-names/controls/documentation-examples.json), not copied TypeSpec or a new Markdown parser.                          |
| Corpus reduction and partial Swagger coverage                         | [Fresh full-run observations](../refresh-20261117-names/runs/full-corpus/manifest.json), the 51 bound source captures and [182-record reconciliation](reconciliation.json). |

The old direct-constraint solver cases are removed because their predicate is
deliberately no longer implemented, not relocated into another rule suite.
A focused explicit-reset case remains. No framework-only test suite or new
production special case replaces the removed comparator.

- The new ignored-constraint regression first failed against the old candidate
  with four unwanted format/length/item/numeric diagnostics; it passes after
  removal. All **76 canonical PATCH tests**, root format/lint, the clean ARM
  dependency build and Chronus verification passed.
- **17 injected controls** preserve violating/compliant names, body/path checks,
  actual missing-name suppression and explicit/default/preset activation.
  Four constraint-difference controls now correctly expect no warning.
- **37 applicable portable controls** passed. Six unrelated resource-group-rule
  fixtures were explicitly excluded before execution because their unmerged
  rule is not part of this candidate; they are not counted as passes.
- Both actual published ARM-template Incorrect/Correct snippets were extracted
  through the website Markdown AST and compiled unchanged. The incorrect one
  reports only the PATCH-only `extra`; its correction reaches the same check
  without that violation.
- **12 extraction controls** passed, including suppressed missing-name and opaque
  container/path cases. The installed production collector/path helpers are
  used without modifying their behavior. The extractor tests candidate presence
  only and explicitly does not evaluate value compatibility.
- All **51 retained-record projects** were captured against the final installed
  artifacts. Their configured diagnostic arrays equal the full-run arrays
  exactly, including order. All 182 record dispositions are accounted for.
- A complete CLI manifest, package/source hashes, all 15 archives and their
  members, built/packed/installed selected-rule equality and runtime entrypoint
  receipts bind this candidate to its execution. The deleted helper is absent
  from the packed ARM package.
- The packed `arm-resource-patch.js`, `use-model-request-body.js` and
  `model-utils.js` bytes are unchanged from the preceding candidate. Earlier
  separate owning-rule probes still apply; they are not added to this rule's
  warning totals.
- All [six exact-head CI Build jobs](../refresh-20261117-names/provenance/ci-build-checks.json)
  passed. External integration is left unchanged as requested.

Core remains `e06f6b34fdad9d7f49bfc084a598b03c60684e9a`; the actual tooling
revision is `688486d1e9a1701c34fc912c01705d098625c2a3`.
Frozen specs, Swagger baseline and evaluated staging supplement are unchanged.
No Swagger was generated. See [replay instructions](../replay.md).

The [November 12 assessment](../direct-20261112/assessment.md) and earlier
observations remain immutable historical evidence; their direct-constraint
coverage is not a claim about this candidate.

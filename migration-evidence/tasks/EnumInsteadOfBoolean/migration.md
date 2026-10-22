# EnumInsteadOfBoolean migration report

## 1. Conclusion and scope

**Standard Boolean checks are covered, with broad real-project overlap.**
The native `@azure-tools/typespec-azure-core/no-boolean` rule covers ordinary
Boolean properties, parameters and direct bodies. It detects findings in
**312 of the 313 Swagger-affected projects (99.68%)**, supporting the migration
approach.

The remaining semantic gaps are five Boolean representation corner cases,
not absence of the core check. Full Swagger parity requires addressing these
cases and retaining validation for opaque external JSON. The evidence supports
the standard-case behavior, not yet complete replacement.

This compares `EnumInsteadOfBoolean` with the official native rule on production
ARM APIs, using each project's latest emitted API version in the frozen snapshot.
Native activation was forced for analysis; production defaults remain unchanged.
[Frozen inputs and policies](evidence-details.md#mapping-and-frozen-inputs).

## 2. Actual coverage

| Measure                                           |                 Result |
| ------------------------------------------------- | ---------------------: |
| Projects assessed / selected; execution failures  |       **487 / 487; 0** |
| Swagger diagnostic events                         |              **8,338** |
| Native findings: raw / aligned to emitted API     |      **4,823 / 4,680** |
| Swagger-affected projects also detected by native | **312 / 313 (99.68%)** |
| Swagger-only / native-only projects               |              **1 / 0** |

**99.68% is project overlap, not functional equivalence.** Swagger events and
native semantic targets are different counting units; `4,680 / 8,338` is not
diagnostic coverage. Exact matched-diagnostic coverage remains **unassessed**:
4,069 Swagger events lack document attribution.

[Full results](runs/full-4/coverage.md) |
[Independent counts and all 487 project rows](runs/full-4/audit/project-counts.csv).

## 3. Function-level coverage

**Core behavior is covered; the targeted corner-case audit exposes five gaps.**
The five passing native tests cover ordinary Boolean model properties, path
parameters, request bodies, response bodies and a compliant string union.

The separate six-shape stress test detects **1 / 6 representations (16.7%)**.
It deliberately tests alternatives to a direct Boolean scalar; its equally
weighted cases are **not a production coverage estimate**. "Corner case"
describes representation, not proven rarity. Nullable and dictionary forms
occur in real specs; their overall frequency remains unmeasured.

All six shapes compile and emit Boolean schemas. **Compiler-prevented: 0;
approved retirements: 0; unassessed within this inventory: 0.**

| Audited behavior            | Native / Swagger findings | Result and example                                                                    |
| --------------------------- | ------------------------: | ------------------------------------------------------------------------------------- |
| Standard `boolean` property |                     1 / 1 | [Core case covered](evidence-details.md#semantic-and-activation-evidence)             |
| Boolean literal `true`      |                     0 / 1 | [Corner case: literal type](evidence-details.md#gap-example-boolean-literal)          |
| Nullable `boolean \| null`  |                     0 / 1 | [Corner case: union type](evidence-details.md#gap-example-nullable-boolean)           |
| Derived Boolean scalar      |                     0 / 1 | [Corner case: scalar subtype](evidence-details.md#gap-example-derived-boolean-scalar) |
| `boolean[]` item            |                     0 / 1 | [Corner case: array element](evidence-details.md#gap-example-array-item)              |
| `Record<boolean>` value     |                     0 / 1 | [Corner case: dictionary value](evidence-details.md#gap-example-dictionary-value)     |

The compliant string-union control is accepted by both engines. A Delete-only
property omitted from GET output is correctly excluded from aligned findings.
[Compiled controls and results](controls/results.json) |
[Source, predicates and surface tests](evidence-details.md#semantic-and-activation-evidence).

## 4. Why diagnostic counts differ

Raw per-project differences total **4,037 Swagger-higher events and 379
native-higher findings**. Opposing differences must not cancel.
The examples below explain distinct causes, not a complete count partition.

| Cause                                                                                                                         | Verified observation                                                            | Disposition                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| [Reference traversal](evidence-details.md#gap-example-reference-traversal-multiplies-validator-observations)                  | SQL: 2,224 Swagger events / 157 native findings                                 | Preserve events; missing source attribution prevents exact target assignment.                     |
| [Native target multiplicity](evidence-details.md#gap-example-the-largest-native-higher-outlier-has-distinct-semantic-targets) | Billing: 75 / 145; independent traversal confirms 145 distinct property objects | Not duplicate rule execution; do not merge distinct targets sharing a location.                   |
| [External JSON boundary](evidence-details.md#gap-example-an-opaque-external-swagger-model-has-no-native-property)             | BatchPricingsAPI: 2 / 0                                                         | Boolean field exists only in referenced JSON; retain Swagger validation.                          |
| [Removed source declaration](evidence-details.md#gap-example-an-older-version-boolean-is-not-emitted)                         | Advisor: native raw 3 becomes aligned 2; Swagger 2                              | Correct version exclusion of one native finding, not evidence that Swagger misses can be ignored. |

**No findings were waived as obsolete.** Swagger was freshly generated from the
same frozen specs, not borrowed from an old legacy report. Retiring a requirement
would need an explicit policy decision or version-removal proof for that target.
Unresolved correspondence remains visible; no blanket normalization is claimed.
[Code-backed explanations and residuals](evidence-details.md#real-service-cardinality-and-projection-examples).

## 5. Examples and required action

**Working core check (compiled control):**

```typespec
plain: boolean;
```

Both engines report one finding for its emitted `{"type":"boolean"}` schema.
[Source, output and paired results](evidence-details.md#semantic-and-activation-evidence).

**Machine Learning, `2026-09-01`:** `Docker.privileged` remains authorable:

```typespec
privileged?: boolean | null;
```

It emits `{"type":"boolean","x-nullable":true}`. Swagger flags it; native does
not. Its suppression targets `no-nullable`, not `no-boolean`.
[Exact source and schema](evidence-details.md#gap-example-a-real-nullable-boolean-is-missed).

**Purview, `2024-04-01-preview`:** `BatchFeatureStatus.features` uses:

```typespec
features?: Record<boolean>;
```

The emitted `additionalProperties.type` is `boolean`. Swagger flags that value;
native does not. Its suppression targets `arm-no-record`, not `no-boolean`.
[Exact source and schema](evidence-details.md#gap-example-a-real-boolean-dictionary-value-is-missed).

The five corner-case links in section 3 each open a small source/schema example
with the observed engine behavior. The two real-service examples above show
why these cases remain relevant, despite the positive standard-case results.

For full parity, update the production rule and its tests for the five missing
representations, preserving compliant controls and avoiding duplicate warnings.
[Required production changes](evidence-details.md#required-typespec-rule-changes).
An approved narrower policy would support a scoped conclusion, not strict
legacy equivalence. This report changes neither the rule nor its enablement.

[Reproduction instructions](evidence-details.md#reproduce-the-recorded-comparison) |
[Preserved specs source](evidence-details.md#preserved-specs-source) |
[Assets and verification receipt](publication.json).
Local baseline reuse and download-only analysis replay are verified; full
fresh-machine CLI regeneration remains unverified.

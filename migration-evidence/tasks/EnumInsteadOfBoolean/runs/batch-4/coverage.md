# Native TypeSpec coverage analysis

Validators: `EnumInsteadOfBoolean`
Native rules: `@azure-tools/typespec-azure-core/no-boolean`
Scope: `boolean-http`; partial: true.

**This is observed coverage, not an automatic equivalence decision.**
Primary counting unit: sum of raw member validator occurrences versus aligned native diagnostics, counted once.
Member-native attribution is unavailable. Test every member's semantics, including members with no observations.
Cross-validator overlap is not normalized. Equal source locations do not establish one actionable grouped violation.
JSON paths and source locations are different identity domains. One-sided projects and outliers require investigation.
Aligned diagnostics are source diagnostics filtered by locations in the selected-version HTTP graph, not a rerun of arbitrary rule predicates on a projected program.

| Measure | Value |
| --- | ---: |
| Selected / assessable projects | 1 / 1 |
| Unassessed projects | 0 |
| Validator / native / overlap projects | 1 / 0 / 0 |
| Observed validator-project coverage | 0 |
| Validator raw / file-independent paths | 2 / 1 |
| Native raw / aligned / source targets | 0 / 0 / 0 |
| Native findings under project defaults | 0 |
| Validator excess / native excess | 1 / 0 |
| Raw validator excess / raw native excess (primary) | 2 / 0 |

## Member observations (not member-native coverage)

- EnumInsteadOfBoolean: 2 raw observations; completeness not determined.

## One-sided projects

- Validator only: `specification/security/resource-manager/Microsoft.Security/Security/BatchPricingsAPI`

## Unassessed projects


## Diagnostic outliers

| Project | Validator raw | Native aligned | Raw difference | Validator paths | Native targets | Location difference |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| specification/security/resource-manager/Microsoft.Security/Security/BatchPricingsAPI | 2 | 0 | 2 | 1 | 0 | 1 |

# Native TypeSpec coverage analysis

Validators: `PathContainsResourceGroup`
Native rules: `@azure-tools/typespec-azure-resource-manager/resource-group-path-parameter`
Scope: `source`; partial: false.

**This is observed coverage, not an automatic equivalence decision.**
Primary counting unit: sum of raw member validator occurrences versus aligned native diagnostics, counted once.
Member-native attribution is unavailable. Test every member's semantics, including members with no observations.
Cross-validator overlap is not normalized. Equal source locations do not establish one actionable grouped violation.
JSON paths and source locations are different identity domains. One-sided projects and outliers require investigation.
Source diagnostics include all declared versions; Swagger uses the latest emitted API version.

| Measure | Value |
| --- | ---: |
| Selected / assessable projects | 487 / 487 |
| Unassessed projects | 0 |
| Validator / native / overlap projects | 3 / 3 / 3 |
| Observed validator-project coverage | 100 |
| Validator raw / file-independent paths | 43 / 15 |
| Native raw / aligned / source targets | 31 / 31 / 31 |
| Native findings under project defaults | not assessed |
| Validator excess / native excess | 0 / 16 |
| Raw validator excess / raw native excess (primary) | 27 / 15 |

## Member observations (not member-native coverage)

- PathContainsResourceGroup: 43 raw observations; completeness not determined.

## One-sided projects


## Unassessed projects


## Diagnostic outliers

| Project | Validator raw | Native aligned | Raw difference | Validator paths | Native targets | Location difference |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| specification/network/resource-manager/Microsoft.Network/Network/Network | 30 | 3 | 27 | 2 | 3 | -1 |
| specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration | 11 | 26 | -15 | 11 | 26 | -15 |

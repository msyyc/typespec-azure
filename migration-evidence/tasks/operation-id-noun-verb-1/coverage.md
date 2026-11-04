# Native TypeSpec coverage analysis

Validators: `OperationIdNounVerb`
Native rules: `@azure-tools/typespec-client-generator-core/no-redundant-operation-group-name`
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
| Validator / native / overlap projects | 35 / 37 / 35 |
| Observed validator-project coverage | 100 |
| Validator raw / file-independent paths | 265 / 122 |
| Native raw / aligned / source targets | 123 / 123 / 123 |
| Native findings under project defaults | not assessed |
| Validator excess / native excess | 4 / 5 |
| Raw validator excess / raw native excess (primary) | 147 / 5 |

## Member observations (not member-native coverage)

- OperationIdNounVerb: 265 raw observations; completeness not determined.

## One-sided projects

- Native only: `specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization`
- Native only: `specification/fileshares/resource-manager/Microsoft.FileShares/FileShares`

## Unassessed projects


## Diagnostic outliers

| Project | Validator raw | Native aligned | Raw difference | Validator paths | Native targets | Location difference |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| specification/network/resource-manager/Microsoft.Network/Network/Network | 154 | 11 | 143 | 11 | 11 | 0 |
| specification/fileshares/resource-manager/Microsoft.FileShares/FileShares | 0 | 4 | -4 | 0 | 4 | -4 |
| specification/network/resource-manager/Microsoft.Network/Network/Vmss | 5 | 3 | 2 | 5 | 3 | 2 |
| specification/billing/resource-manager/Microsoft.Billing/Billing | 5 | 4 | 1 | 5 | 4 | 1 |
| specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization | 0 | 1 | -1 | 0 | 1 | -1 |
| specification/resources/resource-manager/Microsoft.Resources/resources | 4 | 3 | 1 | 4 | 3 | 1 |

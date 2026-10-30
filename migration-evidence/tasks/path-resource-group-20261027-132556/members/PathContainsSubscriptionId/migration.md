# PathContainsSubscriptionId migration

## 1. Conclusion and scope

The TypeSpec rule `@azure-tools/typespec-azure-resource-manager/use-scope-path-standard-name` includes
[`PathContainsSubscriptionId`](https://github.com/Azure/azure-openapi-validator/blob/18a7944e7fc3155e8ef1498665465ed5f455f54a/docs/path-contains-subscription-id.md) under the one admitted ARM scope-name policy.
The material naming predicate and compliant controls are covered.
Subscription behavior has discriminating violating/compliant template controls, including B-only and both-wrong; the frozen corpus supplies no positive prevalence evidence. Native source and immutable inputs are published. Separate independent local development/readiness reviews and both distinct Balanced GitHub checkpoints are clean for the unchanged native candidate; see the [shared final review receipts](../../runs/combined-native-20261029-cycle0/reviews/final-review-summary.json).

## 2. Actual coverage

All 487 production ARM projects were assessed without failures. Counts are
individual findings, not project counts; raw TypeSpec attribution to this member
is unassessed, not inferred from messages.

| Count | Swagger linter | TypeSpec linter |
| --- | ---: | --- |
| Reported diagnostics | 0 | Unassessed per member;31 for the combined rule |

## 3. Function-level coverage

| Behavior | Result |
| --- | --- |
| Wrong/missing/literal name; serialized @path name | Covered in canonical semantics and actual injected controls |
| Canonical/absent scope; case-insensitive full-path exception | Covered |
| A-only/B-only/both/neither supported standard templates | Covered; two independent warnings when both fail |
| Audience/method/default activation | Concrete ARM GET/PUT/PATCH/DELETE; one shared opt-in ID |

## 4. Why diagnostic counts differ

See the [combined grouped evidence](../../runs/combined-native-20261029-cycle0/evidence-details.md)
for all differing projects, source/reference multiplicity and exact operation
units. No per-member native diagnostic percentage is fabricated.

## NOTES

Shared immutable baseline, frozen-reference limitations, common activation,
source/artifact identity, controls, full population and completed publication/review
gates are in the [combined report](../../migration.md) and linked appendix.

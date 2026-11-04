# Scoped PATCH correspondence corrections

**Historical validation:** the source-only simplification and current corpus
assessment are recorded in [simplification.md](simplification.md) and
[migration.md](migration.md). Per-version body-removal expectations below
describe the preceding candidate and are no longer the current contract.

Candidate: [`60a56b11d149b5960783e0c18da675d6cceb902e`](https://github.com/Azure/typespec-azure/commit/60a56b11d149b5960783e0c18da675d6cceb902e),
following `7baca4db3d7824c24c30961c50c3f47a6df8d958`.

## Corrections and regression evidence

The canonical behavior suite remains
[`patch-operations.test.ts`](https://github.com/Azure/typespec-azure/blob/60a56b11d149b5960783e0c18da675d6cceb902e/packages/typespec-azure-resource-manager/test/rules/patch-operations.test.ts).
The five changed/new assertions for the two corrections failed against the
previous implementation before the production edits. All 59 cases pass on
the final candidate.

| Claim                                                                      | Rule behavior regression                                              |
| -------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Inherited nested leaves are compared, not opaque wrapper names             | `compares inherited leaves rather than their nested wrapper names`    |
| Read-only direct members do not hide inherited writable PUT leaves         | `finds inherited writable PUT leaves behind read-only direct members` |
| Genuine inherited PATCH-only leaves still produce the property finding     | `reports genuinely missing inherited nested PATCH leaves`             |
| Missing or explicit void PUT input cannot satisfy nonempty PATCH input     | `reports PATCH properties when the PUT body is missing (%s)`          |
| A PUT body removed at a service-version boundary is absent in that version | `recognizes removed explicit put body parameters`                     |

The recursion gate now uses the same inherited JSON-property iterator and
payload filters as leaf collection. Effective overrides, visibility, `never`,
nullable single-model unwrapping and branch-local cycle handling are preserved.
The previously intentional opaque inherited-wrapper behavior is corrected too:
under this existing flattened-leaf policy, equivalent inherited leaves must
not fail merely because their outer wrapper names differ.

An absent/void PUT body supplies no corresponding property names, so each
effective PATCH leaf uses the existing missing-property diagnostic and authored
target/deduplication behavior. An actual but unsupported PUT body is still
skipped rather than interpreted as an empty object. Missing/empty PATCH
validation still takes precedence.

## Native validation and injected integration

Commands ran from the existing candidate worktree:

```powershell
# packages\typespec-azure-resource-manager
pnpm exec vitest run test\rules\patch-operations.test.ts
pnpm run build
pnpm run lint

# Repository root
pnpm -r --filter '@azure-tools/typespec-autorest...' --filter '@azure-tools/typespec-azure-rulesets...' --filter '@typespec/integration-tester...' build
pnpm exec chronus verify

# packages\samples
pnpm exec vitest run
```

Results: **59 rule tests and 40 sample compilation/snapshot tests passed**.
ARM and the public dependency closure built successfully. ARM lint, changed-file
Prettier checks, Chronus verification and `git diff --check` passed.
An independent read-only review of the four-file correction found no
significant issues. The existing unreleased feature entry was updated rather
than adding a redundant release entry.

The final 15-package public closure was built and packed from the clean
candidate/core checkout, then injected into the isolated frozen specs runtime.
**14 selected-rule injected controls passed**, including extra-leaf rejection,
compliant subset, same-name/different-type acceptance, empty PATCH, authored
suppression, explicit activation despite configuration disablement, both
existing presets, absent PUT, void PUT, unsupported PUT, inherited PUT,
genuinely missing inherited PATCH leaf, and read-only PUT discriminator.
These exercise the registered linter, not only the raw helper.

The applicable portable harness passed **37 cases**; **6 fixtures requiring
the unrelated, absent `resource-group-path-parameter` rule were excluded
explicitly**, not counted as passes. No missing rule was added to this PR.
See the refresh's saved control receipts and portable log.

## Deliberately unchanged policies

- Historical names and nested types remain a known limitation, temporarily
  accepted for this migration under [#5875](https://github.com/Azure/typespec-azure/issues/5875).
  There is no rule-local snapshot implementation or claim that historical
  shapes are now reconstructed.
- BillingTrust does not require a TypeSpec linter visibility/discriminator fix.
  Its PUT `kind` has `@visibility(Lifecycle.Read)`, while PATCH's is request-visible.
  A shared emitted schema retaining a `readOnly: true` property does not prove
  that the property belongs to the PUT request. Discriminator metadata and
  internal back-PUT tolerance do not override the authored lifecycle contract.
  Keep the warning for that contract; any intentional source exception needs
  separate authoring/suppression justification.
- Whole-schema equality is not added. The rule compares property presence,
  not general type compatibility. The existing empty-PATCH check is retained.

Fresh full-corpus results, exact old/new source-diagnostic deltas, runtime
identities and portable artifacts are published separately in
[`refresh-20261103`](refresh-20261103/task.json). The original receipts remain
historical evidence, not validation of the corrected candidate.

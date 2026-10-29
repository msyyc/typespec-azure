# Retained local-review fixes

The retained independent reviewer found two real semantic misses in candidate
`9dcf4cb3cf1be3d8b050bfb65c404573fe2981a3`. Its successful corpus run remains
historical evidence, not validation of the corrected implementation.

The corrected immutable candidate is
`c7de182af36594ba2ef2cc427d271b47bc45b238`, tree
`7493f714cd9ee8531640ecd90204e03316ed1602`, with the same core commit
`cefb035e7721a6fdcb6de605b5f469b93055a880`.

## Inherited dictionary values

An inherited `Record` stores its indexer on a base model, not necessarily on
the referenced derived model:

```tsp
model Entry {
  systemData?: string;
}
model Values extends Record<Entry> {}
model MoreValues extends Values {}
model Resource {
  properties: {
    entries?: MoreValues;
  };
}
```

The old direct-indexer check found no warning. The rule now resolves the
nearest indexer up the base-model chain and visits its value. It does not
recursively treat the base model as a separate payload root, which could
incorrectly broaden a narrowed polymorphic type.

## Applicable discriminated alternatives

```tsp
@discriminator("kind")
model Bag {
  kind: string;
}
model Bad extends Bag {
  kind: "bad";
  systemData?: string;
}
model Resource {
  properties: Bag;
}
```

The old property-only walk found no warning because the offending property is
on the applicable alternative. The rule now uses the compiler's public
`getDiscriminator` and program-aware `getDiscriminatedUnionFromInheritance`
APIs, then visits the resolved alternatives. The pinned AutoRest emitter's
`includeDerivedModel` and derived-schema/discriminator handling establish that
these concrete alternatives are included in the serialized shape.

This is not a walk of every `derivedModels` descendant. Unrelated inheritance
descendants remain excluded. A property typed as a narrowed compliant subtype
does not acquire an offending sibling alternative from its base's discriminator.

## Discriminating validation

Four focused tests were added to the existing canonical suite:

| Test                                                                         | Distinct assertion                                                                                                 |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `traverses inherited dictionary indexers`                                    | Multiple inherited indexer levels; exact authored target.                                                          |
| `traverses applicable discriminator alternatives`                            | A base-typed bag reaches its concrete offending alternative.                                                       |
| `terminates shared polymorphic dictionary cycles and respects encoded names` | Intermediate inheritance, dictionary/discriminator recursion, encoded `SystemData`, and shared-root deduplication. |
| `excludes unrelated descendants and alternatives of a narrowed subtype`      | No blind descendant/sibling expansion; renamed dictionary member remains compliant.                                |

Before implementation, the three violating regressions failed with zero
diagnostics and the other twelve cases passed. After the coherent fix, all
fifteen focused cases passed. The full ARM scope passed all 723 tests in 83
files with zero skips, preserving the original 719 tests plus these four
regressions. The existing `--maxWorkers=1` profile, pool, fixtures, assertions,
dependencies, and timeouts were unchanged.

The actual injected-package controls passed all eleven cases. Four new
standard `TrackedResource`/`ArmResourceRead` cases prove inherited dictionaries,
discriminator alternatives, narrowed compliance, and polymorphic dictionary
cycles with encoded names and deduplication. The seven existing controls,
including both complete published snippets and both inactive defaults, also
passed.

Only the ARM package required a new build/archive. The other nineteen
archives, including the previously snapshot-built rulesets package and three
separately identified external pins, remain byte-identical. Old snapshots,
archives, corpus outputs, releases, and immutable evidence commits are retained.
The existing unreleased feature description was updated; no review-history
changeset or registration/default change was added.

The required fresh full-population comparison uses the same frozen Swagger,
487 projects, source scope, configured mode, concurrency two, and unchanged
3,600-second native-phase budget. It is justified by both evidenced correctness
fixes, not used as a per-edit debugger. Current completion and counts belong
in the main report and the new run receipts; the old run cannot certify them.

Retained independent re-review is CLEAN, and the coordinator approved the exact
source. Canonical draft PR #5892 publishes native commit
`a85ba2c68327b2cadeecd7458691c4e2051b6acc`, whose complete root tree is identical
to the reviewed immutable candidate. No production source changed during
publication. The separate A/B checkpoints and actual external integration
verification remain required; PR creation is not migration completion.

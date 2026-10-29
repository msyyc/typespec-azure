# Checkpoint A round 1 fixes

Copilot review
[5703826510](https://github.com/Azure/typespec-azure/pull/5892#pullrequestreview-5703826510)
reported two valid findings against native head
`a85ba2c68327b2cadeecd7458691c4e2051b6acc`.

## Never-typed properties

[Comment 4417001420](https://github.com/Azure/typespec-azure/pull/5892#discussion_r4417001420)
is valid. AutoRest omits a model property whose type is `never` before resolving
its emitted schema name. The native rule previously matched `systemData` first,
so it warned about a field that does not exist on the wire.

The rule now skips a `never`-typed property before name matching and traversal.
A focused compliant regression and the actual-package
`never-typed-system-data` control both pass with zero target diagnostics.

## Inherited discriminator metadata

[Comment 4417001482](https://github.com/Azure/typespec-azure/pull/5892#discussion_r4417001482)
is valid. Compiler discriminator metadata is stored on the decorated model, so
an undecorated intermediate model does not return it directly.

The rule now walks the current model's base chain only to locate discriminator
metadata, then calls `getDiscriminatedUnionFromInheritance` with the current
model. This discovers alternatives below `Intermediate` without broadening to
siblings below `Base`. Focused and actual-package controls cover the violating
intermediate case and retain the compliant narrowed-sibling case.

## Candidate and validation

The immutable candidate is
`e837d711e0ff9b6962c47a53852ed94b1a5fe591`, tree
`638ed6d8370405bf0f76bb307e62da07a7ec1fd8`, based on published native head
`a85ba2c68327b2cadeecd7458691c4e2051b6acc`. Exact source, package, and packed
member identities are in [candidate.json](candidate.json).

- 17 focused tests pass.
- The complete ARM package passes 725 tests in 83 files with zero skips under
  the unchanged `--maxWorkers=1` profile.
- ARM build, lint, documentation generation, formatting, and 9 rulesets tests
  pass.
- All 13 actual injected-package controls pass, including both new regressions.
- The fresh 487-project source-scope run completed naturally against the same
  frozen Swagger baseline with 487 assessable projects, no failures, Swagger
  raw count 0, native raw count 2, and default target count 0.
- [All project rows and both witnesses](checkpointA-round1-gap-reconciliation.json)
  match the prior corrected run, so there is no new unexplained gap.

The first fresh-run invocation is retained as a failure: its launcher used
`npm_config_registry` instead of the required `PNPM_CONFIG_REGISTRY`, contacted
the public registry, and failed during installation. A coordinator-authorized
supplemental deterministic correction ran with the approved registry and
`PNPM_CONFIG_OFFLINE=true`. Exact artifact injection then used only the cache,
the 13 controls passed, and the fresh corpus run completed. This correction did
not reset or consume the exhausted ordinary development, round, reserve, or
native-timeout allowances.

No native fix is staged, committed, pushed, or used to resolve either thread
pending explicit publication approval.

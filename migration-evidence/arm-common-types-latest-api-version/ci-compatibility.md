# CI-derived compatibility proposal for PR 6035

## Causal conclusion

The completed [external integration job](https://github.com/Azure/typespec-azure/actions/runs/42748157117/job/129605225452)
tested linter head `55770151a2ae8df4ad6baae90482f4f164424ea3`. Its 455 diagnostic
occurrences all use the newly restored `outdated` message of
`@azure-tools/typespec-azure-resource-manager/arm-common-types-version`.
They are attributable to PR 6035, not simply matched by diagnostic code:
the pre-change rule only reported missing explicit configuration and contained
no outdated-selection message or reporting path. The current source adds that
separate path after the existing configuration guard, checking only the last
declared API-version member and selecting a member override before the namespace
default. The observed message names latest common-types v6 versus v3/v4/v5;
none is the unchanged missing-configuration message.

[Pre-change source](https://github.com/Azure/typespec-azure/blob/895c7b84c16cc8ab4d834381886bc727fa564c20/packages/typespec-azure-resource-manager/src/rules/arm-common-types-version.ts),
[exact changed source](https://github.com/Azure/typespec-azure/blob/55770151a2ae8df4ad6baae90482f4f164424ea3/packages/typespec-azure-resource-manager/src/rules/arm-common-types-version.ts)
and [PR comparison](https://github.com/Azure/typespec-azure/pull/6035/files)
support that attribution. Native severity remains warning. The existing
integration harness appends `--warn-as-error`, explaining the errors in CI.
Compiler source checks authored suppressions before promoting warning severity;
this is not an attempt to suppress genuine compiler errors.

## Diagnostic inventory and source mapping

| Observation | Count |
| --- | ---: |
| Projects in the completed current-consumer CI run | 605 |
| Passed / failed projects | 219 / 386 |
| Raw diagnostic occurrences | 455 |
| Raw occurrences selecting v5 / v3 / v4 | 364 / 83 / 8 |
| Unique diagnosed source targets and files | 379 |
| Confirmed PR-caused compatibility targets | 379 |
| Namespace-default / member-override selections | 333 / 46 |
| Proposed enum-member suppressions | 379 |
| Unique suppressions for v5 / v3 / v4 | 296 / 77 / 6 |
| Historical-member or namespace suppressions added | 0 |
| Unrelated, false-positive or unresolved targets included | 0 |

The [complete machine-readable inventory](ci-compatibility-inventory.json)
retains every raw occurrence with its original log line, project/config,
reported file/span/message and source snippet; each normalized target maps
back to its occurrence IDs. Deduplication removes 76 extra occurrences from
the edit count without deleting their evidence. Failed projects and authored
annotations are different counting units.

Every reported file, line and source snippet exactly matches proposed source
base `06472951865696fb06a0e36ece718d62bf4edc33`. Each declaration is still the
last member of its namespace's version enum, and its effective explicit
common-types selection matches the reported older version. The mapping handles
namespace defaults, member overrides, string-valued and qualified decorators,
backtick enum members, nested namespaces, and imported version enums. All targets
are versioned enum members; no unversioned exception is needed.

## Proposal and contract preservation

The isolated source branch is
`Azure/azure-rest-api-specs:fix/typespec-next-arm-common-types-latest-api-version-compat`,
created from freshly fetched `typespec-next` commit
`06472951865696fb06a0e36ece718d62bf4edc33` and targeting `typespec-next` in
that same Azure repository. It does not reuse or alter the frozen specs runtime.
The proposed source commit is
[`7569b3fdeac8618541bb62cf43a560aebc8c3602`](https://github.com/Azure/azure-rest-api-specs/commit/7569b3fdeac8618541bb62cf43a560aebc8c3602).

Each addition is one fully qualified rule-specific `#suppress` immediately on
the diagnosed latest member, with its actual v3/v4/v5 contract-preservation
reason. No API-version order, decorator selection, API contract, existing
annotation, config, dependency, generated Swagger or CI setting is changed.
The [TypeSpec directive reference](https://typespec.io/docs/language-basics/directives/#suppress)
documents the warning-code and justification arguments. This proposal defers
contract-changing common-types upgrades to separate service compatibility review.

Local validation not run, as requested; changes derived from failed CI evidence.
Read-only source/diff analysis and exact annotation mapping are not compilation
or emitted-output equivalence checks. No dependency setup, local compiler,
build, test, lint, formatting, integration or Swagger generation was run.
The repository authoring guide was read directly because its optional skill
loader is not registered here; its normal local validation step is explicitly
superseded by this user's CI-evidence-only instruction.

## Provenance limits and completion boundary

The original failed-step log SHA-256 is
`bb2b2cd90512f0e54bea74403b94395722873815152a80339042a2faa4fbb0a1`.
The full retained job log confirms the native checkout and consumer branch,
but does **not** print the exact consumer checkout SHA; the run has no published
artifact exposing it. Therefore the proposed base is not relabeled as an
attested CI input. Current-source file/span/snippet and effective-selection
matching is the explicit basis for annotations despite that provenance limit.

The integration harness logs only the first failed compilation output for a
project and omits that entrypoint's name. The inventory retains candidate
`client.tsp`/`main.tsp` files and compilation occurrence provenance, not a guessed
failed entrypoint. Shared-target observations remain traceable.

Completion means an analyzed suppression-only draft PR and direct bidirectional
linter/consumer description links. It does not mean CI was repaired or green,
that either PR was merged, or that checkpoint B ran. No CI rerun/wait or landing
coordination is part of this proposal. The existing native assessment, failed
external integration result and unstarted B remain unchanged.

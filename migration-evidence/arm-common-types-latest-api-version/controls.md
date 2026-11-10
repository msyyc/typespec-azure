# Scoped behavior and validation evidence

## Recovery, not a second migration

This is a selective recovery of [PR 5271](https://github.com/Azure/typespec-azure/pull/5271), which [PR 6000](https://github.com/Azure/typespec-azure/pull/6000) reverted. [Issue 6007](https://github.com/Azure/typespec-azure/issues/6007) supplies the narrower, approved latest-API-version scope. It retains the existing enabled warning, `@azure-tools/typespec-azure-resource-manager/arm-common-types-version`; it neither repairs the immutable LintDiff implementation nor introduces a duplicate rule.

The implementation takes the last member returned by `getVersion(program, namespace).getVersions()`. The versioning API retains declaration order; ARM's separate version-progression policy enforces increasing dates. Stable and preview members share one timeline. The effective member selection overrides the namespace default. The newest common-types version comes from the registry's newest-first `allVersions`, not a production filename map or hardcoded version.

The existing all-version explicit-configuration predicate runs first. Its namespace diagnostic, message, and precedence are unchanged, including missing historical configuration. Unversioned ARM namespaces retain latest-selection guidance. The rule does not traverse emitted references, HTTP operations, or payloads.

## Evidence-to-claim mapping

[claims.json](claims.json) maps every claimed behavior to the existing rule suite and, where applicable, actual injected-package controls. The focused suite passed **15 cases**. Six meaningful missing-outdated-warning expectations failed before the production edit; the initial red receipt also retains two subsequently corrected test-marker positions.

The selected injected population was declared before execution and passed **all eight cases**:

| Control                                    | Observed target warnings | Purpose                                                                                |
| ------------------------------------------ | -----------------------: | -------------------------------------------------------------------------------------- |
| `latest-old`                               |                        1 | Exact latest-member target and message                                                 |
| `historical-old-latest-current`            |                        0 | Historical older selections remain valid                                               |
| `missing-historical-configuration`         |                        1 | Historical gap still produces the namespace configuration warning                      |
| `unversioned-old`                          |                        1 | Unversioned latest-selection guidance                                                  |
| `authored-latest-suppression`              |                        0 | Existing authored suppression remains effective                                        |
| `existing-resource-manager-default-policy` |                        1 | The existing resource-manager preset enables the warning without comparison activation |
| `target-only-positive`                     |                        1 | Target-only activation with default activation explicitly not assessed                 |
| `target-only-compliant`                    |                        0 | Target-only compliant control                                                          |

These controls use the real installed candidate artifact closure. Their fixture `v6` expectations describe the recorded registry, not a production constant.

The original pinned portable harness passed **37 applicable cases**. Six predeclared `resource-group-path-parameter` cases required a different, unregistered migration rule and were **non-applicable**, not passes. The suite itself was not edited. Its package-loading, configuration activation, options, suppression, Boolean graph, and target-attribution controls remained applicable.

The first selected-control attempt could not resolve TypeSpec imports because its task-owned external fixture root lacked the `node_modules` junction created by the original portable harness. A separately authorized, once-only correction added that junction and verified its resolved target before rerunning the complete eight-case population in a new directory. The failed run and original helper hash remain retained locally; no candidate source, dependency, timeout, or test population changed.

## Development gates

The following commands ran from the candidate repository root using its checked-in configuration:

```powershell
mise exec -- pnpm exec vitest run --config vitest.config.fast.ts packages/typespec-azure-resource-manager/test/rules/arm-common-types-version.test.ts
mise exec -- pnpm exec vitest run --config vitest.config.fast.ts packages/typespec-azure-resource-manager/test packages/typespec-azure-rulesets/test packages/samples/test/samples.test.ts
mise exec -- pnpm exec vitest run --config vitest.config.fast.ts packages/typespec-azure-resource-manager/test packages/typespec-azure-rulesets/test packages/samples/test/samples.test.ts --maxWorkers=1
mise exec -- pnpm format
mise exec -- pnpm lint
git diff --check
```

The original full selection naturally completed **89 files / 915 tests**, with 914 passing and one 10,000 ms per-test timeout in `enforce-constraint.test.ts`, “emits no error when template param extends from Resource.” The coordinator authorized one diagnostic rerun of the **same complete selection**, adding only `--maxWorkers=1`; it passed **89 files / 915 tests** in 583.16 seconds. Ordinary and hook timeouts, source, dependencies, fixtures, and skips were unchanged. The cause of the original timeout is unproven.

Affected ARM/rulesets builds and generated ARM documentation passed. Root format and root lint passed. The first root lint attempt identified absent, already-declared `vite/client` types in the Azure playground closure; a frozen, scripts-disabled filtered install repaired that proven missing prerequisite. No manifest, lockfile, core gitlink, global registry, or lint configuration changed.

All **four actual final Markdown examples** were compiled through the existing public package Tester with the registered rule explicitly enabled. They produced the exact namespace/latest-member diagnostics or zero warnings as documented, with no unrelated diagnostics. The documentation hash and snippet ranges are recorded in [claims.json](claims.json).

An independent persistent semantic reviewer accepted the exact source patch and release-entry hashes before immutable artifact preparation. Source acceptance does not substitute for later artifact/evidence acceptance, either GitHub review checkpoint, or final-head external integration.

## Sample suppressions: individual reassessment

All paths below are under `packages/samples/specs/resource-manager/`. Existing contracts and common-types selections were preserved. Suppressions were restored only where the latest declared member intentionally remains older than the recorded registry.

| Sample                                              | Latest declared API member | Effective selection | Reason retained                                          |
| --------------------------------------------------- | -------------------------- | ------------------- | -------------------------------------------------------- |
| `legacy/legacy-operations/main.tsp`                 | `2021-10-01-preview`       | `v5`                | Grandfathered legacy operation/schema contract           |
| `legacy/managed-identity/main.tsp`                  | `2023-03-01-preview`       | `v3`                | Deliberate combination with legacy `v4` managed identity |
| `legacy/non-standard-properties/main.tsp`           | `2021-10-01-preview`       | `v5`                | Grandfathered property/schema contract                   |
| `legacy/nsp/main.tsp`                               | `2025-11-19-preview`       | `v5`                | Existing legacy network-security-perimeter example       |
| `legacy/optional-body/main.tsp`                     | `2025-01-01-preview`       | `v5`                | Grandfathered optional-body contract                     |
| `legacy/polymorphic-resource/main.tsp`              | `2025-10-01-preview`       | `v5`                | Grandfathered polymorphic-resource contract              |
| `legacy/private-endpoints/main.tsp`                 | `2021-10-01-preview`       | `v5`                | Grandfathered private-endpoint schema                    |
| `legacy/private-links/main.tsp`                     | `2021-10-01-preview`       | `v5`                | Grandfathered private-link schema                        |
| `legacy/rename-operations/main.tsp`                 | `2025-01-01-preview`       | `v5`                | Grandfathered renamed-operation contract                 |
| `legacy/static-routes/main.tsp`                     | `2025-06-01-preview`       | `v5`                | Grandfathered static-route contract                      |
| `resource-common-properties/private-links/main.tsp` | `2023-11-01-preview`       | `v5`                | Demonstrates older private-link schema compatibility     |

The final sample's historical `2023-08-01` member retains `v4` **without a suppression**: historical older selection is compliant under the recovered policy. The complete sample test selection passed.

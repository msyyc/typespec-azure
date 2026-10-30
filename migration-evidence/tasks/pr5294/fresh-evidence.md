# Fresh run provenance and recovery

## Frozen inputs and result

| Input                    | Exact identity                                                     |
| ------------------------ | ------------------------------------------------------------------ |
| PR implementation        | `94b316787e2a19847c26986412ce254ca4da33b4`                         |
| Candidate core gitlink   | `cefb035e7721a6fdcb6de605b5f469b93055a880`                         |
| Coverage tooling         | `cd39d7aa2fa95b1307ad5ee6742a8378c7bdc603`                         |
| Tested specs             | `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`                         |
| Baseline metadata commit | `317e703b3e380d3b64e0dacb3a2c6fc0651de253`                         |
| Baseline identity        | `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995` |
| Run                      | `20261030-94b316787`, complete                                     |

The candidate was reused in its existing worktree. A separate reusable specs
worktree was created at the exact frozen source. The existing evidence branch
and PR link were retained. No source, lockfile, core gitlink or default ruleset
was committed or changed in the implementation PR.

All 487 selected projects compiled successfully in the native run. The shared
baseline had zero compile/validation failures and 649 Swagger files. Selected
Swagger observations are 715 `PatchBodyParametersSchema`, 150
`ConsistentPatchProperties`, 110 `UnSupportedPatchProperties`. Combined TypeSpec
findings are 1,337, counted once.

The baseline's producer used different candidate/core/tooling identities.
The [actual change inventory](runs/20261030-94b316787/producer-candidate-change-inventory.txt)
includes emission/library changes, not merely lint edits. Therefore the run
explicitly uses `frozen-reference`, not a fabricated strict lint-only receipt.
Backward compatibility is assumed and actual source compilation was tested;
identical emitted Swagger was neither tested nor claimed.

## Execution and validation

- Node `26.5.0`; specs-declared pnpm `12.6.0`; candidate pnpm `11.10.0`.
  The approved registry was preserved process-locally with
  `PNPM_CONFIG_REGISTRY`, without global changes.
- Missing candidate dependencies were restored only after the required build
  failed because Azure Examples had no installed `tsp` executable.
  The frozen, filtered dependency closure then built successfully.
- Chronus `1.5.1` packed seven Azure and thirteen pinned-core packages.
  Repeated `--only` selectors were required. Core packing used the already
  installed Chronus directly to avoid unrelated package-manager setup.
  Exact archive hashes and sanitized successful build/pack logs are retained.
- The candidate integration CLI ran **patch/install stages only**, never its
  checkout/reset stage. It restored specs manifests and preserved the lockfile.
- Fresh owning ARM tests: **758 passed, zero failed/skipped**, including all 113
  canonical PATCH tests. Injected PATCH controls: **10 configured + 10 target-only
  passed**, checking all three members, compliance, source suppression,
  ineffective Create-only input and identity exemption. Configured controls
  confirm the shared resource-manager ruleset leaves the rule disabled.
- Generic injected controls: **37 passed, six failed** because this candidate
  does not register the unrelated `resource-group-path-parameter` rule expected
  by newer tooling. Those failures are retained and are not represented as a
  passing generic suite. No production change was made to satisfy them.
- An initial layout control returned an empty HTTP response and therefore had
  no comparison body. The control was corrected to a nonempty resource response;
  its first failure remains locally retained. This was not a linter repair.
- The full native run had `scope: source`, no filter/limit, target-only,
  concurrency 2 and a 7,200-second native-stage budget. It ran from
  `2026-10-30T06:35:40Z` to `07:49:01Z`, including setup and repeated complete
  dataset verification. Native execution itself ran approximately `07:07:23Z`
  to `07:30:16Z`; the budget was not exceeded.
- All 93,496 baseline dataset files were checked by the pinned baseline helper.
  The analyzer also verified the retained inventory, copied dataset, final
  dataset hashes, unchanged input snapshots and unchanged artifact hashes.
  Every successful worker's compiler/ARM/emitter entrypoint hash matched its
  packed artifact.

The [sanitized manifest](runs/20261030-94b316787/manifest.json),
[control results](runs/20261030-94b316787/controls.json),
[loaded packages](runs/20261030-94b316787/loaded-packages.json), and
[original receipt hashes](runs/20261030-94b316787/receipt-identities.json)
retain these distinctions. Machine-specific checkout/entrypoint paths were
replaced with role tokens; source targets, messages and counts were preserved.
Sanitized manifest bytes intentionally differ from original receipts and must
not be fed to strict compatibility verification as if byte-identical.

## Durable inputs and observations

| Archive                                       | Repository / release                                                     |      Bytes | SHA-256                                                            |
| --------------------------------------------- | ------------------------------------------------------------------------ | ---------: | ------------------------------------------------------------------ |
| `swagger-arm-20261026-2cd3c5dd.tar.gz`        | `msyyc/azure-rest-api-specs` / `swagger-lint-baseline-20261026-2cd3c5dd` | 51,932,501 | `0904cbd17e24ce076e7969837b85b1f5b3682e5ae25b8805b048fb506e77c1d0` |
| `pr5294-candidate-artifacts-94b316787.tar.gz` | `msyyc/typespec-azure` / `pr5294-native-coverage-20261030`               |  2,469,688 | `a7a24372568d446a5d66f0472a5dc5eb999186f468e3f4864b4e48afcc0a2267` |
| `pr5294-native-observations-94b316787.tar.gz` | Same evidence release                                                    |    882,988 | `6fae965dcc0d4509280d7c6bdb62c04dc9c6b494ec947c170c3fc4e72c1188de` |

The candidate archive contains all 20 packages and successful build/pack
provenance. The observations archive contains complete sanitized native/member
receipts, full population inventory, controls, independent recount and available
installation locks. Git holds the compact project/version/status/Swagger-file
inventory; the full 16 MB source/asset inventory remains in the archive and
selected baseline, not silently discarded.

Source retention reuses the verified existing ref:
`msyyc/azure-rest-api-specs:evidence/long-running-operations-options-validator-20261022-source`
at **exactly** `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`.
It was read back from GitHub without moving it. This source ref is distinct from
the metadata branch and generated baseline.

Download/hash and clean-checkout recovery status is recorded in
[recovery.json](runs/20261030-94b316787/recovery.json).
Unchanged source refs alone do not prove locked transitive runtimes or full
diagnostic regeneration.

## Read or recount saved observations

From a fresh checkout of
`msyyc/typespec-azure:evidence/pr5294-patch-body-migration`:

```powershell
python migration-evidence\tasks\pr5294\runs\20261030-94b316787\reanalyze.py `
  migration-evidence\tasks\pr5294\runs\20261030-94b316787 `
  <NEW_ANALYSIS_JSON>
```

This dependency-free recount independently checks every project, member total,
raw/location count, one-sided set and both directional gaps against the saved
tool report. It must reproduce 975 / 1,337 findings, 27 / 56 directional projects,
102 / 464 excesses and absolute difference 566.
It reads saved observations; it does **not** execute either linter.

Download complete archives without overwriting existing files:

```powershell
gh release download pr5294-native-coverage-20261030 --repo msyyc/typespec-azure `
  --pattern "pr5294-*.tar.gz" --dir <NEW_DOWNLOAD_DIRECTORY>
gh release download swagger-lint-baseline-20261026-2cd3c5dd `
  --repo msyyc/azure-rest-api-specs `
  --pattern swagger-arm-20261026-2cd3c5dd.tar.gz --dir <NEW_DOWNLOAD_DIRECTORY>
Get-FileHash <DOWNLOADED_ARCHIVE> -Algorithm SHA256
```

Verify sizes/hashes before extraction. Recounting `observations` from the
downloaded archive is independent of the compact Git inventory. Rendering
`fresh-differences.md` from saved counts uses the retained
`render-differences.py`; its cause annotations are human assessment, not an
automatic equivalence decision.

## Fully rerun native diagnostics

Recover the exact candidate/core, tooling and preserved specs commits above
into separate clean worktrees under the user's worktrees boundary. Do not fetch
moving tips, reset another task's checkout, reuse a shared writable runtime,
change the baseline or regenerate Swagger. Unpack the candidate archive to
recover `candidate-artifacts`; build the pinned integration-tester closure if
its generated CLI implementation is missing.

Recover the immutable descriptor at metadata commit
`317e703b3e380d3b64e0dacb3a2c6fc0651de253`, path
`.lintdiff-baselines/swagger-arm-20261026-2cd3c5dd/baseline.json`.
Its original descriptor SHA-256 is
`ac511e7ff4b519619f30af811107b7f770a92a5bb56b199dfca983262dc8fd31`.
Use the pinned tooling's `shared_baseline.py fetch` with that descriptor and a
new absolute output directory, optionally supplying the verified downloaded
archive. This helper restores/verifies the sealed Swagger-only baseline; it
never generates Swagger.

The required build closure was selected with:

```powershell
mise exec -- pnpm -r `
  --filter '@azure-tools/typespec-azure-resource-manager...' `
  --filter '@azure-tools/typespec-autorest...' `
  --filter '@azure-tools/typespec-azure-rulesets...' `
  --filter '@azure-tools/typespec-azure-portal-core...' `
  --filter '@azure-tools/typespec-client-generator-core...' `
  --filter '@typespec/openapi3...' --filter '@typespec/xml...' `
  --filter '@typespec/events...' --filter '@typespec/sse...' `
  --filter '@typespec/streams...' --filter '@typespec/integration-tester...' build
```

The [artifact inventory](runs/20261030-94b316787/candidate-artifacts.json) lists
every explicit Chronus selector and expected package version/hash. Rebuilding
can change package bytes; do not silently substitute new tarballs for the
recorded artifacts.

From the candidate root, inject with the recorded specs package manager:

```powershell
mise exec node@26.5.0 pnpm@12.6.0 -- node `
  core\packages\tsp-integration\cmd\tsp-integration.js azure-specs `
  --repo <SPECS_ROOT> --stage patch --stage install --tgz-dir <ARTIFACTS>
```

Rerun the owning tests, supplied injected controls, and `patch-controls.mjs`
against those packages. Keep default-activation checks separate from the
target-only run. Preserve known unrelated generic failures explicitly.
Then run from the tooling's `packages\typespec-lintdiff`:

```powershell
mise exec node@26.5.0 pnpm@12.6.0 -- node --import tsx/esm `
  test\harness\native-coverage.ts `
  --candidate-repo <CANDIDATE_ROOT> --specs-repo <SPECS_ROOT> `
  --tgz-dir <ARTIFACTS> --output <NEW_EMPTY_OUTPUT> `
  --validator-rule PatchBodyParametersSchema `
  --validator-rule ConsistentPatchProperties `
  --validator-rule UnSupportedPatchProperties `
  --tsp-rule @azure-tools/typespec-azure-resource-manager/no-unsafe-patch-body-properties `
  --scope source --baseline-run <VERIFIED_BASELINE_RUN> `
  --baseline-policy frozen-reference --native-mode target-only `
  --native-budget-seconds 7200 --concurrency 2
```

Available source/install locks and package hashes are retained, but this is not
a claim of complete transitive runtime locking across machines. A future full
rerun must record its own resolved runtime and failures, rerun semantic controls,
and reassess each count/source gap before regenerating `migration.md`.
The current task performed one complete fresh native run. A second full native
run is not required or claimed by the saved-observation recovery check.

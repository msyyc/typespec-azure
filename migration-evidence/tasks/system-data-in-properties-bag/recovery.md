# Recovering the SystemDataInPropertiesBag evidence

## What each recovery path proves

- **Read evidence:** fetch this evidence branch and inspect its report, exact population, diagnostics, package identities, and input asset manifest. This does not execute a linter.
- **Recount observations:** run `node recount.mjs runs\cycle0\observations.json` from this directory. The dependency-free helper independently groups every selected project and preserves failed/unassessed projects, raw findings, conservative locations, and both excess directions. It does not rerun TypeSpec or Swagger and does not establish semantic equivalence.
- **Regenerate coverage:** recover the pinned source/runtime below, inject the recorded packages, rerun the documented controls, and run fresh native diagnostics against the saved Swagger baseline. This is separate from recounting. A complete second native corpus execution is not claimed by the fresh-checkout recovery gate.

The [independent fresh-checkout recovery receipt](fresh-recovery.json) passed
against initial published commit
`b45d7c3a54f05bda2f7552e4ca4501d5316d8322`. It records the fresh downloads,
source and package reconstruction, complete sealed-baseline verification, and
all-project recount. This is not a full second corpus run or a fresh runtime
dependency installation.

## Immutable inputs

The [fork release](https://github.com/msyyc/typespec-azure/releases/tag/systemdata-in-properties-bag-cycle0-20261029) retains `systemdata-cycle0-inputs.tar.gz`. Its bytes and SHA-256 are in `assets.json`. The archive contains:

- `candidate.bundle`: immutable validation commit `9dcf4cb3cf1be3d8b050bfb65c404573fe2981a3`, requiring canonical base `2160a1a6b0e7827aff13f01a2fd296e534945411`;
- the twelve exact tested source files, with both working-file and Git-blob SHA-256 values;
- `tooling-source.tar.gz`: clean tracked tooling at `Azure/typespec-azure` commit `cd39d7aa2fa95b1307ad5ee6742a8378c7bdc603`, including the comparison harness and dependency manifests/lockfile;
- twenty package archives and their package names, versions, hashes, and distinct build/external provenance;
- the one-time actual-package controls and saved-producer audit helpers;
- the pinned baseline descriptor.

The candidate's core gitlink is `microsoft/typespec` commit `cefb035e7721a6fdcb6de605b5f469b93055a880`. The source bundle is a validation snapshot, not the native publisher branch or an approved native PR commit.

The shared Swagger archive is independently published in [`msyyc/azure-rest-api-specs`](https://github.com/msyyc/azure-rest-api-specs/releases/tag/swagger-lint-baseline-20261026-2cd3c5dd):

- asset `swagger-arm-20261026-2cd3c5dd.tar.gz`;
- 51,932,501 bytes;
- SHA-256 `0904cbd17e24ce076e7969837b85b1f5b3682e5ae25b8805b048fb506e77c1d0`;
- identity `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`;
- descriptor metadata commit `317e703b3e380d3b64e0dacb3a2c6fc0651de253`;
- descriptor SHA-256 `ac511e7ff4b519619f30af811107b7f770a92a5bb56b199dfca983262dc8fd31`.

The frozen specs source is retained separately at `msyyc/azure-rest-api-specs`, branch `evidence/long-running-operations-options-validator-20261022-source`, exact commit `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`. The source branch is not the metadata branch and contains no runtime-injection overlay.

## Recover without the development checkout

Use a fresh evidence checkout and new task-owned directories below the chosen worktrees boundary. Do not copy unpublished local inputs or use temporary system directories.

1. Download both named immutable release assets with `gh release download --repo ... --pattern ... --dir ...`. Verify byte lengths and SHA-256 before extraction.
2. Extract the input archive and verify every file against `inputs.json`, including all twenty packages and twelve source files. Retain the three external frozen registry packages as external provenance, not candidate-built outputs.
3. Initialize an isolated candidate repository, fetch the exact canonical base, verify and fetch `candidate.bundle`, and select its exact commit. Verify the tree `e710df8841fd1312953da137588f172449473c84` and task-file blob hashes. Recover core at its exact gitlink. Do not resolve moving `main` or `next`.
4. Recover the exact tooling archive and frozen specs source. Check the preserved specs ref and fetched SHA. Restore the shared baseline archive without changing it; run its supported verifier before using the unpacked directory as a CLI baseline.
5. To recount only, use this checkout's published `observations.json` and `recount.mjs`. Compare its output with the published summary. This requires only Node, not compiler packages or a network install.

The independent check uses a fresh recursive clone of the published evidence
branch, downloads both release assets into that checkout, and verifies the
published file catalog against both working files and Git blobs. Candidate
reconstruction uses these exact Git operations, with task-owned paths substituted:

```powershell
git init --quiet <candidate>
git -C <candidate> fetch --depth 1 https://github.com/Azure/typespec-azure.git 2160a1a6b0e7827aff13f01a2fd296e534945411
git -C <candidate> bundle verify <inputs>\candidate.bundle
git -C <candidate> fetch <inputs>\candidate.bundle HEAD
git -C <candidate> -c core.autocrlf=false checkout --detach 9dcf4cb3cf1be3d8b050bfb65c404573fe2981a3
git -C <candidate> submodule update --init --depth 1 core
```

The process-local checkout option preserves the tested source bytes without
changing global Git configuration. Verify all twelve working-file and Git-blob
hashes against `inputs.json`, the candidate tree, the core commit, and every
package archive's hash and actual `package/package.json` name/version.

Recover the frozen specs source into a separate task-owned Git object store by
fetching the exact `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9` commit from its
preservation repository with `--depth 1`. Verify the preserved ref still names
that commit, run `git fsck --connectivity-only --no-dangling FETCH_HEAD`, and
inspect the complete tracked tree and the recorded source witnesses. This check
recovers the complete source object closure; it does not claim to provision an
installed specs runtime or run another corpus.

The archived tooling contains the supported local baseline recovery entrypoint:

```powershell
python <tooling>\.github\skills\analyze-native-lint-coverage\shared_baseline.py fetch `
  --descriptor <inputs>\baseline-descriptor.json `
  --archive <downloads>\swagger-arm-20261026-2cd3c5dd.tar.gz `
  --output <new-empty-baseline-path>
```

It verifies the downloaded archive, safely extracts it into a new directory,
and verifies the complete sealed file inventory, project population, and
diagnostic shards. This is baseline recovery, not Swagger generation or a new
Swagger-linter execution. The fresh check uses the downloaded tooling and
inputs, not unpublished development files or a session-directory cache.

## Full regeneration prerequisites and command

Use Node 26.5.0, candidate/tooling pnpm 11.10.0, and specs pnpm 12.6.0. Use the approved registry `https://packagefeedproxy.microsoft.io/npm/` through process-local `PNPM_CONFIG_REGISTRY`. Follow the repository's pinned mise configuration and explicit missing-dependency setup, rather than installing arbitrary latest versions. Full tooling setup also requires its own recorded Git commit and core gitlink: recover that Git tree and initialize its submodule rather than treating an archive's empty submodule directory as an installed workspace.

The source archive includes the tooling lockfile. The selected candidate/compiler/library packages are exact archives, but the evidence does **not** assert a fully portable lock of every transitive installed dependency. Preserve the supported injection mechanism's metadata restoration and record the actual resulting runtime. Do not blindly run an unfrozen specs install or resolve its historical `next` overrides.

The existing candidate `core\packages\tsp-integration\cmd\tsp-integration.js` must have its required prepared dependency/build closure. Inject with only the `patch` and `install` stages, exact `--repo` and `--tgz-dir`, and the specs package manager. Do not run its checkout/reset stage. The supported runner restores the original workspace metadata and lockfile in `finally`.

Run the archived `run-injected-controls.mjs` with the specs directory, exact worker entrypoint, actual candidate rule document, and a new output directory. Its full literal published snippets, suppression, complete graph, and both default/explicit activation cases must pass before fresh corpus execution.

From the recovered tooling's **`packages\typespec-lintdiff` directory** (where its installed `tsx` dependency resolves), run:

```powershell
mise exec node@26.5.0 pnpm@12.6.0 -- node --import tsx/esm .\test\harness\native-coverage.ts `
  --candidate-repo <clean-candidate> `
  --specs-repo <frozen-specs-runtime> `
  --tgz-dir <verified-artifacts> `
  --validator-rule SystemDataInPropertiesBag `
  --tsp-rule @azure-tools/typespec-azure-resource-manager/no-nested-system-data `
  --scope source `
  --baseline-run <verified-unpacked-shared-baseline> `
  --baseline-policy frozen-reference `
  --output <new-empty-output> `
  --concurrency 2 `
  --native-budget-seconds 3600 `
  --native-mode configured
```

The existing analyzer performs its normal final-run patch/install and baseline integrity checks. Never omit `--baseline-run`, run the Swagger generator, add a filter/limit, reuse old native findings, or treat failed projects as compliant. The 3,600-second budget applies to the native worker phase; baseline integrity/copy preparation is separate and must finish normally.

Before any rerun, inspect the installed CLI grammar and dependency scope. Preserve the original invocation's bootstrap and pack errors; a different cwd or selector spelling is a local command correction, not a reason to install extra root dependencies.

For applicable ARM test gates, the verified package-scoped profile is `pnpm --filter @azure-tools/typespec-azure-resource-manager exec vitest run --maxWorkers=1`: the original 719 tests in 83 files, zero skips, unchanged pool/assertions/dependencies/test and hook timeouts. The previous timeout recovered with unproven cause; this does not prove contention.

Reinvestigate failures, one-sided projects, count differences, version/reachability, and intentional semantic differences before producing a new migration conclusion. Identical counts cannot regenerate the prose or establish functional equivalence.

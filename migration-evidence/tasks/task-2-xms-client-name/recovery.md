# Recovery and reproduction

## Status and identities

Independent source and artifact/report reviews passed. Native commit
`c06d3a4a7ed1bb2cb417c76c6348624472c0c3ad` is pushed to canonical Azure.
The evidence branch and immutable candidate assets are published. The actual
[release download round trip](publication/assets.json) passed. Fresh
published-checkout recovery is pending. No pull request, CI run or integration
acceptance is claimed.

The assessed candidate is immutable snapshot
`d065102fa52bf69b680f08016fc049d7185b7c22`, tree
`e6e427fdc92eab80b88ffe67773467ad12b787b7`. Its canonical base is
`Azure/typespec-azure@9024f28739650a92c05465c8318fc08bc17a48cc`.
Its `core` gitlink is `41e2a4e70f0ea49ee52fa9d0d6d3d9c698c6ac08`.
The native task commit has exactly the assessed 16 task-file bytes and the same
complete tree as the snapshot. Its parent is the recorded canonical base.
Do not substitute an unverified branch head for this snapshot.

The specs source is
`Azure/azure-rest-api-specs@6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc`.
The retained source ref is
`msyyc/azure-rest-api-specs:evidence/shared-swagger-baseline-20261117-source`.
This ref is separate from the metadata discovery ref.

The frozen Swagger baseline is `swagger-arm-20261117-6eeeaa99`, identity
`7eebd1aed4f40d8305c29be3ecbf6b4ee4585db2f4b3b1b4fe5c800fac7583d8`.
Its descriptor is pinned at metadata commit
`2c35e1f6a7139768b03234983ad201d8fefa4d0b`, not moving `current.json`.
The archive has 53,558,923 bytes and SHA-256
`0331b41caeb28ef10ff3a2d023c96eed14561b357e4179b4fb537969469af20c`.
Use the immutable asset reference from the retained descriptor.
Do not regenerate Swagger if the download or verification fails.

## Read saved evidence

After publication, fetch the exact evidence commit recorded in the publication
receipt. Verify every published Git blob against `prepared-inventory.json`.
Download the candidate artifacts and source bundle using the
[published asset receipt](publication/assets.json). Verify byte length and
SHA-256 before extraction. The receipt records the actual immutable release URL.

The candidate source bundle advertises `HEAD` at the snapshot commit. It contains
only the reviewed change above its required canonical base. It is not a full
repository clone. Its bytes and prerequisite are in
`receipts/source-bundle.json`. Local `git bundle verify` passed; recovery from a
fresh published evidence checkout remains a later required gate.

## Reanalyze saved observations

Run the dependency-free helper from this directory:

```powershell
python .\reanalyze.py
```

The helper reads the saved project inventory, selected Swagger observations,
all project receipts, and the original coverage report. It independently groups
the receipts, checks the selected and assessable populations, and verifies raw,
aligned, directional-excess and source-key counts against the report.
It does not compile specs, rerun either linter, restore a sealed baseline, or
decide semantic equivalence.

## Inspect the saved parameter-attribution evidence

The [DeploymentStacks attribution receipt](receipts/deployment-stack-parameter-identities.json)
answers one concrete question that source inspection alone did not settle.
Six distinct parameter objects each carry three relevant propagated application
nodes. Omitting any one application preserves the effective name and exact-name
policy on every affected parameter. The initial shared-object hypothesis was
disproved, not used as a correspondence claim.

The original read-only project compile passed in about six seconds, with no
compiler or configuration diagnostics. Its loaded compiler and TCGC entrypoint
hashes match the injected candidate. This observation does not add diagnostics
to the full-run corpus, rerun unit tests, mutate the Program, or emit Swagger.

The sanitized
[inspection script](receipts/inspect-deployment-stack-parameters.mjs)
uses `$SPECS` as a path placeholder. Resolve that placeholder to the recovered,
injected specs root before execution with the recorded Node version, and supply
a new output filename as the script's first argument. The original local
execution is verified; replay of the published sanitized script is still a
later recovery gate, not a claimed result.

## Recover the exact candidate

Use a new task-owned directory under the caller's worktrees boundary.
Clone the canonical repository with `--no-checkout` and repository-local
`submodule.recurse=false`. Check out the recorded base with command-local
recursion disabled. Fetch `HEAD` from the verified source bundle, then check
out the recorded snapshot before initializing `core` at its pinned gitlink.

For example, after resolving `$Candidate` and `$Bundle` to absolute paths:

```powershell
git clone --no-checkout --config submodule.recurse=false `
  https://github.com/Azure/typespec-azure $Candidate
git -C $Candidate -c submodule.recurse=false checkout `
  --no-recurse-submodules --detach 9024f28739650a92c05465c8318fc08bc17a48cc
git -C $Candidate fetch $Bundle HEAD
git -C $Candidate -c submodule.recurse=false checkout `
  --no-recurse-submodules --detach d065102fa52bf69b680f08016fc049d7185b7c22
git -C $Candidate submodule update --init
```

Verify the root, snapshot commit, tree, core commit, clean state, and all 16
source-file hashes. Do not copy the failed partial snapshot or inherit a global
recursive checkout into an uninitialized `core`.

The candidate tools are Node 26.5.0 and pnpm 11.10.0. The specs tools are Node
26.5.0 and pnpm 12.6.0. The compiler is the candidate's 1.18.0, not an
independently selected compiler. Preserve the approved package registry.

For a fresh build, trust the task-owned mise configuration, select the recorded
native dependency profile, and use frozen filtered `--ignore-scripts`
installation only for missing prerequisites. Build the TCGC, AutoRest, rulesets,
integration-tester and formatter closures explicitly. The retained build and
payload receipts explain the original prepared-output provenance; they do not
prove that a later rebuild will have identical bytes.

The published package closure has six Azure packages and nine core packages.
Use `candidate-artifact-inventory.json` as the exact package list and checksum
authority. Pack the Azure packages under the Azure root Chronus configuration
and core packages under the `core` configuration. Repeat `--only=<package>` for
each package; this Chronus parser does not accept a greedy trailing list.
Use `--pack-destination <absolute-directory>`.
Do not include unrelated unbuilt packages.

The original artifact proof checks every non-manifest payload byte against the
snapshot and records publish-time package-manifest dependency substitutions.
Reusing those exact artifacts is different from reproducing a build.
For a rebuild, regenerate this proof before calling the artifacts equivalent.

## Rerun controls and full coverage

### Lightweight recovery controls

The original integration installer uses `--no-lockfile`; its restored root
lock is not an effective candidate-install lock. The read-only
[recovery closure](recovery-runtime-closure.json) captures the unchanged
installed runtime's 78 reachable package/version records and their own-file
hashes. All 15 candidate entrypoints still match the assessed identities.
This is input retention, not another compile or full coverage run.

Use the published helpers to create an isolated control runtime from downloaded
artifacts. The helper pins registry dependency versions and parent-specific
overrides, including both recorded `string-width` versions. It does not select
latest versions or reuse an unpublished `node_modules` directory.

```powershell
python .\prepare-recovery-runtime.py --artifacts $Artifacts --runtime $Runtime
Set-Location -LiteralPath $Runtime
mise exec node@26.5.0 pnpm@12.6.0 -- pnpm install --ignore-scripts --no-optional
mise exec node@26.5.0 -- node $RecoveredEvidence\verify-recovery-runtime.mjs `
  $Runtime $NewReceipt
```

The byte verifier checks every retained package-file record, not just versions.
Resolve the 16 published control input paths to the recovered fixtures and this
runtime. Use the pinned worker below and restore fixture `node_modules`
junctions to the new runtime. Saved-count reanalysis and lightweight controls
do not regenerate Swagger or repeat the 490-project run.

### Full comparison regeneration

Use tooling revision
`Azure/typespec-azure@7b63cb7fc9d8385505ebf098ee2deedff5f6464f`.
The analyzer is
`packages\typespec-lintdiff\test\harness\native-coverage.ts`.
The worker is `native-coverage-worker.mjs` beside it.
Use an exclusive writable specs runtime at the frozen source commit.
Keep output outside both clean inputs.

The integration CLI must execute only `patch` and `install` for the supplied
specs checkout and candidate tarball directory. Its checkout stage can reset
source and must not run. Verify the actual loaded package entrypoint hashes
against the artifacts. Run the retained portable controls with their disclosed
six unrelated-rule exclusions and all 16 target controls. Restore each fixture's
`node_modules` junction to the exclusive injected specs runtime before calling
the worker with its portable input paths resolved.

For required changed-file unit validation, preserve all cases in the three
changed TCGC files and the one changed rulesets file. The approved TCGC profile
uses `--maxWorkers=1`; test and hook limits stay 10000 ms. Do not convert this
profile into a full-package run or claim that historical timeout causes were
proved.

The full comparison command must use the specs manager on `PATH`, not an
implicit tooling-manager script. From `packages\typespec-lintdiff`:

```powershell
mise exec node@26.5.0 pnpm@12.6.0 -- node --import tsx/esm `
  test\harness\native-coverage.ts `
  --candidate-repo $Candidate `
  --specs-repo $Specs `
  --tgz-dir $Artifacts `
  --validator-rule XmsClientName `
  --tsp-rule @azure-tools/typespec-client-generator-core/no-redundant-client-name `
  --scope source `
  --baseline-run $VerifiedBaseline `
  --baseline-policy frozen-reference `
  --native-mode target-only `
  --output $NewEmptyOutput
```

The default analyzer concurrency is two. No filter, limit, Swagger generation,
or native-package lane applies. The analyzer verifies the baseline and performs
its required patch/install setup even after a separate control injection.
Preserve failures, unassessed projects, raw and ambient diagnostics.
Default activation needs the separate preset/all controls.

A fresh full rerun requires its own cost/budget declaration. Reconcile all
one-sided findings and semantic controls before rewriting `migration.md`.
Counts cannot regenerate the prose assessment or establish equivalence.

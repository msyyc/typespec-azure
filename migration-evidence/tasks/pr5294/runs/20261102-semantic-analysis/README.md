# November 2 semantic analysis

This supplements, rather than replaces, the October 30 full-population run.
All candidate, core, specs and baseline identities remain frozen. No Swagger
generation or production repair was performed.

`analysis.json` contains the complete 487-project accounting.
`difference-ledger.json` contains only differing check/path groups and their
captured source/representation evidence.
`archive.json` pins the supplemental asset's size, SHA-256 and inventory hash.
The archive retains all 136 native and 136 Swagger receipts, all 48 source
applicability receipts, original saved observations, actual callback paths,
operation attribution, read-only probes and authored analysis helpers.

## Download and independently recount

Use a new download/extraction/output directory; never overwrite existing
observations:

```powershell
gh release download pr5294-native-coverage-20261030 --repo msyyc/typespec-azure `
  --pattern pr5294-semantic-analysis-20261102.tar.gz --dir <NEW_DOWNLOAD_DIRECTORY>
Get-FileHash <DOWNLOADED_ARCHIVE> -Algorithm SHA256
tar -xzf <DOWNLOADED_ARCHIVE> -C <NEW_EXTRACTION_DIRECTORY>
python migration-evidence\tasks\pr5294\runs\20261102-semantic-analysis\recount.py `
  migration-evidence\tasks\pr5294\runs\20261102-semantic-analysis `
  <NEW_EXTRACTION_DIRECTORY> <NEW_RECOUNT_JSON>
```

Check `archive.json` before extraction. `recount.py` independently verifies every
archived payload hash, all original diagnostic multisets, the full population,
both directional raw gaps, function-level accounting and the difference ledger.
It reads retained observations and does not execute either linter.

## Reproduce focused observation

Recover the baseline, candidate artifacts and frozen specs runtime using
the [original recovery instructions](../../fresh-evidence.md).
Use Node `26.5.0`; resolve libraries from the injected specs installation.
Each observer writes a **new** output and refuses an existing output:

```powershell
mise exec node@26.5.0 -- node <EXTRACTED>\replay\native-trace.mjs `
  <SPECS_ROOT> <EXACT_PROJECT_SOURCE_PATH> `
  <EXTRACTED>\saved\native-results.json <NEW_NATIVE_RECEIPT>

mise exec node@26.5.0 -- node <EXTRACTED>\replay\swagger-trace.mjs `
  <SPECS_ROOT> <RETAINED_DATASET> `
  <EXTRACTED>\saved\swagger-observations.json <NEW_SWAGGER_RECEIPT> `
  <EXACT_PROJECT_SOURCE_PATH>

mise exec node@26.5.0 -- node <EXTRACTED>\replay\inspect-swagger-input.mjs `
  <SPECS_ROOT> <EXACT_PROJECT_SOURCE_PATH> `
  <EXTRACTED>\source-inspection-requests.json <NEW_SOURCE_RECEIPT>

mise exec node@26.5.0 -- node <EXTRACTED>\replay\resolver-controls.mjs `
  <SPECS_ROOT> <RETAINED_DATASET> <NEW_RESOLVER_CONTROL>

mise exec node@26.5.0 -- node <EXTRACTED>\replay\reporting-control.mjs `
  <SPECS_ROOT> <RETAINED_DATASET> <NEW_REPORTING_CONTROL>
```

The Swagger observer accepts optional
`--inspect=<PATH_TO_REMAINING_NATIVE_INSPECTION_REQUESTS>` before the project
filter to capture the additional request/response field chains. It uses a fresh
resolver per document and refuses network reference reads.

The source observer was extended with resource-root payload probes after the
48-project applicability run; those extra fields appear in the separately
retained resource-name controls. Its effective-input check is unchanged.
These helpers are instrumentation, not production-rule replacements or a new
Swagger baseline. The causal mutations in `resolver-controls.mjs` are explicitly
authored in-memory counterfactuals and must not be presented as emitted output.

Prior owning ARM tests remain 758/758 and injected PATCH controls 20/20.
The six unrelated generic-control failures remain disclosed. Reproduction must
record actual runtime identities and failures; recovering saved files does not
certify a new candidate or full semantic equivalence.

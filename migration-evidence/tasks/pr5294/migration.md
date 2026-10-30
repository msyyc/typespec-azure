# ARM PATCH property migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/no-unsafe-patch-body-properties`
consolidates the Swagger linters
[PatchBodyParametersSchema](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-body-parameters-schema.md),
[ConsistentPatchProperties](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-patch-properties.md), and
[UnSupportedPatchProperties](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/un-supported-patch-properties.md).
**The fresh current-head run completed for all 487 frozen ARM projects. This is
an intentional native semantic consolidation, not full Swagger equivalence.**
Source-versus-latest-version populations, deliberate behavior changes and
unresolved within-project correspondence prevent a full-parity conclusion.
Diagnostic differences are reported, not repaired.

## 2. Actual coverage

Fresh TypeSpec diagnostics were collected on October 30, 2026 for **487 selected,
487 assessable projects; zero compilation/worker failures or exclusions**.
The verified shared baseline supplies 649 saved Swagger files and their findings;
Swagger was not regenerated. Reported diagnostics are individual findings,
not project counts.

| Count                                   | Swagger linter | TypeSpec linter |
| --------------------------------------- | -------------: | --------------: |
| Fresh comparison, reported diagnostics  |            975 |           1,337 |
| After analysis: common actionable units |     Unassessed |      Unassessed |

The Swagger total is **715 + 150 + 110** for the three original rules.
The combined TypeSpec total is counted once; member-specific TypeSpec
attribution is unassessed. No justified common actionable unit or normalization
has been established. [Exact run and independent recount](runs/20261030-94b316787/analysis.json).

## 3. Function-level coverage

| Behavior and compliant control                                                                                      | Result                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Required PATCH input and defaults; optional, default-free input accepted                                            | Covered; all defaults include falsy values missed by Swagger's truthiness check                |
| Ordinary Read/Create-only input excluded; explicitly exposed non-Update input checked                               | Covered native policy; intentionally differs from emitted mutability/schema sharing            |
| Immutable root `id`, `name`, `type`, `location` and `properties.provisioningState`; unrelated nested names accepted | Covered; Update visibility never makes those paths mutable                                     |
| Partial encoded JSON layout, including inherited overrides, nullable models and missing nested leaves               | Covered; not type assignability and not emitted `allOf`/synthetic-discriminator equivalence    |
| Explicit resource association; PATCH/GET 200/201 precedence; safety without a comparison resource                   | Covered; standard ARM PATCH templates use explicit association                                 |
| Top-level encoded case-insensitive `identity` safety exemption                                                      | Covered; layout comparison is deliberately not exempt                                          |
| Array replacement elements                                                                                          | Extended: required descendants allowed; defaults, visibility and supported item layout checked |
| Open resource records                                                                                               | Covered named keys and named-member layouts; record indexer values not recursively expanded    |
| Request multi-model unions, tuples and multipart/native File transport                                              | Outside traversal; no exhaustive Swagger-parity claim                                          |
| Unsupported resource unions                                                                                         | Descendant layout skipped; independent safety and supported siblings retained                  |
| Ambiguous response candidates, no-service GET fallback, derived File overrides, response visibility                 | Current behavior tested; scope/design remains under review                                     |

See [behavior evidence and member notes](evidence-details.md#member-evidence).
Compiler-invalid discriminator/File constructions are not counted as linter
coverage. SDK-scope fixture behavior is source-side evidence, not proof that the
official package tests a client-generator integration.

## 4. Why diagnostic counts differ

| Differing project or diagnostic group                       | Swagger / TypeSpec | Cause and disposition                                                                                                                                                                                                |
| ----------------------------------------------------------- | -----------------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Six Swagger-only projects with Read-only provisioning state |              9 / 0 | Effective input excludes these fields; saved Swagger diagnoses reference siblings carrying `readOnly`. No TypeSpec repair justified for these exclusions. [Evidence](fresh-examples.md#read-only-reference-siblings) |
| ConfidentialLedger and SAPDiscoverySites                    |              2 / 0 | Inherited Read/Create-only location and a Read-only performance-data subtree are outside PATCH input. [Evidence](fresh-examples.md#excluded-input)                                                                   |
| ManagedNetworkFabric and ProgrammableConnectivity           |             0 / 35 | Removed/renamed properties remain in unprojected source but not latest-version Swagger. This is not a version-aligned comparison. [Evidence](fresh-examples.md#version-populations)                                  |
| Remaining thirteen TypeSpec-only projects                   |             0 / 61 | Falsy defaults, array traversal and recursive Informatica layout differences; Informatica's saved Swagger absence remains unresolved. [Evidence](fresh-examples.md#native-only-projects)                             |
| EventGrid                                                   |          117 / 200 | Layout fanout and repeated source uses; exact target correspondence remains unassessed. [Evidence](fresh-examples.md#outliers)                                                                                       |
| NetApp; Search                                              |     6 / 42; 6 / 39 | Arrays, versioned source and layout differences; residual correspondence remains unassessed. [Evidence](fresh-examples.md#outliers)                                                                                  |
| SQL; DomainRegistration                                     |    47 / 17; 16 / 1 | Material Create/Read-only input differences; no blanket normalization of residuals. [Evidence](fresh-examples.md#outliers)                                                                                           |
| EdgeOrder                                                   |             8 / 29 | Three parent-layout findings versus 23 leaf-layout findings, plus a zero default. [Evidence](fresh-examples.md#parent-and-leaf-counting)                                                                             |

All **83 unequal-count projects** and every exact target are retained in the
[fresh difference inventory](fresh-differences.md). The **102 Swagger excess
findings** and **464 TypeSpec excess findings** must not cancel into the net
**+362**; absolute per-project difference is **566**. There are also 404 equal-count
projects, whose equal totals do not prove correspondence. Unexplained residuals
remain open; no source changes were made to equalize results.

## NOTES

- Assessed PR: [Azure/typespec-azure#5294](https://github.com/Azure/typespec-azure/pull/5294),
  source head `94b316787e2a19847c26986412ce254ca4da33b4`,
  core `cefb035e7721a6fdcb6de605b5f469b93055a880`.
  [Implementation](https://github.com/msyyc/typespec-azure/blob/94b316787e2a19847c26986412ce254ca4da33b4/packages/typespec-azure-resource-manager/src/rules/no-unsafe-patch-body-properties.ts),
  [tests](https://github.com/msyyc/typespec-azure/blob/94b316787e2a19847c26986412ce254ca4da33b4/packages/typespec-azure-resource-manager/test/rules/no-unsafe-patch-body-properties.test.ts),
  [public contract](https://github.com/msyyc/typespec-azure/blob/94b316787e2a19847c26986412ce254ca4da33b4/packages/typespec-azure-resource-manager/src/rules/no-unsafe-patch-body-properties.md).
- Fresh builds and **758/758 owning ARM tests** passed, including all 113
  canonical PATCH tests. **20/20 injected PATCH controls** passed across configured
  and target-only modes. Generic injected controls: 37 passed; six require the
  unrelated `resource-group-path-parameter` rule absent from this candidate and
  failed explicitly. They were not repaired or counted as passing.
  [Control receipt](runs/20261030-94b316787/controls.json).
- Frozen specs: `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`.
  Baseline metadata: `317e703b3e380d3b64e0dacb3a2c6fc0651de253`;
  baseline identity `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`.
  Metadata commit and tested specs commit are different.
  [Pinned descriptor](runs/20261030-94b316787/selected-descriptor.json).
- Policy: `scope: source`, no filter/limit, `frozen-reference`, target-only,
  concurrency 2, native budget 7,200 seconds. Native execution took about
  23 minutes; setup, full baseline copying/hash verification and final integrity
  checks were additional. Saved Swagger is a historical reference, not newly
  re-emitted or proven identical under the candidate's changed runtime.
- Project guardrails: Swagger findings in 121 projects, TypeSpec findings in 128,
  overlap 113, Swagger-only 8, TypeSpec-only 15. Raw-count direction:
  Swagger higher in 27 projects, TypeSpec higher in 56. Conservative location
  summaries are 431 Swagger paths and 935 TypeSpec source locations; these are
  different identity domains, not normalized actionable counts.
- Loaded compiler `1.17.0`, ARM `0.73.0`, AutoRest emitter `0.73.2`,
  Node `26.5.0`, specs pnpm `12.6.0`.
  [Actual loaded package hashes](runs/20261030-94b316787/loaded-packages.json)
  matched the packed candidate artifacts in every successful worker.
- Audience: explicitly enabled ARM analysis; the TypeSpec linter is a warning,
  registered but disabled in the shared resource-manager ruleset. It does not
  automatically distinguish ARM from data-plane services in a mixed program.
  Other PATCH rules and their overlapping diagnostics remain unchanged.
- The target-only corpus run did not execute configured/default activation:
  those findings remain null/unassessed for all 487 projects, not zero.
  The ten separately configured PATCH controls verify default disablement.
- Member notes: [required/default/visibility](members/PatchBodyParametersSchema/migration.md),
  [layout](members/ConsistentPatchProperties/migration.md),
  [immutable properties](members/UnSupportedPatchProperties/migration.md).
  [Historical fixtures](fixture-differences.md) and their older 468-project
  corpus remain historical; aggregate changes across different populations
  are not measured regressions.
- [Provenance, durable assets and recovery](fresh-evidence.md).
  Source preservation uses the verified existing specs-fork ref at the exact
  frozen SHA. Reading/recounting saved observations is distinct from rerunning
  native diagnostics. No Swagger generation, production edits, enablement
  changes, review replies or thread resolution were performed.

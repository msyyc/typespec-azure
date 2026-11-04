# specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI

[All project differences](../instance-correspondence.md#differing-projects).

**Project totals:** Swagger 1 raw / 1 member checks; TypeSpec 0 raw; 0 findings credited to the same comparison. Common project/route unit: 1 Swagger / 0 TypeSpec. Counts repeated across different members at the same operation are non-additive.

<a id="s-5855bd5b6e6f7223"></a>

### PutRequestResponseSchemeArm: SqlVulnerabilityAssessmentBaselineRules_CreateOrUpdate

**Identity:** `5855bd5b6e6f7223`; `/{resourceId}/providers/Microsoft.Security/sqlVulnerabilityAssessments/default/baselineRules/{ruleId}`.
**Swagger document:** `projects/specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI/swagger/preview/2026-04-01-preview/security-SqlVulnerabilityAssessments.json`.
**Cause:** PUT stored under lists rather than lifecycle.createOrUpdate.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation                                     | Request schema                   | Success response schemas                                         |
| -------------------------------------------------------------- | -------------------------------- | ---------------------------------------------------------------- |
| `put` `SqlVulnerabilityAssessmentBaselineRules_CreateOrUpdate` | `#/definitions/RuleResultsInput` | `200: #/definitions/RuleResults; 201: #/definitions/RuleResults` |

| TypeSpec operation                                                                                                                                                                                                                                                                                          | Effective request                                 | Canonical association / request checked                                           | Registered return candidates                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------- |
| [SqlVulnerabilityAssessmentsAPI.SqlVulnerabilityAssessmentBaselineRules.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI/RuleResults.tsp#L87) | `SqlVulnerabilityAssessmentsAPI.RuleResultsInput` | `SqlVulnerabilityAssessmentsAPI.RuleResults: lists.createOrUpdate; request=False` | `SqlVulnerabilityAssessmentsAPI.RuleResults` |

**Explanation:** The operation is associated through lists. Existing response traversal visits it, but the new request branch does not.

**Disposition:** TypeSpec rule update required: cover PUT request comparisons stored by legacy/list registration; add violating and compliant legacy-template fixtures.

**Raw observation IDs:** `PutRequestResponseSchemeArm:185`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

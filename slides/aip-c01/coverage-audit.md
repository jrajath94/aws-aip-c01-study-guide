# AIP-C01 deck coverage audit

Source: the 200 example questions in the repo question bank. Each row maps one question ID to the slide that teaches its topic. Slide IDs match `project/slides/<id>.html`.

## Result

- Questions mapped: 200 of 200.
- Questions with no slide: 0.
- Mapped slides that do not exist as files: 0 (checked with a script before commit).
- Coverage means the slide teaches the topic and the trap. It does not mean the slide repeats the question wording.

## Domain 1 (61 questions)

| Question | Slide | Question | Slide |
|---|---|---|---|
| q-d1-001 | d1-kb | q-d1-033 | d1-hybrid-rerank |
| q-d1-002 | d1-solution-design | q-d1-034 | d1-embedding-dimensions |
| q-d1-003 | d1-solution-design | q-d1-035 | d1-query-rewrite |
| q-d1-004 | d1-behavior-knowledge | q-d1-036 | d1-chunking-change |
| q-d1-005 | d1-constraints | q-d1-037 | d1-chunking-change |
| q-d1-006 | d1-constraints | q-d1-038 | d1-embedding-dimensions |
| q-d1-007 | d1-t12-resilience | q-d1-039 | d1-mcp-tools |
| q-d1-008 | d1-cross-region | q-d1-040 | d1-t16-prompts |
| q-d1-009 | d1-routing-mechanisms | q-d1-041 | d2-prompt-mgmt |
| q-d1-010 | d4-capacity | q-d1-042 | d1-flows-vs-sfn |
| q-d1-011 | d1-cross-region | q-d1-043 | d1-structured-output |
| q-d1-012 | d1-customize-ladder | q-d1-044 | d1-model-lifecycle |
| q-d1-013 | d1-model-lifecycle | q-d1-201 | d1-chunking-tables |
| q-d1-014 | d1-t12-resilience | q-d1-202 | d1-embedding-dimensions |
| q-d1-015 | d1-data-tools | q-d1-203 | d1-hybrid-rerank |
| q-d1-016 | d1-data-tools | q-d1-204 | d1-query-rewrite |
| q-d1-017 | d1-service-distractors | q-d1-205 | d1-behavior-knowledge |
| q-d1-018 | d1-service-distractors | q-d1-206 | d1-vector-scale |
| q-d1-019 | d1-data-tools | q-d1-207 | d1-chunking-tables |
| q-d1-020 | d1-invoke-converse | q-d1-208 | d1-customize-ladder |
| q-d1-021 | d1-kb | q-d1-209 | d1-data-tools |
| q-d1-022 | d1-tenant-isolation | q-d1-210 | d1-tenant-isolation |
| q-d1-023 | d1-service-distractors | q-d1-211 | d1-routing-mechanisms |
| q-d1-024 | d1-t14-vector | q-d1-212 | d1-t12-resilience |
| q-d1-025 | d1-kb-sources | q-d1-213 | d1-solution-design |
| q-d1-026 | d1-citations | q-d1-214 | d1-kb-sources |
| q-d1-027 | d1-t14-vector | q-d1-215 | d1-cross-region |
| q-d1-028 | d1-tenant-isolation | q-d1-216 | d1-citations |
| q-d1-029 | d1-tenant-isolation | q-d1-217 | d1-kb |
| q-d1-030 | d1-chunking-change | | |
| q-d1-031 | d1-chunking-tables | | |
| q-d1-032 | d1-chunking-tables | | |

## Domain 2 (51 questions)

| Question | Slide | Question | Slide |
|---|---|---|---|
| q-d2-001 | d2-agent-aliases | q-d2-019 | d2-endpoints |
| q-d2-002 | d2-action-group-auth | q-d2-020 | d2-sfn-events |
| q-d2-003 | d2-multi-agent | q-d2-021 | d2-onprem |
| q-d2-004 | d2-agent-memory | q-d2-022 | d2-gateway-access |
| q-d2-005 | d2-human-approval | q-d2-023 | d5-cicd |
| q-d2-006 | d2-lambda-limits | q-d2-024 | d2-gateway-access |
| q-d2-007 | d2-agent-frameworks | q-d2-025 | d3-audit-lineage |
| q-d2-008 | d2-mcp-hosting | q-d2-026 | d2-converse-embeddings |
| q-d2-009 | d2-agentcore | q-d2-027 | d2-converse-embeddings |
| q-d2-010 | d2-agent-frameworks | q-d2-028 | d2-converse-embeddings |
| q-d2-011 | d2-agent-safeguards | q-d2-029 | d2-streaming-paths |
| q-d2-012 | d2-agent-tracing | q-d2-030 | d4-capacity |
| q-d2-013 | d2-spiky-batch | q-d2-031 | d2-applyguardrail |
| q-d2-014 | d2-spiky-batch | q-d2-032 | d2-converse-embeddings |
| q-d2-015 | d2-batch | q-d2-033 | d2-apps-q |
| q-d2-016 | d2-endpoints | q-d2-034 | d1-data-tools |
| q-d2-017 | d1-routing-mechanisms | q-d2-035 | d2-apps-q |
| q-d2-018 | d2-endpoints | q-d2-036 | d2-apps-q |
| q-d2-201 | d2-multi-agent | q-d2-209 | d2-apps-q |
| q-d2-202 | d2-agentcore | q-d2-210 | d1-flows-vs-sfn |
| q-d2-203 | d2-mcp-hosting | q-d2-211 | d2-gateway-access |
| q-d2-204 | d2-converse-embeddings | q-d2-212 | d2-batch |
| q-d2-205 | d2-agent-tracing | q-d2-213 | d2-action-group-auth |
| q-d2-206 | d2-human-approval | q-d2-214 | d1-flows-vs-sfn |
| q-d2-207 | d2-agent-memory | q-d2-215 | d2-human-approval |
| q-d2-208 | d2-streaming-paths | | |

## Domain 3 (41 questions)

| Question | Slide | Question | Slide |
|---|---|---|---|
| q-d3-001 | d3-denied-topics | q-d3-021 | d3-audit-lineage |
| q-d3-002 | d3-sensitive | q-d3-022 | d3-continuous-fairness |
| q-d3-003 | d3-word-filters | q-d3-023 | d3-continuous-fairness |
| q-d3-004 | d3-prompt-attacks | q-d3-024 | d3-transparency-fairness |
| q-d3-005 | d3-grounding | q-d3-025 | d5-judge |
| q-d3-006 | d3-grounding | q-d3-026 | d3-transparency-fairness |
| q-d3-007 | d3-defense | q-d3-027 | d3-transparency-fairness |
| q-d3-008 | d3-guardrails | q-d3-028 | d3-rai |
| q-d3-009 | d3-governance | q-d3-201 | d3-guardrails |
| q-d3-010 | d3-limits | q-d3-202 | d3-guardrails |
| q-d3-011 | d3-privatelink | q-d3-203 | d3-grounding |
| q-d3-012 | d3-pii-pipeline | q-d3-204 | d3-org-governance |
| q-d3-013 | d3-pii-pipeline | q-d3-205 | d3-privatelink |
| q-d3-014 | d3-pii-pipeline | q-d3-206 | d3-pii-pipeline |
| q-d3-015 | d3-logging-privacy | q-d3-207 | d3-logging-privacy |
| q-d3-016 | d3-sensitive | q-d3-208 | d3-scope-cross-region |
| q-d3-017 | d3-governance | q-d3-209 | d3-defense |
| q-d3-018 | d3-data | q-d3-210 | d3-continuous-fairness |
| q-d3-019 | d3-lake-model-cards | q-d3-211 | d3-prompt-attacks |
| q-d3-020 | d3-audit-lineage | q-d3-212 | d3-detect-mode |
| | | q-d3-213 | d3-logging-privacy |

## Domain 4 (25 questions)

| Question | Slide | Question | Slide |
|---|---|---|---|
| q-d4-001 | d4-prompt-cache | q-d4-010 | d4-sampling |
| q-d4-002 | d4-capacity | q-d4-011 | d4-sampling |
| q-d4-003 | d4-model-right | q-d4-012 | d4-retrieval-latency |
| q-d4-004 | d4-batch-tiers | q-d4-013 | d4-attribution-anomaly |
| q-d4-005 | d4-cost-levers | q-d4-014 | d4-attribution-anomaly |
| q-d4-006 | d4-semantic-cache | q-d4-015 | d4-tracing-monitor |
| q-d4-007 | d4-cost-levers | q-d4-016 | d4-tracing-monitor |
| q-d4-008 | d4-sampling | q-d4-017 | d4-tracing-monitor |
| q-d4-009 | d4-latency | q-d4-201 | d4-capacity |
| q-d4-202 | d4-prompt-cache | q-d4-205 | d4-attribution-anomaly |
| q-d4-203 | d4-model-right | q-d4-206 | d4-semantic-cache |
| q-d4-204 | d1-vector-scale | q-d4-207 | d4-throttle |
| | | q-d4-208 | d4-capacity |

## Domain 5 (22 questions)

| Question | Slide | Question | Slide |
|---|---|---|---|
| q-d5-001 | d5-methods-budget | q-d5-010 | d5-debug-table |
| q-d5-002 | d5-judge | q-d5-011 | d5-debug-table |
| q-d5-003 | d5-subjective | q-d5-012 | d5-debug-table |
| q-d5-004 | d5-rag-metrics | q-d5-013 | d5-debug-table |
| q-d5-005 | d5-regression-cicd | q-d5-014 | d5-debug-table |
| q-d5-006 | d5-subjective | q-d5-015 | d5-debug-table |
| q-d5-007 | d5-methods-budget | q-d5-201 | d5-rag-metrics |
| q-d5-008 | d5-subjective | q-d5-202 | d5-rag-metrics |
| q-d5-009 | d5-debug-table | q-d5-203 | d5-judge-calibration |
| | | q-d5-204 | d5-methods-budget |
| | | q-d5-205 | d5-methods-budget |
| | | q-d5-206 | d5-debug-table |
| | | q-d5-207 | d5-methods-budget |

## Not covered by a question in the bank

The question bank does not test these topics. The deck covers them as study material from the repo and AWS domain pages. See the gap slides for the "Not in source" items.

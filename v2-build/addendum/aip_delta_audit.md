# AIP-C01 Addendum Delta Audit v1.0

Research date: 2026-10-06. Scope: v2-build fragments (d1/d2/d3/d4d5/stage8/qbank), stage1 ledger and maps. Method: direct inspection of built HTML. Every P01-P33 row and G01-G20 row below rests on text found or not found in the fragments. Learner state is UNKNOWN for every row: no learner data exists, and this audit did not observe the learner.

## Identity check

The workspace holds the AWS Certified Generative AI Developer Professional (AIP-C01) v2 rebuild. Fragment set: L0-L11 lessons, Stage 8 matrices/drills/L12/troubleshooting, 60-question bank. The addendum applies cleanly. No restart, no renumber, no artifact deleted.

## Content states used

ADEQUATE: mechanism plus distinction plus example plus assessment exist. PARTIAL: one exact element is absent. ABSENT: verified necessary concept is not taught. WRONG-STALE: a taught claim needs a sourced correction. OPTIONAL: not needed for AIP decisions. UNKNOWN: evidence was inaccessible.

## Prerequisite audit: P01-P33

| Delta | Candidate | State | Learner | Existing location | Exact missing element | Decision that fails without it | Planned addition |
|---|---|---|---|---|---|---|---|
| P01 | Numeracy for AI/cloud | PARTIAL | UNKNOWN | L0/L1/L10 teach tokens, ratios, prices, p50/p95/p99 | Log scale at meaning level (order of magnitude) | Cost comparisons across 10x model prices (Q25/Q48 stems) | Bridge B-P01 |
| P02 | Resource vocabulary | PARTIAL | UNKNOWN | L0: Region/AZ, L9: VPC/endpoints, L1/L6: managed vs self-hosted | ARN anatomy, control plane vs data plane | 3.2.1/4.3.3: CloudTrail records data-plane API calls (L10 names it, never defines it), reading ARNs in policies | Bridge B-P02 |
| P03 | Shared responsibility | ABSENT | UNKNOWN | None found | Customer duties (config, access, data) vs provider duties (physical, hypervisor, managed service operation) | 3.3.3: vendor eligibility is not application compliance, why Guardrails do not certify legal compliance | Bridge B-P03 |
| P04 | Reliability | PARTIAL | UNKNOWN | L1: resilience/degradation ladder, L2: gateway resilience | Availability vs durability, RTO/RPO, backup vs replication | 1.2.3/2.4.3: replication and backup address different failures | Bridge B-P04 |
| P05 | Credentials/roles | PARTIAL | UNKNOWN | L0: Effect/Action/Resource, least privilege, L9: trust policy, external ID | Assume-role flow (STS AssumeRole to temporary credentials), execution role, signing purpose, SDK Region choice | 2.1.3 agent execution roles, 2.3.3 least-privilege FM access, confused-deputy fix mechanism | Bridge B-P05 |
| P06 | Policy evaluation | ADEQUATE | UNKNOWN | L9 full teach: five checkpoints, Alice worked eval, deny-source drill | None | None. Link only. | None |
| P07 | Data authorization | PARTIAL | UNKNOWN | L7: RBAC, L9: confused deputy + external ID, L3: tenant metadata filters | ABAC at meaning level, document-level permission model | 3.2.1 granular data access, 1.4.2 metadata-driven access control naming | Bridge B-P07 |
| P08 | Encryption/secrets | ADEQUATE | UNKNOWN | L9 full teach: envelope encryption, data key vs KMS key, rotation, key deletion | None | None. Link only. | None |
| P09 | Network path | ADEQUATE | UNKNOWN | L9 full teach: VPC, subnets, SG vs NACL, interface vs gateway endpoints, endpoint policies | None | None. Link only. | None |
| P10 | Residency | PARTIAL | UNKNOWN | L9: "A VPC endpoint keeps traffic private. It never moves data residency. The Region does that.", L1: cross-region compliance flag | Private path vs processing geography boundary for Bedrock, see G09 correction | C05/C06 decisions, Q27 as built is ambiguous on this exact point | Patch P-G09 (correction) |
| P11 | Compute | PARTIAL | UNKNOWN | L0: Lambda/EC2/Step Functions ladder, L6: GPU memory sizing | Cold starts, statelessness of Lambda | 2.2.2 LLM deployment challenges, streaming UX design | Bridge B-P11 |
| P12 | Storage patterns | PARTIAL | UNKNOWN | L0/L3: S3, DynamoDB, ElastiCache, vector index vs transactional truth | Block/file/key-value/relational one-liners (EBS/EFS/RDS roles) | 1.4.1 vector DB architecture choice, model-weight storage | Bridge B-P12 |
| P13 | Object/data lifecycle | PARTIAL | UNKNOWN | L2: S3 source of truth, L9: lifecycle rules age data out | Object/key/version/metadata anatomy, deletion-layer differences (object vs index vs cache vs log) | 1.4.5 maintenance, 3.2.2 retention, erasure paths (Q20) | Bridge B-P13 |
| P14 | Conversation state | PARTIAL | UNKNOWN | L5: DynamoDB session state, summary memory, delete path | Conditional writes, TTL as expiry, not an authorization boundary | 2.1.1 agent memory correctness under concurrent writes | Bridge B-P14 |
| P15 | APIs/SDKs | ADEQUATE | UNKNOWN | L6: Converse unified schema, SDK sync/streaming clients, SQS async, WebSocket/SSE browser UX, gateway limits | None | None. Link only. | None |
| P16 | Interaction patterns | ADEQUATE | UNKNOWN | L6/L7: sync/async/stream, SQS, EventBridge, webhooks, queue-backpressure worked example | SNS one-liner only (alert fan-out) | 4.3.2 alerting, minor | Bridge B-P16 (one-liner) |
| P17 | Failure semantics | ADEQUATE | UNKNOWN | L5/L6/L7/L10: timeout, retry, backoff, jitter, idempotency, DLQ, backpressure, circuit breaker, fallback | None | None. Link only. | None |
| P18 | Orchestration | PARTIAL | UNKNOWN | L0/L4/L5: Step Functions waits, branching, approval gates, max steps | Task/catch/retry by name, agent reasoning does not replace workflow enforcement | 2.1.2/2.1.3: ReAct vs enforced orchestration, error handling in chains | Bridge B-P18 |
| P19 | Config/prompt lifecycle | PARTIAL | UNKNOWN | L1: AppConfig config-driven routing, L4: Prompt Management versions/approvals | Parameter Store, Secrets Manager, config vs secret vs prompt separation | Secret storage (Q28 stem: a release leaked a test API key) | Bridge B-P19 |
| P20 | AI task families | PARTIAL | UNKNOWN | L0/L1: GenAI adaptation ladder (prompt/RAG/fine-tune) | AI/ML/DL/GenAI naming, learning modes, training vs inference | 1.1.1/1.2.1: use GenAI only when probabilistic generation fits | Bridge B-P20 |
| P21 | FM mechanics | PARTIAL | UNKNOWN | L0: tokens, context, embeddings, temperature/top-p/top-k | Logits, model parameters at meaning level | 4.2.4 sampling tuning (what temperature acts on), 1.2.4 LoRA ("trains two small matrices" of what) | Bridge B-P21 |
| P22 | Adaptation | PARTIAL | UNKNOWN | L0/L1: prompt/RAG/fine-tune/LoRA choice level, facts vs behavior rule | SFT vs continued pre-training vs distillation, named | 1.2.4 customization lifecycle method choice | Bridge B-P22 |
| P23 | Statistical validity | PARTIAL | UNKNOWN | L11: golden dataset, holdout set, leakage (with figure) | Train/validation/test naming, overfit, baseline, shift | 5.1.2 eval design, why a holdout stays locked | Bridge B-P23 |
| P24 | Metric basics | ADEQUATE | UNKNOWN | L11: precision/recall/F1 toy, nDCG/MRR | None | None. Link only. | None |
| P25 | Responsible AI | ADEQUATE | UNKNOWN | L9 full teach: bias, privacy, transparency, safety, uncertainty, human review, A2I | None | None. Link only. | None |
| P26 | Formats and data quality | PARTIAL | UNKNOWN | L2: schema validity, dedup worked example, completeness/freshness | JSONL/CSV/Parquet/media one-liners | 1.3.2 processing pipelines, fine-tune data prep formats | Bridge B-P26 |
| P27 | Processing services | PARTIAL | UNKNOWN | L2: Glue Data Quality, SageMaker Processing, Transcribe, Textract, Comprehend, L7: BDA | Data Wrangler one-liner | 1.3.1 data validation workflow choice | Bridge B-P27 |
| P28 | SageMaker lifecycle | PARTIAL | UNKNOWN | L1: Processing, fine-tune, Model Registry, endpoints, rollback/retire, L9: Clarify | Model Monitor, human labeling loop for training data | 1.2.4 lifecycle monitoring, 5.1.3 annotation | Bridge B-P28 |
| P29 | Deployment | ADEQUATE | UNKNOWN | L6: on-demand/provisioned/batch/SageMaker real-time/serverless/async, L1: registry versions | None | None. Link only. | None |
| P30 | Change delivery | PARTIAL | UNKNOWN | L1: model registry versions, L4: prompt versions pinned with model, L7: CodePipeline/CodeBuild, canary, rollback | IaC one-liner | 2.3.5 CI/CD as code | Bridge B-P30 |
| P31 | Observability | ADEQUATE | UNKNOWN | L10 full teach: metrics/logs/traces/audit, correlation IDs, dashboards, anomaly detection | None | None. Link only. | None |
| P32 | Capacity | PARTIAL | UNKNOWN | L6/L10: provisioned throughput, quotas (named), p50/p95/p99 toy, utilization, concurrency | Quota vs rate vs concurrency vs capacity distinctions, quota increase does not prove p99 | 4.1.3/4.2.5 capacity planning | Bridge B-P32 |
| P33 | Conditional service recognition | ADEQUATE | UNKNOWN | Inline one-liners throughout L0-L11 | None | None. Link only. | None |

## Core-gap audit: G01-G20

| Delta | Official anchor | State | Learner | Existing location | Exact missing element | Decision that fails without it | Planned addition |
|---|---|---|---|---|---|---|---|
| G01 | 1.1.3 | PARTIAL | UNKNOWN | L1: reusable components, Well-Architected GenAI Lens review | Decision records across environments, compatibility and policy validation | 1.1.3: why the tenth deployment matches the first | Patch P-G01 |
| G02 | 1.2.2 | PARTIAL | UNKNOWN | L1: config-driven routing (AppConfig), Converse normalized contract (Q7), circuit-breaker failure semantics | Capability detection when switching provider/model/Region | 1.2.2: recheck feature/API/template/quota compatibility (C09) | Patch P-G02 |
| G03 | 1.4.2 | PARTIAL | UNKNOWN | L3: S3 object metadata, custom attributes, tags, DynamoDB document metadata, tenant filters at retrieval | Ingestion sidecars as a third mechanism, provenance schema (author/timestamp/tenant) design | 1.4.2: metadata vs tags vs sidecars are distinct mechanisms | Patch P-G03 |
| G04 | 1.4.3-1.4.5 | PARTIAL | UNKNOWN | L3: sharding, multi-index, incremental sync, change detection, scheduled refresh, Q11: embedding change without reindex | Delete propagation (object delete vs index delete vs cache purge vs log retention), embedding-model change forces full reindex | 1.4.5: stale index serves stale facts, erasure (Q20) | Patch P-G04 |
| G05 | 1.6.2 | PARTIAL | UNKNOWN | L4: Step Functions clarification workflow, Comprehend intent, DynamoDB turn history | Bounded clarification turns, do not call tools until intent is clear | 1.6.2: when ambiguity needs another question vs a tool call | Patch P-G05 |
| G06 | 1.6.3-1.6.6 | PARTIAL | UNKNOWN | L4: Prompt Management versions/approvals, Prompt Flows branching, native-vs-custom (S3) comparison | Prompt A/B testing: native vs custom split mechanism | 1.6.4: verify a prompt change before it becomes default | Patch P-G06 |
| G07 | 2.1.4 | ADEQUATE | UNKNOWN | L5: router, ensemble with custom aggregation, selection framework, small-to-big rule | None | None. Link only. | None |
| G08 | 2.1.5 | PARTIAL | UNKNOWN | L5: approval gate for irreversible actions, Step Functions holds the wait | Review state, artifacts, timeout/escalation, exact action binding beyond yes/no approval | 2.1.5: human expertise workflow, not a bare approve button | Patch P-G08 |
| G09 | 2.3.4 | PARTIAL + WRONG-STALE | UNKNOWN | L7: Outposts = data residency, Wavelength = edge latency, L9: endpoint privacy vs Region residency | Bedrock is a regional service, it does not run natively on Outposts. Private path protects transit only, inference still executes in-Region. L7 check Q1 answer and Q27 explanation overstate the claim. | C05/C06: network path and processing location are separate, the built Q27 is ambiguous on this exact point | Patch P-G09 (correction), in-place fix of Q27 in qbank.html |
| G10 | 2.5.2 | ADEQUATE | UNKNOWN | L7: Amplify declarative UI, OpenAPI contract, Prompt Flows no-code builder | None | None. Link only. | None |
| G11 | 2.5.3/2.5.4/2.5.6 | PARTIAL | UNKNOWN | L7: BDA orchestration, Q Developer code/test/error-pattern roles, Logs Insights + X-Ray troubleshooting | Q Developer assistance vs verified diagnosis: it suggests, tests and traces verify | 2.5.6: an AI suggestion is not a diagnosis | Patch P-G11 |
| G12 | 3.1.2-3.1.4 | PARTIAL | UNKNOWN | L8: input/output filters, grounding, defense in depth, JSON schema rule (referenced by L11) | Deterministic execution vs probabilistic interpretation, text-to-SQL still needs authorization, validation, and execution checks | 3.1.2: generated SQL is not authorized execution | Patch P-G12 |
| G13 | 3.3.1-3.3.4 | PARTIAL | UNKNOWN | L9: CloudTrail audit, model cards, Glue Data Catalog, metadata tags, decision logs, A2I, retention | Lineage as audit evidence: Glue lineage plus catalog plus decision logs as one evidence chain | 3.3.1/3.3.2: evidence required for lineage/compliance, not a service list | Patch P-G13 |
| G14 | 3.4.1-3.4.3 | PARTIAL | UNKNOWN | L9: transparency, confidence/uncertainty, evidence citation, inspectable traces, fairness metrics, LLM-as-a-judge, Clarify | Traces are not proof of correctness, native vs custom uncertainty/fairness metrics boundary | 3.4.1: an inspectable trace can still mislead | Patch P-G14 |
| G15 | 4.1.4 | PARTIAL | UNKNOWN | L10: prompt/semantic/deterministic/edge caching, fingerprinting, invalidation, tenant-key rule | Hash collisions and normalization for deterministic request hashing | 4.1.4: when two different requests share one hash | Patch P-G15 |
| G16 | 4.2.1 | ADEQUATE | UNKNOWN | L10: pre-compute for predictable queries, cache serve, benchmark rule (p50/p95, never the mean) | None | None. Link only. | None |
| G17 | 4.3.4/4.3.5 | ADEQUATE | UNKNOWN | L10: tool usage baselines with deviation alarms, index latency/shard health, scheduled reindex, data-quality validation | None | None. Link only. | None |
| G18 | 5.1.3/5.1.8 | PARTIAL | UNKNOWN | L11: feedback interfaces, ratings, annotation into the golden set, ship-collect-label-retest loop | Feedback biases, stakeholder comparison reports, measurable action per finding | 5.1.3/5.1.8: feedback is data with bias, not truth | Patch P-G18 |
| G19 | 5.1.9 | PARTIAL | UNKNOWN | L11: synthetic user workflows, hallucination-rate checks, semantic drift checks, consistency checks | Jointly versioned deployment gates: model plus prompt plus index pinned as one release | 5.1.9: a model upgrade with a stale index is not a tested release | Patch P-G19 |
| G20 | 5.2.3/5.2.5 | ADEQUATE | UNKNOWN | L11 playbooks: prompt-version confusion, schema failures, trace-log diagnostics, version-pin checks | None | None. Link only. | None |

## Question-bank audit: C01-C30 axis coverage (60 built questions)

Method: each question mapped to its primary trap axis by the decision it tests. Stage 8 minimal-pair drills (Pairs A-F) and L12 worked scenarios (W1-W6) add transfer practice on top, the mapping below counts the bank only.

Covered axes with question IDs: C01: Q6, Q21, Q31, Q36, Q51. C02: Q4, Q18, Q25, Q46, Q48. C03: Q26. C04: Q22, Q33. C05: Q27, Q40. C06: Q2. C07: Q38. C08: Q17. C09: Q2, Q7. C10: Q23, Q24, Q47, Q50. C11: Q55. C12: Q29, Q49. C13: Q9, Q10, Q12, Q13. C14: Q53, Q56. C15: Q11, Q20, Q56. C17: Q32. C18: Q39. C19: Q1, Q5, Q35, Q58, Q59. C20: Q44, Q52, Q57. C21: Q14, Q45. C22: Q30. C24: Q16, Q28, Q41, Q45, Q60. C25: all multi-select items (Q2, Q5, Q12, Q17, Q27, Q28, Q30, Q37, Q39, Q41, Q45, Q49, Q51, Q53, Q58, Q60). C26: Q8. C27: Q15, Q19, Q34, Q37, Q42, Q54.

Absent axes (no bank coverage): C16 (shared cache to per-tenant answers, hit-time authorization), C23 (fallback to a different contract/safety/Region, graceful degradation must preserve mandatory requirements), C28 (current supported feature vs stale training-guide assumption), C29 (semantically equivalent paraphrase, mechanism transfer), C30 (contradictory hard requirements, identify infeasibility).

Thin axes (one item each, acceptable, no new items planned): C03, C07, C11, C17, C22.

Builder-flagged items reviewed: Q51 (key A,B, lens-pairing item, defensible), Q24 (key B, provisioned-plus-on-demand, defensible), Q13 (key B, decomposition, defensible), Q25/Q48 (kept distinct: Q25 tests 2.2.3 confidence-escalation cascade in D2, Q48 tests 4.1.2 classifier-routed tiering in D4, different skills, different mechanisms), Q39 (keys A,B, input detection plus output redaction, defensible).

Adversarial answer-key review: separate self-audit pass, 2026-10-06. Every distractor in all 60 items was attacked for hidden correctness (service/API/Region/model support, quota/pricing scope, permission layers, processing geography, retry/state ambiguity, managed vs custom, freshness/authorization, latency assumptions, set sufficiency/cardinality, unstated assumptions). Findings: 59 items hold their keys. One item fails: Q27 (Select TWO, D2). Its explanation claims "Outposts keeps processing local" while the stem demands Bedrock models for generation, Bedrock inference executes in an AWS Region, not on Outposts, so the A+B set rests on an ambiguous reading of "data must stay in the hospital data center" (at rest vs at processing). Fix applied in place in qbank.html: stem now pins the constraint to data at rest plus prompt transit, and the explanation states the in-Region processing boundary explicitly. L7 check Q1 in d2-lessons.html carries the same overstatement, it is not edited in place per the no-fragment-edit rule. It ships as correction patch P-G09 with an exact anchor. No item is marked UNRELEASED.

## Totals

ADEQUATE (link only): P06, P08, P09, P15, P17, P24, P25, P29, P31, P33, G07, G10, G16, G17, G20. PARTIAL: 18 prerequisites (bridges B-P01..B-P32 as listed), 13 core gaps (patches P-G01..P-G19 as listed). ABSENT: P03 (bridge B-P03). WRONG-STALE: G09/P10 boundary (correction patch P-G09, Q27 fixed in place). OPTIONAL: none claimed, SNS one-liner rides inside B-P16. UNKNOWN: none, every row was inspected.

# AIP-C01 Question Pattern Intelligence

**Exam:** AWS Certified Generative AI Developer – Professional (AIP-C01)
**Researched:** 2026-09-28
**Purpose:** PATTERN INTELLIGENCE for the study-guide build. No question was copied verbatim from any copyrighted bank. Every pattern below is an original analysis of *how* questions are constructed: topic → concept tested → phrasing shape → trap design → services combined.

---

## 0. Source inventory and honesty note

This exam launched late 2025, so the public corpus is thin and noisy. What I mined:

| Source | What it is | Reliability note |
|---|---|---|
| 107-question bank mirrored across ~9 dump sites (bootdumps, dumpsdownload, vcecollection, dumpsolutions, dumpscollection, dumps-files, prep4away, pass4lead, actualtestpdf demo PDF) | All share ONE underlying question bank (same stems, same option letters). | **Marked answers are unreliable** — several look like truncation artifacts (single-letter answers on 16-option questions). Use for *patterns only*, never trust the stated answer. |
| GitHub `phamhoangha/aip-c01-lesson-learned` — 20 original practice questions (CC BY 4.0, author states they are original works) | Best-structured pattern source: each question names what it tests and the services it touches. | Higher trust; conceptual, not recalled-real items. |
| SkillCertExams sample page (2 full sample stems) | Pattern-consistent with the 107-bank style. | Moderate. |
| certsmania PDF ("shared by Bernard") | Full stems + guardrail-focused. | Moderate. |
| Candidate writeups: dev.to/Makendrang (passed beta in 2 weeks, Early Adopter), dev.to/muswain (12-cert journey, took AIP-C01 beta Mar 2026), kodekloud study guide, certempire exam guide, dev.to/aiarch_wibo ("the exam, explained") | Confirm exam *feel*: heavily scenario-based, lengthy stems, 750/1000 pass mark, multiple-response items with **no partial credit**, ~50% typical pro-level pass rate. | High trust for exam feel; no real items disclosed. |

**Bottom line:** ~120 question-stems analyzed. The patterns below repeat across independent sources, which is why they are the safest thing to teach.

---

## 1. Pattern catalog (20 analyzed patterns)

Each pattern: **Topic** → concept really tested → phrasing shape → the trap → services combined.

### P1. Hallucination fix: grounding, not filtering
- **Topic:** RAG / hallucination mitigation (D1, D5)
- **Concept:** A model inventing products not in the catalog is a *grounding* failure, not a safety-policy failure.
- **Phrasing shape:** Scenario: app uses Bedrock + Claude, recommends products; users complain recommendations are unavailable or irrelevant; investigation finds most interactions are unique and recommended products are not in the catalog. → "Which solution will meet this requirement?"
- **The trap:** Every option sounds right — Guardrail grounding, Automated Reasoning checks, prompt engineering to restrict responses, response caching, streaming. The trap is that *guardrails* feel like the answer for "wrong content," but grounding to a catalog is a retrieval problem. Options also tempt with *validating recommendations against the catalog* (post-hoc validation), which is weaker than RAG + rerank.
- **Services combined:** Bedrock Knowledge Bases + OpenSearch vector store + Bedrock Rerank API + PerformanceConfigLatency.

### P2. The provisioned-throughput code bug
- **Topic:** Provisioned throughput vs on-demand invocation (D4, D2)
- **Concept:** Provisioned throughput only works when you invoke the *provisioned model ARN*; passing the base model ID routes to on-demand and gets throttled.
- **Phrasing shape:** Metrics show provisioned capacity unused while on-demand requests are throttled. Code block shown: `invoke_model(modelId="anthropic.claudev2", ...)`. → "Which solution will meet these requirements?"
- **The trap:** Options offer *more* provisioned throughput (raise model units), exponential backoff, or switching to streaming. All dodge the real bug: the ARN. Also tests knowing `CreateProvisionedModelThroughput` returns a distinct ARN.
- **Services combined:** Bedrock `CreateProvisionedModelThroughput` API + `bedrock-runtime` InvokeModel + CloudWatch `InvocationThrottled`/token metrics.

### P3. Intelligent prompt routing vs hand-rolled routing
- **Topic:** Cost optimization via model routing (D4)
- **Concept:** Split traffic by complexity — small cheap model for simple queries, big capable model for hard ones — using Bedrock *intelligent prompt routing* instead of custom plumbing.
- **Phrasing shape:** 70% simple product questions / 30% complex reasoning questions. Requirement: cost-effective auto-routing, maintain satisfaction, minimize latency. → "...with the LEAST implementation effort?"
- **The trap:** A hand-rolled multi-stage Lambda classifier looks cheaper ("small model classifies complexity"), but it adds operational overhead; a single mid-size model looks simple but wastes money on the 70%. The *rule-based keyword router* is the cheap-looking loser.
- **Services combined:** Bedrock intelligent prompt routing vs Lambda routing logic vs provisioned/on-demand pricing mix.

### P4. The governance mega-bundle
- **Topic:** Responsible AI + observability combo (D3, D5)
- **Concept:** Map each requirement to the right managed service; know which services are *Bedrock-native* vs legacy-ML.
- **Phrasing shape:** Long stem (6-8 requirements): detect/prevent hallucinations, safety controls, drift monitoring, audit trail of all prompt/response pairs, 60-day deadline, integrate with existing dashboard, 200ms response. → "...with the LEAST operational overhead?"
- **The trap:** Options are *service bundles* (4-5 services each). Decoy bundles include SageMaker Model Monitor (classic ML drift — wrong for GenAI), AWS WAF (network filtering — wrong layer), Lambda custom validation (operational overhead), RDS storage of logs (heavy). Correct bundle centers Bedrock Guardrails + Bedrock Model Evaluation + CloudWatch metrics.
- **Services combined:** Bedrock Guardrails, Bedrock Model Evaluation, CloudWatch custom metrics/anomaly detection, DynamoDB/S3 audit storage.

### P5. RAG relevance: hybrid search + rerank
- **Topic:** Retrieval quality for terminology-heavy corpora (D1)
- **Concept:** Pure vector search fails on exact terminology/citations; the fix is *hybrid (vector + keyword) search plus a reranker*.
- **Phrasing shape:** Legal/medical research assistant; must find semantic relationships between domain terms and citations; fast and precise. → "Which solution will meet these requirements?"
- **The trap:** Default KB vector search, query expansion via FM, Kendra query suggestions, custom Lambda merge logic. The pattern tests the triad: hybrid search → rerank model → precise results.
- **Services combined:** Bedrock Knowledge Bases, OpenSearch hybrid search, Bedrock Rerank API, Titan Embeddings.

### P6. RAG ingestion pipeline at scale
- **Topic:** Building a RAG corpus from bulk data with PII removal (D1)
- **Concept:** "Least operational overhead" at scale = serverless orchestration + managed services, not tuning Lambda concurrency by hand and not running EMR clusters.
- **Phrasing shape:** 50GB of JSON in S3, extract relevant data, remove PII, generate embeddings, must finish within 4 hours, cost-effective. → "...with the LEAST operational overhead?"
- **The trap:** Lambda+Comprehend+Bedrock sounds serverless but is a tuning nightmare at 50GB; Glue + SageMaker Processing adds model management; EMR + Comprehend UDFs + Aurora pgvector is the classic "too much machinery" answer. Winner: Step Functions orchestrating Comprehend (PII) + Bedrock (embeddings) + OpenSearch Serverless (vector store).
- **Services combined:** Step Functions, Comprehend PII, Bedrock embeddings, OpenSearch Serverless.

### P7. Bedrock Data Automation for multimodal ingestion
- **Topic:** Multimodal document/media processing (D1)
- **Concept:** Know *when BDA is the anchor service*: mixed file types (PDF, PPTX, Word, video) at volume needing extraction + summarization.
- **Phrasing shape:** 10,000+ sources/day, 500 concurrent uploads, extract key concepts and summaries, realtime collaboration with version control. → "Which solution will meet these requirements?"
- **The trap:** Using Knowledge Bases to "process all multimedia," Guardrails to "extract content," SageMaker endpoints for extraction, Bedrock Agents for change tracking. Winner combines BDA + Textract/Transcribe + S3 versioning + DynamoDB + AppSync subscriptions.
- **Services combined:** Bedrock Data Automation, Textract, Transcribe, S3, AppSync, DynamoDB.

### P8. Latency optimization bundle — Select TWO
- **Topic:** SageMaker LLM endpoint latency (D4)
- **Concept:** First-token latency for interactive chat: *preload the model* (no cold start) + *stream responses*; min instances > 0.
- **Phrasing shape:** Containerized LLM on SageMaker; users abandon after 2s; p95 must be under 800ms. Options list preload, lazy load, dynamic batching, bigger GPU, min-instances 0/1, streaming, async inference. → "Which combination of solutions will meet this requirement? (Select TWO.)"
- **The trap:** Async inference *sounds* like a latency tool but kills interactivity; larger GPU helps throughput not first-token; min instances 0 + per-request processing is the cold-start disaster. "Dynamic batching" is a throughput, not latency, play.
- **Services combined:** SageMaker realtime endpoints, container preload, streaming.

### P9. Flows + Prompt Management + Guardrails — Select TWO
- **Topic:** Structured prompting with safety (D2, D3)
- **Concept:** Two orthogonal mechanisms: *Prompt Management variables* for required inputs/format; *Guardrail in "detect" mode* for notification-without-blocking.
- **Phrasing shape:** Bedrock Flow with Nova Pro; four required inputs; consistent output format; notify on bullying language but do NOT block flagged responses. → "Which additional steps must the company take...? (Select TWO.)"
- **The trap:** Guardrail filter response = block (wrong — the requirement says notify only); hate filter vs insults filter (different content policies); attaching guardrail to the wrong node; prompt *router* (cost optimization — irrelevant).
- **Services combined:** Bedrock Flows, Prompt Management, Bedrock Guardrails (detect vs block).

### P10. Lineage + realtime PII filtering + audit trail
- **Topic:** Data governance pipeline (D1, D3)
- **Concept:** Three distinct jobs need three distinct services: Glue Data Catalog (source registration/lineage), Bedrock Guardrails PII filter (realtime), CloudTrail (audit).
- **Phrasing shape:** Medical/legal GenAI; end-to-end data lineage; realtime PII filtering; audit trails with automated compliance reporting. → "Which solution will meet these requirements?"
- **The trap:** Macie (scans S3 at rest — not realtime inference filtering), AWS WAF (wrong layer for PII), Comprehend Medical with scheduled Lambda (batch, not realtime), Rekognition Custom Labels (nonsense decoy for text PII). Athena "for lineage" is a near-miss.
- **Services combined:** Glue Data Catalog, Bedrock Guardrails PII, CloudTrail, CloudWatch.

### P11. Multi-agent supervisor/collaborator topology
- **Topic:** Bedrock Agents architecture (D2)
- **Concept:** The supervisor classifies intent in natural language and routes to specialized collaborator agents, each grounded on its own knowledge base.
- **Phrasing shape:** Healthcare assistant; departments (clinical, insurance, scheduling, claims); must be scalable, onboard new features, handle thousands of parallel interactions, domain-specific answers. → "Which solution will meet these requirements?"
- **The trap:** A supervisor *per department* with manual handoffs (anti-pattern); a single general-purpose agent with action groups and rule-based routing (doesn't scale cleanly); all agents sharing one KB (loses domain isolation); IAM filtering presented as the routing mechanism (it's access control, not routing).
- **Services combined:** Bedrock Agents (supervisor + collaborators), Knowledge Bases per department, IAM.

### P12. Knowledge Base for semantic + metadata search
- **Topic:** Semantic search over archives (D1)
- **Concept:** Embeddings + managed vector store is the least-overhead path; hand-hosting sentence-transformers on SageMaker is the operational-overhead trap.
- **Phrasing shape:** University archive; search by text + metadata; metadata has no keywords; <1M files. → "...with the LEAST operational overhead?"
- **The trap:** Comprehend topic extraction + Aurora (keyword mindset — misses semantic similarity); SageMaker sentence-transformer + pgvector (correct idea, wrong operations); OpenSearch Neural plugin vs Aurora Serverless pgvector (two managed options — tests store choice).
- **Services combined:** Titan Embeddings (Bedrock), OpenSearch neural search vs Aurora pgvector.

### P13. CI/CD model evaluation with quality gates
- **Topic:** Evaluation + deployment gates (D5)
- **Concept:** Bedrock Model Evaluation jobs (automated, parallel, judge-model) wired into a CI/CD pipeline that *blocks deployment* below quality thresholds.
- **Phrasing shape:** Multilingual assistant; after a model upgrade, inconsistent behavior; evaluation must run 15,000 conversations in parallel, finish in 45 minutes, fully automated, block deployment on failure. → "Which solution will meet these requirements?"
- **The trap:** Traffic simulation frameworks, multi-Region deployment with Route 53 (availability ≠ quality), post-deployment manual audits (too late, not automated), rule-based preprocessing (doesn't evaluate the model). Sibling variants: judge-model comparison of two FMs (JSONL prompts in S3, run a job per FM), retrieve-only vs retrieve-and-generate eval types with precision@k / LLM-as-judge metrics.
- **Services combined:** Bedrock Model Evaluation, CI/CD (CodePipeline/Step Functions), CloudWatch, S3 datasets.

### P14. Guardrail configuration — Select THREE
- **Topic:** Guardrail policy design (D3)
- **Concept:** Map each control to the right guardrail primitive: *denied topics* for conversation patterns, *word filters* for competitor names, *high grounding threshold* for factual claims.
- **Phrasing shape:** Finance assistant; block inappropriate advice, competitor mentions, ungrounded claims. → "Which combination of steps will meet these requirements? (Select THREE.)"
- **The trap:** Polarity traps — *low* grounding threshold is offered (opposite of intent); content filters for topics that belong in denied topics; word filters without setting input/output action to block.
- **Services combined:** Bedrock Guardrails (denied topics, content filters, word filters, contextual grounding).

### P15. Centralized org governance: SCP + Guardrails — Select TWO
- **Topic:** Organization-wide Bedrock governance (D3)
- **Concept:** SCPs enforce *which models* and *require a guardrail identifier*; CloudFormation StackSets deploy the *guardrail itself* with block filtering across accounts.
- **Phrasing shape:** Multi-account org; employees use Bedrock everywhere; must block proprietary topics in prompts, restrict to approved models, manage centrally. → "Which combination of solutions will meet these requirements? (Select TWO.)"
- **The trap:** IAM permissions boundaries (can't validate request parameters like guardrail identifiers); mask filtering instead of block (masking redacts output — the requirement is to *prevent* submission); SCPs alone without the guardrail deployment; data-residency red herrings.
- **Services combined:** AWS Organizations SCPs, IAM permissions boundaries, Bedrock Guardrails, CloudFormation StackSets.

### P16. Cross-Region inference vs provisioned throughput
- **Topic:** Throttling resilience, cheapest fix (D4)
- **Concept:** Cross-region inference profiles absorb bursty/peak throttling at pay-as-you-go pricing; provisioned throughput is for *sustained predictable* load (and commits hourly cost).
- **Phrasing shape:** Peaky traffic (evenings per timezone, flash sales); throttling errors; "must not require a fixed hourly cost during low traffic." → "Which solution will meet these requirements?" / "MOST cost-effective"
- **The trap:** Provisioned throughput sized to peak (expensive idle); custom multi-Region failover logic in Lambda (operational overhead); CloudWatch-alarms-only options (observability ≠ mitigation). The giveaway phrase is *no fixed hourly cost*.
- **Services combined:** Bedrock cross-region inference profiles, provisioned throughput, CloudWatch metrics.

### P17. Stop sequences / inference parameters
- **Topic:** Generation control (D1/D2)
- **Concept:** Stopping generation at a specific phrase = *stop sequences* (an inference parameter), not a guardrail or post-processing.
- **Phrasing shape:** Short concept stem: need generation to halt when a specific phrase appears. → single correct mechanism.
- **The trap:** Guardrails (safety ≠ control flow), Lambda post-processing (wasteful), max tokens (too blunt).
- **Services combined:** Bedrock inference parameters (stop sequences, temperature, top-p).

### P18. IAM condition key for guardrail enforcement
- **Topic:** Mandatory guardrails via policy (D3)
- **Concept:** The `bedrock:GuardrailIdentifier` IAM condition key *requires* a guardrail identifier on every InvokeModel call.
- **Phrasing shape:** Requirement that every model call be guardrailed; developers keep forgetting to pass the guardrail. → "Which solution enforces this?"
- **The trap:** SCPs that name models (wrong mechanism), application-level checks (unenforceable), CloudTrail auditing (detective, not preventive).
- **Services combined:** IAM policies, condition keys, Bedrock Guardrails.

### P19. AgentCore / Strands / MCP agent deployment
- **Topic:** Agentic AI runtime (D2)
- **Concept:** Modern AWS agentic stack: Strands SDK or AgentCore for the agent, MCP servers for tools, AgentCore Runtime for deployment, Cognito OAuth for MCP auth (Streamable HTTP, not STDIO).
- **Phrasing shape:** Company builds agent with Lambda functions; must expose user info via MCP server; only authorized users may access. → "Which solution will meet these requirements?"
- **The trap:** STDIO transport for a remote MCP server (STDIO is for local processes); stuffing credentials into environment variables; Lambda layer as the "server." Correct: Lambda-hosted MCP + API Gateway HTTP + Streamable HTTP transport + Cognito OAuth.
- **Services combined:** Lambda, MCP (Streamable HTTP), API Gateway, Cognito, Bedrock AgentCore, Strands.

### P20. Observability: anomaly detection on token metrics
- **Topic:** FM ops monitoring (D5)
- **Concept:** Bedrock *model invocation logging* emits InputTokenCount/OutputTokenCount; *CloudWatch anomaly detection* alarms auto-adjust baselines as traffic patterns change.
- **Phrasing shape:** Token consumption surges despite steady traffic; need to find which tool integrations cause it; thresholds must auto-adjust. → "Which solution will meet these requirements?"
- **The trap:** Static CloudWatch alarms with fixed thresholds (the stem explicitly says traffic patterns change); S3 + Glue + Athena (batch forensics — right idea, wrong latency/overhead); manual threshold updates via Lambda (operational overhead). Metric filters to extract per-tool patterns + anomaly detection is the managed answer.
- **Services combined:** Bedrock model invocation logging, CloudWatch Logs metric filters, CloudWatch anomaly detection.

### Bonus recurring mini-patterns (seen 3+ times each)
- **Streaming for perceived latency:** `InvokeModelWithResponseStream` + API Gateway WebSocket API + Lambda for realtime UIs; NOT client-side polling. (D2)
- **Conversation memory:** DynamoDB with session IDs + server-side encryption for multi-turn context; NOT S3-per-interaction files. (D2)
- **Bedrock Rerank:** improve retrieval relevance with the managed rerank inside the KB's reranking config — "LEAST operational overhead" over a self-hosted SageMaker reranker. (D1)
- **Prompt governance + long-term logging:** Prompt Management versions + model invocation logging to S3 with Object Lock. (D2/D3)
- **Amazon Q Developer:** code generation/refactor and test generation in CI/CD — tested as a productivity tool, not an architecture component. (D2)
- **SageMaker inference-type selection:** image gen / long jobs → async inference; chat → realtime + streaming; infrequent bulk → batch transform. (D4)
- **S3 Vectors vs OpenSearch:** large-scale *infrequent* vector search → S3 Vectors (cost); frequent low-latency → OpenSearch. (D4)
- **PII redaction before search:** Comprehend PII redaction + Kendra — know the pre-ingestion redaction pattern. (D3)
- **Evaluation metric literacy:** context relevance/coverage for retrieval; faithfulness and citation precision for generation; fairness metrics via model evaluation jobs; LLM-as-a-judge with a 1–5 scale. (D5)
- **Multi-Region patterns:** cross-region *inference profiles* (throttling relief) vs cross-region *guardrail inference* (safety failover) vs SCP region allow-lists (data residency). Three different mechanisms, often in the same option pool. (D3/D4)

---

## 2. Topic frequency tally

Counted across ~120 stems from the sources above. Ranked by number of question-stems where the topic is the *primary* concept.

| Rank | Topic | Stems | Notes |
|---|---|---|---|
| 1 | Knowledge Bases / RAG / chunking / retrieval (hybrid search, rerank, query decomposition, metadata filtering) | ~25 | The exam's center of gravity. Chunking strategies (fixed / hierarchical / semantic), rerank, hybrid search appear constantly. |
| 2 | Bedrock Guardrails (content/denied-topic/word/PII filters, detect-block-mask modes, grounding thresholds, cross-region guardrails) | ~20 | Single most-asked *feature*. Mode selection (detect vs block vs mask) is a favorite discriminator. |
| 3 | Bedrock Agents (supervisor/collaborator, action groups, AgentCore, Strands, MCP) | ~12 | Multi-agent topology and MCP auth are the new-exam tells. |
| 4 | Throughput & throttling (provisioned throughput ARN bug, on-demand vs PT, cross-region inference) | ~12 | The ARN code-bug pattern repeats; cost framing decides CRI vs PT. |
| 5 | Data ingestion pipelines (Comprehend PII, Step Functions orchestration, BDA, embeddings at scale) | ~10 | "Least operational overhead" is almost always the qualifier here. |
| 6 | Model evaluation (judge models, JSONL datasets, CI/CD quality gates, retrieve-vs-generate eval types, metrics) | ~10 | Automated + parallel + blocking gates is the signature shape. |
| 7 | Observability (invocation logging, token metrics, anomaly detection, X-Ray, guardrail tracing) | ~10 | Token-count metrics and anomaly detection recur. |
| 8 | Prompt Management / Flows / prompt governance | ~8 | Variables, versioning, approval workflows, long-term logging. |
| 9 | Governance & compliance (SCPs, StackSets, CloudTrail, Glue lineage, S3 Object Lock, Macie) | ~8 | Centralized multi-account control is the favorite scenario. |
| 10 | SageMaker hosting & inference optimization (endpoint types, preload, streaming, tensor parallelism) | ~8 | Latency math (p95, first-token) drives these. |
| 11 | Security (IAM condition keys, VPC endpoints, Cognito, KMS, data residency) | ~6 | `bedrock:GuardrailIdentifier` condition key; region allow-lists. |
| 12 | Cost optimization (intelligent routing, S3 Vectors, caching, batch) | ~6 | "MOST cost-effective" + "no fixed hourly cost" are the tells. |
| 13 | Amazon Q Developer (code/test generation) | ~3 | Light but present. |
| 14 | Fine-tuning / distillation / custom models | ~3–4 | Surprisingly thin in this bank; the exam guide lists it, so treat as under-sampled rather than unimportant. |

**Service mention tally (rough):** Bedrock core ~90% of questions; OpenSearch ~25%; Comprehend ~20%; Step Functions ~20%; CloudWatch ~20%; Lambda ~20%; SageMaker ~15%; S3 ~15%; API Gateway ~12%; Glue ~10%; CloudTrail ~10%; DynamoDB ~10%; Cognito/IAM ~10%.

---

## 3. AWS signature-move list

How AWS writes AIP-C01 items — the repeatable moves to train for:

1. **"LEAST operational overhead"** — the dominant qualifier. Appears in a large share of questions. It almost always points to the fully-managed Bedrock-native path (Knowledge Bases, Step Functions + managed services, OpenSearch Serverless, BDA) and kills hand-rolled options (EMR, self-hosted rerankers, Lambda tuning gymnastics).
2. **"MOST cost-effective"** — pairs with traffic-shape clues: spiky/bursty + "no fixed hourly cost" → cross-region inference or on-demand; sustained predictable → provisioned throughput; 70/30 complexity split → intelligent prompt routing.
3. **"LEAST implementation effort" / "LEAST custom development effort"** — kills custom Lambda classifiers, manual frameworks, and DIY pipelines; points to managed features (intelligent routing, Flows, Bedrock evaluation jobs).
4. **Multi-response "Select TWO" / "Select THREE"** — frequent; candidate writeups confirm **no partial credit**. The exam-explained writeup notes this explicitly. Select-THREE appears on guardrail-configuration and "combination of steps" items.
5. **"Which combination of steps will meet these requirements?"** — options are *recipes*: each option is 3–6 sub-steps (A–F style letter groups). Tests sequencing knowledge (e.g., JSONL → S3 → evaluation job → judge model → per-FM run).
6. **Code-diagnosis stems** — a code block contains the bug (`modelId="anthropic.claudev2"` instead of the provisioned ARN; missing streaming API; polling instead of WebSocket). The fix is always the Bedrock-native API detail.
7. **Polarity traps** — low vs high grounding threshold; detect vs block vs mask guardrail mode; provisioned vs on-demand; lazy load vs preload; fixed vs anomaly-detection thresholds. The wrong polarity is always offered.
8. **Bedrock-native vs legacy-ML decoys** — SageMaker Model Monitor offered where Bedrock Model Evaluation is correct; Kendra offered where Knowledge Bases is correct; Macie offered for realtime PII where Guardrails PII filter is correct. Knowing *which layer* a service operates at is the whole test.
9. **Service-bundle options** — instead of 4 single services, each option bundles 3–5 services into a mini-architecture. You must validate *every* service in the bundle; one wrong member kills the option.
10. **Negative phrasing** — "must NOT require a fixed hourly cost," "does not want to block all flagged responses," "without accessing full content." The requirement that eliminates the tempting option is often stated negatively.
11. **Numbered constraints as filters** — p95 < 800ms, 10,000 req/hr, 4-hour window, 50GB, 15,000 parallel conversations in 45 min, 200ms response, 500,000 concurrent calls. Numbers aren't decoration; each one eliminates an option (batch transform can't do 200ms; manual audit can't do 15k parallel).
12. **"Which solution will meet these requirements?"** (bare) — no qualifier; then *all* requirements in the stem are hard constraints and you must satisfy every one. Longest stems use this.
13. **New-service spotlight** — Bedrock Rerank API, Bedrock Data Automation, AgentCore, S3 Vectors, intelligent prompt routing, cross-region inference profiles, Strands, MCP, Automated Reasoning checks. If a service launched in the last year, expect it to be the correct answer's centerpiece at least once.
14. **Scenario length** — stems run 120–250 words with 4–7 distinct requirements. Successful candidates report reading the *question* (last line) first, then the requirements, then the scenario — the study guide should teach this.
15. **Two-correct-answers that are orthogonal** — in Select TWO, the two answers often cover two *different* mechanisms (e.g., Prompt Management variables + guardrail in detect mode; preload + streaming). If your two picks solve the same sub-problem, one is wrong.

---

## 4. Per-domain "how they ask" notes

### D1 — Foundation Models (31%)
- **How they ask:** RAG end-to-end: chunking strategy choice (fixed vs hierarchical vs semantic with token/overlap numbers), hybrid search + rerank for terminology-heavy corpora, query decomposition, ingestion pipelines with PII removal, embedding model selection, BDA for multimodal. "Least operational overhead" is the default qualifier.
- **Favorite discriminators:** hierarchical chunking (parent 1000/child 200 tokens) for cross-section context; hybrid search + reranker over pure vector; managed embeddings (Titan via Bedrock) over self-hosted sentence-transformers; BDA over KB for mixed file types.
- **Trap zone:** confusing grounding (RAG) with safety (guardrails); vector-store choice (OpenSearch vs Aurora pgvector vs S3 Vectors).

### D2 — Implementation and Integration (26%)
- **How they ask:** Agent architectures (supervisor→collaborator routing, action groups, AgentCore, Strands, MCP auth with Cognito OAuth), streaming via WebSocket + `InvokeModelWithResponseStream`, Flows + Prompt Management with variables, conversation memory in DynamoDB, Q Developer as a productivity tool, API design (token limits, retries).
- **Favorite discriminators:** MCP Streamable HTTP vs STDIO; supervisor intent classification vs per-department supervisors; detect-mode guardrails on Flows nodes.
- **Trap zone:** over-engineering with Lambda glue where a managed feature exists; confusing transport/auth layers.

### D3 — AI Safety, Security, and Governance (20%)
- **How they ask:** Guardrail policy design (denied topics / content filters / word filters / PII / grounding thresholds, detect-block-mask modes), centralized org control (SCPs requiring guardrail identifier, StackSets deploying guardrails), audit (CloudTrail, invocation logging, S3 Object Lock), IAM condition keys, data residency via region allow-lists and cross-region guardrail inference.
- **Favorite discriminators:** mask vs block vs detect; permissions boundaries can't validate request params; Macie is at-rest, Guardrails PII is realtime.
- **Trap zone:** polarity (low vs high threshold); detective vs preventive controls.

### D4 — Optimization (12%)
- **How they ask:** Cost and performance trade-offs with traffic-shape clues. Provisioned throughput ARN bug; cross-region inference for bursty throttling; intelligent prompt routing for 70/30 splits; SageMaker endpoint tuning (preload, streaming, inference types); S3 Vectors for infrequent search; ElastiCache/DynamoDB response caching.
- **Favorite discriminators:** "no fixed hourly cost" → CRI/on-demand; sustained load → provisioned throughput; first-token latency → preload + streaming.
- **Trap zone:** bigger instance / more throughput as the reflex answer; async inference for interactive workloads.

### D5 — Testing, Validation, and Troubleshooting (11%)
- **How they ask:** Bedrock Model Evaluation jobs (judge models, JSONL datasets in S3, retrieve-only vs retrieve-and-generate, precision@k, faithfulness, citation precision, LLM-as-judge 1–5 scales), CI/CD quality gates that block deployment, observability (invocation logging, token metrics, anomaly detection, guardrail tracing via GuardrailContentSource), troubleshooting (embedding version mismatch after deploy, throttling diagnosis).
- **Favorite discriminators:** automated + parallel + blocking (vs manual/post-hoc); anomaly detection vs static alarms; metric names (InvocationsIntervened, InputTokenCount/OutputTokenCount).
- **Trap zone:** classic-ML tooling (SageMaker Clarify/Model Monitor) offered for GenAI eval problems.

---

## 5. Difficulty and scenario-length notes

- **Length:** most stems 120–250 words; multi-requirement (4–7 constraints). Options are long too — bundle-style answers of 3–5 services each, or 10–16 single-service options on Select TWO/THREE items.
- **Difficulty mix (estimated from bank):** ~20% direct concept checks (stop sequences, IAM condition key, inference-type selection), ~50% scenario architecture selection (the bulk: RAG, guardrails, agents, pipelines), ~30% hard multi-constraint bundles and Select TWO/THREE with polarity traps.
- **Time pressure:** 75 questions in 180 minutes (~2.4 min/question) with long stems — skimming discipline is a real test dimension.
- **No softballs:** multiple candidate writeups agree there is no "which service does X" trivia; every item is a scenario requiring implementation judgment.

---

*End of pattern intelligence. Built for the AIP-C01 study guide; pair with the exam blueprint domains when authoring practice items.*

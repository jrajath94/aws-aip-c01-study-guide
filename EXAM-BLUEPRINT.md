# AWS Certified Generative AI Developer – Professional (AIP-C01): Exam Blueprint

This is the single source of truth for writer workers building the AIP-C01 study volumes. Every topic is organized per the official exam guide's five content domains, and for each topic it records: what AWS actually tests (concrete service features, defaults, limits), how AWS asks it (question style and scenario framing, in the Stephane Maarek "most correct answer" style), and the common trap patterns (plausible-but-wrong distractors).

No personal identifiers appear anywhere in this document.

**Last verified: 2026-09-28 against AWS documentation.**

---

## 1. Verified facts vs assumptions

**Verified from the official exam guide (docs.aws.amazon.com, AWS Certified Generative AI Developer – Professional, exam guide v1.0):**

- Exam code: AIP-C01. Level: Professional.
- Five content domains and weights: Domain 1 Foundation Model Integration, Data Management, and Compliance (31%); Domain 2 Implementation and Integration (26%); Domain 3 AI Safety, Security, and Governance (20%); Domain 4 Operational Efficiency and Optimization for GenAI Applications (12%); Domain 5 Testing, Validation, and Troubleshooting (11%). All confirmed verbatim from the official guide.
- Question types: multiple choice (one correct + three distractors) and multiple response (two or more correct out of five or more options; must select ALL correct for credit). No partial credit. Unanswered = incorrect. No penalty for guessing.
- 10 unscored questions, not identified, mixed into the exam. Compensatory scoring: no per-domain minimum, only the overall score matters. Scaled score 100–1000, pass 750.
- Target candidate: 2+ years building production-grade apps on AWS or open source, general AI/ML or data engineering experience, 1 year hands-on GenAI implementation. Explicitly OUT of scope: model development and training, advanced ML techniques, data engineering and feature engineering.
- The full task/skill statements for all five domains are taken verbatim from the official guide and are reproduced in this document.

**Verified from multiple independent corroborating sources (Whizlabs, IT Mastery Exam Prep, official AWS certification listing pages, exam-taker reports):**

- 75 questions total: 65 scored + 10 unscored. 180 minutes. USD 300. Delivery: Pearson VUE testing center or online proctored.
- During the beta period the exam was 85 questions, 205 minutes, $150 — those numbers are stale and must not appear in study materials.

**Assumptions / things that could not be confirmed from an official primary source (flagged for writers: present as approximate or community-reported, not as official fact):**

- Per-domain scored question counts are estimated from weights applied to 65 scored questions: D1 ~20, D2 ~17, D3 ~13, D4 ~8, D5 ~7. AWS does not publish exact counts.
- The Kodekloud AIP-C01 study guide states "130 minutes" for exam duration. This conflicts with every other source including the AWS certification page (180 minutes). Treated as a Kodekloud error.
- Quotas, defaults, and limits cited in this blueprint (e.g. KB default ~300-token chunks, 50 MB file limits, agent idle session TTL 600s, cache TTLs of 5 minutes / 1 hour) come from AWS documentation and community notes current as of 2026 and change over time. The exam is deliberately designed to test judgment and best practices rather than volatile numeric limits (see exam-taker evidence below), so writers should teach the principle first and give numbers only as "current documented values, verify at build time."

---

## 2. The exam's question style: "how AWS asks this"

Evidence from multiple exam-taker reports (dev.to/aiarch_wibo-style posts, Kodekloud, Whizlabs, TutorialsDojo) converges on one picture:

1. **Scenario-based, never definition-based.** Each question is a 3–6 sentence scenario with hard constraints (latency, cost, region, compliance, team skill) followed by "which combination of steps" or "which THREE services." The right answer satisfies ALL constraints; distractors each violate exactly one.
2. **"Choose the MOST correct answer."** All four options are plausible; the exam rewards the best practice for the given constraints. Stephane Maarek's classic heuristics apply directly: when in doubt, prefer the more managed, more serverless, less operational-overhead option. Custom-built solutions are almost never correct unless the scenario explicitly requires something no managed service does.
3. **No partial credit on multiple response.** "Select THREE" means all three must be right. This is where the exam punishes shaky knowledge: you must be able to rule out every distractor individually.
4. **Think like an architect, not a coder.** Exam takers consistently report the test does not care about SDK syntax, exact API parameters, or per-model feature matrices. It cares about: which service, which integration pattern, sync vs async, which guardrail control, which cost lever, which evaluation method, and what order of operations.
5. **The three judgment filters behind most questions:** (a) reduce operational overhead, (b) improve security / responsible AI, (c) minimize latency or cost without breaking the constraint. The correct answer is usually the one that hits all three while a distractor sacrifices one.
6. **Long stems.** Expect multi-constraint scenarios: "12 languages, 99.9% availability with automatic failover, switch models without code deployments, validate before production." Train readers to extract each constraint and map it to one architectural decision (multilingual model = no custom training; failover = cross-region inference; no-code model switch = Lambda + API Gateway + AppConfig; validate first = PoC; Well-Architected = GenAI Lens).

---

## 3. Cross-cutting decision ladders (memorize these; they underpin half the exam)

### 3.1 Grounding strategy ladder: prompt engineering -> RAG -> agents -> fine-tuning -> custom model

AWS tests whether you climb this ladder in order and stop at the cheapest step that works:

- **Prompt engineering** first: new output format, tone, few-shot examples, chain-of-thought. No new knowledge needed.
- **RAG / Knowledge Bases**: the model needs facts it was not trained on (company docs, policies, product catalogs) or citations/source attribution. Retrieval, not retraining.
- **Bedrock Agents / agentic**: the task requires actions (call APIs, query databases, multi-step tool use), reasoning over tools, or session memory across turns.
- **Fine-tuning (SFT / continued pre-training / distillation)**: the model needs a new *behavior* baked into its weights — consistent brand voice at scale, domain-specific classification, a smaller cheaper model that matches a larger one on a narrow task. Requires labeled data in S3, a customization job, and (usually) Provisioned Throughput to serve.
- **Trap:** choosing fine-tuning when the scenario says "documents updated quarterly" or "must cite sources" — that is RAG. Choosing RAG when the scenario says "same task repeated millions of times, cost is the problem" — that is distillation to a smaller model or prompt caching. Choosing a custom model when the scenario only needs a different tone — prompt engineering.

### 3.2 Inference pricing ladder: on-demand -> prompt caching -> batch -> provisioned -> smaller model

- **On-demand**: spiky, experimental, unpredictable workloads.
- **Prompt caching**: repeated large static prefixes (system prompts, few-shot examples, long documents). Cheaper input tokens, but needs minimum token thresholds and works only on supported models (Claude 3.5+, Nova) via `cachePoint` (Converse) / `cache_control` (InvokeModel).
- **Batch inference**: non-interactive, hours-scale latency acceptable, ~50% cheaper than on-demand. S3 input, S3 output, async.
- **Provisioned Throughput**: predictable steady baseline traffic, latency guarantees, throttling protection. Hourly commit, 1–6 month terms; must route invocations to the provisioned model ARN (the classic exam bug: buying PT but still calling the base model ID via `invoke_model` and getting throttled).
- **Smaller model / model cascade**: route simple queries to Haiku/Nova Lite, complex ones to Sonnet/Opus. A classifier or prompt router in front.
- **Trap:** "provisioned throughput" as the answer to a cost problem on spiky traffic — PT is a latency/throughput guarantee, not a cost saver for bursty workloads. Hybrid answers (PT for baseline + on-demand for peaks) are the "most correct" pattern.

### 3.3 Safety control ladder: prompt design -> guardrails -> IAM/network -> evaluation -> human review

- Guardrails (Bedrock) for content safety, applied on inputs and/or outputs, via inline `guardrailConfig` or standalone `ApplyGuardrail` API.
- Prompt-attack (jailbreak/injection) detection as a distinct guardrail feature.
- Sensitive information filters (block or mask PII) distinct from content filters (toxicity categories) and denied topics (natural-language topic bans) and word filters (exact-match blocklists).
- Contextual grounding checks for RAG hallucination detection; Automated Reasoning checks for deterministic policy verification.
- Defense in depth: Comprehend pre-filter -> Guardrails at the model -> Lambda post-processing -> API Gateway response filtering.
- IAM + VPC endpoints + KMS + CloudTrail for the data/security plane; human review (Step Functions approval, SageMaker Ground Truth / A2I, human evaluation teams) where risk is high.

---

## 4. Domain 1: Foundation Model Integration, Data Management, and Compliance (31%, ~20 scored questions)

The exam's center of gravity. Master this or fail.

### Task 1.1: Analyze requirements and design GenAI solutions

**What AWS tests:**

- Matching architecture to constraints: RAG for private/cited/current knowledge; agents for multi-step tool use; fine-tuning for baked-in behavior; prompt engineering for everything else.
- Proof-of-concept before production: validate feasibility, performance, and business value with Bedrock (on-demand, low setup) before committing to Provisioned Throughput, custom models, or full deployment.
- AWS Well-Architected Framework **Generative AI Lens**: the exam name-drops it as the standard for "design reviews" and "standardized components." Know it exists and what it covers (responsible AI, data, model selection, cost, security pillars applied to GenAI).
- Standardized, reusable components across deployments: prompt templates, model routing layers, guardrail policies, evaluation harnesses — built once, reused.

**How AWS asks this:**

Scenario gives a business goal + 3–4 constraints (e.g. 12 languages, 99.9% availability with failover, switch models without code changes, CTO wants validation first). The correct answer chains: PoC on Bedrock -> cross-region inference for failover -> Lambda + API Gateway + AppConfig for model switching -> GenAI Lens alignment. Distractors hardcode model endpoints, deploy single-region, or skip the PoC.

**Traps:**

- "Select the model with the best published benchmarks" as a complete answer: benchmarks alone ignore cost/latency/compliance constraints.
- Training custom models for multilingual support when Bedrock FMs already cover the languages.
- EC2 + ALB "high availability" — within-region only, does not solve regional outage failover.

### Task 1.2: Select and configure FMs

**What AWS tests:**

- **Model selection criteria**: capability vs cost per token vs latency vs context window vs regional availability. Smaller models (Haiku, Llama 8B, Nova Lite) for cost/latency-sensitive tasks; flagship models for complex reasoning.
- **Flexible architecture for provider switching without code changes**: the canonical trio is **Lambda (routing logic) + API Gateway (stable endpoint, throttling) + AppConfig (feature flags / model identifiers as runtime config)**. AppConfig is the exam's favorite "no redeploy" mechanism.
- **Resilience**: Step Functions circuit breaker patterns; **Bedrock Cross-Region Inference** (inference profiles with `us.`, `eu.`, `au.`, `jp.`, `apac.`, `global.` prefixes) for models with limited regional availability and automatic failover; graceful degradation (fall back to a smaller/cheaper model or a cached response).
- **FM customization lifecycle**: SageMaker AI for domain-specific fine-tuned models; **LoRA / adapters** (parameter-efficient, only small weight deltas trained); SageMaker **Model Registry** for versioning; automated deployment pipelines with rollback; retire-and-replace lifecycle.
- Cross-Region Inference details: call the inference profile ID (`us.anthropic.claude-...`) instead of the bare model ID; Converse accepts ARN or ID, InvokeModel takes the profile ID; quotas are managed at the source region; data stays on the AWS backbone encrypted in transit.

**How AWS asks this:**

"Operations must switch between Claude, Titan, and Llama without code deployments" -> select-three: AppConfig + API Gateway + Lambda. "Model only available in two regions, need resilience" -> cross-region inference profile. "Failed deployment must roll back" -> SageMaker Model Registry + pipeline with rollback.

**Traps:**

- CloudFormation for runtime model switching: CloudFormation changes are deployments, violating "no code changes / no redeploy."
- EventBridge as the model-selection store: it routes events, it does not hold configuration.
- Confusing **inference profiles** (availability/resilience routing, geographic prefixes) with **prompt routers / model routers** (cost/quality routing by prompt complexity) and with **Provisioned Throughput** (reserved capacity). Three different mechanisms, three different exam answers.

### Task 1.3: Data validation and processing pipelines for FM consumption

**What AWS tests:**

- **Glue Data Quality** for automated data-quality monitoring; **SageMaker Data Wrangler** for visual data prep; **custom Lambda** functions for validation/normalization; **CloudWatch metrics** for pipeline observability.
- Multimodal pipelines: **Bedrock Data Automation** for documents/images/video/audio extraction; **Transcribe** for audio; **SageMaker Processing** for batch transforms.
- Input formatting per model: Converse API's unified `messages` format vs InvokeModel's provider-specific bodies; conversation formatting for chat apps; JSON schema for structured output.
- Data enhancement: Comprehend for entity extraction, Bedrock for text reformatting, Lambda for normalization.

**How AWS asks this:**

"Ingest 10,000 mixed files/day (PDF, PPT, video) and extract key concepts into structured summaries" -> Bedrock Data Automation (blueprints, standard vs custom output) + S3 versioning + AppSync/DynamoDB for collaboration. Distractors misuse Guardrails for extraction (Guardrails filter; they do not extract) or Neptune for time-series storage.

**Traps:**

- Using **Bedrock Guardrails to extract content** — wrong tool; Guardrails are safety filters.
- Using **Kendra** where **Knowledge Bases** are needed (Kendra = enterprise search; KB = RAG with embeddings and generation), and vice versa.

### Task 1.4: Vector store solutions

**What AWS tests:**

- **Bedrock Knowledge Bases** as the managed RAG service: data sources (S3, web crawler, Confluence, SharePoint, Salesforce), sync schedules, retrieval configuration, Retrieve and RetrieveAndGenerate APIs.
- Vector store options and their trade-offs: **OpenSearch Serverless** (managed, vector collections), **Aurora PostgreSQL with pgvector** (relational + vectors), **Neptune** (GraphRAG), **S3 Vectors** (cheap, smaller scale), Pinecone/MongoDB/Redis (third-party connectors). Exam framing: OpenSearch for scale, Aurora for relational+vector, S3 Vectors for cost-sensitive dev/test.
- **Metadata frameworks**: S3 object metadata, custom attributes, tags for domain classification and filtered retrieval.
- **Freshness**: incremental sync, scheduled refresh pipelines, change detection — KB data sources support sync schedules; "quarterly document updates" in a scenario points to automated ingestion, not one-time loads.
- Performance: OpenSearch sharding, multi-index per domain, hierarchical indexing.

**How AWS asks this:**

Multi-tenant scenario ("each hotel needs separate access controls, near-real-time availability data") -> one KB per tenant (or per account) with IAM-scoped access, NOT one shared KB with prompt-level filtering. "Documents updated quarterly" -> sync schedule. "Need citations" -> RetrieveAndGenerate with source attribution.

**Traps:**

- One shared knowledge base for multi-tenant data with different access controls — the exam wants isolation (separate KBs / accounts / IAM boundaries), not prompt instructions to "only answer about your hotel."
- Storing embeddings in **ElastiCache** for durability — ephemeral; use a real vector store, ElastiCache is for caching.
- **DynamoDB as the vector store** — metadata and session state yes, vectors no (use OpenSearch/Aurora/S3 Vectors).

### Task 1.5: Retrieval mechanisms for FM augmentation

**What AWS tests (this is the most technical sub-domain):**

- **Chunking strategies** (set per data source at creation; changing requires recreating the data source): `default` (~300 tokens, prototyping), `fixed_size` (token count + overlap %, predictable), `hierarchical` (child chunks for matching, parent chunks for context — best for structured docs), `semantic` (meaning boundaries — best quality, slower/more expensive ingestion), `none` (pre-chunked input), custom via Lambda.
- **Embedding models**: Titan Text Embeddings v2 (1024/512/256 dims, cheap default), Cohere Embed (multilingual, `input_type` for query vs document). Dimension choice affects storage and accuracy.
- **Hybrid search** (vector + keyword) and **reranking** (Bedrock rerank models) to fix "retrieved but not relevant" failures.
- **Query handling**: query expansion, decomposition (Lambda), transformation (Step Functions).
- **MCP clients** and function-calling interfaces as standardized retrieval access for agents.

**How AWS asks this:**

"RAG returns confident but wrong answers; retrieved chunks look relevant" -> debug chain: retrieval quality first (chunking splitting context? embedding missing nuance? semantic similarity != relevance?), then whether the model uses context (grounding), then chunking strategy. "Tables broken across chunks" -> advanced parsing / hierarchical chunking.

**Traps:**

- Fixing bad retrieval by switching the **generation model** — the failure is in retrieval, not generation.
- **Fixed-size chunking for structured documents** (manuals, legal) — hierarchical is the exam's preferred answer.
- Semantic chunking presented as "always best" — it costs more at ingestion; fixed-size is fine for FAQs.

### Task 1.6: Prompt engineering and governance

**What AWS tests:**

- **Bedrock Prompt Management**: prompts as managed resources — `{{variable}}` placeholders, **variants** (A/B testing), **versions** (immutable snapshots; draft -> version), no extra charge (pay only for model tokens), no redeploy to change a prompt.
- **Bedrock Prompt Flows** (now "Flows"): visual/no-code builder for multi-step GenAI workflows — nodes (prompt, agent, KB, Lambda, condition), conditional branching, reusable components, test panel.
- Governance: approval workflows, CloudTrail for usage audit, CloudWatch Logs for access logging, S3 for template repositories.
- Prompt QA: Lambda to verify outputs, Step Functions for edge-case testing, CloudWatch for regression detection.
- Techniques: system prompts, few-shot, chain-of-thought, structured output (JSON schema / Converse `outputConfig`).

**How AWS asks this:**

"15 prompts across features, marketing keeps changing tone, no redeploys" -> Prompt Management with versioning. "Three-stage prompt chain with branching" -> Prompt Flows vs Step Functions: Flows for prompt-centric no-code chains, Step Functions for general orchestration with human approvals/timeouts.

**Traps:**

- Hardcoding prompts in application code when the scenario demands frequent non-engineer changes.
- **Bedrock Agents** for a fixed deterministic prompt chain — agents are for dynamic tool-using reasoning; Flows/Step Functions are for fixed sequences.
- Confusing prompt **variants** (A/B comparison) with **versions** (immutable releases).

---

## 5. Domain 2: Implementation and Integration (26%, ~17 scored questions)

Design (D1) becomes build (D2).

### Task 2.1: Agentic AI solutions and tool integrations

**What AWS tests:**

- **Bedrock Agents anatomy**: agent (instruction + FM + IAM role), **action groups** (Lambda executor or API-schema/OpenAPI; function schema for simple tools; `actionGroupExecutor`), **knowledge bases** attached for grounding, **guardrails** attached, **prepare-agent** (must run after config changes; DRAFT -> PREPARED), **aliases** (prod), **invoke_agent** via bedrock-agent-runtime with `sessionId`, `enableTrace` for reasoning traces.
- **Multi-agent**: supervisor/collaborator pattern (built-in, NOT action groups between agents); collaborators must be prepared + aliased; `relay-conversation-history`.
- **Strands Agents + AWS Agent Squad**: the code-first / open-source multi-agent frameworks the exam names. **MCP** for agent-tool interaction (MCP servers on Lambda for lightweight tools, ECS for complex ones).
- Safeguards: Step Functions stopping conditions, Lambda timeouts, IAM resource boundaries, circuit breakers, **human-in-the-loop approvals** (Step Functions callback/task tokens).
- **AgentCore**: Runtime (host any-framework agents, `POST /invocations`), Gateway (MCP tool exposure, OAuth/credential management), Memory (short/long-term agent context), Identity, Observability. Migration path: Bedrock Agents -> AgentCore for framework freedom.
- ReAct / chain-of-thought via Step Functions for structured reasoning.

**How AWS asks this:**

"Specialist agents for tax/investment/estate must collaborate, use tools, keep memory for weeks, human approval over $100k" -> Strands + Agent Squad for orchestration, MCP for tools, DynamoDB for weeks-long memory, Step Functions for approval workflow. Single-prompt or Lex-based options are distractors (Lex = conversational UI, not autonomous orchestration; single prompt doesn't scale).

**Traps:**

- **Lambda for long-running agent orchestration** — 15-minute limit; Step Functions for workflows with waits/approvals.
- **S3 for conversation memory** — latency and access patterns; DynamoDB for session state.
- Describing inter-agent communication as **action groups** in supervisor instructions — the exam (and the service) uses the built-in supervisor/collaborator mechanism.
- Forgetting **prepare-agent** after changes — the classic "agent ignores new action group" bug.

### Task 2.2: Model deployment strategies

**What AWS tests:**

- **Lambda for on-demand invocation** (spiky/irregular), **Bedrock Provisioned Throughput** for predictable baselines (hybrid is often the "most correct"), **SageMaker AI endpoints** for custom/self-hosted models (real-time, async, serverless inference options).
- **Batch inference** for non-real-time (50% cheaper, hours latency).
- **Model cascading**: small model first, escalate to large on low confidence.
- Container/GPU deployment considerations for self-hosted LLMs (memory, GPU, token throughput) — conceptual, not deep.

**How AWS asks this:**

"2M requests/day baseline + 10x Friday spikes + sub-3s latency" -> hybrid: PT for baseline, on-demand via Lambda for spikes. "Entirely SageMaker with GPU autoscaling" fails on cost and cold-start latency; "EC2 fixed for peak" fails on cost.

**Traps:**

- Provisioned Throughput for spiky traffic as a pure cost play — PT is for predictable baselines.
- **SageMaker Serverless Inference** for sustained high-throughput — it's for intermittent traffic with cold starts; wrong for strict latency SLAs at scale.

### Task 2.3: Enterprise integration architectures

**What AWS tests:**

- API-based legacy integration, event-driven loose coupling (EventBridge, SQS), data sync patterns.
- API Gateway microservice integrations, Lambda webhooks, EventBridge event-driven GenAI.
- **Secure access**: identity federation, RBAC for models and data, least-privilege FM API access.
- **Outposts** (on-prem data residency) and **Wavelength** (edge) for constrained environments.
- **CI/CD + GenAI gateway**: CodePipeline/CodeBuild with automated tests, security scans, rollback; centralized abstraction layer for model access with observability and policy control.

**How AWS asks this:**

"Legacy Java PMS + per-hotel access control + near-real-time" -> per-tenant KBs, direct ingestion for real-time data, IAM Identity Center permission sets. "Consume FMs securely across the enterprise" -> centralized GenAI gateway (abstraction + policy + observability), not every team calling Bedrock directly.

**Traps:**

- One shared KB with prompt-level access instructions instead of IAM-enforced isolation.
- **CloudTrail for real-time data sync** — CloudTrail is audit logging, not a data pipeline.

### Task 2.4: FM API integrations

**What AWS tests — the API decision matrix (high yield):**

| Need | Answer |
|---|---|
| Unified request/response across providers, tool use, guardrails inline | **Converse / ConverseStream** |
| Provider-specific features, embeddings | **InvokeModel / InvokeModelWithResponseStream** |
| Embeddings | InvokeModel only (Converse is text-generation only) |
| Async, hours OK, cheapest | **Batch inference** (S3 in/out) |
| Real-time token streaming | ConverseStream / InvokeModelWithResponseStream; API Gateway chunked transfer or WebSockets/SSE to the client |
| Reliability | SDK exponential backoff, API Gateway throttling, fallback models, X-Ray tracing |

- **Converse details**: `modelId`, `messages`, `system`, `inferenceConfig` (maxTokens, temperature, topP), `toolConfig`, `guardrailConfig` (identifier + version + trace), `additionalModelRequestFields` for provider escapes, `cachePoint` for prompt caching, `outputConfig` for structured output.
- **InvokeModel details**: provider-specific JSON bodies (e.g. Claude requires `anthropic_version: bedrock-2023-05-31` and `max_tokens`); wrong body = `ValidationException`/`Malformed input`.
- **Streaming**: ConverseStream for incremental delivery; API Gateway has payload/timeout limits — for long streams use WebSockets or direct streaming.

**How AWS asks this:**

"Application bought Provisioned Throughput but still throttled; code calls `invoke_model(modelId='anthropic.claude...')`" -> the code ignores the provisioned model ARN; fix by invoking the provisioned model identifier. "Need same code for Claude, Llama, Titan with tool use" -> Converse API.

**Traps:**

- **InvokeModel for embeddings via Converse** — Converse cannot do embeddings.
- **Converse for provider-specific parameters** without `additionalModelRequestFields` — the escape hatch exists but InvokeModel is the distractor-proof answer for exotic provider features.
- Assuming **guardrails only work with Converse** — `ApplyGuardrail` is standalone and model-agnostic (works with OpenAI/Gemini/self-hosted too).

### Task 2.5: Application integration patterns and development tools

**What AWS tests:**

- API Gateway for GenAI APIs: streaming responses, token-limit management, retries/timeouts.
- **Amplify** for declarative UI; OpenAPI for API-first; Prompt Flows as no-code builders.
- **Bedrock Data Automation** for document-processing workflows (IDP).
- **Amazon Q Developer** for code generation/refactoring/testing; **Q Business** for enterprise knowledge assistants.
- Troubleshooting hooks: CloudWatch Logs Insights for prompt/response analysis, X-Ray for FM call traces.

**How AWS asks this:**

"Generate study materials from 10k+ files/day incl. video, with real-time collaboration" -> BDA for extraction + S3 versioning + AppSync/DynamoDB for collaboration. Distractors: "Bedrock Agents for change tracking," "Guardrails for extraction."

**Traps:**

- **Q Business vs Q Developer**: Business = enterprise chat over company data; Developer = IDE coding assistant. The exam swaps them in distractors.

---

## 6. Domain 3: AI Safety, Security, and Governance (20%, ~13 scored questions)

One in five questions. Under-prepared candidates fail here.

### Task 3.1: Input and output safety controls

**What AWS tests — the Guardrails control matrix (memorize):**

| Control | What it does | Configured by |
|---|---|---|
| Content filters | Hate, insults, sexual, violence, misconduct, prompt attack | Severity threshold NONE/LOW/MEDIUM/HIGH per category |
| Denied topics | Block subject areas (medical diagnosis, financial advice) | Natural-language topic definitions |
| Word filters | Exact-match blocklists | Custom lists |
| Sensitive info filters | PII detection (30+ entity types), custom regex | Block or mask per entity type |
| Contextual grounding | Hallucination check vs source content | Threshold |
| Automated Reasoning | Deterministic logic verification vs policy | Natural-language policy rules |
| (Multimodal) | Image toxicity filtering | Toggle |

- Applied on **inputs, outputs, or both**; via Converse `guardrailConfig` or standalone **ApplyGuardrail** (any model, including non-Bedrock).
- **Prompt injection / jailbreak** = the "prompt attack" content-filter category plus input sanitization and system-prompt protection.
- Hallucination reduction: KB grounding + confidence scoring + JSON Schema structured outputs + contextual grounding checks.
- **Defense in depth** layering: Comprehend pre-filter -> Guardrails -> Lambda post-processing -> API Gateway response filtering.

**How AWS asks this:**

Children's tutor scenario (block profanity/violence inputs, prevent harmful outputs, stop jailbreaks, ground facts) -> the full defense-in-depth stack. "Block medical diagnoses" -> denied topics (not content filters). "Redact SSNs" -> sensitive info filters (not word filters).

**Traps (the exam's favorite confusion set):**

- **Denied topics vs content filters**: denied topics = subject-matter bans in plain language ("investment advice"); content filters = toxicity categories with severity thresholds. Scenario says "prevent the model from discussing X topic" -> denied topics.
- **Word filters vs sensitive info filters**: word filters = exact strings; PII = entity-type detection with block/mask.
- **Contextual grounding vs Automated Reasoning**: grounding = "is this supported by the retrieved source?" (RAG hallucination); Automated Reasoning = "does this violate the formal policy?" (compliance rules, deterministic).
- Relying on the **base model's built-in safety** as the complete answer — never the "most correct" for a sensitive audience.

### Task 3.2: Data security and privacy

**What AWS tests:**

- **VPC endpoints / PrivateLink** for Bedrock (`com.amazonaws.<region>.bedrock`, `bedrock-runtime`, `bedrock-agent`, `bedrock-agent-runtime`): keep traffic off the public internet, no NAT.
- IAM policies for model/KB/agent access; **Lake Formation** for granular data access; CloudWatch for access monitoring.
- **PII pipeline**: Macie (discover PII in S3 at scale) + Comprehend (real-time PII detection, 30+ entity types) + Guardrails (filter at inference) + S3 Lifecycle (retention).
- **KMS** at rest, TLS in transit; data masking/anonymization strategies.
- Bedrock model invocation logging: route to S3/CloudWatch, optionally KMS-encrypted; **disable or restrict it in compliance environments** (logs may contain PII).

**How AWS asks this:**

"Protect PII in customer-service GenAI conversations, minimal custom work" -> select-three: Macie + Comprehend + Guardrails. "Keep Bedrock traffic private" -> VPC interface endpoints.

**Traps:**

- **Translate for PII obfuscation** — preserves meaning, zero protection.
- **Rekognition for text PII** — vision service; Comprehend is the text answer.
- Logging invocations to CloudWatch without encryption in a healthcare scenario — the exam wants KMS or disabled logging.

### Task 3.3: AI governance and compliance

**What AWS tests:**

- **Model cards** (SageMaker: programmatic generation, document limitations/intended use).
- **Data lineage**: Glue Data Catalog registration, metadata tagging, source attribution on generated content.
- **Audit**: CloudTrail for every API call; CloudWatch Logs for decision logs; token-level redaction in logs.
- Continuous monitoring: misuse/drift/policy-violation detection, bias drift monitoring, alerting + remediation workflows.

**How AWS asks this:**

"Regulator asks: which data produced this answer?" -> lineage via Glue catalog + metadata tags + CloudTrail audit trail. "Prove the model's outputs stay unbiased over time" -> bias drift monitoring with automated alerts.

**Traps:**

- **CloudTrail vs CloudWatch Logs**: Trail = who called what API (audit); Logs = application/decision content. The exam tests the distinction.

### Task 3.4: Responsible AI

**What AWS tests:**

- Transparency: reasoning traces (agent tracing, `enableTrace`), confidence metrics, evidence/source attribution in answers.
- Fairness: pre-defined fairness metrics, A/B testing via Prompt Management variants and Flows, **LLM-as-a-judge** automated evaluations.
- Policy compliance: guardrails from policy requirements, model cards documenting limitations, Lambda compliance checks.

**How AWS asks this:**

"Ensure unbiased outputs across demographic groups" -> fairness metrics + A/B testing + LLM-as-judge evals, not "a bigger model."

**Traps:**

- Treating fairness as a one-time check — the exam wants **continuous** bias drift monitoring.

---

## 7. Domain 4: Operational Efficiency and Optimization (12%, ~8 scored questions)

Small domain, tricky questions: every scenario forces cost vs latency vs quality trade-offs.

### Task 4.1: Cost optimization and resource efficiency

**What AWS tests:**

- **Token efficiency**: estimation and tracking, context pruning, prompt compression, response size limits.
- **Tiered model usage**: classifier/router sends simple queries to cheap models, complex to flagship; price-to-performance measurement.
- **Caching**: prompt caching (Converse `cachePoint`, min token thresholds per model, 5-min default TTL / 1-hour on supported models), semantic caching (ElastiCache/DynamoDB for repeated semantically-similar queries), deterministic request hashing.
- **Throughput**: batching, provisioned throughput for steady load, utilization monitoring.

**How AWS asks this:**

"Token costs growing 30%/mo, CFO wants cuts without UX degradation" -> multi-lever: smaller model for low-priority traffic, prompt caching for repeated prefixes, PT for predictable load, prompt compression, complexity-based routing. Single-lever answers are distractors.

**Traps:**

- **Prompt caching vs Provisioned Throughput**: caching attacks repeated-input cost; PT attacks latency/throughput guarantees. Scenario with "same long system prompt on every call" -> caching. Scenario with "throttling at peak, steady baseline" -> PT.
- **Semantic caching presented for highly personalized queries** — low hit rate; the Whizlabs-style explanation explicitly rejects it for personalized recommendations.

### Task 4.2: Application performance

**What AWS tests:**

- Latency levers: pre-computation, latency-optimized models, parallel requests, **streaming** (perceived latency), benchmarking.
- Retrieval performance: index optimization, query preprocessing, hybrid search with custom scoring.
- Throughput: batch inference, concurrent invocation management, token-processing optimization.
- Inference parameters: **temperature / top-p / top-k** matched to the task (low temperature for deterministic/factual, higher for creative); A/B testing for improvements.

**How AWS asks this:**

"Sub-3-second latency, 10x Friday spikes" -> PT baseline + on-demand overflow + streaming. "Inconsistent outputs for identical inputs, need 99.5% consistency" -> temperature 0 + deterministic caching + prompt versioning (and note: provisioned throughput stabilizes latency, not output randomness — don't conflate).

**Traps:**

- **Provisioned Throughput to fix nondeterministic outputs** — PT fixes capacity/latency, not randomness; temperature and prompt control fix consistency.
- **top-k/top-p/temperature as cost controls** — they control randomness/quality, not cost.

### Task 4.3: Monitoring GenAI applications

**What AWS tests:**

- **CloudWatch Bedrock metrics**: `Invocations`, `InputTokenCount`, `OutputTokenCount`, `InvocationThrottles`, latency; anomaly detection on token bursts; cost anomaly detection.
- **Model Invocation Logs**: S3/CloudWatch destinations for request/response forensics.
- **X-Ray** for tracing multi-step agent/FM call chains; CloudWatch Logs Insights for prompt/response analysis.
- Tool/agent observability: call-pattern tracking, multi-agent coordination tracking, usage baselines.
- Vector-store ops: index performance monitoring, automated optimization, data-quality validation.
- GenAI-specific failure detection: **golden datasets** for hallucination detection, output diffing for consistency, reasoning-path tracing.

**How AWS asks this:**

"Near-real-time detection of hallucinations + abnormal token spend, minimal custom work" -> Bedrock evaluation jobs with LLM-based judgments for hallucinations + CloudWatch anomaly detection on token metrics. Building Glue/Athena pipelines for this is the high-overhead distractor.

**Traps:**

- **SageMaker Model Monitor for GenAI text quality drift** — built for tabular ML; Bedrock evaluations / golden datasets are the GenAI answer.
- **CloudTrail for performance monitoring** — audit, not metrics; CloudWatch is the metrics answer.

---

## 8. Domain 5: Testing, Validation, and Troubleshooting (11%, ~7 scored questions)

Smallest domain; questions punish candidates who debug GenAI like traditional software.

### Task 5.1: Evaluation systems

**What AWS tests — the evaluation matrix (memorize):**

| Method | Metrics | When |
|---|---|---|
| **Programmatic (automatic)** | Accuracy, robustness, toxicity; built-in or custom datasets | Objective, repeatable benchmarks |
| **LLM-as-a-judge** | Correctness, completeness, faithfulness (hallucination), harmfulness, refusal, style/tone; custom metrics definable | Human-like quality at scale; RAG eval; agent eval |
| **Human** | Relevance, style, brand voice, any custom metric | Subjective judgment; own employees or **AWS-managed team** |
| Bring-your-own-inference | Evaluate any model/system anywhere | Non-Bedrock or full-app responses |

- **RAG evaluation**: retrieval relevance + generation faithfulness, LLM-as-judge powered.
- **Agent evaluation**: task completion rate, tool-use effectiveness, reasoning quality (multi-step).
- QA gates: continuous evaluation, **regression testing on prompt/model changes**, canary testing, synthetic user workflows, AI-specific deployment validation (hallucination rate, semantic drift checks).

**How AWS asks this:**

"Compare two models for summarization quality including brand voice" -> LLM-as-a-judge for scale + human eval for brand voice. "Validate a new prompt version before rollout" -> regression testing + canary.

**Traps:**

- **Programmatic eval for style/brand voice** — subjective metrics need human or LLM-as-judge.
- **Human eval as the only eval** for large-scale regression — cost/time; the exam wants automated gates with human spot-checks.

### Task 5.2: Troubleshooting

**What AWS tests — the GenAI debug order:**

1. **Content handling**: context window overflow -> chunking strategy, prompt compression, truncation analysis.
2. **API integration**: error logging, request validation (body format per provider!), response analysis. Classic: `ValidationException` from wrong InvokeModel body; `AccessDeniedException` (misleading) when the model isn't available in the region.
3. **Prompt problems**: version comparison, systematic refinement, prompt testing frameworks.
4. **Retrieval problems**: embedding quality, chunking remediation, drift monitoring, vector search perf — with relevance analysis first.
5. **Prompt maintenance**: CloudWatch Logs for prompt confusion diagnosis, X-Ray observability pipelines, schema validation for format drift.

**How AWS asks this:**

"App bought PT but on-demand throttles; code uses `invoke_model(modelId='anthropic.claude...')`" -> code bypasses the provisioned model; invoke the provisioned model ARN/ID. "Agent ignores new action group" -> `prepare-agent` not re-run.

**Traps:**

- Debugging **retrieval** failures by changing the **generation model** or temperature.
- **Increasing PT model units** when the code never routes to the provisioned model — capacity isn't the bug, routing is.

---

## 9. Service and feature reference for writers

Condensed facts every volume needs. All from AWS documentation / official exam guide as of 2026.

**Bedrock inference APIs:** Converse/ConverseStream (unified, tool use, guardrails, caching, structured output); InvokeModel/InvokeModelWithResponseStream (provider-specific bodies, embeddings); Batch inference (S3 in/out, ~50% cheaper, hours latency); Provisioned Throughput (reserved model units, 1–6 mo commit, `CreateProvisionedModelThroughput`); Cross-Region Inference profiles (`us.`/`eu.`/`au.`/`jp.`/`apac.`/`global.` prefixes); Model/prompt routers (cost-quality routing by complexity); Custom models (fine-tune SFT, continued pre-training, reinforcement fine-tuning, distillation; imported models; Nova custom models support on-demand invocation, others need PT).

**Bedrock app services:** Knowledge Bases (S3/web/Confluence/SharePoint/Salesforce sources; chunking default/fixed/hierarchical/semantic/none/custom-Lambda set at creation; Titan/Cohere embeddings; OpenSearch Serverless/Aurora pgvector/Neptune/S3 Vectors/Pinecone/MongoDB/Redis; Retrieve/RetrieveAndGenerate; hybrid search; rerank); Agents (action groups -> Lambda/OpenAPI; prepare-agent; aliases; supervisor/collaborator multi-agent; invoke_agent with sessionId + trace); Guardrails (6 policies + ApplyGuardrail standalone); Prompt Management (versions, variants, {{variables}}, no extra charge); Prompt Flows (visual multi-step builder); Data Automation (4 modalities, standard vs blueprint custom output, async, S3 results, KB parser); Evaluations (programmatic, LLM-as-judge, human, RAG eval, BYOI).

**Agent frameworks (exam-named):** Strands Agents, AWS Agent Squad, MCP (Lambda lightweight / ECS complex servers), AgentCore (Runtime, Gateway, Memory, Identity, Observability).

**SageMaker AI (supporting role):** async inference, serverless inference, real-time endpoints with autoscaling, Model Registry, Clarify (bias/explainability), Model Monitor, Neo, JumpStart, Data Wrangler, Ground Truth/A2I (human review).

**Data/security/ops:** IAM (least privilege, model/KB/agent scoping), KMS, VPC endpoints for Bedrock planes, CloudTrail (audit), CloudWatch (metrics incl. InputTokenCount/OutputTokenCount/InvocationThrottles + Logs Insights + anomaly detection), X-Ray, S3 (versioning, lifecycle, metadata), DynamoDB (session/state), Step Functions (orchestration, approvals, circuit breakers), Lambda (routing, validation, tools), API Gateway (stable endpoints, throttling, streaming), AppConfig (runtime model switching), EventBridge/SQS/SNS (eventing), OpenSearch Service, ElastiCache (caching), Kendra (enterprise search) vs Knowledge Bases (RAG), Q Business (enterprise assistant) vs Q Developer (coding), Comprehend (NLP/PII), Macie (S3 PII discovery), Transcribe, Glue (Data Quality, crawlers, lineage), WAF.

**Out of scope per the official guide (do not build volume content around these):** model training from scratch, advanced ML theory, feature engineering, plus the listed out-of-scope services (Redshift as warehouse, IoT, blockchain, media services, etc.).

---

## 10. Master trap list (distractor patterns to drill in every volume)

1. Choosing **Lambda** for long-running orchestration with waits/approvals -> Step Functions.
2. **InvokeModel vs Converse**: provider-specific body vs unified; embeddings need InvokeModel.
3. **Guardrails denied topics vs content filters** vs word filters vs PII filters — match the control to the scenario verb.
4. **Prompt caching vs Provisioned Throughput**: repeated-prefix cost vs latency/throughput guarantee.
5. **Inference profiles vs prompt routers vs PT**: availability routing vs cost-quality routing vs reserved capacity.
6. **One shared KB** for multi-tenant data -> separate KBs + IAM isolation.
7. **Fine-tuning** when RAG/prompting suffices; **RAG** when behavior change or massive repetition economics point to distillation/caching.
8. **CloudFormation/EventBridge** for runtime model switching -> AppConfig + Lambda + API Gateway.
9. **S3 for session memory** -> DynamoDB; **ElastiCache for durable vectors** -> OpenSearch/Aurora/S3 Vectors.
10. **Kendra vs Knowledge Bases**; **Q Business vs Q Developer**.
11. **Increasing PT units** when code doesn't route to the provisioned model.
12. **PT for output consistency** — temperature/prompt control, not capacity.
13. **Custom/manual builds** when a managed service exists — the exam's default bias.
14. **CloudTrail for metrics / Glue+Athena for real-time hallucination detection** — wrong-plane tools.
15. **Model's built-in safety** as the complete safety answer — never sufficient for sensitive scenarios.

---

## 11. Sources consulted

- Official exam guide: AWS Certified Generative AI Developer – Professional (AIP-C01), v1.0, all five content-domain pages, in-scope and out-of-scope service lists (docs.aws.amazon.com).
- Stephane Maarek + Frank Kane, "Ultimate AWS Certified Generative AI Developer Professional" (Udemy): curriculum themes — Bedrock/SageMaker/Knowledge Bases, agentic systems (Bedrock Agents, Flows, OpenSearch, S3 Vectors, Strands, Agent Squad, AgentCore), RAG/embedding optimization, Prompt Management + Flows, Bedrock Evaluations, Bedrock Data Automation, Glue/Comprehend/Textract pipelines, Step Functions/Lambda/CI-CD orchestration.
- TutorialsDojo AIP-C01 study guide (exam-guide PDF preview): task statements per domain.
- Kodekloud, "AWS AIP-C01 Study Guide: Generative AI Developer Exam 2026": domain scenarios, holy trinity (Agents + Knowledge Bases + Guardrails), cost/latency trade-off framing.
- Whizlabs AIP-C01 sample questions with explanations: scenario style, AppConfig+Lambda+APIGW model switching, PT hybrid deployment, Strands/Agent Squad multi-agent, Macie+Comprehend+Guardrails PII, defense-in-depth safety.
- Exam-taker reports (dev.to): judgment over memorization, architect-not-coder framing, managed-service bias, aging-well best-practice focus.
- AWS Bedrock documentation and blogs: Guardrails policies, Knowledge Bases chunking/embedding/vector stores, Agents action groups + multi-agent, Converse vs InvokeModel, prompt caching, cross-region inference profiles, model evaluation (programmatic/LLM-as-judge/human), custom models (fine-tuning/continued pre-training/distillation/imported), Provisioned Throughput, batch inference, Data Automation, AgentCore, Bedrock Prompt Management and Flows.

---

*End of blueprint. Writers: teach principles first, then the AWS-specific mechanism, then one worked scenario per topic in the "most correct answer" style, then the traps. Every volume must be completable by a developer with 2+ years of AWS experience and no prior GenAI depth.*

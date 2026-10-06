# AIP-C01 Exam Question Patterns from the Internet

Research date: Sept 28, 2026. Pattern analysis only for writing original practice questions. No exam items copied.

## How the exam asks (general read, corroborated across 3+ passer reports)

- Decision exam, not recall. Multi-paragraph company scenarios, 4-5 long plausible options. Usually 3 options are good ideas in the wrong context; one satisfies every constraint at once. Find the decisive constraint first, then compare survivors.
- Favorite stems: "Which solution will meet these requirements?", "Which solution meets these requirements with the LEAST operational overhead?", "Which combination of steps will meet these requirements? (Choose two.)"
- Constraints repeat: least operational overhead, least custom development effort, most cost-effective, must be proactive (not reactive), latency budget, no public internet, frequent data changes, no code redeploy.
- Maarek's generic exam craft (applies here): proceed by elimination; over-complicated solutions are usually wrong; there are few true trick questions at his practice-test level, but at Professional level the traps are constraint mismatches, not tricks.
- 75 items, 180 min, pass 750/1000. 65 scored + 10 unscored. Multiple choice + multiple response, no partial credit on multi-response. Domain weights: D1 31%, D2 26%, D3 20%, D4 12%, D5 11%.
- Traditional ML almost absent: no confusion matrices, no SageMaker training deep dives. RAG domain dominates.

---

## TRAP PATTERNS (numbered)

1. **Proactive vs reactive.** Stem demands proactive action (e.g. alert BEFORE hitting a token limit). Wrong answers detect or react after failure (post-call alarms, retry after rejection, monitor exceeded limits). Right answer estimates/counts tokens before calling the model. Rule: if the stem says "proactively", delete every option that reacts to failures.

2. **Least operational overhead = fewest self-managed services.** Tempting wrong answer: a Lambda glue pipeline or provisioned cluster that "works" but adds managed surface. Right answer: the fully managed native path (Bedrock RetrieveAndGenerate API instead of hand-rolled Retrieve + Converse; Step Functions instead of EventBridge + custom code; Knowledge Bases instead of custom vector DB cluster). Serverless/managed wins nearly half the stems.

3. **Fabricated features.** Wrong answers pair a real service with a capability it does not have. Observed shapes: S3 action nodes inside Bedrock Flows, Guardrails enforcing token quotas, cross-Region Guardrail replication, CloudTrail doing distributed tracing. If an option sounds slightly off, verify whether the feature exists.

4. **CloudTrail vs CloudWatch for safety auditing.** Stem: "audit trail of all safety interventions" (which prompts were blocked, why). Trap: choose CloudTrail. Right: CloudWatch with custom metrics (GuardrailContentSource dimensions like InvocationsIntervened) or model invocation logging. CloudTrail records who called which API and when, not what was blocked or why. But CloudTrail IS right for "who invoked which model from where" compliance auditing.

5. **Model invocation logging vs CloudTrail.** If the stem needs prompt/response CONTENT for audit, the answer is model invocation logging (opt-in, to S3/CloudWatch), not CloudTrail. CloudTrail has API-call metadata only, no token counts, no prompts.

6. **Step Functions Standard vs Express.** Stem with high concurrency pushes you toward Express. Trap: the workflow must Wait-for-Callback (human approval, long pause). Express caps at 5 minutes and cannot durably pause. Right: Standard (exactly-once, long durations, callback support). High throughput does not beat a duration/pause constraint.

7. **Sequential vs parallel.** Tight latency/throughput windows (process N objects in H hours). Trap: Lambda-only (15-min timeout) or sequential workflow. Right: Step Functions Distributed Map (up to 10k parallel child executions over S3 objects).

8. **Right tool for the data type.** Unstructured docs (PDF/HTML) -> Bedrock Knowledge Bases. Relational data -> text-to-SQL on RDS, never embed tables into a vector store. Trap: pick a vector DB for everything because "vector search". Knowledge Bases are for unstructured content; relational queries belong to RDS + text-to-SQL.

9. **Vector store chosen by scale.** Small datasets (< ~1M records) -> Aurora Serverless + pgvector (lowest overhead). Medium-large -> OpenSearch with IVFFlat or HNSW. Small + 100% recall requirement -> flat/brute-force exact search. Trap: OpenSearch for a 50k-record store; HNSW where exact recall is mandatory. Scale is the decisive constraint.

10. **RAG vs fine-tune vs prompt engineering.** New facts that change over time -> RAG (KB). Behavior/tone/format/style -> fine-tuning. Better outputs from same model -> prompt engineering. Trap: fine-tuning to add knowledge (expensive, static); RAG when the requirement is tone (prompt/fine-tune problem).

11. **Hallucination + grounding combo.** Product recommendations not in catalog, "invented items". Tempting partial answers: prompt engineering only, or Guardrails grounding only. Right: Knowledge Bases + RAG (retrieve from catalog first), then validate output against the catalog. Guardrails' Automated Reasoning check is the adjacent 2026 answer for logically verifiable claims; watch for it as the upgrade over plain grounding.

12. **Perceived latency vs real latency.** "Users report slow responses" with unique interactions (so caching will not help). Trap: provisioned throughput (fixes capacity, not first-token latency) or prompt caching (no repeat prefixes). Right: streaming (InvokeModelWithResponseStream / ConverseStream) to reduce perceived latency. For latency-sensitive variants, PerformanceConfigLatency=optimized.

13. **Prompt caching conditions.** Prompt caching pays only with repeated long prefixes (same system prompt / same large context). Trap: enabling it where "most interactions are unique". Right there: streaming or smaller model. When prefixes repeat heavily, prompt caching is the cost/latency answer.

14. **Provisioned throughput misuse.** Stem shows purchased provisioned capacity sitting idle while on-demand calls get throttled, code calling invoke_model with a base modelId. Traps: add more model units, add backoff retries, switch to streaming. Right: pass the provisioned model ARN (from CreateProvisionedModelThroughput) as modelId; fine-tuned models also REQUIRE provisioned throughput and cannot use on-demand at all.

15. **Cross-region inference for throttling/resilience.** Stem: throttling at peak, need resilience without buying provisioned throughput. Trap: buy provisioned throughput in one Region, or hand-rolled Lambda failover routing. Right: cross-Region inference profiles (geography codes in profile IDs) automatically distribute traffic across Regions with capacity. Not valid where data-residency rules forbid cross-Region movement.

16. **Batch inference scope.** 50% discount, S3 in/out. Trap: use it for an interactive assistant with a 2-second SLA. Right: batch is for offline/large-scale non-interactive jobs only.

17. **Guardrails block vs detect.** Stem: "notify if bullying language appears but do NOT block flagged responses". Trap: a blocking content filter. Right: guardrail in detect/monitor mode (content filter set to detect, notifications on intervene metrics without blocking). Detection without blocking = detect mode.

18. **SCP vs IAM permissions boundary for Bedrock governance.** Stem: org-wide, employees may use only approved models. Trap: permissions boundaries alone, or app-level checks. Right: SCPs at the org level (maximum permissions, e.g. require approved guardrail ID on InvokeModel) + permissions boundaries for per-role model limits. SCP = strongest org-level control; deploy guardrails across accounts with CloudFormation StackSets.

19. **Guardrails cannot do access control.** Trap: use Guardrails to enforce which IAM principals can call which model (resource-level access). Right: IAM policies/conditions. Guardrails enforce content safety (filters, PII, denied topics, word filters), not identity access.

20. **PII tool selection.** Discover PII in data at rest in S3 -> Macie. Detect PII in text inline -> Comprehend PII detection. Trap: Macie scanning CloudWatch Logs (Macie scans S3); Guardrails for everything (Guardrails redacts/blocks at invocation time but Comprehend is the detection tool). Pipeline shape: Comprehend detect -> redact -> Bedrock.

21. **VPC / no public internet.** Any stem with "no public internet" -> interface VPC endpoints (PrivateLink) for Bedrock runtime + Lambda in private subnets. Trap: NAT gateway options, public endpoints. NAT violates the constraint even when other parts look right.

22. **Model selection cascade (cost-aware routing).** Varying query complexity + cost pressure. Trap: one flagship model for everything. Right: route simple queries to small/cheap models (e.g. Haiku-class), complex to larger ones; classify complexity first. "Tiered FM usage based on query complexity" is the exam's phrase.

23. **Evaluation ladder.** Stem: choose model under limited resources. Trap: provider benchmarks alone (unverified), exhaustive human eval of everything (too expensive), deploy untested to production A/B. Right: automatic metrics first (fast/cheap screen), LLM-as-judge at scale for quality, cost-performance ratio analysis, human evaluation only on top candidates. Know: BLEU/ROUGE = cheap but miss paraphrase nuance; LLM-as-judge correlates best at scale; humans calibrate, not run every commit. A2I (human review) is for flagged critical interactions, not all traffic.

24. **Agents vs Flows vs Lambda.** Multi-step reasoning with tool calls -> Bedrock Agents (action groups + Lambda). Deterministic, fixed workflow -> Bedrock Flows (prompt chains, no-code). Trap: building agent orchestration out of raw Lambda + Step Functions when Agents/Flows do it natively; or using an Agent where the flow is fixed and deterministic (overhead). Supervisor + collaborator agents = the multi-agent pattern for department/specialty routing with per-KB IAM filtering.

25. **Prompt Management use.** Four required inputs, consistent output format, versioning, reuse across flows. Trap: AppConfig versioning of prompts (AppConfig versions config, prompts belong in Prompt Management), DynamoDB prompt store (custom overhead). Right: Bedrock Prompt Management (variables, templates, versions).

26. **Real-time collaboration with version control.** Multimedia content pipeline needing realtime collab + versioning. Trap: Knowledge Bases for multimedia processing (KB is for retrieval), Guardrails for extraction (no), Neptune for files (no). Right shape: Bedrock Data Automation (BDA) for extracting from docs/audio/video + Textract/Transcribe pairings, S3 versioning for files, AppSync GraphQL subscriptions + DynamoDB for realtime collaboration, Prompt Management versions for prompt version control.

27. **Quality gates in deployment.** "Prevent configs below quality threshold from deploying." Trap: manual review, CloudWatch alarms (reactive monitoring), Comprehend sentiment as a quality gate (wrong tool). Right: Bedrock evaluation jobs on prompt changes in CodePipeline, deploy only when scores exceed threshold.

28. **Caching strategy selection (multi-response).** Valid: semantic caching (near-duplicate queries via embeddings), prompt caching (shared prefixes), result fingerprinting for dedup/eviction. Invalid traps: cache everything indefinitely (stale data), disable caching because "non-deterministic" (wrong - variation is acceptable), cache model weights locally (impossible - Bedrock is managed).

29. **Streaming + API Gateway.** Trap (older knowledge): streaming needs Lambda function URLs. Current: API Gateway REST APIs support Lambda response streaming; HTTP APIs do not. The exam reflects current service state; watch feature recency.

30. **Token counting before the call.** "Proactively alert when approaching model-specific token limits." The working answer estimates token usage before the Bedrock call (count + compare against the model's limit). Post-call alarms are the trap family (see pattern 1).

31. **InvokeModel vs Converse API.** Exam expects Converse/ConverseStream knowledge as the modern unified API, but legacy stems may still use InvokeModel/InvokeModelWithResponseStream. Both families appear; streaming variants are the latency answer.

32. **Data-residency constraint kills cross-Region.** When the stem includes data-residency/regional compliance, cross-Region inference profiles become the trap (pattern 15 inverted). Look for the constraint before choosing.

33. **Fine-tuned model serving requirement.** Any option serving a fine-tuned/custom model via plain on-demand modelId is wrong; custom models need provisioned throughput. Also watch "custom model import" vs fine-tuning confusion.

34. **Multi-account Bedrock governance packaging.** The full-credit combo is usually two pieces: org-level control (SCP requiring approved guardrail/model) + per-account deployment (StackSets) + per-role boundaries. Single-mechanism options are the traps.

35. **"LEAST custom development effort" vs "MOST cost-effective" vs "LEAST operational overhead".** These three phrasings point at different winners. Least custom dev -> managed features over Lambda code. Least operational overhead -> fewest self-managed components. Most cost-effective -> token/model/caching math (smaller model, caching, batch) not necessarily the most managed option. Read the exact adjective.

---

## Multi-response ("Choose TWO / THREE") phrasing patterns

- Wording observed: "Which combination of steps will meet these requirements? (Choose two.)", "Which THREE caching strategies should be implemented...? (Select 3)". AWS style mixes "Choose two" and "(Select N)".
- No partial credit: getting one of two right scores zero. Stems are built so each correct choice covers a DIFFERENT requirement (e.g. one for prompt management, one for detect-only guardrails). The two answers rarely overlap in function.
- Common trap: one right + one "almost right" (blocking guardrail instead of detect-only; CloudWatch dashboard instead of evaluation job). The wrong options are constraint-violations of the second requirement, not random junk.
- Multi-response stems frequently pair one Domain 1 action with one Domain 3 or 4 action (build + govern, retrieve + secure, optimize + monitor).

---

## Service PAIRS tested together

- Guardrails + Agents (defense in depth: guardrails on agent inputs/outputs; prompt-injection blocking + audit of interventions)
- Knowledge Bases + OpenSearch Serverless / Aurora pgvector / MemoryDB (vector store choice by scale; hybrid search)
- Prompt Management + Prompt Flows + Bedrock evaluation jobs (versioned prompts, A/B testing, quality gates)
- Step Functions + Lambda (orchestration + resolvers; Distributed Map for parallel fan-out)
- CloudWatch (custom metrics, InvocationsIntervened, token dashboards) + model invocation logging (content-level audit)
- CloudTrail + IAM/SCP (who-called-what audit + org-level model governance)
- Cross-Region inference profiles + provisioned throughput (throughput strategy alternatives)
- Prompt caching + semantic caching + model cascade (cost optimization triad)
- Bedrock Data Automation + Textract/Transcribe (multimodal document ingestion)
- Comprehend (PII detect) + Macie (S3 discovery) + Guardrails (runtime PII redaction)
- Agents (supervisor/collaborator) + per-KB IAM filtering (multi-tenant data isolation)
- A2I + Bedrock evaluations + LLM-as-judge (human-in-the-loop eval pipeline)
- API Gateway REST + Lambda streaming (real-time UX)
- S3 (versioning) + AppSync subscriptions + DynamoDB (collaborative content pipelines)

---

## Stem phrasing conventions

- Scenario frame: "A <company type> is <building/doing X> by using Amazon Bedrock..." then 2-4 hard requirements, then "Which solution will meet these requirements [with the LEAST operational overhead / MOST cost-effectively / with the LEAST custom development effort]?"
- Constraint keywords that decide the answer: proactively, least operational overhead, least custom development effort, most cost-effective, no public internet, frequently changing data, without deploying new code, real-time, under N seconds, thousands of concurrent, detect but do not block, multi-account, data residency.
- "with the LEAST operational overhead" appears in nearly half the stems (per passer report). Treat as: fewest self-managed components.
- Distractors are long and plausible; each fails a different constraint. Find the killer constraint first.

---

## 10 most-tested specific facts

1. Fine-tuned models require Provisioned Throughput; on-demand modelId will not serve them (must pass the provisioned model ARN).
2. InvokeModelWithResponseStream / ConverseStream = reduced perceived latency for interactive apps; REST API Gateway now supports Lambda streaming (HTTP API does not).
3. Batch inference = ~50% discount, S3-based, offline only; never for interactive SLAs.
4. Cross-Region inference profiles route across Regions automatically to dodge throttling; not allowed under data-residency constraints.
5. Prompt caching needs repeated long prefixes; useless when interactions are unique.
6. Guardrails: block vs detect modes; content filters, denied topics, PII redaction, word filters. Detect mode + notification for "flag without blocking".
7. Model invocation logging (opt-in, S3/CloudWatch) captures prompt/response content; CloudTrail captures API-call metadata only.
8. Same embedding model at ingestion and query time in RAG; chunking strategy per document type (fixed-size vs semantic vs hierarchical).
9. Vector store by scale: Aurora pgvector small, OpenSearch IVFFlat/HNSW medium-large, flat exact search when 100% recall required on small data.
10. Temperature = 0 for deterministic/factual output; streaming + smaller-model routing + caching are the cost/latency levers; token math = (input + output) x price.

---

## 2026 Bedrock features showing up in questions

- Guardrails Automated Reasoning (check/verify logical claims against source; the step beyond plain grounding/RAG for verifiable accuracy).
- Cross-Region inference profiles as the default anti-throttling answer (vs buying provisioned throughput).
- Prompt caching as a first-class cost/latency lever (with its "repeated prefix" precondition).
- Supervisor/collaborator multi-agent pattern (Bedrock multi-agent collaboration) for department-scoped routing with per-KB isolation.
- Bedrock Data Automation (BDA) for multimodal ingestion (docs/audio/video), paired with Textract/Transcribe.
- Bedrock Flows (deterministic prompt chains) vs Agents (reasoning + tool use); Prompt Management for versioned templates.
- LLM-as-a-judge + Bedrock evaluation jobs + A2I as the eval ladder; human review only for flagged critical items.
- Strands Agents / Agent Squad appear in prep materials (Dec 2025 course updates); treat as emerging, likely lighter weight on the exam than core Bedrock Agents.
- API Gateway REST Lambda response streaming (Nov 2025) already reflected in questions.

---

## Sources consulted (pattern analysis only)

- dev.to: "How I Passed the AWS Certified Generative AI Developer Professional Exam: Real Questions, Real Patterns" (passer report, ~Aug 2026)
- dev.to: "How I Passed the AWS Generative AI Developer Professional Certification (and Earned the Early Adopter Badge)" (passer report, Dec 2025)
- medium.com: "I Passed the AWS GenAI Developer Pro" by Maryia Krauchanka (passer report, ~Apr 2026)
- github.com/Tevaalgorithms/aws-aip-c01-exam-prep (exam tips: embedding-model consistency, provisioned throughput for fine-tuned models, PrivateLink, batch inference, hybrid search, cross-region inference, temperature 0)
- examtopics.com AIP-C01 discussions (stem phrasing, multi-response shape, multi-agent supervisor pattern, detect-only guardrail item)
- whizlabs.com AIP-C01 sample questions page (multi-response caching item, eval-ladder item, exam facts: 75 Q, 180 min, 750/1000)
- tutorialsdojo.com AIP-C01 sampler page (topic coverage list)
- dumps-files/dumpsolutions AIP-C01 dumps (stem phrasing + trap shapes only; nothing copied)
- github.com/ka6wke AIP-C01 domain study notes (domain 3 and 4 tips)
- passitexams.com AIP-C01 success path (architecture patterns: Step Functions, VPC endpoints, KMS, model cascade, Strands/Agent Squad, observability)
- udemy.com AIP-C01 course pages (Maarek + Frank Kane course; Maarek exam craft via scribd slide deck: elimination, avoid over-complicated options)

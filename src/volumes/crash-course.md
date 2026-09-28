---
slug: volume-crash-course
file: volume-crash-course.html
title: "AIP-C01 Crash Course: the whole exam in one volume"
label: "Crash Course · One-Volume Sprint"
track: aipc01
---

# AIP-C01 Crash Course {#aip-c01-crash-course}

<style>
details.cc-qa{border:1px solid var(--line,#2a2a2a);border-radius:8px;padding:.6rem .9rem;margin:.5rem 0;background:var(--card,#141414)}
details.cc-qa summary{cursor:pointer;font-weight:600;list-style:none}
details.cc-qa summary::-webkit-details-marker{display:none}
details.cc-qa summary::before{content:"+ ";color:var(--accent,#4da3ff)}
details.cc-qa[open] summary::before{content:"\2212 "}
details.cc-qa blockquote{margin:.5rem 0 0;border-left:3px solid var(--accent,#4da3ff);padding-left:.8rem;color:inherit}
</style>

The entire exam in one volume. No stories, no padding. Decision rules, numbers, traps, and 30 rapid-fire questions. If you know everything here cold, you can answer every item on the exam.

## The exam in 30 seconds {#the-exam-in-30-seconds}

| Fact | Value |
|---|---|
| Questions | 75 (65 scored, 10 unscored) |
| Time | 180 minutes (about 2.4 min per question) |
| Pass | 750 out of 1000 |
| Cost | $300 |
| Formats | Multiple choice + multiple response (select 2/3, no partial credit) |
| D1 Foundation Models, Data & Compliance | 31% (about 20 scored) |
| D2 Implementation & Integration | 26% (about 17 scored) |
| D3 AI Safety, Security & Governance | 20% (about 13 scored) |
| D4 Operational Efficiency & Optimization | 12% (about 8 scored) |
| D5 Testing, Validation & Troubleshooting | 11% (about 7 scored) |

How the exam asks: multi-paragraph company scenario, 2 to 4 hard requirements, 4 long plausible options. Three options are good ideas in the wrong context. One satisfies every constraint at once. Find the killer constraint first, then compare survivors.

## How to use this volume {#how-to-use-this-volume}

- **10 minutes:** read "The exam in 30 seconds," the numbers sheet, and the top 30 traps.
- **1 hour:** add the per-domain decision rules (the "if X, pick Y" lines).
- **1 day:** do all 30 rapid-fire questions, then re-read every rule you missed.

## D1 rapid-fire: Foundation Models, Data & Compliance (31%) {#d1-rapid-fire}

The approach ladder, cheapest first. **Prompt engineering** (new format, tone, few-shot; no new knowledge). **RAG / Knowledge Bases** (private, current, or cited facts the model was not trained on). **Agents** (actions: API calls, databases, multi-step tool use). **Fine-tuning** (new behavior baked into weights; labeled data in S3; needs Provisioned Throughput to serve).

**If the stem says X, pick Y:**

- "Facts change over time" or "must cite sources" → RAG (Knowledge Bases), never fine-tuning.
- "New tone, format, style, behavior" → fine-tuning or prompt engineering, never RAG.
- "Take actions," "call APIs," "multi-step with tools" → Bedrock Agents.
- "Unstructured docs (PDF, HTML)" → Knowledge Bases. "Relational data, SQL" → text-to-SQL on RDS. Never embed tables into a vector store.
- "Small dataset" (under ~1M records) → Aurora Serverless with pgvector. "Large" → OpenSearch with HNSW/IVFFlat. "100% recall on small data" → exact flat search.
- "Throttled at peak, needs resilience" → cross-region inference profiles. Dead under data-residency constraints.
- "Repeated long system prompt" → prompt caching. "Unique interactions" → streaming or a smaller model, never caching.
- "Users report slow responses" → streaming (ConverseStream) for perceived latency. Provisioned Throughput fixes capacity, not first-token speed.
- "Cheapest for nightly 200k summaries" → batch inference (S3 in, S3 out, ~50% off, hours of latency). Never for interactive SLAs.
- "Swap models without redeploying" → model ID in AppConfig, read at runtime. CloudFormation changes are deployments.

**Must know cold:**

- Converse is the unified API (system, messages, inferenceConfig, toolConfig, guardrailConfig). InvokeModel is provider-specific raw bodies, and the ONLY path for embeddings.
- `guardrailConfig` on Converse needs guardrail ID + version; `trace=enabled` shows what fired.
- `stopReason` values: `end_turn` (done), `max_tokens` (truncated), `guardrail_intervened` (blocked).
- Same embedding model at ingestion and query time, or retrieval silently breaks.
- Fine-tuned and custom models REQUIRE Provisioned Throughput. A base model ID will not serve them.
- Temperature 0 = deterministic. Temperature/topP both set = they interact; pick one.
- Token math: cost = (input tokens + output tokens) x price. Estimate before the call for proactive alerts.

## D2 rapid-fire: Implementation & Integration (26%) {#d2-rapid-fire}

**If the stem says X, pick Y:**

- "Reasoning with tools, decides steps itself" → Bedrock Agents (action groups + Lambda).
- "Fixed sequence, same steps every time" → Bedrock Flows (deterministic prompt chains). Agents are overhead here.
- "Which agent call shape" → `invoke_agent` with `agentId` + `agentAliasId` (alias PROD, never DRAFT) + `sessionId` (the memory key) + `inputText`. Returns a stream you iterate.
- "Agent ignores the new action group" → PrepareAgent was skipped. Config changes need prepare before DRAFT picks them up.
- "Lambda action function" → parameters arrive as a LIST of {name, value} dicts. Response needs the exact nested shape with `messageVersion`, `actionGroup`, `function` echoed back and the result string in `responseBody.TEXT.body`.
- "Task runs longer than 15 minutes" → Lambda is dead. Go async or Step Functions.
- "Wait for human approval, takes hours" → Step Functions Standard with wait-for-callback. Express caps at 5 minutes and cannot pause.
- "Process 10k S3 objects in a tight window" → Step Functions Distributed Map (up to 10k parallel children).
- "Stable URL, auth, throttling in front of Bedrock" → API Gateway + Lambda. Direct SDK calls win only when latency is king and no auth is needed.
- "Versioned prompt templates reused across flows" → Prompt Management. Not AppConfig, not DynamoDB.
- "Quality gate before deploy" → Bedrock evaluation jobs in the pipeline; deploy only above the score threshold.

**Must know cold:**

- Agent trace: `enableTrace=true` on `invoke_agent` returns the reasoning trace. The exam's transparency answer.
- Multi-agent pattern: supervisor routes to collaborators, per-KB IAM filtering for tenant isolation.
- Async single request: `start_async_invoke`, poll or events, result to S3. Not streaming (streaming is tokens to a waiting user).
- API Gateway REST APIs support Lambda response streaming. HTTP APIs do not.
- Session memory is keyed by `sessionId`. Reusing one ID across users leaks conversations.

## D3 rapid-fire: AI Safety, Security & Governance (20%) {#d3-rapid-fire}

Guardrails can: content filters (hate, violence, sexual, misconduct), denied topics, word filters, PII detection and redaction, grounding check (hallucination), contextual grounding check, automated reasoning checks. Guardrails can NEVER do: IAM, tenant isolation, data extraction, token quotas, billing.

**If the stem says X, pick Y:**

- "Notify on bad content but do NOT block" → guardrail in **detect mode**, notifications on intervene metrics. Block mode violates the constraint.
- "Block specific topics in and out" → denied topics policy on both inputs and outputs.
- "Find PII in S3 data" → Macie. "Detect PII in live text" → Comprehend. "Redact at call time" → Guardrails. The pipeline is Comprehend detect, redact, then Bedrock.
- "Who called which model and when" → CloudTrail. "Which prompts were blocked and why" → CloudWatch custom metrics. "Full prompt and response text" → model invocation logging (opt-in) to S3.
- "Restrict models across the whole org" → SCPs (require approved guardrail on InvokeModel). Per-role caps → permissions boundaries. Deploy at scale → StackSets.
- "Bedrock with no public internet" → interface VPC endpoints + Lambda in private subnets. NAT gateway violates the constraint.
- "Customer data must not train models" → the model terms/opt-out. Also: invocation logging data stays in your account.
- "Most mathematically certain that outputs obey policy" → Automated Reasoning checks (2026 feature; formal logic), above plain content filters.

**Must know cold:**

- Model eval: programmatic needs ground truth (accuracy, stability, toxicity). LLM-as-judge needs no labels (correctness, faithfulness, fluency). Human eval: last resort, samples only.
- Provider benchmarks never decide your model choice. They are marketing until you run your own eval.
- "Built-in alignment is enough" is always wrong. The deployer owns evaluation and governance.

## D4 rapid-fire: Optimization (12%) {#d4-rapid-fire}

The exam's three adjectives, three different winners. **"Least operational overhead"** → fewest self-managed components (Aurora Serverless, Converse, managed routers). **"Least custom development effort"** → managed features over your Lambda code. **"Most cost-effective"** → token math (smaller model, caching, batch, cascade).

**If the stem says X, pick Y:**

- "Throttled at peak" → Provisioned Throughput (reserved capacity; pass the provisioned ARN as modelId). Fine-tuned models need PT, base models can use on-demand.
- "Costs scale with mixed simple/hard queries" → intelligent prompt routing (cascade simple to cheap, escalate hard).
- "Repeated long prefix, cost pressure" → prompt caching (same context block, cache point set right).
- "Nightly bulk, no SLA" → batch inference (~50% off).
- "Route by complexity for cost" → prompt routers. "Route by region for availability" → inference profiles. Never swap them.
- "Users see slow first token" → streaming. Not PT, not caching.
- "Which metric proves the cache works" → cache read hit rate, not total token spend.

**Must know cold:**

- PT bought but on-demand still throttles → code passes the base model ID instead of the provisioned ARN.
- Prompt routers have a default fallback model. If the fallback fires too often, the tier boundaries are wrong.
- `converse()` `inferenceConfig`: `maxTokens`, `temperature`, `topP`, `stopSequences`. Same shape on InvokeModel? No. InvokeModel takes raw provider JSON.

## D5 rapid-fire: Testing & Validation (11%) {#d5-rapid-fire}

**If the stem says X, pick Y:**

- "Compare models cheaply at scale" → automatic metrics first (ROUGE, faithfulness), then LLM-as-judge on the survivor, humans on flagged samples only. Never humans-on-everything under a budget.
- "Critical flagged interactions" → A2I (human review loop). Not all traffic.
- "Answers confident but wrong after a re-sync" → check the embedding model version and chunking config. The re-sync is the only change; debug the change.
- "RAG retrieval fails silently" → same embedding model at ingest and query; chunk boundaries did not split key facts; KB sync status is in-sync.
- "AccessDenied on InvokeModel" → check model availability in the region BEFORE debugging IAM.
- "Model ignores new prompt template" → Prompt Management version not published, or AppConfig serving a cached value.
- "Test without production traffic" → model evaluation jobs with a golden dataset; A/B with two aliases; shadow traffic through inference profiles.

**Must know cold:**

- Change-point debugging: the broken thing is whatever changed most recently. Debug the delta.
- Eval datasets need labels for programmatic metrics. LLM-as-judge works unlabeled.
- `max_tokens` stopReason on good-looking answers = output was CUT, not finished.

## Must-memorize numbers {#must-memorize-numbers}

| Item | Number |
|---|---|
| Questions / scored / time | 75 / 65 / 180 min |
| Pass score | 750 / 1000 |
| Lambda max duration | 15 minutes |
| Step Functions Express max duration | 5 minutes |
| Step Functions Distributed Map parallel children | up to 10,000 |
| Batch inference discount | ~50% off on-demand |
| Domain weights | D1 31%, D2 26%, D3 20%, D4 12%, D5 11% |
| Approximate scored questions per domain | D1 20, D2 17, D3 13, D4 8, D5 7 |

## Top 30 traps in one line each {#top-30-traps}

1. Lambda waiting, sleeping, or polling past 15 minutes. It dies.
2. "No ML team / least effort" means custom builds lose to Bedrock managed features.
3. Knowledge bases serve documents. No API calls, no access control, no actions.
4. Changing documents or citations = RAG, never fine-tuning.
5. Profiles = availability, routers = cost, Provisioned Throughput = reserved capacity.
6. Guardrails filter content. Not IAM, not tenant isolation, not token quotas.
7. Cheapest option that meets every requirement wins. Premium extras without a stated need lose.
8. CloudFormation = deployment. Runtime switching without redeploys = AppConfig.
9. ElastiCache is ephemeral caching. Durable vectors live in a vector store.
10. Cross-region failover violates data-residency constraints. Check the region first.
11. Converse + Prompt Management + guardrailConfig is rejected. ApplyGuardrail standalone works around it.
12. Agent config changed but behavior did not = PrepareAgent was skipped.
13. AccessDenied on InvokeModel = check regional model availability before IAM.
14. Converse is text generation. Embeddings go through InvokeModel.
15. Built-in safety never transfers evaluation and governance to AWS. You own it.
16. "Proactively" kills every reactive option. Count tokens before the call, not after.
17. Fabricated features: real service + invented capability (S3 nodes in Flows, Guardrail token quotas).
18. CloudTrail = who called what. CloudWatch = what was blocked and why. Invocation logging = prompt and response text.
19. Express = 5-min cap, no callbacks. Hours-long human waits need Standard.
20. Tight window over many objects = Distributed Map. Sequential dies on the clock.
21. Small vectors = Aurora pgvector. Large = OpenSearch. 100% recall small = exact flat search.
22. Slow first token = streaming. PT fixes capacity, caching needs repeated prefixes.
23. Prompt caching needs repeated long prefixes. Unique traffic makes it dead weight.
24. Bought PT but throttled = code passes the base model ID, not the provisioned ARN.
25. "Notify but do not block" = guardrail detect mode.
26. SCPs = org-wide max permissions. Permissions boundaries = per-role caps.
27. Macie finds PII in S3. Comprehend detects in text. Guardrails redact at call time.
28. No public internet = interface VPC endpoints. NAT gateway violates the constraint.
29. Eval ladder: automatic metrics, then LLM-as-judge, humans on top candidates only.
30. Adjectives decide: least custom dev = managed features. Least overhead = fewest components. Most cost-effective = token math.

## 30 rapid-fire questions {#30-rapid-fire-questions}

One question, one-line why. Cover every answer wrong and you are not ready.

:::details CC01. Stem says "answer over contracts that update monthly, with citations." Why is fine-tuning wrong?

Fine-tuning bakes static weights. Monthly changes need re-training, and it cannot cite sources. RAG reads current docs.

:::

:::details CC02. Stem says "same model, 90% of prompts share a 4k system prompt." Which cost lever?

Prompt caching. Repeated long prefixes are its only precondition, and this stem hands it to you.

:::

:::details CC03. `invoke_agent` must use the PROD deployment, not the draft. Which parameter?

`agentAliasId` set to the PROD alias. Agent ID alone routes to DRAFT, the classic bug.

:::

:::details CC04. Lambda action function receives `event["parameters"]`. What shape?

A list of {"name":..., "value":...} dicts. Treating it as a plain dict drops every parameter.

:::

:::details CC05. Approval step takes 4 hours. Express or Standard?

Standard with wait-for-callback. Express caps at 5 minutes and cannot pause for hours.

:::

:::details CC06. "Block bullying topics" vs "notify on bullying but never block." What changes?

Guardrail mode: block vs detect. Same filter, different mode. The constraint is about the mode, not the feature.

:::

:::details CC07. Compliance wants full prompt and response text for blocked calls. CloudTrail or invocation logging?

Invocation logging (opt-in) to S3. CloudTrail records API metadata only, never token content.

:::

:::details CC08. PT purchased, on-demand still throttles, code uses base model ID. Fix?

Pass the provisioned model ARN as `modelId`. Idle capacity means the code never routes to it.

:::

:::details CC09. `stopReason` is `max_tokens` on a clean-looking answer. What happened?

Output was cut mid-generation, not finished. Raise maxTokens or shorten the input.

:::

:::details CC10. "Proactively alert before token limits." Alarm on InputTokenCount or pre-call counting?

Pre-call counting. The metric fires after the call runs, which is reactive, and the stem demands proactive.

:::

:::details CC11. Small vector dataset, 100% recall required. HNSW or exact flat search?

Exact flat search. HNSW is approximate by design; small data makes the exact scan affordable.

:::

:::details CC12. Embeddings for the knowledge base. Converse or InvokeModel?

InvokeModel. Converse is text generation only and has no embedding path.

:::

:::details CC13. Agent ignores the new action group. First check?

PrepareAgent was skipped. Config changes need prepare before the draft behavior changes.

:::

:::details CC14. "Cheapest nightly 500k-row classification." Realtime Converse or batch?

Batch inference (S3 in, S3 out, ~50% off). Realtime pricing for offline bulk is the expensive default.

:::

:::details CC15. Two days to compare two models. Humans read everything or automatic ladder?

Automatic metrics first, LLM-as-judge on the survivor, humans on flagged samples. The ladder climbs in cost order.

:::

:::details CC16. Cross-region inference profile proposed, stem requires data residency in one region. Verdict?

Reject it. Profiles route across regions, which violates the residency constraint. Check the region first.

:::

:::details CC17. "Least operational overhead" for vectors on 200k records. Self-managed OpenSearch or Aurora pgvector?

Aurora Serverless with pgvector. The adjective picks fewest self-managed components, not best raw scale.

:::

:::details CC18. Answers "confident but wrong" after a knowledge base re-sync. Debug generation or retrieval?

Retrieval. The re-sync is the only change: check embedding model version and chunking config drift.

:::

:::details CC19. PII must be found across all S3 buckets. Comprehend or Macie?

Macie. Comprehend scans text you send it; Macie discovers PII across S3 at rest.

:::

:::details CC20. Bedrock in a VPC with no public internet. NAT gateway or interface endpoints?

Interface VPC endpoints. A NAT gateway gives public internet access, violating the explicit constraint.

:::

:::details CC21. Stem offers "Flows with an S3 copy node" as an option. Trust it?

No. Fabricated feature. Flows have no S3 copy action node. Verify node and feature lists before picking.

:::

:::details CC22. Streaming vs Provisioned Throughput for "users report slow responses" on unique queries. Pick?

Streaming (ConverseStream). PT fixes capacity, caching needs repeated prefixes, neither speeds first token.

:::

:::details CC23. `sessionId` reused across all users of a support bot. Risk?

Conversation memory leaks between users. Session ID is the memory key; one ID per user session.

:::

:::details CC24. Restrict model access across 40 AWS accounts. SCP or per-account IAM roles?

SCPs via Organizations (deployed with StackSets). Per-account roles are 40 chances to drift.

:::

:::details CC25. Fine-tuned model served with on-demand pricing. Works?

No. Fine-tuned and custom models require Provisioned Throughput. The base model ID will not serve them.

:::

:::details CC26. "Most mathematically certain outputs obey policy." Content filter or Automated Reasoning checks?

Automated Reasoning checks. Formal logic verification, a stronger guarantee than classifier filters (2026 feature).

:::

:::details CC27. Prompt Management + guardrailConfig on Converse is rejected. Workaround?

ApplyGuardrail as a standalone call. The combination is rejected, so split the calls.

:::

:::details CC28. Temperature 0.7 AND topP 0.9 both set. Fine?

They interact. Set one, not both, or sampling behavior gets unpredictable.

:::

:::details CC29. Distributed Map vs 10k sequential Lambda invocations for a 30-minute window. Pick?

Distributed Map, up to 10k parallel children. Sequential dies on the clock; plain Lambda fan-out dies on orchestration overhead.

:::

:::details CC30. Evaluator asks which model is better for YOUR prompts. Provider benchmark or your own eval job?

Your own eval job. Provider benchmarks never measure your data, your prompts, or your quality bar.

:::

You finished the crash course. Missed more than five? Re-read the decision rules for the domains you missed, then do the full 200-question bank. Missed five or fewer? You are ready to schedule.

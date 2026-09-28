---
slug: volume-question-bank
file: volume-question-bank.html
title: "AWS AIP-C01 Question Bank: 192 Exam-Style Questions plus 75-Question Mock Exam"
label: "Question Bank"
track: aipc01
---

# AWS AIP-C01 Question Bank

140 exam-style questions across all five domains, weighted like the real exam, plus 52 bonus professional-bar questions (Q141-Q192), plus a 75-question mock exam. Generic content only.

FACT-CHECK 2026-09-28: all 140 questions plus the 75-question mock were checked against live AWS documentation on 2026-09-28. Every distractor uses a real service or feature that is wrong for a real, current reason; no fictional service names were found. PROFESSIONAL-BAR AUDIT 2026-09-28: 55 associate-level questions rewritten in place (same ids, same correct letters, mock-exam links and answer key unchanged); 52 bonus professional-bar questions added as Q141-Q192 (ids q-d1-201..216, q-d2-201..213, q-d3-201..211, q-d4-201..206, q-d5-201..206); all new content original, no copied bank items.

:::panel

**Last verified: 2026-09-28 against AWS documentation.** Correct answers, service facts, and API names were checked against current AWS docs on this date. No dollar pricing is asserted anywhere in this bank, so nothing here goes stale with rate changes.

:::


:::figure assets/img/mermaid/09-bank-mix.svg

The 192-question bank follows the exam's domain weights: 60 questions for D1, 49 for D2, 39 for D3, 23 for D4, and 21 for D5.

*Generated diagram for this guide.*

:::

:::panel

**How to use this bank.** Read each question, pick your answer, then open
Reveal answer and explanation to check. Every explanation covers why the correct answer is right, why each
distractor is wrong, and the trap AWS set. **Multiple-response questions are all-or-nothing:** on the real exam you
must select every correct option (and no incorrect ones) to earn credit. There is no partial credit and no penalty for
guessing, so never leave a question blank.

:::

:::panel

**Maarek-style rule of thumb.** When torn between plausible options, prefer the
more managed, more serverless, lower-operational-overhead answer. Custom builds are almost never correct unless the
scenario explicitly requires something no managed service does.

:::

## Domain 1: Foundation Model Integration, Data Management, and Compliance (31% of the exam, 44 questions) {#sec-d1}

**Decision reference.** Climb in order and stop at the cheapest rung that works.

:::ladder

1. **Prompt engineering** — New format, tone, few-shot, chain-of-thought. No new knowledge.
2. **RAG / Knowledge Bases** — Private, current, or cited facts the model was not trained on.
3. **Agents** — Actions: API calls, databases, multi-step tool use, session memory.
4. **Fine-tuning** — New behavior baked into weights. Labeled data in S3, then usually Provisioned Throughput.
5. **Custom model** — Last resort. Out of scope for this exam as a build task.

:::

**How to read this diagram.**

:::walkthrough

1. Rung 1 is the default: if the need is only format, tone, or examples, prompt engineering solves it with zero infrastructure.
2. Rung 2 is for knowledge: documents that change (quarterly policies) or need citations point to RAG with Knowledge Bases.
3. Rung 3 is for actions: when the task calls APIs, queries databases, or reasons across tools, that is agentic.
4. Rung 4 is for behavior: a consistent voice or classification repeated millions of times gets baked into weights via fine-tuning.
5. Rung 5 almost never appears as a correct answer on this exam; distractors love it anyway.
6. If this ladder breaks (you skip rungs), you pay training costs for a retrieval problem or retraining for a prompt problem.
:::

:::pq {#q-d1-001}

*D1 · EASY · ONE ANSWER* — q-d1-001 · 1.1 Solution design

**Q1.** A retail company wants a chatbot that answers questions from its 2,000-page returns policy. The policy changes every quarter, and every answer must cite the exact policy section it came from. Which approach should the developer choose first?

- A. Fine-tune a foundation model on the policy PDFs again every quarter
  > Fine-tuning bakes knowledge into weights, so every quarterly change needs a new training job, and it gives no citations. That is the expensive wrong ladder rung.
- B. Build a retrieval-augmented generation (RAG) solution with a Bedrock Knowledge Base over the policy documents <!-- correct -->
- C. Write one long system prompt containing the full policy text
  > A 2,000-page policy will not fit reliably in a prompt, quarterly edits mean prompt surgery, and there is no citation mechanism. Prompt engineering cannot carry changing private knowledge.
- D. Train a custom model from scratch on company documents
  > Training from scratch is out of scope for this exam and wildly disproportionate: months of work and cost when a managed RAG service solves it.

**Why B is correct:** RAG is the correct first step: the knowledge is private, changes quarterly, and needs citations. A Knowledge Base retrieves the current sections at query time and RetrieveAndGenerate returns source attributions, with no retraining.

**The trap AWS set here:** fine-tuning when the scenario says documents change quarterly and answers must cite sources. That is always RAG (master trap 7).

:::

:::pq {#q-d1-002}

*D1 · EASY · ONE ANSWER* — q-d1-002 · 1.1 Solution design

**Q2.** A startup CTO will approve GenAI spending only after the team proves the approach works on real data. What should the team do before buying Provisioned Throughput or building production infrastructure?

- A. Run a proof of concept on Bedrock using on-demand inference <!-- correct -->
- B. Purchase Provisioned Throughput now to lock in capacity
  > Buying Provisioned Throughput before validation commits hourly spend to an unproven design. PT is for steady production baselines, not experiments.
- C. Build a GPU cluster on EC2 for full control
  > An EC2 GPU cluster is maximum operational overhead for an unproven idea, the opposite of the exam's managed-first bias.
- D. Sign a long-term model hosting contract
  > A hosting contract locks in cost before the team knows which model or pattern even works.

**Why A is correct:** Bedrock on-demand inference needs no commitment, so a PoC validates feasibility, quality, and cost on real data before any capacity purchase. The blueprint calls this out explicitly: PoC first, commit later.

**The trap AWS set here:** committing to capacity (Provisioned Throughput, EC2, contracts) before a proof of concept exists.

:::

:::pq {#q-d1-003}

*D1 · MEDIUM · SELECT 2* — q-d1-003 · 1.1 GenAI Lens

**Q3.** A platform team wants every product squad to build GenAI features in a consistent, reviewable way. Which TWO practices align with the Well-Architected Generative AI Lens? (Select TWO)

- A. A shared, versioned prompt template library every squad reuses <!-- correct -->
- B. One central guardrail policy attached to all squad applications <!-- correct -->
- C. Each squad picks its own vector database, models, and prompt style
  > Ad-hoc per-squad choices are exactly what the Lens is meant to replace; they make reviews and incident response impossible.
- D. Model choice based only on published benchmark leaderboards
  > Benchmarks ignore cost, latency, and compliance constraints, so benchmark-only selection fails the Lens review.
- E. Squads deploy straight to production with no evaluation step
  > Skipping evaluation violates the Lens outright; validation gates are a core pillar.

**Why A, B is correct:** The GenAI Lens rewards standardized reusable components: shared prompt templates and one central guardrail policy mean consistent behavior, one place to audit, and design reviews against a known baseline.

**The trap AWS set here:** benchmark-only model selection and ad-hoc per-team stacks dressed up as autonomy.

:::

:::pq {#q-d1-004}

*D1 · HARD · ONE ANSWER* — q-d1-004 · 1.1 Behavior vs knowledge

**Q4.** A support organization handles 3 million chat replies per month. Every reply must follow a strict 4-step format with a fixed sign-off, in the company voice. The content of each reply varies per customer, but the format never changes. Cost per reply is the top concern. What should the developer do?

- A. Use RAG so the model can look up the format examples each time
  > RAG retrieves knowledge, but the need here is behavior (format), not facts. Retrieval adds latency and cost to every call for zero benefit.
- B. Fine-tune (distill) a small model on the format until it reproduces it reliably, then serve the small model <!-- correct -->
- C. Send every request to the largest flagship model with a long system prompt
  > The flagship model can do the format, but at 3M replies a month the per-token cost is the whole problem. Correct capability, wrong economics.
- D. Build a rule-based template engine with no model at all
  > A pure template engine cannot handle the variable content of each reply; the task still needs generation, just cheap generation.

**Why B is correct:** This is baked-in behavior repeated millions of times: the format never changes, so paying flagship-model prices per reply is wasteful. Distilling the behavior into a small fine-tuned model gives consistent formatting at a fraction of the per-token cost. This is the bottom of the grounding ladder used correctly.

**The trap AWS set here:** reaching for RAG when the scenario needs a behavior baked into weights, and reaching for the flagship model when repetition economics demand a small distilled model (master trap 7).

:::

:::pq {#q-d1-005}

*D1 · HARD · ONE ANSWER* — q-d1-005 · 1.1 Architecture under constraints

**Q5.** A travel company is designing a GenAI trip planner with four hard constraints: support 12 languages, 99.9% availability with automatic failover if a region fails, switch foundation models without code deployments, and prove value to the CTO before production spend. Which combination of steps meets ALL four constraints?

- A. Run a Bedrock proof of concept first; use cross-region inference profiles for failover; route model calls through Lambda plus API Gateway with model identifiers in AppConfig; review the design against the Generative AI Lens <!-- correct -->
- B. Deploy an EC2 fleet behind an Application Load Balancer with hardcoded model endpoints, then go straight to production
  > EC2 plus ALB gives availability inside one region only, so a regional outage still kills the app, and hardcoded endpoints plus skipping the PoC violate two more constraints.
- C. Deploy in a single region using the model with the best published benchmarks, and use CloudFormation to switch models
  > Single-region deployment cannot survive a regional failure, benchmarks ignore the other constraints, and CloudFormation changes are deployments, which violates no-code switching (master trap 8).
- D. Train a custom multilingual model and skip the proof of concept to save time
  > Training a custom model for multilingual support ignores that Bedrock FMs already cover the languages, and skipping the PoC violates the CTO's explicit constraint.

**Why A is correct:** Each constraint maps to one decision: PoC on Bedrock validates before spend; cross-region inference profiles give automatic regional failover; Lambda plus API Gateway plus AppConfig lets ops change the model identifier at runtime with no redeploy; the GenAI Lens is the exam's named standard for design reviews.

**The trap AWS set here:** each distractor satisfies three constraints and quietly violates one. Map every constraint to a decision before picking.

:::

:::pq {#q-d1-006}

*D1 · MEDIUM · ONE ANSWER* — q-d1-006 · 1.2 Model selection

**Q6.** A fraud-detection API must classify 40,000 transactions per hour with a p99 latency budget of 300 ms. Three candidate models clear the team's minimum accuracy bar on a labeled test set: a flagship model (best accuracy, 900 ms p99, highest token price), a mid-size model (meets the accuracy bar, 220 ms p99, moderate price), and a small model (just under the accuracy bar, 90 ms p99, cheapest). Finance caps the monthly token budget. Which selection approach is most correct?

- A. Measure each candidate against the accuracy bar, the 300 ms p99 latency budget, and the token budget, then choose the smallest model that satisfies all three (the mid-size model) <!-- correct -->
- B. Choose the flagship model because it has the highest published benchmark accuracy
  > Benchmarks ignore the 300 ms latency budget and the token cap; the flagship fails both hard constraints.
- C. Choose the small model because it is cheapest and fastest
  > It scores below the minimum accuracy bar, so it fails the correctness constraint that the scenario states explicitly.
- D. Choose the flagship model and add Provisioned Throughput to fix the latency
  > Provisioned Throughput guarantees capacity, not sub-900 ms inference speed; it cannot make a slow model fast.

**Why A is correct:** Model selection is a constraint-satisfaction problem, not a leaderboard contest. The mid-size model is the only candidate that simultaneously clears the accuracy bar, the 300 ms p99 latency budget, and the token budget. The exam rewards measuring capability, cost per token, latency, context window, and regional availability against the scenario's hard constraints, then picking the smallest model that satisfies all of them.

**The trap AWS set here:** Benchmark worship. The exam punishes picking the highest-scoring model when the scenario gives latency and cost constraints that it violates.

:::

:::pq {#q-d1-007}

*D1 · MEDIUM · SELECT 3* — q-d1-007 · 1.2 Runtime model switching

**Q7.** Operations must be able to switch the application between three foundation models without code deployments. Which THREE services form the standard pattern? (Select THREE)

- A. AWS AppConfig <!-- correct -->
- B. Amazon API Gateway <!-- correct -->
- C. AWS Lambda <!-- correct -->
- D. AWS CloudFormation
  > CloudFormation changes are deployments, which directly violates the no-redeploy requirement (master trap 8).
- E. Amazon EventBridge
  > EventBridge routes events; it does not store configuration, so it cannot serve as the model-selection store.

**Why A, B, C is correct:** This is the exam's canonical trio: Lambda holds the routing logic, API Gateway exposes one stable endpoint with throttling, and AppConfig stores the model identifier as runtime configuration that ops can change without a deploy.

**The trap AWS set here:** CloudFormation and EventBridge as the configuration store. Only AppConfig is the runtime no-redeploy mechanism (master trap 8).

:::

:::pq {#q-d1-008}

*D1 · MEDIUM · ONE ANSWER* — q-d1-008 · 1.2 Resilience

**Q8.** A customer-support assistant depends on a foundation model that is available in only two AWS regions. The product requirement is automatic survival of a full regional outage with no manual intervention. Separately, EU customer data must not leave the EU. Which design meets both requirements?

- A. Invoke the model through a cross-region inference profile scoped to EU regions (eu. prefix) so failover is automatic and data stays in the EU <!-- correct -->
- B. Use a us. cross-region inference profile because it has the most destination regions
  > Routing EU customer data through US regions violates the stated data-residency requirement.
- C. Deploy the application behind an Application Load Balancer in two Availability Zones
  > Multi-AZ survives zone failures, not a full regional outage; the requirement is region-level failover.
- D. Keep a single-region deployment and document a manual runbook for regional failover
  > A manual runbook is not automatic failover and fails the product requirement directly.

**Why A is correct:** A cross-region inference profile with the eu. prefix routes requests across EU regions on the AWS backbone when one region fails, giving automatic failover without manual intervention, while keeping data inside the EU boundary. This satisfies the resilience requirement and the data-residency constraint at the same time.

**The trap AWS set here:** Failover versus data residency. The exam pairs automatic failover with a residency constraint so the biggest failover footprint becomes the wrong answer.

:::

:::pq {#q-d1-009}

*D1 · HARD · ONE ANSWER* — q-d1-009 · 1.2 Routing mechanisms

**Q9.** An application sends 60% simple FAQ prompts and 40% complex multi-step reasoning prompts to Bedrock. The CFO demands lower token spend without hurting answer quality on the hard prompts. Which mechanism should the developer implement?

- A. A prompt router (model router) that sends simple prompts to a cheap small model and complex prompts to the flagship model <!-- correct -->
- B. A cross-region inference profile
  > Cross-region inference profiles route for availability across regions, not for cost by complexity. Wrong mechanism for this problem.
- C. Provisioned Throughput on the flagship model
  > Provisioned Throughput reserves capacity and protects latency; it does not make simple prompts cheaper.
- D. Prompt caching on the flagship model
  > Prompt caching cuts cost on repeated prefixes, but these prompts vary per question, so there is little repeated prefix to cache.

**Why A is correct:** This is cost-quality routing by prompt complexity, which is exactly what prompt routers (model routers) do. Simple prompts get cheap inference, hard prompts keep flagship quality, and total spend drops. Do not confuse this with availability routing or reserved capacity.

**The trap AWS set here:** confusing inference profiles (availability), prompt routers (cost-quality), and Provisioned Throughput (capacity). Three mechanisms, three different exam answers (master trap 5).

:::

:::pq {#q-d1-010}

*D1 · MEDIUM · ONE ANSWER* — q-d1-010 · 1.2 Provisioned Throughput

**Q10.** A production application has steady, predictable traffic of 5 million tokens per day and a strict latency SLA. During testing, on-demand throttling caused timeouts. What is the most appropriate capacity choice?

- A. Provisioned Throughput for the steady baseline, keeping on-demand for unexpected peaks <!-- correct -->
- B. On-demand only, with retries on throttle errors
  > Retries do not create capacity; under sustained load they add latency and still fail the SLA.
- C. Batch inference for all traffic
  > Batch inference is hours-scale and non-interactive, so it cannot serve a real-time application at all.
- D. A larger context window model on-demand
  > A larger context window does nothing for throttling or latency; it is a capability feature, not a capacity mechanism.

**Why A is correct:** Provisioned Throughput reserves model units with an hourly commit, which removes throttling risk for the predictable baseline and protects latency. The hybrid pattern (PT for baseline, on-demand for peaks) is the exam's most-correct answer for steady-plus-spiky traffic.

**The trap AWS set here:** treating Provisioned Throughput as a pure cost saver. It is a latency and throughput guarantee for predictable load.

:::

:::pq {#q-d1-011}

*D1 · HARD · ONE ANSWER* — q-d1-011 · 1.2 Cross-region details

**Q11.** A platform team adopts cross-region inference profiles for a latency-sensitive assistant. Finance wants to know where quota is consumed, and security wants to know how prompt data is handled when a request is routed to a second region. Which statement is fully correct?

- A. Invoke the inference profile ID; quotas are consumed in the source region; routed requests stay encrypted on the AWS backbone and are not stored in the destination region <!-- correct -->
- B. Invoke the bare model ID and quotas are pooled across all destination regions
  > You must invoke the profile ID, and quotas are managed at the source region, not pooled across destinations.
- C. Prompt data is persisted in each destination region for audit purposes
  > Cross-region inference does not persist your prompts in destination regions; this invents a data-residency violation.
- D. Cross-region inference requires Provisioned Throughput in every destination region
  > Profiles work with on-demand routing; provisioned capacity is a separate, optional mechanism.

**Why A is correct:** With cross-region inference you invoke the inference profile ID (for example us.anthropic.claude-...), quotas are consumed in the source region where the profile lives, and routed traffic stays encrypted on the AWS backbone in transit. Any option that claims quotas are per-destination-region, that data is stored in the failover region, or that you invoke the bare model ID is wrong on at least one fact.

**The trap AWS set here:** Bundled-fact options. Each distractor is wrong on exactly one fact (invocation target, quota location, data handling), so you must verify every clause.

:::

:::pq {#q-d1-012}

*D1 · MEDIUM · SELECT 2* — q-d1-012 · 1.2 Fine-tuning

**Q12.** A team needs a small model that reliably classifies support tickets into 40 categories. They have 20,000 labeled tickets in S3. Which TWO statements about the fine-tuning approach are true? (Select TWO)

- A. LoRA (parameter-efficient fine-tuning) trains only small weight deltas, keeping the job cheap <!-- correct -->
- B. The labeled tickets in S3 provide the supervised training data the job needs <!-- correct -->
- C. Fine-tuning requires retraining the full model from scratch
  > Full retraining from scratch is never the answer on this exam; that is the out-of-scope option.
- D. Fine-tuning works with zero labeled examples
  > Zero examples means no supervised signal; few-shot prompting is the zero-data tool, not fine-tuning.
- E. RAG alone will bake the classification behavior into the weights
  > RAG retrieves knowledge at query time; it never changes weights, so it cannot bake in behavior.

**Why A, B is correct:** LoRA is the exam's parameter-efficient answer: only adapter weights change, so the job is fast and cheap. And supervised fine-tuning genuinely needs labeled examples, which the 20,000 tickets in S3 supply.

**The trap AWS set here:** RAG as a behavior changer. RAG adds knowledge, fine-tuning changes behavior (master trap 7).

:::

:::pq {#q-d1-013}

*D1 · MEDIUM · SELECT 2* — q-d1-013 · 1.2 Model lifecycle

**Q13.** A team serves a fine-tuned model from SageMaker and needs safe updates with rollback. Which TWO practices should they adopt? (Select TWO)

- A. Version every model in the SageMaker Model Registry <!-- correct -->
- B. Deploy through an automated pipeline that can roll back to the previous version <!-- correct -->
- C. Overwrite the production endpoint in place with each new model
  > In-place overwrites destroy the rollback target; there is nothing to return to when the new model misbehaves.
- D. Delete old model versions immediately after deployment
  > Deleting old versions has the same effect: no artifact, no rollback.
- E. Skip staging and deploy directly to production for speed
  > Skipping staging trades a few minutes for unvalidated production risk, the opposite of a safe lifecycle.

**Why A, B is correct:** The registry gives immutable versioned artifacts, and a pipeline with rollback makes a bad deployment reversible in minutes. Together they are the exam's safe-lifecycle answer.

**The trap AWS set here:** in-place updates that silently destroy the ability to roll back.

:::

:::pq {#q-d1-014}

*D1 · HARD · ONE ANSWER* — q-d1-014 · 1.2 Graceful degradation

**Q14.** During a peak sale, the flagship model becomes unavailable for 20 minutes. The product requirement is that the assistant must keep answering, even at reduced quality, rather than fail. Which design meets the requirement?

- A. A Step Functions circuit breaker that detects repeated failures and fails over to a smaller cheaper model or a cached response <!-- correct -->
- B. Retry the flagship model indefinitely until it recovers
  > Infinite retries turn a 20-minute outage into 20 minutes of timeouts for every user, plus retry storms when the model recovers.
- C. Return an error page asking users to try again later
  > An error page is the literal failure the requirement forbids; it meets no part of keep answering.
- D. Queue all requests for 20 minutes and process them when the model returns
  > Queueing for 20 minutes converts an availability problem into a latency catastrophe; users will not wait.

**Why A is correct:** Graceful degradation means the system sheds quality instead of failing: the circuit breaker stops hammering the dead model and serves a smaller model or cached answers until recovery. Availability is preserved by design.

**The trap AWS set here:** retries and queues that preserve the request but sacrifice the user experience the requirement protects.

:::

:::pq {#q-d1-015}

*D1 · MEDIUM · ONE ANSWER* — q-d1-015 · 1.3 Data pipelines

**Q15.** A pipeline must ingest 10,000 mixed files per day (PDF, PowerPoint, Word, video), extract key concepts into structured summaries, and land them in a knowledge base. The team has two engineers and wants the least operational overhead. Which service is the purpose-built anchor for the extraction step?

- A. Bedrock Data Automation for managed multimodal extraction into structured summaries <!-- correct -->
- B. Bedrock Guardrails to pull the key concepts out of the files
  > Guardrails are safety filters; they screen content, they do not extract or summarize it.
- C. Point a Bedrock Knowledge Base directly at the raw files and let retrieval handle it
  > Knowledge Bases do retrieval over ingested content; they are not a document-understanding and extraction pipeline.
- D. Amazon Textract alone for all file types including video
  > Textract handles documents, not video or audio; the mixed modalities need the multimodal service.

**Why A is correct:** Bedrock Data Automation is purpose-built for exactly this: multimodal extraction (documents, images, video, audio) into structured output via standard output or custom blueprints, as a managed async service. It replaces a hand-rolled chain of Textract plus Transcribe plus custom parsing code, which is precisely the operational overhead the scenario rules out.

**The trap AWS set here:** Guardrails as an extractor and Knowledge Bases as a processor. The exam repeatedly offers safety and retrieval services for an extraction job.

:::

:::pq {#q-d1-016}

*D1 · MEDIUM · ONE ANSWER* — q-d1-016 · 1.3 Data quality

**Q16.** A data engineering team runs a daily ingestion pipeline into a knowledge base. Twice this quarter, malformed records (truncated PDFs, mis-encoded text) reached the knowledge base and corrupted answers for a day before anyone noticed. They need automated monitoring that flags bad records against defined quality rules before they reach the knowledge base, with alerts the on-call engineer can act on. Which approach fits with the least custom code?

- A. Add Glue Data Quality rules on the pipeline with CloudWatch alarms that page on-call when records fail validation <!-- correct -->
- B. Write a custom Lambda function that inspects every record with hand-coded checks
  > This rebuilds a rules engine by hand; it is the operational-overhead answer the scenario rules out.
- C. Put a Bedrock Guardrail in front of the knowledge base to catch malformed records
  > Guardrails screen model inputs and outputs for safety; they are not a data-quality rules engine for pipelines.
- D. Monitor pipeline CloudWatch metrics for byte counts and infer quality from volume
  > Volume metrics cannot detect a truncated PDF or mis-encoded text; this measures throughput, not quality.

**Why A is correct:** Glue Data Quality provides managed, rule-based data-quality monitoring (completeness, validity, format rules) over pipeline data with CloudWatch alerting, which is exactly "flag malformed records against rules before they land." Custom Lambda validators or raw CloudWatch metrics would require the team to build the rules engine themselves, violating the least-custom-code constraint.

**The trap AWS set here:** Metrics versus rules. CloudWatch tells you the pipeline ran; only a quality-rules engine tells you the data was good.

:::

:::pq {#q-d1-017}

*D1 · MEDIUM · ONE ANSWER* — q-d1-017 · 1.3 Wrong-tool trap

**Q17.** A developer proposes using Bedrock Guardrails to pull invoice totals and dates out of scanned PDFs. What is wrong with this proposal?

- A. Guardrails are safety filters; extraction needs Bedrock Data Automation or a parser, not a filter <!-- correct -->
- B. Guardrails cannot process PDF files at all
  > The file-format detail is secondary; even with perfect text input, Guardrails still could not extract fields.
- C. Guardrails only work with Anthropic models
  > Guardrails work across providers, including via the standalone ApplyGuardrail API, so the model claim is false and beside the point.
- D. Nothing is wrong; this is a valid use of Guardrails
  > Accepting the proposal ships a design where the extraction step silently does nothing.

**Why A is correct:** The core error is architectural: Guardrails evaluate content against safety policies (block, mask, filter). They have no extraction capability. Invoice field extraction belongs to Bedrock Data Automation or a document parser.

**The trap AWS set here:** The trap AWS set here is the proposal itself: Guardrails for extraction is a named exam trap. Name the tool's actual job and reject it.

:::

:::pq {#q-d1-018}

*D1 · MEDIUM · ONE ANSWER* — q-d1-018 · 1.3 Kendra vs Knowledge Bases

**Q18.** Employees want to search the company intranet and read the source documents themselves. No text generation is needed, but queries use internal jargon that must match semantically, not just by keyword. The search index must stay current as documents change, with minimal operational overhead. Which service fits, and why not the alternative?

- A. Amazon Kendra for semantic enterprise search with source links; a Knowledge Base would add unneeded generation cost and complexity <!-- correct -->
- B. A Bedrock Knowledge Base with RetrieveAndGenerate for the most modern architecture
  > RetrieveAndGenerate generates answers the scenario explicitly does not need; it adds latency, cost, and hallucination surface for zero benefit.
- C. Amazon Comprehend to extract entities from the intranet
  > Comprehend does NLP analysis, not document search and retrieval.
- D. Self-managed OpenSearch with hand-tuned analyzers
  > This rebuilds what Kendra provides managed, violating the minimal-overhead constraint.

**Why A is correct:** Amazon Kendra is the enterprise-search service: semantic search over content with source-document links and no generation step, which matches "read the source documents themselves" exactly. A Knowledge Base would add an embedding-plus-generation pipeline (and generation cost and latency) for a requirement that explicitly excludes generation.

**The trap AWS set here:** Kendra versus Knowledge Bases. The exam tests whether the scenario needs search (Kendra) or retrieval-plus-generation (Knowledge Bases); "no text generation" is the deciding phrase.

:::

:::pq {#q-d1-019}

*D1 · MEDIUM · ONE ANSWER* — q-d1-019 · 1.3 Audio input

**Q19.** A pipeline must convert thousands of customer call recordings into text before a foundation model analyzes them for sentiment and topics. Compliance requires two things: speaker diarization (who said what) and PII redaction before any transcript reaches the model. Which pipeline meets all three needs with managed services?

- A. Amazon Transcribe with speaker diarization, then Comprehend PII detection and redaction, then Bedrock analysis <!-- correct -->
- B. Amazon Transcribe straight into Bedrock with a prompt telling the model to ignore PII
  > Prompt instructions are not access control; PII still reaches the model and the compliance requirement is violated.
- C. Amazon Comprehend to transcribe the audio directly
  > Comprehend analyzes text; it does not transcribe audio.
- D. Feed the raw audio to a multimodal model and ask it to diarize and redact
  > This puts unredacted PII-bearing audio in front of the model with no diarization guarantee and no auditable redaction step.

**Why A is correct:** Amazon Transcribe provides managed speech-to-text with speaker diarization, and Comprehend provides managed PII entity detection for redaction; chaining Transcribe then Comprehend redaction then Bedrock satisfies transcription, diarization, and the compliance gate with no custom ML. Skipping the redaction step or using a tool that cannot do it violates the compliance requirement.

**The trap AWS set here:** Prompt instructions as a compliance control. The exam treats "tell the model to ignore PII" as no control at all.

:::

:::pq {#q-d1-020}

*D1 · EASY · SELECT 2* — q-d1-020 · 1.3 Input formatting

**Q20.** A chat application must call Claude, Llama, and Titan with the same code and return strictly valid JSON. Which TWO choices support this? (Select TWO)

- A. Use the Converse API's unified messages format across providers <!-- correct -->
- B. Define a JSON schema and request structured output via the Converse outputConfig <!-- correct -->
- C. Hand-write a different request body per provider in application code
  > Per-provider bodies are exactly the maintenance burden Converse exists to remove.
- D. Ask the model politely in prose and hope the output parses
  > Prose instructions produce prose-shaped output; without a schema, parsing fails intermittently.
- E. Use InvokeModel with one shared body for all providers
  > One shared InvokeModel body cannot work because each provider defines its own body format; that is the documented ValidationException trap.

**Why A, B is correct:** Converse normalizes messages, system prompts, and tool config across providers so one code path serves all three models, and outputConfig with a JSON schema constrains generation to valid JSON instead of hoping.

**The trap AWS set here:** one InvokeModel body for every provider. Provider bodies differ; Converse unifies.

:::

:::pq {#q-d1-021}

*D1 · MEDIUM · ONE ANSWER* — q-d1-021 · 1.4 Vector stores

**Q21.** A team wants managed RAG over documents in S3 plus a Confluence space and a Salesforce knowledge base. Requirements: ingestion, embeddings, vector storage, hybrid search, and retrieval in one managed service, with the least operational overhead. The team will not operate vector database clusters. What should they use?

- A. Bedrock Knowledge Bases with its managed ingestion, embeddings, vector store, and hybrid search <!-- correct -->
- B. Self-managed OpenSearch plus a SageMaker endpoint hosting an embedding model
  > Correct architecture, wrong operations: the team explicitly will not operate clusters or model endpoints.
- C. Amazon Kendra with a generation step added in Lambda
  > Kendra is enterprise search, not a RAG vector pipeline; bolting generation onto it rebuilds what Knowledge Bases provides.
- D. Aurora PostgreSQL with pgvector and a hand-built sync pipeline
  > pgvector is a fine store, but the hand-built ingestion, embedding, and sync pipeline violates the least-overhead constraint.

**Why A is correct:** Bedrock Knowledge Bases is the single managed service that covers all of this: multiple data-source connectors (S3, Confluence, Salesforce), managed ingestion and Titan/Cohere embeddings, a managed vector store, hybrid search, and Retrieve/RetrieveAndGenerate APIs. Every alternative requires the team to operate at least one piece (vector cluster, embedding pipeline, or sync jobs) that the scenario rules out.

**The trap AWS set here:** Right architecture, wrong operations. Distractors describe workable systems that the scenario's "no operated infrastructure" constraint kills.

:::

:::pq {#q-d1-022}

*D1 · MEDIUM · SELECT 2* — q-d1-022 · 1.4 Multi-tenant isolation

**Q22.** A hotel platform serves 200 hotels. Each hotel's documents must be invisible to the other hotels, enforced by access control, not by instructions. Which TWO design choices enforce this? (Select TWO)

- A. One knowledge base per hotel (or per account) holding only that hotel's documents <!-- correct -->
- B. IAM policies that scope each hotel's application role to its own knowledge base <!-- correct -->
- C. One shared knowledge base with a system prompt telling the model to answer only about the caller's hotel
  > A prompt instruction is not access control; the model can be jailbroken or simply mistaken, and the exam explicitly rejects this pattern (master trap 6).
- D. A single IAM role shared by all hotels for simplicity
  > One shared role erases the tenant boundary at the identity layer.
- E. Storing all hotel documents in one prefix and relying on file naming
  > File naming conventions are not a security boundary and are invisible to the retrieval layer.

**Why A, B is correct:** Isolation must be structural: separate knowledge bases per tenant plus IAM scoping each role to its own base. Access control is enforced by the platform, not requested of the model.

**The trap AWS set here:** one shared knowledge base plus prompt instructions instead of IAM-enforced isolation (master trap 6).

:::

:::pq {#q-d1-023}

*D1 · EASY · ONE ANSWER* — q-d1-023 · 1.4 Durable vectors

**Q23.** A developer proposes storing the knowledge base embeddings in ElastiCache so retrieval is fast. What is wrong with this plan?

- A. ElastiCache is an ephemeral cache, not a durable vector store; use OpenSearch Serverless, Aurora with pgvector, or S3 Vectors <!-- correct -->
- B. ElastiCache cannot store vectors at all
  > ElastiCache can technically hold vector-shaped data; the problem is durability and indexing, not possibility.
- C. ElastiCache is too slow for retrieval
  > Speed is ElastiCache's strength; durability is its weakness, which is the actual objection.
- D. Nothing is wrong; this is best practice
  > Accepting the plan risks silent data loss on the first failover.

**Why A is correct:** ElastiCache is in-memory and ephemeral: a failover or eviction can lose the embeddings, and it is not a managed vector index. Durable vector storage belongs in OpenSearch Serverless, Aurora pgvector, or S3 Vectors, with ElastiCache optionally in front as a cache.

**The trap AWS set here:** ElastiCache as the durable vector store. Cache is not storage (master trap 9).

:::

:::pq {#q-d1-024}

*D1 · MEDIUM · ONE ANSWER* — q-d1-024 · 1.4 Aurora pgvector

**Q24.** An application already runs on Aurora PostgreSQL and now needs vector similarity search over product descriptions joined with relational inventory data. What is the most operationally efficient choice?

- A. Enable pgvector on Aurora PostgreSQL and store embeddings alongside the relational tables <!-- correct -->
- B. Build a separate OpenSearch cluster and sync inventory nightly
  > A separate cluster plus nightly sync adds infrastructure and staleness for a workload the existing database can serve.
- C. Store embeddings in DynamoDB
  > DynamoDB is not a vector store; it holds metadata and session state, not embeddings (master trap 9).
- D. Export descriptions to S3 and scan them at query time
  > Scanning S3 at query time is orders of magnitude too slow for interactive retrieval.

**Why A is correct:** pgvector brings vector search into the database the team already operates, so similarity queries can join directly against inventory rows with no new cluster, no sync pipeline, and no extra service to learn.

**The trap AWS set here:** DynamoDB as the vector store, and a second cluster when the current database already does the job.

:::

:::pq {#q-d1-025}

*D1 · MEDIUM · ONE ANSWER* — q-d1-025 · 1.4 Freshness

**Q25.** Company policy documents update every quarter, with occasional urgent amendments in between. The RAG assistant must answer from the current version without manual intervention, and urgent amendments must be searchable within an hour of publishing. What should the developer configure?

- A. A scheduled sync for the quarterly updates plus S3-event-driven ingestion jobs for urgent amendments <!-- correct -->
- B. A quarterly sync schedule only
  > This misses the one-hour SLA for urgent amendments published between quarters.
- C. One-time ingestion with a manual re-ingest each quarter
  > Manual re-ingestion violates the no-manual-intervention requirement and cannot meet the amendment SLA.
- D. Recreate the knowledge base from scratch every quarter
  > Recreation is heavy, disrupts the serving endpoint, and still does nothing for between-quarter amendments.

**Why A is correct:** Knowledge Base data sources support sync schedules for the predictable quarterly cadence plus event-driven ingestion (S3 event triggering StartIngestionJob) for urgent amendments, which together give current-version answers with no manual steps and meet the one-hour amendment SLA. A quarterly-only schedule would miss the amendment SLA; manual re-ingestion violates the no-manual-intervention requirement.

**The trap AWS set here:** Cadence versus SLA. The quarterly rhythm tempts a schedule-only answer, but the one-hour amendment requirement kills it.

:::

:::pq {#q-d1-026}

*D1 · MEDIUM · ONE ANSWER* — q-d1-026 · 1.4 Citations

**Q26.** A compliance team requires every generated answer to name the source documents it was drawn from, so auditors can verify each claim. The team also wants an automated check that answers stay faithful to those sources before launch. Which combination meets both needs?

- A. RetrieveAndGenerate for answers with source citations, plus a contextual-grounding evaluation measuring faithfulness to the retrieved sources <!-- correct -->
- B. Retrieve plus a prompt instructing the model to list its sources
  > Without grounded citation support, the model can hallucinate convincing but fake source references.
- C. A Bedrock Guardrail with a high grounding threshold as the only mechanism
  > Guardrails screen for safety and grounding at inference time; they do not produce auditable source citations per answer.
- D. Log all prompts to S3 and reconstruct sources manually during audits
  > Manual reconstruction is not per-answer citation and fails the automated, always-on requirement.

**Why A is correct:** RetrieveAndGenerate returns generated answers with source citations (attribution) directly, satisfying the audit requirement with no custom stitching. Pairing it with a contextual-grounding evaluation (faithfulness scoring against the retrieved sources) gives the pre-launch automated check. Prompting the model to "cite sources" without retrieval grounding produces plausible-looking but unverifiable citations.

**The trap AWS set here:** Prompted citations versus grounded citations. The exam distinguishes citations the retrieval layer produces from citations the model invents.

:::

:::pq {#q-d1-027}

*D1 · MEDIUM · ONE ANSWER* — q-d1-027 · 1.4 GraphRAG

**Q27.** A team wants RAG over a product catalog where the valuable signal is relationships: which accessories fit which models, what replaces what, compatibility constraints. Keyword and vector similarity over descriptions miss these connections. Which store fits, and what does it add over a pure vector store?

- A. Neptune for GraphRAG, adding explicit relationship traversal that pure vector similarity cannot recover <!-- correct -->
- B. A pure vector store with larger embedding dimensions
  > Bigger vectors improve text similarity; they do not encode multi-hop compatibility relationships.
- C. A relational database with recursive SQL for every query
  > Workable in theory, but hand-rolled graph traversal per query is operational overhead versus a managed graph store.
- D. ElastiCache holding the product graph for fast lookups
  > ElastiCache is an ephemeral cache, not a durable graph store with traversal query support.

**Why A is correct:** Neptune supports GraphRAG: traversal of explicit relationships (fits-with, replaces, compatible-with) that similarity search cannot recover from text alone. A pure vector store ranks by embedding closeness, which misses multi-hop compatibility facts that a graph traverses directly. The exam tests knowing that relationship-heavy retrieval is a graph problem, not a similarity problem.

**The trap AWS set here:** Similarity versus structure. When the scenario emphasizes relationships and traversal, the vector store is the wrong tool no matter how it is tuned.

:::

:::pq {#q-d1-028}

*D1 · EASY · ONE ANSWER* — q-d1-028 · 1.4 Filtered retrieval

**Q28.** A support assistant must only retrieve articles for the caller's region (EU articles for EU callers). How should the developer implement this?

- A. Tag documents with region metadata at ingestion and apply metadata filters at retrieval time <!-- correct -->
- B. Ask the model in the prompt to prefer the caller's region
  > Prompt preferences are not enforcement; the model can still cite the wrong region's article.
- C. Create one giant prompt containing all regions
  > One giant prompt wastes context on irrelevant regions on every call.
- D. Fine-tune a separate model per region
  > A model per region multiplies training and serving cost for a problem metadata solves.

**Why A is correct:** S3 object metadata and custom attributes enable filtered retrieval: the query carries a region filter, and the vector store only searches matching documents. Filtering is enforced by the retrieval layer, not requested of the model.

**The trap AWS set here:** prompt instructions as access filtering instead of metadata filters enforced at retrieval.

:::

:::pq {#q-d1-029}

*D1 · HARD · ONE ANSWER* — q-d1-029 · 1.4 Enterprise scenario

**Q29.** A hotel chain runs a legacy Java property system. Requirements: each hotel's data isolated with its own access controls, near-real-time room availability in answers, and minimal custom integration code. Which design is most correct?

- A. One knowledge base per hotel with IAM-scoped access, direct ingestion of availability data for freshness, and IAM Identity Center permission sets for the legacy system integration <!-- correct -->
- B. One shared knowledge base for all hotels with a prompt instructing the model to respect hotel boundaries
  > The shared base with prompt instructions fails isolation (master trap 6): prompts are not access control.
- C. Nightly CSV exports from the Java system loaded into a single knowledge base
  > Nightly exports make availability data up to 24 hours stale, violating near-real-time.
- D. A separate fine-tuned model per hotel
  > A model per hotel is 200 training and serving bills for an isolation problem IAM solves.

**Why A is correct:** Per-hotel knowledge bases with IAM scoping give real isolation; direct ingestion keeps availability near-real-time instead of nightly-stale; Identity Center permission sets integrate the legacy Java system with proper RBAC. Every requirement maps to a mechanism.

**The trap AWS set here:** the shared-KB-plus-prompt option, which looks efficient but violates the isolation requirement structurally.

:::

:::pq {#q-d1-030}

*D1 · HARD · SELECT 2* — q-d1-030 · 1.4 Retrieval debugging

**Q30.** A RAG application returns confident but wrong answers. The retrieved chunks look relevant at a glance. Which TWO should the developer investigate first? (Select TWO)

- A. Whether the chunking strategy splits key context across chunk boundaries <!-- correct -->
- B. Whether the embeddings capture relevance rather than mere semantic similarity <!-- correct -->
- C. Switching to a larger generation model
  > A larger generation model cannot fix broken retrieval; it will just state the wrong answer more fluently.
- D. Raising the temperature
  > Temperature controls randomness, not factuality against sources.
- E. Adding more system prompt examples
  > More prompt examples do not repair chunks that lost their context at ingestion.

**Why A, B is correct:** When chunks look relevant but answers are wrong, the failure is in retrieval, not generation: split context destroys meaning across boundaries, and similarity is not relevance. Both are fixed on the retrieval side (chunking, hybrid search, rerank).

**The trap AWS set here:** debugging a retrieval failure by changing the generation model or temperature.

:::

:::pq {#q-d1-031}

*D1 · MEDIUM · ONE ANSWER* — q-d1-031 · 1.5 Chunking

**Q31.** A RAG system ingests legal contracts where tables and clauses must stay intact. Fixed-size chunking keeps splitting tables across chunks, breaking answers. Which chunking strategy should the developer choose?

- A. Hierarchical chunking, so small child chunks match precisely while parent chunks preserve full context <!-- correct -->
- B. Larger fixed-size chunks with no overlap
  > Larger fixed chunks still split tables, just at different boundaries; size does not respect structure.
- C. No chunking at all
  > No chunking on long contracts blows past context limits and retrieval precision.
- D. Random chunk boundaries
  > Random boundaries are never a strategy; they guarantee split context.

**Why A is correct:** Hierarchical chunking indexes small child chunks for precise matching but returns the parent chunk for context, so tables and clauses survive intact while retrieval stays precise. It is the exam's preferred answer for structured documents.

**The trap AWS set here:** fixed-size chunking for structured documents. Structure needs hierarchical (or semantic), not fixed.

:::

:::pq {#q-d1-032}

*D1 · MEDIUM · ONE ANSWER* — q-d1-032 · 1.5 Chunking cost

**Q32.** A FAQ bot answers from 500 short question-answer pairs, each under 100 tokens. Retrieval precision is poor: answers sometimes come from the wrong pair. The team is considering hierarchical chunking to fix it. What is the most appropriate chunking choice, and why is hierarchical wrong here?

- A. Keep one chunk per Q-A pair (small fixed size or pre-chunked); hierarchical chunking adds cost with no benefit on short pairs <!-- correct -->
- B. Switch to hierarchical chunking with large parent chunks
  > Hierarchical chunking solves cross-section context loss in long documents, not precision over 100-token pairs; it adds ingestion cost for nothing.
- C. Use semantic chunking for the highest quality splits
  > Semantic chunking is the most expensive ingestion option and these pairs are already natural semantic units.
- D. Merge all pairs into large 2,000-token chunks to give the model more context
  > Large chunks dilute precision: the retriever returns haystacks instead of the one relevant pair.

**Why A is correct:** With pre-chunked short Q-A pairs, one chunk per pair (fixed small size or pre-chunked input) keeps each answer's text intact and maximizes precision; hierarchical chunking is designed for long structured documents where child chunks need parent context, and it adds ingestion cost and complexity for zero benefit on 100-token pairs. The precision problem here is more likely an embedding or ranking issue than a chunking one.

**The trap AWS set here:** Bigger machinery for a small problem. The exam offers the most sophisticated chunking strategy where the simplest one is correct.

:::

:::pq {#q-d1-033}

*D1 · MEDIUM · SELECT 2* — q-d1-033 · 1.5 Relevance

**Q33.** Users complain that retrieved passages match keywords but do not actually answer the question. Which TWO changes most directly fix retrieved-but-not-relevant results? (Select TWO)

- A. Enable hybrid search combining vector and keyword ranking <!-- correct -->
- B. Add a rerank model to reorder candidates by true relevance <!-- correct -->
- C. Switch to a larger generation model
  > The generation model is downstream of retrieval; a bigger model still answers from the same irrelevant chunks.
- D. Increase the chunk size to 2,000 tokens
  > Larger chunks dilute precision further and do not fix ranking.
- E. Lower the temperature to zero
  > Temperature affects output randomness, not which chunks were retrieved.

**Why A, B is correct:** Hybrid search blends semantic and keyword signals so keyword-heavy queries stop drifting, and reranking scores the candidate set for actual relevance before generation. Both attack the relevance gap directly.

**The trap AWS set here:** fixing a retrieval ranking problem at the generation layer.

:::

:::pq {#q-d1-034}

*D1 · MEDIUM · ONE ANSWER* — q-d1-034 · 1.5 Embeddings

**Q34.** A knowledge base covers support documents in 12 languages and needs strong multilingual retrieval: a Spanish query must find the Portuguese article that answers it. The team defaults to Titan Text Embeddings v2. What should they choose instead, and which setting matters most?

- A. Cohere Embed multilingual with input_type set appropriately for queries versus documents <!-- correct -->
- B. Titan Text Embeddings v2 because it is the default
  > The default is fine for English-centric content, but the scenario explicitly demands cross-language retrieval quality.
- C. One embedding model per language with per-language indexes
  > Twelve parallel pipelines is operational overhead; a single multilingual model handles cross-language matching natively.
- D. Skip embeddings and use keyword search with translated queries
  > Translation plus keyword search loses semantic matching and adds a translation step to every query.

**Why A is correct:** Cohere Embed is the multilingual-optimized embedding option, and its input_type setting (query versus document) matters because asymmetric retrieval needs different encodings for short queries and long documents. Titan v2 is a strong general default but the scenario's explicit cross-language requirement points to the multilingual-tuned model.

**The trap AWS set here:** Default-model bias. The exam names the scenario constraint (12 languages) that the default choice does not optimize for.

:::

:::pq {#q-d1-035}

*D1 · MEDIUM · ONE ANSWER* — q-d1-035 · 1.5 Query handling

**Q35.** User queries are short and vague (for example, just refund), but the knowledge base articles use formal policy language. Retrieval quality is poor. What should the developer add?

- A. Query expansion in a Lambda function that rewrites the vague query into richer search terms before retrieval <!-- correct -->
- B. A larger generation model
  > The generation model never sees better chunks, so it cannot compensate for failed retrieval.
- C. More training data for the embedding model
  > Retraining embeddings is heavyweight and unnecessary when the gap is query phrasing.
- D. A longer system prompt
  > A longer system prompt does not change what the retriever returns.

**Why A is correct:** Query expansion bridges the vocabulary gap: the Lambda step turns refund into several formal phrasings the articles actually use, so retrieval finds the right passages. This is the standard query-handling fix.

**The trap AWS set here:** prompt or model changes for what is fundamentally a query-to-corpus vocabulary mismatch.

:::

:::pq {#q-d1-036}

*D1 · HARD · SELECT 2* — q-d1-036 · 1.5 Chunking immutability

**Q36.** A team changed the chunking strategy on their knowledge base data source from fixed-size to semantic, re-ran the sync, but retrieval behavior did not change. Which TWO steps actually apply the new strategy? (Select TWO)

- A. Recreate the data source with the new chunking configuration, because chunking is set at creation time <!-- correct -->
- B. Run a fresh ingestion sync after recreating the data source <!-- correct -->
- C. Re-run the same sync without recreating anything
  > Re-running sync on the old data source re-ingests with the old chunking; nothing changes.
- D. Change the generation model to one that prefers semantic chunks
  > The generation model has no influence on how documents were chunked at ingestion.
- E. Edit the stored chunks directly in the vector store
  > Hand-editing stored chunks bypasses the managed pipeline and breaks future syncs.

**Why A, B is correct:** Chunking strategy is fixed when the data source is created, so the only path is recreating the data source with the new setting and then syncing to re-ingest and re-chunk everything.

**The trap AWS set here:** assuming a sync picks up a configuration that is actually immutable after creation.

:::

:::pq {#q-d1-037}

*D1 · HARD · ONE ANSWER* — q-d1-037 · 1.5 Debug chain

**Q37.** A RAG assistant over 500-page technical manuals gives confident but wrong answers, especially on specification tables. Retrieved chunks look relevant, but values cited in answers do not match the source tables. What should the developer do FIRST?

- A. Inspect whether tables are being split across chunks, then move to hierarchical chunking with advanced parsing so tables stay intact <!-- correct -->
- B. Switch the generation model to the largest available flagship model
  > A larger model reasons better but still reads the same broken chunks; retrieval is the failure point.
- C. Raise the temperature to get more creative table interpretations
  > Higher temperature increases hallucination risk on factual tables, the opposite of the fix.
- D. Double the number of retrieved chunks
  > More broken chunks just give the model more broken context to choose from.

**Why A is correct:** The symptom pattern (relevant-looking chunks, wrong table values) points to tables split at chunk boundaries: each chunk looks fine alone but the values lose their row context. Verifying the split and switching to hierarchical chunking with advanced parsing fixes the root cause at ingestion.

**The trap AWS set here:** answering a table-integrity problem with model or retrieval-count changes instead of fixing chunk boundaries.

:::

:::pq {#q-d1-038}

*D1 · MEDIUM · ONE ANSWER* — q-d1-038 · 1.5 Dimensions

**Q38.** A team debates embedding dimensions for Titan Text Embeddings v2: 1024 versus 256. Their corpus is 50 million documents, storage cost is a real concern, but retrieval quality cannot regress on the golden test set. Which statement is correct?

- A. Benchmark both on the golden test set and choose the smallest dimension that preserves quality; 1024 costs more storage, 256 risks nuance loss <!-- correct -->
- B. Always use 1024 because more dimensions are strictly better
  > More dimensions cost more storage and compute; "strictly better" ignores the stated cost constraint.
- C. Always use 256 because storage cost dominates
  > If 256 regresses quality on the golden set, the cost saving violates the no-regression constraint.
- D. Dimensions do not affect retrieval quality
  > Dimensionality directly affects representational capacity and therefore retrieval quality.

**Why A is correct:** 1024 dimensions capture more nuance at higher storage and compute cost; 256 is cheaper and faster with slightly lower quality. The correct engineering answer is to measure both against the golden test set and pick the smallest dimension that holds quality, not to declare one universally better. The exam punishes absolutist answers on trade-off questions.

**The trap AWS set here:** Absolutism on a trade-off. Any option with "always" is wrong when the scenario gives competing constraints.

:::

:::pq {#q-d1-039}

*D1 · MEDIUM · ONE ANSWER* — q-d1-039 · 1.5 MCP

**Q39.** An agent needs a standardized way to discover and call retrieval tools and data sources without custom integration code per tool. Which interface should the developer adopt?

- A. MCP (Model Context Protocol) clients for standardized tool and retrieval access <!-- correct -->
- B. A custom REST client per tool
  > Custom clients per tool multiply integration work with every new source.
- C. Direct database credentials embedded in the agent prompt
  > Credentials in prompts leak secrets into logs and model context.
- D. Screen-scraping the tool's web UI
  > Screen-scraping is brittle and has no place in a production agent.

**Why A is correct:** MCP standardizes how agents discover and invoke tools: one protocol, many tools, no per-tool custom clients. The blueprint names MCP clients as the standardized retrieval access for agents.

**The trap AWS set here:** custom per-tool integration when the exam names a standard protocol.

:::

:::pq {#q-d1-040}

*D1 · MEDIUM · ONE ANSWER* — q-d1-040 · 1.6 Prompt Management

**Q40.** Marketing changes the assistant's tone guidelines every few weeks. Every change currently requires an engineer to edit code and redeploy. New requirements: non-engineers must update prompts without a deploy, marketing wants to A/B test two tone variants, and compliance wants an immutable record of exactly which prompt version served each release. Which approach satisfies all three?

- A. Bedrock Prompt Management with versions for the audit trail and variants for the A/B test, edited without code deploys <!-- correct -->
- B. Keep prompts in application code and add a faster CI/CD pipeline
  > A faster pipeline is still an engineer-driven deploy for every wording tweak; it fails the no-deploy requirement.
- C. Store prompt text in S3 and have marketing edit the files directly
  > Editable, but with no variants for A/B testing and no immutable versioning for the audit trail.
- D. Move the tone guidelines into a Bedrock Agent instruction
  > Agents are for dynamic tool-using reasoning, not for versioned static prompt governance.

**Why A is correct:** Bedrock Prompt Management makes prompts managed resources: {{variable}} templates editable without code deploys, variants for A/B testing, and immutable versions giving the audit trail of what served when. Hardcoded prompts fail all three; S3 text files give editing without versioning or variants.

**The trap AWS set here:** Variants versus versions. The exam tests the distinction: variants compare candidates, versions freeze what shipped.

:::

:::pq {#q-d1-041}

*D1 · MEDIUM · SELECT 2* — q-d1-041 · 1.6 Variants vs versions

**Q41.** A team wants to A/B test two prompt wordings, then lock the winner as the release everyone uses. Which TWO statements about Prompt Management are true? (Select TWO)

- A. Variants allow comparing prompt wordings side by side for A/B testing <!-- correct -->
- B. Versions are immutable snapshots, so the winning wording becomes a locked release <!-- correct -->
- C. Variants are immutable releases
  > Variants are the comparison mechanism, not the release mechanism.
- D. Versions are for A/B comparison
  > Versions are the release mechanism, not the comparison mechanism. The exam swaps these two deliberately.
- E. Drafts cannot be tested before versioning
  > Drafts can be tested in the console before saving a version; that is the normal workflow.

**Why A, B is correct:** Variants exist for comparison (A/B testing wordings), and versions are immutable snapshots: draft, test, then save the winner as a version that cannot silently change under you.

**The trap AWS set here:** swapping variants (A/B) with versions (immutable releases).

:::

:::pq {#q-d1-042}

*D1 · MEDIUM · ONE ANSWER* — q-d1-042 · 1.6 Flows

**Q42.** A business analyst (not an engineer) must build a fixed three-step prompt chain: summarize a ticket, classify it, then draft a reply, with conditional branching when the ticket is urgent. No code changes are allowed. Which service fits?

- A. Bedrock Prompt Flows, the visual no-code builder for multi-step prompt workflows with branching <!-- correct -->
- B. Bedrock Agents, for autonomous tool-using reasoning
  > Agents are for dynamic autonomous reasoning with tools, not fixed deterministic sequences; the exam explicitly warns against agents for fixed chains.
- C. AWS Step Functions with Lambda functions
  > Step Functions orchestrates general workflows with approvals and timeouts, but it is code-centric, not the no-code visual builder the analyst needs.
- D. Amazon EventBridge rules
  > EventBridge routes events; it does not build prompt chains.

**Why A is correct:** Prompt Flows (Flows) is the visual builder for fixed multi-step GenAI workflows: prompt, knowledge base, and Lambda nodes with conditional branching and a test panel, usable without code. Fixed deterministic prompt chains are its exact use case.

**The trap AWS set here:** Bedrock Agents for a fixed deterministic prompt chain. Agents are for dynamic tool use; Flows are for fixed sequences.

:::

:::pq {#q-d1-043}

*D1 · EASY · ONE ANSWER* — q-d1-043 · 1.6 Structured output

**Q43.** An application needs strictly valid JSON from Claude, Llama, and Titan using one code path. Which approach is most reliable?

- A. Converse API with outputConfig and a JSON schema <!-- correct -->
- B. Asking nicely in the system prompt and parsing with a try/except
  > Try/except parsing accepts intermittent failures as normal; the schema prevents them.
- C. InvokeModel with a shared body for all three providers
  > A shared InvokeModel body is invalid: each provider defines its own body format.
- D. Setting temperature to zero and hoping
  > Temperature zero reduces randomness but never guarantees valid JSON structure.

**Why A is correct:** Converse outputConfig with a JSON schema constrains generation to schema-valid JSON across providers, in one unified code path. Schema beats hope.

**The trap AWS set here:** prose instructions plus parsing instead of a real schema constraint.

:::

:::pq {#q-d1-044}

*D1 · HARD · SELECT 3* — q-d1-044 · 1.6 Prompt governance

**Q44.** A company manages 15 production prompts. Compliance requires an approval before any prompt change goes live and a full audit trail of who changed what. Which THREE controls satisfy this? (Select THREE)

- A. Prompt Management versions, so every release is an immutable snapshot <!-- correct -->
- B. An approval workflow (for example Step Functions) gating version publication <!-- correct -->
- C. CloudTrail logging of prompt management API calls for the audit trail <!-- correct -->
- D. Editing prompts directly in application code
  > Code edits bypass versioning, approval, and audit all at once.
- E. Sharing one IAM user across the marketing team
  > A shared IAM user destroys attribution; the audit trail cannot say who did what.

**Why A, B, C is correct:** Versions make each release immutable and referenceable, the approval workflow enforces the human gate before publication, and CloudTrail records every prompt API call with identity and time for the audit trail.

**The trap AWS set here:** code edits and shared credentials that silently erase governance.

:::

## Domain 2: Implementation and Integration (26% of the exam, 36 questions) {#sec-d2}

**Decision reference.** Pick the API by matching the row to the scenario's need.

| Need | Answer |
|---|---|
| Unified requests across providers, tool use, inline guardrails | **Converse / ConverseStream** |
| Provider-specific features, embeddings | **InvokeModel / InvokeModelWithResponseStream** |
| Async, hours OK, cheapest | **Batch inference** (S3 in, S3 out) |
| Reserved capacity, latency SLA | **Provisioned Throughput** (invoke the provisioned ARN) |
| Real-time token streaming | **ConverseStream** plus WebSockets or SSE to the client |

**How to read this diagram.**

:::walkthrough

1. Row 1: same code for Claude, Llama, Titan with tool use means Converse, always.
2. Row 2: embeddings or provider-exotic parameters mean InvokeModel; Converse cannot do embeddings.
3. Row 3: nobody waiting and hours acceptable means batch at roughly half price.
4. Row 4: steady baseline plus latency SLA means Provisioned Throughput, and the code must call the provisioned ARN or throttling continues.
5. Row 5: tokens appearing as generated means ConverseStream; API Gateway timeouts push long streams to WebSockets or SSE.
6. If this table breaks (wrong row), you get ValidationException from mismatched bodies or throttling from bypassed reservations.
:::

:::pq {#q-d2-001}

*D2 · MEDIUM · ONE ANSWER* — q-d2-001 · 2.1 Agent updates

**Q45.** A team runs a Bedrock Agent with dev, staging, and prod aliases. An engineer updates the agent instructions and action-group configuration, tests in the console, then points the prod alias at the new work and announces the release. Production behavior does not change, but the console test showed the new behavior. What is the most likely cause, and what is the correct release sequence?

- A. The changes are still in DRAFT; run prepare-agent to create a new version, then point the prod alias at that version <!-- correct -->
- B. Alias changes need up to an hour to propagate
  > Alias retargeting is not a propagation delay; the problem is there is no prepared version containing the changes.
- C. Redeploy the Lambda functions used by the action groups
  > The Lambda code did not change; the agent configuration was never prepared, so redeploying tools fixes nothing.
- D. Delete and recreate the prod alias
  > Recreating the alias without a prepared version leaves it pointing at the same old behavior.

**Why A is correct:** Console tests run against DRAFT, but aliases can only point to prepared versions. Configuration changes land in DRAFT and do nothing for alias traffic until prepare-agent runs, producing a new numbered version the alias can target. The correct sequence is: edit, prepare-agent, verify the new version, then move the alias. Pointing the alias at DRAFT is impossible, which is why the release silently did nothing.

**The trap AWS set here:** DRAFT versus prepared. The exam's classic agent bug: the console shows new behavior because it tests DRAFT, while alias traffic needs a prepared version.

:::

:::pq {#q-d2-002}

*D2 · MEDIUM · ONE ANSWER* — q-d2-002 · 2.1 Action groups

**Q46.** A Bedrock Agent must look up order status from an internal REST API during conversations. The API requires an OAuth bearer token that expires hourly, and its responses need field filtering before the agent sees them. How should the developer give the agent access to that API?

- A. An action group with a Lambda executor that manages the OAuth token and filters API responses before returning them <!-- correct -->
- B. An action group with only an OpenAPI schema pointing directly at the API
  > A bare schema cannot add expiring bearer tokens or filter response fields; the auth requirement kills this option.
- C. Write the API details into the agent instructions and let the model call it
  > The model cannot execute HTTP calls; instructions describe behavior, they do not create tool access.
- D. Load the order database into a knowledge base and skip the API
  > A knowledge base is for document retrieval, not live order-status lookups; the data would be stale on arrival.

**Why A is correct:** An action group with a Lambda executor is the right integration: the Lambda handles OAuth token refresh and response filtering, and the action group exposes a clean function schema to the agent. A raw OpenAPI schema alone cannot inject expiring auth headers or filter fields, so the Lambda executor is the professional choice when auth and transformation are involved.

**The trap AWS set here:** Schema-only versus Lambda executor. The exam adds an auth or transformation requirement precisely to separate the two action-group patterns.

:::

:::pq {#q-d2-003}

*D2 · MEDIUM · ONE ANSWER* — q-d2-003 · 2.1 Multi-agent

**Q47.** Three specialist Bedrock Agents (tax, investment, estate planning) must collaborate on a client plan under one supervisor agent. How should inter-agent communication be configured?

- A. Use the built-in supervisor/collaborator multi-agent mechanism, with collaborators prepared and aliased <!-- correct -->
- B. Wire the agents together with action groups defined in the supervisor's instructions
  > Action groups invoke Lambda or APIs; describing agents as action groups in instructions is the exam's named misconception.
- C. Chain them with SQS queues and Lambda functions
  > SQS plus Lambda rebuilds orchestration the platform already provides, adding latency and state bugs.
- D. Merge all three into one giant prompt
  > One giant prompt loses specialist boundaries, explodes context, and cannot use per-domain tools cleanly.

**Why A is correct:** Bedrock's multi-agent collaboration is a built-in supervisor/collaborator pattern: the supervisor delegates to collaborator agents, which must be prepared and aliased, with conversation history relay between them. Action groups are for tools, not for agent-to-agent delegation.

**The trap AWS set here:** action groups for inter-agent communication. The service uses supervisor/collaborator, not action groups.

:::

:::pq {#q-d2-004}

*D2 · MEDIUM · ONE ANSWER* — q-d2-004 · 2.1 Agent memory

**Q48.** An agent must remember customer context (plan tier, open tickets, preferences) across sessions for several weeks. Agent sessions expire after 600 seconds idle, and the data must be encrypted and queryable by customer ID in milliseconds. Where should the developer store this long-term memory?

- A. DynamoDB keyed by customer ID with server-side encryption, read on session start and written back on session end <!-- correct -->
- B. One S3 object per customer updated on every turn
  > S3 has higher per-request latency and no millisecond key lookup pattern; it is the wrong access pattern for session state.
- C. Rely on the agent built-in session memory
  > Built-in session memory is scoped to the session and expires with the 600-second idle TTL; it cannot span weeks.
- D. ElastiCache holding the customer context
  > ElastiCache is ephemeral; an eviction or failover silently loses weeks of customer context.

**Why A is correct:** DynamoDB gives millisecond key-value lookup by customer ID, server-side encryption, and durability across the weeks-long horizon, independent of the agent's 600-second session TTL. S3 is the wrong access pattern, session memory is the wrong lifetime, and ElastiCache is the wrong durability.

**The trap AWS set here:** Session memory versus long-term memory. The 600-second idle TTL is the tripwire: anything tied to the session cannot meet a weeks-long requirement.

:::

:::pq {#q-d2-005}

*D2 · MEDIUM · ONE ANSWER* — q-d2-005 · 2.1 Human in the loop

**Q49.** An agent can initiate refunds, but company policy requires a human to approve any refund over $500 before it executes. Approvals may take up to 24 hours, every decision must be audited, and the workflow must survive the approver going home for the night. How should the developer enforce this?

- A. Orchestrate the refund workflow in Step Functions with a callback task token that waits up to 24 hours for human approval, logging every decision <!-- correct -->
- B. Add an instruction telling the agent to ask a human before large refunds
  > Prompt instructions are not enforcement; the agent can and will skip them under pressure.
- C. Implement the wait inside a Lambda function that polls for approval
  > Lambda caps at 15 minutes; it cannot wait 24 hours and polling burns compute.
- D. Use an IAM deny policy on refunds over $500 and have humans run them manually
  > This blocks the agent path entirely instead of gating it, and manual runs lose the audit workflow.

**Why A is correct:** Step Functions with a callback task token pauses the workflow durably until the human approves or the 24-hour timeout fires, giving an auditable, resumable approval gate. A Lambda cannot wait 24 hours (15-minute limit), and prompt instructions asking the agent to "wait for a human" are unenforceable. The timeout plus audit trail is what makes this production-grade.

**The trap AWS set here:** Instructions as enforcement. The exam treats "tell the agent to wait" as no control; durable orchestration with task tokens is the real gate.

:::

:::pq {#q-d2-006}

*D2 · MEDIUM · ONE ANSWER* — q-d2-006 · 2.1 Orchestration limits

**Q50.** An agent workflow runs for up to 45 minutes: it calls tools, waits for a human approval, then calls more tools. A developer proposes implementing the whole orchestration inside one Lambda function. Why is this wrong?

- A. Lambda has a 15-minute maximum execution time; Step Functions is built for long workflows with waits and approvals <!-- correct -->
- B. Lambda cannot call Bedrock APIs
  > Lambda calls Bedrock APIs fine; the limit is duration, not capability.
- C. Lambda is too expensive for 45 minutes
  > Cost is secondary; the design is impossible regardless of price.
- D. Step Functions cannot wait for humans
  > Waiting for humans via task tokens is one of Step Functions' signature features.

**Why A is correct:** Lambda's hard 15-minute limit kills any 45-minute orchestration, and waits burn billed duration. Step Functions is designed for exactly this: durable state, waits, human task tokens, and stopping conditions across hours or days.

**The trap AWS set here:** Lambda for long-running orchestration with waits. That is always Step Functions (master trap 1).

:::

:::pq {#q-d2-007}

*D2 · MEDIUM · SELECT 2* — q-d2-007 · 2.1 Agent frameworks

**Q51.** A team is evaluating the exam-named open-source agent frameworks. Which TWO statements are true? (Select TWO)

- A. Strands Agents is a code-first open-source framework for building agents <!-- correct -->
- B. AWS Agent Squad orchestrates multiple agents working together <!-- correct -->
- C. Strands Agents replaces IAM for agent security
  > No framework replaces IAM; agent tool calls still need least-privilege roles.
- D. Agent Squad is a Bedrock Agent alias type
  > Agent Squad is an orchestration framework, not an alias type; aliases belong to Bedrock Agents versioning.
- E. Both frameworks eliminate the need for human approvals
  > Approvals are a safety requirement no framework waives.

**Why A, B is correct:** Strands is the code-first agent-building framework and Agent Squad is the multi-agent orchestration layer; both are named in the exam guide as the open-source path, complementing Bedrock Agents.

**The trap AWS set here:** framework names confused with Bedrock Agent versioning concepts.

:::

:::pq {#q-d2-008}

*D2 · MEDIUM · ONE ANSWER* — q-d2-008 · 2.1 MCP hosting

**Q52.** A team exposes lightweight utility tools (date math, unit conversion, timezone lookup) to agents via MCP servers. The tools are stateless, bursty, and each invocation lasts under a second. A second set of tools wraps a legacy pricing engine that needs 4 GB of memory and 60-second warmup. Where should each set of MCP servers run?

- A. Lightweight tools on Lambda-hosted MCP servers; the pricing-engine tools on ECS-hosted MCP servers <!-- correct -->
- B. Both sets on EC2 instances for consistent hosting
  > Always-on EC2 for bursty sub-second tools is idle waste; it fails the cost-efficiency test.
- C. Both sets on Lambda for simplicity
  > Lambda cannot serve the 4 GB, 60-second-warmup engine reliably within its execution limits.
- D. Expose both over MCP STDIO transport from the agent host
  > STDIO is for local processes, not for remotely hosted tool servers; remote servers need Streamable HTTP.

**Why A is correct:** Lambda is the right host for lightweight, stateless, bursty MCP tools (scale to zero, sub-second billing), while the heavy stateful pricing engine belongs on ECS where memory and warmup can be provisioned. The exam's hosting rule is Lambda for lightweight and ECS for complex, and it tests whether you split the two instead of forcing one host for both.

**The trap AWS set here:** One host for everything. The scenario deliberately pairs opposite workload shapes so a single-host answer fails one of them.

:::

:::pq {#q-d2-009}

*D2 · MEDIUM · ONE ANSWER* — q-d2-009 · 2.1 AgentCore

**Q53.** A team built agents on Bedrock Agents but now wants to use an open-source agent framework of their choice while keeping AWS-managed hosting, memory, and observability. Which service is the migration path?

- A. Amazon Bedrock AgentCore, with Runtime for hosting any-framework agents plus Gateway, Memory, Identity, and Observability <!-- correct -->
- B. Amazon Lex
  > Lex is a conversational UI builder, not an agent hosting runtime.
- C. AWS Batch
  > Batch runs batch compute jobs, not interactive agents.
- D. Amazon ECS with no agent services
  > Raw ECS gives containers but none of the agent-specific managed services.

**Why A is correct:** AgentCore is the framework-freedom path: Runtime hosts agents built with any framework behind a standard invocations interface, while Gateway, Memory, Identity, and Observability provide the managed pieces Bedrock Agents previously bundled.

**The trap AWS set here:** Lex as the agent answer. Lex is chat UI; AgentCore is agent infrastructure.

:::

:::pq {#q-d2-010}

*D2 · HARD · ONE ANSWER* — q-d2-010 · 2.1 Full agent scenario

**Q54.** A wealth-management firm needs specialist agents for tax, investment, and estate planning that collaborate on client plans, use internal tools, remember client context for weeks, and require human approval for any action over $100,000. Which combination is most correct?

- A. Strands Agents plus Agent Squad for orchestration, MCP for tool access, DynamoDB for weeks-long memory, and Step Functions task tokens for the approval workflow <!-- correct -->
- B. One giant prompt containing all three specialties and tool documentation
  > One giant prompt cannot hold three specialties plus tools plus weeks of memory, and prose approvals are not enforcement.
- C. Amazon Lex bots with S3-stored memory and no approvals
  > Lex is conversational UI, not autonomous orchestration; S3 is wrong for memory access patterns; no approvals violates policy.
- D. A single Bedrock Agent with all tools and approvals requested in prose
  > A single agent with prose approvals fails the approval requirement structurally and overloads one agent's context.

**Why A is correct:** Each requirement maps to a mechanism: Strands plus Agent Squad for multi-agent orchestration, MCP for standardized tool access, DynamoDB for durable weeks-long memory with the right access pattern, and Step Functions task tokens for structural human approval. Nothing is left to prompt goodwill.

**The trap AWS set here:** Lex for orchestration and S3 for memory, plus prose where structure is required.

:::

:::pq {#q-d2-011}

*D2 · MEDIUM · SELECT 2* — q-d2-011 · 2.1 Agent safeguards

**Q55.** An agent with broad tool access goes to production. Which TWO safeguards should the developer implement? (Select TWO)

- A. Step Functions stopping conditions that bound iterations, cost, and time <!-- correct -->
- B. IAM roles with resource boundaries scoping exactly which tools and data the agent can touch <!-- correct -->
- C. Unlimited retries on every tool call
  > Unlimited retries turn one bad tool call into an infinite loop billed to you.
- D. No timeouts, so the agent always finishes
  > No timeouts guarantee hung executions instead of graceful failure.
- E. Full administrative credentials for maximum tool compatibility
  > Admin credentials give a compromised or confused agent the keys to everything.

**Why A, B is correct:** Stopping conditions bound the blast radius of runaway reasoning loops, and IAM resource boundaries enforce least privilege on every tool call. Both are structural controls that work even when the model misbehaves.

**The trap AWS set here:** operational unboundedness (no limits, no timeouts, admin creds) dressed as reliability.

:::

:::pq {#q-d2-012}

*D2 · HARD · ONE ANSWER* — q-d2-012 · 2.1 Tracing

**Q56.** An agent's answers are sometimes wrong and the team cannot tell whether the failure is in reasoning, tool selection, or tool results. What should they enable to diagnose this?

- A. Agent trace (enableTrace on invoke_agent) to inspect the reasoning path, tool calls, and observations step by step <!-- correct -->
- B. A higher temperature for more diverse reasoning
  > Temperature changes output randomness; it does not reveal the reasoning path.
- C. A larger context window
  > A larger context window holds more history but explains nothing about the failure.
- D. More CloudTrail log retention
  > CloudTrail shows API calls were made, not why the agent chose them or what it concluded.

**Why A is correct:** Tracing exposes the agent's internal loop: the model's reasoning, which action group it chose, the exact tool input, and the observation returned. That decomposes wrong answer into reasoning failure vs tool failure vs bad tool data.

**The trap AWS set here:** CloudTrail as a reasoning debugger. Trail audits calls; traces reveal reasoning.

:::

:::pq {#q-d2-013}

*D2 · MEDIUM · ONE ANSWER* — q-d2-013 · 2.2 Spiky traffic

**Q57.** A GenAI feature gets unpredictable bursts: quiet for hours, then thousands of requests in minutes, then quiet again. Users tolerate a few seconds of latency, but the CFO will not pay for idle capacity. The team is debating Provisioned Throughput for "reliability." Which invocation approach is most cost-effective?

- A. On-demand model invocation behind Lambda, scaling to zero between bursts <!-- correct -->
- B. Provisioned Throughput sized for the burst peaks
  > This commits hourly cost for capacity idle most of the time, violating the no-idle-cost constraint.
- C. A fixed EC2 fleet sized for peak bursts
  > Fixed fleets idle between bursts; it is the most expensive way to serve spiky traffic.
- D. Batch inference for the bursts
  > Batch inference has hours-scale latency and S3-based I/O; it cannot serve interactive burst traffic.

**Why A is correct:** On-demand invocation behind Lambda fits bursty, unpredictable traffic: zero idle cost, automatic scaling, and acceptable latency for a few-seconds tolerance. Provisioned Throughput commits hourly cost for capacity that sits idle between bursts, which directly violates the CFO's constraint. The exam's traffic-shape rule is spiky plus no-idle-cost equals on-demand, not provisioned.

**The trap AWS set here:** Provisioned Throughput as a reliability reflex. The exam uses the word "reliability" to tempt PT where the traffic shape demands on-demand.

:::

:::pq {#q-d2-014}

*D2 · HARD · ONE ANSWER* — q-d2-014 · 2.2 Hybrid deployment

**Q58.** An application serves 2 million requests per day as a steady baseline, with 10x spikes every Friday evening and a sub-3-second latency requirement. Which deployment is most correct?

- A. Provisioned Throughput covering the steady baseline, with on-demand invocations via Lambda absorbing the Friday spikes <!-- correct -->
- B. Provisioned Throughput sized for the 10x Friday peak, running all week
  > Sizing PT for the peak pays peak prices during every quiet hour of the week.
- C. On-demand only for everything, with client-side retries
  > Pure on-demand risks throttling exactly when the Friday spike needs guaranteed latency.
- D. SageMaker Serverless Inference for the full workload
  > Serverless Inference is for intermittent traffic with cold-start tolerance, not sustained high-throughput with a 3-second SLA.

**Why A is correct:** The hybrid pattern matches cost to shape: PT's hourly commit covers the predictable baseline with latency guarantees, while on-demand elasticity absorbs spikes without paying for peak capacity all week. This is the exam's signature most-correct deployment answer.

**The trap AWS set here:** single-mode answers (all PT, all on-demand) when the traffic shape demands a hybrid.

:::

:::pq {#q-d2-015}

*D2 · MEDIUM · ONE ANSWER* — q-d2-015 · 2.2 Batch

**Q59.** A company generates 50,000 product-description summaries every night. Nobody reads them until morning, the job must finish within 6 hours, and the CFO wants the lowest correct price after seeing the on-demand bill. Which inference option is cheapest and still correct?

- A. Batch inference with S3 input and output, scheduled nightly <!-- correct -->
- B. On-demand invocations as today
  > On-demand charges the real-time premium for responsiveness nobody uses; it is the expensive status quo.
- C. Provisioned Throughput for the nightly window
  > PT commits hourly capacity; a once-daily batch job cannot justify reserved throughput.
- D. Real-time streaming invocations for faster per-item latency
  > Streaming optimizes perceived latency for interactive users; there are no interactive users here.

**Why A is correct:** Bedrock batch inference is built for exactly this: non-interactive bulk jobs with hours-scale latency tolerance, S3 input and output, at roughly half the on-demand price. On-demand pays a premium for real-time responsiveness the scenario explicitly does not need, and provisioned throughput would commit hourly capacity for a job that runs once a day.

**The trap AWS set here:** Latency nobody needs. Every distractor pays for real-time responsiveness that "nobody reads until morning" rules out.

:::

:::pq {#q-d2-016}

*D2 · MEDIUM · ONE ANSWER* — q-d2-016 · 2.2 Custom models

**Q60.** A team fine-tuned their own model with proprietary training code and must serve it on AWS with autoscaling real-time endpoints under their full control, including custom container logic for request preprocessing. They also need blue-green deployments with rollback. Which service should host it?

- A. SageMaker AI real-time endpoints with autoscaling, custom containers, and Model Registry deployment pipelines <!-- correct -->
- B. Bedrock Provisioned Throughput on the fine-tuned weights
  > Provisioned Throughput reserves capacity for Bedrock-hosted models; it does not host customer-trained containers.
- C. AWS Lambda with the model weights in the deployment package
  > Lambda has strict package-size and no-GPU limits; it cannot serve LLM weights.
- D. EC2 instances with manually managed model servers
  > This works but abandons autoscaling, managed deployment guardrails, and rollback for hand-rolled operations.

**Why A is correct:** SageMaker AI real-time endpoints are the managed path for self-trained models: autoscaling, custom containers, and deployment guardrails (blue-green, rollback via Model Registry pipelines) under the team's full control. Bedrock Provisioned Throughput serves Bedrock-provided models, not customer-trained containers, and Lambda cannot serve GPU model containers.

**The trap AWS set here:** Bedrock versus SageMaker hosting. The exam tests whether the model is Bedrock-provided (PT) or customer-trained (SageMaker endpoints).

:::

:::pq {#q-d2-017}

*D2 · MEDIUM · SELECT 2* — q-d2-017 · 2.2 Model cascade

**Q61.** A team implements a model cascade to cut costs. Which TWO statements describe a correct cascade? (Select TWO)

- A. Simple queries go to a small cheap model first <!-- correct -->
- B. Low-confidence answers escalate to the larger flagship model <!-- correct -->
- C. Every query goes to the flagship model for safety
  > Always-flagship is the spend the cascade exists to cut.
- D. The small model handles everything with no escalation path
  > No escalation path means hard queries get bad answers with no recovery.
- E. Cascade means running both models on every query
  > Running both models every time doubles cost instead of cutting it.

**Why A, B is correct:** A cascade is a cost-quality router: the cheap model answers what it can confidently, and only uncertain or complex queries pay flagship prices. The confidence-gated escalation is what makes it a cascade rather than just a small model.

**The trap AWS set here:** cascade without the confidence-gated escalation, which is just a small model with extra steps.

:::

:::pq {#q-d2-018}

*D2 · MEDIUM · ONE ANSWER* — q-d2-018 · 2.2 Serverless inference

**Q62.** A SageMaker endpoint serves an internal data-labeling tool used a few times per hour, with no strict latency SLA and a mandate to minimize idle spend. Which inference option fits, and what is its key limitation the team must accept?

- A. Serverless Inference to eliminate idle cost, accepting cold-start latency on the first request after idle <!-- correct -->
- B. A real-time endpoint with autoscaling to zero
  > Real-time endpoints keep instances warm and bill for them; they do not scale to zero cost.
- C. Async inference for the labeling requests
  > Async inference targets long-running jobs with notification patterns, not intermittent interactive use.
- D. Provisioned Throughput for guaranteed capacity
  > PT commits hourly cost for a tool used a few times per hour; it maximizes the idle spend the scenario forbids.

**Why A is correct:** SageMaker Serverless Inference scales to zero for intermittent traffic, eliminating idle cost, which matches the usage pattern exactly. The accepted trade-off is cold starts: the first request after idle pays spin-up latency, which is why the "no strict latency SLA" constraint is the deciding factor.

**The trap AWS set here:** The limitation is part of the answer. The exam wants both the choice and its accepted trade-off: scale-to-zero means cold starts.

:::

:::pq {#q-d2-019}

*D2 · HARD · ONE ANSWER* — q-d2-019 · 2.2 Async inference

**Q63.** A media company runs inference jobs that take 30 to 60 minutes each: generating long-form video summaries. No user waits on the request; a notification fires when each job completes. Which SageMaker option fits?

- A. SageMaker Async Inference, which queues long-running requests and notifies on completion <!-- correct -->
- B. SageMaker real-time endpoints with 60-second timeouts
  > Real-time endpoints cap request handling far below 60 minutes; the job would be killed mid-run.
- C. Lambda invoking the model synchronously
  > Lambda's 15-minute limit cannot host a 60-minute synchronous call.
- D. Batch inference on Bedrock with streaming
  > Bedrock batch inference is a different service path, and streaming is meaningless for a non-interactive hour-long job.

**Why A is correct:** Async Inference exists for jobs that run minutes to an hour: it queues the request, processes it, and delivers the result to S3 with an SNS notification. The 30-60 minute duration rules out synchronous paths entirely.

**The trap AWS set here:** synchronous serving for hour-long jobs. Duration dictates async.

:::

:::pq {#q-d2-020}

*D2 · MEDIUM · ONE ANSWER* — q-d2-020 · 2.3 Event-driven

**Q64.** When a new order is placed, a GenAI service should generate a confirmation summary without the ordering system waiting for it. The summary must not be lost if the GenAI service is briefly down, and ordering must never block on summary generation. Which integration pattern provides this loose coupling?

- A. Publish an order event to EventBridge or SQS; the GenAI service consumes asynchronously with retries and a dead-letter queue <!-- correct -->
- B. Call the GenAI service synchronously from the ordering API
  > Synchronous calls make ordering wait on and fail with the summary service, violating both requirements.
- C. Stream order changes through CloudTrail to the GenAI service
  > CloudTrail is audit logging, not an event bus; it has no delivery guarantees or consumer pattern for this.
- D. Have the GenAI service poll the orders database every minute
  > Polling couples the services through the database, adds latency, and wastes queries when there are no orders.

**Why A is correct:** Publishing an order event to EventBridge or SQS decouples the systems: the ordering service returns immediately, and the GenAI consumer processes the event asynchronously with retries and a dead-letter queue for failures. Synchronous invocation would couple availability and latency of the two systems, violating both stated requirements.

**The trap AWS set here:** CloudTrail as an event bus. The exam offers audit logging where an event-driven pattern is needed.

:::

:::pq {#q-d2-021}

*D2 · MEDIUM · ONE ANSWER* — q-d2-021 · 2.3 Outposts

**Q65.** A bank must process customer data with a GenAI application, but regulators require the data to remain on the bank's own premises at all times. The bank still wants AWS-managed infrastructure and APIs rather than building its own platform. Which AWS option addresses this?

- A. AWS Outposts to run AWS infrastructure on the bank's premises <!-- correct -->
- B. VPC interface endpoints for Bedrock
  > Endpoints keep traffic off the public internet, but processing and storage still happen in the AWS region.
- C. KMS encryption on all data stores
  > Encryption protects data at rest; it does not keep the data on premises.
- D. Direct Connect to the nearest region
  > Direct Connect is private networking to a region; the data still leaves the premises for processing.

**Why A is correct:** AWS Outposts extends AWS infrastructure and services to on-premises locations, so data stays within the bank's premises while the team keeps AWS APIs and managed services. VPC endpoints keep traffic private but data still resides in an AWS region; KMS encrypts data but does not control where it lives. Residency is a location question, not an encryption question.

**The trap AWS set here:** Encryption versus residency. The exam offers KMS and private networking where the requirement is physical data location.

:::

:::pq {#q-d2-022}

*D2 · MEDIUM · ONE ANSWER* — q-d2-022 · 2.3 GenAI gateway

**Q66.** Fifty engineering teams each call Bedrock directly with their own keys, prompts, and logging. Security wants centralized policy enforcement, cost attribution, and observability. What should the company build?

- A. A centralized GenAI gateway: one abstraction layer for model access with policy control, logging, and cost tracking <!-- correct -->
- B. A shared spreadsheet of API keys
  > A spreadsheet of keys is a credential leak with extra steps.
- C. Fifty separate AWS accounts with no central view
  > Separate accounts without central governance multiply the problem instead of solving it.
- D. Direct model access with a request in the wiki to be careful
  > Wiki requests are not enforcement; nothing stops a team from ignoring them.

**Why A is correct:** A GenAI gateway centralizes model access behind one layer that enforces guardrail and IAM policy, emits uniform logs, and attributes token spend per team. It converts fifty snowflakes into one governed surface.

**The trap AWS set here:** decentralized direct access dressed as team autonomy when the requirement is governance.

:::

:::pq {#q-d2-023}

*D2 · MEDIUM · ONE ANSWER* — q-d2-023 · 2.3 CI/CD

**Q67.** A team ships its GenAI application weekly. Twice, a prompt change silently degraded answer quality and was discovered by customers days later. The team wants every release to run automated quality checks that block a bad release, with rollback if production metrics regress. Which pipeline practice matches the exam's enterprise guidance?

- A. CI/CD with automated model and prompt evaluation gates that block deployment on quality failure, plus monitored rollback <!-- correct -->
- B. Deploy weekly and monitor customer complaints as the quality signal
  > Customers as QA is the current failure mode; it detects regressions days late.
- C. Run evaluations manually after each deployment
  > Manual post-deploy checks are too slow and do not block the bad release.
- D. Freeze all prompt changes to stop regressions
  > Freezing changes stops improvement; the requirement is safe shipping, not no shipping.

**Why A is correct:** A CI/CD pipeline (CodePipeline or equivalent) with automated evaluation jobs as quality gates that block deployment on failure, plus production monitoring with automated rollback, is the enterprise pattern. "Deploy then test" or manual checks are exactly what allowed the silent regressions; the gate must come before production traffic.

**The trap AWS set here:** Detective versus preventive. Post-deploy monitoring detects the damage; only a pre-deploy gate prevents it.

:::

:::pq {#q-d2-024}

*D2 · MEDIUM · SELECT 2* — q-d2-024 · 2.3 Secure access

**Q68.** An enterprise rolls out GenAI to 2,000 employees. Which TWO controls belong in the access design? (Select TWO)

- A. IAM Identity Center permission sets giving each team least-privilege access to specific models and knowledge bases <!-- correct -->
- B. Least-privilege IAM policies on every Bedrock, knowledge base, and agent API call <!-- correct -->
- C. One shared IAM user whose credentials are emailed to all employees
  > A shared user destroys attribution and cannot be scoped per team.
- D. Administrator access for every employee to avoid permission tickets
  > Admin for everyone is the opposite of least privilege and a compliance failure.
- E. Hardcoded access keys in the frontend JavaScript
  > Frontend keys are extractable by anyone with a browser; they are never an access design.

**Why A, B is correct:** Identity Center provides federated RBAC so each team gets exactly the models and data it needs, and least-privilege policies on FM APIs enforce that boundary at every call. Identity plus policy is the complete access story.

**The trap AWS set here:** shared credentials or admin-for-all as simplicity. Least privilege is non-negotiable.

:::

:::pq {#q-d2-025}

*D2 · HARD · ONE ANSWER* — q-d2-025 · 2.3 Wrong-plane trap

**Q69.** A developer proposes using CloudTrail to stream real-time inventory changes from the legacy database into the GenAI application. What is wrong with this proposal?

- A. CloudTrail records AWS API activity for auditing; it is not a data pipeline and cannot stream database changes <!-- correct -->
- B. CloudTrail is too expensive for this volume
  > Cost is irrelevant; the service fundamentally cannot do the job.
- C. CloudTrail cannot be enabled on databases
  > The enablement detail misses the point: even where enabled, Trail carries API events, not row changes.
- D. Nothing is wrong; this is a standard pattern
  > Accepting the proposal builds a pipeline on a service that will never emit the needed events.

**Why A is correct:** CloudTrail's job is audit: who called which AWS API and when. It never sees inside database rows and has no streaming data-plane role. Real-time data sync needs CDC, DMS, or event publishing, not an audit log.

**The trap AWS set here:** The trap AWS set here is the proposal itself: CloudTrail for real-time data sync. Audit is not a data plane (master trap 14).

:::

:::pq {#q-d2-026}

*D2 · MEDIUM · ONE ANSWER* — q-d2-026 · 2.4 Converse API

**Q70.** An application must call Claude, Llama, and Titan with tool use, using identical code for all three. One workflow also needs a Claude-specific parameter that the unified API does not natively expose. Which API should the developer use, and how is the provider-specific need handled?

- A. Converse API for all calls, passing the Claude-specific parameter via additionalModelRequestFields <!-- correct -->
- B. InvokeModel with three separate provider-specific code paths
  > This triples the integration code and abandons the identical-code requirement.
- C. Converse API, dropping the Claude-specific parameter
  > Dropping a required parameter silently changes behavior; the escape hatch exists precisely for this.
- D. Raw HTTPS calls to each provider
  > This rebuilds auth, retry, and parsing for three providers by hand.

**Why A is correct:** The Converse API provides the unified request and response format with tool use across providers, satisfying the identical-code requirement. For the Claude-specific parameter, additionalModelRequestFields is the documented escape hatch that passes provider-specific fields through the unified API, so the team keeps one code path instead of branching to InvokeModel.

**The trap AWS set here:** The escape hatch. The exam tests whether you know additionalModelRequestFields keeps the unified path instead of forcing a provider-specific branch.

:::

:::pq {#q-d2-027}

*D2 · MEDIUM · ONE ANSWER* — q-d2-027 · 2.4 Embeddings API

**Q71.** An application has two needs: chat completions with tool use across Claude and Llama, and text embeddings to populate its vector store. A developer proposes using the Converse API for both to keep one code path. What is wrong with this plan?

- A. Converse cannot generate embeddings; use InvokeModel with an embedding model for the vector store and Converse for chat <!-- correct -->
- B. Nothing is wrong; Converse supports embeddings
  > Converse is text-generation only; this is the exact misconception the question tests.
- C. Use Comprehend to generate the embeddings
  > Comprehend performs NLP analysis; it does not produce embedding vectors for vector stores.
- D. Use Kendra to generate the embeddings
  > Kendra is enterprise search, not an embedding API.

**Why A is correct:** The Converse API is text-generation only; it cannot produce embeddings. Embeddings require InvokeModel with an embedding model. The correct design uses Converse for the chat completions and InvokeModel for the embeddings: two APIs, each for what it supports. The "one code path" goal cannot override API capabilities.

**The trap AWS set here:** Unified API overreach. Converse unifies chat, not everything; embeddings are the documented exception.

:::

:::pq {#q-d2-028}

*D2 · MEDIUM · ONE ANSWER* — q-d2-028 · 2.4 Provider specifics

**Q72.** A developer needs a Claude-specific parameter that the Converse API does not natively expose. Which approach is correct?

- A. Use InvokeModel with Claude's provider-specific request body including the required fields <!-- correct -->
- B. Give up; the parameter cannot be used on Bedrock
  > The parameter is fully usable; Bedrock does not hide provider features.
- C. Put the parameter in the system prompt as text
  > Prose in the system prompt does not set API parameters.
- D. Switch to a different cloud provider
  > Switching clouds over one parameter is disproportionate when the API already supports it.

**Why A is correct:** InvokeModel is the provider-specific path: it accepts each provider's native body (for Claude, fields like anthropic_version and max_tokens), which is where provider-exotic parameters live. Converse also offers additionalModelRequestFields as an escape hatch, but InvokeModel is the direct answer.

**The trap AWS set here:** assuming Converse covers everything. Provider-exotic features mean InvokeModel.

:::

:::pq {#q-d2-029}

*D2 · MEDIUM · ONE ANSWER* — q-d2-029 · 2.4 Streaming

**Q73.** A chat application must show tokens to the user as they are generated, minimizing perceived latency. Which combination delivers this?

- A. ConverseStream (or InvokeModelWithResponseStream) with WebSockets or server-sent events to the browser <!-- correct -->
- B. Batch inference with hourly polling
  > Batch is hours-scale; it cannot stream anything.
- C. API Gateway with default settings and a 29-second integration timeout for a 5-minute stream
  > API Gateway's timeouts will cut a long stream mid-response; that is why the exam pushes WebSockets for streaming.
- D. Emailing the completed response
  > Email is not a real-time UX pattern.

**Why A is correct:** ConverseStream emits tokens incrementally, and WebSockets or SSE carry them to the browser as they arrive. API Gateway has payload and timeout limits, so long streams go over WebSockets or direct streaming instead.

**The trap AWS set here:** API Gateway default limits silently killing long streams. Stream over WebSockets/SSE.

:::

:::pq {#q-d2-030}

*D2 · HARD · ONE ANSWER* — q-d2-030 · 2.4 PT routing bug

**Q74.** A company bought Provisioned Throughput for Claude. The application still gets throttled at peak, and CloudWatch shows all invocations hitting the on-demand model ID. Code review finds: invoke_model(modelId='anthropic.claude-...'). What is the fix?

- A. Invoke the provisioned model identifier (the provisioned model ARN), not the base model ID <!-- correct -->
- B. Buy more Provisioned Throughput model units
  > More units cannot help traffic that never routes to the provisioned model; this is the exam's classic capacity-versus-routing trap (master trap 11).
- C. Increase the retry count in the SDK
  > Retries on the wrong target still hit the on-demand pool.
- D. Switch to a different region
  > Regions do not fix a routing bug in the code.

**Why A is correct:** The code bypasses the reservation entirely: PT capacity only applies when invocations target the provisioned model ARN/ID. Calling the base model ID sends traffic to the shared on-demand pool, so throttling persists no matter how much PT was purchased. Routing, not capacity, is the bug.

**The trap AWS set here:** increasing PT units when the code never routes to the provisioned model. Check the target first (master trap 11).

:::

:::pq {#q-d2-031}

*D2 · MEDIUM · SELECT 2* — q-d2-031 · 2.4 ApplyGuardrail

**Q75.** A team uses a non-Bedrock model but wants Bedrock Guardrails safety checks on its inputs and outputs. Which TWO statements are true? (Select TWO)

- A. The standalone ApplyGuardrail API evaluates content independently of any model <!-- correct -->
- B. Guardrails can protect non-Bedrock models, including third-party and self-hosted ones <!-- correct -->
- C. Guardrails only work inside the Converse API
  > Converse is one integration path, not the only one; standalone is the other.
- D. ApplyGuardrail generates the model's response
  > ApplyGuardrail assesses content; it never generates text.
- E. Guardrails require the model to run on Bedrock
  > The model-location claim is exactly the misconception the standalone API disproves.

**Why A, B is correct:** ApplyGuardrail is model-agnostic: it takes content in and returns a safety assessment, so any model (OpenAI, Gemini, self-hosted) can be wrapped with Bedrock safety policy without running on Bedrock.

**The trap AWS set here:** guardrails only work with Converse or Bedrock-hosted models. ApplyGuardrail is standalone.

:::

:::pq {#q-d2-032}

*D2 · MEDIUM · ONE ANSWER* — q-d2-032 · 2.4 ValidationException

**Q76.** A developer migrates a working Titan integration to Claude on Bedrock, keeping the same InvokeModel call structure but swapping the model ID and body. Calls now fail with ValidationException. Model access and IAM permissions are verified working. What should the developer check first, and why did Titan work?

- A. The request body format: Claude requires anthropic_version and max_tokens, which the Titan-shaped body lacks <!-- correct -->
- B. Request a quota increase for Claude
  > ValidationException is a malformed-request error, not a throttling or quota error.
- C. Re-verify IAM permissions for the Claude model
  > Permissions are stated as verified; repeating a ruled-out check is the debugging anti-pattern.
- D. Switch to the Converse API to avoid body formats entirely
  > Converse would work, but the question asks for the diagnosis; the body mismatch is the root cause to fix first.

**Why A is correct:** InvokeModel bodies are provider-specific: Claude requires anthropic_version (bedrock-2023-05-31) and max_tokens, while Titan has a different schema. The Titan body was valid for Titan and invalid for Claude, so the first check is the request body against Claude's documented format. IAM and model access are already verified, so re-checking them wastes the debugging step.

**The trap AWS set here:** Provider-specific bodies. The exam punishes assuming one InvokeModel body shape works across providers.

:::

:::pq {#q-d2-033}

*D2 · MEDIUM · ONE ANSWER* — q-d2-033 · 2.5 Q Developer

**Q77.** Developers want an AI assistant inside their IDE that suggests code, refactors functions, and writes unit tests, integrated with their CI pipeline for automated test generation on pull requests. Which service fits, and which similarly named service is the distractor?

- A. Amazon Q Developer for IDE assistance and test generation; Q Business is the enterprise-chat distractor <!-- correct -->
- B. Amazon Q Business for IDE code suggestions
  > Q Business answers questions over enterprise data; it does not live in the IDE or generate tests.
- C. Bedrock Agents to review every pull request autonomously
  > Agents are for application workflows, not a managed developer-productivity tool.
- D. A knowledge base over the codebase with manual prompting
  > This rebuilds by hand what Q Developer provides managed, with no IDE integration.

**Why A is correct:** Amazon Q Developer is the coding assistant: IDE integration, code suggestions, refactoring, and test generation, including CI workflows. Amazon Q Business is the similarly named distractor: it is an enterprise chat assistant over company data, not a developer tool. The exam swaps the two names deliberately.

**The trap AWS set here:** Q Developer versus Q Business. The exam's favorite name-swap: one is for developers, one is for enterprise chat.

:::

:::pq {#q-d2-034}

*D2 · MEDIUM · ONE ANSWER* — q-d2-034 · 2.5 IDP

**Q78.** An insurance company must process 20,000 claim documents per day (PDFs, photos, forms, some handwritten) into structured data for downstream systems. The pipeline must handle all four modalities, extract to a defined schema, and run with minimal custom code. Which service is built for this document-processing workflow?

- A. Bedrock Data Automation with a custom blueprint defining the claim schema <!-- correct -->
- B. Amazon Textract alone with custom post-processing in Lambda
  > Textract extracts text, but the multimodal mix and schema mapping need the orchestration BDA provides; this is the hand-built alternative.
- C. Bedrock Guardrails to validate and structure the documents
  > Guardrails filter content for safety; they do not extract structured data from documents.
- D. A Bedrock Knowledge Base over the claim documents
  > Knowledge Bases do retrieval-augmented generation, not structured extraction into downstream systems.

**Why A is correct:** Bedrock Data Automation is the managed intelligent-document-processing service: multimodal input (documents, images), extraction to standard or blueprint-defined custom schemas, async at scale. Textract alone would need a hand-built orchestration layer for the photos, handwriting, and schema mapping that BDA provides natively.

**The trap AWS set here:** Extraction versus retrieval. The exam offers Knowledge Bases and Guardrails where the job is structured document extraction.

:::

:::pq {#q-d2-035}

*D2 · MEDIUM · ONE ANSWER* — q-d2-035 · 2.5 Amplify

**Q79.** A frontend team must ship a web UI for the GenAI assistant in two weeks, with user authentication, a chat interface that streams responses, and API integration, but minimal backend code. Which service fits, and what does it not replace?

- A. AWS Amplify for the UI, auth, and API integration; the Bedrock model layer stays behind the API <!-- correct -->
- B. EC2 instances with a hand-built web stack
  > Hand-built servers maximize backend code and ops work, violating both constraints.
- C. S3 static hosting alone
  > Static hosting has no authentication or API integration story for a streaming chat UI.
- D. Amplify as a replacement for the Bedrock model calls
  > Amplify builds the app tier; it does not host or replace foundation-model inference.

**Why A is correct:** AWS Amplify is the declarative UI-plus-backend service: managed hosting, Cognito authentication, and API integration with minimal backend code, which matches the two-week, minimal-backend constraint. It does not replace the model-serving layer; the assistant still calls Bedrock behind the Amplify-built API.

**The trap AWS set here:** Layer confusion. Amplify accelerates the app tier; the exam tests whether you know it does not replace the model tier.

:::

:::pq {#q-d2-036}

*D2 · HARD · ONE ANSWER* — q-d2-036 · 2.5 Full scenario

**Q80.** A publisher must generate study materials from 10,000+ files per day including video, with editors collaborating on drafts in real time. Which combination is most correct?

- A. Bedrock Data Automation for extraction, S3 versioning for draft history, and AppSync with DynamoDB for real-time collaboration <!-- correct -->
- B. Bedrock Agents for change tracking and Guardrails for extraction
  > Agents do not do change tracking and Guardrails do not extract; both halves of this option misuse the services.
- C. Emailing files between editors and manual uploads
  > Email collaboration at 10,000 files a day is an operational collapse.
- D. A single EC2 instance running a video converter
  > One EC2 instance is a single point of failure that cannot scale to the volume.

**Why A is correct:** Each need maps to a service: Data Automation extracts from mixed modalities at scale, S3 versioning keeps every draft recoverable, and AppSync plus DynamoDB gives real-time collaborative editing with offline sync. Nothing is repurposed outside its job.

**The trap AWS set here:** Agents for change tracking and Guardrails for extraction. Name each service's real job.

:::

## Domain 3: AI Safety, Security, and Governance (20% of the exam, 28 questions) {#sec-d3}

**Decision reference.** Match the scenario verb in the question stem to the control in the left column.

| Control | What it does | Scenario verb |
|---|---|---|
| Content filters | Toxicity categories plus prompt attack, severity NONE to HIGH | block profanity, violence, jailbreaks |
| Denied topics | Subject-area bans in natural language | never discuss medical diagnosis |
| Word filters | Exact-match blocklists | never say these brand names |
| Sensitive info filters | PII entity detection, block or mask | redact SSNs |
| Contextual grounding | Is the answer supported by the source? | RAG hallucinations |
| Automated Reasoning | Deterministic check against policy rules | totals must equal line items |

**How to read this diagram.**

:::walkthrough

1. Profanity, violence, or jailbreak language maps to content filters, with prompt attack as its own category.
2. A ban on discussing a subject (investment advice, diagnoses) maps to denied topics, never to content filters.
3. Specific exact strings map to word filters; PII patterns map to sensitive info filters, never the reverse.
4. Is this claim in the source maps to contextual grounding; does this violate the formal rule maps to Automated Reasoning.
5. The exam's favorite confusion set lives in this table: read the verb, pick the row.
6. If this table breaks (wrong control), the guardrail deploys but the requirement silently goes unenforced.
:::

:::pq {#q-d3-001}

*D3 · MEDIUM · ONE ANSWER* — q-d3-001 · 3.1 Denied topics

**Q81.** A health chatbot must never provide medical diagnoses, even if the user asks directly or rephrases the request ("what do these symptoms mean?"). The team debates three guardrail controls: a content filter, a word filter listing diseases, or a denied topic. Which control enforces this, and why do the other two fail?

- A. A denied topic defined in natural language covering medical diagnosis <!-- correct -->
- B. A content filter with a high severity threshold
  > Content filters score toxicity categories; there is no "medical advice" toxicity category to threshold.
- C. A word filter listing disease names
  > Exact-match lists lose to rephrasing ("what do these symptoms mean?") and need endless maintenance.
- D. A system prompt instructing the model to refuse diagnoses
  > Prompt instructions are jailbreakable; the requirement demands an enforced control, not a request.

**Why A is correct:** Denied topics block subject areas defined in natural language ("providing medical diagnoses"), which catches rephrasings that a fixed word list misses. Content filters target toxicity categories (hate, violence), not subject matter; word filters are exact-match blocklists that lose to paraphrase. The scenario verb "must never discuss this subject" is the denied-topics trigger.

**The trap AWS set here:** Control-to-verb matching. "Never discuss this subject" maps to denied topics; the exam punishes reaching for toxicity or exact-match controls.

:::

:::pq {#q-d3-002}

*D3 · MEDIUM · ONE ANSWER* — q-d3-002 · 3.1 PII redaction

**Q82.** A support chatbot must redact Social Security numbers from its outputs before users see them, while keeping the rest of the answer readable (for example, "your SSN ending in 1234"). Blocking the entire response is unacceptable to the product team. Which guardrail control does this, and which action mode?

- A. A sensitive information filter for the SSN entity type in mask mode on outputs <!-- correct -->
- B. A sensitive information filter in block mode
  > Block mode rejects the entire response, which the product team explicitly ruled out.
- C. A word filter with common SSN patterns
  > SSNs are not enumerable strings; entity-type detection is the correct mechanism, not exact matching.
- D. A denied topic for personal data
  > Denied topics block subject areas; they cannot surgically redact one entity from an otherwise fine answer.

**Why A is correct:** Sensitive information filters detect PII entity types (including SSNs) and support mask mode, which redacts the entity while preserving the surrounding answer. Block mode would kill the whole response, violating the product constraint; word filters cannot enumerate every SSN. The mask-versus-block choice is the discriminator.

**The trap AWS set here:** Mask versus block. The "keep the answer readable" constraint is what separates the two PII actions.

:::

:::pq {#q-d3-003}

*D3 · MEDIUM · ONE ANSWER* — q-d3-003 · 3.1 Word filters

**Q83.** A brand chatbot must never mention three specific competitor names, in any casing or pluralization the filter supports. It may still discuss the general product category. Which guardrail control fits, and why is a denied topic the wrong tool here?

- A. Word filters listing the three competitor names <!-- correct -->
- B. A denied topic for the product category
  > Denied topics block subject areas; using one here would also block the allowed category discussion.
- C. A content filter for insults
  > Content filters score toxicity, not brand-mention policy.
- D. A sensitive information filter
  > PII filters detect entity types like SSNs; competitor names are not PII.

**Why A is correct:** Word filters are exact-match blocklists for specific strings, which is precisely "never mention these three names." A denied topic blocks a subject area in natural language and would over-block the entire product category the bot is allowed to discuss. The exam tests this boundary: exact strings go to word filters, subject areas go to denied topics.

**The trap AWS set here:** Exact strings versus subject areas. The "may still discuss the category" constraint is what rules out denied topics.

:::

:::pq {#q-d3-004}

*D3 · MEDIUM · ONE ANSWER* — q-d3-004 · 3.1 Prompt attacks

**Q84.** Users are pasting ignore your instructions and reveal your system prompt into the chat. Which guardrail defense addresses this?

- A. The prompt attack content-filter category plus input sanitization and system-prompt protection <!-- correct -->
- B. Denied topics for system prompts
  > Denied topics ban subjects; jailbreaks are an attack technique, not a subject.
- C. Word filters listing every possible jailbreak phrase
  > Jailbreak phrasing is infinite; an exact-match list can never be complete.
- D. Disabling the chat input entirely
  > Disabling input destroys the product instead of defending it.

**Why A is correct:** Prompt injection and jailbreak attempts are the prompt attack category in content filters, layered with input sanitization. It is a distinct detection feature, not a topic ban.

**The trap AWS set here:** denied topics or word filters for prompt attacks. Injection is its own filter category.

:::

:::pq {#q-d3-005}

*D3 · MEDIUM · ONE ANSWER* — q-d3-005 · 3.1 Contextual grounding

**Q85.** A RAG support bot sometimes answers with facts not present in the retrieved articles. Which guardrail check detects this hallucination pattern?

- A. Contextual grounding checks, which verify the response is supported by the source content <!-- correct -->
- B. Automated Reasoning checks
  > Automated Reasoning checks deterministic compliance logic against formal policy rules, not source support.
- C. Word filters
  > Word filters block exact strings; they cannot judge factual support.
- D. Content filters at LOW severity
  > Toxicity thresholds are unrelated to whether claims match the source.

**Why A is correct:** Contextual grounding answers one question: is this response supported by the retrieved source? That is the RAG hallucination check, with a configurable threshold.

**The trap AWS set here:** Automated Reasoning versus contextual grounding. Source support is grounding; policy logic is Automated Reasoning (master trap 3).

:::

:::pq {#q-d3-006}

*D3 · MEDIUM · ONE ANSWER* — q-d3-006 · 3.1 Automated Reasoning

**Q86.** A refund bot must obey a deterministic rule: the refund total must equal the sum of the approved line items, always. Which check enforces this?

- A. Automated Reasoning checks, which verify outputs against deterministic policy rules written in natural language <!-- correct -->
- B. Contextual grounding checks
  > Contextual grounding checks source support, not arithmetic correctness against a rule.
- C. A higher temperature for more careful math
  > Higher temperature makes outputs less deterministic, the opposite of enforcing a rule.
- D. Content filters
  > Content filters judge toxicity categories, not math.

**Why A is correct:** Automated Reasoning performs deterministic logic verification against formal policy rules, so an arithmetic compliance rule like totals must match line items is enforced by logic, not by probabilistic judgment.

**The trap AWS set here:** contextual grounding for a deterministic rule. Rules need Automated Reasoning (master trap 3).

:::

:::pq {#q-d3-007}

*D3 · MEDIUM · SELECT 2* — q-d3-007 · 3.1 Defense in depth

**Q87.** A children's tutoring app must block profanity in inputs, prevent harmful outputs, stop jailbreak attempts, and ground facts in lesson material. Which TWO layers belong in its defense-in-depth design? (Select TWO)

- A. Bedrock Guardrails applied on both inputs and outputs <!-- correct -->
- B. A Comprehend pre-filter for toxicity and PII before the model call <!-- correct -->
- C. Relying on the base model's built-in safety alone
  > Base-model safety alone is never the most-correct answer for a sensitive audience; it is one layer, not a design (master trap 15).
- D. No logging, to keep the design simple
  > No logging removes the audit trail a children's product regulator will demand.
- E. A single system prompt asking the model to be safe
  > A prompt request is not a control; jailbreaks target exactly this layer.

**Why A, B is correct:** Defense in depth layers independent controls: Guardrails on inputs and outputs catch what one side misses, and a Comprehend pre-filter adds a separate toxicity/PII screen before the model ever sees the text. Layers fail independently, which is the point.

**The trap AWS set here:** the base model's built-in safety as the complete answer. Never sufficient for sensitive scenarios (master trap 15).

:::

:::pq {#q-d3-008}

*D3 · MEDIUM · ONE ANSWER* — q-d3-008 · 3.1 Input and output

**Q88.** A team wants guardrails to screen user prompts before the model sees them AND screen generated answers before users see them. Their model runs outside Bedrock (a self-hosted open model). Which statements are true about meeting this requirement?

- A. One guardrail configured for inputs and outputs, invoked via ApplyGuardrail on the prompt and on the completion <!-- correct -->
- B. Two separate guardrails are required, one for inputs and one for outputs
  > A single guardrail covers inputs, outputs, or both; splitting them doubles management for nothing.
- C. Guardrails only work with Bedrock-hosted models
  > ApplyGuardrail is model-agnostic and works with self-hosted or third-party models.
- D. Input screening is not supported; guardrails only screen outputs
  > Guardrails explicitly support input screening, which is where prompt attacks are caught.

**Why A is correct:** Guardrails apply to inputs, outputs, or both, configured once per guardrail. For a non-Bedrock model, the standalone ApplyGuardrail API provides the same checks without Converse, so the team calls it on the prompt before inference and on the completion after. No second guardrail and no Bedrock-hosted model are required.

**The trap AWS set here:** "Is this supported" upgraded. The exam hides the real test (ApplyGuardrail for non-Bedrock models) behind a yes/no framing.

:::

:::pq {#q-d3-009}

*D3 · HARD · ONE ANSWER* — q-d3-009 · 3.1 Combined scenario

**Q89.** A fintech chatbot must: refuse investment advice, redact account numbers from outputs, resist jailbreak attempts, and ground every answer in the bank's policy documents. Which combination is most correct?

- A. Denied topics for investment advice, sensitive information filters masking account numbers, the prompt attack filter for jailbreaks, plus a knowledge base with contextual grounding checks <!-- correct -->
- B. Content filters at HIGH severity for everything
  > One severity knob cannot express a topic ban, PII masking, and source grounding; it conflates every control into toxicity.
- C. Word filters listing financial terms and a long system prompt
  > Word lists cannot cover advice phrasing, and prompts do not enforce.
- D. Relying on the flagship model's built-in safety
  > Built-in safety alone is never the complete answer for a regulated audience (master trap 15).

**Why A is correct:** Each requirement maps to its control: denied topics for the subject ban, sensitive info filters for the PII entity, prompt attack detection for jailbreaks, and KB grounding plus contextual grounding for factual answers. Four requirements, four matched mechanisms.

**The trap AWS set here:** one blunt control for four distinct requirements. Match the control to the scenario verb (master trap 3).

:::

:::pq {#q-d3-010}

*D3 · HARD · ONE ANSWER* — q-d3-010 · 3.1 Hallucination reduction

**Q90.** A RAG application's hallucination rate is too high for a regulated deployment. Which combination most reduces hallucinations?

- A. Knowledge base grounding plus confidence scoring, JSON Schema structured outputs, and contextual grounding checks <!-- correct -->
- B. A larger generation model with a higher temperature
  > A larger model with higher temperature is more fluent and more creative, which increases fabrication risk on factual tasks.
- C. Removing all guardrails to reduce latency
  > Removing guardrails removes the verification layer entirely.
- D. Longer prompts with more examples
  > More examples improve style, not factuality against sources.

**Why A is correct:** Hallucinations fall when every layer constrains fabrication: grounding supplies true sources, confidence scoring surfaces uncertainty, JSON Schema restricts output shape, and contextual grounding verifies claims against sources. No single knob does all four.

**The trap AWS set here:** model size or temperature as the hallucination fix. Grounding plus verification is the fix.

:::

:::pq {#q-d3-011}

*D3 · MEDIUM · ONE ANSWER* — q-d3-011 · 3.2 VPC endpoints

**Q91.** A company requires all Bedrock API traffic to stay off the public internet, with no NAT gateways in the design. The application uses model invocation, knowledge bases, and agents. Which configuration meets the requirement?

- A. VPC interface endpoints for the bedrock, bedrock-runtime, bedrock-agent, and bedrock-agent-runtime planes <!-- correct -->
- B. A NAT gateway in each Availability Zone
  > NAT gateways route to the public internet; the requirement is no public internet at all.
- C. KMS encryption on all Bedrock requests
  > Encryption protects payloads; it does not change the network path.
- D. A single interface endpoint for bedrock-runtime only
  > This covers invocations but leaves knowledge-base and agent API calls on the public path.

**Why A is correct:** VPC interface endpoints (PrivateLink) for each Bedrock plane used (bedrock, bedrock-runtime, bedrock-agent, bedrock-agent-runtime) keep API traffic on the AWS private network with no NAT and no public internet traversal. A NAT gateway still sends traffic over the public internet; KMS and security groups do not change routing.

**The trap AWS set here:** Partial coverage. The scenario names three planes so that a single-endpoint answer leaves traffic exposed.

:::

:::pq {#q-d3-012}

*D3 · MEDIUM · SELECT 3* — q-d3-012 · 3.2 PII pipeline

**Q92.** A customer-service GenAI application must protect PII across stored chat logs and live conversations, with minimal custom code. Which THREE services form the standard pipeline? (Select THREE)

- A. Amazon Macie to discover PII in S3 at scale <!-- correct -->
- B. Amazon Comprehend for real-time PII detection in text <!-- correct -->
- C. Bedrock Guardrails sensitive information filters at inference time <!-- correct -->
- D. Amazon Translate to obfuscate the PII
  > Translate preserves meaning across languages; it protects nothing.
- E. Amazon Rekognition to find PII in chat text
  > Rekognition is a vision service; chat text is Comprehend's domain.

**Why A, B, C is correct:** The three cover the full lifecycle: Macie finds PII already sitting in S3, Comprehend detects it in live text streams, and Guardrails filters block or mask it at inference. Minimal custom code, complete coverage.

**The trap AWS set here:** Translate for obfuscation and Rekognition for text PII. Both are wrong-plane tools.

:::

:::pq {#q-d3-013}

*D3 · MEDIUM · ONE ANSWER* — q-d3-013 · 3.2 Macie

**Q93.** A company has 40 TB of historical chat logs in S3 and needs to find where PII is stored before designing protections. The discovery must be automated, cover the full 40 TB, and classify findings by PII type. Which service discovers PII at this scale, and why not the inference-time tools?

- A. Macie for automated PII discovery and classification across the S3 data at rest <!-- correct -->
- B. Bedrock Guardrails PII filters
  > Guardrails screen live model inputs and outputs; they do not scan stored objects.
- C. Comprehend DetectPIIEntities over every object
  > Per-call API scanning of 40 TB is operational overhead; Macie is the managed discovery service.
- D. Manual Athena queries with regex patterns
  > Hand-written regex cannot reliably detect PII types and does not scale to 40 TB of logs.

**Why A is correct:** Macie is the managed data-discovery service for S3 at scale: automated PII classification across terabytes of stored objects. Guardrails PII filters and Comprehend operate at inference time on live traffic; they do not scan 40 TB of objects at rest. The exam's layer rule is Macie for at-rest discovery, Guardrails for inference-time filtering.

**The trap AWS set here:** At-rest versus inference-time. The 40 TB figure is the signal: this is a discovery job, not a live-filtering job.

:::

:::pq {#q-d3-014}

*D3 · MEDIUM · ONE ANSWER* — q-d3-014 · 3.2 Comprehend realtime

**Q94.** A live chat moderator dashboard needs real-time detection of PII entities in streaming conversation text, flagged within seconds so moderators can intervene. Separately, the model itself must never emit PII. Which two-layer design fits with managed services?

- A. Comprehend real-time PII detection for the moderator stream plus Guardrails PII filters on the model calls <!-- correct -->
- B. Macie for the live stream
  > Macie scans S3 objects at rest; it has no streaming API for live chat.
- C. Guardrails alone for both needs
  > Guardrails protect the model boundary; they do not feed a moderator dashboard on the raw stream.
- D. Amazon Rekognition for the text stream
  > Rekognition is a vision service; the stream is text, which is Comprehend's domain.

**Why A is correct:** Comprehend real-time PII detection fits the streaming moderator dashboard (entity detection on live text), while Bedrock Guardrails sensitive-information filters at the model call prevent the model from emitting PII. Macie is at-rest discovery and cannot do seconds-latency streaming; one layer alone leaves either the dashboard or the model uncovered.

**The trap AWS set here:** Two consumers, two layers. The dashboard and the model are different enforcement points needing different services.

:::

:::pq {#q-d3-015}

*D3 · MEDIUM · ONE ANSWER* — q-d3-015 · 3.2 Invocation logging

**Q95.** A healthcare application logs Bedrock model invocations to CloudWatch for debugging, but the logs may contain patient information. What should the developer do?

- A. Disable invocation logging or restrict it with KMS encryption and tight access controls <!-- correct -->
- B. Keep logging everything; debugging needs full data
  > Full PHI in logs is a compliance violation regardless of debugging convenience.
- C. Move the logs to a public S3 bucket for easier access
  > A public bucket turns a violation into a breach.
- D. Log only the model ID and hope that is enough
  > Model IDs alone cannot debug prompt-level issues, so this both fails compliance hygiene and fails debugging.

**Why A is correct:** Invocation logs can contain prompts and completions, which means PHI. In compliance environments the exam answer is to disable logging or encrypt it with KMS and lock down access; convenience never outranks the compliance requirement.

**The trap AWS set here:** unencrypted invocation logging in a healthcare scenario. Logs carry PII; treat them accordingly.

:::

:::pq {#q-d3-016}

*D3 · MEDIUM · ONE ANSWER* — q-d3-016 · 3.2 Obfuscation trap

**Q96.** A developer proposes running all user text through Amazon Translate twice (to another language and back) to obfuscate PII before model calls. Why is this wrong?

- A. Translation preserves meaning, so PII survives intact; it provides zero protection and adds latency <!-- correct -->
- B. Translate cannot process PII
  > Translate processes any text; the problem is what it preserves, not what it accepts.
- C. Translate is too expensive for this
  > Cost is secondary to the fact that the protection is fictional.
- D. Double translation is not supported
  > Round-trip translation is supported; support is not the issue.

**Why A is correct:** Obfuscation must destroy or mask the sensitive data; translation preserves semantic content by design, so names, numbers, and identifiers come through unchanged. The proposal adds latency while protecting nothing.

**The trap AWS set here:** The trap AWS set here is the proposal itself: Translate for PII protection. Meaning-preserving transforms are not masking.

:::

:::pq {#q-d3-017}

*D3 · HARD · ONE ANSWER* — q-d3-017 · 3.2 Bank scenario

**Q97.** A bank's GenAI assistant handles account data under strict regulation: traffic must stay private, data encrypted at rest, every API call audited, and prompts must never persist in logs. Which combination is most correct?

- A. VPC interface endpoints for Bedrock, KMS encryption at rest, CloudTrail for API auditing, and invocation logging disabled <!-- correct -->
- B. Public Bedrock endpoints with TLS only
  > Public endpoints with TLS fail the private-traffic requirement outright.
- C. CloudWatch Logs for auditing API calls
  > CloudWatch Logs hold application content; API auditing is CloudTrail's job.
- D. Storing prompts in S3 for debugging convenience
  > Persisting prompts in S3 directly violates the no-persistence requirement.

**Why A is correct:** Each regulatory need maps to a control: PrivateLink keeps traffic off the public internet, KMS encrypts data at rest, CloudTrail audits who called what, and disabling invocation logging guarantees prompts never persist. TLS alone leaves three requirements unmet.

**The trap AWS set here:** TLS as the complete security answer, and CloudWatch Logs confused with CloudTrail auditing.

:::

:::pq {#q-d3-018}

*D3 · MEDIUM · ONE ANSWER* — q-d3-018 · 3.3 Lake Formation

**Q98.** A data lake holds tables with different sensitivity levels. GenAI pipelines for three teams must each read only the columns their team is authorized for; Team A must never see the salary column that Team B needs. IAM table-level grants are too coarse. Which service provides this granular access control?

- A. Lake Formation with column-level grants per team <!-- correct -->
- B. IAM policies on the tables
  > IAM grants are table-level; they cannot hide one column from one team while showing it to another.
- C. Separate S3 buckets per column
  > Physically shredding tables per column is unmaintainable and breaks every query.
- D. Bedrock Guardrails to filter the salary data from outputs
  > Guardrails screen model content; they are not a data-access control for pipelines.

**Why A is correct:** Lake Formation provides column-level (and row-level) fine-grained access control over data lake tables, which is exactly "Team B sees the salary column, Team A does not." IAM policies grant at the table or object level and cannot express column grants; Guardrails operate at model inference, not data access.

**The trap AWS set here:** Access control versus content filtering. The exam offers inference-time safety where the requirement is data-plane authorization.

:::

:::pq {#q-d3-019}

*D3 · MEDIUM · ONE ANSWER* — q-d3-019 · 3.3 Model Cards

**Q99.** A regulated company must document each model's intended uses, limitations, and evaluation results for auditors, versioned alongside the model artifacts so the documentation cannot drift from what is deployed. Which SageMaker feature produces this, and what does it not replace?

- A. SageMaker Model Cards versioned with the model; they document the model, not its API audit trail <!-- correct -->
- B. CloudTrail logs as the model documentation
  > CloudTrail records API calls; it does not document intended uses, limitations, or eval results.
- C. A wiki page updated by the ML team
  > A wiki drifts from deployed artifacts; it is not versioned with the model package.
- D. SageMaker Clarify reports as the full documentation
  > Clarify covers bias and explainability analysis; it is one input to a card, not the card itself.

**Why A is correct:** SageMaker Model Cards produce versioned, programmatic documentation of intended uses, limitations, and evaluation results tied to the model package. They do not replace CloudTrail audit logs (who called what API when); cards document the model, trails document its use. The exam tests knowing documentation-of-the-model versus audit-of-its-use.

**The trap AWS set here:** Model documentation versus usage audit. Cards describe the model; CloudTrail describes who used it.

:::

:::pq {#q-d3-020}

*D3 · MEDIUM · ONE ANSWER* — q-d3-020 · 3.3 Audit trail

**Q100.** After a disputed AI-generated decision, auditors ask: which IAM identity invoked the model, at what time, and with which parameters? Which service answers this?

- A. AWS CloudTrail, which records every Bedrock API call with identity and timestamp <!-- correct -->
- B. CloudWatch Logs Insights over application logs
  > CloudWatch Logs hold application and decision content; the who-called-what audit is Trail's plane.
- C. The model's own memory
  > Models do not retain invocation audit records.
- D. Amazon S3 access logs
  > S3 access logs cover S3 requests only, not Bedrock invocations.

**Why A is correct:** CloudTrail is the API audit trail: who called what, when, from where. Identity-plus-timestamp-plus-API-action is the signature CloudTrail question.

**The trap AWS set here:** CloudWatch Logs for API auditing. Trail audits calls; Logs hold content.

:::

:::pq {#q-d3-021}

*D3 · MEDIUM · ONE ANSWER* — q-d3-021 · 3.3 Lineage

**Q101.** A regulator asks: which source documents produced this specific generated answer? Which combination provides the lineage?

- A. Glue Data Catalog registration of sources, metadata tagging through the pipeline, and source attribution on generated content <!-- correct -->
- B. A longer context window
  > Context size does not record where content came from.
- C. Deleting old document versions
  > Deleting versions destroys lineage instead of building it.
- D. Training the model on fewer documents
  > Fewer documents do not create traceability.

**Why A is correct:** Lineage is built from cataloged sources (Glue Data Catalog), metadata tags carried through ingestion, and attribution attached to outputs, so any answer traces back to its documents. No single feature does this alone.

**The trap AWS set here:** single-feature answers for lineage, which is always a combination of catalog, tags, and attribution.

:::

:::pq {#q-d3-022}

*D3 · HARD · SELECT 2* — q-d3-022 · 3.3 Continuous compliance

**Q102.** A lending assistant operates under fair-lending regulation. Which TWO practices demonstrate continuous compliance rather than one-time checking? (Select TWO)

- A. Automated monitoring for misuse, drift, and policy violations with alerting <!-- correct -->
- B. A remediation workflow triggered by monitoring alerts <!-- correct -->
- C. One pre-launch fairness review with no follow-up
  > One pre-launch review cannot catch drift that appears months later.
- D. Deleting decision logs after 7 days to save storage
  > Deleting logs destroys the evidence regulators require.
- E. Annual manual spot checks only
  > Annual checks leave eleven months of unmonitored operation.

**Why A, B is correct:** Continuous means always-on: monitoring detects drift, misuse, and violations as they happen, and the remediation workflow acts on alerts without waiting for a human audit cycle. That is the exam's governance posture.

**The trap AWS set here:** one-time checks dressed as compliance. The exam wants continuous monitoring plus remediation.

:::

:::pq {#q-d3-023}

*D3 · HARD · ONE ANSWER* — q-d3-023 · 3.3 Bias over time

**Q103.** A hiring assistant passed fairness testing at launch. Six months later, applicant demographics shifted and outputs show skew. What should the team have had in place?

- A. Continuous bias drift monitoring with automated alerts, not just the launch-time test <!-- correct -->
- B. A larger model
  > Model size does not prevent drift-induced skew.
- C. More training data at launch
  > Launch-time data cannot cover future demographic shifts.
- D. A disclaimer in the UI
  > A disclaimer does not detect or fix biased outputs.

**Why A is correct:** Fairness is a moving target: data drift changes model behavior after launch, so only continuous monitoring with alerts catches skew when it appears. A launch test is a snapshot, not a guarantee.

**The trap AWS set here:** treating fairness as a one-time check. The exam demands continuous monitoring.

:::

:::pq {#q-d3-024}

*D3 · MEDIUM · ONE ANSWER* — q-d3-024 · 3.4 Transparency

**Q104.** Loan applicants must be told why the AI assistant reached its recommendation, in terms they can verify: which sources were used and how confident the system is. A vendor proposes "our model is 99% accurate, so explanations are unnecessary." Which capability provides the required transparency?

- A. Per-decision explanations with source citations, confidence signals, and inspectable reasoning traces <!-- correct -->
- B. The vendor accuracy claim as sufficient transparency
  > Aggregate accuracy explains nothing about why this applicant got this recommendation.
- C. A larger, more accurate model
  > Accuracy and explainability are different properties; a bigger model is no more transparent.
- D. A prompt asking the model to explain itself, with no grounding
  > Ungrounded self-explanations can be plausible fabrications; verifiability requires citations and traces.

**Why A is correct:** Transparency for loan decisions means attributable, verifiable explanation: source citations for the facts used, confidence signals, and reasoning traces the applicant (and auditor) can inspect. Raw accuracy claims do not explain any individual decision. The exam treats "the model is accurate" as the anti-answer to a transparency requirement.

**The trap AWS set here:** Accuracy as transparency. The exam offers "the model is very accurate" wherever explainability is required; it never satisfies the requirement.

:::

:::pq {#q-d3-025}

*D3 · MEDIUM · ONE ANSWER* — q-d3-025 · 3.4 Model comparison

**Q105.** A team must compare two models for support-summary quality, including whether summaries match the company brand voice. Which evaluation approach is most correct?

- A. LLM-as-a-judge for correctness at scale, plus human evaluation for brand voice <!-- correct -->
- B. Programmatic metrics only
  > Programmatic metrics cannot judge style or voice.
- C. Pick the model with more parameters
  > Parameter count does not predict brand-voice fit.
- D. Ask the sales team informally
  > Informal opinions are not an evaluation methodology.

**Why A is correct:** Quality at scale needs LLM-as-a-judge (correctness, completeness, faithfulness across thousands of samples), while brand voice is subjective and needs human judgment. The combination covers objective and subjective in the right proportions.

**The trap AWS set here:** programmatic evaluation for subjective style. Subjective needs human or LLM-as-judge.

:::

:::pq {#q-d3-026}

*D3 · MEDIUM · ONE ANSWER* — q-d3-026 · 3.4 Fairness

**Q106.** A team must ensure assistant outputs stay unbiased across demographic groups. Which approach is most correct?

- A. Pre-defined fairness metrics, A/B testing via Prompt Management variants, and LLM-as-a-judge evaluations <!-- correct -->
- B. Using a bigger model, which is naturally fairer
  > Model size has no reliable relationship with fairness.
- C. Removing all demographic words from prompts
  > Word removal is cosmetic and can hide bias while leaving disparate outcomes.
- D. Testing once with five examples
  > Five examples cannot measure group-level disparities.

**Why A is correct:** Fairness is engineered: define metrics up front, A/B test variants for disparate impact, and evaluate with LLM-as-judge at scale. Bigger models are not inherently fairer, and five examples prove nothing.

**The trap AWS set here:** a bigger model as the fairness fix. Fairness needs metrics and measurement, not scale.

:::

:::pq {#q-d3-027}

*D3 · MEDIUM · ONE ANSWER* — q-d3-027 · 3.4 Responsible AI

**Q107.** A news summarizer must show readers which source each claim came from, so readers can verify claims themselves. The team must also prove before launch that summaries stay faithful to those sources. Which principle is this, and how is it implemented and measured?

- A. Transparency via per-claim source citations, implemented with grounded generation and measured by faithfulness evaluation <!-- correct -->
- B. Fairness, measured with demographic parity metrics
  > The requirement is verifiability of claims, not unbiased treatment of groups.
- C. Safety, implemented with a content filter
  > Content filters score toxicity; they do not attribute claims to sources.
- D. Trust in the base model, with no citations
  > Unverifiable summaries fail the stated reader-verification requirement.

**Why A is correct:** This is transparency through source attribution: citations on claims, implemented via retrieval-grounded generation, and measured pre-launch with faithfulness (groundedness) evaluations against the cited sources. It is not a fairness or toxicity problem, so fairness metrics and content filters miss the requirement entirely.

**The trap AWS set here:** Principle-to-mechanism mapping. The exam upgrades "which principle" into "which principle, implemented how, measured how."

:::

:::pq {#q-d3-028}

*D3 · HARD · ONE ANSWER* — q-d3-028 · 3.4 Regulated fairness

**Q108.** A bank deploys a loan-advice assistant under fair-lending scrutiny. Regulators will ask for proof of ongoing fairness. Which combination is most correct?

- A. Pre-defined fairness metrics with continuous drift monitoring and alerts, model cards documenting limitations, and a human review loop for edge cases <!-- correct -->
- B. A one-time bias test before launch
  > One-time tests cannot catch post-launch drift.
- C. The largest available model with default settings
  > Default settings on a large model are not evidence of fairness.
- D. A system prompt asking the model to be fair
  > A prompt request is not a control and not auditable evidence.

**Why A is correct:** Regulated fairness needs the full stack: metrics defined before launch, continuous monitoring because drift happens, model cards documenting known limitations for auditors, and humans reviewing the edge cases automation cannot judge. Each piece answers a regulator's question.

**The trap AWS set here:** one-time testing or prompt requests as fairness proof. Regulators want continuous, documented, human-backed evidence.

:::

## Domain 4: Operational Efficiency and Optimization (12% of the exam, 17 questions) {#sec-d4}

**Decision reference.** Match the cost lever to the traffic shape and symptom, not to the buzzword.

:::ladder

1. **On-demand** — Spiky, experimental, unpredictable. Pay per token.
2. **Prompt caching** — Repeated large static prefixes. Cheaper cached input tokens via cachePoint.
3. **Batch inference** — Non-interactive, hours OK. About 50 percent cheaper.
4. **Provisioned Throughput** — Steady baseline, latency SLA, no throttling. Hourly commit.
5. **Smaller model / cascade** — Route simple queries cheap; escalate hard ones on low confidence.

:::

**How to read this diagram.**

:::walkthrough

1. Spiky unpredictable traffic stays on-demand; reserved capacity for bursts wastes money.
2. The same long system prompt on every call is the prompt caching signature.
3. Nobody waiting and hours acceptable is batch pricing, roughly half off.
4. Steady baseline plus throttling or latency SLA is Provisioned Throughput.
5. Mostly simple queries with some hard ones is a cascade: cheap first, escalate on low confidence.
6. If this ladder breaks (wrong lever), you pay peak prices in quiet hours or throttle under steady load.
:::

:::pq {#q-d4-001}

*D4 · MEDIUM · ONE ANSWER* — q-d4-001 · 4.1 Prompt caching

**Q109.** Every call to a support assistant starts with the same 8,000-token system prompt of policy text, and token costs are climbing 30% month over month. The prompt rarely changes, the model is Claude 3.5, and the team is considering Provisioned Throughput to cut the bill. What is the most direct cost fix, and why is Provisioned Throughput the wrong lever?

- A. Enable prompt caching on the static system prompt; Provisioned Throughput addresses capacity, not repeated-prefix cost <!-- correct -->
- B. Buy Provisioned Throughput to lower the token bill
  > PT reserves throughput; it does not discount repeated input tokens.
- C. Shorten the policy text with a smaller model
  > Rewriting compliance policy text risks losing coverage; the cost lever is caching, not content surgery.
- D. Set temperature to 0 to reduce token usage
  > Temperature controls randomness, not token count or cost.

**Why A is correct:** Prompt caching (cachePoint) makes the repeated 8,000-token prefix dramatically cheaper: the static prefix is the exact pattern caching attacks, with a 5-minute default TTL that covers conversational turns. Provisioned Throughput is a latency and throughput guarantee, not a repeated-input cost saver; it commits hourly spend without reducing the per-token cost of the repeated prefix.

**The trap AWS set here:** Caching versus Provisioned Throughput. "Same long prefix on every call" is the caching trigger; the exam offers PT to test whether you know what PT actually buys.

:::

:::pq {#q-d4-002}

*D4 · MEDIUM · ONE ANSWER* — q-d4-002 · 4.1 Caching vs PT

**Q110.** An application has steady, predictable traffic and users report throttling errors at peak. The token bill is acceptable; latency and reliability are the problems. What should the developer choose?

- A. Provisioned Throughput for the predictable baseline <!-- correct -->
- B. Prompt caching
  > Prompt caching cuts repeated-input cost, which is not the reported problem.
- C. Semantic caching in ElastiCache
  > Semantic caching helps repeated similar queries, not throttling under load.
- D. A smaller model
  > A smaller model changes quality and price, not reserved capacity.

**Why A is correct:** Throttling under steady predictable load is a capacity problem, and Provisioned Throughput reserves model units to eliminate it. The bill is fine, so cost levers are the wrong tools; this is the latency/throughput guarantee case.

**The trap AWS set here:** cost levers for a capacity problem. Match the lever to the symptom: throttling means capacity (master trap 4).

:::

:::pq {#q-d4-003}

*D4 · MEDIUM · SELECT 2* — q-d4-003 · 4.1 Tiered models

**Q111.** A team wants tiered model usage: cheap models for simple queries, flagship quality for hard ones. Which TWO pieces make this work? (Select TWO)

- A. A classifier or router that scores query complexity before choosing the model <!-- correct -->
- B. Routing simple queries to the small model and complex ones to the flagship <!-- correct -->
- C. Sending every query to the flagship model
  > Always-flagship is the spend tiering exists to cut.
- D. Using the small model for everything with no fallback
  > Small-model-only sacrifices quality on hard queries with no recovery.
- E. Choosing models randomly to spread load
  > Random routing optimizes nothing and risks quality on every hard query.

**Why A, B is correct:** Tiered usage needs both halves: a complexity signal (classifier or prompt router) and the routing policy that acts on it. Without the classifier there is no signal; without the policy there is no savings.

**The trap AWS set here:** tiering without the complexity signal. A router with no classifier is decoration.

:::

:::pq {#q-d4-004}

*D4 · MEDIUM · ONE ANSWER* — q-d4-004 · 4.1 Batch inference

**Q112.** A nightly job summarizes 20,000 support tickets. It currently uses on-demand calls, takes 3 hours, and the CFO asks why it costs so much. The summaries must be ready by 6 AM; nobody consumes them before then. What is the cheapest correct change?

- A. Move the job to batch inference with S3 input and output <!-- correct -->
- B. Keep on-demand but add retries
  > Retries do not change the per-token price; the cost problem is the pricing tier, not reliability.
- C. Buy Provisioned Throughput for the nightly window
  > PT commits hourly capacity for a batch job; batch inference is the purpose-built cheaper tier.
- D. Enable prompt caching on the ticket text
  > Ticket text is unique per call, so there is no repeated prefix for caching to discount.

**Why A is correct:** Batch inference fits the workload shape exactly: non-interactive, hours-tolerant, S3 in and out, at roughly half the on-demand price, comfortably inside the 6 AM deadline. The current on-demand spend pays a real-time premium for responsiveness the 6 AM deadline does not require.

**The trap AWS set here:** Deadline-shaped pricing. "Ready by 6 AM, nobody reads before then" is the batch-inference trigger; every real-time option wastes money.

:::

:::pq {#q-d4-005}

*D4 · MEDIUM · SELECT 3* — q-d4-005 · 4.1 Multi-lever savings

**Q113.** Token costs grow 30% per month. The CFO demands cuts with no UX degradation. Which THREE levers belong in the plan? (Select THREE)

- A. Route low-priority traffic to smaller cheaper models <!-- correct -->
- B. Prompt caching for the repeated system prefix <!-- correct -->
- C. Provisioned Throughput for the predictable baseline load <!-- correct -->
- D. Always use the flagship model for every query
  > Always-flagship is the current expensive default, not a cut.
- E. Disable all logging to save money
  > Disabling logging saves pennies while destroying observability and audit trails.

**Why A, B, C is correct:** Cost optimization is multi-lever: smaller models cut per-token price where quality allows, caching discounts repeated prefixes, and PT rightsizes the steady baseline. Each lever attacks a different part of the bill without touching user experience.

**The trap AWS set here:** single-lever answers. The exam's most-correct cost answers stack complementary levers.

:::

:::pq {#q-d4-006}

*D4 · MEDIUM · ONE ANSWER* — q-d4-006 · 4.1 Semantic cache

**Q114.** A FAQ bot receives the same 200 questions phrased slightly differently, thousands of times a day. Full model calls answer each one today. The team debates prompt caching versus a semantic cache. Which reduces model calls here, and why does prompt caching fail?

- A. A semantic cache on question embeddings; prompt caching needs identical prefixes and misses paraphrases <!-- correct -->
- B. Prompt caching on the FAQ prompt
  > Prompt caching matches exact prefixes; "phrased slightly differently" defeats it.
- C. Provisioned Throughput to absorb the volume
  > PT guarantees capacity; it does not reduce the number of model calls or their cost.
- D. Fine-tune a model on the 200 questions
  > Fine-tuning bakes in behavior but every query still costs a full model call.

**Why A is correct:** A semantic cache (ElastiCache or DynamoDB keyed by embedding similarity) matches paraphrases of the same question, which is exactly "phrased slightly differently." Prompt caching requires byte-identical prefixes, so reworded questions miss the cache entirely. The paraphrase tolerance is the discriminator between the two caching layers.

**The trap AWS set here:** Two caches, different keys. Prompt caching keys on exact tokens; semantic caching keys on meaning. The paraphrase detail picks the winner.

:::

:::pq {#q-d4-007}

*D4 · HARD · ONE ANSWER* — q-d4-007 · 4.1 Cost scenario

**Q115.** A SaaS company serves 8 million chat requests per month. Analysis shows: 70% are simple lookups answerable by a small model, every request carries the same 6,000-token policy prefix, traffic is steady day to day, and Friday evenings spike 5x. Which cost plan is most correct?

- A. Route simple queries to a small model, enable prompt caching for the repeated prefix, hold Provisioned Throughput for the steady baseline, and let on-demand absorb Friday spikes <!-- correct -->
- B. Run everything on the flagship model with on-demand pricing
  > All-flagship on-demand ignores every observed savings opportunity.
- C. Buy Provisioned Throughput sized for the Friday peak and use it all week
  > Peak-sized PT pays peak prices through every quiet hour.
- D. Cache full responses for every query including personalized ones
  > Full-response caching on personalized queries gets near-zero hit rates; the blueprint explicitly rejects this.

**Why A is correct:** Every observed fact maps to a lever: 70% simple means tiered routing, the repeated prefix means prompt caching, steady baseline means PT, and 5x spikes mean on-demand overflow. The most-correct answer stacks all four instead of picking one.

**The trap AWS set here:** any single-lever plan. Real cost optimization composes levers to match the traffic shape.

:::

:::pq {#q-d4-008}

*D4 · MEDIUM · ONE ANSWER* — q-d4-008 · 4.2 Temperature

**Q116.** A classification task returns different labels for identical inputs across runs, but the business requires 99.5% consistency for audit purposes. A developer proposes buying Provisioned Throughput "so the model behaves the same every time." What is the first fix, and why is the proposal wrong?

- A. Set temperature to 0 with versioned prompts; Provisioned Throughput fixes capacity, not randomness <!-- correct -->
- B. Buy Provisioned Throughput for consistent outputs
  > PT guarantees throughput and latency; it does not make sampling deterministic.
- C. Increase max tokens for more thorough reasoning
  > Longer outputs do not stabilize the label; they add variance surface.
- D. Switch to a larger model
  > A larger model is still stochastic at temperature above 0.

**Why A is correct:** Set temperature to 0 (with fixed seeds where supported and versioned prompts): nondeterminism across identical inputs is a sampling problem, fixed by sampling controls. Provisioned Throughput reserves capacity and stabilizes latency; it has no effect on output randomness. The exam's classic conflation is capacity versus determinism.

**The trap AWS set here:** Capacity versus determinism. The exam offers Provisioned Throughput wherever consistency is demanded; it never fixes sampling randomness.

:::

:::pq {#q-d4-009}

*D4 · MEDIUM · ONE ANSWER* — q-d4-009 · 4.2 Streaming

**Q117.** Users complain a chat assistant feels slow, though total response time is acceptable. The biggest win for perceived latency is:

- A. Streaming tokens with ConverseStream so users read while the model still generates <!-- correct -->
- B. A larger model for faster thinking
  > Larger models are generally slower per token, the opposite direction.
- C. Batch inference
  > Batch is hours-scale and non-interactive.
- D. Longer system prompts
  > Longer prompts add input processing time, making things worse.

**Why A is correct:** Streaming attacks perceived latency: the first token arrives in a fraction of the total time, so the app feels instant even when full generation takes seconds. Perceived latency and actual latency are different problems.

**The trap AWS set here:** optimizing total time when the complaint is perceived latency. Stream first.

:::

:::pq {#q-d4-010}

*D4 · MEDIUM · ONE ANSWER* — q-d4-010 · 4.2 PT consistency trap

**Q118.** A developer proposes buying Provisioned Throughput to make model outputs more consistent across identical prompts. Why is this wrong?

- A. Provisioned Throughput reserves capacity and stabilizes latency; output randomness is controlled by temperature and prompt design, not capacity <!-- correct -->
- B. Provisioned Throughput makes outputs less consistent
  > PT does not harm consistency; it is simply irrelevant to it.
- C. Temperature cannot be set on provisioned models
  > Inference parameters apply normally to provisioned models.
- D. Consistency is impossible with any model
  > Deterministic outputs are achievable with temperature 0 and controlled prompts.

**Why A is correct:** Capacity and randomness are independent axes: PT buys reserved model units (no throttling, stable latency), while temperature and prompt control govern sampling variance. Buying capacity to fix randomness is a category error the exam names explicitly.

**The trap AWS set here:** The trap AWS set here is the proposal itself: PT for output consistency. Name the two axes and keep them separate (master trap 12).

:::

:::pq {#q-d4-011}

*D4 · EASY · ONE ANSWER* — q-d4-011 · 4.2 Inference params

**Q119.** A developer proposes tuning temperature, top-p, and top-k to cut the token bill. Why is this misguided?

- A. Those parameters control randomness and output quality, not cost; token count and model choice drive the bill <!-- correct -->
- B. Those parameters do not exist
  > They exist and matter, just for quality, not cost.
- C. Those parameters increase cost directly
  > They do not carry a price tag; the bill is tokens times model rate.
- D. Cost cannot be optimized at all
  > Cost is highly optimizable, through the right levers.

**Why A is correct:** Temperature, top-p, and top-k shape the sampling distribution: creativity versus determinism. They do not change per-token price or, reliably, token counts. Cost levers are model selection, caching, batching, and prompt compression.

**The trap AWS set here:** quality knobs as cost knobs. Keep the two families separate.

:::

:::pq {#q-d4-012}

*D4 · HARD · ONE ANSWER* — q-d4-012 · 4.2 Retrieval latency

**Q120.** A RAG application's p99 latency is 9 seconds. Profiling shows retrieval takes 7 seconds: unoptimized vector index, no query preprocessing, and keyword-only search missing often. Which combination most reduces retrieval latency?

- A. Index optimization and sharding, query preprocessing, hybrid search with custom scoring, plus caching of frequent queries <!-- correct -->
- B. A larger generation model
  > The generation model is 2 of the 9 seconds; upsizing it worsens latency.
- C. Higher temperature
  > Temperature does not affect retrieval speed.
- D. Provisioned Throughput on the embedding model
  > PT on embeddings buys capacity that is not the problem; the index itself is slow.

**Why A is correct:** The profile says retrieval is the bottleneck, so every fix targets retrieval: optimized indexes and sharding cut search time, preprocessing shrinks the query, hybrid search with scoring finds answers in fewer round trips, and caching skips repeat work. Fix the measured bottleneck.

**The trap AWS set here:** model-side fixes for a measured retrieval bottleneck. Profile first, then fix what is slow.

:::

:::pq {#q-d4-013}

*D4 · MEDIUM · ONE ANSWER* — q-d4-013 · 4.3 Cost attribution

**Q121.** A product manager wants per-feature token spend to attribute costs to teams: which feature burned how many input and output tokens last month. Finance also wants the numbers reconciled against the AWS bill. Which setup provides the raw data and the reconciliation?

- A. CloudWatch InputTokenCount and OutputTokenCount metrics tagged per feature, reconciled with the Cost and Usage Report <!-- correct -->
- B. CloudTrail logs grouped by feature
  > CloudTrail audits who called what; it does not record token counts per call.
- C. A single account-level token metric
  > Account-level totals cannot attribute spend to features or teams.
- D. Manual sampling of prompts to estimate per-feature cost
  > Sampling is neither complete nor auditable for chargeback.

**Why A is correct:** CloudWatch Bedrock metrics (InputTokenCount, OutputTokenCount, Invocations) broken down by cost-allocation tags per feature give the raw per-feature data; the Cost and Usage Report reconciles those against the bill. CloudTrail records API calls, not token counts, so it cannot attribute spend.

**The trap AWS set here:** Audit versus metering. CloudTrail answers "who called what"; only token metrics answer "what did it cost."

:::

:::pq {#q-d4-014}

*D4 · MEDIUM · SELECT 2* — q-d4-014 · 4.3 Anomaly detection

**Q122.** A team needs near-real-time detection of hallucinations in production plus alerts on abnormal token spend, with minimal custom code. Which TWO capabilities meet this? (Select TWO)

- A. Bedrock evaluation jobs with LLM-based judgments scoring outputs against quality criteria <!-- correct -->
- B. CloudWatch anomaly detection on token count metrics <!-- correct -->
- C. A hand-built Glue plus Athena pipeline over raw logs
  > Glue plus Athena is the high-overhead distractor: batch, custom, and slow where managed real-time exists (master trap 14).
- D. CloudTrail for real-time metric alerts
  > CloudTrail is audit logging, not a metrics alerting plane.
- E. Manual daily reading of random outputs
  > Manual sampling cannot be near-real-time at production volume.

**Why A, B is correct:** Bedrock evaluations bring LLM-as-a-judge scoring to production outputs for hallucination detection, and CloudWatch anomaly detection watches token metrics for spend spikes. Both are managed, near-real-time, and low-code.

**The trap AWS set here:** Glue plus Athena for real-time detection, and CloudTrail for metrics. Wrong-plane tools (master trap 14).

:::

:::pq {#q-d4-015}

*D4 · MEDIUM · ONE ANSWER* — q-d4-015 · 4.3 Tracing

**Q123.** A multi-step agent calls three tools and a knowledge base per request. Debugging is hard because failures hide inside the chain: the team cannot tell whether a bad answer came from poor reasoning, a wrong tool choice, or a bad tool result. What provides end-to-end visibility into the chain?

- A. X-Ray tracing across the agent chain plus the agent trace showing reasoning, tool selection, and tool results per step <!-- correct -->
- B. CloudWatch Logs with verbose logging
  > Logs show disconnected lines; they do not reconstruct the multi-step chain structure.
- C. CloudTrail for the agent API calls
  > CloudTrail audits API invocations; it captures none of the reasoning or tool-result content.
- D. A Bedrock Guardrail in trace mode
  > Guardrails screen content; they do not trace multi-step agent execution.

**Why A is correct:** Distributed tracing with X-Ray across the agent steps, combined with the agent's own trace output (enableTrace showing reasoning, tool selection, and tool results per step), decomposes the chain into inspectable spans. CloudWatch Logs alone show disconnected log lines with no chain structure; CloudTrail shows API calls but not the reasoning between them.

**The trap AWS set here:** Logs versus traces. The exam offers logging wherever chain structure is the actual need; only tracing reconstructs the steps.

:::

:::pq {#q-d4-016}

*D4 · MEDIUM · ONE ANSWER* — q-d4-016 · 4.3 Model Monitor trap

**Q124.** A developer proposes SageMaker Model Monitor to detect quality drift in the chatbot's free-text answers. Why is this the wrong tool?

- A. Model Monitor is built for tabular ML feature and prediction drift; GenAI text quality drift needs Bedrock evaluations or golden datasets <!-- correct -->
- B. Model Monitor cannot run on a schedule
  > Scheduling is not the issue; the data type is.
- C. Model Monitor only works with Bedrock
  > Model Monitor is SageMaker-side, not Bedrock-side; the direction of the claim is backwards.
- D. Text drift cannot be monitored at all
  > Text drift is monitorable, with the right evaluation-based tools.

**Why A is correct:** Model Monitor watches statistical drift in structured features and predictions. Free-text answer quality (hallucinations, tone drift, factuality) needs LLM-as-a-judge evaluations or golden-dataset comparisons, which are the GenAI-native tools.

**The trap AWS set here:** The trap AWS set here is the proposal itself: tabular ML monitoring for GenAI text. Match the monitor to the data type.

:::

:::pq {#q-d4-017}

*D4 · HARD · ONE ANSWER* — q-d4-017 · 4.3 Forensics

**Q125.** Last Tuesday a customer received a badly wrong answer. Support must find the exact prompt, retrieved chunks, and model response for that request. Which setup makes this possible?

- A. Model invocation logging to S3 or CloudWatch, queried with CloudWatch Logs Insights for prompt and response forensics <!-- correct -->
- B. CloudTrail lookup of the request
  > CloudTrail records that an API call happened, not the prompt and response content.
- C. Guessing from the current prompt template
  > The current template may differ from Tuesday's version; reconstruction needs the logged artifact.
- D. Application metrics dashboards
  > Metrics dashboards show aggregates, never individual payloads.

**Why A is correct:** Invocation logging captures the actual request and response payloads; Logs Insights then searches them by time, user, or session to reconstruct exactly what happened. Forensics needs payloads, not just metadata.

**The trap AWS set here:** CloudTrail for content forensics. Trail proves the call; logs hold the content.

:::

## Domain 5: Testing, Validation, and Troubleshooting (11% of the exam, 15 questions) {#sec-d5}

**Decision reference.** Debug in this order. Skipping steps is how hours get lost.

:::ladder

1. **Content handling** — Context overflow: chunking, prompt compression, truncation analysis.
2. **API integration** — ValidationException means the provider body; misleading AccessDenied means region availability.
3. **Prompt problems** — Version comparison, systematic refinement, regression suites.
4. **Retrieval problems** — Embedding quality, chunking, relevance. Retrieval before generation, always.
5. **Capacity vs routing** — PT throttling: check the provisioned ARN target first, then size units.

:::

**How to read this diagram.**

:::walkthrough

1. Step 1 first: whole documents in prompts cause silent truncation; fix with chunking plus retrieval.
2. Step 2: ValidationException with good permissions is the request body; AccessDenied in one region is availability.
3. Step 3: changed behavior means version comparison plus regression data, not temperature tuning.
4. Step 4: confident-but-wrong on RAG is retrieval until proven otherwise; never fix it with a bigger model.
5. Step 5: PT throttling means check routing to the provisioned ARN before buying more units.
6. If this order breaks (generation fixed first), you tune the wrong layer while the real bug sits upstream.
:::

:::pq {#q-d5-001}

*D5 · MEDIUM · ONE ANSWER* — q-d5-001 · 5.1 Programmatic eval

**Q126.** A team needs an objective, repeatable benchmark of summary accuracy run nightly over 10,000 examples, with results comparable across prompt versions. Human review at that scale is impossible, and the metric must be deterministic. Which evaluation method fits, and what is its boundary?

- A. Programmatic evaluation on a fixed dataset; it covers objective metrics, not subjective style <!-- correct -->
- B. Nightly human review of all 10,000 summaries
  > Impossible at this scale and non-deterministic across reviewers.
- C. LLM-as-a-judge for the accuracy benchmark
  > Judge models add cost and non-determinism; for objective accuracy, programmatic scoring is the repeatable choice.
- D. Skip evaluation and monitor production complaints
  > Production complaints are lagging, sparse, and cannot compare prompt versions.

**Why A is correct:** Programmatic (automatic) evaluation with built-in or custom datasets gives deterministic, repeatable scoring at 10,000-example nightly scale. Its boundary is subjectivity: it measures what can be computed (accuracy, toxicity, robustness), not style or brand voice, which need LLM-as-a-judge or human review.

**The trap AWS set here:** Scale plus determinism. "10,000 nightly" plus "comparable across versions" rules out humans and judges for the objective benchmark.

:::

:::pq {#q-d5-002}

*D5 · MEDIUM · ONE ANSWER* — q-d5-002 · 5.1 LLM-as-judge

**Q127.** A team needs human-like quality judgments (correctness, completeness, faithfulness) across 50,000 RAG answers before launch. Human review at that scale is impossible, but leadership does not trust a purely automated gate. Which method fits, and what guardrail makes it trustworthy?

- A. LLM-as-a-judge scoring, calibrated against a human-reviewed sample measuring judge-human agreement <!-- correct -->
- B. Programmatic exact-match scoring on all 50,000 answers
  > Exact match cannot score free-text correctness, completeness, or faithfulness.
- C. Human review of a 50-answer sample as the whole gate
  > A 50-answer sample cannot gate 50,000 answers; it calibrates the judge, it does not replace it.
- D. Launch without evaluation and rely on user feedback
  > User feedback is post-harm and cannot prevent a bad launch.

**Why A is correct:** LLM-as-a-judge evaluation scores correctness, completeness, and faithfulness at 50,000-answer scale where humans cannot go. The trust guardrail is calibration: a human-reviewed sample validates the judge's agreement rate before the gate is trusted, combining scale with verified judgment quality.

**The trap AWS set here:** Calibration, not replacement. The exam wants the judge for scale plus humans for trust, not either extreme alone.

:::

:::pq {#q-d5-003}

*D5 · MEDIUM · ONE ANSWER* — q-d5-003 · 5.1 Human eval

**Q128.** A luxury brand must verify that generated copy matches its distinctive voice before launch: subtle, understated, never slangy. Automated metrics keep passing copy that the brand team rejects. Which evaluation method fits, and how should it be staffed at reasonable cost?

- A. Human evaluation on a representative sample, staffed by the brand team or an AWS-managed evaluation team <!-- correct -->
- B. Programmatic metrics tuned until they pass
  > Tuning metrics to pass is grading your own homework; metrics cannot judge subtle voice.
- C. LLM-as-a-judge alone for the voice check
  > Judge models approximate taste but miss the subtle distinctions the brand team already catches them missing.
- D. Skip pre-launch evaluation and A/B test in production
  > Shipping off-brand copy to luxury customers to "test" it risks brand damage.

**Why A is correct:** Brand voice is subjective judgment that programmatic metrics and even LLM judges handle poorly when the bar is this subtle; human evaluation by the brand team (or an AWS-managed human team) is the correct method. The cost control is sampling: humans judge a representative set deeply rather than everything shallowly.

**The trap AWS set here:** Subjective bar, subjective judge. When automated metrics pass what experts reject, the metric is wrong, not the experts.

:::

:::pq {#q-d5-004}

*D5 · MEDIUM · SELECT 2* — q-d5-004 · 5.1 RAG eval

**Q129.** A team evaluates a RAG system before launch. Which TWO dimensions must the evaluation cover? (Select TWO)

- A. Retrieval relevance: do the retrieved chunks actually answer the query <!-- correct -->
- B. Generation faithfulness: is the answer supported by the retrieved chunks <!-- correct -->
- C. Model parameter count
  > Parameter count does not measure retrieval or faithfulness.
- D. Prompt length in tokens
  > Prompt length is an input detail, not a quality dimension.
- E. The color scheme of the UI
  > UI styling is unrelated to RAG correctness.

**Why A, B is correct:** RAG evaluation is two-sided by construction: the retriever must return relevant chunks and the generator must stay faithful to them. A system can fail on either side independently, so both need measurement, typically LLM-as-a-judge powered.

**The trap AWS set here:** evaluating only generation. RAG fails on the retrieval side just as often.

:::

:::pq {#q-d5-005}

*D5 · MEDIUM · ONE ANSWER* — q-d5-005 · 5.1 Regression

**Q130.** A team ships a new prompt version weekly. What prevents silent quality regressions?

- A. Regression testing on every prompt and model change, plus canary deployments <!-- correct -->
- B. Shipping directly to 100% of traffic for fast feedback
  > Full-traffic shipping turns every regression into a full outage.
- C. Testing once at initial launch
  > Launch-only testing cannot catch regressions introduced by later changes.
- D. Longer prompts
  > Prompt length is unrelated to regression safety.

**Why A is correct:** Regression suites rerun golden evaluations on every change to catch drift, and canary deployments limit blast radius so a bad version affects a fraction of traffic first. Change-gated quality is the deployment-validation answer.

**The trap AWS set here:** launch-only testing. Quality gates must run on every change.

:::

:::pq {#q-d5-006}

*D5 · MEDIUM · SELECT 2* — q-d5-006 · 5.1 Combined eval

**Q131.** A team compares two models for customer-support answers, judging both factual correctness and empathy of tone. Which TWO methods together cover this? (Select TWO)

- A. LLM-as-a-judge for correctness at scale across thousands of answers <!-- correct -->
- B. Human evaluation for empathy and tone, which are subjective <!-- correct -->
- C. Programmatic metrics alone for both dimensions
  > Programmatic metrics cannot judge empathy or tone.
- D. No evaluation; trust the benchmark scores
  > Published benchmarks do not measure your task or your tone.
- E. A single engineer's gut feeling
  > One opinion is not an evaluation methodology.

**Why A, B is correct:** Correctness at scale is the judge's job (thousands of answers graded consistently), while empathy is subjective and belongs to human evaluators. The split matches each method to its strength.

**The trap AWS set here:** one method for both dimensions. Objective scale and subjective taste need different tools.

:::

:::pq {#q-d5-007}

*D5 · HARD · ONE ANSWER* — q-d5-007 · 5.1 BYOI

**Q132.** A company evaluates a third-party model's answers and also wants to score its full application's end-to-end responses (which mix model output with business logic). Which evaluation capability supports this?

- A. Bring-your-own-inference: evaluate any model or full system responses, not just Bedrock invocations <!-- correct -->
- B. Programmatic evaluation limited to Bedrock models
  > Bedrock-only programmatic eval cannot see the third-party model or the app layer.
- C. Human evaluation only
  > Human-only evaluation cannot scale to regression suites.
- D. Disabling evaluation for third-party models
  > Disabling evaluation abandons quality control where it is needed most.

**Why A is correct:** Bring-your-own-inference decouples evaluation from the inference source: you supply the responses (any model, full application output) and the evaluation harness scores them. That covers third-party models and end-to-end app responses alike.

**The trap AWS set here:** assuming evaluation only works on Bedrock-hosted models. BYOI evaluates anything.

:::

:::pq {#q-d5-008}

*D5 · MEDIUM · ONE ANSWER* — q-d5-008 · 5.1 Subjective metrics

**Q133.** A developer proposes using programmatic exact-match metrics to evaluate whether marketing copy matches the brand voice. Why is this wrong?

- A. Brand voice is subjective; exact-match metrics cannot judge style, so human or LLM-as-a-judge evaluation is needed <!-- correct -->
- B. Programmatic metrics are always wrong
  > Programmatic metrics are right for objective measures like accuracy; the objection is specific to subjective style.
- C. Brand voice cannot be evaluated at all
  > Voice is evaluable, just not by string equality.
- D. Exact-match is too expensive
  > Exact-match is cheap; cheap and wrong is still wrong.

**Why A is correct:** Exact-match compares strings for equality; brand voice is about tone, rhythm, and word choice, where many different strings are equally good. Subjective metrics need judgment-based methods.

**The trap AWS set here:** The trap AWS set here is the proposal itself: exact-match for style. Match the metric family to the quality type.

:::

:::pq {#q-d5-009}

*D5 · MEDIUM · ONE ANSWER* — q-d5-009 · 5.2 ValidationException

**Q134.** A team migrates a working InvokeModel integration from Titan to Claude, keeping the same call structure with a new model ID. Calls fail with ValidationException. Model access and IAM permissions are verified working, and the same code works against Titan in the same region. What is the most likely cause?

- A. The request body uses Titan schema; Claude requires anthropic_version and max_tokens <!-- correct -->
- B. The IAM role lacks Claude permissions
  > Permissions are verified working; re-checking a ruled-out cause wastes the debugging step.
- C. Claude is not available in the region
  > Region unavailability surfaces as AccessDeniedException, not ValidationException, and Titan works in the same region.
- D. The application needs a quota increase
  > Quota exhaustion throttles; it does not produce ValidationException.

**Why A is correct:** InvokeModel request bodies are provider-specific: Claude requires anthropic_version (bedrock-2023-05-31) and max_tokens, which the Titan-shaped body lacks. "Works on Titan, fails on Claude, same region, permissions verified" isolates the variable to the body format, which is the first thing to check per the GenAI debug order (request validation before permissions).

**The trap AWS set here:** Error-code literacy. ValidationException means malformed request; the exam pairs it with verified permissions to force the body-format diagnosis.

:::

:::pq {#q-d5-010}

*D5 · EASY · ONE ANSWER* — q-d5-010 · 5.2 AccessDenied region

**Q135.** An application gets AccessDeniedException calling a model that works fine in another region. Permissions are identical. What is the most likely cause?

- A. The model is not available in this region; the error message is misleading <!-- correct -->
- B. The IAM policy has a typo
  > A typo would fail in every region, not just this one.
- C. The application needs a VPN
  > Network paths do not produce authorization-shaped errors.
- D. The model was deleted globally
  > Global deletion would break the working region too.

**Why A is correct:** Bedrock returns a misleading AccessDeniedException when a model ID is not available in the calling region. Identical permissions working elsewhere is the tell: availability, not authorization, is the problem.

**The trap AWS set here:** trusting the error name. On Bedrock, AccessDenied can mean not available here.

:::

:::pq {#q-d5-011}

*D5 · MEDIUM · ONE ANSWER* — q-d5-011 · 5.2 Prepare agent

**Q136.** A developer adds a new action group to a Bedrock Agent and tests the draft in the console: the agent never calls the new tool. The agent was not prepared after the change, and production traffic runs on an alias. What is the fix, and why did the console test mislead?

- A. Run prepare-agent to create a new version, then point the alias at it; the console tests DRAFT, not the alias version <!-- correct -->
- B. Delete and recreate the action group
  > Recreating without preparing leaves the same DRAFT-only state.
- C. Increase the agent idle timeout
  > Timeouts do not affect tool availability; this misdiagnoses a versioning problem as a performance one.
- D. Wait for the configuration to propagate
  > There is no propagation delay; preparation is an explicit required step.

**Why A is correct:** The agent must be prepared after configuration changes (DRAFT to PREPARED), and the alias must point at the new prepared version; the console tests DRAFT, which is why the new tool seemed present there while alias traffic never saw it. "Prepare, version, retarget alias" is the complete fix sequence.

**The trap AWS set here:** Console versus alias. The console tests DRAFT, so it shows the tool working while production on the alias never gets it.

:::

:::pq {#q-d5-012}

*D5 · MEDIUM · ONE ANSWER* — q-d5-012 · 5.2 Debug order

**Q137.** After a knowledge base re-sync, answers get worse: confident but wrong, on topics that worked before. What should the developer check FIRST?

- A. Retrieval quality: chunking, embeddings, and relevance, before touching the generation model or temperature <!-- correct -->
- B. Switch to a larger generation model immediately
  > A larger model amplifies the same bad retrieval more fluently.
- C. Raise the temperature for more creative answers
  > Higher temperature increases fabrication on factual content.
- D. Rewrite all the system prompts
  > Prompt rewrites do not fix chunks that changed at ingestion.

**Why A is correct:** The GenAI debug order starts at retrieval for RAG failures: re-syncs can change chunking or embeddings, and confident-but-wrong is the signature of broken retrieval feeding a fluent generator. Generation changes come only after retrieval is ruled out.

**The trap AWS set here:** debugging retrieval failures at the generation layer. Retrieval first, always.

:::

:::pq {#q-d5-013}

*D5 · HARD · ONE ANSWER* — q-d5-013 · 5.2 Context overflow

**Q138.** An application stuffs entire 200-page PDFs into prompts. Recently, requests fail or answers ignore the document's later sections. What is the most correct remediation?

- A. Fix content handling: apply a chunking strategy with retrieval instead of whole-document stuffing, add prompt compression, and analyze truncation <!-- correct -->
- B. Buy a model with a bigger context window and keep stuffing
  > A bigger window delays the problem and multiplies cost; the pattern is still broken.
- C. Split the PDF randomly into halves
  > Random halves still overflow and destroy document structure.
- D. Set temperature to zero
  > Temperature affects randomness, not context limits.

**Why A is correct:** The debug order's first step is content handling: context overflow causes silent truncation (later sections vanish) or failures. Chunking plus retrieval feeds the model only relevant sections, compression trims waste, and truncation analysis confirms what was actually sent.

**The trap AWS set here:** bigger context as the fix. Overflow is a content-handling problem, solved with retrieval and compression.

:::

:::pq {#q-d5-014}

*D5 · MEDIUM · SELECT 2* — q-d5-014 · 5.2 Prompt regression

**Q139.** After switching to a new model version, several prompts behave differently. Which TWO steps diagnose this systematically? (Select TWO)

- A. Compare prompt versions in Prompt Management to isolate what changed <!-- correct -->
- B. Run the regression test suite over golden datasets to quantify the behavior shift <!-- correct -->
- C. Raise the temperature to smooth out differences
  > Temperature changes randomness; it cannot diagnose a model-version behavior shift.
- D. Delete the old prompt versions
  > Deleting old versions destroys the baseline needed for comparison.
- E. Blame the users' phrasing
  > User phrasing did not change; the model version did.

**Why A, B is correct:** Systematic diagnosis means isolating the change (version comparison shows exactly what moved) and measuring its impact (regression suites quantify the shift on golden data). Both are evidence-based; everything else is guessing.

**The trap AWS set here:** tuning randomness instead of measuring. Diagnose with versions and regression data.

:::

:::pq {#q-d5-015}

*D5 · HARD · ONE ANSWER* — q-d5-015 · 5.2 Capacity vs routing

**Q140.** An application correctly invokes its provisioned model ARN, but still throttles when traffic hits 3x the baseline the Provisioned Throughput was sized for. What is the most correct fix?

- A. Increase Provisioned Throughput model units for the higher baseline, or add on-demand overflow for peaks <!-- correct -->
- B. Check whether the code uses the base model ID
  > The stem states the ARN is already correct; re-checking routing wastes the debugging step.
- C. Decrease the temperature
  > Temperature does not affect throttling.
- D. Switch to batch inference
  > Batch inference cannot serve real-time peak traffic.

**Why A is correct:** This is the mirror image of the routing bug: routing is correct this time, so capacity genuinely is the constraint. The fix is more units for a higher sustained baseline, or hybrid on-demand overflow for peaks. Rule out routing first, then size capacity to load.

**The trap AWS set here:** assuming every PT throttle is the routing bug. Routing is ruled out here, so capacity is the real fix.

:::

## Bonus Professional-Bar Practice Questions (52 questions, Q141-Q192) {#bonus}

:::panel

**How to use these.** The 140-question bank above is weighted like the real exam. These 52 bonus questions are calibrated one notch harder: longer multi-constraint stems, plausible-but-wrong distractors, and the traps AWS actually sets. Work them after the main bank. Generic content only.

:::

**Domain 1: Foundation Model Integration, Data Management, and Compliance** (Q141-Q156)

:::pq {#q-d1-201}

*D1 · HARD · ONE ANSWER* — q-d1-201 · 1.5 Hierarchical chunking

**Q141.** A RAG assistant answers questions from 500-page technical manuals. Retrieval returns chunks that look relevant, but answers cite wrong specification values, especially from tables that span pages. Fixed-size chunking splits tables across chunks, and the team is debating semantic chunking. Which chunking strategy should they choose, and what parent-child structure addresses the table problem?

- A. Hierarchical chunking: small child chunks for matching, larger parent chunks preserving table context <!-- correct -->
- B. Semantic chunking for the highest quality splits
  > Semantic chunking avoids bad splits but is the most expensive ingestion option and less predictable than hierarchical for structured manuals.
- C. Larger fixed-size chunks with more overlap
  > Bigger fixed chunks still split tables at arbitrary boundaries; overlap papers over the problem without fixing it.
- D. Switch the generation model to a larger one
  > The failure is in retrieval (broken tables), not generation; a bigger model cannot recover split table values.

**Why A is correct:** Hierarchical chunking with small child chunks for precise matching and larger parent chunks for context keeps tables intact within parent boundaries while the child chunks give the retriever precise targets. Semantic chunking would also avoid mid-table splits but costs more at ingestion and is less predictable; fixed-size is the current failure. The parent-child structure is the exam's preferred answer for structured documents.

**The trap AWS set here:** Retrieval versus generation. The wrong values come from broken chunks, so changing the model is the classic misdiagnosis.

:::

:::pq {#q-d1-202}

*D1 · MEDIUM · ONE ANSWER* — q-d1-202 · 1.5 Embedding selection

**Q142.** A knowledge base must support semantic search over 8 million support articles in English and Spanish, with 200 ms p99 retrieval latency. The team must choose between Titan Text Embeddings v2 at 1024 dimensions and Cohere Embed multilingual at lower dimensions. Storage budget is tight. What is the most correct selection process?

- A. Choose the multilingual-optimized embedding model for the language requirement, then benchmark smaller dimensions against a golden set for the storage and latency constraints <!-- correct -->
- B. Default to Titan v2 at 1024 dimensions for maximum quality
  > This ignores both the Spanish requirement and the storage budget; defaults are not decisions.
- C. Use two separate embedding models, one per language
  > Two pipelines double operations and cannot do cross-language matching.
- D. Pick the cheapest embedding option without benchmarking
  > Unmeasured quality risk on 8 million articles violates the retrieval-quality requirement.

**Why A is correct:** The multilingual requirement points to Cohere Embed (multilingual-optimized with input_type for query versus document asymmetry), and the tight storage budget plus latency SLA point to benchmarking smaller dimensions against a golden set rather than defaulting to 1024. The exam wants constraint-driven selection: language coverage first, then measured dimension trade-off, not a default pick.

**The trap AWS set here:** Default-model bias plus dimension absolutism. Both the model default and the 1024 default must be overridden by scenario constraints.

:::

:::pq {#q-d1-203}

*D1 · HARD · ONE ANSWER* — q-d1-203 · 1.5 Hybrid search + rerank

**Q143.** A legal research assistant retrieves passages that match keywords but miss the actual answer: queries use precise statutory citations like "Section 230(c)(1)" that vector search paraphrases away, while pure keyword search misses semantically related clauses. The team tried query expansion with the foundation model and saw little gain. Which retrieval change most directly fixes this?

- A. Hybrid search combining vector and keyword retrieval, with a rerank model reordering the merged results <!-- correct -->
- B. More aggressive query expansion with a larger model
  > Expansion helps vague queries; it cannot recover exact statutory citations that vector search already paraphrased away.
- C. A larger embedding model with more dimensions
  > Bigger vectors improve semantic matching but still miss exact-match citation strings.
- D. A custom Lambda that merges keyword and vector results with hand-tuned weights
  > Hand-tuned merging is operational overhead; the managed reranker does this with less custom code.

**Why A is correct:** Hybrid search (vector plus keyword) captures both the exact citation strings and the semantic relationships, and a reranker reorders the merged candidates by true relevance. Query expansion helps vague queries, not precise citations; pure vector search is the current failure. The exam's triad for terminology-heavy corpora is hybrid search then rerank, not more expansion.

**The trap AWS set here:** More of the failing approach. The exam offers a bigger version of what already failed (expansion, embeddings) instead of the architectural change (hybrid plus rerank).

:::

:::pq {#q-d1-204}

*D1 · MEDIUM · ONE ANSWER* — q-d1-204 · 1.5 Query decomposition

**Q144.** Users ask multi-hop questions like "Which of our suppliers had a price increase after the Q2 contract renewal and also ships to the EU?" Single-vector retrieval returns passages about only one clause of the question. Which query-handling step should the developer add before retrieval?

- A. Decompose the question into sub-questions with a Lambda step, retrieve per sub-question, then synthesize <!-- correct -->
- B. Increase the number of retrieved chunks for the full question
  > More chunks of the same poorly-matched retrieval adds noise, not the missing hops.
- C. Ask the model to answer from its training knowledge
  > Training knowledge is stale and ungrounded for supplier-specific facts; this abandons RAG.
- D. Add a reranker after retrieval
  > Reranking reorders bad candidates; it cannot create the missing per-hop retrieval.

**Why A is correct:** Query decomposition breaks the multi-hop question into sub-questions (supplier price increases post-Q2; EU shipping suppliers), retrieves for each, then synthesizes. Single-vector retrieval embeds the whole compound question into one vector that matches no single passage well. Decomposition is the managed pattern for multi-hop; it happens before retrieval, not after.

**The trap AWS set here:** Post-retrieval fixes for a pre-retrieval problem. Rerank and top-k tune the candidate set; decomposition changes what is retrieved.

:::

:::pq {#q-d1-205}

*D1 · MEDIUM · ONE ANSWER* — q-d1-205 · 1.1 Grounding ladder

**Q145.** A vendor proposes fine-tuning a foundation model on the company's 2,000-page returns policy so the chatbot "knows" the policy. The policy changes every quarter, and every answer must cite the exact policy section. What is wrong with the proposal, and what should the developer do instead?

- A. Reject fine-tuning: use RAG with quarterly re-syncs so answers cite current policy sections <!-- correct -->
- B. Accept fine-tuning and retrain every quarter
  > Quarterly retraining is expensive and still cannot produce auditable section citations.
- C. Fine-tune once and prompt the model to cite sections
  > Citations from weights are unverifiable; the model will hallucinate plausible section numbers.
- D. Use prompt engineering with the full policy in context
  > A 2,000-page policy exceeds practical context windows and wastes tokens on every call.

**Why A is correct:** Fine-tuning bakes knowledge into weights that go stale every quarter and cannot produce verifiable section citations; this is a grounding problem, not a behavior problem. RAG over the policy documents gives current-version answers with citations, and re-syncing each quarter is trivial compared to retraining. The exam's ladder rule is quarterly-changing plus citations equals RAG, never fine-tuning.

**The trap AWS set here:** Fine-tuning for knowledge. The exam's most repeated ladder trap: training weights where retrieval is the answer.

:::

:::pq {#q-d1-206}

*D1 · HARD · SELECT 2* — q-d1-206 · 1.4 Vector store trade-offs

**Q146.** A startup runs similarity search over 100 million product embeddings. Queries run a few hundred times per day, latency tolerance is 2 seconds, and the burn rate is critical. A solutions architect proposes OpenSearch Serverless; the CTO asks for the cheapest correct option. Which TWO statements are true? (Select TWO)

- A. S3 Vectors is the most cost-effective choice for infrequent large-scale search <!-- correct -->
- B. OpenSearch Serverless is optimized for frequent low-latency queries, which this workload does not need <!-- correct -->
- C. ElastiCache should back the vector store for durability
  > ElastiCache is an ephemeral cache, not a durable vector store.
- D. DynamoDB can serve as the vector index
  > DynamoDB is not a vector index; it holds metadata, not embeddings.
- E. A self-hosted vector database on EC2 is cheapest
  > Self-hosting trades the managed bill for engineering time the startup does not have.

**Why A, B is correct:** S3 Vectors is the cost-optimized choice for large-scale infrequent search: it removes the always-on cluster cost that dominates at a few hundred queries per day, and 2-second tolerance fits its profile. OpenSearch Serverless is built for frequent low-latency querying and would bill for capacity the workload never uses.

**The trap AWS set here:** Cluster cost for idle workloads. The exam tests whether the vector store matches the query frequency, not just the data size.

:::

:::pq {#q-d1-207}

*D1 · MEDIUM · ONE ANSWER* — q-d1-207 · 1.5 Custom chunking

**Q147.** A knowledge base ingests research papers with embedded figures, equations, and tables. Standard chunking mangles the equations and splits figure captions from their figures. The team needs chunk boundaries that respect document structure. Which approach should they use?

- A. Custom chunking with a Lambda function implementing structure-aware boundaries <!-- correct -->
- B. Hierarchical chunking with default settings
  > Hierarchical chunking handles prose context, not equations or figure-caption pairing.
- C. Semantic chunking for meaning-based splits
  > Meaning boundaries do not preserve document structure like equations and captions.
- D. Pre-chunk the papers manually before ingestion
  > Manual chunking does not scale and cannot be maintained as papers are added.

**Why A is correct:** Custom chunking via Lambda lets the team define structure-aware boundaries (keep equations intact, keep captions with figures) that no fixed strategy provides. Hierarchical chunking helps long structured prose but does not understand equations or figure-caption pairing; semantic chunking splits on meaning boundaries, not document structure.

**The trap AWS set here:** Strategy shopping. The exam offers the standard strategies where only a custom structure-aware one fits.

:::

:::pq {#q-d1-208}

*D1 · HARD · ONE ANSWER* — q-d1-208 · 1.2 Model customization ladder

**Q148.** A company has three needs: (1) support summaries must always follow a strict 4-step format in the company voice, at 3 million replies per month where token cost dominates; (2) the model must understand proprietary internal jargon that appears in no public corpus; (3) a classifier must sort tickets into 40 categories at minimal cost per ticket. Which customization mapping is most correct?

- A. Distill a small model for the classifier and the fixed-format replies; continued pre-training for the proprietary jargon <!-- correct -->
- B. Fine-tune the flagship model separately for all three needs
  > Three full fine-tunes maximize cost; the classifier and fixed format need small cheap models, not flagship fine-tunes.
- C. Use RAG for all three needs
  > RAG grounds facts; it does not bake in format behavior or cut per-ticket inference cost.
- D. Use prompt engineering alone for all three
  > Prompting cannot match distillation economics at 3 million replies per month or teach truly novel jargon reliably.

**Why A is correct:** This is the customization ladder applied three times: (3) the high-volume narrow classifier is a distillation target (small model matching the large one on the narrow task, cheapest per ticket); (2) genuinely new domain knowledge baked into weights is continued pre-training; (1) the strict format at 3M replies per month is also a distillation or fine-tuning play because per-token cost dominates, not RAG (the format never changes, so retrieval adds nothing). Fine-tuning everything is the expensive overkill answer.

**The trap AWS set here:** One tool for three jobs. Each need sits at a different rung of the customization ladder; the exam punishes single-mechanism answers.

:::

:::pq {#q-d1-209}

*D1 · MEDIUM · ONE ANSWER* — q-d1-209 · 1.3 BDA blueprints

**Q149.** A logistics company processes 30,000 invoices per day in 40 different layouts. They need specific fields (invoice number, line items, tax totals) extracted into a fixed schema, with new layouts onboarded without code changes. Which Bedrock Data Automation feature addresses the fixed-schema requirement?

- A. Custom blueprints defining the invoice schema, applied across layouts without code changes <!-- correct -->
- B. Standard output with post-processing in Lambda to fit the schema
  > Post-processing reintroduces the per-layout custom code the scenario rules out.
- C. Bedrock Guardrails to validate the extracted fields
  > Guardrails screen content for safety; they do not define extraction schemas.
- D. A knowledge base over the invoices with natural-language queries
  > A KB answers questions; it does not produce 30,000 schema-conformant records per day.

**Why A is correct:** BDA custom blueprints define the exact output schema (fields, types) so extraction conforms to the fixed invoice schema across all 40 layouts, and new layouts are onboarded as blueprint configuration, not code. Standard output gives generic extraction without the fixed schema; Textract plus Lambda would hand-build the schema mapping per layout.

**The trap AWS set here:** Standard versus blueprint output. "Fixed schema" is the blueprint trigger; standard output is the generic-extraction distractor.

:::

:::pq {#q-d1-210}

*D1 · MEDIUM · SELECT 2* — q-d1-210 · 1.4 Filtered retrieval

**Q150.** A support assistant serves three regions. Articles are tagged by region and product line in S3 metadata. Requirements: EU callers must only retrieve EU articles, and the product-line filter must apply before the vector search runs to keep latency down. Which TWO design choices meet both requirements? (Select TWO)

- A. Filter retrieval by the region metadata attribute so EU callers only see EU articles <!-- correct -->
- B. Apply the product-line metadata filter before vector search to scope the candidate set <!-- correct -->
- C. Retrieve broadly and filter articles in the application after generation
  > Post-generation filtering wastes retrieval and risks leaking content into the model context.
- D. Maintain three separate embedding models, one per region
  > The boundary is a metadata filter, not a model boundary; three models triple cost for nothing.
- E. Ask the model to only use EU articles via the system prompt
  > Prompt instructions are not access control and are invisible to the retrieval layer.

**Why A, B is correct:** Metadata filtering on the region and product-line attributes enforces the EU-only boundary at retrieval time, and applying the filter pre-retrieval (as a search filter, not post-processing) keeps the vector search scoped and fast. Post-filtering retrieved chunks wastes the vector search on disallowed content and adds latency.

**The trap AWS set here:** Filter placement. Pre-retrieval filtering is both the security boundary and the latency optimization; post-filtering is neither.

:::

:::pq {#q-d1-211}

*D1 · HARD · ONE ANSWER* — q-d1-211 · 1.2 Routing mechanisms

**Q151.** An application has three routing needs: (1) survive a regional outage of the model automatically; (2) send simple queries to a cheap model and hard queries to the flagship without custom code; (3) guarantee throughput for a steady 5M-token-per-day baseline. A developer proposes one mechanism for all three. Why is this wrong, and what is the correct mapping?

- A. Cross-region inference for outage survival, intelligent prompt routing for complexity-based cost routing, Provisioned Throughput for the steady baseline <!-- correct -->
- B. Provisioned Throughput for all three needs
  > PT reserves capacity; it does not route across regions or by prompt complexity.
- C. Intelligent prompt routing for all three needs
  > Prompt routers optimize cost versus quality; they do not provide regional failover or reserved capacity.
- D. Cross-region inference profiles for all three needs
  > Profiles provide availability routing; they do not do complexity routing or capacity reservation.

**Why A is correct:** These are three different mechanisms: (1) cross-region inference profiles route for availability across regions; (2) intelligent prompt routing (model routers) route by prompt complexity for cost versus quality; (3) Provisioned Throughput reserves capacity for the steady baseline. No single mechanism does all three; the exam's favorite confusion set is exactly these three names, and the scenario assigns one job to each.

**The trap AWS set here:** The three-router confusion set. The exam names all three mechanisms in one scenario and demands one job per mechanism.

:::

:::pq {#q-d1-212}

*D1 · MEDIUM · ONE ANSWER* — q-d1-212 · 1.2 Runtime model switching

**Q152.** Operations must switch the production application between Claude and Llama without code deployments, and they want to canary the switch to 5% of traffic first. The application front door is API Gateway with Lambda handlers. Which combination enables no-deploy switching with canary control?

- A. AppConfig for the model identifier as runtime configuration plus traffic splitting in the Lambda routing for the 5% canary <!-- correct -->
- B. CloudFormation parameters updated per switch
  > CloudFormation updates are deployments, violating the no-deploy requirement.
- C. EventBridge rules to select the model
  > EventBridge routes events; it does not store configuration or split traffic by percentage.
- D. Hardcode both model IDs and redeploy for each switch
  > This is the current pain the scenario asks to eliminate.

**Why A is correct:** AppConfig holds the model identifier as runtime configuration the Lambda reads per request (no redeploy), and API Gateway or the Lambda routing logic splits 5% of traffic to the new model for the canary. CloudFormation changes are deployments, and EventBridge routes events rather than holding configuration.

**The trap AWS set here:** Configuration versus deployment. The exam offers CloudFormation where runtime configuration is required.

:::

:::pq {#q-d1-213}

*D1 · MEDIUM · ONE ANSWER* — q-d1-213 · 1.1 GenAI Lens

**Q153.** A platform team wants every product squad to build GenAI features in a consistent, reviewable way: standard components for prompts, model routing, guardrails, and evaluation, with design reviews before production. Which framework should anchor the review standard?

- A. The Well-Architected Framework Generative AI Lens as the design-review and component standard <!-- correct -->
- B. Each squad defines its own review checklist
  > Squad-local checklists defeat the consistency requirement.
- C. The standard Well-Architected Framework with no GenAI content
  > The base framework lacks the GenAI-specific guidance (model selection, grounding, evaluation) the scenario needs.
- D. SOC 2 compliance checklists as the design standard
  > SOC 2 audits controls; it does not standardize GenAI architecture components.

**Why A is correct:** The AWS Well-Architected Framework Generative AI Lens is the exam-named standard for GenAI design reviews and standardized components across deployments. It applies the Well-Architected pillars to GenAI specifically (responsible AI, data, model selection, cost, security), which is what "consistent, reviewable" demands.

**The trap AWS set here:** Generic versus GenAI-specific. The base Well-Architected Framework is close but misses the GenAI Lens the exam names.

:::

:::pq {#q-d1-214}

*D1 · MEDIUM · ONE ANSWER* — q-d1-214 · 1.4 Web crawler source

**Q154.** A competitive-intelligence assistant must track 200 competitor documentation sites, re-crawling weekly for changes, with changed pages re-ingested automatically. The team will not build or operate a crawler. Which knowledge base data-source option fits?

- A. A web-crawler data source with a weekly crawl schedule and automatic change ingestion <!-- correct -->
- B. A custom crawler writing to S3 with a manual ingestion trigger
  > This rebuilds crawling and scheduling by hand, violating the no-operate constraint.
- C. One-time ingestion of the current site contents
  > One-time ingestion goes stale within a week; the requirement is continuous tracking.
- D. Amazon Kendra web crawler with generation added in Lambda
  > Kendra crawls for search, but the scenario needs RAG ingestion; bolting generation onto Kendra rebuilds the KB.

**Why A is correct:** Knowledge Bases support web-crawler data sources with scheduled re-crawls and automatic re-ingestion of changed pages, which is the managed answer for "track sites weekly with no crawler to operate." A hand-built crawler plus S3 upload pipeline is the operational-overhead alternative the scenario rules out.

**The trap AWS set here:** Build versus managed crawl. The weekly-change requirement tempts a custom crawler; the managed data source already does it.

:::

:::pq {#q-d1-215}

*D1 · HARD · ONE ANSWER* — q-d1-215 · 1.2 CRI data residency

**Q155.** A team in Frankfurt adopts a cross-region inference profile for resilience. Security asks two questions: which region's quotas are consumed, and can prompt data be processed outside the EU? The team assumes quotas are split across destination regions and data never leaves Frankfurt. Which corrections are needed?

- A. Quotas are consumed in the source region, and routed requests are processed in destination regions, so EU scoping must be explicit <!-- correct -->
- B. Quotas are split evenly across destination regions and data stays in Frankfurt
  > Both claims are wrong: quotas stay at the source, and routing moves processing to destinations.
- C. No quotas apply to cross-region inference
  > Quotas always apply; they are simply accounted at the source region.
- D. Cross-region inference requires a VPC endpoint in each destination region
  > VPC endpoints are per-VPC for private access; they are not a per-destination-region CRI requirement.

**Why A is correct:** Quotas are consumed in the source region (where the profile lives), not split across destinations, and cross-region routing by design processes requests in other regions, so data does leave Frankfurt unless the profile is scoped accordingly. Both team assumptions are wrong; the exam tests the two most misunderstood CRI facts together.

**The trap AWS set here:** Double misconception. The exam bundles the two most common CRI misunderstandings (quota location, data movement) into one question.

:::

:::pq {#q-d1-216}

*D1 · MEDIUM · ONE ANSWER* — q-d1-216 · 1.4 Grounding evaluation

**Q156.** A regulated RAG deployment must prove before launch that answers stay faithful to retrieved sources, with a numeric score per answer the auditors can sample. Which evaluation approach provides this, and which metric does it use?

- A. LLM-as-a-judge faithfulness scoring of each answer against its retrieved sources <!-- correct -->
- B. Programmatic exact-match against reference answers
  > Exact match cannot measure whether free-text answers stay faithful to sources.
- C. Human review of every answer before launch
  > Humans cannot score production volumes; sampling calibrates the automated gate.
- D. A Bedrock Guardrail grounding threshold as the evaluation
  > Guardrails enforce at inference time; they do not produce auditable per-answer evaluation scores.

**Why A is correct:** Contextual-grounding evaluation (LLM-as-a-judge scoring faithfulness or groundedness of each answer against its retrieved sources) produces the per-answer numeric score auditors can sample. Programmatic exact-match cannot score free-text faithfulness, and human review cannot cover the volume needed for a launch gate.

**The trap AWS set here:** Enforcement versus evaluation. Guardrails act at runtime; auditors need measured scores, which is an evaluation job.

:::

**Domain 2: Implementation and Integration** (Q157-Q169)

:::pq {#q-d2-201}

*D2 · HARD · ONE ANSWER* — q-d2-201 · 2.1 Multi-agent topology

**Q157.** A healthcare assistant must serve four departments (clinical, insurance, scheduling, claims) with domain-specific answers, onboard new departments without redesign, and handle thousands of parallel interactions. Each department needs its own knowledge base for data isolation. How should inter-agent communication be configured?

- A. One supervisor agent routing in natural language to specialist collaborator agents, each with its own knowledge base, each prepared and aliased <!-- correct -->
- B. A separate supervisor per department with manual handoffs between them
  > Multiple supervisors with manual handoffs is the scaling anti-pattern; one supervisor routes to many collaborators.
- C. A single general-purpose agent with action groups and rule-based routing
  > Rule-based routing inside one agent does not scale to new departments and loses per-department KB isolation.
- D. All agents sharing one knowledge base with prompt instructions for isolation
  > Shared KB plus prompt instructions destroys the per-department data isolation requirement.

**Why A is correct:** The supervisor/collaborator pattern is the managed multi-agent topology: the supervisor classifies intent in natural language and routes to specialist collaborators, each grounded on its own knowledge base and each prepared and aliased. A supervisor per department with manual handoffs is the anti-pattern; a single agent with action groups cannot scale domain isolation cleanly.

**The trap AWS set here:** Routing mechanism confusion. Action groups connect agents to tools; the supervisor/collaborator mechanism connects agents to agents.

:::

:::pq {#q-d2-202}

*D2 · MEDIUM · ONE ANSWER* — q-d2-202 · 2.1 AgentCore migration

**Q158.** A team built agents on Bedrock Agents but now wants to use an open-source agent framework of their choice while keeping AWS-managed hosting, memory, and observability. They do not want to operate the runtime themselves. Which service is the migration path, and what does it preserve?

- A. Bedrock AgentCore: host the chosen framework on managed Runtime with Memory, Gateway, and Observability <!-- correct -->
- B. Stay on Bedrock Agents and rewrite the agent in the Bedrock-native style
  > This abandons the framework-choice requirement the migration is for.
- C. Self-host the framework on ECS with hand-built memory and tracing
  > Self-hosting rebuilds the managed memory and observability the scenario wants to keep.
- D. Move agent logic into Lambda functions orchestrated by Step Functions
  > This replaces the agent framework with workflow orchestration, losing agent reasoning entirely.

**Why A is correct:** Bedrock AgentCore is the managed runtime for any-framework agents: Runtime hosts the agent code (POST /invocations), Memory provides short and long-term context, Gateway exposes MCP tools, and Observability covers traces, while the team keeps its chosen framework. Staying on Bedrock Agents would force the Bedrock-native framework; self-hosting on ECS abandons managed memory and observability.

**The trap AWS set here:** Framework freedom versus managed operations. The exam tests whether AgentCore is the bridge between the two.

:::

:::pq {#q-d2-203}

*D2 · HARD · ONE ANSWER* — q-d2-203 · 2.1 MCP auth

**Q159.** A company builds an agent that exposes user profile data through an MCP server backed by Lambda functions. Only authorized users may access the tools, the server is remote (not on the agent host), and credentials must not live in environment variables. Which combination is most correct?

- A. Lambda-hosted MCP server over Streamable HTTP behind API Gateway, with Cognito OAuth for user authorization <!-- correct -->
- B. MCP over STDIO transport with credentials in Lambda environment variables
  > STDIO is local-only, and environment variables are not a credential-management story.
- C. Direct Lambda invocation from the agent with IAM roles as the only control
  > IAM covers service auth, but the requirement is per-user authorization, which needs Cognito OAuth.
- D. Embed the user data in the agent instructions
  > Instructions are not tool access and leak data into every prompt.

**Why A is correct:** Remote MCP servers use Streamable HTTP transport (STDIO is for local processes only), fronted by API Gateway, with Cognito OAuth authorizing users and AgentCore Gateway managing tool credentials. Stuffing secrets in environment variables and using STDIO for a remote server are the two classic MCP mistakes the scenario is designed to catch.

**The trap AWS set here:** Transport versus auth. STDIO-for-remote and env-var credentials are the two MCP traps in one question.

:::

:::pq {#q-d2-204}

*D2 · MEDIUM · ONE ANSWER* — q-d2-204 · 2.4 Converse vs InvokeModel

**Q160.** An application needs three things from Bedrock: chat completions with tool use across Claude and Llama with one code path, text embeddings for its vector store, and one Anthropic-specific sampling parameter on the Claude calls. Which API mapping is correct?

- A. Converse for chat and tool use with additionalModelRequestFields for the Anthropic parameter; InvokeModel for embeddings <!-- correct -->
- B. Converse for everything including embeddings
  > Converse cannot generate embeddings; this is the documented exception.
- C. InvokeModel with separate provider bodies for everything
  > This abandons the one-code-path requirement for chat for no reason.
- D. Comprehend for embeddings and Converse for chat
  > Comprehend does not produce embedding vectors for vector stores.

**Why A is correct:** Converse covers the unified chat-plus-tool-use path (with additionalModelRequestFields for the Anthropic-specific parameter), and InvokeModel covers the embeddings (Converse is text-generation only). This is the API decision matrix in one scenario: unified chat goes to Converse, embeddings always go to InvokeModel, provider extras go through the escape hatch.

**The trap AWS set here:** Matrix completion. Each of the three needs maps to a different API rule; one wrong mapping kills the option.

:::

:::pq {#q-d2-205}

*D2 · MEDIUM · ONE ANSWER* — q-d2-205 · 2.1 Agent trace

**Q161.** An agent's answers are sometimes wrong, and the team cannot tell whether the failure is in reasoning, tool selection, or tool results. They need per-step visibility into what the agent thought, which tool it chose, and what the tool returned. What should they enable?

- A. Agent tracing with enableTrace to capture reasoning, tool selection, and tool results per step <!-- correct -->
- B. Verbose CloudWatch Logs on the application
  > Application logs do not capture the agent's internal reasoning and tool-selection steps.
- C. X-Ray tracing on the Lambda functions
  > X-Ray traces service calls; it does not expose agent reasoning or tool-choice rationale.
- D. A larger model for better reasoning
  > A bigger model does not provide visibility; the requirement is diagnosis, not capability.

**Why A is correct:** Agent tracing (enableTrace on invoke_agent) emits the per-step record: the model's reasoning, the tool selected with its inputs, and the tool's outputs. This decomposes "sometimes wrong" into the exact failing step. CloudWatch Logs show the application's view, not the agent's internal steps; X-Ray traces service calls, not agent reasoning.

**The trap AWS set here:** Observability layer. Logs and X-Ray observe the plumbing; only the agent trace observes the reasoning.

:::

:::pq {#q-d2-206}

*D2 · HARD · SELECT 2* — q-d2-206 · 2.1 Human in the loop

**Q162.** An agent processes vendor payments. Policy: any payment over $10,000 needs a finance approver before execution; approvers have 4 business hours; every approval or rejection must be audited; the workflow must survive approver unavailability. Which TWO mechanisms together satisfy this? (Select TWO)

- A. Step Functions callback task token with a 4-hour timeout for the approval wait <!-- correct -->
- B. Step Functions execution history and decision logging for the audit trail <!-- correct -->
- C. A Lambda function that sleeps until approval arrives
  > Lambda caps at 15 minutes; it cannot wait 4 business hours.
- D. An agent instruction to ask finance before large payments
  > Instructions are not an enforceable gate and produce no audit record.
- E. An IAM policy denying payments over $10,000
  > A deny blocks the workflow instead of gating it through approval.

**Why A, B is correct:** Step Functions with a callback task token provides the durable multi-hour wait with a 4-hour timeout and automatic escalation, and the execution history plus decision logging provides the audit trail. The two answers are orthogonal: one is the waiting mechanism, the other is the audit mechanism. A Lambda waiter cannot span 4 hours, and prompt instructions are not enforcement.

**The trap AWS set here:** Orthogonal answers. The two correct picks solve different sub-problems (waiting versus auditing); picks that solve the same sub-problem are wrong.

:::

:::pq {#q-d2-207}

*D2 · MEDIUM · ONE ANSWER* — q-d2-207 · 2.1 Conversation memory

**Q163.** A chat application must keep multi-turn conversation context per user with millisecond reads, server-side encryption, and TTL expiry of inactive sessions. The team proposes one S3 object per conversation updated on every turn. What is wrong, and what should they use?

- A. Use DynamoDB keyed by session ID with TTL; S3 has the wrong latency and access pattern for per-turn session state <!-- correct -->
- B. Keep the S3-per-conversation design and add versioning
  > Versioning does not fix latency, TTL, or the per-turn rewrite cost.
- C. Store the conversation in the client browser
  > Client storage is untrusted, unencrypted by the service, and lost across devices.
- D. Use ElastiCache with no persistence
  > Ephemeral cache loses conversations on eviction; session state needs durability.

**Why A is correct:** DynamoDB with the session ID as the key gives millisecond reads, server-side encryption, and native TTL expiry, which matches all three requirements. S3 per-turn updates have higher latency, no native TTL, and the wrong access pattern for session state; the exam's rule is DynamoDB for session state, S3 for objects.

**The trap AWS set here:** Access pattern. S3 is for objects, DynamoDB is for millisecond key lookups; the per-turn update pattern decides it.

:::

:::pq {#q-d2-208}

*D2 · MEDIUM · ONE ANSWER* — q-d2-208 · 2.4 Streaming

**Q164.** A chat application must show tokens to the user as they are generated, minimizing perceived latency. The backend is API Gateway plus Lambda calling Bedrock. Which combination delivers token-by-token streaming to the browser?

- A. ConverseStream from Bedrock with API Gateway WebSockets pushing tokens to the browser <!-- correct -->
- B. Standard Converse calls with the client polling every 500 ms
  > Polling adds latency and request churn; streaming pushes tokens as generated.
- C. Batch inference with the client downloading the result
  > Batch inference has hours-scale latency; it cannot stream anything.
- D. Async SageMaker inference with SNS notifications
  > Async notification patterns suit long jobs, not token-by-token chat.

**Why A is correct:** ConverseStream (or InvokeModelWithResponseStream) emits tokens incrementally, and API Gateway WebSocket APIs (or chunked transfer) carry the stream to the browser; Lambda polls nothing. Client-side polling is the anti-pattern: it adds latency and request overhead instead of pushing tokens as they arrive.

**The trap AWS set here:** Polling versus pushing. The exam offers polling wherever streaming is the requirement; it never minimizes perceived latency.

:::

:::pq {#q-d2-209}

*D2 · MEDIUM · ONE ANSWER* — q-d2-209 · 2.5 Q Business vs Developer

**Q165.** A company wants two things: (1) developers get code suggestions in their IDE and automated test generation in CI; (2) employees ask questions over HR policies and benefits documents in a chat UI. A vendor proposes Amazon Q Business for both. What is wrong with the proposal?

- A. Q Developer covers the IDE and CI need; Q Business covers the HR chat need; one service cannot do both <!-- correct -->
- B. Q Business covers both needs
  > Q Business does not live in the IDE or generate tests; the developer need is unserved.
- C. Q Developer covers both needs
  > Q Developer is a coding tool, not an enterprise chat over HR documents.
- D. Bedrock Agents replace both
  > Agents are application building blocks, not managed productivity tools for these two jobs.

**Why A is correct:** Q Business is the enterprise-chat assistant over company data (need 2); Q Developer is the coding assistant with IDE integration and test generation (need 1). One service cannot do both jobs; the proposal misassigns the developer-productivity need to the enterprise-chat service. The exam swaps these names deliberately.

**The trap AWS set here:** Name-swap. The proposal assigns both jobs to one Q service; the exam tests whether you split them correctly.

:::

:::pq {#q-d2-210}

*D2 · MEDIUM · ONE ANSWER* — q-d2-210 · 2.3 Flows vs Step Functions

**Q166.** A business analyst must build a fixed three-step prompt chain (summarize ticket, classify, draft reply) with conditional branching for urgent tickets, no code. Separately, the payments team needs an approval workflow with 4-hour human waits and audit trails. Which service mapping is correct?

- A. Bedrock Flows for the no-code prompt chain; Step Functions for the approval workflow <!-- correct -->
- B. Bedrock Agents for both
  > Agents suit dynamic tool-using reasoning, not a fixed deterministic chain or a durable approval wait.
- C. Step Functions for both
  > Step Functions can do the chain but forces code on the analyst, violating the no-code requirement.
- D. Bedrock Flows for both
  > Flows lack durable multi-hour human-approval waits with task tokens.

**Why A is correct:** Bedrock Flows is the no-code visual builder for fixed prompt chains with conditional branching (the analyst's need), while Step Functions is the durable orchestration service for human-approval waits and audit (the payments need). Using agents for the fixed chain adds nondeterminism; using Flows for the 4-hour approval misses durable waits.

**The trap AWS set here:** Fixed chain versus durable wait. No-code branching points to Flows; human waits point to Step Functions.

:::

:::pq {#q-d2-211}

*D2 · MEDIUM · ONE ANSWER* — q-d2-211 · 2.3 GenAI gateway

**Q167.** Fifty engineering teams each call Bedrock directly with their own keys, prompts, and logging. Security wants centralized policy enforcement (including mandatory guardrails), finance wants cost attribution per team, and platform wants one observability view. What should the company build?

- A. A centralized GenAI gateway abstracting Bedrock with policy enforcement, per-team cost tagging, and unified logging <!-- correct -->
- B. Let teams keep direct access and audit with CloudTrail
  > CloudTrail is detective; it cannot enforce guardrails or attribute cost per team.
- C. SCPs restricting which models teams can call
  > SCPs control which models are callable, not guardrail enforcement or cost attribution.
- D. One shared IAM role for all teams
  > A shared role erases the per-team identity needed for attribution and least privilege.

**Why A is correct:** A centralized GenAI gateway (abstraction layer in front of Bedrock, typically API Gateway plus Lambda) enforces policies like mandatory guardrail identifiers in one place, tags usage per team for cost attribution, and centralizes logging. Per-team direct access cannot be governed; SCPs alone cannot validate request parameters like guardrail identifiers.

**The trap AWS set here:** Detective versus preventive. Auditing direct access detects violations; only a gateway in the path prevents them.

:::

:::pq {#q-d2-212}

*D2 · MEDIUM · ONE ANSWER* — q-d2-212 · 2.4 Batch inference API

**Q168.** A nightly process classifies 100,000 support tickets with no latency requirement beyond "by morning." The team currently fans out 100,000 on-demand calls and hits throttling. Which API change fixes both cost and throttling with the least code change?

- A. Move the workload to batch inference with S3 input and output <!-- correct -->
- B. Add exponential backoff to the on-demand fan-out
  > Backoff survives throttling but keeps the expensive real-time pricing tier.
- C. Buy Provisioned Throughput for the nightly window
  > PT commits hourly capacity; batch inference is the purpose-built cheaper tier for this shape.
- D. Shard the calls across regions
  > Sharding dodges throttling but keeps on-demand pricing and adds complexity.

**Why A is correct:** Batch inference takes the whole set as S3 input and returns S3 output asynchronously at roughly half the on-demand price, eliminating both the per-call throttling and the real-time premium. The code change is the invocation pattern, not the prompt; provisioned throughput would commit hourly capacity for a nightly job.

**The trap AWS set here:** Reliability fix versus pricing fix. Backoff and sharding address throttling; only batch inference also fixes the cost.

:::

:::pq {#q-d2-213}

*D2 · HARD · ONE ANSWER* — q-d2-213 · 2.1 Action group auth

**Q169.** An action group fronts an internal API that requires per-request OAuth tokens and returns paginated results the agent should never see raw. The developer configures the action group with a bare OpenAPI schema and no Lambda. In testing, calls fail authentication and the agent hallucinates pagination details. Which two-part fix is needed?

- A. Add a Lambda executor that injects OAuth tokens and filters pagination internals from responses <!-- correct -->
- B. Add the OAuth token to the agent instructions
  > Instructions cannot execute auth flows, and secrets in prompts leak.
- C. Increase the model context window to fit raw pagination
  > Fitting raw pages does not fix authentication and feeds the model noise.
- D. Replace the action group with a knowledge base over API docs
  > Docs describe the API; they do not execute authenticated calls.

**Why A is correct:** A Lambda executor is required for both failures: it injects the per-request OAuth token (a bare schema cannot do auth) and it strips pagination internals before returning results to the agent (so the model never sees raw page tokens to hallucinate about). The bare-schema setup fails exactly these two responsibilities.

**The trap AWS set here:** Schema-only limits. Auth injection and response shaping are the two jobs that force a Lambda executor.

:::

**Domain 3: AI Safety, Security, and Governance** (Q170-Q180)

:::pq {#q-d3-201}

*D3 · HARD · ONE ANSWER* — q-d3-201 · 3.1 Guardrail contexts

**Q170.** A fintech assistant must screen user prompts for jailbreak attempts before the model sees them, screen generated answers for account-number leakage before users see them, and apply the same policy to a fraud model that runs outside Bedrock. The team assumes guardrails only work on Bedrock model outputs via Converse. Which corrections are needed?

- A. Configure one guardrail for inputs and outputs; enforce it on the external model via ApplyGuardrail on prompts and completions <!-- correct -->
- B. Use Converse guardrailConfig for the Bedrock model and skip screening the external model
  > This leaves the fraud model unscreened, violating the same-policy requirement.
- C. Deploy two guardrails, one for inputs and one for outputs
  > One guardrail covers both directions; splitting doubles management.
- D. Screen outputs only, since prompt attacks cannot be filtered
  > Prompt-attack filtering is an input-side control; skipping it misses the jailbreak requirement.

**Why A is correct:** Guardrails apply to inputs, outputs, or both in one configuration, and the standalone ApplyGuardrail API enforces the same policy on non-Bedrock models. The team needs input screening (prompt attacks) plus output screening (PII), invoked via ApplyGuardrail on the prompt and on the completion for the external model. Both assumptions (outputs-only, Bedrock-only) are wrong.

**The trap AWS set here:** Double misconception. Inputs-and-outputs plus ApplyGuardrail-for-any-model are the two facts the scenario tests together.

:::

:::pq {#q-d3-202}

*D3 · HARD · ONE ANSWER* — q-d3-202 · 3.1 Control mapping

**Q171.** A finance assistant has four requirements: (1) refuse to give investment advice; (2) block the exact phrase of an internal project codename; (3) redact account numbers from outputs while keeping answers readable; (4) catch "ignore your instructions" jailbreak attempts in prompts. Which control mapping satisfies all four?

- A. Denied topic for investment advice; word filter for the codename; sensitive-information filter in mask mode for account numbers; prompt-attack filter on inputs <!-- correct -->
- B. Content filter for investment advice; denied topic for the codename; PII filter in block mode; output-only screening
  > Content filters score toxicity, not advice topics; block mode kills readable answers; output-only misses prompt attacks.
- C. Word filters for all four requirements
  > Word filters are exact-match; they cannot detect PII entity types or jailbreak phrasing.
- D. A single high grounding threshold for all four
  > Grounding checks faithfulness to sources; it does none of the four safety jobs.

**Why A is correct:** Each verb maps to one control: (1) subject-matter refusal is a denied topic; (2) an exact secret phrase is a word filter; (3) PII redaction preserving readability is a sensitive-information filter in mask mode; (4) jailbreak attempts are the prompt-attack content filter on inputs. Any option that swaps two of these (for example, content filter for investment advice) fails its requirement.

**The trap AWS set here:** Control-to-verb mapping. Four requirements, four controls; the exam punishes any swap.

:::

:::pq {#q-d3-203}

*D3 · MEDIUM · ONE ANSWER* — q-d3-203 · 3.1 Grounding vs reasoning

**Q172.** A refund bot must obey a deterministic rule: the refund total must equal the sum of the approved line items, always. Separately, a RAG support bot must not state facts absent from the retrieved articles. Which check belongs to each requirement?

- A. Automated Reasoning checks for the refund arithmetic; contextual grounding checks for the RAG faithfulness <!-- correct -->
- B. Contextual grounding for the refund arithmetic; Automated Reasoning for the RAG faithfulness
  > Grounding checks source support, not arithmetic; reasoning checks policy logic, not source comparison.
- C. A content filter for both
  > Content filters score toxicity categories; they verify neither arithmetic nor source faithfulness.
- D. Prompt instructions for both
  > Instructions are not verifiable enforcement for deterministic rules.

**Why A is correct:** Automated Reasoning checks verify deterministic policy rules expressed in natural language (the refund arithmetic), while contextual grounding checks verify that generated claims are supported by the retrieved source content (the RAG faithfulness requirement). Swapping them fails both: grounding cannot prove arithmetic, and reasoning checks do not compare against retrieved sources.

**The trap AWS set here:** The exam's favorite pair. Grounding is "supported by the source"; Automated Reasoning is "consistent with the policy."

:::

:::pq {#q-d3-204}

*D3 · HARD · SELECT 2* — q-d3-204 · 3.3 Org governance

**Q173.** A multi-account organization needs central control: employees must only call approved foundation models, every model call must pass through the corporate guardrail, and the guardrail policy itself must be deployed identically to all accounts. Developers keep forgetting to attach the guardrail. Which TWO mechanisms together enforce this? (Select TWO)

- A. SCPs restricting models and requiring the guardrail identifier, enforced with the bedrock:GuardrailIdentifier condition key <!-- correct -->
- B. CloudFormation StackSets deploying the identical guardrail policy to all accounts <!-- correct -->
- C. IAM permission boundaries on developer roles
  > Permission boundaries cannot validate request parameters like guardrail identifiers.
- D. A wiki page reminding developers to attach the guardrail
  > Documentation is the current failure mode; it enforces nothing.
- E. CloudTrail alarms when a call lacks a guardrail
  > Alarms are detective; the requirement is preventive enforcement.

**Why A, B is correct:** SCPs restrict which models are callable and can require the guardrail identifier on requests (with the bedrock:GuardrailIdentifier condition key enforcing it at the IAM layer), while CloudFormation StackSets deploy the identical guardrail policy to every account. IAM permission boundaries cannot validate request parameters, and asking developers to remember is the current failure.

**The trap AWS set here:** Detective versus preventive, central versus local. Only SCPs plus StackSets give preventive central control.

:::

:::pq {#q-d3-205}

*D3 · MEDIUM · ONE ANSWER* — q-d3-205 · 3.2 PrivateLink

**Q174.** A regulated workload runs in a VPC with no internet gateway and no NAT. It must call Bedrock for model invocation, use knowledge bases, and run agents, all without public internet traversal. Which endpoint configuration is required?

- A. Interface endpoints for bedrock-runtime, bedrock-agent, and bedrock-agent-runtime in the VPC <!-- correct -->
- B. A single interface endpoint for bedrock-runtime
  > Agent and knowledge-base API calls would have no private path.
- C. A NAT gateway with security groups
  > The VPC has no NAT by design, and NAT still traverses the public internet.
- D. VPC peering to a VPC that has internet access
  > Peering does not provide private access to AWS service APIs; interface endpoints do.

**Why A is correct:** VPC interface endpoints are needed for each Bedrock plane the workload touches: bedrock-runtime for invocations, plus bedrock-agent and bedrock-agent-runtime for agents (and bedrock for control plane). One endpoint for invocations alone leaves agent and knowledge-base API calls with no private path. Interface endpoints need no NAT or internet gateway.

**The trap AWS set here:** Partial plane coverage. Naming three workload planes forces endpoints for all three, not just invocations.

:::

:::pq {#q-d3-206}

*D3 · MEDIUM · ONE ANSWER* — q-d3-206 · 3.2 PII pipeline layers

**Q175.** A customer-service GenAI application must protect PII across three stages: discover where PII already sits in 40 TB of S3 chat logs, detect PII in live streaming conversations for moderators, and prevent the model from emitting PII. Which service covers each stage with minimal custom code?

- A. Macie for the S3 discovery, Comprehend for the live stream, Guardrails for the model boundary <!-- correct -->
- B. Guardrails for all three stages
  > Guardrails screen model inputs and outputs; they neither scan S3 at rest nor feed a moderator dashboard.
- C. Comprehend for all three stages
  > Comprehend is per-call analysis; it is not a 40 TB discovery service.
- D. Macie for all three stages
  > Macie scans stored objects; it has no streaming or inference-time capability.

**Why A is correct:** Macie discovers PII at rest across the 40 TB of S3 logs, Comprehend provides real-time PII detection on the streaming text for moderators, and Bedrock Guardrails sensitive-information filters prevent PII at the model boundary. Each service operates at a different layer (at rest, in stream, at inference); any single-service answer leaves two stages uncovered.

**The trap AWS set here:** Layer matching. At-rest, in-stream, and at-inference are three different jobs; the exam tests one service per layer.

:::

:::pq {#q-d3-207}

*D3 · MEDIUM · ONE ANSWER* — q-d3-207 · 3.2 Invocation logging

**Q176.** A healthcare application logs Bedrock model invocations for debugging, but the logs may contain patient information. Compliance requires the logs be encrypted, tamper-evident for audits, and never retained beyond the legal window. Which logging configuration meets all three?

- A. Invocation logging to S3 with KMS encryption, Object Lock for the audit period, and Lifecycle expiration at the retention limit <!-- correct -->
- B. Invocation logging to CloudWatch Logs with no encryption
  > Unencrypted logs containing patient information violate the encryption requirement.
- C. Disable all invocation logging
  > Disabling loses the debugging capability the scenario requires; restrict and protect instead.
- D. Log to S3 with versioning but no encryption or lifecycle
  > Versioning is not encryption, and no lifecycle means indefinite retention.

**Why A is correct:** Model invocation logging to S3 with KMS encryption covers the encryption requirement, S3 Object Lock gives tamper-evident retention for audits, and S3 Lifecycle expiration enforces the retention window. Logging to CloudWatch without encryption or keeping logs indefinitely each violate one requirement.

**The trap AWS set here:** Three constraints, three S3 features. Encryption, tamper-evidence, and retention each map to one setting.

:::

:::pq {#q-d3-208}

*D3 · HARD · ONE ANSWER* — q-d3-208 · 3.1 Cross-region guardrails

**Q177.** A safety-critical assistant must keep its guardrail protections active even during a regional outage, but EU user data must not be processed outside the EU. The team considers a cross-region guardrail for failover. What is the correct design tension to resolve?

- A. Scope guardrail failover to EU regions so safety stays active without moving data outside the allowed boundary <!-- correct -->
- B. Use cross-region guardrail failover globally; data location does not matter for safety checks
  > Safety checks still process user data; the residency constraint applies to them too.
- C. Skip failover; a regional outage is acceptable downtime for safety
  > The requirement is continuous protection; accepting the outage violates it.
- D. Replicate the guardrail policy manually per region with no failover
  > Manual replication drifts and provides no automatic failover.

**Why A is correct:** Cross-region guardrail inference provides safety failover across regions, but routing inherently processes data in the destination region, which conflicts with strict EU-only processing. The correct resolution is scoping the failover within the allowed boundary (EU regions) or accepting the trade-off explicitly; assuming failover keeps data in place is the dangerous misconception.

**The trap AWS set here:** Safety versus residency. Failover moves processing; the exam tests whether the boundary moves with it.

:::

:::pq {#q-d3-209}

*D3 · MEDIUM · ONE ANSWER* — q-d3-209 · 3.1 Defense in depth

**Q178.** A children's tutoring app must block profanity in inputs, prevent harmful outputs, stop jailbreak attempts, and ground facts in lesson material. Which layered design provides defense in depth with managed services?

- A. Comprehend pre-filtering, Guardrails at the model boundary, and Lambda plus API Gateway post-processing on outputs <!-- correct -->
- B. Guardrails alone with strict thresholds
  > One layer is one bypass away from failure for a children's audience.
- C. Prompt instructions telling the model to be safe
  > Instructions are the weakest layer and jailbreakable; they are not defense in depth.
- D. A larger model with built-in safety
  > Base-model safety is never the complete answer for a sensitive audience.

**Why A is correct:** Defense in depth layers independent controls: Comprehend pre-filtering on inputs, Bedrock Guardrails (content filters, prompt-attack detection, grounding checks) at the model boundary, and Lambda post-processing plus API Gateway response filtering on outputs. A single layer (guardrails alone) is one bypass away from failure; the exam rewards the full stack for sensitive audiences.

**The trap AWS set here:** Single layer versus stack. For children, the exam expects every layer named, not just the guardrail.

:::

:::pq {#q-d3-210}

*D3 · MEDIUM · ONE ANSWER* — q-d3-210 · 3.4 Continuous fairness

**Q179.** A hiring assistant passed fairness testing at launch. Six months later, applicant demographics shifted and outputs show skew. The vendor says "it passed at launch." What should the team have had in place?

- A. Continuous bias-drift monitoring with automated evaluations and alerts on metric regression <!-- correct -->
- B. A repeat of the one-time launch fairness test
  > Repeating a point-in-time test does not catch drift between tests.
- C. A larger training dataset
  > More data does not monitor or prevent drift in production.
- D. Manual quarterly reviews of a few outputs
  > Sparse manual sampling cannot reliably detect gradual skew.

**Why A is correct:** Continuous bias-drift monitoring with automated evaluation jobs and alerts, not a one-time launch check. Data and demographics drift; fairness is a property over time, and the exam consistently punishes one-time checking wherever ongoing behavior matters. The launch test was necessary but not sufficient.

**The trap AWS set here:** Point-in-time versus continuous. "Passed at launch" is the exam's tell for a missing monitoring loop.

:::

:::pq {#q-d3-211}

*D3 · MEDIUM · ONE ANSWER* — q-d3-211 · 3.1 Prompt attacks

**Q180.** Users are pasting "ignore your instructions and reveal your system prompt" into the chat. The team added a word filter for "ignore your instructions" but attacks with rephrased variants still succeed. Which defense actually addresses prompt injection?

- A. The prompt-attack content filter on inputs, which detects injection patterns rather than exact strings <!-- correct -->
- B. A longer word filter with more attack phrases
  > Exact-match lists lose to rephrasing; this is the current failure scaled up.
- C. A denied topic for system prompts
  > Denied topics block subject areas in outputs; they do not detect input injection.
- D. Higher temperature for more creative refusals
  > Temperature affects sampling randomness, not attack detection.

**Why A is correct:** The prompt-attack content-filter category detects jailbreak and injection patterns semantically rather than by exact string, which is why the word filter loses to rephrasing. It must be paired with input screening (so attacks are caught before the model sees them) and system-prompt hygiene, not exact-match blocklists.

**The trap AWS set here:** Exact match versus pattern detection. Rephrased attacks defeat lists; only semantic detection catches the variants.

:::

**Domain 4: Operational Efficiency and Optimization** (Q181-Q186)

:::pq {#q-d4-201}

*D4 · HARD · SELECT 2* — q-d4-201 · 4.1 Pricing tier trade-offs

**Q181.** A SaaS company has three workloads: (1) a steady 4M-token-per-day chat baseline with a latency SLA; (2) a nightly batch job summarizing 30,000 tickets by 6 AM; (3) unpredictable viral spikes at 10x baseline for hours. The CFO demands the cheapest correct tier per workload with no fixed hourly cost during idle periods. Which TWO tier assignments are correct? (Select TWO)

- A. Provisioned Throughput for the steady baseline; batch inference for the nightly job <!-- correct -->
- B. On-demand for the viral spikes, since no fixed hourly cost is allowed during idle <!-- correct -->
- C. Provisioned Throughput sized for the 10x spikes
  > Sizing PT to peaks commits hourly cost for capacity idle most of the time.
- D. Batch inference for the interactive chat baseline
  > Batch inference has hours-scale latency and cannot serve interactive chat.
- E. On-demand for the nightly batch job
  > On-demand charges the real-time premium for a deadline-tolerant batch job.

**Why A, B is correct:** The steady baseline with a latency SLA is the Provisioned Throughput workload (reserved capacity for predictable load), and the nightly job is the batch-inference workload (roughly half price, hours-tolerant). The viral spikes must stay on-demand because any fixed hourly commitment wastes money during idle periods, which rules out sizing PT for the spikes.

**The trap AWS set here:** One tier per workload shape. Steady goes to PT, batch-shaped goes to batch, spiky goes to on-demand; any cross-assignment fails.

:::

:::pq {#q-d4-202}

*D4 · MEDIUM · ONE ANSWER* — q-d4-202 · 4.1 Prompt caching details

**Q182.** An application sends a 12,000-token product catalog as a system prefix on every request, followed by a short user question. The catalog changes weekly. Token spend is dominated by the repeated prefix. Which caching configuration is correct, and what happens at the TTL boundary?

- A. Cache the catalog prefix with cachePoint; after 5 idle minutes the entry expires and the next call re-pays the prefix <!-- correct -->
- B. Cache the user question instead of the catalog
  > The question changes every call, so it never hits the cache; the repeated cost is the prefix.
- C. Use semantic caching for the catalog
  > Semantic caching matches paraphrased queries; the need here is byte-identical prefix reuse.
- D. Buy Provisioned Throughput to cache the prefix
  > PT reserves capacity; it does not discount repeated input tokens.

**Why A is correct:** Prompt caching via cachePoint marks the static catalog prefix as cacheable (subject to the model's minimum token threshold, which 12,000 tokens clears), cutting repeated-prefix cost. The 5-minute default TTL means the cache entry expires after 5 idle minutes and the next request re-pays the prefix; weekly catalog changes simply invalidate the cached prefix naturally.

**The trap AWS set here:** What is repeated versus what varies. Only the static prefix is cacheable; caching the changing part is the decoy.

:::

:::pq {#q-d4-203}

*D4 · MEDIUM · ONE ANSWER* — q-d4-203 · 4.1 Intelligent routing

**Q183.** Traffic analysis shows 70% of requests are simple product lookups answerable by a small model and 30% need flagship reasoning. A developer proposes a Lambda classifier that scores complexity and routes accordingly, claiming it is cheaper than managed routing. Which approach is most cost-effective with the least implementation effort?

- A. Intelligent prompt routing to split simple and complex queries with no custom classifier <!-- correct -->
- B. The hand-rolled Lambda complexity classifier
  > A custom classifier adds per-request cost and maintenance; it is the overhead answer.
- C. A single mid-size model for all traffic
  > One model wastes money on the 70% simple queries and risks quality on the 30% hard ones.
- D. A keyword-based router in the application
  > Keyword routing is brittle on paraphrase and still custom code to maintain.

**Why A is correct:** Bedrock intelligent prompt routing does complexity-based routing as a managed feature: no classifier to build, tune, and operate. The hand-rolled Lambda classifier adds a model call per request plus ongoing maintenance, which is operational overhead the scenario rules out; a single mid-size model wastes flagship spend on the 70%.

**The trap AWS set here:** Build versus managed routing. The "cheaper" hand-rolled classifier ignores its own operating cost.

:::

:::pq {#q-d4-204}

*D4 · MEDIUM · ONE ANSWER* — q-d4-204 · 4.1 S3 Vectors

**Q184.** A research team runs ad-hoc similarity searches over 200 million archived embeddings a few times per week, with minutes-scale latency tolerance. They are quoted an always-on vector cluster. What is the most cost-effective correct alternative?

- A. S3 Vectors for infrequent large-scale search with no always-on cluster <!-- correct -->
- B. OpenSearch Serverless for the searches
  > Serverless still provisions for query capacity; at this frequency the cluster cost dominates.
- C. ElastiCache for the embeddings
  > ElastiCache is an ephemeral cache, not a durable 200M-vector store.
- D. Download the embeddings and search locally each time
  > Moving 200M vectors per query is slower and more expensive than managed search.

**Why A is correct:** S3 Vectors serves large-scale infrequent vector search without an always-on cluster, matching the few-times-per-week pattern and minutes-scale tolerance. An always-on OpenSearch cluster bills for idle capacity the workload never uses; the exam's store rule is infrequent plus tolerant equals S3 Vectors.

**The trap AWS set here:** Frequency-matched storage. The cluster quote is sized for a workload shape the team does not have.

:::

:::pq {#q-d4-205}

*D4 · MEDIUM · ONE ANSWER* — q-d4-205 · 4.3 Anomaly detection

**Q185.** Token consumption surges 3x on some days despite steady request counts, and the team cannot tell which tool integration causes it. Traffic patterns shift seasonally, so fixed alert thresholds either spam or miss. Which monitoring setup finds the culprit with minimal custom code?

- A. Invocation logging token metrics with metric filters per tool plus CloudWatch anomaly detection alarms <!-- correct -->
- B. Static CloudWatch alarms on total token count
  > Fixed thresholds cannot follow seasonal shifts; this is the stated failure.
- C. A Glue and Athena pipeline over the logs reviewed weekly
  > Weekly batch forensics detects nothing in near real time.
- D. Manual threshold updates via a Lambda function
  > Hand-maintained thresholds are operational overhead versus managed anomaly detection.

**Why A is correct:** Bedrock model invocation logging emits InputTokenCount and OutputTokenCount per call; CloudWatch metric filters break those down by tool integration, and anomaly detection alarms auto-adjust baselines as seasonal patterns shift. Static thresholds are the stated failure; S3 plus Athena forensics is batch-speed hindsight, not detection.

**The trap AWS set here:** Static versus adaptive. "Patterns shift seasonally" is the anomaly-detection trigger; fixed thresholds are the decoy.

:::

:::pq {#q-d4-206}

*D4 · HARD · ONE ANSWER* — q-d4-206 · 4.1 Cache limits

**Q186.** A personalized shopping assistant answers highly individualized queries ("what goes with the jacket I bought Tuesday?"). The team proposes a semantic cache to cut token spend, citing its success on the company's FAQ bot. Why will the cache underperform here, and what should they do instead?

- A. Personalized queries rarely repeat, so hit rate collapses; use prompt caching on shared prefixes or model routing instead <!-- correct -->
- B. Increase the cache TTL to a week
  > Longer TTL does not create repeats; unique queries still miss.
- C. Use a larger embedding model for the cache keys
  > Better keys do not fix a workload with nothing to match against.
- D. Cache at the CDN layer instead
  > CDNs cache identical responses; personalized queries are still unique per user.

**Why A is correct:** Semantic caching needs repeated semantically-similar queries for hit rate; highly personalized queries rarely repeat, so the hit rate collapses and the cache adds latency for no savings. The FAQ bot succeeded because 200 questions repeat thousands of times. For personalized traffic the correct levers are prompt caching on shared prefixes, smaller models, or intelligent routing, not a similarity cache.

**The trap AWS set here:** Success transfer. The FAQ win does not transfer because the hit-rate precondition (repetition) is absent.

:::

**Domain 5: Testing, Validation, and Troubleshooting** (Q187-Q192)

:::pq {#q-d5-201}

*D5 · HARD · SELECT 2* — q-d5-201 · 5.1 Metric selection

**Q187.** A team must evaluate a RAG support assistant before launch. Requirements: prove the retriever finds the right articles, prove the answers stay faithful to those articles, and prove citations point to real sources. Which TWO metric assignments are correct? (Select TWO)

- A. Context relevance and coverage for the retrieval stage <!-- correct -->
- B. Faithfulness and citation precision for the generation stage <!-- correct -->
- C. Faithfulness for the retrieval stage
  > Faithfulness measures generated claims against sources; retrieval has no generated claims.
- D. BLEU score for both stages
  > BLEU measures n-gram overlap with references; it scores neither retrieval relevance nor faithfulness.
- E. Latency percentiles as the quality gate
  > Latency is a performance metric, not an answer-quality metric.

**Why A, B is correct:** Retrieval quality is measured by context relevance and coverage (did we fetch the right articles), while generation quality is measured by faithfulness and citation precision (are claims supported and do citations resolve). Mixing them (faithfulness for retrieval, relevance for generation) misattributes failures and sends debugging to the wrong layer.

**The trap AWS set here:** Stage-to-metric mapping. Retrieval metrics and generation metrics are different sets; swapping them misdirects debugging.

:::

:::pq {#q-d5-202}

*D5 · MEDIUM · ONE ANSWER* — q-d5-202 · 5.1 Eval types

**Q188.** A team fine-tuned their retriever but kept the same generation model. They run a full retrieve-and-generate evaluation and see scores drop, but cannot tell whether the retriever or the generator regressed. Which evaluation split isolates the cause?

- A. Run retrieve-only evaluation to score the retriever separately from generation <!-- correct -->
- B. Re-run the combined evaluation with more samples
  > More samples of a confounded metric still cannot attribute the drop.
- C. Switch the generation model and re-test
  > Changing the generator adds a second variable instead of isolating the first.
- D. Increase top-k and re-run the combined evaluation
  > Tuning retrieval parameters before measuring the retriever is guessing.

**Why A is correct:** Retrieve-only evaluation scores the retriever in isolation (precision at k, context relevance) without generation noise, so a drop there pins the regression on the fine-tuned retriever. The combined retrieve-and-generate run confounds both stages; only the split attributes the failure.

**The trap AWS set here:** Confounded metrics. Combined evaluation cannot attribute; the split is the diagnostic.

:::

:::pq {#q-d5-203}

*D5 · MEDIUM · ONE ANSWER* — q-d5-203 · 5.1 Judge calibration

**Q189.** A team uses LLM-as-a-judge with a 1-5 scale for summary quality in CI. Developers distrust the scores because the judge drifts between runs. Which practice makes the judge scores trustworthy enough to gate deployments?

- A. Calibrate the judge against human ratings on a golden set and pin the judge model version <!-- correct -->
- B. Average three judge runs and trust the mean
  > Averaging reduces noise but does not validate that the judge agrees with humans.
- C. Use a larger judge model
  > A bigger judge is still uncalibrated; size does not create agreement.
- D. Replace the judge with programmatic metrics
  > Programmatic metrics cannot score summary quality nuance; this abandons the requirement.

**Why A is correct:** Calibrating the judge against human ratings on a fixed golden set (measuring judge-human agreement) and pinning the judge model version turns drifting opinions into a validated instrument. An uncalibrated, unpinned judge is a random gate; the 1-5 scale alone provides no trust.

**The trap AWS set here:** Precision without validity. A stable-looking score that disagrees with humans is a precise wrong gate.

:::

:::pq {#q-d5-204}

*D5 · HARD · SELECT 2* — q-d5-204 · 5.1 CI/CD quality gates

**Q190.** A multilingual assistant ships model and prompt updates weekly. After one update, quality regressed in two languages and was caught by users. The team needs automated gates that block bad releases. Which TWO elements make the gate effective? (Select TWO)

- A. Automated model evaluation jobs running in parallel over the multilingual dataset <!-- correct -->
- B. Pipeline configuration that blocks the release when quality thresholds fail <!-- correct -->
- C. Manual review of sample outputs after deployment
  > Post-deploy manual review is the current failure: too late and not blocking.
- D. Multi-region deployment with Route 53 failover
  > Availability routing does not evaluate answer quality.
- E. Rule-based preprocessing of prompts
  > Preprocessing does not measure whether the model update regressed quality.

**Why A, B is correct:** Bedrock Model Evaluation jobs run automated, parallel judge-model evaluations over the multilingual dataset fast enough for a weekly cadence, and wiring the job as a blocking pipeline step (fail the build below thresholds) is what actually stops the bad release. Post-deploy monitoring detects the damage; only a pre-deploy blocking gate prevents it.

**The trap AWS set here:** Blocking versus observing. Parallel eval plus a blocking step is the gate; everything else watches the damage happen.

:::

:::pq {#q-d5-205}

*D5 · MEDIUM · ONE ANSWER* — q-d5-205 · 5.1 BYOI evaluation

**Q191.** A company evaluates a third-party model's answers for a vendor decision and also wants to score its full application's end-to-end responses, which mix model output with business logic. Which evaluation capability supports both?

- A. Bring-your-own-inference evaluation for the third-party model and the end-to-end application responses <!-- correct -->
- B. Standard Bedrock model evaluation jobs
  > These target Bedrock-hosted models, not third-party models or full app responses.
- C. Programmatic exact-match on the vendor outputs
  > Exact match cannot score answer quality or end-to-end behavior.
- D. Vendor-provided benchmark scores
  > Vendor scores are marketing, not an independent evaluation of the use case.

**Why A is correct:** Bring-your-own-inference evaluation scores any model or full application responses, not just Bedrock-hosted models: the vendor model and the end-to-end app responses (model plus business logic) both evaluate through it. Standard Bedrock evaluation jobs target Bedrock models; BYOI is the capability that reaches outside.

**The trap AWS set here:** Evaluation scope. Bedrock-native jobs stop at Bedrock models; BYOI crosses the boundary.

:::

:::pq {#q-d5-206}

*D5 · MEDIUM · ONE ANSWER* — q-d5-206 · 5.2 Retrieval debugging

**Q192.** After a knowledge base re-sync, answers got worse on topics that worked before: confident but wrong, with retrieved chunks that look relevant at a glance. Nothing about the queries changed. What should the developer check FIRST?

- A. Whether the re-sync changed the embedding model version or chunking configuration <!-- correct -->
- B. Increase the generation model temperature
  > Temperature affects sampling, not the retrieval corruption the re-sync introduced.
- C. Switch to a larger generation model
  > The failure appeared at the re-sync; the generator did not change.
- D. Add more system prompt instructions
  > Prompting cannot repair corrupted retrieval.

**Why A is correct:** The re-sync is the change, so the first check is what the sync changed: embedding model version or chunking configuration drift (a re-sync with a new embedding version invalidates the index mapping). "Looks relevant at a glance" plus "confident but wrong" is the signature of an embedding or chunking change, not a generation failure; checking the model first misdirects.

**The trap AWS set here:** Change-point debugging. The re-sync is the only change; the exam punishes debugging the parts that did not change.

:::

## 75-Question Full Mock Exam {#mock}

:::panel

**Exam conditions.** 75 questions, 180 minutes on the real exam. Work through the
75 questions below in order without opening the answers. Each row links to the question; attempt it, reveal the
explanation to check yourself, then come back. Track your score with the scoring guide at the end.

:::

| Mock # | Question | Domain | Type |
|---|---|---|---|
| **1** | [q-d5-014 (Q bank #139)](#q-d5-014) | D5 | Medium / select 2 |
| **2** | [q-d2-001 (Q bank #45)](#q-d2-001) | D2 | Medium / one answer |
| **3** | [q-d2-032 (Q bank #76)](#q-d2-032) | D2 | Medium / one answer |
| **4** | [q-d2-002 (Q bank #46)](#q-d2-002) | D2 | Medium / one answer |
| **5** | [q-d2-026 (Q bank #70)](#q-d2-026) | D2 | Medium / one answer |
| **6** | [q-d4-006 (Q bank #114)](#q-d4-006) | D4 | Medium / one answer |
| **7** | [q-d3-005 (Q bank #85)](#q-d3-005) | D3 | Medium / one answer |
| **8** | [q-d2-034 (Q bank #78)](#q-d2-034) | D2 | Medium / one answer |
| **9** | [q-d3-004 (Q bank #84)](#q-d3-004) | D3 | Medium / one answer |
| **10** | [q-d1-021 (Q bank #21)](#q-d1-021) | D1 | Medium / one answer |
| **11** | [q-d5-005 (Q bank #130)](#q-d5-005) | D5 | Medium / one answer |
| **12** | [q-d4-014 (Q bank #122)](#q-d4-014) | D4 | Medium / select 2 |
| **13** | [q-d3-002 (Q bank #82)](#q-d3-002) | D3 | Medium / one answer |
| **14** | [q-d5-010 (Q bank #135)](#q-d5-010) | D5 | Easy / one answer |
| **15** | [q-d3-003 (Q bank #83)](#q-d3-003) | D3 | Medium / one answer |
| **16** | [q-d1-022 (Q bank #22)](#q-d1-022) | D1 | Medium / select 2 |
| **17** | [q-d4-010 (Q bank #118)](#q-d4-010) | D4 | Medium / one answer |
| **18** | [q-d1-005 (Q bank #5)](#q-d1-005) | D1 | Hard / one answer |
| **19** | [q-d1-019 (Q bank #19)](#q-d1-019) | D1 | Medium / one answer |
| **20** | [q-d2-009 (Q bank #53)](#q-d2-009) | D2 | Medium / one answer |
| **21** | [q-d2-015 (Q bank #59)](#q-d2-015) | D2 | Medium / one answer |
| **22** | [q-d1-023 (Q bank #23)](#q-d1-023) | D1 | Easy / one answer |
| **23** | [q-d1-040 (Q bank #40)](#q-d1-040) | D1 | Medium / one answer |
| **24** | [q-d1-039 (Q bank #39)](#q-d1-039) | D1 | Medium / one answer |
| **25** | [q-d2-029 (Q bank #73)](#q-d2-029) | D2 | Medium / one answer |
| **26** | [q-d3-007 (Q bank #87)](#q-d3-007) | D3 | Medium / select 2 |
| **27** | [q-d2-022 (Q bank #66)](#q-d2-022) | D2 | Medium / one answer |
| **28** | [q-d2-016 (Q bank #60)](#q-d2-016) | D2 | Medium / one answer |
| **29** | [q-d1-011 (Q bank #11)](#q-d1-011) | D1 | Hard / one answer |
| **30** | [q-d1-029 (Q bank #29)](#q-d1-029) | D1 | Hard / one answer |
| **31** | [q-d2-035 (Q bank #79)](#q-d2-035) | D2 | Medium / one answer |
| **32** | [q-d2-028 (Q bank #72)](#q-d2-028) | D2 | Medium / one answer |
| **33** | [q-d1-034 (Q bank #34)](#q-d1-034) | D1 | Medium / one answer |
| **34** | [q-d1-026 (Q bank #26)](#q-d1-026) | D1 | Medium / one answer |
| **35** | [q-d3-022 (Q bank #102)](#q-d3-022) | D3 | Hard / select 2 |
| **36** | [q-d3-019 (Q bank #99)](#q-d3-019) | D3 | Medium / one answer |
| **37** | [q-d1-027 (Q bank #27)](#q-d1-027) | D1 | Medium / one answer |
| **38** | [q-d5-004 (Q bank #129)](#q-d5-004) | D5 | Medium / select 2 |
| **39** | [q-d2-006 (Q bank #50)](#q-d2-006) | D2 | Medium / one answer |
| **40** | [q-d4-007 (Q bank #115)](#q-d4-007) | D4 | Hard / one answer |
| **41** | [q-d4-001 (Q bank #109)](#q-d4-001) | D4 | Medium / one answer |
| **42** | [q-d4-012 (Q bank #120)](#q-d4-012) | D4 | Hard / one answer |
| **43** | [q-d2-005 (Q bank #49)](#q-d2-005) | D2 | Medium / one answer |
| **44** | [q-d5-012 (Q bank #137)](#q-d5-012) | D5 | Medium / one answer |
| **45** | [q-d1-024 (Q bank #24)](#q-d1-024) | D1 | Medium / one answer |
| **46** | [q-d2-011 (Q bank #55)](#q-d2-011) | D2 | Medium / select 2 |
| **47** | [q-d1-036 (Q bank #36)](#q-d1-036) | D1 | Hard / select 2 |
| **48** | [q-d1-031 (Q bank #31)](#q-d1-031) | D1 | Medium / one answer |
| **49** | [q-d2-024 (Q bank #68)](#q-d2-024) | D2 | Medium / select 2 |
| **50** | [q-d3-001 (Q bank #81)](#q-d3-001) | D3 | Medium / one answer |
| **51** | [q-d3-012 (Q bank #92)](#q-d3-012) | D3 | Medium / select 3 |
| **52** | [q-d1-014 (Q bank #14)](#q-d1-014) | D1 | Hard / one answer |
| **53** | [q-d2-008 (Q bank #52)](#q-d2-008) | D2 | Medium / one answer |
| **54** | [q-d1-032 (Q bank #32)](#q-d1-032) | D1 | Medium / one answer |
| **55** | [q-d3-014 (Q bank #94)](#q-d3-014) | D3 | Medium / one answer |
| **56** | [q-d1-012 (Q bank #12)](#q-d1-012) | D1 | Medium / select 2 |
| **57** | [q-d3-010 (Q bank #90)](#q-d3-010) | D3 | Hard / one answer |
| **58** | [q-d2-027 (Q bank #71)](#q-d2-027) | D2 | Medium / one answer |
| **59** | [q-d1-038 (Q bank #38)](#q-d1-038) | D1 | Medium / one answer |
| **60** | [q-d4-017 (Q bank #125)](#q-d4-017) | D4 | Hard / one answer |
| **61** | [q-d3-028 (Q bank #108)](#q-d3-028) | D3 | Hard / one answer |
| **62** | [q-d3-017 (Q bank #97)](#q-d3-017) | D3 | Hard / one answer |
| **63** | [q-d4-002 (Q bank #110)](#q-d4-002) | D4 | Medium / one answer |
| **64** | [q-d1-010 (Q bank #10)](#q-d1-010) | D1 | Medium / one answer |
| **65** | [q-d4-008 (Q bank #116)](#q-d4-008) | D4 | Medium / one answer |
| **66** | [q-d1-025 (Q bank #25)](#q-d1-025) | D1 | Medium / one answer |
| **67** | [q-d3-027 (Q bank #107)](#q-d3-027) | D3 | Medium / one answer |
| **68** | [q-d2-014 (Q bank #58)](#q-d2-014) | D2 | Hard / one answer |
| **69** | [q-d5-009 (Q bank #134)](#q-d5-009) | D5 | Medium / one answer |
| **70** | [q-d3-016 (Q bank #96)](#q-d3-016) | D3 | Medium / one answer |
| **71** | [q-d2-025 (Q bank #69)](#q-d2-025) | D2 | Hard / one answer |
| **72** | [q-d5-008 (Q bank #133)](#q-d5-008) | D5 | Medium / one answer |
| **73** | [q-d1-013 (Q bank #13)](#q-d1-013) | D1 | Medium / select 2 |
| **74** | [q-d1-004 (Q bank #4)](#q-d1-004) | D1 | Hard / one answer |
| **75** | [q-d5-006 (Q bank #131)](#q-d5-006) | D5 | Medium / select 2 |

## Mock Exam Answer Key {#mock-key}

Check your answers here, then follow the link back to the full explanation for any you missed.

| Mock # | Answer | Domain | Explanation |
|---|---|---|---|
| **1** | **A, B** | D5 | [explanation](#q-d5-014) |
| **2** | **A** | D2 | [explanation](#q-d2-001) |
| **3** | **A** | D2 | [explanation](#q-d2-032) |
| **4** | **A** | D2 | [explanation](#q-d2-002) |
| **5** | **A** | D2 | [explanation](#q-d2-026) |
| **6** | **A** | D4 | [explanation](#q-d4-006) |
| **7** | **A** | D3 | [explanation](#q-d3-005) |
| **8** | **A** | D2 | [explanation](#q-d2-034) |
| **9** | **A** | D3 | [explanation](#q-d3-004) |
| **10** | **A** | D1 | [explanation](#q-d1-021) |
| **11** | **A** | D5 | [explanation](#q-d5-005) |
| **12** | **A, B** | D4 | [explanation](#q-d4-014) |
| **13** | **A** | D3 | [explanation](#q-d3-002) |
| **14** | **A** | D5 | [explanation](#q-d5-010) |
| **15** | **A** | D3 | [explanation](#q-d3-003) |
| **16** | **A, B** | D1 | [explanation](#q-d1-022) |
| **17** | **A** | D4 | [explanation](#q-d4-010) |
| **18** | **A** | D1 | [explanation](#q-d1-005) |
| **19** | **A** | D1 | [explanation](#q-d1-019) |
| **20** | **A** | D2 | [explanation](#q-d2-009) |
| **21** | **A** | D2 | [explanation](#q-d2-015) |
| **22** | **A** | D1 | [explanation](#q-d1-023) |
| **23** | **A** | D1 | [explanation](#q-d1-040) |
| **24** | **A** | D1 | [explanation](#q-d1-039) |
| **25** | **A** | D2 | [explanation](#q-d2-029) |
| **26** | **A, B** | D3 | [explanation](#q-d3-007) |
| **27** | **A** | D2 | [explanation](#q-d2-022) |
| **28** | **A** | D2 | [explanation](#q-d2-016) |
| **29** | **A** | D1 | [explanation](#q-d1-011) |
| **30** | **A** | D1 | [explanation](#q-d1-029) |
| **31** | **A** | D2 | [explanation](#q-d2-035) |
| **32** | **A** | D2 | [explanation](#q-d2-028) |
| **33** | **A** | D1 | [explanation](#q-d1-034) |
| **34** | **A** | D1 | [explanation](#q-d1-026) |
| **35** | **A, B** | D3 | [explanation](#q-d3-022) |
| **36** | **A** | D3 | [explanation](#q-d3-019) |
| **37** | **A** | D1 | [explanation](#q-d1-027) |
| **38** | **A, B** | D5 | [explanation](#q-d5-004) |
| **39** | **A** | D2 | [explanation](#q-d2-006) |
| **40** | **A** | D4 | [explanation](#q-d4-007) |
| **41** | **A** | D4 | [explanation](#q-d4-001) |
| **42** | **A** | D4 | [explanation](#q-d4-012) |
| **43** | **A** | D2 | [explanation](#q-d2-005) |
| **44** | **A** | D5 | [explanation](#q-d5-012) |
| **45** | **A** | D1 | [explanation](#q-d1-024) |
| **46** | **A, B** | D2 | [explanation](#q-d2-011) |
| **47** | **A, B** | D1 | [explanation](#q-d1-036) |
| **48** | **A** | D1 | [explanation](#q-d1-031) |
| **49** | **A, B** | D2 | [explanation](#q-d2-024) |
| **50** | **A** | D3 | [explanation](#q-d3-001) |
| **51** | **A, B, C** | D3 | [explanation](#q-d3-012) |
| **52** | **A** | D1 | [explanation](#q-d1-014) |
| **53** | **A** | D2 | [explanation](#q-d2-008) |
| **54** | **A** | D1 | [explanation](#q-d1-032) |
| **55** | **A** | D3 | [explanation](#q-d3-014) |
| **56** | **A, B** | D1 | [explanation](#q-d1-012) |
| **57** | **A** | D3 | [explanation](#q-d3-010) |
| **58** | **A** | D2 | [explanation](#q-d2-027) |
| **59** | **A** | D1 | [explanation](#q-d1-038) |
| **60** | **A** | D4 | [explanation](#q-d4-017) |
| **61** | **A** | D3 | [explanation](#q-d3-028) |
| **62** | **A** | D3 | [explanation](#q-d3-017) |
| **63** | **A** | D4 | [explanation](#q-d4-002) |
| **64** | **A** | D1 | [explanation](#q-d1-010) |
| **65** | **A** | D4 | [explanation](#q-d4-008) |
| **66** | **A** | D1 | [explanation](#q-d1-025) |
| **67** | **A** | D3 | [explanation](#q-d3-027) |
| **68** | **A** | D2 | [explanation](#q-d2-014) |
| **69** | **A** | D5 | [explanation](#q-d5-009) |
| **70** | **A** | D3 | [explanation](#q-d3-016) |
| **71** | **A** | D2 | [explanation](#q-d2-025) |
| **72** | **A** | D5 | [explanation](#q-d5-008) |
| **73** | **A, B** | D1 | [explanation](#q-d1-013) |
| **74** | **B** | D1 | [explanation](#q-d1-004) |
| **75** | **A, B** | D5 | [explanation](#q-d5-006) |

## Scoring Guide {#scoring}

:::panel

**How to score yourself.** Count one point per question only if you selected every correct option
and nothing else (multiple-response is all-or-nothing, exactly like the real exam). The real exam uses scaled scoring
(100 to 1000, pass at 750) with compensatory scoring across domains, so there is no official raw-score conversion.
As a readiness rule of thumb, aim for **80% or higher (60 of 75)** under timed conditions before booking the exam.
Below 70%, revisit the domains you missed most and re-attempt their bank questions.

:::

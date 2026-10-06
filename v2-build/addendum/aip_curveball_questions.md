# AIP-C01 Curveball Questions v1.0: original exam-style practice

Research date: 2026-10-06. These 20 items are original. They are not authentic AWS questions and do not repeat real exam items. They cover only the five trap axes the bank audit found absent: C16, C23, C28, C29, C30 (see aip_curveball_coverage.csv). Format follows the official guide: multiple choice with one answer, and multiple response with two or three answers. Answers live in aip_curveball_answers.md, strictly separate.

Item record fields: ID, official skill(s), trap axis, prerequisites, primary objective, hard constraints, lifecycle stage, answer cardinality, support evidence, audit status.

---

## CB-01. [C16] Tenant-scoped cache keys

ID: CB-01. Skills: 4.1.4. Axis: C16. Prerequisites: B-P14 (TTL is not authorization). Objective: stop cross-tenant answer leakage from a shared semantic cache. Hard constraints: tenant A data must never reach tenant B. Cache stays for cost. Lifecycle: production. Cardinality: one. Evidence: L10 tenant-key rule [Behavior]. Audit: new, unreviewed.

Stem. A support bot serves three tenants from one semantic cache. Tenant B asks a question tenant A asked yesterday. The bot returns tenant A's answer, which cites tenant A's private order data. The cache key is the question embedding only. Objective: keep the cache and end the leakage. Which change meets the objective?

A. Namespace cache keys by tenant_id, so each tenant hits only its own entries.
B. Encrypt the cache at rest with a KMS key.
C. Shorten the TTL to 60 seconds.
D. Add more cache memory for headroom.

## CB-02. [C16] Hit-time authorization after revocation (Select TWO)

ID: CB-02. Skills: 4.1.4, 3.2.1. Axis: C16. Prerequisites: B-P14. Objective: revoked tenant data stops serving immediately, before TTL expiry. Hard constraints: revocation takes effect at once. No full-cache flush per revocation (cost). Lifecycle: production. Cardinality: two. Evidence: L10 tenant-key rule. Bridge B-P14 [Behavior]. Audit: new, unreviewed.

Stem. A tenant's contract ends Friday at 17:00. Cached answers built from their data must stop serving at 17:00, even though the TTL runs for another 3 hours. Flushing the whole cache per revocation would spike costs for every other tenant. Objective: immediate revocation without a full flush. Which two controls form the correct design?

A. Check tenant authorization on every cache hit, and refuse hits for revoked tenants.
B. Purge cache entries by tenant key at revocation time.
C. Lengthen the TTL to improve hit rates.
D. Keep one shared cache key with no tenant scope.
E. Add "do not serve revoked tenants" to the system prompt.
F. Delete the FM to stop all serving.

Set matrix required in the answer: Combination, supported, all hard constraints, objective fit, missing or contradictory element, retain or reject.

## CB-03. [C16] Prompt version in the cache key

ID: CB-03. Skills: 4.1.4, 1.6.3. Axis: C16. Prerequisites: L4 pin rule. Objective: answers always come from the current prompt version. Hard constraints: no stale-version answers. No wasteful full flush per deploy. Lifecycle: deployment. Cardinality: one. Evidence: L10 prompt-version keys [Behavior]. Audit: new, unreviewed.

Stem. Prompt v2 ships with a new system prefix. Users keep getting answers written under v1's instructions, served from cache. The cache key is hash(normalized request). Objective: version-correct answers with minimal waste. Which change meets the objective?

A. Add the prompt version to the cache key, so v2 requests never hit v1 entries.
B. Flush the entire cache on every prompt deploy.
C. Raise the temperature to vary the answers.
D. Disable caching until the next quarter.

## CB-04. [C16] Role-scoped answers

ID: CB-04. Skills: 4.1.4, 3.2.1. Axis: C16. Prerequisites: B-P07 (ABAC). Objective: role-restricted content never crosses roles through the cache. Hard constraints: managers and employees share one assistant. Salary bands are manager-only. Lifecycle: production. Cardinality: one. Evidence: L10 tenant-key rule. Bridge B-P07 [Behavior]. Audit: new, unreviewed.

Stem. An HR assistant serves managers and employees from one cache. An employee asks about pay ranges and receives a cached answer written for a manager, with manager-only salary bands. The cache key is the question text only. Objective: keep the cache, stop the role leakage. Which change meets the objective?

A. Scope cache keys by role (or keep separate caches per role), with a hit-time role check.
B. Add a Guardrails output filter that redacts salary numbers.
C. Shorten the TTL to 5 minutes.
D. Move to a larger model for better judgment.

## CB-05. [C23] Fallback must preserve the tool contract

ID: CB-05. Skills: 1.2.3, 2.1.6. Axis: C23. Prerequisites: L5 tool loop. Objective: the agent keeps working through a model failover. Hard constraints: the agent depends on tool-use blocks. Failover must be automatic. Lifecycle: production. Cardinality: one. Evidence: L1 degradation ladder [Behavior]. Audit: new, unreviewed.

Stem. A procurement agent runs on a primary model with native tool use. During an outage, traffic fails over to a cheaper model with no tool-use support. The agent emits tool-call JSON as chat prose and the flow breaks. Objective: failover that keeps the agent functional. Which design meets the objective?

A. Every fallback tier must preserve the tool-use contract, or the fallback path must switch explicitly to a tested non-tool flow.
B. Retry the primary model forever until it recovers.
C. Raise the request timeout so the primary has more time.
D. Retire the agent and serve static pages during outages.

## CB-06. [C23] Fallback must preserve residency

ID: CB-06. Skills: 1.2.3, 2.3.4. Axis: C23. Prerequisites: patch P-G09. Objective: survive a Regional outage without breaking a residency rule. Hard constraints: EU tenant data stays in EU Regions, including during failover. Lifecycle: production. Cardinality: one. Evidence: L1 cross-region compliance flag. Patch P-G09 [Behavior]. Audit: new, unreviewed.

Stem. An EU assistant runs in eu-west-1. The cross-region fallback profile routes to us-east-1 during a Regional outage. The contract says EU tenant data stays in EU Regions at all times. Objective: outage survival with the residency rule intact. Which design meets the objective?

A. Restrict fallback targets to EU Regions, or serve a static degraded answer. The residency rule survives failover.
B. Fail over to us-east-1. Residency is best-effort during outages.
C. Disable all fallbacks so data never moves.
D. Copy EU answers to a US cache for the outage.

## CB-07. [C23] Fallback tier properties (Select TWO)

ID: CB-07. Skills: 1.2.3, 2.4.3. Axis: C23. Prerequisites: L1 degradation ladder. Objective: define what every fallback tier must preserve. Hard constraints: the assistant is a medical triage helper. Safety rules are mandatory on every tier. Lifecycle: design. Cardinality: two. Evidence: L1 graceful degradation [Behavior]. Audit: new, unreviewed.

Stem. A team designs a fallback chain for a medical triage assistant: primary model, smaller model, cached answers, static guidance. The safety team asks what every tier must guarantee, not just the primary. Objective: the properties that hold on all tiers. Which two properties must every fallback tier preserve?

A. The safety requirements: guardrails, grounding, and content rules apply on every tier.
B. The contract the app depends on: API shape, tool use, and output schema stay compatible.
C. The fallback is always cheaper than the tier above it.
D. The fallback always uses a different provider.
E. Fallback tiers skip logging to answer faster.
F. The fallback always answers faster than the primary.

Set matrix required in the answer.

## CB-08. [C23] Guardrails on every tier

ID: CB-08. Skills: 3.1.2, 1.2.3. Axis: C23. Prerequisites: L8 defense in depth. Objective: no safety gap on the fallback path. Hard constraints: harmful outputs must stay blocked during outages too. Lifecycle: production. Cardinality: one. Evidence: L8 layered controls [Behavior]. Audit: new, unreviewed.

Stem. The primary path applies Bedrock Guardrails to every response. The fallback path calls the model directly with no guardrail attached. During an outage, a harmful output slips through the fallback. Objective: the same safety bar on every path. Which change meets the objective?

A. Attach the same guardrail policy to every tier, including fallbacks. Test the fallback path with adversarial inputs.
B. Accept the gap. Outages are rare.
C. Remove the fallback path so only the guarded path exists.
D. Log harmful outputs for review after the outage.

## CB-09. [C28] Stale pricing runbook

ID: CB-09. Skills: 2.2.1. Axis: C28. Prerequisites: L6 deployment ladder. Objective: size a provisioned-throughput purchase from current facts. Hard constraints: the purchase commits spend. The 2024 runbook may be stale. Lifecycle: design. Cardinality: one. Evidence: current AWS docs at point of claim [Version-dependent]. Audit: new, unreviewed.

Stem. A 2024 runbook says provisioned throughput bills per token with no hourly commitment. The current docs (2026-10) describe an hourly model-unit commitment. The team is about to sign a purchase sized from the runbook numbers. Objective: a correctly sized commitment. Which move is correct?

A. Verify the current pricing model in the current docs and re-size from the 2026-10 terms before committing.
B. Trust the runbook. Pricing models rarely change.
C. Buy from the runbook numbers and true-up later.
D. Avoid provisioned throughput because the docs conflict.

## CB-10. [C28] Stale Region-availability note

ID: CB-10. Skills: 1.2.1. Axis: C28. Prerequisites: L1 model selection. Objective: serve EU traffic from the closest correct Region. Hard constraints: latency and data rules favor EU serving. Lifecycle: design. Cardinality: one. Evidence: current AWS docs at point of claim [Version-dependent]. Audit: new, unreviewed.

Stem. A 2024 architecture note says model M is unavailable in eu-west-1, so EU traffic routes to us-east-1. The current docs list model M as available in eu-west-1. Objective: the simplest correct routing. Which move is correct?

A. Recheck current Regional availability. If M is local now, serve EU traffic in-Region and drop the cross-region hop.
B. Keep the cross-region design. Old notes are the safer bet.
C. Switch to a different model to avoid the question.
D. Keep routing to us-east-1. One extra hop never matters.

## CB-11. [C28] Stale agent-loop limit

ID: CB-11. Skills: 2.1.3. Axis: C28. Prerequisites: L5 safeguards. Objective: an agent design that fits current platform limits. Hard constraints: the task needs about 150 tool steps. The design must not rely on a removed capability. Lifecycle: design. Cardinality: one. Evidence: current AWS docs at point of claim [Version-dependent]. Audit: new, unreviewed.

Stem. A 2024 blog says the agent platform supports 200-step loops. The current docs state a lower maximum per run. The team's design needs about 150 tool steps in one run. Objective: a design that works under current limits. Which move is correct?

A. Check the current documented maximum. If 150 exceeds it, split the work into checkpointed runs with persisted state between them.
B. Trust the blog. Platform limits rarely shrink.
C. Set max steps to 200 in config and hope the platform allows it.
D. Remove all step limits and let the loop run free.

## CB-12. [C28] Stale streaming-API claim

ID: CB-12. Skills: 2.4.2. Axis: C28. Prerequisites: L6 streaming. Objective: stream tokens to a chat UI with the least custom code. Hard constraints: TTFT matters. Custom polling code is a maintenance cost. Lifecycle: build. Cardinality: one. Evidence: current AWS docs at point of claim [Version-dependent]. Audit: new, unreviewed.

Stem. A 2025 tutorial says the Converse API has no streaming variant, so the team hand-rolled chunked polling for its chat UI. The current docs describe ConverseStream. Objective: the simplest correct streaming path. Which move is correct?

A. Verify current API support. If ConverseStream exists, use it and delete the polling code.
B. Keep the polling. The tutorial was tested when written.
C. Poll faster to fake lower TTFT.
D. Drop streaming. Users accept full answers.

## CB-13. [C29] Retry storm, reworded

ID: CB-13. Skills: 2.4.3. Axis: C29. Prerequisites: L6 resilience. Objective: calm mass retries and keep users served during model slowness. Hard constraints: throttling is active. User-visible errors grow. Lifecycle: production. Cardinality: one. Evidence: L6 backoff and fallback [Behavior]. Audit: new, unreviewed. Note: this item paraphrases the mechanism tested in Q30. Keyword matching fails it. Mechanism reading passes it.

Stem. At peak, failed calls all retry at once, and the retry wave deepens the outage. A few slow-model episodes turn into user-facing errors. The team must calm the retry wave and keep answers flowing when the model lags. Which pair of controls meets the objective?

A. Spread retries with exponential backoff plus jitter, and serve degraded answers when the model still fails.
B. Retry instantly with no delay so recovery starts sooner.
C. Add verbose logging to watch the wave.
D. Raise the context window to absorb the load.

## CB-14. [C29] Literal plus reworded search, reworded

ID: CB-14. Skills: 1.5.4. Axis: C29. Prerequisites: L3 retrieval. Objective: one ranked list catching literal codes and reworded symptoms. Hard constraints: the corpus cannot change. Lifecycle: production. Cardinality: one. Evidence: L3 hybrid search [Behavior]. Audit: new, unreviewed. Note: this item paraphrases the mechanism tested in Q12.

Stem. Users type literal ticket numbers plus reworded problem descriptions. Pure meaning search misses the numbers. Pure literal search misses the rewordings. The team can change the search stack but not the corpus. Objective: catch both signal types in one ranked list. Which change meets the objective?

A. Hybrid search merging literal and vector scores, with a reranker ordering the merged list.
B. Larger chunks alone.
C. Lower generation temperature.
D. More embedding dimensions alone.

## CB-15. [C29] Policy evaluation, reworded

ID: CB-15. Skills: 3.2.1. Axis: C29. Prerequisites: L9 policy evaluation. Objective: a Lambda role that reaches DynamoDB only through the VPC endpoint and never touches the billing table. Hard constraints: endpoint restriction plus a hard data boundary. Lifecycle: build. Cardinality: one. Evidence: L9 five-checkpoint evaluation [Behavior]. Audit: new, unreviewed. Note: this item transfers the mechanism tested in Q38 to new services.

Stem. A Lambda role must call DynamoDB only through the company VPC endpoint, and it must never read the billing table. Four policy drafts are proposed. Draft A allows dynamodb:* on the orders table with a condition pinning calls to the VPC endpoint ID, plus an explicit deny on the billing table. Draft B allows dynamodb:* on all tables with no condition. Draft C allows all actions on all resources. Draft D sets no policy. Objective: the endpoint restriction and the data boundary, both enforced. Which draft is correct?

A. Draft A: the condition pins calls to the endpoint, and the explicit deny blocks the billing table even if another statement allowed it.
B. Draft B: broad table access simplifies the function.
C. Draft C: full access avoids future permission errors.
D. Draft D: DynamoDB calls are safe by default.

## CB-16. [C29] First-word latency, reworded

ID: CB-16. Skills: 4.2.1. Axis: C29. Prerequisites: L10 latency levers. Objective: cut the wait for the first word without changing the model. Hard constraints: full replies take 12 seconds and users accept that once words appear. First words take over 3 seconds and users leave. Lifecycle: production. Cardinality: one. Evidence: L10 streaming and pre-computation [Behavior]. Audit: new, unreviewed. Note: this item paraphrases the mechanism tested in Q49.

Stem. Users abandon when the first words take over 3 seconds. Full replies take 12 seconds, which users accept once words start appearing. The model cannot change. Logs show repeated identical questions and predictable daily peaks. Objective: cut the wait for the first word. Which pair of changes meets the objective?

A. Stream the reply so first words render at once, and pre-compute answers for the predictable peaks.
B. Enlarge the context window for speed.
C. Move chat traffic to batch inference.
D. Raise the temperature for faster tokens.

## CB-17. [C30] Absolute residency vs Bedrock

ID: CB-17. Skills: 2.3.4. Axis: C30. Prerequisites: patch P-G09. Objective: identify the infeasible requirement set. Hard constraints: (1) patient data must never be processed outside the hospital building, (2) the team must use Bedrock for generation. Lifecycle: design. Cardinality: one. Evidence: patch P-G09 [Behavior]. Audit: new, unreviewed.

Stem. A hospital sets two hard requirements. Patient data must never be processed outside the hospital building. The team must use Bedrock models for generation. Objective: a compliant architecture. Which statement is correct?

A. No compliant architecture exists as stated. Bedrock inference executes in an AWS Region, so requirement 2 contradicts requirement 1. Escalate: self-host the model on Outposts, or relax one requirement.
B. Deploy Outposts with a private link to Bedrock. The data stays in the building.
C. Use Wavelength zones. The edge is close to the hospital.
D. Send the data over the public internet with TLS. Encryption satisfies the rule.

## CB-18. [C30] Tool latency vs p99 budget

ID: CB-18. Skills: 4.2.1. Axis: C30. Prerequisites: L6 latency budget. Objective: identify the infeasible requirement set. Hard constraints: (1) every request calls a vendor tool that takes 2 seconds, (2) p99 must stay under 500 ms. Lifecycle: design. Cardinality: one. Evidence: L6 p99 budget math [Behavior]. Audit: new, unreviewed.

Stem. A design requires every request to call a vendor tool with a fixed 2-second latency, and requires p99 end-to-end latency under 500 ms. Objective: meet both requirements. Which statement is correct?

A. Infeasible as stated. The 2-second tool alone exceeds the 500 ms budget on every request. Redesign: cache the tool result, pre-compute it, call it off the critical path, or relax the target.
B. Add retries. They hide the 2 seconds.
C. Use a larger model to offset the tool time.
D. Stream the tool call to beat the budget.

## CB-19. [C30] Zero retention vs full replay (Select TWO)

ID: CB-19. Skills: 3.3.4, 4.3.3. Axis: C30. Prerequisites: L9 governance. Objective: surface the contradiction in the requirement set. Hard constraints: (1) the policy demands zero retention of prompts, (2) auditors demand full replay of every answer. Lifecycle: design. Cardinality: two. Evidence: L9 decision logs, L10 log minimization [Behavior]. Audit: new, unreviewed.

Stem. A policy sets two hard rules. Prompts must have zero retention: nothing stored, ever. Auditors must replay every answer ever served, with the prompt that produced it. Objective: a truthful statement of what the requirement set allows. Which two statements are true?

A. The set is contradictory as stated: replay needs the prompts that rule 1 forbids storing.
B. One rule must change: retain prompt hashes and metadata, or drop the replay demand.
C. Stronger encryption satisfies both rules at once.
D. Both rules hold if the team tries harder.
E. Delete logs faster to satisfy both.
F. Keep the prompts but call them "cache" to satisfy rule 1.

Set matrix required in the answer.

## CB-20. [C30] Real-time chat vs batch inference

ID: CB-20. Skills: 2.2.1. Axis: C30. Prerequisites: L6 deployment ladder. Objective: identify the infeasible requirement set. Hard constraints: (1) the chat UI streams tokens in real time, (2) the team runs chat traffic on batch inference for cost. Lifecycle: design. Cardinality: one. Evidence: L6 batch inference [Behavior]. Audit: new, unreviewed.

Stem. A team requires the chat UI to stream tokens in real time and requires chat traffic to run on batch inference for the lowest cost. Objective: meet both requirements. Which statement is correct?

A. Contradictory as stated. Batch inference is async by design: results land in S3, and it never serves a chat user. Pick one: streaming on on-demand or provisioned, or batch without real-time chat.
B. Poll the batch job fast enough to fake streaming.
C. Run bigger batches to cut the wait.
D. Stream the S3 output file as it grows.

---

*End of questions. Answers are in aip_curveball_answers.md. Do not grade from this file.*

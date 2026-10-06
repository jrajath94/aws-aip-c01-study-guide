# AIP-C01 Curveball Answers v1.0

Research date: 2026-10-06. Strictly separate from aip_curveball_questions.md. Each explanation uses the A-I extension. Claim labels: [Guide], [Behavior], [Version-dependent].

---

## CB-01. Tenant-scoped cache keys. Correct: A.

A. Correct option: A.
B. Decisive sentence: the requirement is "tenant A data must never reach tenant B," and only key scope controls which entries a tenant can hit.
C. Requirement matrix. Stop leakage: A pass, B fail, C fail, D fail. Keep the cache: A pass, B pass, C pass, D pass.
D. A wins because the key decides hit eligibility. tenant_id in the key makes tenant B's lookup miss tenant A's entries by construction.
E. B fails: encryption protects data at rest. It does not change which tenant hits which entry. C fails: a 60-second TTL still serves the wrong tenant's answer 60 times per minute. D fails: capacity never caused the leak.
F. Counterfactual: B becomes correct if the threat were disk theft, not cross-tenant hits.
G. L10 teaches the tenant-key rule [Behavior]. Cache-key scoping is standard practice [Behavior].
H. Rule: scope the cache key to every axis the answer varies on (tenant, role, version). Boundary: one shared key is correct only when all answers are identical for all users.
I. Missing prerequisite: B-P14 (TTL is not authorization). Repair: re-read the TTL trap, then explain why expiry never replaces key scope.

## CB-02. Hit-time authorization after revocation. Correct: A, B.

A. Correct options: A, B.
B. Decisive sentence: the requirement is "cached answers must stop serving at 17:00" with "no full flush," and only per-hit checks plus targeted purge meet both.
C. Set matrix (plausible exact-cardinality combinations).

| Combination | Supported | All hard constraints | Objective fit | Missing or contradictory element | Retain or reject |
|---|---|---|---|---|---|
| A plus B | Yes | Yes | Yes | None | Retain |
| A plus C | Yes | No | No | Longer TTL fights immediate revocation | Reject |
| B plus D | No | No | No | D removes tenant scope, the leak class itself | Reject |
| A plus E | Yes | No | No | A prompt cannot enforce serving. The cache serves before the model runs | Reject |

D. A plus B wins because the hit-time check enforces revocation instantly and the targeted purge removes the entries, while other tenants keep their cache warm.
E. C fails: longer TTL extends the exposure window. D fails: it deletes the tenant boundary. E fails: the prompt runs after the cache hit, so it cannot block a served answer. F fails: it kills the product to fix the cache.
F. Counterfactual: a full flush becomes correct if tenants were few and revocations rare. The stem rules that out by cost.
G. L10 tenant-key rule and purge-on-update [Behavior]. Hit-time authorization is standard access-control practice [Behavior].
H. Rule: enforce revocation at read time, not at expiry time. Boundary: TTL bounds staleness, never access.
I. Missing prerequisite: B-P14. Repair: write the two-sentence difference between expiry and authorization, then re-grade.

## CB-03. Prompt version in the cache key. Correct: A.

A. Correct option: A.
B. Decisive sentence: the requirement is "answers always come from the current prompt version" with "no wasteful full flush."
C. Requirement matrix. Version-correct answers: A pass, B pass, C fail, D pass. No wasteful flush: A pass, B fail, C pass, D fail.
D. A wins because version in the key routes v2 traffic to v2 entries only, and old entries age out by TTL instead of a destructive flush.
E. B fails the waste constraint: it throws away every tenant's warm entries on each deploy. C fails: temperature changes variety, not version routing. D fails: it deletes the cost saving the cache exists for.
F. Counterfactual: B becomes correct if the cache held only one prompt's entries and deploys were rare.
G. L10 prompt-version keys [Behavior]. L4 pin rule (model plus prompt version) [Behavior].
H. Rule: the cache key must name every input that changes the answer, including the prompt version. Boundary: flushing is for emergencies, not deploys.
I. Missing prerequisite: L4 pin rule. Repair: explain why "same prompt text, new version" still needs key separation.

## CB-04. Role-scoped answers. Correct: A.

A. Correct option: A.
B. Decisive sentence: the requirement is "manager-only salary bands must never reach employees," and only key scope plus a hit-time role check enforces it.
C. Requirement matrix. Role leakage stopped: A pass, B partial, C fail, D fail. Cache kept: A pass, B pass, C pass, D pass.
D. A wins because the leak happens at the cache hit, before any output filter runs. B is feasible but inferior: redaction after a wrong-role hit is a second net, not the boundary.
E. C fails: 5 minutes still leaks 5 minutes of salary bands. D fails: model size never caused the leak.
F. Counterfactual: B becomes the correct second layer in a defense-in-depth design, but never the only layer.
G. Bridge B-P07 (ABAC) [Behavior]. L10 key-scope rule [Behavior].
H. Rule: authorization decisions happen before the data moves, at retrieval and at cache-hit time. Boundary: output filtering is remediation, not access control.
I. Missing prerequisite: B-P07. Repair: name the enforcement layer for "managers only" in one sentence.

## CB-05. Fallback must preserve the tool contract. Correct: A.

A. Correct option: A.
B. Decisive sentence: the requirement is "the agent keeps working through failover," and the agent works only when the tool-use contract holds.
C. Requirement matrix. Agent functional on fallback: A pass, B fail, C fail, D fail. Automatic failover: A pass, B fail, C pass, D fail.
D. A wins because it states the real choice: same contract on the fallback tier, or a different tested flow. Both keep the agent coherent.
E. B fails: infinite retry on a dead primary is an outage, not a fallback. C fails: timeouts do not add tool support. D fails: it abandons the product during every outage.
F. Counterfactual: B becomes correct if the outage were a 30-second blip, not a failover event.
G. L1 degradation ladder [Behavior]. Converse tool-use blocks are provider-specific [Version-dependent].
H. Rule: a fallback must preserve every contract the app depends on, or switch to a flow tested without it. Boundary: graceful degradation never means silently broken.
I. Missing prerequisite: L5 tool loop. Repair: list the three things the agent loop assumes about the model (tool blocks, schema, stop behavior).

## CB-06. Fallback must preserve residency. Correct: A.

A. Correct option: A.
B. Decisive sentence: the requirement is "EU tenant data stays in EU Regions at all times," and "at all times" includes failover.
C. Requirement matrix. Residency holds during outage: A pass, B fail, C pass, D fail. Service stays useful: A pass, B pass, C fail, D pass.
D. A wins because it keeps both requirements: EU-only fallback targets, or an honest static answer when no EU capacity exists.
E. B fails: "best-effort" rewrites a hard requirement into a preference. C fails: no fallback is an availability failure. D fails: it moves EU data to the US, the exact violation.
F. Counterfactual: B becomes correct only if the contract allowed cross-border processing during declared disasters, which it does not.
G. Patch P-G09, L1 cross-region compliance flag [Behavior].
H. Rule: hard requirements survive failover. Boundary: a fallback that breaks a hard rule is not a fallback, it is a violation path.
I. Missing prerequisite: patch P-G09. Repair: state in one sentence where Bedrock inference executes.

## CB-07. Fallback tier properties. Correct: A, B.

A. Correct options: A, B.
B. Decisive sentence: the requirement is "what every tier must guarantee" for a medical helper, and only safety and contract compatibility are guarantees.
C. Set matrix.

| Combination | Supported | All hard constraints | Objective fit | Missing or contradictory element | Retain or reject |
|---|---|---|---|---|---|
| A plus B | Yes | Yes | Yes | None | Retain |
| A plus C | Yes | No | No | Cheaper is an objective, not a guarantee. A tier can cost more and still be correct | Reject |
| B plus D | Yes | No | No | Provider diversity is a tactic, not a property | Reject |
| A plus E | No | No | No | Skipping logging breaks audit on the tier that needs it most | Reject |

D. A plus B wins because safety and contract are the two properties users and regulators rely on at 3 AM, on every tier.
E. C fails: cost is optimized, not guaranteed. D fails: same provider with two Regions is a fine fallback. E fails: it destroys forensics during the incident. F fails: speed is a goal, not a guarantee.
F. Counterfactual: C joins the set only if the objective were cost-first, which the medical context forbids.
G. L1 graceful degradation [Behavior]. L8 layered safety [Behavior].
H. Rule: guarantees travel down the fallback chain. Preferences do not. Boundary: never trade a mandatory requirement for a cheaper tier.
I. Missing prerequisite: L1 degradation ladder. Repair: rank safety, contract, cost, speed for a medical helper in one line.

## CB-08. Guardrails on every tier. Correct: A.

A. Correct option: A.
B. Decisive sentence: the requirement is "harmful outputs must stay blocked during outages too."
C. Requirement matrix. Blocked on every path: A pass, B fail, C pass, D fail. Tested before the outage: A pass, B fail, C pass, D fail.
D. A wins because it closes the exact gap the incident exposed, and adversarial testing proves the fallback path before the next outage.
E. B fails: rare is not never, and the incident already happened once. C fails: it deletes availability to buy safety, a false choice. D fails: logging is detection, and the requirement is prevention.
F. Counterfactual: D becomes a useful second control beside A, never instead of it.
G. L8 defense in depth [Behavior]. Guardrails attach per invocation path [Behavior].
H. Rule: every invocation path carries the same safety policy. Boundary: an untested fallback path is an unguarded path.
I. Missing prerequisite: L8 layered controls. Repair: name the three layers that must exist on the fallback path.

## CB-09. Stale pricing runbook. Correct: A.

A. Correct option: A.
B. Decisive sentence: the requirement is "a correctly sized commitment," and only current terms size it correctly.
C. Requirement matrix. Sized from true terms: A pass, B fail, C fail, D pass. Commits spend wisely: A pass, B fail, C fail, D fail.
D. A wins because pricing models change and the commitment is real money.
E. B fails: "rarely change" is not "never change," and the docs already changed. C fails: it commits first and learns later, the expensive order. D fails: it avoids the decision instead of verifying it.
F. Counterfactual: B becomes correct if the team verified the runbook against current docs this quarter.
G. Current AWS pricing pages at claim time [Version-dependent]. The addendum requires dated verification for pricing claims.
H. Rule: verify dated facts in current docs before committing spend. Boundary: a runbook is a starting point, never a price quote.
I. Missing prerequisite: L6 deployment ladder. Repair: state the current provisioned-throughput billing shape in one sentence from the docs.

## CB-10. Stale Region-availability note. Correct: A.

A. Correct option: A.
B. Decisive sentence: the requirement is "the simplest correct routing," and current availability decides it.
C. Requirement matrix. EU served correctly: A pass, B pass, C pass, D pass. Simplest correct: A pass, B fail, C fail, D fail.
D. A wins because a local model removes a cross-region hop, its latency, and its data-movement question.
E. B fails: it pays the hop forever to honor a stale note. C fails: it changes the model to dodge a lookup. D fails: the hop adds latency and moves data across borders for no reason.
F. Counterfactual: B becomes correct if current docs still showed the model absent in eu-west-1.
G. Current AWS Regional availability tables [Version-dependent].
H. Rule: recheck availability before designing around absence. Boundary: absence in an old note is not absence today.
I. Missing prerequisite: L1 model selection. Repair: name the four model-selection axes and mark which one the note got wrong.

## CB-11. Stale agent-loop limit. Correct: A.

A. Correct option: A.
B. Decisive sentence: the requirement is "a design that works under current limits," and only the current docs state them.
C. Requirement matrix. Works today: A pass, B fail, C fail, D fail. Task still completes: A pass, B pass, C fail, D fail.
D. A wins because checkpointed runs with persisted state complete 150 steps under any per-run cap.
E. B fails: the docs already state a lower maximum. C fails: config cannot grant what the platform denies. D fails: it removes the runaway protection L5 requires.
F. Counterfactual: C becomes correct if the current docs confirm the 200-step cap.
G. Current Bedrock Agents quotas [Version-dependent]. L5 max-steps rule [Behavior].
H. Rule: design to the documented limit, not the remembered one. Boundary: a blog is evidence of the past, not the present.
I. Missing prerequisite: L5 safeguards. Repair: explain why checkpointing beats hoping, in one sentence.

## CB-12. Stale streaming-API claim. Correct: A.

A. Correct option: A.
B. Decisive sentence: the requirement is "the simplest correct streaming path," and a native API beats hand-rolled polling.
C. Requirement matrix. True streaming: A pass, B fail, C fail, D fail. Least custom code: A pass, B fail, C fail, D pass.
D. A wins because ConverseStream removes the polling code, its bugs, and its maintenance.
E. B fails: it keeps dead code to honor a stale tutorial. C fails: faster polling is still polling, with worse load. D fails: it drops the TTFT requirement.
F. Counterfactual: B becomes correct if current docs showed no streaming variant.
G. Current Bedrock API reference [Version-dependent]. L6 streaming table [Behavior].
H. Rule: verify the API surface before building around its absence. Boundary: tutorial age matters as much as tutorial quality.
I. Missing prerequisite: L6 streaming. Repair: name the two Bedrock streaming APIs and their IAM actions.

## CB-13. Retry storm, reworded. Correct: A.

A. Correct option: A.
B. Decisive sentence: the requirement is "calm the retry wave and keep answers flowing," and only spread retries plus a degraded path do both.
C. Requirement matrix. Wave calmed: A pass, B fail, C fail, D fail. Users served during lag: A pass, B fail, C fail, D fail.
D. A wins because jitter desynchronizes the retries and the degraded path covers the failures that remain.
E. B fails: instant retries are the wave. C fails: logs watch the outage. They do not fix it. D fails: window size never caused throttling.
F. Counterfactual: B becomes correct if failures were rare and isolated, not a correlated wave.
G. L6 backoff and fallback [Behavior]. Same mechanism as Q30, reworded to test transfer (axis C29).
H. Rule: name the mechanism, not the keyword. Boundary: "retry storm," "thundering herd," and "correlated retries" are one phenomenon.
I. Missing prerequisite: L6 resilience. Repair: explain in one sentence why jitter helps when backoff alone does not.

## CB-14. Literal plus reworded search, reworded. Correct: A.

A. Correct option: A.
B. Decisive sentence: the requirement is "catch both signal types in one ranked list."
C. Requirement matrix. Literal codes caught: A pass, B partial, C fail, D fail. Rewordings caught: A pass, B fail, C fail, D partial. One ranked list: A pass, B fail, C fail, D fail.
D. A wins because hybrid catches both signals and the reranker fixes the ranking that raw score fusion gets wrong.
E. B fails: bigger chunks dilute literal matches. C fails: temperature is a generation dial, unrelated to retrieval. D fails: dimensions alone do not add literal matching.
F. Counterfactual: D becomes useful only beside a literal index, never alone.
G. L3 hybrid search and reranking [Behavior]. Same mechanism as Q12, reworded (axis C29).
H. Rule: match the retrieval method to the query shape, not to the vocabulary of the question. Boundary: "literal" and "exact code" name one need.
I. Missing prerequisite: L3 retrieval. Repair: state when hybrid beats pure vector in one sentence.

## CB-15. Policy evaluation, reworded. Correct: A.

A. Correct option: A.
B. Decisive sentence: the requirement is "the endpoint restriction and the data boundary, both enforced."
C. Requirement matrix. Endpoint restriction: A pass, B fail, C fail, D fail. Billing table blocked: A pass, B fail, C fail, D fail. Least privilege: A pass, B fail, C fail, D fail.
D. A wins because the condition pins the network path and the explicit deny defeats any allow on the billing table.
E. B fails: no condition means any network path, and all tables are open. C fails: it is the opposite of least privilege. D fails: no policy means default deny for the role's own calls and no boundary at all.
F. Counterfactual: B becomes correct if the requirement dropped both the endpoint rule and the billing boundary.
G. L9 five-checkpoint evaluation [Behavior]. Same mechanism as Q38 on new services (axis C29).
H. Rule: read the mechanism across service names. Boundary: a condition plus a deny travels. The service name does not matter.
I. Missing prerequisite: L9 policy evaluation. Repair: evaluate draft A layer by layer in four lines.

## CB-16. First-word latency, reworded. Correct: A.

A. Correct option: A.
B. Decisive sentence: the requirement is "cut the wait for the first word" with "the model cannot change."
C. Requirement matrix. First word sooner: A pass, B fail, C fail, D fail. Model unchanged: A pass, B pass, C pass, D pass. Fits chat: A pass, B pass, C fail, D pass.
D. A wins because streaming attacks perceived latency and pre-computation attacks real latency, both without touching the model.
E. B fails: bigger windows slow generation. C fails: batch is async and never serves chat. D fails: temperature changes variety, not speed.
F. Counterfactual: C becomes correct for the nightly digest job, never for chat.
G. L10 streaming and pre-computation [Behavior]. Same mechanism as Q49, reworded (axis C29).
H. Rule: perceived latency and real latency are different targets with different tools. Boundary: "first paint of text" and "TTFT" name one metric.
I. Missing prerequisite: L10 latency levers. Repair: name which lever attacks perceived vs real latency.

## CB-17. Absolute residency vs Bedrock. Correct: A.

A. Correct option: A.
B. Decisive sentence: the two hard requirements contradict because Bedrock inference executes in an AWS Region.
C. Requirement matrix. Compliant with rule 1: A pass (by escalation), B fail, C fail, D fail. Uses Bedrock: A fail (as stated), B pass, C fail, D pass. Honest about the conflict: A pass, B fail, C fail, D fail.
D. A wins because it is the only option that does not invent a feasible answer. The addendum forbids inventing feasibility for contradictory requirements.
E. B fails: this is the Q27-shaped answer, but Q27's stem allowed data at rest plus private transit. This stem says "never be processed outside," which Bedrock violates. C fails: Wavelength is edge compute, not residency. D fails: TLS does not change processing geography.
F. Counterfactual: B becomes correct if rule 1 softened to "data at rest stays in the building," which is exactly the fixed Q27.
G. Patch P-G09 [Behavior]. L9 endpoint-vs-Region rule [Behavior].
H. Rule: when hard requirements contradict, say so and escalate. Boundary: never ship a "compliant" architecture that quietly violates a hard rule.
I. Missing prerequisite: patch P-G09. Repair: state where Bedrock inference executes, in one sentence.

## CB-18. Tool latency vs p99 budget. Correct: A.

A. Correct option: A.
B. Decisive sentence: the 2-second tool alone exceeds the 500 ms budget on every request, so no tuning meets both.
C. Requirement matrix. Honest about infeasibility: A pass, B fail, C fail, D fail. Offers a real path: A pass, B fail, C fail, D fail.
D. A wins because arithmetic is not negotiable: p99 cannot be under 500 ms when every request waits 2 seconds.
E. B fails: retries add latency. They never remove the 2 seconds. C fails: model size does not change tool time. D fails: streaming the tool output still starts after 2 seconds.
F. Counterfactual: A becomes a design task if the tool moved off the critical path (async, cache, pre-compute).
G. L6 p99 budget math [Behavior].
H. Rule: check the arithmetic before the architecture. Boundary: a p99 target and a fixed serial latency either fit or they do not.
I. Missing prerequisite: L6 latency budget. Repair: compute the minimum possible p99 given a 2-second serial tool.

## CB-19. Zero retention vs full replay. Correct: A, B.

A. Correct options: A, B.
B. Decisive sentence: the requirement is "a truthful statement of what the requirement set allows," and only naming the contradiction plus the way out is truthful.
C. Set matrix.

| Combination | Supported | All hard constraints | Objective fit | Missing or contradictory element | Retain or reject |
|---|---|---|---|---|---|
| A plus B | Yes | Yes | Yes | None | Retain |
| A plus C | Yes | No | No | Encryption changes storage safety, not the retention contradiction | Reject |
| B plus E | Yes | No | No | Faster deletion deepens the replay problem | Reject |
| C plus D | Yes | No | No | Effort does not resolve a logical contradiction | Reject |

D. A plus B wins because A names the conflict and B names the only exits: keep hashes and metadata, or drop replay.
E. C fails: encrypted storage is still storage, and it still cannot replay what was never kept. D fails: hope is not architecture. E fails: it satisfies rule 1 harder while breaking rule 2 harder. F fails: renaming storage does not change retention.
F. Counterfactual: the set becomes feasible if "replay" is redefined as "replay from hashes and metadata," which is exactly option B's first exit.
G. L9 decision logs, L10 log minimization [Behavior].
H. Rule: a contradiction is a finding, not a design task. Boundary: never rename a control to pretend a rule holds.
I. Missing prerequisite: L9 governance. Repair: write the two rules as formal statements and derive the contradiction in three lines.

## CB-20. Real-time chat vs batch inference. Correct: A.

A. Correct option: A.
B. Decisive sentence: the two requirements contradict because batch inference is async by design and never serves a chat user.
C. Requirement matrix. Real-time streaming: A pass (by choosing), B fail, C fail, D fail. Lowest cost: A partial (by choosing), B pass, C pass, D fail. Honest: A pass, B fail, C fail, D fail.
D. A wins because it refuses the false compromise and names the real choice: streaming on on-demand or provisioned, or batch without real-time chat.
E. B fails: polling a batch job is latency theater. The job still completes in minutes. C fails: bigger batches are slower, not faster. D fails: the S3 file appears when the job ends, not token by token.
F. Counterfactual: the set becomes feasible if "chat" is redefined as "answers within the hour," which is not chat.
G. L6 batch inference [Behavior].
H. Rule: deployment modes hold fixed shapes. Requirements fit the shape or the design fails. Boundary: cost never converts batch into real-time.
I. Missing prerequisite: L6 deployment ladder. Repair: state the batch inference contract (async, S3, cheapest) in one sentence.

---

*End of answers. Grade only from this file. Question file carries no answer material.*

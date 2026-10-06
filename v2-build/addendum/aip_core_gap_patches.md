# AIP-C01 Core Gap Patches v1.0

Research date: 2026-10-06. Rule: each patch inserts at one exact anchor. No patch rewrites its host lesson. Anchors are h3 ids verified to exist in the named fragment. The assembler applies patches in patch-ID order. Claim labels: [Guide], [Behavior], [Version-dependent].

---

## P-G01. Decision records and cross-environment validation (skill 1.1.3)

Anchor: after <h3 id="l1-limits"> in fragments/d1-lessons.html (insert before <h3 id="l1-closest">).

Patch text:

<p><b>Decision records.</b> A decision record is a short written note per architectural choice: the requirement, the options, the winner, and why. Skill 1.1.3 wants standardized reusable components across environments, and records are what make the tenth deployment match the first. Store the record with the component version. A reviewer in the next Region reads the record instead of re-deciding.</p>
<p><b>Cross-environment validation.</b> A component that passes in one environment can fail in the next. Validate three things per environment: compatibility (the model and APIs exist in that Region), policy (the data rules of that jurisdiction hold), and configuration (quotas and endpoints match). A component is not portable until all three pass.</p>
<p class="trap">Trap: "It worked in us-east-1" is not portability proof. Regions differ in model availability, and jurisdictions differ in data rules.</p>

Validation: L12 W6 (resilience and fallback design) reuses the three-check rule.

## P-G02. Capability detection on model or provider switch (skill 1.2.2)

Anchor: after <h3 id="l1-closest"> in fragments/d1-lessons.html (insert before <h3 id="l1-arch">).

Patch text:

<p><b>Capability detection.</b> Config-driven routing (L1) moves the model choice to config, but the new target must support what the app uses. Before the flip, check the capability contract: streaming API shape, tool-use blocks, context window, Region availability, and quota. A model that lacks tool use breaks an agent that the old model served fine. Detect, do not assume.</p>
<p><b>Template check.</b> Prompt templates carry model-specific syntax (L4). A template written for one provider's Converse schema may misbehave on another provider's raw API. Pin the template version to the model version (L4 rule) and re-run the golden set on the switch.</p>
<p class="trap">Trap: "The config flip worked" means traffic moved. It does not mean the new model supports every feature the old one did. Q7 tests the normalized contract for exactly this reason.</p>

Validation: qbank Q7 (Converse migration) and Q2 (cross-Region profile) exercise the check.

## P-G03. Ingestion sidecars and provenance schemas (skill 1.4.2)

Anchor: before <h3 id="l3-limits"> in fragments/d1-lessons.html (insert at end of the l3-aws section).

Patch text:

<p><b>Three metadata mechanisms.</b> S3 object metadata travels with the object (timestamps, content type). Tags label the object for cost and policy (domain, tenant). An ingestion sidecar is a separate small file written next to the source at ingest time: it holds provenance the source cannot carry, such as the extractor version, the parse warnings, and the ingest timestamp. Three mechanisms, three jobs. Do not store provenance in the prompt and call it metadata.</p>
<p><b>Provenance schema.</b> Every chunk answers four questions: who wrote it (author), when (timestamp), whose data it is (tenant_id), and where it came from (source_uri). Define the four fields once, enforce them at ingest, and filter on them at retrieval (L3 tenant filter). A chunk without tenant_id is a leak waiting for a query.</p>
<p class="trap">Trap: tags are for labeling and policy, not for long provenance text. Provenance belongs in metadata or a sidecar, where retrieval filters can read it.</p>

Validation: L11 contract tests check the output schema, which now includes provenance fields.

## P-G04. Delete propagation and embedding-model changes (skills 1.4.3-1.4.5)

Anchor: before <h3 id="l3-check"> in fragments/d1-lessons.html (insert at end of the l3-limits section).

Patch text:

<p><b>Delete propagation.</b> One delete is four deletes (bridge B-P13). The sync pipeline must propagate each layer: S3 delete removes the object, index delete removes the vector entry, cache purge removes stored answers by tenant key, and the log-retention rule bounds the evidence trail. A pipeline that syncs adds but never syncs deletes serves ghost chunks: the source is gone, the answer remains.</p>
<p><b>Embedding-model change.</b> Vectors from model A live in A's space. Vectors from model B live in B's space. The spaces do not mix. Swapping the embedding model without a full reindex corrupts every similarity score (qbank Q11). The change checklist: new model, full re-embed, full reindex, golden-set re-run, then cutover. There is no partial upgrade.</p>
<p class="trap">Trap: "We only changed the embedding model" still needs a full reindex. The index is the model's output, not independent data.</p>

Validation: qbank Q11 tests the embedding-swap failure. Q20 tests the erasure path.

## P-G05. Bounded clarification and the no-tool-yet rule (skill 1.6.2)

Anchor: after <h3 id="l4-closest"> in fragments/d1-lessons.html (insert before <h3 id="l4-arch">).

Patch text:

<p><b>Bounded clarification.</b> A clarification workflow asks one question per ambiguity, then stops. Cap the turns: two follow-ups, then the system acts on its best reading and says what it assumed. An unbounded loop asks forever and the user leaves. Store each answer in session state (L4) so the model never re-asks.</p>
<p><b>The no-tool-yet rule.</b> When intent is unclear, do not call tools yet. A tool call with a guessed argument is a side effect built on a guess: the wrong order refunded, the wrong record deleted. Clarify first, then call. The workflow enforces the order (bridge B-P18): the choice state routes unclear intents to the clarification branch, and the tool states sit behind it.</p>
<p class="trap">Trap: "The model can clarify by calling the lookup tool first." A lookup on a guessed entity leaks or corrupts. Questions are cheap. Tool calls are not.</p>

Validation: L4 check Q3 (clarification design) now grades the bound and the order.

## P-G06. Prompt A/B testing: native vs custom (skills 1.6.3-1.6.6)

Anchor: before <h3 id="l4-arch"> in fragments/d1-lessons.html (insert at end of the l4-closest section).

Patch text:

<p><b>Prompt A/B testing.</b> An A/B test serves prompt version A to some traffic and version B to the rest, then compares golden-set scores and live metrics. The native path uses Prompt Management versions plus gateway routing (L7): no new code, the split is configuration. The custom path splits in application code: full control, but you own the traffic split, the metric join, and the cleanup. Both need the L4 pin rule: model version plus prompt version, or the test measures two changes at once.</p>
<p><b>Choose.</b> Choose the native path when the gateway and Prompt Management already serve traffic. Choose custom only when the split needs logic the gateway cannot express (per-tenant splits with custom attributes).</p>
<p class="trap">Trap: an A/B test that changes the prompt and the model together proves nothing about either. Pin one, vary one.</p>

Validation: L10 per-use-case tuning (4.2.4) references this patch for temperature A/B tests.

## P-G08. Human review beyond yes/no: state, artifacts, timeout, escalation, binding (skill 2.1.5)

Anchor: after <h3 id="l5-limits"> in fragments/d2-lessons.html (insert before <h3 id="l5-closest">).

Patch text:

<p><b>Review state.</b> A human review is a workflow state, not a button. The state holds: the proposed action, the artifacts (the order, the policy clause, the tool arguments), the requester, and the deadline. The reviewer decides on the artifacts, not on a one-line summary.</p>
<p><b>Timeout and escalation.</b> Every review state has a timeout. On timeout, the workflow escalates (a second reviewer, a manager) or fails closed (the action is denied). "Wait forever" is not a design. The L0 rule applies: Step Functions holds the wait, Lambda never does.</p>
<p><b>Exact action binding.</b> The approval binds to the exact action: refund order 88231 for $120.00, not "a refund". If the agent changes the amount after approval, the approval no longer covers it. Re-approval is required. An approval for "the refund" that the agent edits into a larger refund is a bypass.</p>
<p class="trap">Trap: a human who approves without seeing the tool arguments approved a blank check. Artifacts are the approval.</p>

Validation: qbank Q33 (refund approval design) grades the binding. L5 check Q3 grades the wait holder.

## P-G09. CORRECTION. Outposts, Wavelength, and where Bedrock inference runs (skill 2.3.4)

Type: correction. Two inserts in fragments/d2-lessons.html. Do not edit any other text.

Insert 1. Anchor: after <h3 id="l7-limits"> (insert before <h3 id="l7-closest">).

Patch text:

<p><b>Correction: where the inference runs.</b> Bedrock is a regional AWS service. It does not run natively on Outposts. Outposts keeps your data, your application, and your processing on premises. When the app calls Bedrock, the request travels to the AWS Region and the model runs there. A private link (Direct Connect plus VPC endpoints) protects the request in transit. It does not change where the inference executes. If the jurisdiction rule forbids any processing outside the building, Bedrock is infeasible for that data: self-host the model on Outposts (SageMaker) instead. Network path and processing location are separate (L9 rule). [Behavior]</p>
<p><b>Wavelength boundary.</b> Wavelength puts compute at the mobile edge for low latency. It is not on-premises data residency and it does not hold regulated data on premises (L7 limits). Choose Wavelength for edge latency, Outposts for on-premises data, and neither as a way to run Bedrock outside a Region.</p>

Insert 2. Anchor: replace the answer block of L7 check Q1 exactly. Existing text to replace:

<div class="answer"><p>Correct: Outposts: it runs AWS services on premises, so the data stays in the building. Wavelength fails: it is edge compute for low latency, not on-premises data residency.</p></div>

Replacement text:

<div class="answer"><p>Correct: Outposts for the data and the app, with a private route to Bedrock in-Region. Outposts runs AWS services on premises, so records at rest stay in the building. But Bedrock inference executes in the AWS Region, not on Outposts: prompt content is processed in-Region, and the private link protects transit only. If the rule forbids any off-premises processing, Bedrock is infeasible and the model must be self-hosted on Outposts. Wavelength fails: it is edge compute for low latency, not on-premises data residency.</p></div>

Validation: qbank Q27 was fixed in place to match this boundary. The C05/C06 curveballs (CB-17..CB-20) test it.

## P-G11. Q Developer assistance vs verified diagnosis (skills 2.5.3/2.5.4/2.5.6)

Anchor: before <h3 id="l7-arch"> in fragments/d2-lessons.html (insert at end of the l7-closest section).

Patch text:

<p><b>Assistance vs diagnosis.</b> Q Developer assists: it writes code, suggests APIs, and flags likely slow paths and error patterns. Assistance is a suggestion. A diagnosis is verified: the fix is proven by a test, a trace, or a metric. The workflow is suggest, then verify. A Q Developer flag that "this looks like a throttling error" becomes a diagnosis only when the X-Ray trace shows the throttled call and the retry metric drops after the fix.</p>
<p><b>BDA mapping.</b> Bedrock Data Automation orchestrates document processing (skill 2.5.3): extraction, transformation, and routing across document types. It is the managed path. A hand-rolled Lambda chain is the custom path (L2 closest-alternative rule). Map the use case first: standard documents fit BDA, exotic layouts need custom steps.</p>
<p class="trap">Trap: "Q Developer found the bug" without a confirming test is still a hypothesis. The exam rewards the verification step, not the suggestion.</p>

Validation: L11 playbooks (5.2.2/5.2.6) require trace or metric evidence per diagnosis.

## P-G12. Deterministic execution vs probabilistic interpretation, and text-to-SQL discipline (skills 3.1.2-3.1.4)

Anchor: after <h3 id="l8-limits"> in fragments/d3-lessons.html (insert before <h3 id="l8-closest">).

Patch text:

<p><b>Deterministic vs probabilistic.</b> Some steps must be deterministic: schema validation, arithmetic, business-rule checks, and authorization. A model interpreting a rule is probabilistic: it usually applies the rule, sometimes it does not. Put deterministic steps in code (Lambda, policy engine). Let the model do language. Never let the model be the only enforcement of a money rule.</p>
<p><b>Text-to-SQL discipline.</b> A model that writes SQL generated text, not an authorized query. Four gates stand between the words and the database: the SQL parses against the schema, the query passes business validation (no DELETE without approval), the caller is authorized for the tables and rows (B-P07), and execution runs with least-privilege credentials on a read replica where writes are forbidden. Generated SQL that skips any gate is a suggestion with a database password.</p>
<p class="trap">Trap: "The model wrote correct SQL" answers generation. Authorization, validation, and execution are separate gates, and each can fail while the SQL is perfect.</p>

Validation: L11 structured-output playbook (5.2.3) references the schema gate.

## P-G13. Lineage as audit evidence (skills 3.3.1-3.3.4)

Anchor: after <h3 id="l9-limits"> in fragments/d3-lessons.html (insert before <h3 id="l9-closest">).

Patch text:

<p><b>The evidence chain.</b> A regulator asks "which data trained this model and which version serves each request." Three links answer together. The Glue Data Catalog registers the sources. Glue lineage tracks each dataset from source tables to the training data: machine-readable, not a wiki. Model cards bind the training data, the version, and the limits in code-readable form. Decision logs record which prompt and model version answered each request. One link alone fails the audit: the catalog without lineage cannot trace, lineage without the card cannot bind the version, the card without decision logs cannot replay.</p>
<p><b>Evidence, not service names.</b> Listing Glue, SageMaker, and CloudTrail is not an answer. The answer is the joined evidence: source to dataset (lineage), dataset to model (card), model version to request (decision log). Build the joins in the pipeline, or the audit assembles them by hand.</p>
<p class="trap">Trap: "CloudTrail proves our training data." CloudTrail proves API calls. Lineage proves data origin (qbank Q41).</p>

Validation: qbank Q41 tests the full chain.

## P-G14. Traces are not proof, and native vs custom metrics (skills 3.4.1-3.4.3)

Anchor: before <h3 id="l9-arch"> in fragments/d3-lessons.html (insert at end of the l9-closest section).

Patch text:

<p><b>Traces are not proof.</b> An inspectable agent trace shows what the model said it did. A model can produce a clean, plausible trace for a wrong answer: the reasoning display is generated text, not a recording of thought. Treat traces as debugging input, not correctness evidence. Correctness evidence is independent: grounding checks, golden-set scores, human review of the artifacts.</p>
<p><b>Native vs custom metrics.</b> Native metrics come from the service: Bedrock invocation counts, Guardrails block rates. Custom metrics come from your code: faithfulness scores, per-tenant quality, business outcomes. Define fairness and uncertainty metrics up front (L9), publish them as custom CloudWatch metrics (L10), and never present a native operational metric as a quality metric. Token counts do not measure fairness.</p>
<p class="trap">Trap: "The trace looks reasonable, so the answer is right." Reasonable-looking is what language models produce by default, including when wrong.</p>

Validation: L11 faithfulness checks (5.1.5) are the independent evidence for traces.

## P-G15. Hash collisions and normalization in deterministic caching (skill 4.1.4)

Anchor: after <h3 id="l10-limits"> in fragments/d4d5-lessons.html (insert before <h3 id="l10-closest">).

Patch text:

<p><b>Collisions.</b> Deterministic request hashing serves byte-identical repeats from the hash. A hash collision means two different requests share one hash, and the second request gets the first request's answer. With a 64-bit hash and 1M cached requests, the collision chance is about 1 in 36 million: tiny, but not zero. The defense is key design: hash the normalized request plus the tenant ID plus the prompt version plus the model ID. A collision then needs the same tenant, version, and model too.</p>
<p><b>Normalization.</b> Hash the canonical form, not the raw bytes. Sort JSON keys, strip insignificant whitespace, lowercase nothing the model treats as significant. Without normalization, two identical questions in different key order miss each other and the hit rate falls for no reason.</p>
<p class="trap">Trap: "Same hash means same request." It means probably the same request. The tenant and version in the key are what make "probably" safe.</p>

Validation: L10 cache-leakage playbook inspects key format. This patch adds the collision question to that inspection.

## P-G18. Feedback biases, stakeholder reports, measurable action (skills 5.1.3/5.1.8)

Anchor: after <h3 id="l11-limits"> in fragments/d4d5-lessons.html (insert before <h3 id="l11-closest">).

Patch text:

<p><b>Feedback biases.</b> User feedback is data with bias, not truth. Angry users rate more than happy ones (selection bias). Users rate the interface, not the answer (attribution bias). A 2.1 average rating can hide a 4.5 on easy questions and a 1.2 on the hard ones that matter. Slice ratings by question type, tenant, and difficulty before acting. Calibrate with the golden set: if users rate 2 stars but the golden set holds steady, the product changed, not the model.</p>
<p><b>Stakeholder reports and action.</b> A report compares: this release vs last, per segment, with the golden-set scores beside the user ratings. Every finding ends in a measurable action: "hard-question faithfulness fell 8 points, owner is the retrieval team, fix lands before the next release." A report with no owner and no date is a diary.</p>
<p class="trap">Trap: "Users love it, 4.6 stars" while the hard-question slice sits at 2.0. Averages hide the failures that churn accounts.</p>

Validation: bridge B-P23 (baselines) and L11 annotation workflow feed the calibration step.

## P-G19. Jointly versioned deployment gates (skill 5.1.9)

Anchor: before <h3 id="l11-arch"> in fragments/d4d5-lessons.html (insert at end of the l11-closest section).

Patch text:

<p><b>One release, four versions.</b> A GenAI release is a set: the model version, the prompt version, the index version (embeddings plus chunking), and the config version (thresholds, routing rules). The deployment gate pins all four as one release candidate. A model upgrade with a stale index is not a tested release: the vectors belong to the old model (patch P-G04). A prompt v4 with index v2 is not a tested release either.</p>
<p><b>The gate.</b> Synthetic user workflows run on the pinned set. Hallucination-rate and semantic-drift checks compare against the previous pinned set, not against a single component. Rollback restores the whole set: model, prompt, index, config. Rolling back the model alone while the index stays new is a new untested combination.</p>
<p class="trap">Trap: "We rolled back the model" while the prompt and index stayed on the new versions. That is not the old system. It is a third system nobody tested.</p>

Validation: L4 pin rule and patch P-G04 supply the version identities. Qbank Q58 tests the gate.

---

*End of patches. Assembler: insert each patch at its anchor in patch-ID order. P-G09 insert 2 is a replacement, not an addition.*

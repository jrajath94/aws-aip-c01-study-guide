# AIP-C01 Review Sheets v1.0

Date: 2026-10-06. Purpose: one-page recall per domain before timed practice.
Rule: each sheet names the decisions, not the prose. If a line needs
explanation, the lesson teaches it. No new claims appear here. Every claim
below is taught in the named lesson.

## D1 review sheet (31%, lessons L1-L4)

- Technique first: prompt, then RAG, then fine-tune. Climb one rung only when
  the lower rung fails a named test. (L1)
- Model selection: capability, cost, latency, regional availability. A model
  not served in your Region loses by default. (L1)
- Resilience: retry, switch Region, switch model, degrade. Cross-region
  inference adds latency and moves data across borders. (L1, patch P-G09)
- Data: validate before embed. Glue Data Quality for rules, SageMaker
  Processing for transforms, Transcribe/Textract/Comprehend/BDA for media.
  (L2)
- Vector stores: the index is the model's output. An embedding-model change
  forces a full reindex. Delete must propagate: object, index, cache, log.
  (L3, patch P-G04)
- Retrieval: chunk, embed, search, rerank. Diagnose retrieval and generation
  separately. (L3)
- Prompts: version, approve, pin with the model. A/B test before a prompt
  becomes default. Bounded clarification: no tool calls until intent is
  clear. (L4, patches P-G05, P-G06)

## D2 review sheet (26%, lessons L5-L7)

- Agents: loop of reason, act, observe. The state machine enforces the
  approval step, not the model's good intentions. (L5)
- Memory: session state in DynamoDB, summary memory, delete path. TTL is
  expiry, not an authorization boundary. (L5, bridge B-P14)
- Human in the loop: review state, artifacts, timeout, escalation, and the
  exact action bound to the approval. Not a bare yes button. (L5, patch P-G08)
- Deployment: on-demand for spiky, provisioned for steady, batch for bulk.
  Provisioned throughput is reserved capacity, not a discount. (L6)
- APIs: Converse unifies model calls. Streaming cuts time to first token, not
  full p99. (L6)
- Enterprise: GenAI gateway centralizes auth, logging, cost. CI/CD as code.
  Q Developer suggests, tests and traces verify. (L7, patch P-G11)
- Hybrid: Outposts keeps data at rest local. Wavelength serves edge latency.
  Bedrock inference runs in-Region, never on Outposts. Private path protects
  transit only. (L7, patch P-G09)

## D3 review sheet (20%, lessons L8-L9)

- Defense in depth: input filters, grounding, output filters, audit. One
  layer is not a system. (L8)
- Deterministic steps belong in code: schema, arithmetic, business rules,
  authorization. Generated SQL is not authorized execution. (L8, patch P-G12)
- Guardrails enforce your policy. They never certify legal compliance.
  (L8, L9)
- IAM: explicit deny wins. Cross-account needs both sides. External ID
  defeats the confused deputy. (L9)
- Encryption: envelope encryption, KMS key vs data key. Customer owns
  config, access, data. Vendor eligibility is not application compliance.
  (L9, bridge B-P03)
- Network: VPC endpoint keeps traffic private. It never moves data
  residency. The Region does that. (L9, patch P-G09)
- Privacy: Macie finds PII, never quarantines. Anonymization cuts risk,
  never guarantees it. (L9)
- Responsible AI: bias, transparency, uncertainty, human review. A trace is
  inspectable. It is not proof of correctness. (L9, patch P-G14)

## D4 review sheet (12%, lesson L10)

- Cost: tokens in plus tokens out times price. Cache the repeated prefix.
  Semantic cache needs a tenant-scoped key and hit-time authorization.
  (L10, patch P-G15)
- Hash collisions: two different requests can share one hash. Normalize and
  version the key. (L10, patch P-G15)
- Performance: benchmark p50 and p95, never the mean. Quota is not rate.
  A quota increase does not prove p99. (L10, bridge B-P32)
- Monitoring: metrics, logs, traces, audit. Tool-usage baselines with
  deviation alarms. Index health: latency, shards, freshness. (L10)

## D5 review sheet (11%, lesson L11)

- Eval: golden set locked, holdout locked, no leakage. Precision, recall, F1
  on retrieval. nDCG on ranking. LLM-as-a-judge has bias, calibrate it.
  (L11)
- Deployment gates: model plus prompt plus index pinned as one release.
  Synthetic users, hallucination rate, drift checks. (L11, patch P-G19)
- Feedback is data with bias, not truth. Measurable action per finding.
  (L11, patch P-G18)
- Troubleshooting: symptom, likely causes, evidence, diagnostic, fix, verify.
  Ten playbooks in lesson L11.

## Method sheet (L12 + senior playbook)

Study mode: name the ask and stage, quote constraints, name the layer, check
compatibility, eliminate infeasible options with the exact clause, rank
survivors on the stated objective, check boundaries end to end, verify the
whole scenario, state why losers lose, cite evidence and open assumptions.
Timed mode: ASK, MUST, LAYER, ELIMINATE, RANK, CHECK SET.

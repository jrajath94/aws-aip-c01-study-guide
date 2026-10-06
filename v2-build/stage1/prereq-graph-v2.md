# AIP-C01 Prerequisite Dependency Graph v2 (Stage 1)

Research date: 2026-10-06. Purpose: the minimum foundation knowledge the crash course must teach just-in-time so every Layer-A (mechanism + decision rule) explanation is understandable. This is a crash course, not a CCP course: teach only what the blueprint skills require, remediated inside the domain lesson that needs it.

## P1. Regions and Availability Zones

- **Which AIP-C01 concepts depend on it:** 1.2.2 (model switching without code changes), 1.2.3 (Cross-Region Inference, inference profiles), 2.3.4 (Outposts/Wavelength), 2.4.3 (resilience), D4 cost/performance trade-offs (region pricing differences).
- **Minimum necessary depth:** What a Region and an AZ are in one sentence each; why models are not available in every Region; the idea that a cross-region inference profile routes to a region where the model exists (prefixes like us./eu. name the home region); AZs only matter as "multiple failure domains."
- **Quick diagnostic question:** A company runs its chat app in us-east-1, but the model it wants is only served in us-west-2. What changes about the request routing, and what trade-off appears?
- **Remediation pointer:** Crash-course Lesson L0 (foundation ramp) + revisited inside D1 model-selection lesson.

## P2. Networking basics (VPC, PrivateLink/VPC endpoints)

- **Which AIP-C01 concepts depend on it:** 3.2.1 (VPC endpoints for Bedrock isolation), 2.4.2 (streaming via API Gateway), 2.5.1 (API Gateway limits), 4.2.1 (latency), 4.3.3 (forensic traceability).
- **Minimum necessary depth:** VPC = private network in the cloud; a VPC interface endpoint (PrivateLink) lets services talk to AWS APIs without crossing the public internet and without NAT; why compliance scenarios demand it. API Gateway and streaming basics at concept level only (front door + throttling + limits exist).
- **Quick diagnostic question:** A healthcare customer needs Bedrock calls that never leave the private network. What single AWS networking feature achieves this, and why does it matter for HIPAA-style compliance?
- **Remediation pointer:** D3 safety/security lesson (3.2.1), first teach of the concept; D1/D2 lessons reference it, not re-teach.

## P3. IAM policy evaluation

- **Which AIP-C01 concepts depend on it:** 2.1.3 (IAM resource boundaries for agents), 2.3.3 (RBAC, least privilege FM access), 3.2.1 (IAM policies for data access), 1.4.2/1.6.3 (access control over prompts/templates and KB metadata).
- **Minimum necessary depth:** Identity-based policy anatomy (effect, action, resource) in one example; explicit deny beats allow; least privilege principle; the idea of scoping a policy down to one model or one knowledge base; federation/SSO at concept level only.
- **Quick diagnostic question:** An agent needs to read one DynamoDB table and invoke one Bedrock model. Write the principle a secure policy follows, and name the one policy element that must never be left as "*".
- **Remediation pointer:** D3 safety/security lesson (3.2.1/2.3.3 taught there); agent-safeguard lesson in D2 references it.

## P4. Encryption and KMS

- **Which AIP-C01 concepts depend on it:** 3.2.2/3.2.3 (PII protection, privacy-preserving systems), model invocation logging (S3/CloudWatch destinations), 3.3.x (compliance).
- **Minimum necessary depth:** Encryption at rest vs in transit in two sentences; KMS = managed keys; the exam-level decision: turn on KMS encryption for invocation logs in regulated workloads, or disable logging when logs would hold PII. No key rotation mechanics, no envelope encryption math.
- **Quick diagnostic question:** A regulated workload logs every model invocation to S3. Name two compliant choices for the logs, and the risk of neither.
- **Remediation pointer:** D3 safety/security lesson alongside 3.2.2.

## P5. Compute limits and timeouts

- **Which AIP-C01 concepts depend on it:** 2.1.3 (Lambda timeouts vs Step Functions waits), 2.2.1/2.2.2 (deployment choices), 2.4.1-2.4.3 (streaming, retries), 4.1.3/4.2.x (batching, throughput), 1.4.5 (sync schedules).
- **Minimum necessary depth:** Lambda has a hard maximum runtime (minutes-scale) so it cannot do long waits - that is what Step Functions is for; API Gateway and Lambda impose payload/timeout limits relevant to streaming responses; batch inference is the async, cheapest pattern for non-interactive work; provisioned throughput is reserved capacity for steady load, not a cost saver for spiky traffic. Teach as decision rules, not numeric trivia. (Note: numeric limits change; the exam tests judgment, so teach the pattern: "which compute fits this duration/pattern," not exact seconds.)
- **Quick diagnostic question:** An agent workflow waits up to 2 hours for a human approval, then calls a model. Which two AWS compute services handle the wait and the model call respectively, and why can one service not do both?
- **Remediation pointer:** Crash-course Lesson L0 (foundation ramp) as the compute decision ladder; D2 agent lesson reuses it.

## P6. Storage basics (S3, DynamoDB)

- **Which AIP-C01 concepts depend on it:** 1.3.x (data pipelines in/out of S3), 1.4.1/1.4.2 (S3 as document repository; DynamoDB for metadata), 1.6.2/2.1.1 (DynamoDB for conversation history and agent memory), 3.2.2 (S3 Lifecycle retention), 4.1.4 (caching stores).
- **Minimum necessary depth:** S3 = durable object storage, source of truth for documents/datasets/logs, Lifecycle rules age data out; DynamoDB = fast key-value store, the right home for session state and conversation history (NOT a vector store, NOT the right home for binary documents); ElastiCache = ephemeral cache, fine for caching, wrong for durability. One-sentence rule per service on what it is FOR.
- **Quick diagnostic question:** An agent must remember a conversation for weeks and also store PDF source documents. Which two storage services do you pick, and why is one service for both jobs wrong?
- **Remediation pointer:** Crash-course Lesson L0 (foundation ramp); vector-store lessons in D1 reference the "DynamoDB is not a vector store" rule explicitly.

## P7. ML/AI basics (tokens, embeddings, temperature/top-p/top-k, agents, eval)

- **Which AIP-C01 concepts depend on it:** Nearly everything. Tokens: 4.1.1, 5.2.1, 1.5.1. Embeddings: 1.5.2, 4.1.4, 5.1.6. Temperature/top-p/top-k: 4.2.4, 5.1.x. Agents/tool use: 2.1.x. Fine-tuning vs RAG: 1.1.1, 1.2.4.
- **Minimum necessary depth:** Tokens = the units models read and are billed in (words split into pieces); context window = how much the model can see at once, larger costs more; embeddings = vectors capturing meaning, used for similarity search (NOT keywords); temperature/top-p/top-k = randomness controls, low for factual, higher for creative; agent = model that calls tools in a loop to complete tasks; fine-tuning changes weights (behavior baked in, needs labeled data), RAG adds knowledge at query time (no weight change); prompt engineering changes instructions only.
- **Quick diagnostic question:** Two scenarios: (a) support answers must cite the current product manual, updated monthly; (b) a million daily classification calls where each call costs too much. For each, choose prompt engineering, RAG, or fine-tuning, and give the one-sentence reason.
- **Remediation pointer:** Crash-course Lesson L0 (foundation ramp) - the AI basics ramp. Every later lesson assumes this; if the diagnostic fails, the learner loops back to L0, not forward.

## P8. Observability basics (metrics vs logs vs traces)

- **Which AIP-C01 concepts depend on it:** 4.3.x (monitoring), 5.2.x (troubleshooting), 3.3.4 (continuous monitoring), 1.3.1 (pipeline observability).
- **Minimum necessary depth:** Metrics (numbers over time - CloudWatch), logs (event text - CloudWatch Logs), traces (request journey across services - X-Ray), audit (who called what - CloudTrail). The exam's favorite distinction: CloudTrail is for audit, never for performance monitoring.
- **Quick diagnostic question:** Token spend spikes at 3am. Which CloudWatch capability finds it, and why is CloudTrail the wrong tool for this job?
- **Remediation pointer:** D4 monitoring lesson (4.3.x), first teach; D5 troubleshooting lesson references it.

## Dependency ordering for the crash-course lesson plan

L0 (foundation ramp) covers P1, P5, P6, P7, and the P8 one-liner — everything D1-D5 lessons assume. P2, P3, P4 are taught inside D3 (safety/security) where the blueprint first demands them, and referenced forward/backward from D1/D2 lessons that need them. P8 gets its full teach in D4 (monitoring). No prerequisite is taught twice in full; later lessons carry one-line callbacks.

## What this graph deliberately excludes

Advanced ML theory (gradients, backprop, attention math), data engineering internals, exact numeric service limits (teach as version-dependent), SDK syntax. The official guide lists model development/training, advanced ML techniques, and data/feature engineering as out of scope for the target candidate - this graph follows that boundary.

# AIP-C01 v2 First Diagnostics - ANSWER KEY (Stage 1)

Research date: 2026-10-06. This file is the hidden answer key for diagnostics-v2.md. Do not merge into the diagnostics file or publish alongside it.

All items are original exam-style practice questions. Not real exam content.

---

**A1.** The knowledge base with monthly sync is correct. Decisive reason: the knowledge changes monthly, so retrieval (RAG) with a sync schedule keeps answers current and citable; fine-tuning bakes knowledge into weights and cannot provide source citations, and monthly re-tuning is the wrong economics for changing facts.

**A2.** AWS AppConfig (holds the model identifier as runtime configuration, changeable without redeploy), Amazon API Gateway (stable endpoint, request validation, throttling), AWS Lambda (routing logic that reads the AppConfig value and calls the chosen provider's model).

**A3.** Investigate first: retrieval quality (chunking strategy, embedding quality, relevance of what was retrieved - the failure is upstream of generation). Investigate last: the generation model or its temperature (the retrieved chunks already look relevant, so generation is the least likely culprit). Order matters because fixing the wrong layer (e.g., swapping models) leaves the real defect in place while burning time and money.

**A4.** A single Lambda function cannot wait 4 hours: Lambda has a hard maximum runtime measured in minutes. AWS Step Functions should own the workflow (it supports long waits, human-approval callbacks, and sequential orchestration); Lambda handles the individual model/tool calls.

**A5.** Bug: the code invokes the base model ID, so requests never route to the purchased provisioned throughput and stay on on-demand capacity. Fix: invoke the provisioned model identifier/ARN (the provisioned throughput's model ARN) instead of the base model ID.

**A6.** (a) Profanity in inputs: content filters. (b) Refusing medical diagnoses: denied topics. (c) Redacting SSNs: sensitive information (PII) filters. Word filters (exact-match blocklists) are the wrong control for all three: they cannot judge toxicity categories, cannot enforce topic bans, and cannot detect PII entity types.

**A7.** VPC interface endpoints (PrivateLink) for Bedrock keep traffic off the public internet - skipping it exposes regulated data to internet-path risk. KMS-encrypted invocation logging (or disabling logging where logs would hold PII) protects log contents at rest - skipping it leaves sensitive prompt/response data unencrypted in S3/CloudWatch.

**A8.** First problem: prompt caching (the repeated 8,000-token static prefix is the textbook caching case). Second problem: provisioned throughput (reserved capacity for steady baseline traffic with throttling). Not interchangeable: caching attacks repeated-input cost, provisioned throughput attacks latency/throughput guarantees - caching does nothing for throttling, and provisioned throughput does nothing for repeated-prefix cost.

**A9.** Before production: regression testing on prompt/model changes (compares new outputs against a golden set) and canary testing (limited rollout with quality comparison). Continuous after deployment: continuous evaluation workflows with automated quality gates.

**A10.** Conversation history: DynamoDB (fast key-value, right home for session state). PDF documents: S3 (durable object storage for source documents; the vector index lives in a vector store like OpenSearch or a knowledge base). ElastiCache rule: it is an ephemeral cache, not durable storage - never the system of record for anything that must survive.

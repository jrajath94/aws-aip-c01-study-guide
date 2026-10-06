# AIP-C01 Prerequisite Bridge Cards v1.0

Research date: 2026-10-06. Audience: strong software engineer, zero AWS knowledge. Rule: each card teaches only what the audit found missing (see aip_delta_audit.md). Cards are short by design. No full certification courses. Every card ends with a transfer check and a separate answer. All numbers in toy examples are original illustrations, not source claims. Claim labels: [Guide] (official exam guide), [Behavior] (documented service behavior), [Version-dependent] (values that change).

---

## B-P01. Log scale at meaning level (P01)

Dependency: P01 numeracy. Core use: D1/D4 cost and latency comparisons.

Mechanism. A log scale counts multiplication steps, not addition steps. One order of magnitude means 10x. Two orders mean 100x. On a log scale, $0.003 and $0.03 and $0.30 sit at equal spacing.

Tiny worked example. A small model costs $0.30 per 1M tokens. A large model costs $3.00 per 1M tokens [Version-dependent]. The gap is one order of magnitude. At 10M tokens per day, the small model costs $3.00 per day and the large costs $30.00 per day. The $27.00 daily gap is the decision, not the absolute prices.

Choose. Choose log thinking when you compare options across 10x gaps: model prices, token counts, request rates. Do not choose it for small gaps: 8,000 vs 8,500 tokens is arithmetic, not orders of magnitude.

Trap. A 10 percent latency cut sounds good until the p99 is 10x the mean. Percent changes hide order-of-magnitude tails.

Transfer check. A reranker adds 40 ms per query. The model call takes 4,000 ms. Is the reranker cost an order-of-magnitude concern?

Answer. No. 4,000 / 40 = 100. The model call is two orders of magnitude larger. Fix the model call first.

Source: general numeracy, 2026-10-06. Next core use: L1 token cost math, L10 p50/p95/p99.

---

## B-P02. ARN anatomy and control plane vs data plane (P02)

Dependency: P02 resource vocabulary. Core use: D3 IAM policies, D4 observability.

Mechanism. An ARN (Amazon Resource Name) is the full address of one AWS resource. Format: arn:partition:service:region:account:resource. Example: arn:aws:s3:::reports-bucket/q3.pdf names the S3 service, an empty region (S3 ARNs skip it), and the object path. Policies match on this string, so one wrong segment denies the call.

The control plane configures. The data plane serves. CreateBucket is control plane. GetObject is data plane. CloudTrail records both, but it records data-plane calls only when the trail enables them.

Tiny worked example. Alice calls s3:GetObject on arn:aws:s3:::reports-bucket/q3.pdf. The identity policy allows s3:GetObject on arn:aws:s3:::reports-bucket/*. The ARN of the object matches the pattern reports-bucket/*. The allow applies. Change the ARN to arn:aws:s3:::other-bucket/q3.pdf and the same policy denies.

Choose. Choose ARN-level Resources in policies for least privilege (L0 rule). Do not choose "*" when the policy can name the exact ARN. Choose the data-plane lens (CloudTrail data events, X-Ray) when the question is about request behavior.

Trap. "CloudTrail records API calls" does not mean it records every data-plane call by default. Object-level S3 calls need data events enabled.

Transfer check. A policy allows dynamodb:GetItem on arn:aws:dynamodb:us-east-1:123456789012:table/orders. The app reads table refunds in the same account and Region. Allow or deny?

Answer. Deny. The ARN names table/orders only. The refunds table has a different ARN, so the allow never matches.

Source: AWS IAM documentation concepts, 2026-10-06 [Behavior]. Next core use: L9 Alice policy evaluation, L10 CloudTrail data-plane note.

---

## B-P03. Shared responsibility (P03)

Dependency: P03. Core use: D3 governance and compliance.

Mechanism. AWS owns the cloud itself: buildings, power, network hardware, hypervisor, and the operation of managed services. You own what you put in and how you configure it: your data, your access policies, your encryption settings, your application code. The line moves with the service. On EC2 you patch the OS. On Lambda there is no OS to patch. On Bedrock you never see a server at all, but you still own the prompts, the data you send, and who may call the model.

Tiny worked example. A team stores patient notes in S3 and calls Bedrock for summaries. AWS owns S3 durability and Bedrock availability. The team owns: the bucket policy (who reads the notes), the KMS key choice (who decrypts), the decision to send notes to the model at all, and the log retention rule. A breach through a public bucket is the team's misconfiguration, not an AWS failure.

Choose. Choose managed services to shrink your side of the line (less patching, less key handling). Do not choose a managed service and assume it owns your compliance. Vendor eligibility (a service appears on a compliance list) is not application compliance (your use passes an audit).

Trap. "Bedrock is HIPAA-eligible" does not make your app compliant. Eligibility is AWS's side. Your prompts, logs, and access controls are your side.

Transfer check. A team turns on Bedrock Guardrails and declares the app compliant with a data-protection law. What is still absent?

Answer. Everything on the customer side: proof of what data reaches the model, log scrubbing, access policies, retention rules, and a legal review. Guardrails are one control, not a compliance verdict.

Source: AWS shared responsibility model, 2026-10-06 [Guide]. Next core use: L9 governance, 3.3.3.

---

## B-P04. Availability, durability, RTO, RPO, backup vs replication (P04)

Dependency: P04 reliability. Core use: D1/D2 resilience designs.

Mechanism. Availability is the share of time a system answers. Durability is the share of data that survives. A system can be highly available and still lose data, or highly durable and still go offline. RTO (recovery time objective) is how fast you must be back. RPO (recovery point objective) is how much data loss you can take, measured in time. Replication copies data to a live second location for failover (serves availability and short RTO). Backup copies data to a restore point for recovery after corruption or deletion (serves durability and RPO).

Tiny worked example. A knowledge base holds 2M documents in S3 with cross-Region replication to a second Region. Region A fails at 10:00. Traffic fails over by 10:04. RTO = 4 minutes. Replication lag was 2 minutes, so documents written 09:58-10:00 are absent from Region B. RPO = 2 minutes of writes. Now a bad script deletes half the corpus in both Regions (replication copies the delete). The backup from last night restores it. Replication did not help. Only the backup did.

Choose. Choose replication when the failure is a dead location and you need fast failover. Choose backup when the failure is bad data (deletion, corruption, bug) and you need an old good copy. Most production systems need both.

Trap. "We replicate, so we are backed up." Replication copies mistakes too. A delete that replicates is not a backup.

Transfer check. An agent writes user facts to DynamoDB with point-in-time recovery enabled. A bug writes wrong facts for 6 hours. Does failover to a replica fix it? What does?

Answer. No. The replica holds the same wrong facts. Restore from the point-in-time backup to a time before the bug.

Source: AWS resilience concepts, 2026-10-06 [Behavior]. Next core use: L1 circuit breaker and graceful degradation, L11 troubleshooting.

---

## B-P05. Assume role, execution role, STS, signing, SDK Region (P05)

Dependency: P05 credentials/roles. Core use: D2 agent safeguards, D3 access design.

Mechanism. A principal (user, role, or service) proves identity on every call. Long-lived access keys are one proof, and a bad one to scatter. The better pattern is assume role: a principal calls STS AssumeRole, proves who it is, and gets temporary credentials (an access key, a secret, and a session token) that expire in minutes to hours. An execution role is the role a compute service assumes to act for you: the Lambda execution role is what lets your function call Bedrock. Trust is not permission: the trust policy says who may assume the role. The permission policy says what the role may do. Both must allow.

Signing proves the request came from the credential holder without sending the secret. The SDK signs each request with the secret key. The SDK Region decides which regional endpoint receives the call, and some calls fail when the Region has no such service.

Tiny worked example. A Lambda function needs bedrock:InvokeModel. The function has execution role arn:aws:iam::123456789012:role/agent-role. At runtime the Lambda service calls STS AssumeRole on agent-role and hands the function temporary credentials. The role trust policy allows lambda.amazonaws.com to assume it. The permission policy allows bedrock:InvokeModel on one model ARN. The SDK signs the InvokeModel call and sends it to us-east-1. Remove the trust policy entry and the assume fails: no credentials, no call. Remove the permission entry and the call signs fine but Bedrock denies it.

Choose. Choose execution roles with short-lived credentials for every compute-to-service call. Do not choose long-lived access keys inside code or config. Choose the SDK Region that serves the model (L1 inference profiles).

Trap. "The trust policy allows it" does not grant the action. Trust answers who may become the role. Permission answers what the role may do. You need both.

Transfer check. An agent on EC2 calls STS AssumeRole for a role whose trust policy names lambda.amazonaws.com only. What happens, and what is the one-line fix?

Answer. AssumeRole denies: the trust policy does not name ec2.amazonaws.com. Fix: add ec2.amazonaws.com (or the instance role path) to the trust policy, or run the agent where the trust already allows.

Source: AWS IAM/STS concepts, 2026-10-06 [Behavior]. Next core use: L5 agent least privilege, L9 confused deputy.

---

## B-P07. ABAC and document-level permissions (P07)

Dependency: P07 data authorization. Core use: D1 metadata access control, D3 granular access.

Mechanism. RBAC (role-based access control) grants by job: the support role reads tickets. ABAC (attribute-based access control) grants by attributes: a principal with department=claims reads documents tagged department=claims. The policy compares the requester's tags with the resource's tags at call time. Document-level permissions extend this to retrieval: each chunk carries tenant_id and clearance, and the retriever filters on them before the vector search runs (L3 rule).

Tiny worked example. Two analysts share the support role. Ana has clearance=2. Ben has clearance=5. Documents carry clearance tags 1-5. An ABAC policy allows s3:GetObject when the principal's clearance tag >= the object's clearance tag. Ana requests a clearance-4 document: 2 >= 4 is false, deny. Ben requests it: 5 >= 4 is true, allow. Same role, different answers, no policy edit per person.

Choose. Choose RBAC when access follows stable jobs. Choose ABAC when access follows data attributes (tenant, clearance, department) that change per document. Choose metadata filters at retrieval time for RAG (L3), never prompt text as the enforcement.

Trap. A prompt that says "only show clearance-2 docs" is not access control. The model can be talked past the instruction. Enforcement lives in the policy and the retrieval filter.

Transfer check. A KB holds docs for tenants A and B. The app adds "Answer only from tenant A docs" to the system prompt. A user from tenant B asks about tenant A data. Is tenant A data safe?

Answer. No. The filter must run before retrieval on a tenant_id attribute. The prompt instruction is bypassable.

Source: AWS IAM ABAC concepts, 2026-10-06 [Behavior]. Next core use: L3 metadata-driven access control, L9 granular access.

---

## B-P16. SNS one-liner (P16)

Dependency: P16 interaction patterns. Core use: D4 alerting.

Mechanism. SNS (Simple Notification Service) is the fan-out service: one published message reaches many subscribers (email, SMS, Lambda, SQS queues) at once. SQS is one queue for one consumer pool. EventBridge routes events by pattern. SNS notifies humans and systems about one event.

Tiny worked example. A CloudWatch alarm fires on token-spend anomaly. The alarm publishes to one SNS topic. Three subscribers get it at once: the on-call phone by SMS, the team channel by email, and a Lambda that opens a ticket. One publish, three landings, no polling.

Choose. Choose SNS when one event must notify many targets now. Choose SQS when workers must drain a backlog in order. The exam pairs alarms with SNS.

Trap. SNS delivers notifications. It does not store them for replay. A subscriber that is down misses the message unless a queue sits behind it.

Transfer check. A token-burst alarm must page the on-call engineer and open a ticket. One service or two?

Answer. One SNS topic with two subscribers: the pager and the ticketing Lambda. The topic is the fan-out point.

Source: AWS SNS concepts, 2026-10-06 [Behavior]. Next core use: L10 anomaly detection alarms.

---

## B-P11. Cold starts and statelessness (P11)

Dependency: P11 compute. Core use: D2 deployment, streaming UX.

Mechanism. A cold start is the setup tax on a fresh compute unit: the platform loads your code and its libraries before the first request runs. Lambda functions are stateless: nothing from one run survives into the next except what you wrote to outside storage. A warm function answers fast. A cold function answers after the setup tax. Provisioned concurrency keeps functions warm for a price.

Tiny worked example. A chat API on Lambda sees 10 requests per minute, evenly spaced. Each request lands on a cold function with a 900 ms setup tax. Median latency = 900 ms setup + 120 ms work = 1,020 ms. Move to 600 requests per minute and functions stay warm: median latency = 120 ms. Same code, 8.5x latency gap, caused only by traffic shape.

Choose. Choose provisioned concurrency or a warm service when TTFT or p99 matters and traffic is thin. Do not choose it for batch jobs: the night-shift crew does not care about the first second. Never store session state in function memory. L0 put it in DynamoDB for this reason.

Trap. "Lambda is fast" is traffic-dependent. Cold starts punish exactly the low-traffic demos where you measure first impressions.

Transfer check. A support chat on Lambda shows 2-second first responses at night and 200 ms at noon. Code is unchanged. What is the cause and the cheapest fix that keeps Lambda?

Answer. Cold starts at night (thin traffic). Cheapest fix: provisioned concurrency sized to the night baseline, or accept it if night users are internal.

Source: AWS Lambda concepts, 2026-10-06 [Behavior]. Next core use: L6 deployment ladder, L10 TTFT.

---

## B-P12. Storage pattern one-liners: block, file, key-value, relational, cache, vector (P12)

Dependency: P12 storage patterns. Core use: D1 vector architecture.

Mechanism. Each store answers one access shape. Block storage (EBS) is a disk for one server. File storage (EFS) is a shared folder for many servers. Key-value (DynamoDB) answers "give me the item with this key" in milliseconds. Relational (RDS/Aurora) answers joins and transactions with SQL. Cache (ElastiCache) answers repeats fast and forgets. Vector index (OpenSearch, pgvector) answers "find the nearest meaning". A vector index is not a transactional source of truth: it has no joins, no multi-row transactions.

Tiny worked example. A RAG system holds 2M documents. It keeps: PDFs in S3 (durable objects), metadata rows in DynamoDB (key lookup by doc ID), vectors in OpenSearch (nearest-neighbor search), order records in RDS (transactions with joins), hot answers in ElastiCache (repeat speed). Five stores, five jobs. Ask OpenSearch for "all refunds over $500 joined to users" and it fails: that is a relational question.

Choose. Choose the store by the question shape: key lookup to DynamoDB, meaning search to the vector index, transactions to RDS, repeats to cache, blobs to S3. Do not choose one store for every job because the console is familiar.

Trap. DynamoDB with a "vector" attribute is not vector search. A scan reads the whole table per query. The exam sets this trap in several wordings (L3).

Transfer check. Model weights (40 GB) must load onto GPU hosts at deploy time. Which store: EFS, DynamoDB, or ElastiCache?

Answer. EFS (shared file). Weights are large files many hosts read. DynamoDB is the wrong shape. ElastiCache forgets.

Source: AWS storage concepts, 2026-10-06 [Behavior]. Next core use: L3 vector-store design, L6 GPU weight loading.

---

## B-P13. Object, key, version, metadata, lifecycle, deletion layers (P13)

Dependency: P13 object/data lifecycle. Core use: D1 KB maintenance, D3 retention.

Mechanism. In S3, an object is the file plus its metadata. The key is its path-like name. A version is one saved copy when versioning is on: each overwrite adds a version, and delete writes a delete marker instead of erasing. Metadata is key-value data about the object: system metadata (size, timestamps) and user metadata (author, tenant_id) plus tags. Lifecycle rules move or expire objects by age: to cheaper storage, then to deletion. Four deletions differ: object deletion removes the file, index deletion removes the vector entry, cache deletion (purge) removes the stored answer, log retention controls when evidence ages out. One delete does not trigger the others by itself.

Tiny worked example. A tenant leaves and demands erasure. The team deletes 5,000 PDFs from S3. The vector index still answers from their chunks. The semantic cache still serves their answers. CloudWatch Logs still hold their prompts for 90 days. Real erasure needs four passes: S3 delete (plus delete markers if versioned), index delete, cache purge by tenant key, and a log-retention exception. Miss one pass and the data lives on.

Choose. Choose versioning when overwrites must stay recoverable. Choose lifecycle rules for automatic aging. Choose explicit multi-layer deletion for erasure and revocation.

Trap. "We deleted the source files" does not mean the RAG system forgot them. The index and the cache are separate copies.

Transfer check. A lifecycle rule deletes raw transcripts from S3 after 30 days. Do vector embeddings of those transcripts vanish too?

Answer. No. The rule touches S3 only. The index needs its own delete pass (see patch P-G04).

Source: AWS S3 concepts, 2026-10-06 [Behavior]. Next core use: L3 freshness, L9 retention, patch P-G04.

---

## B-P14. Conditional writes and TTL as expiry, not authorization (P14)

Dependency: P14 conversation state. Core use: D2 agent memory.

Mechanism. A conditional write succeeds only when a condition holds at write time: "write this fact only if no fact with this key exists" or "only if the version I read is still current." Two writers racing on one key stop overwriting each other blindly. TTL (time to live) is an expiry stamp on an item: DynamoDB deletes the item after the stamp passes, asynchronously. TTL is cleanup, not security: an expired-but-not-yet-deleted item can still be read, and TTL never replaces an authorization check.

Tiny worked example. Two agent turns update the same user fact at once. Turn A reads version 7. Turn B reads version 7. Turn A writes version 8 with condition "current version is 7": succeeds. Turn B writes version 8 with condition "current version is 7": fails, because the version is now 8. Turn B re-reads and retries with the merged value. Without the condition, the last writer silently wins and one update is lost.

Choose. Choose conditional writes for read-modify-write on shared state (agent memory, counters). Choose TTL for automatic cleanup of session data and caches. Do not choose TTL as an access boundary for revoked users or tenants.

Trap. "The TTL expired, so the data is gone and access is safe." Deletion is asynchronous, and a revoked tenant needs a filter at read time, not a stamp at write time.

Transfer check. A revoked tenant's cached answers carry a 1-hour TTL. The tenant is revoked at 10:00. Is the tenant locked out at 10:05?

Answer. Not by the TTL. Cached answers may serve until expiry and deletion. Lockout needs a hit-time authorization check (see curveball C16).

Source: AWS DynamoDB concepts, 2026-10-06 [Behavior]. Next core use: L5 agent memory, C16 curveballs.

---

## B-P18. Orchestration: tasks, catch, retry, and the enforcement boundary (P18)

Dependency: P18 orchestration. Core use: D2 agents and safeguards.

Mechanism. A state machine is a workflow with named states and transitions: task states do work, choice states branch, catch blocks handle a named error, retry policies re-run a failed task with backoff, and a terminal state stops the run. The machine enforces the order: a step cannot run before its turn, and a failed step cannot be skipped silently. Agent reasoning does not replace this enforcement. A model can decide which tool looks useful, but only the state machine guarantees the approval step ran, the timeout fired, and the loop stopped.

Tiny worked example. A refund flow: task 1 reads the order, task 2 calls the refund tool, choice 3 checks the amount. Over $50 goes to the approval state (human, 2-hour timeout). A catch on task 2 retries twice with backoff, then routes to a compensation state that notifies support. The model never decides to skip approval: the choice state sends every large refund to the human. Remove the state machine and keep only the agent, and a clever prompt injection can talk the model past the approval.

Choose. Choose Step Functions when order, retries, timeouts, and human gates must hold under adversarial input. Choose agent reasoning for open-ended planning inside a guarded step. Never let the model own the guard.

Trap. "The agent was told to ask for approval" is a suggestion. A state machine approval state is enforcement. The exam tests the difference.

Transfer check. An agent loop has max 40 steps and a prompt that says "stop after 3 tool calls". Which one actually stops a runaway loop?

Answer. The max-steps setting. The prompt is a suggestion the model can ignore under a confusing tool result.

Source: AWS Step Functions concepts, 2026-10-06 [Behavior]. Next core use: L5 safeguards, L7 approval gates.

---

## B-P19. Parameter Store vs Secrets Manager vs AppConfig vs Prompt Management (P19)

Dependency: P19 config/prompt lifecycle. Core use: D1 config routing, D2 CI/CD.

Mechanism. Four stores, four jobs. AppConfig holds application configuration with validation and gradual rollout: feature flags, model IDs, thresholds. Parameter Store holds plain configuration values and small secrets with IAM control. Secrets Manager holds real secrets (API keys, DB passwords) with automatic rotation. Prompt Management holds prompt templates with versions and approvals. Storing a template is not safe rollout, and storing a secret in AppConfig is not secret management.

Tiny worked example. A GenAI service needs: the active model ID, a database password, and the support prompt template. The model ID goes in AppConfig (operators flip it without a deploy, L1). The password goes in Secrets Manager (rotation every 30 days, never in code). The prompt goes in Prompt Management (v5 approved before it becomes default, L4). A developer puts the password in AppConfig "for speed." It now sits in plaintext config, visible to everyone who reads flags, with no rotation. The Q28 leak scenario starts exactly here.

Choose. Choose AppConfig for values operators change. Choose Secrets Manager for anything that authenticates. Choose Prompt Management for anything the model reads as instructions. Never store a secret where a config reader can see it.

Trap. "It is in a managed store, so it is safe." Safety follows the store's job: AppConfig manages rollout, Secrets Manager manages secrecy.

Transfer check. A test API key leaked in a release. It lived in a config file in the repo. Which two changes fix the class of problem?

Answer. Move the key to Secrets Manager with rotation, and add a secret scan to the CI/CD test stage (Q28 control B).

Source: AWS config/secret concepts, 2026-10-06 [Behavior]. Next core use: L1 config-driven routing, L7 CI/CD gates.

---

## B-P20. AI, ML, DL, GenAI, and training vs inference (P20)

Dependency: P20 AI task families. Core use: D1 technique choice.

Mechanism. AI is the whole field: machines doing tasks that need judgment. ML is the slice that learns patterns from data instead of following hand-written rules. DL is the slice of ML that uses large neural networks. GenAI is the slice of DL that generates new content: text, images, code. Training is the expensive phase that adjusts weights on data. Inference is the cheap phase that runs the trained model on one input. Fine-tuning is extra training on your examples. RAG is not training at all: it pastes facts into the prompt at inference time.

Tiny worked example. A team needs invoice totals extracted from 1M scans per month. A rules engine (plain software, no ML) fails on new layouts. A classifier (ML) needs 10,000 labeled invoices. A GenAI model (no training) reads each invoice with a prompt and returns JSON. Cost: prompt path = 1M x 2,000 tokens x price. The team picks GenAI because layouts change monthly and labeling 10,000 invoices costs more than the tokens. That is the 1.1.1 fit test: probabilistic generation fits variable layouts.

Choose. Choose GenAI when the input varies and the output is new content. Choose classic ML when the task is a stable classification with labeled data. Choose rules when the input is rigid. Never fine-tune to teach fresh facts (L1 rule).

Trap. "AI" on a vendor slide can mean a regex. Ask which slice: rules, ML, or GenAI. The choice changes cost, data needs, and failure modes completely.

Transfer check. A fraud score must be a stable number from 40 numeric features, retrained monthly on labeled outcomes. GenAI, ML classifier, or rules?

Answer. ML classifier. Numeric features, labeled data, stable task. GenAI adds cost and nondeterminism for no gain.

Source: standard AI/ML definitions, 2026-10-06. Next core use: L1 escalation ladder, 1.1.1/1.2.1.

---

## B-P21. Logits and model parameters at meaning level (P21)

Dependency: P21 FM mechanics. Core use: D1 customization, D4 sampling tuning.

Mechanism. Parameters are the model's learned weights: billions of numbers that encode what training taught. More parameters usually mean more capability and more cost. Logits are the raw scores the model assigns to each possible next token before sampling. Temperature reshapes the logits: low temperature sharpens the differences (the top token wins almost always), high temperature flattens them (unlikely tokens get a real chance). Top-p and top-k cut the candidate list before the pick. Sampling dials act on logits, not on words.

Tiny worked example. Next-token logits: "Paris" = 9.0, "London" = 8.8, "Tokyo" = 2.0. At temperature near 0, "Paris" wins every run: 9.0 beats 8.8 decisively after sharpening. At high temperature, "London" wins often and "Tokyo" sometimes. Same logits, different behavior. LoRA (L1) trains two small matrices per layer: it changes a few million parameters, not the billions of the base model. That is why the adapter is megabytes while the model is gigabytes.

Choose. Choose low temperature when the answer must be steady and factual (the dials act on logits, so low means "trust the top score"). Choose higher values for brainstorming. Choose LoRA when behavior must change but full retraining is too costly.

Trap. "Higher temperature makes the model smarter." It makes the model more varied. On factual tasks, variety is error.

Transfer check. A classifier built on token probabilities behaves randomly at temperature 1.0 but stably at 0.1. Why?

Answer. Temperature flattens the logits at 1.0, so near-tie tokens win by chance. At 0.1 the top logit dominates and the pick is steady.

Source: standard FM sampling concepts, 2026-10-06. Next core use: L1 LoRA, L10 per-use-case tuning.

---

## B-P22. SFT vs continued pre-training vs distillation (P22)

Dependency: P22 adaptation. Core use: D1 customization lifecycle.

Mechanism. Three training-based adaptations, three different problems. SFT (supervised fine-tuning) trains on input-output pairs to teach behavior: "when you see X, answer like Y." Continued pre-training trains on raw domain text to teach vocabulary and style: the model absorbs how a field talks. Distillation trains a small model to copy a large model's answers: the small one learns the behavior at a fraction of the serving cost. None of them reliably teaches fresh facts (L1 rule): facts still come from retrieval.

Tiny worked example. A bank needs a support model. SFT on 5,000 ideal support transcripts teaches tone and structure. Continued pre-training on 2M pages of banking regulation teaches the jargon. Distillation copies the tuned large model into a small one that costs 10x less per token [Version-dependent]. Pick the wrong one and pay: SFT on raw regulation text teaches nothing (no input-output pairs), continued pre-training on transcripts wastes compute (the behavior was already there).

Choose. Choose SFT for behavior and format. Choose continued pre-training for domain language. Choose distillation for cost after the big model works. Choose RAG for fresh facts, always.

Trap. "We fine-tuned on the new product docs, so it knows the new prices." Training memorizes unreliably. The model will still invent prices. Retrieval is the fix.

Transfer check. A team wants a small cheap model that answers like their tuned large model on support tickets. Which adaptation, and what data does it need?

Answer. Distillation. It needs the large model's answers on representative tickets as training targets, not raw manuals.

Source: standard FM adaptation concepts, 2026-10-06. Next core use: L1 skill 1.2.4, patch P-G19.

---

## B-P23. Train, validation, test, overfit, baseline, shift (P23)

Dependency: P23 statistical validity. Core use: D5 evaluation.

Mechanism. Training data teaches. Validation data tunes (which prompt, which threshold). Test data judges once, at the end. The holdout set (L11) is test data locked away from tuning. Leakage is test data that sneaks into tuning: the score looks great and means nothing. Overfit is a model (or prompt) that memorizes the tuning data and fails on new inputs. A baseline is the dumb version you must beat: the old prompt, a keyword search, a coin flip. Shift is the world moving: user language changes, and last month's golden set stops representing today.

Tiny worked example. A team tunes a prompt on 200 examples and scores 96 percent. They score the locked holdout: 71 percent. The 25-point gap is overfit to the tuning set (or leakage, if holdout examples appeared in tuning). The baseline keyword search scores 68 percent on the holdout. The tuned prompt beats the baseline by 3 points, not 28. Ship or not is now an honest question.

Choose. Choose three separate splits whenever you tune and judge. Choose a baseline before you celebrate a score. Choose to re-check for shift on a schedule (L9 bias drift, L11 drift checks).

Trap. "96 percent on our eval set" with no mention of a locked holdout is not evidence. It is a tuning score wearing a test score's clothes.

Transfer check. A reranker tuned on the golden set beats the old ranker 88 to 82 on the same set. What single check decides whether the win is real?

Answer. Score both on the locked holdout set. If the gap survives there, the win is real. If it collapses, it was overfit.

Source: standard ML evaluation concepts, 2026-10-06. Next core use: L11 evaluation layers, patch P-G18.

---

## B-P26. Data formats: JSONL, CSV, Parquet, media (P26)

Dependency: P26 formats and data quality. Core use: D1 data pipelines.

Mechanism. Format is the shape of the bytes. Quality is whether the content is right. Schema validity never proves content quality (L2 rule). CSV is rows and commas: simple, fragile with nested text. JSONL is one JSON object per line: the standard shape for training and eval records, one record per line, easy to stream. Parquet is a compressed columnar binary: the standard for large analytics datasets, cheap to scan by column. Media (audio, image, PDF) needs an extractor before a model can use it (L2: Transcribe, Textract).

Tiny worked example. A fine-tune job needs 50,000 support Q/A pairs. As CSV, a multi-line answer breaks the row parsing. As JSONL, each line is {"prompt": ..., "response": ...}: the loader streams line by line and never holds the whole file in memory. As Parquet, analysts scan the "category" column over 50,000 rows without reading the text. Three formats, three jobs. The training job wants JSONL.

Choose. Choose JSONL for training/eval record streams. Choose Parquet for large tabular analytics. Choose CSV for small human-edited tables. Choose the extractor (Transcribe/Textract) before the model for media.

Trap. "The file parsed, so the data is good." Parsing checks shape. A valid JSONL line can still hold a wrong price (L2 dedupe/validation lesson).

Transfer check. A nightly job scans 2M catalog rows to count bad prices per category. CSV, JSONL, or Parquet?

Answer. Parquet. Columnar scan reads only the price and category columns over 2M rows. CSV/JSONL would read every byte.

Source: standard data-format concepts, 2026-10-06. Next core use: L2 pipelines, 1.3.2.

---

## B-P27. Data Wrangler one-liner (P27)

Dependency: P27 processing services. Core use: D1 data validation.

Mechanism. SageMaker Data Wrangler is the visual tool for preparing tabular data for ML: it profiles columns, finds missing values and outliers, and exports a repeatable preparation flow. It sits before training. Glue Data Quality (L2) sits before FM consumption and checks rules on the data as it flows. One prepares training tables. The other guards the pipeline.

Tiny worked example. A team readies 100,000 loan applications for a classifier. Data Wrangler shows 12 percent missing income values and 40 duplicate applicant IDs. The team fills the incomes by rule and drops the dupes, then exports the flow so next month's data gets the same cleaning. Without it, the model trains on the dupes and learns that duplicates mean approval.

Choose. Choose Data Wrangler for interactive tabular preparation before training. Choose Glue Data Quality for automated rule checks on flowing data (L2). They stack, not substitute.

Trap. "We cleaned it once in a notebook" is not a pipeline. Next month's data arrives dirty again. Export the flow.

Transfer check. A monthly retrain needs the same dedupe and fill rules applied to each new data drop. Notebook or Data Wrangler flow?

Answer. Data Wrangler flow (or any saved pipeline). The rules must run identically every month.

Source: AWS SageMaker concepts, 2026-10-06 [Behavior]. Next core use: L2 validation workflows, 1.3.1.

---

## B-P28. Model Monitor and the human labeling loop (P28)

Dependency: P28 SageMaker lifecycle. Core use: D1 customization, D5 evaluation.

Mechanism. SageMaker Model Monitor watches a deployed endpoint for drift: it compares live traffic against a baseline (the training data or an early window) and alarms when the inputs or the predictions shift. A human labeling loop (SageMaker Ground Truth, or A2I for review in L9) puts people where the model is unsure: humans label the hard cases, and the labels flow back into training or the golden set. Monitor finds the drift. Humans supply the ground truth to fix it.

Tiny worked example. A classifier serves loan decisions. Model Monitor compares this week's applications against the baseline: the average income dropped 30 percent (an economic shift). It alarms. The team routes 500 low-confidence applications to human labelers. The labels show the model now rejects good applicants at 3x the old rate. The team retrains on the labeled data. Without the monitor, the drift runs silently for months. Without the labelers, there is no corrected data to retrain on.

Choose. Choose Model Monitor for continuous deployed-model watching. Choose human labeling for ground truth on the cases the model gets wrong. Choose A2I (L9) for human review of individual high-stakes outputs.

Trap. "The endpoint is healthy" (CPU fine, latency fine) does not mean the model is right. Operational health and model quality are different monitors.

Transfer check. A support classifier's accuracy falls over two months with no code change. Which two controls find it and fix the data?

Answer. Model Monitor (or the L11 drift checks) finds the shift. A human labeling loop produces corrected labels for retraining.

Source: AWS SageMaker concepts, 2026-10-06 [Behavior]. Next core use: L1 customization lifecycle, L11 drift checks.

---

## B-P30. IaC one-liner (P30)

Dependency: P30 change delivery. Core use: D2 CI/CD.

Mechanism. IaC (infrastructure as code) defines AWS resources in text files (CloudFormation, CDK, Terraform) instead of console clicks. The file is the truth: review it, version it, deploy it the same way in every environment. Click-ops drifts: dev and prod stop matching, and nobody knows which click made them differ.

Tiny worked example. A GenAI gateway needs an API Gateway, a Lambda, and an S3 bucket in dev and prod. With IaC, one template deploys both. The only difference is a parameter file. A console-built dev gateway gets a 30-second timeout. Prod gets the default 29 seconds by a missed click. The bug appears only in prod. The template makes the difference visible in a diff.

Choose. Choose IaC for every environment that matters. Choose console clicks only for throwaway experiments. The exam's 2.3.5 pipeline story assumes IaC underneath.

Trap. "We documented the console steps" is not IaC. Docs drift. Code deploys.

Transfer check. Two environments behave differently and no code changed. First suspect?

Answer. Configuration drift from manual changes. IaC with drift detection names the exact difference.

Source: standard DevOps concepts, 2026-10-06. Next core use: L7 CI/CD, 2.3.5.

---

## B-P32. Quota vs rate vs concurrency vs capacity, and the p99 rule (P32)

Dependency: P32 capacity. Core use: D4 performance and cost.

Mechanism. Four different limits. Quota is the account ceiling: how many requests per second AWS allows (raisable by request). Rate is what you actually send. Concurrency is how many run at once. Capacity is what the system can absorb: provisioned throughput, instance count, queue depth. A quota increase raises the ceiling. It does not add capacity. Tail latency (p99) is the latency of the slowest 1 percent: averages hide it, and it is what users feel at scale.

Tiny worked example. A fraud check sends a steady 50 requests per second. The Bedrock quota is 100 per second. At a sale, traffic hits 400 per second for 10 minutes. The team raises the quota to 500. Calls still throttle. The quota is now 500, but provisioned capacity covers only 100 per second, and on-demand absorbs the rest at higher cost and higher tail latency. p50 stays 300 ms. p99 jumps to 8 seconds because retries pile onto the throttled calls (L6 latency budget). The quota increase did not prove the p99.

Choose. Choose quota increases to remove the ceiling. Choose provisioned capacity or queues to absorb the load. Choose p99 (never the mean) as the launch target.

Trap. "We raised the quota, so we handle the spike." The ceiling is not the floor. Capacity and retry behavior decide the spike.

Transfer check. After a quota increase, p99 latency still misses the SLA at peak. What two things do you check next?

Answer. Actual provisioned capacity vs peak rate, and the retry/backoff config (retry storms inflate the tail).

Source: AWS quota/capacity concepts, 2026-10-06 [Behavior]. Next core use: L6 deployment ladder, L10 latency levers.

---

*End of bridge cards. Each card links forward to its core lesson. No card replaces a core lesson.*

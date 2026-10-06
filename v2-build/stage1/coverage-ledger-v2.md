# AIP-C01 Coverage Ledger v2 (Stage 1)

Research date: 2026-10-06. Source: official AIP-C01 exam guide.

A skill counts as COVERED only when the learner gets all four of: (1) a mechanism explanation, (2) a decision rule with limitations, (3) an application example, (4) a diagnostic/assessment opportunity. All rows currently: **not started**.

Columns: Domain | Task | Skill | Skill summary (paraphrase of official text) | Prerequisite dependencies | Required concepts | Relevant services | Lesson location | Comparison table location | Worked scenario location | Practice question IDs | Evidence sources | Status.

---

## Domain 1: Foundation Model Integration, Data Management, and Compliance (31%)

| Task | Skill | Skill summary | Prerequisite dependencies | Required concepts | Relevant services | Lesson | Comp. table | Worked scenario | Practice Q IDs | Evidence sources | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.1 | 1.1.1 | Architecture designs matched to business needs and technical constraints | Prereq: regions/AZs; ML basics (FM types) | RAG vs agents vs fine-tuning vs prompt engineering decision ladder; cost/latency/compliance constraints | Bedrock, Well-Architected Tool | TBD | TBD | TBD | TBD | Official guide Task 1.1 | not started |
| 1.1 | 1.1.2 | Technical PoC to validate feasibility, performance, business value before scale-up | Prereq: ML basics | PoC pattern; on-demand vs committed capacity | Bedrock | TBD | TBD | TBD | TBD | Official guide Task 1.1 | not started |
| 1.1 | 1.1.3 | Standardized reusable components across deployments | Prereq: none | Well-Architected GenAI Lens pillars; component standardization | Well-Architected Tool | TBD | TBD | TBD | TBD | Official guide Task 1.1 | not started |
| 1.2 | 1.2.1 | Evaluate and choose FMs via benchmarks, capability and limitation analysis | Prereq: ML basics (tokens, context window) | Capability vs cost/latency/region trade-offs | Bedrock (models) | TBD | TBD | TBD | TBD | Official guide Task 1.2 | not started |
| 1.2 | 1.2.2 | Flexible architecture for model/provider switching without code changes | Prereq: regions/AZs; IAM basics | Runtime configuration pattern; stable endpoint + config-driven routing | Lambda, API Gateway, AppConfig | TBD | TBD | TBD | TBD | Official guide Task 1.2 | not started |
| 1.2 | 1.2.3 | Resilient AI systems: circuit breakers, cross-region inference, graceful degradation | Prereq: regions/AZs | Inference profiles vs bare model IDs; circuit breaker pattern; degradation ladder | Step Functions, Bedrock Cross-Region Inference | TBD | TBD | TBD | TBD | Official guide Task 1.2 | not started |
| 1.2 | 1.2.4 | FM customization lifecycle: fine-tune (LoRA/adapters), registry, pipelines, rollback, retire | Prereq: ML basics | SFT/continued pre-training/distillation; versioned model artifacts; rollback pattern | SageMaker AI, SageMaker Model Registry | TBD | TBD | TBD | TBD | Official guide Task 1.2 | not started |
| 1.3 | 1.3.1 | Data validation workflows for FM consumption quality | Prereq: storage basics (S3) | Data quality dimensions for LLM input | Glue Data Quality, SageMaker Data Wrangler, Lambda, CloudWatch | TBD | TBD | TBD | TBD | Official guide Task 1.3 | not started |
| 1.3 | 1.3.2 | Processing pipelines for text/image/audio/tabular data | Prereq: ML basics | Multimodal extraction; batch transforms | Bedrock multimodal models, SageMaker Processing, Transcribe | TBD | TBD | TBD | TBD | Official guide Task 1.3 | not started |
| 1.3 | 1.3.3 | Format inputs per model-specific requirements | Prereq: ML basics (tokens) | Provider-specific request bodies vs unified APIs; conversation formatting | Bedrock APIs, SageMaker AI endpoints | TBD | TBD | TBD | TBD | Official guide Task 1.3 | not started |
| 1.3 | 1.3.4 | Enhance input data quality (reformat, entity extract, normalize) | Prereq: none beyond 1.3.1-1.3.3 | Entity extraction; normalization | Bedrock, Comprehend, Lambda | TBD | TBD | TBD | TBD | Official guide Task 1.3 | not started |
| 1.4 | 1.4.1 | Vector database architectures for FM augmentation | Prereq: ML basics (embeddings) | Vector similarity; managed vs self-managed vector stores | Bedrock Knowledge Bases, OpenSearch Service (Neural plugin), RDS, DynamoDB | TBD | TBD | TBD | TBD | Official guide Task 1.4 | not started |
| 1.4 | 1.4.2 | Metadata frameworks for search precision and context | Prereq: storage basics (S3) | Filtered retrieval; metadata-driven access control | S3 object metadata, custom attributes, tags | TBD | TBD | TBD | TBD | Official guide Task 1.4 | not started |
| 1.4 | 1.4.3 | High-performance vector DB architecture at scale | Prereq: compute limits (parallelism) | Sharding; multi-index; hierarchical indexing | OpenSearch Service | TBD | TBD | TBD | TBD | Official guide Task 1.4 | not started |
| 1.4 | 1.4.4 | Integration components connecting GenAI apps to doc systems, KBs, wikis | Prereq: none | Connector pattern | AWS service integrations (various) | TBD | TBD | TBD | TBD | Official guide Task 1.4 | not started |
| 1.4 | 1.4.5 | Data maintenance systems keeping vector stores current | Prereq: compute limits (scheduling) | Incremental sync; change detection; scheduled refresh | Lambda/EventBridge/Step Functions patterns | TBD | TBD | TBD | TBD | Official guide Task 1.4 | not started |
| 1.5 | 1.5.1 | Document segmentation (chunking) for retrieval | Prereq: ML basics (tokens) | Fixed/hierarchical/semantic/custom chunking; overlap; chunk size vs context | Bedrock KB chunking, Lambda (custom chunking) | TBD | TBD | TBD | TBD | Official guide Task 1.5 | not started |
| 1.5 | 1.5.2 | Embedding solution selection and configuration | Prereq: ML basics (embeddings) | Dimensions; batch embedding; query vs document embedding | Titan embeddings, Bedrock embedding models, Lambda | TBD | TBD | TBD | TBD | Official guide Task 1.5 | not started |
| 1.5 | 1.5.3 | Deploy and configure vector search solutions | Prereq: 1.4.1 | Semantic search configuration | OpenSearch vector search, Aurora pgvector, Bedrock KBs | TBD | TBD | TBD | TBD | Official guide Task 1.5 | not started |
| 1.5 | 1.5.4 | Advanced search: semantic + hybrid + reranking | Prereq: 1.5.3 | Hybrid search; rerankers; relevance vs recall | OpenSearch, Bedrock reranker models | TBD | TBD | TBD | TBD | Official guide Task 1.5 | not started |
| 1.5 | 1.5.5 | Query handling: expansion, decomposition, transformation | Prereq: none beyond 1.5.4 | Query expansion vs decomposition; transformation chains | Bedrock, Lambda, Step Functions | TBD | TBD | TBD | TBD | Official guide Task 1.5 | not started |
| 1.5 | 1.5.6 | Consistent access mechanisms: function calling, MCP clients, standardized APIs | Prereq: ML basics (tool use) | Function calling; MCP | MCP clients, function calling interfaces | TBD | TBD | TBD | TBD | Official guide Task 1.5 | not started |
| 1.6 | 1.6.1 | Model instruction frameworks controlling FM behavior | Prereq: ML basics (system prompts) | Role definitions; instruction hierarchy; policy enforcement | Bedrock Prompt Management, Bedrock Guardrails, templates | TBD | TBD | TBD | TBD | Official guide Task 1.6 | not started |
| 1.6 | 1.6.2 | Interactive AI systems: context, clarification, intent, conversation memory | Prereq: storage basics (DynamoDB) | Session state; intent recognition; clarification loops | Step Functions, Comprehend, DynamoDB | TBD | TBD | TBD | TBD | Official guide Task 1.6 | not started |
| 1.6 | 1.6.3 | Prompt management and governance: templates, approvals, audit, access logs | Prereq: IAM basics | Versioning; approval workflows; audit trails | Bedrock Prompt Management, S3, CloudTrail, CloudWatch Logs | TBD | TBD | TBD | TBD | Official guide Task 1.6 | not started |
| 1.6 | 1.6.4 | QA systems for prompt effectiveness: verification, edge cases, regression | Prereq: none beyond 1.6.3 | Regression testing of prompts; golden outputs | Lambda, Step Functions, CloudWatch | TBD | TBD | TBD | TBD | Official guide Task 1.6 | not started |
| 1.6 | 1.6.5 | Iterative prompt refinement beyond basics | Prereq: ML basics (CoT) | Structured inputs; output format specs; chain-of-thought; feedback loops | (technique-level; Bedrock) | TBD | TBD | TBD | TBD | Official guide Task 1.6 | not started |
| 1.6 | 1.6.6 | Complex prompt systems: sequential chains, branching, reusable components | Prereq: 1.6.3 | Prompt chaining; conditional branching; pre/post-processing | Bedrock Prompt Flows | TBD | TBD | TBD | TBD | Official guide Task 1.6 | not started |

---

## Domain 2: Implementation and Integration (26%)

| Task | Skill | Skill summary | Prerequisite dependencies | Required concepts | Relevant services | Lesson | Comp. table | Worked scenario | Practice Q IDs | Evidence sources | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.1 | 2.1.1 | Autonomous agent systems with memory and state management | Prereq: ML basics (agents); storage basics (DynamoDB) | Multi-agent orchestration; agent memory | Strands Agents, AWS Agent Squad, MCP | TBD | TBD | TBD | TBD | Official guide Task 2.1 | not started |
| 2.1 | 2.1.2 | Structured reasoning: ReAct and chain-of-thought via orchestration | Prereq: ML basics (reasoning patterns) | ReAct loop; trace inspection | Step Functions | TBD | TBD | TBD | TBD | Official guide Task 2.1 | not started |
| 2.1 | 2.1.3 | Safeguarded AI workflows: stopping conditions, timeouts, IAM boundaries, circuit breakers | Prereq: compute limits; IAM basics | Runaway-agent containment; least privilege for tools | Step Functions, Lambda, IAM | TBD | TBD | TBD | TBD | Official guide Task 2.1 | not started |
| 2.1 | 2.1.4 | Model coordination across capabilities: specialized models, ensembles, selection | Prereq: 1.2.1 | Ensemble aggregation; model selection frameworks | (framework-level; FMs) | TBD | TBD | TBD | TBD | Official guide Task 2.1 | not started |
| 2.1 | 2.1.5 | Human-augmented AI: review/approval workflows, feedback collection | Prereq: compute limits (Step Functions waits) | Human-in-the-loop patterns | Step Functions, API Gateway | TBD | TBD | TBD | TBD | Official guide Task 2.1 | not started |
| 2.1 | 2.1.6 | Tool integrations: custom behaviors, function definitions, error handling, param validation | Prereq: ML basics (tool use) | Tool schemas; error handling | Strands API, Lambda | TBD | TBD | TBD | TBD | Official guide Task 2.1 | not started |
| 2.1 | 2.1.7 | MCP servers: stateless lightweight (Lambda) vs complex (ECS); client libraries | Prereq: compute limits; networking basics | MCP protocol; server hosting trade-offs | Lambda, ECS, MCP client libraries | TBD | TBD | TBD | TBD | Official guide Task 2.1 | not started |
| 2.2 | 2.2.1 | FM deployment by need: on-demand (Lambda), provisioned throughput, hybrid (SageMaker endpoints) | Prereq: compute limits | Throughput vs cost vs latency | Lambda, Bedrock provisioned throughput, SageMaker AI endpoints | TBD | TBD | TBD | TBD | Official guide Task 2.2 | not started |
| 2.2 | 2.2.2 | LLM-specific deployment challenges: containers, memory, GPU, token throughput, model loading | Prereq: compute limits | GPU memory sizing; model loading strategies | Containers (ECS/EKS/Fargate), SageMaker AI | TBD | TBD | TBD | TBD | Official guide Task 2.2 | not started |
| 2.2 | 2.2.3 | Optimized deployment: right-size models, small models for tasks, model cascading | Prereq: 1.2.1 | Cascade routing; small-model economics | (API-level; FMs) | TBD | TBD | TBD | TBD | Official guide Task 2.2 | not started |
| 2.3 | 2.3.1 | Enterprise connectivity: legacy APIs, event-driven loose coupling, data sync | Prereq: networking basics | Event-driven architecture; sync vs async | (pattern-level), EventBridge | TBD | TBD | TBD | TBD | Official guide Task 2.3 | not started |
| 2.3 | 2.3.2 | GenAI in existing apps: microservice integration, webhooks, event-driven | Prereq: compute limits | Webhook pattern; microservice API composition | API Gateway, Lambda, EventBridge | TBD | TBD | TBD | TBD | Official guide Task 2.3 | not started |
| 2.3 | 2.3.3 | Secure access: identity federation, RBAC, least-privilege FM API access | Prereq: IAM basics | Federation; RBAC; least privilege | IAM Identity Center, IAM | TBD | TBD | TBD | TBD | Official guide Task 2.3 | not started |
| 2.3 | 2.3.4 | Cross-environment AI: on-prem data (Outposts), edge (Wavelength), secure routing | Prereq: regions/AZs; networking basics | Data residency; edge latency | Outposts, Wavelength | TBD | TBD | TBD | TBD | Official guide Task 2.3 | not started |
| 2.3 | 2.3.5 | CI/CD pipelines and GenAI gateway architectures | Prereq: none | Centralized abstraction layer; automated testing + security scans + rollback | CodePipeline, CodeBuild | TBD | TBD | TBD | TBD | Official guide Task 2.3 | not started |
| 2.4 | 2.4.1 | Flexible model interaction: sync Bedrock APIs, async via SDKs + SQS, API Gateway clients | Prereq: compute limits | Sync vs async; queue-based decoupling | Bedrock APIs, AWS SDKs, SQS, API Gateway | TBD | TBD | TBD | TBD | Official guide Task 2.4 | not started |
| 2.4 | 2.4.2 | Real-time interaction: streaming APIs, WebSockets/SSE, chunked transfer | Prereq: networking basics | Token streaming; SSE vs WebSockets | Bedrock streaming APIs, API Gateway | TBD | TBD | TBD | TBD | Official guide Task 2.4 | not started |
| 2.4 | 2.4.3 | Resilient FM systems: exponential backoff, rate limiting, fallbacks, tracing | Prereq: networking basics | Retry with backoff; graceful degradation | AWS SDKs, API Gateway, X-Ray | TBD | TBD | TBD | TBD | Official guide Task 2.4 | not started |
| 2.4 | 2.4.4 | Intelligent model routing: static, dynamic content-based, metrics-based | Prereq: 1.2.1 | Routing tiers; request transformation | Step Functions, API Gateway | TBD | TBD | TBD | TBD | Official guide Task 2.4 | not started |
| 2.5 | 2.5.1 | FM API interfaces via API Gateway: streaming, token limits, retries | Prereq: networking basics; compute limits | API Gateway limits for streaming workloads | API Gateway | TBD | TBD | TBD | TBD | Official guide Task 2.5 | not started |
| 2.5 | 2.5.2 | Accessible AI interfaces: declarative UI, API-first, no-code workflow builders | Prereq: none | UI integration patterns | Amplify, OpenAPI, Bedrock Prompt Flows | TBD | TBD | TBD | TBD | Official guide Task 2.5 | not started |
| 2.5 | 2.5.3 | Business system enhancements: CRM, document processing, automated data workflows | Prereq: 1.3.2 | Document processing orchestration | Lambda, Step Functions, Bedrock Data Automation | TBD | TBD | TBD | TBD | Official guide Task 2.5 | not started |
| 2.5 | 2.5.4 | Developer productivity: Q Developer for code gen/refactor/testing | Prereq: none | AI coding assistance | Amazon Q Developer | TBD | TBD | TBD | TBD | Official guide Task 2.5 | not started |
| 2.5 | 2.5.5 | Advanced GenAI apps: native orchestration, agent patterns, prompt chaining | Prereq: 2.1.1, 1.6.6 | Agent design patterns | Strands Agents, AWS Agent Squad, Step Functions, Bedrock | TBD | TBD | TBD | TBD | Official guide Task 2.5 | not started |
| 2.5 | 2.5.6 | Troubleshooting efficiency: Logs Insights, X-Ray tracing, error pattern recognition | Prereq: none | Log-based debugging; distributed tracing | CloudWatch Logs Insights, X-Ray, Q Developer | TBD | TBD | TBD | TBD | Official guide Task 2.5 | not started |

---

## Domain 3: AI Safety, Security, and Governance (20%)

| Task | Skill | Skill summary | Prerequisite dependencies | Required concepts | Relevant services | Lesson | Comp. table | Worked scenario | Practice Q IDs | Evidence sources | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 3.1 | 3.1.1 | Content safety against harmful user inputs | Prereq: ML basics (prompt attacks) | Content filters; custom moderation workflows; real-time validation | Bedrock Guardrails, Step Functions, Lambda | TBD | TBD | TBD | TBD | Official guide Task 3.1 | not started |
| 3.1 | 3.1.2 | Content safety against harmful outputs | Prereq: 3.1.1 | Output filtering; toxicity evals; deterministic alternatives | Bedrock Guardrails, FM evaluations, text-to-SQL | TBD | TBD | TBD | TBD | Official guide Task 3.1 | not started |
| 3.1 | 3.1.3 | Accuracy verification to reduce hallucinations: grounding, fact-checking, confidence scoring, structured outputs | Prereq: 1.5.x (retrieval) | Grounding; confidence scoring; schema enforcement | Bedrock Knowledge Bases, JSON Schema | TBD | TBD | TBD | TBD | Official guide Task 3.1 | not started |
| 3.1 | 3.1.4 | Defense-in-depth safety: pre-processing filters, model guardrails, post-processing validation, API response filtering | Prereq: 3.1.1 | Layered controls | Comprehend, Bedrock, Lambda, API Gateway | TBD | TBD | TBD | TBD | Official guide Task 3.1 | not started |
| 3.1 | 3.1.5 | Advanced threat detection: prompt injection/jailbreak detection, sanitization, safety classifiers, adversarial testing | Prereq: ML basics (attack types) | Injection vs jailbreak; adversarial testing | (mechanism-level) | TBD | TBD | TBD | TBD | Official guide Task 3.1 | not started |
| 3.2 | 3.2.1 | Protected AI environments: VPC endpoints, IAM access patterns, granular data access, access monitoring | Prereq: networking basics (VPC endpoints); IAM basics | PrivateLink; least privilege; data access monitoring | VPC endpoints, IAM, Lake Formation, CloudWatch | TBD | TBD | TBD | TBD | Official guide Task 3.2 | not started |
| 3.2 | 3.2.2 | Privacy-preserving systems: PII detection, native privacy features, output filtering, retention | Prereq: IAM basics; encryption/KMS | PII lifecycle; retention policies | Comprehend, Macie, Bedrock, Bedrock Guardrails, S3 Lifecycle | TBD | TBD | TBD | TBD | Official guide Task 3.2 | not started |
| 3.2 | 3.2.3 | Privacy-focused systems: masking, PII detection, anonymization | Prereq: 3.2.2 | Masking vs anonymization vs redaction | Comprehend, Bedrock Guardrails | TBD | TBD | TBD | TBD | Official guide Task 3.2 | not started |
| 3.3 | 3.3.1 | Compliance frameworks: model cards, data lineage, metadata tagging, decision logs | Prereq: none | Provenance; auditability | SageMaker AI (model cards), Glue (lineage), CloudWatch Logs | TBD | TBD | TBD | TBD | Official guide Task 3.3 | not started |
| 3.3 | 3.3.2 | Data source tracking and traceability | Prereq: 3.3.1 | Source attribution; audit logging | Glue Data Catalog, metadata tagging, CloudTrail | TBD | TBD | TBD | TBD | Official guide Task 3.3 | not started |
| 3.3 | 3.3.3 | Organizational governance systems aligned to policy, regulation, responsible AI | Prereq: 3.3.1-3.3.2 | Governance frameworks | (framework-level) | TBD | TBD | TBD | TBD | Official guide Task 3.3 | not started |
| 3.3 | 3.3.4 | Continuous monitoring and advanced governance: misuse/drift detection, bias drift, alerting, remediation, token redaction, response logging | Prereq: none beyond 3.3.1 | Drift types; alerting loops | (monitoring-level) | TBD | TBD | TBD | TBD | Official guide Task 3.3 | not started |
| 3.4 | 3.4.1 | Transparent AI: reasoning displays, confidence metrics, evidence attribution, reasoning traces | Prereq: none | Explainability vs faithfulness | CloudWatch, Bedrock agent tracing | TBD | TBD | TBD | TBD | Official guide Task 3.4 | not started |
| 3.4 | 3.4.2 | Fairness evaluations: fairness metrics, A/B testing, LLM-as-a-judge | Prereq: 5.1.x concepts | Fairness metrics; evaluation methods | CloudWatch, Bedrock Prompt Management, Bedrock Prompt Flows | TBD | TBD | TBD | TBD | Official guide Task 3.4 | not started |
| 3.4 | 3.4.3 | Policy-compliant AI: guardrails from policy, model cards, automated compliance checks | Prereq: 3.1.1, 3.3.1 | Policy-to-control mapping | Bedrock Guardrails, model cards, Lambda | TBD | TBD | TBD | TBD | Official guide Task 3.4 | not started |

---

## Domain 4: Operational Efficiency and Optimization for GenAI Applications (12%)

| Task | Skill | Skill summary | Prerequisite dependencies | Required concepts | Relevant services | Lesson | Comp. table | Worked scenario | Practice Q IDs | Evidence sources | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.1 | 4.1.1 | Token efficiency: estimation, tracking, context optimization, compression, pruning, response limits | Prereq: ML basics (tokens) | Token economics; compression vs quality | (technique-level) | TBD | TBD | TBD | TBD | Official guide Task 4.1 | not started |
| 4.1 | 4.1.2 | Cost-effective model selection: trade-offs, tiered usage, price-to-performance | Prereq: 1.2.1 | Tiered routing; inference cost balancing | (framework-level) | TBD | TBD | TBD | TBD | Official guide Task 4.1 | not started |
| 4.1 | 4.1.3 | High-performance FM systems: batching, capacity planning, utilization, auto-scaling, provisioned throughput | Prereq: compute limits; 2.2.1 | Throughput levers | (capacity-level) | TBD | TBD | TBD | TBD | Official guide Task 4.1 | not started |
| 4.1 | 4.1.4 | Intelligent caching: semantic caching, fingerprinting, edge caching, deterministic hashing, prompt caching | Prereq: ML basics (embeddings) | Cache hit criteria; TTL; cache invalidation | ElastiCache, CloudFront (edge), Bedrock prompt caching | TBD | TBD | TBD | TBD | Official guide Task 4.1 | not started |
| 4.2 | 4.2.1 | Responsive AI: pre-computation, latency-optimized models, parallel requests, streaming, benchmarking | Prereq: networking basics; compute limits | Latency levers; perceived vs actual latency | Bedrock models, (streaming-level) | TBD | TBD | TBD | TBD | Official guide Task 4.2 | not started |
| 4.2 | 4.2.2 | Retrieval performance: index optimization, query preprocessing, hybrid search with custom scoring | Prereq: 1.5.4 | Index tuning; scoring functions | OpenSearch Service | TBD | TBD | TBD | TBD | Official guide Task 4.2 | not started |
| 4.2 | 4.2.3 | FM throughput optimization: token processing, batch inference, concurrent invocations | Prereq: compute limits | Batch vs real-time; concurrency management | (batch inference-level) | TBD | TBD | TBD | TBD | Official guide Task 4.2 | not started |
| 4.2 | 4.2.4 | Performance tuning per use case: parameters, A/B testing, temperature/top-k/top-p | Prereq: ML basics (sampling params) | Sampling parameters; determinism vs creativity | (parameter-level) | TBD | TBD | TBD | TBD | Official guide Task 4.2 | not started |
| 4.2 | 4.2.5 | Efficient resource allocation: capacity planning for tokens, utilization monitoring, GenAI-tuned auto-scaling | Prereq: compute limits | Traffic pattern modeling | Auto Scaling | TBD | TBD | TBD | TBD | Official guide Task 4.2 | not started |
| 4.2 | 4.2.6 | FM system performance for GenAI workflows: API profiling, vector DB query optimization, inference latency reduction, service communication | Prereq: 1.5.3 | Profiling; query optimization | (profiling-level) | TBD | TBD | TBD | TBD | Official guide Task 4.2 | not started |
| 4.3 | 4.3.1 | Holistic observability: metrics, tracing, FM interaction tracing, business metrics, dashboards | Prereq: none | Observability pillars | CloudWatch dashboards | TBD | TBD | TBD | TBD | Official guide Task 4.3 | not started |
| 4.3 | 4.3.2 | GenAI monitoring: token usage, prompt effectiveness, hallucination rates, response quality, anomaly detection, invocation logs, cost anomaly | Prereq: 4.3.1 | FM-specific KPIs; anomaly detection | CloudWatch, Bedrock Model Invocation Logs, Cost Anomaly Detection | TBD | TBD | TBD | TBD | Official guide Task 4.3 | not started |
| 4.3 | 4.3.3 | Integrated observability: dashboards, business impact, compliance monitoring, forensic traceability, audit logging, user tracking, behavior patterns | Prereq: 4.3.1 | Audit vs metrics distinction | CloudWatch, CloudTrail | TBD | TBD | TBD | TBD | Official guide Task 4.3 | not started |
| 4.3 | 4.3.4 | Tool performance frameworks: call patterns, metrics, tool-calling observability, multi-agent coordination, baselines | Prereq: 2.1.1 | Agent telemetry | (observability-level) | TBD | TBD | TBD | TBD | Official guide Task 4.3 | not started |
| 4.3 | 4.3.5 | Vector store operations: performance monitoring, automated index optimization, data quality validation | Prereq: 1.4.1, 1.4.3 | Index health metrics | OpenSearch Service | TBD | TBD | TBD | TBD | Official guide Task 4.3 | not started |
| 4.3 | 4.3.6 | FM-specific troubleshooting: golden datasets, output diffing, reasoning path tracing, observability pipelines | Prereq: ML basics | GenAI failure modes | (pipeline-level) | TBD | TBD | TBD | TBD | Official guide Task 4.3 | not started |

---

## Domain 5: Testing, Validation, and Troubleshooting (11%)

| Task | Skill | Skill summary | Prerequisite dependencies | Required concepts | Relevant services | Lesson | Comp. table | Worked scenario | Practice Q IDs | Evidence sources | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 5.1 | 5.1.1 | Assessment frameworks beyond traditional ML metrics: relevance, factual accuracy, consistency, fluency | Prereq: ML basics | GenAI quality dimensions | (metrics-level) | TBD | TBD | TBD | TBD | Official guide Task 5.1 | not started |
| 5.1 | 5.1.2 | Systematic model evaluation: Bedrock Model Evaluations, A/B and canary testing, multi-model eval, cost-performance analysis | Prereq: 5.1.1 | Eval types; token efficiency; latency-to-quality ratios | Bedrock Model Evaluations | TBD | TBD | TBD | TBD | Official guide Task 5.1 | not started |
| 5.1 | 5.1.3 | User-centered evaluation: feedback interfaces, rating systems, annotation workflows | Prereq: none | Human feedback loops | (UX-level) | TBD | TBD | TBD | TBD | Official guide Task 5.1 | not started |
| 5.1 | 5.1.4 | QA processes: continuous evaluation, regression testing, automated quality gates | Prereq: 5.1.2 | Regression gates for model/prompt changes | (pipeline-level) | TBD | TBD | TBD | TBD | Official guide Task 5.1 | not started |
| 5.1 | 5.1.5 | Multi-perspective assessment: RAG evaluation, LLM-as-a-judge, human feedback | Prereq: 5.1.2 | RAG eval dimensions; judge bias | (eval-level) | TBD | TBD | TBD | TBD | Official guide Task 5.1 | not started |
| 5.1 | 5.1.6 | Retrieval quality testing: relevance scoring, context matching, retrieval latency | Prereq: 1.5.x | Retrieval metrics | (retrieval-level) | TBD | TBD | TBD | TBD | Official guide Task 5.1 | not started |
| 5.1 | 5.1.7 | Agent performance frameworks: task completion, tool effectiveness, Bedrock Agent evals, reasoning quality | Prereq: 2.1.1 | Agent eval dimensions | Bedrock Agent evaluations | TBD | TBD | TBD | TBD | Official guide Task 5.1 | not started |
| 5.1 | 5.1.8 | Reporting systems: visualizations, automated reporting, model comparison | Prereq: 5.1.2 | Stakeholder communication | QuickSight, CloudWatch dashboards | TBD | TBD | TBD | TBD | Official guide Task 5.1 | not started |
| 5.1 | 5.1.9 | Deployment validation: synthetic user workflows, hallucination rate and semantic drift checks, consistency checks | Prereq: 5.1.4 | Deployment safety gates | (validation-level) | TBD | TBD | TBD | TBD | Official guide Task 5.1 | not started |
| 5.2 | 5.2.1 | Content handling troubleshooting: context overflow diagnostics, dynamic chunking, prompt optimization, truncation analysis | Prereq: ML basics (tokens); 1.5.1 | Context window mechanics | (diagnostic-level) | TBD | TBD | TBD | TBD | Official guide Task 5.2 | not started |
| 5.2 | 5.2.2 | FM integration troubleshooting: error logging, request validation, response analysis | Prereq: networking basics | API error classes | CloudWatch Logs | TBD | TBD | TBD | TBD | Official guide Task 5.2 | not started |
| 5.2 | 5.2.3 | Prompt troubleshooting beyond basics: testing frameworks, version comparison, systematic refinement | Prereq: 1.6.3-1.6.5 | Prompt debugging workflow | (prompt-level) | TBD | TBD | TBD | TBD | Official guide Task 5.2 | not started |
| 5.2 | 5.2.4 | Retrieval troubleshooting: relevance analysis, embedding diagnostics, drift monitoring, vectorization fixes, chunking remediation, search perf | Prereq: 1.5.x | Retrieval debug chain (retrieval -> grounding -> chunking) | (retrieval-level) | TBD | TBD | TBD | TBD | Official guide Task 5.2 | not started |
| 5.2 | 5.2.5 | Prompt maintenance troubleshooting: template testing, Logs-based prompt-confusion diagnosis, X-Ray observability, schema validation, refinement | Prereq: 1.6.3 | Prompt drift; format consistency | CloudWatch Logs, X-Ray | TBD | TBD | TBD | TBD | Official guide Task 5.2 | not started |

---

## Summary counts

- Domain 1: 28 skills (Tasks 1.1:3, 1.2:4, 1.3:4, 1.4:5, 1.5:6, 1.6:6)
- Domain 2: 25 skills (Tasks 2.1:7, 2.2:3, 2.3:5, 2.4:4, 2.5:6)
- Domain 3: 15 skills (Tasks 3.1:5, 3.2:3, 3.3:4, 3.4:3)
- Domain 4: 16 skills (Tasks 4.1:4, 4.2:6, 4.3:6)
- Domain 5: 14 skills (Tasks 5.1:9, 5.2:5)
- **Total: 98 skills. All not started.**

Mastery gate per skill (from Stage 1 plan): mechanism explanation + decision rule with limitations + application example + diagnostic/assessment opportunity. The lesson-plan stage fills the TBD columns.

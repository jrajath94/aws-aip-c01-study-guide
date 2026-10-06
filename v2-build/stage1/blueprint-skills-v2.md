# AIP-C01 Blueprint: Full Domain/Task/Skill Structure (v2 build, Stage 1)

Research date: 2026-10-06. Source: official AIP-C01 exam guide (HTML domain pages 1-5 + official PDF), read in full.

IMPORTANT COPYRIGHT NOTE FOR BUILDERS: the statements below are faithful paraphrases of the official skill text, labeled as such. Do not copy the official guide verbatim into publishable study material beyond brief fair-use quotes. Skill statements are paraphrased; the AWS services and mechanisms the guide names as examples are transcribed because identifiers (service names) are facts, not creative text.

Legend: **[Paraphrase]** = faithful paraphrase of the official skill statement. **Services named in guide** = services/features the official guide cites as examples for that skill.

---

## Domain 1: Foundation Model Integration, Data Management, and Compliance (31%)

### Task 1.1: Analyze requirements and design GenAI solutions

- **Skill 1.1.1** [Paraphrase]: Produce full architectural designs matched to stated business needs and technical constraints (right FM, right integration pattern, right deployment strategy). Services named in guide: appropriate FMs, integration patterns, deployment strategies.
- **Skill 1.1.2** [Paraphrase]: Build technical proof-of-concept implementations to confirm feasibility, performance, and business value before full-scale deployment. Services named in guide: Amazon Bedrock.
- **Skill 1.1.3** [Paraphrase]: Build standardized reusable technical components so implementations stay consistent across many deployments. Services named in guide: AWS Well-Architected Framework, AWS WA Tool Generative AI Lens.

### Task 1.2: Select and configure FMs

- **Skill 1.2.1** [Paraphrase]: Evaluate and choose FMs so the choice fits the business use case and technical requirements (benchmarks, capability analysis, limitation evaluation). Services named in guide: performance benchmarks, capability analysis, limitation evaluation.
- **Skill 1.2.2** [Paraphrase]: Build flexible architecture patterns that allow dynamic model selection and provider switching with no code changes. Services named in guide: AWS Lambda, Amazon API Gateway, AWS AppConfig.
- **Skill 1.2.3** [Paraphrase]: Design resilient AI systems that keep operating through service disruptions. Services named in guide: AWS Step Functions circuit breaker patterns, Amazon Bedrock Cross-Region Inference (for models with limited regional availability), cross-Region model deployment, graceful degradation strategies.
- **Skill 1.2.4** [Paraphrase]: Deploy and manage the FM customization lifecycle: deploy domain-specific fine-tuned models; use parameter-efficient adaptation (LoRA, adapters); version with a model registry; use automated deployment pipelines; plan rollback for failed deployments; retire and replace models at end of life. Services named in guide: Amazon SageMaker AI, LoRA and adapters, SageMaker Model Registry, automated deployment pipelines, rollback strategies, lifecycle management.

### Task 1.3: Implement data validation and processing pipelines for FM consumption

- **Skill 1.3.1** [Paraphrase]: Build data validation workflows so data meets quality standards before FM consumption. Services named in guide: AWS Glue Data Quality, SageMaker Data Wrangler, custom Lambda functions, Amazon CloudWatch metrics.
- **Skill 1.3.2** [Paraphrase]: Build data processing workflows for complex data types - text, image, audio, tabular - with the specialized processing each needs for FM consumption. Services named in guide: Amazon Bedrock multimodal models, SageMaker Processing, AWS Transcribe, advanced multimodal pipeline architectures.
- **Skill 1.3.3** [Paraphrase]: Format input data for FM inference per model-specific requirements. Services named in guide: JSON formatting for Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications.
- **Skill 1.3.4** [Paraphrase]: Improve input data quality to get better, more consistent FM responses. Services named in guide: Amazon Bedrock (text reformatting), Amazon Comprehend (entity extraction), Lambda functions (normalization).

### Task 1.4: Design and implement vector store solutions

- **Skill 1.4.1** [Paraphrase]: Design vector database architectures purpose-built for FM augmentation, enabling efficient semantic retrieval beyond keyword search. Services named in guide: Amazon Bedrock Knowledge Bases (hierarchical organization), Amazon OpenSearch Service with the Neural plugin for Bedrock integration (topic-based segmentation), Amazon RDS with Amazon S3 document repositories, Amazon DynamoDB with vector databases (metadata and embeddings).
- **Skill 1.4.2** [Paraphrase]: Build metadata frameworks that improve search precision and context awareness in FM interactions. Services named in guide: S3 object metadata (document timestamps), custom attributes (authorship), tagging systems (domain classification).
- **Skill 1.4.3** [Paraphrase]: Build high-performance vector database architectures that keep semantic search fast at scale. Services named in guide: OpenSearch sharding strategies, multi-index approaches for specialized domains, hierarchical indexing techniques.
- **Skill 1.4.4** [Paraphrase]: Use AWS services to build integration components that connect GenAI applications to document management systems, knowledge bases, and internal wikis for comprehensive data integration. Services named in guide: document management systems, knowledge bases, internal wikis.
- **Skill 1.4.5** [Paraphrase]: Build data maintenance systems that keep vector stores current and accurate. Services named in guide: incremental update mechanisms, real-time change detection, automated synchronization workflows, scheduled refresh pipelines.

### Task 1.5: Design retrieval mechanisms for FM augmentation

- **Skill 1.5.1** [Paraphrase]: Design document segmentation (chunking) approaches that optimize retrieval performance for FM context augmentation. Services named in guide: Amazon Bedrock chunking capabilities, Lambda functions for fixed-size chunking, custom processing for hierarchical chunking based on content structure.
- **Skill 1.5.2** [Paraphrase]: Select and configure embedding solutions to create efficient vector representations for semantic search (dimensionality and domain fit). Services named in guide: Amazon Titan embeddings, Amazon Bedrock embedding models, Lambda functions to batch-generate embeddings.
- **Skill 1.5.3** [Paraphrase]: Deploy and configure vector search solutions for semantic search in FM augmentation. Services named in guide: OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality.
- **Skill 1.5.4** [Paraphrase]: Build advanced search architectures that improve relevance and accuracy of retrieved information. Services named in guide: OpenSearch for semantic search, hybrid search combining keywords and vectors, Amazon Bedrock reranker models.
- **Skill 1.5.5** [Paraphrase]: Build sophisticated query handling systems (expansion, decomposition, transformation) that improve retrieval effectiveness and result quality. Services named in guide: Amazon Bedrock for query expansion, Lambda functions for query decomposition, Step Functions for query transformation.
- **Skill 1.5.6** [Paraphrase]: Build consistent access mechanisms for seamless FM integration (standardized retrieval interfaces). Services named in guide: function calling interfaces for vector search, MCP clients for vector queries, standardized API patterns for retrieval augmentation.

### Task 1.6: Implement prompt engineering strategies and governance for FM interactions

- **Skill 1.6.1** [Paraphrase]: Build model instruction frameworks that control FM behavior and outputs. Services named in guide: Amazon Bedrock Prompt Management (role definitions), Amazon Bedrock Guardrails (responsible AI guidelines), template configurations (response formatting).
- **Skill 1.6.2** [Paraphrase]: Build interactive AI systems that maintain context and improve user interactions with FMs (clarification, intent, conversation memory). Services named in guide: Step Functions (clarification workflows), Amazon Comprehend (intent recognition), DynamoDB (conversation history storage).
- **Skill 1.6.3** [Paraphrase]: Build prompt management and governance systems - parameterized templates, approval workflows, template repositories, usage audit, access logging. Services named in guide: Amazon Bedrock Prompt Management, Amazon S3 (template repositories), AWS CloudTrail (usage tracking), Amazon CloudWatch Logs (access logging).
- **Skill 1.6.4** [Paraphrase]: Build quality assurance systems that verify prompt effectiveness and reliability (output verification, edge-case testing, prompt regression testing). Services named in guide: Lambda (verify expected output), Step Functions (edge cases), CloudWatch (prompt regression).
- **Skill 1.6.5** [Paraphrase]: Iteratively refine prompts to improve response quality beyond basic prompting. Services named in guide: structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops.
- **Skill 1.6.6** [Paraphrase]: Design complex prompt systems for sophisticated tasks - sequential prompt chains, conditional branching, reusable prompt components, integrated pre/post-processing. Services named in guide: Amazon Bedrock Prompt Flows.

---

## Domain 2: Implementation and Integration (26%)

### Task 2.1: Implement agentic AI solutions and tool integrations

- **Skill 2.1.1** [Paraphrase]: Build intelligent autonomous systems with proper memory and state management. Services named in guide: Strands Agents and AWS Agent Squad (multi-agent systems), MCP (agent-tool interactions).
- **Skill 2.1.2** [Paraphrase]: Build problem-solving systems that let FMs break complex problems into structured reasoning steps. Services named in guide: Step Functions (ReAct patterns, chain-of-thought reasoning).
- **Skill 2.1.3** [Paraphrase]: Build safeguarded AI workflows that keep FM behavior controlled. Services named in guide: Step Functions (stopping conditions), Lambda (timeout mechanisms), IAM policies (resource boundaries), circuit breakers (failure mitigation).
- **Skill 2.1.4** [Paraphrase]: Build model coordination systems that optimize performance across multiple capabilities (specialized models, ensembles, selection). Services named in guide: specialized FMs for complex tasks, custom aggregation logic for model ensembles, model selection frameworks.
- **Skill 2.1.5** [Paraphrase]: Build collaborative AI systems that combine FM capabilities with human expertise. Services named in guide: Step Functions (review/approval processes), API Gateway (feedback collection), human augmentation patterns.
- **Skill 2.1.6** [Paraphrase]: Build intelligent tool integrations that extend FM capabilities with reliable tool operations. Services named in guide: Strands API (custom behaviors), standardized function definitions, Lambda (error handling, parameter validation).
- **Skill 2.1.7** [Paraphrase]: Build model extension frameworks (MCP servers) that enhance FM capabilities - lightweight tools on stateless Lambda, complex tools on ECS, consistent client access patterns. Services named in guide: Lambda (stateless MCP servers), Amazon ECS (complex-tool MCP servers), MCP client libraries.

### Task 2.2: Implement model deployment strategies

- **Skill 2.2.1** [Paraphrase]: Deploy FMs to fit application needs and performance requirements. Services named in guide: Lambda (on-demand invocation), Amazon Bedrock provisioned throughput, SageMaker AI endpoints (hybrid solutions).
- **Skill 2.2.2** [Paraphrase]: Handle the deployment challenges specific to LLMs (unlike traditional ML): container deployment patterns optimized for memory, GPU utilization, token processing capacity, and model loading strategies. Services named in guide: container-based deployment patterns, specialized model loading strategies.
- **Skill 2.2.3** [Paraphrase]: Build optimized FM deployment approaches balancing performance and resources - right-size the model, use smaller pre-trained models for specific tasks, cascade routine queries across models via APIs. Services named in guide: model selection, smaller pre-trained models, API-based model cascading.

### Task 2.3: Design and implement enterprise integration architectures

- **Skill 2.3.1** [Paraphrase]: Build enterprise connectivity that brings FM capabilities into existing enterprise environments. Services named in guide: API-based legacy integrations, event-driven architectures (loose coupling), data synchronization patterns.
- **Skill 2.3.2** [Paraphrase]: Add GenAI functionality to existing applications. Services named in guide: API Gateway (microservice integrations), Lambda (webhook handlers), Amazon EventBridge (event-driven integrations).
- **Skill 2.3.3** [Paraphrase]: Build secure access frameworks with proper controls. Services named in guide: identity federation between FM services and enterprise systems, role-based access control for model and data access, least-privilege FM API access.
- **Skill 2.3.4** [Paraphrase]: Build cross-environment AI solutions that keep data compliant across jurisdictions while enabling FM access. Services named in guide: AWS Outposts (on-premises data integration), AWS Wavelength (edge deployments), secure routing between cloud and on-premises.
- **Skill 2.3.5** [Paraphrase]: Build CI/CD pipelines and GenAI gateway architectures for secure, compliant enterprise consumption of FMs. Services named in guide: AWS CodePipeline, AWS CodeBuild, automated testing frameworks (continuous deployment/testing of GenAI components with security scans and rollback support), centralized abstraction layers, observability and control mechanisms.

### Task 2.4: Implement FM API integrations

- **Skill 2.4.1** [Paraphrase]: Build flexible model interaction systems - synchronous requests from various compute environments via Bedrock APIs, async via language-specific SDKs and SQS, custom API clients with request validation via API Gateway. Services named in guide: Amazon Bedrock APIs, language-specific AWS SDKs, Amazon SQS, API Gateway.
- **Skill 2.4.2** [Paraphrase]: Build real-time AI interaction systems for immediate feedback. Services named in guide: Amazon Bedrock streaming APIs (incremental response delivery), WebSockets or server-sent events (real-time text generation), API Gateway (chunked transfer encoding).
- **Skill 2.4.3** [Paraphrase]: Build resilient FM systems for reliable operations. Services named in guide: AWS SDK exponential backoff, API Gateway rate limiting, fallback mechanisms (graceful degradation), AWS X-Ray (observability across service boundaries).
- **Skill 2.4.4** [Paraphrase]: Build intelligent model routing systems that optimize model selection (static routing configs, dynamic content-based routing, metrics-based intelligent routing). Services named in guide: application code (static routing), Step Functions (dynamic content-based routing to specialized FMs), API Gateway with request transformations.

### Task 2.5: Implement application integration patterns and development tools

- **Skill 2.5.1** [Paraphrase]: Build FM API interfaces tuned to GenAI workload needs via API Gateway: streaming responses, token limit management, retry strategies for model timeouts. Services named in guide: API Gateway.
- **Skill 2.5.2** [Paraphrase]: Build accessible AI interfaces that accelerate FM adoption. Services named in guide: AWS Amplify (declarative UI components), OpenAPI specs (API-first development), Amazon Bedrock Prompt Flows (no-code workflow builders).
- **Skill 2.5.3** [Paraphrase]: Enhance business systems with GenAI - e.g. CRM enhancements, document processing orchestration, automated data processing workflows. Services named in guide: Lambda (CRM enhancements), Step Functions (document processing), Amazon Bedrock Data Automation.
- **Skill 2.5.4** [Paraphrase]: Boost developer productivity for GenAI application workflows. Services named in guide: Amazon Q Developer (code generation/refactoring, code suggestions, API assistance, AI component testing, performance optimization).
- **Skill 2.5.5** [Paraphrase]: Build advanced GenAI applications with sophisticated AI capabilities. Services named in guide: Strands Agents and AWS Agent Squad (AWS-native orchestration), Step Functions (agent design patterns), Amazon Bedrock (prompt chaining patterns).
- **Skill 2.5.6** [Paraphrase]: Improve troubleshooting efficiency for FM applications. Services named in guide: CloudWatch Logs Insights (prompt/response analysis), X-Ray (FM API call tracing), Amazon Q Developer (GenAI-specific error pattern recognition).

---

## Domain 3: AI Safety, Security, and Governance (20%)

### Task 3.1: Implement input and output safety controls

- **Skill 3.1.1** [Paraphrase]: Build content safety systems against harmful user inputs to FMs. Services named in guide: Amazon Bedrock Guardrails (content filtering), Step Functions and Lambda (custom moderation workflows), real-time validation mechanisms.
- **Skill 3.1.2** [Paraphrase]: Build content safety frameworks that prevent harmful outputs. Services named in guide: Amazon Bedrock Guardrails (response filtering), specialized FM evaluations (content moderation/toxicity detection), text-to-SQL transformations (deterministic results).
- **Skill 3.1.3** [Paraphrase]: Build accuracy verification systems that reduce hallucinations - ground responses with retrieval, fact-checking, confidence scoring, semantic similarity verification, structured output enforcement. Services named in guide: Amazon Bedrock Knowledge Bases, confidence scoring, semantic similarity search, JSON Schema.
- **Skill 3.1.4** [Paraphrase]: Build defense-in-depth safety systems against FM misuse: pre-processing filters, model-based guardrails, post-processing validation, API response filtering. Services named in guide: Amazon Comprehend (pre-processing), Amazon Bedrock (model-based guardrails), Lambda (post-processing validation), API Gateway (response filtering).
- **Skill 3.1.5** [Paraphrase]: Build advanced threat detection for adversarial inputs and security vulnerabilities: prompt injection/jailbreak detection, input sanitization, content filters, safety classifiers, automated adversarial testing. Services named in guide: prompt injection and jailbreak detection mechanisms, input sanitization, content filters, safety classifiers, adversarial testing workflows.

### Task 3.2: Implement data security and privacy controls

- **Skill 3.2.1** [Paraphrase]: Build protected AI environments for FM deployments - network isolation, secure data access patterns, granular data access, access monitoring. Services named in guide: VPC endpoints, IAM policies, AWS Lake Formation, CloudWatch.
- **Skill 3.2.2** [Paraphrase]: Build privacy-preserving systems for sensitive information during FM interactions: PII detection, native data privacy features, output filtering, data retention policies. Services named in guide: Amazon Comprehend and Amazon Macie (PII detection), Amazon Bedrock native data privacy features, Amazon Bedrock Guardrails (output filtering), Amazon S3 Lifecycle configurations (retention).
- **Skill 3.2.3** [Paraphrase]: Build privacy-focused AI systems that protect user privacy without killing FM utility - data masking, PII detection, anonymization strategies. Services named in guide: data masking techniques, Amazon Comprehend PII detection, anonymization strategies, Amazon Bedrock Guardrails.

### Task 3.3: Implement AI governance and compliance mechanisms

- **Skill 3.3.1** [Paraphrase]: Build compliance frameworks for FM deployments: programmatic model cards, automatic data lineage tracking, metadata tagging for source attribution, decision logs. Services named in guide: SageMaker AI (programmatic model cards), AWS Glue (data lineage), metadata tagging, CloudWatch Logs (decision logs).
- **Skill 3.3.2** [Paraphrase]: Build data source tracking for traceability in GenAI applications. Services named in guide: AWS Glue Data Catalog (register data sources), metadata tagging (source attribution in generated content), CloudTrail (audit logging).
- **Skill 3.3.3** [Paraphrase]: Build organizational governance systems giving consistent oversight of FM implementations aligned with organizational policies, regulatory requirements, and responsible AI principles. Services named in guide: comprehensive frameworks aligned with organizational policies, regulatory requirements, responsible AI principles.
- **Skill 3.3.4** [Paraphrase]: Build continuous monitoring and advanced governance controls for safety audits and regulatory readiness: automated misuse/drift/policy-violation detection, bias drift monitoring, alerting and remediation workflows, token-level redaction, response logging, AI output policy filters. Services named in guide: automated detection systems, bias drift monitoring, alerting/remediation workflows, token-level redaction, response logging, AI output policy filters.

### Task 3.4: Implement responsible AI principles

- **Skill 3.4.1** [Paraphrase]: Build transparent AI systems for FM outputs: user-facing reasoning explanations, confidence metrics and uncertainty quantification, evidence/source attribution, reasoning traces. Services named in guide: reasoning displays, CloudWatch (confidence metrics), evidence presentation, Amazon Bedrock agent tracing.
- **Skill 3.4.2** [Paraphrase]: Apply fairness evaluations for unbiased FM outputs: pre-defined fairness metrics, systematic A/B testing, automated model evaluations with LLM-as-a-judge. Services named in guide: pre-defined fairness metrics in CloudWatch, Amazon Bedrock Prompt Management and Prompt Flows (A/B testing), Amazon Bedrock with LLM-as-a-judge.
- **Skill 3.4.3** [Paraphrase]: Build policy-compliant AI systems following responsible AI practices: guardrails from policy requirements, model cards documenting FM limitations, automated compliance checks. Services named in guide: Amazon Bedrock Guardrails, model cards, Lambda (compliance checks).

---

## Domain 4: Operational Efficiency and Optimization for GenAI Applications (12%)

### Task 4.1: Implement cost optimization and resource efficiency strategies

- **Skill 4.1.1** [Paraphrase]: Build token efficiency systems that cut FM costs without losing effectiveness: token estimation/tracking, context window optimization, response size controls, prompt compression, context pruning, response limiting. Services named in guide: token estimation and tracking, context window optimization, response size controls, prompt compression, context pruning, response limiting.
- **Skill 4.1.2** [Paraphrase]: Build cost-effective model selection frameworks: cost-capability tradeoff evaluation, tiered FM usage by query complexity, inference cost vs response quality balancing, price-to-performance measurement, efficient inference patterns. Services named in guide: tradeoff evaluation, tiered FM usage, inference cost balancing, price-to-performance measurement.
- **Skill 4.1.3** [Paraphrase]: Build high-performance FM systems that maximize resource utilization and throughput: batching, capacity planning, utilization monitoring, auto-scaling, provisioned throughput optimization. Services named in guide: batching strategies, capacity planning, utilization monitoring, auto-scaling configurations, provisioned throughput optimization.
- **Skill 4.1.4** [Paraphrase]: Build intelligent caching systems that cut costs and improve response times by skipping unnecessary FM calls: semantic caching, result fingerprinting, edge caching, deterministic request hashing, prompt caching. Services named in guide: semantic caching, result fingerprinting, edge caching, deterministic request hashing, prompt caching.

### Task 4.2: Optimize application performance

- **Skill 4.2.1** [Paraphrase]: Build responsive AI systems that handle latency-cost tradeoffs and improve UX: pre-computation for predictable queries, latency-optimized Bedrock models, parallel requests, response streaming, performance benchmarking. Services named in guide: pre-computation, latency-optimized Amazon Bedrock models, parallel requests, response streaming, performance benchmarking.
- **Skill 4.2.2** [Paraphrase]: Improve retrieval performance (relevance and speed) for FM context augmentation: index optimization, query preprocessing, hybrid search with custom scoring. Services named in guide: index optimization, query preprocessing, hybrid search with custom scoring.
- **Skill 4.2.3** [Paraphrase]: Optimize FM throughput for GenAI-specific challenges: token processing optimization, batch inference, concurrent invocation management. Services named in guide: token processing optimization, batch inference strategies, concurrent model invocation management.
- **Skill 4.2.4** [Paraphrase]: Tune FM performance for specific use cases: model-specific parameter configs, A/B testing of improvements, right temperature and top-k/top-p choices per requirement. Services named in guide: model-specific parameter configurations, A/B testing, temperature and top-k/top-p selection.
- **Skill 4.2.5** [Paraphrase]: Build efficient resource allocation systems for FM workloads: capacity planning for token processing, utilization monitoring for prompt/completion patterns, auto-scaling tuned to GenAI traffic patterns. Services named in guide: capacity planning, utilization monitoring, auto-scaling configurations optimized for GenAI traffic.
- **Skill 4.2.6** [Paraphrase]: Optimize FM system performance for GenAI workflows: API call profiling for prompt-completion patterns, vector database query optimization, LLM inference latency reduction, efficient service communication patterns. Services named in guide: API call profiling, vector DB query optimization, latency reduction techniques for LLM inference, efficient service communication.

### Task 4.3: Implement monitoring systems for GenAI applications

- **Skill 4.3.1** [Paraphrase]: Build holistic observability systems giving complete visibility into FM application performance: operational metrics, performance tracing, FM interaction tracing, business impact metrics with custom dashboards. Services named in guide: operational metrics, performance tracing, FM interaction tracing, business impact metrics with custom dashboards.
- **Skill 4.3.2** [Paraphrase]: Build comprehensive GenAI monitoring systems that proactively find issues and track FM-specific KPIs: CloudWatch for token usage / prompt effectiveness / hallucination rates / response quality; anomaly detection for token bursts and response drift; Bedrock Model Invocation Logs for request/response analysis; performance benchmarks; cost anomaly detection. Services named in guide: CloudWatch, anomaly detection, Amazon Bedrock Model Invocation Logs, performance benchmarks, cost anomaly detection.
- **Skill 4.3.3** [Paraphrase]: Build integrated observability solutions giving actionable insights: operational dashboards, business impact visualizations, compliance monitoring, forensic traceability and audit logging, user interaction tracking, model behavior pattern tracking. Services named in guide: dashboards, business impact visualizations, compliance monitoring, forensic traceability, audit logging, user interaction tracking, model behavior pattern tracking.
- **Skill 4.3.4** [Paraphrase]: Build tool performance frameworks for optimal FM tool operation: call pattern tracking, performance metric collection, tool-calling observability, multi-agent coordination tracking, usage baselines for anomaly detection. Services named in guide: call pattern tracking, performance metric collection, tool calling observability, multi-agent coordination tracking, usage baselines.
- **Skill 4.3.5** [Paraphrase]: Build vector store operational management systems: performance monitoring for vector databases, automated index optimization, data quality validation. Services named in guide: performance monitoring, automated index optimization routines, data quality validation processes.
- **Skill 4.3.6** [Paraphrase]: Build FM-specific troubleshooting frameworks that catch GenAI failure modes traditional ML lacks: golden datasets for hallucination detection, output diffing for response consistency, reasoning path tracing for logical errors, specialized observability pipelines. Services named in guide: golden datasets, output diffing techniques, reasoning path tracing, specialized observability pipelines.

---

## Domain 5: Testing, Validation, and Troubleshooting (11%)

### Task 5.1: Implement evaluation systems for GenAI

- **Skill 5.1.1** [Paraphrase]: Build assessment frameworks that judge FM output quality and effectiveness beyond traditional ML metrics - relevance, factual accuracy, consistency, fluency. Services named in guide: metrics for relevance, factual accuracy, consistency, fluency.
- **Skill 5.1.2** [Paraphrase]: Build systematic model evaluation systems that identify optimal configurations: Bedrock Model Evaluations, A/B and canary testing of FMs, multi-model evaluation, cost-performance analysis (token efficiency, latency-to-quality ratios, business outcomes). Services named in guide: Amazon Bedrock Model Evaluations, A/B testing, canary testing, multi-model evaluation, cost-performance analysis.
- **Skill 5.1.3** [Paraphrase]: Build user-centered evaluation mechanisms that continuously improve FM performance from user experience: feedback interfaces, output rating systems, annotation workflows for response quality. Services named in guide: feedback interfaces, rating systems, annotation workflows.
- **Skill 5.1.4** [Paraphrase]: Build systematic QA processes that keep FM performance standards consistent: continuous evaluation workflows, regression testing for model outputs, automated quality gates for deployments. Services named in guide: continuous evaluation workflows, regression testing, automated quality gates.
- **Skill 5.1.5** [Paraphrase]: Build assessment systems that evaluate FM outputs from multiple perspectives: RAG evaluation, automated quality assessment with LLM-as-a-judge, human feedback collection. Services named in guide: RAG evaluation, LLM-as-a-judge, human feedback collection interfaces.
- **Skill 5.1.6** [Paraphrase]: Build retrieval quality testing that evaluates and optimizes information retrieval components for FM augmentation: relevance scoring, context matching verification, retrieval latency measurement. Services named in guide: relevance scoring, context matching verification, retrieval latency measurements.
- **Skill 5.1.7** [Paraphrase]: Build agent performance frameworks that confirm agents work correctly and efficiently: task completion rates, tool usage effectiveness, Bedrock Agent evaluations, reasoning quality assessment in multi-step workflows. Services named in guide: task completion rate measurements, tool usage effectiveness evaluations, Amazon Bedrock Agent evaluations, reasoning quality assessment.
- **Skill 5.1.8** [Paraphrase]: Build reporting systems that communicate performance metrics and insights to stakeholders: visualization tools, automated reporting, model comparison visualizations. Services named in guide: visualization tools, automated reporting mechanisms, model comparison visualizations.
- **Skill 5.1.9** [Paraphrase]: Build deployment validation systems that keep FM updates reliable: synthetic user workflows, AI-specific output validation (hallucination rates, semantic drift), automated quality checks for response consistency. Services named in guide: synthetic user workflows, hallucination rate and semantic drift validation, automated quality checks.

### Task 5.2: Troubleshoot GenAI applications

- **Skill 5.2.1** [Paraphrase]: Fix content handling issues so necessary information is processed completely in FM interactions: context window overflow diagnostics, dynamic chunking strategies, prompt design optimization, truncation error analysis. Services named in guide: context window overflow diagnostics, dynamic chunking, prompt design optimization, truncation-related error analysis.
- **Skill 5.2.2** [Paraphrase]: Diagnose and fix FM API integration issues: error logging, request validation, response analysis. Services named in guide: error logging, request validation, response analysis.
- **Skill 5.2.3** [Paraphrase]: Troubleshoot prompt engineering problems beyond basic prompt tweaks: prompt testing frameworks, version comparison, systematic refinement. Services named in guide: prompt testing frameworks, version comparison, systematic refinement.
- **Skill 5.2.4** [Paraphrase]: Troubleshoot retrieval system issues hurting FM augmentation effectiveness: response relevance analysis, embedding quality diagnostics, drift monitoring, vectorization issue resolution, chunking and preprocessing remediation, vector search performance optimization. Services named in guide: model response relevance analysis, embedding quality diagnostics, drift monitoring, vectorization issue resolution, chunking/preprocessing remediation, vector search performance optimization.
- **Skill 5.2.5** [Paraphrase]: Troubleshoot prompt maintenance issues to keep improving FM interaction performance: template testing, CloudWatch Logs for prompt-confusion diagnosis, X-Ray prompt observability pipelines, schema validation for format inconsistencies, systematic refinement workflows. Services named in guide: template testing, CloudWatch Logs, X-Ray, schema validation, systematic refinement workflows.

---

## In-scope service list (official PDF, pages 18-23)

(Identical to the list in exam-facts-v2.md. Listed here so lesson writers can check "is this service fair game" while building each lesson.)

Analytics: Amazon Athena, Amazon EMR, AWS Glue, Amazon Kinesis, Amazon OpenSearch Service, Amazon QuickSight, Amazon MSK. Application Integration: Amazon AppFlow, AWS AppConfig, Amazon EventBridge, Amazon SNS, Amazon SQS, AWS Step Functions. Compute: AWS App Runner, Amazon EC2, AWS Lambda, AWS Lambda@Edge, AWS Outposts, AWS Wavelength. Containers: Amazon ECR, Amazon ECS, Amazon EKS, AWS Fargate. Customer Engagement: Amazon Connect. Database: Amazon Aurora, Amazon DocumentDB, Amazon DynamoDB, DynamoDB Streams, Amazon ElastiCache, Amazon Neptune, Amazon RDS. Developer Tools: AWS Amplify, AWS CDK, AWS CLI, AWS CloudFormation, AWS CodeArtifact, AWS CodeBuild, AWS CodeDeploy, AWS CodePipeline, Kiro, AWS Tools and SDKs, AWS X-Ray. Machine Learning: Amazon Augmented AI, Amazon Bedrock, Amazon Bedrock AgentCore, Amazon Bedrock Knowledge Bases, Amazon Bedrock Prompt Management, Amazon Bedrock Prompt Flows, Amazon Comprehend, Amazon Kendra, Amazon Lex, Amazon Q Business, Amazon Q Business Apps, Amazon Q Developer, Amazon Quick, Amazon Rekognition, Amazon SageMaker AI, Amazon SageMaker Clarify, Amazon SageMaker Data Wrangler, Amazon SageMaker Ground Truth, Amazon SageMaker JumpStart, Amazon SageMaker Model Monitor, Amazon SageMaker Model Registry, Amazon SageMaker Neo, Amazon SageMaker Processing, Amazon SageMaker Unified Studio, Amazon Textract, Amazon Titan, Amazon Transcribe. Management and Governance: AWS Auto Scaling, AWS Chatbot, AWS CloudTrail, Amazon CloudWatch, Amazon CloudWatch Logs, Amazon CloudWatch Synthetics, AWS Cost Anomaly Detection, AWS Cost Explorer, Amazon Managed Grafana, AWS Service Catalog, AWS Systems Manager, AWS Well-Architected Tool. Migration and Transfer: AWS DataSync, AWS Transfer Family. Networking and Content Delivery: Amazon API Gateway, AWS AppSync, Amazon CloudFront, Elastic Load Balancing, AWS Global Accelerator, AWS PrivateLink, Amazon Route 53, Amazon VPC. Security, Identity, and Compliance: Amazon Cognito, AWS Encryption SDK, IAM, IAM Access Analyzer, IAM Identity Center, AWS KMS, Amazon Macie, AWS Secrets Manager, AWS WAF. Storage: Amazon EBS, Amazon EFS, Amazon S3, Amazon S3 Intelligent-Tiering, Amazon S3 Lifecycle policies, Amazon S3 Cross-Region Replication.

## Out-of-scope service list (official PDF, pages 23-29)

(Identical to the list in exam-facts-v2.md.)

Application Integration: Amazon MQ. Analytics: AWS Clean Rooms, AWS Data Exchange, Amazon DataZone, Amazon FinSpace. Blockchain: Amazon Managed Blockchain. Business Applications: Alexa for Business, Amazon Chime, AWS Wickr, Amazon WorkDocs, Amazon WorkMail. Cloud Financial Management: AWS Budgets, AWS Cost and Usage Report, Reserved Instance reports, AWS Savings Plans. Compute: AWS Batch, EC2 Image Builder, ECS Anywhere, EKS Anywhere, Elastic Beanstalk, Lightsail, Local Zones, Serverless Application Repository. Containers: App2Container, Copilot, ROSA. Customer Engagement: Amazon SES. Database: Keyspaces, QLDB, Redshift, Timestream. Developer Tools: Cloud9, CloudShell, CodeGuru, CodeStar, Corretto. End User Computing: AppStream 2.0, WorkLink, WorkSpaces, WorkSpaces Web. Frontend Web and Mobile: Device Farm, Location Service, Pinpoint. Game Development: GameLift, Lumberyard. IoT: AWS IoT 1-Click, IoT Analytics, IoT Button, IoT Core, IoT Device Defender, IoT Device Management, IoT Events, IoT FleetWise, IoT Greengrass, IoT SiteWise, IoT TwinMaker. Management and Governance: Console Mobile Application, Health Dashboard, License Manager, Proton, Trusted Advisor. ML: DeepComposer, DeepRacer, DevOps Guru, Forecast, Fraud Detector, HealthLake, Lookout for Equipment, Lookout for Metrics, Lookout for Vision, Monitron, Panorama. Media Services: Elastic Transcoder, Elemental MediaConnect, Elemental MediaConvert, Elemental MediaLive, Elemental MediaPackage, Elemental MediaStore, Elemental MediaTailor, Interactive Video Service, Kinesis Video Streams, Nimble Studio. Migration and Transfer: Application Discovery Service, Application Migration Service, CloudEndure Migration, Migration Hub, Snow Family. Networking: App Mesh, Cloud Map, Direct Connect, Private 5G, Transit Gateway, VPN. Quantum: Braket. Robotics: RoboMaker. Satellite: Ground Station.

## Technologies and concepts that might appear (official PDF, page 17)

RAG; vector databases and embeddings; prompt engineering and management; FM integration; agentic AI systems; Responsible AI practices; content safety and moderation; model evaluation and validation; cost optimization for AI workloads; performance tuning for AI applications; monitoring and observability for AI systems; security and governance for AI applications; API design and integration patterns; event-driven architectures; serverless computing; container orchestration; infrastructure as code (IaC); CI/CD for AI applications; hybrid cloud architectures; enterprise system integration.

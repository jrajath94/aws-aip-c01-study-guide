#!/usr/bin/env python3
"""
Master Enrichment Script for AIP-C01 Visual Course
Enriches all 95 slides with:
1. High-resolution architecture diagram / SVG asset paths
2. 5-Layer Russian Doll First-Principles Learning content:
   - Layer 1: First Principle Intuition
   - Layer 2: AWS Architecture Flow
   - Layer 3: Exact APIs, Parameters & Code
   - Layer 4: Amazon Traps & Limits
   - Layer 5: 2-Day Exam Decision Rule
3. Linked practice question IDs from the 250-question bank
"""

import json, os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 1. Slide to Diagram Image Mapping
IMAGE_MAP = {
    "core-001": "../assets/img/density/cc-prereq-map.svg",
    "core-002": "../assets/img/density/cc-numbers.svg",
    "core-003": "../assets/img/custom/pat-exam-surface.svg",
    "core-004": "../assets/img/custom/pat1-constraints.svg",
    "core-005": "../assets/img/v2/d1-tokens-1.png",
    "core-006": "../assets/img/v2/d2-deploy-ladder-1.png",
    "core-007": "../assets/img/v2/s8-method-1.png",
    "core-008": "../assets/img/foundations/found-genai-arch.svg",
    "core-009": "../assets/img/v2/d1-model-switch-1.png",
    "core-010": "../assets/img/custom/sd-55-authtrio.svg",
    "core-011": "../assets/img/v2/s8-api-1.png",
    "core-012": "../assets/img/density/cc-converse-shape.svg",
    "core-013": "../assets/img/custom/bank-14-inference.svg",
    "core-014": "../assets/img/v2/d1-prompt-gov-1.png",
    "core-015": "../assets/img/density/cc-xregion.svg",
    "core-016": "../assets/img/custom/bank-42-loravsfull.svg",
    "core-017": "../assets/img/v2/s8-ladder-1.png",
    "core-018": "../assets/img/v2/d1-data-pipeline-1.png",
    "core-019": "../assets/img/density/cc-bda-flow.svg",
    "core-020": "../assets/img/v2/ad-rag-layers-1.png",
    "core-021": "../assets/img/custom/sd-35-vectorstores.svg",
    "core-022": "../assets/img/custom/sd-36-retrieval.svg",
    "core-023": "../assets/img/density/cc-vector-decision.svg",
    "core-024": "../assets/img/custom/sd-32-sync.svg",
    "core-025": "../assets/img/v2/d1-chunking-1.png",
    "core-026": "../assets/img/custom/sd-34-embeddings.svg",
    "core-027": "../assets/img/density/cc-rerank-before-after.svg",
    "core-028": "../assets/img/v2/s8-retrieval-1.png",
    "core-029": "../assets/img/v2/s8-rag-call-1.png",
    "core-030": "../assets/img/custom/bank-13-prompting.svg",
    "core-031": "../assets/img/custom/sd-52-session.svg",
    "core-032": "../assets/img/density/cc-prompt-lifecycle.svg",
    "core-033": "../assets/img/density/cc-flows.svg",
    "core-034": "../assets/img/v2/d2-agent-loop-1.png",
    "core-035": "../assets/img/density/cc-strands-loop.svg",
    "core-036": "../assets/img/v2/s8-loop-gate-1.png",
    "core-037": "../assets/img/custom/sd-47-multiagent.svg",
    "core-038": "../assets/img/custom/sd-45-tasktoken.svg",
    "core-039": "../assets/img/custom/bank-22-actions.svg",
    "core-040": "../assets/img/v2/d2-mcp-1.png",
    "core-041": "../assets/img/density/cc-agentcore.svg",
    "core-042": "../assets/img/v2/d2-deploy-ladder-1.png",
    "core-043": "../assets/img/foundations/found-instance-types.svg",
    "core-044": "../assets/img/density/cc-model-funnel.svg",
    "core-045": "../assets/img/foundations/found-messaging.svg",
    "core-046": "../assets/img/foundations/found-sso-vs-roles.svg",
    "core-047": "../assets/img/foundations/found-regions.svg",
    "core-048": "../assets/img/v2/d2-gateway-1.png",
    "core-049": "../assets/img/mermaid/03-sync-async-decision.svg",
    "core-050": "../assets/img/custom/sd-53-streaming.svg",
    "core-051": "../assets/img/density/d2-retry-backoff.svg",
    "core-052": "../assets/img/custom/pat5-ladder.svg",
    "core-053": "../assets/img/foundations/found-api-gateway.svg",
    "core-054": "../assets/img/custom/sd-46-agentdebug.svg",
    "core-055": "../assets/img/v2/d3-injection-1.png",
    "core-056": "../assets/img/v2/d3-guardrail-1.png",
    "core-057": "../assets/img/v2/d3-detect-block-1.png",
    "core-058": "../assets/img/density/d3-grounding-example.svg",
    "core-059": "../assets/img/density/cc-reasoning-tradeoff.svg",
    "core-060": "../assets/img/v2/d3-vpc-endpoint-1.png",
    "core-061": "../assets/img/v2/d3-envelope-1.png",
    "core-062": "../assets/img/v2/d3-macie-1.png",
    "core-063": "../assets/img/density/cc-privacy.svg",
    "core-064": "../assets/img/density/d3-model-card.svg",
    "core-065": "../assets/img/custom/bank-31-controls.svg",
    "core-066": "../assets/img/density/d3-safety-eval.svg",
    "core-067": "../assets/img/custom/bank-34-responsible.svg",
    "core-068": "../assets/img/v2/d1-context-budget-1.png",
    "core-069": "../assets/img/v2/d4-cost-per-success-1.png",
    "core-070": "../assets/img/v2/d4-prompt-cache-1.png",
    "core-071": "../assets/img/v2/ad-cache-key-1.png",
    "core-072": "../assets/img/v2/d2-break-even-1.svg",
    "core-073": "../assets/img/v2/d4-latency-tail-1.png",
    "core-074": "../assets/img/density/cc-rag-stages.svg",
    "core-075": "../assets/img/v2/d4-observability-1.png",
    "core-076": "../assets/img/density/cc-three-logs.svg",
    "core-077": "../assets/img/v2/d4-agent-trace-1.png",
    "core-078": "../assets/img/v2/d5-troubleshoot-1.png",
    "core-079": "../assets/img/custom/d5-eval-matrix.svg",
    "core-080": "../assets/img/custom/bank-51-evalmethods.svg",
    "core-081": "../assets/img/v2/d5-judge-bias-1.png",
    "core-082": "../assets/img/v2/d5-ndcg-1.png",
    "core-083": "../assets/img/custom/sd-72-metrics.svg",
    "core-084": "../assets/img/mls2/mls2-groundtruth.svg",
    "core-085": "../assets/img/v2/d5-holdout-leak-1.png",
    "core-086": "../assets/img/custom/bank-16-costlatency.svg",
    "core-087": "../assets/img/v2/ad-path-exec-1.png",
    "core-088": "../assets/img/density/cc-eval-harness.svg",
    "core-089": "../assets/img/density/d1-retrieval-debug.svg",
    "core-090": "../assets/img/density/d2-retry-backoff.svg",
    "core-091": "../assets/img/custom/d5-trap-traditional-fix.svg",
    "core-092": "../assets/img/density/cc-chunking-before-after.svg",
    "core-093": "../assets/img/v2/d1-rag-1.png",
    "core-094": "../assets/img/v2/d2-agent-loop-1.png",
    "core-095": "../assets/img/density/cc-numbers.svg",
}

# 2. Comprehensive Russian Doll Knowledge Base for All 95 Slides
def get_russian_doll(sid, title, domain):
    # Specialized deep dives based on slide ID and topic
    d = {}
    
    if sid == "core-001":
        d["intuition"] = "AIP-C01 is a professional scenario exam testing whether you can build, secure, scale, and evaluate production GenAI systems on AWS, not just invoke an API."
        d["architecture"] = "End-to-end GenAI architecture: Client -> API Gateway/CloudFront -> GenAI Gateway/Lambda -> Amazon Bedrock (Models, Knowledge Bases, Agents, Guardrails) + Vector Storage (OpenSearch/Aurora) + KMS + CloudWatch/CloudTrail."
        d["api"] = "Focus on AWS SDK (boto3: bedrock, bedrock-runtime, bedrock-agent, bedrock-agent-runtime) and AWS CLI bedrock commands."
        d["traps"] = "Trap: Thinking AIP-C01 is conversational trivia. It is a 180-minute scenario test with 75 multi-step questions requiring rigorous trade-off decisions."
        d["examRule"] = "Exam Rule: Always choose the solution that satisfies ALL stated constraints (security, latency, cost, residency), not just the newest feature."

    elif sid == "core-002":
        d["intuition"] = "The exam scoring follows a scaled 100-1000 model with 750 to pass. 65 questions are scored and 10 unscored questions are evaluated for future exams."
        d["architecture"] = "Compensatory scoring engine: Strong performance in Domain 1 (31%) or Domain 2 (26%) can compensate for minor deficits in smaller domains, but broad coverage is vital."
        d["api"] = "Key numbers: 75 total questions, 180 minutes (~2.4 minutes/question), 750 passing score, $300 fee."
        d["traps"] = "Trap: Leaving questions blank. There is NO penalty for guessing on AWS exams; always select an answer."
        d["examRule"] = "Exam Rule: Multiple-response questions state exactly how many options to pick ('Select TWO' or 'Select THREE'). Partial credit is NOT given."

    elif sid == "core-003":
        d["intuition"] = "A 2-day study horizon requires prioritized high-yield domain coverage: 77% of the exam lies in Domains 1, 2, and 3."
        d["architecture"] = "Day 1: Foundation Models, RAG, Prompt Engineering, Agentic AI. Day 2: Security, Governance, Optimization, Evaluation, and Timed 75-Question Mock."
        d["api"] = "Domain 1: 31%, Domain 2: 26%, Domain 3: 20%, Domain 4: 12%, Domain 5: 11%."
        d["traps"] = "Trap: Spending 80% of your time on basic ML concepts like neural networks. Traditional ML development is out of scope."
        d["examRule"] = "Exam Rule: Prioritize Bedrock Knowledge Bases, Bedrock Agents, Bedrock Guardrails, and Cross-Region Inference."

    elif sid == "core-004":
        d["intuition"] = "Every question stem describes a specific enterprise persona, problem, and 2-4 hard constraints (budget, latency, security, regulatory)."
        d["architecture"] = "Filter funnel: Eliminate options that violate hard constraints (e.g. data residency, VPC isolation) -> Compare remaining options on the primary objective ('most cost-effective', 'least operational overhead')."
        d["api"] = "Look for trigger phrases: 'least operational overhead' -> Managed Bedrock vs self-hosted EC2/EKS; 'lowest latency' -> Provisioned Throughput or Prompt Caching."
        d["traps"] = "Trap: Selecting an architecturally valid option that violates a secondary constraint (e.g. sending data to another Region when residency in eu-central-1 is required)."
        d["examRule"] = "Exam Rule: The 'best' architecture on paper is wrong if it violates a stated operational or budget limit."

    elif sid == "core-005":
        d["intuition"] = "Tokens are numerical representations of sub-word fragments (~0.75 words/token in English). Context window is a hard physical memory boundary."
        d["architecture"] = "Total Context Budget = System Instructions + History/Conversation + Retrieved RAG Passages + Tool Definitions + Reserved Max Output Tokens."
        d["api"] = "bedrock_runtime.converse(..., inferenceConfig={'maxTokens': 2048, 'temperature': 0.1}). Check response['stopReason'] ('end_turn' vs 'max_tokens')."
        d["traps"] = "Trap: Confusing maxTokens with input limit. maxTokens only limits the *generated output tokens*, not the input prompt length."
        d["examRule"] = "Exam Rule: If a response is truncated mid-sentence or mid-JSON, check if stopReason == 'max_tokens' and increase maxTokens or prompt reserve."

    elif sid == "core-006":
        d["intuition"] = "The Solution Ladder: Start with Prompt Engineering -> RAG (dynamic facts) -> Fine-Tuning (style/format) -> Pre-training (new language/domain from scratch)."
        d["architecture"] = "Prompt Eng (zero/few-shot) requires no training; RAG grounds models with dynamic external data; Fine-tuning adjusts weights with labeled pairs; Continued Pre-training adds unlabeled domain corpus."
        d["api"] = "boto3.client('bedrock').create_model_customization_job(customizationType='FINE_TUNING'|'CONTINUED_PRE_TRAINING')."
        d["traps"] = "Trap: Choosing Fine-Tuning when data changes frequently. Fine-tuning freezes knowledge at training time; only RAG handles continuously updating facts!"
        d["examRule"] = "Exam Rule: Dynamic changing knowledge -> RAG. Specialized tone, acronyms, or rigid formatting -> Fine-tuning (LoRA)."

    elif sid == "core-007":
        d["intuition"] = "A proof of concept must be grounded in measurable acceptance criteria on representative domain data, not cherry-picked examples."
        d["architecture"] = "PoC Pipeline: Representative test set -> Baseline prompt -> Evaluator (Automated metrics + LLM-as-a-judge) -> Iterative enhancement (Few-shot -> RAG -> Tools)."
        d["api"] = "Amazon Bedrock Model Evaluation API: create_evaluation_job(evaluationJobName=..., roleArn=..., datasetMetricConfigs=...)."
        d["traps"] = "Trap: Purchasing Provisioned Throughput during PoC stage. Use on-demand serverless inference until traffic patterns and throughput are proven."
        d["examRule"] = "Exam Rule: During exploration and PoC, always start with On-Demand serverless inference and prompt iteration."

    elif sid == "core-008":
        d["intuition"] = "The AWS Well-Architected Framework Generative AI Lens defines 6 pillars tailored for LLM applications: Operational Excellence, Security, Reliability, Performance, Cost, Sustainability."
        d["architecture"] = "Layered Architecture: Experience Layer -> Generative AI Gateway (API Gateway + WAF) -> Foundation Models / Orchestration Layer -> Data & Retrieval Layer -> Storage & Observability."
        d["api"] = "Key controls: Bedrock Guardrails for safety, AWS KMS for CMK encryption, Amazon CloudWatch for invocations, AWS CloudTrail for audit."
        d["traps"] = "Trap: Directly exposing Bedrock API keys or SDK to client browsers. Always mediate access through a secure API Gateway and Lambda backend."
        d["examRule"] = "Exam Rule: Enterprise GenAI applications must enforce security and authorization at the backend gateway, never inside client prompt text."

    elif sid == "core-009":
        d["intuition"] = "Model selection balances task complexity, modality, context window size, latency (TTFT), and cost per 1,000 tokens."
        d["architecture"] = "Model Spectrum: Lightweight fast models (Claude Haiku, Amazon Titan Text Lite) for classification/routing -> Heavy frontier models (Claude Opus/Sonnet) for complex reasoning and code."
        d["api"] = "List available models: bedrock.list_foundation_models(byInferenceType='ON_DEMAND', byOutputModality='TEXT')."
        d["traps"] = "Trap: Selecting the largest model by default. Smaller models with RAG or structured prompts often match accuracy at 10x lower cost and latency."
        d["examRule"] = "Exam Rule: Model selection criteria order: Task requirement & Modality -> Quality threshold -> Latency (TTFT) -> Cost per token."

    elif sid == "core-010":
        d["intuition"] = "Accessing models requires two independent gates: 1) Activating model access in the Amazon Bedrock console, and 2) IAM permissions on the model ARN."
        d["architecture"] = "Identity (IAM User/Role) -> IAM Policy allowing bedrock:InvokeModel on arn:aws:bedrock:region::foundation-model/model-id -> Bedrock Model Access enabled in Region."
        d["api"] = "IAM Action: 'bedrock:InvokeModel', 'bedrock:InvokeModelWithResponseStream', Resource: 'arn:aws:bedrock:*::foundation-model/*'."
        d["traps"] = "Trap: Having full AdministratorAccess in IAM but receiving AccessDeniedException. If the model access is not activated in the Bedrock console, calls fail!"
        d["examRule"] = "Exam Rule: An AccessDenied error when invoking Bedrock can mean EITHER missing IAM permissions OR model access not granted in Bedrock console/Marketplace."

    elif sid == "core-011":
        d["intuition"] = "Converse API provides a unified, standardized interface across all Bedrock foundation models, eliminating provider-specific JSON schemas."
        d["architecture"] = "Client -> bedrock-runtime.converse() -> Unified Messages Schema (system, user, assistant, toolUse, toolResult) -> Bedrock maps to Anthropic, Meta, Mistral, or Amazon schemas."
        d["api"] = "bedrock_runtime.converse(modelId='anthropic.claude-3-5-sonnet-...', messages=[{'role': 'user', 'content': [{'text': 'Hello'}]}], inferenceConfig={'temperature': 0.5})."
        d["traps"] = "Trap: Using InvokeModel with Claude-specific schema (`prompt: '\n\nHuman: ...'`) when building multi-model architectures. Use Converse API for multi-model interoperability."
        d["examRule"] = "Exam Rule: When an application needs to switch foundation models easily without code rewrites, choose the Bedrock Converse API."

    elif sid == "core-012":
        d["intuition"] = "Strict JSON validation and structured output guarantee downstream integration safety; LLM output must be treated as untrusted user input."
        d["architecture"] = "Request -> Converse API with toolConfig / outputConfig -> Model generates structured JSON arguments -> Application validates schema (e.g. Pydantic) -> Business Logic."
        d["api"] = "converse(..., toolConfig={'tools': [{'toolSpec': {'name': 'lookup', 'inputSchema': {'json': schema}}}]}). Check contentBlock['toolUse']."
        d["traps"] = "Trap: Trusting model-generated JSON to directly execute SQL or shell commands. Always validate permissions and parameters server-side before execution."
        d["examRule"] = "Exam Rule: Tool use / function calling via Converse API toolConfig is the recommended way to extract reliable structured JSON."

    elif sid == "core-013":
        d["intuition"] = "Temperature and Top-P govern the randomness and sampling distribution of output tokens; they do NOT correct factual hallucinations."
        d["architecture"] = "Logits -> Softmax with Temperature (T -> 0: greedy argmax, deterministic; T -> 1: creative) -> Top-P Nucleus Sampling (sums top probabilities up to P) -> Top-K (top K tokens)."
        d["api"] = "inferenceConfig={'temperature': 0.0, 'topP': 0.9, 'maxTokens': 1024}. Note: When temperature is 0, topP is usually ignored."
        d["traps"] = "Trap: Setting temperature=0 to prevent hallucinations. Temperature=0 makes token selection deterministic, but the model can still generate false statements deterministically!"
        d["examRule"] = "Exam Rule: For factual, extraction, and code tasks, use temperature 0.0 to 0.2. For creative drafting, use 0.7 to 1.0. To fix factual errors, use RAG or Guardrails, not temperature."

    elif sid == "core-014":
        d["intuition"] = "Decoupling model selection, prompt templates, and guardrail settings from application code enables zero-downtime updates and rapid rollbacks."
        d["architecture"] = "AWS AppConfig or Amazon Bedrock Prompt Management -> Lambda / Microservice fetches latest active version -> Invokes Bedrock without application redeployment."
        d["api"] = "bedrock_agent.get_prompt(promptIdentifier='prompt-id', promptVersion='1'). AWS AppConfig GetLatestConfiguration."
        d["traps"] = "Trap: Hardcoding model IDs and prompt strings directly inside application source code, requiring full CI/CD deployment to change a prompt."
        d["examRule"] = "Exam Rule: Use Amazon Bedrock Prompt Management or AWS AppConfig to manage prompts and model configurations dynamically without application deployments."

    elif sid == "core-015":
        d["intuition"] = "Cross-Region Inference automatically distributes inference requests across multiple AWS Regions to achieve higher throughput and avoid ThrottlingException."
        d["architecture"] = "Application -> Bedrock System-Defined Inference Profile (e.g. us.anthropic.claude-3-5-sonnet) -> Bedrock routes traffic across us-east-1, us-west-2, us-east-2 dynamically."
        d["api"] = "bedrock_runtime.converse(modelId='us.anthropic.claude-3-5-sonnet-20240620-v1:0', ...). Prefix 'us.', 'eu.', or 'apac.' defines geographical boundaries."
        d["traps"] = "Trap: Believing cross-region inference violates data residency. Geographical profiles (e.g. eu.anthropic...) only route within European Regions (eu-central-1, eu-west-1, etc.)."
        d["examRule"] = "Exam Rule: To mitigate regional capacity constraints and eliminate 429 ThrottlingException spikes at no extra cost, use Bedrock Cross-Region Inference Profiles."

    elif sid == "core-016":
        d["intuition"] = "Model customization alters model weights via Fine-Tuning (labeled prompt-response pairs) or Continued Pre-Training (unlabeled domain text)."
        d["architecture"] = "Labeled Dataset in S3 (JSONL: {\"prompt\": \"...\", \"completion\": \"...\"}) -> Bedrock Fine-Tuning Job -> Custom Model -> Provisioned Throughput required for deployment."
        d["api"] = "bedrock.create_model_customization_job(jobName='ft-job', customModelName='domain-v1', baseModelIdentifier='...', trainingDataConfig={'s3Uri': 's3://.../train.jsonl'})."
        d["traps"] = "Trap: Forgetting that custom Bedrock models CANNOT be invoked via on-demand pricing! You MUST purchase Provisioned Throughput (at least 1 Model Unit) to serve custom models."
        d["examRule"] = "Exam Rule: Custom models in Bedrock require Provisioned Throughput to serve. Always check if RAG or few-shot prompting can solve the task before fine-tuning."

    elif sid == "core-017":
        d["intuition"] = "Customized models must follow rigorous MLOps lifecycles: data versioning, validation split, evaluation benchmarks, canary deployment, and rollback strategy."
        d["architecture"] = "S3 (versioned training data) -> Bedrock Customization Job -> SageMaker Model Registry / Bedrock Custom Model -> A/B Testing / Canary -> Production Provisioned Throughput."
        d["api"] = "Amazon Bedrock: list_custom_models(), get_custom_model(). AWS KMS key policy must grant Bedrock service principal access to training data."
        d["traps"] = "Trap: Training without a validation dataset. Without a holdout evaluation dataset, you cannot detect catastrophic forgetting or overfitting."
        d["examRule"] = "Exam Rule: Custom model training requires S3 bucket permissions and an IAM service role trusted by bedrock.amazonaws.com with kms:Decrypt permissions."

    elif sid == "core-018":
        d["intuition"] = "Garbage in, garbage out: RAG retrieval quality is bounded by document cleansing, deduplication, formatting, and structural integrity."
        d["architecture"] = "Raw Documents -> AWS Glue / SageMaker Processing (clean HTML, deduplicate, normalize whitespace, extract metadata) -> S3 -> Knowledge Base Sync."
        d["api"] = "AWS Glue Data Quality rulesets, Amazon Comprehend for language and PII pre-screening."
        d["traps"] = "Trap: Ingesting raw PDFs with scanned images or unparsed tables directly into naive text chunkers. Tables lose row-column structure unless parsed properly."
        d["examRule"] = "Exam Rule: High-accuracy enterprise RAG requires clean source data preparation and metadata enrichment before vector ingestion."

    elif sid == "core-019":
        d["intuition"] = "Multimodal RAG extracts and unifies information across text, tables, charts, images, and audio into rich embeddings or structured representations."
        d["architecture"] = "Multimodal Documents -> Amazon Bedrock Data Automation (BDA) or Amazon Textract (AnalyzeDocument with TABLES/FORMS) -> Text + Layout -> Titan Multimodal Embeddings."
        d["api"] = "textract.analyze_document(FeatureTypes=['TABLES', 'FORMS']). bedrock-runtime.invoke_model(modelId='amazon.titan-embed-image-v1')."
        d["traps"] = "Trap: Using standard OCR for complex tabular data. Standard OCR turns tables into flat strings where column alignment is destroyed. Use Textract Tables feature."
        d["examRule"] = "Exam Rule: For document workflows with financial tables, invoices, and forms, use Amazon Textract or Amazon Bedrock Data Automation."

    elif sid == "core-020":
        d["intuition"] = "Vector embeddings map semantic meaning into high-dimensional geometric space; cosine similarity measures directional alignment between query and chunks."
        d["architecture"] = "Document Chunks -> Embedding Model (e.g. Titan Text Embeddings v2) -> 1024-dim Vector -> Vector Index (HNSW or IVF) -> Query Vector -> Top-K Nearest Neighbors."
        d["api"] = "Similarity Metrics: Cosine Similarity (direction-only), Dot Product (requires normalized vectors), Euclidean Distance (L2 norm)."
        d["traps"] = "Trap: Switching embedding models without re-embedding the entire vector database! Vectors from Model A are completely incompatible with Model B."
        d["examRule"] = "Exam Rule: If you change the embedding model, you MUST re-index and re-embed all documents in the vector store from scratch."

    elif sid == "core-021":
        d["intuition"] = "Choose vector stores based on operational overhead, scale, hybrid search support, and existing AWS infrastructure footprint."
        d["architecture"] = "Managed Bedrock Knowledge Base vector options: 1) Amazon OpenSearch Serverless (AOSS) - default serverless vector search, 2) Amazon Aurora PostgreSQL with pgvector, 3) Pinecone, 4) Amazon Neptune Analytics (graph + vector)."
        d["api"] = "Knowledge Base storage configuration: storageConfiguration={'type': 'OPENSEARCH_SERVERLESS' | 'RDS' | 'PINECONE' | 'NEPTUNE'}."
        d["traps"] = "Trap: Choosing Amazon DynamoDB as a vector store. DynamoDB does NOT natively support vector indexing or similarity search without custom external search engines."
        d["examRule"] = "Exam Rule: Default managed vector store for Bedrock Knowledge Bases is OpenSearch Serverless (AOSS). If existing relational workloads exist, use Aurora PostgreSQL pgvector."

    elif sid == "core-022":
        d["intuition"] = "Metadata filtering enforces multi-tenant security and pre-filters search spaces by tenant ID, department, date, or document classification."
        d["architecture"] = "Query + User Context (tenant_id='corp-a', role='hr') -> Bedrock Retrieve API with filter -> Vector Store executes pre-filter (metadata match) THEN vector search -> Authorized chunks."
        d["api"] = "bedrock_agent_runtime.retrieve(knowledgeBaseId=..., retrievalQuery={'text': '...'}, retrievalConfiguration={'vectorSearchConfiguration': {'filter': {'equals': {'key': 'tenantId', 'value': 'tenant-123'}}}})."
        d["traps"] = "Trap: Attempting to enforce multi-tenant isolation via prompt instructions ('Only answer from tenant A'). Prompts can be bypassed via injection; use metadata filters!"
        d["examRule"] = "Exam Rule: Multi-tenant document isolation and access control MUST be enforced via Vector Store Metadata Filters in the retrieval query, not prompt instructions."

    elif sid == "core-023":
        d["intuition"] = "Scaling vector databases requires balancing indexing throughput, query latency, OpenSearch Compute Units (OCUs), and memory footprint."
        d["architecture"] = "OpenSearch Serverless automatically scales indexing OCUs and search OCUs independently based on workload demand; requires minimum 2 search OCUs and 2 indexing OCUs."
        d["api"] = "AOSS capacity limits: OpenSearch Serverless minimum baseline is 4 OCUs (2 search + 2 indexing for HA). Maximum limit can be configured via Account quotas."
        d["traps"] = "Trap: Expecting zero cost when an OpenSearch Serverless collection is idle. AOSS maintains a minimum OCU baseline for high availability."
        d["examRule"] = "Exam Rule: OpenSearch Serverless automatically scales compute units (OCUs) for search and ingestion independently, with built-in AZ redundancy."

    elif sid == "core-024":
        d["intuition"] = "Synchronizing Knowledge Bases detects new, updated, and deleted source files in S3 and reconciles vector index embeddings incrementally."
        d["architecture"] = "S3 Bucket (DataSource) -> StartIngestionJob -> Bedrock reads S3 changes -> Chunks & embeds new/updated files -> Deletes obsolete vectors from vector store -> Ingestion complete."
        d["api"] = "bedrock_agent.start_ingestion_job(knowledgeBaseId='kb-id', dataSourceId='ds-id'). Status: STARTING -> IN_PROGRESS -> COMPLETE / FAILED."
        d["traps"] = "Trap: Editing a file in S3 and expecting the Knowledge Base to answer with new data immediately. You MUST trigger an Ingestion Job to synchronize changes!"
        d["examRule"] = "Exam Rule: Updates or deletions in S3 do not take effect in Bedrock Knowledge Bases until a DataSource Ingestion Job is executed."

    elif sid == "core-025":
        d["intuition"] = "Chunking determines retrieval granularity: small chunks preserve specific facts, while large chunks provide broad narrative context."
        d["architecture"] = "Chunking Strategies in Bedrock: 1) Default/Fixed (300 tokens, 20% overlap), 2) Hierarchical (Parent-Child: searches small child chunks, returns larger parent chunk to model), 3) Semantic (splits on embedding similarity shifts)."
        d["api"] = "Knowledge Base chunking configuration: chunkingStrategy='FIXED_SIZE' | 'HIERARCHICAL' | 'SEMANTIC' | 'NONE'."
        d["traps"] = "Trap: Using fixed-size chunking for complex legal/technical contracts where context spans multiple paragraphs. Use Hierarchical Chunking (Parent-Child)!"
        d["examRule"] = "Exam Rule: When retrieval requires pinpoint precision but the LLM needs wide surrounding context to answer accurately, choose Hierarchical (Parent-Child) Chunking."

    elif sid == "core-026":
        d["intuition"] = "Embedding models convert text into dense semantic vectors; dimension size (e.g. 1024 vs 512 vs 256) trades off memory storage for fine-grained accuracy."
        d["architecture"] = "Titan Embeddings Text v2 supports flexible output dimensions: 1024, 512, or 256 dimensions with normalized vector output."
        d["api"] = "invoke_model(modelId='amazon.titan-embed-text-v2:0', body=json.dumps({'inputText': '...', 'dimensions': 512, 'normalize': True}))."
        d["traps"] = "Trap: Comparing cosine similarity scores across different embedding models. Embeddings are relative to their own training vector space."
        d["examRule"] = "Exam Rule: Amazon Titan Text Embeddings v2 supports reduced dimensions (512 or 256) to lower vector store storage costs by up to 75% with minimal accuracy loss."

    elif sid == "core-027":
        d["intuition"] = "Hybrid search merges Lexical Search (BM25 keyword match for exact IDs/acronyms) and Semantic Vector Search, followed by Re-ranking."
        d["architecture"] = "User Query -> Parallel Search: [BM25 Keyword Search] + [Dense Vector Search] -> Reciprocal Rank Fusion (RRF) -> Cohere Rerank model -> Top-K re-ranked passages."
        d["api"] = "Bedrock Knowledge Base retrievalConfiguration: vectorSearchConfiguration={'overrideSearchType': 'HYBRID'} + rerankingConfiguration={'type': 'BEDROCK_RERANKING_MODEL'}."
        d["traps"] = "Trap: Relying purely on semantic vector search for queries containing part numbers, serial codes, or error codes. Pure vector search often fails exact string matching!"
        d["examRule"] = "Exam Rule: For technical documentation with part numbers, error codes, and exact acronyms, always choose HYBRID search (lexical + semantic) with re-ranking."

    elif sid == "core-028":
        d["intuition"] = "Raw user queries are often ambiguous, multi-part, or referential; query transformation rewrites, decomposes, or expands queries before retrieval."
        d["architecture"] = "Conversational Query ('How do I fix the error mentioned above?') -> Bedrock Knowledge Base Query Reformulation (LLM rewrites query using conversation history) -> Standalone search query."
        d["api"] = "Bedrock Knowledge Base automatically performs query reformulation in RetrieveAndGenerate multi-turn sessions."
        d["traps"] = "Trap: Passing raw multi-turn follow-up queries ('what about for Mac?') directly to the vector store. Without reformulation, the vector search lacks the core entity context!"
        d["examRule"] = "Exam Rule: Use Query Reformulation / Query Decomposition when handling multi-turn conversational RAG or complex compound queries."

    elif sid == "core-029":
        d["intuition"] = "Bedrock provides two primary RAG APIs: Retrieve (returns raw chunks only) vs RetrieveAndGenerate (handles retrieval + model synthesis end-to-end)."
        d["architecture"] = "Retrieve: Query -> Knowledge Base -> Chunks + Citations (Client calls LLM). RetrieveAndGenerate: Query -> Knowledge Base -> Bedrock FM -> Final Grounded Answer + Citations."
        d["api"] = "bedrock-agent-runtime.retrieve(knowledgeBaseId=..., retrievalQuery=...) vs bedrock-agent-runtime.retrieve_and_generate(input={'text': '...'}, retrieveAndGenerateConfiguration=...)."
        d["traps"] = "Trap: Calling RetrieveAndGenerate when your application requires a custom prompt template or a self-hosted model. Use Retrieve API if you need full control over the generation prompt!"
        d["examRule"] = "Exam Rule: Choose Retrieve if you need raw passages, custom prompt templates, or client-side control. Choose RetrieveAndGenerate for fully managed RAG with automatic citations."

    elif sid == "core-030":
        d["intuition"] = "Prompt engineering structures instructions, roles, context, constraints, and few-shot examples using clear XML delimiters to prevent instruction leakage."
        d["architecture"] = "Prompt Structure: System Role -> Task Instructions -> XML Tagged Context (<context>...</context>) -> Few-Shot Examples (<example>...</example>) -> User Input -> Output Format Indicator."
        d["api"] = "Converse API: pass system instructions in `system=[{'text': '...'}]`, user messages in `messages=[{'role': 'user', 'content': [{'text': '...'}]}]`."
        d["traps"] = "Trap: Concatenating untrusted user input directly into system instructions without XML tags. Delimit untrusted input with tags like `<user_query>` to prevent jailbreak override."
        d["examRule"] = "Exam Rule: Anthropic Claude and modern models on Bedrock perform best with clear XML tags (`<context>`, `<rules>`, `<instructions>`) delineating prompt sections."

    elif sid == "core-031":
        d["intuition"] = "Multi-turn chatbots require managing conversational history within context token limits, pruning or summarizing older turns to prevent context exhaustion."
        d["architecture"] = "Session Memory Strategies: 1) Full history (grows tokens linearly), 2) Sliding window (keeps last N turns), 3) Summary memory (LLM compresses past turns into a rolling summary)."
        d["api"] = "Amazon DynamoDB stores conversation history by `session_id`; Bedrock Agent manages session state automatically via `sessionId` parameter."
        d["traps"] = "Trap: Passing unbounded conversation history into every request. Eventually the request exceeds the model's max context length (ValidationException)."
        d["examRule"] = "Exam Rule: Store multi-turn conversation history in Amazon DynamoDB; apply sliding window or rolling summarization to bound context token consumption."

    elif sid == "core-032":
        d["intuition"] = "Amazon Bedrock Prompt Management provides versioned, testable, and reusable prompt assets with dynamic template variables."
        d["architecture"] = "Bedrock Prompt Management: Prompt Resource -> DRAFT version (editable) -> Created Versions (immutable, e.g. 1, 2, 3) -> Dynamic variables defined via `{{variable_name}}`."
        d["api"] = "bedrock-agent.create_prompt(name='CustomerSupport', variants=[{'name': 'v1', 'modelId': '...', 'templateType': 'TEXT', 'templateConfiguration': {'text': {'text': 'Hello {{user}}'}}}])"
        d["traps"] = "Trap: Pointing production applications to the 'DRAFT' version of a prompt. DRAFT versions can be modified at any time; production should ALWAYS reference numbered immutable versions!"
        d["examRule"] = "Exam Rule: Production workloads using Bedrock Prompt Management must target immutable numbered versions (e.g. version '2'), never the mutable DRAFT."

    elif sid == "core-033":
        d["intuition"] = "Amazon Bedrock Flows visually orchestrates complex multi-step generative AI workflows with branching logic, parallel execution, and data transformation."
        d["architecture"] = "Flow Nodes: Input Node -> Prompt Node (invokes FM) -> Condition Node (branching if/else) -> Knowledge Base Node (retrieval) -> Lambda Node -> Output Node."
        d["api"] = "bedrock-agent.create_flow(), prepare_flow(), invoke_flow(). Flows emit events over an SSE response stream."
        d["traps"] = "Trap: Building custom Lambda state machines for simple sequential prompt chains. Bedrock Flows provides managed visual prompt chaining without infrastructure."
        d["examRule"] = "Exam Rule: Use Amazon Bedrock Flows to visually design, test, and run multi-step prompt workflows with conditional branching and knowledge base lookups."

    elif sid == "core-034":
        d["intuition"] = "Agents use the ReAct (Reasoning + Acting) loop: the foundation model analyzes the goal, determines if a tool/retrieval is needed, observes the result, and iterates until done."
        d["architecture"] = "User Query -> Agent Orchestrator -> FM Thought ('I need to check account balance') -> Action Group (invokes Lambda) -> Observation ('Balance: $400') -> FM Answer."
        d["api"] = "bedrock-agent.create_agent(agentName=..., foundationModel=..., instruction=...). Invoke: bedrock-agent-runtime.invoke_agent(agentId=..., agentAliasId=..., sessionId=...)."
        d["traps"] = "Trap: Modifying an agent configuration and testing immediately without calling `prepare_agent`. Changes DO NOT take effect until the agent is prepared!"
        d["examRule"] = "Exam Rule: After creating or editing a Bedrock Agent, you MUST call `PrepareAgent` (or click Prepare in console) before invocations will reflect the changes."

    elif sid == "core-035":
        d["intuition"] = "Agents can be built using Amazon Bedrock managed agents or open-source multi-agent frameworks (e.g. LangGraph, CrewAI, Autogen) hosted on AWS."
        d["architecture"] = "Fully Managed: Amazon Bedrock Agents (serverless, native integration with OpenAPI and Lambda). Custom Code: EKS/ECS hosting containerized multi-agent state machines."
        d["api"] = "Bedrock Agent Components: Foundation Model + Instructions + Action Groups + Knowledge Bases + Guardrails + Memory (session state)."
        d["traps"] = "Trap: Re-inventing tool calling, session memory, and RAG orchestration from scratch on EC2 when a fully managed serverless agent is requested."
        d["examRule"] = "Exam Rule: When the requirement specifies 'least operational effort' for an interactive agent with tools and knowledge bases, choose Amazon Bedrock Agents."

    elif sid == "core-036":
        d["intuition"] = "Autonomous agents risk infinite loops, run-away API costs, and tool thrashing; execution must be strictly bounded with loop limits and timeouts."
        d["architecture"] = "Agent Guardrails: Maximum iteration count (e.g. max 5 steps) + Global execution timeout + Idempotency keys on write tools + Circuit breaker on tool errors."
        d["api"] = "Bedrock Agent sessionState: pass sessionAttributes and promptSessionAttributes to control execution limits and propagate context across turns."
        d["traps"] = "Trap: Allowing an agent to retry failing tool calls indefinitely. Always implement an iteration limit and fallback to human handoff or graceful failure."
        d["examRule"] = "Exam Rule: Bounded agent execution requires maximum loop iteration limits, tool timeout handling, and session state monitoring."

    elif sid == "core-037":
        d["intuition"] = "Multi-agent systems divide complex domains into specialized sub-agents (e.g. Billing Agent, Technical Agent) coordinated by a Supervisor Agent."
        d["architecture"] = "User Query -> Supervisor/Router Agent -> Routes to Domain Specialist Agent -> Specialist uses private Action Groups & Knowledge Base -> Returns answer to Supervisor."
        d["api"] = "Bedrock Multi-Agent Collaboration: Supervisor agent delegates to sub-agents registered as collaborators. Sub-agents execute independent instruction sets."
        d["traps"] = "Trap: Stuffing all company tools (50+ APIs) into a single monolithic agent. Model tool selection accuracy degrades rapidly with too many tools; use multi-agent specialization!"
        d["examRule"] = "Exam Rule: When an application requires dozens of tools across different domains, decompose into specialized sub-agents with a routing supervisor."

    elif sid == "core-038":
        d["intuition"] = "High-impact actions (wire transfers, deleting resources, placing orders) require Human-in-the-Loop (HITL) approval before execution."
        d["architecture"] = "Agent identifies action -> Step Functions Task Token or Return of Control -> Pauses execution & notifies reviewer -> Reviewer approves -> Execution resumes."
        d["api"] = "Bedrock Agent Action Group: `customControlMethod='RETURN_OF_CONTROL'` (agent pauses and returns toolUse to client instead of calling Lambda directly)."
        d["traps"] = "Trap: Allowing an autonomous agent to execute irreversible financial or database write actions directly without human verification."
        d["examRule"] = "Exam Rule: For sensitive or regulated tool execution, use Return of Control (`RETURN_OF_CONTROL`) or AWS Step Functions task tokens to pause for human approval."

    elif sid == "core-039":
        d["intuition"] = "Action Groups connect agents to external business systems via OpenAPI 3.0 schemas, mapping model intent into validated REST parameters."
        d["architecture"] = "Agent -> OpenAPI 3.0 Schema (stored in S3) -> Bedrock validates parameters -> Executes target AWS Lambda function (or Return of Control) -> Returns response."
        d["api"] = "bedrock-agent.create_agent_action_group(actionGroupName=..., apiSchema={'s3': {'s3BucketName': '...', 's3ObjectKey': 'openapi.json'}}, actionGroupExecutor={'lambda': 'arn:...'})"
        d["traps"] = "Trap: Forgetting to add a resource-based policy on the Lambda function granting `bedrock.amazonaws.com` permission to invoke it (`lambda:InvokeFunction`)."
        d["examRule"] = "Exam Rule: Action Group Lambda execution requires an OpenAPI 3.0 schema and a Lambda resource policy permitting `bedrock.amazonaws.com` with source ARN condition."

    elif sid == "core-040":
        d["intuition"] = "Model Context Protocol (MCP) is an open standard that decouples LLM applications from tool/data integrations via client-server architecture."
        d["architecture"] = "MCP Host (Application/Agent) <-> MCP Client <-> Standardized JSON-RPC Protocol (stdio / SSE) <-> MCP Server (Database, Filesystem, GitHub, AWS)."
        d["api"] = "MCP Primitives: Prompts (reusable templates), Resources (context/documents), Tools (executable functions with JSON schemas)."
        d["traps"] = "Trap: Writing custom bespoke connectors for every new data source. MCP provides a standardized protocol for tool discovery and execution."
        d["examRule"] = "Exam Rule: Model Context Protocol (MCP) uses JSON-RPC to standardize how generative AI agents discover and execute tools and access resources."

    elif sid == "core-041":
        d["intuition"] = "AgentCore component boundaries isolate Orchestration (ReAct reasoning), Working Memory (short-term session), Long-Term Memory (vector/RAG), and Tools."
        d["architecture"] = "User Input -> Safety Guardrails -> Orchestrator <-> Working Memory (DynamoDB) <-> Long-term Knowledge (Knowledge Bases) <-> Action Groups (Lambda) -> Output Guardrail."
        d["api"] = "Separate IAM execution roles for Agent (bedrock.amazonaws.com), Lambda tools, and Knowledge Base vector access."
        d["traps"] = "Trap: Conflating working memory with Knowledge Bases. Working memory tracks conversation state; Knowledge Bases supply permanent enterprise documents."
        d["examRule"] = "Exam Rule: Maintain clear isolation between Agent Orchestration, Ephemeral Session Memory (DynamoDB), and Enterprise Knowledge Bases (OpenSearch)."

    elif sid == "core-042":
        d["intuition"] = "Deployment modes balance control vs management: Fully Managed Serverless (Bedrock), Curated Managed Hosting (SageMaker JumpStart), Self-Managed (EKS/EC2)."
        d["architecture"] = "Bedrock: Zero infrastructure, multi-tenant/provisioned serverless. SageMaker JumpStart: Dedicated instances (ml.g5/p4d), custom containers, private VPC hosting."
        d["api"] = "SageMaker: sagemaker.create_model(), create_endpoint_config(), create_endpoint(). Bedrock: invoke_model() directly."
        d["traps"] = "Trap: Choosing SageMaker endpoint hosting when the requirement calls for zero server management and pay-per-token pricing. Use Bedrock!"
        d["examRule"] = "Exam Rule: 'Zero infrastructure management and pay-per-token' -> Bedrock. 'Custom HuggingFace container, full VPC isolation, dedicated GPU control' -> SageMaker."

    elif sid == "core-043":
        d["intuition"] = "Self-hosting LLMs on AWS requires understanding GPU instance families, VRAM memory footprints, quantization, and serving engines (vLLM, TGI)."
        d["architecture"] = "EC2/SageMaker Instance Families: G5 (NVIDIA A10G), P4d/P4de (NVIDIA A100), P5 (NVIDIA H100), Trn1 (AWS Trainium), Inf2 (AWS Inferentia2)."
        d["api"] = "AWS Neuron SDK for compiling and serving models on Inferentia2 (inf2) and Trainium (trn1) for high-throughput, cost-effective inference."
        d["traps"] = "Trap: Deploying an unquantized 70B parameter model on a single 24GB VRAM GPU. A 70B model in fp16 requires at least ~140GB VRAM (e.g. ml.g5.48xlarge or ml.p4d)."
        d["examRule"] = "Exam Rule: For low-cost, high-throughput custom model hosting on AWS silicon, use AWS Inferentia2 (Inf2) instances with AWS Neuron SDK."

    elif sid == "core-044":
        d["intuition"] = "Model routing cascades route incoming requests to the cheapest and fastest model capable of solving the task, escalating only when needed."
        d["architecture"] = "Request -> Classifier / Small Model (e.g. Claude Haiku / Titan Lite) -> Simple task? Answer immediately! Complex query? Escalate to Claude Sonnet/Opus."
        d["api"] = "Gateway routing logic evaluates query classification confidence score. If confidence > 0.85 -> small model, else -> large model."
        d["traps"] = "Trap: Sending 100% of enterprise traffic to flagship models. 70%+ of typical enterprise requests are simple queries that smaller models solve at 90% lower cost."
        d["examRule"] = "Exam Rule: Implement a Model Cascade / Router to optimize cost and latency: evaluate with lightweight models first, escalate complex tasks to frontier models."

    elif sid == "core-045":
        d["intuition"] = "Event-driven GenAI architectures decouple real-time user experiences from long-running inference jobs using Amazon EventBridge and SQS."
        d["architecture"] = "Client -> API Gateway -> SQS Queue -> Lambda Worker -> Bedrock Model -> Amazon EventBridge -> WebSocket / Push Notification to Client."
        d["api"] = "boto3.client('sqs').send_message(), boto3.client('events').put_events(). API Gateway WebSocket API for push updates."
        d["traps"] = "Trap: Making synchronous REST calls from API Gateway with a 29-second hard timeout for agent workflows that take 45+ seconds. The gateway will time out!"
        d["examRule"] = "Exam Rule: API Gateway has a 29-second maximum integration timeout. For agent tasks exceeding 29s, use asynchronous processing with SQS/Step Functions and WebSockets."

    elif sid == "core-046":
        d["intuition"] = "Enterprise federation connects corporate identity providers (Okta, Azure AD, Ping) to AWS using IAM Identity Center and OIDC/SAML 2.0."
        d["architecture"] = "Corporate IdP -> IAM Identity Center (SAML 2.0) -> Temporary AWS credentials via STS:AssumeRoleWithWebIdentity -> Enforces user-level access to Bedrock."
        d["api"] = "AWS STS AssumeRole, IAM Session Tags (`aws:PrincipalTag/Department`) for attribute-based access control (ABAC) to Bedrock resources."
        d["traps"] = "Trap: Creating static IAM user access keys for every enterprise employee. Always use IAM Identity Center and federated temporary role credentials."
        d["examRule"] = "Exam Rule: Enterprise user authentication to GenAI applications must use IAM Identity Center with SAML/OIDC federation and temporary STS credentials."

    elif sid == "core-047":
        d["intuition"] = "Data residency and sovereignty regulations (GDPR, HIPAA, country-specific laws) dictate where data and model inference can physically execute."
        d["architecture"] = "Regulated Data in Germany -> Local AWS Region (eu-central-1 Frankfurt) -> Bedrock single-region endpoint -> Stored in local S3 with KMS CMK -> Never leaves Region."
        d["api"] = "Ensure modelId uses regional identifier (`anthropic.claude...`), NOT cross-region profile (`us.` or `global.`) if strict residency is enforced."
        d["traps"] = "Trap: Enabling a US Cross-Region Inference Profile for data subject to European GDPR residency mandates. The data would leave the European Economic Area!"
        d["examRule"] = "Exam Rule: When compliance requires strict in-country data residency, use single-region Bedrock endpoints or geographically restricted inference profiles."

    elif sid == "core-048":
        d["intuition"] = "A Generative AI Gateway centralizes rate limiting, authentication, telemetry, cost tracking, and model switching behind a unified corporate facade."
        d["architecture"] = "Internal Apps -> Amazon API Gateway / ALB -> Lambda Gateway Authorizer -> Bedrock Guardrails -> Bedrock Converse API -> CloudWatch Metrics."
        d["api"] = "API Gateway Usage Plans and API Keys for consumer quota management; CloudWatch EMF (Embedded Metric Format) for token usage tracking."
        d["traps"] = "Trap: Letting individual development teams call Bedrock APIs directly with uncontrolled IAM roles, causing fragmented billing and lack of centralized guardrails."
        d["examRule"] = "Exam Rule: A Generative AI Gateway pattern provides centralized governance, rate-limiting, authentication, cost allocation, and safety enforcement."

    elif sid == "core-049":
        d["intuition"] = "Choose invocation patterns based on SLA: Synchronous for instant chat, Asynchronous/Streaming for interactive UI, Batch for bulk offline processing."
        d["architecture"] = "Sync: invoke_model(). Streaming: invoke_model_with_response_stream(). Batch: create_model_invocation_job() (50% cheaper, processing thousands of records via S3)."
        d["api"] = "bedrock.create_model_invocation_job(jobName=..., roleArn=..., modelId=..., inputDataConfig={'s3InputDataConfig': {'s3Uri': 's3://.../batch.jsonl'}})."
        d["traps"] = "Trap: Running thousands of offline document summarization requests via synchronous on-demand API. Use Bedrock Batch Inference for 50% discount and no quota thrashing!"
        d["examRule"] = "Exam Rule: For non-real-time bulk workloads (e.g. nightly document analysis), use Amazon Bedrock Batch Inference for a 50% cost reduction."

    elif sid == "core-050":
        d["intuition"] = "Response streaming reduces perceived latency (Time to First Token - TTFT) from seconds to milliseconds by streaming token chunks via Server-Sent Events (SSE)."
        d["architecture"] = "Client -> HTTP Chunked Transfer / SSE -> Bedrock ConverseStream API -> Token chunks emitted as generated -> Client UI renders text progressively."
        d["api"] = "bedrock_runtime.converse_stream(modelId=..., messages=...). Iterate: `for event in response['stream']: if 'contentBlockDelta' in event: print(event['contentBlockDelta']['delta']['text'])`."
        d["traps"] = "Trap: Placing an intermediate API component (like an unconfigured buffering proxy) that buffers the entire response before returning, destroying the streaming benefit."
        d["examRule"] = "Exam Rule: Use `converse_stream` or `invoke_model_with_response_stream` with HTTP Server-Sent Events (SSE) to achieve minimum Time to First Token (TTFT)."

    elif sid == "core-051":
        d["intuition"] = "Handling 429 ThrottlingException and transient errors requires exponential backoff with full jitter to avoid the 'thundering herd' problem."
        d["architecture"] = "Client -> Bedrock call fails with ThrottlingException -> Wait `random(0, min(max_backoff, base * 2^attempt))` -> Retry up to max attempts -> Circuit breaker opens on sustained failure."
        d["api"] = "botocore.config.Config(retries={'max_attempts': 10, 'mode': 'adaptive'}). Full Jitter algorithm: `sleep = random.uniform(0, min(cap, base * 2 ** attempt))`."
        d["traps"] = "Trap: Using fixed retry intervals (e.g. retry every 2 seconds). All failing clients retry simultaneously and re-throttle the service. Always add random Jitter!"
        d["examRule"] = "Exam Rule: Handle Bedrock ThrottlingException using Exponential Backoff with FULL JITTER or enable the AWS SDK 'adaptive' retry mode."

    elif sid == "core-052":
        d["intuition"] = "Routing policies switch to fallback models or degraded modes when a primary model experiences an outage or capacity exhaustion."
        d["architecture"] = "Primary Model (Claude 3.5 Sonnet) -> Throttling / 5xx error? -> Fallback Model (Amazon Titan / Claude 3 Haiku) -> Graceful degradation message if all fail."
        d["api"] = "Try/Except block catching `ClientError`: if e.response['Error']['Code'] == 'ThrottlingException': invoke fallback model."
        d["traps"] = "Trap: Falling back to a model with a smaller context window without validating input token size, leading to an immediate `ValidationException`."
        d["examRule"] = "Exam Rule: Resilient production architectures must define automated fallback models and verify token limit compatibility before routing."

    elif sid == "core-053":
        d["intuition"] = "Developer tooling and interfaces like AWS SDK, AWS CDK, Bedrock Playground, and LangChain accelerate prototyping and deployment."
        d["architecture"] = "Infrastructure as Code: AWS CDK (L2 Bedrock constructs: `bedrock.CfnKnowledgeBase`, `bedrock.CfnAgent`, `bedrock.CfnGuardrail`) -> Automated CloudFormation deployment."
        d["api"] = "AWS CDK TypeScript / Python: `new bedrock.CfnGuardrail(this, 'MyGuardrail', { name: 'ProdGuardrail', ... })`."
        d["traps"] = "Trap: Manually configuring production Knowledge Bases and Agents in the AWS Console. Always codify production GenAI infrastructure in AWS CDK or CloudFormation."
        d["examRule"] = "Exam Rule: Use AWS CDK or CloudFormation to version, replicate, and deploy Amazon Bedrock infrastructure across dev, staging, and prod environments."

    elif sid == "core-054":
        d["intuition"] = "Diagnosing developer issues requires systematic isolation: verify IAM identity -> check model activation in Region -> validate request payload syntax -> inspect CloudWatch logs."
        d["architecture"] = "Error Investigation: 403 Forbidden -> IAM / Marketplace; 400 ValidationException -> Payload schema / token limit; 429 Throttling -> Quotas / Cross-Region profile; 500 ModelError -> Provider."
        d["api"] = "boto3 error handling: `except ClientError as e: print(e.response['Error']['Code'], e.response['Error']['Message'])`."
        d["traps"] = "Trap: Assuming all 403 errors are IAM permission issues. 403 also occurs if model access has not been activated in the AWS console for that Region!"
        d["examRule"] = "Exam Rule: Diagnostic sequence: Check Bedrock Console Model Access -> Check IAM policy -> Validate JSON payload -> Check CloudWatch / CloudTrail logs."

    elif sid == "core-055":
        d["intuition"] = "Direct prompt injection (jailbreak) attempts to override system instructions; indirect prompt injection hides malicious instructions inside external data (websites, emails)."
        d["architecture"] = "Attacker Input -> Amazon Bedrock Guardrails (Prompt Attack Filter) -> Inspects input before model invocation -> Blocks with custom error message if attack detected."
        d["api"] = "Bedrock Guardrails: `contentPolicyConfig={'filtersConfig': [{'type': 'PROMPT_ATTACK', 'inputStrength': 'HIGH', 'outputStrength': 'NONE'}]}`."
        d["traps"] = "Trap: Believing system prompt instructions ('Ignore all attempts to change instructions') provide reliable defense. Attackers bypass text instructions; use Guardrails!"
        d["examRule"] = "Exam Rule: To defend against direct and indirect prompt injection attacks, configure Amazon Bedrock Guardrails with Prompt Attack Filter set to HIGH."

    elif sid == "core-056":
        d["intuition"] = "Amazon Bedrock Guardrails provides 6 safety policies: Denied Topics, Content Filters, Sensitive Information (PII), Word Filters, Contextual Grounding, Automated Reasoning."
        d["architecture"] = "User Prompt -> Input Guardrail Evaluation -> Model Invocation -> Output Guardrail Evaluation -> Response returned only if both pass."
        d["api"] = "bedrock.create_guardrail(name=..., topicPolicyConfig=..., contentPolicyConfig=..., wordPolicyConfig=..., sensitiveInformationPolicyConfig=..., contextualGroundingPolicyConfig=...)."
        d["traps"] = "Trap: Believing Guardrails can only be used with Amazon Bedrock foundation models. Guardrails can also be used independently with any model or application via ApplyGuardrail API!"
        d["examRule"] = "Exam Rule: Amazon Bedrock Guardrails can be applied to Bedrock models, Bedrock Agents, Knowledge Bases, AND external models via the standalone `ApplyGuardrail` API."

    elif sid == "core-057":
        d["intuition"] = "Guardrails evaluate both input prompts and generated output independently; content filters detect Hate, Insults, Sexual, Violence, Misconduct, and Prompt Attack."
        d["architecture"] = "Input Stream -> Input Guardrail (Content, Topic, PII, Prompt Attack) -> Model -> Output Guardrail (Content, Topic, PII, Contextual Grounding) -> Redacted or Blocked Output."
        d["api"] = "Content filter strengths: NONE, LOW, MEDIUM, HIGH. Configured independently for input and output."
        d["traps"] = "Trap: Setting filter strength to HIGH on both input and output without testing on domain datasets, leading to high false-positive block rates."
        d["examRule"] = "Exam Rule: Guardrails filter strengths (LOW, MEDIUM, HIGH) can and should be tuned independently for user inputs versus model outputs."

    elif sid == "core-058":
        d["intuition"] = "Contextual Grounding Check detects hallucinations in RAG applications by evaluating Grounding (factual support in reference docs) and Relevance (addressing user query)."
        d["architecture"] = "User Query + Retrieved Reference Source + Model Output -> Contextual Grounding Policy -> Computes Grounding Score (0.0 to 1.0) & Relevance Score (0.0 to 1.0) -> Blocks if below threshold."
        d["api"] = "contextualGroundingPolicyConfig={'filtersConfig': [{'type': 'GROUNDING', 'threshold': 0.85}, {'type': 'RELEVANCE', 'threshold': 0.80}]}."
        d["traps"] = "Trap: Using traditional content filters to stop factual hallucinations. Content filters only check toxicity; only Contextual Grounding checks factual faithfulness to RAG sources!"
        d["examRule"] = "Exam Rule: To prevent hallucinations in RAG and verify that model outputs are grounded in retrieved source documents, configure Contextual Grounding Check."

    elif sid == "core-059":
        d["intuition"] = "Automated Reasoning checks use mathematical formal methods and logic solvers to verify critical business rules without relying on probabilistic LLM judgment."
        d["architecture"] = "Business Policy Rules (Formal Logic) -> Automated Reasoning Validator -> Evaluates LLM action/response against provable invariants -> Guaranteed compliance."
        d["api"] = "Used in mission-critical compliance and security policies where 99.9% statistical accuracy is unacceptable and mathematical certainty is required."
        d["traps"] = "Trap: Using an LLM-as-a-judge to verify strict regulatory or mathematical constraints. LLM judges are probabilistic; Automated Reasoning provides deterministic mathematical proofs."
        d["examRule"] = "Exam Rule: When zero tolerance for compliance violation is required, choose Automated Reasoning over probabilistic LLM evaluators."

    elif sid == "core-060":
        d["intuition"] = "Enterprise security mandates that GenAI traffic never traverses the public internet; use AWS PrivateLink VPC Endpoints with IAM endpoint policies."
        d["architecture"] = "VPC Private Subnet -> VPC Interface Endpoint for Bedrock (`com.amazonaws.region.bedrock-runtime`) -> PrivateLink -> Bedrock Service (no Internet Gateway / NAT required)."
        d["api"] = "VPC Endpoint Policy: enforce `Condition: {'StringEquals': {'aws:PrincipalArn': 'arn:aws:iam::account:role/AppRole'}}`. IAM Policy: `Condition: {'StringEquals': {'aws:sourceVpce': 'vpce-xxx'}}`."
        d["traps"] = "Trap: Configuring an S3 Gateway Endpoint and expecting it to secure Bedrock runtime calls. Bedrock requires an Interface VPC Endpoint (PrivateLink)!"
        d["examRule"] = "Exam Rule: To restrict Bedrock access strictly to private subnets without internet access, create an Interface VPC Endpoint (PrivateLink) and use `aws:sourceVpce` condition key."

    elif sid == "core-061":
        d["intuition"] = "Data protection requires envelope encryption: data at rest is encrypted with Customer Managed Keys (CMK) in AWS KMS; data in transit uses TLS 1.3."
        d["architecture"] = "S3 (docs) + OpenSearch Serverless (vectors) + Bedrock Custom Models + Model Invocation Logs ALL encrypted with dedicated AWS KMS Customer Managed Keys (CMK)."
        d["api"] = "KMS Key Policy MUST grant Bedrock service principal: `Principal: {'Service': 'bedrock.amazonaws.com'}, Action: ['kms:Decrypt', 'kms:GenerateDataKey*'], Condition: {'StringEquals': {'aws:SourceAccount': '...'}}`."
        d["traps"] = "Trap: Using AWS Managed Keys when regulatory requirements mandate annual key rotation and cross-account access control. Customer Managed Keys (CMK) are required!"
        d["examRule"] = "Exam Rule: Custom encryption at rest for Bedrock resources (Knowledge Bases, Custom Models, Invocation Logs) requires an AWS KMS Customer Managed Key (CMK) with appropriate key policy."

    elif sid == "core-062":
        d["intuition"] = "PII protection detects and masks sensitive personal data (SSN, credit cards, emails) using Bedrock Guardrails PII filters or Amazon Macie on S3."
        d["architecture"] = "Inbound/Outbound text -> Bedrock Guardrails Sensitive Information Filter -> Detects 30+ entity types -> Action: ANONYMIZE (replaces with `[SSN]`) or BLOCK (halts response)."
        d["api"] = "sensitiveInformationPolicyConfig={'piiEntitiesConfig': [{'type': 'SSN', 'action': 'ANONYMIZE'}, {'type': 'CREDIT_DEBIT_CARD_NUMBER', 'action': 'BLOCK'}], 'regexesConfig': [...]}."
        d["traps"] = "Trap: Choosing BLOCK when the application needs to process the text with sensitive data masked. Use ANONYMIZE to mask PII while keeping conversation flowing!"
        d["examRule"] = "Exam Rule: To mask sensitive personal data without blocking the request, configure Bedrock Guardrails PII filter with action set to ANONYMIZE."

    elif sid == "core-063":
        d["intuition"] = "Amazon Bedrock provides strong data privacy boundaries: customer prompts, completions, and custom models are NEVER used to train base foundation models."
        d["architecture"] = "Customer Account -> Secure Encrypted Bedrock API -> Ephemeral processing in isolated tenant container -> Response returned -> Zero data retained for base model training."
        d["api"] = "AWS SOC, ISO, HIPAA eligible; AWS Artifact provides compliance verification reports."
        d["traps"] = "Trap: Believing third-party model providers on Bedrock (Anthropic, Meta, Cohere) receive customer data for external training. None of the providers train on Bedrock customer data!"
        d["examRule"] = "Exam Rule: AWS guarantees that customer inputs and model outputs in Amazon Bedrock are never used to train Amazon or third-party foundation models."

    elif sid == "core-064":
        d["intuition"] = "AI governance requires tracking model cards, lineage, training datasets, and intended use cases to comply with EU AI Act and ISO 42001."
        d["architecture"] = "SageMaker Model Cards / Bedrock Model Cards -> Documents model purpose, training metrics, ethical considerations, evaluation results, and approval history."
        d["api"] = "sagemaker.create_model_card(modelCardName=..., content=json.dumps({'intended_uses': '...', 'risk_rating': 'LOW'}))."
        d["traps"] = "Trap: Treating AI governance as an informal wiki document. Regulators require formal, versioned, auditable Model Cards tied to deployed model artifacts."
        d["examRule"] = "Exam Rule: For auditable model documentation, governance, and compliance reporting, use Amazon SageMaker Model Cards."

    elif sid == "core-065":
        d["intuition"] = "Continuous governance combines AWS Config rules, Service Control Policies (SCPs), and automated compliance checks across multi-account AWS Organizations."
        d["architecture"] = "AWS Organizations SCP (restricts Bedrock model IDs and regions) -> AWS Config (monitors encryption at rest and logging) -> Security Hub (aggregates posture)."
        d["api"] = "SCP Policy: `Deny bedrock:* on arn:aws:bedrock:*:*:custom-model/* unless Condition: {'StringEquals': {'aws:PrincipalArn': 'arn:.../MLOpsRole'}}`."
        d["traps"] = "Trap: Managing security rules account by account. Enterprise governance must use AWS Organizations Service Control Policies (SCPs) at the OU level."
        d["examRule"] = "Exam Rule: Use AWS Organizations SCPs to enforce guardrail attachments, restrict authorized model IDs, and mandate specific AWS Regions across all accounts."

    elif sid == "core-066":
        d["intuition"] = "Responsible AI demands transparency: clearly disclosing AI-generated content, conveying model confidence, and surfacing citations for every factual claim."
        d["architecture"] = "Model Output -> Citations from Knowledge Base -> Displayed in UI with clickable source reference links -> Discloses AI participation."
        d["api"] = "RetrieveAndGenerate response metadata includes `citations[].retrievedReferences[].location.s3Location.uri` and snippet text."
        d["traps"] = "Trap: Stripping citation metadata before displaying answers to users. Regulated domains require source provenance and citation display."
        d["examRule"] = "Exam Rule: To provide transparency and verifiable answers, expose Bedrock Knowledge Base citation metadata directly in the user interface."

    elif sid == "core-067":
        d["intuition"] = "Fairness evaluation measures disparate impact, demographic parity, and representational bias across protected sub-populations."
        d["architecture"] = "Evaluation Dataset -> SageMaker Clarify / Bedrock Model Evaluation -> Tests model responses across demographic prompts -> Computes bias and fairness metrics."
        d["api"] = "SageMaker Clarify pre-training and post-training bias metrics: Class Imbalance (CI), Difference in Positive Proportions (DPPL), Disparate Impact."
        d["traps"] = "Trap: Assuming prompt safety filters automatically eliminate demographic bias. Dedicated fairness evaluation with diverse benchmark datasets is required."
        d["examRule"] = "Exam Rule: Use Amazon SageMaker Clarify or Amazon Bedrock Model Evaluation to detect, measure, and mitigate model bias across demographic groups."

    elif sid == "core-068":
        d["intuition"] = "Cost optimization begins with token economics: Input tokens are typically 3-4x cheaper than output tokens; minimize output verbosity and prune context."
        d["architecture"] = "Token Cost = (Input Tokens / 1,000 * Input Rate) + (Output Tokens / 1,000 * Output Rate). Claude 3.5 Sonnet: $0.003/1k input, $0.015/1k output."
        d["api"] = "Inspect response['usage']: `inputTokens`, `outputTokens`, `totalTokens`. Set `maxTokens` to constrain runaway generation costs."
        d["traps"] = "Trap: Allowing the model to output long preambles ('Sure! Here is the answer you requested: ...'). Instruct model: 'Answer directly in JSON with zero preamble' to save output tokens!"
        d["examRule"] = "Exam Rule: Output tokens cost significantly more than input tokens. Enforce concise outputs, zero conversational filler, and token limits to minimize billable cost."

    elif sid == "core-069":
        d["intuition"] = "Analyze unit economics: calculate Cost Per Successful Task, comparing prompt engineering vs RAG vs fine-tuning vs self-hosting over anticipated query volume."
        d["architecture"] = "Cost Comparison: Low volume (<50k queries/day) -> Serverless On-Demand Bedrock. High steady volume (>500k queries/day) -> Provisioned Throughput or fine-tuned smaller model on EC2."
        d["api"] = "AWS Cost Explorer + Cost Allocation Tags (`Project: GenAI-Support`, `Environment: Prod`) activated in Billing console."
        d["traps"] = "Trap: Calculating only API invocation costs and ignoring auxiliary costs: vector storage (AOSS OCUs), S3 storage, NAT Gateway bandwidth, and KMS requests."
        d["examRule"] = "Exam Rule: Comprehensive GenAI cost modeling must account for Model Invocations + Vector Store OCUs + CloudWatch Ingestion + Network Data Transfer."

    elif sid == "core-070":
        d["intuition"] = "Amazon Bedrock Prompt Caching caches frequent prompt prefixes (system instructions, few-shot examples, large RAG documents), reducing input cost and latency."
        d["architecture"] = "First Request -> Writes Prompt Prefix to Cache -> Subsequent Requests matching prefix -> Reads from Cache -> 90% cheaper input tokens + up to 85% lower latency."
        d["api"] = "Converse API: add cachePoint to messages or system blocks: `system=[{'text': long_instructions, 'cachePoint': {'type': 'default'}}]`."
        d["traps"] = "Trap: Putting dynamic user variables *before* the static cached instructions. Cache matches strictly from the beginning of the prompt; static prefixes MUST come first!"
        d["examRule"] = "Exam Rule: To leverage Prompt Caching, place all static content (system instructions, tool definitions, reference docs) at the START of the prompt before dynamic user inputs."

    elif sid == "core-071":
        d["intuition"] = "Prompt caching requires minimum prefix token thresholds (e.g. 1,024 tokens for Claude models) and has a 5-minute Time-To-Live (TTL) refreshed on each hit."
        d["architecture"] = "Cache Key = Model ID + Prompt Prefix Tokens. Cache hit response usage indicates `cachedInputTokenCount`."
        d["api"] = "Inspect response['usage']: `inputTokenCount`, `outputTokenCount`, `cacheReadInputTokenCount`, `cacheWriteInputTokenCount`."
        d["traps"] = "Trap: Attempting to cache short 100-token prompts. Prompts below the model's minimum cache threshold (e.g. 1024 tokens) will NOT be cached."
        d["examRule"] = "Exam Rule: Prompt Caching requires meeting the minimum token threshold (1,024 tokens) and provides a 5-minute rolling TTL refreshed by cache hits."

    elif sid == "core-072":
        d["intuition"] = "Capacity planning compares On-Demand serverless pricing against Provisioned Throughput (committed Model Units) for guaranteed throughput and custom models."
        d["architecture"] = "Provisioned Throughput: 1 Model Unit (MU) provides guaranteed TPS/RPM with no throttling. Available in No Commitment, 1-Month Commitment, or 6-Month Commitment."
        d["api"] = "bedrock.create_provisioned_model_throughput(modelId=..., provisionedModelName=..., modelUnits=1, commitmentDuration='OneMonth')."
        d["traps"] = "Trap: Purchasing Provisioned Throughput for highly bursty, intermittent workloads. On-Demand pricing is significantly cheaper for variable low-utilization traffic!"
        d["examRule"] = "Exam Rule: Use Provisioned Throughput when you require guaranteed capacity/low latency SLAs with steady high volume, OR when deploying Custom/Fine-Tuned models."

    elif sid == "core-073":
        d["intuition"] = "Latency decomposes into Time to First Token (TTFT - dominated by prompt processing and model startup) and Inter-Token Latency (governed by generation length)."
        d["architecture"] = "Total Latency = Network Overhead + Guardrail Input Check + TTFT + (Generated Tokens * Inter-Token Latency) + Guardrail Output Check."
        d["api"] = "CloudWatch Metrics for Bedrock: `InvocationLatency` (total time) and `FirstTokenLatency` (TTFT)."
        d["traps"] = "Trap: Believing streaming reduces total generation time. Streaming does not change total execution time; it drastically reduces *perceived* latency by streaming TTFT!"
        d["examRule"] = "Exam Rule: To optimize user-perceived responsiveness, implement response streaming to minimize Time to First Token (TTFT)."

    elif sid == "core-074":
        d["intuition"] = "Retrieval optimization tunes chunk size, top-K count, vector index configuration, and re-ranking to balance search recall against model context bloat."
        d["architecture"] = "Query -> Initial Vector Search retrieves Top 20 chunks -> Cohere Re-ranker filters down to Top 3 most relevant chunks -> Clean, compact context sent to FM."
        d["api"] = "Bedrock Knowledge Base retrievalConfiguration: `vectorSearchConfiguration={'numberOfResults': 3}`. High top-K wastes context tokens and degrades attention."
        d["traps"] = "Trap: Passing 20+ retrieved chunks into the LLM prompt. The model suffers from the 'Lost in the Middle' phenomenon where facts in the middle of long context are ignored!"
        d["examRule"] = "Exam Rule: Combine high recall initial retrieval (Top-20) with a Re-ranker to pass only the top 3-5 highest-scoring passages to the foundation model."

    elif sid == "core-075":
        d["intuition"] = "End-to-end GenAI observability captures metrics, structured application logs, and distributed traces across client, gateway, agent, vector store, and model."
        d["architecture"] = "App -> AWS X-Ray Tracing (propagates trace ID) -> CloudWatch Logs (structured JSON) -> CloudWatch Metrics & Dashboards -> CloudWatch Alarms."
        d["api"] = "AWS X-Ray SDK: trace Bedrock API calls, Lambda execution, and database lookups into a unified Service Map."
        d["traps"] = "Trap: Relying solely on basic CloudWatch metrics. You cannot debug agent tool failures or slow retrieval without distributed tracing (AWS X-Ray)."
        d["examRule"] = "Exam Rule: Use AWS X-Ray and Amazon CloudWatch ServiceLens for distributed tracing of multi-step agent and RAG workflows."

    elif sid == "core-076":
        d["intuition"] = "Distinguish management plane auditing (AWS CloudTrail) from data plane payload inspection (Bedrock Model Invocation Logging)."
        d["architecture"] = "CloudTrail logs management events (`CreateModelCustomizationJob`, `CreateAgent`). Bedrock Model Invocation Logging logs exact prompt and output text to S3 / CloudWatch."
        d["api"] = "bedrock.put_model_invocation_logging_configuration(loggingConfig={'cloudWatchConfig': {'logGroupName': '...'}, 's3Config': {'bucketName': '...'}, 'textDataDeliveryEnabled': True})."
        d["traps"] = "Trap: Searching CloudTrail to find the prompt text a user submitted. CloudTrail NEVER records request/response body payloads! You MUST enable Model Invocation Logging!"
        d["examRule"] = "Exam Rule: To audit the actual prompt text and model completions for compliance, enable Amazon Bedrock Model Invocation Logging to S3 or CloudWatch Logs."

    elif sid == "core-077":
        d["intuition"] = "Agent telemetry tracks tool call success rates, tool latency, loop iteration counts, and reasoning traces to detect thrashing and failed executions."
        d["architecture"] = "Bedrock Agent invoke_agent() -> Returns event stream with `trace` events -> Pre-processing trace, Orchestration trace, Post-processing trace, Failure trace."
        d["api"] = "invoke_agent(enableTrace=True). Read event stream: `if 'trace' in event: trace_data = event['trace']['trace']`."
        d["traps"] = "Trap: Turning off agent traces in production without centralizing error logs. When an agent returns a generic failure, trace events are the only way to inspect why it failed."
        d["examRule"] = "Exam Rule: Set `enableTrace=True` in `invoke_agent` to inspect step-by-step agent reasoning, tool inputs/outputs, and knowledge base lookups."

    elif sid == "core-078":
        d["intuition"] = "Diagnosing GenAI system failures requires localizing faults into 4 categories: Model Failure, Retrieval Failure, Guardrail Interception, or Tool/Network Error."
        d["architecture"] = "Triage: Blocked output? -> Check Guardrail action. Generic answer? -> Check RAG retrieval relevancy. Schema error? -> Check tool JSON schema. 429? -> Quota."
        d["api"] = "Bedrock CloudWatch Metrics: `InvocationLatency`, `Invocations`, `InvocationClientErrors`, `InvocationServerErrors`."
        d["traps"] = "Trap: Blaming the foundation model when a RAG query gives a poor answer. In 80%+ of cases, the failure is poor chunking or irrelevant vector retrieval, not model reasoning!"
        d["examRule"] = "Exam Rule: Systematic failure diagnosis: 1) Verify raw retrieved chunks, 2) Inspect guardrail block logs, 3) Validate tool output format, 4) Check token limits."

    elif sid == "core-079":
        d["intuition"] = "Evaluation measures GenAI across distinct dimensions: Task Accuracy, Faithfulness/Groundedness, Semantic Similarity, Robustness, Toxicity, and Cost/Latency."
        d["architecture"] = "Evaluation Harness -> Feeds Golden Test Dataset -> Runs Target Model -> Evaluates against reference answers across multiple automated and judge metrics."
        d["api"] = "Bedrock Model Evaluation: Automatic evaluation jobs supporting built-in metrics and curated benchmark datasets."
        d["traps"] = "Trap: Using a single accuracy metric to evaluate generative text. You must evaluate multiple dimensions (faithfulness, answer relevance, toxicity, latency)."
        d["examRule"] = "Exam Rule: A robust GenAI evaluation harness evaluates both RAG retrieval performance AND generation quality across multiple orthogonal dimensions."

    elif sid == "core-080":
        d["intuition"] = "Evaluation uses three complementary tiers: Programmatic (deterministic regex/code checks), Model-Based (LLM-as-a-judge for complex reasoning), and Human Evaluation."
        d["architecture"] = "Fast/Cheap: Programmatic unit tests -> Scalable/Deep: LLM-as-a-Judge -> Ground Truth Gold Standard: Human Subject Matter Expert (SME) review."
        d["api"] = "Amazon Bedrock Human Evaluation: configure workforce using Amazon Mechanical Turk, AWS Managed Workforce, or Private Company Workforce (Amazon Cognito/OIDC)."
        d["traps"] = "Trap: Relying exclusively on human evaluation for CI/CD gates. Human evaluation is slow and expensive; use automated LLM judges for CI/CD and humans for spot audits!"
        d["examRule"] = "Exam Rule: For automated CI/CD regression gates, use LLM-as-a-Judge. For final compliance sign-off and golden dataset labeling, use Private Human Workforces."

    elif sid == "core-081":
        d["intuition"] = "LLM-as-a-Judge systems suffer from known systematic biases: Position Bias, Verbosity/Length Bias, Self-Enhancement Bias, and Egocentric Bias."
        d["architecture"] = "Calibration: Swap order of candidates (A/B and B/A) to defeat position bias; strip formatting to defeat verbosity bias; use few-shot scoring rubrics."
        d["api"] = "Judge Prompt Structure: Chain-of-Thought reasoning required *before* score emission: `Score 1-5 with detailed justification based strictly on rubric.`"
        d["traps"] = "Trap: Asking a judge model to output a score directly without generating reasoning first. Generating chain-of-thought justification drastically improves judge correlation!"
        d["examRule"] = "Exam Rule: Mitigate LLM judge bias by: 1) Swapping position order (A/B testing), 2) Requiring chain-of-thought rationale before scoring, 3) Using strict rubric anchors."

    elif sid == "core-082":
        d["intuition"] = "Retrieval metrics evaluate whether the vector search retrieved the right documents: Recall@K, Precision@K, Mean Reciprocal Rank (MRR), and NDCG."
        d["architecture"] = "Recall@K: % of relevant docs retrieved in top K. MRR: 1 / rank of first relevant doc. NDCG (Normalized Discounted Cumulative Gain): measures graded relevance and ranking order."
        d["api"] = "NDCG@K = DCG@K / IDCG@K (Ideal DCG). Measures whether highly relevant passages are placed at the very top of the retrieved list."
        d["traps"] = "Trap: Measuring only Precision@K. In RAG, high Recall@K is crucial because the LLM can filter irrelevant context, but it CANNOT answer if relevant facts were missed!"
        d["examRule"] = "Exam Rule: NDCG measures ranked document relevance order; Recall@K measures retrieval completeness; MRR measures how fast the first relevant document appears."

    elif sid == "core-083":
        d["intuition"] = "Generation metrics measure answer quality: ROUGE (n-gram recall against reference), BLEU (n-gram precision), BERTScore (semantic embedding similarity), Perplexity."
        d["architecture"] = "ROUGE-1/2/L (used for summarization); BLEU (used for machine translation); BERTScore (captures synonyms and semantic equivalence); Perplexity (model uncertainty)."
        d["api"] = "ROUGE-L measures the Longest Common Subsequence (LCS). High BERTScore indicates semantic equivalence even if literal words differ."
        d["traps"] = "Trap: Using exact string matching or simple BLEU to evaluate creative answers. Two answers can use completely different words and both be 100% correct; use BERTScore or LLM judge!"
        d["examRule"] = "Exam Rule: For summarization, use ROUGE. For translation, use BLEU. For semantic equivalence with paraphrasing, use BERTScore or LLM-as-a-judge."

    elif sid == "core-084":
        d["intuition"] = "Production feedback loops collect explicit user feedback (thumbs up/down, edits) and implicit feedback (dwell time, copy actions) to continuously expand test sets."
        d["architecture"] = "UI -> User clicks Thumbs Down -> Triggers Lambda -> Stores Query, Context, and Completion into S3 'Negative Samples' bucket -> SME reviews & adds to regression suite."
        d["api"] = "Amazon Kinesis Data Firehose -> Amazon S3 -> SageMaker Ground Truth for active learning and dataset curation."
        d["traps"] = "Trap: Discarding production failures after resolving the user ticket. Every verified failure should be curated into the automated regression test suite!"
        d["examRule"] = "Exam Rule: Capture real-world user feedback (thumbs up/down) in S3 to curate high-value golden datasets for automated regression testing."

    elif sid == "core-085":
        d["intuition"] = "Regression gates in CI/CD block deployments if a prompt revision, model version update, or retrieval change degrades accuracy or increases latency."
        d["architecture"] = "GitHub Actions / AWS CodePipeline -> Pull Request -> Runs Automated Eval Harness against 500 golden questions -> Quality >= 95% baseline? -> Pass gate!"
        d["api"] = "AWS CodeBuild executes evaluation script, reports metrics to Amazon CloudWatch, fails build if test score drops below threshold."
        d["traps"] = "Trap: Data contamination / leakage where test evaluation questions were accidentally included in few-shot prompt examples or fine-tuning datasets."
        d["examRule"] = "Exam Rule: Prevent data leakage by strictly isolating holdout test datasets from prompt few-shot examples and training datasets."

    elif sid == "core-086":
        d["intuition"] = "Canary and shadow testing validate new models in production safely before full cutover: Shadow testing mirrors production traffic without serving output to users."
        d["architecture"] = "Shadow Deployment: API Gateway / Lambda duplicates live request -> Sends to both Model A (Production) and Model B (Candidate) -> Compares quality and latency -> Discards Model B response."
        d["api"] = "Application Load Balancer weighted target groups, or Amazon CloudWatch Evidently for feature flagging and A/B experimentation."
        d["traps"] = "Trap: Doing a 100% all-at-once cutover to a new foundation model in production without shadow testing. Model behavioral shifts can cause silent production failures."
        d["examRule"] = "Exam Rule: Use Shadow Testing to evaluate a new model against live production traffic with zero impact on real end users."

    elif sid == "core-087":
        d["intuition"] = "Evaluating multi-step agents requires testing trajectory correctness: Goal Completion Rate, Path Efficiency (number of steps), and Tool Selection Accuracy."
        d["architecture"] = "Agent Eval Harness -> Simulates mock tool environments -> Evaluates: 1) Did agent call the right tool? 2) Were tool arguments correct? 3) Did agent terminate in <= 5 steps?"
        d["api"] = "Trajectory Evaluation compares the sequence of (Thought, Action, Action Input, Observation) against the optimal golden path."
        d["traps"] = "Trap: Evaluating an agent purely on its final text answer. An agent might hallucinate the answer by luck while calling wrong or dangerous tools! Inspect tool trajectories!"
        d["examRule"] = "Exam Rule: Agent evaluation must inspect the complete execution trajectory (tool selection, parameters, step efficiency), not just the final output text."

    elif sid == "core-088":
        d["intuition"] = "Evaluation reports must synthesize metrics into clear business decision artifacts: trade-off curves, radar charts, cost vs accuracy frontiers."
        d["architecture"] = "Evaluation Run -> Aggregates Metrics (Quality, Latency P95, Cost/1k tokens, Safety Pass Rate) -> Generates Comparative Pareto Frontier Dashboard."
        d["api"] = "Amazon QuickSight or Amazon Managed Grafana visualizing Bedrock evaluation metrics and CloudWatch custom metrics."
        d["traps"] = "Trap: Presenting only raw metric numbers (e.g. '0.84 NDCG') to business stakeholders without translating into business impact (task success, cost per transaction)."
        d["examRule"] = "Exam Rule: The best model for an enterprise application is on the Pareto frontier balancing quality threshold against cost and P95 latency."

    elif sid == "core-089":
        d["intuition"] = "Context overflow occurs when total tokens exceed model context limits; silent truncation silently drops the end of prompts or documents, causing severe hallucinations."
        d["architecture"] = "Detection: Compare token count against model limit before invocation -> Prune conversation history or summarize documents before calling API."
        d["api"] = "Catch `ValidationException: Input token count exceeds maximum limit`. Use CountTokens API or local tokenizer before sending payload."
        d["traps"] = "Trap: Failing to reserve tokens for model output. If prompt uses 99% of context window, model has only 1% left for output and truncates prematurely!"
        d["examRule"] = "Exam Rule: Always calculate and validate Total Input Tokens + Desired Max Output Tokens against the model context window before invocation."

    elif sid == "core-090":
        d["intuition"] = "API errors must be classified accurately: Client Errors (4xx: fix payload/auth) vs Server Errors (5xx: retry) vs Quota/Throttling (429: backoff/cross-region)."
        d["architecture"] = "400 ValidationException (bad JSON / token overflow) -> Do NOT retry without fixing payload; 403 AccessDenied -> check IAM/console; 429 Throttling -> retry with backoff; 503 ModelNotReady -> wait."
        d["api"] = "Error code matrix: `ThrottlingException`, `ModelNotReadyException`, `ModelTimeoutException`, `ResourceNotFoundException`, `ServiceQuotaExceededException`."
        d["traps"] = "Trap: Retrying 400 ValidationException or 403 AccessDenied with exponential backoff. Non-transient client errors will NEVER succeed on retry; log and fail immediately!"
        d["examRule"] = "Exam Rule: Only retry transient errors (429 ThrottlingException, 503 ModelNotReady, 500 InternalServerException) with jittered backoff. Never retry 400 or 403."

    elif sid == "core-091":
        d["intuition"] = "Prompt defects manifest as formatting non-compliance, reasoning gaps, sycophancy, or prompt injection vulnerability; diagnose with step-by-step ablation."
        d["architecture"] = "Ablation Testing: Remove few-shot examples -> does quality drop? Add explicit negative constraints -> does format improve? Use XML boundaries -> does leakage stop?"
        d["api"] = "Refine prompt: Add 'Think step by step in <scratchpad> before answering' to activate chain-of-thought reasoning; add explicit JSON schemas with examples."
        d["traps"] = "Trap: Rewriting the entire prompt when an error occurs. Perform controlled single-variable ablation to isolate which prompt clause caused the defect."
        d["examRule"] = "Exam Rule: When a model fails complex reasoning, add Chain-of-Thought (CoT) instructions or few-shot demonstration exemplars."

    elif sid == "core-092":
        d["intuition"] = "Retrieval defects occur when the vector store returns irrelevant chunks, misses critical passages, or truncates relevant sentences due to bad chunk boundaries."
        d["architecture"] = "Audit: Inspect raw retrieved chunks returned by `retrieve()`. If chunks lack key info -> adjust chunk size/overlap. If right chunks rank low -> add Re-ranking / Hybrid search."
        d["api"] = "Tune Knowledge Base: Increase chunk overlap (e.g. from 10% to 20%), switch to Hierarchical Chunking, or enable HYBRID search with Cohere Rerank."
        d["traps"] = "Trap: Changing foundation models when the answer is factually wrong. In RAG architectures, check the retrieved evidence first; 90% of failures originate in retrieval!"
        d["examRule"] = "Exam Rule: When RAG answers are inaccurate, inspect the retrieved chunks first. If relevant chunks are missing, adjust chunk size, overlap, and search type."

    elif sid == "core-093":
        d["intuition"] = "End-to-End Enterprise Secure RAG Architecture: Fully private, multi-tenant, encrypted, grounded, and observable knowledge retrieval."
        d["architecture"] = "Client -> VPC Interface Endpoint -> API Gateway -> Lambda -> Bedrock Guardrails -> Bedrock Knowledge Base (S3 CMK + OpenSearch Serverless VPC) -> Hybrid Search -> Converse API -> CloudWatch Logging."
        d["api"] = "Key components: S3 DataSource + KMS CMK + AOSS + Bedrock Knowledge Base + Contextual Grounding Guardrail + Model Invocation Logging."
        d["traps"] = "Trap: Missing the KMS decrypt permission for the Bedrock service role on the S3 bucket or vector store, causing silent sync failures."
        d["examRule"] = "Exam Rule: The reference secure RAG architecture combines VPC Endpoints, KMS CMKs, Metadata tenant filtering, Guardrails Contextual Grounding, and Invocation Logging."

    elif sid == "core-094":
        d["intuition"] = "End-to-End Action Agent Architecture: Autonomous, tool-enabled, secure, and observable agentic workflow with human-in-the-loop safeguards."
        d["architecture"] = "User -> Bedrock Agent -> Instructions + Action Group (OpenAPI in S3 + Lambda) + Knowledge Base -> ReAct Reasoning Loop -> Step Functions HITL -> Execution -> Final Answer."
        d["api"] = "boto3: create_agent, create_agent_action_group, associate_agent_knowledge_base, prepare_agent, invoke_agent."
        d["traps"] = "Trap: Forgetting that an agent requires `PrepareAgent` and an alias (e.g. `PROD`) before deployment to production."
        d["examRule"] = "Exam Rule: Production Bedrock Agent deployment requires creating an Agent Alias pointing to a prepared snapshot version."

    elif sid == "core-095":
        d["intuition"] = "Master Decision Rules for AIP-C01: Instant heuristics to eliminate distractors and select credited answers within 30 seconds."
        d["architecture"] = "Core Decision Matrix: RAG vs Fine-tuning; On-Demand vs Provisioned; Single-Region vs Cross-Region Profile; Guardrails vs Prompts; Claude Haiku vs Sonnet."
        d["api"] = "Review key quotas: 75 questions, 180 minutes, 750 pass, 29s API Gateway timeout, 5-minute prompt cache TTL, 1024 token cache minimum."
        d["traps"] = "Trap: Rushing through the question stem. The last sentence often contains the decisive constraint ('most cost-effective', 'without managing servers', 'strict in-country residency')."
        d["examRule"] = "Exam Rule: Read the last sentence of the question first to identify the primary optimization target, then eliminate options that violate hard constraints."

    return d

print("Configured Russian Doll generator.")

def main():
    core_path = ROOT / 'course/core.json'
    course_data_path = ROOT / 'course/course-data.json'
    
    with open(core_path) as f:
        core = json.load(f)
        
    with open(course_data_path) as f:
        course_data = json.load(f)
        
    quizzes = course_data.get('quizzes', [])
    print(f"Loaded {len(core)} core slides and {len(quizzes)} quizzes.")
    
    # Pre-index quizzes for fast matching
    quiz_index = []
    for q in quizzes:
        q_words = set(re.findall(r'[a-z]{4,}', q['title'].lower() + ' ' + q['answer'].lower()))
        quiz_index.append((q['id'], q.get('domain', 0), q_words, q['title']))
        
    for s in core:
        sid = s['id']
        title = s['title']
        domain = s.get('domain', 0)
        
        # 1. Attach Diagram Image
        if sid in IMAGE_MAP:
            s['image'] = IMAGE_MAP[sid]
            
        # 2. Attach Russian Doll 5-Layer Content
        s['russianDoll'] = get_russian_doll(sid, title, domain)
        
        # 3. Match practice questions
        s_words = set(re.findall(r'[a-z]{4,}', title.lower() + ' ' + s.get('lead', '').lower()))
        
        scored = []
        for qid, qdom, qwords, qtitle in quiz_index:
            # Score by keyword intersection
            overlap = len(s_words & qwords)
            if qdom == domain and overlap > 0:
                score = overlap * 2
                scored.append((score, qid, qtitle))
            elif overlap >= 2:
                scored.append((overlap, qid, qtitle))
                
        scored.sort(key=lambda x: x[0], reverse=True)
        # Top 3 questions
        s['linkedQuizzes'] = [item[1] for item in scored[:3]]
        
    print("Writing enriched core slides to course/core.json...")
    with open(core_path, 'w') as f:
        json.dump(core, f, indent=2, ensure_ascii=False)
        
    print("Successfully enriched all 95 slides!")

if __name__ == '__main__':
    main()

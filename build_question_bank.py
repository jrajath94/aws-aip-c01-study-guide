#!/usr/bin/env python3
"""Build volume-question-bank.html: 140 exam-style questions, 5 domains, mock exam."""
import random, html, re, sys

QUESTIONS = []
def q(dom, diff, fmt, topic, stem, opts, ans, *rest):
    if fmt == "multi":
        nsel, why, wrongs, trap = rest
    else:
        why, wrongs, trap = rest
        nsel = None
    QUESTIONS.append(dict(dom=dom, diff=diff, fmt=fmt, topic=topic, stem=stem,
                          opts=opts, ans=ans, why=why, wrongs=wrongs, trap=trap, nsel=nsel))

# ================= DOMAIN 1 (31%) =================
# 1.1 solution design
q("d1","easy","single","1.1 Solution design",
  "A retail company wants a chatbot that answers questions from its 2,000-page returns policy. The policy changes every quarter, and every answer must cite the exact policy section it came from. Which approach should the developer choose first?",
  ["Fine-tune a foundation model on the policy PDFs again every quarter",
   "Build a retrieval-augmented generation (RAG) solution with a Bedrock Knowledge Base over the policy documents",
   "Write one long system prompt containing the full policy text",
   "Train a custom model from scratch on company documents"],
  [1],
  "RAG is the correct first step: the knowledge is private, changes quarterly, and needs citations. A Knowledge Base retrieves the current sections at query time and RetrieveAndGenerate returns source attributions, with no retraining.",
  ["Fine-tuning bakes knowledge into weights, so every quarterly change needs a new training job, and it gives no citations. That is the expensive wrong ladder rung.",
   "A 2,000-page policy will not fit reliably in a prompt, quarterly edits mean prompt surgery, and there is no citation mechanism. Prompt engineering cannot carry changing private knowledge.",
   "Training from scratch is out of scope for this exam and wildly disproportionate: months of work and cost when a managed RAG service solves it."],
  "The trap AWS set here: fine-tuning when the scenario says documents change quarterly and answers must cite sources. That is always RAG (master trap 7).")

q("d1","easy","single","1.1 Solution design",
  "A startup CTO will approve GenAI spending only after the team proves the approach works on real data. What should the team do before buying Provisioned Throughput or building production infrastructure?",
  ["Run a proof of concept on Bedrock using on-demand inference",
   "Purchase Provisioned Throughput now to lock in capacity",
   "Build a GPU cluster on EC2 for full control",
   "Sign a long-term model hosting contract"],
  [0],
  "Bedrock on-demand inference needs no commitment, so a PoC validates feasibility, quality, and cost on real data before any capacity purchase. The blueprint calls this out explicitly: PoC first, commit later.",
  ["Buying Provisioned Throughput before validation commits hourly spend to an unproven design. PT is for steady production baselines, not experiments.",
   "An EC2 GPU cluster is maximum operational overhead for an unproven idea, the opposite of the exam's managed-first bias.",
   "A hosting contract locks in cost before the team knows which model or pattern even works."],
  "The trap AWS set here: committing to capacity (Provisioned Throughput, EC2, contracts) before a proof of concept exists.")

q("d1","medium","multi","1.1 GenAI Lens",
  "A platform team wants every product squad to build GenAI features in a consistent, reviewable way. Which TWO practices align with the Well-Architected Generative AI Lens? (Select TWO)",
  ["A shared, versioned prompt template library every squad reuses",
   "One central guardrail policy attached to all squad applications",
   "Each squad picks its own vector database, models, and prompt style",
   "Model choice based only on published benchmark leaderboards",
   "Squads deploy straight to production with no evaluation step"],
  [0,1], 2,
  "The GenAI Lens rewards standardized reusable components: shared prompt templates and one central guardrail policy mean consistent behavior, one place to audit, and design reviews against a known baseline.",
  ["Ad-hoc per-squad choices are exactly what the Lens is meant to replace; they make reviews and incident response impossible.",
   "Benchmarks ignore cost, latency, and compliance constraints, so benchmark-only selection fails the Lens review.",
   "Skipping evaluation violates the Lens outright; validation gates are a core pillar."],
  "The trap AWS set here: benchmark-only model selection and ad-hoc per-team stacks dressed up as autonomy.")

q("d1","hard","single","1.1 Behavior vs knowledge",
  "A support organization handles 3 million chat replies per month. Every reply must follow a strict 4-step format with a fixed sign-off, in the company voice. The content of each reply varies per customer, but the format never changes. Cost per reply is the top concern. What should the developer do?",
  ["Use RAG so the model can look up the format examples each time",
   "Fine-tune (distill) a small model on the format until it reproduces it reliably, then serve the small model",
   "Send every request to the largest flagship model with a long system prompt",
   "Build a rule-based template engine with no model at all"],
  [1],
  "This is baked-in behavior repeated millions of times: the format never changes, so paying flagship-model prices per reply is wasteful. Distilling the behavior into a small fine-tuned model gives consistent formatting at a fraction of the per-token cost. This is the bottom of the grounding ladder used correctly.",
  ["RAG retrieves knowledge, but the need here is behavior (format), not facts. Retrieval adds latency and cost to every call for zero benefit.",
   "The flagship model can do the format, but at 3M replies a month the per-token cost is the whole problem. Correct capability, wrong economics.",
   "A pure template engine cannot handle the variable content of each reply; the task still needs generation, just cheap generation."],
  "The trap AWS set here: reaching for RAG when the scenario needs a behavior baked into weights, and reaching for the flagship model when repetition economics demand a small distilled model (master trap 7).")

q("d1","hard","single","1.1 Architecture under constraints",
  "A travel company is designing a GenAI trip planner with four hard constraints: support 12 languages, 99.9% availability with automatic failover if a region fails, switch foundation models without code deployments, and prove value to the CTO before production spend. Which combination of steps meets ALL four constraints?",
  ["Run a Bedrock proof of concept first; use cross-region inference profiles for failover; route model calls through Lambda plus API Gateway with model identifiers in AppConfig; review the design against the Generative AI Lens",
   "Deploy an EC2 fleet behind an Application Load Balancer with hardcoded model endpoints, then go straight to production",
   "Deploy in a single region using the model with the best published benchmarks, and use CloudFormation to switch models",
   "Train a custom multilingual model and skip the proof of concept to save time"],
  [0],
  "Each constraint maps to one decision: PoC on Bedrock validates before spend; cross-region inference profiles give automatic regional failover; Lambda plus API Gateway plus AppConfig lets ops change the model identifier at runtime with no redeploy; the GenAI Lens is the exam's named standard for design reviews.",
  ["EC2 plus ALB gives availability inside one region only, so a regional outage still kills the app, and hardcoded endpoints plus skipping the PoC violate two more constraints.",
   "Single-region deployment cannot survive a regional failure, benchmarks ignore the other constraints, and CloudFormation changes are deployments, which violates no-code switching (master trap 8).",
   "Training a custom model for multilingual support ignores that Bedrock FMs already cover the languages, and skipping the PoC violates the CTO's explicit constraint."],
  "The trap AWS set here: each distractor satisfies three constraints and quietly violates one. Map every constraint to a decision before picking.")

q("d1","easy","single","1.2 Model selection",
  "A developer is comparing foundation models for a latency-sensitive classification task. Which set of factors should drive the choice?",
  ["Capability, cost per token, latency, context window, and regional availability",
   "Parameter count alone",
   "Vendor popularity",
   "Size of the model's training dataset"],
  [0],
  "Model selection is a five-way trade: can it do the task, what does it cost per token, how fast does it respond, does the context window fit the input, and is it available in the needed regions. Smaller models win on cost and latency when the task allows.",
  ["Parameter count correlates with capability but says nothing about price, speed, or regional availability.",
   "Popularity is not an engineering criterion and appears in distractors to test whether you evaluate trade-offs.",
   "Training data size is not published comparably across providers and does not decide fit for the task."],
  "The trap AWS set here: single-factor selection (benchmarks, size, popularity) instead of the full trade-off set.")

q("d1","medium","multi","1.2 Runtime model switching",
  "Operations must be able to switch the application between three foundation models without code deployments. Which THREE services form the standard pattern? (Select THREE)",
  ["AWS AppConfig", "Amazon API Gateway", "AWS Lambda", "AWS CloudFormation", "Amazon EventBridge"],
  [0,1,2], 3,
  "This is the exam's canonical trio: Lambda holds the routing logic, API Gateway exposes one stable endpoint with throttling, and AppConfig stores the model identifier as runtime configuration that ops can change without a deploy.",
  ["CloudFormation changes are deployments, which directly violates the no-redeploy requirement (master trap 8).",
   "EventBridge routes events; it does not store configuration, so it cannot serve as the model-selection store."],
  "The trap AWS set here: CloudFormation and EventBridge as the configuration store. Only AppConfig is the runtime no-redeploy mechanism (master trap 8).")

q("d1","easy","single","1.2 Resilience",
  "A foundation model the application depends on is available in only two AWS regions. The application must survive a full regional outage automatically. What should the developer use?",
  ["A Bedrock cross-region inference profile, invoking the profile ID with the geographic prefix",
   "An EC2 fleet in both regions behind a load balancer",
   "A duplicate copy of the model weights in a second region",
   "Amazon CloudFront in front of the model endpoint"],
  [0],
  "Cross-region inference profiles route requests across regions automatically when you invoke the profile ID (for example the us. prefixed ID). Traffic stays on the AWS backbone encrypted in transit, and quotas are managed at the source region.",
  ["EC2 plus a load balancer keeps GPUs warm but does not move foundation-model inference across regions; the model still only serves from its two regions.",
   "You cannot copy a Bedrock hosted model's weights to another region; availability is controlled by the inference profile, not by you.",
   "CloudFront caches HTTP content at the edge; it does not provide failover for stateful model inference calls."],
  "The trap AWS set here: EC2 plus ALB high availability, which is within-region only and never solves regional model failover.")

q("d1","hard","single","1.2 Routing mechanisms",
  "An application sends 60% simple FAQ prompts and 40% complex multi-step reasoning prompts to Bedrock. The CFO demands lower token spend without hurting answer quality on the hard prompts. Which mechanism should the developer implement?",
  ["A prompt router (model router) that sends simple prompts to a cheap small model and complex prompts to the flagship model",
   "A cross-region inference profile",
   "Provisioned Throughput on the flagship model",
   "Prompt caching on the flagship model"],
  [0],
  "This is cost-quality routing by prompt complexity, which is exactly what prompt routers (model routers) do. Simple prompts get cheap inference, hard prompts keep flagship quality, and total spend drops. Do not confuse this with availability routing or reserved capacity.",
  ["Cross-region inference profiles route for availability across regions, not for cost by complexity. Wrong mechanism for this problem.",
   "Provisioned Throughput reserves capacity and protects latency; it does not make simple prompts cheaper.",
   "Prompt caching cuts cost on repeated prefixes, but these prompts vary per question, so there is little repeated prefix to cache."],
  "The trap AWS set here: confusing inference profiles (availability), prompt routers (cost-quality), and Provisioned Throughput (capacity). Three mechanisms, three different exam answers (master trap 5).")

q("d1","medium","single","1.2 Provisioned Throughput",
  "A production application has steady, predictable traffic of 5 million tokens per day and a strict latency SLA. During testing, on-demand throttling caused timeouts. What is the most appropriate capacity choice?",
  ["Provisioned Throughput for the steady baseline, keeping on-demand for unexpected peaks",
   "On-demand only, with retries on throttle errors",
   "Batch inference for all traffic",
   "A larger context window model on-demand"],
  [0],
  "Provisioned Throughput reserves model units with an hourly commit, which removes throttling risk for the predictable baseline and protects latency. The hybrid pattern (PT for baseline, on-demand for peaks) is the exam's most-correct answer for steady-plus-spiky traffic.",
  ["Retries do not create capacity; under sustained load they add latency and still fail the SLA.",
   "Batch inference is hours-scale and non-interactive, so it cannot serve a real-time application at all.",
   "A larger context window does nothing for throttling or latency; it is a capability feature, not a capacity mechanism."],
  "The trap AWS set here: treating Provisioned Throughput as a pure cost saver. It is a latency and throughput guarantee for predictable load.")

q("d1","medium","single","1.2 Cross-region details",
  "A team adopts cross-region inference profiles. Which statement about quotas and data handling is correct?",
  ["Quotas are managed at the source region, and data stays on the AWS backbone encrypted in transit",
   "Each region in the profile gets its own independent quota pool",
   "Request payloads travel over the public internet between regions",
   "The application must copy its prompts to S3 in each region first"],
  [0],
  "With cross-region inference, quota accounting stays with the source region's quota, and AWS routes the request across regions on its private backbone with encryption in transit. No prompt copying is involved.",
  ["There is no per-region quota pool to sum; the source region's quota governs, which surprises teams that assume additive capacity.",
   "Traffic never traverses the public internet; that would violate the private-connectivity story AWS tells for Bedrock.",
   "Prompts go in the API call itself; S3 staging is a batch-inference concept, not a cross-region one."],
  "The trap AWS set here: assuming quotas add up across regions or that cross-region means public-internet transit.")

q("d1","medium","multi","1.2 Fine-tuning",
  "A team needs a small model that reliably classifies support tickets into 40 categories. They have 20,000 labeled tickets in S3. Which TWO statements about the fine-tuning approach are true? (Select TWO)",
  ["LoRA (parameter-efficient fine-tuning) trains only small weight deltas, keeping the job cheap",
   "The labeled tickets in S3 provide the supervised training data the job needs",
   "Fine-tuning requires retraining the full model from scratch",
   "Fine-tuning works with zero labeled examples",
   "RAG alone will bake the classification behavior into the weights"],
  [0,1], 2,
  "LoRA is the exam's parameter-efficient answer: only adapter weights change, so the job is fast and cheap. And supervised fine-tuning genuinely needs labeled examples, which the 20,000 tickets in S3 supply.",
  ["Full retraining from scratch is never the answer on this exam; that is the out-of-scope option.",
   "Zero examples means no supervised signal; few-shot prompting is the zero-data tool, not fine-tuning.",
   "RAG retrieves knowledge at query time; it never changes weights, so it cannot bake in behavior."],
  "The trap AWS set here: RAG as a behavior changer. RAG adds knowledge, fine-tuning changes behavior (master trap 7).")

q("d1","medium","multi","1.2 Model lifecycle",
  "A team serves a fine-tuned model from SageMaker and needs safe updates with rollback. Which TWO practices should they adopt? (Select TWO)",
  ["Version every model in the SageMaker Model Registry",
   "Deploy through an automated pipeline that can roll back to the previous version",
   "Overwrite the production endpoint in place with each new model",
   "Delete old model versions immediately after deployment",
   "Skip staging and deploy directly to production for speed"],
  [0,1], 2,
  "The registry gives immutable versioned artifacts, and a pipeline with rollback makes a bad deployment reversible in minutes. Together they are the exam's safe-lifecycle answer.",
  ["In-place overwrites destroy the rollback target; there is nothing to return to when the new model misbehaves.",
   "Deleting old versions has the same effect: no artifact, no rollback.",
   "Skipping staging trades a few minutes for unvalidated production risk, the opposite of a safe lifecycle."],
  "The trap AWS set here: in-place updates that silently destroy the ability to roll back.")

q("d1","hard","single","1.2 Graceful degradation",
  "During a peak sale, the flagship model becomes unavailable for 20 minutes. The product requirement is that the assistant must keep answering, even at reduced quality, rather than fail. Which design meets the requirement?",
  ["A Step Functions circuit breaker that detects repeated failures and fails over to a smaller cheaper model or a cached response",
   "Retry the flagship model indefinitely until it recovers",
   "Return an error page asking users to try again later",
   "Queue all requests for 20 minutes and process them when the model returns"],
  [0],
  "Graceful degradation means the system sheds quality instead of failing: the circuit breaker stops hammering the dead model and serves a smaller model or cached answers until recovery. Availability is preserved by design.",
  ["Infinite retries turn a 20-minute outage into 20 minutes of timeouts for every user, plus retry storms when the model recovers.",
   "An error page is the literal failure the requirement forbids; it meets no part of keep answering.",
   "Queueing for 20 minutes converts an availability problem into a latency catastrophe; users will not wait."],
  "The trap AWS set here: retries and queues that preserve the request but sacrifice the user experience the requirement protects.")

# 1.3 data pipelines
q("d1","easy","single","1.3 Data pipelines",
  "A pipeline must ingest 10,000 mixed files per day (PDF, PowerPoint, video) and extract key concepts into structured summaries for a knowledge base. Which service is purpose-built for this extraction?",
  ["Bedrock Data Automation", "Bedrock Guardrails", "Amazon Neptune", "AWS WAF"],
  [0],
  "Bedrock Data Automation extracts insights from documents, images, video, and audio with standard or blueprint-customized outputs, asynchronously, landing results in S3. Mixed-modality extraction at scale is its exact job.",
  ["Guardrails are safety filters; they block or mask content, they do not extract concepts. This is the exam's favorite wrong-tool trap.",
   "Neptune is a graph database for relationships, not a document extraction service.",
   "WAF filters web attacks; it has no role in a data pipeline."],
  "The trap AWS set here: Bedrock Guardrails as an extraction tool. Guardrails filter, they never extract.")

q("d1","easy","single","1.3 Data quality",
  "A data engineering team wants automated monitoring that flags malformed records in the ingestion pipeline before they reach the knowledge base. Which service provides this?",
  ["AWS Glue Data Quality", "Amazon CloudTrail", "Amazon Comprehend", "AWS Config"],
  [0],
  "Glue Data Quality continuously evaluates datasets against data-quality rules and reports anomalies, which is precisely automated malformed-record detection before downstream consumption.",
  ["CloudTrail audits API calls; it never inspects record contents.",
   "Comprehend extracts NLP insights from text; it is not a data-quality rules engine.",
   "Config tracks resource configuration drift, not data record quality."],
  "The trap AWS set here: audit and NLP services standing in for a data-quality rules engine.")

q("d1","medium","single","1.3 Wrong-tool trap",
  "A developer proposes using Bedrock Guardrails to pull invoice totals and dates out of scanned PDFs. What is wrong with this proposal?",
  ["Guardrails are safety filters; extraction needs Bedrock Data Automation or a parser, not a filter",
   "Guardrails cannot process PDF files at all",
   "Guardrails only work with Anthropic models",
   "Nothing is wrong; this is a valid use of Guardrails"],
  [0],
  "The core error is architectural: Guardrails evaluate content against safety policies (block, mask, filter). They have no extraction capability. Invoice field extraction belongs to Bedrock Data Automation or a document parser.",
  ["The file-format detail is secondary; even with perfect text input, Guardrails still could not extract fields.",
   "Guardrails work across providers, including via the standalone ApplyGuardrail API, so the model claim is false and beside the point.",
   "Accepting the proposal ships a design where the extraction step silently does nothing."],
  "The trap AWS set here is the proposal itself: Guardrails for extraction is a named exam trap. Name the tool's actual job and reject it.")

q("d1","easy","single","1.3 Kendra vs Knowledge Bases",
  "Employees want to search the company intranet and read the source documents themselves. No text generation is needed. Which service fits?",
  ["Amazon Kendra", "Bedrock Knowledge Bases", "Amazon SageMaker", "Amazon Lex"],
  [0],
  "Kendra is enterprise search: it indexes content and returns ranked documents for humans to read. When there is no generation step, search beats RAG.",
  ["Knowledge Bases exist to feed retrieved chunks into a model for generation; with no generation needed, it adds cost and complexity for nothing.",
   "SageMaker is a model building and hosting platform, not an enterprise search engine.",
   "Lex builds conversational interfaces, which is the opposite of read-the-document search."],
  "The trap AWS set here: Knowledge Bases wherever documents appear. No generation means Kendra (master trap 10).")

q("d1","easy","single","1.3 Audio input",
  "A pipeline must convert thousands of customer call recordings into text before a foundation model analyzes them. Which service does the transcription?",
  ["Amazon Transcribe", "Amazon Polly", "Amazon Comprehend", "Amazon Rekognition"],
  [0],
  "Transcribe is speech-to-text; it turns audio recordings into timestamped text that downstream models can consume.",
  ["Polly is text-to-speech, the reverse direction.",
   "Comprehend analyzes text that already exists; it cannot transcribe audio.",
   "Rekognition analyzes images and video frames, not speech."],
  "The trap AWS set here: Polly versus Transcribe direction confusion, plus Rekognition for anything with a timeline.")

q("d1","easy","multi","1.3 Input formatting",
  "A chat application must call Claude, Llama, and Titan with the same code and return strictly valid JSON. Which TWO choices support this? (Select TWO)",
  ["Use the Converse API's unified messages format across providers",
   "Define a JSON schema and request structured output via the Converse outputConfig",
   "Hand-write a different request body per provider in application code",
   "Ask the model politely in prose and hope the output parses",
   "Use InvokeModel with one shared body for all providers"],
  [0,1], 2,
  "Converse normalizes messages, system prompts, and tool config across providers so one code path serves all three models, and outputConfig with a JSON schema constrains generation to valid JSON instead of hoping.",
  ["Per-provider bodies are exactly the maintenance burden Converse exists to remove.",
   "Prose instructions produce prose-shaped output; without a schema, parsing fails intermittently.",
   "One shared InvokeModel body cannot work because each provider defines its own body format; that is the documented ValidationException trap."],
  "The trap AWS set here: one InvokeModel body for every provider. Provider bodies differ; Converse unifies.")

# 1.4 vector stores
q("d1","easy","single","1.4 Vector stores",
  "A team wants managed RAG over documents in S3 with no infrastructure to operate: ingestion, embeddings, vector storage, and retrieval in one service. What should they use?",
  ["Bedrock Knowledge Bases", "Self-managed OpenSearch on EC2", "Amazon RDS with a custom vector plugin", "A hand-rolled FAISS index on EBS"],
  [0],
  "Knowledge Bases is the managed RAG service: it syncs S3 data sources, generates embeddings, stores vectors, and exposes Retrieve and RetrieveAndGenerate, with zero cluster management.",
  ["Self-managed OpenSearch on EC2 reintroduces every operational burden the managed service removes.",
   "RDS with a custom plugin is undifferentiated heavy lifting when a managed RAG path exists.",
   "A hand-rolled FAISS index means owning scaling, durability, and sync yourself, the exam's classic custom-build distractor (master trap 13)."],
  "The trap AWS set here: custom-built vector plumbing when a managed RAG service exists (master trap 13).")

q("d1","medium","multi","1.4 Multi-tenant isolation",
  "A hotel platform serves 200 hotels. Each hotel's documents must be invisible to the other hotels, enforced by access control, not by instructions. Which TWO design choices enforce this? (Select TWO)",
  ["One knowledge base per hotel (or per account) holding only that hotel's documents",
   "IAM policies that scope each hotel's application role to its own knowledge base",
   "One shared knowledge base with a system prompt telling the model to answer only about the caller's hotel",
   "A single IAM role shared by all hotels for simplicity",
   "Storing all hotel documents in one prefix and relying on file naming"],
  [0,1], 2,
  "Isolation must be structural: separate knowledge bases per tenant plus IAM scoping each role to its own base. Access control is enforced by the platform, not requested of the model.",
  ["A prompt instruction is not access control; the model can be jailbroken or simply mistaken, and the exam explicitly rejects this pattern (master trap 6).",
   "One shared role erases the tenant boundary at the identity layer.",
   "File naming conventions are not a security boundary and are invisible to the retrieval layer."],
  "The trap AWS set here: one shared knowledge base plus prompt instructions instead of IAM-enforced isolation (master trap 6).")

q("d1","easy","single","1.4 Durable vectors",
  "A developer proposes storing the knowledge base embeddings in ElastiCache so retrieval is fast. What is wrong with this plan?",
  ["ElastiCache is an ephemeral cache, not a durable vector store; use OpenSearch Serverless, Aurora with pgvector, or S3 Vectors",
   "ElastiCache cannot store vectors at all",
   "ElastiCache is too slow for retrieval",
   "Nothing is wrong; this is best practice"],
  [0],
  "ElastiCache is in-memory and ephemeral: a failover or eviction can lose the embeddings, and it is not a managed vector index. Durable vector storage belongs in OpenSearch Serverless, Aurora pgvector, or S3 Vectors, with ElastiCache optionally in front as a cache.",
  ["ElastiCache can technically hold vector-shaped data; the problem is durability and indexing, not possibility.",
   "Speed is ElastiCache's strength; durability is its weakness, which is the actual objection.",
   "Accepting the plan risks silent data loss on the first failover."],
  "The trap AWS set here: ElastiCache as the durable vector store. Cache is not storage (master trap 9).")

q("d1","medium","single","1.4 Aurora pgvector",
  "An application already runs on Aurora PostgreSQL and now needs vector similarity search over product descriptions joined with relational inventory data. What is the most operationally efficient choice?",
  ["Enable pgvector on Aurora PostgreSQL and store embeddings alongside the relational tables",
   "Build a separate OpenSearch cluster and sync inventory nightly",
   "Store embeddings in DynamoDB",
   "Export descriptions to S3 and scan them at query time"],
  [0],
  "pgvector brings vector search into the database the team already operates, so similarity queries can join directly against inventory rows with no new cluster, no sync pipeline, and no extra service to learn.",
  ["A separate cluster plus nightly sync adds infrastructure and staleness for a workload the existing database can serve.",
   "DynamoDB is not a vector store; it holds metadata and session state, not embeddings (master trap 9).",
   "Scanning S3 at query time is orders of magnitude too slow for interactive retrieval."],
  "The trap AWS set here: DynamoDB as the vector store, and a second cluster when the current database already does the job.")

q("d1","easy","single","1.4 Freshness",
  "Company policy documents update every quarter. The RAG assistant must answer from the current version without manual intervention. What should the developer configure?",
  ["A sync schedule on the knowledge base data source",
   "A one-time ingestion of the documents",
   "Quarterly retraining of the embedding model",
   "Manual re-upload by an administrator each quarter"],
  [0],
  "Knowledge base data sources support scheduled syncs that pick up changed, added, and deleted documents automatically, so answers always reflect the current version with no human step.",
  ["One-time ingestion freezes the knowledge at load time; quarterly updates would never appear.",
   "Retraining the embedding model is unrelated to document freshness and is heavyweight overkill.",
   "Manual re-upload works until someone forgets, which is exactly the operational failure the schedule prevents."],
  "The trap AWS set here: one-time loads or manual steps where the scenario demands automated freshness.")

q("d1","easy","single","1.4 Citations",
  "A compliance team requires every generated answer to include the source documents it was drawn from. Which API meets this requirement directly?",
  ["RetrieveAndGenerate, which returns generated text with source attributions",
   "InvokeModel with a larger context window",
   "Batch inference",
   "The ApplyGuardrail API"],
  [0],
  "RetrieveAndGenerate performs retrieval plus generation in one call and returns citations to the source chunks, which is the built-in mechanism for source attribution.",
  ["A larger context window holds more text but creates no citations by itself.",
   "Batch inference changes price and latency, not attribution.",
   "ApplyGuardrail evaluates content against safety policies; it does not retrieve or cite sources."],
  "The trap AWS set here: confusing safety APIs (ApplyGuardrail) with retrieval APIs when the requirement is citations.")

q("d1","easy","single","1.4 GraphRAG",
  "A team wants RAG over a knowledge graph of product relationships (accessories, replacements, compatibility) where traversal of connections matters more than text similarity. Which vector/graph store fits?",
  ["Amazon Neptune", "Amazon ElastiCache", "Amazon S3 Standard", "Amazon DynamoDB"],
  [0],
  "Neptune is the graph database behind GraphRAG patterns: it traverses relationships (compatible-with, replaces, accessory-of) that pure vector similarity cannot express.",
  ["ElastiCache is a cache, not a durable graph store.",
   "S3 stores objects; it has no graph traversal engine.",
   "DynamoDB is key-value/document storage, not a graph database."],
  "The trap AWS set here: key-value or cache services standing in for a graph engine when relationships are the query.")

q("d1","easy","single","1.4 Filtered retrieval",
  "A support assistant must only retrieve articles for the caller's region (EU articles for EU callers). How should the developer implement this?",
  ["Tag documents with region metadata at ingestion and apply metadata filters at retrieval time",
   "Ask the model in the prompt to prefer the caller's region",
   "Create one giant prompt containing all regions",
   "Fine-tune a separate model per region"],
  [0],
  "S3 object metadata and custom attributes enable filtered retrieval: the query carries a region filter, and the vector store only searches matching documents. Filtering is enforced by the retrieval layer, not requested of the model.",
  ["Prompt preferences are not enforcement; the model can still cite the wrong region's article.",
   "One giant prompt wastes context on irrelevant regions on every call.",
   "A model per region multiplies training and serving cost for a problem metadata solves."],
  "The trap AWS set here: prompt instructions as access filtering instead of metadata filters enforced at retrieval.")

q("d1","hard","single","1.4 Enterprise scenario",
  "A hotel chain runs a legacy Java property system. Requirements: each hotel's data isolated with its own access controls, near-real-time room availability in answers, and minimal custom integration code. Which design is most correct?",
  ["One knowledge base per hotel with IAM-scoped access, direct ingestion of availability data for freshness, and IAM Identity Center permission sets for the legacy system integration",
   "One shared knowledge base for all hotels with a prompt instructing the model to respect hotel boundaries",
   "Nightly CSV exports from the Java system loaded into a single knowledge base",
   "A separate fine-tuned model per hotel"],
  [0],
  "Per-hotel knowledge bases with IAM scoping give real isolation; direct ingestion keeps availability near-real-time instead of nightly-stale; Identity Center permission sets integrate the legacy Java system with proper RBAC. Every requirement maps to a mechanism.",
  ["The shared base with prompt instructions fails isolation (master trap 6): prompts are not access control.",
   "Nightly exports make availability data up to 24 hours stale, violating near-real-time.",
   "A model per hotel is 200 training and serving bills for an isolation problem IAM solves."],
  "The trap AWS set here: the shared-KB-plus-prompt option, which looks efficient but violates the isolation requirement structurally.")

q("d1","hard","multi","1.4 Retrieval debugging",
  "A RAG application returns confident but wrong answers. The retrieved chunks look relevant at a glance. Which TWO should the developer investigate first? (Select TWO)",
  ["Whether the chunking strategy splits key context across chunk boundaries",
   "Whether the embeddings capture relevance rather than mere semantic similarity",
   "Switching to a larger generation model",
   "Raising the temperature",
   "Adding more system prompt examples"],
  [0,1], 2,
  "When chunks look relevant but answers are wrong, the failure is in retrieval, not generation: split context destroys meaning across boundaries, and similarity is not relevance. Both are fixed on the retrieval side (chunking, hybrid search, rerank).",
  ["A larger generation model cannot fix broken retrieval; it will just state the wrong answer more fluently.",
   "Temperature controls randomness, not factuality against sources.",
   "More prompt examples do not repair chunks that lost their context at ingestion."],
  "The trap AWS set here: debugging a retrieval failure by changing the generation model or temperature.")

# 1.5 retrieval mechanisms
q("d1","medium","single","1.5 Chunking",
  "A RAG system ingests legal contracts where tables and clauses must stay intact. Fixed-size chunking keeps splitting tables across chunks, breaking answers. Which chunking strategy should the developer choose?",
  ["Hierarchical chunking, so small child chunks match precisely while parent chunks preserve full context",
   "Larger fixed-size chunks with no overlap",
   "No chunking at all",
   "Random chunk boundaries"],
  [0],
  "Hierarchical chunking indexes small child chunks for precise matching but returns the parent chunk for context, so tables and clauses survive intact while retrieval stays precise. It is the exam's preferred answer for structured documents.",
  ["Larger fixed chunks still split tables, just at different boundaries; size does not respect structure.",
   "No chunking on long contracts blows past context limits and retrieval precision.",
   "Random boundaries are never a strategy; they guarantee split context."],
  "The trap AWS set here: fixed-size chunking for structured documents. Structure needs hierarchical (or semantic), not fixed.")

q("d1","easy","single","1.5 Chunking cost",
  "A FAQ bot answers from 500 short question-answer pairs. Which chunking approach is most appropriate?",
  ["Fixed-size chunking, which is cheap and predictable for simple Q and A pairs",
   "Semantic chunking, because it is always the best quality",
   "Hierarchical chunking with three levels",
   "Custom Lambda chunking with an LLM per document"],
  [0],
  "For simple FAQs, fixed-size chunking is fast, cheap, and predictable. Semantic chunking costs more at ingestion and buys little when each pair is already a natural unit.",
  ["Semantic is not always best; on simple content it adds ingestion cost without retrieval gain.",
   "Hierarchical chunking is built for structured long documents, overkill for short pairs.",
   "LLM chunking per document is the most expensive option for the simplest content."],
  "The trap AWS set here: semantic chunking presented as always best. Match the strategy to the content, not the hype.")

q("d1","medium","multi","1.5 Relevance",
  "Users complain that retrieved passages match keywords but do not actually answer the question. Which TWO changes most directly fix retrieved-but-not-relevant results? (Select TWO)",
  ["Enable hybrid search combining vector and keyword ranking",
   "Add a rerank model to reorder candidates by true relevance",
   "Switch to a larger generation model",
   "Increase the chunk size to 2,000 tokens",
   "Lower the temperature to zero"],
  [0,1], 2,
  "Hybrid search blends semantic and keyword signals so keyword-heavy queries stop drifting, and reranking scores the candidate set for actual relevance before generation. Both attack the relevance gap directly.",
  ["The generation model is downstream of retrieval; a bigger model still answers from the same irrelevant chunks.",
   "Larger chunks dilute precision further and do not fix ranking.",
   "Temperature affects output randomness, not which chunks were retrieved."],
  "The trap AWS set here: fixing a retrieval ranking problem at the generation layer.")

q("d1","easy","single","1.5 Embeddings",
  "A knowledge base covers documents in 12 languages and needs strong multilingual retrieval. Which embedding model choice fits best?",
  ["Cohere Embed, which is built for multilingual content with query versus document input types",
   "A keyword-only index with no embeddings",
   "One-hot encoding of the vocabulary",
   "Titan Text Embeddings v2 is the only allowed option"],
  [0],
  "Cohere Embed is the multilingual embedding option, and its input_type distinction (query vs document) improves cross-lingual retrieval quality. Titan v2 is the cheap default, but multilingual is Cohere's strength.",
  ["Keyword-only search fails across languages where terms do not overlap.",
   "One-hot encoding has no semantic content and cannot scale to real vocabularies.",
   "Titan v2 is a fine default but not the best fit when the requirement explicitly names 12 languages."],
  "The trap AWS set here: defaulting to Titan when the scenario explicitly demands multilingual embeddings.")

q("d1","medium","single","1.5 Query handling",
  "User queries are short and vague (for example, just refund), but the knowledge base articles use formal policy language. Retrieval quality is poor. What should the developer add?",
  ["Query expansion in a Lambda function that rewrites the vague query into richer search terms before retrieval",
   "A larger generation model",
   "More training data for the embedding model",
   "A longer system prompt"],
  [0],
  "Query expansion bridges the vocabulary gap: the Lambda step turns refund into several formal phrasings the articles actually use, so retrieval finds the right passages. This is the standard query-handling fix.",
  ["The generation model never sees better chunks, so it cannot compensate for failed retrieval.",
   "Retraining embeddings is heavyweight and unnecessary when the gap is query phrasing.",
   "A longer system prompt does not change what the retriever returns."],
  "The trap AWS set here: prompt or model changes for what is fundamentally a query-to-corpus vocabulary mismatch.")

q("d1","hard","multi","1.5 Chunking immutability",
  "A team changed the chunking strategy on their knowledge base data source from fixed-size to semantic, re-ran the sync, but retrieval behavior did not change. Which TWO steps actually apply the new strategy? (Select TWO)",
  ["Recreate the data source with the new chunking configuration, because chunking is set at creation time",
   "Run a fresh ingestion sync after recreating the data source",
   "Re-run the same sync without recreating anything",
   "Change the generation model to one that prefers semantic chunks",
   "Edit the stored chunks directly in the vector store"],
  [0,1], 2,
  "Chunking strategy is fixed when the data source is created, so the only path is recreating the data source with the new setting and then syncing to re-ingest and re-chunk everything.",
  ["Re-running sync on the old data source re-ingests with the old chunking; nothing changes.",
   "The generation model has no influence on how documents were chunked at ingestion.",
   "Hand-editing stored chunks bypasses the managed pipeline and breaks future syncs."],
  "The trap AWS set here: assuming a sync picks up a configuration that is actually immutable after creation.")

q("d1","hard","single","1.5 Debug chain",
  "A RAG assistant over 500-page technical manuals gives confident but wrong answers, especially on specification tables. Retrieved chunks look relevant, but values cited in answers do not match the source tables. What should the developer do FIRST?",
  ["Inspect whether tables are being split across chunks, then move to hierarchical chunking with advanced parsing so tables stay intact",
   "Switch the generation model to the largest available flagship model",
   "Raise the temperature to get more creative table interpretations",
   "Double the number of retrieved chunks"],
  [0],
  "The symptom pattern (relevant-looking chunks, wrong table values) points to tables split at chunk boundaries: each chunk looks fine alone but the values lose their row context. Verifying the split and switching to hierarchical chunking with advanced parsing fixes the root cause at ingestion.",
  ["A larger model reasons better but still reads the same broken chunks; retrieval is the failure point.",
   "Higher temperature increases hallucination risk on factual tables, the opposite of the fix.",
   "More broken chunks just give the model more broken context to choose from."],
  "The trap AWS set here: answering a table-integrity problem with model or retrieval-count changes instead of fixing chunk boundaries.")

q("d1","easy","single","1.5 Dimensions",
  "A team debates embedding dimensions: 1024 versus 256 for Titan Text Embeddings v2. Which statement is correct?",
  ["Higher dimensions generally improve accuracy but increase storage and cost",
   "Dimensions have no effect on accuracy or cost",
   "Lower dimensions are always more accurate",
   "Dimension choice only affects the generation model"],
  [0],
  "Dimensions are a direct trade-off: more dimensions capture finer semantic distinctions (better retrieval accuracy) but every stored vector gets bigger, raising vector-store storage and cost. Titan v2's 1024/512/256 options exist precisely for this tuning.",
  ["Ignoring the trade-off leads to either wasted spend or silently worse retrieval.",
   "Lower dimensions compress information; they do not improve accuracy.",
   "Dimensions are an embedding/index concern, independent of which model generates the answer."],
  "The trap AWS set here: treating dimension choice as free. It is a storage-versus-accuracy trade-off.")

q("d1","medium","single","1.5 MCP",
  "An agent needs a standardized way to discover and call retrieval tools and data sources without custom integration code per tool. Which interface should the developer adopt?",
  ["MCP (Model Context Protocol) clients for standardized tool and retrieval access",
   "A custom REST client per tool",
   "Direct database credentials embedded in the agent prompt",
   "Screen-scraping the tool's web UI"],
  [0],
  "MCP standardizes how agents discover and invoke tools: one protocol, many tools, no per-tool custom clients. The blueprint names MCP clients as the standardized retrieval access for agents.",
  ["Custom clients per tool multiply integration work with every new source.",
   "Credentials in prompts leak secrets into logs and model context.",
   "Screen-scraping is brittle and has no place in a production agent."],
  "The trap AWS set here: custom per-tool integration when the exam names a standard protocol.")

# 1.6 prompt engineering
q("d1","easy","single","1.6 Prompt Management",
  "Marketing changes the assistant's tone guidelines every few weeks, and every change currently requires an engineer to edit code and redeploy. What removes the redeploy from the loop?",
  ["Bedrock Prompt Management: store prompts as versioned resources with variables, editable without code changes",
   "Hardcode the new tone into the system prompt each time",
   "Fine-tune the model on the new tone each time",
   "Email the tone guidelines to the developers"],
  [0],
  "Prompt Management stores prompts as managed resources with {{variable}} placeholders and immutable versions, so non-engineers can update wording and the application picks up the new version with no deployment. There is no extra charge beyond model tokens.",
  ["Hardcoding keeps the engineer-and-redeploy bottleneck the scenario wants to remove.",
   "Fine-tuning for a tone tweak is wildly disproportionate in time and cost.",
   "Emailing guidelines changes nothing in the running system."],
  "The trap AWS set here: hardcoding prompts in application code when the scenario demands frequent non-engineer changes.")

q("d1","medium","multi","1.6 Variants vs versions",
  "A team wants to A/B test two prompt wordings, then lock the winner as the release everyone uses. Which TWO statements about Prompt Management are true? (Select TWO)",
  ["Variants allow comparing prompt wordings side by side for A/B testing",
   "Versions are immutable snapshots, so the winning wording becomes a locked release",
   "Variants are immutable releases",
   "Versions are for A/B comparison",
   "Drafts cannot be tested before versioning"],
  [0,1], 2,
  "Variants exist for comparison (A/B testing wordings), and versions are immutable snapshots: draft, test, then save the winner as a version that cannot silently change under you.",
  ["Variants are the comparison mechanism, not the release mechanism.",
   "Versions are the release mechanism, not the comparison mechanism. The exam swaps these two deliberately.",
   "Drafts can be tested in the console before saving a version; that is the normal workflow."],
  "The trap AWS set here: swapping variants (A/B) with versions (immutable releases).")

q("d1","medium","single","1.6 Flows",
  "A business analyst (not an engineer) must build a fixed three-step prompt chain: summarize a ticket, classify it, then draft a reply, with conditional branching when the ticket is urgent. No code changes are allowed. Which service fits?",
  ["Bedrock Prompt Flows, the visual no-code builder for multi-step prompt workflows with branching",
   "Bedrock Agents, for autonomous tool-using reasoning",
   "AWS Step Functions with Lambda functions",
   "Amazon EventBridge rules"],
  [0],
  "Prompt Flows (Flows) is the visual builder for fixed multi-step GenAI workflows: prompt, knowledge base, and Lambda nodes with conditional branching and a test panel, usable without code. Fixed deterministic prompt chains are its exact use case.",
  ["Agents are for dynamic autonomous reasoning with tools, not fixed deterministic sequences; the exam explicitly warns against agents for fixed chains.",
   "Step Functions orchestrates general workflows with approvals and timeouts, but it is code-centric, not the no-code visual builder the analyst needs.",
   "EventBridge routes events; it does not build prompt chains."],
  "The trap AWS set here: Bedrock Agents for a fixed deterministic prompt chain. Agents are for dynamic tool use; Flows are for fixed sequences.")

q("d1","easy","single","1.6 Structured output",
  "An application needs strictly valid JSON from Claude, Llama, and Titan using one code path. Which approach is most reliable?",
  ["Converse API with outputConfig and a JSON schema",
   "Asking nicely in the system prompt and parsing with a try/except",
   "InvokeModel with a shared body for all three providers",
   "Setting temperature to zero and hoping"],
  [0],
  "Converse outputConfig with a JSON schema constrains generation to schema-valid JSON across providers, in one unified code path. Schema beats hope.",
  ["Try/except parsing accepts intermittent failures as normal; the schema prevents them.",
   "A shared InvokeModel body is invalid: each provider defines its own body format.",
   "Temperature zero reduces randomness but never guarantees valid JSON structure."],
  "The trap AWS set here: prose instructions plus parsing instead of a real schema constraint.")

q("d1","hard","multi","1.6 Prompt governance",
  "A company manages 15 production prompts. Compliance requires an approval before any prompt change goes live and a full audit trail of who changed what. Which THREE controls satisfy this? (Select THREE)",
  ["Prompt Management versions, so every release is an immutable snapshot",
   "An approval workflow (for example Step Functions) gating version publication",
   "CloudTrail logging of prompt management API calls for the audit trail",
   "Editing prompts directly in application code",
   "Sharing one IAM user across the marketing team"],
  [0,1,2], 3,
  "Versions make each release immutable and referenceable, the approval workflow enforces the human gate before publication, and CloudTrail records every prompt API call with identity and time for the audit trail.",
  ["Code edits bypass versioning, approval, and audit all at once.",
   "A shared IAM user destroys attribution; the audit trail cannot say who did what."],
  "The trap AWS set here: code edits and shared credentials that silently erase governance.")

# ================= DOMAIN 2 (26%) =================
# 2.1 agents
q("d2","easy","single","2.1 Agent updates",
  "A team updated a Bedrock Agent's instructions and uses an alias for production traffic, but production behavior did not change. What is the most likely cause?",
  ["The alias still points to the old agent version; create a new version and point the alias at it",
   "The foundation model needs retraining",
   "The IAM role needs more permissions",
   "Aliases update automatically within 24 hours"],
  [0],
  "Bedrock Agent aliases pin to a specific prepared version. Editing the draft changes nothing for alias traffic until you prepare the agent and create a new version, then move the alias. The draft/prepare/version/alias lifecycle is the whole answer.",
  ["Retraining the model is unrelated to agent configuration routing.",
   "Permissions would cause access errors, not silently stale behavior.",
   "Aliases never move on their own; that assumption is how stale production agents happen."],
  "The trap AWS set here: assuming edits flow to production automatically. Aliases pin versions; move them explicitly.")

q("d2","easy","single","2.1 Action groups",
  "A Bedrock Agent must look up order status from an internal REST API during conversations. How should the developer give the agent access to that API?",
  ["Define an action group with the API's OpenAPI schema (or a Lambda executor) so the agent can call it as a tool",
   "Paste the API documentation into the agent's instructions",
   "Give the agent the database password in its system prompt",
   "Have the agent ask the user to call the API manually"],
  [0],
  "Action groups are how agents get tools: an OpenAPI schema (or Lambda executor function) describes the API, and the agent invokes it through the actionGroupExecutor at runtime with proper IAM scoping.",
  ["Documentation in instructions teaches nothing executable; the agent cannot make HTTP calls from prose.",
   "Passwords in prompts leak into logs and traces; tools use IAM roles, not pasted secrets.",
   "Manual user calls defeat the purpose of an autonomous agent."],
  "The trap AWS set here: prose in instructions standing in for a real tool binding.")

q("d2","medium","single","2.1 Multi-agent",
  "Three specialist Bedrock Agents (tax, investment, estate planning) must collaborate on a client plan under one supervisor agent. How should inter-agent communication be configured?",
  ["Use the built-in supervisor/collaborator multi-agent mechanism, with collaborators prepared and aliased",
   "Wire the agents together with action groups defined in the supervisor's instructions",
   "Chain them with SQS queues and Lambda functions",
   "Merge all three into one giant prompt"],
  [0],
  "Bedrock's multi-agent collaboration is a built-in supervisor/collaborator pattern: the supervisor delegates to collaborator agents, which must be prepared and aliased, with conversation history relay between them. Action groups are for tools, not for agent-to-agent delegation.",
  ["Action groups invoke Lambda or APIs; describing agents as action groups in instructions is the exam's named misconception.",
   "SQS plus Lambda rebuilds orchestration the platform already provides, adding latency and state bugs.",
   "One giant prompt loses specialist boundaries, explodes context, and cannot use per-domain tools cleanly."],
  "The trap AWS set here: action groups for inter-agent communication. The service uses supervisor/collaborator, not action groups.")

q("d2","medium","single","2.1 Agent memory",
  "An agent must remember customer context across sessions for several weeks. Where should the developer store this long-term memory?",
  ["Amazon DynamoDB", "Amazon S3", "The agent's system prompt", "ElastiCache only"],
  [0],
  "DynamoDB gives millisecond key-value access with fine-grained per-user partitioning, which matches session memory access patterns: frequent small reads/writes keyed by user or session. Weeks-long agent memory is the textbook DynamoDB case.",
  ["S3 has high per-request latency and no fast key lookups; it is for objects, not conversational state (master trap 9).",
   "The system prompt cannot grow unboundedly and is not a data store.",
   "ElastiCache alone is ephemeral; memory that must survive weeks needs durable storage, with cache optionally in front."],
  "The trap AWS set here: S3 for conversation memory. Latency and access patterns say DynamoDB (master trap 9).")

q("d2","easy","single","2.1 Human in the loop",
  "An agent can initiate refunds, but company policy requires a human to approve any refund over $500 before it executes. How should the developer enforce this?",
  ["A Step Functions workflow with a callback/task token that pauses the agent until a human approves or rejects",
   "A longer system prompt asking the agent to be careful",
   "Letting the agent approve its own refunds and logging the decision",
   "Disabling refunds entirely"],
  [0],
  "Step Functions task tokens implement true human-in-the-loop: the workflow pauses, notifies the approver, and only resumes the agent's tool call on explicit approval. The pause is structural, not requested of the model.",
  ["A prompt request is not enforcement; the agent can still act, especially under jailbreak pressure.",
   "Self-approval by the agent is no control at all.",
   "Disabling refunds fails the business requirement instead of controlling it."],
  "The trap AWS set here: prompt instructions as an approval control. Approvals must pause the workflow structurally.")

q("d2","medium","single","2.1 Orchestration limits",
  "An agent workflow runs for up to 45 minutes: it calls tools, waits for a human approval, then calls more tools. A developer proposes implementing the whole orchestration inside one Lambda function. Why is this wrong?",
  ["Lambda has a 15-minute maximum execution time; Step Functions is built for long workflows with waits and approvals",
   "Lambda cannot call Bedrock APIs",
   "Lambda is too expensive for 45 minutes",
   "Step Functions cannot wait for humans"],
  [0],
  "Lambda's hard 15-minute limit kills any 45-minute orchestration, and waits burn billed duration. Step Functions is designed for exactly this: durable state, waits, human task tokens, and stopping conditions across hours or days.",
  ["Lambda calls Bedrock APIs fine; the limit is duration, not capability.",
   "Cost is secondary; the design is impossible regardless of price.",
   "Waiting for humans via task tokens is one of Step Functions' signature features."],
  "The trap AWS set here: Lambda for long-running orchestration with waits. That is always Step Functions (master trap 1).")

q("d2","medium","multi","2.1 Agent frameworks",
  "A team is evaluating the exam-named open-source agent frameworks. Which TWO statements are true? (Select TWO)",
  ["Strands Agents is a code-first open-source framework for building agents",
   "AWS Agent Squad orchestrates multiple agents working together",
   "Strands Agents replaces IAM for agent security",
   "Agent Squad is a Bedrock Agent alias type",
   "Both frameworks eliminate the need for human approvals"],
  [0,1], 2,
  "Strands is the code-first agent-building framework and Agent Squad is the multi-agent orchestration layer; both are named in the exam guide as the open-source path, complementing Bedrock Agents.",
  ["No framework replaces IAM; agent tool calls still need least-privilege roles.",
   "Agent Squad is an orchestration framework, not an alias type; aliases belong to Bedrock Agents versioning.",
   "Approvals are a safety requirement no framework waives."],
  "The trap AWS set here: framework names confused with Bedrock Agent versioning concepts.")

q("d2","easy","single","2.1 MCP hosting",
  "A team exposes lightweight utility tools (date math, unit conversion) to agents via MCP servers. Where should these lightweight MCP servers run?",
  ["AWS Lambda", "A dedicated EC2 fleet", "Amazon RDS", "On-premises servers only"],
  [0],
  "Lightweight, short-lived tool executions map perfectly to Lambda: no servers to manage, scale-to-zero, pay per call. The blueprint's guidance is explicit: Lambda for lightweight MCP servers, ECS for complex long-running ones.",
  ["A dedicated EC2 fleet for trivial tools is idle capacity you pay for around the clock.",
   "RDS is a database, not a tool-execution host.",
   "On-premises adds network hops and ops burden for stateless utilities."],
  "The trap AWS set here: heavyweight hosting for lightweight tools. Match the host to the workload.")

q("d2","medium","single","2.1 AgentCore",
  "A team built agents on Bedrock Agents but now wants to use an open-source agent framework of their choice while keeping AWS-managed hosting, memory, and observability. Which service is the migration path?",
  ["Amazon Bedrock AgentCore, with Runtime for hosting any-framework agents plus Gateway, Memory, Identity, and Observability",
   "Amazon Lex",
   "AWS Batch",
   "Amazon ECS with no agent services"],
  [0],
  "AgentCore is the framework-freedom path: Runtime hosts agents built with any framework behind a standard invocations interface, while Gateway, Memory, Identity, and Observability provide the managed pieces Bedrock Agents previously bundled.",
  ["Lex is a conversational UI builder, not an agent hosting runtime.",
   "Batch runs batch compute jobs, not interactive agents.",
   "Raw ECS gives containers but none of the agent-specific managed services."],
  "The trap AWS set here: Lex as the agent answer. Lex is chat UI; AgentCore is agent infrastructure.")

q("d2","hard","single","2.1 Full agent scenario",
  "A wealth-management firm needs specialist agents for tax, investment, and estate planning that collaborate on client plans, use internal tools, remember client context for weeks, and require human approval for any action over $100,000. Which combination is most correct?",
  ["Strands Agents plus Agent Squad for orchestration, MCP for tool access, DynamoDB for weeks-long memory, and Step Functions task tokens for the approval workflow",
   "One giant prompt containing all three specialties and tool documentation",
   "Amazon Lex bots with S3-stored memory and no approvals",
   "A single Bedrock Agent with all tools and approvals requested in prose"],
  [0],
  "Each requirement maps to a mechanism: Strands plus Agent Squad for multi-agent orchestration, MCP for standardized tool access, DynamoDB for durable weeks-long memory with the right access pattern, and Step Functions task tokens for structural human approval. Nothing is left to prompt goodwill.",
  ["One giant prompt cannot hold three specialties plus tools plus weeks of memory, and prose approvals are not enforcement.",
   "Lex is conversational UI, not autonomous orchestration; S3 is wrong for memory access patterns; no approvals violates policy.",
   "A single agent with prose approvals fails the approval requirement structurally and overloads one agent's context."],
  "The trap AWS set here: Lex for orchestration and S3 for memory, plus prose where structure is required.")

q("d2","medium","multi","2.1 Agent safeguards",
  "An agent with broad tool access goes to production. Which TWO safeguards should the developer implement? (Select TWO)",
  ["Step Functions stopping conditions that bound iterations, cost, and time",
   "IAM roles with resource boundaries scoping exactly which tools and data the agent can touch",
   "Unlimited retries on every tool call",
   "No timeouts, so the agent always finishes",
   "Full administrative credentials for maximum tool compatibility"],
  [0,1], 2,
  "Stopping conditions bound the blast radius of runaway reasoning loops, and IAM resource boundaries enforce least privilege on every tool call. Both are structural controls that work even when the model misbehaves.",
  ["Unlimited retries turn one bad tool call into an infinite loop billed to you.",
   "No timeouts guarantee hung executions instead of graceful failure.",
   "Admin credentials give a compromised or confused agent the keys to everything."],
  "The trap AWS set here: operational unboundedness (no limits, no timeouts, admin creds) dressed as reliability.")

q("d2","hard","single","2.1 Tracing",
  "An agent's answers are sometimes wrong and the team cannot tell whether the failure is in reasoning, tool selection, or tool results. What should they enable to diagnose this?",
  ["Agent trace (enableTrace on invoke_agent) to inspect the reasoning path, tool calls, and observations step by step",
   "A higher temperature for more diverse reasoning",
   "A larger context window",
   "More CloudTrail log retention"],
  [0],
  "Tracing exposes the agent's internal loop: the model's reasoning, which action group it chose, the exact tool input, and the observation returned. That decomposes wrong answer into reasoning failure vs tool failure vs bad tool data.",
  ["Temperature changes output randomness; it does not reveal the reasoning path.",
   "A larger context window holds more history but explains nothing about the failure.",
   "CloudTrail shows API calls were made, not why the agent chose them or what it concluded."],
  "The trap AWS set here: CloudTrail as a reasoning debugger. Trail audits calls; traces reveal reasoning.")

# 2.2 deployment
q("d2","easy","single","2.2 Spiky traffic",
  "A GenAI feature gets unpredictable bursts of traffic: quiet for hours, then thousands of requests in minutes. Which invocation pattern fits best?",
  ["AWS Lambda invoking the model on demand",
   "Provisioned Throughput sized for the peak burst",
   "A fixed EC2 fleet sized for peak",
   "Batch inference"],
  [0],
  "Lambda scales to zero and bursts on demand, so spiky irregular traffic pays only for what it uses. Reserved capacity for unpredictable peaks means paying for idle most of the time.",
  ["Provisioned Throughput commits hourly spend; sizing it for rare peaks wastes money the other 95% of the time.",
   "A fixed EC2 fleet for peak is the same idle-capacity waste with added server management.",
   "Batch inference is hours-scale and non-interactive; it cannot serve bursty real-time requests."],
  "The trap AWS set here: Provisioned Throughput as the answer to spiky traffic. PT is for predictable baselines, not bursts.")

q("d2","hard","single","2.2 Hybrid deployment",
  "An application serves 2 million requests per day as a steady baseline, with 10x spikes every Friday evening and a sub-3-second latency requirement. Which deployment is most correct?",
  ["Provisioned Throughput covering the steady baseline, with on-demand invocations via Lambda absorbing the Friday spikes",
   "Provisioned Throughput sized for the 10x Friday peak, running all week",
   "On-demand only for everything, with client-side retries",
   "SageMaker Serverless Inference for the full workload"],
  [0],
  "The hybrid pattern matches cost to shape: PT's hourly commit covers the predictable baseline with latency guarantees, while on-demand elasticity absorbs spikes without paying for peak capacity all week. This is the exam's signature most-correct deployment answer.",
  ["Sizing PT for the peak pays peak prices during every quiet hour of the week.",
   "Pure on-demand risks throttling exactly when the Friday spike needs guaranteed latency.",
   "Serverless Inference is for intermittent traffic with cold-start tolerance, not sustained high-throughput with a 3-second SLA."],
  "The trap AWS set here: single-mode answers (all PT, all on-demand) when the traffic shape demands a hybrid.")

q("d2","easy","single","2.2 Batch",
  "A company generates 50,000 product-description summaries every night. Nobody reads them until morning. What is the cheapest correct inference option?",
  ["Batch inference, writing results to S3 hours later at roughly half the on-demand price",
   "Real-time Converse calls as each description arrives",
   "Provisioned Throughput for the nightly job",
   "Streaming every summary to a dashboard"],
  [0],
  "Batch inference is built for non-interactive workloads: S3 input, S3 output, hours-scale latency, about 50% cheaper than on-demand. Overnight summaries are the textbook case.",
  ["Real-time calls pay full price for latency nobody needs.",
   "PT commits hourly capacity for a job that runs once a night; the commit math never works.",
   "Streaming optimizes perceived latency for humans watching; nobody watches at 3 AM."],
  "The trap AWS set here: real-time or reserved capacity for a workload whose latency requirement is literally tomorrow.")

q("d2","medium","single","2.2 Custom models",
  "A team fine-tuned their own model and must serve it on AWS with autoscaling real-time endpoints under their full control. Which service should host it?",
  ["Amazon SageMaker AI real-time endpoints",
   "Bedrock on-demand for any custom model",
   "AWS Lambda with the model weights bundled",
   "Amazon CloudFront"],
  [0],
  "SageMaker real-time endpoints host self-hosted and fine-tuned models with autoscaling, instance choice, and deployment control. That is the custom-model serving path on this exam.",
  ["Bedrock serves its own hosted and imported models; an arbitrary self-hosted fine-tune needs SageMaker (or import), not plain on-demand.",
   "Lambda cannot hold multi-gigabyte model weights in memory or serve them with GPU inference.",
   "CloudFront is a CDN; it does not run model inference."],
  "The trap AWS set here: Bedrock on-demand as the universal serving answer. Self-hosted models mean SageMaker endpoints.")

q("d2","medium","multi","2.2 Model cascade",
  "A team implements a model cascade to cut costs. Which TWO statements describe a correct cascade? (Select TWO)",
  ["Simple queries go to a small cheap model first",
   "Low-confidence answers escalate to the larger flagship model",
   "Every query goes to the flagship model for safety",
   "The small model handles everything with no escalation path",
   "Cascade means running both models on every query"],
  [0,1], 2,
  "A cascade is a cost-quality router: the cheap model answers what it can confidently, and only uncertain or complex queries pay flagship prices. The confidence-gated escalation is what makes it a cascade rather than just a small model.",
  ["Always-flagship is the spend the cascade exists to cut.",
   "No escalation path means hard queries get bad answers with no recovery.",
   "Running both models every time doubles cost instead of cutting it."],
  "The trap AWS set here: cascade without the confidence-gated escalation, which is just a small model with extra steps.")

q("d2","easy","single","2.2 Serverless inference",
  "A SageMaker endpoint serves an internal tool used a few times per hour with no strict latency SLA. Which inference option fits, and what is its key limitation?",
  ["SageMaker Serverless Inference; it is wrong for sustained high-throughput or strict latency SLAs because of cold starts",
   "SageMaker Serverless Inference; it guarantees sub-second latency at any scale",
   "Real-time endpoints; they scale to zero automatically",
   "Batch transform; it is interactive"],
  [0],
  "Serverless Inference scales to zero for intermittent traffic, which fits a few-requests-per-hour tool. Its cold starts make it the wrong choice for sustained throughput or strict latency, which is exactly what the exam tests.",
  ["No serverless option guarantees sub-second latency at scale; cold starts are the documented trade-off.",
   "Real-time endpoints do not scale to zero; they bill for running instances.",
   "Batch transform is non-interactive by definition."],
  "The trap AWS set here: Serverless Inference for sustained high-throughput. Intermittent traffic only.")

q("d2","hard","single","2.2 Async inference",
  "A media company runs inference jobs that take 30 to 60 minutes each: generating long-form video summaries. No user waits on the request; a notification fires when each job completes. Which SageMaker option fits?",
  ["SageMaker Async Inference, which queues long-running requests and notifies on completion",
   "SageMaker real-time endpoints with 60-second timeouts",
   "Lambda invoking the model synchronously",
   "Batch inference on Bedrock with streaming"],
  [0],
  "Async Inference exists for jobs that run minutes to an hour: it queues the request, processes it, and delivers the result to S3 with an SNS notification. The 30-60 minute duration rules out synchronous paths entirely.",
  ["Real-time endpoints cap request handling far below 60 minutes; the job would be killed mid-run.",
   "Lambda's 15-minute limit cannot host a 60-minute synchronous call.",
   "Bedrock batch inference is a different service path, and streaming is meaningless for a non-interactive hour-long job."],
  "The trap AWS set here: synchronous serving for hour-long jobs. Duration dictates async.")

# 2.3 enterprise integration
q("d2","easy","single","2.3 Event-driven",
  "When a new order is placed, a GenAI service should generate a confirmation summary without the ordering system waiting for it. Which integration pattern provides this loose coupling?",
  ["Publish an order event to Amazon EventBridge and let the GenAI service consume it asynchronously",
   "Make the ordering system call the GenAI API synchronously and wait",
   "Share a database table between the two systems",
   "Email the order details to the GenAI team"],
  [0],
  "EventBridge decouples the systems: the order service publishes an event and moves on, while the GenAI consumer processes it independently, with retries and scaling handled by the event bus.",
  ["Synchronous calls couple availability and latency; a slow model blocks checkout.",
   "A shared table couples schemas and creates hidden dependencies between teams.",
   "Email is not an integration pattern; it is an operations incident waiting to happen."],
  "The trap AWS set here: synchronous calls where the scenario explicitly says the caller must not wait.")

q("d2","medium","single","2.3 Data residency",
  "A bank must process customer data with a GenAI application, but regulations require the data to stay on premises. Which AWS option addresses this?",
  ["AWS Outposts, running AWS infrastructure on premises for data residency",
   "A public Bedrock endpoint with client-side encryption",
   "Amazon CloudFront with edge caching",
   "Storing the data in a public S3 bucket"],
  [0],
  "Outposts extends AWS infrastructure into the customer's data center, so regulated workloads run on AWS services while data never leaves the premises. Data residency is its defining use case.",
  ["A public endpoint still sends data to AWS regions, violating the on-premises requirement regardless of encryption.",
   "CloudFront caches content at edge locations worldwide, the opposite of residency control.",
   "A public bucket is a breach, not a compliance strategy."],
  "The trap AWS set here: encryption as a residency answer. Residency is about where data lives, not how it is scrambled.")

q("d2","medium","single","2.3 GenAI gateway",
  "Fifty engineering teams each call Bedrock directly with their own keys, prompts, and logging. Security wants centralized policy enforcement, cost attribution, and observability. What should the company build?",
  ["A centralized GenAI gateway: one abstraction layer for model access with policy control, logging, and cost tracking",
   "A shared spreadsheet of API keys",
   "Fifty separate AWS accounts with no central view",
   "Direct model access with a request in the wiki to be careful"],
  [0],
  "A GenAI gateway centralizes model access behind one layer that enforces guardrail and IAM policy, emits uniform logs, and attributes token spend per team. It converts fifty snowflakes into one governed surface.",
  ["A spreadsheet of keys is a credential leak with extra steps.",
   "Separate accounts without central governance multiply the problem instead of solving it.",
   "Wiki requests are not enforcement; nothing stops a team from ignoring them."],
  "The trap AWS set here: decentralized direct access dressed as team autonomy when the requirement is governance.")

q("d2","easy","single","2.3 CI/CD",
  "A team ships a GenAI application weekly. Which pipeline practice matches the exam's enterprise guidance?",
  ["CodePipeline and CodeBuild with automated tests, security scans, and rollback on failure",
   "Manual zip uploads to production on Fridays",
   "Deploying from a developer's laptop",
   "Skipping tests because prompts cannot be tested"],
  [0],
  "The standard enterprise pattern applies to GenAI too: pipeline-driven builds, automated evaluation and security gates, and rollback when a stage fails. Prompts are testable artifacts with regression suites.",
  ["Manual uploads are unrepeatable and unauditable.",
   "Laptop deploys bypass every control the pipeline exists to provide.",
   "Prompts absolutely can be tested: regression suites over golden datasets are a named exam practice."],
  "The trap AWS set here: prompts cannot be tested. They can, with golden datasets and regression gates.")

q("d2","medium","multi","2.3 Secure access",
  "An enterprise rolls out GenAI to 2,000 employees. Which TWO controls belong in the access design? (Select TWO)",
  ["IAM Identity Center permission sets giving each team least-privilege access to specific models and knowledge bases",
   "Least-privilege IAM policies on every Bedrock, knowledge base, and agent API call",
   "One shared IAM user whose credentials are emailed to all employees",
   "Administrator access for every employee to avoid permission tickets",
   "Hardcoded access keys in the frontend JavaScript"],
  [0,1], 2,
  "Identity Center provides federated RBAC so each team gets exactly the models and data it needs, and least-privilege policies on FM APIs enforce that boundary at every call. Identity plus policy is the complete access story.",
  ["A shared user destroys attribution and cannot be scoped per team.",
   "Admin for everyone is the opposite of least privilege and a compliance failure.",
   "Frontend keys are extractable by anyone with a browser; they are never an access design."],
  "The trap AWS set here: shared credentials or admin-for-all as simplicity. Least privilege is non-negotiable.")

q("d2","hard","single","2.3 Wrong-plane trap",
  "A developer proposes using CloudTrail to stream real-time inventory changes from the legacy database into the GenAI application. What is wrong with this proposal?",
  ["CloudTrail records AWS API activity for auditing; it is not a data pipeline and cannot stream database changes",
   "CloudTrail is too expensive for this volume",
   "CloudTrail cannot be enabled on databases",
   "Nothing is wrong; this is a standard pattern"],
  [0],
  "CloudTrail's job is audit: who called which AWS API and when. It never sees inside database rows and has no streaming data-plane role. Real-time data sync needs CDC, DMS, or event publishing, not an audit log.",
  ["Cost is irrelevant; the service fundamentally cannot do the job.",
   "The enablement detail misses the point: even where enabled, Trail carries API events, not row changes.",
   "Accepting the proposal builds a pipeline on a service that will never emit the needed events."],
  "The trap AWS set here is the proposal itself: CloudTrail for real-time data sync. Audit is not a data plane (master trap 14).")

# 2.4 FM APIs
q("d2","easy","single","2.4 Converse",
  "An application must call Claude, Llama, and Titan with tool use, using identical code for all three. Which API should the developer use?",
  ["The Converse API (Converse/ConverseStream)",
   "InvokeModel with one shared request body",
   "A separate SDK per provider",
   "Batch inference"],
  [0],
  "Converse provides a unified messages format, toolConfig, guardrailConfig, and inferenceConfig across providers, so one code path serves Claude, Llama, and Titan including tool use.",
  ["One shared InvokeModel body is invalid because each provider defines its own body schema.",
   "Per-provider SDKs are the maintenance burden Converse eliminates.",
   "Batch inference is non-interactive S3-based processing, not a real-time unified API."],
  "The trap AWS set here: one InvokeModel body for all providers. Converse unifies; InvokeModel specializes.")

q("d2","easy","single","2.4 Embeddings",
  "An application needs text embeddings for its vector store. Which API supports this?",
  ["InvokeModel, because the Converse API is text-generation only and cannot produce embeddings",
   "Converse, because it supports every model feature",
   "ApplyGuardrail",
   "ConverseStream"],
  [0],
  "Embeddings are a provider-specific InvokeModel operation (for example, calling the Titan or Cohere embedding model). Converse is text generation only, so it has no embedding path.",
  ["Converse cannot do embeddings no matter how it is configured; this is a documented API boundary.",
   "ApplyGuardrail evaluates safety; it generates nothing.",
   "Streaming changes delivery, not capability; ConverseStream still cannot embed."],
  "The trap AWS set here: Converse for embeddings. Generation API versus embedding operation, know the line.")

q("d2","medium","single","2.4 Provider specifics",
  "A developer needs a Claude-specific parameter that the Converse API does not natively expose. Which approach is correct?",
  ["Use InvokeModel with Claude's provider-specific request body including the required fields",
   "Give up; the parameter cannot be used on Bedrock",
   "Put the parameter in the system prompt as text",
   "Switch to a different cloud provider"],
  [0],
  "InvokeModel is the provider-specific path: it accepts each provider's native body (for Claude, fields like anthropic_version and max_tokens), which is where provider-exotic parameters live. Converse also offers additionalModelRequestFields as an escape hatch, but InvokeModel is the direct answer.",
  ["The parameter is fully usable; Bedrock does not hide provider features.",
   "Prose in the system prompt does not set API parameters.",
   "Switching clouds over one parameter is disproportionate when the API already supports it."],
  "The trap AWS set here: assuming Converse covers everything. Provider-exotic features mean InvokeModel.")

q("d2","medium","single","2.4 Streaming",
  "A chat application must show tokens to the user as they are generated, minimizing perceived latency. Which combination delivers this?",
  ["ConverseStream (or InvokeModelWithResponseStream) with WebSockets or server-sent events to the browser",
   "Batch inference with hourly polling",
   "API Gateway with default settings and a 29-second integration timeout for a 5-minute stream",
   "Emailing the completed response"],
  [0],
  "ConverseStream emits tokens incrementally, and WebSockets or SSE carry them to the browser as they arrive. API Gateway has payload and timeout limits, so long streams go over WebSockets or direct streaming instead.",
  ["Batch is hours-scale; it cannot stream anything.",
   "API Gateway's timeouts will cut a long stream mid-response; that is why the exam pushes WebSockets for streaming.",
   "Email is not a real-time UX pattern."],
  "The trap AWS set here: API Gateway default limits silently killing long streams. Stream over WebSockets/SSE.")

q("d2","hard","single","2.4 PT routing bug",
  "A company bought Provisioned Throughput for Claude. The application still gets throttled at peak, and CloudWatch shows all invocations hitting the on-demand model ID. Code review finds: invoke_model(modelId='anthropic.claude-...'). What is the fix?",
  ["Invoke the provisioned model identifier (the provisioned model ARN), not the base model ID",
   "Buy more Provisioned Throughput model units",
   "Increase the retry count in the SDK",
   "Switch to a different region"],
  [0],
  "The code bypasses the reservation entirely: PT capacity only applies when invocations target the provisioned model ARN/ID. Calling the base model ID sends traffic to the shared on-demand pool, so throttling persists no matter how much PT was purchased. Routing, not capacity, is the bug.",
  ["More units cannot help traffic that never routes to the provisioned model; this is the exam's classic capacity-versus-routing trap (master trap 11).",
   "Retries on the wrong target still hit the on-demand pool.",
   "Regions do not fix a routing bug in the code."],
  "The trap AWS set here: increasing PT units when the code never routes to the provisioned model. Check the target first (master trap 11).")

q("d2","medium","multi","2.4 ApplyGuardrail",
  "A team uses a non-Bedrock model but wants Bedrock Guardrails safety checks on its inputs and outputs. Which TWO statements are true? (Select TWO)",
  ["The standalone ApplyGuardrail API evaluates content independently of any model",
   "Guardrails can protect non-Bedrock models, including third-party and self-hosted ones",
   "Guardrails only work inside the Converse API",
   "ApplyGuardrail generates the model's response",
   "Guardrails require the model to run on Bedrock"],
  [0,1], 2,
  "ApplyGuardrail is model-agnostic: it takes content in and returns a safety assessment, so any model (OpenAI, Gemini, self-hosted) can be wrapped with Bedrock safety policy without running on Bedrock.",
  ["Converse is one integration path, not the only one; standalone is the other.",
   "ApplyGuardrail assesses content; it never generates text.",
   "The model-location claim is exactly the misconception the standalone API disproves."],
  "The trap AWS set here: guardrails only work with Converse or Bedrock-hosted models. ApplyGuardrail is standalone.")

q("d2","easy","single","2.4 ValidationException",
  "An InvokeModel call fails with ValidationException. The model ID and IAM permissions are correct. What should the developer check first?",
  ["The request body format against the provider's documented schema for that model",
   "The color scheme of the application UI",
   "The S3 bucket versioning status",
   "The CloudTrail trail name"],
  [0],
  "InvokeModel takes provider-specific bodies, and a malformed body (missing anthropic_version for Claude, wrong field names) is the classic ValidationException cause when identity and permissions check out.",
  ["UI styling has no relationship to API validation errors.",
   "S3 versioning is irrelevant to a synchronous model invocation.",
   "The trail name does not affect request validation."],
  "The trap AWS set here: permission or network debugging for what is a request-body schema error.")

# 2.5 app patterns
q("d2","easy","single","2.5 Q Developer vs Q Business",
  "Developers want an AI assistant inside their IDE that suggests code, refactors functions, and writes unit tests. Which service fits?",
  ["Amazon Q Developer", "Amazon Q Business", "Amazon Kendra", "Amazon Lex"],
  [0],
  "Q Developer is the coding assistant: IDE integration, code generation, refactoring, and test support. Q Business is the enterprise knowledge assistant over company data; the exam swaps them in distractors.",
  ["Q Business answers questions over enterprise content; it does not live in the IDE writing code (master trap 10).",
   "Kendra is enterprise search, not a coding pair programmer.",
   "Lex builds chat interfaces, not code suggestions."],
  "The trap AWS set here: Q Business versus Q Developer. Business is knowledge chat; Developer is the IDE coder (master trap 10).")

q("d2","medium","single","2.5 IDP",
  "An insurance company must process 20,000 claim documents per day (PDFs, photos, forms) into structured data for downstream systems. Which service is built for this document-processing workflow?",
  ["Bedrock Data Automation, with standard or blueprint-customized extraction outputs",
   "Bedrock Guardrails",
   "Amazon Polly",
   "A fleet of EC2 instances running manual scripts"],
  [0],
  "Bedrock Data Automation is the intelligent document processing path: multimodal extraction (documents, images, video, audio) with standard outputs or custom blueprints, async at scale, results to S3.",
  ["Guardrails filter content; they extract nothing.",
   "Polly is text-to-speech, unrelated to document intake.",
   "EC2 fleets with scripts are the custom-build distractor the managed service replaces."],
  "The trap AWS set here: Guardrails for extraction, again. Filters do not extract.")

q("d2","easy","single","2.5 Amplify",
  "A frontend team must ship a web UI for the GenAI assistant quickly, with authentication and API integration but minimal backend code. Which service fits?",
  ["AWS Amplify, for declarative UI development with built-in auth and API connections",
   "Amazon EC2 with hand-configured web servers",
   "AWS Batch",
   "Amazon Route 53 alone"],
  [0],
  "Amplify is the declarative frontend path: UI components, authentication, and API/DataStore integration with minimal backend code, which matches a fast-shipping frontend team.",
  ["Hand-configured EC2 is maximum undifferentiated work for a standard web UI.",
   "Batch runs compute jobs, not user interfaces.",
   "Route 53 is DNS; it serves no UI."],
  "The trap AWS set here: EC2 hand-rolls for a standard frontend need. Managed first.")

q("d2","hard","single","2.5 Full scenario",
  "A publisher must generate study materials from 10,000+ files per day including video, with editors collaborating on drafts in real time. Which combination is most correct?",
  ["Bedrock Data Automation for extraction, S3 versioning for draft history, and AppSync with DynamoDB for real-time collaboration",
   "Bedrock Agents for change tracking and Guardrails for extraction",
   "Emailing files between editors and manual uploads",
   "A single EC2 instance running a video converter"],
  [0],
  "Each need maps to a service: Data Automation extracts from mixed modalities at scale, S3 versioning keeps every draft recoverable, and AppSync plus DynamoDB gives real-time collaborative editing with offline sync. Nothing is repurposed outside its job.",
  ["Agents do not do change tracking and Guardrails do not extract; both halves of this option misuse the services.",
   "Email collaboration at 10,000 files a day is an operational collapse.",
   "One EC2 instance is a single point of failure that cannot scale to the volume."],
  "The trap AWS set here: Agents for change tracking and Guardrails for extraction. Name each service's real job.")

# ================= DOMAIN 3 (20%) =================
# 3.1 safety controls
q("d3","easy","single","3.1 Denied topics",
  "A health chatbot must never provide medical diagnoses, even if the user asks directly. Which guardrail control enforces this?",
  ["Denied topics, defined in natural language (for example, medical diagnosis)",
   "Content filters with a toxicity threshold",
   "Word filters with a list of disease names",
   "A longer system prompt"],
  [0],
  "Denied topics block entire subject areas described in plain language. Prevent the model from discussing X topic maps directly to denied topics, not to toxicity categories.",
  ["Content filters target toxicity categories (hate, violence, sexual) with severity thresholds, not subject-matter bans.",
   "Word filters block exact strings; users easily rephrase around a finite list.",
   "A system prompt requests behavior but enforces nothing under jailbreak pressure."],
  "The trap AWS set here: content filters for a subject-matter ban. Topic bans are denied topics (master trap 3).")

q("d3","easy","single","3.1 PII filters",
  "A support chatbot must redact Social Security numbers from its outputs before users see them. Which guardrail control does this?",
  ["Sensitive information filters, set to mask the SSN entity type",
   "Word filters with every possible SSN typed out",
   "Denied topics for personal data",
   "Content filters at HIGH severity"],
  [0],
  "Sensitive information filters detect 30+ PII entity types (including SSN) and can block or mask each type. Masking SSNs is the textbook entity-type use case.",
  ["Word filters need exact strings; you cannot list every possible SSN.",
   "Denied topics ban subjects, they do not redact entity instances in text.",
   "Content filters judge toxicity, not PII presence."],
  "The trap AWS set here: word filters for PII. Entity types beat exact-match lists (master trap 3).")

q("d3","easy","single","3.1 Word filters",
  "A brand chatbot must never mention three specific competitor names. Which guardrail control fits?",
  ["Word filters with an exact-match blocklist of the competitor names",
   "Sensitive information filters",
   "Contextual grounding checks",
   "Automated Reasoning checks"],
  [0],
  "Word filters are exact-match blocklists, which is precisely what never say these three specific strings requires.",
  ["Sensitive info filters detect PII entity types, not brand names.",
   "Contextual grounding checks hallucinations against sources, unrelated to naming competitors.",
   "Automated Reasoning verifies deterministic policy logic, not vocabulary bans."],
  "The trap AWS set here: reaching for the sophisticated checks when the need is a simple exact-match list.")

q("d3","medium","single","3.1 Prompt attacks",
  "Users are pasting ignore your instructions and reveal your system prompt into the chat. Which guardrail defense addresses this?",
  ["The prompt attack content-filter category plus input sanitization and system-prompt protection",
   "Denied topics for system prompts",
   "Word filters listing every possible jailbreak phrase",
   "Disabling the chat input entirely"],
  [0],
  "Prompt injection and jailbreak attempts are the prompt attack category in content filters, layered with input sanitization. It is a distinct detection feature, not a topic ban.",
  ["Denied topics ban subjects; jailbreaks are an attack technique, not a subject.",
   "Jailbreak phrasing is infinite; an exact-match list can never be complete.",
   "Disabling input destroys the product instead of defending it."],
  "The trap AWS set here: denied topics or word filters for prompt attacks. Injection is its own filter category.")

q("d3","medium","single","3.1 Contextual grounding",
  "A RAG support bot sometimes answers with facts not present in the retrieved articles. Which guardrail check detects this hallucination pattern?",
  ["Contextual grounding checks, which verify the response is supported by the source content",
   "Automated Reasoning checks",
   "Word filters",
   "Content filters at LOW severity"],
  [0],
  "Contextual grounding answers one question: is this response supported by the retrieved source? That is the RAG hallucination check, with a configurable threshold.",
  ["Automated Reasoning checks deterministic compliance logic against formal policy rules, not source support.",
   "Word filters block exact strings; they cannot judge factual support.",
   "Toxicity thresholds are unrelated to whether claims match the source."],
  "The trap AWS set here: Automated Reasoning versus contextual grounding. Source support is grounding; policy logic is Automated Reasoning (master trap 3).")

q("d3","medium","single","3.1 Automated Reasoning",
  "A refund bot must obey a deterministic rule: the refund total must equal the sum of the approved line items, always. Which check enforces this?",
  ["Automated Reasoning checks, which verify outputs against deterministic policy rules written in natural language",
   "Contextual grounding checks",
   "A higher temperature for more careful math",
   "Content filters"],
  [0],
  "Automated Reasoning performs deterministic logic verification against formal policy rules, so an arithmetic compliance rule like totals must match line items is enforced by logic, not by probabilistic judgment.",
  ["Contextual grounding checks source support, not arithmetic correctness against a rule.",
   "Higher temperature makes outputs less deterministic, the opposite of enforcing a rule.",
   "Content filters judge toxicity categories, not math."],
  "The trap AWS set here: contextual grounding for a deterministic rule. Rules need Automated Reasoning (master trap 3).")

q("d3","medium","multi","3.1 Defense in depth",
  "A children's tutoring app must block profanity in inputs, prevent harmful outputs, stop jailbreak attempts, and ground facts in lesson material. Which TWO layers belong in its defense-in-depth design? (Select TWO)",
  ["Bedrock Guardrails applied on both inputs and outputs",
   "A Comprehend pre-filter for toxicity and PII before the model call",
   "Relying on the base model's built-in safety alone",
   "No logging, to keep the design simple",
   "A single system prompt asking the model to be safe"],
  [0,1], 2,
  "Defense in depth layers independent controls: Guardrails on inputs and outputs catch what one side misses, and a Comprehend pre-filter adds a separate toxicity/PII screen before the model ever sees the text. Layers fail independently, which is the point.",
  ["Base-model safety alone is never the most-correct answer for a sensitive audience; it is one layer, not a design (master trap 15).",
   "No logging removes the audit trail a children's product regulator will demand.",
   "A prompt request is not a control; jailbreaks target exactly this layer."],
  "The trap AWS set here: the base model's built-in safety as the complete answer. Never sufficient for sensitive scenarios (master trap 15).")

q("d3","easy","single","3.1 Input and output",
  "A team wants guardrails to screen user prompts before the model sees them AND screen generated answers before users see them. Is this supported?",
  ["Yes, guardrails can be applied on inputs, outputs, or both",
   "No, guardrails only screen outputs",
   "No, guardrails only screen inputs",
   "Only with two separate AWS accounts"],
  [0],
  "Guardrails are configured per direction: input screening, output screening, or both, via the Converse guardrailConfig or the standalone ApplyGuardrail API.",
  ["Output-only screening lets prompt attacks reach the model.",
   "Input-only screening lets harmful generations reach the user.",
   "No account gymnastics are needed; direction is a configuration choice."],
  "The trap AWS set here: assuming one direction only. Design both sides deliberately.")

q("d3","hard","single","3.1 Combined scenario",
  "A fintech chatbot must: refuse investment advice, redact account numbers from outputs, resist jailbreak attempts, and ground every answer in the bank's policy documents. Which combination is most correct?",
  ["Denied topics for investment advice, sensitive information filters masking account numbers, the prompt attack filter for jailbreaks, plus a knowledge base with contextual grounding checks",
   "Content filters at HIGH severity for everything",
   "Word filters listing financial terms and a long system prompt",
   "Relying on the flagship model's built-in safety"],
  [0],
  "Each requirement maps to its control: denied topics for the subject ban, sensitive info filters for the PII entity, prompt attack detection for jailbreaks, and KB grounding plus contextual grounding for factual answers. Four requirements, four matched mechanisms.",
  ["One severity knob cannot express a topic ban, PII masking, and source grounding; it conflates every control into toxicity.",
   "Word lists cannot cover advice phrasing, and prompts do not enforce.",
   "Built-in safety alone is never the complete answer for a regulated audience (master trap 15)."],
  "The trap AWS set here: one blunt control for four distinct requirements. Match the control to the scenario verb (master trap 3).")

q("d3","hard","single","3.1 Hallucination reduction",
  "A RAG application's hallucination rate is too high for a regulated deployment. Which combination most reduces hallucinations?",
  ["Knowledge base grounding plus confidence scoring, JSON Schema structured outputs, and contextual grounding checks",
   "A larger generation model with a higher temperature",
   "Removing all guardrails to reduce latency",
   "Longer prompts with more examples"],
  [0],
  "Hallucinations fall when every layer constrains fabrication: grounding supplies true sources, confidence scoring surfaces uncertainty, JSON Schema restricts output shape, and contextual grounding verifies claims against sources. No single knob does all four.",
  ["A larger model with higher temperature is more fluent and more creative, which increases fabrication risk on factual tasks.",
   "Removing guardrails removes the verification layer entirely.",
   "More examples improve style, not factuality against sources."],
  "The trap AWS set here: model size or temperature as the hallucination fix. Grounding plus verification is the fix.")

# 3.2 data security
q("d3","easy","single","3.2 Private connectivity",
  "A company requires all Bedrock API traffic to stay off the public internet. What should the developer configure?",
  ["VPC interface endpoints (PrivateLink) for the Bedrock, Bedrock runtime, agent, and agent runtime planes",
   "A NAT gateway for outbound traffic",
   "Public endpoints with IP allowlisting",
   "A VPN to the model's data center"],
  [0],
  "VPC interface endpoints keep Bedrock traffic on the AWS private network with no public IPs and no NAT. Each plane (bedrock, bedrock-runtime, bedrock-agent, bedrock-agent-runtime) gets its endpoint.",
  ["A NAT gateway still sends traffic to public endpoints; it hides source IPs but not the public path.",
   "IP allowlisting on a public endpoint leaves traffic on the public internet.",
   "There is no model data center to VPN to; Bedrock is a regional AWS service."],
  "The trap AWS set here: NAT or allowlists as private connectivity. PrivateLink is the private path.")

q("d3","medium","multi","3.2 PII pipeline",
  "A customer-service GenAI application must protect PII across stored chat logs and live conversations, with minimal custom code. Which THREE services form the standard pipeline? (Select THREE)",
  ["Amazon Macie to discover PII in S3 at scale",
   "Amazon Comprehend for real-time PII detection in text",
   "Bedrock Guardrails sensitive information filters at inference time",
   "Amazon Translate to obfuscate the PII",
   "Amazon Rekognition to find PII in chat text"],
  [0,1,2], 3,
  "The three cover the full lifecycle: Macie finds PII already sitting in S3, Comprehend detects it in live text streams, and Guardrails filters block or mask it at inference. Minimal custom code, complete coverage.",
  ["Translate preserves meaning across languages; it protects nothing.",
   "Rekognition is a vision service; chat text is Comprehend's domain."],
  "The trap AWS set here: Translate for obfuscation and Rekognition for text PII. Both are wrong-plane tools.")

q("d3","easy","single","3.2 Macie",
  "A company has 40 TB of historical chat logs in S3 and needs to find where PII is stored before designing protections. Which service discovers PII at this scale?",
  ["Amazon Macie", "Amazon Comprehend", "AWS CloudTrail", "Amazon GuardDuty"],
  [0],
  "Macie is built for S3 at scale: it crawls buckets and classifies sensitive data including PII, producing a findings inventory. Discovery across 40 TB is its exact job.",
  ["Comprehend analyzes text passed to it; it does not crawl S3 buckets for discovery.",
   "CloudTrail audits API calls, not bucket contents.",
   "GuardDuty detects threats and anomalies, not PII locations."],
  "The trap AWS set here: Comprehend for bucket-scale discovery. Discovery is Macie; analysis is Comprehend.")

q("d3","easy","single","3.2 Comprehend",
  "A live chat moderator needs real-time detection of PII entities in streaming conversation text. Which service fits?",
  ["Amazon Comprehend", "Amazon Macie", "Amazon Textract", "AWS Security Hub"],
  [0],
  "Comprehend detects 30+ PII entity types in text in real time, which is the live-stream detection requirement. Macie is the batch S3 discovery counterpart.",
  ["Macie works on S3 objects in batch, not on live streams.",
   "Textract extracts text from documents and images, not PII entities from chat.",
   "Security Hub aggregates security findings; it does not analyze text."],
  "The trap AWS set here: Macie versus Comprehend. S3 batch discovery is Macie; live text is Comprehend.")

q("d3","medium","single","3.2 Invocation logging",
  "A healthcare application logs Bedrock model invocations to CloudWatch for debugging, but the logs may contain patient information. What should the developer do?",
  ["Disable invocation logging or restrict it with KMS encryption and tight access controls",
   "Keep logging everything; debugging needs full data",
   "Move the logs to a public S3 bucket for easier access",
   "Log only the model ID and hope that is enough"],
  [0],
  "Invocation logs can contain prompts and completions, which means PHI. In compliance environments the exam answer is to disable logging or encrypt it with KMS and lock down access; convenience never outranks the compliance requirement.",
  ["Full PHI in logs is a compliance violation regardless of debugging convenience.",
   "A public bucket turns a violation into a breach.",
   "Model IDs alone cannot debug prompt-level issues, so this both fails compliance hygiene and fails debugging."],
  "The trap AWS set here: unencrypted invocation logging in a healthcare scenario. Logs carry PII; treat them accordingly.")

q("d3","medium","single","3.2 Obfuscation trap",
  "A developer proposes running all user text through Amazon Translate twice (to another language and back) to obfuscate PII before model calls. Why is this wrong?",
  ["Translation preserves meaning, so PII survives intact; it provides zero protection and adds latency",
   "Translate cannot process PII",
   "Translate is too expensive for this",
   "Double translation is not supported"],
  [0],
  "Obfuscation must destroy or mask the sensitive data; translation preserves semantic content by design, so names, numbers, and identifiers come through unchanged. The proposal adds latency while protecting nothing.",
  ["Translate processes any text; the problem is what it preserves, not what it accepts.",
   "Cost is secondary to the fact that the protection is fictional.",
   "Round-trip translation is supported; support is not the issue."],
  "The trap AWS set here is the proposal itself: Translate for PII protection. Meaning-preserving transforms are not masking.")

q("d3","hard","single","3.2 Bank scenario",
  "A bank's GenAI assistant handles account data under strict regulation: traffic must stay private, data encrypted at rest, every API call audited, and prompts must never persist in logs. Which combination is most correct?",
  ["VPC interface endpoints for Bedrock, KMS encryption at rest, CloudTrail for API auditing, and invocation logging disabled",
   "Public Bedrock endpoints with TLS only",
   "CloudWatch Logs for auditing API calls",
   "Storing prompts in S3 for debugging convenience"],
  [0],
  "Each regulatory need maps to a control: PrivateLink keeps traffic off the public internet, KMS encrypts data at rest, CloudTrail audits who called what, and disabling invocation logging guarantees prompts never persist. TLS alone leaves three requirements unmet.",
  ["Public endpoints with TLS fail the private-traffic requirement outright.",
   "CloudWatch Logs hold application content; API auditing is CloudTrail's job.",
   "Persisting prompts in S3 directly violates the no-persistence requirement."],
  "The trap AWS set here: TLS as the complete security answer, and CloudWatch Logs confused with CloudTrail auditing.")

q("d3","easy","single","3.2 Lake Formation",
  "A data lake holds tables with different sensitivity levels, and GenAI pipelines must only read columns each team is authorized for. Which service provides this granular access control?",
  ["AWS Lake Formation", "Amazon S3 versioning", "AWS WAF", "Amazon EventBridge"],
  [0],
  "Lake Formation provides column-, row-, and cell-level permissions over data lake tables, which is the granular control the scenario requires.",
  ["S3 versioning protects against overwrites; it grants no column-level access control.",
   "WAF filters web attacks, unrelated to data authorization.",
   "EventBridge routes events; it authorizes nothing."],
  "The trap AWS set here: S3 features standing in for real authorization. Versioning is not access control.")

# 3.3 governance
q("d3","easy","single","3.3 Model cards",
  "A regulated company must document each model's intended uses, limitations, and evaluation results for auditors. Which SageMaker feature produces this?",
  ["SageMaker Model Cards", "SageMaker JumpStart", "SageMaker Neo", "SageMaker Clarify"],
  [0],
  "Model Cards document a model's intended use, limitations, and evaluation results in a standard auditable format, with programmatic generation support.",
  ["JumpStart provides pre-built models and solutions, not compliance documentation.",
   "Neo compiles models for edge deployment targets, unrelated to documentation.",
   "Clarify measures bias and explainability; its outputs can feed a card, but it is not the card."],
  "The trap AWS set here: Clarify versus Model Cards. Clarify measures; Cards document.")

q("d3","medium","single","3.3 Audit trail",
  "After a disputed AI-generated decision, auditors ask: which IAM identity invoked the model, at what time, and with which parameters? Which service answers this?",
  ["AWS CloudTrail, which records every Bedrock API call with identity and timestamp",
   "CloudWatch Logs Insights over application logs",
   "The model's own memory",
   "Amazon S3 access logs"],
  [0],
  "CloudTrail is the API audit trail: who called what, when, from where. Identity-plus-timestamp-plus-API-action is the signature CloudTrail question.",
  ["CloudWatch Logs hold application and decision content; the who-called-what audit is Trail's plane.",
   "Models do not retain invocation audit records.",
   "S3 access logs cover S3 requests only, not Bedrock invocations."],
  "The trap AWS set here: CloudWatch Logs for API auditing. Trail audits calls; Logs hold content.")

q("d3","medium","single","3.3 Lineage",
  "A regulator asks: which source documents produced this specific generated answer? Which combination provides the lineage?",
  ["Glue Data Catalog registration of sources, metadata tagging through the pipeline, and source attribution on generated content",
   "A longer context window",
   "Deleting old document versions",
   "Training the model on fewer documents"],
  [0],
  "Lineage is built from cataloged sources (Glue Data Catalog), metadata tags carried through ingestion, and attribution attached to outputs, so any answer traces back to its documents. No single feature does this alone.",
  ["Context size does not record where content came from.",
   "Deleting versions destroys lineage instead of building it.",
   "Fewer documents do not create traceability."],
  "The trap AWS set here: single-feature answers for lineage, which is always a combination of catalog, tags, and attribution.")

q("d3","hard","multi","3.3 Continuous compliance",
  "A lending assistant operates under fair-lending regulation. Which TWO practices demonstrate continuous compliance rather than one-time checking? (Select TWO)",
  ["Automated monitoring for misuse, drift, and policy violations with alerting",
   "A remediation workflow triggered by monitoring alerts",
   "One pre-launch fairness review with no follow-up",
   "Deleting decision logs after 7 days to save storage",
   "Annual manual spot checks only"],
  [0,1], 2,
  "Continuous means always-on: monitoring detects drift, misuse, and violations as they happen, and the remediation workflow acts on alerts without waiting for a human audit cycle. That is the exam's governance posture.",
  ["One pre-launch review cannot catch drift that appears months later.",
   "Deleting logs destroys the evidence regulators require.",
   "Annual checks leave eleven months of unmonitored operation."],
  "The trap AWS set here: one-time checks dressed as compliance. The exam wants continuous monitoring plus remediation.")

q("d3","hard","single","3.3 Bias over time",
  "A hiring assistant passed fairness testing at launch. Six months later, applicant demographics shifted and outputs show skew. What should the team have had in place?",
  ["Continuous bias drift monitoring with automated alerts, not just the launch-time test",
   "A larger model",
   "More training data at launch",
   "A disclaimer in the UI"],
  [0],
  "Fairness is a moving target: data drift changes model behavior after launch, so only continuous monitoring with alerts catches skew when it appears. A launch test is a snapshot, not a guarantee.",
  ["Model size does not prevent drift-induced skew.",
   "Launch-time data cannot cover future demographic shifts.",
   "A disclaimer does not detect or fix biased outputs."],
  "The trap AWS set here: treating fairness as a one-time check. The exam demands continuous monitoring.")

# 3.4 responsible AI
q("d3","easy","single","3.4 Transparency",
  "Loan applicants must be told why the AI assistant reached its recommendation. Which capability provides this transparency?",
  ["Reasoning traces and evidence or source attribution in answers",
   "A higher temperature",
   "A bigger context window",
   "Faster inference"],
  [0],
  "Transparency means showing the why: agent reasoning traces (enableTrace) expose the decision path, and source attribution shows the evidence behind claims. Both are named transparency mechanisms.",
  ["Temperature affects randomness, not explainability.",
   "Context size does not explain decisions.",
   "Speed is unrelated to transparency."],
  "The trap AWS set here: performance knobs as transparency. Transparency is traces plus evidence.")

q("d3","medium","single","3.4 Model comparison",
  "A team must compare two models for support-summary quality, including whether summaries match the company brand voice. Which evaluation approach is most correct?",
  ["LLM-as-a-judge for correctness at scale, plus human evaluation for brand voice",
   "Programmatic metrics only",
   "Pick the model with more parameters",
   "Ask the sales team informally"],
  [0],
  "Quality at scale needs LLM-as-a-judge (correctness, completeness, faithfulness across thousands of samples), while brand voice is subjective and needs human judgment. The combination covers objective and subjective in the right proportions.",
  ["Programmatic metrics cannot judge style or voice.",
   "Parameter count does not predict brand-voice fit.",
   "Informal opinions are not an evaluation methodology."],
  "The trap AWS set here: programmatic evaluation for subjective style. Subjective needs human or LLM-as-judge.")

q("d3","medium","single","3.4 Fairness",
  "A team must ensure assistant outputs stay unbiased across demographic groups. Which approach is most correct?",
  ["Pre-defined fairness metrics, A/B testing via Prompt Management variants, and LLM-as-a-judge evaluations",
   "Using a bigger model, which is naturally fairer",
   "Removing all demographic words from prompts",
   "Testing once with five examples"],
  [0],
  "Fairness is engineered: define metrics up front, A/B test variants for disparate impact, and evaluate with LLM-as-judge at scale. Bigger models are not inherently fairer, and five examples prove nothing.",
  ["Model size has no reliable relationship with fairness.",
   "Word removal is cosmetic and can hide bias while leaving disparate outcomes.",
   "Five examples cannot measure group-level disparities."],
  "The trap AWS set here: a bigger model as the fairness fix. Fairness needs metrics and measurement, not scale.")

q("d3","easy","single","3.4 Attribution",
  "A news summarizer must show readers which source each claim came from. Which responsible AI principle does this implement?",
  ["Transparency through evidence and source attribution",
   "Fairness",
   "Data minimization",
   "Latency optimization"],
  [0],
  "Showing the evidence behind each claim is transparency: the reader can verify rather than trust. Source attribution is the named mechanism.",
  ["Fairness concerns disparate impact across groups, not sourcing.",
   "Data minimization is about collecting less data, not citing it.",
   "Latency is a performance concern, unrelated to trust."],
  "The trap AWS set here: confusing the responsible AI principles. Attribution is transparency.")

q("d3","hard","single","3.4 Regulated fairness",
  "A bank deploys a loan-advice assistant under fair-lending scrutiny. Regulators will ask for proof of ongoing fairness. Which combination is most correct?",
  ["Pre-defined fairness metrics with continuous drift monitoring and alerts, model cards documenting limitations, and a human review loop for edge cases",
   "A one-time bias test before launch",
   "The largest available model with default settings",
   "A system prompt asking the model to be fair"],
  [0],
  "Regulated fairness needs the full stack: metrics defined before launch, continuous monitoring because drift happens, model cards documenting known limitations for auditors, and humans reviewing the edge cases automation cannot judge. Each piece answers a regulator's question.",
  ["One-time tests cannot catch post-launch drift.",
   "Default settings on a large model are not evidence of fairness.",
   "A prompt request is not a control and not auditable evidence."],
  "The trap AWS set here: one-time testing or prompt requests as fairness proof. Regulators want continuous, documented, human-backed evidence.")

# ================= DOMAIN 4 (12%) =================
# 4.1 cost optimization
q("d4","easy","single","4.1 Prompt caching",
  "Every call to a support assistant starts with the same 8,000-token system prompt of policy text, and token costs are climbing. What is the most direct cost fix?",
  ["Prompt caching via the Converse cachePoint, so the repeated prefix is billed at the cheaper cached rate",
   "Provisioned Throughput",
   "A larger context window",
   "Batch inference"],
  [0],
  "Prompt caching exists for exactly this: large static prefixes repeated across calls. The cachePoint marks the prefix, and cached input tokens cost less. Same behavior, lower bill.",
  ["Provisioned Throughput guarantees capacity and latency; it does not discount repeated input tokens.",
   "A larger window holds more text but charges full price for all of it.",
   "Batch inference is for non-interactive workloads, not a live chat assistant."],
  "The trap AWS set here: Provisioned Throughput for a repeated-prefix cost problem. Caching attacks repeated-input cost; PT attacks latency guarantees (master trap 4).")

q("d4","medium","single","4.1 Caching vs PT",
  "An application has steady, predictable traffic and users report throttling errors at peak. The token bill is acceptable; latency and reliability are the problems. What should the developer choose?",
  ["Provisioned Throughput for the predictable baseline",
   "Prompt caching",
   "Semantic caching in ElastiCache",
   "A smaller model"],
  [0],
  "Throttling under steady predictable load is a capacity problem, and Provisioned Throughput reserves model units to eliminate it. The bill is fine, so cost levers are the wrong tools; this is the latency/throughput guarantee case.",
  ["Prompt caching cuts repeated-input cost, which is not the reported problem.",
   "Semantic caching helps repeated similar queries, not throttling under load.",
   "A smaller model changes quality and price, not reserved capacity."],
  "The trap AWS set here: cost levers for a capacity problem. Match the lever to the symptom: throttling means capacity (master trap 4).")

q("d4","medium","multi","4.1 Tiered models",
  "A team wants tiered model usage: cheap models for simple queries, flagship quality for hard ones. Which TWO pieces make this work? (Select TWO)",
  ["A classifier or router that scores query complexity before choosing the model",
   "Routing simple queries to the small model and complex ones to the flagship",
   "Sending every query to the flagship model",
   "Using the small model for everything with no fallback",
   "Choosing models randomly to spread load"],
  [0,1], 2,
  "Tiered usage needs both halves: a complexity signal (classifier or prompt router) and the routing policy that acts on it. Without the classifier there is no signal; without the policy there is no savings.",
  ["Always-flagship is the spend tiering exists to cut.",
   "Small-model-only sacrifices quality on hard queries with no recovery.",
   "Random routing optimizes nothing and risks quality on every hard query."],
  "The trap AWS set here: tiering without the complexity signal. A router with no classifier is decoration.")

q("d4","easy","single","4.1 Batch savings",
  "A nightly job summarizes 20,000 tickets. It currently uses on-demand calls and the CFO asks why it costs so much. What is the cheapest correct change?",
  ["Move the job to batch inference, which costs roughly half of on-demand for non-interactive work",
   "Buy Provisioned Throughput for the nightly window",
   "Switch to the largest flagship model for speed",
   "Run the job at noon instead of midnight"],
  [0],
  "Batch inference is priced about 50% below on-demand precisely for workloads like this: S3 in, S3 out, hours of latency tolerance. The job's shape is the discount's shape.",
  ["PT commits hourly capacity; a once-nightly job cannot amortize the commit.",
   "The flagship model maximizes per-token price, the opposite of the CFO's ask.",
   "Time of day does not change on-demand pricing."],
  "The trap AWS set here: reserved capacity for a batch-shaped workload. Batch pricing is the lever.")

q("d4","medium","multi","4.1 Multi-lever savings",
  "Token costs grow 30% per month. The CFO demands cuts with no UX degradation. Which THREE levers belong in the plan? (Select THREE)",
  ["Route low-priority traffic to smaller cheaper models",
   "Prompt caching for the repeated system prefix",
   "Provisioned Throughput for the predictable baseline load",
   "Always use the flagship model for every query",
   "Disable all logging to save money"],
  [0,1,2], 3,
  "Cost optimization is multi-lever: smaller models cut per-token price where quality allows, caching discounts repeated prefixes, and PT rightsizes the steady baseline. Each lever attacks a different part of the bill without touching user experience.",
  ["Always-flagship is the current expensive default, not a cut.",
   "Disabling logging saves pennies while destroying observability and audit trails."],
  "The trap AWS set here: single-lever answers. The exam's most-correct cost answers stack complementary levers.")

q("d4","easy","single","4.1 Semantic caching",
  "A FAQ bot receives the same 200 questions phrased slightly differently, thousands of times a day. What reduces model calls here?",
  ["Semantic caching in ElastiCache or DynamoDB, keyed by meaning rather than exact text",
   "Prompt caching of the system prompt",
   "Provisioned Throughput",
   "A larger embedding model"],
  [0],
  "Semantic caching matches new queries to previously answered similar ones, so thousands of rephrased repeats never reach the model. Exact-text caching would miss the rephrasings; semantic matching catches them.",
  ["Prompt caching discounts the prefix, but the per-query generation cost remains on every call.",
   "PT guarantees capacity; it does not eliminate redundant calls.",
   "A larger embedding model improves match quality but does not itself skip model calls."],
  "The trap AWS set here: semantic caching for highly personalized queries, where hit rates collapse. It shines on repeated similar questions.")

q("d4","hard","single","4.1 Cost scenario",
  "A SaaS company serves 8 million chat requests per month. Analysis shows: 70% are simple lookups answerable by a small model, every request carries the same 6,000-token policy prefix, traffic is steady day to day, and Friday evenings spike 5x. Which cost plan is most correct?",
  ["Route simple queries to a small model, enable prompt caching for the repeated prefix, hold Provisioned Throughput for the steady baseline, and let on-demand absorb Friday spikes",
   "Run everything on the flagship model with on-demand pricing",
   "Buy Provisioned Throughput sized for the Friday peak and use it all week",
   "Cache full responses for every query including personalized ones"],
  [0],
  "Every observed fact maps to a lever: 70% simple means tiered routing, the repeated prefix means prompt caching, steady baseline means PT, and 5x spikes mean on-demand overflow. The most-correct answer stacks all four instead of picking one.",
  ["All-flagship on-demand ignores every observed savings opportunity.",
   "Peak-sized PT pays peak prices through every quiet hour.",
   "Full-response caching on personalized queries gets near-zero hit rates; the blueprint explicitly rejects this."],
  "The trap AWS set here: any single-lever plan. Real cost optimization composes levers to match the traffic shape.")

# 4.2 performance
q("d4","easy","single","4.2 Determinism",
  "A classification task returns different labels for identical inputs across runs, but the business requires 99.5% consistency. What is the first fix?",
  ["Set temperature to 0 (and keep top-p/top-k deterministic) to remove sampling randomness",
   "Buy Provisioned Throughput",
   "Use a larger context window",
   "Add more few-shot examples"],
  [0],
  "Temperature controls sampling randomness; temperature 0 makes output deterministic for identical inputs. Inconsistency across identical inputs is a randomness problem, and temperature is the randomness knob.",
  ["PT stabilizes latency and capacity, not output randomness; this is the exam's named confusion (master trap 12).",
   "Context size does not affect sampling variance.",
   "More examples improve task understanding but do not remove sampling randomness."],
  "The trap AWS set here: Provisioned Throughput for output consistency. PT fixes capacity, not randomness (master trap 12).")

q("d4","medium","single","4.2 Streaming",
  "Users complain a chat assistant feels slow, though total response time is acceptable. The biggest win for perceived latency is:",
  ["Streaming tokens with ConverseStream so users read while the model still generates",
   "A larger model for faster thinking",
   "Batch inference",
   "Longer system prompts"],
  [0],
  "Streaming attacks perceived latency: the first token arrives in a fraction of the total time, so the app feels instant even when full generation takes seconds. Perceived latency and actual latency are different problems.",
  ["Larger models are generally slower per token, the opposite direction.",
   "Batch is hours-scale and non-interactive.",
   "Longer prompts add input processing time, making things worse."],
  "The trap AWS set here: optimizing total time when the complaint is perceived latency. Stream first.")

q("d4","medium","single","4.2 PT consistency trap",
  "A developer proposes buying Provisioned Throughput to make model outputs more consistent across identical prompts. Why is this wrong?",
  ["Provisioned Throughput reserves capacity and stabilizes latency; output randomness is controlled by temperature and prompt design, not capacity",
   "Provisioned Throughput makes outputs less consistent",
   "Temperature cannot be set on provisioned models",
   "Consistency is impossible with any model"],
  [0],
  "Capacity and randomness are independent axes: PT buys reserved model units (no throttling, stable latency), while temperature and prompt control govern sampling variance. Buying capacity to fix randomness is a category error the exam names explicitly.",
  ["PT does not harm consistency; it is simply irrelevant to it.",
   "Inference parameters apply normally to provisioned models.",
   "Deterministic outputs are achievable with temperature 0 and controlled prompts."],
  "The trap AWS set here is the proposal itself: PT for output consistency. Name the two axes and keep them separate (master trap 12).")

q("d4","easy","single","4.2 Inference params",
  "A developer proposes tuning temperature, top-p, and top-k to cut the token bill. Why is this misguided?",
  ["Those parameters control randomness and output quality, not cost; token count and model choice drive the bill",
   "Those parameters do not exist",
   "Those parameters increase cost directly",
   "Cost cannot be optimized at all"],
  [0],
  "Temperature, top-p, and top-k shape the sampling distribution: creativity versus determinism. They do not change per-token price or, reliably, token counts. Cost levers are model selection, caching, batching, and prompt compression.",
  ["They exist and matter, just for quality, not cost.",
   "They do not carry a price tag; the bill is tokens times model rate.",
   "Cost is highly optimizable, through the right levers."],
  "The trap AWS set here: quality knobs as cost knobs. Keep the two families separate.")

q("d4","hard","single","4.2 Retrieval latency",
  "A RAG application's p99 latency is 9 seconds. Profiling shows retrieval takes 7 seconds: unoptimized vector index, no query preprocessing, and keyword-only search missing often. Which combination most reduces retrieval latency?",
  ["Index optimization and sharding, query preprocessing, hybrid search with custom scoring, plus caching of frequent queries",
   "A larger generation model",
   "Higher temperature",
   "Provisioned Throughput on the embedding model"],
  [0],
  "The profile says retrieval is the bottleneck, so every fix targets retrieval: optimized indexes and sharding cut search time, preprocessing shrinks the query, hybrid search with scoring finds answers in fewer round trips, and caching skips repeat work. Fix the measured bottleneck.",
  ["The generation model is 2 of the 9 seconds; upsizing it worsens latency.",
   "Temperature does not affect retrieval speed.",
   "PT on embeddings buys capacity that is not the problem; the index itself is slow."],
  "The trap AWS set here: model-side fixes for a measured retrieval bottleneck. Profile first, then fix what is slow.")

# 4.3 monitoring
q("d4","easy","single","4.3 Token metrics",
  "A product manager wants per-feature token spend to attribute costs to teams. Which CloudWatch metrics provide the raw data?",
  ["InputTokenCount and OutputTokenCount on the Bedrock namespace",
   "InvocationThrottles",
   "CPUUtilization on EC2",
   "S3 bucket size metrics"],
  [0],
  "Bedrock emits InputTokenCount and OutputTokenCount per invocation; dimensioned by model and API, they are the raw material for per-feature cost attribution.",
  ["InvocationThrottles counts throttled calls, useful for capacity but not for spend math.",
   "EC2 CPU metrics are irrelevant to serverless Bedrock token billing.",
   "Bucket size tracks storage, not model tokens."],
  "The trap AWS set here: throttle or infrastructure metrics for a token-billing question. Spend is token counts.")

q("d4","medium","multi","4.3 Anomaly detection",
  "A team needs near-real-time detection of hallucinations in production plus alerts on abnormal token spend, with minimal custom code. Which TWO capabilities meet this? (Select TWO)",
  ["Bedrock evaluation jobs with LLM-based judgments scoring outputs against quality criteria",
   "CloudWatch anomaly detection on token count metrics",
   "A hand-built Glue plus Athena pipeline over raw logs",
   "CloudTrail for real-time metric alerts",
   "Manual daily reading of random outputs"],
  [0,1], 2,
  "Bedrock evaluations bring LLM-as-a-judge scoring to production outputs for hallucination detection, and CloudWatch anomaly detection watches token metrics for spend spikes. Both are managed, near-real-time, and low-code.",
  ["Glue plus Athena is the high-overhead distractor: batch, custom, and slow where managed real-time exists (master trap 14).",
   "CloudTrail is audit logging, not a metrics alerting plane.",
   "Manual sampling cannot be near-real-time at production volume."],
  "The trap AWS set here: Glue plus Athena for real-time detection, and CloudTrail for metrics. Wrong-plane tools (master trap 14).")

q("d4","easy","single","4.3 Tracing",
  "A multi-step agent calls three tools and a knowledge base per request. Debugging is hard because failures hide inside the chain. What provides end-to-end visibility?",
  ["AWS X-Ray tracing across the agent and FM call chain",
   "CloudTrail",
   "S3 versioning",
   "Longer log retention alone"],
  [0],
  "X-Ray traces requests across service boundaries, showing each tool call's latency and errors inside the agent's chain. That is the multi-step observability answer.",
  ["CloudTrail audits API calls; it does not trace latency through a call chain.",
   "S3 versioning protects objects; it observes nothing.",
   "Longer retention keeps more logs but does not connect them into a trace."],
  "The trap AWS set here: CloudTrail for performance tracing. Trail audits; X-Ray traces.")

q("d4","medium","single","4.3 Model Monitor trap",
  "A developer proposes SageMaker Model Monitor to detect quality drift in the chatbot's free-text answers. Why is this the wrong tool?",
  ["Model Monitor is built for tabular ML feature and prediction drift; GenAI text quality drift needs Bedrock evaluations or golden datasets",
   "Model Monitor cannot run on a schedule",
   "Model Monitor only works with Bedrock",
   "Text drift cannot be monitored at all"],
  [0],
  "Model Monitor watches statistical drift in structured features and predictions. Free-text answer quality (hallucinations, tone drift, factuality) needs LLM-as-a-judge evaluations or golden-dataset comparisons, which are the GenAI-native tools.",
  ["Scheduling is not the issue; the data type is.",
   "Model Monitor is SageMaker-side, not Bedrock-side; the direction of the claim is backwards.",
   "Text drift is monitorable, with the right evaluation-based tools."],
  "The trap AWS set here is the proposal itself: tabular ML monitoring for GenAI text. Match the monitor to the data type.")

q("d4","hard","single","4.3 Forensics",
  "Last Tuesday a customer received a badly wrong answer. Support must find the exact prompt, retrieved chunks, and model response for that request. Which setup makes this possible?",
  ["Model invocation logging to S3 or CloudWatch, queried with CloudWatch Logs Insights for prompt and response forensics",
   "CloudTrail lookup of the request",
   "Guessing from the current prompt template",
   "Application metrics dashboards"],
  [0],
  "Invocation logging captures the actual request and response payloads; Logs Insights then searches them by time, user, or session to reconstruct exactly what happened. Forensics needs payloads, not just metadata.",
  ["CloudTrail records that an API call happened, not the prompt and response content.",
   "The current template may differ from Tuesday's version; reconstruction needs the logged artifact.",
   "Metrics dashboards show aggregates, never individual payloads."],
  "The trap AWS set here: CloudTrail for content forensics. Trail proves the call; logs hold the content.")

# ================= DOMAIN 5 (11%) =================
# 5.1 evaluation
q("d5","easy","single","5.1 Programmatic eval",
  "A team needs an objective, repeatable benchmark of summary accuracy run nightly over 10,000 examples. Which evaluation method fits?",
  ["Programmatic (automatic) evaluation with built-in or custom datasets",
   "Human evaluation by the whole company",
   "LLM-as-a-judge with no dataset",
   "No evaluation; ship it"],
  [0],
  "Programmatic evaluation computes objective metrics (accuracy, robustness, toxicity) deterministically over datasets, which makes it repeatable and cheap enough to run nightly at 10,000-example scale.",
  ["Whole-company human review nightly is impossibly expensive and slow.",
   "LLM-as-a-judge without a dataset has nothing to judge against.",
   "Shipping unevaluated is how regressions reach customers."],
  "The trap AWS set here: human evaluation at machine scale. Objective plus repeatable plus large means programmatic.")

q("d5","easy","single","5.1 LLM-as-a-judge",
  "A team needs human-like quality judgments (correctness, completeness, faithfulness) across 50,000 RAG answers. Human review at that scale is impossible. Which method fits?",
  ["LLM-as-a-judge evaluation",
   "Programmatic exact-match metrics",
   "Skipping evaluation",
   "One engineer reading 50 samples"],
  [0],
  "LLM-as-a-judge applies model-based grading on correctness, completeness, faithfulness, harmfulness, and custom metrics at a scale humans cannot match. It is the exam's answer for human-like quality at machine scale.",
  ["Exact-match metrics fail on paraphrased correct answers, which is most of RAG output.",
   "Skipping evaluation abandons quality control entirely.",
   "Fifty samples cannot represent 50,000 answers."],
  "The trap AWS set here: exact-match metrics for free-text quality. Paraphrase-tolerant judgment needs the judge.")

q("d5","easy","single","5.1 Human eval",
  "A luxury brand must verify that generated copy matches its distinctive voice before launch. Which evaluation method fits?",
  ["Human evaluation, because brand voice is subjective judgment",
   "Programmatic accuracy metrics",
   "Latency benchmarking",
   "Token counting"],
  [0],
  "Brand voice is taste, tone, and nuance: subjective by definition. Human evaluators (employees or an AWS-managed team) are the method for subjective quality.",
  ["Accuracy metrics measure factuality, not voice.",
   "Latency measures speed, not style.",
   "Token counts measure length, not luxury."],
  "The trap AWS set here: programmatic metrics for subjective style. Subjective needs humans (or LLM-as-judge).")

q("d5","medium","multi","5.1 RAG eval",
  "A team evaluates a RAG system before launch. Which TWO dimensions must the evaluation cover? (Select TWO)",
  ["Retrieval relevance: do the retrieved chunks actually answer the query",
   "Generation faithfulness: is the answer supported by the retrieved chunks",
   "Model parameter count",
   "Prompt length in tokens",
   "The color scheme of the UI"],
  [0,1], 2,
  "RAG evaluation is two-sided by construction: the retriever must return relevant chunks and the generator must stay faithful to them. A system can fail on either side independently, so both need measurement, typically LLM-as-a-judge powered.",
  ["Parameter count does not measure retrieval or faithfulness.",
   "Prompt length is an input detail, not a quality dimension.",
   "UI styling is unrelated to RAG correctness."],
  "The trap AWS set here: evaluating only generation. RAG fails on the retrieval side just as often.")

q("d5","medium","single","5.1 Regression",
  "A team ships a new prompt version weekly. What prevents silent quality regressions?",
  ["Regression testing on every prompt and model change, plus canary deployments",
   "Shipping directly to 100% of traffic for fast feedback",
   "Testing once at initial launch",
   "Longer prompts"],
  [0],
  "Regression suites rerun golden evaluations on every change to catch drift, and canary deployments limit blast radius so a bad version affects a fraction of traffic first. Change-gated quality is the deployment-validation answer.",
  ["Full-traffic shipping turns every regression into a full outage.",
   "Launch-only testing cannot catch regressions introduced by later changes.",
   "Prompt length is unrelated to regression safety."],
  "The trap AWS set here: launch-only testing. Quality gates must run on every change.")

q("d5","medium","multi","5.1 Combined eval",
  "A team compares two models for customer-support answers, judging both factual correctness and empathy of tone. Which TWO methods together cover this? (Select TWO)",
  ["LLM-as-a-judge for correctness at scale across thousands of answers",
   "Human evaluation for empathy and tone, which are subjective",
   "Programmatic metrics alone for both dimensions",
   "No evaluation; trust the benchmark scores",
   "A single engineer's gut feeling"],
  [0,1], 2,
  "Correctness at scale is the judge's job (thousands of answers graded consistently), while empathy is subjective and belongs to human evaluators. The split matches each method to its strength.",
  ["Programmatic metrics cannot judge empathy or tone.",
   "Published benchmarks do not measure your task or your tone.",
   "One opinion is not an evaluation methodology."],
  "The trap AWS set here: one method for both dimensions. Objective scale and subjective taste need different tools.")

q("d5","hard","single","5.1 BYOI",
  "A company evaluates a third-party model's answers and also wants to score its full application's end-to-end responses (which mix model output with business logic). Which evaluation capability supports this?",
  ["Bring-your-own-inference: evaluate any model or full system responses, not just Bedrock invocations",
   "Programmatic evaluation limited to Bedrock models",
   "Human evaluation only",
   "Disabling evaluation for third-party models"],
  [0],
  "Bring-your-own-inference decouples evaluation from the inference source: you supply the responses (any model, full application output) and the evaluation harness scores them. That covers third-party models and end-to-end app responses alike.",
  ["Bedrock-only programmatic eval cannot see the third-party model or the app layer.",
   "Human-only evaluation cannot scale to regression suites.",
   "Disabling evaluation abandons quality control where it is needed most."],
  "The trap AWS set here: assuming evaluation only works on Bedrock-hosted models. BYOI evaluates anything.")

q("d5","medium","single","5.1 Subjective metrics",
  "A developer proposes using programmatic exact-match metrics to evaluate whether marketing copy matches the brand voice. Why is this wrong?",
  ["Brand voice is subjective; exact-match metrics cannot judge style, so human or LLM-as-a-judge evaluation is needed",
   "Programmatic metrics are always wrong",
   "Brand voice cannot be evaluated at all",
   "Exact-match is too expensive"],
  [0],
  "Exact-match compares strings for equality; brand voice is about tone, rhythm, and word choice, where many different strings are equally good. Subjective metrics need judgment-based methods.",
  ["Programmatic metrics are right for objective measures like accuracy; the objection is specific to subjective style.",
   "Voice is evaluable, just not by string equality.",
   "Exact-match is cheap; cheap and wrong is still wrong."],
  "The trap AWS set here is the proposal itself: exact-match for style. Match the metric family to the quality type.")

# 5.2 troubleshooting
q("d5","easy","single","5.2 ValidationException",
  "An InvokeModel call to Claude fails with ValidationException. Model access and IAM permissions are verified working. What is the most likely cause?",
  ["The request body does not match Claude's provider-specific schema (for example, a missing anthropic_version or max_tokens field)",
   "The AWS region is down",
   "The model is too popular",
   "The API key expired"],
  [0],
  "With access and permissions ruled out, ValidationException points at the request shape: InvokeModel bodies are provider-specific, and Claude requires its documented fields. Wrong body is the classic cause.",
  ["A regional outage produces different errors, not validation errors.",
   "Popularity causes throttling, not validation failures.",
   "Bedrock uses IAM, not API keys; and auth failures look different."],
  "The trap AWS set here: debugging permissions or networks for a request-body schema error.")

q("d5","easy","single","5.2 AccessDenied region",
  "An application gets AccessDeniedException calling a model that works fine in another region. Permissions are identical. What is the most likely cause?",
  ["The model is not available in this region; the error message is misleading",
   "The IAM policy has a typo",
   "The application needs a VPN",
   "The model was deleted globally"],
  [0],
  "Bedrock returns a misleading AccessDeniedException when a model ID is not available in the calling region. Identical permissions working elsewhere is the tell: availability, not authorization, is the problem.",
  ["A typo would fail in every region, not just this one.",
   "Network paths do not produce authorization-shaped errors.",
   "Global deletion would break the working region too."],
  "The trap AWS set here: trusting the error name. On Bedrock, AccessDenied can mean not available here.")

q("d5","easy","single","5.2 Prepare-agent",
  "A developer adds a new action group to a Bedrock Agent and tests the draft, but the agent never calls the new tool. The agent was not prepared after the change. What is the fix?",
  ["Run prepare-agent to rebuild the agent with the new configuration, moving DRAFT to PREPARED",
   "Retrain the foundation model",
   "Delete and recreate the IAM role",
   "Increase the Lambda timeout"],
  [0],
  "Bedrock Agents only serve the prepared state; configuration edits sit in DRAFT until prepare-agent compiles them. The classic agent ignores new action group bug is always the missed prepare step.",
  ["The model needs no retraining for an agent configuration change.",
   "The IAM role is unrelated to configuration compilation.",
   "Lambda timeouts affect execution duration, not tool visibility."],
  "The trap AWS set here: infrastructure debugging for a missed lifecycle step. Prepare after every change.")

q("d5","medium","single","5.2 Debug order",
  "After a knowledge base re-sync, answers get worse: confident but wrong, on topics that worked before. What should the developer check FIRST?",
  ["Retrieval quality: chunking, embeddings, and relevance, before touching the generation model or temperature",
   "Switch to a larger generation model immediately",
   "Raise the temperature for more creative answers",
   "Rewrite all the system prompts"],
  [0],
  "The GenAI debug order starts at retrieval for RAG failures: re-syncs can change chunking or embeddings, and confident-but-wrong is the signature of broken retrieval feeding a fluent generator. Generation changes come only after retrieval is ruled out.",
  ["A larger model amplifies the same bad retrieval more fluently.",
   "Higher temperature increases fabrication on factual content.",
   "Prompt rewrites do not fix chunks that changed at ingestion."],
  "The trap AWS set here: debugging retrieval failures at the generation layer. Retrieval first, always.")

q("d5","hard","single","5.2 Context overflow",
  "An application stuffs entire 200-page PDFs into prompts. Recently, requests fail or answers ignore the document's later sections. What is the most correct remediation?",
  ["Fix content handling: apply a chunking strategy with retrieval instead of whole-document stuffing, add prompt compression, and analyze truncation",
   "Buy a model with a bigger context window and keep stuffing",
   "Split the PDF randomly into halves",
   "Set temperature to zero"],
  [0],
  "The debug order's first step is content handling: context overflow causes silent truncation (later sections vanish) or failures. Chunking plus retrieval feeds the model only relevant sections, compression trims waste, and truncation analysis confirms what was actually sent.",
  ["A bigger window delays the problem and multiplies cost; the pattern is still broken.",
   "Random halves still overflow and destroy document structure.",
   "Temperature affects randomness, not context limits."],
  "The trap AWS set here: bigger context as the fix. Overflow is a content-handling problem, solved with retrieval and compression.")

q("d5","medium","multi","5.2 Prompt regression",
  "After switching to a new model version, several prompts behave differently. Which TWO steps diagnose this systematically? (Select TWO)",
  ["Compare prompt versions in Prompt Management to isolate what changed",
   "Run the regression test suite over golden datasets to quantify the behavior shift",
   "Raise the temperature to smooth out differences",
   "Delete the old prompt versions",
   "Blame the users' phrasing"],
  [0,1], 2,
  "Systematic diagnosis means isolating the change (version comparison shows exactly what moved) and measuring its impact (regression suites quantify the shift on golden data). Both are evidence-based; everything else is guessing.",
  ["Temperature changes randomness; it cannot diagnose a model-version behavior shift.",
   "Deleting old versions destroys the baseline needed for comparison.",
   "User phrasing did not change; the model version did."],
  "The trap AWS set here: tuning randomness instead of measuring. Diagnose with versions and regression data.")

q("d5","hard","single","5.2 Capacity vs routing",
  "An application correctly invokes its provisioned model ARN, but still throttles when traffic hits 3x the baseline the Provisioned Throughput was sized for. What is the most correct fix?",
  ["Increase Provisioned Throughput model units for the higher baseline, or add on-demand overflow for peaks",
   "Check whether the code uses the base model ID",
   "Decrease the temperature",
   "Switch to batch inference"],
  [0],
  "This is the mirror image of the routing bug: routing is correct this time, so capacity genuinely is the constraint. The fix is more units for a higher sustained baseline, or hybrid on-demand overflow for peaks. Rule out routing first, then size capacity to load.",
  ["The stem states the ARN is already correct; re-checking routing wastes the debugging step.",
   "Temperature does not affect throttling.",
   "Batch inference cannot serve real-time peak traffic."],
  "The trap AWS set here: assuming every PT throttle is the routing bug. Routing is ruled out here, so capacity is the real fix.")

# ================= RENDERER =================
DOMAINS = [
    ("d1", "Domain 1: Foundation Model Integration, Data Management, and Compliance", "31%"),
    ("d2", "Domain 2: Implementation and Integration", "26%"),
    ("d3", "Domain 3: AI Safety, Security, and Governance", "20%"),
    ("d4", "Domain 4: Operational Efficiency and Optimization", "12%"),
    ("d5", "Domain 5: Testing, Validation, and Troubleshooting", "11%"),
]

DIAGRAMS = {
"d1": ("""<div class="ladder">
<div class="rung"><span class="rung-n">1</span><div><b>Prompt engineering</b><span>New format, tone, few-shot, chain-of-thought. No new knowledge.</span></div></div>
<div class="rung"><span class="rung-n">2</span><div><b>RAG / Knowledge Bases</b><span>Private, current, or cited facts the model was not trained on.</span></div></div>
<div class="rung"><span class="rung-n">3</span><div><b>Agents</b><span>Actions: API calls, databases, multi-step tool use, session memory.</span></div></div>
<div class="rung"><span class="rung-n">4</span><div><b>Fine-tuning</b><span>New behavior baked into weights. Labeled data in S3, then usually Provisioned Throughput.</span></div></div>
<div class="rung"><span class="rung-n">5</span><div><b>Custom model</b><span>Last resort. Out of scope for this exam as a build task.</span></div></div>
</div>""",
"Climb in order and stop at the cheapest rung that works.",
["Rung 1 is the default: if the need is only format, tone, or examples, prompt engineering solves it with zero infrastructure.",
 "Rung 2 is for knowledge: documents that change (quarterly policies) or need citations point to RAG with Knowledge Bases.",
 "Rung 3 is for actions: when the task calls APIs, queries databases, or reasons across tools, that is agentic.",
 "Rung 4 is for behavior: a consistent voice or classification repeated millions of times gets baked into weights via fine-tuning.",
 "Rung 5 almost never appears as a correct answer on this exam; distractors love it anyway.",
 "If this ladder breaks (you skip rungs), you pay training costs for a retrieval problem or retraining for a prompt problem."]),
"d2": ("""<table class="matrix">
<tr><th>Need</th><th>Answer</th></tr>
<tr><td>Unified requests across providers, tool use, inline guardrails</td><td><b>Converse / ConverseStream</b></td></tr>
<tr><td>Provider-specific features, embeddings</td><td><b>InvokeModel / InvokeModelWithResponseStream</b></td></tr>
<tr><td>Async, hours OK, cheapest</td><td><b>Batch inference</b> (S3 in, S3 out)</td></tr>
<tr><td>Reserved capacity, latency SLA</td><td><b>Provisioned Throughput</b> (invoke the provisioned ARN)</td></tr>
<tr><td>Real-time token streaming</td><td><b>ConverseStream</b> plus WebSockets or SSE to the client</td></tr>
</table>""",
"Pick the API by matching the row to the scenario's need.",
["Row 1: same code for Claude, Llama, Titan with tool use means Converse, always.",
 "Row 2: embeddings or provider-exotic parameters mean InvokeModel; Converse cannot do embeddings.",
 "Row 3: nobody waiting and hours acceptable means batch at roughly half price.",
 "Row 4: steady baseline plus latency SLA means Provisioned Throughput, and the code must call the provisioned ARN or throttling continues.",
 "Row 5: tokens appearing as generated means ConverseStream; API Gateway timeouts push long streams to WebSockets or SSE.",
 "If this table breaks (wrong row), you get ValidationException from mismatched bodies or throttling from bypassed reservations."]),
"d3": ("""<table class="matrix">
<tr><th>Control</th><th>What it does</th><th>Scenario verb</th></tr>
<tr><td>Content filters</td><td>Toxicity categories plus prompt attack, severity NONE to HIGH</td><td>block profanity, violence, jailbreaks</td></tr>
<tr><td>Denied topics</td><td>Subject-area bans in natural language</td><td>never discuss medical diagnosis</td></tr>
<tr><td>Word filters</td><td>Exact-match blocklists</td><td>never say these brand names</td></tr>
<tr><td>Sensitive info filters</td><td>PII entity detection, block or mask</td><td>redact SSNs</td></tr>
<tr><td>Contextual grounding</td><td>Is the answer supported by the source?</td><td>RAG hallucinations</td></tr>
<tr><td>Automated Reasoning</td><td>Deterministic check against policy rules</td><td>totals must equal line items</td></tr>
</table>""",
"Match the scenario verb in the question stem to the control in the left column.",
["Profanity, violence, or jailbreak language maps to content filters, with prompt attack as its own category.",
 "A ban on discussing a subject (investment advice, diagnoses) maps to denied topics, never to content filters.",
 "Specific exact strings map to word filters; PII patterns map to sensitive info filters, never the reverse.",
 "Is this claim in the source maps to contextual grounding; does this violate the formal rule maps to Automated Reasoning.",
 "The exam's favorite confusion set lives in this table: read the verb, pick the row.",
 "If this table breaks (wrong control), the guardrail deploys but the requirement silently goes unenforced."]),
"d4": ("""<div class="ladder">
<div class="rung"><span class="rung-n">1</span><div><b>On-demand</b><span>Spiky, experimental, unpredictable. Pay per token.</span></div></div>
<div class="rung"><span class="rung-n">2</span><div><b>Prompt caching</b><span>Repeated large static prefixes. Cheaper cached input tokens via cachePoint.</span></div></div>
<div class="rung"><span class="rung-n">3</span><div><b>Batch inference</b><span>Non-interactive, hours OK. About 50 percent cheaper.</span></div></div>
<div class="rung"><span class="rung-n">4</span><div><b>Provisioned Throughput</b><span>Steady baseline, latency SLA, no throttling. Hourly commit.</span></div></div>
<div class="rung"><span class="rung-n">5</span><div><b>Smaller model / cascade</b><span>Route simple queries cheap; escalate hard ones on low confidence.</span></div></div>
</div>""",
"Match the cost lever to the traffic shape and symptom, not to the buzzword.",
["Spiky unpredictable traffic stays on-demand; reserved capacity for bursts wastes money.",
 "The same long system prompt on every call is the prompt caching signature.",
 "Nobody waiting and hours acceptable is batch pricing, roughly half off.",
 "Steady baseline plus throttling or latency SLA is Provisioned Throughput.",
 "Mostly simple queries with some hard ones is a cascade: cheap first, escalate on low confidence.",
 "If this ladder breaks (wrong lever), you pay peak prices in quiet hours or throttle under steady load."]),
"d5": ("""<div class="ladder">
<div class="rung"><span class="rung-n">1</span><div><b>Content handling</b><span>Context overflow: chunking, prompt compression, truncation analysis.</span></div></div>
<div class="rung"><span class="rung-n">2</span><div><b>API integration</b><span>ValidationException means the provider body; misleading AccessDenied means region availability.</span></div></div>
<div class="rung"><span class="rung-n">3</span><div><b>Prompt problems</b><span>Version comparison, systematic refinement, regression suites.</span></div></div>
<div class="rung"><span class="rung-n">4</span><div><b>Retrieval problems</b><span>Embedding quality, chunking, relevance. Retrieval before generation, always.</span></div></div>
<div class="rung"><span class="rung-n">5</span><div><b>Capacity vs routing</b><span>PT throttling: check the provisioned ARN target first, then size units.</span></div></div>
</div>""",
"Debug in this order. Skipping steps is how hours get lost.",
["Step 1 first: whole documents in prompts cause silent truncation; fix with chunking plus retrieval.",
 "Step 2: ValidationException with good permissions is the request body; AccessDenied in one region is availability.",
 "Step 3: changed behavior means version comparison plus regression data, not temperature tuning.",
 "Step 4: confident-but-wrong on RAG is retrieval until proven otherwise; never fix it with a bigger model.",
 "Step 5: PT throttling means check routing to the provisioned ARN before buying more units.",
 "If this order breaks (generation fixed first), you tune the wrong layer while the real bug sits upstream."]),
}

CSS = """
*{box-sizing:border-box}
body{margin:0;background:#F8F7F3;color:#24292F;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.65}
.wrap{display:flex;align-items:flex-start}
.rail{position:sticky;top:0;height:100vh;overflow-y:auto;width:250px;flex:0 0 250px;background:#FFFFFF;border-right:1px solid #E3E0D8;padding:1.2rem 1rem}
.rail h3{font-size:.8rem;text-transform:uppercase;letter-spacing:.06em;color:#5C6570;margin:1.2rem 0 .4rem}
.rail h3:first-child{margin-top:0}
.rail a{display:block;color:#1F5FBF;text-decoration:none;padding:.28rem .4rem;border-radius:6px;font-size:.92rem}
.rail a:hover{background:#EFF0EA}
.rail .exam-link{font-weight:700}
.main{flex:1;min-width:0;padding:2.5rem 2rem;max-width:80ch;margin:0 auto}
h1{font-size:1.9rem;line-height:1.25;margin:0 0 .5rem}
h2{font-size:1.35rem;margin:2.5rem 0 1rem;padding-top:1rem;border-top:2px solid #E3E0D8}
h2:first-of-type{border-top:none;padding-top:0}
.sub{color:#5C6570;margin:0 0 1.5rem}
.badge{display:inline-block;font-size:.72rem;font-weight:700;padding:.12rem .55rem;border-radius:999px;margin-right:.4rem;vertical-align:middle}
.b-easy{background:#E8F3E8;color:#2E7D32}.b-med{background:#FBF3E4;color:#A15C07}.b-hard{background:#FBEAEA;color:#B3261E}
.b-dom{background:#E7EFFC;color:#1F5FBF}.b-fmt{background:#EFF0EA;color:#24292F}
.q{background:#FFFFFF;border:1px solid #E3E0D8;border-radius:10px;padding:1.2rem 1.3rem;margin:1.2rem 0}
.q-head{margin-bottom:.6rem}
.q-id{font-size:.78rem;color:#5C6570;font-weight:700}
.q-stem{margin:.5rem 0 .8rem}
ol.opts{list-style:none;padding:0;margin:0 0 .6rem}
ol.opts li{padding:.45rem .7rem;border:1px solid #E3E0D8;border-radius:8px;margin:.35rem 0;background:#F8F7F3}
ol.opts li b{color:#1F5FBF;margin-right:.5rem}
details.ans{margin-top:.6rem;border:1px solid #E3E0D8;border-radius:8px;background:#F8F7F3}
details.ans summary{cursor:pointer;padding:.6rem .9rem;font-weight:700;color:#1F5FBF}
details.ans .ans-body{padding:.2rem .9rem 1rem}
.correct-line{font-weight:700;color:#2E7D32}
.why-wrong{margin:.6rem 0}
.why-wrong li{margin:.3rem 0}
.trap{background:#FBF3E4;border-left:4px solid #A15C07;padding:.6rem .9rem;margin-top:.8rem;border-radius:0 8px 8px 0}
.trap b{color:#A15C07}
.ladder{margin:1rem 0}
.rung{display:flex;gap:.8rem;align-items:flex-start;background:#FFFFFF;border:1px solid #E3E0D8;border-radius:8px;padding:.7rem .9rem;margin:.45rem 0}
.rung-n{flex:0 0 1.7rem;height:1.7rem;border-radius:50%;background:#1F5FBF;color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center;font-size:.85rem}
.rung b{display:block}
.rung span span{color:#5C6570;font-size:.92rem}
.walk{margin:.6rem 0 1.6rem}
.walk li{margin:.3rem 0}
table.matrix{width:100%;border-collapse:collapse;margin:1rem 0;background:#FFFFFF;font-size:.93rem}
table.matrix th,table.matrix td{border:1px solid #E3E0D8;padding:.55rem .7rem;text-align:left;vertical-align:top}
table.matrix th{background:#163D7A;color:#fff}
table.matrix tr:nth-child(even) td{background:#F8F7F3}
table.mock{width:100%;border-collapse:collapse;background:#FFFFFF;font-size:.9rem;margin:1rem 0}
table.mock th,table.mock td{border:1px solid #E3E0D8;padding:.45rem .6rem;text-align:left}
table.mock th{background:#163D7A;color:#fff}
table.mock tr:nth-child(even) td{background:#F8F7F3}
.note{background:#E7EFFC;border:1px solid #1F5FBF;border-radius:8px;padding:.8rem 1rem;margin:1.2rem 0}
code{background:#EFF0EA;padding:.1rem .35rem;border-radius:4px;font-size:.9em}
pre{background:#EFF0EA;padding:.9rem 1rem;border-radius:8px;overflow-x:auto;font-size:.85rem}
@media(max-width:900px){.rail{display:none}.main{padding:1.2rem}}
"""

def letters(idxs):
    return ", ".join("ABCDE"[i] for i in sorted(idxs))

def validate():
    assert len(QUESTIONS) >= 120, f"only {len(QUESTIONS)} questions"
    for i, x in enumerate(QUESTIONS):
        assert len(x["opts"]) == (4 if x["fmt"]=="single" else 5), f"Q{i} opt count"
        assert len(x["wrongs"]) == len(x["opts"]) - len(x["ans"]), f"Q{i} wrongs count"
        assert all(0 <= a < len(x["opts"]) for a in x["ans"]), f"Q{i} ans range"
        assert x["fmt"]=="single" and len(x["ans"])==1 or x["fmt"]=="multi" and len(x["ans"])>=2, f"Q{i} ans/fmt"
        for bad in ["\u2014","\u2013"]:
            for k in ("stem","why","trap"):
                assert bad not in x[k], f"Q{i} dash in {k}"
            for o in x["opts"]+x["wrongs"]:
                assert bad not in o, f"Q{i} dash in opt/wrong"
    print(f"VALID: {len(QUESTIONS)} questions", file=sys.stderr)

def render_question(x, num):
    qid = x["qid"]
    diff_badge = {"easy":'<span class="badge b-easy">EASY</span>',
                  "medium":'<span class="badge b-med">MEDIUM</span>',
                  "hard":'<span class="badge b-hard">HARD</span>'}[x["diff"]]
    fmt_badge = ('<span class="badge b-fmt">ONE ANSWER</span>' if x["fmt"]=="single"
                 else f'<span class="badge b-fmt">SELECT {x["nsel"]}</span>')
    dom_badge = f'<span class="badge b-dom">{x["dom"].upper()}</span>'
    opts = "\n".join(f'<li><b>{"ABCDE"[i]}</b>{html.escape(o)}</li>' for i, o in enumerate(x["opts"]))
    distractor_idxs = [i for i in range(len(x["opts"])) if i not in x["ans"]]
    wrong_items = "\n".join(
        f"<li><b>{'ABCDE'[i]}</b> is wrong: {html.escape(w)}</li>"
        for i, w in zip(distractor_idxs, x["wrongs"]))
    return f"""<div class="q" id="{qid}">
<div class="q-head">{dom_badge}{diff_badge}{fmt_badge} <span class="q-id">{qid} &middot; {html.escape(x['topic'])}</span></div>
<p class="q-stem"><b>Q{num}.</b> {html.escape(x['stem'])}</p>
<ol class="opts">{opts}</ol>
<details class="ans"><summary>Reveal answer and explanation</summary>
<div class="ans-body">
<p class="correct-line">Correct answer: {letters(x['ans'])}</p>
<p><b>Why {letters(x['ans'])} is correct:</b> {html.escape(x['why'])}</p>
<ul class="why-wrong">{wrong_items}</ul>
<div class="trap"><b>The trap AWS set here:</b> {html.escape(x['trap'][len('The trap AWS set here: '):] if x['trap'].startswith('The trap AWS set here:') else x['trap'])}</div>
</div></details>
</div>"""

def build():
    validate()
    # assign qids per domain
    counters = {}
    for x in QUESTIONS:
        counters[x["dom"]] = counters.get(x["dom"], 0) + 1
        x["qid"] = f"q-{x['dom']}-{counters[x['dom']]:03d}"
    ids = [x["qid"] for x in QUESTIONS]
    assert len(set(ids)) == len(ids), "duplicate qids"

    parts = []
    parts.append("<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>")
    parts.append("<meta name='viewport' content='width=device-width,initial-scale=1'>")
    parts.append("<title>AWS AIP-C01 Question Bank: 140 Exam-Style Questions plus 75-Question Mock Exam</title>")
    parts.append(f"<style>{CSS}</style></head><body><div class='wrap'>")

    # rail
    rail = ["<nav class='rail'><h3>Question Bank</h3><a href='#top'>How to use this bank</a>"]
    for d, title, wt in DOMAINS:
        rail.append(f"<a href='#sec-{d}'>{title.split(':')[0]} ({wt})</a>")
    rail.append("<h3>Mock Exam</h3><a class='exam-link' href='#mock'>75-Question Mock Exam</a>")
    rail.append("<a href='#mock-key'>Answer Key</a><a href='#scoring'>Scoring Guide</a></nav>")
    parts.append("".join(rail))

    parts.append("<main class='main' id='top'>")
    parts.append("<h1>AWS AIP-C01 Question Bank</h1>")
    parts.append("<p class='sub'>140 exam-style questions across all five domains, weighted like the real exam, plus a 75-question mock exam. Generic content only.</p>")
    parts.append("""<div class="note"><b>How to use this bank.</b> Read each question, pick your answer, then open
<q>Reveal answer and explanation</q> to check. Every explanation covers why the correct answer is right, why each
distractor is wrong, and the trap AWS set. <b>Multiple-response questions are all-or-nothing:</b> on the real exam you
must select every correct option (and no incorrect ones) to earn credit. There is no partial credit and no penalty for
guessing, so never leave a question blank.</div>""")
    parts.append("""<div class="note"><b>Maarek-style rule of thumb.</b> When torn between plausible options, prefer the
more managed, more serverless, lower-operational-overhead answer. Custom builds are almost never correct unless the
scenario explicitly requires something no managed service does.</div>""")

    # domain sections
    n = 0
    for d, title, wt in DOMAINS:
        dq = [x for x in QUESTIONS if x["dom"] == d]
        parts.append(f"<h2 id='sec-{d}'>{html.escape(title)} <span class='sub'>({wt} of the exam, {len(dq)} questions)</span></h2>")
        fig, cap, walk = DIAGRAMS[d]
        parts.append(f"<p><b>Decision reference.</b> {html.escape(cap)}</p>")
        parts.append(fig)
        parts.append("<p><b>How to read this diagram.</b></p><ol class='walk'>" +
                     "".join(f"<li>{html.escape(w)}</li>" for w in walk) + "</ol>")
        for x in dq:
            n += 1
            parts.append(render_question(x, n))

    # mock exam: weighted, deterministic shuffle
    rng = random.Random(42)
    want = {"d1": 23, "d2": 20, "d3": 15, "d4": 9, "d5": 8}
    pool = []
    for d, cnt in want.items():
        dq = [x for x in QUESTIONS if x["dom"] == d]
        rng.shuffle(dq)
        pool.extend(dq[:cnt])
    rng.shuffle(pool)
    assert len(pool) == 75

    parts.append("<h2 id='mock'>75-Question Full Mock Exam</h2>")
    parts.append("""<div class="note"><b>Exam conditions.</b> 75 questions, 180 minutes on the real exam. Work through the
75 questions below in order without opening the answers. Each row links to the question; attempt it, reveal the
explanation to check yourself, then come back. Track your score with the scoring guide at the end.</div>""")
    rows = []
    for i, x in enumerate(pool, 1):
        rows.append(f"<tr><td><b>{i}</b></td><td><a href='#{x['qid']}'>{x['qid']} (Q bank #{QUESTIONS.index(x)+1})</a></td>"
                    f"<td>{x['dom'].upper()}</td><td>{x['diff'].capitalize()} / {'one answer' if x['fmt']=='single' else 'select '+str(x['nsel'])}</td></tr>")
    parts.append("<table class='mock'><tr><th>Mock #</th><th>Question</th><th>Domain</th><th>Type</th></tr>" + "".join(rows) + "</table>")

    parts.append("<h2 id='mock-key'>Mock Exam Answer Key</h2>")
    parts.append("<p>Check your answers here, then follow the link back to the full explanation for any you missed.</p>")
    krows = []
    for i, x in enumerate(pool, 1):
        krows.append(f"<tr><td><b>{i}</b></td><td><b>{letters(x['ans'])}</b></td><td>{x['dom'].upper()}</td>"
                     f"<td><a href='#{x['qid']}'>explanation</a></td></tr>")
    parts.append("<table class='mock'><tr><th>Mock #</th><th>Answer</th><th>Domain</th><th>Explanation</th></tr>" + "".join(krows) + "</table>")

    parts.append("""<h2 id="scoring">Scoring Guide</h2>
<div class="note"><b>How to score yourself.</b> Count one point per question only if you selected every correct option
and nothing else (multiple-response is all-or-nothing, exactly like the real exam). The real exam uses scaled scoring
(100 to 1000, pass at 750) with compensatory scoring across domains, so there is no official raw-score conversion.
As a readiness rule of thumb, aim for <b>80% or higher (60 of 75)</b> under timed conditions before booking the exam.
Below 70%, revisit the domains you missed most and re-attempt their bank questions.</div>""")

    parts.append("</main></div></body></html>")
    out = "\n".join(parts)
    # final safety: no em/en dashes, no gradients, no external refs
    assert "\u2014" not in out and "\u2013" not in out, "dash found"
    assert "gradient" not in out.lower(), "gradient found"
    assert "http://" not in out and "https://" not in out, "external url found"
    # anchor check
    anchors = set(re.findall(r'href=\'#([a-z0-9\-]+)\'', out))
    defined = set(re.findall(r'id=["\']([a-z0-9\-]+)["\']', out))
    missing = anchors - defined
    assert not missing, f"missing anchors: {missing}"
    with open("/home/hatch/workspace/your_files/aws-aip-c01-cert/volume-question-bank.html", "w") as f:
        f.write(out)
    print(f"WROTE {len(out)} bytes", file=sys.stderr)

if __name__ == "__main__":
    build()

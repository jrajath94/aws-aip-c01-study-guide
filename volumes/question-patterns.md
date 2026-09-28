---
slug: volume-question-patterns
file: volume-question-patterns.html
title: "AWS AIP-C01: Question Patterns"
label: "Question Patterns · How AWS Asks"
track: aipc01
---

# AWS AIP-C01: Question Patterns {#aws-aip-c01-question-patterns}

81 original practice questions across all five domains, built from the question patterns AWS actually uses. Formats: matching 3, mc 63, mr 12, ordering 3. Every question shows the trap AWS set and hides the answer until you ask for it. Last verified against AWS documentation: 2026-09-28.

## How AWS Asks: the 6 question patterns {#how-aws-asks-the-6-question-patterns}

### Pattern 1: Constraint extraction {#pattern-1-constraint-extraction}

Every stem hides 2 to 4 hard constraints (cost, latency, no ML team, no redeploy, region lock). The correct answer is the only option that satisfies ALL of them. Method: underline each constraint before reading options, then eliminate any option that violates even one.

### Pattern 2: MOST correct, not merely correct {#pattern-2-most-correct-not-merely-correct}

Two or three options will technically work. The winner is decided by tiebreakers in this order: managed service over custom build, cheaper over pricier at the same quality, simpler architecture over complex, AWS-native over third-party. When torn, ask: which option would an AWS solutions architect defend in a review?

### Pattern 3: Ordering and lifecycle {#pattern-3-ordering-and-lifecycle}

Steps must follow the real service lifecycle: configure, then prepare, then test; select a model before customizing it; scope before building. Any option that inverts a lifecycle dependency is wrong on sight.

### Pattern 4: Vocabulary precision {#pattern-4-vocabulary-precision}

AWS tests whether you know which lever solves which problem: inference profiles (availability and resilience), prompt routers (cost by complexity), Provisioned Throughput (reserved capacity), ApplyGuardrail (standalone policy checks), returnControl (human gates). If two options sound similar, the difference is one precise term.

### Pattern 5: Managed-first and the ladder {#pattern-5-managed-first-and-the-ladder}

Default to the managed service and climb the capability ladder only until the requirement is met: prompt engineering, then RAG, then agents, then fine-tuning. Options that jump straight to training or custom builds fail the overhead filter.

### Pattern 6: Wrong-plane distractors {#pattern-6-wrong-plane-distractors}

Distractors name real services doing the wrong job: Guardrails for extraction, knowledge bases for live API calls, CloudFormation for runtime config, encryption for network isolation. Ask of every option: is this service's actual job the job the stem needs?

## Exam surface: what each domain really tests {#exam-surface-what-each-domain-really-tests}

| Domain | Weight | What they actually test |
|---|---|---|
| D1 | 31% | RAG over fine-tuning for fresh documents, chunking and embedding tradeoffs, Converse API fields, prompt caching, model switching without redeploys |
| D2 | 26% | Agent lifecycle (configure, prepare, test), action groups with Lambda or OpenAPI, knowledge base grounding, returnControl for approvals, trace for debugging |
| D3 | 20% | Guardrail control types, denied topics vs word filters vs PII filters, defense in depth on inputs and outputs, faithfulness and citation metrics, LLM-as-a-judge bias |
| D4 | 12% | LoRA vs full fine-tuning, catastrophic forgetting, data curation order, distributed training vocabulary, SageMaker lineage (Registry plus Experiments) |
| D5 | 11% | Bedrock data-use posture (no training on customer data), VPC isolation, human-in-the-loop for high-stakes outputs, CloudWatch Bedrock metrics, erasure covering derived data |

## Tactics: how to attack each format {#tactics-how-to-attack-each-format}

- **Multiple choice:** extract constraints first, then eliminate. Never pick an option that violates a stated constraint, even if it sounds sophisticated.
- **Multiple response:** evaluate each option independently against the constraints. The two correct answers each stand alone; do not look for pairs that sound good together.
- **Ordering:** anchor the first and last steps (what must come before everything, what must come last), then fill the middle. Lifecycle dependencies decide ties.
- **Matching:** match the most distinctive pair first to shrink the field, then the next. Never match by vague association; each pair has one precise mechanism.
- **Time management:** 75 questions in 180 minutes is about 2.4 minutes per question. If an option violates a constraint on sight, eliminate and move on.

## Trap catalog: the 15 traps AWS reuses {#trap-catalog-the-15-traps-aws-reuses}

1. **Lambda 15-minute timeout:** any option with a Lambda waiting, sleeping, or polling for a long task dies. Go async or use Step Functions.
2. **Custom code vs managed:** when the stem says no ML team or least effort, custom builds lose to Bedrock managed features.
3. **Knowledge base scope:** knowledge bases serve documents. They never call APIs, never enforce access control, never execute actions.
4. **Fine-tuning for fresh data:** changing documents or a need for citations means RAG, never fine-tuning.
5. **Capacity confusion set:** inference profiles for availability, prompt routers for cost by complexity, Provisioned Throughput for reserved capacity. Do not mix them.
6. **Guardrails wrong plane:** guardrails filter content. They do not extract data, enforce tenant isolation, or replace IAM.
7. **Ladder jumping:** the cheapest option that meets the requirement wins. Premium features without a stated need lose.
8. **CloudFormation for runtime config:** a stack update is a deployment. Runtime switching without redeploys means AppConfig.
9. **ElastiCache as storage:** ElastiCache is ephemeral caching. Durable vectors live in a vector store.
10. **Residency blindness:** cross-region failover is wrong when the stem requires data residency. Check the region constraint first.
11. **Prompt Management plus guardrailConfig:** Converse rejects that combination. ApplyGuardrail standalone is the workaround.
12. **Missing prepare step:** agent config changes need prepare before testing. Changed-but-same-behavior means prepare was skipped.
13. **Misleading AccessDenied:** check model availability in the region before debugging permissions.
14. **Converse for embeddings:** Converse is text generation only. Embeddings go through InvokeModel.
15. **Built-in safety is enough:** alignment and guardrails never transfer the deployer's responsibility to evaluate and govern.

## D1: Develop and Optimize GenAI Apps with Bedrock {#D1}

Q1

Easy

Multiple choice

D1: Develop and Optimize GenAI Apps with Bedrock

A company wants a GenAI assistant that answers questions from its internal HR handbook. The CTO will only fund production work after the team demonstrates the approach on real documents. The team has two AWS developers and no ML specialists. What should the team do first?

1. A.Run a proof of concept on Amazon Bedrock with on-demand invocation over a sample of the handbook documents
2. B.Fine-tune a foundation model on the full handbook and purchase Provisioned Throughput before any testing
3. C.Build a custom training pipeline on Amazon SageMaker AI to pre-train a model on HR text
4. D.Deploy a multi-region production architecture with cross-region inference profiles

The trap AWS set here:

Pattern 1: the stem says 'demonstrates the approach first'. Any option that commits production spend before validation violates that constraint.

Q2

Medium

Multiple response

D1: Develop and Optimize GenAI Apps with Bedrock

A platform team wants every product squad to ship GenAI features in a consistent, reviewable way. Which TWO practices align with the AWS Well-Architected Generative AI Lens guidance for standardized, reusable components? (Select TWO)

*Select 2.*

1. A.Build prompt templates, model routing layers, guardrail policies, and evaluation harnesses once and reuse them across squads
2. B.Let each squad pick its own models, prompts, and safety controls with no shared review so teams move faster
3. C.Run architecture design reviews against the Generative AI Lens before production deployments
4. D.Require every squad to fine-tune its own foundation model so each feature has a dedicated model
5. E.Standardize on invoking models only through raw HTTP calls with hardcoded credentials in each service

The trap AWS set here:

Pattern 2: option B sounds agile ('move faster') but directly contradicts the standardization constraint in the stem.

Q3

Medium

Ordering

D1: Develop and Optimize GenAI Apps with Bedrock

Place these Generative AI lifecycle stages in the order the Well-Architected Generative AI Lens presents them, from first to last.

1. 1.Scoping: define the business problem and success criteria
2. 2.Model selection: choose and evaluate candidate foundation models
3. 3.Integration: connect the solution to applications and data
4. 4.Deployment and continuous improvement: release, monitor, and iterate
5. 5.Customization: adapt the model with RAG, agents, or fine-tuning as needed

order answer: 1 then 2 then 5 then 3 then 4

The trap AWS set here:

Pattern 3: watch for 'customization before model selection' orderings; the Lens selects first, then customizes.

Q4

Medium

Multiple choice

D1: Develop and Optimize GenAI Apps with Bedrock

A support assistant must answer from 5,000 policy documents that are reissued every quarter. The team debates fine-tuning a model on the documents versus building retrieval over them. Which approach is MOST correct, and why?

1. A.Retrieval-augmented generation over a knowledge base, because quarterly updates only require re-syncing documents, and answers can cite sources
2. B.Fine-tuning, because a fine-tuned model memorizes the documents and never needs the documents at inference time
3. C.Fine-tuning, because retrieval cannot handle 5,000 documents
4. D.Prompt engineering alone, because 5,000 documents fit in a single prompt

The trap AWS set here:

Pattern 6, trap 7: fine-tuning when the scenario says documents update regularly or answers must cite sources. That is RAG.

Q5

Medium

Multiple choice

D1: Develop and Optimize GenAI Apps with Bedrock

A company is launching a customer FAQ assistant in 30 languages. The team is debating whether to train a custom multilingual model. What is the MOST correct guidance?

1. A.Use Bedrock foundation models that already support the required languages; training a custom model for language coverage alone is unnecessary
2. B.Train a custom multilingual model because only custom models can handle 30 languages reliably
3. C.Build 30 separate single-language assistants, one per language, to avoid multilingual models entirely
4. D.Use machine translation on every request instead of a multilingual model because translation is always cheaper

The trap AWS set here:

Pattern 5: training a custom model sounds thorough, but it fails the operational-overhead and managed-first filters.

Q6

Easy

Multiple choice

D1: Develop and Optimize GenAI Apps with Bedrock

Operations must switch a production assistant between three foundation models without code deployments or restarts. Model identifiers are currently hardcoded in the application. Which change meets the requirement with the least operational overhead?

1. A.Store model identifiers in AWS AppConfig as runtime configuration, with a Lambda routing layer reading the current value and API Gateway fronting a stable endpoint
2. B.Store model identifiers in CloudFormation parameters and update the stack whenever operations wants a switch
3. C.Publish the model identifiers to an EventBridge event bus and have the application poll for events
4. D.Email the new model identifier to the on-call engineer, who updates the code and redeploys

The trap AWS set here:

Pattern 1, trap 8: CloudFormation for runtime switching. A stack update is a deployment, not runtime configuration.

Q7

Hard

Matching

D1: Develop and Optimize GenAI Apps with Bedrock

Match each mechanism to the problem it solves.

| Items | Descriptions |
|---|---|
| **1.** Cross-region inference profile | **C.** A model has limited regional availability; the application needs automatic failover and higher effective quotas |
| **2.** Prompt router (model router) | **B.** Simple prompts should use a cheap model and complex prompts a flagship model, routed by prompt complexity |
| **3.** Provisioned Throughput | **A.** Steady, predictable traffic needs reserved capacity with latency guarantees and throttling protection |

The trap AWS set here:

Pattern 4: this is the exam's favorite confusion set (trap 5). Memorize which lever solves which problem.

Q8

Hard

Multiple choice

D1: Develop and Optimize GenAI Apps with Bedrock

An application calls a foundation model with its base model ID and receives an error stating that invocation with on-demand throughput is not supported for that model ID, suggesting an inference profile instead. The model works in the console. What is the MOST correct fix?

1. A.Invoke the model through its inference profile ID (for example, a geographic profile such as us. or a global profile) instead of the bare model ID
2. B.Increase the Provisioned Throughput units on the model
3. C.Add exponential backoff retries around the same base model ID call
4. D.Request a quota increase for on-demand throughput in the region

The trap AWS set here:

Pattern 6: reaching for retries or quota increases when the error message names the fix. Read the error.

Q9

Medium

Multiple choice

D1: Develop and Optimize GenAI Apps with Bedrock

A team fully fine-tunes a large open model every week to keep a ticket-classification behavior current. Training costs are large and each run risks regressions. The task is narrow: classify tickets into 40 categories. What is the MOST correct change?

1. A.Switch to parameter-efficient fine-tuning with LoRA adapters, version the adapters in SageMaker Model Registry, and deploy through an automated pipeline with rollback
2. B.Continue full fine-tuning but run it daily so the model is never stale
3. C.Replace fine-tuning with a larger base model and hope the behavior emerges
4. D.Fine-tune once and never update the model again to avoid regression risk

The trap AWS set here:

Pattern 5: full fine-tuning weekly is the expensive habit; the MOST-correct answer attacks both cost (adapters) and safety (registry plus rollback).

Q10

Hard

Multiple response

D1: Develop and Optimize GenAI Apps with Bedrock

During a regional degradation, a flagship model becomes slow and throttled. The product requirement is that the assistant keeps answering, even at reduced quality, with no manual intervention. Which TWO design choices meet this requirement? (Select TWO)

*Select 2.*

1. A.A Step Functions circuit breaker that detects repeated model failures and routes traffic to a smaller fallback model or cached responses
2. B.Hardcoding the flagship model ID in every client so behavior is predictable during the incident
3. C.Graceful degradation: fall back to a cheaper model or a recent cached response when the primary model fails
4. D.Waiting for the region to recover while returning errors to users, to preserve answer quality
5. E.Deploying the entire application on EC2 instances in a second region with a load balancer

The trap AWS set here:

Pattern 2: option E looks like resilience engineering, but it solves regional instance failover, not model degradation, and it is a custom build.

Q11

Easy

Multiple choice

D1: Develop and Optimize GenAI Apps with Bedrock

A pipeline must ingest 20,000 vendor invoices per day (PDFs and photos) and extract the same set of fields from each: invoice number, date, line items, and total. Which approach is MOST correct?

1. A.Use Bedrock Data Automation with a custom blueprint defining the required fields, producing structured output per document
2. B.Use Bedrock Guardrails to read the invoice totals out of the documents
3. C.Use Amazon Kendra to extract the fields, since Kendra is the extraction service
4. D.Have a Lambda function call a foundation model with a free-form prompt and parse whatever text comes back with string splitting

The trap AWS set here:

Pattern 6: Guardrails for extraction. Guardrails filter; they never extract.

Q12

Medium

Multiple choice

D1: Develop and Optimize GenAI Apps with Bedrock

A pipeline converts thousands of support call recordings into text with Amazon Transcribe before a foundation model analyzes them. Product names and internal acronyms are consistently mistranscribed. What is the MOST correct fix?

1. A.Add a custom vocabulary to Transcribe with the product names, acronyms, and domain terms
2. B.Switch the transcription to Bedrock Data Automation because Transcribe cannot handle audio
3. C.Increase the foundation model's temperature so it guesses the intended words creatively
4. D.Route the audio through Amazon Translate first to normalize the language

The trap AWS set here:

Pattern 1: fix the failure at the layer where it occurs. The transcript is wrong, so tune transcription, not the downstream model.

Q13

Easy

Multiple choice

D1: Develop and Optimize GenAI Apps with Bedrock

A startup is building a retrieval prototype over 50,000 internal documents. Cost must stay minimal during development, and query volume is low. Which vector store choice is MOST correct for this stage?

1. A.Amazon S3 Vectors, which is the cost-efficient option suited to smaller-scale and development workloads
2. B.Amazon OpenSearch Serverless with a large provisioned collection sized for peak production traffic
3. C.A self-managed vector database on EC2 with EBS volumes for maximum control
4. D.Amazon ElastiCache, because in-memory retrieval is fastest and the data persists there

The trap AWS set here:

Pattern 5: match the store to the stage. Cost-sensitive prototype points to S3 Vectors, not the production-grade default.

Q14

Medium

Multiple choice

D1: Develop and Optimize GenAI Apps with Bedrock

A knowledge base must answer questions that need both keyword precision (exact product codes) and semantic understanding (natural-language descriptions). Retrieved passages sometimes match keywords but do not answer the question. Which retrieval improvement is MOST correct?

1. A.Enable hybrid search combining vector and keyword retrieval, and add a rerank model to score candidates by true relevance
2. B.Switch to a larger generation model so answers sound more confident
3. C.Increase the chunk overlap to 90 percent so every chunk contains every keyword
4. D.Disable vector search and use keyword search only, since keywords are precise

The trap AWS set here:

Pattern 1: the failure is retrieval quality ('match keywords but do not answer'), so the fix must be in retrieval, not generation.

Q15

Medium

Multiple choice

D1: Develop and Optimize GenAI Apps with Bedrock

A company runs one knowledge base shared by three subsidiaries. Each subsidiary's documents must be invisible to the others, enforced by the platform, not by asking the model nicely. What is the MOST correct design?

1. A.Separate knowledge bases per subsidiary with IAM-scoped access, so isolation is enforced by access control
2. B.One shared knowledge base with a system prompt instructing the model to only answer about the caller's subsidiary
3. C.One shared knowledge base with document filenames prefixed by subsidiary name
4. D.One shared knowledge base and a post-processing Lambda that deletes sentences mentioning other subsidiaries

The trap AWS set here:

Pattern 6, trap 6: one shared KB with prompt-level 'access control'. The exam always demands real isolation.

Q16

Medium

Multiple response

D1: Develop and Optimize GenAI Apps with Bedrock

A product catalog changes weekly. The RAG assistant must answer from the current catalog without manual re-ingestion work each week. Which TWO choices form the MOST correct design? (Select TWO)

*Select 2.*

1. A.Configure the knowledge base data source with a scheduled sync so catalog changes are ingested automatically
2. B.Reload the entire catalog by hand every Monday morning before business hours
3. C.Store the catalog in S3 as the knowledge base data source so syncs pick up new versions
4. D.Fine-tune the model on each weekly catalog snapshot so the knowledge is in the weights
5. E.Delete and recreate the knowledge base every week to guarantee freshness

The trap AWS set here:

Pattern 2: options B and E both 'work' in a brute-force sense but violate the automation constraint; the exam rewards the managed sync.

Q17

Medium

Multiple choice

D1: Develop and Optimize GenAI Apps with Bedrock

A RAG system ingests API reference documentation with deeply nested sections: service, resource, operation, parameters, examples. Fixed-size chunking keeps splitting parameter tables away from their operations. Which chunking strategy is MOST correct?

1. A.Hierarchical chunking, so small child chunks match precisely while parent chunks preserve the surrounding section context
2. B.Semantic chunking, because it is always the best strategy regardless of cost
3. C.Fixed-size chunking with zero overlap to keep chunks small and fast
4. D.No chunking, treating each whole document as a single chunk

The trap AWS set here:

Pattern 5: 'semantic is always best' is the tempting overgeneralization; structured docs point to hierarchical.

Q18

Hard

Multiple choice

D1: Develop and Optimize GenAI Apps with Bedrock

A team ingests a large marketing blog archive into a knowledge base. Retrieval quality is acceptable with fixed-size chunking, but the team is considering semantic chunking for a small quality gain. Ingestion cost is a concern. What is the MOST correct guidance?

1. A.Stay with fixed-size chunking; semantic chunking costs more at ingestion and the gain does not justify it for this corpus
2. B.Switch to semantic chunking immediately because it is the premium option and cost does not matter
3. C.Switch to hierarchical chunking because blogs are hierarchical documents
4. D.Disable chunking and rely on the model's long context window instead

The trap AWS set here:

Pattern 5, trap 7-adjacent: the ladder principle applies to chunking too. Stop at the cheapest step that works.

Q19

Medium

Multiple choice

D1: Develop and Optimize GenAI Apps with Bedrock

A team stores 2 million text chunks as embeddings. They compare Titan Text Embeddings v2 at 1024 dimensions versus 256 dimensions. Storage cost matters and retrieval quality must stay acceptable. Which statement is MOST correct?

1. A.256 dimensions use roughly one quarter of the storage of 1024 dimensions, so test whether the smaller size keeps quality acceptable before committing to 1024
2. B.Dimension count has no effect on storage or cost, so always use 1024
3. C.256 dimensions are always strictly better because smaller is faster
4. D.Embedding dimensions can be changed any time without re-ingesting the vectors

The trap AWS set here:

Pattern 1: the stem gives you both constraints (cost and quality). The correct answer is the only one that honors both instead of maximizing one.

Q20

Medium

Multiple choice

D1: Develop and Optimize GenAI Apps with Bedrock

Users ask multi-part questions like 'What is the return window for opened electronics, and how do I start a return from the mobile app?' Retrieval returns passages about only one part. Which query-handling improvement is MOST correct?

1. A.Decompose the query with a Lambda function into sub-questions, retrieve for each, then synthesize the answer
2. B.Increase the number of retrieved chunks from 5 to 50 and hope both parts appear
3. C.Switch the embedding model to a larger one so multi-part queries embed better
4. D.Tell users to ask only one question at a time through input validation

The trap AWS set here:

Pattern 1: retrieve-then-synthesize per sub-question. The trap options attack the wrong layer (embeddings, chunk counts) or the user.

Q21

Easy

Multiple choice

D1: Develop and Optimize GenAI Apps with Bedrock

A knowledge base covers documents in English, Spanish, and Japanese. Retrieval quality on non-English documents is poor with the current embeddings. Which embedding choice is MOST correct?

1. A.Cohere Embed multilingual, which is designed for multilingual retrieval across languages
2. B.Titan Text Embeddings v1 at 1536 dimensions, because more dimensions fix language coverage
3. C.An English-only embedding model with query translation at retrieval time
4. D.Keyword search only, abandoning embeddings for non-English content

The trap AWS set here:

Pattern 6: dimension count confused with capability. Dimensions trade cost and precision; language coverage comes from the model's training.

Q22

Medium

Multiple response

D1: Develop and Optimize GenAI Apps with Bedrock

Marketing rewrites the assistant's tone guidelines every few weeks. Every change currently requires a code deployment, and compliance needs an audit trail of who changed which prompt and when. Which TWO capabilities solve both problems? (Select TWO)

*Select 2.*

1. A.Bedrock Prompt Management versions, which create immutable snapshots of each prompt for audit and rollback
2. B.Hardcoding the new tone into the application code on every change, with git history as the audit trail
3. C.AWS CloudTrail logging of prompt management API calls, showing who changed what and when
4. D.Storing prompts in an engineer's laptop notes and pasting them into the console when needed
5. E.Disabling all prompt changes after launch so no audit trail is needed

The trap AWS set here:

Pattern 2: option B is half-right (git is an audit trail) but it preserves the redeploy pain the stem explicitly wants gone.

Q23

Hard

Multiple choice

D1: Develop and Optimize GenAI Apps with Bedrock

A team needs a fixed four-step document pipeline: extract text, classify the document, summarize it, then write the summary to a database. A compliance officer must approve the summary before it is stored, and the approval can take hours. Which orchestration choice is MOST correct?

1. A.AWS Step Functions, because the workflow has fixed steps plus a long human-approval wait that exceeds Lambda limits
2. B.Bedrock Prompt Flows, because the pipeline is prompt-centric and approvals can be added as nodes
3. C.Bedrock Agents, because agents handle multi-step reasoning autonomously
4. D.A single Lambda function that sleeps until the officer approves

The trap AWS set here:

Pattern 5: three plausible orchestrators, but only Step Functions handles fixed steps plus long human waits. Match the tool to the workflow shape.

Q24

Medium

Multiple choice

D1: Develop and Optimize GenAI Apps with Bedrock

An application needs the model to call a `get_order_status` function with a typed `order_id` parameter during conversations, working identically across Claude, Llama, and Titan. Which approach is MOST correct?

1. A.Use the Converse API with toolConfig declaring the function and its parameters, letting each model use the unified tool-use format
2. B.Describe the function in the prompt text and parse the model's free-form reply with regular expressions
3. C.Use InvokeModel with a hand-built provider-specific body per model, duplicating the tool declaration three times
4. D.Skip tool use and have the model guess order statuses from its training data

The trap AWS set here:

Pattern 1: 'identically across three providers' is the constraint that kills the per-provider and regex options.

Q25

Hard

Multiple choice

D1: Develop and Optimize GenAI Apps with Bedrock

A team stores prompts in Bedrock Prompt Management and calls them through the Converse API. They try to add `guardrailConfig` inline on the Converse call and the request is rejected. They still need guardrail protection on these prompts. What is the MOST correct fix?

1. A.Apply the guardrail separately with the standalone ApplyGuardrail API on inputs and outputs, since guardrailConfig cannot be combined with Prompt Management prompts in Converse
2. B.Embed the guardrail rules as text inside the prompt template and hope the model obeys them
3. C.Abandon Prompt Management and hardcode the prompts so guardrailConfig works again
4. D.Disable guardrails for these prompts because Prompt Management prompts are inherently safe

The trap AWS set here:

Pattern 6: a real API restriction with a clean workaround. The trap answers either weaken safety or destroy governance.

## D2: Agents, Tools, and Workflow Automation {#D2}

Q26

Medium

Ordering

D2: Agents, Tools, and Workflow Automation

Place these steps in the correct order to build a Bedrock agent that answers questions about company products using internal documents.

1. 1.Define the agent's instructions and session behavior in the agent configuration
2. 2.Define action groups that map user requests to API calls or Lambda functions
3. 3.Prepare the agent, then test through the alias
4. 4.Create an agent alias for the production deployment
5. 5.Create a knowledge base from the product documents and connect it to the agent

order answer: 1 then 5 then 2 then 4 then 3

The trap AWS set here:

Pattern 3: 'prepare the agent' always comes after configuration changes and before testing or alias use.

Q27

Medium

Multiple choice

D2: Agents, Tools, and Workflow Automation

An agent must book refund appointments by calling the company's internal scheduling API. The API expects `customer_id` and `preferred_date`. How should the agent access this capability?

1. A.Define an action group whose function schema declares the scheduling operation and its parameters, backed by a Lambda executor that calls the API
2. B.Give the agent the API's base URL in its instructions and let it guess the request format
3. C.Have the agent output the API request as plain text for a human to execute
4. D.Connect the knowledge base to the scheduling API so retrieval returns appointment slots

The trap AWS set here:

Pattern 6: knowledge bases for live actions. KB = documents, action groups = actions.

Q28

Hard

Multiple choice

D2: Agents, Tools, and Workflow Automation

An agent team updates the agent's instructions to fix a reasoning flaw, then tests immediately. The agent behaves exactly as before the change. The configuration was saved. What is the MOST likely cause?

1. A.The agent was not prepared after the configuration change, so the update is not active in the test invocation
2. B.The instructions were saved to the wrong region, so the test used the old region's agent
3. C.Agent instructions only take effect after 24 hours of propagation
4. D.Testing requires a new agent alias to be created for every instruction change

The trap AWS set here:

Pattern 6: 'configuration changed but behavior unchanged' almost always points to the missing prepare step.

Q29

Medium

Multiple choice

D2: Agents, Tools, and Workflow Automation

During testing, an agent's orchestration trace shows it calling the wrong action group for 'cancel my subscription' requests. The function schemas look correct. What should the team examine next?

1. A.The agent's instructions and the action group descriptions, because ambiguous descriptions cause the model to pick the wrong group
2. B.The knowledge base chunk size, because retrieval determines action selection
3. C.The guardrail denied-topic list, because it blocks the cancel operation
4. D.The model's temperature, because high temperature causes wrong API choices

The trap AWS set here:

Pattern 1: schemas correct plus wrong selection points at the selection signal (descriptions), not at retrieval or sampling knobs.

Q30

Easy

Multiple choice

D2: Agents, Tools, and Workflow Automation

An agent must answer questions from an internal wiki, and every answer should cite the wiki page it came from. The wiki is updated weekly. What is the MOST correct setup?

1. A.Connect a knowledge base built on the wiki to the agent, with scheduled syncs so weekly updates are ingested
2. B.Paste the entire wiki into the agent's instructions so the context is always present
3. C.Fine-tune the foundation model on the wiki so answers come from its weights
4. D.Have the agent call a search-engine API through an action group for each question

The trap AWS set here:

Pattern 6: agents do not change the RAG rule. Updating documents plus citations still means knowledge base, not fine-tuning.

Q31

Medium

Multiple choice

D2: Agents, Tools, and Workflow Automation

A company deploys a Bedrock agent that handles refund requests. The agent must never issue a refund above $500 without a manager's approval, and every approval must be recorded. Which design is MOST correct?

1. A.Implement returnControl in the agent's action group: the agent pauses, a Step Functions workflow routes the approval to a manager, and the decision plus full trace are logged
2. B.Tell the agent in its instructions to never refund above $500 without asking, and trust it to comply
3. C.Set a guardrail denied topic for refunds so the agent cannot process any refund
4. D.Let the agent issue refunds directly and email a report afterward for the manager to review

The trap AWS set here:

Pattern 6: 'tell the agent' for a compliance gate. Approval gates need returnControl, not instructions.

Q32

Hard

Multiple response

D2: Agents, Tools, and Workflow Automation

An agent intermittently returns answers that contradict the company's pricing documents, though retrieval usually finds the right pages. Which TWO are the MOST likely causes to investigate? (Select TWO)

*Select 2.*

1. A.Hallucination: the model generated beyond what the retrieved passages support, so add a faithfulness evaluation and grounding checks
2. B.Stale knowledge base content where the pricing documents changed but the scheduled sync failed
3. C.Provisioned Throughput running out of capacity during peak hours
4. D.The agent's IAM role having too many permissions on the knowledge base
5. E.Users asking questions in ALL CAPS, which confuses the retrieval model

The trap AWS set here:

Pattern 1: 'contradicts the documents it retrieved' narrows the cause to the grounding layer: generation fidelity or source freshness.

Q33

Medium

Multiple choice

D2: Agents, Tools, and Workflow Automation

A support agent handles 10,000 conversations a day. Each conversation independently repeats the same 4,000-token product catalog context. Costs are high. What is the MOST correct optimization?

1. A.Use prompt caching with a cachePoint after the stable catalog content, so the repeated prefix is billed at the lower cached rate
2. B.Increase the model's max tokens so the catalog fits more comfortably
3. C.Fine-tune the model on the catalog so the context is no longer needed
4. D.Switch to a smaller model and accept lower answer quality

The trap AWS set here:

Pattern 5: repeated stable context is a caching problem, not a model-size or training problem.

Q34

Hard

Multiple choice

D2: Agents, Tools, and Workflow Automation

An agent uses tool calling in a loop: each turn it calls tools and continues reasoning. The team notices that placing the tool definitions after the conversation messages in the request yields worse tool selection than placing them first. They also see rising costs from repeated system prompts. What is the MOST correct combined fix?

1. A.Place tool definitions and system content first, then a cachePoint after the stable content, so both tool selection and caching work on the stable prefix
2. B.Move the tool definitions into the user messages so the model reads them last
3. C.Remove the system prompt entirely to cut costs
4. D.Disable tool calling and have the model describe the actions in prose

The trap AWS set here:

Pattern 2: a combined question where each half has a verified rule (ordering for selection, cachePoint for cost). The correct option honors both.

Q35

Medium

Multiple choice

D2: Agents, Tools, and Workflow Automation

An agent must read a 200-page PDF contract, extract the renewal clause, and summarize the termination terms. The PDF is already in S3. What is the MOST correct way to give the agent the document content?

1. A.Use Bedrock Data Automation to parse the PDF into structured text, then provide the extracted content to the agent
2. B.Paste the PDF's binary bytes into the agent's instructions
3. C.Have the agent download the PDF with a Lambda function and parse it with string operations
4. D.Email the PDF to the agent's service account and let it read the attachment

The trap AWS set here:

Pattern 5: the managed parser (Data Automation) beats every hand-built or misapplied alternative.

Q36

Medium

Multiple response

D2: Agents, Tools, and Workflow Automation

A company wants its support agent to improve its answers over time from conversation logs. Which TWO practices form the MOST correct improvement loop? (Select TWO)

*Select 2.*

1. A.Store conversation history in a session store and periodically review traces and user feedback to refine instructions and action groups
2. B.Run LLM-as-a-judge evaluations on sampled conversations, scoring faithfulness and correctness against the knowledge base
3. C.Automatically fine-tune the foundation model on every conversation the same night it happens
4. D.Delete all conversation logs immediately for privacy, then guess at improvements
5. E.Let the agent rewrite its own instructions in production without review

The trap AWS set here:

Pattern 6: 'improve over time' tempts training-based answers, but the exam's loop is evaluate, then refine deliberately.

Q37

Hard

Multiple choice

D2: Agents, Tools, and Workflow Automation

An agent handles insurance claims. Regulations require that every automated decision be explainable: which documents were used, which tools were called, and what the model reasoned at each step. What is the MOST correct way to satisfy this?

1. A.Enable tracing on the agent invocations and persist the full trace (pre-processing, orchestration, post-processing) with the decision record
2. B.Ask the agent to explain itself in its final answer and store that text as the explanation
3. C.Store only the final answer and the timestamp; the model is deterministic so it can be re-run
4. D.Rely on CloudTrail alone, since it records the agent invocation

The trap AWS set here:

Pattern 6: trace (the execution record) versus self-explanation (generated text). Compliance needs the record, not the narration.

Q38

Medium

Multiple choice

D2: Agents, Tools, and Workflow Automation

A team builds a multi-agent system: a supervisor agent coordinates three specialist agents (billing, technical, shipping). During testing, the specialists never receive the conversation history from the supervisor. Which configuration is the MOST likely fix?

1. A.Enable conversation history relay between the supervisor and collaborator agents so context flows across the team
2. B.Increase the supervisor agent's max tokens so it can hold more history
3. C.Merge all three specialists into one agent with longer instructions
4. D.Give each specialist its own separate knowledge base so they do not need history

The trap AWS set here:

Pattern 4: multi-agent collaboration is a supervisor/collaborator relationship with history relay, not action groups.

Q39

Easy

Multiple choice

D2: Agents, Tools, and Workflow Automation

A developer wants agents built in the AWS console to be deployable through the team's CI/CD pipeline with code review. What is the MOST correct approach?

1. A.Define the agents with infrastructure as code (CloudFormation or CDK) so agent configuration is versioned, reviewed, and deployed like other infrastructure
2. B.Export console screenshots of the agent configuration and attach them to the deployment ticket
3. C.Have one engineer manually recreate the agent in production after testing in development
4. D.Store the agent configuration in a shared document and copy values into the console per environment

The trap AWS set here:

Pattern 5: anything 'deployable through CI/CD with review' points to IaC, regardless of which service is being deployed.

Q40

Medium

Multiple choice

D2: Agents, Tools, and Workflow Automation

An agent's action group calls a Lambda function that sometimes takes 3 minutes to complete. The agent invocation fails before the function finishes. What is the MOST correct fix?

1. A.Redesign so the Lambda returns quickly and the long work continues asynchronously, with the agent polling or being notified on completion
2. B.Increase the agent's timeout to 30 minutes so it can wait for the Lambda
3. C.Chain three Lambda functions in sequence so each handles one minute of the work
4. D.Remove the Lambda and have the agent perform the 3-minute task by reasoning longer

The trap AWS set here:

Pattern 1: the failure is synchronous coupling. The fix is async with polling or notification, not longer waits.

Q41

Hard

Multiple choice

D2: Agents, Tools, and Workflow Automation

A company runs two agents: one answers employee HR questions, one answers customer support questions. The HR agent must never see customer data and vice versa. Both invoke the same Lambda tools. What is the MOST correct isolation design?

1. A.Scope each agent's IAM role and each action group's Lambda permissions to only the data its domain needs, keeping tool code shared but data access separated
2. B.Put both agents in the same IAM role with full access, since the agents' instructions will keep them in their lanes
3. C.Merge the two agents into one agent with a prompt that switches between HR and customer modes
4. D.Give both agents access to all data but add a guardrail denied topic for the other domain's content

The trap AWS set here:

Pattern 6, trap 6: isolation must be enforced by IAM, never by prompts or content filters.

Q42

Medium

Multiple response

D2: Agents, Tools, and Workflow Automation

An agent's answers are factually correct but users complain the tone is inconsistent: sometimes formal, sometimes casual, occasionally slang. Which TWO fixes are MOST correct? (Select TWO)

*Select 2.*

1. A.Add explicit tone and style guidelines to the agent's instructions and prompt templates
2. B.Create prompt variants in Prompt Management to A/B test tone settings and adopt the winner
3. C.Fine-tune the foundation model on formal documents so the tone is permanently formal
4. D.Increase the temperature to make the tone more creative and varied
5. E.Add a guardrail denied topic for casual language

The trap AWS set here:

Pattern 5: tone is prompt-layer. The exam punishes reaching for fine-tuning or guardrails when instructions suffice.

Q43

Medium

Multiple choice

D2: Agents, Tools, and Workflow Automation

A team is choosing between Bedrock Prompt Flows and Bedrock Agents for a deterministic five-step claims intake process: collect fields, validate, look up policy, compute payout, store result. No step requires open-ended reasoning. What is the MOST correct choice?

1. A.Prompt Flows, because the process is a fixed sequence of prompt-centric steps with no autonomous reasoning
2. B.Agents, because agents are newer and more capable than flows
3. C.Agents, because only agents can call Lambda functions
4. D.Prompt Flows, because flows support human approval gates lasting several days

The trap AWS set here:

Pattern 4: flows versus agents is decided by workflow shape (fixed sequence vs autonomous reasoning), not by capability marketing.

Q44

Hard

Matching

D2: Agents, Tools, and Workflow Automation

Match each API to its purpose.

| Items | Descriptions |
|---|---|
| **1.** InvokeModel | **C.** Send a single request to a foundation model, including embedding models |
| **2.** Converse | **B.** Hold a multi-turn conversation with unified text, tool use, and guardrail fields across providers |
| **3.** ApplyGuardrail | **A.** Evaluate text against guardrail policies independently of any model call |

The trap AWS set here:

Pattern 4: the exam loves API-purpose matching. InvokeModel for embeddings is the detail most people miss.

Q45

Easy

Multiple choice

D2: Agents, Tools, and Workflow Automation

A developer prototypes an agent in the AWS console and wants to inspect what the agent is thinking at each step: which passages it retrieved and which tools it called. What should the developer enable?

1. A.Trace, which returns the pre-processing, orchestration, and post-processing steps of the agent invocation
2. B.CloudWatch Logs on the Lambda function only, which shows the agent's reasoning
3. C.X-Ray tracing on the API Gateway, which captures the agent's internal steps
4. D.Guardrail trace, which logs the agent's tool selection logic

The trap AWS set here:

Pattern 6: each trace type shows its own plane. Agent reasoning needs the agent trace.

Q46

Medium

Multiple choice

D2: Agents, Tools, and Workflow Automation

An agent must call a partner's REST API that is described by an OpenAPI specification. The team wants the agent to use the API without writing custom Lambda executor code. What is the MOST correct approach?

1. A.Define the action group with the OpenAPI schema directly, letting Bedrock map operations to API calls without a custom executor
2. B.Write a Lambda function that hardcodes each API endpoint and have the action group call it
3. C.Paste the OpenAPI specification into the agent's instructions and let the model craft HTTP requests
4. D.Use a knowledge base to store the API documentation so the agent can read it at runtime

The trap AWS set here:

Pattern 5: the managed path (OpenAPI schema on the action group) beats custom code when the scenario says 'without writing custom code'.

Q47

Hard

Multiple choice

D2: Agents, Tools, and Workflow Automation

An agent books travel using three tools: search_flights, reserve_hotel, and charge_card. Testing shows the agent sometimes charges the card before confirming the flight and hotel are available. The business rule is: never charge before both are confirmed. What is the MOST correct fix?

1. A.Encode the ordering rule in the agent's instructions and add a confirmation step via returnControl before the charge_card call executes
2. B.Remove the charge_card tool and have the agent email the card details to finance
3. C.Increase the model's context window so it remembers the business rule better
4. D.Add a guardrail denied topic for credit card charges

The trap AWS set here:

Pattern 6: money movement needs a hard control (returnControl), not just instructions. Guide plus gate.

## D3: Responsible AI, Guardrails, and Evaluation {#D3}

Q48

Hard

Matching

D3: Responsible AI, Guardrails, and Evaluation

Match each Bedrock Guardrails control to what it filters.

| Items | Descriptions |
|---|---|
| **1.** Content filters | **A.** Hate, insults, sexual, violence, misconduct, and prompt attacks at LOW, MEDIUM, or HIGH strength |
| **2.** Denied topics | **D.** Subject areas the application must never discuss, defined in natural language |
| **3.** Word filters | **B.** Exact strings such as competitor names or profanity, blocked on match |
| **4.** Sensitive information filters | **C.** PII and custom regex patterns, blocked or masked on detection |

The trap AWS set here:

Pattern 4: denied topics versus word filters is the classic confusion. Topics are subject areas; words are exact strings.

Q49

Medium

Multiple choice

D3: Responsible AI, Guardrails, and Evaluation

A financial advice assistant must refuse to provide personalized investment recommendations, but it may explain general investing concepts. How should this be enforced?

1. A.A guardrail denied topic defining personalized investment advice, applied to both inputs and outputs
2. B.A word filter listing every stock ticker symbol
3. C.A content filter set to HIGH, which blocks all financial content
4. D.Instructions telling the model to be careful with financial questions

The trap AWS set here:

Pattern 6: subject-area refusal is denied topics. Word filters are for exact strings.

Q50

Hard

Ordering

D3: Responsible AI, Guardrails, and Evaluation

Place these safeguards in the order they should be applied to user input in a defense-in-depth design, from outermost to innermost.

1. 1.Bedrock Guardrails on the input (prompt attack and content filters)
2. 2.Logging and monitoring of flagged interactions for review
3. 3.Input validation and sanitization at the application edge (length, format, allowlists)
4. 4.Model invocation with least-privilege IAM and scoped tool permissions
5. 5.Bedrock Guardrails on the output (content and sensitive-info filters)

order answer: 3 then 1 then 4 then 5 then 2

The trap AWS set here:

Pattern 3: guardrails belong on BOTH inputs and outputs. An ordering that applies them only once is wrong.

Q51

Medium

Multiple choice

D3: Responsible AI, Guardrails, and Evaluation

A healthcare assistant must never reveal patient phone numbers or email addresses in its answers, even if those appear in retrieved documents. What is the MOST correct control?

1. A.A guardrail sensitive-information filter for PII with the mask action, applied to the model output
2. B.A denied topic for phone numbers and email addresses
3. C.Instructions telling the model to omit contact details
4. D.Encrypting the knowledge base documents so the model cannot read phone numbers

The trap AWS set here:

Pattern 6: PII is sensitive-information filters. Denied topics cannot do pattern detection.

Q52

Medium

Multiple response

D3: Responsible AI, Guardrails, and Evaluation

A public-facing assistant is being probed with prompt injection attempts: users paste fake system instructions trying to make the assistant reveal its hidden prompt. Which TWO defenses are MOST correct? (Select TWO)

*Select 2.*

1. A.A guardrail with the prompt attack filter enabled to detect and block injection attempts
2. B.Clearly separating system instructions from user input and never echoing the system prompt
3. C.Training the model to recognize injection attempts through fine-tuning
4. D.Disabling all user input and offering only canned button responses
5. E.Storing the system prompt in a separate AWS account from the application

The trap AWS set here:

Pattern 6: prompt injection is fought with the prompt attack filter plus input separation, not with training or account tricks.

Q53

Easy

Multiple choice

D3: Responsible AI, Guardrails, and Evaluation

A company must prove to auditors that its assistant's answers are grounded in retrieved company documents, not invented. Which evaluation approach is MOST correct?

1. A.Run RAG evaluations measuring faithfulness, correctness, and citation precision against the retrieved passages
2. B.Count the number of tokens in each answer; longer answers are more grounded
3. C.Ask the model whether its own answers are grounded and record its response
4. D.Measure the assistant's uptime; available systems are more trustworthy

The trap AWS set here:

Pattern 6: grounding is measured with faithfulness and citation metrics, never with self-reports or proxy statistics.

Q54

Medium

Multiple choice

D3: Responsible AI, Guardrails, and Evaluation

An assistant's answers are evaluated by human reviewers for tone and helpfulness, and the team wants automated nightly scoring to catch regressions between human reviews. Which combination is MOST correct?

1. A.LLM-as-a-judge scoring correctness, faithfulness, and professional style nightly, plus periodic human evaluation for nuanced tone judgments
2. B.Human evaluation only, because automated judges are never reliable enough to use
3. C.LLM-as-a-judge only, because human review is too slow to ever be useful
4. D.Programmatic metrics only (BLEU and ROUGE), because they are fully deterministic

The trap AWS set here:

Pattern 2: the absolutes ('never', 'only') mark the wrong answers. The exam rewards the complementary pairing.

Q55

Hard

Multiple choice

D3: Responsible AI, Guardrails, and Evaluation

A team runs LLM-as-a-judge evaluations comparing two prompt versions. The judge consistently prefers whichever answer appears first. The team needs trustworthy comparisons. What is the MOST correct fix?

1. A.Randomize or counterbalance the presentation order across comparisons so position bias cancels out
2. B.Use a larger judge model, because larger models do not have position bias
3. C.Show the judge only one answer at a time and ask for an absolute score with no comparison
4. D.Replace the judge with exact-match scoring, which has no position bias

The trap AWS set here:

Pattern 1: the artifact is in the method (order), so the fix is in the method (counterbalance), not in model size.

Q56

Medium

Multiple choice

D3: Responsible AI, Guardrails, and Evaluation

A RAG assistant cites sources, but auditors find that some citations point to documents that do not support the cited claim. Which metric directly measures this failure, and what is the MOST correct response?

1. A.Citation precision; investigate retrieval and generation to find why unsupported claims get citations
2. B.Answer length; shorten answers so fewer citations are needed
3. C.Invocation count; the assistant is being called too often
4. D.Latency; slow answers cause citation errors

The trap AWS set here:

Pattern 1: name the metric that matches the failure (precision of citations), then fix the cause, not a proxy.

Q57

Easy

Multiple choice

D3: Responsible AI, Guardrails, and Evaluation

A company is choosing a foundation model for a customer-facing assistant. The security team asks how to compare models on safety before selecting one. What is the MOST correct guidance?

1. A.Review the model providers' safety evaluations and red-teaming reports, then run the company's own safety evaluations on shortlisted models
2. B.Choose the largest model, because larger models are inherently safer
3. C.Choose whichever model the engineering team used last time
4. D.Skip safety comparison; Bedrock Guardrails make model choice irrelevant to safety

The trap AWS set here:

Pattern 6, trap 15: guardrails do not replace model-level safety evaluation. Defense in depth means both.

Q58

Medium

Multiple choice

D3: Responsible AI, Guardrails, and Evaluation

An assistant must refuse harmful requests, but testing shows it sometimes complies with disallowed content wrapped in hypothetical framing ('imagine a world where...'). Which evaluation dimension should the team prioritize, and what is the MOST correct mitigation?

1. A.Harmfulness and refusal metrics in LLM-as-a-judge evaluations; strengthen guardrails and add adversarial test cases with hypothetical framing
2. B.Latency metrics; faster refusals are safer refusals
3. C.Cost metrics; harmful requests are expensive to process
4. D.User satisfaction metrics; satisfied users do not write hypotheticals

The trap AWS set here:

Pattern 1: jailbreak framing is a safety problem. Measure refusal and harmfulness, mitigate with guardrails and adversarial tests.

Q59

Hard

Multiple choice

D3: Responsible AI, Guardrails, and Evaluation

A team wants to prove that a new prompt version is genuinely better, not just luckier on a small test set. Their current test set has 40 examples. What is the MOST correct evaluation practice?

1. A.Build a larger, representative golden dataset with clear pass criteria, version it, and re-run it on every prompt change
2. B.Test on the same 40 examples repeatedly until the new prompt passes
3. C.Test each prompt version on a different 40 examples so results stay fresh
4. D.Have the prompt author grade their own prompt's outputs; they know the intent best

The trap AWS set here:

Pattern 2: the wrong options are all methodological sins (p-hacking, moving goalposts, self-grading). The exam rewards the disciplined golden dataset.

Q60

Medium

Multiple response

D3: Responsible AI, Guardrails, and Evaluation

A company deploys an assistant that gives financial summaries. Regulators require that the assistant's behavior be consistent and that any behavior change be traceable to a specific approved change. Which TWO practices satisfy this? (Select TWO)

*Select 2.*

1. A.Version prompts in Prompt Management and deploy only approved versions, so every behavior maps to an immutable snapshot
2. B.Log model inputs, outputs, guardrail interventions, and version identifiers for every interaction
3. C.Let the model update its own prompts nightly based on user feedback to stay current
4. D.Disable all logging to reduce storage costs, since regulators only need the final answers
5. E.Change prompts directly in production and document the change in a chat message afterward

The trap AWS set here:

Pattern 6: regulated behavior needs versioned artifacts plus logs. Every wrong option breaks one of those halves.

Q61

Medium

Multiple choice

D3: Responsible AI, Guardrails, and Evaluation

An assistant occasionally produces answers that are fluent but factually wrong about company policy. The team wants an automated check that verifies each factual claim against the retrieved documents before the answer reaches the user. Which technique is MOST correct?

1. A.Contextual grounding checks, which verify that generated claims are supported by the retrieved context
2. B.A higher temperature setting, which makes the model more careful
3. C.A longer system prompt describing the company's values
4. D.Retrying the request until the answer looks right to a reviewer

The trap AWS set here:

Pattern 6: claim verification against retrieved context is contextual grounding. The distractors are all different-plane knobs.

Q62

Hard

Multiple choice

D3: Responsible AI, Guardrails, and Evaluation

A team tests an assistant with 500 adversarial prompts covering jailbreaks, PII extraction, and disallowed content. The assistant blocks 490. Leadership asks whether 98 percent is good enough to launch. What is the MOST correct response?

1. A.No: analyze the 10 failures for patterns, fix the systematic gaps, and define an explicit risk-acceptance bar with leadership before launch
2. B.Yes: 98 percent is an A grade, so launch immediately
3. C.No: no system may ever launch until it blocks 100 percent of adversarial prompts
4. D.Yes: adversarial testing is just a formality, so the number does not matter

The trap AWS set here:

Pattern 2: both absolutes are wrong. The exam wants failure analysis plus explicit risk acceptance.

Q63

Medium

Multiple choice

D3: Responsible AI, Guardrails, and Evaluation

A company uses a third-party model through Bedrock Marketplace for a specialized task. The security team asks who is responsible for the model's safety behavior: AWS, the model provider, or the company. What is the MOST correct guidance?

1. A.The company remains responsible for safe deployment: it must evaluate the model and apply guardrails, using provider safety documentation as input
2. B.The model provider is solely responsible, so no company-side safety work is needed
3. C.AWS is solely responsible for all models available through Bedrock, including Marketplace models
4. D.Safety responsibility is automatically handled by the model's built-in alignment, so deployment needs no extra controls

The trap AWS set here:

Pattern 6, trap 15: built-in safety never transfers the deployer's responsibility. The exam always keeps responsibility with the deployer.

## D4: FM Customization and Training {#D4}

Q64

Easy

Multiple choice

D4: FM Customization and Training

A company trains a custom model on SageMaker AI using proprietary source code. The training data must never leave the company's AWS environment, and the training cluster must have no internet access. Which networking setup is MOST correct?

1. A.Run the training jobs in a VPC with no internet gateway or NAT, using VPC endpoints for the AWS services the job needs
2. B.Run the training jobs on the public internet but encrypt the dataset with KMS
3. C.Download the dataset to engineers' laptops and train locally to keep it off the network
4. D.Use the default SageMaker network settings, which already block all internet access

The trap AWS set here:

Pattern 1: 'never leave the environment, no internet access' is a network-isolation constraint. Only the VPC option satisfies it.

Q65

Medium

Multiple choice

D4: FM Customization and Training

A training job processes 50 TB of data stored in S3. Data loading is the bottleneck: GPUs sit idle waiting for batches. Which storage optimization is MOST correct?

1. A.Use FSx for Lustre backed by the S3 dataset as a high-throughput parallel file system for the training job
2. B.Copy the 50 TB to EBS volumes attached to each training instance
3. C.Stream the data directly from S3 with no caching and accept the idle GPUs
4. D.Compress the dataset into a single ZIP file in S3 for faster transfer

The trap AWS set here:

Pattern 1: 'GPUs idle waiting for data' is a data-loading bottleneck. The fix is parallel high-throughput storage, not more compute.

Q66

Medium

Multiple choice

D4: FM Customization and Training

A team fine-tunes a 70B-parameter model. A single GPU cannot hold the model, so they split layers across 8 GPUs, and they also shard the optimizer state to reduce memory per GPU. Which techniques are they using?

1. A.Model parallelism for splitting layers across GPUs, and ZeRO-style optimizer sharding for the optimizer state
2. B.Data parallelism for both, since all parallelism is data parallelism
3. C.Pipeline parallelism for the optimizer state and tensor parallelism for the data
4. D.Quantization for the layer split and pruning for the optimizer state

The trap AWS set here:

Pattern 4: parallelism vocabulary. Layer split equals model parallelism; optimizer sharding equals ZeRO.

Q67

Hard

Multiple response

D4: FM Customization and Training

A pre-training run on a large cluster keeps failing: some runs diverge with loss spikes, others crash when a single node fails. Which TWO practices address these failure modes? (Select TWO)

*Select 2.*

1. A.Add gradient clipping and learning-rate warmup to control loss spikes and divergence
2. B.Use checkpointing with automatic restart so a node failure resumes from the last saved state instead of from scratch
3. C.Increase the batch size indefinitely, which prevents both divergence and node failures
4. D.Disable all logging to make the training run faster and more stable
5. E.Train on a single GPU to eliminate multi-node failure modes

The trap AWS set here:

Pattern 1: two distinct failure modes need two distinct fixes. Each wrong option fixes neither or refuses the workload.

Q68

Medium

Multiple choice

D4: FM Customization and Training

After fine-tuning, a model performs well on the fine-tuning task but has noticeably degraded on general knowledge it previously had. What is this phenomenon, and what is the MOST correct mitigation?

1. A.Catastrophic forgetting; mitigate with a replay buffer of general data mixed into fine-tuning, or use parameter-efficient adapters instead of full fine-tuning
2. B.Overfitting; mitigate by training for more epochs on the fine-tuning data
3. C.Underfitting; mitigate by increasing the learning rate sharply
4. D.Data leakage; mitigate by encrypting the fine-tuning dataset

The trap AWS set here:

Pattern 6: name the phenomenon (catastrophic forgetting), then pick the mitigation that matches it. The distractors name real phenomena with wrong fixes.

Q69

Easy

Multiple choice

D4: FM Customization and Training

A team evaluates a fine-tuned summarization model. They need a quick automated signal of summary quality during development, plus a definitive human judgment before release. Which pairing is MOST correct?

1. A.ROUGE scores for fast automated iteration, plus human evaluation of factuality and usefulness before release
2. B.Human evaluation for every training epoch, because automation is never useful
3. C.ROUGE scores as the sole release criterion, because they are fully objective
4. D.Model loss curves only, because lower loss always means better summaries

The trap AWS set here:

Pattern 2: the exam pairs cheap automated metrics for iteration with human judgment for release. Absolutes on either side are wrong.

Q70

Medium

Multiple choice

D4: FM Customization and Training

A fine-tuning dataset contains customer support transcripts. Before training, the team must reduce the risk of the model memorizing and regurgitating customer phone numbers. What is the MOST correct data preparation step?

1. A.Scrub PII from the training data with detection and redaction before training begins
2. B.Train first and add a guardrail afterward to catch phone numbers in outputs
3. C.Encrypt the dataset; encrypted PII cannot be memorized
4. D.Rely on the base model's safety alignment to avoid regurgitating phone numbers

The trap AWS set here:

Pattern 6, trap 15: the fix belongs at the data layer (scrub before training), not as a post-hoc filter or alignment hope.

Q71

Hard

Multiple choice

D4: FM Customization and Training

A team fine-tunes with LoRA adapters. After deployment, they need to serve the base model plus three task-specific adapters from the same endpoint fleet, switching adapters per request with minimal latency. What is the MOST correct serving approach?

1. A.Serve the shared base model with dynamically loaded adapters per request, keeping one base in memory and swapping lightweight adapters
2. B.Deploy three separate full-model copies, one per adapter, tripling the GPU footprint
3. C.Merge all three adapters into the base weights permanently and serve one model
4. D.Bake each adapter into a separate container image and redeploy for every request type

The trap AWS set here:

Pattern 5: the adapter architecture exists so you do not duplicate the base. Any option that duplicates or destroys that property is wrong.

Q72

Medium

Multiple response

D4: FM Customization and Training

A company must keep full lineage for a fine-tuned model: which dataset version, which code, which hyperparameters, and which base model produced it. Which TWO SageMaker AI capabilities support this? (Select TWO)

*Select 2.*

1. A.SageMaker Model Registry to version the model artifacts with metadata and approval status
2. B.SageMaker Experiments to track hyperparameters, code versions, and dataset references per training run
3. C.Storing the model weights on an engineer's workstation with a README file
4. D.Emailing the hyperparameters to the team after each run
5. E.Keeping lineage in the model file's filename, like model_v7_final_FINAL.pt

The trap AWS set here:

Pattern 2: lineage needs systems of record (Registry plus Experiments). Every wrong option is an informal substitute.

Q73

Medium

Multiple choice

D4: FM Customization and Training

A pre-training dataset is assembled from web crawls. The team discovers it contains large amounts of duplicated text, machine-generated spam, and some toxic content. What is the MOST correct data curation sequence?

1. A.Deduplicate, filter spam and low-quality text, remove toxic content, then document the dataset composition before training
2. B.Train on the raw crawl; scale overcomes data quality problems
3. C.Remove toxic content only; duplicates and spam are harmless at scale
4. D.Document the raw crawl as-is and skip curation to save time

The trap AWS set here:

Pattern 2: 'scale fixes data' is the tempting fallacy. The exam rewards the curation pipeline in order.

## D5: Security, Governance, and Monitoring {#D5}

Q74

Easy

Multiple choice

D5: Security, Governance, and Monitoring

A company deploys a customer-facing assistant. The compliance team requires that all prompts and model responses be logged for audit, but customer PII in the logs must be protected. Which logging design is MOST correct?

1. A.Enable model invocation logging to S3 with KMS encryption, and redact or mask PII before or as logs are written
2. B.Disable all logging to avoid storing any customer data
3. C.Log prompts and responses in plain text to a public S3 bucket for easy auditor access
4. D.Store logs only in the application's memory so they disappear on restart

The trap AWS set here:

Pattern 1: the stem has two constraints (audit + PII protection). Only the option honoring both is correct.

Q75

Medium

Multiple choice

D5: Security, Governance, and Monitoring

A company processes customer feedback with a Bedrock model. Legal requires that prompts and responses never be used to train or improve any AWS model, and that data stay within the AWS region. Which statement is MOST correct?

1. A.Bedrock does not use customer prompts or responses to train models, and data stays within the selected region for processing
2. B.Bedrock trains on customer data by default; the company must file a support ticket to opt out per request
3. C.Data residency is automatic across all regions simultaneously, so region selection does not matter
4. D.The company must encrypt prompts client-side or AWS will use them for training

The trap AWS set here:

Pattern 6: the exam tests Bedrock's actual data-use posture. Distractors invent opt-outs and conditions that do not exist.

Q76

Medium

Multiple response

D5: Security, Governance, and Monitoring

A GenAI application handles EU customer data. Which TWO controls support GDPR-aligned deployment on Bedrock? (Select TWO)

*Select 2.*

1. A.Keep processing in an EU region and use cross-region inference only with profiles that preserve the required data residency
2. B.Apply data minimization: send the model only the customer data the task needs, and set retention policies on logs
3. C.Store all EU customer data in a US region because S3 is cheaper there
4. D.Send full customer records to the model on every request to maximize answer quality
5. E.Disable encryption because GDPR only cares about consent, not security

The trap AWS set here:

Pattern 2: residency plus minimization. Each wrong option sacrifices one of them for cost, convenience, or a false legal claim.

Q77

Hard

Multiple choice

D5: Security, Governance, and Monitoring

An assistant stores conversation history for context. A user exercises their right to erasure and asks that all their data be deleted. The history lives in the agent's session store, invocation logs in S3, and embeddings derived from their documents in a vector index. What is the MOST correct deletion approach?

1. A.Delete from all three locations (session store, S3 logs, and the vector index entries), and verify each deletion, because erasure must cover derived data too
2. B.Delete the session store entry only; logs and embeddings are system data, not user data
3. C.Anonymize the user's name in future responses and leave stored data untouched
4. D.Wait 30 days; the data will age out of all three systems automatically

The trap AWS set here:

Pattern 6: derived data (embeddings) counts. The exam tests whether you remember that erasure reaches the vector index.

Q78

Medium

Multiple choice

D5: Security, Governance, and Monitoring

A team discovers their assistant's training and evaluation data over-represents one demographic and under-represents others. The assistant will serve a global user base. What is the MOST correct response?

1. A.Rebalance the dataset to represent the served population, add fairness evaluations slicing metrics by demographic, and monitor for disparate performance after launch
2. B.Ship as-is; the model will generalize to under-represented groups automatically
3. C.Remove all demographic information from the data; blindness guarantees fairness
4. D.Collect more data only from the over-represented group to improve overall accuracy

The trap AWS set here:

Pattern 2: 'blindness guarantees fairness' is the tempting fallacy. The exam rewards measure, rebalance, and monitor.

Q79

Easy

Multiple choice

D5: Security, Governance, and Monitoring

A company builds an assistant that writes performance reviews from manager notes. HR policy requires a human to review and approve every generated review before it is shared. Which deployment pattern is MOST correct?

1. A.Human-in-the-loop: the assistant drafts, a Step Functions workflow routes each draft to the manager for approval via task token, and only approved drafts are delivered
2. B.Fully autonomous delivery; the model is accurate enough that review adds no value
3. C.Human-on-the-loop: deliver all drafts immediately and let managers complain afterward if something is wrong
4. D.Disable the assistant; automation has no place in performance reviews

The trap AWS set here:

Pattern 4: in-the-loop (approve before) versus on-the-loop (monitor after). Stakes decide, and performance reviews are high-stakes.

Q80

Medium

Multiple choice

D5: Security, Governance, and Monitoring

A support assistant's CloudWatch dashboard shows a rising InvocationThrottles metric on the AWS/Bedrock namespace, and users report intermittent 'try again' errors. InputTokenCount and OutputTokenCount are flat. What is the MOST correct interpretation and fix?

1. A.The application is hitting API throttling limits; add exponential backoff with jitter and consider spreading load or requesting quota increases
2. B.The model is generating too many tokens; reduce max tokens to fix the throttling
3. C.CloudWatch metrics are delayed; wait 24 hours and the throttles will clear
4. D.The knowledge base is out of sync; re-sync it to stop the throttling

The trap AWS set here:

Pattern 1: read the metric. Throttles with flat tokens means rate limiting, not token bloat. Fix the call pattern.

Q81

Hard

Multiple choice

D5: Security, Governance, and Monitoring

A company must demonstrate continuous responsible-AI governance: model risk assessments before launch, guardrails in production, ongoing monitoring, and periodic re-assessment. Which operating pattern is MOST correct?

1. A.A governance pipeline: risk assessment gates promotion to production, guardrails enforce policy at runtime, CloudWatch monitors invocations and guardrail interventions, and scheduled reviews re-assess risk as models and data change
2. B.A one-time risk assessment before the first launch, with no further reviews
3. C.Guardrails only, because runtime enforcement replaces governance
4. D.Monitoring only, because observed behavior is the only thing that matters

The trap AWS set here:

Pattern 2: governance is a lifecycle, not a single control. Every wrong option is one layer pretending to be the whole program.

## Verification log {#verification-log}

Every AWS service fact used in these questions was verified against official AWS documentation on **2026-09-28**. Facts that could not be verified against a live official source are marked UNVERIFIED below and are not asserted as fact in any question.

- Verified: Converse API fields (modelId, messages, system, inferenceConfig, toolConfig, guardrailConfig, additionalModelRequestFields, outputConfig, promptVariables), content blocks (toolUse, toolResult, cachePoint, guardContent, reasoningContent), and the restriction that Prompt Management prompts cannot combine with inline guardrailConfig, inferenceConfig, system, or toolConfig.
- Verified: Guardrail control types: content filters (Hate, Insults, Sexual, Violence, Misconduct, Prompt Attack; LOW/MEDIUM/HIGH), denied topics, word filters (exact match), sensitive-information filters (block/mask PII plus custom regex), contextual grounding, Automated Reasoning checks; ApplyGuardrail as a standalone model-agnostic API.
- Verified: Knowledge base chunking strategies (default, fixed-size, hierarchical, semantic, none, plus custom Lambda), set per data source at creation; Titan Text Embeddings v2 dimensions (256/512/1024); Cohere Embed English and Multilingual (1024); vector store options including OpenSearch Serverless, Aurora PostgreSQL, Pinecone, Redis, MongoDB Atlas, Neptune Analytics, OpenSearch managed cluster, S3 Vectors.
- Verified: Cross-region inference via geographic profiles (us., eu. prefixes) and global profiles; prefix as data-residency decision; some models requiring inference profile IDs; inference profiles not supporting Provisioned Throughput.
- Verified: Batch inference via CreateModelInvocationJob with S3 input/output; no tool calling or structured output in batch; no prompt caching in batch; provisioned models excluded from batch.
- Verified: Prompt caching via cachePoint after stable content, per-model minimum token thresholds, TTL options (default 5 min, up to 1 hour), cacheReadInputTokens and cacheWriteInputTokens usage fields.
- Verified: Agents: invoke_agent parameters (agentId, agentAliasId, sessionId, inputText, enableTrace), returnControl, endSession, prepare-after-change requirement, aliases, multi-agent supervisor/collaborator with conversation history relay, action groups via Lambda executor or OpenAPI/function schema.
- Verified: Prompt Management versions numbered from 1 as immutable snapshots; variants for A/B testing.
- Verified: Evaluation metric families: programmatic (BERT Score, F1, exact match), LLM-as-a-judge dimensions (correctness, completeness, faithfulness, harmfulness, refusal, stereotyping, professional style/tone), human evaluation options, RAG retrieval and retrieve-and-generate metrics (context relevance, context coverage, faithfulness, correctness, completeness, citation precision/coverage).
- Verified: Bedrock Data Automation for documents, images, video, and audio with blueprints for custom fields; usable as a knowledge base parser.
- Verified: CloudWatch AWS/Bedrock metrics: Invocations, InputTokenCount, OutputTokenCount, InvocationThrottles.
- Verified: Lambda 15-minute maximum timeout; Step Functions Standard up to 1 year with task tokens for human approvals; InvokeModel (not Converse) for embeddings.
- UNVERIFIED: Exact Bedrock pricing figures are not stated in any question; all cost claims are qualitative (discounted, lower, cheaper), which matches how the exam itself phrases cost comparisons.
- UNVERIFIED: The AppConfig plus Lambda plus API Gateway model-switching architecture is presented as the exam's canonical pattern per preparation providers, not as an AWS-documented reference architecture.
- UNVERIFIED: No exact default chunk-size token count is asserted anywhere; chunking questions use relative comparisons only.

Built from original questions written for the AIP-C01 exam blueprint. Public sources were studied for style and coverage only; no question text was copied from any source. Generic content only.

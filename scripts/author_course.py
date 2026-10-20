import json,pathlib,re
slides=[]
def L(title,skills,lead,points,trap,question,answer,sources='',diagram=''):
 slides.append(dict(id='core-'+str(len(slides)+1).zfill(3),title=title,skills=skills.split(),domain=int(skills[0]) if skills else 0,lead=lead,points=points.split(' || '),trap=trap,question=question,answer=answer,sources=sources.split() or ['domain'+skills[0]] if skills else ['exam'],diagram=diagram))
L('AIP-C01: the two-day course','','Use this course for decisions, architecture, and recall. The repository reference provides the full source depth.',
 'Read each core slide. Explain its decision aloud. || Reveal the answer after you attempt each recall prompt. || Use the repository reference for weak topics and all source questions. || Complete the mock without notes. Review each error before exam day.',
 'AWS states that its published guide is non-exhaustive. This course cannot guarantee every exam topic or a pass.',
 'What does success require beyond recognition?','Explain why each alternative fails a stated requirement. Use evidence, service boundaries, and measurable tradeoffs.')
L('Exam facts and score','','The official guide identifies 65 scored questions and 10 unscored questions. Unscored questions are not identified.',
 'Multiple choice has one correct answer and three distractors. || Multiple response requires all correct options for credit. || The score scale is 100 to 1,000. The minimum pass score is 750. || Unanswered questions count as incorrect. A guess has no penalty.',
 'A scaled score of 750 does not mean 75 percent correct. Domain question counts can vary.',
 'Can a weak domain still permit a pass?','Yes. AWS uses an overall compensatory score. You still need broad coverage.','exam')
L('Two-day route','','This is a proposed study schedule. It assumes two full days and prior AWS application experience.',
 'Day 1: spend 2 hours on foundations and model APIs. || Day 1: spend 4 hours on RAG, prompts, and agents. || Day 2: spend 3 hours on security, operations, and evaluation. || Day 2: reserve 3 hours for the repository mock and 2 hours for error review.',
 'These times are study allocations, not evidence of readiness. Use recall results to move time toward weak skills.',
 'What receives priority when time is short?','Domain 1 has 31 percent. Domain 2 has 26 percent. Domain 3 has 20 percent. Keep Domain 4 and 5 in scope.')
L('Scenario decisions','','The credited option must satisfy every stated requirement at once.',
 'Identify the outcome, data source, trust boundary, and failure mode. || Mark hard limits for residency, response time, cost, and operations. || Eliminate options that fail one hard requirement. || Compare the remaining options against the requested objective.',
 'A managed service is not automatically correct. A residency or control requirement can force another design.',
 'A question asks for least operational effort. Should you choose the cheapest raw compute option?','Only if it also meets the operational objective. Compare the total required work and all hard constraints.')
L('Tokens, context, and inference','1.2.1 4.1.1','Inference predicts output from input. A token is a model-specific unit, not a fixed number of words.',
 'The context budget includes instructions, conversation, retrieved data, tools, and output reserve. || maxTokens limits generated output. It does not shorten input. || Count tokens with a supported tokenizer or CountTokens API. || Compare models with representative inputs and the same quality threshold.',
 'A larger context window does not guarantee that the model uses every fact well.',
 'A response stops halfway through valid JSON. What should you inspect first?','Inspect stopReason and the output token limit. Then test the total context budget. Do not raise temperature.','model-parameters converse-api')
L('Prompt, RAG, tools, or customization','1.1.1','Select the smallest architecture that meets the task and its constraints.',
 'Use prompts and examples for instructions, format, and task demonstrations. || Use RAG for external facts, current documents, and evidence references. || Use tools for current system state and authorized actions. || Consider customization for repeated behavior after prompt and retrieval tests.',
 'Fine-tuning can encode knowledge, but it does not provide automatic freshness or reliable document citations.',
 'A policy changes each week and answers require exact source passages. What is the first design?','Use authorized retrieval over the current policy. Return source references and test citation support.','knowledge-bases customization','rag')
L('Requirements and proof of concept','1.1.1 1.1.2','A proof of concept must test a business task with representative data and measurable acceptance limits.',
 'Record accuracy, latency percentiles, cost per successful task, and safety requirements. || Include long inputs, ambiguous requests, unavailable tools, and restricted documents. || Compare a baseline prompt with RAG or tools when the task requires them. || Decide whether to continue from measured results.',
 'Do not purchase fixed capacity before the workload and quality threshold are clear.',
 'A demo works for five examples. Is the architecture ready?','No. Test a representative evaluation set, failure paths, security controls, and expected traffic.','genai-lens evaluation')
L('Reusable architecture and the GenAI Lens','1.1.3','The Generative AI Lens applies architectural guidance to the GenAI lifecycle.',
 'Reuse a model gateway, prompt contract, evaluation harness, and telemetry schema. || Define ownership across data, application, model, and platform layers. || Review operational excellence, security, reliability, performance, cost, and sustainability. || Version infrastructure, prompts, retrieval configuration, and model configuration together.',
 'A framework review does not replace measurable tests or application authorization.',
 'Why use common components across teams?','They reduce inconsistent policy enforcement and duplicate work. Each use case still requires its own quality tests.','genai-lens')
L('Model selection','1.2.1','Select a model from measured task performance and required features.',
 'Check modality, context, language, tool use, structured output, and regional availability. || Benchmark factual quality and task completion on representative data. || Compare time to first token, total time, throughput, and cost. || Record unsupported features and fallback behavior before release.',
 'The largest model and the newest model are not universal answers.',
 'Which model wins when one is cheaper but fails the required quality floor?','Exclude it. Optimize cost only among models that meet every required threshold.','bedrock-overview evaluation')
L('Model access and authorization','1.2.1 3.2.1','Model activation and IAM authorization are separate checks.',
 'Many models use default access with the required Marketplace permissions. || Some providers or accounts require additional prerequisites. || Check model availability in the selected Region and account. || Check IAM, SCPs, permission boundaries, endpoint policy, and resource scope.',
 'The repository claim that every model requires a manual access request is outdated. AccessDenied can reflect IAM policy failures.',
 'An invocation returns AccessDenied. What is the correct diagnostic approach?','Inspect explicit denies, identity permissions, model prerequisites, Region, account access, and profile permissions. Do not assume one cause.','model-access iam')
L('Converse and InvokeModel','1.3.3 2.4.1','Converse provides a common message interface for supported models. InvokeModel uses model-specific payloads.',
 'Use Converse for supported conversation and tool-use workloads. || Use InvokeModel for supported model-specific inference, such as embeddings. || Use the runtime client for inference and the correct agent-runtime client for retrieval or agents. || Validate the model feature matrix before a provider switch.',
 'One Converse interface does not imply identical capabilities across models.',
 'Can one InvokeModel JSON body call every provider?','No. Match each provider schema. Converse reduces schema differences for models and features that support it.','converse-current converse-api bedrock-api')
L('Request and response contracts','1.3.3 2.5.1','Treat each model request and response as a versioned interface.',
 'Converse uses modelId, messages, optional system instructions, and inferenceConfig. || Pass supported toolConfig, guardrailConfig, or outputConfig only when appropriate. || Read content blocks, stopReason, usage, and metrics. || Validate structure and business meaning before any downstream action.',
 'Valid JSON does not establish factual accuracy, authorization, or safe tool parameters.',
 'A model returns a valid purchase object with an unauthorized account. What stops it?','Server-side authorization and business validation. Output schema checks alone cannot establish permission.','converse-api structured-output')
L('Temperature, top-p, and top-k','1.2.1 4.2.4','These controls affect token selection. They do not establish factual truth.',
 'Lower temperature generally reduces output variation. || Top-p limits the candidate set by cumulative probability. || Top-k limits the candidate set by count when the model supports it. || Tune supported parameters with an evaluation set and fixed prompt versions.',
 'Temperature zero does not guarantee identical output across all systems or correct facts.',
 'A grounded answer cites the wrong policy. Should temperature be the first change?','Inspect retrieved evidence, source freshness, and prompt use. Change the generation controls only after the cause is clear.','model-parameters')
L('Configuration without a code release','1.2.2 2.4.4','Separate model selection policy from provider-specific code.',
 'Use AppConfig for validated model and prompt configuration. || Route requests through an API and a stable internal model contract. || Use capability checks before a fallback or provider change. || Roll out configuration gradually with alarms and rollback.',
 'Changing the model ID alone can break tool schemas, token limits, safety settings, or response formats.',
 'How can a team switch models without application code changes?','Use an adapter layer and governed configuration. Test compatible capabilities before activation.','converse-current genai-lens','gateway')
L('Cross-Region inference and resilience','1.2.3','Inference profiles can route supported model requests across eligible Regions.',
 'Check the profile destination set against residency rules. || Authorize the source and required destination model resources. || Combine bounded retries with fallback and a circuit breaker. || Test degraded operation when the preferred model is unavailable.',
 'Cross-Region inference does not mean unrestricted global failover. A geography profile and a global profile have different boundaries.',
 'An application must keep data in one Region. Is a multi-Region profile automatically acceptable?','No. Verify each destination. Use a compliant regional design when any destination violates the requirement.','cross-region','resilience')
L('Customization choices','1.2.4','Customization changes model behavior or knowledge through an additional process.',
 'Fine-tuning uses task examples and target outputs. || Continued pre-training uses domain data where the model and service support it. || Distillation transfers behavior from a teacher to a smaller student where supported. || LoRA and adapters reduce the trainable parameter set in supported model workflows.',
 'Customization does not remove the need for retrieval, evaluation, or security controls.',
 'A team needs a stable domain format. How should it justify fine-tuning?','Compare prompt baselines with fine-tuning on a held-out set. Include deployment cost and regression risk.','customization sagemaker-deploy')
L('Customized model lifecycle','1.2.4 2.3.5','Treat a custom model as a versioned production dependency.',
 'Register model versions, input data versions, metrics, and approval status. || Use SageMaker Model Registry for governed SageMaker deployment workflows. || Test candidates with a canary and a rollback target. || Retire old versions after retention and recovery requirements permit it.',
 'A successful training job does not prove safe or cost-effective production behavior.',
 'A new version harms output quality. Which artifact allows a reliable rollback?','A known-good model version with its prompt, retrieval settings, container, and infrastructure configuration.','sagemaker-deploy customization')
L('Data quality before inference','1.3.1 1.3.4','Bad source data becomes bad retrieval and bad answers.',
 'Check completeness, schema, duplicates, encoding, freshness, and document ownership. || Use Glue Data Quality for rules and quality metrics. || Use Lambda or SageMaker Processing for normalization and validation. || Quarantine failed records and emit actionable metrics.',
 'An LLM can reformat text but can also alter facts. Verify extracted values against the source.',
 'Two current policy versions conflict. What should the pipeline do?','Resolve version precedence with source metadata. Quarantine unresolved conflicts. Do not ask generation to hide the conflict.','knowledge-bases')
L('Multimodal data preparation','1.3.2 2.5.3','Each modality needs a suitable extraction and validation path.',
 'Use Textract for document text, forms, and tables where appropriate. || Use Transcribe for audio transcripts and Comprehend for entity or PII analysis. || Use Bedrock Data Automation for supported multimodal extraction workflows. || Preserve source location, timestamp, confidence, and access metadata.',
 'OCR text can lose table relationships. An image-capable model does not automatically solve every layout error.',
 'A financial table produces wrong totals. Which layer should you inspect?','Inspect extraction, row-column relationships, units, and source values before the prompt.','bedrock-data-automation knowledge-bases','ingest')
L('Vector search from first principles','1.4.1','An embedding maps content into a vector space. A vector index retrieves nearby representations.',
 'Embed the document chunks and query with compatible model settings. || Store source ID, text reference, version, and access metadata beside each vector. || Use similarity search for conceptual matches. || Use lexical search for exact identifiers or terms when needed.',
 'Embedding similarity is not a probability that a passage or answer is true.',
 'An exact product code fails semantic search. What can help?','Use hybrid lexical and vector retrieval. Preserve exact identifiers in indexed text and metadata.','knowledge-bases retrieval','vector')
L('Vector store selection','1.4.1 1.5.3','Select a store from retrieval, scale, transaction, and operational requirements.',
 'OpenSearch supports search-focused architectures with vectors and lexical retrieval. || Aurora PostgreSQL with pgvector can combine relational data and vector queries. || Knowledge Bases supports a defined set of vector store integrations. || Validate filtering, hybrid search, dimensions, region, and cost for the chosen integration.',
 'DynamoDB metadata storage does not automatically make DynamoDB a substitute for a supported vector index.',
 'A team needs SQL joins plus embeddings beside existing relational records. Which option should it assess?','Assess Aurora PostgreSQL with pgvector. Confirm performance and the required Knowledge Bases integration support.','knowledge-bases retrieval')
L('Metadata and authorized retrieval','1.4.2 3.2.1','Metadata gives each retrieved passage context and access boundaries.',
 'Store tenant, document ID, version, effective date, language, and classification. || Derive tenant filters from authenticated identity on the server. || Apply access filters before evidence reaches the model. || Preserve source references through retrieval, response, and audit records.',
 'A prompt instruction such as use only my tenant cannot replace authorization.',
 'Two tenants ask the same question. Can they share one semantic cache entry?','Only when access scopes and source permissions permit the same content. Include tenant and authorization scope in cache policy.','retrieval knowledge-bases','secure-rag')
L('Vector scale and integration','1.4.3 1.4.4','Index layout and connector behavior affect relevance, isolation, and latency.',
 'Partition by domain or tenant when the access and scale model requires it. || Balance shards and replicas against query and update traffic. || Use connectors, APIs, AppFlow, or custom extraction for enterprise sources. || Monitor index memory, refresh lag, query latency, and failed updates.',
 'More shards can increase overhead. Tune from representative load tests.',
 'Search latency rises after a large import. What should you inspect?','Inspect shard distribution, memory, refresh activity, query filters, and competing ingestion traffic.','knowledge-bases genai-lens')
L('Fresh vectors and document deletion','1.4.5','A source edit does not help answers until retrieval sees the current version.',
 'Use version-aware incremental sync and change detection. || Retry failed ingestion with idempotent document identifiers. || Remove stale vectors and cached responses after source deletion or permission change. || Record ingestion status, update lag, and the last successful sync.',
 'A successful source upload is not proof of successful indexing.',
 'Answers cite a deleted policy. Where do you investigate?','Inspect source deletion behavior, ingestion results, index state, metadata filters, and caches.','kb-sync','ingest')
L('Chunking choices','1.5.1','Chunk size trades focused retrieval against complete context.',
 'Fixed-size chunks use a token limit and overlap. || Semantic chunks follow meaning changes and add processing cost. || Hierarchical chunks retrieve children and return broader parent context. || No chunking treats each document as one chunk and suits carefully prepared small documents.',
 'Hierarchy can return fewer results than requested after parent replacement. More chunks are not always more evidence.',
 'A clause depends on the previous paragraph. What should you test?','Test overlap, semantic boundaries, or parent context. Evaluate retrieval and answer quality together.','chunking','chunk')
L('Embedding selection and migration','1.5.2','An embedding model defines the space in which similarity has meaning.',
 'Compare domain fit, language, dimensions, input length, latency, and storage cost. || Use the same compatible configuration for document and query vectors. || Batch embedding jobs where the pipeline permits it. || Re-embed and rebuild the index when a model change creates an incompatible space.',
 'Equal dimensions do not imply compatible vector spaces.',
 'A team changes only the query embedding model. What can fail?','Query vectors can become incomparable with stored document vectors. Rebuild and validate the compatible corpus index.','knowledge-bases')
L('Hybrid retrieval and reranking','1.5.4','A search stage finds candidates. A reranker scores the candidates for the query.',
 'Vector search matches meaning. Lexical search matches exact terms. || Hybrid search combines both signals where the integration supports it. || Retrieve a candidate set and rerank before prompt construction. || Balance final context size against recall, cost, and latency.',
 'A reranker cannot recover a relevant passage that the candidate stage never returns.',
 'Product codes matter, but users paraphrase descriptions. Which search approach should you test?','Test hybrid retrieval followed by reranking. Measure exact-code accuracy and semantic recall.','retrieval','rerank')
L('Query transformation and decomposition','1.5.5','A user question can require several retrieval operations.',
 'Rewrite unclear queries without changing their meaning. || Expand terms when domain synonyms matter. || Decompose multi-part questions into evidence requests. || Aggregate evidence with source references and an explicit context budget.',
 'Uncontrolled expansion can add irrelevant evidence or broaden data access.',
 'One question compares two policies from different years. What retrieval plan fits?','Retrieve each policy with explicit year and version filters. Compare the passages after both evidence sets are present.','retrieval')
L('Retrieval APIs and tool contracts','1.5.6','A stable retrieval contract separates evidence access from answer generation.',
 'Retrieve returns evidence for custom generation workflows. || RetrieveAndGenerate combines managed retrieval and generation with source references. || A function or MCP interface can expose controlled search to an agent. || Return source, access scope, score meaning, and failure status explicitly.',
 'Converse does not automatically query a Knowledge Base. Connect retrieval through application logic or a supported managed workflow.',
 'Which API fits custom evidence inspection before generation?','Use Retrieve. Inspect and authorize evidence, then construct the model request.','kb-retrieve-api kb-rag-api','rag')
L('Prompt structure and instruction boundaries','1.6.1 1.6.5','A prompt states the task, constraints, evidence, and required output.',
 'Place stable behavior in system instructions where the model supports them. || Separate user content and retrieved evidence from trusted instructions. || Use examples for the exact task and output format. || Require source-supported answers and an explicit insufficient-evidence response.',
 'Instruction hierarchy helps model behavior but does not create a security boundary.',
 'A retrieved document says ignore all previous rules. What should happen?','Treat the sentence as untrusted source content. Enforce tool and data permissions outside the model.','prompt-management guardrails')
L('Conversation state and clarification','1.6.2','Conversation history is application data with a token budget and an access scope.',
 'Persist session records with authenticated ownership, such as in DynamoDB. || Summarize or prune history under tested rules. || Ask for missing required fields before a tool action. || Separate durable user preferences from short-lived request state.',
 'Bedrock inference calls do not replace application session control. A summary can lose important constraints.',
 'An assistant loses an earlier spending limit. What should you change?','Keep the limit in validated structured state and include it in authorization checks. Do not rely only on a conversation summary.','converse-current','chat')
L('Prompt management and regression','1.6.3 1.6.4','Prompts require version control, release control, and tests.',
 'Use Prompt Management for reusable prompt resources and versions. || Store test datasets, parameter values, and evaluation results with the prompt version. || Use CI/CD or orchestration for approval steps and policy gates. || Track prompt access and operations with the appropriate logs.',
 'A prompt resource does not establish a complete organizational approval workflow by itself.',
 'A prompt edit fixes one example and breaks another. What is missing?','A regression set and a release gate with defined task metrics.','prompt-management evaluation')
L('Flows and complex prompt systems','1.6.6 2.5.2 2.5.5','Bedrock Flows connects supported workflow nodes in an explicit process.',
 'Use sequential nodes for fixed prompt and retrieval stages. || Use conditions for branches with clear business rules. || Use reusable components and validated input-output contracts. || Compare a flow with Step Functions when integrations, retries, or approvals require broader orchestration.',
 'A fixed workflow and an autonomous agent solve different control problems.',
 'A document workflow always extracts, validates, and summarizes. Does it require an autonomous agent?','No. A deterministic workflow can provide clear control and simpler tests. Use an agent when dynamic tool decisions add value.','flows','workflow')
L('Agent loop and state','2.1.1 2.1.2','An agent uses model output to choose a tool, observe its result, and continue toward a goal.',
 'Maintain task state, conversation state, and durable memory separately. || Use ReAct-style cycles for action and observation. || Persist tool results with correlation IDs and the responsible identity. || Stop on success, a step limit, a deadline, or an unrecoverable error.',
 'A model proposal is not an authorized action. The tool service must enforce permission and input validity.',
 'Why can an agent loop fail despite a correct model response?','The tool can fail, return stale data, or repeat a side effect. Test the complete loop and state transitions.','agents agentcore strands','agent')
L('Strands, Agent Squad, and managed agents','2.1.1 2.5.5','Distinguish agent development frameworks from managed service components.',
 'Strands provides an SDK for model-driven agent loops and tools. || Agent Squad supports coordination across agents and routing patterns. || Bedrock Agents provides managed orchestration with supported tools and knowledge sources. || AgentCore provides components for agent deployment and operation.',
 'The framework name does not prove that memory, authorization, or evaluation is automatic.',
 'An existing custom framework needs managed execution. Must the team rewrite the agent as Bedrock Agents?','No. Assess AgentCore Runtime compatibility and required protocols before a rewrite.','agentcore strands','agent')
L('Bounded agent execution','2.1.3','Agent reliability needs explicit stopping rules and resource limits.',
 'Set a maximum step count, elapsed time, token budget, and tool budget. || Use timeouts and circuit breakers around unreliable tools. || Limit role permissions to approved resources and actions. || Return a clear partial result when a safe limit ends execution.',
 'A system prompt that says do not loop cannot replace an enforced step limit.',
 'An agent repeats the same failed call. Which controls help?','Track repeat calls, use bounded retries, enforce a step budget, and open a circuit after repeated failures.','agents genai-lens','agent')
L('Multi-agent coordination','2.1.4','Specialized agents can divide work when their interfaces and authority remain clear.',
 'Use a supervisor for routing and result synthesis where that pattern fits. || Use specialized models or agents for distinct capabilities. || Validate collaborator outputs against a shared task contract. || Measure coordination cost, failure propagation, and task completion.',
 'More agents add latency and failure paths. A single workflow can be better for a fixed process.',
 'A supervisor combines contradictory answers. What is missing?','A defined evidence contract, conflict resolution rule, and evaluation of the combined result.','agents strands','multiagent')
L('Human review and approvals','2.1.5','Human review controls consequential actions and unresolved uncertainty.',
 'Pause the workflow before the side effect. || Show the exact proposed action, evidence, and relevant limits. || Bind approval to the actor, action, parameters, and expiry. || Record the decision and resume with an idempotency key.',
 'Approval of a general goal does not validate changed parameters or a different transaction.',
 'An agent proposes a refund. Where should human approval occur?','After parameter validation and before the refund tool executes. Bind approval to the exact refund.','genai-lens','approval')
L('Tool schemas and reliable side effects','2.1.6','A tool definition describes an interface. The implementation controls its behavior.',
 'Define names, parameter types, required fields, and response types precisely. || Validate input, authorization, and business rules on the server. || Use idempotency for retryable write operations. || Return structured errors that distinguish retryable and permanent failures.',
 'A timeout does not prove that a side effect failed. A blind retry can duplicate the action.',
 'A payment call times out after the service accepts it. What prevents duplicate payment?','An idempotency key and an operation status lookup. Do not retry with a new transaction identity.','converse-api agents','tool')
L('MCP client and server','2.1.7 1.5.6','MCP standardizes how a client discovers and uses server capabilities.',
 'Expose narrow tools with explicit schemas and least privilege. || Use Lambda for suitable lightweight stateless integrations. || Use containers when long-lived or complex tool services require them. || Authenticate the client and authorize each downstream operation.',
 'MCP is an interface protocol. It does not make every tool safe or every result trustworthy.',
 'Should an MCP server receive administrator access for flexible tools?','No. Scope credentials to approved operations and validate every request outside the model.','agentcore strands','mcp')
L('AgentCore component boundaries','2.1.1 2.1.7','Select AgentCore components by the responsibility each one supplies.',
 'Runtime executes agents and tools in supported environments. || Gateway exposes supported tools through managed access interfaces. || Memory manages supported state and memory use cases. || Identity and observability address access and operational insight.',
 'A managed runtime does not remove application-specific authorization or evaluation duties.',
 'A custom agent needs tool access and memory. Which design decision comes first?','Separate execution, tool access, identity, and memory requirements. Select and configure each required component.','agentcore agentcore-runtime','agentcore')
L('Deployment modes','2.2.1','Match deployment to traffic, model support, control requirements, and operational effort.',
 'Use Bedrock on-demand inference for supported variable workloads. || Assess Provisioned Throughput for supported models and capacity requirements. || Use SageMaker endpoints when supported custom hosting and runtime control matter. || Keep invocation and deployment capacity identifiers consistent.',
 'Lambda can invoke a model. It is not the host for a large GPU model.',
 'The team buys provisioned capacity but still invokes the base model ID. What should it verify?','Verify the correct provisioned resource ARN and invocation path. Capacity selection does not automatically rewrite application calls.','bedrock-provisioned sagemaker-deploy')
L('LLM hosting mechanics','2.2.2','Large models can face memory and token throughput limits that differ from small predictive models.',
 'Plan for model weights, runtime overhead, KV cache, and concurrent requests. || Assess quantization, model parallelism, and supported inference containers. || Measure cold start, model load time, and warm capacity. || Scale against token work and latency, not request count alone.',
 'A GPU with enough memory for weights can still lack memory for the target concurrency.',
 'Longer prompts cause out-of-memory failures at the same request rate. Why?','Prompt and generated tokens increase KV cache and runtime memory use. Test realistic sequence lengths and concurrency.','sagemaker-deploy')
L('Small models and cascades','2.2.3 4.1.2','A cascade uses a lower-cost path for suitable tasks and escalates when the task requires more capability.',
 'Route with validated task classes, rules, or calibrated evaluation signals. || Use a smaller model only when it meets the required quality floor. || Include routing and escalation costs in the comparison. || Track quality by task segment after deployment.',
 'A model saying I am confident is not a calibrated probability of correctness.',
 'A small model handles routine classification well. Must every request use the flagship?','No. Use the validated smaller path for those tasks. Define and test escalation criteria.','evaluation genai-lens','cascade')
L('Enterprise events and APIs','2.3.1 2.3.2','Integration style follows the response contract and failure behavior.',
 'Use synchronous APIs when callers need an immediate result. || Use SQS for buffered work and backpressure. || Use EventBridge for event routing across decoupled systems. || Use Step Functions for explicit multi-step state, retry, and recovery.',
 'An event bus routes events. It does not replace every queue or durable workflow.',
 'A document arrives in S3 and needs extraction, validation, and indexing. Which pattern fits?','Use an event-driven workflow with durable state and failure handling. Keep ingestion idempotent.','genai-lens','ingest')
L('Federation and secure enterprise access','2.3.3','User identity and service identity serve different purposes.',
 'Use federation or Cognito for supported user authentication. || Use execution roles and temporary credentials for AWS service calls. || Propagate trusted tenant and role context through the gateway. || Enforce object-level authorization at data and tool boundaries.',
 'An authenticated user can still lack permission for a particular document or action.',
 'Can a client-supplied tenant ID define a retrieval filter?','No. Derive the tenant scope from verified identity and server-side authorization.','iam vpc','gateway')
L('Hybrid, edge, and residency','2.3.4','Data location and model execution location are separate architectural facts.',
 'Use approved connectivity between cloud and on-premises systems. || Assess Outposts for supported on-premises AWS workloads. || Assess Wavelength for supported edge latency requirements. || Verify service and model availability before an edge or hybrid commitment.',
 'Outposts and Wavelength do not imply that every Bedrock foundation model runs locally.',
 'A rule prohibits source documents from leaving a site. Does a private network alone satisfy it?','No. Verify which content leaves the site, where processing occurs, and which services support the required local execution.','vpc genai-lens')
L('GenAI gateway and CI/CD','2.3.5','A gateway centralizes policy while CI/CD controls release quality.',
 'Apply request validation, identity checks, budgets, and model routing at the gateway. || Trace requests across retrieval, generation, and tool calls. || Use CodeBuild and CodePipeline for tests, scans, and release gates. || Version the complete application configuration and preserve rollback targets.',
 'Central routing without per-user data authorization can concentrate a security defect.',
 'A model passes unit tests but fails factual evaluations. Should the pipeline release it?','No. Require task quality, safety, latency, and cost gates appropriate to the application.','evaluation genai-lens','gateway')
L('Synchronous, asynchronous, and batch calls','2.4.1','These patterns differ in caller behavior and service support.',
 'Synchronous inference keeps the caller attached to one result. || Application-level async uses a queue, worker, and status record. || Service async operations exist only for supported models and tasks. || Batch inference processes supported bulk jobs without an interactive response.',
 'An application queue does not turn every model into a service-native asynchronous model.',
 'A nightly workload accepts delayed results. Which approach should you assess?','Assess supported batch inference first. Compare turnaround time, supported formats, and total cost.','batch bedrock-api','async')
L('Streaming from model to client','2.4.2 2.5.1','Streaming can improve time to first token while the full response still takes time.',
 'Use ConverseStream or InvokeModelWithResponseStream where supported. || Preserve streaming through every intermediary and client. || Distinguish partial text from a completed, validated response. || Plan moderation, interruption, cancellation, and error behavior.',
 'Streaming does not automatically reduce total token work or prevent unsafe partial content.',
 'The backend streams but the browser shows one final response. What should you inspect?','Inspect buffering, integration type, protocol support, proxies, and client parsing across the full path.','converse-stream-api response-stream','stream')
L('Retries, backpressure, and circuit breakers','2.4.3','Retry only when the failure class and remaining request budget permit it.',
 'Use exponential backoff with jitter for appropriate transient errors. || Bound retry count and total elapsed time. || Queue excess work and cap concurrent invocations. || Use a circuit breaker or tested fallback after repeated service failures.',
 'Immediate retries amplify throttling. Retries cannot fix a malformed request or missing permission.',
 'A traffic spike causes throttling. What is the first architectural response?','Apply backpressure and bounded retries. Measure token quotas and concurrency before capacity or routing changes.','bedrock-errors cross-region','resilience')
L('Routing policy and fallback quality','2.4.4','Routing needs both an availability policy and a capability policy.',
 'Use static routes for known task classes. || Use dynamic routing when measured signals justify its overhead. || Preserve residency and authorization constraints on every route. || Re-evaluate prompts, output contracts, and tools for each fallback model.',
 'A fallback that returns an invalid business result is not a successful recovery.',
 'The preferred model fails. Can the next available model always answer?','Only if it meets the task, safety, schema, Region, and quality requirements. Otherwise return a controlled failure.','converse-current cross-region','cascade')
L('Application interfaces and workflow tools','2.5.2 2.5.3','A useful AI interface exposes task progress, uncertainty, and the next permitted action.',
 'Use Amplify for suitable application interface development. || Use OpenAPI contracts for stable client integration. || Use Flows for supported visual workflow authoring. || Add GenAI to CRM or document systems through controlled service interfaces.',
 'A polished chat interface cannot compensate for an incorrect evidence or authorization path.',
 'A document process needs typed fields before a CRM update. What must happen before the update?','Validate extraction schema, source support, and field permissions. Obtain any required approval.','flows bedrock-data-automation')
L('Developer tools and diagnosis','2.5.4 2.5.6','Amazon Q Developer can assist development. The engineer remains responsible for correctness and security.',
 'Use assistance for code, refactoring, API examples, and error analysis. || Validate generated code against current API contracts. || Use Logs Insights for correlated application evidence. || Use X-Ray or compatible traces to locate latency and failure boundaries.',
 'Generated code can use old SDKs or invent fields. Verify execution and permissions.',
 'An AI suggestion requests broad administrator permissions. Should you accept it?','No. Determine the required API actions and resources. Use least privilege and validate the result.','bedrock-errors genai-lens')
L('Input safety and prompt attacks','3.1.1 3.1.5','Treat user content, documents, tool responses, and external pages as potentially adversarial.',
 'Use supported Guardrails content and prompt-attack controls. || Separate trusted instructions from untrusted evidence. || Sanitize and validate data at ingestion and tool boundaries. || Test direct injection, indirect injection, encoding tricks, and data exfiltration attempts.',
 'Keyword filters alone miss indirect and transformed attacks.',
 'A document tells the agent to send secrets to a URL. Which boundary must stop the action?','Tool authorization, destination restrictions, and secret access limits must stop it even if the model follows the instruction.','guardrails','safety')
L('Guardrails policy selection','3.1.1 3.1.2','Match the policy to the exact harm or business restriction.',
 'Use content filters for supported harmful content categories. || Use denied topics for defined prohibited subjects. || Use word filters for specific words or phrases. || Use sensitive information filters for supported PII and regex patterns.',
 'A denied topic and a word filter are not interchangeable. A business topic can use many different words.',
 'A bank prohibits investment advice but permits product facts. Which control should it assess?','A denied topic that describes the prohibited advice, plus tests for false positives and permitted product questions.','guardrails')
L('Guardrails placement and output safety','3.1.2 3.1.4','Protect the input, retrieved context, tool path, and final output with suitable controls.',
 'Apply Guardrails through supported inference integrations or ApplyGuardrail. || Validate output structure and business rules after generation. || Filter or mask sensitive outputs where policy requires it. || Design buffering and release rules for streaming output.',
 'One content check does not enforce retrieval permissions, tool authorization, or SQL safety.',
 'A model generates SQL. Does a safety filter make the query safe?','No. Validate the query, use a read-only role where appropriate, enforce data scope, and restrict execution.','guardrails guardrails-api','safety')
L('Grounding, relevance, and hallucination','3.1.3','Grounding asks whether the answer follows supplied evidence. Relevance asks whether it addresses the question.',
 'Use current authorized sources and preserve citations. || Evaluate support for each factual claim. || Use supported contextual grounding checks when appropriate. || Return uncertainty or insufficient evidence when support is absent.',
 'A citation can be real while its passage does not support the claim. JSON Schema cannot establish factual truth.',
 'An answer is fluent and well formatted but unsupported. Which metric detects the defect?','Faithfulness or grounding against the retrieved context. Also assess factual correctness against an authoritative reference.','guardrails-grounding evaluation','rag')
L('Automated Reasoning checks','3.1.3 3.4.3','Automated Reasoning checks assess responses against a formal policy within supported use cases.',
 'Translate policy material into a validated formal representation. || Check the response against policy rules and stated facts. || Inspect findings and route unsupported or ambiguous cases appropriately. || Maintain policy versions and regression tests after rule changes.',
 'Formal policy consistency is not a universal guarantee of truth outside the policy model.',
 'A refund answer contradicts a clear policy rule. Which additional check can help?','Assess Automated Reasoning checks with a validated refund policy. Keep data and authorization controls separate.','guardrails-reasoning')
L('Private network and IAM controls','3.2.1','PrivateLink controls network access paths. IAM controls permitted actions and resources.',
 'Create the appropriate interface endpoints for runtime and other required APIs. || Configure endpoint security groups, private DNS, and endpoint policy. || Use scoped execution roles and temporary credentials. || Verify data service, KMS, and tool permissions separately.',
 'A VPC endpoint does not grant IAM permission or prove that the application never uses another public path.',
 'A private subnet can reach S3 but cannot call Bedrock. What should you verify?','Check the runtime endpoint, DNS, network controls, IAM, endpoint policy, and model access.','vpc iam','private')
L('Encryption and secrets','3.2.1 3.2.2','Protect data in transit, stored content, indexes, logs, backups, and secrets.',
 'Use TLS for service traffic. || Use supported KMS encryption controls for stored data. || Restrict key use and inspect both IAM and key policy. || Store credentials in Secrets Manager and use temporary role credentials when possible.',
 'Encryption does not make an unauthorized read acceptable. KMS access can independently block an otherwise permitted workflow.',
 'S3 access succeeds but an encrypted source cannot be read. What should you inspect?','Inspect the KMS key policy, grants, role permissions, and service integration requirements.','data-protection iam')
L('PII discovery, redaction, and retention','3.2.2 3.2.3','Choose a control based on where the sensitive data exists and when it must be protected.',
 'Use Macie to discover sensitive data in supported S3 analysis workflows. || Use Comprehend for supported PII detection in text. || Use Guardrails sensitive information controls in supported model paths. || Apply retention and deletion rules to sources, vectors, conversation state, and logs.',
 'Masking can leave re-identification risk. Deleting an S3 object does not remove every derivative automatically.',
 'PII appears in prompt logs. Is an output-only filter sufficient?','No. Minimize or redact inputs and logs, restrict access, and enforce retention. Review all data paths.','data-protection data-retention guardrails','pii')
L('Bedrock privacy boundaries','3.2.2','Distinguish model provider access from application storage and service-specific retention.',
 'AWS states that model providers lack access to Bedrock deployment accounts and customer prompts there. || Review current data retention and abuse detection terms for the selected service and model. || Treat enabled invocation logs as sensitive application data. || Apply your own access, deletion, and encryption controls.',
 'Do not generalize a claim about base inference to every optional feature, logging setting, or model offering.',
 'Does a provider privacy statement mean the team can log prompts without restrictions?','No. Your application logs can contain confidential data and require a separate retention and access policy.','data-protection data-retention logging')
L('Governance, model cards, and lineage','3.3.1 3.3.2','Governance links decisions to data, model versions, policies, and accountable owners.',
 'Document intended use, limits, evaluation evidence, and approval status in model cards. || Register source datasets and metadata with suitable catalog controls. || Preserve document and prompt versions in decision records. || Retain audit evidence under defined access and retention rules.',
 'A catalog entry does not automatically prove complete data lineage or regulatory compliance.',
 'An auditor asks why an answer changed. Which records matter?','The model, prompt, retrieval configuration, source version, tool outputs, and policy version for each request.','genai-lens logging')
L('Policy ownership and continuous controls','3.3.3 3.3.4','An organization needs policy owners, release rules, and controls that continue after deployment.',
 'Define permitted use cases, data classes, escalation, and exception owners. || Monitor misuse, policy violations, quality drift, and cost anomalies. || Redact sensitive telemetry and restrict audit access. || Connect alerts to tested remediation and review workflows.',
 'A one-time launch review cannot detect future data, model, or usage changes.',
 'A safe assistant drifts after a new document import. What should trigger review?','A quality or policy alarm tied to the data change, with evidence and a known rollback or quarantine action.','genai-lens evaluation')
L('Transparency and uncertainty','3.4.1','A useful explanation shows evidence, limits, and the basis for a decision.',
 'Show source passages and relevant task constraints. || Record trace events and tool outcomes for diagnosis. || Report measured uncertainty only when the measure has a valid interpretation. || Give users a review path for consequential errors.',
 'Do not equate hidden chain-of-thought, a fluent explanation, or a model confidence claim with proof.',
 'How should a medical policy assistant explain a recommendation?','Show the authoritative policy evidence, applicable limits, and uncertainty. Route decisions that require professional review.','evaluation genai-lens')
L('Fairness and responsible AI evaluation','3.4.2 3.4.3','Fairness tests compare relevant user groups and scenarios under a defined task policy.',
 'Use representative and adversarial evaluation sets. || Compare outcome quality, refusal errors, and safety by relevant segment. || Use human review for context that automatic metrics miss. || Repeat tests after model, prompt, source, or policy changes.',
 'An LLM judge can reproduce bias. An overall average can hide a poor subgroup result.',
 'A model passes an overall quality threshold but fails one user group. Can the average justify release?','No. Evaluate the subgroup failure against the stated fairness and safety requirements.','evaluation genai-lens')
L('Token cost and context efficiency','4.1.1','Cost depends on the selected model, pricing mode, tokens, and optional services.',
 'Estimate input and output tokens separately. || Remove duplicate evidence, obsolete history, and unnecessary output. || Reserve enough output budget for the task. || Compare cost per successful task with its quality and latency.',
 'A shorter prompt can omit decisive evidence. Cost reduction must preserve the acceptance criteria.',
 'Which cost metric handles retries and failed answers better than cost per call?','Cost per successful task. Include retries, retrieval, orchestration, evaluations, and operational services.','prompt-cache genai-lens')
L('A worked cost comparison','4.1.1 4.1.2','The following values are illustrative assumptions from the repository, not a current AWS price quote.',
 'Input price: $3 per million tokens. Output price: $15 per million tokens. || Input: 4,000 tokens. Output: 1,000 tokens. || Input cost: $0.012. Output cost: $0.015. Total: $0.027. || Compare alternatives at the same successful-task volume and quality level.',
 'The example excludes storage, retrieval, logs, networking, tools, retries, and taxes.',
 'Why can output limits matter more than a small prompt reduction here?','The assumed output price is five times the input price per token. Confirm current model rates before any financial decision.','repo-d1')
L('Prompt cache and result cache','4.1.4','Prompt caching reuses eligible model context. Result caching reuses an application answer.',
 'Use prompt caching for supported repeated prefixes and model-specific rules. || Use exact result caching when request identity and freshness permit it. || Use semantic result caching only with tested equivalence and access controls. || Include model, prompt, source, tenant, and policy versions in cache decisions.',
 'A cache hit can return an outdated or unauthorized answer if the key omits state or identity.',
 'Users ask different questions about one long document. Which cache can reduce repeated prefix processing?','Prompt caching where the model supports it. Each new answer still requires generation.','prompt-cache','cache')
L('Prompt cache limits and measurements','4.1.4 4.3.2','Cache support, token thresholds, TTL, and price differ by model and API.',
 'Place stable content before changing content when the cache design requires a shared prefix. || Confirm supported cache checkpoints and minimum token thresholds. || Read cache write and cache read usage fields. || Compare actual hit rates and effective cost on representative traffic.',
 'Do not memorize a universal five-minute TTL. Current documentation lists model-specific cache behavior.',
 'Caching is enabled but cost does not fall. What should you inspect?','Inspect prefix stability, minimum tokens, expiry, supported fields, actual hits, and cache write charges.','prompt-cache')
L('Capacity and throughput','4.1.3 4.2.3 4.2.5','Capacity planning must account for prompt length, output length, concurrency, and quota.',
 'Measure token demand and latency by task class. || Use supported batching or bulk inference for suitable work. || Compare on-demand and provisioned modes for measured traffic. || Scale self-hosted endpoints from relevant utilization and queue signals.',
 'Provisioned capacity does not guarantee every response latency. Model support and commitment terms vary.',
 'Request count is stable but throttling rises. What changed?','Check input and output token lengths, concurrency, quota dimensions, and retry amplification.','bedrock-provisioned batch')
L('Latency and critical path','4.2.1 4.2.6','Measure each stage before a latency change.',
 'Separate authentication, retrieval, reranking, generation, and tool time. || Track time to first token and full response time. || Parallelize independent work when resource and policy limits permit it. || Use supported latency-optimized modes only after quality and cost tests.',
 'Streaming improves perceived response time but does not remove a slow retrieval stage.',
 'Retrieval takes most of the request time. Would a faster model solve the main problem?','No. Optimize retrieval filters, index behavior, query work, and evidence volume first.','genai-lens retrieval','latency')
L('Retrieval optimization','4.2.2 4.3.5','Optimize search with relevance and latency metrics together.',
 'Inspect candidate recall before the generation stage. || Tune index layout, metadata filters, and query preprocessing. || Test hybrid scoring and reranker candidate counts. || Monitor stale documents, failed embeddings, and source synchronization.',
 'A smaller top-k can reduce cost while hiding required evidence.',
 'How should a team select the number of returned passages?','Measure retrieval recall, answer support, latency, and prompt cost over representative queries.','retrieval evaluation','rerank')
L('Observability by request and task','4.3.1 4.3.3','Telemetry must explain technical health and business outcomes.',
 'Propagate a correlation ID across gateway, retrieval, model, and tools. || Capture model and prompt versions, token use, stop reasons, and latency. || Track task completion, user correction, quality scores, and safety events. || Restrict telemetry access and remove unnecessary sensitive content.',
 'CloudWatch does not infer hallucination rate from raw service metrics. Supply evaluated custom metrics.',
 'Availability is high but users reject answers. Which additional signal matters?','Task quality and completion metrics with representative evaluated samples.','logging evaluation','observe')
L('CloudTrail and invocation logs','4.3.2 3.3.2','Audit events and model request bodies have different purposes and controls.',
 'Use CloudTrail for supported API audit events and identity evidence. || Configure required data event coverage explicitly. || Enable supported model invocation logging for detailed request and response analysis. || Use CloudWatch Logs or S3 destinations with encryption, access limits, and retention.',
 'CloudTrail is not a universal store for prompt and completion bodies. Invocation logging needs explicit configuration.',
 'An auditor needs who called the API and what prompt produced an answer. Is one default log enough?','No. Combine configured audit coverage with protected application or invocation logs and correlation IDs.','bedrock-cloudtrail logging')
L('Tools, agents, and vector telemetry','4.3.4 4.3.5','An agent can fail in a tool or retrieval stage while model inference succeeds.',
 'Track tool name, arguments after redaction, latency, retry count, and result status. || Measure agent steps, repeated calls, completion rate, and cost. || Monitor vector query latency, ingestion lag, and retrieval quality. || Alert on deviations from task-specific baselines.',
 'A successful HTTP response can still contain a failed business operation.',
 'An agent suddenly spends more tokens per task. What should you trace?','Inspect extra steps, tool failures, repeated retrieval, larger histories, and changed model or prompt versions.','agentcore logging','observe')
L('GenAI failure diagnosis','4.3.6','Use a reproducible case and change one relevant layer at a time.',
 'Replay a fixed golden dataset with versioned configuration. || Compare evidence, prompts, tool traces, and outputs. || Separate retrieval failure from unsupported generation. || Route failures to the correct owner with source evidence.',
 'Exact output diffs can overcount harmless wording changes. Use semantic and task-aware checks.',
 'The same question fails only after a source update. What is the best first comparison?','Compare old and new source versions, chunks, metadata, and retrieved evidence before model changes.','evaluation logging')
L('Evaluation dimensions','5.1.1','A useful evaluation set measures the task rather than only text similarity.',
 'Measure correctness, relevance, completeness, consistency, and fluency as appropriate. || Add safety, privacy, latency, and cost thresholds. || Include expected outputs or evidence with clear rubrics. || Report results by important task and user segments.',
 'A fluent answer can be wrong. A lexically different answer can be correct.',
 'Two answers use different words but convey the same supported facts. What should the metric recognize?','Semantic and task equivalence. Exact string equality alone is too narrow for that task.','evaluation')
L('Programmatic, judge, and human evaluation','5.1.2 5.1.5','These methods provide different evidence and can complement each other.',
 'Use deterministic checks for schema, required values, and business rules. || Use model-based judges for rubric-based assessment at scale. || Use domain experts for difficult or consequential judgments. || Use Bedrock evaluation jobs where the required models, data, and metrics are supported.',
 'A judge model is a measurement tool with bias and uncertainty. It is not ground truth.',
 'Which method can prove that JSON contains required fields?','A schema validator. Human or model review can then assess semantic correctness and usefulness.','evaluation')
L('Judge design and calibration','5.1.5','A judge needs a clear rubric and calibration against human labels.',
 'Define the criterion and score anchors before the test. || Hide model identity when it could bias the judgment. || Test position bias and reverse pair order for pairwise comparisons. || Measure agreement with expert labels and review disagreements.',
 'A judge may favor verbose answers or its own model family. Do not treat one score as objective truth.',
 'A judge always prefers the first answer. How can you detect the issue?','Swap answer order, randomize presentation, and compare scores against human-labeled examples.','evaluation')
L('RAG retrieval metrics','5.1.6','Retrieval tests ask whether the necessary evidence appears in the candidate set.',
 'Recall@k measures the share of relevant items found within k results. || Precision@k measures the share of returned items that are relevant. || MRR emphasizes the rank of the first relevant result. || Evaluate ranking metrics and retrieval latency against query-level ground truth.',
 'Higher recall alone can add noisy context. Score generation quality as well.',
 'The right passage exists but appears below the returned cutoff. Which stage needs work?','Candidate retrieval or ranking. Test hybrid search, filters, query transformation, and the cutoff.','evaluation retrieval')
L('RAG answer metrics','5.1.5 5.1.6','Score the retrieval stage and the answer stage separately.',
 'Check context relevance for the retrieved evidence. || Check faithfulness for support in the supplied context. || Check answer correctness against authoritative ground truth. || Check completeness and citation support for the user question.',
 'An answer can be faithful to an outdated source and still be factually wrong.',
 'The answer follows the passage, but the passage contains an old policy. Is this a generation failure?','The main defect is source freshness or version selection. Fix the source and retrieval path.','evaluation evaluation-metrics','rag')
L('Feedback and annotation','5.1.3','User feedback provides signals that require context and review.',
 'Capture the task, output version, and a useful error category. || Let reviewers label unsupported facts, missing evidence, and unsafe behavior. || Remove sensitive content that the evaluation process does not need. || Feed reviewed failures into the regression set.',
 'A thumbs-up signal alone cannot establish factual correctness.',
 'A user dislikes a correct refusal. Should the team optimize only for approval rate?','No. Evaluate policy compliance and task usefulness with human review and a defined rubric.','evaluation')
L('Regression gates and model comparisons','5.1.2 5.1.4','A release comparison must hold the task and evaluation method steady.',
 'Use a held-out golden dataset with versioned references. || Compare candidate and baseline on quality, safety, latency, and cost. || Define release and rollback thresholds before the experiment. || Run the gate after prompt, model, data, retrieval, or tool changes.',
 'Do not tune repeatedly on the only test set. Preserve a held-out measure of generalization.',
 'A model improves average quality but breaks a critical workflow. Should average gain win?','No. Apply the required workflow and safety thresholds before aggregate optimization.','evaluation genai-lens','eval')
L('A/B, canary, and shadow tests','5.1.2 5.1.9','These deployment patterns answer different questions.',
 'A/B tests compare alternatives on controlled traffic groups. || Canary releases expose a limited production share before expansion. || Shadow tests send copied inputs to a candidate without its normal production effect. || Synthetic tests probe critical user journeys with known expectations.',
 'Shadow tools must not duplicate real side effects. A canary still needs rollback rules.',
 'Which pattern measures candidate behavior on real inputs before users receive its output?','A shadow test with isolated side effects and approved data handling.','evaluation genai-lens')
L('Agent evaluation','5.1.7','Evaluate the complete task path, including tools, state, and side effects.',
 'Measure task completion and correct tool selection. || Validate arguments, action order, and authorization behavior. || Measure step count, tool failures, recovery, latency, and cost. || Test long tasks, interruptions, repeated requests, and malicious tool results.',
 'A good final answer can hide an unsafe intermediate action.',
 'An agent completes a task but calls an unauthorized tool first. Is it a pass?','No. The evaluation must include intermediate actions and security boundaries.','evaluation agentcore','agent')
L('Reports that support a decision','5.1.8','A report should show the release decision and the evidence behind it.',
 'Present sample count, dataset version, rubric, and important segments. || Compare baseline and candidate with quality, latency, safety, and cost. || Show known failures and uncertainty instead of only averages. || State the owner, decision, and rollback or follow-up action.',
 'A precise percentage from a tiny or biased sample can mislead.',
 'Which result is more useful than one overall quality score?','A task-segment comparison with critical failures, uncertainty, and acceptance thresholds.','evaluation')
L('Context overflow and truncation','5.2.1','Distinguish an oversized request from an output that stops at its limit.',
 'Count system, messages, tools, retrieved data, and output reserve. || Inspect stopReason and any validation error. || Prune or summarize tested history and reduce noisy evidence. || Use segmentation or a suitable model when the complete task exceeds the limit.',
 'Raising maxTokens can worsen the total budget. Character count is not a reliable token count.',
 'A request fails before any token returns. Is the output token cap the only suspect?','No. Check total context, input schema, model support, quota, and the specific error response.','converse-api bedrock-errors')
L('API failure classification','5.2.2','The error class determines the next step.',
 'AccessDenied: inspect identity, policy, model access, Region, and profile permissions. || ValidationException: inspect schema, unsupported parameters, and size limits. || Throttling: inspect quotas, token load, concurrency, and retry behavior. || Timeout or service failure: inspect latency, retry safety, and fallback policy.',
 'Do not retry permission failures or invalid requests without a relevant change.',
 'A request fails after a provider switch. What should you inspect before retries?','Inspect the new model capabilities, request schema, supported parameters, Region, and endpoint.','bedrock-errors model-access')
L('Prompt defect diagnosis','5.2.3 5.2.5','Prompt diagnosis needs versioned inputs, outputs, and expected behavior.',
 'Check unresolved template variables and conflicting instructions. || Inspect message order, examples, system support, and source delimiters. || Validate output format and stop conditions. || Change one prompt feature and run the regression set.',
 'Adding more instructions can create conflicts and consume the evidence budget.',
 'Only one prompt version breaks extraction. What is the best first test?','Replay the same cases against both versions. Compare template expansion, schema, and evidence placement.','prompt-management converse-api')
L('Retrieval defect diagnosis','5.2.4','Trace the evidence path before a generation change.',
 'Verify source presence, latest version, and ingestion success. || Verify embedding model, dimensions, and document-query compatibility. || Inspect chunk boundaries, metadata, filters, and ranked candidates. || Check reranking, final context assembly, and cached answers.',
 'A model upgrade cannot reliably fix missing or unauthorized evidence.',
 'The correct document is indexed but never returned for one tenant. What should you inspect?','Inspect tenant metadata and server-side filter construction first. Then inspect query and ranking behavior.','retrieval kb-sync','rag')
L('End-to-end secure RAG case','1.1.1 2.3.5 3.2.1 5.1.5','A policy assistant needs current evidence, tenant isolation, citations, and an auditable response path.',
 'Authenticate the user and derive the permitted data scope. || Retrieve current authorized passages and rerank when justified. || Construct a bounded prompt and apply the required safety controls. || Validate the answer, return supporting citations, and record protected telemetry.',
 'Citations, encryption, and Guardrails do not replace tenant authorization.',
 'Where should tenant filtering occur?','At retrieval before evidence enters the prompt. Validate identity and enforce access at the source and tool boundary as well.','knowledge-bases guardrails vpc','secure-rag')
L('End-to-end action agent case','2.1.3 2.1.5 2.1.6 5.1.7','A refund agent must inspect policy and order state before it proposes a controlled transaction.',
 'Retrieve the current refund policy and authorized order state. || Validate amount, customer scope, and policy conditions. || Obtain required approval for the exact refund. || Execute once with an idempotency key and verify operation status.',
 'A fluent explanation of the refund does not authorize the transaction.',
 'Which test exposes duplicate refunds after timeouts?','Replay the same approved action and idempotency key under timeout and retry conditions. Assert one side effect.','agents genai-lens','approval')
L('Final decision rules','','Use these rules as recall prompts after the full course.',
 'Fresh facts and citations require a controlled evidence path. || Tool actions require server-side permission, validation, and retry safety. || Optimization must preserve task quality and hard constraints. || Release decisions require versioned tests and a rollback path.',
 'Treat repository rules such as always choose managed or always choose RAG as heuristics that require context.',
 'How should you review a wrong answer?','Record the missed constraint, the correct service boundary, why each distractor fails, and one new test case.')
pathlib.Path('course/core.json').write_text(json.dumps(slides,indent=2,ensure_ascii=False))
print('Core slides:',len(slides))

import json,pathlib
slides=[]
def L(title,skills,lead,points,trap,question,answer,sources,diagram=''):
 slides.append(dict(id='advanced-'+str(len(slides)+1).zfill(3),title=title,skills=skills.split(),domain=int(skills[0]),lead=lead,points=points.split(' || '),trap=trap,question=question,answer=answer,sources=sources.split(),diagram=diagram))
L('Prompt technique comparison','1.6.1 1.6.5','Select the technique from the defect you need to correct.',
 'Zero-shot supplies a task without task examples. || Few-shot supplies representative examples of input and desired output. || Chain-of-thought patterns request intermediate reasoning or decomposition. || ReAct alternates reasoning, tool action, and observations.',
 'A reasoning explanation is not evidence of truth. Use verified sources, tool results, and answer checks.',
 'The model understands a task but repeatedly uses the wrong field names. Which low-effort change should you test?','Use a precise output schema where supported, plus consistent examples and validation. Fine-tuning is not the first required step.','prompt-management converse-api')
L('Prompt injection and tool output','3.1.5 2.1.6','Indirect injection reaches an agent through a document or a tool result.',
 'Treat retrieved instructions as data, even when the source appears trusted. || Restrict tool destinations, data scope, and permitted side effects. || Avoid unnecessary secrets in model context. || Test attacks that ask the model to alter filters or expose prior messages.',
 'A tool result can be accurate data and still contain an injected instruction.',
 'A search result asks the agent to remove a tenant filter for better accuracy. What must happen?','Reject the filter change at the server boundary. The model cannot expand its own authorization.','guardrails genai-lens','tool')
L('Inference permission matrix','2.4.1 3.2.1','API method names and IAM action names are not always identical.',
 'Converse requires the relevant bedrock:InvokeModel permission. || ConverseStream requires the relevant bedrock:InvokeModelWithResponseStream permission. || InvokeModel uses bedrock:InvokeModel for supported resources. || Retrieval and agent APIs use their own relevant actions and resource scope.',
 'Do not invent bedrock:Converse as a substitute IAM action for the Converse runtime API.',
 'A role can use Converse but cannot stream. Which action should you inspect?','Inspect bedrock:InvokeModelWithResponseStream, resource scope, and any applicable deny.','converse-api converse-stream-api iam')
L('Converse with a prompt version','1.6.3 2.4.1','A Prompt Management resource can define parts of the model request.',
 'A modelId can reference a supported prompt version ARN. || Use promptVariables for values that the prompt template requires. || Respect request field restrictions when a prompt resource defines configuration. || Keep prompt version and variable contract in the release record.',
 'Do not assume that system, toolConfig, inferenceConfig, and additionalModelRequestFields can override a prompt resource request.',
 'A call works with a model ID but fails with a prompt ARN. What should you inspect?','Inspect prompt variables and the API restrictions on fields defined by Prompt Management.','converse-api prompt-management')
L('Structured output and business validity','1.3.3 3.1.3','A supported structured output feature constrains shape. The application still checks meaning.',
 'Confirm the chosen model and API support the required JSON Schema feature. || Use supported outputConfig or tool schema settings as appropriate. || Validate required fields, types, bounds, and allowed values. || Check factual support, permissions, and business rules separately.',
 'Do not claim that every Converse model supports strict structured output. A valid object can still contain fabricated values.',
 'A valid JSON order contains a nonexistent item. Which validation catches it?','A business lookup against the authorized system of record, after schema validation.','structured-output converse-api')
L('Bedrock agent lifecycle','2.1.1 2.1.6','Separate the editable agent configuration from the version that production invokes.',
 'Define instructions, action groups, knowledge sources, and execution permissions. || Prepare and test the draft agent through the supported lifecycle. || Use versions and aliases for controlled production routing. || Review tool and source changes with task and safety tests.',
 'A changed draft does not imply that every existing production alias now uses that configuration.',
 'A new action group does not appear in production behavior. What should you inspect?','Inspect the agent preparation state, version, alias target, action group configuration, and invocation identifiers.','agents-current agents')
L('Bedrock action groups and return control','2.1.5 2.1.6','An action group connects a model decision to a defined external capability.',
 'Describe operations through a supported API schema or function definition. || Use Lambda execution where the integration requires it. || Use return control when the application must handle the proposed action. || Keep approvals and idempotency at the actual side-effect boundary.',
 'Return control gives application control over execution. It is not automatic human approval.',
 'A transaction needs custom approval before execution. Which pattern should you assess?','Use an application-controlled execution path, with approval bound to the exact validated operation.','agents-current agents','approval')
L('Knowledge Bases metadata and sync','1.4.2 1.4.5','A managed ingestion path still needs correct metadata and observable update behavior.',
 'Supply supported metadata in the data source format. || Preserve document identifiers, versions, effective dates, and access scope. || Run or trigger ingestion after source changes under the supported connector behavior. || Inspect ingestion statistics and deletion handling before answers use the update.',
 'A scheduled sync cannot promise instant freshness. Define the acceptable source-to-index delay.',
 'A policy needs immediate withdrawal. Which derived data requires review?','Review vectors, source caches, answer caches, conversation references, and retained logs under the applicable policy.','kb-sync retrieval')
L('Search and assistant service boundaries','1.4.1 2.5.3','A search service, an assistant, and a custom RAG application have different control surfaces.',
 'Kendra supplies enterprise search with supported connectors and access features. || Q Business supplies a managed enterprise assistant over supported business data. || Bedrock Knowledge Bases supplies retrieval and generation integration for custom applications. || A custom vector path gives control over indexing, retrieval, and application assembly.',
 'Choose from required customization, connectors, permissions, and operational effort. Do not select from product names alone.',
 'The team needs a custom model workflow with its own tool actions. Is a managed enterprise assistant always sufficient?','No. Compare its supported integration surface with the required custom workflow and control boundaries.','knowledge-bases genai-lens')
L('Graph retrieval and relational retrieval','1.4.1 1.5.4','Some questions depend on relationships or exact structured values instead of semantic proximity alone.',
 'Graph retrieval can follow entity relationships and multi-hop context. || Relational queries can supply exact values from a system of record. || Vector retrieval can supply semantic document context. || Combine results only after access checks and explicit source handling.',
 'Do not generate and execute unrestricted SQL or graph queries under a broad service role.',
 'A question asks for current account balance. Should a static vector document provide the final value?','Use an authorized system-of-record query for the current value. Use document retrieval for explanatory policy if needed.','knowledge-bases genai-lens','tool')
L('API Gateway response streaming','2.4.2 2.5.1','Current AWS documentation supports response streaming for compatible REST API proxy integrations.',
 'Set the supported response transfer mode to STREAM where the design requires it. || Check HTTP_PROXY or AWS_PROXY integration requirements. || Validate endpoint type, backend behavior, timeout, and client protocol. || Measure time to first byte through the complete route.',
 'Do not reuse an old rule that all API Gateway responses buffer. Do not assume every HTTP or WebSocket integration supports the same behavior.',
 'A REST API proxy still buffers an entire model response. What should you verify?','Verify the response transfer mode and backend stream support. Then test proxies and client parsing.','response-stream converse-stream-api','stream')
L('SageMaker inference pattern comparison','2.2.1 2.2.2','Choose an endpoint or batch pattern from latency, payload, runtime, and hardware requirements.',
 'Real-time endpoints fit interactive requests with suitable provisioned resources. || Asynchronous inference fits supported queued requests and delayed results. || Batch Transform fits offline bulk processing. || Serverless inference fits supported intermittent workloads and has distinct resource limits.',
 'Serverless inference does not imply GPU support for every large model. Verify runtime and model compatibility.',
 'A large custom model needs GPU control and predictable interactive capacity. What should the team assess?','Assess suitable real-time hosting resources and serving containers, then benchmark concurrency, memory, and latency.','sagemaker-deploy')
L('Provisioned capacity and overflow','2.2.1 4.1.3','A mixed capacity design requires explicit routing and capacity assumptions.',
 'Confirm that the chosen model supports the required provisioned offering. || Invoke the correct provisioned resource identifier. || Measure baseline token work and the relevant commitment terms. || Implement and test any separate on-demand overflow path.',
 'Do not assume automatic spillover from provisioned capacity to a base on-demand model.',
 'Provisioned capacity saturates during a spike. What does a safe overflow design need?','A tested route to compatible permitted capacity, bounded retries, preserved quality, and no violation of residency rules.','bedrock-provisioned','resilience')
L('Batch input, output, and failure handling','2.4.1 4.2.3','Batch inference is a job workflow with model-specific support and data contracts.',
 'Prepare the required supported records and unique identifiers. || Place inputs and outputs in approved S3 locations. || Grant the service role the required data and KMS access. || Track job state and inspect failed records before a selective retry.',
 'Batch inference is not a universal replacement for interactive or service-native async inference.',
 'A batch job partially fails. Should the entire business operation run again without inspection?','No. Inspect record-level results and retry safely with stable identifiers.','batch')
L('Cost and quota are separate','4.1.3 4.2.3','A lower bill does not prove that a request avoids every quota.',
 'Inspect the documented quota dimensions for the selected model and mode. || Measure request rate, input token rate, output token work, and concurrency as applicable. || Account for retries and parallel model calls. || Use queue limits and admission control before overload spreads.',
 'A cache hit can affect quota accounting differently by model. Use current model-specific documentation.',
 'Prompt compression lowers cost but throttling remains. What should you inspect?','Inspect the actual quota dimension, concurrency, request rate, output demand, and retry amplification.','prompt-cache bedrock-errors')
L('Retrieval metrics with a small example','5.1.6','Metric definitions separate evidence coverage from evidence noise.',
 'Recall@k is relevant returned passages divided by all relevant passages. || Precision@k is relevant returned passages divided by returned passages. || Reciprocal rank is one divided by the rank of the first relevant result. || A worked numerical example is not in source.',
 'A metric depends on the relevance labels and evaluation unit. Record those definitions.',
 'If a reranker moves the first relevant passage earlier, what improves?','Reciprocal rank improves. Recall may remain unchanged if the same relevant passages remain in the returned set.','evaluation retrieval')
L('Bedrock RAG metric names','5.1.5 5.1.6','Know what each built-in measure checks before you select it.',
 'Correctness assesses answer accuracy. Completeness assesses coverage of the question. || Faithfulness assesses support relative to retrieved text. || Citation precision assesses whether cited passages support their use. || Citation coverage assesses whether citations cover the response evidence needs.',
 'Some metrics require ground-truth data. Check the dataset contract and supported job type.',
 'An answer contains accurate facts but omits support for half its claims. Which evidence measure matters?','Assess citation coverage and citation precision, plus correctness and faithfulness under the defined rubric.','evaluation-metrics')
L('Automated Reasoning runtime findings','3.1.3 3.4.3','Automated Reasoning checks return findings. The application decides the next action.',
 'VALID concerns only the policy scope captured by its variables. || INVALID indicates a detected conflict with the modeled policy. || Ambiguous or complex cases can require clarification or review. || Configure the supported content qualifiers and verify actual policy evaluation.',
 'Detect mode does not automatically block the response. Missing qualifiers can cause no evaluation in some invocation paths.',
 'A policy check returns an invalid finding. What should the application do?','Apply its defined response policy, such as rewrite, clarification, refusal, or human review. Log the decision under data controls.','reasoning-integration guardrails-reasoning')
L('Data poisoning and evidence integrity','3.1.5 1.3.1','A retrieved passage can be incorrect because the source or ingestion path was compromised.',
 'Control who can write and approve trusted source content. || Track version, origin, and access metadata through ingestion. || Detect unexpected source changes and quality regressions. || Quarantine suspect content and invalidate affected derived data.',
 'A grounded response can faithfully repeat poisoned evidence. A grounding score alone cannot establish source truth.',
 'After a source update, many answers repeat the same false rule. Which layer needs investigation?','Inspect source integrity, write permissions, approval history, ingestion changes, and cached results before prompt tuning.','genai-lens knowledge-bases')
L('Exam-day time allocation','5.1.4','Use a time plan that leaves room for questions with uncertain constraints.',
 'AWS lists 75 questions in 180 minutes. || The simple average is 2.4 minutes per question. || Answer all questions because unanswered items count as incorrect. || For multiple response, select every required correct option.',
 'A time average is a planning aid. It is not a required pace for each question or a scoring formula.',
 'Why should you avoid a long stall on one uncertain question?','It can consume time needed for several answerable questions. Use the exam interface review tools under its current rules.','exam certification')
pathlib.Path('course/advanced.json').write_text(json.dumps(slides,indent=2));print('Advanced slides:',len(slides))

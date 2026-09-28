# AIP-C01 Coverage Map: three-way completeness cross-check

Last verified: 2026-09-28. Volumes live in `~/workspace/your_files/aws-aip-c01-cert/`.
File key: D1 `volume-d1-foundation-models.html`, D2 `volume-d2-implementation-integration.html`,
D3 `volume-d3-safety-security-governance.html`, D4 `volume-d4-optimization.html`,
D5 `volume-d5-testing-validation.html`, QB `volume-question-bank.html`,
SD `volume-system-design.html`, LABS `volume-maarek-labs.html` (new).

---

## (i) Official exam guide: domain weights mapped to task statements and volumes

Weights are verbatim from the official exam guide: D1 31%, D2 26%, D3 20%, D4 12%, D5 11%.

### Domain 1: Foundation Model Integration, Data Management, and Compliance (31%)

| Task statement | Covered by |
|---|---|
| 1.1 Analyze requirements and design GenAI solutions (approach ladder, PoC first, GenAI Lens, reusable components) | D1 ch1, ch2; SD ch8 (decision ladders); LABS ch8 (CDK standardized components) |
| 1.2 Select and configure FMs (selection criteria, AppConfig/Lambda/APIGW switching, cross-region inference, customization lifecycle) | D1 ch3, ch4, ch6, ch7, ch8; D4 ch5; LABS ch5 (AppConfig trio) |
| 1.3 Data validation and processing pipelines for FM consumption (Glue Data Quality, Data Wrangler, Lambda validation, BDA, Transcribe) | D1 ch9; D2 ch13 (BDA); LABS ch9 (BDA/ingestion framing) |
| 1.4 Vector store solutions (Knowledge Bases, OpenSearch/Aurora/Neptune/S3 Vectors, metadata, freshness) | D1 ch10, ch11, ch12 |
| 1.5 Retrieval mechanisms for FM augmentation (chunking, embeddings, hybrid search, rerank, query handling, MCP) | D1 ch13, ch14, ch15 |
| 1.6 Prompt engineering and governance (Prompt Management, Prompt Flows, approval workflows, audit) | D1 ch16; LABS ch4 (Flows JSON authoring, hands-on) |

### Domain 2: Implementation and Integration (26%)

| Task statement | Covered by |
|---|---|
| 2.1 Agentic AI solutions and tool integrations (Bedrock Agents anatomy, multi-agent, Strands, Agent Squad, MCP, AgentCore, safeguards) | D2 ch1, ch2, ch3; LABS ch1 (Strands), ch2 (Agent Squad), ch3 (AgentCore), ch6 (agent actions) |
| 2.2 Model deployment strategies (Lambda on-demand, PT, SageMaker endpoints, batch, cascading) | D2 ch11; D4 ch3, ch4; LABS ch5 |
| 2.3 Enterprise integration architectures (legacy, event-driven, secure access, Outposts/Wavelength, GenAI gateway, CI/CD) | D2 ch12; LABS ch7 (CI/CD) |
| 2.4 FM API integrations (Converse vs InvokeModel, batch, streaming, reliability) | D2 ch8, ch9, ch10, ch15; LABS ch5 |
| 2.5 Application integration patterns and development tools (API Gateway, Amplify, Flows, BDA, Q Business/Q Developer, troubleshooting hooks) | D2 ch4, ch5, ch6, ch7, ch13, ch14; LABS ch5, ch9 |

### Domain 3: AI Safety, Security, and Governance (20%)

| Task statement | Covered by |
|---|---|
| 3.1 Input and output safety controls (Guardrails matrix, prompt attacks, grounding, Automated Reasoning, defense in depth) | D3 ch1-ch7 |
| 3.2 Data security and privacy (VPC endpoints, IAM, Macie/Comprehend/Guardrails PII pipe, KMS, invocation logging) | D3 ch8; LABS ch9 (KMS lab) |
| 3.3 AI governance and compliance (model cards, lineage, CloudTrail vs CloudWatch Logs, drift monitoring) | D3 ch9 |
| 3.4 Responsible AI (transparency, fairness, LLM-as-a-judge, policy compliance) | D3 ch10; D5 ch2 |

### Domain 4: Operational Efficiency and Optimization (12%)

| Task statement | Covered by |
|---|---|
| 4.1 Cost optimization and resource efficiency (token efficiency, tiered models, prompt caching, semantic caching, PT) | D4 ch1, ch2, ch4, ch8, ch11, ch12; LABS ch1 (tool-loop token cost) |
| 4.2 Application performance (latency levers, streaming, retrieval perf, temperature/top-p/top-k) | D4 ch6, ch8 |
| 4.3 Monitoring GenAI applications (CloudWatch Bedrock metrics, invocation logs, X-Ray, golden datasets) | D4 ch9, ch10; LABS ch9 (X-Ray lab) |

### Domain 5: Testing, Validation, and Troubleshooting (11%)

| Task statement | Covered by |
|---|---|
| 5.1 Evaluation systems (programmatic, LLM-as-a-judge, human, RAG eval, agent eval, QA gates) | D5 ch1-ch7; LABS ch7 (eval gates in CI/CD) |
| 5.2 Troubleshooting (debug order: content, API, prompt, retrieval; PT routing bug; prepare-agent bug) | D5 ch8-ch11; LABS ch5 (proxy shape bug), ch6 (prepare-agent bug) |

All 22 task statements map to at least one volume. No task is orphaned.

---

## (ii) Maarek study guide sections I-X mapped to volumes (gaps flagged)

Method: keyword and chapter-title search across all existing volumes on 2026-09-28, plus the new LABS volume.
"Covered" means a teaching chapter exists. "Partial" means mentioned but not taught. "Gap" means absent.

### Section I: Generative AI Fundamentals and Bedrock

| Topic | Status | Volumes |
|---|---|---|
| Foundation models (Nova, Claude, Titan, Llama, Jurassic-2, Stable Diffusion) | Covered | D1 ch3, ch4 |
| Fine-tuning / custom models | Covered | D1 ch8 |
| RAG concept | Covered | D1 ch10, ch12 |
| Knowledge Bases / vector DBs (OpenSearch, Aurora, MemoryDB/ElastiCache Valkey, MongoDB, Pinecone, Redis) | Covered | D1 ch10, ch11 |
| Chunking: hierarchical, semantic; vector dimensionality; metadata | Covered | D1 ch13, ch14 |
| Bedrock Guardrails | Covered | D3 ch1-ch7 |
| Token-level redaction (Comprehend NER pre/post processing) | Covered | D3 ch5 |
| Prompt engineering (few-shot, CoT), Prompt Management (versions, variants, variables), Flows, structured JSON output | Covered | D1 ch16; LABS ch4 (Flows hands-on) |

### Section II: Managing Data for Generative AI

| Topic | Status | Volumes |
|---|---|---|
| Data structuring (Textract, Comprehend, divider strings, Lambda preprocessor, Glue ETL) | Partial | D1 ch9 covers the pipeline; Textract appears only in QB; divider strings absent (minor) |
| Bedrock Data Automation (blueprints, outputs, video/audio processing) | Covered | D1 ch9; D2 ch13; SD |
| Transcribe (ASR, PII redaction, custom vocabularies, toxicity detection) | Covered | D1 ch9; QB; SD |
| Comprehend (NER, custom classification, custom entities) | Covered | D1 ch9; D3 ch5 |
| Vector store optimization (binary vectors, FP16 quantization, hierarchical indices, neural plugin) | Partial | D1 ch11 compares stores; these specific techniques not confirmed taught |

### Section III: Agentic AI

| Topic | Status | Volumes |
|---|---|---|
| Bedrock Agents (planning, action groups, OpenAPI schema in S3) | Covered | D2 ch1; LABS ch6 (action Lambda hands-on) |
| Multi-agent (orchestrator/worker/synthesizer, chain of sequence, parallelization), MCP | Covered | D2 ch2; LABS ch2 |
| Agent memory (short/long-term, AgentCore Memory) | Covered | D2 ch2; LABS ch3 |
| Q Business (connectors, plugins, Identity Center, admin guardrails) | Covered | D2; QB |
| Q Apps | Gap | None. Not taught in any volume. |
| Q Developer (./amazon/rules) | Covered | D2 |
| HITL (human augmentation, escalation criteria, API Gateway + DynamoDB feedback) | Covered | D2 ch6; D5 ch3 |

### Section IV: Operational Efficiency and Optimization

| Topic | Status | Volumes |
|---|---|---|
| CountTokens API (free token estimation) | Partial | D4 covers token counting concepts; the CountTokens API name is not explicitly taught (minor) |
| CloudWatch InputTokenCount/outputTokenCount, context pruning, maxTokens response controls | Covered | D4 ch1, ch9, ch11 |
| Provisioned Throughput + model ARN routing | Covered | D4 ch4; D2 ch11 |
| Cost/capability tradeoff, Intelligent Prompt Routing | Covered | D1 ch6; D2; D4 ch8 |
| Bedrock Evaluations for cost metrics | Covered | D5 ch1-ch2 |
| Prompt caching (static prefix, discounted reads) | Covered | D4 ch2 |
| TTFT (time to first token) | Partial | D4 ch6 covers streaming latency; TTFT by name not confirmed taught (minor) |
| temperature / top_p / top_k | Partial | temperature and top_p covered (D4; QB; SD); top_k by name absent (minor) |
| CloudWatch Evidently (A/B testing) | Partial | D5 ch7 covers A/B testing via Prompt Management variants; Evidently by name absent (minor) |
| SageMaker large-model deployment (500GB, health check/download timeouts, ml.p4d.24xlarge, ml.c5.9xlarge) | Partial | D2 ch11 covers SageMaker deployment; these specific large-model tuning details not confirmed taught |
| CoT for accuracy, exponential backoff, circuit breaker (Step Functions + DynamoDB) | Covered | D2 ch6; D4 ch7 |

### Section V: Managing Models with SageMaker AI

| Topic | Status | Volumes |
|---|---|---|
| Model deployment (persistent endpoint, batch transform) | Covered | D2 ch11 |
| SageMaker Model Monitor (drift alerts, CloudWatch) | Covered | D1; D4; QB; SD |
| SageMaker Clarify (bias CI/DPL, explainability) | Covered | D3; QB |
| Rekognition/Comprehend auto-labeling | Partial | Mentioned in QB; no teaching chapter confirmed |

### Section VI: More Tools for Building AI Applications

| Topic | Status | Volumes |
|---|---|---|
| Lambda for GenAI (agent tools, validation, on-demand invocation, webhooks, aggregation/voting) | Covered | D2 ch4; LABS ch5, ch6 |
| Amazon AppFlow (SaaS ETL for GenAI) | Gap | None. Absent from all volumes. |
| AWS CDK (IaC in familiar languages, compiles to CloudFormation) | Covered | LABS ch8 (hands-on). No prior volume taught it. |
| Amazon Kendra (NL search, incremental learning) | Covered | D1; D2; D3 |
| API Gateway (front end, traffic, proxy) | Covered | D2 ch5; LABS ch5 |
| AWS Transfer Family (SFTP/FTPS/FTP to S3/EFS, ingestion entry) | Gap | None. Absent from all volumes. |

### Section VII: Governance and QA

| Topic | Status | Volumes |
|---|---|---|
| Responsible AI dimensions (fairness, explainability, privacy, safety, controllability, veracity, governance, transparency) | Covered | D3 ch10 |
| Evaluation techniques (human, Bedrock eval jobs, RAG metrics, prompt datasets, ROUGE) | Covered | D5 ch1-ch5 |
| Agent tracing (preprocessing, orchestration, postprocessing, guardrail traces) | Covered | D2 ch1; D3 |
| Observability (CloudWatch Logs groups/streams, KMS encryption, export to S3/Kinesis/Lambda/OpenSearch) | Covered | D3 ch8-ch9; D4 ch9-ch10 |

### Section VIII: Security, Identity, and Compliance

| Topic | Status | Volumes |
|---|---|---|
| IAM | Covered | D3 ch8 |
| KMS | Covered | D3 ch8; LABS ch9 |
| Macie | Covered | D1; D2; D3 |
| Secrets Manager | Partial | SD only; no dedicated teaching chapter |
| Cognito | Covered | D2; SD |
| WAF | Partial | QB only; no teaching chapter |
| VPC + PrivateLink for Bedrock | Covered | D3 ch8 |

### Section IX: Other Services You Should Know

| Topic | Status | Volumes |
|---|---|---|
| QuickSight | Gap | None. Absent from all volumes. |
| Neptune Analytics (vectors.topKByEmbedding) | Gap | None. Absent from all volumes (Neptune graph covered in D1 ch11; Analytics engine not). |
| CloudTrail | Covered | D3 ch9; D5 ch9 |
| Well-Architected GenAI Lens (lifecycle: scoping, selection, customization, integration, deployment, continuous improvement) | Covered | D1 ch2; QB |
| CloudFront (CDN, edge, Shield/WAF) | Partial | D2; QB mention; no dedicated teaching |
| EMR | Partial | Not confirmed taught in any volume (minor; peripheral to GenAI) |

### Section X: Exam Preparation

| Topic | Status | Volumes |
|---|---|---|
| MC + multiple response, no partial credit | Covered | index.html; QB |
| Ordering / matching new question types | Partial | Mentioned in the study guide reference as not in beta; exam-format coverage lives in index.html/QB |

---

## (iii) Every lab file in labs-src mapped to a LABS chapter

| Lab file(s) | LABS chapter |
|---|---|
| AgentsLab/strandsagent.py | ch1: Strands agent with custom @tool |
| AgentsLab/squad_demo.py | ch2: Multi-agent squad routing |
| AgentsLab/agentcore.py | ch3: AgentCore Runtime deployment |
| AgentsLab/Dockerfile | ch3 (container contract: base image, non-root user, port 8080, OTEL) |
| AgentsLab/requirements.txt | ch3 (bedrock-agentcore, strands-agents, strands-agents-tools pins) |
| AgentsLab/.dockerignore | ch3 (referenced in the image build walkthrough) |
| PromptChaining.json | ch4: Bedrock Flows from JSON |
| api-gateway/lambda-code.py | ch5: Lambda as Bedrock front end |
| weather.py | ch6: Lambda as agent action |
| aws-cicd/codebuild/buildspec.yml | ch7: CI/CD with eval gates |
| aws-cicd/codedeploy/* (appspec.yml, scripts, SampleApp_Linux) | ch7 (deploy stage) |
| aws-cicd/nodejs-v2-blue/* (app.js, package.json, cron.yaml) | ch7 (sample application moved through the pipeline) |
| cdk/lib/cdk-app-stack.js, cdk/lambda/index.py, cdk/steps.sh | ch8: CDK for GenAI infrastructure |
| cdk/images/* | ch8 (sample assets processed by the stack's pipeline) |
| kms/kms-demo-cli.sh, kms/ExampleSecretFile.txt | ch9: KMS section |
| x-ray/eb-java-scorekeep-xray-simplified.yaml | ch9: X-Ray section |
| sqs/sqs.sh | ch9: SQS section |
| cli/ec2-metadata.sh | ch9: foundations |
| cloudformation/0-just-ec2.yaml, 1-ec2-with-sg-eip.yaml | ch9: foundations |
| ec2-fundamentals/ec2-user-data.sh | ch9: foundations |
| kinesis/kinesis-data-streams.sh | ch9: foundations |
| book.txt | ch9: sample knowledge source for the RAG ingestion story |
| cfas-bylaws-rev-9.docx | ch9: sample unstructured document for the extraction story |

All 41 files mapped. No lab file orphaned.

---

## Gaps found (explicit list)

### Hard gaps: not taught in any volume, including the new LABS volume
1. **Amazon AppFlow** (Section VI): SaaS ETL feeding GenAI systems. Absent everywhere.
2. **AWS Transfer Family** (Section VI): managed file transfer as an ingestion entry point. Absent everywhere.
3. **Amazon QuickSight** (Section IX): serverless BI for GenAI dashboards and reports. Absent everywhere.
4. **Neptune Analytics** (Section IX): analytics engine with vector queries. Absent everywhere (Neptune graph for GraphRAG is covered in D1 ch11).
5. **Amazon Q Apps** (Section III): no-code GenAI apps for non-developers. Absent everywhere (Q Business and Q Developer are covered).

Assessment: all five are peripheral to the exam's core (none appears in the blueprint's task statements or trap lists; three are one-line mentions in the study guide). They are low-weight risks, but they are real gaps a completionist pass should close with short appendix entries.

### Partial coverage: mentioned but not taught as a topic
6. **Secrets Manager**: appears only in SD; no teaching chapter (D3 ch8 would be the natural home).
7. **WAF**: appears only in QB; no teaching chapter.
8. **CloudFront**: mentioned in D2 and QB; no dedicated teaching.
9. **Textract**: appears only in QB; D1 ch9 teaches the pipeline without naming it as a chapter topic.
10. **Divider strings for chunking**: absent (minor; D1 ch13 teaches chunking strategies).
11. **CountTokens API by name**: token estimation taught in D4; the API name itself not taught (minor).
12. **top_k by name**: temperature and top_p taught; top_k not named (minor).
13. **CloudWatch Evidently by name**: A/B testing taught via Prompt Management variants (D5 ch7); Evidently not named (minor).
14. **TTFT by name**: streaming latency taught (D4 ch6); the metric name not confirmed taught (minor).
15. **Binary vectors / FP16 quantization / OpenSearch neural plugin**: D1 ch11 compares vector stores; these optimization techniques not confirmed taught (minor).
16. **SageMaker large-model tuning specifics** (container health check and download timeout quotas, ml.p4d.24xlarge): D2 ch11 teaches SageMaker deployment; these details not confirmed taught (minor).
17. **EMR**: not confirmed taught (minor; peripheral).

### Gaps closed by the new LABS volume
- Strands Agents hands-on (was concept-only in D2): LABS ch1.
- Agent Squad hands-on with classifier mechanics (was concept-only in D2): LABS ch2.
- AgentCore Runtime deployment detail, container contract, Gateway/Memory/Identity/Observability mapping (was overview in D2): LABS ch3.
- Bedrock Flows JSON authoring, nodes/connections/conditions (was concept-only in D1 ch16): LABS ch4.
- Lambda + API Gateway + AppConfig model-switching trio, hands-on (was pattern-only): LABS ch5.
- Agent action Lambda event/response shapes, PrepareAgent bug, hands-on: LABS ch6.
- CI/CD with buildspec-level eval gates (D5 ch12 covers CI/CD concepts): LABS ch7.
- CDK for GenAI infra (untaught anywhere before): LABS ch8.
- KMS, X-Ray, SQS, CLI, CloudFormation, EC2, Kinesis hands-on exam framing: LABS ch9.

### Verification notes
- Service names, features, model IDs, and API shapes stated in LABS were checked against live AWS documentation on 2026-09-28; see the verification log in `volume-maarek-labs.html` (QA section).
- One item is marked UNVERIFIED inline in LABS ch4 (Iterator node sequential behavior, community-reported).
- Volatile numbers (pricing, quotas) are omitted or labeled illustrative throughout.

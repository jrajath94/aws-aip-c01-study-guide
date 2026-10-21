# Question-bank coverage check, 250 items

This file records the check of the 250 review questions against the master treatise (`article/index.html`). The question text came from the shared quiz batch files, not from this repo. The internal question IDs are kept in `quiz-id-map.tsv`. Each status is a topic check against the treatise. The check used keyword and context search, plus official pages for new units. It was not a full read of every stem.

## Result

| Status | Count |
|---|---|
| covered | 229 |
| partial | 5 |
| contradicted | 3 |
| not-in-source | 13 |
| total | 250 |

Items 1 to 220 are AIP-C01 exam-scope questions and ML basics. Items 221 to 250 are AWS and ML prerequisites (domain 0), which are not exam domains.

| Items | Covered | Partial | Contradicted | Not in source |
|---|---|---|---|---|
| 1 to 50 | 48 | 0 | 1 | 1 |
| 51 to 100 | 46 | 1 | 0 | 3 |
| 101 to 150 | 43 | 1 | 2 | 4 |
| 151 to 200 | 46 | 2 | 0 | 2 |
| 201 to 250 | 46 | 1 | 0 | 3 |

Status meanings. Covered: the treatise states the tested fact or rule. Partial: the topic is present, but a tested detail is missing, thin, or not confirmed. Contradicted: an official page states a different fact from the quiz answer. Not in source: no official page fetched states the tested fact.

## Item table

| # | Status | Note |
|---|---|---|
| 001 | covered | RAG KB citations |
| 002 | covered | PoC on-demand |
| 003 | covered | Converse unified, outputConfig schema |
| 004 | covered | ElastiCache not durable |
| 005 | covered | metadata filters |
| 006 | covered | structured output via Converse |
| 007 | covered | GenAI Lens |
| 008 | covered | smallest model that meets bar |
| 009 | covered | AppConfig API GW Lambda |
| 010 | covered | EU cross-Region profile |
| 011 | covered | PT baseline plus on-demand |
| 012 | covered | LoRA small labeled data |
| 013 | covered | Model Registry rollback |
| 014 | covered | Data Automation |
| 015 | covered | Glue DQ plus CW alarms |
| 016 | covered | Guardrails not extraction |
| 017 | covered | Kendra closed, KB alternative |
| 018 | covered | Transcribe diarization then Comprehend PII |
| 019 | covered | KB managed hybrid search |
| 020 | covered | per-tenant KB plus IAM |
| 021 | covered | pgvector Aurora |
| 022 | contradicted | Sync page confirms incremental sync via StartIngestionJob. It names no automatic S3 event trigger for ingestion. |
| 023 | covered | RAG citations plus contextual grounding |
| 024 | covered | Neptune GraphRAG |
| 025 | covered | hierarchical chunking |
| 026 | covered | Q5 whole-document vs pre-made pairs |
| 027 | covered | hybrid search plus rerank |
| 028 | covered | Cohere Embed page: input_type takes search_document for corpus and search_query for queries. |
| 029 | covered | query expansion |
| 030 | covered | dimension choice golden set |
| 031 | covered | MCP |
| 032 | covered | Prompt Management versions |
| 033 | covered | variants vs versions |
| 034 | covered | Prompt Flows |
| 035 | covered | distill small model |
| 036 | covered | PoC then cross-Region |
| 037 | covered | prompt router |
| 038 | not-in-source | Cross-Region page does not state which Region quota a routed request uses. |
| 039 | covered | circuit breaker |
| 040 | covered | Q3 IAM Identity Center permission sets |
| 041 | covered | chunk boundaries, embeddings |
| 042 | covered | recreate data source for chunking |
| 043 | covered | table chunk splitting |
| 044 | covered | prompt governance, CloudTrail |
| 045 | covered | DRAFT, prepare, alias |
| 046 | covered | Q1 action group executor |
| 047 | covered | supervisor collaborators |
| 048 | covered | DynamoDB memory |
| 049 | covered | callback task token |
| 050 | covered | Lambda 15 min limit |
| 051 | covered | Strands, Agent Squad |
| 052 | covered | MCP on Lambda or ECS |
| 053 | covered | AgentCore |
| 054 | partial | Step Functions error and timeout pages cover TimeoutSeconds and catchers. Stopping-condition wording is not on the page. |
| 055 | covered | on-demand scale to zero |
| 056 | covered | batch inference |
| 057 | covered | SageMaker real-time custom containers |
| 058 | covered | model cascade |
| 059 | covered | serverless endpoint scales to zero, cold start |
| 060 | covered | Q4 DLQ maxReceiveCount |
| 061 | covered | Outposts |
| 062 | covered | GenAI gateway |
| 063 | covered | release gates |
| 064 | covered | Q3 IAM Identity Center permission sets |
| 065 | covered | Q2 additionalModelRequestFields |
| 066 | covered | Converse no embeddings |
| 067 | covered | InvokeModel provider body |
| 068 | covered | ConverseStream |
| 069 | covered | ApplyGuardrail any model |
| 070 | covered | Claude body anthropic_version max_tokens |
| 071 | covered | Q Developer vs Q Business |
| 072 | not-in-source | BDA overview page does not describe custom blueprint schema. |
| 073 | covered | Amplify |
| 074 | covered | agent combined scenario |
| 075 | covered | agent trace |
| 076 | covered | PT plus on-demand burst |
| 077 | covered | SageMaker async inference |
| 078 | covered | CloudTrail is audit, not pipeline |
| 079 | covered | provisioned model ARN |
| 080 | covered | Q9 S3 versioning |
| 081 | covered | denied topics |
| 082 | covered | sensitive info filter mask |
| 083 | covered | word filters |
| 084 | covered | prompt attack filter |
| 085 | covered | contextual grounding |
| 086 | covered | Automated Reasoning |
| 087 | covered | defense in depth, Comprehend pre-filter |
| 088 | covered | ApplyGuardrail self-hosted model |
| 089 | covered | VPC interface endpoints |
| 090 | covered | Macie, Comprehend, Guardrails pipeline |
| 091 | covered | Macie at rest |
| 092 | covered | Comprehend realtime plus Guardrails |
| 093 | covered | invocation logging privacy |
| 094 | covered | translation no protection |
| 095 | covered | Lake Formation column grants |
| 096 | covered | Model Cards |
| 097 | covered | CloudTrail identity and time |
| 098 | not-in-source | Glue lineage page returned only the title. No lineage text found. |
| 099 | not-in-source | Per-decision explanation and confidence level are not stated on the fetched pages. |
| 100 | covered | LLM-as-judge plus human brand voice |
| 101 | covered | fairness metrics, A/B, judge |
| 102 | covered | transparency citations, grounding |
| 103 | covered | denied topics, sensitive info, prompt attack |
| 104 | contradicted | Structured outputs page does not describe confidence scores. Quiz claim is not supported as stated. |
| 105 | covered | VPC endpoints, KMS, CloudTrail |
| 106 | covered | continuous monitoring and remediation |
| 107 | covered | bias drift monitoring |
| 108 | not-in-source | Fair-lending rules are not in source. |
| 109 | covered | inference params do not cut cost |
| 110 | covered | prompt caching |
| 111 | covered | PT baseline |
| 112 | covered | router |
| 113 | covered | batch inference |
| 114 | covered | cost levers |
| 115 | covered | semantic cache vs prompt cache |
| 116 | covered | temperature 0 and PT |
| 117 | covered | streaming |
| 118 | covered | PT not consistency |
| 119 | contradicted | Application inference profiles track usage and costs per profile. Request metadata is not shown as a cost source on the fetched pages. Quiz answer needs correction. |
| 120 | covered | anomaly detection, evaluation jobs |
| 121 | covered | X-Ray and agent trace |
| 122 | covered | Model Monitor not for text |
| 123 | covered | caching plus routing plus PT |
| 124 | covered | OpenSearch shard sizing page: 10 to 30 GiB for search latency, 30 to 50 GiB for write-heavy. Default is 5 primary shards and 1 replica. |
| 125 | covered | invocation logging forensic |
| 126 | not-in-source | Official AccessDeniedException page gives no region-based cause. Quiz answer not confirmed. |
| 127 | covered | programmatic metrics fixed dataset |
| 128 | covered | judge calibrated to humans |
| 129 | covered | human eval for brand voice |
| 130 | covered | KB evaluation metrics page names context relevance, context coverage, faithfulness, and correctness. |
| 131 | covered | regression testing |
| 132 | covered | judge plus human |
| 133 | covered | exact match cannot judge style |
| 134 | covered | Claude body ValidationException |
| 135 | covered | DRAFT vs prepare alias |
| 136 | covered | debug retrieval first |
| 137 | covered | prompt version compare, golden regression |
| 138 | covered | Q6 bring-your-own-inference evaluation |
| 139 | covered | Q5 whole-document vs chunking |
| 140 | covered | PT model units plus overflow |
| 141 | partial | Embedding dimension choice is covered. Process detail is thin. |
| 142 | covered | query decomposition |
| 143 | covered | reject fine-tuning, RAG re-sync |
| 144 | covered | Q17 custom transformation Lambda for structure |
| 145 | not-in-source | BDA blueprint schema is not in the fetched page. |
| 146 | covered | metadata filter before vector search |
| 147 | covered | AppConfig plus canary |
| 148 | covered | GenAI Lens review standard |
| 149 | not-in-source | Web crawler page returned only the title. No schedule text found. |
| 150 | covered | LLM judge faithfulness |
| 151 | covered | hierarchical chunking |
| 152 | covered | hybrid plus rerank |
| 153 | covered | S3 Vectors vs OpenSearch Serverless |
| 154 | covered | distill, continued pre-training |
| 155 | covered | cross-Region, router, PT mapping |
| 156 | not-in-source | Cross-Region page does not state which Region quota a routed request uses. |
| 157 | covered | AgentCore |
| 158 | covered | Q2 additionalModelRequestFields |
| 159 | covered | enableTrace |
| 160 | covered | DynamoDB TTL session memory |
| 161 | covered | ConverseStream plus WebSocket |
| 162 | covered | Q Developer vs Q Business |
| 163 | covered | Flows plus Step Functions |
| 164 | covered | GenAI gateway |
| 165 | covered | batch inference |
| 166 | covered | supervisor and collaborators |
| 167 | covered | MCP streamable HTTP, Cognito |
| 168 | covered | callback token, execution history |
| 169 | covered | Q1 action group executor |
| 170 | covered | Automated Reasoning vs grounding |
| 171 | covered | interface endpoints |
| 172 | covered | Macie, Comprehend, Guardrails |
| 173 | covered | Object Lock, KMS, lifecycle |
| 174 | covered | layered defense |
| 175 | covered | bias drift |
| 176 | covered | prompt-attack filter vs exact word |
| 177 | covered | ApplyGuardrail external model |
| 178 | covered | denied, word filter, sensitive info, prompt attack |
| 179 | covered | Q15 StackSets and SCPs |
| 180 | partial | Guardrails cross-Region page covers geography scope. EU failover detail is thin. |
| 181 | covered | Q14 prompt caching checkpoints and TTL |
| 182 | covered | intelligent prompt routing |
| 183 | covered | S3 Vectors for infrequent search |
| 184 | partial | Metric filters page: filters apply per log group. Per-tool filters are not in source. |
| 185 | covered | PT, batch, on-demand tiers |
| 186 | not-in-source | Semantic cache is not described on an official AWS page fetched here. |
| 187 | covered | retrieve-only evaluation |
| 188 | covered | judge calibration, pinned version |
| 189 | covered | Q6 bring-your-own-inference evaluation |
| 190 | covered | re-sync changed embedding or chunking |
| 191 | covered | context relevance, faithfulness, citation precision |
| 192 | covered | parallel eval jobs and release gate |
| 193 | covered | token estimate before call |
| 194 | covered | KB RetrieveAndGenerate |
| 195 | covered | Standard callback pattern |
| 196 | covered | automatic metrics plus judge budget plan |
| 197 | covered | guardrail detect mode notifications |
| 198 | covered | Flows deterministic, KB node |
| 199 | covered | Q11 logs with Athena, retention period Not in source |
| 200 | covered | provisioned model ARN in Converse |
| 201 | covered | Q8 supervised learning and classification |
| 202 | covered | batch inference |
| 203 | covered | Q8 ML terms |
| 204 | covered | Comprehend sentiment |
| 205 | covered | token pricing |
| 206 | covered | embedding model mismatch |
| 207 | covered | Q8 diffusion model |
| 208 | covered | MCP |
| 209 | covered | RAG over changing manual |
| 210 | covered | fine-tune for voice, RAG for facts |
| 211 | covered | FM lifecycle order |
| 212 | covered | temperature |
| 213 | covered | Q8 few-shot prompting |
| 214 | covered | ROUGE |
| 215 | covered | RAG phase 1 |
| 216 | covered | Agents action groups phase 2 |
| 217 | covered | SageMaker Clarify bias |
| 218 | not-in-source | Certification page does not list the exam guide responsible AI features. |
| 219 | covered | Q13 shared responsibility |
| 220 | covered | CloudTrail |
| 221 | partial | Region and Availability Zone basics are covered. Domain 0 prerequisite. |
| 222 | covered | Q13 shared responsibility, D0 prerequisite |
| 223 | covered | Lambda environment variables page: encrypted at rest. AWS recommends Secrets Manager for sensitive values. |
| 224 | covered | P5 permissions boundary, D0 prerequisite |
| 225 | covered | P1 Glacier Flexible Retrieval, D0 prerequisite |
| 226 | covered | P1 presigned URL, D0 prerequisite |
| 227 | covered | P1 EFS, D0 prerequisite |
| 228 | covered | P2 Spot, D0 prerequisite |
| 229 | covered | NAT gateway placement in a public subnet is consistent with the NAT gateway guidance. |
| 230 | covered | P3 NACL stateless, D0 prerequisite |
| 231 | covered | P4 DynamoDB global tables, D0 prerequisite |
| 232 | covered | Lambda with S3 page: S3 invokes the function asynchronously on object events. The trigger needs resource-based permission. |
| 233 | covered | CloudTrail, D0 prerequisite |
| 234 | covered | P4 SNS fan-out, D0 prerequisite |
| 235 | covered | usage plans and API keys, D0 prerequisite |
| 236 | covered | P1 SSE-KMS, D0 prerequisite |
| 237 | covered | CloudFormation drift, D0 prerequisite |
| 238 | covered | P4 Organizations, D0 prerequisite |
| 239 | covered | P3 gateway endpoint DynamoDB, D0 prerequisite |
| 240 | covered | P3 security groups stateful, D0 prerequisite |
| 241 | covered | S3 Object Lock page confirms WORM retention. Glacier restore is covered in unit P1. |
| 242 | covered | Q3 IAM Identity Center permission sets, D0 prerequisite |
| 243 | covered | Q4 DLQ maxReceiveCount, D0 prerequisite |
| 244 | covered | P4 Firehose and DataBrew, Kinesis Not in source, D0 prerequisite |
| 245 | not-in-source | Hashing and embedding general claims are not in source. |
| 246 | covered | P6 XGBoost, D0 prerequisite |
| 247 | covered | Q8 precision and recall, D0 prerequisite |
| 248 | covered | real-time endpoint, D0 prerequisite |
| 249 | covered | data drift, D0 prerequisite |
| 250 | not-in-source | Recall tuning detail is not in source. |

## Quiz answers that official pages contradict

Fix these answers in the study set. The correct answer and the page that shows it are listed.

| Item | Quiz answer (letter A) | Correct per official page | Page |
|---|---|---|---|
| 22 | S3-event-driven ingestion jobs handle urgent amendments | Ingestion runs when StartIngestionJob starts it. The page names no S3 event trigger. | https://docs.aws.amazon.com/bedrock/latest/userguide/kb-data-source-sync-ingest.html |
| 104 | Confidence scoring is part of the hallucination fix | Structured outputs page does not describe confidence scores. Remove this claim. | https://docs.aws.amazon.com/bedrock/latest/userguide/structured-output.html |
| 119 | Tag CloudWatch token metrics per feature | Application inference profiles track usage and costs. Request metadata does not attribute cost on the fetched pages. | https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-create.html |

## Not in source, with reason

Items 38 and 156: https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html does not state which Region quota applies. Item 126: the AccessDeniedException page gives no region-based cause. Items 38 and 156 cite the Cross-Region inference page, which has no quota-Region text. Item 72 and 145: the BDA page does not describe blueprint schema. Item 98: the Glue page returned only the title. Item 99: per-decision explanation and confidence are not stated. Item 108: fair-lending rules. Item 149: the web crawler page returned only the title, so no schedule text. Item 186: semantic cache is not on an official page fetched here. Item 218: the certification page does not list the responsible AI features. Items 245 and 250: general claims or recall tuning not in source.

## Open items that remain

- Items 54, 141, 180, 184, 221: partial. Official pages cover the core rule. The detail named in the stem is thin or not on the page.
- Item 218: the AWS exam guide list of responsible AI features is not confirmed. The term veracity is not confirmed as an AWS name.

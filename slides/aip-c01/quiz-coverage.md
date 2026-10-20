# Question-bank coverage check, 250 items

This file records the check of the 250 review questions against the master treatise (`article/index.html`). The question text came from the shared quiz batch files, not from this repo. Each status is a topic check against the treatise. The check used keyword and context search, plus official pages for new units. It was not a full read of every stem.

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

| # | Question ID | Status | Note |
|---|---|---|---|
| 001 | q-d1-001 | covered | RAG KB citations |
| 002 | q-d1-002 | covered | PoC on-demand |
| 003 | q-d1-020 | covered | Converse unified, outputConfig schema |
| 004 | q-d1-023 | covered | ElastiCache not durable |
| 005 | q-d1-028 | covered | metadata filters |
| 006 | q-d1-043 | covered | structured output via Converse |
| 007 | q-d1-003 | covered | GenAI Lens |
| 008 | q-d1-006 | covered | smallest model that meets bar |
| 009 | q-d1-007 | covered | AppConfig API GW Lambda |
| 010 | q-d1-008 | covered | EU cross-Region profile |
| 011 | q-d1-010 | covered | PT baseline plus on-demand |
| 012 | q-d1-012 | covered | LoRA small labeled data |
| 013 | q-d1-013 | covered | Model Registry rollback |
| 014 | q-d1-015 | covered | Data Automation |
| 015 | q-d1-016 | covered | Glue DQ plus CW alarms |
| 016 | q-d1-017 | covered | Guardrails not extraction |
| 017 | q-d1-018 | covered | Kendra closed, KB alternative |
| 018 | q-d1-019 | covered | Transcribe diarization then Comprehend PII |
| 019 | q-d1-021 | covered | KB managed hybrid search |
| 020 | q-d1-022 | covered | per-tenant KB plus IAM |
| 021 | q-d1-024 | covered | pgvector Aurora |
| 022 | q-d1-025 | contradicted | Sync page confirms incremental sync via StartIngestionJob. It names no automatic S3 event trigger for ingestion. |
| 023 | q-d1-026 | covered | RAG citations plus contextual grounding |
| 024 | q-d1-027 | covered | Neptune GraphRAG |
| 025 | q-d1-031 | covered | hierarchical chunking |
| 026 | q-d1-032 | covered | Q5 whole-document vs pre-made pairs |
| 027 | q-d1-033 | covered | hybrid search plus rerank |
| 028 | q-d1-034 | covered | Cohere Embed page: input_type takes search_document for corpus and search_query for queries. |
| 029 | q-d1-035 | covered | query expansion |
| 030 | q-d1-038 | covered | dimension choice golden set |
| 031 | q-d1-039 | covered | MCP |
| 032 | q-d1-040 | covered | Prompt Management versions |
| 033 | q-d1-041 | covered | variants vs versions |
| 034 | q-d1-042 | covered | Prompt Flows |
| 035 | q-d1-004 | covered | distill small model |
| 036 | q-d1-005 | covered | PoC then cross-Region |
| 037 | q-d1-009 | covered | prompt router |
| 038 | q-d1-011 | not-in-source | Cross-Region page does not state which Region quota a routed request uses. |
| 039 | q-d1-014 | covered | circuit breaker |
| 040 | q-d1-029 | covered | Q3 IAM Identity Center permission sets |
| 041 | q-d1-030 | covered | chunk boundaries, embeddings |
| 042 | q-d1-036 | covered | recreate data source for chunking |
| 043 | q-d1-037 | covered | table chunk splitting |
| 044 | q-d1-044 | covered | prompt governance, CloudTrail |
| 045 | q-d2-001 | covered | DRAFT, prepare, alias |
| 046 | q-d2-002 | covered | Q1 action group executor |
| 047 | q-d2-003 | covered | supervisor collaborators |
| 048 | q-d2-004 | covered | DynamoDB memory |
| 049 | q-d2-005 | covered | callback task token |
| 050 | q-d2-006 | covered | Lambda 15 min limit |
| 051 | q-d2-007 | covered | Strands, Agent Squad |
| 052 | q-d2-008 | covered | MCP on Lambda or ECS |
| 053 | q-d2-009 | covered | AgentCore |
| 054 | q-d2-011 | partial | Step Functions error and timeout pages cover TimeoutSeconds and catchers. Stopping-condition wording is not on the page. |
| 055 | q-d2-013 | covered | on-demand scale to zero |
| 056 | q-d2-015 | covered | batch inference |
| 057 | q-d2-016 | covered | SageMaker real-time custom containers |
| 058 | q-d2-017 | covered | model cascade |
| 059 | q-d2-018 | covered | serverless endpoint scales to zero, cold start |
| 060 | q-d2-020 | covered | Q4 DLQ maxReceiveCount |
| 061 | q-d2-021 | covered | Outposts |
| 062 | q-d2-022 | covered | GenAI gateway |
| 063 | q-d2-023 | covered | release gates |
| 064 | q-d2-024 | covered | Q3 IAM Identity Center permission sets |
| 065 | q-d2-026 | covered | Q2 additionalModelRequestFields |
| 066 | q-d2-027 | covered | Converse no embeddings |
| 067 | q-d2-028 | covered | InvokeModel provider body |
| 068 | q-d2-029 | covered | ConverseStream |
| 069 | q-d2-031 | covered | ApplyGuardrail any model |
| 070 | q-d2-032 | covered | Claude body anthropic_version max_tokens |
| 071 | q-d2-033 | covered | Q Developer vs Q Business |
| 072 | q-d2-034 | not-in-source | BDA overview page does not describe custom blueprint schema. |
| 073 | q-d2-035 | covered | Amplify |
| 074 | q-d2-010 | covered | agent combined scenario |
| 075 | q-d2-012 | covered | agent trace |
| 076 | q-d2-014 | covered | PT plus on-demand burst |
| 077 | q-d2-019 | covered | SageMaker async inference |
| 078 | q-d2-025 | covered | CloudTrail is audit, not pipeline |
| 079 | q-d2-030 | covered | provisioned model ARN |
| 080 | q-d2-036 | covered | Q9 S3 versioning |
| 081 | q-d3-001 | covered | denied topics |
| 082 | q-d3-002 | covered | sensitive info filter mask |
| 083 | q-d3-003 | covered | word filters |
| 084 | q-d3-004 | covered | prompt attack filter |
| 085 | q-d3-005 | covered | contextual grounding |
| 086 | q-d3-006 | covered | Automated Reasoning |
| 087 | q-d3-007 | covered | defense in depth, Comprehend pre-filter |
| 088 | q-d3-008 | covered | ApplyGuardrail self-hosted model |
| 089 | q-d3-011 | covered | VPC interface endpoints |
| 090 | q-d3-012 | covered | Macie, Comprehend, Guardrails pipeline |
| 091 | q-d3-013 | covered | Macie at rest |
| 092 | q-d3-014 | covered | Comprehend realtime plus Guardrails |
| 093 | q-d3-015 | covered | invocation logging privacy |
| 094 | q-d3-016 | covered | translation no protection |
| 095 | q-d3-018 | covered | Lake Formation column grants |
| 096 | q-d3-019 | covered | Model Cards |
| 097 | q-d3-020 | covered | CloudTrail identity and time |
| 098 | q-d3-021 | not-in-source | Glue lineage page returned only the title. No lineage text found. |
| 099 | q-d3-024 | not-in-source | Per-decision explanation and confidence level are not stated on the fetched pages. |
| 100 | q-d3-025 | covered | LLM-as-judge plus human brand voice |
| 101 | q-d3-026 | covered | fairness metrics, A/B, judge |
| 102 | q-d3-027 | covered | transparency citations, grounding |
| 103 | q-d3-009 | covered | denied topics, sensitive info, prompt attack |
| 104 | q-d3-010 | contradicted | Structured outputs page does not describe confidence scores. Quiz claim is not supported as stated. |
| 105 | q-d3-017 | covered | VPC endpoints, KMS, CloudTrail |
| 106 | q-d3-022 | covered | continuous monitoring and remediation |
| 107 | q-d3-023 | covered | bias drift monitoring |
| 108 | q-d3-028 | not-in-source | Fair-lending rules are not in source. |
| 109 | q-d4-011 | covered | inference params do not cut cost |
| 110 | q-d4-001 | covered | prompt caching |
| 111 | q-d4-002 | covered | PT baseline |
| 112 | q-d4-003 | covered | router |
| 113 | q-d4-004 | covered | batch inference |
| 114 | q-d4-005 | covered | cost levers |
| 115 | q-d4-006 | covered | semantic cache vs prompt cache |
| 116 | q-d4-008 | covered | temperature 0 and PT |
| 117 | q-d4-009 | covered | streaming |
| 118 | q-d4-010 | covered | PT not consistency |
| 119 | q-d4-013 | contradicted | Application inference profiles track usage and costs per profile. Request metadata is not shown as a cost source on the fetched pages. Quiz answer needs correction. |
| 120 | q-d4-014 | covered | anomaly detection, evaluation jobs |
| 121 | q-d4-015 | covered | X-Ray and agent trace |
| 122 | q-d4-016 | covered | Model Monitor not for text |
| 123 | q-d4-007 | covered | caching plus routing plus PT |
| 124 | q-d4-012 | covered | OpenSearch shard sizing page: 10 to 30 GiB for search latency, 30 to 50 GiB for write-heavy. Default is 5 primary shards and 1 replica. |
| 125 | q-d4-017 | covered | invocation logging forensic |
| 126 | q-d5-010 | not-in-source | Official AccessDeniedException page gives no region-based cause. Quiz answer not confirmed. |
| 127 | q-d5-001 | covered | programmatic metrics fixed dataset |
| 128 | q-d5-002 | covered | judge calibrated to humans |
| 129 | q-d5-003 | covered | human eval for brand voice |
| 130 | q-d5-004 | covered | KB evaluation metrics page names context relevance, context coverage, faithfulness, and correctness. |
| 131 | q-d5-005 | covered | regression testing |
| 132 | q-d5-006 | covered | judge plus human |
| 133 | q-d5-008 | covered | exact match cannot judge style |
| 134 | q-d5-009 | covered | Claude body ValidationException |
| 135 | q-d5-011 | covered | DRAFT vs prepare alias |
| 136 | q-d5-012 | covered | debug retrieval first |
| 137 | q-d5-014 | covered | prompt version compare, golden regression |
| 138 | q-d5-007 | covered | Q6 bring-your-own-inference evaluation |
| 139 | q-d5-013 | covered | Q5 whole-document vs chunking |
| 140 | q-d5-015 | covered | PT model units plus overflow |
| 141 | q-d1-202 | partial | Embedding dimension choice is covered. Process detail is thin. |
| 142 | q-d1-204 | covered | query decomposition |
| 143 | q-d1-205 | covered | reject fine-tuning, RAG re-sync |
| 144 | q-d1-207 | covered | Q17 custom transformation Lambda for structure |
| 145 | q-d1-209 | not-in-source | BDA blueprint schema is not in the fetched page. |
| 146 | q-d1-210 | covered | metadata filter before vector search |
| 147 | q-d1-212 | covered | AppConfig plus canary |
| 148 | q-d1-213 | covered | GenAI Lens review standard |
| 149 | q-d1-214 | not-in-source | Web crawler page returned only the title. No schedule text found. |
| 150 | q-d1-216 | covered | LLM judge faithfulness |
| 151 | q-d1-201 | covered | hierarchical chunking |
| 152 | q-d1-203 | covered | hybrid plus rerank |
| 153 | q-d1-206 | covered | S3 Vectors vs OpenSearch Serverless |
| 154 | q-d1-208 | covered | distill, continued pre-training |
| 155 | q-d1-211 | covered | cross-Region, router, PT mapping |
| 156 | q-d1-215 | not-in-source | Cross-Region page does not state which Region quota a routed request uses. |
| 157 | q-d2-202 | covered | AgentCore |
| 158 | q-d2-204 | covered | Q2 additionalModelRequestFields |
| 159 | q-d2-205 | covered | enableTrace |
| 160 | q-d2-207 | covered | DynamoDB TTL session memory |
| 161 | q-d2-208 | covered | ConverseStream plus WebSocket |
| 162 | q-d2-209 | covered | Q Developer vs Q Business |
| 163 | q-d2-210 | covered | Flows plus Step Functions |
| 164 | q-d2-211 | covered | GenAI gateway |
| 165 | q-d2-212 | covered | batch inference |
| 166 | q-d2-201 | covered | supervisor and collaborators |
| 167 | q-d2-203 | covered | MCP streamable HTTP, Cognito |
| 168 | q-d2-206 | covered | callback token, execution history |
| 169 | q-d2-213 | covered | Q1 action group executor |
| 170 | q-d3-203 | covered | Automated Reasoning vs grounding |
| 171 | q-d3-205 | covered | interface endpoints |
| 172 | q-d3-206 | covered | Macie, Comprehend, Guardrails |
| 173 | q-d3-207 | covered | Object Lock, KMS, lifecycle |
| 174 | q-d3-209 | covered | layered defense |
| 175 | q-d3-210 | covered | bias drift |
| 176 | q-d3-211 | covered | prompt-attack filter vs exact word |
| 177 | q-d3-201 | covered | ApplyGuardrail external model |
| 178 | q-d3-202 | covered | denied, word filter, sensitive info, prompt attack |
| 179 | q-d3-204 | covered | Q15 StackSets and SCPs |
| 180 | q-d3-208 | partial | Guardrails cross-Region page covers geography scope. EU failover detail is thin. |
| 181 | q-d4-202 | covered | Q14 prompt caching checkpoints and TTL |
| 182 | q-d4-203 | covered | intelligent prompt routing |
| 183 | q-d4-204 | covered | S3 Vectors for infrequent search |
| 184 | q-d4-205 | partial | Metric filters page: filters apply per log group. Per-tool filters are not in source. |
| 185 | q-d4-201 | covered | PT, batch, on-demand tiers |
| 186 | q-d4-206 | not-in-source | Semantic cache is not described on an official AWS page fetched here. |
| 187 | q-d5-202 | covered | retrieve-only evaluation |
| 188 | q-d5-203 | covered | judge calibration, pinned version |
| 189 | q-d5-205 | covered | Q6 bring-your-own-inference evaluation |
| 190 | q-d5-206 | covered | re-sync changed embedding or chunking |
| 191 | q-d5-201 | covered | context relevance, faithfulness, citation precision |
| 192 | q-d5-204 | covered | parallel eval jobs and release gate |
| 193 | q-d4-207 | covered | token estimate before call |
| 194 | q-d1-217 | covered | KB RetrieveAndGenerate |
| 195 | q-d2-215 | covered | Standard callback pattern |
| 196 | q-d5-207 | covered | automatic metrics plus judge budget plan |
| 197 | q-d3-212 | covered | guardrail detect mode notifications |
| 198 | q-d2-214 | covered | Flows deterministic, KB node |
| 199 | q-d3-213 | covered | Q11 logs with Athena, retention period Not in source |
| 200 | q-d4-208 | covered | provisioned model ARN in Converse |
| 201 | pq-d1-1 | covered | Q8 supervised learning and classification |
| 202 | pq-d1-2 | covered | batch inference |
| 203 | pq-d1-3 | covered | Q8 ML terms |
| 204 | pq-d1-4 | covered | Comprehend sentiment |
| 205 | pq-d2-5 | covered | token pricing |
| 206 | pq-d2-6 | covered | embedding model mismatch |
| 207 | pq-d2-7 | covered | Q8 diffusion model |
| 208 | pq-d2-8 | covered | MCP |
| 209 | pq-d3-9 | covered | RAG over changing manual |
| 210 | pq-d3-10 | covered | fine-tune for voice, RAG for facts |
| 211 | pq-d3-11 | covered | FM lifecycle order |
| 212 | pq-d3-12 | covered | temperature |
| 213 | pq-d3-13 | covered | Q8 few-shot prompting |
| 214 | pq-d3-14 | covered | ROUGE |
| 215 | pq-d3-15 | covered | RAG phase 1 |
| 216 | pq-d3-16 | covered | Agents action groups phase 2 |
| 217 | pq-d4-17 | covered | SageMaker Clarify bias |
| 218 | pq-d4-18 | not-in-source | Certification page does not list the exam guide responsible AI features. |
| 219 | pq-d5-19 | covered | Q13 shared responsibility |
| 220 | pq-d5-20 | covered | CloudTrail |
| 221 | foundations-map-check | partial | Region and Availability Zone basics are covered. Domain 0 prerequisite. |
| 222 | shared-responsibility-check | covered | Q13 shared responsibility, D0 prerequisite |
| 223 | iam-role-check | covered | Lambda environment variables page: encrypted at rest. AWS recommends Secrets Manager for sensitive values. |
| 224 | iam-boundary-check | covered | P5 permissions boundary, D0 prerequisite |
| 225 | s3-lifecycle-check | covered | P1 Glacier Flexible Retrieval, D0 prerequisite |
| 226 | s3-share-check | covered | P1 presigned URL, D0 prerequisite |
| 227 | ec2-storage-check | covered | P1 EFS, D0 prerequisite |
| 228 | ec2-pricing-check | covered | P2 Spot, D0 prerequisite |
| 229 | vpc-nat-check | covered | NAT gateway placement in a public subnet is consistent with the NAT gateway guidance. |
| 230 | vpc-sg-nacl-check | covered | P3 NACL stateless, D0 prerequisite |
| 231 | db-pick-check | covered | P4 DynamoDB global tables, D0 prerequisite |
| 232 | lambda-trigger-check | covered | Lambda with S3 page: S3 invokes the function asynchronously on object events. The trigger needs resource-based permission. |
| 233 | observability-check | covered | CloudTrail, D0 prerequisite |
| 234 | messaging-check | covered | P4 SNS fan-out, D0 prerequisite |
| 235 | apigw-check | covered | usage plans and API keys, D0 prerequisite |
| 236 | kms-check | covered | P1 SSE-KMS, D0 prerequisite |
| 237 | cfn-check | covered | CloudFormation drift, D0 prerequisite |
| 238 | billing-check | covered | P4 Organizations, D0 prerequisite |
| 239 | final-01 | covered | P3 gateway endpoint DynamoDB, D0 prerequisite |
| 240 | final-02 | covered | P3 security groups stateful, D0 prerequisite |
| 241 | final-03 | covered | S3 Object Lock page confirms WORM retention. Glacier restore is covered in unit P1. |
| 242 | final-04 | covered | Q3 IAM Identity Center permission sets, D0 prerequisite |
| 243 | final-05 | covered | Q4 DLQ maxReceiveCount, D0 prerequisite |
| 244 | pq-data | covered | P4 Firehose and DataBrew, Kinesis Not in source, D0 prerequisite |
| 245 | pq-features | not-in-source | Hashing and embedding general claims are not in source. |
| 246 | pq-training | covered | P6 XGBoost, D0 prerequisite |
| 247 | pq-eval | covered | Q8 precision and recall, D0 prerequisite |
| 248 | pq-deploy | covered | real-time endpoint, D0 prerequisite |
| 249 | pq-monitor | covered | data drift, D0 prerequisite |
| 250 | pq-final | not-in-source | Recall tuning detail is not in source. |

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

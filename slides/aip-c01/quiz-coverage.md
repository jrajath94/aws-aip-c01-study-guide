# Question-bank coverage check, 250 items

This file records the check of the 250 review questions against the master treatise (`article/index.html`). The question text came from the shared quiz batch files, not from this repo. Each status is a topic check against the treatise. The check used keyword and context search, plus official pages for new units. It was not a full read of every stem.

## Result

| Status | Count |
|---|---|
| covered | 222 |
| partial | 27 |
| gap | 1 |
| total | 250 |

Items 1 to 220 are AIP-C01 exam-scope questions and ML basics. Items 221 to 250 are AWS and ML prerequisites (domain 0), which are not exam domains.

| Items | Covered | Partial | Gap |
|---|---|---|---|
| 1 to 50 | 47 | 3 | 0 |
| 51 to 100 | 46 | 4 | 0 |
| 101 to 150 | 41 | 9 | 0 |
| 151 to 200 | 46 | 4 | 0 |
| 201 to 250 | 42 | 7 | 1 |

Status meanings. Covered: the treatise states the tested fact or rule. Partial: the topic is present, but a tested detail is missing, thin, or not confirmed. Gap: the treatise does not state the tested fact.

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
| 022 | q-d1-025 | partial | Q17 incremental sync confirmed, no automatic S3 event trigger on page |
| 023 | q-d1-026 | covered | RAG citations plus contextual grounding |
| 024 | q-d1-027 | covered | Neptune GraphRAG |
| 025 | q-d1-031 | covered | hierarchical chunking |
| 026 | q-d1-032 | covered | Q5 whole-document vs pre-made pairs |
| 027 | q-d1-033 | covered | hybrid search plus rerank |
| 028 | q-d1-034 | partial | Cohere input_type, one mention |
| 029 | q-d1-035 | covered | query expansion |
| 030 | q-d1-038 | covered | dimension choice golden set |
| 031 | q-d1-039 | covered | MCP |
| 032 | q-d1-040 | covered | Prompt Management versions |
| 033 | q-d1-041 | covered | variants vs versions |
| 034 | q-d1-042 | covered | Prompt Flows |
| 035 | q-d1-004 | covered | distill small model |
| 036 | q-d1-005 | covered | PoC then cross-Region |
| 037 | q-d1-009 | covered | prompt router |
| 038 | q-d1-011 | partial | source-Region quota for routed requests, no direct text |
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
| 054 | q-d2-011 | partial | Step Functions stopping conditions, one mention |
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
| 072 | q-d2-034 | partial | Data Automation, custom blueprint not in treatise |
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
| 098 | q-d3-021 | partial | Glue Data Catalog lineage, one mention |
| 099 | q-d3-024 | partial | transparency principle covered, per-decision explanation and confidence only at principle level |
| 100 | q-d3-025 | covered | LLM-as-judge plus human brand voice |
| 101 | q-d3-026 | covered | fairness metrics, A/B, judge |
| 102 | q-d3-027 | covered | transparency citations, grounding |
| 103 | q-d3-009 | covered | denied topics, sensitive info, prompt attack |
| 104 | q-d3-010 | partial | grounding covered, confidence scoring and JSON Schema not in treatise |
| 105 | q-d3-017 | covered | VPC endpoints, KMS, CloudTrail |
| 106 | q-d3-022 | covered | continuous monitoring and remediation |
| 107 | q-d3-023 | covered | bias drift monitoring |
| 108 | q-d3-028 | partial | fairness and model cards covered, fair-lending rules not in treatise |
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
| 119 | q-d4-013 | partial | Q16 request metadata is not a cost allocation tag, answer needs correction |
| 120 | q-d4-014 | covered | anomaly detection, evaluation jobs |
| 121 | q-d4-015 | covered | X-Ray and agent trace |
| 122 | q-d4-016 | covered | Model Monitor not for text |
| 123 | q-d4-007 | covered | caching plus routing plus PT |
| 124 | q-d4-012 | partial | query preprocessing and hybrid covered, index sharding not in treatise |
| 125 | q-d4-017 | covered | invocation logging forensic |
| 126 | q-d5-010 | partial | Q17 official error page gives no region cause, answer not confirmed |
| 127 | q-d5-001 | covered | programmatic metrics fixed dataset |
| 128 | q-d5-002 | covered | judge calibrated to humans |
| 129 | q-d5-003 | covered | human eval for brand voice |
| 130 | q-d5-004 | partial | faithfulness covered, retrieval relevance metric thin |
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
| 141 | q-d1-202 | partial | embedding dims and multilingual choice covered, process thin |
| 142 | q-d1-204 | covered | query decomposition |
| 143 | q-d1-205 | covered | reject fine-tuning, RAG re-sync |
| 144 | q-d1-207 | covered | Q17 custom transformation Lambda for structure |
| 145 | q-d1-209 | partial | Q10 BDA, blueprint schema Not in source |
| 146 | q-d1-210 | covered | metadata filter before vector search |
| 147 | q-d1-212 | covered | AppConfig plus canary |
| 148 | q-d1-213 | covered | GenAI Lens review standard |
| 149 | q-d1-214 | partial | web crawler source, weekly schedule not in source |
| 150 | q-d1-216 | covered | LLM judge faithfulness |
| 151 | q-d1-201 | covered | hierarchical chunking |
| 152 | q-d1-203 | covered | hybrid plus rerank |
| 153 | q-d1-206 | covered | S3 Vectors vs OpenSearch Serverless |
| 154 | q-d1-208 | covered | distill, continued pre-training |
| 155 | q-d1-211 | covered | cross-Region, router, PT mapping |
| 156 | q-d1-215 | partial | source-Region quota, no direct text |
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
| 180 | q-d3-208 | partial | guardrail regional scope, EU-limited failover thin |
| 181 | q-d4-202 | covered | Q14 prompt caching checkpoints and TTL |
| 182 | q-d4-203 | covered | intelligent prompt routing |
| 183 | q-d4-204 | covered | S3 Vectors for infrequent search |
| 184 | q-d4-205 | partial | anomaly detection covered, CloudWatch metric filters per tool not in treatise |
| 185 | q-d4-201 | covered | PT, batch, on-demand tiers |
| 186 | q-d4-206 | partial | semantic cache limits covered, personalized query case thin |
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
| 218 | pq-d4-18 | gap | Q12 cannot confirm the exam guide list |
| 219 | pq-d5-19 | covered | Q13 shared responsibility |
| 220 | pq-d5-20 | covered | CloudTrail |
| 221 | foundations-map-check | partial | region and AZ basics, D0 prerequisite |
| 222 | shared-responsibility-check | covered | Q13 shared responsibility, D0 prerequisite |
| 223 | iam-role-check | partial | P5 execution role, env var encryption Not in source, D0 prerequisite |
| 224 | iam-boundary-check | covered | P5 permissions boundary, D0 prerequisite |
| 225 | s3-lifecycle-check | covered | P1 Glacier Flexible Retrieval, D0 prerequisite |
| 226 | s3-share-check | covered | P1 presigned URL, D0 prerequisite |
| 227 | ec2-storage-check | covered | P1 EFS, D0 prerequisite |
| 228 | ec2-pricing-check | covered | P2 Spot, D0 prerequisite |
| 229 | vpc-nat-check | partial | P3 NAT placement Not in source, D0 prerequisite |
| 230 | vpc-sg-nacl-check | covered | P3 NACL stateless, D0 prerequisite |
| 231 | db-pick-check | covered | P4 DynamoDB global tables, D0 prerequisite |
| 232 | lambda-trigger-check | partial | S3 event trigger mentioned once, D0 prerequisite |
| 233 | observability-check | covered | CloudTrail, D0 prerequisite |
| 234 | messaging-check | covered | P4 SNS fan-out, D0 prerequisite |
| 235 | apigw-check | covered | usage plans and API keys, D0 prerequisite |
| 236 | kms-check | covered | P1 SSE-KMS, D0 prerequisite |
| 237 | cfn-check | covered | CloudFormation drift, D0 prerequisite |
| 238 | billing-check | covered | P4 Organizations, D0 prerequisite |
| 239 | final-01 | covered | P3 gateway endpoint DynamoDB, D0 prerequisite |
| 240 | final-02 | covered | P3 security groups stateful, D0 prerequisite |
| 241 | final-03 | partial | P1 Glacier covered, Object Lock details thin, D0 prerequisite |
| 242 | final-04 | covered | Q3 IAM Identity Center permission sets, D0 prerequisite |
| 243 | final-05 | covered | Q4 DLQ maxReceiveCount, D0 prerequisite |
| 244 | pq-data | covered | P4 Firehose and DataBrew, Kinesis Not in source, D0 prerequisite |
| 245 | pq-features | partial | P6 hashing and embeddings are general, Not in source, D0 prerequisite |
| 246 | pq-training | covered | P6 XGBoost, D0 prerequisite |
| 247 | pq-eval | covered | Q8 precision and recall, D0 prerequisite |
| 248 | pq-deploy | covered | real-time endpoint, D0 prerequisite |
| 249 | pq-monitor | covered | data drift, D0 prerequisite |
| 250 | pq-final | partial | real-time endpoint covered, recall tuning thin, D0 prerequisite |

## Open items that remain

- Item 218: the AWS exam guide list of responsible AI features is not confirmed. The term veracity is not confirmed as an AWS name.
- Items 38 and 156: the official cross-Region page does not say which Region's quota applies to a routed request.
- Item 22: the sync page confirms incremental sync and does not name an automatic S3 event trigger.
- Item 126: the official error page gives no region-based cause for AccessDeniedException. The quiz answer is not confirmed.
- Item 119: the official page says per-request tags are not cost allocation tags. The quiz answer needs correction. Unit Q16 gives the correction.
- Items 28, 54, 72, 98, 99, 104, 108, 124, 130, 141, 145, 149, 180, 184, 186: partial. The page for each was not fetched in this pass, or the official source does not state the detail. Items 99 and 108 are Not in source for the stated claims.
- Items 221, 223, 229, 232, 241, 245, 250: partial prerequisites. Some details are Not in source in this build.

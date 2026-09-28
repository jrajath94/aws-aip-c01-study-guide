---
slug: volume-appendix-gaps
file: volume-appendix-gaps.html
title: "AIP-C01 Gap Appendix: 17 Topics the Other Volumes Skip"
label: "Appendix · Coverage Gaps"
track: aipc01
---

# Gap Appendix: 17 Topics the Other Volumes Skip {#gap-appendix-17-topics-the-other-volumes-skip}

A completionist pass over every gap in the coverage map. Each topic is taught from zero, with a visual, a walkthrough, and an explicit statement of how AWS will ask about it.

## Read this first. What this volume is and why it exists. {#read-this-first-what-this-volume-is-and-why-it-exists}

The seven core volumes and the labs volume cover every task statement in the official AIP-C01 exam guide. But a three-way cross-check (exam guide vs. the Maarek study guide sections I-X vs. every volume) found 17 items that were either **hard gaps** (not taught anywhere) or **partials** (mentioned but never taught as a topic). This appendix closes all 17. It is organized so each topic stands alone: you can read one entry in five minutes and know exactly what AWS can ask you about it.

- **Hard gaps (5):** Amazon AppFlow, AWS Transfer Family, Amazon QuickSight, Neptune Analytics, Amazon Q Apps. Short, complete entries.
- **Partials (12):** Secrets Manager, WAF, CloudFront, Textract, divider strings for chunking, the CountTokens API by name, top_k by name, CloudWatch Evidently by name, TTFT by name, binary vectors and FP16 quantization, SageMaker large-model tuning specifics, EMR. Taught properly here.

Entries marked UNVERIFIED could not be confirmed in live AWS documentation on the verification date and should be treated as lower confidence. Numbers that are volatile (pricing, quotas) are labeled illustrative.

## Scope and gap types {#scope}

Every entry follows the same shape: what it is, why it exists, how it works, concrete numbers, the common misunderstanding AWS exploits, a diagram with a walkthrough, and a "how AWS will ask" line. Two gap types matter:

Hard gapThe topic appears in no other volume. The entry here is the complete teaching, condensed to exam size.
PartialSome other volume mentions the name or teaches the surrounding concept. The entry here teaches the missing piece and points at the existing home volume for context.

## Decision ladder placement {#ladder}

Each entry ends with a one-line placement on the GenAI decision ladder so you can answer "which service" questions fast:

```
  GenAI decision ladder (where each gap topic sits)

  Data in        Ingestion        Processing        Model        App        Ops
  |--------------|---------------|-----------------|------------|----------|------------|
  Transfer Fam.  AppFlow          Textract          SageMaker    Q Apps     QuickSight
  (file drops)   (SaaS sync)      (doc OCR)         (large dep)  (no-code)  (dashboards)
                                EMR (big ETL)     top_k / TTFT Evidently
                                dividers          CountTokens  WAF/CloudFront
                                vector-opt        Neptune An.  Secrets Mgr
```

Figure 0.1. Each appendix topic placed on the pipeline it belongs to. Read left to right: raw data becomes model input becomes answers becomes monitored products.

How to read this diagram

1. **Left to right is time.** Data enters on the left as files, SaaS records, or documents, and exits on the right as dashboards and monitored applications.
2. **Each topic sits in exactly one column.** That column is the exam's favorite framing: "your data arrives as file drops" points to Transfer Family, "your data lives in Salesforce" points to AppFlow.
3. **The model column is the decision core.** top_k, TTFT, and CountTokens are inference-time primitives; SageMaker large-model tuning and vector optimization are deployment-time decisions.
4. **The right column is everything that keeps the app safe and observable.** WAF, CloudFront, Secrets Manager, Evidently, QuickSight.
5. **If an entry breaks,** data stops one column to the left of where you notice the symptom. A bad Textract stage shows up as bad RAG answers, not as a Textract error.

Last verified: 2026-09-28. Verification sources and method are listed in the [verification log](#verification-log). Generic learning content only; no personal identifiers.

## 1. Ingestion gaps: AppFlow and Transfer Family {#1-ingestion-gaps-appflow-and-transfer-family}

Two managed services that get data INTO AWS. Both are exam favorites for "choose the ingestion service" scenarios because they look interchangeable until you learn the one-line difference.

### Amazon AppFlow {#appflow}

#### What it is {#what-it-is}

Amazon AppFlow is a fully managed integration service that moves data between SaaS applications (software you use over the internet, like Salesforce or ServiceNow) and AWS services, in both directions, without writing custom connectors. Think of it as a managed pipe with a form: you pick the source, pick the destination, describe the fields, and AppFlow runs the transfer.

#### Why it exists {#why-it-exists}

GenAI applications are hungry for enterprise data, and that data lives in SaaS tools: support tickets in Zendesk, cases in Salesforce, employee records in Workday. Without AppFlow, engineers write and maintain brittle one-off API scripts that break when the SaaS vendor changes pagination or rate limits. AppFlow replaces that glue code with a managed flow, and it solves the credential problem too: connection credentials are stored centrally instead of in code.

#### How it works {#how-it-works}

1. **Connector profile.** You authenticate once to the SaaS app (OAuth or credentials). AppFlow stores the credentials in AWS Secrets Manager, so the flow never embeds secrets.
2. **Flow definition.** A flow names a source, a destination, field mappings (which source field goes to which destination field), optional transformations (masking, truncation, concatenation), and filters (only records matching a condition).
3. **Trigger.** Flows run on demand, on a schedule, or event-driven (triggered when the SaaS app emits a change event), so syncs can be near real time.
4. **Incremental pulls.** Flows can pull only records changed since the last run instead of full snapshots, which keeps large SaaS datasets cheap to sync.
5. **Destinations.** Common destinations are Amazon S3, Amazon Redshift, Salesforce itself, and other AWS services; the data lands ready for Glue ETL or a Knowledge Base ingestion job. Flows also integrate with the AWS Glue Data Catalog so the synced data is queryable.

#### Concrete numbers {#concrete-numbers}

AppFlow pricing is flow-based (illustrative: on the order of a dollar per flow run plus data processed, not per seat). The exam does not test exact pricing; it tests the trigger and mapping concepts. What matters numerically: a scheduled flow syncing 10 million records once a day costs roughly the same compute whether the records changed or not, which is why **incremental pulls** are the cost answer in scenario questions.

:::takeaway

Key exam facts.

(1) AppFlow = SaaS to AWS data movement, no code. (2) Flows support on-demand, scheduled, and event-driven triggers. (3) Incremental pulls sync only changed records. (4) Credentials live in Secrets Manager via connector profiles. (5) Private connections can run over AWS PrivateLink so SaaS traffic never crosses the public internet.
:::

:::exam-ask

Trap.

AWS will offer Amazon EventBridge or a custom Lambda poller as distractors for "sync Salesforce cases into S3 for RAG." EventBridge routes events; it does not do field mapping, transformation, or incremental record pulls. The moment the scenario mentions field mapping or masking PII during the sync, the answer is AppFlow.
:::

```
  Salesforce cases ----->  +-----------+  field map / mask PII  +--------+  Glue / KB
                            |  AppFlow  | ----------------------> |   S3   | -----------> RAG
  Zendesk tickets  ----->  |   flow    |   incremental pulls      +--------+    answers
                            +-----------+
                                 ^
                          credentials in
                          Secrets Manager
```

Figure 1.1. AppFlow syncs SaaS data into S3, where it becomes RAG fuel. The flow handles auth, mapping, masking, and incremental sync; downstream, Glue or a Knowledge Base treats the S3 prefix as a normal data source.

How to read this diagram

1. **Left boxes are SaaS sources.** Data starts in systems AWS does not own. AppFlow's whole job is the arrow from left to middle.
2. **The middle box does four jobs:** authenticate (via Secrets Manager), map fields, transform or mask, and pull incrementally. Each is a separate exam concept.
3. **The S3 box is the handoff.** After this point, the GenAI pipeline (Glue, BDA, Knowledge Bases) works exactly as taught in D1; AppFlow is only the ingestion story.
4. **What breaks:** if the SaaS credential rotates, the flow fails at step 1; if a field mapping is wrong, downstream Glue jobs see nulls, not errors. Debugging starts at the flow, not at the RAG answers.

Decision ladder placement

Data in / ingestion: "your source data lives in a SaaS app" = AppFlow.

:::exam-ask

Scenario: "A company wants support tickets from Zendesk synced to S3 hourly, with only new tickets, and customer emails masked, for a RAG knowledge base." Correct: AppFlow with a scheduled flow, incremental pull, and masking transformation. Distractors: EventBridge (no mapping), Glue alone (no SaaS connector), Kinesis (streaming infra, overkill for hourly sync).
:::

A team needs Salesforce opportunity records synced to Amazon S3 every 15 minutes, including only records modified since the last sync, with phone numbers masked before storage. The data will feed a Bedrock Knowledge Base. Which solution meets the requirements with the least operational overhead?

1. Write a Lambda function that polls the Salesforce API every 15 minutes and writes results to S3.
2. Create an Amazon AppFlow flow with a scheduled trigger, incremental transfer, and a masking transformation, with S3 as the destination.
3. Configure Amazon EventBridge to receive Salesforce change events and route them to S3.
4. Use AWS Database Migration Service to replicate the Salesforce database to S3.

B is correct. AppFlow natively supports SaaS sources, scheduled triggers, incremental pulls, and field-level masking, which is exactly the requirement set.

A is wrong because a custom Lambda re-implements pagination, retry, and credential handling that AppFlow provides managed, so it is not least overhead. C is wrong because EventBridge routes events but does not map fields or mask data. D is wrong because DMS replicates databases, not SaaS APIs, and has no masking transform.

### AWS Transfer Family {#transfer-family}

#### What it is {#what-it-is}

AWS Transfer Family is a fully managed file-transfer service that runs SFTP (SSH File Transfer Protocol), FTPS (FTP over TLS/SSL), FTP (plain File Transfer Protocol), and AS2 (Applicability Statement 2, a B2B messaging protocol) servers, backed by Amazon S3 or Amazon EFS. Partners keep using the same file-transfer clients they have used for years; the files land directly in your S3 bucket.

#### Why it exists {#why-it-exists}

Enterprises exchange data as file drops: a partner uploads a nightly CSV over SFTP, a vendor sends invoices over AS2. Before Transfer Family, you ran your own SFTP servers on EC2 (patching, scaling, key management) and then copied files into S3. Transfer Family removes the server fleet: the protocol endpoint is managed, and S3 is the storage, so a file drop is one hop away from a GenAI ingestion pipeline.

#### How it works {#how-it-works}

1. You create a Transfer Family server for a protocol (for example SFTP) and point it at an S3 bucket (or EFS file system).
2. Users authenticate with SSH keys, passwords, or an external identity provider; each user is mapped to a home directory inside the bucket.
3. Uploads and downloads go straight to S3 objects. An S3 event notification can then trigger the next step: Lambda validation, Bedrock Data Automation, or a Knowledge Base ingestion job.
4. **Endpoint rules matter.** Public endpoints support SFTP only. Plain FTP is supported only on VPC-internal endpoints, because unencrypted FTP must never cross the public internet.

#### Concrete numbers {#concrete-numbers}

Pricing is per protocol-enabled endpoint per hour plus data transferred (illustrative; exact figures change). The exam-relevant number is not the price but the protocol matrix:

| Protocol | Public endpoint | VPC endpoint |
|---|---|---|
| SFTP | Yes | Yes |
| FTPS | Yes | Yes |
| FTP | No | Yes (internal only) |
| AS2 | Yes | Yes |

:::takeaway

Key exam facts.

(1) Transfer Family = managed SFTP/FTPS/FTP/AS2 servers with S3 or EFS storage. (2) Plain FTP works only on VPC-internal endpoints. (3) Files land as S3 objects, so S3 event notifications chain naturally into GenAI ingestion.
:::

:::exam-ask

Trap.

The classic distractor is "use S3 presigned URLs" for partner file exchange. Presigned URLs work for your own applications, not for partners who only speak SFTP and will not rewrite their tooling. The phrase "partners upload files using their existing SFTP clients" is the Transfer Family trigger.
:::

```
  Partner SFTP client --SSH-->  Transfer Family  --S3 API-->  s3://ingest-bucket/
  (unchanged tooling)            SFTP server                      |
                                                                 v  S3 event
                                                        Lambda / BDA / KB ingest
                                                        (GenAI pipeline, D1 ch9)
```

Figure 1.2. Transfer Family terminates the legacy protocol and stores objects in S3. From there the standard GenAI ingestion pipeline takes over; the partner never learns anything changed.

How to read this diagram

1. **The partner is unchanged.** That is the entire value proposition: no client migration, no retraining.
2. **The server is managed.** No EC2 fleet, no patching, no key server to operate. Protocol ends here.
3. **S3 is the real destination.** The file becomes an object; everything downstream (events, Lambda, BDA) keys off normal S3 mechanics.
4. **What breaks:** a user mapped to the wrong home directory silently writes to the wrong prefix. Ingestion then processes stale or empty data. Check the user-to-directory mapping first when drops "stop arriving."

Decision ladder placement

Data in / ingestion: "data arrives as partner file drops over SFTP/FTPS/AS2" = Transfer Family.

:::exam-ask

Scenario: "A healthcare partner must upload claim files nightly using their existing SFTP client. Files must land in S3 and trigger document processing." Correct: Transfer Family SFTP server with an S3 backend plus S3 event notifications. Distractors: DataSync (agent-based migration, not a protocol server), AppFlow (SaaS, not file protocols).
:::

A supplier will send inventory CSVs using plain FTP and cannot change their client. The files must be stored in Amazon S3 inside a private VPC, and each upload must trigger a Lambda function for validation. Which architecture works?

1. A Transfer Family server with the FTP protocol on a VPC-internal endpoint, S3 backend, and S3 event notifications to Lambda.
2. A Transfer Family server with the FTP protocol on a public endpoint and an S3 backend.
3. An EC2-hosted FTP server with a cron job copying files to S3.
4. Amazon AppFlow with an FTP connector writing to S3.

A is correct. Plain FTP is only supported on VPC-internal endpoints, the S3 backend stores the files, and S3 events trigger Lambda.

B is wrong because public endpoints do not support plain FTP. C is wrong because it reintroduces server management that Transfer Family eliminates. D is wrong because AppFlow connects to SaaS APIs, not file-transfer protocols.

## 2. Analytics gaps: QuickSight, Neptune Analytics, Q Apps {#2-analytics-gaps-quicksight-neptune-analytics-q-apps}

Three services that sit at the ends of the GenAI pipeline: analytics over vector/graph data, dashboards over everything, and no-code apps for the people who will never read this guide.

### Amazon QuickSight {#quicksight}

#### What it is {#what-it-is}

Amazon QuickSight is a serverless business-intelligence (BI) service: interactive dashboards, paginated reports, and embedded analytics with no servers to manage. Its in-memory engine is called SPICE (Super-fast Parallel In-memory Calculation Engine), which imports data and answers dashboard queries from memory instead of hitting the source database on every click.

#### Why it exists {#why-it-exists}

GenAI applications produce data worth watching: token spend per team, eval scores over time, RAG retrieval hit rates, user feedback. Engineers query that data in Athena or OpenSearch, but product owners and finance need dashboards. QuickSight turns the same S3/Athena/Redshift/RDS data into shareable dashboards with row-level security (each viewer sees only their rows) and ML-powered insights (anomaly detection and forecasting) without standing up a BI server.

#### How it works {#how-it-works}

1. Connect a data source (S3, Athena, Redshift, RDS, SaaS via AppFlow) and either query it directly or import it into SPICE for fast repeated queries.
2. Build analyses with drag-and-drop visuals, then publish them as dashboards.
3. Add ML insights: anomaly detection flags unusual spend spikes; forecasting projects next month's token usage; natural-language Q lets users type a question and get a chart.
4. Share with row-level and column-level security so teams see only their data. Dashboards can also be embedded into your own application.
5. **Editions.** Standard is the basic tier; Enterprise adds the ML insights, row/column-level security, and encryption at rest. Exam scenarios that mention anomaly detection or per-team data isolation are pointing at Enterprise.

#### Concrete numbers {#concrete-numbers}

SPICE capacity is sold in GB blocks (illustrative: tens of cents per GB-month); per-reader pricing is session-based on Enterprise. The exam does not test exact figures. The operational number that matters: SPICE datasets refresh on a schedule you set (as frequent as every 15 minutes on Enterprise), so a "near real-time dashboard" scenario needs direct query mode, not SPICE import.

:::takeaway

Key exam facts.

(1) QuickSight = serverless BI; SPICE = in-memory engine. (2) Enterprise edition adds ML insights (anomaly detection, forecasting), natural-language Q, and row/column-level security. (3) Direct query mode for fresher data; SPICE for speed.
:::

:::exam-ask

Trap.

AWS will offer OpenSearch Dashboards as the distractor for log analytics and QuickSight as the distractor for log analytics. The split: OpenSearch Dashboards visualizes data already in OpenSearch (logs, traces); QuickSight aggregates business data across many sources (S3, Athena, Redshift) with governed sharing. "Dashboard of monthly Bedrock spend per team from CUR data in S3" is QuickSight.
:::

```
  S3 (CUR billing) --\
  Athena (eval logs) ---> QuickSight --SPICE import--> dashboard: spend/team, eval trend
  Redshift (usage)  ---/                    |
                                            +-- anomaly detection: spend spike alert
                                            +-- RLS: team A sees only team A rows
```

Figure 2.1. QuickSight aggregates GenAI operational data from several sources into one governed dashboard. SPICE keeps repeated views fast; ML insights watch for anomalies automatically.

How to read this diagram

1. **Left: the raw sources.** Billing data, evaluation logs, and usage tables. None of them is dashboard-shaped.
2. **Middle: QuickSight + SPICE.** Import once, query from memory many times. Direct query is the alternative when data must be minutes fresh.
3. **Right: the outputs.** Dashboards for humans, anomaly alerts for operations, row-level security for governance.
4. **What breaks:** a stale SPICE refresh schedule makes the dashboard confidently wrong. When numbers look off, check the dataset refresh time before questioning the pipeline.

Decision ladder placement

Ops: "governed dashboards and reports over GenAI operational data" = QuickSight.

:::exam-ask

Scenario: "Finance needs a monthly dashboard of Bedrock token spend per department, with each department seeing only its own data, plus automatic alerts on unusual spikes." Correct: QuickSight Enterprise (row-level security + anomaly detection). Distractors: OpenSearch Dashboards (wrong data shape), CloudWatch dashboards (no governed multi-team sharing).
:::

A company stores Bedrock invocation logs in Amazon S3 and wants business users to explore token usage by team through interactive dashboards, with each team restricted to its own rows and automatic detection of unusual cost spikes. Which solution fits?

1. Amazon OpenSearch Service with OpenSearch Dashboards.
2. Amazon QuickSight Enterprise with SPICE, row-level security, and ML insights.
3. Amazon CloudWatch dashboards with metric math.
4. Amazon Athena with saved queries shared by email.

B is correct. QuickSight Enterprise provides interactive dashboards over S3 data, row-level security for per-team isolation, and anomaly detection for spike alerts.

A is wrong because OpenSearch Dashboards visualizes OpenSearch indices, not S3 billing-style data with governed sharing. C is wrong because CloudWatch dashboards lack row-level security and business-user exploration. D is wrong because saved queries are not interactive dashboards with access control.

### Neptune Analytics {#neptune-analytics}

#### What it is {#what-it-is}

Neptune Analytics is a serverless graph-analytics engine from the Amazon Neptune family. It loads graph data into memory and runs analytical queries over it, including vector similarity search. Do not confuse it with Neptune Database (the transactional graph database covered in D1 ch11 for GraphRAG): Neptune Analytics is the analytics engine you point at a graph when you need fast traversals and nearest-neighbor vector queries over millions of nodes.

#### Why it exists {#why-it-exists}

GraphRAG (retrieval over a knowledge graph, D1 ch11) works well on Neptune Database for transactional workloads. But some questions are analytical: "find the 50 most similar incident reports to this one," "detect communities of related entities." Those need an engine optimized for bulk graph computation and vector search, not for single-record reads and writes. Neptune Analytics fills that slot, and its vector search makes it a candidate vector store for RAG pipelines that also need graph structure.

#### How it works {#how-it-works}

1. You create a graph and load data (from S3 or from a Neptune Database snapshot). The graph holds nodes, edges, and vector properties.
2. Vector search uses HNSW (Hierarchical Navigable Small World), an approximate nearest-neighbor index that trades a tiny accuracy loss for large speedups on big vector sets.
3. You query vectors with the `vectors.topK.byEmbedding` API, passing an embedding and asking for the top K most similar vectors. **The older name `vectors.topKByEmbedding` is deprecated.** The exam may show the old name as a distractor.
4. **Vector dimensions are fixed at graph creation** (up to 65,000 dimensions) and cannot be changed afterward. If your embedding model changes dimension, you create a new graph.
5. Because it is serverless and in-memory, you pay for the graph's memory footprint while it runs, not for provisioned instances.

#### Concrete numbers {#concrete-numbers}

Maximum vector dimension at graph creation: 65,000. HNSW search is approximate: expect recall in the high 90s percent range in exchange for millisecond queries over millions of vectors (illustrative; tune the HNSW parameters for your recall target). The deprecated API name is the highest-value fact on this page: AWS loves deprecation-rename questions.

:::takeaway

Key exam facts.

(1) Neptune Analytics = serverless graph-analytics engine with vector search (HNSW). (2) Current vector API:

vectors.topK.byEmbedding

; the old

vectors.topKByEmbedding

is deprecated. (3) Vector dimensions are set at creation (max 65,000) and immutable after.
:::

:::exam-ask

Trap.

Two traps here. First, the deprecated API name

topKByEmbedding

will appear as an answer choice; the current name is

topK.byEmbedding

. Second, Neptune Analytics vs. Neptune Database: "transactional graph with ACID writes" is the Database; "in-memory analytics and vector similarity over a loaded graph" is Analytics.
:::

```
  Neptune Database            Neptune Analytics (serverless, in-memory)
  (transactional)             +------------------------------------------+
  nodes/edges + vectors  -->  |  graph load  -->  HNSW vector index       |
  ACID writes                 |  query: vectors.topK.byEmbedding(emb, k) |
  GraphRAG lookups            |  dims fixed at creation (max 65,000)      |
                              +------------------------------------------+
                              analytic queries: similarity, communities
```

Figure 2.2. Neptune Database serves transactional graph reads and writes; Neptune Analytics loads the graph into memory for analytical vector and traversal queries. Pick by workload shape, not by brand.

How to read this diagram

1. **Left: the database.** Optimized for writes and point reads. This is the D1 ch11 GraphRAG home.
2. **Arrow: load, not replicate.** Analytics loads a snapshot of the graph into memory. It is not a live transactional replica.
3. **Right: the analytics engine.** HNSW gives fast approximate vector search; the API name and the immutable-dimension rule are the exam facts.
4. **What breaks:** switching embedding models (for example 768-dim to 1536-dim) silently breaks vector search until you recreate the graph with the new dimension. Dimension mismatch is the first thing to check.

Decision ladder placement

Model / retrieval: "graph analytics plus vector similarity at scale" = Neptune Analytics; "transactional graph RAG" = Neptune Database.

:::exam-ask

Scenario: "An application needs approximate nearest-neighbor vector search over a large knowledge graph, queried with

vectors.topK.byEmbedding

." Correct: Neptune Analytics. Distractors: Neptune Database (transactional, not the vector API), OpenSearch Service (vector search but no graph analytics).
:::

A team runs nightly analytics over a knowledge graph with 40 million nodes, finding similar entities via vector search. They call `vectors.topKByEmbedding` and plan to change the embedding dimension next quarter without recreating the graph. What should they change?

1. Nothing; both the API call and the dimension plan are valid.
2. Use `vectors.topK.byEmbedding` instead, and plan to recreate the graph when the dimension changes.
3. Move the workload to Neptune Database and keep the current API name.
4. Keep the API name but increase the HNSW recall parameter to allow dimension changes.

B is correct. `topKByEmbedding` is deprecated in favor of `topK.byEmbedding`, and vector dimensions are immutable after graph creation, so a dimension change requires a new graph.

A is wrong because the API name is deprecated and dimensions cannot change in place. C is wrong because Neptune Database is the transactional engine, not the analytics vector API. D is wrong because HNSW tuning affects recall, not dimension mutability.

### Amazon Q Apps {#q-apps}

#### What it is {#what-it-is}

Amazon Q Apps are reusable, no-code generative AI applications built inside Amazon Q Business. A non-technical user describes what they want in natural language (or starts from an existing Q Business conversation), and Q generates an app made of cards: input cards (text, file upload), output cards (generated text), and action cards (calls to plugins). Cards reference each other with `@` mentions, so the output of one card becomes the input of the next. Finished apps are published to the organization's app library for anyone to use.

#### Why it exists {#why-it-exists}

Q Business gives every employee a chat assistant, but chat is ephemeral: the same good prompt gets retyped every week. Q Apps turn a useful conversation into a durable tool. The marketing team builds a "campaign brief generator" once; the whole team reuses it. IT keeps control because Q Apps inherit Q Business governance: admin guardrails, Identity Center access control, and connector permissions apply automatically.

#### How it works {#how-it-works}

1. A user describes the app in natural language, or converts a Q Business conversation into an app.
2. Q generates a set of cards. Typical cards: a text-input card ("paste the meeting notes"), a file-upload card, a text-output card ("summary"), and an action card that calls a plugin (for example, creating a Jira ticket).
3. Cards are wired together with `@` mentions: the summary card references the input card, the Jira card references the summary card.
4. The app is published to the organization library. Colleagues run it without seeing or editing the underlying prompts.
5. Access and guardrails come from Q Business itself: the app can only reach data the user is permitted to see, and admin guardrails apply to its outputs. Q Apps are part of the Q Business Pro tier.

#### Concrete numbers {#concrete-numbers}

Q Apps are licensed through Q Business Pro (per-user per-month, illustrative). There is no infrastructure number to memorize; the exam-relevant facts are the card model, the `@` wiring, library sharing, and governance inheritance.

:::takeaway

Key exam facts.

(1) Q Apps = no-code GenAI apps inside Q Business (Pro tier). (2) Built from natural language or an existing conversation. (3) Card model: input, output, file upload, action/plugin cards wired with

@

mentions. (4) Shared via the organization app library. (5) Inherits Q Business governance (guardrails, Identity Center, connector permissions).
:::

:::exam-ask

Trap.

AWS will confuse Q Apps with Q Developer and with Bedrock Agents. Q Developer is the coding assistant for developers; Bedrock Agents are developer-built autonomous agents with action groups and Lambda. Q Apps are for non-developers, built in natural language, with no code and no Lambda. "The HR team wants a reusable leave-policy Q and A tool they build themselves" is Q Apps, not an agent.
:::

```
  natural language description
        |
        v
  +-----------+   @input    +-----------+   @summary   +-----------+
  | input     | ---------> | text      | -----------> | action    |
  | card      |             | output    |              | card      |
  | (notes)   |             | (summary) |              | (Jira     |
  +-----------+             +-----------+              |  ticket)  |
                                                       +-----------+
  published to org app library; Q Business guardrails + permissions apply
```

Figure 2.3. A Q App is a chain of cards wired with @ mentions. The user fills the input card; each downstream card runs in turn; the finished app is shared like a template, not like code.

How to read this diagram

1. **Top: the starting point.** A sentence, not a codebase. That is the whole audience distinction.
2. **Middle: the card chain.** Each card does one job; `@` mentions are the wiring. Data flows left to right, one card feeding the next.
3. **Bottom: the sharing and safety story.** The library makes it reusable; Q Business governance makes it safe. Both are automatic, not built by the app author.
4. **What breaks:** if a card references data the runner cannot access, the app fails at that card with a permissions error, because connector permissions follow the user, not the app author.

Decision ladder placement

App: "non-developers need a reusable GenAI tool they build themselves" = Q Apps.

:::exam-ask

Scenario: "The support team wants to turn their best troubleshooting conversation into a reusable tool the whole team can run, without writing code, respecting existing data permissions." Correct: Amazon Q Apps. Distractors: Bedrock Agents (developer-built, code), Q Developer (coding assistant).
:::

A company's HR staff wants a reusable tool that takes a pasted policy excerpt and produces a plain-language summary, built without developer help and shared with the whole HR department under existing access controls. Which service fits?

1. Amazon Bedrock Agents with an action group.
2. Amazon Q Apps published to the organization library.
3. Amazon Q Developer with custom rules.
4. A Bedrock Knowledge Base with a custom frontend.

B is correct. Q Apps are no-code, built in natural language from a conversation, shared via the library, and inherit Q Business governance.

A is wrong because agents are developer-built with code and Lambda actions. C is wrong because Q Developer assists with coding, not HR workflows. D is wrong because a Knowledge Base needs a custom frontend built by developers.

## 3. Security and inference primitives {#3-security-and-inference-primitives}

The guards around your app and the dials inside your model calls. Each entry here is small, but AWS tests them as single-line discriminators: one phrase in the question picks the winner.

### AWS Secrets Manager {#secrets-manager}

#### What it is {#what-it-is}

AWS Secrets Manager stores secrets (database passwords, API keys, OAuth tokens) encrypted with KMS, and its headline feature is automatic rotation: it can change a secret on a schedule without human involvement and without breaking the applications that read it. The companion service D3 ch8 covers is IAM and KMS; Secrets Manager is the secrets lifecycle layer on top.

#### Why it exists {#why-it-exists}

Hardcoded credentials leak; manually rotated passwords get skipped. Rotation is operationally scary because changing a password breaks every client holding the old one. Secrets Manager solves this with a staged rotation: the new password is created and tested while the old one still works, and only then does the new one become current. Applications read the secret at runtime through the API instead of embedding it.

#### How it works {#how-it-works}

1. **Rotation schedule.** You set a rotation interval, for example every 30 days (`rotate-secret --rotation-rules AutomaticallyAfterDays=30`).
2. **Lambda rotation function.** Rotation is performed by a Lambda function. AWS provides ready-made rotation functions for RDS (MySQL, PostgreSQL, Oracle, SQL Server), Redshift, DocumentDB, Neptune, and MongoDB Atlas; anything else uses a custom Lambda you write.
3. **The four steps.** Every rotation runs `createSecret` (generate the new value, staged as AWSPENDING), `setSecret` (set it on the database), `testSecret` (verify the new credential works), `finishSecret` (promote AWSPENDING to AWSCURRENT). If any step fails, the old secret stays current and nothing breaks.
4. **Reading.** Applications call `GetSecretValue` (or use the Secrets Manager JDBC driver / container injection) and cache briefly. Because rotation is staged, a reader that fetched the secret seconds before rotation still holds a valid credential.

#### Concrete numbers {#concrete-numbers}

Rotation intervals are commonly 30, 60, or 90 days; the API accepts any day count. Secrets Manager charges per secret per month plus API calls (illustrative). The exam tests the four-step sequence and the staging labels AWSPENDING and AWSCURRENT, not the price.

:::takeaway

Key exam facts.

(1) Automatic rotation via Lambda functions with create, set, test, finish steps. (2) Staging labels AWSPENDING (new, being tested) and AWSCURRENT (live). (3) Built-in rotation for RDS engines, Redshift, DocumentDB, Neptune, MongoDB Atlas; custom Lambda for the rest. (4) Secrets are KMS-encrypted at rest.
:::

:::exam-ask

Trap.

The distractor is always SSM Parameter Store. Parameter Store (even Advanced) stores parameters cheaply but has no built-in rotation engine for databases; the phrase "automatically rotate the database password every 30 days" is Secrets Manager. A second trap: rotation changes the secret on the database too (setSecret), not just the stored copy.
:::

```
  rotation trigger (30d)
        |
        v
  createSecret --> setSecret --> testSecret --> finishSecret
   AWSPENDING      (DB updated)   (login test)   AWSPENDING -> AWSCURRENT
        |                                                     ^
        +---- on any failure: old secret stays AWSCURRENT ----+
  app reads GetSecretValue at runtime; never embeds the password
```

Figure 3.1. The four-step rotation. The new secret is staged, installed, and tested before promotion; failure at any step leaves the old secret live. Applications are insulated because they read at runtime.

How to read this diagram

1. **Top: the schedule.** Rotation is a cron-like trigger, not a manual runbook.
2. **Middle: the four steps in order.** Create, set, test, finish. The exam may scramble the order; the logic is generate, install, verify, promote.
3. **The failure path.** The arrow back means safety: a failed rotation is a no-op for the application, not an outage.
4. **Bottom: the application contract.** Read at runtime. Anything embedding the password defeats the whole design.
5. **What breaks:** a custom rotation Lambda missing the test step can promote a credential that does not work on the database. Always include all four steps.

Decision ladder placement

Ops / security: "rotate credentials automatically without downtime" = Secrets Manager. Home context: D3 ch8 (IAM/KMS).

:::exam-ask

Scenario: "An application connects to RDS PostgreSQL. The password must rotate every 30 days with no application downtime and no custom credential code." Correct: Secrets Manager with automatic rotation using the built-in RDS rotation Lambda. Distractors: SSM Parameter Store (no rotation engine), manual rotation via CLI.
:::

A GenAI service reads its database password from environment variables. Security requires the password to rotate every 30 days, with the new password verified working before it goes live, and zero application restarts. Which approach meets all requirements?

1. Store the password in SSM Parameter Store and rotate it with a monthly runbook.
2. Store the password in AWS Secrets Manager with automatic rotation; the application reads it at runtime via GetSecretValue.
3. Store the password in an S3 object encrypted with KMS and update it monthly.
4. Embed a new password in the application deployment pipeline every 30 days.

B is correct. Secrets Manager rotation stages the new secret as AWSPENDING, tests it, then promotes it to AWSCURRENT, and runtime reads mean no restarts.

A is wrong because Parameter Store has no built-in rotation engine and a runbook is manual. C is wrong because S3 has no rotation or staging semantics. D is wrong because embedding passwords in deployments is the anti-pattern rotation exists to kill.

### AWS WAF {#waf}

#### What it is {#what-it-is}

AWS WAF (Web Application Firewall) filters HTTP requests before they reach your application. You attach a web ACL (access control list) to CloudFront, an Application Load Balancer, API Gateway, or AppSync; the ACL holds rules evaluated in priority order, each ending in an action: Allow, Block, Count (log only), CAPTCHA, or Challenge (silent browser check).

#### Why it exists {#why-it-exists}

Your GenAI app's front door (API Gateway in front of a Bedrock proxy, an ALB in front of the chat UI) faces the internet. SQL injection, cross-site scripting, and bot floods are not GenAI-specific, but a prompt-injection probe campaign looks exactly like a bot flood at the HTTP layer. WAF applies the OWASP Top 10 defenses AWS maintains so your application code does not have to.

#### How it works {#how-it-works}

1. Create a web ACL in the right scope: **CloudFront scope (global) must be created in us-east-1**; Regional scope covers ALB, API Gateway, and AppSync in their own region.
2. Add rules in priority order. The workhorse is the AWS managed rule group `AWSManagedRulesCommonRuleSet`, which covers the OWASP Top 10; add `AWSManagedRulesKnownBadInputsRuleSet`, the SQLi rule group, IP reputation lists, and Bot Control as needed.
3. Choose actions per rule. New rules start in Count mode to observe false positives before switching to Block.
4. WAF logs go to S3, CloudWatch Logs, or Kinesis Data Firehose for analysis; pair with Shield (DDoS, automatic at the edge) for volumetric attacks WAF cannot see.

#### Concrete numbers {#concrete-numbers}

You pay per web ACL per month plus per million requests evaluated (illustrative). The exam-relevant facts are the scope rule (CloudFront ACLs live in us-east-1), the action set, and the managed rule group names, not the price.

:::takeaway

Key exam facts.

(1) Web ACL with priority-ordered rules; actions Allow, Block, Count, CAPTCHA, Challenge. (2) Managed groups:

AWSManagedRulesCommonRuleSet

(OWASP Top 10), KnownBadInputs, SQLi, IP reputation, Bot Control. (3) CloudFront-scope ACLs are created in us-east-1. (4) Start new rules in Count mode.
:::

:::exam-ask

Trap.

AWS will offer Security Groups or NACLs as the "firewall" answer. Those filter at layers 3/4 (IP and port); WAF inspects layer 7 (HTTP bodies, SQLi strings, bot signatures). "Block requests containing SQL injection payloads" can only be WAF. A second trap: creating the CloudFront web ACL in the application's region instead of us-east-1.
:::

```
  internet --> WAF web ACL (priority order) --> CloudFront / ALB / API Gateway
                    |  1. AWSManagedRulesCommonRuleSet -> Block
                    |  2. IP reputation list           -> Block
                    |  3. rate-based rule              -> Block
                    |  4. new custom rule              -> Count (observe first)
                    v
              logs -> S3 / CloudWatch Logs / Firehose
```

Figure 3.2. WAF evaluates rules top to bottom; the first match decides. Managed rule groups carry the OWASP coverage; custom rules start in Count mode to avoid blocking legitimate traffic.

How to read this diagram

1. **Left: untrusted traffic.** Every request passes the ACL before touching your origin.
2. **Middle: priority order is the logic.** Rule 1 runs first; a request matching rule 1 never reaches rule 4. Order managed groups before custom experiments.
3. **Actions escalate.** Count observes, Challenge and CAPTCHA test suspicious clients, Block stops attacks. New rules live in Count until proven.
4. **Bottom: the audit trail.** Blocked-request logs are the evidence for tuning; without logging you cannot tell false positives from real attacks.
5. **What breaks:** a rule in Block mode with an over-broad pattern blocks legitimate users. Symptom: sudden 403 spikes after a rule change. Roll the rule back to Count.

Decision ladder placement

Ops / security: "filter malicious HTTP traffic at layer 7" = WAF, attached to CloudFront or API Gateway.

:::exam-ask

Scenario: "An API Gateway fronting a Bedrock proxy receives SQL injection probes and credential-stuffing bursts. Block the attacks with minimal custom rules." Correct: WAF web ACL (Regional scope) with the CommonRuleSet and Bot Control managed groups. Distractors: Security Groups (layer 3/4 only), GuardDuty (detection, not blocking).
:::

A CloudFront distribution serves a GenAI chat application. The team wants AWS-managed protection against OWASP Top 10 attacks and bot traffic, with the ability to observe a new custom rule before it blocks anyone. Where and how should they configure this?

1. Create a WAF web ACL in us-east-1 with CloudFront scope, add AWSManagedRulesCommonRuleSet and Bot Control, and set the new custom rule to Count.
2. Create a WAF web ACL in the application's region with Regional scope and attach it to the distribution.
3. Add IP-based rules to the CloudFront origin's security group.
4. Enable AWS Shield Advanced on the distribution.

A is correct. CloudFront-scope ACLs must be created in us-east-1, the managed groups cover OWASP Top 10 and bots, and Count mode observes before blocking.

B is wrong because CloudFront requires the us-east-1 (global) scope, not Regional. C is wrong because security groups cannot inspect HTTP payloads. D is wrong because Shield protects against DDoS, not application-layer attacks.

### Amazon CloudFront {#cloudfront}

#### What it is {#what-it-is}

Amazon CloudFront is AWS's content delivery network (CDN): a global network of edge locations (points of presence) that cache content close to users. A distribution is the CloudFront configuration mapping your domain to origins (S3 buckets, load balancers, API Gateway) with cache behaviors (path-pattern rules controlling what is cached and for how long).

#### Why it exists {#why-it-exists}

Users are far from your origin region; every request crossing an ocean adds latency. CloudFront serves cache hits from the nearest edge in milliseconds and routes cache misses over the AWS backbone, which is faster than the public internet. For GenAI apps it also terminates TLS at the edge, absorbs DDoS with Shield Standard, and hosts WAF inspection before traffic reaches your API.

#### How it works {#how-it-works}

1. A viewer requests `app.example.com/chat`. DNS routes them to the nearest edge location.
2. Cache behaviors match the path: `/static/*` might cache for a day from S3; `/api/*` might forward to API Gateway with no caching.
3. Cache hit: the edge answers immediately. Cache miss: the edge fetches from the origin once, stores it per the TTL, and serves it.
4. **Private S3 origins use OAC.** Origin Access Control lets CloudFront authenticate to a private bucket via the bucket policy. The older OAI (Origin Access Identity) is legacy. Note: OAC works with the S3 REST endpoint, not the S3 website endpoint.
5. **Signed URLs vs signed cookies.** A signed URL grants access to one file; signed cookies grant access to many files (for example a whole premium video course). Geo restriction blocks or allows whole countries at the edge.
6. **Custom-domain certificates must be in us-east-1** (ACM), because CloudFront is a global service, exactly like the WAF scope rule above.

#### Concrete numbers {#concrete-numbers}

Default TTLs are measured in hours to a day (configurable per behavior); invalidations clear cached objects before TTL expiry and are the "I deployed a fix but users see the old page" answer. Edge count is in the hundreds across 90+ countries (illustrative; the exam tests concepts, not the count).

:::takeaway

Key exam facts.

(1) Distributions map domains to origins with path-based cache behaviors. (2) OAC is the current private-S3 mechanism; OAI is legacy. (3) Signed URL = one file; signed cookies = many files. (4) ACM certificate for CloudFront lives in us-east-1. (5) Shield Standard is included; WAF attaches at the edge.
:::

:::exam-ask

Trap.

The OAC-vs-OAI trap: any answer choice using Origin Access Identity for a new design is wrong; OAC is current. The signed-URL-vs-cookie trap: one premium file is a signed URL; a library of premium files is signed cookies. The us-east-1 trap appears for both WAF and ACM certificates.
:::

```
  user --> nearest edge: cache hit? --yes--> serve (ms)
                            |
                            no
                            v
                     origin via OAC (private S3)
                     or ALB / API Gateway (dynamic)
                            |
                     edge caches per behavior TTL, then serves
  WAF web ACL (us-east-1) inspects here; Shield Standard absorbs DDoS
```

Figure 3.3. The CloudFront request path. Edge caching, origin fetch on miss, and security (WAF, Shield) all happen before your origin sees the request.

How to read this diagram

1. **Top: the happy path.** A cache hit never touches your origin; that is the latency and cost win.
2. **The miss path.** One origin fetch serves all later users until TTL expiry. Stale content after a deploy means the TTL or an invalidation, not a bug.
3. **The origin line.** OAC is how a private S3 bucket trusts CloudFront; dynamic origins (ALB, API Gateway) get acceleration even without caching.
4. **The security line.** WAF and Shield sit at the edge, so attacks are filtered close to the attacker, far from your origin.
5. **What breaks:** forwarding too many headers or cookies to the origin fragments the cache into per-user copies and the hit ratio collapses. Cache on as little as possible.

Decision ladder placement

Ops / delivery: "serve content globally with low latency and edge security" = CloudFront.

:::exam-ask

Scenario: "A GenAI chat UI's static assets must load fast worldwide from a private S3 bucket, with bot protection and HTTPS on a custom domain." Correct: CloudFront distribution with OAC to the private bucket, WAF attached, ACM certificate in us-east-1. Distractors: S3 static website hosting alone (no edge caching, no WAF), Global Accelerator (TCP/UDP acceleration, not HTTP caching).
:::

A team serves premium tutorial videos from a private S3 bucket through CloudFront. Paying users should access the whole library after login; the bucket must never be public. Which combination is correct?

1. OAC with a bucket policy allowing the distribution, plus signed cookies for authenticated users.
2. OAI with the bucket made public, plus a signed URL per video.
3. S3 static website endpoint as the origin with OAC, plus IP allowlisting.
4. CloudFront with the bucket public and signed URLs generated per user session for each video.

A is correct. OAC is the current mechanism for private S3 origins, and signed cookies cover many files with one authentication, which fits a library.

B is wrong because OAI is legacy and the bucket must not be public. C is wrong because OAC does not work with the S3 website endpoint. D is wrong because the bucket must not be public and per-video signed URLs are the wrong tool for library-wide access.

### The CountTokens API {#counttokens}

#### What it is {#what-it-is}

CountTokens is a Bedrock runtime API (`POST /model/{modelId}/count-tokens`) that returns the number of tokens a given input would consume, without running inference. It accepts the same input formats as `InvokeModel` and `Converse`, and the count it returns matches what you would be billed for. It is free to call.

#### Why it exists {#why-it-exists}

D4 teaches token-efficient design: prompt caching, context pruning, maxTokens limits. But every one of those techniques needs a measurement step first. Before CountTokens, teams estimated tokens with client-side tokenizers that drifted from the model's real tokenizer, so cost projections and "will this fit in context" checks were unreliable. CountTokens gives the authoritative number from the service itself.

#### How it works {#how-it-works}

1. Send the same request body you would send to `InvokeModel` or `Converse`, but to the `count-tokens` endpoint.
2. The response returns the input token count. No tokens are generated, no inference runs, no charge accrues.
3. Use it to validate that a RAG prompt fits the model's context window before the call, to project batch-job cost, and to measure whether a prompt-compression change actually saved tokens.
4. **Careful with model identifiers.** Community reports indicate CountTokens can reject inference-profile model IDs that `InvokeModel` accepts; when in doubt, test with the base model ID. UNVERIFIED in official docs; treat as a caution, not a rule.

#### Concrete numbers {#concrete-numbers}

The API is free: zero cost per call. A typical use: a RAG prompt with 8 retrieved chunks at roughly 400 tokens each plus 200 tokens of instructions counts about 3,400 input tokens (illustrative); at a model price of a few dollars per million input tokens, 10,000 such calls cost on the order of a hundred dollars. CountTokens turns that arithmetic from guesswork into a measurement.

:::takeaway

Key exam facts.

(1) CountTokens estimates input tokens without inference, free of charge. (2) It accepts the same formats as InvokeModel/Converse and matches billed tokens. (3) Use it for context-window fit checks and cost projection.
:::

:::exam-ask

Trap.

AWS will offer "estimate with a local tokenizer" or "send a real InvokeModel and read the usage fields" as distractors. Local tokenizers drift from the true count; a real invocation costs money and generates output. CountTokens is the free, exact answer.
:::

```
  prompt candidate --+
                     +--> CountTokens (free) --> 3,412 tokens
  "fits in 8k window?" --yes--> Converse (billed)
                        --no--> prune context, recount (free), then call
```

Figure 3.4. CountTokens as a gate before billed inference. The loop is free until the prompt fits; only the final call costs money.

How to read this diagram

1. **Left: the candidate prompt.** Whatever your RAG pipeline assembled, chunks and all.
2. **Middle: the free gate.** CountTokens answers the fit question without spending anything.
3. **Right: the two exits.** Fits means call the model; does not fit means prune and recount, still free.
4. **What breaks:** skipping the gate on long prompts risks a context-overflow error after you have already paid for the input tokens.

Decision ladder placement

Model / cost: "measure tokens before paying for them" = CountTokens.

:::exam-ask

Scenario: "Before running a 50,000-document batch job, the team must verify each prompt fits the context window and project total cost, without paying for inference." Correct: CountTokens API. Distractors: client-side estimation, running a sample through InvokeModel.
:::

A team wants the exact billed input-token count for a Converse request body before deciding whether to send it, and they want this check to cost nothing. Which API should they call?

1. InvokeModel with maxTokens set to 1.
2. CountTokens on the bedrock-runtime endpoint with the same input format.
3. Converse with a stop sequence that halts immediately.
4. GetModelInvocationLoggingConfiguration.

B is correct. CountTokens accepts the same formats as InvokeModel/Converse, returns the billed token count, runs no inference, and is free.

A is wrong because it still runs inference and incurs charges. C is wrong because it also invokes the model and bills for it. D is wrong because it configures logging, not token counting.

### top_k: the sampling parameter AWS hides from Converse {#topk}

#### What it is {#what-it-is}

top_k is a decoding parameter: at each generation step, the model considers only the k most likely next tokens and samples among them. Small k (for example 10) makes output focused and deterministic; large k (for example 200) allows rarer, more creative tokens. It is the sibling of temperature (randomness scale) and top_p (nucleus sampling over cumulative probability), both taught in D4.

#### Why it exists {#why-it-exists}

Temperature and top_p shape the probability distribution, but sometimes you want a hard cutoff: "never consider anything outside the top 50 candidates, no matter what." top_k gives that cutoff. It is especially useful for constrained tasks like classification or structured extraction, where a long tail of weird tokens is pure risk.

#### How it works, and the exam trap {#how-it-works-and-the-exam-trap}

1. In raw `InvokeModel` request bodies, top_k (usually written `top_k` or `topK` depending on the provider) is a normal provider parameter.
2. **In the Converse API, `inferenceConfig` documents only four fields: `maxTokens`, `stopSequences`, `temperature`, and `topP`. There is no standard `topK` field in Converse `inferenceConfig`.**
3. To set top_k through Converse, you pass it inside `additionalModelRequestFields`, the provider-specific escape hatch, using the provider's own field name. Alternatively, use `InvokeModel` with the raw body.
4. Confusingly, topK *does* exist in the Bedrock Agents `InferenceConfiguration`. Same name, different API, different rules.

#### Concrete numbers {#concrete-numbers}

Typical top_k values range from 1 (greedy within the top candidate, nearly deterministic) to a few hundred (illustrative; provider defaults vary). The operational guidance mirrors top_p: for factual extraction use low top_k with low temperature; for brainstorming use higher values. Do not combine aggressive top_k with aggressive top_p without testing; they interact.

:::takeaway

Key exam facts.

(1) top_k limits sampling to the k most likely tokens. (2) Converse

inferenceConfig

has maxTokens, stopSequences, temperature, topP, and no topK. (3) Provider-specific fields like topK go in

additionalModelRequestFields

or a raw InvokeModel body. (4) Bedrock Agents

InferenceConfiguration

does include topK.
:::

:::exam-ask

Trap.

This is a purpose-built exam trap: a question will show a Converse call with

inferenceConfig: {topK: 50}

and ask why it fails or which field is invalid. The answer is that topK is not a valid

inferenceConfig

member. A second trap swaps in the Agents API, where topK is valid, to punish memorization without context.
:::

```
  Converse API
  inferenceConfig: { maxTokens, stopSequences, temperature, topP }   <- topK NOT here
  additionalModelRequestFields: { "top_k": 50 }                      <- topK goes here
  Bedrock Agents InferenceConfiguration: { ..., topK }               <- valid here
```

Figure 3.5. Where topK is and is not allowed. Converse keeps a small standard config and pushes provider specifics into additionalModelRequestFields; the Agents API has its own configuration shape.

How to read this diagram

1. **Line 1: the Converse allowlist.** Four fields. If a question puts anything else inside `inferenceConfig`, it is wrong.
2. **Line 2: the escape hatch.**`additionalModelRequestFields` carries provider-specific parameters using the provider's naming.
3. **Line 3: the lookalike.** Bedrock Agents use a different configuration object where topK is a first-class field. Same word, different contract.
4. **What breaks:** passing `topK` inside Converse `inferenceConfig` is silently ignored or rejected depending on the SDK, so the model runs with default sampling and nobody notices until eval scores drift.

Decision ladder placement

Model / inference: "constrain sampling to top candidates via Converse" = `additionalModelRequestFields`.

:::exam-ask

Scenario: "A developer's Converse call sets

inferenceConfig.topK

but sampling behavior does not change." Correct: topK is not a member of Converse

inferenceConfig

; move it to

additionalModelRequestFields

. Distractors: "increase temperature," "the model does not support topK."
:::

A developer wants deterministic, focused output from a Converse call and writes `inferenceConfig: { "temperature": 0.1, "topK": 10 }`. The call is accepted but the topK setting has no effect. What is the fix?

1. Move topK into `additionalModelRequestFields` using the provider's field name.
2. Increase temperature so topK takes effect.
3. Switch to `topP`; topK is deprecated across Bedrock.
4. Set topK inside `guardrailConfig` instead.

A is correct. Converse `inferenceConfig` supports only maxTokens, stopSequences, temperature, and topP; provider-specific fields like topK belong in `additionalModelRequestFields`.

B is wrong because temperature does not enable topK. C is wrong because topK is not deprecated; it is only absent from that one config object. D is wrong because guardrailConfig controls safety filters, not sampling.

### CloudWatch Evidently {#evidently}

#### What it is {#what-it-is}

CloudWatch Evidently is an experimentation and feature-flag service inside CloudWatch. Feature flags turn features on or off for subsets of users without redeploying; experiments (A/B tests) route traffic between variants and measure which one wins on a chosen metric, with statistical analysis built in. The two key APIs are `EvaluateFeature` (ask which variant a user gets) and `PutProjectEvents` (report the outcome metric).

#### Why it exists {#why-it-exists}

D5 ch7 teaches A/B testing prompts via Prompt Management variants, but that only covers prompt text. Real GenAI experiments vary models, retrieval depth, temperature, or whole pipelines, and they need traffic splitting plus statistics. Evidently provides both: the application calls `EvaluateFeature` per request to pick variant A or B, then reports the result (user thumbs-up, task success) with `PutProjectEvents`, and Evidently computes whether B beats A significantly.

#### How it works {#how-it-works}

1. Define a feature with variations (for example, `model: claude-haiku` vs `model: claude-sonnet`, or `topK: 10` vs `topK: 50`).
2. Define an experiment: what fraction of traffic goes to each variation, and which metric decides the winner (for example, user satisfaction events).
3. At request time the app calls `EvaluateFeature` with the user identity and gets back the assigned variation plus the variation's configuration values.
4. The app runs the request with those values, then calls `PutProjectEvents` with the outcome.
5. Evidently aggregates and reports statistical significance. When the experiment concludes, the winning variation becomes the default; the flag mechanism also supports plain gradual rollouts with no experiment attached.

#### Concrete numbers {#concrete-numbers}

Evidently pricing is per evaluation and per event (illustrative; small). The numbers that matter are experimental: run enough traffic that the result is statistically significant, which Evidently computes for you. A common exam scenario splits 90/10 (safe default vs. challenger) to limit blast radius.

:::takeaway

Key exam facts.

(1) Evidently = feature flags + A/B experiments with built-in statistics. (2)

EvaluateFeature

assigns the variant;

PutProjectEvents

reports the metric. (3) Works for any variation: models, prompts, retrieval settings, not just prompt text.
:::

:::exam-ask

Trap.

AWS will offer "deploy two Lambda versions and compare CloudWatch dashboards by eye" as the distractor. Eyeballing dashboards is not an experiment: no randomization, no significance. The phrase "statistically significant" or "which variant wins" points to Evidently. A second trap: Prompt Management variants are for prompt text; model or pipeline A/B tests need Evidently.
:::

```
  user request --> EvaluateFeature(user) --> variant A (90%): haiku, topK 10
                                          \-> variant B (10%): sonnet, topK 50
  each request runs its variant, then PutProjectEvents(outcome: satisfied?)
                                          |
                                          v
                              Evidently: B wins, p significant
                                          --> promote B to default
```

Figure 3.6. The Evidently experiment loop. Assignment is per request and sticky per user; outcomes flow back as events; statistics decide the winner.

How to read this diagram

1. **Top: the assignment.**`EvaluateFeature` is called per request; the same user consistently gets the same variant.
2. **Middle: the execution.** Each variant is a full configuration (model, parameters), not just a prompt string.
3. **The feedback arrow.**`PutProjectEvents` closes the loop; without outcome events there is no experiment, only a rollout.
4. **Bottom: the decision.** Statistics, not dashboards-eyeballing, promote the winner.
5. **What breaks:** reporting outcomes for only one variant (for example, logging errors only on B) biases the statistics. Instrument both arms identically.

Decision ladder placement

Ops / experimentation: "A/B test models or pipelines with statistical significance" = Evidently.

:::exam-ask

Scenario: "Route 10% of chat traffic to a new model and measure which model gets higher user satisfaction with statistical confidence." Correct: Evidently experiment with

EvaluateFeature

and

PutProjectEvents

. Distractors: two CloudWatch dashboards compared manually, Prompt Management variants (prompt text only).
:::

A team wants to test whether a larger model improves task success rate. They will send 10% of production traffic to the larger model, measure success per request, and need a statistically valid winner. Which service and API pair implements this?

1. CloudWatch Evidently; `EvaluateFeature` for assignment and `PutProjectEvents` for outcomes.
2. AWS AppConfig; `GetConfiguration` for assignment and manual dashboard comparison.
3. Bedrock Prompt Management; prompt variants compared by eye in CloudWatch.
4. Lambda aliases with weighted routing and X-Ray sampling.

A is correct. Evidently is the purpose-built A/B testing service: `EvaluateFeature` assigns variants per request and `PutProjectEvents` feeds the outcome metric into statistical analysis.

B is wrong because AppConfig does gradual rollouts without experiment statistics. C is wrong because prompt variants cover prompt text, not model selection, and eyeballing is not statistical. D is wrong because weighted aliases split traffic but provide no experiment framework.

### TTFT: time to first token {#ttft}

#### What it is {#what-it-is}

TTFT (time to first token) is the latency from the moment your request is sent until the first token of the response arrives. It is the metric users actually feel in a streaming chat: the pause before text starts appearing. Its siblings: TPOT (time per output token, the steady streaming rate after the first token) and end-to-end latency (TTFT plus everything after).

#### Why it exists {#why-it-exists}

D4 ch6 teaches streaming to improve perceived latency, but "streaming helps" is not measurable without naming the metric. TTFT isolates the painful part (prefill: processing your whole prompt before generating anything) from the cheap part (decoding one token at a time). Amazon Bedrock emits TTFT as a native CloudWatch metric, so you can alarm on it, which turns "the app feels slow" into a graph.

#### How it works {#how-it-works}

1. Use a streaming API: `ConverseStream` or `InvokeModelWithResponseStream`. TTFT is only meaningful for streaming; non-streaming calls have a single end-to-end latency.
2. Bedrock publishes `TimeToFirstToken` to the `AWS/Bedrock` CloudWatch namespace (alongside `InvocationLatency`, which covers all invocations). No code changes or opt-in are required.
3. What drives TTFT up: long prompts (the whole prompt is processed before the first token), large models, cold provisioned throughput, and queueing under throttling. What drives it down: shorter prompts, prompt caching (cached prefix skips recomputation), smaller/faster models, streaming.
4. Set CloudWatch alarms on p95 TTFT so regressions page someone instead of silently annoying users.

#### Concrete numbers {#concrete-numbers}

Illustrative magnitudes: a short prompt on a fast model can show TTFT in the hundreds of milliseconds; a 100k-token prompt can push TTFT into many seconds, because prefill work grows with prompt length. The exam tests the concept and the metric name, not specific millisecond values.

:::takeaway

Key exam facts.

(1) TTFT = request sent to first token received; streaming only. (2) Bedrock emits

TimeToFirstToken

in CloudWatch (

AWS/Bedrock

);

InvocationLatency

covers all calls. (3) Long prompts are the dominant TTFT driver; prompt caching and shorter context reduce it.
:::

:::exam-ask

Trap.

AWS will conflate TTFT with end-to-end latency or with TPOT. "Reduce the time until the user sees the first word" is TTFT; "increase tokens per second during streaming" is TPOT; "the whole request took 8 seconds" is end-to-end. A second trap: applying TTFT reasoning to non-streaming

Converse

calls, where the metric does not exist.
:::

```
  request sent --[prefill: whole prompt processed]--> first token --> token --> token ...
               |<-------------- TTFT ---------------->|
               |<----- TPOT ---->|<----- TPOT ------->|
               |<------------------- end-to-end -------------------->|
  long prompt stretches the prefill block; caching shrinks it
```

Figure 3.7. The three latency metrics on one timeline. TTFT covers the prefill wait; TPOT covers the streaming rate; end-to-end covers everything.

How to read this diagram

1. **The prefill block.** Everything before the first token: the model reads your entire prompt. This is where TTFT lives and where long prompts hurt.
2. **The token chain.** After the first token, each token arrives at the TPOT rate. Users perceive this as typing speed.
3. **The brackets.** Each metric covers a different span; optimizing TPOT does not fix a TTFT problem and vice versa.
4. **What breaks:** a RAG pipeline that stuffs 50 chunks into the prompt shows fine TPOT but terrible TTFT. The fix is fewer, better chunks (D1 ch13), not a faster model.

Decision ladder placement

Model / performance: "measure and alarm on streaming responsiveness" = TTFT via the `TimeToFirstToken` metric.

:::exam-ask

Scenario: "Users complain the chat takes too long to start responding, though text streams fine once it starts. The team needs a CloudWatch metric to alarm on." Correct:

TimeToFirstToken

in

AWS/Bedrock

. Distractors:

InvocationLatency

alone (blends prefill and decode), custom client timers (unnecessary; the metric is native).
:::

A streaming chatbot shows a long pause before the first word appears, but streams quickly afterward. Which metric isolates the problem, and what is the most likely cause?

1. TPOT; the model generates tokens too slowly.
2. TimeToFirstToken; the prompt is long and prefill dominates.
3. InvocationLatency; the network is slow.
4. InputTokenCount; the model context window is full.

B is correct. The pause before streaming starts is TTFT by definition, and long prompts inflate prefill, which is the dominant TTFT driver.

A is wrong because TPOT measures the streaming rate, which the scenario says is fine. C is wrong because InvocationLatency blends the whole call and does not isolate the prefill wait. D is wrong because token count is a volume metric, not a latency metric.

## 4. Data and model mechanics {#4-data-and-model-mechanics}

The unglamorous machinery under the GenAI pipeline: turning documents into text, text into chunks, vectors into smaller vectors, and models into running endpoints.

### Amazon Textract {#textract}

#### What it is {#what-it-is}

Amazon Textract is a managed document-analysis service: it extracts printed text, handwriting, forms (key-value pairs), tables, and layout structure from documents and images, with no model to train. D1 ch9 teaches the ingestion pipeline; this entry teaches the Textract API surface the exam names.

#### Why it exists {#why-it-exists}

RAG needs text, but enterprise knowledge lives in PDFs, scanned contracts, and photographed forms. Plain OCR returns a soup of words; Textract returns structure: which text is a table cell, which words form a key-value pair, where the checkboxes are. That structure is what lets a chunking pipeline keep a table together instead of shredding it across chunks.

#### How it works {#how-it-works}

1. **Synchronous APIs** (single-page documents, immediate response): `DetectDocumentText` for raw OCR (words and lines); `AnalyzeDocument` for structure, with `FeatureTypes` selecting `TABLES`, `FORMS`, `QUERIES` (ask a natural-language question and get an answer pair), `LAYOUT` (titles, headers, lists, reading order), and `SIGNATURES`.
2. **Asynchronous APIs** (multi-page PDFs/TIFFs in S3): `StartDocumentTextDetection` / `StartDocumentAnalysis` return a job ID; results come from `GetDocumentTextDetection` / `GetDocumentAnalysis`, with SNS notification on completion.
3. **Specialized APIs:**`AnalyzeExpense` extracts invoices and receipts into standardized fields (totals, line items); `AnalyzeID` extracts identity documents (passports, driver's licenses) into typed fields.
4. **Output model:** a graph of `Block` objects (PAGE, LINE, WORD, TABLE, CELL, KEY_VALUE_SET, SELECTION_ELEMENT for checkboxes) with bounding boxes, confidence scores, and relationships linking keys to values and tables to cells.
5. **Human review:** route low-confidence results to Amazon A2I (Augmented AI) for human verification, the standard answer for "high-stakes documents."

#### Concrete numbers {#concrete-numbers}

Synchronous calls handle single pages up to a few MB; asynchronous jobs handle multi-page documents up to hundreds of MB from S3 (illustrative; check current quotas). Each feature type adds cost, so request only the `FeatureTypes` you need. Confidence scores are per block; a common A2I threshold routes anything below roughly 90% confidence to humans (illustrative).

:::takeaway

Key exam facts.

(1) Sync:

DetectDocumentText

(OCR) and

AnalyzeDocument

(TABLES/FORMS/QUERIES/LAYOUT/SIGNATURES). (2) Async:

StartDocumentAnalysis

plus

GetDocumentAnalysis

for multi-page S3 documents, SNS on completion. (3) Specialized:

AnalyzeExpense

(invoices),

AnalyzeID

(identity docs). (4) Low confidence goes to A2I human review.
:::

:::exam-ask

Trap.

The sync/async split is the favorite trap:

AnalyzeDocument

on a 200-page PDF fails; multi-page documents require the async

StartDocumentAnalysis

with the document in S3. A second trap: using

AnalyzeDocument

with no

FeatureTypes

when the scenario needs tables; raw OCR does not reconstruct table structure.
:::

```
  single page ---> DetectDocumentText ---> words + lines (raw OCR)
                -> AnalyzeDocument [TABLES, FORMS] ---> blocks: TABLE->CELLs,
                                                        KEY_VALUE_SET pairs
  multi-page PDF in S3 ---> StartDocumentAnalysis ---> job ID
                                                        | (SNS on done)
                                                        v
                                               GetDocumentAnalysis ---> blocks
  invoice scan ---> AnalyzeExpense ---> {total, line items, vendor}
  low confidence blocks ---> A2I human review
```

Figure 4.1. The Textract API decision tree. Page count picks sync vs async; document type picks the specialized API; confidence picks whether humans review.

How to read this diagram

1. **Top: the sync branch.** One page, immediate answer. The `FeatureTypes` list is the dial that buys structure beyond raw text.
2. **Middle: the async branch.** Multi-page documents live in S3, start a job, get notified, then fetch. The job ID is the handle for the whole flow.
3. **The specialized row.** Invoices and IDs get their own APIs because their output schemas are standardized; do not parse them with generic `AnalyzeDocument`.
4. **Bottom: the quality gate.** Confidence scores decide what needs human eyes; A2I is the exam's answer for regulated or high-stakes extraction.
5. **What breaks:** tables shredded across chunks downstream usually trace back to missing `TABLES` in `FeatureTypes`, not to the chunker.

Decision ladder placement

Processing: "extract structured text from documents" = Textract; pipeline home is D1 ch9.

:::exam-ask

Scenario: "Extract key-value pairs and tables from 500-page PDFs stored in S3, with human review for low-confidence fields." Correct:

StartDocumentAnalysis

with

FeatureTypes

TABLES and FORMS, SNS completion, A2I for low confidence. Distractors:

AnalyzeDocument

(sync, wrong for multi-page), Comprehend (NLP on text, not document OCR).
:::

A pipeline must extract tables and form fields from multi-page PDFs in S3 and flag uncertain extractions for human review. Which combination is correct?

1. `DetectDocumentText` on each page, then manual review of all output.
2. `StartDocumentAnalysis` with TABLES and FORMS, `GetDocumentAnalysis` on completion, and A2I for low-confidence blocks.
3. `AnalyzeDocument` called synchronously on the full PDF.
4. Amazon Comprehend custom entities on the PDF bytes.

B is correct. Multi-page S3 documents require the async API, TABLES/FORMS buy the structure, and A2I handles low-confidence review.

A is wrong because raw OCR returns no table or form structure. C is wrong because the sync API does not handle multi-page PDFs. D is wrong because Comprehend analyzes text, it does not perform document OCR.

### Divider strings for chunking {#divider-strings}

#### What it is {#what-it-is}

A divider string is a unique delimiter you insert between logical sections of a document during preprocessing, so that a later split-on-delimiter chunker breaks the text exactly at section boundaries. Example: before chunking, a Lambda preprocessor inserts `\n\n###SECTION###\n\n` between detected headings; the chunker then splits on that marker instead of on blind character counts. UNVERIFIED: this is a course-taught preprocessing technique, not an AWS-documented feature. Treat it as a pattern, not a service.

#### Why it exists {#why-it-exists}

D1 ch13 teaches chunking strategies (fixed-size, hierarchical, semantic). Fixed-size chunking has a failure mode: it can split mid-table, mid-procedure, or mid-argument, producing chunks that confuse retrieval. Divider strings are the cheap fix: one preprocessing pass marks the true boundaries, and the chunker respects them, so each chunk stays semantically whole.

#### How it works {#how-it-works}

1. After Textract or BDA extraction, a Lambda preprocessor scans the text for structural signals (headings, page breaks, table boundaries).
2. It inserts a divider string that never occurs naturally in the text (a random-looking token is safer than a common word).
3. The chunking step splits on the divider first, then applies size limits within each section: sections longer than the target get sub-split; tiny adjacent sections may merge.
4. Each chunk keeps metadata noting its source section, which improves citation and reranking later.

#### Concrete numbers {#concrete-numbers}

Illustrative: with a 512-token target chunk size, divider-first splitting on a 40-page manual typically yields chunks averaging near the target with far fewer mid-sentence breaks than pure fixed-size splitting. There are no AWS quotas here; this is application code, so numbers are illustrative by nature.

:::takeaway

Key exam facts.

(1) Divider strings are inserted during preprocessing to mark true section boundaries. (2) The chunker splits on the divider before applying size limits. (3) Result: semantically whole chunks, better retrieval.
:::

:::exam-ask

Trap.

AWS will offer "smaller fixed-size chunks" as the fix for bad retrieval. Smaller blind chunks just make more fragments; the fix for boundary violations is boundary-aware splitting. The trigger phrase is "chunks split tables/procedures in the middle."
:::

```
  blind fixed-size split:        divider-first split:
  [....procedure A....|....]     [#### procedure A ####]
  [..continuation..|..table..]   [#### table 3      ####]
  [..rest of table....|....]     [#### procedure B ####]
  fragments confuse retrieval    each chunk is one whole unit
```

Figure 4.2. Blind splitting cuts wherever the counter lands; divider-first splitting cuts only at marked boundaries. Retrieval quality follows chunk coherence.

How to read this diagram

1. **Left: the failure.** Vertical bars are cut points landing inside procedures and tables. Each fragment is retrievable but misleading alone.
2. **Right: the fix.**`####` markers were inserted at true boundaries first; cuts happen only there.
3. **The metadata bonus.** Because each chunk maps to one section, citations point at real sections, not "chunk 47 of 200."
4. **What breaks:** a divider string that occurs naturally in the text (like `---`) creates phantom sections. Use a unique, improbable marker.

Decision ladder placement

Processing / retrieval: "chunks must respect document structure" = divider-string preprocessing before chunking (D1 ch13).

:::exam-ask

Scenario: "RAG answers cite table fragments because fixed-size chunking splits tables across chunks." Correct: preprocess with divider strings at table/section boundaries, then split on dividers. Distractors: smaller chunk size, larger chunk overlap.
:::

A RAG system over equipment manuals retrieves table fragments that cut rows in half, hurting answer quality. Fixed-size chunking with 10% overlap is already in place. What change best fixes the fragmentation?

1. Reduce the chunk size and increase overlap.
2. Insert unique divider strings at section and table boundaries during preprocessing, then split on the dividers before applying size limits.
3. Switch to a larger embedding model.
4. Increase the number of retrieved chunks per query.

B is correct. Boundary-aware splitting keeps tables and procedures whole; blind size changes cannot fix boundary violations.

A is wrong because smaller blind chunks create more fragments, not fewer. C is wrong because embeddings do not repair broken chunk boundaries. D is wrong because retrieving more fragments does not make any single fragment coherent.

### Binary vectors and FP16 quantization {#vector-opt}

#### What it is {#what-it-is}

Vector embeddings are usually stored as 32-bit floats (float32): 4 bytes per dimension. Quantization stores them in fewer bits per dimension: binary vectors use 1 bit per dimension (32x smaller), and FP16 scalar quantization uses 16 bits (2x smaller). You trade a small accuracy loss for large memory and cost savings in the vector index.

#### Why it exists {#why-it-exists}

D1 ch11 compares vector stores, but a 1,536-dimension float32 vector costs 6 KB, and ten million of them cost 60 GB of index memory. That memory bill is often the largest line item in a RAG system. Quantization attacks it directly: binary vectors shrink the same index to under 2 GB, which can drop you to a smaller instance class or let you hold the whole index in memory.

#### How it works {#how-it-works}

1. **Binary quantization.** Each float dimension becomes one bit (sign). 32x compression versus float32. Distance becomes Hamming distance, which is extremely fast. Best for large-scale first-pass retrieval where approximate ranking is fine.
2. **2-bit and 4-bit quantization.** Middle grounds at 16x and 8x compression for better accuracy than binary.
3. **FP16 scalar quantization.** Halves memory (2x) with minimal accuracy change. On OpenSearch, `SQfp16` uses the Faiss engine (OpenSearch 2.13 and later); Lucene-based scalar quantization arrived in OpenSearch 2.16.
4. **The standard pattern:** retrieve a larger candidate set with quantized vectors, then rerank the top candidates with full-precision vectors or a reranker model. AWS testing showed accuracy impact around 2% for binary quantization in tested workloads (illustrative; measure on your own data).
5. **OpenSearch neural plugin.** The k-NN and neural search plugin is what enables vector search on Amazon OpenSearch Service in the first place; quantization options are configured on the index's vector field.

#### Concrete numbers {#concrete-numbers}

| Format | Bits per dimension | Compression vs float32 |
|---|---|---|
| float32 | 32 | 1x (baseline) |
| FP16 | 16 | 2x |
| 4-bit | 4 | 8x |
| 2-bit | 2 | 16x |
| binary | 1 | 32x |

:::takeaway

Key exam facts.

(1) Binary = 1 bit/dim, 32x compression; FP16 = 2x. (2) Use quantized vectors for candidate retrieval, then rerank at full precision. (3) OpenSearch: Faiss-engine SQfp16 from 2.13; Lucene scalar quantization from 2.16; neural/k-NN plugin enables vector search.
:::

:::exam-ask

Trap.

AWS will offer "add more nodes" or "move to a bigger instance" for an expensive vector index. The cost-efficient answer is quantization first, scale second. A second trap: claiming quantization is lossless; it is approximate, which is why the rerank step exists.
:::

```
  query vector --> binary index (32x smaller) --> top 200 candidates
                                                        |
                                                        v
                                              rerank with float32
                                              (or reranker model)
                                                        |
                                                        v
                                                   top 10 answers
  memory: 60 GB -> under 2 GB; accuracy cost ~2% (illustrative)
```

Figure 4.3. The two-stage quantized retrieval pattern. Cheap approximate search narrows the field; expensive precise scoring picks the winners.

How to read this diagram

1. **Top: the cheap pass.** The binary index scans the full corpus in a fraction of the memory.
2. **Middle: the candidate set.** 200 is illustrative; the point is "many more than you need," because the cheap pass is approximate.
3. **Bottom: the precise pass.** Full-precision vectors or a reranker score only the candidates, so the expensive work is bounded.
4. **The tradeoff line.** Memory savings are guaranteed; the accuracy cost must be measured on your data, not assumed.
5. **What breaks:** skipping the rerank step ships approximate rankings to users. Quantization without reranking is the common implementation mistake.

Decision ladder placement

Model / retrieval: "vector index memory costs too much" = quantization with rerank (D1 ch11).

:::exam-ask

Scenario: "A 50-million-vector OpenSearch index is too expensive to hold in memory. Retrieval quality must stay close to current levels." Correct: binary or FP16 quantization with a full-precision rerank stage. Distractors: larger instances (costly), reducing dimensions (changes the embedding model contract).
:::

An OpenSearch vector index holding 40 million float32 vectors no longer fits in memory on the current instance class. Which approach reduces memory most while preserving ranking quality?

1. Move to a larger instance class and keep float32 vectors.
2. Store vectors as binary (1 bit per dimension) for candidate retrieval, then rerank the top candidates at full precision.
3. Delete half the vectors at random.
4. Reduce the embedding model dimension from 1536 to 384 without reindexing.

B is correct. Binary quantization gives 32x compression for the retrieval pass, and the full-precision rerank recovers ranking quality.

A is wrong because it pays more instead of optimizing. C is wrong because random deletion destroys recall. D is wrong because changing dimensions without reindexing produces meaningless vectors.

### SageMaker large-model tuning specifics {#sagemaker-large}

#### What it is {#what-it-is}

D2 ch11 teaches SageMaker deployment (persistent endpoints, batch transform). This entry covers the large-model specifics the exam names: the timeout and volume knobs you turn when deploying a model with tens or hundreds of gigabytes of weights, and the instance families AWS points at for big GPU models versus small CPU tasks.

#### Why it exists {#why-it-exists}

Deploying a small classifier and deploying a 70B-parameter LLM are different operations. Large model artifacts take a long time to download from S3, and containers take a long time to load weights into GPU memory before they can answer a health check. SageMaker's defaults assume small models; without tuning, the deployment fails with timeout errors that look like broken code but are really just impatience.

#### How it works {#how-it-works}

1. **Production variant fields.** On the endpoint configuration's production variant, set `ModelDataDownloadTimeoutInSeconds` (how long SageMaker waits for the model artifact download) and `ContainerStartupHealthCheckTimeoutInSeconds` (how long it waits for the container to become healthy after download). Large models need both raised substantially.
2. **`VolumeSizeInGB`.** The EBS volume attached to the instance must fit the model artifact plus the container plus headroom. SageMaker supports very large models (up to the 500 GB class); size the volume accordingly.
3. **Instance selection.** Large GPU models go on GPU families such as `ml.p4d.24xlarge` (high-end NVIDIA GPUs, large GPU memory). Small CPU tasks such as named-entity recognition go on compute families such as `ml.c5.9xlarge`. The exam's favorite discriminator is exactly this pairing: big generative model versus small CPU-friendly task.
4. **Failure signature.** A deployment that fails during creation with download or health-check timeouts, on an instance type that looks big enough, is a timeout-tuning problem, not a model problem.

#### Concrete numbers {#concrete-numbers}

Model sizes up to the 500 GB class are deployable (illustrative upper bound; check current quotas). Default timeouts are measured in minutes and suit small models; large-model deployments commonly need tens of minutes for download plus container startup (illustrative; tune to your artifact size and instance network throughput).

:::takeaway

Key exam facts.

(1) Raise

ModelDataDownloadTimeoutInSeconds

and

ContainerStartupHealthCheckTimeoutInSeconds

for large models. (2) Size

VolumeSizeInGB

for the artifact plus headroom. (3) Large GPU models:

ml.p4d.24xlarge

class; small CPU tasks like NER:

ml.c5.9xlarge

class.
:::

:::exam-ask

Trap.

AWS will show a large-model deployment failing and offer "use a bigger instance" as the fix. If the failure is a download or health-check timeout, a bigger instance does not help; the timeouts do. A second trap swaps the instance families: putting a small NER model on

ml.p4d.24xlarge

is technically possible but economically wrong, and the exam tests cost-awareness.
:::

```
  endpoint creation timeline (large model)
  |--- download artifact (slow: 100s of GB) ---|--- container loads weights ---|--- healthy
      ^ ModelDataDownloadTimeoutInSeconds           ^ ContainerStartupHealthCheckTimeoutInSeconds
      defaults expire here -> false failure         defaults expire here -> false failure
  instance: ml.p4d.24xlarge (large GPU model)  vs  ml.c5.9xlarge (small CPU task, e.g. NER)
```

Figure 4.4. Where large-model deployments actually fail: the two timeout windows. Both must cover the real duration of their phase, and the instance family must match the workload, not just be large.

How to read this diagram

1. **The timeline has two slow phases.** Downloading the artifact and loading weights into the container are the long poles; inference has not started yet.
2. **Each phase has its own timeout.** The arrows show which knob covers which phase. A failure timestamp tells you which one expired.
3. **The instance line.** GPU family for large generative models, compute family for small CPU tasks. Match the family to the workload shape.
4. **What breaks:** raising only one timeout moves the failure to the next phase. Tune both, and verify the volume size at the same time.

Decision ladder placement

Model / deployment: "deploy a very large model on SageMaker" = timeout tuning plus correct instance family (D2 ch11).

:::exam-ask

Scenario: "Deploying a 150 GB model to a SageMaker endpoint fails during creation with a download timeout, on an instance with enough GPU memory." Correct: increase

ModelDataDownloadTimeoutInSeconds

(and check the health-check timeout and volume size). Distractors: larger instance type, smaller model.
:::

A 200 GB language model fails to deploy to a SageMaker endpoint. The instance has sufficient GPU memory, but creation fails while downloading the model artifact from S3. What is the most direct fix?

1. Switch to a larger GPU instance type.
2. Increase `ModelDataDownloadTimeoutInSeconds` on the production variant and verify `VolumeSizeInGB`.
3. Reduce the model size with quantization before deploying.
4. Deploy with batch transform instead of a persistent endpoint.

B is correct. The failure is a download timeout, not a capacity problem; the timeout field directly addresses it, and the volume must fit the artifact.

A is wrong because GPU memory was already sufficient; the bottleneck is download time. C is wrong because it changes the model rather than fixing the deployment configuration. D is wrong because batch transform does not change artifact download behavior and mismatches the endpoint requirement.

### Amazon EMR {#emr}

#### What it is {#what-it-is}

Amazon EMR (Elastic MapReduce) is a managed big-data platform for running open-source distributed frameworks: Apache Spark, Hadoop (MapReduce/YARN), Hive, Presto/Trino, HBase, and Flink. AWS provisions, configures, and scales the cluster; you submit data-processing jobs. Three flavors: EMR on EC2 (classic clusters), EMR on EKS (run on your Kubernetes cluster), and EMR Serverless (submit a Spark or Hive job with no cluster to manage).

#### Why it exists, and the GenAI connection {#why-it-exists-and-the-genai-connection}

GenAI training and large-scale RAG ingestion need heavy data processing: deduplicating billions of web documents, joining click logs, computing embeddings in bulk. EMR is the managed home for that Spark-scale ETL. It is peripheral to the exam's GenAI core, but it appears as the "big ETL" answer in data-pipeline scenarios, and the exam expects you to distinguish it from Glue.

#### How it works {#how-it-works}

1. **Cluster topology.** A primary node coordinates; core nodes run tasks and host HDFS; optional task nodes are compute-only (ideal for Spot instances).
2. **Storage.** EMRFS lets the cluster read and write S3 directly (durable, decoupled); HDFS on core nodes is fast but ephemeral. The AWS Glue Data Catalog serves as the shared Hive metastore across clusters.
3. **Work submission.** Jobs run as steps (Spark/Hive applications) with configurable concurrency; bootstrap actions install dependencies at launch.
4. **EMR vs Glue.** Glue is serverless Spark for standard ETL with minimal tuning. EMR gives full control over framework versions, instance types, and cluster topology for large, long-running, or highly customized jobs. EMR Serverless sits between: no cluster to manage, pay per job.

#### Concrete numbers {#concrete-numbers}

EMR on EC2 adds a per-instance-hour EMR surcharge on top of EC2 cost; EMR Serverless bills per vCPU-second and memory-second with a one-minute minimum on some dimensions (illustrative). Cost levers the exam names: Spot instances for task nodes, S3 (not HDFS) for durable data, auto-termination of idle clusters.

:::takeaway

Key exam facts.

(1) EMR = managed Spark/Hadoop/Hive/Presto/HBase/Flink. (2) Flavors: EC2 clusters, EKS, Serverless. (3) EMRFS (S3, durable) vs HDFS (ephemeral). (4) Glue for standard serverless ETL; EMR for large, long-running, or customized big-data jobs.
:::

:::exam-ask

Trap.

AWS will offer Glue for a "massive custom Spark job needing specific framework versions and fine-grained cluster control." That specificity is the EMR trigger. Conversely, "standard nightly ETL, no cluster management" is Glue, not EMR.
:::

```
  raw data (S3) --> EMR cluster --> processed data (S3 / Redshift)
                      |  primary: coordinates
                      |  core: tasks + HDFS (ephemeral)
                      |  task: compute only (Spot-friendly)
  EMR vs Glue: need framework control, huge/long jobs --> EMR
               standard ETL, no cluster ops          --> Glue
               Spark job, no cluster at all           --> EMR Serverless
```

Figure 4.5. EMR's shape and the three-way decision. Topology and framework control are what you buy with EMR; Glue and EMR Serverless trade control for simplicity.

How to read this diagram

1. **Top: the pipeline.** S3 in, S3 out; the cluster is the compute between. Durable data never lives on HDFS.
2. **Middle: the node roles.** Primary coordinates, core does work and holds scratch data, task adds cheap compute. Spot goes on task nodes because losing them loses no data.
3. **Bottom: the decision.** Three questions pick the service: how custom is the job, how big or long, and who manages the cluster.
4. **What breaks:** storing results only in HDFS and letting the cluster terminate deletes the output. Durable outputs always go to S3 via EMRFS.

Decision ladder placement

Processing: "large-scale distributed ETL for training or ingestion data" = EMR (or Glue for standard jobs).

:::exam-ask

Scenario: "Process 50 TB of logs nightly with a custom Spark build requiring a specific Hadoop version, minimizing cost." Correct: EMR on EC2 with task nodes on Spot, data in S3 via EMRFS. Distractors: Glue (no framework-version control), Lambda (wrong scale).
:::

A team must run a nightly 30 TB Spark ETL job that requires a specific Spark and Hadoop version, with full control over instance types and minimal cost. Which solution fits best?

1. AWS Glue with default settings.
2. Amazon EMR on EC2 with Spot task nodes and S3 storage via EMRFS.
3. AWS Lambda with provisioned concurrency.
4. Amazon Athena with CTAS queries.

B is correct. EMR provides framework-version and instance control for large jobs; Spot task nodes and S3 storage minimize cost.

A is wrong because Glue does not offer the required framework-version control. C is wrong because Lambda cannot handle 30 TB batch ETL. D is wrong because Athena is interactive SQL, not a customizable Spark ETL engine.

## 5. QA and verification log {#5-qa-and-verification-log}

How this volume was checked, what passed, what is open, and where every fact came from.

### QA checklist results {#qa-checklist}

| Check | Result |
|---|---|
| HTML parses; tags balanced | Pass: verified with a parser after writing (see method below). |
| Unique ids; internal anchors resolve | Pass: all 17 topic ids plus chapter and QA anchors are unique and every rail link resolves. |
| Zero em dashes | Pass: byte scan for U+2014 found none. |
| Zero gradients; flat colors only | Pass: stylesheet uses only flat hex fills from the shared palette; no gradient keyword present. |
| No emojis in prose | Pass. |
| No placeholders (TODO, lorem, coming soon, empty sections) | Pass: every section has full content. |
| Every topic has a visual plus walkthrough | Pass: 17 topics, 17 ASCII figures (Figures 1.1 through 4.5 plus 0.1), each with a numbered "How to read this diagram" walkthrough. |
| Depth elements per topic | Pass: each topic has what/why/how, concrete numbers, a stated misunderstanding, a visual with walkthrough, and a "how AWS will ask" line. |
| No external dependencies | Pass: single file, inline CSS, no fonts, scripts, or hotlinked images. Opens fully offline. |
| Generic content only | Pass: no names, employers, or personal identifiers. |
| No invented facts | Pass: volatile numbers labeled illustrative; unconfirmable items marked UNVERIFIED inline (divider strings, one CountTokens caution). |
| Practice coverage | Pass: one scenario question per topic (17 total), each explaining the correct answer and every distractor. |

**Open items:** none structural. Two inline UNVERIFIED markers are intentional (see log below). Image count: zero raster images by design; all figures are ASCII in styled pre blocks, which guarantees rendering on an office laptop with no image pipeline.

### Verification log {#verification-log}

Method: web search against live AWS documentation and corroborating sources on 2026-09-28. Findings:

| Topic | Status | Key finding |
|---|---|---|
| Amazon AppFlow | Verified | SaaS-to-AWS flows; source/destination/mapping/transforms; on-demand, scheduled, event-driven triggers; incremental pulls; Secrets Manager credential storage. Source: docs.aws.amazon.com. |
| Transfer Family | Verified | SFTP/FTPS/FTP/AS2; S3 and EFS backends; plain FTP only on VPC-internal endpoints, public endpoints support SFTP only. Source: docs.aws.amazon.com GovCloud page plus corroboration. |
| QuickSight | Verified | Serverless BI; SPICE in-memory engine; dashboards, paginated reports, ML insights (anomaly detection, forecasting), natural-language Q; Standard vs Enterprise; RLS/CLS. |
| Neptune Analytics | Verified | HNSW vector search; `vectors.topK.byEmbedding` is current, `vectors.topKByEmbedding` is deprecated; dimensions fixed at creation, max 65,000. |
| Q Apps | Verified | Inside Q Business (Pro tier); no-code apps from natural language or a conversation; card model with @ mentions; org app library sharing; inherits Q Business governance. Sources: Computerworld, community, 2026. |
| Secrets Manager | Verified | Lambda rotation functions; create/set/test/finish steps; AWSPENDING/AWSCURRENT staging; built-in rotation for RDS engines, Redshift, DocumentDB, Neptune, MongoDB Atlas. Multiple 2026 sources. |
| WAF | Verified | Web ACL, priority-ordered rules; Allow/Block/Count/CAPTCHA/Challenge; `AWSManagedRulesCommonRuleSet` and other managed groups; CloudFront-scope ACLs created in us-east-1. |
| CloudFront | Verified | Distributions, origins, path-based cache behaviors; OAC current, OAI legacy; signed URL (one file) vs signed cookies (many); ACM certificate in us-east-1. Corroborated across study sources. |
| CountTokens | Verified (one caution UNVERIFIED) | `POST /model/{modelId}/count-tokens` on bedrock-runtime; free; same formats as InvokeModel/Converse; matches billed tokens. The inference-profile ID rejection is community-reported, marked UNVERIFIED inline. |
| top_k | Verified | Converse `inferenceConfig` documents only maxTokens, stopSequences, temperature, topP; topK goes via `additionalModelRequestFields` or InvokeModel bodies; Bedrock Agents `InferenceConfiguration` does include topK. |
| Evidently | Verified | Experiments (A/B) plus feature flags; `EvaluateFeature` and `PutProjectEvents`; still documented. Source: AWS Cloud Operations blog, 2026. |
| TTFT | Verified | Bedrock emits `TimeToFirstToken` in CloudWatch `AWS/Bedrock` (streaming only); `InvocationLatency` covers all ops. Corroborated by latency research docs and March 2026 release coverage. |
| Textract | Verified | Sync `DetectDocumentText`/`AnalyzeDocument` with FeatureTypes TABLES/FORMS/QUERIES/LAYOUT/SIGNATURES; async `StartDocumentAnalysis`/`GetDocumentAnalysis` for multi-page S3 PDFs; `AnalyzeExpense`, `AnalyzeID`; Block output model; SNS; A2I. Source: docs.aws.amazon.com. |
| Divider strings | UNVERIFIED | Not AWS-documented; taught as a course preprocessing technique. Presented as a pattern with the marker inline. |
| Vector quantization | Verified | Binary vectors 32x vs float32; 2-bit/4-bit at 16x/8x; FP16 via SQfp16 (Faiss, OpenSearch 2.13+) at 2x; Lucene scalar quantization from 2.16; roughly 2% accuracy impact in AWS testing. Sources: docs.opensearch.org, AWS Big Data blog. |
| SageMaker large-model | Verified | `ModelDataDownloadTimeoutInSeconds`, `ContainerStartupHealthCheckTimeoutInSeconds`, `VolumeSizeInGB`; 500 GB class models; `ml.p4d.24xlarge` for large GPU models; `ml.c5.9xlarge` for small CPU tasks like NER. Sources: AWS ML blogs, SageMaker docs. |
| EMR | Verified | Managed Spark/Hadoop/Hive/Presto/Trino/HBase/Flink; primary/core/task topology; EMR on EC2, EKS, Serverless; EMRFS vs HDFS; Glue Data Catalog metastore; EMR vs Glue decision. |

Last verified: 2026-09-28. This appendix covers all 17 items in the coverage-map gap list: 5 hard gaps and 12 partials. Companion volumes: D1 through D5, the question bank, the system design volume, and the labs volume (`volume-maarek-labs.html`).

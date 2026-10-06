# AIP-C01 Verified Exam Facts (v2 build, Stage 1)

Research date: 2026-10-06.

Primary sources read in full:
- Official exam guide, HTML: https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html plus all five content-domain pages (-domain1 through -domain5), the service-mentions page, and the Technologies and concepts page.
- Official exam guide, PDF: https://docs.aws.amazon.com/pdfs/aws-certification/latest/ai-professional-01/ai-professional-01.pdf (PDF conversion; footer carries "Copyright (c) 2026 Amazon Web Services, Inc. and/or its affiliates"). In-scope services on PDF pages 18-23; out-of-scope on pages 23-29; technologies and concepts on page 17.
- Baseline for comparison: ~/workspace/your_files/aws-aip-c01-cert/EXAM-BLUEPRINT.md (verified 2026-09-28).

Claim labels used on every fact below:
- **[Guide]** = Official exam-guide requirement or statement (verified in both HTML and PDF on 2026-10-06).
- **[Behavior]** = Verified current AWS behavior (from AWS docs outside the exam guide; where the guide itself states it, marked [Guide] instead).
- **[Secondary]** = Corroborated by multiple independent secondary sources but NOT stated in the official exam guide.
- **[Unverified]** = Could not be verified from any acceptable source.
- **[Version-dependent]** = Documented value that changes over time; teach the principle, verify the number.

## Exam facts

| Fact | Value | Claim label |
|---|---|---|
| Exam code | AIP-C01 | [Guide] |
| Full name | AWS Certified Generative AI Developer - Professional | [Guide] |
| Total questions | 75 | [Guide] |
| Scored questions | 65 | [Guide] |
| Unscored questions | 10, unidentified, used to evaluate future questions | [Guide] |
| Question types | Multiple choice (1 correct + 3 distractors); Multiple response (2+ correct out of 5+ options; must select ALL correct for credit; no partial credit) | [Guide] |
| Ordering / matching types | NOT listed in the guide's question-type section | [Guide] (absence verified) |
| Duration | 180 minutes | [Secondary] |
| Price | USD 300 | [Secondary] |
| Delivery | Pearson VUE testing center or online proctored | [Secondary] |
| Scoring | Scaled 100-1000; minimum passing score 750; pass/fail designation; scaled scores equate difficulty across exam forms | [Guide] |
| Scoring model | Compensatory: no per-domain minimum; only the overall score matters | [Guide] |
| Unanswered questions | Scored as incorrect; no penalty for guessing | [Guide] |
| Target candidate | 2+ years building production-grade apps on AWS or open source; general AI/ML or data engineering experience; 1 year hands-on GenAI implementation | [Guide] |
| Job tasks OUT of scope | Model development and training; advanced ML techniques; data engineering and feature engineering (list is non-exhaustive) | [Guide] |
| Recommended AWS knowledge | Compute, storage, networking; security and identity; deployment and IaC; monitoring and observability; cost optimization | [Guide] |

## Domain weights [Guide]

| Domain | Weight (of scored content) |
|---|---|
| D1 Foundation Model Integration, Data Management, and Compliance | 31% |
| D2 Implementation and Integration | 26% |
| D3 AI Safety, Security, and Governance | 20% |
| D4 Operational Efficiency and Optimization for GenAI Applications | 12% |
| D5 Testing, Validation, and Troubleshooting | 11% |

## Deltas vs the Sept 28, 2026 baseline (EXAM-BLUEPRINT.md)

- NO CHANGE on any official fact. 75 questions (65 scored + 10 unscored), MC + multiple response, 750/1000 pass, compensatory scoring, and domain weights 31/26/20/12/11 all re-verified against the current official guide on 2026-10-06.
- One correction to the baseline's "question types" line: the baseline listed "ordering + matching" as question types. The current official guide lists only multiple choice and multiple response. Ordering/matching were re-verified absent in the Oct 6 guide. (Possible the baseline drew those from a different AWS exam template; for AIP-C01 the official guide does not name them.)
- Duration (180 min) and price ($300) still do NOT appear in the official exam guide itself (HTML or PDF). They remain corroborated by multiple independent secondary sources (dev.to FAQ updated ~Aug 2026, certcrush.app, three independent GitHub study repos) — keep the [Secondary] label. The Kodekloud "130 minutes" outlier persists; it conflicts with every other source and remains treated as an error.

## Unresolved / honestly UNVERIFIED items

1. **Guide version number.** The baseline cited "exam guide v1.0". The fetched guide (HTML and PDF, Oct 6, 2026) carries no visible version label; the PDF footer shows only "Copyright (c) 2026". Version number: [Unverified].
2. **Exam duration and price.** Not in the official guide. [Secondary] per the table above; re-verify at registration.
3. **Per-domain scored-question counts.** AWS publishes only weights, not counts. The baseline's estimates (D1 ~20, D2 ~17, D3 ~13, D4 ~8, D5 ~7 out of 65 scored) remain estimates, not facts. Do not present them as official.
4. **Languages.** The guide does not name exam languages. Not verified; do not claim.

## Note on scaled score

The guide states scoring is scaled 100-1000 with a 750 pass mark, explicitly to equate difficulty across forms. Do not translate 750 into a raw "percentage of questions right" — the guide gives no raw-to-scaled mapping, and any such conversion would be fabrication.

## In-scope / out-of-scope service lists (from the official PDF, pages 18-29)

Both lists are explicitly non-exhaustive and subject to change.

**In-scope (by category):** Analytics: Amazon Athena, Amazon EMR, AWS Glue, Amazon Kinesis, Amazon OpenSearch Service, Amazon QuickSight, Amazon MSK. Application Integration: Amazon AppFlow, AWS AppConfig, Amazon EventBridge, Amazon SNS, Amazon SQS, AWS Step Functions. Compute: AWS App Runner, Amazon EC2, AWS Lambda, AWS Lambda@Edge, AWS Outposts, AWS Wavelength. Containers: Amazon ECR, Amazon ECS, Amazon EKS, AWS Fargate. Customer Engagement: Amazon Connect. Database: Amazon Aurora, Amazon DocumentDB, Amazon DynamoDB, DynamoDB Streams, Amazon ElastiCache, Amazon Neptune, Amazon RDS. Developer Tools: AWS Amplify, AWS CDK, AWS CLI, AWS CloudFormation, AWS CodeArtifact, AWS CodeBuild, AWS CodeDeploy, AWS CodePipeline, Kiro, AWS Tools and SDKs, AWS X-Ray. Machine Learning: Amazon Augmented AI, Amazon Bedrock, Amazon Bedrock AgentCore, Amazon Bedrock Knowledge Bases, Amazon Bedrock Prompt Management, Amazon Bedrock Prompt Flows, Amazon Comprehend, Amazon Kendra, Amazon Lex, Amazon Q Business, Amazon Q Business Apps, Amazon Q Developer, Amazon Quick, Amazon Rekognition, Amazon SageMaker AI, Amazon SageMaker Clarify, Amazon SageMaker Data Wrangler, Amazon SageMaker Ground Truth, Amazon SageMaker JumpStart, Amazon SageMaker Model Monitor, Amazon SageMaker Model Registry, Amazon SageMaker Neo, Amazon SageMaker Processing, Amazon SageMaker Unified Studio, Amazon Textract, Amazon Titan, Amazon Transcribe. Management and Governance: AWS Auto Scaling, AWS Chatbot, AWS CloudTrail, Amazon CloudWatch, Amazon CloudWatch Logs, Amazon CloudWatch Synthetics, AWS Cost Anomaly Detection, AWS Cost Explorer, Amazon Managed Grafana, AWS Service Catalog, AWS Systems Manager, AWS Well-Architected Tool. Migration and Transfer: AWS DataSync, AWS Transfer Family. Networking and Content Delivery: Amazon API Gateway, AWS AppSync, Amazon CloudFront, Elastic Load Balancing, AWS Global Accelerator, AWS PrivateLink, Amazon Route 53, Amazon VPC. Security, Identity, and Compliance: Amazon Cognito, AWS Encryption SDK, IAM, IAM Access Analyzer, IAM Identity Center, AWS KMS, Amazon Macie, AWS Secrets Manager, AWS WAF. Storage: Amazon EBS, Amazon EFS, Amazon S3, Amazon S3 Intelligent-Tiering, Amazon S3 Lifecycle policies, Amazon S3 Cross-Region Replication.

**Out-of-scope (notable for writers - do not build exam content around these):** Application Integration: Amazon MQ. Analytics: AWS Clean Rooms, AWS Data Exchange, Amazon DataZone, Amazon FinSpace. Blockchain: Amazon Managed Blockchain. Business Applications: Alexa for Business, Amazon Chime, AWS Wickr, Amazon WorkDocs, Amazon WorkMail. Cloud Financial Management: AWS Budgets, AWS Cost and Usage Report, Reserved Instance reports, AWS Savings Plans. Compute: AWS Batch, EC2 Image Builder, ECS Anywhere, EKS Anywhere, Elastic Beanstalk, Lightsail, Local Zones, Serverless Application Repository. Containers: App2Container, Copilot, ROSA. Customer Engagement: Amazon SES. Database: Keyspaces, QLDB, Redshift, Timestream. Developer Tools: Cloud9, CloudShell, CodeGuru, CodeStar, Corretto. End User Computing: AppStream 2.0, WorkLink, WorkSpaces, WorkSpaces Web. Frontend Web and Mobile: Device Farm, Location Service, Pinpoint. Game Development: GameLift, Lumberyard. IoT: full IoT family. Management and Governance: Console Mobile App, Health Dashboard, License Manager, Proton, Trusted Advisor. ML: DeepComposer, DeepRacer, DevOps Guru, Forecast, Fraud Detector, HealthLake, Lookout for Equipment/Metrics/Vision, Monitron, Panorama. Media Services: full Elemental family plus Elastic Transcoder, IVS, Kinesis Video Streams, Nimble Studio. Migration and Transfer: Application Discovery Service, Application Migration Service, CloudEndure, Migration Hub, Snow Family. Networking: App Mesh, Cloud Map, Direct Connect, Private 5G, Transit Gateway, VPN. Quantum: Braket. Robotics: RoboMaker. Satellite: Ground Station.

All list facts above: [Guide] (verbatim transcription from the official PDF).

## Technologies and concepts that might appear (official PDF, page 17)

The guide names (non-exhaustive, no weight implied by order): RAG; vector databases and embeddings; prompt engineering and management; FM integration; agentic AI systems; Responsible AI practices; content safety and moderation; model evaluation and validation; cost optimization for AI workloads; performance tuning for AI applications; monitoring and observability for AI systems; security and governance for AI applications; API design and integration patterns; event-driven architectures; serverless computing; container orchestration; infrastructure as code (IaC); CI/CD for AI applications; hybrid cloud architectures; enterprise system integration. [Guide]

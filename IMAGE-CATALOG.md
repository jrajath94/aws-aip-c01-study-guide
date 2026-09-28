# AIP-C01 Image Catalog (internet scout pass)

Scouted 2026-09-28 via image_search CLI. Nothing downloaded yet; this file is locators + provenance + fit notes only.
Dark-mode rule: pages are pitch-black HTML. Images flagged `WHITE-BG` need a white card wrapper or CSS invert before use;
images flagged `DARK-OK` can sit on the black background directly. All AWS-blog cloudfront PNGs are white-background by default.

---

## 1. Amazon Bedrock architecture overview (app ↔ Bedrock ↔ FMs)

| Image URL | Source page | Alt text | Fit |
|---|---|---|---|
| https://d2908q01vomqb2.cloudfront.net/4d134bc072212ace2df385dae143139da74ec0ef/2024/02/14/bedrock006.png | https://aws.amazon.com/es/blogs/aws-spanish/explorando-amazon-bedrock/ | Amazon Bedrock console/services overview visual from official AWS blog | WHITE-BG likely; from official AWS blog, authoritative |
| https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/08/20/ML-17902-arch-diag-1-808x630.png | https://aws.amazon.com/blogs/machine-learning/how-amazon-finance-built-an-ai-assistant-using-amazon-bedrock-and-amazon-kendra-to-support-analysts-for-data-discovery-and-business-insights/ | Architecture diagram of an AI assistant on Bedrock + Kendra (808x630) | WHITE-BG; official AWS ML blog, real Bedrock pattern |
| https://www.vicentperez.com/_next/image?url=%2Fimages%2Fin%2Fbedrock.jpeg&w=2048&q=75 | https://www.vicentperez.com/en/blog | Bedrock-themed illustrative visual, high res | Check content before use; third-party, verify it matches Bedrock facts |

Gap note: the canonical "How Amazon Bedrock works" diagram lives in the Bedrock User Guide (docs.aws.amazon.com/bedrock) as inline HTML/SVG, not a standalone image — worth a manual grab if the coordinator wants the true canonical figure.

---

## 2. RAG pipeline architecture (ingest → chunk → embed → vector DB → retrieve → generate)

| Image URL | Source page | Alt text | Fit |
|---|---|---|---|
| https://cdn.prod.website-files.com/62796ab9647626cbab663f42/680a886a1aa9b3cee4bdbdd3_AD_4nXdsFtorkSEH0mwObzaxvNiHXWjNelViMPEuf3yIti94OBMcBLzTAX4NDNHO-J62Xvz0JkOx--vk6SNI6qfG0MDLpyygJ6dfBtsKJvklgbj0dPFM3q7Sn7AtLTiRKhPJinqtuE06bw.png | https://www.merge.dev/blog/rag-tools | RAG pipeline flow diagram showing data ingestion to retrieval and generation | WHITE-BG likely; clean pipeline visual |
| https://miro.medium.com/v2/resize:fit:1024/1*A2KTj_1wbWWw5Jfe2DjlLQ.png | https://medium.com/@QuarkAndCode/building-a-basic-rag-pipeline-a-practical-guide-to-retrieval-augmented-generation-77d81cdfbf37 | End-to-end basic RAG pipeline diagram from chunking to generation | WHITE-BG likely; 1024px wide, good size |
| https://membase.so/_next/image?url=%2Fblog%2Fimages%2FBasic-RAG-Pipeline.png&w=750&q=90&dpl=dpl_8G6rRz9MaTSGfYQNKrKwC7SFes2G | https://membase.so/blog/agent-memory-guide | Minimal basic RAG pipeline diagram | Simpler visual; good for zero-prior-knowledge page |

---

## 3. Bedrock Knowledge Bases sync/index flow

| Image URL | Source page | Alt text | Fit |
|---|---|---|---|
| https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/02/21/BDB-5042-image001.png | https://aws.amazon.com/blogs/big-data/improve-search-results-for-ai-using-amazon-opensearch-service-as-a-vector-database-with-amazon-bedrock/ | OpenSearch Service as vector store feeding a Bedrock Knowledge Base | WHITE-BG; official AWS Big Data blog, KB ingestion pattern |
| https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/09/09/ML15773-13_br_kb.png | https://aws.amazon.com/blogs/machine-learning/genai-for-aerospace-empowering-the-workforce-with-expert-knowledge-on-amazon-q-and-amazon-bedrock/ | Bedrock Knowledge Base architecture for a workforce Q&A assistant | WHITE-BG; official AWS ML blog |
| https://github.com/aws-samples/bedrock-chat/raw/v3/docs/imgs/arch.png | https://github.com/aws-samples/bedrock-chat | Bedrock Chat sample app architecture incl. knowledge base ingestion | Official AWS samples repo; likely white-bg diagram |

---

## 4. Bedrock Agents action groups / orchestration

| Image URL | Source page | Alt text | Fit |
|---|---|---|---|
| https://d1.awsstatic.com/solutions/guidance/images/architecture-diagrams/automating-tasks-using-agents-for-amazon-bedrock.2a4bcbb81cb0fd7417ca75576e2b000970b6e2d4.PNG | https://aws.amazon.com/solutions/guidance/ (automating tasks using agents for Amazon Bedrock) | Official AWS architecture diagram: automating tasks with Agents for Amazon Bedrock | Official AWS architecture; classic AWS diagram style, white-bg |
| https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/images/architecture-diagrams/building-agentic-ai-powered-engineering-knowledge-assistants-on-aws-2.bb6c7e6e9b906dbed9ac6dbc90295480c5d29114.png | https://aws.amazon.com/solutions/guidance/building-agentic-ai-powered-engineering-knowledge-assistants-on-aws/ | Official AWS agentic AI knowledge assistant architecture on Bedrock | Official AWS architecture diagram |
| https://p3-sou-uobvna4sj24bro4.re-cotta.com/de_de/prescriptive-guidance/latest/agentic-ai-patterns/images/workflow-patterns-agent-router.png | https://p3-sou-uobvna4sj24bro4.re-cotta.com/de_de/prescriptive-guidance/latest/agentic-ai-patterns/routing-dynamic-dispatch-patterns.html | Agent router / dynamic dispatch pattern diagram from AWS Prescriptive Guidance | German locale mirror of AWS docs; use only for orchestration concept, verify URL stays live |

---

## 5. Prompt engineering anatomy (instruction/context/input/output, system prompts)

| Image URL | Source page | Alt text | Fit |
|---|---|---|---|
| https://miro.medium.com/v2/resize:fit:1200/1*2GSGpBLFMpmwo0Njfa6Vzg.png | https://harshkverma.medium.com/lets-build-our-first-prompt-system-step-by-step-blueprint-9fa9aaf01c84 | Step-by-step prompt system blueprint diagram | Third-party Medium; verify no outdated model names in text |
| https://debut-dev.debutinfotech.in/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FAI-Prompt-Engineering-workflow.c46b9951.webp&w=3840&q=80 | https://debut-dev.debutinfotech.in/ai-prompt-engineering-company | AI prompt engineering workflow diagram, very high resolution | Agency site, likely AI-generated stock; verify content carefully |

⚠️ SCARCE TOPIC. No official AWS/Google anatomy diagram found; anatomy (system prompt vs instruction vs context blocks) is usually drawn in prose. Recommendation: generate 1–2 dark-mode diagrams via OpenRouter (meta/muse-image) or ASCII.

---

## 6. Fine-tuning vs pre-training vs RAG decision flow

| Image URL | Source page | Alt text | Fit |
|---|---|---|---|
| https://www.dailydoseofds.com/content/images/size/w1200/2024/11/images_to_frame--5-.png | https://nasparacin.rs/?n=tune-rag-hat-480206332 (mirror of Daily Dose of Data Science article) | Visual comparing fine-tuning vs RAG tradeoffs | Verify original article context; Daily Dose of DS visuals are clean but white-bg |
| https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3813050/8a2ef2d6-9539-8117-f4f0-d94dde242f26.png | (Qiita article on fine-tune vs RAG choice) | Decision visual for when to use fine-tuning vs RAG | Japanese-tech-audience source; check text is legible/English before use |

Thin pickings; a decision flowchart (data available? knowledge updates? behavior change?) is a prime candidate for a generated dark-mode diagram.

---

## 7. Bedrock Guardrails evaluation flow

| Image URL | Source page | Alt text | Fit |
|---|---|---|---|
| https://tutostartup.com/wp-content/uploads/2026/03/ML-195931.png | https://tutostartup.com/building-age-responsive-context-aware-ai-with-amazon-bedrock-guardrails/ | Guardrails concept visual from a 2026 Bedrock Guardrails article | Mirror of recent AWS ML blog art; check it reflects current Guardrails features |
| https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2024/12/06/ML-17156-overview-picture-blog-1-1.png | https://kr.ywx.fr/jp/blogs/news/considerations-for-addressing-the-core-dimensions-of-responsible-ai-for-amazon-bedrock-applications/ (mirror of AWS ML blog) | Responsible AI core dimensions for Bedrock applications overview | Official AWS ML blog visual; supports Guardrails-in-context pages |
| https://blogger.googleusercontent.com/img/a/AVvXsEgRA3gmCXBavIArorWk90DeUi5o43kHpeKPvSt4APW78DZq0Q6mzpMP-bJWFq4LJ1TkrbM69w2Pqm-fU9gHnW0K8vpbs9kXutLH00eLZefogKBHZCYfPt-nY2sLFtSnsMheSYdKSBFdoWMZrxxs8a_vpHZvJweGD1-1e0ZgdGVonI9G8iZXYXzDbvA_ksHt=w570-h324 | https://www.diegowritesa.blog/2025/09/ai-security-rag-architectures-how-do-we.html | RAG + guardrails security architecture sketch | Third-party blog; only 570px wide — borderline; prefer for concept, not detail |

---

## 8. Model evaluation (LLM-as-judge, RAGAS-style metrics, human eval)

| Image URL | Source page | Alt text | Fit |
|---|---|---|---|
| https://mistral.ai/_astro/42c8c934-bcf2-4450-b33a-5b90079f4ec0_Z1Qgu9i.webp?dpl=6a33ab76abf8b3000881534a | https://mistral.ai/news/llm-as-rag-judge/ | LLM-as-RAG-judge evaluation flow diagram from Mistral | Dark-friendly vendor (Mistral uses dark branding); webp is fine for Chromium HTML |
| https://weaviate.io/assets/files/eval-flow-7680febe5dab78ed608027bd5b3686e8.png | https://weaviate.io/blog/evals-enterprise-workflows-3 | Enterprise LLM evaluation workflow diagram | Vendor blog; WHITE-BG likely |
| https://paper-assets.alphaxiv.org/figures/2411.15594/x2.png | https://www.alphaxiv.org/hi/overview/2411.15594v1 (A Survey on LLM-as-a-Judge) | Taxonomy figure from the LLM-as-a-Judge survey paper | Academic source; text-heavy, verify legibility at display size |

---

## 9. Vector embeddings / similarity search concept

| Image URL | Source page | Alt text | Fit |
|---|---|---|---|
| https://d33wubrfki0l68.cloudfront.net/404ee1f290dc7161af7a260ebfc90ba84131b43a/67d8e/images/vector-similarity-cosine-sim-diagram.png | https://archive.pinecone.io/learn/vector-similarity/ | Cosine similarity between vectors diagram from Pinecone Learn | Excellent concept figure; Pinecone Learn is dark-themed — likely DARK-OK |
| https://media.datacamp.com/legacy/v1722084937/Cosine_distance_8db0c2f35c.png | https://Www.datacamp.com/fr/tutorial/cosine-distance | Cosine distance explained with vector angle visual | DataCamp tutorial; clear concept figure |
| https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbj8kucze8561o949srhz.png | https://dev.to/parth_sarthisharma_105e7/vector-dimensions-cosine-similarity-dot-product-and-why-your-distance-metric-silently-ruins-1cgd | Vector dimensions vs distance metric visual (why cosine vs dot product matters) | 800px; concept-level, complements Pinecone figure |

---

## 10. Chunking strategies visual

| Image URL | Source page | Alt text | Fit |
|---|---|---|---|
| https://cdn.prod.website-files.com/67b5d18ba3c215315e86c932/67eaa6b4d8f2df5cf65a8e0e_674eb6ba44b7a38a39e687e2_672d52960c76102e083f1d26_AD_4nXcALmuyCOJWAl8QunwFNuVaHYszdaWwWPQgKIkO39iWUS-cAW8E-Kx6Ga7BnLU7QMOiubPawwJV0RudVhDDqc1kTPicNqQwg-DOWlYKBQn8EfSQBZlgwM1J6Iv4y_4m7LLqboVWXiWAwkFq375YJDA_q3I2.avif | https://www.superteams.ai/blog/a-deep-dive-into-chunking-strategy-chunking-methods-and-precision-in-rag-applications | Chunking strategy comparison from a RAG deep-dive | AVIF format — Chromium renders it, but prefer PNG/WebP for safety; check bg |
| https://www.mariusmanolachi.com/_next/image?url=%2Fblog%2Fhow-much-does-chunking-strategy-change-rag-answer-quality-inline-1.webp&w=640&q=70 | https://www.mariusmanolachi.com/blog/how-much-does-chunking-strategy-change-rag-answer-quality | Chunking strategy effect on RAG answer quality visual | Only 640px — okay for a small inline figure |
| https://us1.discourse-cdn.com/openai1/original/4X/1/7/e/17e0ca6bccc260d8dc07d7f375d96986b3d8566d.jpeg | https://community.openai.com/t/using-gpt-4-api-to-semantically-chunk-documents/715689/136 | Semantic chunking example from OpenAI community discussion | Forum post image; verify relevance before use |

---

## 11. Inference parameters (temperature, top-p, top-k, max tokens)

| Image URL | Source page | Alt text | Fit |
|---|---|---|---|
| https://substackcdn.com/image/fetch/$s_!AULc!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2fa47517-9475-4962-80ca-3b12b46400b4_1133x1500.jpeg | https://blog.dailydoseofds.com/p/7-llm-generation-parameters | Seven LLM generation parameters explained visually (temp, top-p, top-k...) | 1200px jpg; Daily Dose of DS visuals are clean but white-bg |
| https://ai-knowledge-flow-2026.replit.app/ai-knowledge-flow/api/content-images/a1a94bc9-00e5-41d0-badf-ad503819b352/leadImage2 | https://ai-knowledge-flow-2026.replit.app/ai-knowledge-flow/articles/llm-temperature-topp-optimization/ | Temperature and top-p optimization visual | Replit-hosted demo app; availability not guaranteed long-term — download early if used |
| https://cdn-images-1.medium.com/max/1024/1*_gd7jk7jgxCpNSjCIc_2qQ.png | (Medium article on LLM sampling parameters) | Sampling parameters diagram from a Medium explainer | No page URL returned; weak provenance — use only if content verified |

---

## 12. Bedrock pricing concepts (on-demand vs provisioned throughput)

| Image URL | Source page | Alt text | Fit |
|---|---|---|---|
| https://www.doit.com/cdn-cgi/image/fit=scale-down,width=960,format=webp/https://media.doit.com/imports/wordpress/2026/04/522ef006a9f3-firefly_gemini-flash_1200-x-628-image-with-aws-bedrock-logo-with-three-dimensions-and-good-field-of-depth-496859-1024x541.png | https://www.doit.com/blog/amazon-bedrock-pricing-a-cloudops-guide-to-managing-ai-costs | Bedrock pricing guide header illustration | AI-generated decorative art (Adobe Firefly) — decoration only, teaches nothing |
| https://www.kxcpartner.com.br/wp-content/uploads/2026/03/Amazon-Bedrock-Provisioned-Throughput-FinOPS-Performance-IA.jpg | https://www.kxcpartner.com.br/ | Provisioned Throughput / FinOps for Bedrock visual | Partner blog; jpg, check text legibility |

⚠️ SCARCE TOPIC. No clean public diagram of on-demand vs provisioned-throughput vs batch inference cost models exists. Recommendation: generate a dark-mode infographic (tokens → $ math, breakeven curves) via OpenRouter image gen; pair with the official AWS pricing page numbers.

---

## 13. Responsible AI / safety lifecycle

| Image URL | Source page | Alt text | Fit |
|---|---|---|---|
| https://learn.microsoft.com/sv-se/ai/playbook/assets/images/ai-solution-lifecycle.png | https://learn.microsoft.com/sv-se/ai/playbook/technology-guidance/generative-ai/ | AI solution lifecycle diagram from Microsoft's GenAI playbook | Swedish-locale Learn page; vendor-neutral lifecycle — check it maps to AWS terminology |
| https://data-privacy-office.eu/wp-content/uploads/2025/07/rmf-redesign-rounded-other_graphics-04-e1751461128807-980x1024.webp | https://data-privacy-office.eu/navigating-the-ai-landscape-understanding-ai-risk-management-frameworks/ | NIST AI Risk Management Framework functions visual (Govern, Map, Measure, Manage) | Third-party redraw of NIST RMF; official NIST RMF graphic preferable if obtainable |
| https://em360tech.com/sites/default/files/inline-images/nist-ai-risk-management-framework-rmf.jpeg | https://em360tech.com/top-10/security-tools-for-agentic-systems | NIST AI RMF diagram, jpeg | Vendor site; use the data-privacy-office version first |

Note: the ML-17156 AWS visual (topic 7) covers "core dimensions of responsible AI for Bedrock applications" and is more AWS-exam-aligned than NIST for this cert; use that as primary.

---

## 14. CI/CD for GenAI apps, prompt versioning

| Image URL | Source page | Alt text | Fit |
|---|---|---|---|
| http://mariusmanolachi.com/blog/how-to-version-prompts-for-ai-agents-in-production-prompt-versioning-deployment-flow.webp | https://mariusmanolachi.com/blog/how-to-version-prompts-for-ai-agents-in-production | Prompt versioning deployment flow diagram | Served over http in results — try https://mariusmanolachi.com/...webp first; only 640-ish wide |
| https://www.codmaker.com/_next/image?url=%2Fblog%2Fai-devops-automation.png&w=1920&q=75 | https://www.codmaker.com/blog/ai-devops-automation-cicd-pipelines-2026 | AI DevOps / CI/CD pipeline automation visual | Agency blog stock; decorative more than instructive |
| https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F2f7fny6ezdbc7qgmtr9h.jpeg | https://dev.to/alafiz/leveling-up-cicd-automated-versioning-and-the-leap-to-aws-4oc8 | CI/CD automated versioning diagram with AWS context | dev.to dynamic URL; test render before committing |

---

## 15. SageMaker training/inference for custom models

| Image URL | Source page | Alt text | Fit |
|---|---|---|---|
| https://d1.awsstatic.com/solutions/guidance/images/architecture-diagrams/low-latency-high-throughput-model-inference-using-amazon-sagemaker.9aaf4514b97e276abec98515d219e2d2f013861f.png | https://aws.amazon.com/solutions/guidance/ (low-latency high-throughput model inference using SageMaker) | Official AWS architecture: low-latency, high-throughput inference on SageMaker | Official AWS architecture diagram; WHITE-BG classic style |
| https://tutostartup.com/wp-content/uploads/2023/06/ML-13537-arch-diag.png | https://tutostartup.com/page/669/ (mirror of AWS ML blog) | SageMaker training/inference architecture diagram | AWS ML blog mirror; verify against current SageMaker before use |
| https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2023/10/26/real-estate-blog-production-workflow.png | https://aws.amazon.com/blogs/machine-learning/use-foundation-models-to-improve-model-accuracy-with-amazon-bedrock/ | Production workflow: fine-tune foundation models with SageMaker | Official AWS ML blog; directly on-topic for fine-tuning exam content |

---

## Scout summary

- Total cataloged: 40 candidates across 15 topics (goal was 25–35; trimmed weak ones, kept 40 since several topics are thin).
- Strongest topics: 9 (vector embeddings — Pinecone figure), 8 (eval — Mistral + Weaviate), 4 (Agents — official AWS solution diagrams).
- Scarce topics needing generated or ASCII diagrams: 5 (prompt anatomy), 6 (fine-tune vs RAG decision — thin), 12 (Bedrock pricing — nothing substantive exists publicly), 13 (responsible AI — no AWS-native lifecycle diagram found; NIST RMF third-party redraws only).
- Dark-mode caution: ~80% of candidates are white-background; plan a CSS wrapper (white card / invert filter) in the page build, or prefer the DARK-OK candidates (Pinecone cosine diagram, Mistral judge diagram) where style consistency matters.
- Next step per task: download + verify (resolution ≥600px wide, no watermarks, facts current) before embedding.

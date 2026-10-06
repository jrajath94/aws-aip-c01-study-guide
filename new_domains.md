## D1 · Fundamentals of AI and ML (20%) {#d1-fundamentals}

### Ladder 1: The AI family (AI → ML → deep learning → GenAI)

**Rung 1: The plainest picture.** AI means machines doing tasks that need human-like judgment: recognizing speech, reading documents, making recommendations. Everything in this domain is a smaller circle inside that big idea.

:::figure assets/img/internet/aif-ai-ml-dl-genai.jpg light
The nesting of the field: AI is the outermost idea, machine learning sits inside it, deep learning inside that, generative AI at the center.
Image: Wikimedia Commons
:::

**Rung 2: Add one layer.** Machine learning is AI that learns from data instead of following hand-written rules. You show it thousands of examples, and it finds the pattern itself. It comes in three flavors: supervised (the examples include the right answers), unsupervised (no answers, it finds groups on its own), and reinforcement learning (it learns by trial and error, chasing rewards).

:::figure assets/img/mermaid/aif-rung-ml-learns.svg light
Machine learning in one picture: examples go in, training happens, a model comes out, and the model predicts on new data.
:::

**Rung 3: Exam grade.** Deep learning is machine learning done with neural networks, which are stacks of simple computing units inspired by brain neurons. Generative AI is deep learning that creates new content: text, images, audio. The nesting from rung 1 is now exact: GenAI ⊂ deep learning ⊂ ML ⊂ AI. Agentic AI (exam guide v1.1) sits at the center too: GenAI systems that take actions through tools, not just produce text.

:::figure assets/img/internet/aif-neural-network.png light
A neural network: an input layer, hidden layers, and an output layer. Deep learning means many hidden layers stacked.
Image: Wikimedia Commons
:::

### Ladder 2: The three ways models learn

**Rung 1: The plainest picture.** Supervised learning is learning with an answer key. Every training example comes with its label: this photo is a cat, this transaction is fraud. The model studies labeled examples until it can label new ones.

:::figure assets/img/mermaid/aif-rung-supervised.svg light
Supervised vs unsupervised at a glance: with labels the model learns the categories; without labels it must discover the groups itself.
:::

**Rung 2: Add one layer.** Unsupervised learning gets no answer key: it looks for natural groups (customers who behave alike) or compresses data down to its essentials. Reinforcement learning gets no answer key either; instead an agent takes actions in an environment and learns from rewards and penalties, like training a dog with treats.

:::figure assets/img/internet/aif-reinforcement-learning.png light
Reinforcement learning as a loop: the agent acts, the environment responds with a new state and a reward, and the agent adjusts.
Image: Wikimedia Commons
:::

**Rung 3: Exam grade.** Match the stem to the type: labeled data and a target to predict means supervised; unlabeled data and "find groups" means unsupervised; an agent, actions, and rewards means reinforcement learning. Supervised splits further into classification (predict a category, like fraud or not) and regression (predict a number, like a price). Note the v1.1 connection: RLHF, the technique that aligns chat models with human preferences, is reinforcement learning with human rankings as the reward signal.

:::figure assets/img/mermaid/aif-rung-learning-map.svg light
The exam decision in one diagram: check what the data looks like, and the learning type follows.
:::

:::exam-ask
A company wants to predict which customers will cancel, using five years of labeled cancel-or-stay records. Which learning type?

Supervised learning: the records are labeled, and the task predicts a category. If the stem had said "group customers by behavior with no labels", the answer would flip to unsupervised.
:::

:::details Knowledge check: name the learning type
1. Sorting support tickets into "billing", "technical", "other" from labeled history. 2. Finding unusual network traffic with no labeled attacks. 3. A robot learning to walk by falling over.

**Answers: 1. Supervised (classification: labeled tickets, category output). 2. Unsupervised (anomaly detection on unlabeled data). 3. Reinforcement learning (agent, actions, reward signal).**
:::

### Ladder 3: Training, inference, and the two failure modes

**Rung 1: The plainest picture.** Training is the learning phase: the model studies data and adjusts itself. Inference is the using phase: the finished model makes predictions on new data. Training happens once (or periodically); inference happens every time someone uses the system.

:::figure assets/img/mermaid/aif-rung-training-inference.svg light
The two phases side by side: training learns patterns from data with answers; inference applies them to new data without answers.
:::

**Rung 2: Add one layer.** Two things go wrong. Overfitting means the model memorized the training data, noise included, so it fails on new data: low training error, high test error. Underfitting means the model is too simple to catch the pattern: high error everywhere. You want the middle: the model learns the real pattern and ignores the noise.

:::figure assets/img/internet/aif-overfitting.png light
Overfitting vs underfitting: the wiggly curve memorizes every point including noise; the straight line misses the pattern; the smooth curve captures it.
Image: Wikimedia Commons
:::

**Rung 3: Exam grade.** To judge a model you need two kinds of numbers. Model metrics: accuracy (fraction correct overall), precision (of the items flagged positive, how many truly were), recall (of the truly positive items, how many got flagged). The exam's classic: a fraud model with high precision but low recall catches few criminals while rarely accusing the innocent. Read these off a confusion matrix: rows are actual classes, columns are predicted classes, and the four cells are true positives, false positives, true negatives, false negatives. Business metrics sit above: task completion rate, user satisfaction, cost per prediction. The bias-variance link: high bias underfits (too simple), high variance overfits (too twitchy). Fix overfitting with more data or simpler models; fix underfitting with richer features or bigger models.

:::figure assets/img/internet/aif-confusion-matrix.png light
A confusion matrix: actual classes on the rows, predicted classes on the columns. Precision and recall are computed from its four cells.
Image: Wikimedia Commons
:::

:::details Knowledge check: precision vs recall
A spam filter flags 100 emails as spam; 90 really are spam. Meanwhile 10 real spam emails slipped into the inbox. What are precision and recall?

**Precision 90/100 = 90%. Recall 90/100 = 90% here too (90 caught of 100 total spam).** The point: precision asks "of what you flagged, how much was right"; recall asks "of what was real, how much did you catch".
:::

### Ladder 4: The four inference types

**Rung 1: The plainest picture.** Real-time inference answers now: one request in, one answer back in milliseconds. A fraud check while you tap your card. Batch inference answers later: millions of rows scored on a schedule, like churn scores every Sunday night. The question is always "how fast must the answer come back?"

:::figure assets/img/mermaid/aif-rung-realtime-batch.svg light
The two extremes: real-time serves one request in milliseconds; batch scores millions of rows on a schedule.
:::

**Rung 2: Add one layer.** Two more options fill the middle. Asynchronous inference handles one large payload that takes minutes: you submit, go away, collect the result later (a two-hour video to transcribe). Serverless inference removes server management entirely: it scales to zero when idle and you pay per use, which fits spiky, unpredictable traffic.

:::figure assets/img/mermaid/aif-rung-async-serverless.svg light
The middle options: async for single large jobs with delayed results; serverless for spiky traffic with no servers to manage.
:::

**Rung 3: Exam grade.** The exam hands you a scenario and expects the cheapest fit: interactive and instant means real-time; big single payload with minutes to spare means async; huge volume on a schedule means batch; unpredictable spikes with no ops team means serverless. Bedrock adds its own flavors: on-demand (pay per token), provisioned throughput (reserved capacity for steady heavy workloads), and cross-region inference (route across regions for availability).

:::figure assets/img/mermaid/aif-inference-chooser.svg light
The inference decision tree: latency need, payload size, volume pattern, and traffic shape pick the type.
:::

:::details Knowledge check: which inference type?
1. A chatbot answering shoppers. 2. Transcribing one 3-hour board meeting. 3. Scoring 5 million loan applications nightly. 4. A demo app with 10 users today and maybe 10,000 tomorrow.

**Answers: 1. Real-time (interactive). 2. Asynchronous (single large payload, minutes OK). 3. Batch (huge volume, scheduled). 4. Serverless (spiky, unpredictable).**
:::

### Ladder 4: The AWS AI service map

**Rung 1: The plainest picture.** There are two ways to build. Train your own model from your data: that is SageMaker AI. Use a ready-made foundation model through an API: that is Bedrock. The exam's first split is always this one.

:::figure assets/img/mermaid/aif-rung-build-choice.svg light
The first decision: training your own model points to SageMaker AI; using a foundation model points to Bedrock.
:::

**Rung 2: Add one layer.** For everyday AI tasks you do not build at all; you call a specialist service. Text: Comprehend finds insights in text, Translate changes languages, Kendra searches your documents. Voice: Transcribe turns speech into text, Polly turns text into speech. Vision and documents: Rekognition analyzes images and video, Textract reads text from documents. Each does one job well.

:::figure assets/img/mermaid/aif-rung-services.svg light
The specialist services grouped by what they consume: text, voice, and vision plus documents.
:::

**Rung 3: Exam grade.** Name the service from the verb: "chatbot" means Lex; "search company documents" means Kendra; "read text from scanned forms" means Textract; "convert a call recording to text" means Transcribe; "synthesize voice" means Polly; "detect objects in photos" means Rekognition; "analyze sentiment" means Comprehend; "translate" means Translate. Personalize recommends products, Forecast (note: not in the v1.1 in-scope list, so the exam will not ask it) predicts demand, and for BI questions over data there is Q in QuickSight. Lex builds conversational interfaces; Q is the ready-made assistant. Services map to the ML lifecycle: S3 and Glue hold and prepare data, SageMaker AI trains, Bedrock and the specialist services serve, and MLOps (pipelines, monitoring, retraining) keeps it all running in production. When is AI the wrong answer? When a fixed rule or a database query solves it, when labeled data does not exist and cannot be made, or when the cost exceeds the value.

:::figure assets/img/mermaid/aif-ml-lifecycle.svg light
The ML lifecycle: data, training, deployment, and monitoring, with AWS services mapped to each stage.
:::

## D2 · Fundamentals of Generative AI (24%) {#d2-generative-ai}

### Ladder 1: Tokens, the unit of everything

**Rung 1: The plainest picture.** Models do not read words; they read tokens, which are chunks of text smaller than words. "Unbelievable" might become "un", "believ", "able". Everything a model does is counted and priced in tokens.

:::figure assets/img/mermaid/aif-rung-tokens.svg light
Tokenization: a sentence is split into token chunks, and everything downstream is priced and processed per token.
:::

**Rung 2: Add one layer.** The context window is the model's working memory: the maximum tokens it can consider at once, covering your prompt plus any retrieved documents plus the conversation so far. Feed it more than fits and the oldest content gets dropped. Long context is powerful and expensive, because cost grows with tokens in.

:::figure assets/img/mermaid/aif-rung-context.svg light
The context window as working memory: prompt, retrieved documents, and history all share it, and overflow drops the oldest content.
:::

**Rung 3: Exam grade.** Token pricing is per input token and per output token, and output tokens cost more because generating text burns more compute. Prompt caching stores repeated prompt prefixes so you pay full price once and a discount after. Inference cost also depends on model size and request volume: bigger models and longer outputs cost more. When a stem asks about cutting cost, think: smaller model, shorter outputs, caching.

:::figure assets/img/mermaid/aif-rung-pricing.svg light
Token pricing: input tokens are cheaper, output tokens cost more, so long generated answers dominate the bill.
:::

### Ladder 2: Embeddings, meaning as coordinates

**Rung 1: The plainest picture.** An embedding turns text into a list of numbers (a vector) that captures its meaning. Texts with similar meanings get similar numbers, so "king" sits near "queen" and far from "carburetor". Meaning becomes geometry: nearness equals relatedness.

:::figure assets/img/mermaid/aif-embedding-search.svg light
Embeddings turn text into vectors; similarity search then finds the stored vectors nearest to the question vector.
:::

**Rung 2: Add one layer.** That geometry is what makes semantic search work: embed the question, then fetch the stored vectors closest to it. The retrieved documents mean something similar to the question even if they share no exact words. This is the retrieval half of RAG, coming up in D3.

:::figure assets/img/mermaid/aif-embedding-search.svg light
The same pipeline as the retrieval step: the question is embedded with the same model, and the nearest stored chunks come back.
:::

**Rung 3: Exam grade.** The exam-grade rule: the same embedding model must run at ingest time and at query time, because each model has its own private vector space and vectors from two models are not comparable. On AWS the vectors live in a vector store: OpenSearch Service, Aurora, Neptune, or RDS for PostgreSQL. Chunking quality decides retrieval quality, which is why Bedrock Knowledge Bases chunks your S3 documents before embedding them.

:::details Knowledge check: why did search break?
A team embedded 100,000 documents with Model X, then switched the query side to cheaper Model Y. Retrieval quality collapsed overnight. What broke?

**The vector spaces no longer match.** Model Y's question vectors live in a different geometry than Model X's document vectors, so "nearest" is meaningless. Fix: embed queries with Model X too, or re-embed everything with one model.
:::

### Ladder 3: The Transformer

**Rung 1: The plainest picture.** The Transformer is the architecture behind modern language models. Its trick: read the whole sentence at once instead of word by word, then predict the next token, then the next, until the answer is complete. Every chatbot you have used is a Transformer predicting one token at a time.

:::figure assets/img/internet/aif-transformer.png light
The Transformer: the encoder stack reads the input, the decoder stack writes the output, and attention connects them.
Image: Wikimedia Commons
:::

**Rung 2: Add one layer.** Two halves do the work. The encoder reads and understands the input, turning it into a rich representation. The decoder writes the output one token at a time. Attention is the wiring between them: when producing each token, the model looks back at the input and decides which parts matter most.

:::figure assets/img/mermaid/aif-rung-encoder-decoder.svg light
Encoder and decoder split the job: one understands the input, the other writes the output.
:::

**Rung 3: Exam grade.** Self-attention is attention inside a single sentence: each word looks at every other word and weighs their relevance. In "the animal did not cross the street because it was too tired", self-attention links "it" back to "animal", not "street". That is how the model resolves meaning from context rather than word order. The exam tests this idea, not the math: attention means weighing which words matter for each prediction.

:::figure assets/img/mermaid/aif-rung-attention.svg light
Self-attention: each word weighs the other words, so "it" resolves to "animal" by meaning, not by position.
:::

### Ladder 4: Diffusion and multimodal models

**Rung 1: The plainest picture.** Diffusion models make images from text. They start with pure static noise and gradually remove it, guided by your description, until a picture emerges. Noise in, picture out: that is the whole idea.

:::figure assets/img/mermaid/aif-diffusion.svg light
Diffusion: start from random noise and reverse the noising process step by step, guided by the text prompt, until an image appears.
:::

**Rung 2: Add one layer.** Multimodal models accept and produce more than one kind of input: text, images, audio together. Embeddings are the bridge: text and images are mapped into one shared space, so the model can reason across them ("what is funny about this picture?"). A model that only handles text is unimodal; one that handles several types is multimodal.

:::figure assets/img/mermaid/aif-rung-multimodal.svg light
Multimodal models map text and images into one shared embedding space, then reason across both.
:::

**Rung 3: Exam grade.** Match the model type to the task: text generation means large language models (Transformers); image generation from text means diffusion models; finding similar documents means embedding models. "Multimodal input" in a stem means the model takes more than text. Do not confuse diffusion (creates images) with embeddings (represents meaning as vectors).

### Ladder 5: Foundation models, lifecycle and selection

**Rung 1: The plainest picture.** A foundation model is a huge model pre-trained once on massive data, then adapted to many tasks. Train once, reuse everywhere: that reuse is what makes it a "foundation".

:::figure assets/img/mermaid/aif-fm-lifecycle.svg light
The foundation model lifecycle: pre-train once on broad data, adapt to tasks, evaluate, deploy, and monitor.
:::

**Rung 2: Add one layer.** The lifecycle runs in order: select and prepare data, pre-train the base model, adapt it (fine-tune or align), evaluate it, deploy it, then monitor it in production. Pre-training builds broad knowledge; adaptation aims it at your task. Adaptation is orders of magnitude cheaper than pre-training, which is why almost everyone adapts rather than trains from scratch.

:::figure assets/img/mermaid/aif-fm-lifecycle.svg light
The same lifecycle with the cost insight: pre-training is the expensive once-only step; adaptation is the cheap repeated step.
:::

**Rung 3: Exam grade.** Selecting a model means checking accuracy on your task, cost, latency, and whether its size fits your deployment. Open models (weights public, self-hostable) trade control for operational burden; closed models (API-only) trade convenience for dependence. Model distillation compresses a big capable model into a smaller cheaper one that mimics it: useful when latency or cost bites. Continued pre-training adds domain knowledge before any task adaptation.

:::figure assets/img/mermaid/aif-rung-selection.svg light
Model selection in one check: accuracy on your task, cost, latency, and size fit for deployment.
:::

### Ladder 6: Agents

**Rung 1: The plainest picture.** A chatbot answers questions. An agent takes actions: it books the flight, files the ticket, queries the database. Answers versus actions is the whole distinction.

:::figure assets/img/mermaid/aif-agent-loop.svg light
The agent loop: reason about the goal, act through a tool, observe the result, repeat until done.
:::

**Rung 2: Add one layer.** The agent runs a loop: reason about what to do next, act by calling a tool (an API, a database, a browser), observe the result, and repeat until the goal is reached. Tools are the agent's hands; without them it is just a chatbot. A multi-agent pattern splits the work: several specialized agents collaborate, like a researcher agent feeding a writer agent.

:::figure assets/img/mermaid/aif-agent-loop.svg light
The same loop with the key detail: tools are what turn reasoning into action, and observation is what keeps it on track.
:::

**Rung 3: Exam grade.** The Model Context Protocol (MCP) is the open standard for connecting agents to external systems and data, so tools plug in consistently instead of through one-off integrations. Context engineering means deliberately assembling everything the agent needs (instructions, tools, retrieved facts) into its working context. The exam's agent trigger words: "take actions", "call APIs", "multi-step with tools". If the stem says "answer questions from documents", that is RAG, not agents.

:::details Knowledge check: agent or chatbot?
1. A support widget that answers FAQs from the help center. 2. A system that reads a complaint email, checks the order database, and issues a refund by itself.

**Answers: 1. Chatbot (answers only, no actions). 2. Agent (multi-step: read, query, act through tools).**
:::

### Ladder 7: AWS for building GenAI

**Rung 1: The plainest picture.** Amazon Bedrock is the front door: one API that serves many foundation models from Amazon and others. You pick a model, send a prompt, get text back. No training, no servers.

:::figure assets/img/mermaid/aif-rung-bedrock.svg light
Bedrock as the front door: one API to many models, with Knowledge Bases, Guardrails, and Agents built around it.
:::

**Rung 2: Add one layer.** Around that API, Bedrock bundles the pieces: Knowledge Bases for RAG over your documents, Guardrails for safety filters, Agents for tool-using workflows, Prompt Management for versioning prompts, and Model Evaluation for testing. Amazon Q is the ready-made assistant family: Q Business for company knowledge, Q Developer for coding help. PartyRock is the playground for trying prompts without code.

:::details Knowledge check: which AWS GenAI service?
1. A team wants to query FMs from Amazon, Anthropic, and Meta through one API. 2. HR wants an assistant that answers questions from company wikis. 3. A developer wants code completions in the IDE.

**Answers: 1. Amazon Bedrock (one API, many models). 2. Amazon Q Business (company knowledge assistant). 3. Amazon Q Developer (coding assistant).**
:::

## D3 · Applications of Foundation Models (28%) {#d3-foundation-model-apps}

### Ladder 1: The customization ladder

**Rung 1: The plainest picture.** The cheapest way to change a model's behavior costs nothing: rewrite the prompt. Better instructions, a few examples, a clearer format. This is prompt engineering, and it adds no new knowledge to the model.

:::figure assets/img/mermaid/aif-rung-prompt-anatomy.svg light
A prompt's anatomy: context sets the role, the instruction gives the task, input data supplies the material, the output indicator sets the format.
:::

**Rung 2: Add one layer.** When the model needs facts it was never trained on, fetch them at query time and paste them into the prompt. That is RAG: the model answers from your documents, cites them, and never needs retraining. New knowledge without touching the weights.

:::figure assets/img/mermaid/aif-rag-pipeline.svg light
The RAG pipeline: embed the question, similarity-search the vector store, retrieve the top chunks, build an augmented prompt, generate a cited answer.
:::

**Rung 3: Add one layer.** When the need is behavior rather than facts (your brand voice, your output format), continue training the model on your labeled examples. That is fine-tuning: the new behavior lands in the weights. It costs real money and compute, and the knowledge still goes stale.

:::figure assets/img/mermaid/aif-rung-finetune.svg light
Fine-tuning: a base foundation model plus your labeled examples becomes a customized model with your behavior in its weights.
:::

**Rung 4: Exam grade.** The full decision tree, cheapest first: same knowledge with better answers means prompt engineering; new private or current facts means RAG; new behavior, tone, or style means fine-tuning; whole new base knowledge means pre-training (months, millions, only the largest companies). Two more terms: in-context learning is the fancy name for few-shot prompting (teaching by example with no weight changes), and model distillation compresses a big model into a smaller cheaper one that mimics it.

:::figure assets/img/mermaid/aif-customization-decision.svg light
The customization decision tree: the question "what is missing" picks the method, from prompt engineering up to pre-training.
:::

:::takeaway
The exam's favorite decision: "facts change over time" or "must cite sources" always points to RAG, never fine-tuning. "New tone, format, or behavior" points to fine-tuning or prompt engineering, never RAG.
:::

### Ladder 2: Prompt engineering, rung by rung

**Rung 1: The plainest picture.** A prompt has parts, and naming them helps you fix weak prompts: context (who the model should be), instruction (what to do), input data (the material), output indicator (the format), and negative prompts (what never to do, like "do not invent details").

:::figure assets/img/mermaid/aif-rung-prompt-anatomy.svg light
The same anatomy as a checklist: when a prompt fails, check which part is missing or vague.
:::

**Rung 2: Add one layer.** Techniques stack by power: zero-shot (no examples), one-shot (one example), few-shot (a few examples, also called in-context learning), chain-of-thought ("think step by step" before answering, best for math and multi-step logic). Prompt templates make reusable skeletons with slots for the variable parts.

:::figure assets/img/mermaid/aif-rung-prompt-tech.svg light
Prompt techniques in climbing order: from zero examples up to showing the model the reasoning steps.
:::

**Rung 3: Exam grade.** Production prompting adds discipline: be specific and concise, iterate empirically, version prompts with Bedrock Prompt Management instead of pasting strings into code. And know the attacks: prompt injection (smuggled instructions in user input), jailbreaking (tricks past safety rules), poisoning (corrupted training or retrieval data), hijacking (the task gets redirected).

:::figure assets/img/mermaid/aif-rung-risks.svg light
The four prompt risks: injection smuggles instructions, jailbreaking bypasses rules, poisoning corrupts data, hijacking redirects the task.
:::

:::details Knowledge check: which technique?
A model keeps getting multi-step word problems wrong. Which prompt technique helps most, and why?

**Answer: chain-of-thought.** Asking the model to reason step by step before answering improves multi-step reasoning. Few-shot shows examples; chain-of-thought shows the working.
:::

### Ladder 3: Inference parameters

**Rung 1: The plainest picture.** Temperature is the creativity knob, running from 0 to about 1. Near 0 the model picks the most likely token every time: focused, repeatable, a bit dull. Near 1 it samples more freely: varied, creative, less predictable. Factual work wants 0; brainstorming wants higher.

:::figure assets/img/mermaid/aif-rung-temperature.svg light
Temperature as a knob: near 0 one answer dominates; near 1 many answers are possible.
:::

**Rung 2: Exam grade.** Top-p and top-k trim the candidate pool before sampling: smaller values mean safer, more predictable text. Max tokens caps the response length; hitting the cap truncates the answer mid-sentence. Practical rules: temperature 0 for anything factual or deterministic, and change one knob at a time so you know what helped.

### Ladder 4: Fine-tuning methods

**Rung 1: The plainest picture.** Instruction tuning teaches the model to follow directions: train it on instruction-and-response pairs until it answers in your style and format. Show it what good looks like, repeatedly.

:::figure assets/img/mermaid/aif-rung-finetune.svg light
Instruction tuning: pairs of instructions and ideal responses teach the model your desired behavior.
:::

**Rung 2: Add one layer.** The family grows: domain adaptation trains on your industry's text so the model speaks your vocabulary; transfer learning adapts a pre-trained model to a new but related task; continued pre-training adds domain knowledge before any instruction tuning; RLHF uses human rankings as rewards so the model learns which answers people prefer (this is how models get aligned and polite).

:::figure assets/img/mermaid/aif-rung-finetune.svg light
The same picture with the key distinction: fine-tuning changes behavior in the weights, while RAG would only supply facts.
:::

**Rung 3: Exam grade.** Data preparation decides whether fine-tuning works: curate the dataset (relevant, high quality), label it where the method needs labels, keep it representative of production, and mind governance (consent, PII, licensing). Final exam line: fine-tuning beats RAG when the need is behavior, not facts; RAG beats fine-tuning when facts change or must be cited.

### Ladder 5: Evaluating models

**Rung 1: The plainest picture.** The simplest check is automatic: compare the model's output against a reference answer and score the overlap. Fast, cheap, repeatable. Human judges are the gold standard: slow, expensive, but they catch what metrics miss.

:::figure assets/img/mermaid/aif-rung-eval.svg light
Evaluation routes: automatic metrics for speed, human judges for truth, business metrics for whether users actually benefit.
:::

**Rung 2: Add one layer.** The named metrics: ROUGE measures overlap with reference summaries (summarization), BLEU measures overlap for translation, BERTScore measures semantic similarity via embeddings instead of exact words. LLM-as-a-judge uses a strong model to score a weaker model's outputs: fast and cheap, with its own bias risk. Amazon Bedrock Model Evaluation runs automatic and human evaluations as a managed service.

:::figure assets/img/mermaid/aif-rung-eval.svg light
The same routes with the exam detail: ROUGE for summaries, BLEU for translation, BERTScore for meaning, LLM-as-a-judge for scale.
:::

**Rung 3: Exam grade.** Then check business alignment, because a high BLEU score means nothing if users hate the product: task completion rate, user satisfaction, cost per interaction. Evaluate RAG systems on retrieval quality too (did it fetch the right chunks?), and agents on whether they completed the task with the right tool calls.

:::details Knowledge check: pick the metric
A team fine-tuned a summarization model. Which automatic metric fits, and what is its blind spot?

**Answer: ROUGE, which measures overlap with reference summaries.** Blind spot: it rewards word overlap, so a perfectly good paraphrase can score badly. Pair it with human evaluation or LLM-as-a-judge for meaning.
:::

### Ladder 6: Agents in production on AWS

**Rung 1: The plainest picture.** Bedrock Agents turn a foundation model into a worker: you give it a goal, instructions, and action groups (the tools it may call), and it reasons through multi-step tasks.

:::figure assets/img/mermaid/aif-rung-agent-aws.svg light
Agents on AWS: Bedrock Agents orchestrate, AgentCore hosts in production with identity and policy, Strands is the open-source SDK.
:::

**Rung 2: Add one layer.** Demos are easy; production is the exam's concern. Amazon Bedrock AgentCore is the production home: a runtime plus Identity (which identity the agent acts as) plus Policy (what the agent is allowed to do). Strands Agents is the open-source SDK for building agents in code.

:::figure assets/img/mermaid/aif-rung-agent-aws.svg light
The same map with the production insight: Identity says who the agent is, Policy says what it may touch.
:::

**Rung 3: Exam grade.** The exam's agent trigger words stay constant: "take actions", "call APIs", "multi-step with tools". If the stem says "answer questions from documents", pick RAG. If it says the agent must file tickets, query systems, or book things, pick Bedrock Agents on AgentCore.

<div class="vid" data-vid="iQNc3D_WTG0">
<div class="vid-frame"><iframe id="ytf-iQNc3D_WTG0" src="https://www.youtube-nocookie.com/embed/iQNc3D_WTG0?enablejsapi=1&rel=0" title="AIF-C01 Exam Prep: RAG, Bedrock Agents and Amazon Q, 15 Questions Explained (How To Center)" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
<div class="vid-bar" role="group" aria-label="Playback speed"><span class="lbl">Speed:</span><button type="button" data-speed="0.5">0.5x</button><button type="button" data-speed="0.75">0.75x</button><button type="button" data-speed="1" class="on">1x</button><button type="button" data-speed="1.25">1.25x</button><button type="button" data-speed="1.5">1.5x</button><button type="button" data-speed="1.75">1.75x</button><button type="button" data-speed="2">2x</button></div>
<p class="vid-note"><strong>Watch:</strong> AWS AI Practitioner Exam Prep: RAG, Bedrock Agents and Amazon Q, 15 Questions Explained, by How To Center. Transcript-checked: 15 exam-style Domain 3 questions with full explanations of why each wrong option is wrong, covering vector stores, Bedrock Agents, Q Business vs Q Developer, model selection, fine-tuning tradeoffs, provisioned throughput, and grounding. Pause and answer before the reveal.</p>
</div>
## D4 · Guidelines for Responsible AI (14%) {#d4-responsible-ai}

### Ladder 1: Bias and fairness

**Rung 1: The plainest picture.** Bias means the system treats some groups worse than others. A hiring model that favors one group, a voice assistant that misunderstands one accent. The model learned it from the data, and now it repeats it at scale.

:::figure assets/img/mermaid/aif-rung-bias.svg light
Bias in one picture: biased training data teaches the model the bias, and the model produces unfair predictions.
:::

**Rung 2: Add one layer.** Bias enters through three doors. Historical bias: the data reflects past discrimination (old hiring records that favored one group). Sampling bias: the data does not represent everyone (a voice model trained on one accent). Label bias: the labels themselves encode prejudice. A model can be highly accurate on average and still be unfair to a subgroup.

:::figure assets/img/mermaid/aif-rung-bias.svg light
The same picture with the exam question attached: which door did the bias enter through, historical, sampling, or label?
:::

**Rung 3: Exam grade.** The guide's fairness features: fairness (no group systematically disadvantaged), inclusivity (works for diverse users), safety, veracity (truthful outputs). Fight bias with subgroup analysis (measure performance per group, not just overall) and healthy datasets (inclusive, diverse, curated from trustworthy sources, balanced). The D1 link: high bias underfits, high variance overfits; a biased model is often a high-bias model. Legal risks the exam names: IP infringement from reproducing copyrighted text, discrimination liability from biased outputs, loss of customer trust, and hallucinations presented as fact. Sustainability counts too: training and running large models costs real energy, so the smallest model that meets the need is the responsible pick.

### Ladder 2: The responsible-AI toolkit

**Rung 1: The plainest picture.** Two tools do the daily work. Guardrails sit around the model and filter what goes in and out: block toxicity, redact PII, refuse off-topic requests. Clarify inspects the model itself: it finds bias in data and models and explains individual predictions.

:::figure assets/img/mermaid/aif-rung-guardrails.svg light
Guardrails as filters: inputs are screened before the model, outputs are screened after, and only safe answers reach the user.
:::

**Rung 2: Add one layer.** Three more complete the kit. Model Cards document a model's facts: intended use, training data, metrics, limitations. A2I (Augmented AI) routes low-confidence or sensitive predictions to human reviewers. Model Monitor watches deployed models for drift and quality drops, because a model that was fair at launch can drift.

:::figure assets/img/mermaid/aif-rung-toolkit.svg light
The toolkit at a glance: Clarify finds bias, Guardrails block bad content, Model Cards document, A2I brings in humans.
:::

**Rung 3: Exam grade.** Match the tool to the verb: "detect bias" means Clarify; "filter outputs" means Guardrails; "document the model" means Model Cards; "human review" means A2I; "watch production" means Model Monitor. Guardrails also run contextual grounding checks that catch hallucinations.

:::takeaway
Exam pairing: Clarify finds bias, Guardrails blocks bad content, Model Cards document the model, A2I brings in humans. Match the tool to the verb in the stem: "detect bias" is Clarify, "filter outputs" is Guardrails.
:::

:::details Knowledge check: which responsible-AI tool?
1. A bank must prove its loan model does not discriminate by zip code. 2. A chatbot must refuse to output personal phone numbers. 3. A hospital wants a doctor to review every AI-flagged scan before action.

**Answers: 1. SageMaker Clarify (detect bias, subgroup analysis). 2. Bedrock Guardrails (filter PII in outputs). 3. Amazon A2I (human review workflow).**
:::

### Ladder 3: Transparency and explainability

**Rung 1: The plainest picture.** Transparent means you can see how the system works: open weights, documented data, clear licensing. Explainable means you can say why it made a specific decision. These are different things, and the exam separates them exactly this way.

:::figure assets/img/mermaid/aif-rung-transparency.svg light
Transparent vs explainable: you can have full visibility into a model and still not know why it made one decision.
:::

**Rung 2: Exam grade.** A model can be transparent without being explainable: you can read every weight of a huge neural network and still not know why it denied a loan. The tradeoff the exam names: the most capable models tend to be the least interpretable, so measure both and choose consciously. Helpers: Model Cards and Clarify, Bedrock Model Evaluations, open models with open data. Human-centered design keeps people in charge: show users when AI is involved, give feedback mechanisms ("this answer was wrong"), and keep a human in the loop for high-stakes calls.

## D5 · Security, Compliance, and Governance (14%) {#d5-security-governance}

### Ladder 1: The shared responsibility model for AI

**Rung 1: The plainest picture.** AWS secures the building: data centers, network, hardware. You secure your rooms: your data, who can access it, how it is encrypted. If you leave your door open, that is on you.

:::figure assets/img/mermaid/aif-rung-shared-resp.svg light
Shared responsibility: AWS secures the cloud itself; you secure what you put in it.
:::

**Rung 2: Add one layer.** For AI workloads the split gets specific. AWS handles the managed infrastructure under Bedrock and SageMaker. You handle IAM (who can call what, with least privilege), encryption settings and KMS keys, network access (VPC, PrivateLink), and the AI choices themselves: which model, how guardrails are configured, what the prompts contain.

:::figure assets/img/mermaid/aif-rung-shared-resp.svg light
The same split with the AI details: your side holds IAM, KMS, network access, prompts, documents, and model choice.
:::

**Rung 3: Exam grade.** Two Bedrock privacy facts the exam loves: Bedrock does not train its base models on your prompts or data, and your fine-tuned customizations stay private to your account. Your inputs are encrypted and never shared with model providers. Data residency (some data must stay in a specific region) and retention rules are also your responsibility.

:::details Knowledge check: who is responsible?
A company stores customer chat logs in S3 and uses them to fine-tune a Bedrock model. The S3 bucket is left public. Whose failure is that under the shared responsibility model?

**Answer: the customer's.** AWS secures the S3 infrastructure; access control on the bucket is the customer's job. Same for IAM policies, KMS settings, and what data they choose to upload.
:::

### Ladder 2: Securing the AI system

**Rung 1: The plainest picture.** Lock the doors first. IAM roles and policies with least privilege: grant only the access needed, nothing more. A Bedrock-calling app gets permission to invoke models, not admin over the account. Encrypt data at rest with KMS and in transit with TLS. Secrets (API keys, passwords) go in Secrets Manager, never in code.

:::figure assets/img/mermaid/aif-rung-secure.svg light
The three locks: IAM for least-privilege access, KMS for encryption, Secrets Manager for credentials.
:::

**Rung 2: Add one layer.** Then shrink the attack surface. Keep traffic off the public internet with VPC endpoints (PrivateLink) to Bedrock and S3. Scan S3 with Macie to find PII before it ever reaches a training set. Filter live inputs and outputs with Bedrock Guardrails: toxicity filters, PII redaction, topic blocking, grounding checks. For agents, AgentCore Identity says who the agent acts as and Policy caps what it may do.

:::figure assets/img/mermaid/aif-rung-secure.svg light
The same locks extended: network isolation, PII scanning, and content filtering layer on top of access control.
:::

**Rung 3: Exam grade.** Name the AI-specific threats: prompt injection (malicious instructions smuggled in input), data leakage (the model revealing private training or retrieved data), toxicity in outputs. Defenses: validate and filter inputs, give tools least-privilege access, filter and validate outputs, and keep an audit trail with CloudTrail logging every API call. Grounding fights hallucinations: RAG grounding (answers from retrieved documents), output validation (check answers against rules), confidence scoring (route low-confidence answers to humans via A2I). Data lineage answers "where did this data come from": document origins with cataloging and Model Cards, cite sources in RAG answers.

### Ladder 3: Governance and compliance

**Rung 1: The plainest picture.** Governance means rules for data's whole life: how it is collected, where it lives, how long it is kept, who touched it. Without rules, nobody can prove anything to an auditor.

:::figure assets/img/mermaid/aif-rung-govern.svg light
The data lifecycle that governance covers: collect, store, use, then retain or delete on a defined schedule.
:::

**Rung 2: Add one layer.** AWS provides the toolkit. CloudTrail logs every API call: the audit trail. Config checks resources against compliance rules and records configuration history. Audit Manager collects evidence for audits automatically. Artifact gives on-demand access to AWS's own compliance reports (SOC, ISO, PCI). Trusted Advisor checks your account against best practices. Inspector finds software vulnerabilities in EC2 and containers.

:::figure assets/img/mermaid/aif-rung-govern.svg light
The same lifecycle with the watchers attached: logging, compliance rules, evidence collection, and best-practice checks.
:::

**Rung 3: Exam grade.** Match the tool to the verb: "log API calls" is always CloudTrail; "check compliance rules" is Config; "gather audit evidence" is Audit Manager; "read AWS compliance reports" is Artifact; "best-practice advice" is Trusted Advisor. Processes matter as much as tools: written policies, a regular review cadence, team training on AI risks, and the Generative AI Security Scoping Matrix for deciding how much scrutiny each use case needs. Transparency standards: document what the system does, what data it uses, and where humans stay in the loop.

:::takeaway
Exam pairing: Config checks compliance, Audit Manager gathers audit evidence, Artifact holds AWS's compliance reports, CloudTrail logs API calls, Trusted Advisor gives best-practice advice. "Prove to an auditor" points to Audit Manager or Artifact. "Log API activity" is always CloudTrail.
:::

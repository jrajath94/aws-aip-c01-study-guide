#!/usr/bin/env python3
"""Build volume-question-patterns.html: how-AWS-asks pattern guide + original 80-question bank.
All questions are original scenarios written for this volume. No question is copied
from any public source. Facts verified against live AWS docs on 2026-09-28.
"""
import html, json, random, re, sys

OUT = "/home/hatch/workspace/your_files/aws-aip-c01-cert/volume-question-patterns.html"

PALETTE = {
    "paper": "#F8F7F3", "ink": "#24292F", "muted": "#5C6570", "blue": "#1F5FBF",
    "board": "#163D7A", "amber": "#A15C07", "card": "#FFFFFF", "codebg": "#EFF0EA",
    "rule": "#E3E0D8",
}

CSS = """
*{box-sizing:border-box}
body{margin:0;background:#F8F7F3;color:#24292F;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;line-height:1.65;font-size:16px}
a{color:#1F5FBF;text-decoration:none}a:hover{text-decoration:underline}
.rail{position:fixed;top:0;left:0;bottom:0;width:250px;background:#163D7A;color:#fff;overflow-y:auto;padding:22px 18px}
.rail h2{font-size:13px;text-transform:uppercase;letter-spacing:.08em;color:#bcd2f5;margin:18px 0 8px}
.rail a{display:block;color:#dbe7fb;padding:5px 8px;border-radius:6px;font-size:14px}
.rail a:hover{background:#1F5FBF;color:#fff;text-decoration:none}
.rail .brand{font-weight:700;font-size:16px;color:#fff;margin-bottom:4px}
.rail .sub{font-size:12px;color:#9db9e8;margin-bottom:10px}
.main{margin-left:250px;padding:36px 48px;max-width:calc(72ch + 96px)}
.main .col{max-width:72ch}
h1{font-size:30px;margin:0 0 8px}h2{font-size:23px;margin:38px 0 12px;padding-top:8px;border-top:2px solid #E3E0D8}h3{font-size:18px;margin:26px 0 8px}h4{font-size:16px;margin:20px 0 6px}
.kicker{color:#5C6570;font-size:14px;margin-bottom:6px}
.badge{display:inline-block;font-size:12px;font-weight:700;padding:2px 10px;border-radius:20px;margin-right:6px;vertical-align:middle}
.b-easy{background:#e6f2e6;color:#1e6b1e}.b-med{background:#fdf0dc;color:#A15C07}.b-hard{background:#fbe4e4;color:#a02020}
.b-fmt{background:#e3ecfa;color:#1F5FBF}.b-dom{background:#EFF0EA;color:#24292F}
.card{background:#FFFFFF;border:1px solid #E3E0D8;border-radius:10px;padding:20px 22px;margin:18px 0}
.stem{font-size:16px;margin:6px 0 12px}
.opts{list-style:none;padding:0;margin:10px 0}
.opts li{padding:8px 12px;border:1px solid #E3E0D8;border-radius:8px;margin:7px 0;background:#F8F7F3}
.opts li b{color:#1F5FBF;margin-right:8px}
details{margin-top:12px;border:1px solid #E3E0D8;border-radius:8px;background:#fff}
summary{cursor:pointer;padding:10px 14px;font-weight:700;color:#1F5FBF}
.ans{padding:4px 18px 16px}
.ans .correct{font-weight:700;color:#1e6b1e}
.whywrong{margin:8px 0}.whywrong li{margin:5px 0}
.trap{background:#fdf0dc;border-left:4px solid #A15C07;padding:10px 14px;border-radius:0 8px 8px 0;margin:12px 0;font-size:15px}
.pattern{background:#FFFFFF;border:1px solid #E3E0D8;border-radius:10px;padding:20px 22px;margin:18px 0}
.pattern h3{margin-top:0;color:#163D7A}
table{border-collapse:collapse;width:100%;margin:12px 0;font-size:15px}
th,td{border:1px solid #E3E0D8;padding:8px 10px;text-align:left;vertical-align:top}
th{background:#163D7A;color:#fff}
tr:nth-child(even) td{background:#f4f3ee}
code{background:#EFF0EA;padding:1px 6px;border-radius:4px;font-size:14px}
pre{background:#EFF0EA;padding:14px;border-radius:8px;overflow-x:auto;font-size:13.5px;line-height:1.55}
.diagram{background:#fff;border:1px solid #E3E0D8;border-radius:10px;padding:18px;margin:14px 0}
.chip{display:inline-block;background:#e3ecfa;color:#163D7A;border-radius:6px;padding:2px 10px;font-size:13px;font-weight:600;margin:2px}
.flow{display:flex;flex-wrap:wrap;gap:0;align-items:stretch;margin:12px 0}
.fbox{background:#fff;border:2px solid #1F5FBF;border-radius:8px;padding:10px 14px;font-size:14px;font-weight:600;max-width:180px}
.farr{align-self:center;font-size:22px;color:#1F5FBF;padding:0 8px;font-weight:700}
.note{background:#eef4fd;border-left:4px solid #1F5FBF;padding:10px 14px;border-radius:0 8px 8px 0;margin:12px 0;font-size:15px}
.warn{background:#fff8ec;border-left:4px solid #A15C07;padding:10px 14px;border-radius:0 8px 8px 0;margin:12px 0;font-size:15px}
.toc-rail{font-size:13px}
footer{margin:40px 0 20px;color:#5C6570;font-size:13px;border-top:1px solid #E3E0D8;padding-top:14px}
@media(max-width:900px){.rail{display:none}.main{margin-left:0;padding:20px}}
"""

GUIDE_HTML = """
<div class="kicker">AWS Certified Generative AI Developer Professional (AIP-C01)</div>
<h1>Question Patterns: How AWS Asks</h1>
<p class="kicker">Pattern guide plus an original 80-question bank across all five domains and all four question formats. Last verified against live AWS documentation: <b>2026-09-28</b>.</p>

<div class="note"><b>How to use this volume.</b> Part 1 teaches the six question patterns AWS uses, with the anatomy of each stem, what the distractors look like, and a concrete attack plan. Part 2 is the bank: 80 original scenario questions. Every question hides its answer in a collapsible panel that explains why the correct answer is right, why each distractor is wrong, and names the trap AWS set. Work each question closed-book, then open the panel.</div>

<h2 id="p0">The exam surface, in one page</h2>
<div class="card"><div class="col">
<table>
<tr><th>Fact</th><th>Value</th></tr>
<tr><td>Questions</td><td>75 total: 65 scored plus 10 unscored (unscored are not identified)</td></tr>
<tr><td>Time</td><td>180 minutes, about 2.4 minutes per question</td></tr>
<tr><td>Pass mark</td><td>750 on a 100 to 1000 scaled score</td></tr>
<tr><td>Scoring</td><td>Compensatory: only the overall score matters, no per-domain minimum</td></tr>
<tr><td>Formats</td><td>Multiple choice, multiple response, ordering, matching</td></tr>
<tr><td>Partial credit</td><td>None. Multiple response and the newer formats are all-or-nothing. Unanswered counts as incorrect, and there is no penalty for guessing, so never leave a question blank.</td></tr>
<tr><td>Domain weights</td><td>D1 Foundation Model Integration, Data, Compliance 31%. D2 Implementation and Integration 26%. D3 AI Safety, Security, Governance 20%. D4 Operational Efficiency and Optimization 12%. D5 Testing, Validation, Troubleshooting 11%.</td></tr>
</table>
</div></div>

<h2 id="p1">Pattern 1: the scenario multiple-choice question</h2>
<div class="pattern">
<h3>Anatomy of the stem</h3>
<p>Nearly every scored question follows this shape: 3 to 6 sentences of scenario, then a hard list of constraints, then a discriminator phrase. Learn to see the three layers:</p>
<div class="diagram">
<p><b>Layer 1, the situation</b> (1 to 2 sentences): who is building what. Example: "A company is building a support assistant over its product manuals."</p>
<p><b>Layer 2, the constraints</b> (the actual test): latency, cost, region, compliance, team skill, data freshness. <span class="chip">sub-3-second latency</span> <span class="chip">data must stay in the EU</span> <span class="chip">no ML engineers on the team</span> <span class="chip">documents update weekly</span></p>
<p><b>Layer 3, the discriminator</b>: "Which solution will meet these requirements <b>with the LEAST operational overhead</b>?" or "<b>MOST cost-effectively</b>?" or "Which is the <b>MOST correct</b>?"</p>
</div>
<h3>What the distractors look like</h3>
<table>
<tr><th>Distractor species</th><th>How to spot it</th></tr>
<tr><td>The one-constraint violator</td><td>Satisfies three constraints, silently breaks the fourth. Example: single-region high availability when the stem demanded regional failover.</td></tr>
<tr><td>The wrong-plane tool</td><td>A real service doing a job it does not do: Bedrock Guardrails used to <i>extract</i> data, CloudTrail used for <i>metrics</i>, Amazon Translate used for <i>PII protection</i>.</td></tr>
<tr><td>The custom build</td><td>Self-managed EC2, hand-rolled orchestration, or training a custom model where a managed service or prompt work would do. Almost never correct unless the stem explicitly requires something no managed service offers.</td></tr>
<tr><td>The right service, wrong mechanism</td><td>CloudFormation for runtime model switching (a deployment, not runtime config), EventBridge as a configuration store, ElastiCache as a durable vector store.</td></tr>
</table>
<h3>Attack plan</h3>
<p>1. Read the stem and underline each constraint. 2. Turn each constraint into one architectural decision (weekly doc updates = sync schedule, not one-time load). 3. Eliminate every option that violates even one constraint. 4. Among survivors, apply the Maarek heuristic: prefer the more managed, more serverless, lower-overhead option. 5. If two options survive, re-read the discriminator: it is pointing at the implicit constraint (cost, overhead, security) that separates them.</p>
</div>

<h2 id="p2">Pattern 2: multiple response (select TWO / THREE)</h2>
<div class="pattern">
<h3>Anatomy</h3>
<p>Five or more options, "Select TWO" or "Select THREE". All-or-nothing scoring: one wrong pick zeroes the question. This format punishes shaky knowledge because you must rule out <i>every</i> distractor individually.</p>
<h3>What the distractors look like</h3>
<p>AWS pairs one genuinely correct option with a near-miss that shares vocabulary with it. Classic pair: <b>prompt caching</b> (repeated large static prefixes, a cost lever) next to <b>Provisioned Throughput</b> (steady baseline traffic, a latency and throughput guarantee). The stem mentions cost; the trap option is the throughput answer.</p>
<h3>Attack plan</h3>
<p>Judge each option on its own, never as a pair. Ask of each: "does this independently satisfy a stated constraint?" Beware the option that is true in general but wrong for this scenario (SageMaker Model Monitor is a fine service, just built for tabular ML drift, not GenAI text quality). Count your selections before moving on: "Select THREE" with two picked is a guaranteed zero.</p>
</div>

<h2 id="p3">Pattern 3: ordering (place steps in sequence)</h2>
<div class="pattern">
<h3>Anatomy</h3>
<p>Three to five steps, all plausible, one correct sequence. AWS tests lifecycle and debug order: agent setup, RAG debugging, deployment promotion, defense-in-depth layering.</p>
<h3>Attack plan</h3>
<p>Find the anchors first: what must be first, what must be last. Then chain the middle. Two anchors AWS loves:</p>
<div class="diagram"><div class="flow">
<div class="fbox">Configure agent (action groups, KB)</div><div class="farr">></div>
<div class="fbox">Run prepare-agent</div><div class="farr">></div>
<div class="fbox">Create alias (prod)</div><div class="farr">></div>
<div class="fbox">Invoke with sessionId</div>
</div>
<p style="font-size:14px;color:#5C6570">Anchor logic: you cannot alias an unprepared agent, and you cannot invoke a production alias that does not exist. "Prepare, then alias, then invoke" is fixed; the only question is what comes before prepare.</p></div>
<p>The same anchor logic works for debugging: check the cheapest, most-likely layer first (retrieval quality before generation model; request body format before IAM policy).</p>
</div>

<h2 id="p4">Pattern 4: matching (pair items from two lists)</h2>
<div class="pattern">
<h3>Anatomy</h3>
<p>Two short lists, for example guardrail controls on the left and scenario needs on the right. Every pair must be correct; one wrong pair zeroes the question.</p>
<h3>Attack plan</h3>
<p>Match the pairs you are certain about first, then eliminate. The exam builds these around its favorite confusion sets: denied topics vs content filters vs word filters vs sensitive-information filters; inference profiles vs prompt routers vs Provisioned Throughput; Converse vs InvokeModel vs batch. If you can name the confusion set, you can solve the matching question in under a minute.</p>
</div>

<h2 id="p5">Pattern 5: the MOST-correct discriminator</h2>
<div class="pattern">
<h3>Anatomy</h3>
<p>Two options are both defensible. The stem contains an implicit constraint the weaker option ignores. The three implicit constraints behind most AIP-C01 questions:</p>
<div class="diagram"><div class="flow">
<div class="fbox">Reduce operational overhead</div><div class="farr">></div>
<div class="fbox">Improve security and responsible AI</div><div class="farr">></div>
<div class="fbox">Cut latency or cost without breaking the explicit constraints</div>
</div></div>
<h3>Attack plan</h3>
<p>When two options both work, pick the one that also satisfies the implicit filters: managed over self-built, serverless over servers, least privilege over broad access, evaluated over assumed. The exam is a professional-level test; it rewards the answer a careful senior engineer would defend in a design review.</p>
</div>

<h2 id="p6">Pattern 6: the anti-pattern trap ("a developer proposes...")</h2>
<div class="pattern">
<h3>Anatomy</h3>
<p>The stem describes a plausible-sounding plan built on a real service used for the wrong job, then asks what is wrong with it. You are not choosing an architecture; you are diagnosing a category error.</p>
<h3>The master trap catalog (drilled across this bank)</h3>
<table>
<tr><th>#</th><th>The trap</th><th>The correction</th></tr>
<tr><td>1</td><td>Lambda for long-running orchestration with waits or approvals</td><td>Step Functions; Lambda caps at 15 minutes per invocation</td></tr>
<tr><td>2</td><td>InvokeModel vs Converse confusion</td><td>Converse: unified multi-provider calls, tool use, guardrails inline, structured output. InvokeModel: provider-specific request bodies and embeddings</td></tr>
<tr><td>3</td><td>Guardrail control confusion</td><td>Denied topics (subject bans) vs content filters (toxicity categories) vs word filters (exact strings) vs sensitive-info filters (PII block or mask)</td></tr>
<tr><td>4</td><td>Prompt caching vs Provisioned Throughput</td><td>Caching attacks repeated-prefix cost; Provisioned Throughput buys latency and throughput guarantees for steady baselines</td></tr>
<tr><td>5</td><td>Inference profiles vs prompt routers vs Provisioned Throughput</td><td>Profiles: availability and resilience routing. Routers: cost and quality routing by prompt complexity. Provisioned Throughput: reserved capacity</td></tr>
<tr><td>6</td><td>One shared knowledge base for multi-tenant data</td><td>Separate knowledge bases with IAM isolation, not prompt instructions</td></tr>
<tr><td>7</td><td>Fine-tuning when RAG or prompting suffices; RAG when economics point to distillation or caching</td><td>Climb the ladder: prompt, RAG, agents, fine-tune, and stop at the cheapest step that works</td></tr>
<tr><td>8</td><td>CloudFormation or EventBridge for runtime model switching</td><td>AppConfig feature flags plus Lambda routing plus API Gateway</td></tr>
<tr><td>9</td><td>S3 for session memory; ElastiCache as a durable vector store; DynamoDB as a vector store</td><td>DynamoDB for session state; OpenSearch Serverless, Aurora pgvector, or S3 Vectors for vectors</td></tr>
<tr><td>10</td><td>Kendra vs Knowledge Bases; Q Business vs Q Developer</td><td>Kendra: enterprise search. Knowledge Bases: RAG. Q Business: enterprise assistant over company data. Q Developer: IDE coding assistant</td></tr>
<tr><td>11</td><td>Raising Provisioned Throughput when code never routes to the provisioned model</td><td>Invoke the provisioned model ARN; capacity is not the bug, routing is</td></tr>
<tr><td>12</td><td>Provisioned Throughput to fix nondeterministic outputs</td><td>Temperature and prompt control fix consistency; throughput fixes capacity</td></tr>
<tr><td>13</td><td>Custom or manual builds where a managed service exists</td><td>The exam default bias: managed first</td></tr>
<tr><td>14</td><td>CloudTrail for metrics; Glue plus Athena for real-time detection</td><td>CloudTrail is audit; CloudWatch is metrics; Bedrock evaluations plus anomaly detection are the GenAI-native answer</td></tr>
<tr><td>15</td><td>The base model's built-in safety as the complete safety answer</td><td>Never sufficient for a sensitive audience; layer guardrails and review</td></tr>
</table>
</div>

<h2 id="p7">Exam-day tactics</h2>
<div class="card"><div class="col">
<p><b>Budget 2 to 2.5 minutes per question.</b> Long stems are front-loaded: read the last sentence first (it holds the actual question), then scan the stem for constraints. Flag scenario questions with four or more constraints and return to them; bank the quick definition-adjacent ones early.</p>
<p><b>Never leave a question blank.</b> There is no guessing penalty and unanswered counts as incorrect. On multiple response, an educated partial guess still beats a blank, but remember: only a fully correct set earns credit, so spend the time to rule out each option.</p>
<p><b>Think like an architect, not a coder.</b> The exam does not test SDK syntax or exact API parameters. It tests: which service, which integration pattern, sync vs async, which guardrail control, which cost lever, which evaluation method, and what order of operations.</p>
<p><b>Ten questions are unscored and unmarked.</b> If a question feels alien or oddly specific, it may be an unscored field-test item. Answer it sensibly and move on; do not let it rattle you.</p>
</div></div>
"""

NAV = [
    ("p0", "Exam surface"),
    ("p1", "P1 Scenario MC"),
    ("p2", "P2 Multi-response"),
    ("p3", "P3 Ordering"),
    ("p4", "P4 Matching"),
    ("p5", "P5 MOST-correct"),
    ("p6", "P6 Anti-pattern traps"),
    ("p7", "Exam-day tactics"),
    ("bank", "Question bank"),
    ("verify", "Verification log"),
]

QUESTIONS = []

# ---------------- Domain 1 (Q1-Q25) ----------------
QUESTIONS += [
dict(id="Q1", domain="D1", difficulty="Easy", format="mc",
stem="A company wants a GenAI assistant that answers questions from its internal HR handbook. The CTO will only fund production work after the team demonstrates the approach on real documents. The team has two AWS developers and no ML specialists. What should the team do first?",
options=[
"Run a proof of concept on Amazon Bedrock with on-demand invocation over a sample of the handbook documents",
"Fine-tune a foundation model on the full handbook and purchase Provisioned Throughput before any testing",
"Build a custom training pipeline on Amazon SageMaker AI to pre-train a model on HR text",
"Deploy a multi-region production architecture with cross-region inference profiles"],
correct=[0],
why="The exam rewards validating feasibility, performance, and business value with a low-setup proof of concept before committing to expensive options like fine-tuning or Provisioned Throughput. Bedrock on-demand needs no capacity commitment and no ML specialists.",
why_wrong=[
"Fine-tuning plus Provisioned Throughput before any validation inverts the correct order: it commits cost and complexity before knowing the approach works. Fine-tuning is also the wrong tool for document Q and A, which is a retrieval problem.",
"Pre-training a custom model is model development, which the exam guide lists as out of scope, and it is wildly disproportionate for answering questions from one handbook.",
"Multi-region production architecture skips validation entirely and adds cost and complexity before the approach is proven."],
trap="Pattern 1: the stem says 'demonstrates the approach first'. Any option that commits production spend before validation violates that constraint."),

dict(id="Q2", domain="D1", difficulty="Medium", format="mr", select=2,
stem="A platform team wants every product squad to ship GenAI features in a consistent, reviewable way. Which TWO practices align with the AWS Well-Architected Generative AI Lens guidance for standardized, reusable components? (Select TWO)",
options=[
"Build prompt templates, model routing layers, guardrail policies, and evaluation harnesses once and reuse them across squads",
"Let each squad pick its own models, prompts, and safety controls with no shared review so teams move faster",
"Run architecture design reviews against the Generative AI Lens before production deployments",
"Require every squad to fine-tune its own foundation model so each feature has a dedicated model",
"Standardize on invoking models only through raw HTTP calls with hardcoded credentials in each service"],
correct=[0,2],
why="The Generative AI Lens exists precisely for design reviews of GenAI workloads, and its guidance pushes standardized reusable components (templates, routing, guardrails, eval harnesses) so safety and quality do not depend on each squad reinventing them.",
why_wrong=[
"No shared review or standards is the opposite of the Lens guidance; it guarantees inconsistent safety and duplicated work.",
"Per-squad fine-tuning multiplies cost and operational burden for no stated benefit; fine-tuning is for baked-in behavior needs, not a standardization strategy.",
"Hardcoded credentials violate basic security practice and have nothing to do with standardization; centralized, managed access is the exam answer."],
trap="Pattern 2: option B sounds agile ('move faster') but directly contradicts the standardization constraint in the stem."),

dict(id="Q3", domain="D1", difficulty="Medium", format="ordering",
stem="Place these Generative AI lifecycle stages in the order the Well-Architected Generative AI Lens presents them, from first to last.",
steps=[
"Scoping: define the business problem and success criteria",
"Model selection: choose and evaluate candidate foundation models",
"Customization: adapt the model with RAG, agents, or fine-tuning as needed",
"Integration: connect the solution to applications and data",
"Deployment and continuous improvement: release, monitor, and iterate"],
why="The Lens frames GenAI work as a lifecycle: scope the problem first, then select a model against the requirements, then customize only as far as needed, then integrate, then deploy with continuous improvement. Customization before selection is a classic exam inversion.",
trap="Pattern 3: watch for 'customization before model selection' orderings; the Lens selects first, then customizes.",
why_wrong=[
"Placing customization before model selection inverts the lifecycle: you cannot adapt a model you have not chosen yet.",
"Putting integration before customization skips the adaptation stage the Lens requires before connecting to applications.",
"Starting with deployment means building before scoping the problem, which the Lens lists as the mandatory first stage."],
),
dict(id="Q4", domain="D1", difficulty="Medium", format="mc",
stem="A support assistant must answer from 5,000 policy documents that are reissued every quarter. The team debates fine-tuning a model on the documents versus building retrieval over them. Which approach is MOST correct, and why?",
options=[
"Retrieval-augmented generation over a knowledge base, because quarterly updates only require re-syncing documents, and answers can cite sources",
"Fine-tuning, because a fine-tuned model memorizes the documents and never needs the documents at inference time",
"Fine-tuning, because retrieval cannot handle 5,000 documents",
"Prompt engineering alone, because 5,000 documents fit in a single prompt"],
correct=[0],
why="Quarterly document updates plus a need for current answers is the textbook RAG signal: updating means re-syncing a data source, not retraining. RAG also gives source attribution, which fine-tuning cannot.",
why_wrong=[
"Fine-tuning bakes knowledge into weights; every quarterly reissue would require retraining, and the model cannot cite sources. This is trap 7.",
"Retrieval handles far larger corpora than 5,000 documents; scale is not the issue, freshness and attribution are.",
"5,000 documents do not fit in any prompt; context-window stuffing fails on both size and cost, and it provides no update story."],
trap="Pattern 6, trap 7: fine-tuning when the scenario says documents update regularly or answers must cite sources. That is RAG."),

dict(id="Q5", domain="D1", difficulty="Medium", format="mc",
stem="A company is launching a customer FAQ assistant in 30 languages. The team is debating whether to train a custom multilingual model. What is the MOST correct guidance?",
options=[
"Use Bedrock foundation models that already support the required languages; training a custom model for language coverage alone is unnecessary",
"Train a custom multilingual model because only custom models can handle 30 languages reliably",
"Build 30 separate single-language assistants, one per language, to avoid multilingual models entirely",
"Use machine translation on every request instead of a multilingual model because translation is always cheaper"],
correct=[0],
why="Foundation models on Bedrock already cover dozens of languages. The exam punishes training custom models for capabilities the base models already have; custom training is reserved for baked-in behavior, not language coverage.",
why_wrong=[
"Custom multilingual training is model development: out of scope for this exam and disproportionate when base models already cover the languages.",
"Thirty separate assistants multiplies operational overhead by thirty for no benefit; it violates the reduce-overhead filter.",
"Translation on every request adds latency, cost, and error stacking on every turn, and it is not 'always cheaper'; it also does nothing for generation quality."],
trap="Pattern 5: training a custom model sounds thorough, but it fails the operational-overhead and managed-first filters."),

dict(id="Q6", domain="D1", difficulty="Easy", format="mc",
stem="Operations must switch a production assistant between three foundation models without code deployments or restarts. Model identifiers are currently hardcoded in the application. Which change meets the requirement with the least operational overhead?",
options=[
"Store model identifiers in AWS AppConfig as runtime configuration, with a Lambda routing layer reading the current value and API Gateway fronting a stable endpoint",
"Store model identifiers in CloudFormation parameters and update the stack whenever operations wants a switch",
"Publish the model identifiers to an EventBridge event bus and have the application poll for events",
"Email the new model identifier to the on-call engineer, who updates the code and redeploys"],
correct=[0],
why="AppConfig is the exam's canonical runtime configuration mechanism: feature flags and values change without redeployments. Lambda holds the routing logic, API Gateway keeps the client-facing endpoint stable.",
why_wrong=[
"CloudFormation parameter updates are deployments, which directly violates the 'without code deployments' constraint. This is trap 8.",
"EventBridge routes events; it is not a configuration store. Polling an event bus for config is a category error.",
"Manual code edits and redeploys are exactly what the requirement forbids, plus they are slow and error-prone."],
trap="Pattern 1, trap 8: CloudFormation for runtime switching. A stack update is a deployment, not runtime configuration."),

dict(id="Q7", domain="D1", difficulty="Hard", format="matching",
stem="Match each mechanism to the problem it solves.",
pairs=[
["Cross-region inference profile", "A model has limited regional availability; the application needs automatic failover and higher effective quotas"],
["Prompt router (model router)", "Simple prompts should use a cheap model and complex prompts a flagship model, routed by prompt complexity"],
["Provisioned Throughput", "Steady, predictable traffic needs reserved capacity with latency guarantees and throttling protection"]],
why="Three different mechanisms, three different exam answers. Inference profiles route for availability and resilience across regions. Prompt routers route for cost and quality by complexity. Provisioned Throughput reserves capacity for predictable load.",
trap="Pattern 4: this is the exam's favorite confusion set (trap 5). Memorize which lever solves which problem.",
why_wrong=[
"Provisioned Throughput reserves capacity; it does not route across regions, so it cannot solve regional availability.",
"Prompt routers optimize cost by prompt complexity; they provide neither failover nor reserved capacity.",
"Cross-region inference profiles do not reserve capacity; they route for availability, which is a different problem from throttling protection."
],
),

dict(id="Q8", domain="D1", difficulty="Hard", format="mc",
stem="An application calls a foundation model with its base model ID and receives an error stating that invocation with on-demand throughput is not supported for that model ID, suggesting an inference profile instead. The model works in the console. What is the MOST correct fix?",
options=[
"Invoke the model through its inference profile ID (for example, a geographic profile such as us. or a global profile) instead of the bare model ID",
"Increase the Provisioned Throughput units on the model",
"Add exponential backoff retries around the same base model ID call",
"Request a quota increase for on-demand throughput in the region"],
correct=[0],
why="Some models do not support direct on-demand invocation with base model IDs and require an inference profile ID. The error message says exactly this. Retries, quotas, and Provisioned Throughput do not change the addressing requirement.",
why_wrong=[
"Provisioned Throughput is not supported on inference profiles and does not fix an addressing error; this confuses trap 5 mechanisms.",
"Retrying the same incorrect call repeats the same error; backoff fixes throttling, not invalid addressing.",
"A quota increase does not help when the model ID itself is not invokable on-demand; the error is about how the model is addressed, not capacity."],
trap="Pattern 6: reaching for retries or quota increases when the error message names the fix. Read the error."),

dict(id="Q9", domain="D1", difficulty="Medium", format="mc",
stem="A team fully fine-tunes a large open model every week to keep a ticket-classification behavior current. Training costs are large and each run risks regressions. The task is narrow: classify tickets into 40 categories. What is the MOST correct change?",
options=[
"Switch to parameter-efficient fine-tuning with LoRA adapters, version the adapters in SageMaker Model Registry, and deploy through an automated pipeline with rollback",
"Continue full fine-tuning but run it daily so the model is never stale",
"Replace fine-tuning with a larger base model and hope the behavior emerges",
"Fine-tune once and never update the model again to avoid regression risk"],
correct=[0],
why="LoRA trains only small adapter weights instead of the full model, which is cheaper and safer for a narrow behavior change. Model Registry versions each adapter, and a pipeline with rollback makes updates safe. This is the FM customization lifecycle the exam tests.",
why_wrong=[
"More frequent full fine-tuning multiplies the cost problem and keeps the regression risk; it treats the symptom, not the cause.",
"A larger base model does not reliably produce a specific 40-category behavior, and it raises inference cost on every request.",
"Never updating guarantees staleness; it trades one failure mode for another instead of making updates safe."],
trap="Pattern 5: full fine-tuning weekly is the expensive habit; the MOST-correct answer attacks both cost (adapters) and safety (registry plus rollback)."),

dict(id="Q10", domain="D1", difficulty="Hard", format="mr", select=2,
stem="During a regional degradation, a flagship model becomes slow and throttled. The product requirement is that the assistant keeps answering, even at reduced quality, with no manual intervention. Which TWO design choices meet this requirement? (Select TWO)",
options=[
"A Step Functions circuit breaker that detects repeated model failures and routes traffic to a smaller fallback model or cached responses",
"Hardcoding the flagship model ID in every client so behavior is predictable during the incident",
"Graceful degradation: fall back to a cheaper model or a recent cached response when the primary model fails",
"Waiting for the region to recover while returning errors to users, to preserve answer quality",
"Deploying the entire application on EC2 instances in a second region with a load balancer"],
correct=[0,2],
why="Automatic failover needs a decision point (circuit breaker in Step Functions, which handles state and retries cleanly) and a degraded-but-working target (smaller model or cached response). Together they satisfy 'keeps answering with no manual intervention'.",
why_wrong=[
"Hardcoding the model ID removes the ability to fail over at all; it is the opposite of resilience.",
"Returning errors while waiting violates the 'keeps answering' requirement; quality preservation does not justify an outage.",
"EC2 plus a load balancer is within-region high availability thinking and a heavy custom build; it does not solve model-level degradation and fails the managed-first filter."],
trap="Pattern 2: option E looks like resilience engineering, but it solves regional instance failover, not model degradation, and it is a custom build."),

dict(id="Q11", domain="D1", difficulty="Easy", format="mc",
stem="A pipeline must ingest 20,000 vendor invoices per day (PDFs and photos) and extract the same set of fields from each: invoice number, date, line items, and total. Which approach is MOST correct?",
options=[
"Use Bedrock Data Automation with a custom blueprint defining the required fields, producing structured output per document",
"Use Bedrock Guardrails to read the invoice totals out of the documents",
"Use Amazon Kendra to extract the fields, since Kendra is the extraction service",
"Have a Lambda function call a foundation model with a free-form prompt and parse whatever text comes back with string splitting"],
correct=[0],
why="Bedrock Data Automation is the document-extraction service, and blueprints declare exactly which fields to extract, giving consistent structured output across document types. This is its canonical IDP use case.",
why_wrong=[
"Guardrails filter content for safety; they do not extract data. This is the wrong-plane trap.",
"Kendra is enterprise search over documents, not a field-extraction service; it finds documents, it does not return invoice totals.",
"Free-form prompting plus string splitting is fragile: output format drifts, parsing breaks, and there is no schema guarantee."],
trap="Pattern 6: Guardrails for extraction. Guardrails filter; they never extract."),

dict(id="Q12", domain="D1", difficulty="Medium", format="mc",
stem="A pipeline converts thousands of support call recordings into text with Amazon Transcribe before a foundation model analyzes them. Product names and internal acronyms are consistently mistranscribed. What is the MOST correct fix?",
options=[
"Add a custom vocabulary to Transcribe with the product names, acronyms, and domain terms",
"Switch the transcription to Bedrock Data Automation because Transcribe cannot handle audio",
"Increase the foundation model's temperature so it guesses the intended words creatively",
"Route the audio through Amazon Translate first to normalize the language"],
correct=[0],
why="Transcribe custom vocabularies exist exactly for domain-specific words, brand names, and acronyms that the base speech model mistranscribes. The failure is in transcription, so the fix belongs at the transcription layer.",
why_wrong=[
"Transcribe is the audio-to-text service; replacing it misdiagnoses the problem, and Data Automation is not the transcription fix here.",
"Raising temperature makes outputs more random, which worsens fidelity on transcripts; temperature controls creativity, not accuracy.",
"Translate converts between languages; it does not fix misrecognized domain terms and adds a pointless hop."],
trap="Pattern 1: fix the failure at the layer where it occurs. The transcript is wrong, so tune transcription, not the downstream model."),

dict(id="Q13", domain="D1", difficulty="Easy", format="mc",
stem="A startup is building a retrieval prototype over 50,000 internal documents. Cost must stay minimal during development, and query volume is low. Which vector store choice is MOST correct for this stage?",
options=[
"Amazon S3 Vectors, which is the cost-efficient option suited to smaller-scale and development workloads",
"Amazon OpenSearch Serverless with a large provisioned collection sized for peak production traffic",
"A self-managed vector database on EC2 with EBS volumes for maximum control",
"Amazon ElastiCache, because in-memory retrieval is fastest and the data persists there"],
correct=[0],
why="S3 Vectors is the exam's cost-sensitive choice for dev, test, and smaller-scale knowledge bases. OpenSearch Serverless fits production scale; paying for it during a low-volume prototype wastes money.",
why_wrong=[
"Sizing production-grade OpenSearch for a prototype violates the cost constraint; it is the right service at the wrong stage.",
"Self-managing a vector database on EC2 is maximum operational overhead, the opposite of the exam's managed-first bias.",
"ElastiCache is ephemeral caching, not durable vector storage; vectors would be lost on eviction or restart. This is trap 9."],
trap="Pattern 5: match the store to the stage. Cost-sensitive prototype points to S3 Vectors, not the production-grade default."),

dict(id="Q14", domain="D1", difficulty="Medium", format="mc",
stem="A knowledge base must answer questions that need both keyword precision (exact product codes) and semantic understanding (natural-language descriptions). Retrieved passages sometimes match keywords but do not answer the question. Which retrieval improvement is MOST correct?",
options=[
"Enable hybrid search combining vector and keyword retrieval, and add a rerank model to score candidates by true relevance",
"Switch to a larger generation model so answers sound more confident",
"Increase the chunk overlap to 90 percent so every chunk contains every keyword",
"Disable vector search and use keyword search only, since keywords are precise"],
correct=[0],
why="Hybrid search gets the best of both retrieval modes, and reranking re-scores the candidate set by actual relevance, which fixes 'keyword match but not an answer'. Switching the generation model does not fix a retrieval problem.",
why_wrong=[
"A larger generation model cannot fix irrelevant retrieval; confident wording over wrong passages is worse, not better.",
"Extreme overlap explodes storage and ingestion cost while barely helping relevance; it is a brute-force non-fix.",
"Keyword-only search throws away semantic understanding, which the scenario explicitly requires."],
trap="Pattern 1: the failure is retrieval quality ('match keywords but do not answer'), so the fix must be in retrieval, not generation."),

dict(id="Q15", domain="D1", difficulty="Medium", format="mc",
stem="A company runs one knowledge base shared by three subsidiaries. Each subsidiary's documents must be invisible to the others, enforced by the platform, not by asking the model nicely. What is the MOST correct design?",
options=[
"Separate knowledge bases per subsidiary with IAM-scoped access, so isolation is enforced by access control",
"One shared knowledge base with a system prompt instructing the model to only answer about the caller's subsidiary",
"One shared knowledge base with document filenames prefixed by subsidiary name",
"One shared knowledge base and a post-processing Lambda that deletes sentences mentioning other subsidiaries"],
correct=[0],
why="Tenant isolation must be enforced by IAM boundaries, not by prompt instructions the model can ignore or leak around. Separate knowledge bases per tenant with scoped access is the exam's required pattern.",
why_wrong=[
"Prompt instructions are not access control; models can be jailbroken or simply make mistakes, leaking other tenants' data.",
"Filename prefixes are cosmetic; any caller with KB access can retrieve any document regardless of prefix.",
"Post-processing deletion is fragile and reactive; sensitive content has already been retrieved and processed, and sentence filtering cannot guarantee isolation."],
trap="Pattern 6, trap 6: one shared KB with prompt-level 'access control'. The exam always demands real isolation."),

dict(id="Q16", domain="D1", difficulty="Medium", format="mr", select=2,
stem="A product catalog changes weekly. The RAG assistant must answer from the current catalog without manual re-ingestion work each week. Which TWO choices form the MOST correct design? (Select TWO)",
options=[
"Configure the knowledge base data source with a scheduled sync so catalog changes are ingested automatically",
"Reload the entire catalog by hand every Monday morning before business hours",
"Store the catalog in S3 as the knowledge base data source so syncs pick up new versions",
"Fine-tune the model on each weekly catalog snapshot so the knowledge is in the weights",
"Delete and recreate the knowledge base every week to guarantee freshness"],
correct=[0,2],
why="S3 as the data source plus a scheduled sync gives automated freshness: new catalog versions land in S3 and the sync ingests them on schedule. No manual work, no retraining.",
why_wrong=[
"Manual weekly reloads are operational toil and fragile; the scenario demands automation.",
"Weekly fine-tuning for catalog freshness is trap 7 again: expensive, slow, and it cannot cite sources.",
"Recreating the KB weekly destroys configuration and history for no benefit; sync exists exactly to avoid this."],
trap="Pattern 2: options B and E both 'work' in a brute-force sense but violate the automation constraint; the exam rewards the managed sync."),

dict(id="Q17", domain="D1", difficulty="Medium", format="mc",
stem="A RAG system ingests API reference documentation with deeply nested sections: service, resource, operation, parameters, examples. Fixed-size chunking keeps splitting parameter tables away from their operations. Which chunking strategy is MOST correct?",
options=[
"Hierarchical chunking, so small child chunks match precisely while parent chunks preserve the surrounding section context",
"Semantic chunking, because it is always the best strategy regardless of cost",
"Fixed-size chunking with zero overlap to keep chunks small and fast",
"No chunking, treating each whole document as a single chunk"],
correct=[0],
why="Hierarchical chunking is designed for structured documents: child chunks give precise matching, parent chunks restore the context (which operation a parameter table belongs to). This directly fixes tables split from their sections.",
why_wrong=[
"Semantic chunking is not 'always best'; it costs more at ingestion and is not the exam's preferred answer for structured, hierarchical documents.",
"Zero-overlap fixed-size chunking makes the splitting problem worse, not better.",
"No chunking creates enormous chunks that dilute retrieval precision and waste context on every query."],
trap="Pattern 5: 'semantic is always best' is the tempting overgeneralization; structured docs point to hierarchical."),

dict(id="Q18", domain="D1", difficulty="Hard", format="mc",
stem="A team ingests a large marketing blog archive into a knowledge base. Retrieval quality is acceptable with fixed-size chunking, but the team is considering semantic chunking for a small quality gain. Ingestion cost is a concern. What is the MOST correct guidance?",
options=[
"Stay with fixed-size chunking; semantic chunking costs more at ingestion and the gain does not justify it for this corpus",
"Switch to semantic chunking immediately because it is the premium option and cost does not matter",
"Switch to hierarchical chunking because blogs are hierarchical documents",
"Disable chunking and rely on the model's long context window instead"],
correct=[0],
why="Semantic chunking uses a model to find meaning boundaries, which raises ingestion cost. For a uniform corpus like blog posts where fixed-size already retrieves well, the exam's cost filter says do not pay for quality you do not need.",
why_wrong=[
"'Premium option' thinking ignores the stated cost concern; the exam tests cost judgment, not feature maximalism.",
"Blogs are not deeply hierarchical documents with nested tables; hierarchical chunking solves a different problem.",
"Whole-document chunks destroy retrieval precision and inflate every prompt with irrelevant text."],
trap="Pattern 5, trap 7-adjacent: the ladder principle applies to chunking too. Stop at the cheapest step that works."),

dict(id="Q19", domain="D1", difficulty="Medium", format="mc",
stem="A team stores 2 million text chunks as embeddings. They compare Titan Text Embeddings v2 at 1024 dimensions versus 256 dimensions. Storage cost matters and retrieval quality must stay acceptable. Which statement is MOST correct?",
options=[
"256 dimensions use roughly one quarter of the storage of 1024 dimensions, so test whether the smaller size keeps quality acceptable before committing to 1024",
"Dimension count has no effect on storage or cost, so always use 1024",
"256 dimensions are always strictly better because smaller is faster",
"Embedding dimensions can be changed any time without re-ingesting the vectors"],
correct=[0],
why="Storage scales linearly with dimensions: 256 is one quarter of 1024, so the vector footprint drops by about 75 percent. Titan Text Embeddings v2 supports 1024, 512, and 256 dimensions precisely so teams can trade quality against cost. The exam wants the tradeoff tested, not assumed.",
why_wrong=[
"Dimension count directly drives storage and cost; claiming otherwise ignores the tradeoff the question is about.",
"'Always better' is false: smaller dimensions can lose retrieval accuracy on hard corpora; the right size is measured, not assumed.",
"Changing dimensions changes every vector, so the index must be rebuilt; dimensions are set when vectors are created."],
trap="Pattern 1: the stem gives you both constraints (cost and quality). The correct answer is the only one that honors both instead of maximizing one."),

dict(id="Q20", domain="D1", difficulty="Medium", format="mc",
stem="Users ask multi-part questions like 'What is the return window for opened electronics, and how do I start a return from the mobile app?' Retrieval returns passages about only one part. Which query-handling improvement is MOST correct?",
options=[
"Decompose the query with a Lambda function into sub-questions, retrieve for each, then synthesize the answer",
"Increase the number of retrieved chunks from 5 to 50 and hope both parts appear",
"Switch the embedding model to a larger one so multi-part queries embed better",
"Tell users to ask only one question at a time through input validation"],
correct=[0],
why="Multi-part questions fail because one embedding cannot represent two intents well. Decomposition into sub-questions, independent retrieval per sub-question, and synthesis is the standard fix, and Lambda is the natural place for the decomposition step.",
why_wrong=[
"Retrieving 50 chunks floods the prompt with noise and cost; it does not reliably cover both intents.",
"A larger embedding model does not solve the two-intents-one-vector problem; the query handling is the issue, not the embedding quality.",
"Pushing the problem onto users degrades the product instead of fixing the system."],
trap="Pattern 1: retrieve-then-synthesize per sub-question. The trap options attack the wrong layer (embeddings, chunk counts) or the user."),

dict(id="Q21", domain="D1", difficulty="Easy", format="mc",
stem="A knowledge base covers documents in English, Spanish, and Japanese. Retrieval quality on non-English documents is poor with the current embeddings. Which embedding choice is MOST correct?",
options=[
"Cohere Embed multilingual, which is designed for multilingual retrieval across languages",
"Titan Text Embeddings v1 at 1536 dimensions, because more dimensions fix language coverage",
"An English-only embedding model with query translation at retrieval time",
"Keyword search only, abandoning embeddings for non-English content"],
correct=[0],
why="Cohere Embed multilingual is built for mixed-language corpora; it represents queries and documents from different languages in a shared space. Language coverage is a model property, not a dimension-count property.",
why_wrong=[
"More dimensions do not add language coverage; a model trained mainly on English stays weak on Japanese at any dimension count.",
"Query translation adds latency and error on every request and still leaves document-side representation weak.",
"Abandoning embeddings discards semantic retrieval entirely instead of fixing the embedding choice."],
trap="Pattern 6: dimension count confused with capability. Dimensions trade cost and precision; language coverage comes from the model's training."),

dict(id="Q22", domain="D1", difficulty="Medium", format="mr", select=2,
stem="Marketing rewrites the assistant's tone guidelines every few weeks. Every change currently requires a code deployment, and compliance needs an audit trail of who changed which prompt and when. Which TWO capabilities solve both problems? (Select TWO)",
options=[
"Bedrock Prompt Management versions, which create immutable snapshots of each prompt for audit and rollback",
"Hardcoding the new tone into the application code on every change, with git history as the audit trail",
"AWS CloudTrail logging of prompt management API calls, showing who changed what and when",
"Storing prompts in an engineer's laptop notes and pasting them into the console when needed",
"Disabling all prompt changes after launch so no audit trail is needed"],
correct=[0,2],
why="Prompt Management versions give immutable, restorable snapshots without redeploys, and CloudTrail records every prompt API call with identity and timestamp, which is exactly the audit trail compliance asked for.",
why_wrong=[
"Hardcoding keeps the redeploy problem the stem wants eliminated; git history is not the exam's answer for runtime prompt governance.",
"Laptop notes are ungoverned, unreviewed, and unauditable; the opposite of the requirement.",
"Freezing prompts refuses the business need instead of governing it."],
trap="Pattern 2: option B is half-right (git is an audit trail) but it preserves the redeploy pain the stem explicitly wants gone."),

dict(id="Q23", domain="D1", difficulty="Hard", format="mc",
stem="A team needs a fixed four-step document pipeline: extract text, classify the document, summarize it, then write the summary to a database. A compliance officer must approve the summary before it is stored, and the approval can take hours. Which orchestration choice is MOST correct?",
options=[
"AWS Step Functions, because the workflow has fixed steps plus a long human-approval wait that exceeds Lambda limits",
"Bedrock Prompt Flows, because the pipeline is prompt-centric and approvals can be added as nodes",
"Bedrock Agents, because agents handle multi-step reasoning autonomously",
"A single Lambda function that sleeps until the officer approves"],
correct=[0],
why="Step Functions is the orchestration service for fixed sequences with waits, retries, and human approvals via task tokens; a standard execution can wait far beyond Lambda's 15-minute cap. Prompt Flows suits prompt-centric chains without long human waits, and agents suit dynamic tool-using reasoning, not fixed deterministic pipelines.",
why_wrong=[
"Prompt Flows is for prompt-centric no-code chains; an hours-long human approval gate with database writes is general orchestration, which is Step Functions territory.",
"Agents are for dynamic reasoning over tools, not fixed deterministic sequences; using an agent here adds nondeterminism to a compliance pipeline.",
"A Lambda cannot sleep for hours; it times out at 15 minutes, and sleeping burns compute. This is trap 1."],
trap="Pattern 5: three plausible orchestrators, but only Step Functions handles fixed steps plus long human waits. Match the tool to the workflow shape."),

dict(id="Q24", domain="D1", difficulty="Medium", format="mc",
stem="An application needs the model to call a `get_order_status` function with a typed `order_id` parameter during conversations, working identically across Claude, Llama, and Titan. Which approach is MOST correct?",
options=[
"Use the Converse API with toolConfig declaring the function and its parameters, letting each model use the unified tool-use format",
"Describe the function in the prompt text and parse the model's free-form reply with regular expressions",
"Use InvokeModel with a hand-built provider-specific body per model, duplicating the tool declaration three times",
"Skip tool use and have the model guess order statuses from its training data"],
correct=[0],
why="Converse toolConfig is the unified, provider-independent way to declare tools; the same code works across Claude, Llama, and Titan. Free-form parsing is fragile, and per-provider bodies triple the maintenance.",
why_wrong=[
"Regex-parsing free-form tool calls breaks on format drift and is exactly the fragility tool use was designed to eliminate.",
"Hand-built provider bodies work but triple the code paths; the scenario demands one code path across three providers, which is Converse's purpose.",
"Guessing from training data is hallucination by design and can never return real order statuses."],
trap="Pattern 1: 'identically across three providers' is the constraint that kills the per-provider and regex options."),

dict(id="Q25", domain="D1", difficulty="Hard", format="mc",
stem="A team stores prompts in Bedrock Prompt Management and calls them through the Converse API. They try to add `guardrailConfig` inline on the Converse call and the request is rejected. They still need guardrail protection on these prompts. What is the MOST correct fix?",
options=[
"Apply the guardrail separately with the standalone ApplyGuardrail API on inputs and outputs, since guardrailConfig cannot be combined with Prompt Management prompts in Converse",
"Embed the guardrail rules as text inside the prompt template and hope the model obeys them",
"Abandon Prompt Management and hardcode the prompts so guardrailConfig works again",
"Disable guardrails for these prompts because Prompt Management prompts are inherently safe"],
correct=[0],
why="Converse rejects combining `guardrailConfig` with Prompt Management prompts (along with several other fields). The standalone ApplyGuardrail API applies the same guardrail policies to any text, including non-Bedrock flows, so protection is preserved without giving up prompt governance. Verified in the Converse API documentation.",
why_wrong=[
"Rules-as-text are prompt instructions, not enforcement; the model can be jailbroken past them. This is not a guardrail.",
"Abandoning prompt governance to recover one API field trades away versioning and audit for convenience; the standalone API solves it cleanly.",
"Managed prompts are not inherently safe; 'built-in safety is enough' is trap 15."],
trap="Pattern 6: a real API restriction with a clean workaround. The trap answers either weaken safety or destroy governance."),
]

# ---------------- Domain 2 (Q26-Q47) ----------------
QUESTIONS += [
dict(id="Q26", domain="D2", difficulty="Medium", format="ordering",
stem="Place these steps in the correct order to build a Bedrock agent that answers questions about company products using internal documents.",
steps=[
"Define the agent's instructions and session behavior in the agent configuration",
"Create a knowledge base from the product documents and connect it to the agent",
"Define action groups that map user requests to API calls or Lambda functions",
"Create an agent alias for the production deployment",
"Prepare the agent, then test through the alias"],
why="Agents are built in a fixed lifecycle: configure instructions, attach knowledge, define action groups, alias for production, prepare then test. Prepare-before-test and alias-before-production are the exam's tested ordering constraints.",
trap="Pattern 3: 'prepare the agent' always comes after configuration changes and before testing or alias use.",
why_wrong=[
"Testing before preparing invokes the old configuration; prepare must come before test.",
"Creating the production alias before defining instructions and action groups would alias an incomplete agent.",
"Connecting the knowledge base before configuring the agent instructions reverses the setup dependency."
],
),

dict(id="Q27", domain="D2", difficulty="Medium", format="mc",
stem="An agent must book refund appointments by calling the company's internal scheduling API. The API expects `customer_id` and `preferred_date`. How should the agent access this capability?",
options=[
"Define an action group whose function schema declares the scheduling operation and its parameters, backed by a Lambda executor that calls the API",
"Give the agent the API's base URL in its instructions and let it guess the request format",
"Have the agent output the API request as plain text for a human to execute",
"Connect the knowledge base to the scheduling API so retrieval returns appointment slots"],
correct=[0],
why="Action groups are how agents take actions: a function schema declares the operation and parameters, and a Lambda executor performs the call. Guessing formats or using the KB for live actions are category errors.",
why_wrong=[
"Guessing request formats from instructions is unreliable and untestable; schemas exist precisely to make this deterministic.",
"Human execution of agent output defeats the purpose of an action-taking agent and cannot scale.",
"A knowledge base serves documents, not live APIs; retrieval cannot book appointments."],
trap="Pattern 6: knowledge bases for live actions. KB = documents, action groups = actions."),

dict(id="Q28", domain="D2", difficulty="Hard", format="mc",
stem="An agent team updates the agent's instructions to fix a reasoning flaw, then tests immediately. The agent behaves exactly as before the change. The configuration was saved. What is the MOST likely cause?",
options=[
"The agent was not prepared after the configuration change, so the update is not active in the test invocation",
"The instructions were saved to the wrong region, so the test used the old region's agent",
"Agent instructions only take effect after 24 hours of propagation",
"Testing requires a new agent alias to be created for every instruction change"],
correct=[0],
why="Agents require a prepare step after configuration changes before the changes take effect; testing an unprepared agent invokes the old behavior. This prepare-after-change rule is a classic exam tripwire.",
why_wrong=[
"Region confusion is a distractor; the scenario says the configuration was saved on the same agent being tested.",
"There is no 24-hour propagation for agent instructions; prepare is the explicit activation step.",
"Aliases are stable deployment endpoints; they do not need recreation per change, and that would not explain identical behavior."],
trap="Pattern 6: 'configuration changed but behavior unchanged' almost always points to the missing prepare step."),

dict(id="Q29", domain="D2", difficulty="Medium", format="mc",
stem="During testing, an agent's orchestration trace shows it calling the wrong action group for 'cancel my subscription' requests. The function schemas look correct. What should the team examine next?",
options=[
"The agent's instructions and the action group descriptions, because ambiguous descriptions cause the model to pick the wrong group",
"The knowledge base chunk size, because retrieval determines action selection",
"The guardrail denied-topic list, because it blocks the cancel operation",
"The model's temperature, because high temperature causes wrong API choices"],
correct=[0],
why="Action group selection is driven by the agent instructions and the natural-language descriptions of each action group. If schemas are correct but selection is wrong, the descriptions are ambiguous or overlapping. Enable trace to see the reasoning, then sharpen the descriptions.",
why_wrong=[
"Chunk size affects document retrieval, not which action group the agent selects; wrong layer.",
"Denied topics would block or filter content, not cause selection of the wrong action group; wrong mechanism.",
"Temperature affects output randomness, not the systematic choice of the wrong tool; the cause is descriptive ambiguity, not sampling."],
trap="Pattern 1: schemas correct plus wrong selection points at the selection signal (descriptions), not at retrieval or sampling knobs."),

dict(id="Q30", domain="D2", difficulty="Easy", format="mc",
stem="An agent must answer questions from an internal wiki, and every answer should cite the wiki page it came from. The wiki is updated weekly. What is the MOST correct setup?",
options=[
"Connect a knowledge base built on the wiki to the agent, with scheduled syncs so weekly updates are ingested",
"Paste the entire wiki into the agent's instructions so the context is always present",
"Fine-tune the foundation model on the wiki so answers come from its weights",
"Have the agent call a search-engine API through an action group for each question"],
correct=[0],
why="Knowledge bases are the agent-native way to ground answers in documents, with citations and scheduled syncs for freshness. The wiki's weekly updates make RAG the right fit, exactly as in D1.",
why_wrong=[
"The wiki cannot fit in instructions; context is bounded and expensive, and updates would require editing instructions.",
"Fine-tuning on a weekly-changing wiki means weekly retraining with no citations; the same trap 7 as before.",
"An external search API leaks internal questions to the public internet and bypasses the governed KB; wrong tool and wrong boundary."],
trap="Pattern 6: agents do not change the RAG rule. Updating documents plus citations still means knowledge base, not fine-tuning."),

dict(id="Q31", domain="D2", difficulty="Medium", format="mc",
stem="A company deploys a Bedrock agent that handles refund requests. The agent must never issue a refund above $500 without a manager's approval, and every approval must be recorded. Which design is MOST correct?",
options=[
"Implement returnControl in the agent's action group: the agent pauses, a Step Functions workflow routes the approval to a manager, and the decision plus full trace are logged",
"Tell the agent in its instructions to never refund above $500 without asking, and trust it to comply",
"Set a guardrail denied topic for refunds so the agent cannot process any refund",
"Let the agent issue refunds directly and email a report afterward for the manager to review"],
correct=[0],
why="ReturnControl hands the decision back to the application for human approval, and Step Functions orchestrates the wait with task tokens. The trace and workflow execution produce the audit record. Instructions alone are not enforcement.",
why_wrong=[
"Instructions are advisory; a compliance gate needs a hard control, not a request the model might misjudge.",
"A denied topic would block all refunds, not gate large ones; it is the wrong granularity and the wrong mechanism.",
"Post-hoc reports do not prevent the unauthorized refund; the money has already moved."],
trap="Pattern 6: 'tell the agent' for a compliance gate. Approval gates need returnControl, not instructions."),

dict(id="Q32", domain="D2", difficulty="Hard", format="mr", select=2,
stem="An agent intermittently returns answers that contradict the company's pricing documents, though retrieval usually finds the right pages. Which TWO are the MOST likely causes to investigate? (Select TWO)",
options=[
"Hallucination: the model generated beyond what the retrieved passages support, so add a faithfulness evaluation and grounding checks",
"Stale knowledge base content where the pricing documents changed but the scheduled sync failed",
"Provisioned Throughput running out of capacity during peak hours",
"The agent's IAM role having too many permissions on the knowledge base",
"Users asking questions in ALL CAPS, which confuses the retrieval model"],
correct=[0,1],
why="Contradicting retrieved sources is the signature of hallucination or grounding failure, and pricing changes with a failed sync produce exactly 'usually right, intermittently wrong' behavior. Both are grounding-layer causes.",
why_wrong=[
"Throughput exhaustion causes throttling errors, not wrong answers; wrong failure mode.",
"Excess IAM permissions are a security concern, not a cause of factual contradiction.",
"Capitalization does not systematically invert pricing facts; this is noise dressed as a cause."],
trap="Pattern 1: 'contradicts the documents it retrieved' narrows the cause to the grounding layer: generation fidelity or source freshness."),

dict(id="Q33", domain="D2", difficulty="Medium", format="mc",
stem="A support agent handles 10,000 conversations a day. Each conversation independently repeats the same 4,000-token product catalog context. Costs are high. What is the MOST correct optimization?",
options=[
"Use prompt caching with a cachePoint after the stable catalog content, so the repeated prefix is billed at the lower cached rate",
"Increase the model's max tokens so the catalog fits more comfortably",
"Fine-tune the model on the catalog so the context is no longer needed",
"Switch to a smaller model and accept lower answer quality"],
correct=[0],
why="A stable 4,000-token prefix repeated across thousands of calls is the textbook prompt-caching case: cachePoint after the stable content, and repeated reads are billed lower. This is verified Bedrock behavior.",
why_wrong=[
"Raising max tokens increases cost and does not reduce the repeated input tokens; it attacks nothing.",
"Fine-tuning on a catalog is trap 7 again: freshness problems plus retraining cost for what is a caching problem.",
"Downgrading the model sacrifices quality the scenario does not say is acceptable; optimize cost without degrading quality first."],
trap="Pattern 5: repeated stable context is a caching problem, not a model-size or training problem."),

dict(id="Q34", domain="D2", difficulty="Hard", format="mc",
stem="An agent uses tool calling in a loop: each turn it calls tools and continues reasoning. The team notices that placing the tool definitions after the conversation messages in the request yields worse tool selection than placing them first. They also see rising costs from repeated system prompts. What is the MOST correct combined fix?",
options=[
"Place tool definitions and system content first, then a cachePoint after the stable content, so both tool selection and caching work on the stable prefix",
"Move the tool definitions into the user messages so the model reads them last",
"Remove the system prompt entirely to cut costs",
"Disable tool calling and have the model describe the actions in prose"],
correct=[0],
why="Cache checkpoints work on stable prefixes: tools, then system, then messages. Stable-first ordering both improves tool selection (definitions before the conversation they apply to) and lets the cache cover the repeated prefix. Two verified behaviors in one fix.",
why_wrong=[
"Burying tool definitions in user messages makes selection worse and breaks caching of the stable prefix.",
"Deleting the system prompt removes behavioral control; cost-cutting that destroys the product is not optimization.",
"Prose descriptions of actions cannot be executed reliably; this abandons the agent's capability instead of tuning it."],
trap="Pattern 2: a combined question where each half has a verified rule (ordering for selection, cachePoint for cost). The correct option honors both."),

dict(id="Q35", domain="D2", difficulty="Medium", format="mc",
stem="An agent must read a 200-page PDF contract, extract the renewal clause, and summarize the termination terms. The PDF is already in S3. What is the MOST correct way to give the agent the document content?",
options=[
"Use Bedrock Data Automation to parse the PDF into structured text, then provide the extracted content to the agent",
"Paste the PDF's binary bytes into the agent's instructions",
"Have the agent download the PDF with a Lambda function and parse it with string operations",
"Email the PDF to the agent's service account and let it read the attachment"],
correct=[0],
why="Data Automation is the document parser: it converts PDFs (including images and scanned pages) into structured text the agent can reason over. Binary bytes in instructions and string-parsing hacks are fragile; agents have no email inbox.",
why_wrong=[
"Binary PDF bytes are not readable text; instructions hold text, and the model cannot decode PDF internals reliably.",
"Hand-rolled PDF parsing in Lambda duplicates what Data Automation does as a managed service; it fails the managed-first filter.",
"Agents have no email capability; this is a nonsense option testing whether you know the agent's actual interfaces."],
trap="Pattern 5: the managed parser (Data Automation) beats every hand-built or misapplied alternative."),

dict(id="Q36", domain="D2", difficulty="Medium", format="mr", select=2,
stem="A company wants its support agent to improve its answers over time from conversation logs. Which TWO practices form the MOST correct improvement loop? (Select TWO)",
options=[
"Store conversation history in a session store and periodically review traces and user feedback to refine instructions and action groups",
"Run LLM-as-a-judge evaluations on sampled conversations, scoring faithfulness and correctness against the knowledge base",
"Automatically fine-tune the foundation model on every conversation the same night it happens",
"Delete all conversation logs immediately for privacy, then guess at improvements",
"Let the agent rewrite its own instructions in production without review"],
correct=[0,1],
why="Improvement loops are: capture sessions and traces, review them, and run structured evaluations (LLM-as-a-judge with faithfulness and correctness metrics) to find what to fix. Then refine instructions, action groups, and prompts deliberately.",
why_wrong=[
"Nightly fine-tuning on raw conversations is expensive, risks baking in bad behavior, and skips the evaluation step that tells you what to fix.",
"Deleting logs destroys the evidence the loop needs; privacy is handled with retention policies and redaction, not blindness.",
"Self-modifying production instructions without review is unsafe and ungoverned; improvements go through review."],
trap="Pattern 6: 'improve over time' tempts training-based answers, but the exam's loop is evaluate, then refine deliberately."),

dict(id="Q37", domain="D2", difficulty="Hard", format="mc",
stem="An agent handles insurance claims. Regulations require that every automated decision be explainable: which documents were used, which tools were called, and what the model reasoned at each step. What is the MOST correct way to satisfy this?",
options=[
"Enable tracing on the agent invocations and persist the full trace (pre-processing, orchestration, post-processing) with the decision record",
"Ask the agent to explain itself in its final answer and store that text as the explanation",
"Store only the final answer and the timestamp; the model is deterministic so it can be re-run",
"Rely on CloudTrail alone, since it records the agent invocation"],
correct=[0],
why="Agent traces record the actual execution: which knowledge base passages were retrieved, which action groups ran with which inputs, and the model's reasoning at each stage. Persisting the trace is the auditable record; a self-written explanation is unverified narration.",
why_wrong=[
"A self-explanation is generated text, not a record; it can omit or misdescribe what actually happened.",
"Storing only outputs is not explainability, and models are not deterministic enough to reconstruct reasoning by re-running.",
"CloudTrail records the API call, not the agent's internal reasoning, tool calls, and retrieved passages."],
trap="Pattern 6: trace (the execution record) versus self-explanation (generated text). Compliance needs the record, not the narration."),

dict(id="Q38", domain="D2", difficulty="Medium", format="mc",
stem="A team builds a multi-agent system: a supervisor agent coordinates three specialist agents (billing, technical, shipping). During testing, the specialists never receive the conversation history from the supervisor. Which configuration is the MOST likely fix?",
options=[
"Enable conversation history relay between the supervisor and collaborator agents so context flows across the team",
"Increase the supervisor agent's max tokens so it can hold more history",
"Merge all three specialists into one agent with longer instructions",
"Give each specialist its own separate knowledge base so they do not need history"],
correct=[0],
why="Multi-agent collaboration requires the supervisor to relay conversation history to collaborators; without the relay setting, specialists start each turn blind. This is the built-in multi-agent mechanism, distinct from action groups.",
why_wrong=[
"More tokens on the supervisor do not move history to the specialists; the history must be relayed, not just stored.",
"Merging destroys the specialist decomposition the design chose; it avoids the bug instead of fixing the configuration.",
"Separate knowledge bases solve document access, not conversation context; the specialists lack history, not documents."],
trap="Pattern 4: multi-agent collaboration is a supervisor/collaborator relationship with history relay, not action groups."),

dict(id="Q39", domain="D2", difficulty="Easy", format="mc",
stem="A developer wants agents built in the AWS console to be deployable through the team's CI/CD pipeline with code review. What is the MOST correct approach?",
options=[
"Define the agents with infrastructure as code (CloudFormation or CDK) so agent configuration is versioned, reviewed, and deployed like other infrastructure",
"Export console screenshots of the agent configuration and attach them to the deployment ticket",
"Have one engineer manually recreate the agent in production after testing in development",
"Store the agent configuration in a shared document and copy values into the console per environment"],
correct=[0],
why="Infrastructure as code is the exam's answer for reviewable, repeatable deployments of anything AWS builds, including agents. Console click-ops, screenshots, and manual recreation are unreviewed and error-prone.",
why_wrong=[
"Screenshots are not deployable artifacts and cannot be diffed or rolled back.",
"Manual recreation per environment guarantees drift between dev and production.",
"Copy-paste from documents is manual toil with no validation; it is click-ops with extra steps."],
trap="Pattern 5: anything 'deployable through CI/CD with review' points to IaC, regardless of which service is being deployed."),

dict(id="Q40", domain="D2", difficulty="Medium", format="mc",
stem="An agent's action group calls a Lambda function that sometimes takes 3 minutes to complete. The agent invocation fails before the function finishes. What is the MOST correct fix?",
options=[
"Redesign so the Lambda returns quickly and the long work continues asynchronously, with the agent polling or being notified on completion",
"Increase the agent's timeout to 30 minutes so it can wait for the Lambda",
"Chain three Lambda functions in sequence so each handles one minute of the work",
"Remove the Lambda and have the agent perform the 3-minute task by reasoning longer"],
correct=[0],
why="Long-running work must be asynchronous: the function acknowledges fast, work continues in the background, and completion is delivered via polling or callback. Synchronous waiting couples the agent's invocation lifetime to the task and fails at scale.",
why_wrong=[
"Extending timeouts papers over the design flaw; synchronous 3-minute waits are fragile and do not scale with concurrency.",
"Splitting the work across chained functions does not change the total synchronous wait; it adds complexity without fixing the pattern.",
"Reasoning longer does not execute external work; the agent cannot perform the Lambda's task by thinking."],
trap="Pattern 1: the failure is synchronous coupling. The fix is async with polling or notification, not longer waits."),

dict(id="Q41", domain="D2", difficulty="Hard", format="mc",
stem="A company runs two agents: one answers employee HR questions, one answers customer support questions. The HR agent must never see customer data and vice versa. Both invoke the same Lambda tools. What is the MOST correct isolation design?",
options=[
"Scope each agent's IAM role and each action group's Lambda permissions to only the data its domain needs, keeping tool code shared but data access separated",
"Put both agents in the same IAM role with full access, since the agents' instructions will keep them in their lanes",
"Merge the two agents into one agent with a prompt that switches between HR and customer modes",
"Give both agents access to all data but add a guardrail denied topic for the other domain's content"],
correct=[0],
why="Isolation is enforced by IAM scoping on each agent's role and on what each action group can reach. Shared tool code is fine; what matters is that each agent's execution identity can only touch its own domain's data.",
why_wrong=[
"Instructions are not access control; one role with full access means either agent can reach the other's data.",
"Merging destroys the isolation boundary; a mode-switching prompt is the weakest possible separation.",
"Denied topics filter generated content; they do not restrict which data the agent's tools can retrieve. Wrong plane."],
trap="Pattern 6, trap 6: isolation must be enforced by IAM, never by prompts or content filters."),

dict(id="Q42", domain="D2", difficulty="Medium", format="mr", select=2,
stem="An agent's answers are factually correct but users complain the tone is inconsistent: sometimes formal, sometimes casual, occasionally slang. Which TWO fixes are MOST correct? (Select TWO)",
options=[
"Add explicit tone and style guidelines to the agent's instructions and prompt templates",
"Create prompt variants in Prompt Management to A/B test tone settings and adopt the winner",
"Fine-tune the foundation model on formal documents so the tone is permanently formal",
"Increase the temperature to make the tone more creative and varied",
"Add a guardrail denied topic for casual language"],
correct=[0,1],
why="Tone inconsistency is a prompt-layer problem: explicit style guidelines in instructions fix it, and prompt variants let the team test tone settings systematically before adopting one. Both are cheap and reversible.",
why_wrong=[
"Fine-tuning for tone is disproportionate; prompt-level guidance solves it without training cost, and 'permanently formal' may not even be the desired tone.",
"Higher temperature increases variation, which worsens inconsistency; it is the opposite of the fix.",
"Denied topics block subject matter, not style; a topic filter cannot enforce tone. Wrong mechanism."],
trap="Pattern 5: tone is prompt-layer. The exam punishes reaching for fine-tuning or guardrails when instructions suffice."),

dict(id="Q43", domain="D2", difficulty="Medium", format="mc",
stem="A team is choosing between Bedrock Prompt Flows and Bedrock Agents for a deterministic five-step claims intake process: collect fields, validate, look up policy, compute payout, store result. No step requires open-ended reasoning. What is the MOST correct choice?",
options=[
"Prompt Flows, because the process is a fixed sequence of prompt-centric steps with no autonomous reasoning",
"Agents, because agents are newer and more capable than flows",
"Agents, because only agents can call Lambda functions",
"Prompt Flows, because flows support human approval gates lasting several days"],
correct=[0],
why="Prompt Flows orchestrates fixed sequences of prompt-centric steps; agents are for dynamic, tool-using reasoning. A deterministic five-step pipeline with no open-ended reasoning is the flows shape. (Long human waits would push toward Step Functions, but that is not in this scenario.)",
why_wrong=[
"'Newer and more capable' is not a selection criterion; the exam tests matching the tool to the workflow shape.",
"Both flows and agents can invoke Lambda; that capability does not decide between them.",
"Multi-day human approvals are Step Functions territory with task tokens, not the flows differentiator here."],
trap="Pattern 4: flows versus agents is decided by workflow shape (fixed sequence vs autonomous reasoning), not by capability marketing."),

dict(id="Q44", domain="D2", difficulty="Hard", format="matching",
stem="Match each API to its purpose.",
pairs=[
["InvokeModel", "Send a single request to a foundation model, including embedding models"],
["Converse", "Hold a multi-turn conversation with unified text, tool use, and guardrail fields across providers"],
["ApplyGuardrail", "Evaluate text against guardrail policies independently of any model call"]],
why="InvokeModel is the general single-request API (and the one for embeddings). Converse is the unified conversational API with toolConfig and guardrailConfig. ApplyGuardrail applies guardrail policies to arbitrary text with no model involved.",
trap="Pattern 4: the exam loves API-purpose matching. InvokeModel for embeddings is the detail most people miss.",
why_wrong=[
"Converse is text-generation only; it cannot produce embeddings, so InvokeModel is the embeddings API.",
"ApplyGuardrail evaluates text against guardrail policies; it does not invoke models or hold conversations.",
"InvokeModel sends single requests; it does not manage multi-turn conversation state the way Converse does."
],
),

dict(id="Q45", domain="D2", difficulty="Easy", format="mc",
stem="A developer prototypes an agent in the AWS console and wants to inspect what the agent is thinking at each step: which passages it retrieved and which tools it called. What should the developer enable?",
options=[
"Trace, which returns the pre-processing, orchestration, and post-processing steps of the agent invocation",
"CloudWatch Logs on the Lambda function only, which shows the agent's reasoning",
"X-Ray tracing on the API Gateway, which captures the agent's internal steps",
"Guardrail trace, which logs the agent's tool selection logic"],
correct=[0],
why="Agent trace is the built-in inspection mechanism: it exposes the reasoning chain, retrieved passages, and tool calls at each stage. Lambda logs show only the function's view, not the agent's orchestration.",
why_wrong=[
"Lambda logs show the function's execution, not the agent's retrieval choices or reasoning steps.",
"X-Ray traces service hops, not the agent's internal reasoning and orchestration decisions.",
"Guardrail trace shows guardrail evaluations, not tool selection or retrieval; wrong trace."],
trap="Pattern 6: each trace type shows its own plane. Agent reasoning needs the agent trace."),

dict(id="Q46", domain="D2", difficulty="Medium", format="mc",
stem="An agent must call a partner's REST API that is described by an OpenAPI specification. The team wants the agent to use the API without writing custom Lambda executor code. What is the MOST correct approach?",
options=[
"Define the action group with the OpenAPI schema directly, letting Bedrock map operations to API calls without a custom executor",
"Write a Lambda function that hardcodes each API endpoint and have the action group call it",
"Paste the OpenAPI specification into the agent's instructions and let the model craft HTTP requests",
"Use a knowledge base to store the API documentation so the agent can read it at runtime"],
correct=[0],
why="Action groups accept an OpenAPI schema as the function definition, so Bedrock can invoke the partner API directly with no custom executor code. This is the no-custom-code path the scenario asks for.",
why_wrong=[
"Hardcoding endpoints in Lambda is exactly the custom code the scenario wants to avoid; it adds maintenance for no benefit.",
"Letting the model hand-craft HTTP requests from pasted specs is unreliable and untestable.",
"A knowledge base holds documents for retrieval, not executable API bindings; the agent cannot call an API by reading about it."],
trap="Pattern 5: the managed path (OpenAPI schema on the action group) beats custom code when the scenario says 'without writing custom code'."),

dict(id="Q47", domain="D2", difficulty="Hard", format="mc",
stem="An agent books travel using three tools: search_flights, reserve_hotel, and charge_card. Testing shows the agent sometimes charges the card before confirming the flight and hotel are available. The business rule is: never charge before both are confirmed. What is the MOST correct fix?",
options=[
"Encode the ordering rule in the agent's instructions and add a confirmation step via returnControl before the charge_card call executes",
"Remove the charge_card tool and have the agent email the card details to finance",
"Increase the model's context window so it remembers the business rule better",
"Add a guardrail denied topic for credit card charges"],
correct=[0],
why="Sequencing rules belong in instructions, but a money-movement action needs a hard gate: returnControl pauses before charge_card executes so the application can verify both confirmations exist. Instructions guide, returnControl enforces.",
why_wrong=[
"Emailing card details is a security nightmare and abandons the agent's capability; it is not a fix.",
"A larger context window does not enforce ordering; the model can still sequence tools wrong with perfect memory of the rule.",
"A denied topic would block all charges, not order them correctly; wrong mechanism and wrong granularity."],
trap="Pattern 6: money movement needs a hard control (returnControl), not just instructions. Guide plus gate."),
]

# ---------------- Domain 3 (Q48-Q63) ----------------
QUESTIONS += [
dict(id="Q48", domain="D3", difficulty="Hard", format="matching",
stem="Match each Bedrock Guardrails control to what it filters.",
pairs=[
["Content filters", "Hate, insults, sexual, violence, misconduct, and prompt attacks at LOW, MEDIUM, or HIGH strength"],
["Denied topics", "Subject areas the application must never discuss, defined in natural language"],
["Word filters", "Exact strings such as competitor names or profanity, blocked on match"],
["Sensitive information filters", "PII and custom regex patterns, blocked or masked on detection"]],
why="Four controls, four jobs. Content filters handle toxicity categories with strength levels. Denied topics handle subject areas in plain language. Word filters handle exact strings. Sensitive-info filters handle PII with block or mask actions.",
trap="Pattern 4: denied topics versus word filters is the classic confusion. Topics are subject areas; words are exact strings.",
why_wrong=[
"Denied topics define subject areas in natural language; they cannot do exact-string blocking, which is the word filter job.",
"Content filters target toxicity categories at strength levels; PII detection with block or mask actions belongs to sensitive-information filters.",
"Word filters match exact strings; they cannot interpret a subject area described in natural language."
],
),

dict(id="Q49", domain="D3", difficulty="Medium", format="mc",
stem="A financial advice assistant must refuse to provide personalized investment recommendations, but it may explain general investing concepts. How should this be enforced?",
options=[
"A guardrail denied topic defining personalized investment advice, applied to both inputs and outputs",
"A word filter listing every stock ticker symbol",
"A content filter set to HIGH, which blocks all financial content",
"Instructions telling the model to be careful with financial questions"],
correct=[0],
why="Denied topics are the natural-language mechanism for 'never discuss this subject area', and applying the guardrail to both inputs and outputs covers both the user's request and the model's reply. Word filters cannot enumerate advice; content filters target toxicity, not topics.",
why_wrong=[
"Ticker lists are exact strings; advice is a subject area. You cannot enumerate every way to give advice.",
"Content filters at HIGH block toxicity categories, not finance; they would not stop personalized advice and might block legitimate content.",
"Instructions are advisory; a compliance boundary needs guardrail enforcement, not a request."],
trap="Pattern 6: subject-area refusal is denied topics. Word filters are for exact strings."),

dict(id="Q50", domain="D3", difficulty="Hard", format="ordering",
stem="Place these safeguards in the order they should be applied to user input in a defense-in-depth design, from outermost to innermost.",
steps=[
"Input validation and sanitization at the application edge (length, format, allowlists)",
"Bedrock Guardrails on the input (prompt attack and content filters)",
"Model invocation with least-privilege IAM and scoped tool permissions",
"Bedrock Guardrails on the output (content and sensitive-info filters)",
"Logging and monitoring of flagged interactions for review"],
why="Defense in depth layers from the edge inward: validate first, filter the input, constrain what the model can do, filter the output, then observe. Guardrails on both sides of the model is the exam's expected shape.",
trap="Pattern 3: guardrails belong on BOTH inputs and outputs. An ordering that applies them only once is wrong.",
why_wrong=[
"Applying guardrails only on outputs leaves prompt injection unfiltered at the input boundary.",
"Invoking the model before input validation lets malformed or malicious input reach the model unexamined.",
"Logging before the model runs would record nothing; observation belongs at the end of the pipeline."
],
),

dict(id="Q51", domain="D3", difficulty="Medium", format="mc",
stem="A healthcare assistant must never reveal patient phone numbers or email addresses in its answers, even if those appear in retrieved documents. What is the MOST correct control?",
options=[
"A guardrail sensitive-information filter for PII with the mask action, applied to the model output",
"A denied topic for phone numbers and email addresses",
"Instructions telling the model to omit contact details",
"Encrypting the knowledge base documents so the model cannot read phone numbers"],
correct=[0],
why="Sensitive-information filters are built for PII with block or mask actions; masking the output preserves answer utility while removing the PII. Denied topics handle subject areas, not data patterns.",
why_wrong=[
"Denied topics define subject areas in natural language; PII detection needs pattern-based filters, not topic definitions.",
"Instructions are not enforcement; the requirement says 'even if those appear in retrieved documents', which demands a hard filter.",
"Encrypting documents would prevent retrieval from working at all; it breaks the product instead of filtering the output."],
trap="Pattern 6: PII is sensitive-information filters. Denied topics cannot do pattern detection."),

dict(id="Q52", domain="D3", difficulty="Medium", format="mr", select=2,
stem="A public-facing assistant is being probed with prompt injection attempts: users paste fake system instructions trying to make the assistant reveal its hidden prompt. Which TWO defenses are MOST correct? (Select TWO)",
options=[
"A guardrail with the prompt attack filter enabled to detect and block injection attempts",
"Clearly separating system instructions from user input and never echoing the system prompt",
"Training the model to recognize injection attempts through fine-tuning",
"Disabling all user input and offering only canned button responses",
"Storing the system prompt in a separate AWS account from the application"],
correct=[0,1],
why="The prompt attack filter is the purpose-built detector for injection, and architectural separation (system instructions never mixed with or echoed from user input) removes the attack surface. Together they are the exam's injection defense.",
why_wrong=[
"Fine-tuning for injection resistance is disproportionate and unreliable; the managed filter plus architecture is the tested answer.",
"Canned buttons abandon the assistant's purpose; it refuses the product instead of securing it.",
"The account holding the prompt is irrelevant; injection works through the input channel, not through account boundaries."],
trap="Pattern 6: prompt injection is fought with the prompt attack filter plus input separation, not with training or account tricks."),

dict(id="Q53", domain="D3", difficulty="Easy", format="mc",
stem="A company must prove to auditors that its assistant's answers are grounded in retrieved company documents, not invented. Which evaluation approach is MOST correct?",
options=[
"Run RAG evaluations measuring faithfulness, correctness, and citation precision against the retrieved passages",
"Count the number of tokens in each answer; longer answers are more grounded",
"Ask the model whether its own answers are grounded and record its response",
"Measure the assistant's uptime; available systems are more trustworthy"],
correct=[0],
why="Faithfulness measures whether the answer is supported by the retrieved passages, correctness measures factual accuracy, and citation precision measures whether citations point to the right sources. Together they are the auditable grounding proof.",
why_wrong=[
"Token count has no relationship to groundedness; verbosity is not evidence.",
"Self-attestation is generated text, not measurement; the model cannot audit itself.",
"Uptime measures availability, not answer quality; the planes are unrelated."],
trap="Pattern 6: grounding is measured with faithfulness and citation metrics, never with self-reports or proxy statistics."),

dict(id="Q54", domain="D3", difficulty="Medium", format="mc",
stem="An assistant's answers are evaluated by human reviewers for tone and helpfulness, and the team wants automated nightly scoring to catch regressions between human reviews. Which combination is MOST correct?",
options=[
"LLM-as-a-judge scoring correctness, faithfulness, and professional style nightly, plus periodic human evaluation for nuanced tone judgments",
"Human evaluation only, because automated judges are never reliable enough to use",
"LLM-as-a-judge only, because human review is too slow to ever be useful",
"Programmatic metrics only (BLEU and ROUGE), because they are fully deterministic"],
correct=[0],
why="LLM-as-a-judge gives cheap nightly regression signal on correctness, faithfulness, and style, while humans handle the nuanced tone judgments automation cannot. The exam's position is that the methods complement each other.",
why_wrong=[
"'Never reliable enough' is false; LLM judges are the standard for nightly regression detection, with humans as the periodic ground truth.",
"Human-only review cannot run nightly at scale; it misses regressions between reviews.",
"BLEU and ROUGE measure surface text overlap, not correctness or tone; they are the wrong metrics for this job."],
trap="Pattern 2: the absolutes ('never', 'only') mark the wrong answers. The exam rewards the complementary pairing."),

dict(id="Q55", domain="D3", difficulty="Hard", format="mc",
stem="A team runs LLM-as-a-judge evaluations comparing two prompt versions. The judge consistently prefers whichever answer appears first. The team needs trustworthy comparisons. What is the MOST correct fix?",
options=[
"Randomize or counterbalance the presentation order across comparisons so position bias cancels out",
"Use a larger judge model, because larger models do not have position bias",
"Show the judge only one answer at a time and ask for an absolute score with no comparison",
"Replace the judge with exact-match scoring, which has no position bias"],
correct=[0],
why="Position bias is a known LLM-judge artifact: judges favor the first-presented option. Counterbalancing presentation order is the standard methodological fix. Larger models still show the bias; single-answer scoring loses the comparison the team wants.",
why_wrong=[
"Model scale does not eliminate position bias; the bias is methodological, not a capacity problem.",
"Single-answer absolute scoring avoids the bias but abandons the pairwise comparison the team needs; it changes the question instead of fixing the method.",
"Exact match cannot score open-ended answers; it is the wrong metric family for this evaluation."],
trap="Pattern 1: the artifact is in the method (order), so the fix is in the method (counterbalance), not in model size."),

dict(id="Q56", domain="D3", difficulty="Medium", format="mc",
stem="A RAG assistant cites sources, but auditors find that some citations point to documents that do not support the cited claim. Which metric directly measures this failure, and what is the MOST correct response?",
options=[
"Citation precision; investigate retrieval and generation to find why unsupported claims get citations",
"Answer length; shorten answers so fewer citations are needed",
"Invocation count; the assistant is being called too often",
"Latency; slow answers cause citation errors"],
correct=[0],
why="Citation precision measures whether each citation actually supports its claim; unsupported citations are exactly a precision failure. The response is to debug the retrieval-generation boundary, not to shrink answers or watch latency.",
why_wrong=[
"Answer length does not cause unsupported citations; shortening answers hides the metric without fixing the cause.",
"Invocation count is a usage statistic with no bearing on citation correctness.",
"Latency and citation accuracy are unrelated planes; slow answers are not wrong answers."],
trap="Pattern 1: name the metric that matches the failure (precision of citations), then fix the cause, not a proxy."),

dict(id="Q57", domain="D3", difficulty="Easy", format="mc",
stem="A company is choosing a foundation model for a customer-facing assistant. The security team asks how to compare models on safety before selecting one. What is the MOST correct guidance?",
options=[
"Review the model providers' safety evaluations and red-teaming reports, then run the company's own safety evaluations on shortlisted models",
"Choose the largest model, because larger models are inherently safer",
"Choose whichever model the engineering team used last time",
"Skip safety comparison; Bedrock Guardrails make model choice irrelevant to safety"],
correct=[0],
why="Model selection includes safety comparison: provider-published evaluations and red-teaming give the baseline, and the company's own evaluations on shortlisted models confirm behavior in their context. Guardrails add a layer but do not erase model-level differences.",
why_wrong=[
"Model size does not determine safety; larger models can be more capable of harmful outputs, not less.",
"Reusing the last model is not a selection process; it skips the comparison the scenario requires.",
"Guardrails are one layer of defense in depth; they do not make the underlying model's safety profile irrelevant."],
trap="Pattern 6, trap 15: guardrails do not replace model-level safety evaluation. Defense in depth means both."),

dict(id="Q58", domain="D3", difficulty="Medium", format="mc",
stem="An assistant must refuse harmful requests, but testing shows it sometimes complies with disallowed content wrapped in hypothetical framing ('imagine a world where...'). Which evaluation dimension should the team prioritize, and what is the MOST correct mitigation?",
options=[
"Harmfulness and refusal metrics in LLM-as-a-judge evaluations; strengthen guardrails and add adversarial test cases with hypothetical framing",
"Latency metrics; faster refusals are safer refusals",
"Cost metrics; harmful requests are expensive to process",
"User satisfaction metrics; satisfied users do not write hypotheticals"],
correct=[0],
why="Hypothetical framing is a jailbreak technique; the evaluation dimensions that catch it are harmfulness and refusal, and the mitigation is stronger guardrails plus adversarial tests using the same framing. The other metrics are unrelated planes.",
why_wrong=[
"Refusal speed is not safety; a fast compliance with a harmful request is worse than a slow refusal.",
"Cost does not measure or mitigate harm; it is the wrong plane entirely.",
"User satisfaction is orthogonal to safety; a satisfied attacker is still an attacker."],
trap="Pattern 1: jailbreak framing is a safety problem. Measure refusal and harmfulness, mitigate with guardrails and adversarial tests."),

dict(id="Q59", domain="D3", difficulty="Hard", format="mc",
stem="A team wants to prove that a new prompt version is genuinely better, not just luckier on a small test set. Their current test set has 40 examples. What is the MOST correct evaluation practice?",
options=[
"Build a larger, representative golden dataset with clear pass criteria, version it, and re-run it on every prompt change",
"Test on the same 40 examples repeatedly until the new prompt passes",
"Test each prompt version on a different 40 examples so results stay fresh",
"Have the prompt author grade their own prompt's outputs; they know the intent best"],
correct=[0],
why="Trustworthy comparison needs a golden dataset that is large enough, representative, versioned, and stable across runs, with pre-defined pass criteria. Re-testing until passing is p-hacking; changing the test set per version destroys comparability; self-grading is biased.",
why_wrong=[
"Repeated testing until passing is selection bias; it proves persistence, not quality.",
"Different test sets per version make results incomparable; the dataset must be stable to measure change.",
"Self-grading by the author is conflicted; evaluation needs independent judgment against fixed criteria."],
trap="Pattern 2: the wrong options are all methodological sins (p-hacking, moving goalposts, self-grading). The exam rewards the disciplined golden dataset."),

dict(id="Q60", domain="D3", difficulty="Medium", format="mr", select=2,
stem="A company deploys an assistant that gives financial summaries. Regulators require that the assistant's behavior be consistent and that any behavior change be traceable to a specific approved change. Which TWO practices satisfy this? (Select TWO)",
options=[
"Version prompts in Prompt Management and deploy only approved versions, so every behavior maps to an immutable snapshot",
"Log model inputs, outputs, guardrail interventions, and version identifiers for every interaction",
"Let the model update its own prompts nightly based on user feedback to stay current",
"Disable all logging to reduce storage costs, since regulators only need the final answers",
"Change prompts directly in production and document the change in a chat message afterward"],
correct=[0,1],
why="Traceability needs two halves: immutable versioned artifacts (so a behavior maps to an exact approved snapshot) and complete interaction logs (inputs, outputs, guardrail actions, version IDs) tying each decision to that snapshot.",
why_wrong=[
"Self-updating prompts are ungoverned changes; they destroy exactly the traceability regulators demand.",
"Disabling logging removes the evidence; cost-cutting that deletes the audit trail fails the requirement.",
"Post-hoc chat documentation is not change control; production edits without approval break the chain."],
trap="Pattern 6: regulated behavior needs versioned artifacts plus logs. Every wrong option breaks one of those halves."),

dict(id="Q61", domain="D3", difficulty="Medium", format="mc",
stem="An assistant occasionally produces answers that are fluent but factually wrong about company policy. The team wants an automated check that verifies each factual claim against the retrieved documents before the answer reaches the user. Which technique is MOST correct?",
options=[
"Contextual grounding checks, which verify that generated claims are supported by the retrieved context",
"A higher temperature setting, which makes the model more careful",
"A longer system prompt describing the company's values",
"Retrying the request until the answer looks right to a reviewer"],
correct=[0],
why="Contextual grounding checks exist to verify claims against retrieved context; they are the guardrail-side mechanism for exactly this failure. Temperature, values prompts, and retries do not verify claims.",
why_wrong=[
"Higher temperature increases randomness; it makes factual precision worse, not better.",
"Values prompts shape tone and style, not factual grounding against documents.",
"Manual retry-until-right is unscalable toil and not a control; it is hope with extra steps."],
trap="Pattern 6: claim verification against retrieved context is contextual grounding. The distractors are all different-plane knobs."),

dict(id="Q62", domain="D3", difficulty="Hard", format="mc",
stem="A team tests an assistant with 500 adversarial prompts covering jailbreaks, PII extraction, and disallowed content. The assistant blocks 490. Leadership asks whether 98 percent is good enough to launch. What is the MOST correct response?",
options=[
"No: analyze the 10 failures for patterns, fix the systematic gaps, and define an explicit risk-acceptance bar with leadership before launch",
"Yes: 98 percent is an A grade, so launch immediately",
"No: no system may ever launch until it blocks 100 percent of adversarial prompts",
"Yes: adversarial testing is just a formality, so the number does not matter"],
correct=[0],
why="The exam's safety posture is risk-based, not grade-based: investigate the failures (a pattern in 10 failures can be one systematic hole), fix what is fixable, and make the launch decision an explicit risk acceptance with leadership. Neither blind launching nor demanding impossible perfection is correct.",
why_wrong=[
"'A grade' thinking treats safety as school; 10 systematic failures can be one exploited hole, not 2 percent noise.",
"Demanding 100 percent is an impossible bar that blocks every launch; the exam expects risk management, not perfectionism.",
"Dismissing adversarial testing contradicts the entire responsible-AI practice the domain tests."],
trap="Pattern 2: both absolutes are wrong. The exam wants failure analysis plus explicit risk acceptance."),

dict(id="Q63", domain="D3", difficulty="Medium", format="mc",
stem="A company uses a third-party model through Bedrock Marketplace for a specialized task. The security team asks who is responsible for the model's safety behavior: AWS, the model provider, or the company. What is the MOST correct guidance?",
options=[
"The company remains responsible for safe deployment: it must evaluate the model and apply guardrails, using provider safety documentation as input",
"The model provider is solely responsible, so no company-side safety work is needed",
"AWS is solely responsible for all models available through Bedrock, including Marketplace models",
"Safety responsibility is automatically handled by the model's built-in alignment, so deployment needs no extra controls"],
correct=[0],
why="The shared-responsibility reality: the deployer owns safe deployment. Provider documentation informs the evaluation, and the company must still test and guardrail the model in its own context. No party's work eliminates the deployer's responsibility.",
why_wrong=[
"Provider responsibility does not transfer the deployer's duty; the provider cannot test the company's specific use case.",
"AWS provides the platform; it does not assume responsibility for each Marketplace model's behavior in customer applications.",
"'Built-in alignment is enough' is trap 15 again: alignment is one layer, not a deployment safety program."],
trap="Pattern 6, trap 15: built-in safety never transfers the deployer's responsibility. The exam always keeps responsibility with the deployer."),
]

# ---------------- Domain 4 (Q64-Q73) ----------------
QUESTIONS += [
dict(id="Q64", domain="D4", difficulty="Easy", format="mc",
stem="A company trains a custom model on SageMaker AI using proprietary source code. The training data must never leave the company's AWS environment, and the training cluster must have no internet access. Which networking setup is MOST correct?",
options=[
"Run the training jobs in a VPC with no internet gateway or NAT, using VPC endpoints for the AWS services the job needs",
"Run the training jobs on the public internet but encrypt the dataset with KMS",
"Download the dataset to engineers' laptops and train locally to keep it off the network",
"Use the default SageMaker network settings, which already block all internet access"],
correct=[0],
why="VPC-isolated training with no internet path, plus VPC endpoints for required AWS services, is the exam's data-containment pattern. Encryption protects data at rest and in transit but does not remove the internet path; defaults do not isolate.",
why_wrong=[
"Encryption without network isolation still leaves an internet path; the requirement is no internet access, not just encrypted access.",
"Laptop training is ungoverned, unscalable, and a data-loss risk; it is the opposite of a controlled environment.",
"Default SageMaker networking does not provide VPC isolation; isolation must be explicitly configured."],
trap="Pattern 1: 'never leave the environment, no internet access' is a network-isolation constraint. Only the VPC option satisfies it."),

dict(id="Q65", domain="D4", difficulty="Medium", format="mc",
stem="A training job processes 50 TB of data stored in S3. Data loading is the bottleneck: GPUs sit idle waiting for batches. Which storage optimization is MOST correct?",
options=[
"Use FSx for Lustre backed by the S3 dataset as a high-throughput parallel file system for the training job",
"Copy the 50 TB to EBS volumes attached to each training instance",
"Stream the data directly from S3 with no caching and accept the idle GPUs",
"Compress the dataset into a single ZIP file in S3 for faster transfer"],
correct=[0],
why="FSx for Lustre provides a parallel high-throughput file system linked to S3, designed exactly for the data-loading bottleneck in large training jobs. Per-instance EBS copies multiply storage and copy time; a single ZIP serializes access.",
why_wrong=[
"EBS copies per instance mean 50 TB copied N times with no parallel read benefit; it is slower and more expensive.",
"Accepting idle GPUs wastes the most expensive resource in the job; the bottleneck is the thing to fix.",
"A single ZIP forces serialized decompression and single-stream reads; it is the opposite of parallel data loading."],
trap="Pattern 1: 'GPUs idle waiting for data' is a data-loading bottleneck. The fix is parallel high-throughput storage, not more compute."),

dict(id="Q66", domain="D4", difficulty="Medium", format="mc",
stem="A team fine-tunes a 70B-parameter model. A single GPU cannot hold the model, so they split layers across 8 GPUs, and they also shard the optimizer state to reduce memory per GPU. Which techniques are they using?",
options=[
"Model parallelism for splitting layers across GPUs, and ZeRO-style optimizer sharding for the optimizer state",
"Data parallelism for both, since all parallelism is data parallelism",
"Pipeline parallelism for the optimizer state and tensor parallelism for the data",
"Quantization for the layer split and pruning for the optimizer state"],
correct=[0],
why="Splitting model layers across GPUs is model parallelism; sharding optimizer state across workers is the ZeRO technique. The scenario describes each mechanism precisely.",
why_wrong=[
"Data parallelism replicates the model and splits the data; it does not split layers, and it does not describe optimizer sharding.",
"Pipeline parallelism is a form of model parallelism for layers, but it does not describe optimizer state sharding; the terms are swapped.",
"Quantization and pruning reduce precision and size; neither describes distributing layers or sharding optimizer state."],
trap="Pattern 4: parallelism vocabulary. Layer split equals model parallelism; optimizer sharding equals ZeRO."),

dict(id="Q67", domain="D4", difficulty="Hard", format="mr", select=2,
stem="A pre-training run on a large cluster keeps failing: some runs diverge with loss spikes, others crash when a single node fails. Which TWO practices address these failure modes? (Select TWO)",
options=[
"Add gradient clipping and learning-rate warmup to control loss spikes and divergence",
"Use checkpointing with automatic restart so a node failure resumes from the last saved state instead of from scratch",
"Increase the batch size indefinitely, which prevents both divergence and node failures",
"Disable all logging to make the training run faster and more stable",
"Train on a single GPU to eliminate multi-node failure modes"],
correct=[0,1],
why="Loss spikes are an optimization-stability problem (gradient clipping plus warmup is the standard control), and node failures are a fault-tolerance problem (checkpoints with auto-restart). Each practice targets one failure mode.",
why_wrong=[
"Batch size affects optimization dynamics but does not fix node failures, and unbounded batches cause their own divergence.",
"Disabling logging blinds the team without improving stability; observability is not the failure.",
"Single-GPU training abandons the cluster scale the job needs; it avoids the problem by refusing the workload."],
trap="Pattern 1: two distinct failure modes need two distinct fixes. Each wrong option fixes neither or refuses the workload."),

dict(id="Q68", domain="D4", difficulty="Medium", format="mc",
stem="After fine-tuning, a model performs well on the fine-tuning task but has noticeably degraded on general knowledge it previously had. What is this phenomenon, and what is the MOST correct mitigation?",
options=[
"Catastrophic forgetting; mitigate with a replay buffer of general data mixed into fine-tuning, or use parameter-efficient adapters instead of full fine-tuning",
"Overfitting; mitigate by training for more epochs on the fine-tuning data",
"Underfitting; mitigate by increasing the learning rate sharply",
"Data leakage; mitigate by encrypting the fine-tuning dataset"],
correct=[0],
why="Catastrophic forgetting is the loss of prior capabilities when weights shift toward the new task. Replay buffers preserve general knowledge during training, and LoRA-style adapters change far fewer weights, limiting the damage.",
why_wrong=[
"More epochs on the same data worsens forgetting and overfitting; it is the opposite of the fix.",
"A sharply higher learning rate destabilizes training further; it accelerates forgetting, not recovery.",
"Encryption addresses data protection, not capability loss; wrong plane entirely."],
trap="Pattern 6: name the phenomenon (catastrophic forgetting), then pick the mitigation that matches it. The distractors name real phenomena with wrong fixes."),

dict(id="Q69", domain="D4", difficulty="Easy", format="mc",
stem="A team evaluates a fine-tuned summarization model. They need a quick automated signal of summary quality during development, plus a definitive human judgment before release. Which pairing is MOST correct?",
options=[
"ROUGE scores for fast automated iteration, plus human evaluation of factuality and usefulness before release",
"Human evaluation for every training epoch, because automation is never useful",
"ROUGE scores as the sole release criterion, because they are fully objective",
"Model loss curves only, because lower loss always means better summaries"],
correct=[0],
why="ROUGE gives cheap automated iteration signal during development, and human judgment on factuality and usefulness is the release gate. Automated metrics guide; humans decide.",
why_wrong=[
"Human review every epoch is too slow and expensive for the iteration loop; automation exists for this phase.",
"ROUGE measures n-gram overlap, not factuality; it cannot be the sole release criterion.",
"Loss measures training fit, not summary quality; lower loss does not guarantee better or more factual summaries."],
trap="Pattern 2: the exam pairs cheap automated metrics for iteration with human judgment for release. Absolutes on either side are wrong."),

dict(id="Q70", domain="D4", difficulty="Medium", format="mc",
stem="A fine-tuning dataset contains customer support transcripts. Before training, the team must reduce the risk of the model memorizing and regurgitating customer phone numbers. What is the MOST correct data preparation step?",
options=[
"Scrub PII from the training data with detection and redaction before training begins",
"Train first and add a guardrail afterward to catch phone numbers in outputs",
"Encrypt the dataset; encrypted PII cannot be memorized",
"Rely on the base model's safety alignment to avoid regurgitating phone numbers"],
correct=[0],
why="PII scrubbing before training is the data-curation control: what never enters the training set cannot be memorized. Post-hoc guardrails are a second layer, not a substitute for clean data.",
why_wrong=[
"Post-training guardrails help but do not remove memorized PII from the weights; the exam wants the data-layer fix first.",
"Encryption protects data at rest; training decrypts it, and the model memorizes the plaintext. Wrong plane.",
"Base alignment does not prevent memorization of fine-tuning data; alignment is not a data-curation control."],
trap="Pattern 6, trap 15: the fix belongs at the data layer (scrub before training), not as a post-hoc filter or alignment hope."),

dict(id="Q71", domain="D4", difficulty="Hard", format="mc",
stem="A team fine-tunes with LoRA adapters. After deployment, they need to serve the base model plus three task-specific adapters from the same endpoint fleet, switching adapters per request with minimal latency. What is the MOST correct serving approach?",
options=[
"Serve the shared base model with dynamically loaded adapters per request, keeping one base in memory and swapping lightweight adapters",
"Deploy three separate full-model copies, one per adapter, tripling the GPU footprint",
"Merge all three adapters into the base weights permanently and serve one model",
"Bake each adapter into a separate container image and redeploy for every request type"],
correct=[0],
why="Adapters are small by design; the efficient pattern is one resident base model with per-request adapter loading. Separate full copies triple GPU cost, and permanent merging destroys the ability to switch tasks.",
why_wrong=[
"Full copies per adapter waste GPU memory on duplicated base weights; it ignores the entire point of adapters.",
"Merging is irreversible per deployment and prevents per-request task switching; it throws away adapter flexibility.",
"Per-request redeploys are absurd operationally; container swaps are minutes, not milliseconds."],
trap="Pattern 5: the adapter architecture exists so you do not duplicate the base. Any option that duplicates or destroys that property is wrong."),

dict(id="Q72", domain="D4", difficulty="Medium", format="mr", select=2,
stem="A company must keep full lineage for a fine-tuned model: which dataset version, which code, which hyperparameters, and which base model produced it. Which TWO SageMaker AI capabilities support this? (Select TWO)",
options=[
"SageMaker Model Registry to version the model artifacts with metadata and approval status",
"SageMaker Experiments to track hyperparameters, code versions, and dataset references per training run",
"Storing the model weights on an engineer's workstation with a README file",
"Emailing the hyperparameters to the team after each run",
"Keeping lineage in the model file's filename, like model_v7_final_FINAL.pt"],
correct=[0,1],
why="Model Registry versions artifacts with metadata and approval gates; Experiments tracks the full run context (hyperparameters, code, data references). Together they are the lineage story.",
why_wrong=[
"Workstation storage is ungoverned and unshared; it is not lineage, it is a single point of failure.",
"Email is not a system of record; hyperparameters in inboxes are unqueryable and unauditable.",
"Filenames are not metadata; they carry no queryable lineage and no approval state."],
trap="Pattern 2: lineage needs systems of record (Registry plus Experiments). Every wrong option is an informal substitute."),

dict(id="Q73", domain="D4", difficulty="Medium", format="mc",
stem="A pre-training dataset is assembled from web crawls. The team discovers it contains large amounts of duplicated text, machine-generated spam, and some toxic content. What is the MOST correct data curation sequence?",
options=[
"Deduplicate, filter spam and low-quality text, remove toxic content, then document the dataset composition before training",
"Train on the raw crawl; scale overcomes data quality problems",
"Remove toxic content only; duplicates and spam are harmless at scale",
"Document the raw crawl as-is and skip curation to save time"],
correct=[0],
why="Data curation is a pipeline: dedup first (duplicates distort training), then quality and spam filtering, then toxicity removal, then documentation of what remains. 'Scale overcomes quality' is the exam's classic data fallacy.",
why_wrong=[
"Scale amplifies data problems; duplicates and spam at scale produce a worse model, not a better one.",
"Duplicates waste training compute and spam degrades quality; ignoring them is not harmless.",
"Skipping curation to save time trades weeks of training cost for hours of preparation; it is false economy."],
trap="Pattern 2: 'scale fixes data' is the tempting fallacy. The exam rewards the curation pipeline in order."),
]

# ---------------- Domain 5 (Q74-Q81) ----------------
QUESTIONS += [
dict(id="Q74", domain="D5", difficulty="Easy", format="mc",
stem="A company deploys a customer-facing assistant. The compliance team requires that all prompts and model responses be logged for audit, but customer PII in the logs must be protected. Which logging design is MOST correct?",
options=[
"Enable model invocation logging to S3 with KMS encryption, and redact or mask PII before or as logs are written",
"Disable all logging to avoid storing any customer data",
"Log prompts and responses in plain text to a public S3 bucket for easy auditor access",
"Store logs only in the application's memory so they disappear on restart"],
correct=[0],
why="Audit requires the logs to exist; PII protection requires encryption at rest (KMS) plus redaction or masking of sensitive fields. Both halves of the requirement are honored.",
why_wrong=[
"Disabling logging refuses the audit requirement instead of satisfying it securely.",
"Plain-text public logging violates every data-protection principle; accessibility for auditors comes through IAM, not public buckets.",
"In-memory-only logs are not an audit trail; they vanish and cannot be reviewed."],
trap="Pattern 1: the stem has two constraints (audit + PII protection). Only the option honoring both is correct."),

dict(id="Q75", domain="D5", difficulty="Medium", format="mc",
stem="A company processes customer feedback with a Bedrock model. Legal requires that prompts and responses never be used to train or improve any AWS model, and that data stay within the AWS region. Which statement is MOST correct?",
options=[
"Bedrock does not use customer prompts or responses to train models, and data stays within the selected region for processing",
"Bedrock trains on customer data by default; the company must file a support ticket to opt out per request",
"Data residency is automatic across all regions simultaneously, so region selection does not matter",
"The company must encrypt prompts client-side or AWS will use them for training"],
correct=[0],
why="Bedrock's documented posture: customer content is not used for model training or improvement, and processing stays in the selected region. This is the compliance fact the exam tests directly.",
why_wrong=[
"There is no default training on customer data and no per-request opt-out; the premise is false.",
"Region selection determines where processing happens; claiming it does not matter contradicts the residency requirement.",
"Client-side encryption is not the mechanism; the no-training-use posture is contractual and architectural, not encryption-dependent."],
trap="Pattern 6: the exam tests Bedrock's actual data-use posture. Distractors invent opt-outs and conditions that do not exist."),

dict(id="Q76", domain="D5", difficulty="Medium", format="mr", select=2,
stem="A GenAI application handles EU customer data. Which TWO controls support GDPR-aligned deployment on Bedrock? (Select TWO)",
options=[
"Keep processing in an EU region and use cross-region inference only with profiles that preserve the required data residency",
"Apply data minimization: send the model only the customer data the task needs, and set retention policies on logs",
"Store all EU customer data in a US region because S3 is cheaper there",
"Send full customer records to the model on every request to maximize answer quality",
"Disable encryption because GDPR only cares about consent, not security"],
correct=[0,1],
why="GDPR alignment is residency plus minimization: process in-region (and choose inference profiles whose routing preserves residency) and send only necessary data with bounded log retention.",
why_wrong=[
"US-region storage for EU data violates the residency posture the scenario requires; cost does not override it.",
"Full records on every request is the opposite of data minimization; it maximizes exposure for speculative quality gains.",
"GDPR requires appropriate security including encryption; claiming otherwise is false."],
trap="Pattern 2: residency plus minimization. Each wrong option sacrifices one of them for cost, convenience, or a false legal claim."),

dict(id="Q77", domain="D5", difficulty="Hard", format="mc",
stem="An assistant stores conversation history for context. A user exercises their right to erasure and asks that all their data be deleted. The history lives in the agent's session store, invocation logs in S3, and embeddings derived from their documents in a vector index. What is the MOST correct deletion approach?",
options=[
"Delete from all three locations (session store, S3 logs, and the vector index entries), and verify each deletion, because erasure must cover derived data too",
"Delete the session store entry only; logs and embeddings are system data, not user data",
"Anonymize the user's name in future responses and leave stored data untouched",
"Wait 30 days; the data will age out of all three systems automatically"],
correct=[0],
why="Erasure covers the user's data wherever it lives, including derived forms like embeddings; logs and indexes do not become 'system data' exempt from the request. Each store needs explicit deletion with verification.",
why_wrong=[
"'System data' is not a GDPR exemption for user-derived content; logs and embeddings of user data are in scope.",
"Future anonymization does not delete stored data; the request is about existing stores.",
"Automatic aging is not a deletion process; retention windows do not satisfy an explicit erasure request."],
trap="Pattern 6: derived data (embeddings) counts. The exam tests whether you remember that erasure reaches the vector index."),

dict(id="Q78", domain="D5", difficulty="Medium", format="mc",
stem="A team discovers their assistant's training and evaluation data over-represents one demographic and under-represents others. The assistant will serve a global user base. What is the MOST correct response?",
options=[
"Rebalance the dataset to represent the served population, add fairness evaluations slicing metrics by demographic, and monitor for disparate performance after launch",
"Ship as-is; the model will generalize to under-represented groups automatically",
"Remove all demographic information from the data; blindness guarantees fairness",
"Collect more data only from the over-represented group to improve overall accuracy"],
correct=[0],
why="Bias mitigation is a loop: rebalance the data toward the served population, measure sliced metrics to detect disparate performance, and keep monitoring in production. Each step addresses one part of the problem.",
why_wrong=[
"Generalization does not fix representation gaps; under-represented groups stay under-served without intervention.",
"Blindness hides measurement without fixing outcomes; you cannot detect disparate impact on groups you refuse to measure.",
"More majority-group data worsens the imbalance; it optimizes the average while harming the minority."],
trap="Pattern 2: 'blindness guarantees fairness' is the tempting fallacy. The exam rewards measure, rebalance, and monitor."),

dict(id="Q79", domain="D5", difficulty="Easy", format="mc",
stem="A company builds an assistant that writes performance reviews from manager notes. HR policy requires a human to review and approve every generated review before it is shared. Which deployment pattern is MOST correct?",
options=[
"Human-in-the-loop: the assistant drafts, a Step Functions workflow routes each draft to the manager for approval via task token, and only approved drafts are delivered",
"Fully autonomous delivery; the model is accurate enough that review adds no value",
"Human-on-the-loop: deliver all drafts immediately and let managers complain afterward if something is wrong",
"Disable the assistant; automation has no place in performance reviews"],
correct=[0],
why="High-stakes outputs affecting people require human-in-the-loop: the human approves before delivery, enforced by a workflow gate, not by policy text. On-the-loop (review after delivery) is too late for irreversible harm.",
why_wrong=[
"Autonomous delivery of performance reviews removes the required human judgment; accuracy claims do not override HR policy.",
"Post-delivery complaints mean the harm already happened; on-the-loop is the wrong pattern for this stakes level.",
"Disabling refuses the use case instead of governing it; the requirement is approval-gated automation, not no automation."],
trap="Pattern 4: in-the-loop (approve before) versus on-the-loop (monitor after). Stakes decide, and performance reviews are high-stakes."),

dict(id="Q80", domain="D5", difficulty="Medium", format="mc",
stem="A support assistant's CloudWatch dashboard shows a rising InvocationThrottles metric on the AWS/Bedrock namespace, and users report intermittent 'try again' errors. InputTokenCount and OutputTokenCount are flat. What is the MOST correct interpretation and fix?",
options=[
"The application is hitting API throttling limits; add exponential backoff with jitter and consider spreading load or requesting quota increases",
"The model is generating too many tokens; reduce max tokens to fix the throttling",
"CloudWatch metrics are delayed; wait 24 hours and the throttles will clear",
"The knowledge base is out of sync; re-sync it to stop the throttling"],
correct=[0],
why="InvocationThrottles counts throttled API calls; flat token counts rule out a token-volume cause. The fix is client-side backoff with jitter plus capacity-side options (load spreading, quota increases).",
why_wrong=[
"Token counts are flat, so token volume is not the cause; reducing max tokens fixes nothing.",
"Waiting ignores an active user-facing failure; throttling does not self-clear under sustained load.",
"KB sync state has no relationship to API throttling; the metric names the plane (API calls), and the fix must live there."],
trap="Pattern 1: read the metric. Throttles with flat tokens means rate limiting, not token bloat. Fix the call pattern."),

dict(id="Q81", domain="D5", difficulty="Hard", format="mc",
stem="A company must demonstrate continuous responsible-AI governance: model risk assessments before launch, guardrails in production, ongoing monitoring, and periodic re-assessment. Which operating pattern is MOST correct?",
options=[
"A governance pipeline: risk assessment gates promotion to production, guardrails enforce policy at runtime, CloudWatch monitors invocations and guardrail interventions, and scheduled reviews re-assess risk as models and data change",
"A one-time risk assessment before the first launch, with no further reviews",
"Guardrails only, because runtime enforcement replaces governance",
"Monitoring only, because observed behavior is the only thing that matters"],
correct=[0],
why="Governance is continuous: assess before launch, enforce at runtime, monitor always, re-assess on change. Each element covers a different phase; dropping any one leaves a gap the exam will punish.",
why_wrong=[
"One-time assessment decays as models, data, and threats change; governance must be periodic.",
"Guardrails enforce but do not assess or monitor; they are one layer, not the program.",
"Monitoring observes but does not gate launches or enforce policy; it is necessary but not sufficient."],
trap="Pattern 2: governance is a lifecycle, not a single control. Every wrong option is one layer pretending to be the whole program."),
]

# ---------------- Render + QA ----------------
import re, hashlib, html as _html, sys

def esc(s): return _html.escape(str(s))
def letter(i): return chr(65 + i)

def dshuffle(lst, seed):
    n = len(lst)
    order = sorted(range(n), key=lambda i: hashlib.md5(f"{seed}-{i}".encode()).hexdigest())
    inv = [0]*n
    for newpos, oldidx in enumerate(order): inv[oldidx] = newpos
    return [lst[o] for o in order], inv

DOMAIN_NAMES = {
 "D1": "D1: Develop and Optimize GenAI Apps with Bedrock",
 "D2": "D2: Agents, Tools, and Workflow Automation",
 "D3": "D3: Responsible AI, Guardrails, and Evaluation",
 "D4": "D4: FM Customization and Training",
 "D5": "D5: Security, Governance, and Monitoring"}

CSS = """<style>
:root{--paper:#F8F7F3;--ink:#24292F;--muted:#5C6470;--blue:#1F5FBF;--board:#163D7A;
--amber:#A15C07;--amberbg:#FDF3E3;--green:#1E7A34;--greenbg:#E9F5EC;--red:#B42318;
--redbg:#FDECEA;--card:#FFFFFF;--line:#E3E1D8}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
 font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
 line-height:1.6}
.layout{display:flex;max-width:1280px;margin:0 auto}
nav.rail{position:sticky;top:0;align-self:flex-start;width:250px;min-height:100vh;
 padding:24px 18px;border-right:1px solid var(--line);background:#FFFFFF}
nav.rail h3{font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin:0 0 10px}
nav.rail a{display:block;color:var(--ink);text-decoration:none;padding:6px 8px;border-radius:6px;font-size:14px}
nav.rail a:hover{background:var(--paper);color:var(--blue)}
main{flex:1;max-width:72ch;padding:32px 36px 80px;margin:0 auto}
h1{font-size:30px;margin:0 0 6px;color:var(--board)}
.sub{color:var(--muted);margin:0 0 24px}
h2{font-size:22px;color:var(--board);margin:44px 0 12px;padding-top:20px;border-top:2px solid var(--line)}
h3{font-size:17px;margin:26px 0 8px}
p{margin:10px 0}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:14px}
th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
th{background:#EFF3FA;color:var(--board)}
.qcard{background:var(--card);border:1px solid var(--line);border-radius:10px;
 padding:20px 22px;margin:20px 0}
.qhead{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:10px}
.qid{font-weight:700;color:var(--board);font-size:15px}
.badge{font-size:12px;font-weight:700;padding:3px 10px;border-radius:20px}
.easy{background:var(--greenbg);color:var(--green)}
.medium{background:var(--amberbg);color:var(--amber)}
.hard{background:var(--redbg);color:var(--red)}
.fmt{font-size:12px;color:var(--muted);border:1px solid var(--line);border-radius:20px;padding:3px 10px}
.domain{font-size:12px;color:var(--blue);font-weight:600}
.stem{font-size:15.5px;margin:8px 0 12px}
.opts{list-style:none;margin:10px 0;padding:0}
.opts li{padding:8px 12px;border:1px solid var(--line);border-radius:8px;margin:6px 0;background:#FCFBF8}
.opts .k{font-weight:700;color:var(--board);margin-right:8px}
.trap{background:var(--amberbg);border-left:4px solid var(--amber);padding:10px 14px;
 margin:14px 0 6px;font-size:14px;border-radius:0 8px 8px 0}
.trap b{color:var(--amber)}
details.ans{margin-top:10px;border:1px solid var(--line);border-radius:8px;background:#F4F8F1}
details.ans summary{cursor:pointer;padding:10px 14px;font-weight:700;color:var(--green)}
details.ans .body{padding:4px 16px 14px}
.why-wrong li{margin:6px 0}
.correct-line{font-weight:700;color:var(--green)}
.guide{background:#FFFFFF;border:1px solid var(--line);border-radius:10px;padding:20px 24px;margin:18px 0}
.guide h3{color:var(--board)}
ol.tight li,ul.tight li{margin:6px 0}
.verified{color:var(--green);font-weight:600}
.unverified{color:var(--red);font-weight:700}
footer{margin-top:60px;padding-top:20px;border-top:2px solid var(--line);color:var(--muted);font-size:13px}
@media(max-width:900px){nav.rail{display:none}main{padding:20px}}
</style>"""

GUIDE = """<div class="guide" id="how-aws-asks">
<h2 style="border:none;margin-top:0;padding-top:0">How AWS Asks: the 6 question patterns</h2>
<h3>Pattern 1: Constraint extraction</h3>
<p>Every stem hides 2 to 4 hard constraints (cost, latency, no ML team, no redeploy, region lock). The correct answer is the only option that satisfies ALL of them. Method: underline each constraint before reading options, then eliminate any option that violates even one.</p>
<h3>Pattern 2: MOST correct, not merely correct</h3>
<p>Two or three options will technically work. The winner is decided by tiebreakers in this order: managed service over custom build, cheaper over pricier at the same quality, simpler architecture over complex, AWS-native over third-party. When torn, ask: which option would an AWS solutions architect defend in a review?</p>
<h3>Pattern 3: Ordering and lifecycle</h3>
<p>Steps must follow the real service lifecycle: configure, then prepare, then test; select a model before customizing it; scope before building. Any option that inverts a lifecycle dependency is wrong on sight.</p>
<h3>Pattern 4: Vocabulary precision</h3>
<p>AWS tests whether you know which lever solves which problem: inference profiles (availability and resilience), prompt routers (cost by complexity), Provisioned Throughput (reserved capacity), ApplyGuardrail (standalone policy checks), returnControl (human gates). If two options sound similar, the difference is one precise term.</p>
<h3>Pattern 5: Managed-first and the ladder</h3>
<p>Default to the managed service and climb the capability ladder only until the requirement is met: prompt engineering, then RAG, then agents, then fine-tuning. Options that jump straight to training or custom builds fail the overhead filter.</p>
<h3>Pattern 6: Wrong-plane distractors</h3>
<p>Distractors name real services doing the wrong job: Guardrails for extraction, knowledge bases for live API calls, CloudFormation for runtime config, encryption for network isolation. Ask of every option: is this service's actual job the job the stem needs?</p>
</div>
<div class="guide" id="exam-surface">
<h2 style="border:none;margin-top:0;padding-top:0">Exam surface: what each domain really tests</h2>
<table><tr><th>Domain</th><th>Weight</th><th>What they actually test</th></tr>
<tr><td>D1</td><td>31%</td><td>RAG over fine-tuning for fresh documents, chunking and embedding tradeoffs, Converse API fields, prompt caching, model switching without redeploys</td></tr>
<tr><td>D2</td><td>26%</td><td>Agent lifecycle (configure, prepare, test), action groups with Lambda or OpenAPI, knowledge base grounding, returnControl for approvals, trace for debugging</td></tr>
<tr><td>D3</td><td>20%</td><td>Guardrail control types, denied topics vs word filters vs PII filters, defense in depth on inputs and outputs, faithfulness and citation metrics, LLM-as-a-judge bias</td></tr>
<tr><td>D4</td><td>12%</td><td>LoRA vs full fine-tuning, catastrophic forgetting, data curation order, distributed training vocabulary, SageMaker lineage (Registry plus Experiments)</td></tr>
<tr><td>D5</td><td>11%</td><td>Bedrock data-use posture (no training on customer data), VPC isolation, human-in-the-loop for high-stakes outputs, CloudWatch Bedrock metrics, erasure covering derived data</td></tr>
</table>
</div>
<div class="guide" id="tactics">
<h2 style="border:none;margin-top:0;padding-top:0">Tactics: how to attack each format</h2>
<ul class="tight">
<li><b>Multiple choice:</b> extract constraints first, then eliminate. Never pick an option that violates a stated constraint, even if it sounds sophisticated.</li>
<li><b>Multiple response:</b> evaluate each option independently against the constraints. The two correct answers each stand alone; do not look for pairs that sound good together.</li>
<li><b>Ordering:</b> anchor the first and last steps (what must come before everything, what must come last), then fill the middle. Lifecycle dependencies decide ties.</li>
<li><b>Matching:</b> match the most distinctive pair first to shrink the field, then the next. Never match by vague association; each pair has one precise mechanism.</li>
<li><b>Time management:</b> 75 questions in 180 minutes is about 2.4 minutes per question. If an option violates a constraint on sight, eliminate and move on.</li>
</ul>
</div>
<div class="guide" id="trap-catalog">
<h2 style="border:none;margin-top:0;padding-top:0">Trap catalog: the 15 traps AWS reuses</h2>
<ol class="tight">
<li><b>Lambda 15-minute timeout:</b> any option with a Lambda waiting, sleeping, or polling for a long task dies. Go async or use Step Functions.</li>
<li><b>Custom code vs managed:</b> when the stem says no ML team or least effort, custom builds lose to Bedrock managed features.</li>
<li><b>Knowledge base scope:</b> knowledge bases serve documents. They never call APIs, never enforce access control, never execute actions.</li>
<li><b>Fine-tuning for fresh data:</b> changing documents or a need for citations means RAG, never fine-tuning.</li>
<li><b>Capacity confusion set:</b> inference profiles for availability, prompt routers for cost by complexity, Provisioned Throughput for reserved capacity. Do not mix them.</li>
<li><b>Guardrails wrong plane:</b> guardrails filter content. They do not extract data, enforce tenant isolation, or replace IAM.</li>
<li><b>Ladder jumping:</b> the cheapest option that meets the requirement wins. Premium features without a stated need lose.</li>
<li><b>CloudFormation for runtime config:</b> a stack update is a deployment. Runtime switching without redeploys means AppConfig.</li>
<li><b>ElastiCache as storage:</b> ElastiCache is ephemeral caching. Durable vectors live in a vector store.</li>
<li><b>Residency blindness:</b> cross-region failover is wrong when the stem requires data residency. Check the region constraint first.</li>
<li><b>Prompt Management plus guardrailConfig:</b> Converse rejects that combination. ApplyGuardrail standalone is the workaround.</li>
<li><b>Missing prepare step:</b> agent config changes need prepare before testing. Changed-but-same-behavior means prepare was skipped.</li>
<li><b>Misleading AccessDenied:</b> check model availability in the region before debugging permissions.</li>
<li><b>Converse for embeddings:</b> Converse is text generation only. Embeddings go through InvokeModel.</li>
<li><b>Built-in safety is enough:</b> alignment and guardrails never transfer the deployer's responsibility to evaluate and govern.</li>
</ol>
</div>"""

def render_question(q):
    h = []
    h.append(f'<div class="qcard" id="{q["id"]}">')
    h.append('<div class="qhead">')
    h.append(f'<span class="qid">{q["id"]}</span>')
    h.append(f'<span class="badge {q["difficulty"].lower()}">{q["difficulty"]}</span>')
    fmt_label = {"mc":"Multiple choice","mr":"Multiple response","ordering":"Ordering","matching":"Matching"}[q["format"]]
    h.append(f'<span class="fmt">{fmt_label}</span>')
    h.append(f'<span class="domain">{DOMAIN_NAMES[q["domain"]]}</span>')
    h.append('</div>')
    h.append(f'<p class="stem">{esc(q["stem"])}</p>')
    fmt = q["format"]
    if fmt in ("mc","mr"):
        if fmt=="mr": h.append(f'<p><i>Select {q["select"]}.</i></p>')
        h.append('<ol class="opts">')
        for i,opt in enumerate(q["options"]):
            h.append(f'<li><span class="k">{letter(i)}.</span>{esc(opt)}</li>')
        h.append('</ol>')
        corr = ", ".join(letter(i) for i in q["correct"])
    elif fmt=="ordering":
        steps, inv = dshuffle(q["steps"], q["id"])
        h.append('<ol class="opts">')
        for i,s in enumerate(steps):
            h.append(f'<li><span class="k">{i+1}.</span>{esc(s)}</li>')
        h.append('</ol>')
        seq = " then ".join(str(inv[i]+1) for i in range(len(steps)))
        h.append(f'<!-- order answer: {esc(seq)} -->')
        corr = None
    elif fmt=="matching":
        rights = [p[1] for p in q["pairs"]]
        rshuf, inv = dshuffle(rights, q["id"])
        h.append('<table><tr><th>Items</th><th>Descriptions</th></tr>')
        for i,p in enumerate(q["pairs"]):
            h.append(f'<tr><td><b>{i+1}.</b> {esc(p[0])}</td><td><b>{letter(inv[i])}.</b> {esc(rshuf[inv[i]])}</td></tr>')
        h.append('</table>')
        corr = None
    h.append(f'<div class="trap"><b>The trap AWS set here:</b> {esc(q["trap"])}</div>')
    # answer block
    h.append('<details class="ans"><summary>Show answer and explanations</summary><div class="body">')
    if fmt in ("mc","mr"):
        h.append(f'<p class="correct-line">Correct: {corr}</p>')
    elif fmt=="ordering":
        h.append('<p class="correct-line">Correct order:</p><ol>')
        for s in q["steps"]: h.append(f'<li>{esc(s)}</li>')
        h.append('</ol>')
    elif fmt=="matching":
        h.append('<p class="correct-line">Correct matches:</p><ul>')
        for i,p in enumerate(q["pairs"]):
            h.append(f'<li><b>{i+1} &rarr; {letter(inv[i])}</b>: {esc(p[0])} matches {esc(p[1])}</li>')
        h.append('</ul>')
    h.append(f'<p><b>Why this is correct:</b> {esc(q["why"])}</p>')
    h.append('<p><b>Why each distractor is wrong:</b></p><ul class="why-wrong tight">')
    for w in q["why_wrong"]: h.append(f'<li>{esc(w)}</li>')
    h.append('</ul></div></details></div>')
    return "\n".join(h)

# ---- assemble ----
total = len(QUESTIONS)
fmt_counts = {}
dom_counts = {}
for q in QUESTIONS:
    fmt_counts[q["format"]] = fmt_counts.get(q["format"],0)+1
    dom_counts[q["domain"]] = dom_counts.get(q["domain"],0)+1

nav = ['<nav class="rail"><h3>Question Patterns</h3>',
 '<a href="#how-aws-asks">How AWS asks</a>',
 '<a href="#exam-surface">Exam surface</a>',
 '<a href="#tactics">Tactics</a>',
 '<a href="#trap-catalog">Trap catalog</a>',
 '<h3 style="margin-top:18px">Questions by domain</h3>']
for d in ["D1","D2","D3","D4","D5"]:
    nav.append(f'<a href="#{d}">{DOMAIN_NAMES[d]} ({dom_counts.get(d,0)})</a>')
nav.append('<a href="#verification-log">Verification log</a></nav>')
nav_html = "\n".join(nav)

body = []
body.append('<main>')
body.append('<h1>AWS AIP-C01: Question Patterns</h1>')
body.append(f'<p class="sub">{total} original practice questions across all five domains, built from the question patterns AWS actually uses. Formats: '
 + ", ".join(f'{k} {v}' for k,v in sorted(fmt_counts.items()))
 + '. Every question shows the trap AWS set and hides the answer until you ask for it. Last verified against AWS documentation: 2026-09-28.</p>')
body.append(GUIDE)
for d in ["D1","D2","D3","D4","D5"]:
    body.append(f'<h2 id="{d}">{esc(DOMAIN_NAMES[d])}</h2>')
    for q in [x for x in QUESTIONS if x["domain"]==d]:
        body.append(render_question(q))

VLOG = """<h2 id="verification-log">Verification log</h2>
<div class="guide"><p>Every AWS service fact used in these questions was verified against official AWS documentation on <b>2026-09-28</b>. Facts that could not be verified against a live official source are marked <span class="unverified">UNVERIFIED</span> below and are not asserted as fact in any question.</p>
<ul class="tight">
<li><span class="verified">Verified:</span> Converse API fields (modelId, messages, system, inferenceConfig, toolConfig, guardrailConfig, additionalModelRequestFields, outputConfig, promptVariables), content blocks (toolUse, toolResult, cachePoint, guardContent, reasoningContent), and the restriction that Prompt Management prompts cannot combine with inline guardrailConfig, inferenceConfig, system, or toolConfig.</li>
<li><span class="verified">Verified:</span> Guardrail control types: content filters (Hate, Insults, Sexual, Violence, Misconduct, Prompt Attack; LOW/MEDIUM/HIGH), denied topics, word filters (exact match), sensitive-information filters (block/mask PII plus custom regex), contextual grounding, Automated Reasoning checks; ApplyGuardrail as a standalone model-agnostic API.</li>
<li><span class="verified">Verified:</span> Knowledge base chunking strategies (default, fixed-size, hierarchical, semantic, none, plus custom Lambda), set per data source at creation; Titan Text Embeddings v2 dimensions (256/512/1024); Cohere Embed English and Multilingual (1024); vector store options including OpenSearch Serverless, Aurora PostgreSQL, Pinecone, Redis, MongoDB Atlas, Neptune Analytics, OpenSearch managed cluster, S3 Vectors.</li>
<li><span class="verified">Verified:</span> Cross-region inference via geographic profiles (us., eu. prefixes) and global profiles; prefix as data-residency decision; some models requiring inference profile IDs; inference profiles not supporting Provisioned Throughput.</li>
<li><span class="verified">Verified:</span> Batch inference via CreateModelInvocationJob with S3 input/output; no tool calling or structured output in batch; no prompt caching in batch; provisioned models excluded from batch.</li>
<li><span class="verified">Verified:</span> Prompt caching via cachePoint after stable content, per-model minimum token thresholds, TTL options (default 5 min, up to 1 hour), cacheReadInputTokens and cacheWriteInputTokens usage fields.</li>
<li><span class="verified">Verified:</span> Agents: invoke_agent parameters (agentId, agentAliasId, sessionId, inputText, enableTrace), returnControl, endSession, prepare-after-change requirement, aliases, multi-agent supervisor/collaborator with conversation history relay, action groups via Lambda executor or OpenAPI/function schema.</li>
<li><span class="verified">Verified:</span> Prompt Management versions numbered from 1 as immutable snapshots; variants for A/B testing.</li>
<li><span class="verified">Verified:</span> Evaluation metric families: programmatic (BERT Score, F1, exact match), LLM-as-a-judge dimensions (correctness, completeness, faithfulness, harmfulness, refusal, stereotyping, professional style/tone), human evaluation options, RAG retrieval and retrieve-and-generate metrics (context relevance, context coverage, faithfulness, correctness, completeness, citation precision/coverage).</li>
<li><span class="verified">Verified:</span> Bedrock Data Automation for documents, images, video, and audio with blueprints for custom fields; usable as a knowledge base parser.</li>
<li><span class="verified">Verified:</span> CloudWatch AWS/Bedrock metrics: Invocations, InputTokenCount, OutputTokenCount, InvocationThrottles.</li>
<li><span class="verified">Verified:</span> Lambda 15-minute maximum timeout; Step Functions Standard up to 1 year with task tokens for human approvals; InvokeModel (not Converse) for embeddings.</li>
<li><span class="unverified">UNVERIFIED:</span> Exact Bedrock pricing figures are not stated in any question; all cost claims are qualitative (discounted, lower, cheaper), which matches how the exam itself phrases cost comparisons.</li>
<li><span class="unverified">UNVERIFIED:</span> The AppConfig plus Lambda plus API Gateway model-switching architecture is presented as the exam's canonical pattern per preparation providers, not as an AWS-documented reference architecture.</li>
<li><span class="unverified">UNVERIFIED:</span> No exact default chunk-size token count is asserted anywhere; chunking questions use relative comparisons only.</li>
</ul></div>"""
body.append(VLOG)
body.append('<footer>Built from original questions written for the AIP-C01 exam blueprint. Public sources were studied for style and coverage only; no question text was copied from any source. Generic content only.</footer>')
body.append('</main>')

page = ("<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
 "<meta name='viewport' content='width=device-width,initial-scale=1'>"
 "<title>AWS AIP-C01: Question Patterns</title>" + CSS + "</head><body>"
 '<div class="layout">' + nav_html + "\n".join(body) + "</div></body></html>")

OUT = "/home/hatch/workspace/your_files/aws-aip-c01-cert/volume-question-patterns.html"

# ---- QA ----
errors = []
if "\u2014" in page: errors.append("em dash found in output")
if "linear-gradient" in page: errors.append("gradient found in output")
ids = re.findall(r'id="([^"]+)"', page)
dupes = {i for i in ids if ids.count(i) > 1}
if dupes: errors.append(f"duplicate ids: {dupes}")
# tag balance via html.parser
from html.parser import HTMLParser
class Bal(HTMLParser):
    VOID = {"meta","br","hr","img","input","link"}
    def __init__(self):
        super().__init__(convert_charrefs=True); self.stack=[]; self.errs=[]
    def handle_starttag(self,t,a):
        if t not in self.VOID: self.stack.append(t)
    def handle_endtag(self,t):
        if t in self.VOID: return
        if self.stack and self.stack[-1]==t: self.stack.pop()
        elif t in self.stack:
            while self.stack and self.stack[-1]!=t: self.errs.append("unclosed "+self.stack.pop())
            self.stack.pop()
        else: self.errs.append("stray /"+t)
b = Bal(); b.feed(page)
if b.stack: errors.append("unclosed tags: "+str(b.stack))
if b.errs: errors.append("tag errors: "+str(b.errs[:5]))
# question-level checks
for q in QUESTIONS:
    if q["format"] in ("mc","mr"):
        if len(q["options"]) != len(q["why_wrong"]) + len(q["correct"]):
            errors.append(f'{q["id"]}: options/why_wrong/correct count mismatch')
print(f"questions={len(QUESTIONS)} formats={fmt_counts} domains={dom_counts}")
if errors:
    print("QA FAIL:"); [print(" -",e) for e in errors]; sys.exit(1)
print("QA PASS")
open(OUT,"w",encoding="utf-8").write(page)
print("wrote", OUT, len(page), "bytes")

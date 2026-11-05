#!/usr/bin/env python3
"""Rebuild AIP-C01 study pages into an offline visual treatise.

Reads the current volume and companion HTML, keeps the topics, facts,
figures that exist on disk, and practice questions, and writes long-scroll
pages that peel each topic from claim to mechanism to numbers to a worked
scenario to the exam trap.
"""

from __future__ import annotations

import html
import os
import re
import subprocess
import sys
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).resolve().parents[1]
PLATE_DIR = ROOT / "assets" / "img" / "treatise"

NUM_UNIT = re.compile(
    r"(%|percent|token|quota|limit|second|minute|hour|millisecond|\bms\b|"
    r"\bMB\b|\bGB\b|\bTB\b|request|throughput|window|dimension|overlap|"
    r"chunk|\$|RPS|per month|per hour)",
    re.I,
)
TRAP_RE = re.compile(
    r"\b(trap|distractor|wrong answer|common mistake|do not |don't |never )\b",
    re.I,
)
SCEN_RE = re.compile(
    r"\b(company|startup|hospital|retailer|a bank|a team must|worked (case|example|scenario))\b",
    re.I,
)

VOLUMES = [
    ("index.html", "Home"),
    ("prereq-aif-c01.html", "AIF-C01"),
    ("prereq-aws-cloud-foundations.html", "Cloud foundations"),
    ("prereq-ml-specialty.html", "ML Specialty"),
    ("volume-d1-foundation-models.html", "D1 · 31%"),
    ("volume-d2-implementation-integration.html", "D2 · 26%"),
    ("volume-d3-safety-security-governance.html", "D3 · 20%"),
    ("volume-d4-optimization.html", "D4 · 12%"),
    ("volume-d5-testing-validation.html", "D5 · 11%"),
    ("volume-maarek-labs.html", "Labs"),
    ("volume-question-bank.html", "Question bank"),
    ("volume-question-patterns.html", "Patterns"),
    ("volume-crash-course.html", "Crash course"),
    ("volume-system-design.html", "System design"),
    ("volume-appendix-gaps.html", "Appendix"),
]


def xesc(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def wrap_lines(text: str, width: int = 86, limit: int = 3) -> list[str]:
    words = text.split()
    lines: list[str] = []
    cur = ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if len(trial) > width and cur:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines[:limit]


def flow_svg(title: str, steps: list[tuple[str, str]], note: str) -> str:
    cols = 3 if len(steps) > 3 else max(1, len(steps))
    box_w = (900 - (cols - 1) * 18) / cols
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" role="img" '
        f'aria-label="{xesc(title)}">',
        "<rect width='960' height='540' fill='#100e0c'/>",
        "<style>text{font-family:ui-sans-serif,system-ui,sans-serif}</style>",
        f"<text x='32' y='42' fill='#e7a322' font-size='14' letter-spacing='2'>{xesc(title.upper())}</text>",
    ]
    for i, (head, sub) in enumerate(steps):
        col = i % cols
        row = i // cols
        x = 30 + col * (box_w + 18)
        y = 70 + row * 150
        parts.append(
            f"<rect x='{x:.1f}' y='{y:.1f}' width='{box_w:.1f}' height='124' rx='12' "
            "fill='#181512' stroke='#e7a322' stroke-width='1.4'/>"
        )
        parts.append(
            f"<text x='{x + 16:.1f}' y='{y + 32:.1f}' fill='#e7a322' font-size='13'>{i + 1}</text>"
        )
        parts.append(
            f"<text x='{x + 36:.1f}' y='{y + 32:.1f}' fill='#f4efe6' font-size='16'>{xesc(head)}</text>"
        )
        sub_y = y + 58
        for line in wrap_lines(sub, width=28 if cols == 3 else 40, limit=3):
            parts.append(
                f"<text x='{x + 16:.1f}' y='{sub_y:.1f}' fill='#b7aa98' font-size='13'>{xesc(line)}</text>"
            )
            sub_y += 18
        if col < cols - 1 and i + 1 < len(steps) and (i + 1) // cols == row:
            ax = x + box_w + 2
            ay = y + 62
            parts.append(
                f"<path d='M {ax:.1f} {ay:.1f} h 14' stroke='#e7a322' stroke-width='1.6' "
                "marker-end='url(#arrow)'/>"
            )
    parts.append(
        "<defs><marker id='arrow' viewBox='0 0 10 10' refX='8' refY='5' markerWidth='7' "
        "markerHeight='7' orient='auto-start-reverse'><path d='M0 1 L9 5 L0 9 z' fill='#e7a322'/></marker></defs>"
    )
    note_y = 470
    for line in wrap_lines(note, width=90, limit=3):
        parts.append(f"<text x='32' y='{note_y}' fill='#d9cbb8' font-size='14'>{xesc(line)}</text>")
        note_y += 20
    parts.append("</svg>")
    return "\n".join(parts)


def doll_svg() -> str:
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" role="img" aria-label="Five nested layers of a topic: claim, mechanism, numbers, scenario, exam trap.">
<rect width="960" height="540" fill="#100e0c"/>
<style>text{font-family:ui-sans-serif,system-ui,sans-serif}</style>
<text x="32" y="42" fill="#e7a322" font-size="14" letter-spacing="2">HOW TO READ A TOPIC</text>
<rect x="70" y="70" width="820" height="390" rx="18" fill="none" stroke="#6a5738" stroke-width="2"/>
<rect x="120" y="110" width="720" height="310" rx="16" fill="none" stroke="#8d7352" stroke-width="2"/>
<rect x="180" y="155" width="600" height="230" rx="14" fill="none" stroke="#c9842a" stroke-width="2"/>
<rect x="250" y="200" width="460" height="150" rx="12" fill="none" stroke="#e7a322" stroke-width="2"/>
<rect x="330" y="240" width="300" height="80" rx="10" fill="#1c1411" stroke="#e08b72" stroke-width="2"/>
<text x="88" y="98" fill="#b7aa98" font-size="14">1 Claim — what it is and why it exists</text>
<text x="138" y="140" fill="#b7aa98" font-size="14">2 Mechanism — how it actually works</text>
<text x="198" y="186" fill="#b7aa98" font-size="14">3 Numbers — limits, counts, and what is volatile</text>
<text x="268" y="228" fill="#f4efe6" font-size="14">4 Worked scenario</text>
<text x="368" y="286" fill="#e08b72" font-size="16">5 Exam trap</text>
<text x="32" y="500" fill="#d9cbb8" font-size="14">Outer shell first. The credited answer is the mechanism that satisfies every constraint in the stem.</text>
</svg>
"""


def vector_svg() -> str:
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" role="img" aria-label="A query vector lands nearer one cluster of document vectors than another.">
<rect width="960" height="540" fill="#100e0c"/>
<style>text{font-family:ui-sans-serif,system-ui,sans-serif}</style>
<text x="32" y="42" fill="#e7a322" font-size="14" letter-spacing="2">EMBEDDINGS</text>
<circle cx="250" cy="230" r="8" fill="#e7a322"/><circle cx="280" cy="260" r="7" fill="#e7a322"/>
<circle cx="230" cy="270" r="6" fill="#e7a322"/><circle cx="300" cy="220" r="7" fill="#e7a322"/>
<circle cx="620" cy="300" r="8" fill="#8d7352"/><circle cx="660" cy="270" r="7" fill="#8d7352"/>
<circle cx="690" cy="320" r="6" fill="#8d7352"/><circle cx="640" cy="340" r="7" fill="#8d7352"/>
<circle cx="400" cy="200" r="11" fill="none" stroke="#f4efe6" stroke-width="2"/>
<line x1="400" y1="200" x2="270" y2="245" stroke="#e7a322" stroke-width="1.5"/>
<line x1="400" y1="200" x2="650" y2="300" stroke="#6a5738" stroke-width="1.5" stroke-dasharray="4 4"/>
<text x="150" y="360" fill="#e7a322" font-size="15">Near cluster — retrieved</text>
<text x="560" y="400" fill="#b7aa98" font-size="15">Far cluster — not retrieved</text>
<text x="360" y="170" fill="#f4efe6" font-size="14">query</text>
<text x="32" y="470" fill="#d9cbb8" font-size="14">Same embedding model for documents and queries. A new model means a full re-embed.</text>
<text x="32" y="494" fill="#d9cbb8" font-size="14">Cosine similarity is an angle, not a keyword match. Codes and names still need lexical search.</text>
</svg>
"""


def token_svg() -> str:
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" role="img" aria-label="Low temperature peaks on one token. High temperature flattens the distribution.">
<rect width="960" height="540" fill="#100e0c"/>
<style>text{font-family:ui-sans-serif,system-ui,sans-serif}</style>
<text x="32" y="42" fill="#e7a322" font-size="14" letter-spacing="2">NEXT-TOKEN SAMPLING</text>
<polyline fill="none" stroke="#e7a322" stroke-width="2.5" points="80,360 160,340 220,300 260,120 300,300 360,345 520,360"/>
<polyline fill="none" stroke="#b7aa98" stroke-width="2.5" points="80,300 160,280 240,250 320,230 400,220 480,230 560,260 640,290"/>
<text x="560" y="150" fill="#e7a322" font-size="15">Low temperature — sharp, repeatable</text>
<text x="660" y="230" fill="#b7aa98" font-size="15">High temperature — flatter</text>
<text x="32" y="430" fill="#d9cbb8" font-size="14">Temperature reshapes probabilities. It does not add facts.</text>
<text x="32" y="456" fill="#d9cbb8" font-size="14">Top-p and top-k then cut the tail. max tokens caps length. Tokens are the billing unit, not words.</text>
<text x="32" y="490" fill="#b7aa98" font-size="13">Curves are a teaching sketch, not a measured distribution from a model card.</text>
</svg>
"""


PLATES: dict[str, dict] = {
    "doll.svg": {
        "alt": "Five nested layers: claim, mechanism, numbers, worked scenario, and exam trap.",
        "caption": "Read every major topic from the outside in. The outer sentence is the claim. The core is the mistake the exam expects you to make.",
        "credit": "Original diagram for this treatise.",
        "steps": [
            "Name what the thing is and why AWS shipped it.",
            "Follow the mechanism one hop at a time.",
            "Separate stable ideas from quotas and prices.",
            "Run one scenario with every constraint visible.",
            "State the trap before you look at the options.",
        ],
        "svg": doll_svg(),
        "needles": [],
    },
    "domain-weights.svg": {
        "alt": "AIP-C01 domain weights: 31, 26, 20, 12, and 11 percent.",
        "caption": "Official scored weights from the AIP-C01 exam guide. Study time follows the bars. You pass the whole exam at 750, not each domain.",
        "credit": "Weights from the AWS Certified Generative AI Developer - Professional exam guide (AIP-C01), fetched 2026-10-20. Drawing is original.",
        "steps": [
            "Domain 1 is 31 percent: model, data, and compliance choices.",
            "Domain 2 is 26 percent: agents, APIs, and integration.",
            "Domain 3 is 20 percent: safety, security, and governance.",
            "Domain 4 is 12 percent: cost, latency, and operations.",
            "Domain 5 is 11 percent: evaluation and troubleshooting.",
        ],
        "svg": flow_svg(
            "Scored weight",
            [
                ("D1 31%", "Models, data, compliance"),
                ("D2 26%", "Implement and integrate"),
                ("D3 20%", "Safety and governance"),
                ("D4 12%", "Cost and latency"),
                ("D5 11%", "Test and troubleshoot"),
            ],
            "75 questions, 65 scored, 10 unscored. 180 minutes. Pass 750 of 1000. No penalty for guessing.",
        ),
        "needles": ["blueprint", "exam weight", "domain weight", "what this exam"],
    },
    "rag-path.svg": {
        "alt": "RAG path: documents are chunked, embedded, stored, retrieved, and cited by the model.",
        "caption": "Retrieval-augmented generation keeps facts outside the weights. The model answers from chunks it can cite.",
        "credit": "Original diagram. The flow follows Amazon Bedrock Knowledge Bases: ingest, chunk, embed, retrieve, generate.",
        "steps": [
            "Ingestion loads documents from a source such as S3.",
            "Chunking splits them. The strategy is fixed on the data source.",
            "One embedding model writes vectors into a store.",
            "A query embeds with the same model and fetches near chunks.",
            "The model answers from those chunks and returns citations.",
        ],
        "svg": flow_svg(
            "RAG",
            [
                ("Ingest", "Source documents, then sync"),
                ("Chunk", "Fixed, hierarchical, or semantic"),
                ("Embed", "One model, one vector space"),
                ("Retrieve", "Near chunks, optional rerank"),
                ("Cite", "Answer grounded in sources"),
            ],
            "Changing the chunker or the embedding model means a new data source and a full re-index.",
        ),
        "needles": ["knowledge base", "rag", "chunk", "retrieveandgenerate"],
    },
    "approach-ladder.svg": {
        "alt": "Approach ladder from prompt engineering to RAG to agents to fine-tuning.",
        "caption": "Climb only when the cheaper step cannot meet the constraint. Facts that change belong in retrieval. Behavior belongs in weights.",
        "credit": "Original diagram of the decision order used throughout this guide.",
        "steps": [
            "Prompt work changes format, tone, and examples. It adds no new facts.",
            "RAG brings private or current facts and can cite them.",
            "Agents take actions through tools. Text alone is not enough.",
            "Fine-tuning bakes behavior into weights. It does not stay current.",
            "Stop at the first rung that meets every constraint.",
        ],
        "svg": flow_svg(
            "Approach ladder",
            [
                ("Prompt", "Format, tone, few-shot"),
                ("RAG", "Facts and citations"),
                ("Agents", "Tools and actions"),
                ("Fine-tune", "Behavior in weights"),
            ],
            "The exam credits the lowest rung that works. A heavier design without a forcing constraint is the trap.",
        ),
        "needles": ["fine-tun", "ladder", "prompt", "poc", "distill", "custom model"],
    },
    "api-choice.svg": {
        "alt": "Choose InvokeModel for provider-specific bodies and embeddings. Choose Converse for one message format across models.",
        "caption": "Converse is the unified messages API. InvokeModel remains the provider-specific body, and it is the path embeddings use in this guide.",
        "credit": "Original diagram. Converse and Invoke are documented on the Amazon Bedrock overview (fetched 2026-10-20), which also lists Messages, Responses, and Chat Completions.",
        "steps": [
            "Need embeddings or a provider-only body? Use InvokeModel.",
            "Otherwise call Converse so the message shape stays stable.",
            "A person waiting on a chat UI wants the streaming variant.",
            "A job that can wait and land in S3 wants batch.",
            "The overview also documents Messages, Responses, and Chat Completions. The stem names the interface.",
        ],
        "svg": flow_svg(
            "Which call",
            [
                ("InvokeModel", "Provider body, embeddings"),
                ("Converse", "One shape, tools, guardrails"),
                ("Stream", "User is waiting"),
                ("Batch", "S3 in, hours later"),
            ],
            "As of 2026-10-20 the Bedrock overview also documents Messages, Responses, and Chat Completions on bedrock-runtime.",
        ),
        "needles": ["converse", "invokemodel", "invoke model"],
    },
    "agent-loop.svg": {
        "alt": "An agent loop: the model plans, calls a tool, observes the result, and repeats.",
        "caption": "An agent is a loop, not a prompt. Tools do the work. The model decides the next call.",
        "credit": "Original diagram of the Bedrock Agents orchestration loop: plan, act through an action group, observe, repeat.",
        "steps": [
            "The user goal enters the agent with its instructions.",
            "The model picks a tool described by the action group schema.",
            "Lambda, or another target, runs the action and returns data.",
            "The model observes that result and either calls again or answers.",
            "A guardrail can sit on the input and the final output.",
        ],
        "svg": flow_svg(
            "Agent loop",
            [
                ("Goal", "Instructions plus user turn"),
                ("Plan", "Which tool, which arguments"),
                ("Act", "Action group runs"),
                ("Observe", "Tool result returns"),
                ("Stop", "Answer, or ask a human"),
            ],
            "Sensitive actions need an approval break. A trace is how you debug a bad tool choice.",
        ),
        "needles": ["agent", "action group", "multi-agent", "strands", "tool use"],
    },
    "guardrail-stack.svg": {
        "alt": "Six Bedrock Guardrails safeguards between the user and the model.",
        "caption": "A guardrail is one configuration with several filters. It can run on the model call or alone through ApplyGuardrail.",
        "credit": "Filter names from the Amazon Bedrock Guardrails page, fetched 2026-10-20. Drawing is original, not an AWS asset.",
        "steps": [
            "Content filters cover hate, insults, sexual, violence, misconduct, and prompt attack.",
            "Denied topics block subjects you define. Word filters block phrases and profanity.",
            "Sensitive information filters block or mask PII and custom regex matches.",
            "Contextual grounding checks hallucinations against the source and the question.",
            "Automated Reasoning checks the answer against logical rules.",
        ],
        "svg": flow_svg(
            "Guardrail filters",
            [
                ("Content", "Harm categories and prompt attack"),
                ("Topics", "Denied subjects you name"),
                ("Words", "Phrases and profanity"),
                ("Sensitive", "PII and custom regex"),
                ("Grounding", "Source and relevance"),
                ("Reasoning", "Rules and assumptions"),
            ],
            "The Guardrails page excludes reasoning content blocks from these filters. Confirm the current page before exam day.",
        ),
        "needles": [
            "guardrail",
            "content filter",
            "denied topic",
            "word filter",
            "pii",
            "sensitive information",
            "automated reasoning",
            "prompt attack",
            "jailbreak",
            "responsible",
        ],
    },
    "security-plane.svg": {
        "alt": "Security plane around a model call: IAM, KMS, a VPC endpoint, and separate audit logs.",
        "caption": "Identity, encryption, network path, and audit are different controls. One of them does not replace the others.",
        "credit": "Original diagram. Service roles follow the AIP-C01 exam guide in-scope list: IAM, KMS, Amazon VPC, AWS PrivateLink, CloudTrail, CloudWatch.",
        "steps": [
            "IAM decides who may call the API. A guardrail does not.",
            "KMS encrypts data at rest where the service supports a customer key.",
            "A VPC endpoint keeps the call off the public internet.",
            "CloudTrail records who called which API.",
            "Invocation logs and CloudWatch hold the prompt content and the block metrics.",
        ],
        "svg": flow_svg(
            "Security plane",
            [
                ("IAM", "Who may call"),
                ("KMS", "Keys at rest"),
                ("VPC endpoint", "Private network path"),
                ("CloudTrail", "Who called which API"),
                ("Invocation log", "Prompt text and blocks"),
            ],
            "CloudTrail does not store the guardrail's block reason. That lives with invocation logging and metrics.",
        ),
        "needles": ["iam", "kms", "vpc", "privatelink", "cloudtrail", "macie", "secrets manager", "waf", "encrypt"],
    },
    "vector-space.svg": {
        "alt": "Query and document vectors in one space. The nearer cluster is what retrieval returns.",
        "caption": "An embedding is a list of numbers. Near means similar in that model's space, and only in that model's space.",
        "credit": "Original teaching sketch. Store choices in this guide include OpenSearch, Aurora pgvector, and the managed Knowledge Bases store.",
        "steps": [
            "Embed documents and queries with the same model.",
            "A dimension change or a model swap invalidates stored vectors.",
            "Dense search finds similar meaning. Lexical search finds exact tokens.",
            "Hybrid search uses both when the corpus has codes and names.",
            "A vector store is not a cache and not a graph.",
        ],
        "svg": vector_svg(),
        "needles": ["embed", "vector", "pgvector", "opensearch", "similarity", "titan text"],
    },
    "token-sample.svg": {
        "alt": "Low temperature concentrates probability on one token. High temperature flattens it.",
        "caption": "Sampling controls change how the next token is chosen. They do not retrieve facts.",
        "credit": "Original sketch. The curves are illustrative, not a measured model distribution.",
        "steps": [
            "A token is a chunk of text, not a word, and it is the billing unit.",
            "Temperature 0 is the repeatable choice for extraction and classification.",
            "Higher temperature flattens the distribution.",
            "Top-p and top-k trim the candidate set after that.",
            "The context window is the combined budget the model can see.",
        ],
        "svg": token_svg(),
        "needles": ["temperature", "top-p", "top_p", "tokenization", "context window"],
    },
    "sync-async.svg": {
        "alt": "Synchronous streaming for a waiting user, asynchronous batch for work that can land in S3.",
        "caption": "Who is waiting picks the invocation pattern. A chat user needs tokens early. A nightly corpus can wait.",
        "credit": "Original diagram of the sync, streaming, and batch split used in the implementation volume.",
        "steps": [
            "A user in a chat UI is waiting. Stream tokens.",
            "API Gateway and Lambda have their own timeouts. A long call can die there first.",
            "Work with no waiter goes async: queue it, or use batch inference to S3.",
            "Retries need backoff. A tight retry loop burns the quota.",
            "Do not put a human approval inside an Express workflow that cannot wait.",
        ],
        "svg": flow_svg(
            "Who is waiting",
            [
                ("Stream", "A person is watching"),
                ("Sync call", "Short enough for the timeout"),
                ("Queue", "Decouple the slow step"),
                ("Batch", "S3 in, results later"),
            ],
            "Batch price relative to on-demand is a pricing-page number. Treat any discount you remember as volatile.",
        ),
        "needles": ["streaming", "batch", "latency", "async", "timeout", "throttl"],
    },
    "cost-controls.svg": {
        "alt": "Cost controls in order: smaller prompts, caching, a smaller model, batch, then provisioned capacity.",
        "caption": "Spend follows tokens and the capacity you reserve. Cut tokens before you buy throughput.",
        "credit": "Original diagram. Prices and provisioned-throughput terms change. Confirm them on the official pricing and quotas pages.",
        "steps": [
            "Shorten the prompt and the retrieved context first.",
            "Cache a repeated prefix when the provider supports prompt caching.",
            "Route easy turns to a cheaper model. Escalate the hard ones.",
            "Batch the work that nobody is waiting on.",
            "Buy provisioned throughput only for a proven steady load, and call the provisioned ARN.",
        ],
        "svg": flow_svg(
            "Cost controls",
            [
                ("Fewer tokens", "Prompt and chunks"),
                ("Cache", "Repeated prefix"),
                ("Smaller model", "Cascade the hard turns"),
                ("Batch", "No waiter"),
                ("Provision", "Steady base load"),
            ],
            "A provisioned model that you call with the on-demand model ID still burns on-demand quota.",
        ),
        "needles": ["provisioned", "prompt cach", "on-demand", "cost", "pric", "throughput", "token efficien"],
    },
    "eval-loop.svg": {
        "alt": "Evaluation loop: a fixed dataset, a metric or a judge, a change, then the same dataset again.",
        "caption": "A score without a fixed dataset cannot be compared to the next score.",
        "credit": "Original diagram of the evaluation loop in Domain 5.",
        "steps": [
            "Freeze a golden dataset before you change the prompt or the model.",
            "Automatic metrics cover tasks with a checkable output.",
            "LLM-as-a-judge covers open answers, and the judge is also a model.",
            "Human review covers what the automatic job cannot see.",
            "Ship the change only if the same dataset does not regress.",
        ],
        "svg": flow_svg(
            "Eval loop",
            [
                ("Dataset", "Frozen questions and answers"),
                ("Measure", "Metric, judge, or human"),
                ("Change", "Prompt, model, or chunks"),
                ("Gate", "Same set, no regression"),
            ],
            "RAG failures are usually retrieval failures. Score retrieval before you blame the answer model.",
        ),
        "needles": ["evaluat", "llm-as-a-judge", "metric", "a/b", "golden", "red team"],
    },
    "integration-bus.svg": {
        "alt": "A request path from API Gateway through Lambda to Bedrock, with EventBridge and a queue for work that can wait.",
        "caption": "The managed front door, the function, and the model call are three different timeouts and three different IAM roles.",
        "credit": "Original diagram. In-scope integration services in the exam guide include API Gateway, Lambda, Step Functions, EventBridge, SQS, and SNS.",
        "steps": [
            "API Gateway is the front door. It authenticates and throttles.",
            "Lambda calls Bedrock. Its timeout must exceed the model call you expect.",
            "Step Functions owns multi-step workflows and human approval waits.",
            "S3 events and EventBridge start work when an object arrives.",
            "SQS absorbs bursts so a throttle does not become a dropped job.",
        ],
        "svg": flow_svg(
            "Integration path",
            [
                ("API Gateway", "Front door and auth"),
                ("Lambda", "Call Bedrock"),
                ("Bedrock", "Model, agent, or KB"),
                ("EventBridge", "Start from an event"),
                ("Queue", "Burst and retry"),
            ],
            "Express Step Functions are the short workflow. A human pause needs a Standard state machine.",
        ),
        "needles": ["lambda", "api gateway", "step function", "eventbridge", "sqs", "sns"],
    },
    "retrieval-debug.svg": {
        "alt": "Retrieval debug order: test retrieval alone, then chunks, then the embedding model, then the prompt.",
        "caption": "Most bad answers are bad retrieval. Name the phase before you change the model.",
        "credit": "Original diagram of the debug order taught in the retrieval chapter.",
        "steps": [
            "Run Retrieve with a known question. Look at the chunks, not the prose.",
            "If the right passage is missing, fix chunking or the sync.",
            "If passages are present but irrelevant, try hybrid search or a reranker.",
            "If the right passage is in the prompt and the answer is still wrong, fix the prompt.",
            "A model swap does not repair a split chunk.",
        ],
        "svg": flow_svg(
            "Debug retrieval",
            [
                ("Retrieve only", "Known questions"),
                ("Read chunks", "Is the fact in there?"),
                ("Hybrid or rerank", "Codes, names, near misses"),
                ("Prompt last", "Only after retrieval works"),
            ],
            "Ingestion faults and query faults have different fixes. Say which phase failed.",
        ),
        "needles": ["hybrid", "rerank", "retrieval quality"],
    },
}


def write_plates() -> None:
    PLATE_DIR.mkdir(parents=True, exist_ok=True)
    for name, spec in PLATES.items():
        (PLATE_DIR / name).write_text(spec["svg"], encoding="utf-8")


def text_of(node: Tag) -> str:
    return re.sub(r"\s+", " ", node.get_text(" ", strip=True)).strip()


def safe_href(href: str) -> bool:
    lowered = href.strip().lower()
    if lowered.startswith(("javascript:", "data:")):
        return False
    return True


def render_inline(el: Tag) -> str:
    parts: list[str] = []
    for child in el.children:
        if isinstance(child, NavigableString):
            parts.append(html.escape(str(child)))
        elif isinstance(child, Tag):
            if child.name in {"ul", "ol"}:
                parts.append(render_list(child))
            elif child.name == "br":
                parts.append("<br>")
            elif child.name in {"strong", "em", "b", "i", "code"}:
                parts.append(f"<{child.name}>{render_inline(child)}</{child.name}>")
            elif child.name == "a":
                href = child.get("href") or ""
                if href and safe_href(href):
                    parts.append(
                        f'<a href="{html.escape(href, quote=True)}">{render_inline(child)}</a>'
                    )
                else:
                    parts.append(render_inline(child))
            else:
                parts.append(render_inline(child))
    return re.sub(r"\s+", " ", "".join(parts)).strip()


def render_list(el: Tag) -> str:
    tag = "ol" if el.name == "ol" else "ul"
    items = []
    for li in el.find_all("li", recursive=False):
        items.append(f"<li>{render_inline(li)}</li>")
    if not items:
        return ""
    return f"<{tag}>{''.join(items)}</{tag}>"


def render_table(table: Tag) -> str:
    rows = []
    for tr in table.find_all("tr"):
        cells = []
        for cell in tr.find_all(["th", "td"], recursive=False):
            cells.append(f"<{cell.name}>{render_inline(cell)}</{cell.name}>")
        if cells:
            rows.append("<tr>" + "".join(cells) + "</tr>")
    if not rows:
        return ""
    return '<div class="table-wrap"><table>' + "".join(rows) + "</table></div>"


def has_block_child(el: Tag) -> bool:
    block = {
        "p", "ul", "ol", "table", "pre", "figure", "h1", "h2", "h3", "h4",
        "div", "section", "article", "aside", "details", "blockquote", "header",
    }
    return any(isinstance(child, Tag) and child.name in block for child in el.children)


class Builder:
    def __init__(self, path: Path):
        self.path = path
        self.kind = "companion" if "companions" in path.parts else "volume"
        self.asset = "../assets" if self.kind == "companion" else "assets"
        self.h1 = ""
        self.sections: list[dict] = []
        self.current: dict | None = None
        self.used_ids: set[str] = set()
        self.source_h2 = 0
        self.source_pq = 0

    def add_block(self, block: dict) -> None:
        if self.current is None:
            self.current = {
                "id": self.unique("opening"),
                "title": "Start here",
                "blocks": [],
            }
            self.sections.append(self.current)
        self.current["blocks"].append(block)

    def unique(self, raw: str) -> str:
        base = re.sub(r"[^a-z0-9]+", "-", raw.lower()).strip("-")[:80] or "section"
        candidate = base
        n = 2
        while candidate in self.used_ids:
            candidate = f"{base}-{n}"
            n += 1
        self.used_ids.add(candidate)
        return candidate

    def start_section(self, heading: Tag) -> None:
        self.source_h2 += 1
        title = text_of(heading) or "Section"
        raw_id = heading.get("id") or title
        self.current = {"id": self.unique(raw_id), "title": title, "blocks": []}
        self.sections.append(self.current)

    def add_svg(self, svg: Tag) -> None:
        for script in svg.find_all("script"):
            script.decompose()
        raw = str(svg)
        if len(raw) > 50000 or "<script" in raw.lower():
            return
        self.add_block({
            "type": "svg",
            "html": raw,
            "alt": svg.get("aria-label") or "Chart",
        })

    def parse_img(self, image: Tag) -> None:
        src = (image.get("src") or "").split("?")[0]
        if not src or src.startswith(("http://", "https://", "data:")):
            return
        if "/internet/" in src.replace("\\", "/"):
            return
        full = (self.path.parent / src).resolve()
        try:
            full.relative_to(ROOT.resolve())
        except ValueError:
            return
        if not full.is_file():
            return
        alt = image.get("alt") or "Diagram"
        self.add_block({
            "type": "figure",
            "src": src,
            "alt": alt,
            "caption": alt,
            "credit": "Local figure from this guide.",
            "light": self.light_svg(full),
            "width": self.svg_width(full),
            "height": self.svg_height(full),
        })

    def parse_figure(self, figure: Tag) -> None:
        if figure.find("h2") is not None:
            self.walk(figure)
            return
        svg = figure.find("svg")
        image = figure.find("img")
        if image is None:
            if svg is not None:
                self.add_svg(svg)
            return
        src = (image.get("src") or "").split("?")[0]
        if not src or src.startswith(("http://", "https://", "data:")):
            return
        if "/internet/" in src.replace("\\", "/"):
            return
        full = (self.path.parent / src).resolve()
        try:
            full.relative_to(ROOT.resolve())
        except ValueError:
            return
        if not full.is_file():
            return
        captions = []
        for cap in figure.find_all("figcaption"):
            line = text_of(cap)
            if line and line not in captions:
                captions.append(line)
        alt = image.get("alt") or (captions[0] if captions else "Diagram")
        credit = ""
        teaching = []
        for line in captions:
            if line.lower().startswith("source:") or "original figure" in line.lower() or line.lower().startswith("watercolor"):
                credit = line
            else:
                teaching.append(line)
        classes = figure.get("class") or []
        light = "fig-light" in classes or self.light_svg(full)
        self.add_block({
            "type": "figure",
            "src": src,
            "alt": alt,
            "caption": " ".join(teaching)[:700],
            "credit": credit,
            "light": light,
            "width": self.svg_width(full),
            "height": self.svg_height(full),
        })

    def light_svg(self, path: Path) -> bool:
        if path.suffix.lower() != ".svg":
            return False
        head = path.read_text(encoding="utf-8", errors="ignore")[:2000].lower()
        return 'fill="#ffffff"' in head or "fill:#ffffff" in head or 'fill="#fff"' in head

    def svg_box(self, path: Path) -> tuple[int | None, int | None]:
        if path.suffix.lower() != ".svg":
            return None, None
        head = path.read_text(encoding="utf-8", errors="ignore")[:900]
        match = re.search(r'viewBox="([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)"', head)
        if not match:
            return None, None
        return int(float(match.group(3))), int(float(match.group(4)))

    def svg_width(self, path: Path) -> int | None:
        return self.svg_box(path)[0]

    def svg_height(self, path: Path) -> int | None:
        return self.svg_box(path)[1]

    def parse_pq(self, node: Tag) -> None:
        self.source_pq += 1
        question = node.select_one(".pq-question")
        answer = node.select_one(".pq-answer")
        options = []
        for li in node.select(".pq-option"):
            note = li.select_one(".pq-note")
            note_html = render_inline(note) if note else ""
            if note:
                note.extract()
            classes = li.get("class") or []
            options.append({
                "correct": "correct" in classes,
                "html": render_inline(li),
                "note": note_html,
            })
        answer_html = ""
        answer_id = ""
        if answer is not None:
            answer_id = answer.get("id") or ""
            bits = []
            for child in answer.find_all("p"):
                bits.append(f"<p>{render_inline(child)}</p>")
            answer_html = "".join(bits) or f"<p>{html.escape(text_of(answer))}</p>"
        self.add_block({
            "type": "pq",
            "id": node.get("id") or "",
            "question": render_inline(question) if question else html.escape(text_of(node)[:500]),
            "options": options,
            "answer": answer_html,
            "answer_id": answer_id,
        })

    def parse_card(self, anchor: Tag) -> None:
        title_el = anchor.find(["h3", "h2", "h4"])
        kicker_el = anchor.select_one(".w")
        paragraphs = [text_of(p) for p in anchor.find_all("p") if text_of(p)]
        self.add_block({
            "type": "card",
            "href": anchor.get("href") or "",
            "title": text_of(title_el) if title_el else text_of(anchor)[:120],
            "kicker": text_of(kicker_el) if kicker_el else "",
            "body": " ".join(paragraphs),
        })

    def walk(self, node: Tag) -> None:
        for child in list(node.children):
            if not isinstance(child, Tag):
                continue
            if child.name in {"script", "style", "footer", "button"}:
                continue
            if child.get("id") in {"playbook", "tip", "tape", "ds-sidebar-root"}:
                continue
            classes = set(child.get("class") or [])
            if classes & {"colophon", "playbook", "tapebar"}:
                continue
            if child.name == "h1" and not self.h1:
                self.h1 = text_of(child)
                continue
            if child.name == "h2":
                self.start_section(child)
                continue
            if child.name in {"h3", "h4"}:
                title = text_of(child)
                if title:
                    self.add_block({"type": "subhead", "text": title})
                continue
            # Broken markup sometimes nests the rest of the page inside one figure or div.
            if child.name not in {"h1", "h2", "h3", "h4"} and child.find("h2") is not None:
                self.walk(child)
                continue
            if child.name == "img":
                self.parse_img(child)
                continue
            if child.name == "svg":
                self.add_svg(child)
                continue
            if child.name == "figcaption":
                line = text_of(child)
                lowered = line.lower()
                if line and not lowered.startswith("source") and "original figure" not in lowered and len(line) > 30:
                    self.add_block({"type": "p", "html": html.escape(line), "text": line, "key": False})
                continue
            if "vol" in classes and child.name == "a":
                self.parse_card(child)
                continue
            if "pq" in classes:
                self.parse_pq(child)
                continue
            if child.name == "p":
                rendered = render_inline(child)
                plain = text_of(child)
                if len(plain) < 2:
                    continue
                self.add_block({
                    "type": "p",
                    "html": rendered,
                    "text": plain,
                    "key": (child.get("data-kind") == "keyIdea"),
                })
                continue
            if child.name in {"ul", "ol"}:
                rendered = render_list(child)
                if rendered:
                    self.add_block({"type": "list", "html": rendered, "text": text_of(child)})
                continue
            if child.name == "table":
                rendered = render_table(child)
                if rendered:
                    self.add_block({"type": "table", "html": rendered, "text": text_of(child)})
                continue
            if child.name == "pre":
                self.add_block({"type": "pre", "text": child.get_text(), "html": ""})
                continue
            if child.name == "figure":
                self.parse_figure(child)
                continue
            if child.name == "details":
                summary = child.find("summary")
                body_parts = []
                for bit in child.children:
                    if isinstance(bit, Tag) and bit.name == "summary":
                        continue
                    if isinstance(bit, Tag) and bit.name == "table":
                        body_parts.append(render_table(bit))
                    elif isinstance(bit, Tag) and bit.name in {"ul", "ol"}:
                        body_parts.append(render_list(bit))
                    elif isinstance(bit, Tag) and bit.name == "p":
                        body_parts.append(f"<p>{render_inline(bit)}</p>")
                    elif isinstance(bit, Tag):
                        line = text_of(bit)
                        if line:
                            body_parts.append(f"<p>{html.escape(line)}</p>")
                self.add_block({
                    "type": "details",
                    "summary": text_of(summary) if summary else "Details",
                    "html": "".join(body_parts),
                })
                continue
            if "ladder" in classes:
                items = []
                for rung in child.select(".rung"):
                    line = text_of(rung)
                    if line:
                        items.append(f"<li>{html.escape(line)}</li>")
                if items:
                    self.add_block({"type": "list", "html": "<ol>" + "".join(items) + "</ol>", "text": text_of(child)})
                continue
            if child.name == "aside" and "tag" in classes:
                line = text_of(child)
                if line:
                    self.add_block({
                        "type": "p",
                        "html": html.escape(line),
                        "text": line,
                        "key": True,
                    })
                continue
            if not has_block_child(child):
                line = text_of(child)
                if len(line) > 40:
                    self.add_block({"type": "p", "html": html.escape(line), "text": line, "key": False})
                continue
            self.walk(child)

    def parse(self) -> None:
        soup = BeautifulSoup(self.path.read_text(encoding="utf-8", errors="replace"), "lxml")
        if soup.html and soup.html.get("data-treatise") == "1":
            raise SystemExit(f"{self.path} is already a treatise. Restore the source before rebuilding.")
        root = soup.select_one("main#ds-content") or soup.select_one("div.wrap") or soup.body
        if root is None:
            raise SystemExit(f"No content root in {self.path}")
        self.walk(root)
        if not self.h1 and soup.title:
            self.h1 = text_of(soup.title)


def claim_from(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"(?<=[.!?])\s+", text)
    out = parts[0] if parts else text
    index = 1
    while len(out) < 90 and index < len(parts):
        out += " " + parts[index]
        index += 1
    if len(out) > 380:
        out = out[:360].rsplit(" ", 1)[0] + "."
    return out


def classify(paragraph: dict) -> str:
    text = paragraph.get("text") or ""
    if TRAP_RE.search(text):
        return "trap"
    if SCEN_RE.search(text):
        return "scenario"
    if NUM_UNIT.search(text) and re.search(r"\d", text):
        return "numbers"
    return "mechanism"


PLATE_PRIORITY = [
    "guardrail-stack.svg",
    "agent-loop.svg",
    "rag-path.svg",
    "retrieval-debug.svg",
    "vector-space.svg",
    "api-choice.svg",
    "security-plane.svg",
    "cost-controls.svg",
    "sync-async.svg",
    "token-sample.svg",
    "eval-loop.svg",
    "integration-bus.svg",
    "approach-ladder.svg",
    "domain-weights.svg",
]


def pick_plate(section: dict) -> str:
    hay = (section["title"] + " " + " ".join(
        block.get("text", "")[:240] for block in section["blocks"][:4]
    )).lower()
    for name in PLATE_PRIORITY:
        if any(needle in hay for needle in PLATES[name]["needles"]):
            return name
    return "doll.svg"


def img_attrs(block: dict, eager: bool) -> str:
    bits = [
        f'src="{html.escape(block["src"], quote=True)}"',
        f'alt="{html.escape(block.get("alt") or "Diagram", quote=True)}"',
    ]
    if block.get("width") and block.get("height"):
        bits.append(f'width="{block["width"]}"')
        bits.append(f'height="{block["height"]}"')
    if eager:
        bits.append('fetchpriority="high"')
    else:
        bits.append('loading="lazy"')
    return " ".join(bits)


def render_steps(lines: list[str]) -> str:
    clean = [line.strip() for line in lines if line and len(line.strip()) > 8]
    if not clean:
        return ""
    items = "".join(f"<li>{html.escape(line)}</li>" for line in clean[:6])
    return f"<ol class='steps'>{items}</ol>"


def sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [part for part in parts if part][:6]


def render_page(builder: Builder) -> str:
    eager_used = False
    articles = []
    for section in builder.sections:
        blocks = list(section["blocks"])
        claim = ""
        claim_index = None
        for index, block in enumerate(blocks):
            if block["type"] == "p" and (block.get("key") or len(block["text"]) > 40):
                claim = claim_from(block["text"])
                if block.get("key") and len(block["text"]) < 420:
                    claim_index = index
                break
        if len(claim) < 40:
            for block in blocks:
                if block["type"] == "p" and len(block["text"]) > 40:
                    claim = claim_from(block["text"])
                    break
        if not claim:
            claim = f"{section['title']} is a decision you can name in one sentence before you look at the options."

        figure_indexes = [i for i, block in enumerate(blocks) if block["type"] == "figure"]
        plate_html = ""
        if figure_indexes:
            figure = blocks.pop(figure_indexes[0])
            eager = not eager_used
            eager_used = True
            light = " light" if figure.get("light") else ""
            cap = figure.get("caption") or figure.get("alt") or ""
            credit = figure.get("credit") or "Figure carried from this guide. It is a local file."
            plate_html = (
                f"<figure class='plate{light}'>"
                f"<img {img_attrs(figure, eager)}>"
                f"<figcaption>{html.escape(cap)}</figcaption>"
                f"<p class='credit'>{html.escape(credit)}</p>"
                f"{render_steps(sentences(cap))}"
                "</figure>"
            )
        else:
            name = pick_plate(section)
            spec = PLATES[name]
            eager = not eager_used
            eager_used = True
            src = f"{builder.asset}/img/treatise/{name}"
            plate_html = (
                "<figure class='plate'>"
                f"<img src='{src}' alt='{html.escape(spec['alt'], quote=True)}' width='960' height='540' "
                + ("fetchpriority='high'" if eager else "loading='lazy'")
                + ">"
                f"<figcaption>{html.escape(spec['caption'])}</figcaption>"
                f"<p class='credit'>{html.escape(spec['credit'])}</p>"
                f"{render_steps(spec['steps'])}"
                "</figure>"
            )

        def render_block(block: dict) -> str:
            if block["type"] == "p":
                return f"<p>{block['html']}</p>"
            if block["type"] == "list":
                return block["html"]
            if block["type"] == "table":
                return block["html"]
            if block["type"] == "pre":
                return "<pre><code>" + html.escape(block["text"]) + "</code></pre>"
            if block["type"] == "subhead":
                return f"<h3 class='subhead'>{html.escape(block['text'])}</h3>"
            if block["type"] == "figure":
                light = " light" if block.get("light") else ""
                cap = block.get("caption") or block.get("alt") or ""
                return (
                    f"<figure class='inline-fig{light}'><img {img_attrs(block, False)}>"
                    f"<figcaption>{html.escape(cap)}</figcaption></figure>"
                )
            if block["type"] == "svg":
                return (
                    f"<figure class='inline-fig light'><div class='svg-embed'>{block['html']}</div>"
                    f"<figcaption>{html.escape(block.get('alt') or 'Chart')}</figcaption></figure>"
                )
            if block["type"] == "card":
                return (
                    f"<a class='card' href='{html.escape(block['href'], quote=True)}'>"
                    f"<p class='card-kicker'>{html.escape(block['kicker'])}</p>"
                    f"<p class='card-title'>{html.escape(block['title'])}</p>"
                    f"<p>{html.escape(block['body'])}</p></a>"
                )
            if block["type"] == "details":
                return (
                    "<details class='fold'><summary>"
                    + html.escape(block["summary"])
                    + "</summary>"
                    + block["html"]
                    + "</details>"
                )
            if block["type"] == "pq":
                answer_id = block["answer_id"] or f"{section['id']}-answer-{block.get('id') or 'q'}"
                options = []
                for option in block["options"]:
                    klass = "correct" if option["correct"] else "wrong"
                    note = f"<span class='pq-note'>{option['note']}</span>" if option["note"] else ""
                    options.append(f"<li class='pq-option {klass}'>{option['html']}{note}</li>")
                return (
                    f"<article class='pq' id='{html.escape(block['id'], quote=True)}'>"
                    f"<p class='pq-question'>{block['question']}</p>"
                    f"<ul class='pq-options'>{''.join(options)}</ul>"
                    "<button class='pq-reveal' type='button'>Reveal answer</button>"
                    f"<div class='pq-answer' id='{html.escape(answer_id, quote=True)}'>{block['answer']}</div>"
                    "</article>"
                )
            return ""

        def excerpts(kind: str, limit: int = 3) -> list[str]:
            found: list[str] = []
            for block in blocks:
                if block["type"] != "p" or classify(block) != kind:
                    continue
                sentence = claim_from(block["text"])
                if sentence not in found:
                    found.append(sentence)
                if len(found) >= limit:
                    break
            return found

        has_drills = any(block["type"] == "pq" for block in blocks)
        number_lines = excerpts("numbers")
        scenario_lines = excerpts("scenario")
        trap_lines = excerpts("trap")
        if not scenario_lines:
            if has_drills:
                scenario_lines = [
                    "Each question in this section is the worked scenario. Read the last sentence of the stem first. That sentence is the constraint."
                ]
            else:
                scenario_lines = [
                    f"Work “{section['title']}” against one stem. Name the constraint (freshness, citation, latency, a cost ceiling, or a control that must block) and pick the smallest managed mechanism that meets every constraint."
                ]
        if not trap_lines:
            trap_lines = [
                "Exam trap: a real service used for the wrong job, or a heavier ladder rung than the stem requires. Match the verb in the stem — cite, act, block, cheapen, or measure — to one mechanism here."
            ]
        number_html = "<p><span class='volatile'>Volatile.</span> Quotas, model IDs, and prices move. The prose below was checked against AWS documentation on 2026-09-28. Re-check any quota or price before exam day.</p>"
        if number_lines:
            number_html += "".join(f"<p>{html.escape(line)}</p>" for line in number_lines)
        else:
            number_html += "<p>This section states no service quota. Do not memorize a number the text does not give you.</p>"
        mechanism_body = "".join(render_block(block) for block in blocks)
        if not mechanism_body.strip():
            mechanism_body = "<p>Follow the numbered steps in the figure. Each step is one hop in the mechanism.</p>"

        articles.append(
            "<article class='topic'>"
            "<header class='topic-head'>"
            "<p class='peel-label'><span>Outer layer</span> Claim</p>"
            f"<h2 id='{html.escape(section['id'], quote=True)}'>{html.escape(section['title'])}</h2>"
            f"<p class='claim'>{html.escape(claim)}</p>"
            "</header>"
            + plate_html
            + "<div class='doll'>"
            + f"<section class='peel mechanism'><h3>Mechanism</h3>{mechanism_body}</section>"
            + f"<section class='peel numbers'><h3>Numbers and limits</h3>{number_html}</section>"
            + "<section class='peel scenario'><h3>Worked scenario</h3>"
            + "".join(f"<p>{html.escape(line)}</p>" for line in scenario_lines)
            + "</section>"
            + "<section class='peel trap'><h3>Exam trap</h3>"
            + "".join(f"<p>{html.escape(line)}</p>" for line in trap_lines)
            + "</section>"
            + "</div></article>"
        )

    lead = []
    if builder.sections:
        for block in builder.sections[0]["blocks"]:
            if block["type"] == "p" and len(block["text"]) > 60:
                lead.append(claim_from(block["text"]))
            if len(lead) >= 2:
                break
    standfirst = lead[1] if len(lead) > 1 else (lead[0] if lead else "")
    if not standfirst:
        standfirst = "A long-scroll treatise for the AWS Certified Generative AI Developer - Professional exam."

    extra = ""
    name = builder.path.name
    if name in {"index.html", "volume-d1-foundation-models.html"}:
        extra = (
            "<p class='method'>On 2026-10-20 the Amazon Bedrock User Guide overview described a managed service "
            "with access to many foundation models, including Amazon, Anthropic, DeepSeek, Moonshot AI, MiniMax, "
            "OpenAI, and xAI, through the bedrock-runtime endpoint. It documents Converse, Invoke, Messages, "
            "Responses, and Chat Completions. Model catalogs move. The exam guide decides exam scope. A model "
            "name on the overview is not automatically an exam topic.</p>"
        )
    if name == "volume-d3-safety-security-governance.html":
        extra += (
            "<p class='method'>On 2026-10-20 the Bedrock Guardrails page named content filters (Hate, Insults, "
            "Sexual, Violence, Misconduct, and Prompt Attack), denied topics, word filters, sensitive information "
            "filters, contextual grounding checks, and Automated Reasoning checks. Guardrails can ride on an "
            "inference call or run alone through the ApplyGuardrail API. That page says reasoning content blocks "
            "are excluded.</p>"
        )

    if builder.kind == "companion":
        map_links = "".join(
            f"<li><a href='{html.escape(filename, quote=True)}'>{html.escape(label)}</a></li>"
            for filename, label in VOLUMES
        )
        full = f"<p><a href='../{html.escape(name, quote=True)}'>Open the long treatise page for this companion.</a></p>"
        home = "../index.html"
    else:
        map_links = "".join(
            f"<li><a href='{html.escape(filename, quote=True)}'>{html.escape(label)}</a></li>"
            for filename, label in VOLUMES
        )
        full = ""
        home = "index.html"

    title = builder.h1 or builder.path.stem
    return f"""<!DOCTYPE html>
<html lang="en" data-treatise="1">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<title>{html.escape(title)} — AIP-C01 treatise</title>
<link rel="preload" href="{builder.asset}/fonts/CharisSIL-latin-normal-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{builder.asset}/treatise.css">
<script>document.documentElement.classList.add("ds-js");</script>
</head>
<body>
<a class="skip" href="#content">Skip to the treatise</a>
<div class="progress" id="progress" aria-hidden="true"></div>
<header class="mast">
  <a class="brand" href="{home}">AIP-C01</a>
  <p class="mast-title">{html.escape(title)}</p>
  <button class="burger" id="nav-toggle" type="button" aria-expanded="false" aria-controls="sidebar">Sections</button>
</header>
<button class="backdrop" id="nav-backdrop" type="button" aria-label="Close sections"></button>
<div class="shell">
<nav class="sidebar" id="sidebar" aria-label="Sections">
  <label for="section-filter">Filter sections
    <input id="section-filter" type="search" placeholder="Filter sections" autocomplete="off">
  </label>
  <ol class="toc" id="toc"></ol>
  <p class="empty" id="toc-empty" hidden>No section matches.</p>
</nav>
<main id="content">
<header class="hero">
  <p class="kicker">AWS Certified Generative AI Developer — Professional</p>
  <h1>{html.escape(builder.h1 or title)}</h1>
  <p class="standfirst">{html.escape(standfirst)}</p>
  <p class="method">Read inward. The claim is the outer shell. Under it: the mechanism, the numbers, a worked scenario, and the exam trap.</p>
  {extra}
</header>
{''.join(articles)}
<footer class="sources">
  <h2 id="sources">Sources and how to read a number</h2>
  <p>Domain weights, scoring, task statements, and the in-scope service list were checked against the official exam guide on 2026-10-20: <a href="https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html">AWS Certified Generative AI Developer - Professional (AIP-C01)</a>. Bedrock's service description was checked the same day at <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html">What is Amazon Bedrock</a>. Guardrail filter names were checked at <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html">Amazon Bedrock Guardrails</a>.</p>
  <p>The AWS documentation MCP server was not attached in this environment. Pages were fetched from docs.aws.amazon.com instead. Topic prose is the study guide's own explanation, preserved from the previous volumes, which recorded a documentation pass on 2026-09-28. Diagrams drawn for this treatise are original. Where an older local figure is reused, the credit under it says so. Quotas, model IDs, and prices are volatile even when a sentence states them.</p>
  {full}
  <ul class="volume-map">{map_links}</ul>
</footer>
</main>
</div>
<script src="{builder.asset}/treatise.js" defer></script>
</body>
</html>
"""


def check_images(page: Path, markup: str) -> list[str]:
    missing = []
    for src in re.findall(r"<img[^>]+src='([^']+)'", markup) + re.findall(r'<img[^>]+src="([^"]+)"', markup):
        if src.startswith("http"):
            missing.append(src)
            continue
        full = (page.parent / src).resolve()
        if not full.is_file():
            missing.append(src)
    return missing


def main() -> None:
    write_plates()
    pages = [ROOT / name for name, _label in VOLUMES]
    pages += sorted((ROOT / "companions").glob("*.html"))
    failures = []
    for path in pages:
        builder = Builder(path)
        builder.parse()
        markup = render_page(builder)
        missing = check_images(path, markup)
        if missing:
            failures.append(f"{path.name}: missing images {missing[:8]}")
        if "fonts.googleapis.com" in markup or "cdn." in markup:
            failures.append(f"{path.name}: external asset reference")
        out_h2 = markup.count("<h2 ")
        # sources h2 is extra
        if out_h2 < builder.source_h2 + 1:
            failures.append(f"{path.name}: h2 {out_h2} < source {builder.source_h2}")
        old = subprocess.check_output(["git", "show", f"HEAD:{path.relative_to(ROOT)}"], text=True, errors="replace")
        old_h2 = old.count("<h2")
        if out_h2 < old_h2:
            failures.append(f"{path.name}: rebuilt h2 {out_h2} < original {old_h2}")
        out_pq = markup.count("class='pq'")
        if out_pq != builder.source_pq:
            failures.append(f"{path.name}: questions {out_pq} != {builder.source_pq}")
        path.write_text(markup, encoding="utf-8")
        print(f"{path.relative_to(ROOT)}: sections={builder.source_h2} questions={builder.source_pq} bytes={len(markup)}")
    if failures:
        print("FAILURES:")
        for line in failures:
            print(" -", line)
        sys.exit(1)


if __name__ == "__main__":
    main()

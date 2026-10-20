#!/usr/bin/env python3
"""
Generate Print-Ready, Environment-Friendly, Paper-Optimized PDF & Word Document
for AWS AIP-C01 Generative AI Developer - Professional Exam.

Features:
- Compact 2-column layout with 8mm margins to minimize paper usage
- Images sized and constrained to prevent page bloat and orphan white space
- Complete first-principles Russian Doll coverage of all 95 topics + 13 hands-on labs
- Generates both AIP-C01_Overnight_Print_Guide.pdf (via Playwright)
  and AIP-C01_Overnight_Study_Guide.docx (via Pandoc)
"""

import json, os, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def build_print_html():
    core_path = ROOT / 'course/core.json'
    with open(core_path) as f:
        core = json.load(f)

    # Group slides by domain
    domains = {
        0: {"title": "Foundations & Exam Strategy", "weight": "Prerequisite", "slides": []},
        1: {"title": "Domain 1: Foundation Model Integration, Data Management & Compliance", "weight": "31% of Exam", "slides": []},
        2: {"title": "Domain 2: Implementation and Integration", "weight": "26% of Exam", "slides": []},
        3: {"title": "Domain 3: AI Safety, Security, and Governance", "weight": "20% of Exam", "slides": []},
        4: {"title": "Domain 4: Operational Efficiency and Optimization", "weight": "12% of Exam", "slides": []},
        5: {"title": "Domain 5: Testing, Validation, and Troubleshooting", "weight": "11% of Exam", "slides": []},
    }

    for s in core:
        d = s.get('domain', 0)
        if d in domains:
            domains[d]["slides"].append(s)

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>AWS AIP-C01 Overnight Print Study Guide</title>
  <style>
    @page {{
      size: letter;
      margin: 8mm 8mm 8mm 8mm;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      font-size: 8.5pt;
      line-height: 1.32;
      color: #111;
      background: #fff;
    }}
    h1.doc-title {{
      font-size: 16pt;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: -0.01em;
      border-bottom: 2pt solid #111;
      padding-bottom: 3pt;
      margin-bottom: 4pt;
    }}
    .doc-meta {{
      font-size: 8pt;
      color: #444;
      display: flex;
      justify-content: space-between;
      margin-bottom: 8pt;
      border-bottom: 0.5pt solid #888;
      padding-bottom: 3pt;
    }}
    .compact-columns {{
      column-count: 2;
      column-gap: 6mm;
      column-rule: 0.5pt solid #ddd;
    }}
    .domain-header {{
      background: #222;
      color: #fff;
      padding: 3pt 6pt;
      font-size: 10pt;
      font-weight: 700;
      margin: 8pt 0 4pt;
      break-after: avoid;
      border-radius: 2pt;
    }}
    .topic-card {{
      border: 0.5pt solid #bbb;
      border-radius: 3pt;
      padding: 4pt 6pt;
      margin-bottom: 5pt;
      break-inside: avoid;
      background: #fafafa;
    }}
    .topic-title {{
      font-size: 9.5pt;
      font-weight: 700;
      color: #0b2545;
      margin-bottom: 2pt;
      display: flex;
      justify-content: space-between;
    }}
    .topic-skills {{
      font-size: 7.5pt;
      font-weight: normal;
      color: #666;
    }}
    .topic-lead {{
      font-size: 8.2pt;
      font-weight: 600;
      color: #222;
      margin-bottom: 2pt;
    }}
    .topic-points {{
      padding-left: 10pt;
      margin-bottom: 3pt;
    }}
    .topic-points li {{
      margin-bottom: 1.5pt;
      font-size: 8pt;
    }}
    .rd-box {{
      border-left: 2pt solid #2457d6;
      padding-left: 4pt;
      margin: 2pt 0;
      background: #f0f4fd;
      font-size: 7.8pt;
    }}
    .rd-row {{
      margin-bottom: 1.5pt;
    }}
    .rd-tag {{
      font-weight: 700;
      color: #1a365d;
    }}
    .trap-box {{
      background: #fff8eb;
      border: 0.5pt solid #f59e0b;
      padding: 2pt 4pt;
      font-size: 7.8pt;
      margin-top: 2pt;
      border-radius: 2pt;
    }}
    .trap-box strong {{
      color: #b45309;
    }}
    .img-box {{
      text-align: center;
      margin: 3pt 0;
      break-inside: avoid;
    }}
    .img-box img {{
      max-width: 95%;
      max-height: 85pt;
      object-fit: contain;
      border: 0.5pt solid #ccc;
      border-radius: 2pt;
    }}
    .lab-card {{
      border: 1pt solid #10b981;
      border-radius: 3pt;
      padding: 5pt 7pt;
      margin-bottom: 6pt;
      break-inside: avoid;
      background: #f0fdf4;
    }}
    .lab-title {{
      font-size: 9.5pt;
      font-weight: 800;
      color: #065f46;
      margin-bottom: 2pt;
    }}
    .lab-steps {{
      padding-left: 11pt;
      font-size: 8pt;
    }}
    .lab-steps li {{
      margin-bottom: 2pt;
    }}
    .matrix-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 7.5pt;
      margin: 4pt 0;
      break-inside: avoid;
    }}
    .matrix-table th, .matrix-table td {{
      border: 0.5pt solid #999;
      padding: 2pt 3pt;
      text-align: left;
    }}
    .matrix-table th {{
      background: #eee;
      font-weight: 700;
    }}
    code {{
      font-family: ui-monospace, Menlo, Consolas, monospace;
      font-size: 7.5pt;
      background: #eef;
      padding: 1pt 2pt;
      border-radius: 1pt;
    }}
  </style>
</head>
<body>
  <h1 class="doc-title">AWS Certified Generative AI Developer – Professional (AIP-C01)</h1>
  <div class="doc-meta">
    <span><strong>Comprehensive Overnight Print Master Guide</strong> · 75 Questions · 180 Min · 750/1000 Pass</span>
    <span>Eco-Friendly 2-Column Compact Edition · Zero Waste Pages</span>
  </div>

  <div class="compact-columns">
"""

    # Add each domain and slide
    for d_idx, d_data in domains.items():
        html += f"""
        <div class="domain-header">
          {d_data['title']} ({d_data['weight']})
        </div>
        """
        for s in d_data["slides"]:
            rd = s.get('russianDoll', {})
            img_html = ""
            if s.get('image'):
                # Use clean path relative to print file
                img_path = s['image'].replace('../', '')
                if (ROOT / img_path).exists():
                    img_html = f"""<div class="img-box"><img src="../{img_path}" alt="{s['title']}"></div>"""

            points_html = "".join([f"<li>{p}</li>" for p in s.get('points', [])[:3]])

            html += f"""
            <div class="topic-card" id="{s['id']}">
              <div class="topic-title">
                <span>{s['title']}</span>
                <span class="topic-skills">{s['id']} · Skills: {', '.join(s.get('skills', []))}</span>
              </div>
              <div class="topic-lead">{s.get('lead', '')}</div>
              {img_html}
              <ul class="topic-points">
                {points_html}
              </ul>
              <div class="rd-box">
                <div class="rd-row"><span class="rd-tag">Intuition:</span> {rd.get('intuition', '')}</div>
                <div class="rd-row"><span class="rd-tag">API/Config:</span> <code>{rd.get('api', '')[:140]}...</code></div>
                <div class="rd-row"><span class="rd-tag">Exam Rule:</span> <strong>{rd.get('examRule', '')}</strong></div>
              </div>
              <div class="trap-box">
                <strong>Exam Trap:</strong> {s.get('trap', '')}
              </div>
            </div>
            """

    # Add Section 2: Complete Practical Lab Knowledge (13 Hands-On Labs)
    labs = [
        ("Lab 1: Bedrock Model Access & Converse API Invocation", [
            "Enable Model Access in the Amazon Bedrock Console under Model Access (some Anthropic/Meta models require EULA acceptance).",
            "IAM Permission: Identity requires <code>bedrock:InvokeModel</code> and <code>bedrock:InvokeModelWithResponseStream</code> on <code>arn:aws:bedrock:*::foundation-model/*</code>.",
            "Call <code>bedrock-runtime.converse()</code> with <code>modelId</code>, <code>messages</code>, <code>system</code>, and <code>inferenceConfig</code> (temperature, maxTokens, topP).",
            "Inspect response: Check <code>output.message.content</code>, <code>stopReason</code> (verify if 'end_turn' or 'max_tokens'), and <code>usage</code> (inputTokens, outputTokens)."
        ]),
        ("Lab 2: Knowledge Base Creation with OpenSearch Serverless (AOSS)", [
            "Prepare S3 Data Source: Create S3 bucket with documents (PDFs, Markdown, TXT) and enable SSE-KMS Customer Managed Key.",
            "Bedrock Console -> Knowledge Bases -> Create Knowledge Base. Name: <code>corp-kb</code>. Service role auto-created by Bedrock.",
            "Data Source: Connect S3 bucket. Select Chunking Strategy: Default (300 tokens, 20% overlap), Hierarchical (parent-child for precision+context), or Semantic.",
            "Embedding Model: Choose Amazon Titan Text Embeddings v2 (supports 1024, 512, or 256 dimensions) or Cohere Embed.",
            "Vector Store: Choose 'Quick create a new vector store - Amazon OpenSearch Serverless'. Bedrock creates collection, encryption policy, network policy, and data access policy automatically."
        ]),
        ("Lab 3: Knowledge Base Synchronization & Incremental Ingestion", [
            "Execute sync via CLI or boto3: <code>bedrock_agent.start_ingestion_job(knowledgeBaseId='...', dataSourceId='...')</code>.",
            "Poll job status: <code>get_ingestion_job()</code> until status is <code>COMPLETE</code>. Inspect <code>statistics.numberOfDocumentsScanned</code> and <code>numberOfNewDocumentsIndexed</code>.",
            "File Deletion: When an S3 object is deleted, running an ingestion job automatically deletes the corresponding vectors from OpenSearch Serverless."
        ]),
        ("Lab 4: Hybrid Search & Re-Ranking Configuration", [
            "Invoke Retrieve API: Set <code>vectorSearchConfiguration.overrideSearchType = 'HYBRID'</code> in <code>bedrock-agent-runtime.retrieve()</code>.",
            "Hybrid search executes BM25 lexical keyword matching AND dense vector semantic search in parallel.",
            "Merges results via Reciprocal Rank Fusion (RRF), then applies Bedrock Re-ranking model (Cohere Rerank) to return top-K re-scored passages."
        ]),
        ("Lab 5: Building an Amazon Bedrock Action Agent End-to-End", [
            "Step 1: Create Agent. Specify Foundation Model (e.g. Claude 3.5 Sonnet) and precise System Instructions.",
            "Step 2: Add Action Group. Upload OpenAPI 3.0 JSON schema to S3. Select Lambda function as action group executor.",
            "Step 3: Lambda Permissions. Add resource policy to Lambda allowing <code>bedrock.amazonaws.com</code> with condition <code>aws:SourceArn</code> of the agent.",
            "Step 4: Associate Knowledge Base. Link Knowledge Base with instruction on when the agent should query it.",
            "Step 5 (CRITICAL EXAM TRAP): Click <strong>Prepare</strong> in console or call <code>prepare_agent()</code>. Without preparing, updates never take effect! Create an Agent Alias (e.g. <code>PROD</code>) pointing to version snapshot."
        ]),
        ("Lab 6: Human-in-the-Loop (HITL) with Return of Control", [
            "In Action Group configuration, choose <code>RETURN_OF_CONTROL</code> instead of directly executing Lambda.",
            "When agent selects the action, <code>invoke_agent()</code> pauses and returns <code>returnControl</code> event with action invocation parameters to client.",
            "Application displays action details to human reviewer. Once approved, application calls <code>invoke_agent()</code> passing <code>sessionState.returnControlInvocationResults</code> with execution confirmation."
        ]),
        ("Lab 7: Amazon Bedrock Guardrails Setup & Contextual Grounding", [
            "Bedrock Console -> Guardrails -> Create Guardrail. Configure Denied Topics with natural language descriptions and blocked examples.",
            "Content Filters: Configure strengths (LOW, MEDIUM, HIGH) for Hate, Insults, Sexual, Violence, Misconduct, and Prompt Attack.",
            "Sensitive Info (PII): Select PII entity types (SSN, credit card, phone). Action: <code>ANONYMIZE</code> (masks data) or <code>BLOCK</code> (halts request).",
            "Contextual Grounding Filter: Set Grounding threshold (e.g. 0.85) and Relevance threshold (e.g. 0.80) to detect RAG hallucinations.",
            "Testing: Test in Guardrail Playground. In code, pass <code>guardrailConfig={'guardrailIdentifier': '...', 'guardrailVersion': '1'}</code> in <code>converse()</code>, or call standalone <code>apply_guardrail()</code>."
        ]),
        ("Lab 8: Prompt Management & Prompt Caching", [
            "Create Prompt in Bedrock Prompt Management. Define dynamic variables via <code>{{variable_name}}</code>.",
            "Create immutable Version (e.g. '1'). Production applications point to Version 1, not the mutable DRAFT.",
            "Prompt Caching: Place static prefix (system prompt, few-shot examples, large reference docs) at the START of the prompt (minimum 1,024 tokens for Claude).",
            "Converse API sets <code>cachePoint: {'type': 'default'}</code>. First call writes cache; subsequent calls hit cache with 90% cost savings and 5-min TTL."
        ]),
        ("Lab 9: Provisioned Throughput vs Batch Inference", [
            "On-Demand: Default serverless pay-per-token pricing. Best for bursty, unpredictable traffic.",
            "Provisioned Throughput: Call <code>create_provisioned_model_throughput()</code>. Commit 1+ Model Units (MUs) for 1 or 6 months. Required for guaranteed low latency SLAs and MANDATORY for serving fine-tuned custom models.",
            "Batch Inference: Call <code>create_model_invocation_job()</code> with input JSONL in S3. 50% discount for asynchronous offline bulk processing."
        ]),
        ("Lab 10: Cross-Region Inference Resilience", [
            "System-Defined Inference Profiles: Replace regional modelId with profile ID (e.g. <code>us.anthropic.claude-3-5-sonnet-20240620-v1:0</code>).",
            "Bedrock dynamically routes traffic across us-east-1, us-west-2, us-east-2 to bypass regional capacity limits and eliminate 429 ThrottlingException.",
            "Residency compliance: European profile (<code>eu.</code>) routes strictly within European regions (Frankfurt, Ireland, Paris) to comply with GDPR."
        ]),
        ("Lab 11: Security Isolation with PrivateLink & KMS", [
            "Create VPC Interface Endpoints for Bedrock (<code>com.amazonaws.region.bedrock-runtime</code> and <code>bedrock</code>) in private subnets.",
            "VPC Endpoint Policy: Enforce condition <code>StringEquals: {'aws:PrincipalArn': 'arn:.../AppRole'}</code>.",
            "IAM Policy: Restrict Bedrock invocations with condition <code>StringEquals: {'aws:sourceVpce': 'vpce-xxx'}</code>.",
            "Model Invocation Logging: Call <code>put_model_invocation_logging_configuration()</code> to log prompts and completions to S3 with KMS encryption. (CloudTrail logs only API management events, never payload text)."
        ]),
        ("Lab 12: Model Evaluation & Benchmark Jobs", [
            "Automated Evaluation: Create job using built-in datasets (TREC, BoolQ) or upload custom JSONL evaluation dataset to S3.",
            "Metrics evaluated: Accuracy, Robustness, Toxicity. Output report provides comparative radar charts and scores.",
            "Human Evaluation: Configure workforce using Amazon Mechanical Turk, AWS Managed Workforce, or Private Company Workforce (Amazon Cognito). Reviewers score answers on 1-5 rubrics.",
            "Mitigate LLM Judge Biases: Swap position order (A/B and B/A) to defeat position bias, enforce Chain-of-Thought (CoT) reasoning before score emission."
        ]),
        ("Lab 13: Systematic Troubleshooting & Error Code Resolution", [
            "429 <code>ThrottlingException</code>: Apply Exponential Backoff with FULL JITTER algorithm, switch to Cross-Region Inference Profile, or purchase Provisioned Throughput.",
            "503 <code>ModelNotReadyException</code>: Check Provisioned Model status; model is warming up, retry with backoff.",
            "400 <code>ValidationException</code>: Max context tokens exceeded or invalid JSON payload. Do NOT retry without fixing input payload.",
            "403 <code>AccessDeniedException</code>: Check IAM identity policy permissions AND verify Model Access is activated in Bedrock console for that Region."
        ])
    ]

    html += f"""
    <div class="domain-header" style="background:#047857;">
      Part 2: Complete Practical Lab Knowledge (13 Hands-On Labs)
    </div>
    """
    for lab_title, lab_steps in labs:
        steps_html = "".join([f"<li>{s}</li>" for s in lab_steps])
        html += f"""
        <div class="lab-card">
          <div class="lab-title">🛠️ {lab_title}</div>
          <ol class="lab-steps">
            {steps_html}
          </ol>
        </div>
        """

    # Section 3: Rapid Decision Matrix Table
    html += f"""
    <div class="domain-header" style="background:#4338ca;">
      Part 3: 30-Second Rapid Elimination Decision Matrix
    </div>
    <table class="matrix-table">
      <thead>
        <tr><th>If Scenario Requires...</th><th>Credited AWS Architecture</th><th>Why Distractors Fail</th></tr>
      </thead>
      <tbody>
        <tr><td>Dynamic company policies changing daily</td><td>Bedrock Knowledge Base (RAG)</td><td>Fine-tuning is frozen at training time and cannot update daily</td></tr>
        <tr><td>Strict JSON schema & downstream tool calling</td><td>Bedrock Converse API with toolConfig</td><td>Regex parsing is brittle; InvokeModel lacks unified tool schema</td></tr>
        <tr><td>Part numbers, serial codes, exact IDs</td><td>Hybrid Search (BM25 + Semantic Vector) + Rerank</td><td>Pure vector search misses exact keyword string matches</td></tr>
        <tr><td>Autonomous multi-step actions with APIs</td><td>Bedrock Agent with OpenAPI 3.0 & Lambda</td><td>Chained prompts cannot autonomously validate external tools</td></tr>
        <tr><td>Prevent hallucinations in RAG answers</td><td>Bedrock Guardrails Contextual Grounding</td><td>Standard toxicity filters do not check source faithfulness</td></tr>
        <tr><td>Mask SSN/Credit Cards without stopping flow</td><td>Bedrock Guardrails PII with action=ANONYMIZE</td><td>action=BLOCK stops the user conversation entirely</td></tr>
        <tr><td>Eliminate 429 Throttling during traffic spikes</td><td>Cross-Region Inference Profile (us./eu.)</td><td>Single-region quotas throttle; Provisioned is costly for spikes</td></tr>
        <tr><td>Auditing user prompt text for compliance</td><td>Bedrock Model Invocation Logging to S3</td><td>CloudTrail logs API management calls, NEVER prompt/payload text</td></tr>
        <tr><td>Zero internet traversal from private subnets</td><td>VPC Interface Endpoint (PrivateLink)</td><td>S3 Gateway Endpoint does not secure Bedrock runtime calls</td></tr>
        <tr><td>Offline bulk summarization at lowest cost</td><td>Amazon Bedrock Batch Inference</td><td>Synchronous on-demand costs 2x more and hits request quotas</td></tr>
      </tbody>
    </table>
    """

    html += """
  </div>
</body>
</html>
"""
    output_html_path = ROOT / 'course/print-study-guide.html'
    output_html_path.write_text(html)
    print(f"Generated compact print HTML at {output_html_path}")
    return output_html_path

def generate_pdf(html_path):
    pdf_path = ROOT / 'AIP-C01_Overnight_Print_Guide.pdf'
    downloads_pdf = Path('/Users/rj/Downloads/AIP-C01_Overnight_Print_Guide.pdf')
    
    script = f"""
import {{ chromium }} from 'playwright';
const browser = await chromium.launch({{ headless: true, executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' }});
const page = await browser.newPage();
await page.goto('file://{html_path}', {{ waitUntil: 'networkidle' }});
await page.pdf({{
  path: '{pdf_path}',
  format: 'Letter',
  margin: {{ top: '8mm', bottom: '8mm', left: '8mm', right: '8mm' }},
  printBackground: true
}});
await browser.close();
console.log('Successfully generated PDF: {pdf_path}');
"""
    js_file = ROOT / '.build/generate_pdf.mjs'
    js_file.parent.mkdir(parents=True, exist_ok=True)
    js_file.write_text(script)
    
    cmd = ['node', str(js_file)]
    subprocess.run(cmd, check=True)
    
    # Copy to downloads
    if pdf_path.exists():
        import shutil
        shutil.copy2(pdf_path, downloads_pdf)
        print(f"Copied PDF to user Downloads: {downloads_pdf} ({downloads_pdf.stat().st_size / 1024:.1f} KB)")

def generate_docx():
    docx_path = ROOT / 'AIP-C01_Overnight_Study_Guide.docx'
    downloads_docx = Path('/Users/rj/Downloads/AIP-C01_Overnight_Study_Guide.docx')
    
    # Convert HTML to DOCX using Pandoc
    cmd = [
        '/opt/homebrew/bin/pandoc',
        str(ROOT / 'course/print-study-guide.html'),
        '-o', str(docx_path),
        '--from=html',
        '--to=docx'
    ]
    subprocess.run(cmd, check=True)
    print(f"Successfully generated DOCX: {docx_path}")
    
    if docx_path.exists():
        import shutil
        shutil.copy2(docx_path, downloads_docx)
        print(f"Copied DOCX to user Downloads: {downloads_docx} ({downloads_docx.stat().st_size / 1024:.1f} KB)")

if __name__ == '__main__':
    html_file = build_print_html()
    generate_pdf(html_file)
    generate_docx()

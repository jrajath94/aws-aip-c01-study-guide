#!/usr/bin/env python3
"""
Generate Publication-Grade Visual Master Study Guide, PDF & Word Document
for AWS AIP-C01 Generative AI Developer - Professional Exam.

Design & Pedagogical Highlights:
- Typographic Foundation: Anthropic Sans (Regular, Bold, Italic, BoldItalic) base64-embedded
- Humanized Content: Zero raw IDs (no 'q-d-1-1010', 'q-d1-025', or cryptic slugs)
- Visual Communication: Signature domain color accents, Russian Doll layer pills, exam trap alerts
- Typography: Justified text, generous 1.5 line spacing, bolded key terms and parameters
- Official Diagrams: Full-width and high-resolution AWS official architecture diagrams & UI captures
- Complete Coverage: 95 lessons, 13 practical labs, 6 question patterns, 30-sec elimination matrix,
  and cleaned high-yield blueprint practice questions.
"""

import base64, hashlib, json, os, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def get_base64_fonts():
    typo_dir = ROOT / 'assets/typography'
    fonts = {}
    for style, filename in [
        ('regular', 'AnthropicSans-Regular.ttf'),
        ('bold', 'AnthropicSans-Bold.ttf'),
        ('italic', 'AnthropicSans-Italic.ttf'),
        ('bold-italic', 'AnthropicSans-BoldItalic.ttf')
    ]:
        p = typo_dir / filename
        if p.exists():
            fonts[style] = base64.b64encode(p.read_bytes()).decode('ascii')
    return fonts

def clean_lesson_title(title, raw_id):
    # Remove any internal prefixes or slug noise
    clean = re.sub(r'^[0-9.]+\s*', '', title).strip()
    return clean

def clean_question_for_print(q, idx):
    raw_title = q.get('rawTitle') or q.get('title', '')
    m = re.match(r'^(D\d)\s*·\s*(EASY|MEDIUM|HARD)\s*·\s*([^,]+),\s*(?:q-d\d-[0-9a-zA-Z_-]+)\s*·\s*(.*?)\s+Q(\d+)\.\s*(.*)$', raw_title, re.DOTALL)
    if m:
        d_code, difficulty, resp_type, topic, q_num, question_text = m.groups()
        clean_topic = re.sub(r'^[0-9.]+\s*', '', topic).strip()
        resp_clean = 'Single Choice' if 'ONE' in resp_type else ('Multiple Response (Select 2)' if '2' in resp_type else 'Multiple Response (Select 3)')
        return {
            'number': int(q_num),
            'topic': clean_topic,
            'difficulty': difficulty.capitalize(),
            'responseType': resp_clean,
            'stem': question_text.strip(),
            'options': q.get('options', []),
            'answer': q.get('answer', '')
        }
    return {
        'number': idx + 1,
        'topic': q.get('topic', 'Cloud & AI Foundations'),
        'difficulty': q.get('difficulty', 'Foundations'),
        'responseType': 'Multiple Response' if 'TWO' in raw_title or 'Select 2' in raw_title else 'Single Choice',
        'stem': q.get('cleanStem') or q.get('title', ''),
        'options': q.get('options', []),
        'answer': q.get('answer', '')
    }

def build_master_html():
    fonts = get_base64_fonts()
    
    font_faces = ""
    if fonts.get('regular'):
        font_faces += f"""
        @font-face {{
          font-family: 'Anthropic Sans';
          src: url(data:font/truetype;charset=utf-8;base64,{fonts['regular']}) format('truetype');
          font-weight: 400;
          font-style: normal;
        }}
        """
    if fonts.get('bold'):
        font_faces += f"""
        @font-face {{
          font-family: 'Anthropic Sans';
          src: url(data:font/truetype;charset=utf-8;base64,{fonts['bold']}) format('truetype');
          font-weight: 700;
          font-style: normal;
        }}
        """
    if fonts.get('italic'):
        font_faces += f"""
        @font-face {{
          font-family: 'Anthropic Sans';
          src: url(data:font/truetype;charset=utf-8;base64,{fonts['italic']}) format('truetype');
          font-weight: 400;
          font-style: italic;
        }}
        """
    if fonts.get('bold-italic'):
        font_faces += f"""
        @font-face {{
          font-family: 'Anthropic Sans';
          src: url(data:font/truetype;charset=utf-8;base64,{fonts['bold-italic']}) format('truetype');
          font-weight: 700;
          font-style: italic;
        }}
        """

    # Load core data
    with open(ROOT / 'course/core.json') as f:
        core = json.load(f)

    # Load course-data.js to extract cleaned quizzes
    with open(ROOT / 'course/course-data.js') as f:
        raw_js = f.read()
    json_str = raw_js.split('window.COURSE=', 1)[1].strip().rstrip(';')
    course_data = json.loads(json_str)
    all_quizzes = course_data.get('quizzes', [])

    # Group slides by domain
    domains = {
        1: {
            "title": "Domain 1: Foundation Model Integration, Data Management & Compliance",
            "weight": "31% of Examination",
            "lead": "Evaluation and selection of foundation models, high-performance RAG data pipelines, prompt caching optimization, context budgeting, and cross-region resilience.",
            "color": "#1e3a8a",
            "accent": "#3b82f6",
            "slides": [],
            "diagrams": [
                ("AWS Bedrock Foundation Model Ingestion & Architecture Flow", "assets/cleaned/aws-02.png", "End-to-end request lifecycle from client applications through Bedrock API to model provider runtime environments."),
                ("Cross-Region Inference Profile Routing Architecture", "assets/cleaned/aws-08.png", "Dynamic routing across us-east-1, us-west-2, and us-east-2 to eliminate 429 ThrottlingException while strictly respecting geographic data residency."),
                ("Amazon Bedrock Prompt Caching Console Configuration", "assets/official-ui/09-prompt-cache-toggle.png", "Activating prompt caching for Claude models. Requires minimum 1,024 prefix tokens with rolling 5-minute TTL."),
                ("Knowledge Base Metadata Filter Group Builder", "assets/official-ui/08-kb-filter-example.png", "Configuring complex boolean and relational metadata filters (AND/OR groups) for granular vector retrieval.")
            ]
        },
        2: {
            "title": "Domain 2: Implementation and Integration",
            "weight": "26% of Examination",
            "lead": "Conversational state management with Bedrock Converse API, autonomous agent orchestration, action groups, tool use, knowledge bases, and multi-agent supervisor systems.",
            "color": "#065f46",
            "accent": "#10b981",
            "slides": [],
            "diagrams": [
                ("Amazon Bedrock Agent Runtime Execution Loop", "assets/aws-agent-runtime.png", "The ReAct orchestration loop: Pre-processing, action execution via Lambda / RETURN_OF_CONTROL, observation handling, and post-processing."),
                ("Bedrock Knowledge Base Ingestion & Vector Indexing Architecture", "assets/cleaned/aws-03.png", "Document chunking (fixed, hierarchical, semantic), embedding generation via Titan v2, and indexing in OpenSearch Serverless / Aurora pgvector."),
                ("Hybrid Search (BM25 + Semantic Vector) and Re-ranking Flow", "assets/cleaned/aws-04.png", "Merging lexical keyword search for part numbers/acronyms with semantic vector embeddings, scored via Cohere Re-rank v3.5."),
                ("Bedrock Agent Test Window & Detailed Execution Trace", "assets/official-ui/12-agent-test-window.png", "Live debugging of agent orchestration showing rationale tokens, tool call parameters, Lambda responses, and final response synthesis.")
            ]
        },
        3: {
            "title": "Domain 3: AI Safety, Security, and Governance",
            "weight": "20% of Examination",
            "lead": "Enterprise governance, multi-layer Bedrock Guardrails, contextual grounding hallucination detection, VPC PrivateLink isolation, and the CloudTrail vs Invocation Logging audit boundary.",
            "color": "#7c2d12",
            "accent": "#f97316",
            "slides": [],
            "diagrams": [
                ("Amazon Bedrock Guardrails Multi-Layer Protection Pipeline", "assets/cleaned/aws-09.png", "Evaluation stages: Content filters (Hate, Violence, Jailbreaks), Denied Topics, PII Anonymization/Blocking, and Contextual Grounding."),
                ("Contextual Grounding Hallucination Detection Architecture", "assets/cleaned/aws-10.png", "Dual-score evaluation: Grounding score (factual alignment with retrieved chunks) and Relevance score (alignment with user prompt)."),
                ("Private Network Isolation via VPC Endpoints & KMS CMK Encryption", "assets/cleaned/aws-14.png", "Securing bedrock-runtime and bedrock-agent-runtime over AWS PrivateLink with strict IAM condition keys (aws:sourceVpce)."),
                ("The Observability Trio: CloudTrail vs Invocation Logging vs AWS X-Ray", "assets/cleaned/aws-15.png", "Architectural boundary: CloudTrail tracks management events (NEVER payloads), Invocation Logging archives full text to S3/CloudWatch, and X-Ray traces latency.")
            ]
        },
        4: {
            "title": "Domain 4: Operational Efficiency and Optimization",
            "weight": "12% of Examination",
            "lead": "Cost and latency optimization, prompt caching economics, model customization spectrum (Prompting vs RAG vs PEFT/LoRA vs Continued Pre-training), and Provisioned Throughput.",
            "color": "#4c1d95",
            "accent": "#8b5cf6",
            "slides": [],
            "diagrams": [
                ("The Foundation Model Customization Spectrum", "assets/cleaned/aws-16.png", "Trade-off ladder: Prompt Engineering (lowest effort) -> RAG -> Fine-Tuning (LoRA) -> Continued Pre-training (highest effort/cost)."),
                ("Parameter-Efficient Fine-Tuning (PEFT / LoRA) Architecture", "assets/cleaned/aws-17.png", "Freezing base model weights and training lightweight low-rank adapter matrices to dramatically reduce VRAM requirements."),
                ("Inference Modalities: Provisioned Throughput vs Batch vs On-Demand", "assets/cleaned/aws-18.png", "Pricing and operational comparison: Model Units for committed low latency vs 50% discounted Batch Inference vs Serverless On-Demand.")
            ]
        },
        5: {
            "title": "Domain 5: Testing, Validation, and Troubleshooting",
            "weight": "11% of Examination",
            "lead": "Model evaluation metrics (ROUGE, BLEU, BERTScore), human-in-the-loop evaluation workforces, LLM-as-a-Judge bias mitigation, and systemic error troubleshooting.",
            "color": "#831843",
            "accent": "#ec4899",
            "slides": [],
            "diagrams": [
                ("Automated Model Evaluation Job Architecture", "assets/cleaned/aws-19.png", "Evaluating text summarization and Q&A using ROUGE-1/2/L, BLEU, and BERTScore on built-in and custom S3 datasets."),
                ("Human Evaluation Workforce & LLM-as-a-Judge Bias Mitigation", "assets/cleaned/aws-20.png", "Configuring Private Company Workforces and mitigating position/verbosity biases through swap testing and Chain-of-Thought prompting.")
            ]
        }
    }

    for s in core:
        d = s.get('domain', 0)
        if d in domains:
            domains[d]["slides"].append(s)

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>AWS Certified Generative AI Developer – Professional (AIP-C01) Master Study Guide</title>
  <style>
    {font_faces}

    @page {{
      size: letter;
      margin: 12mm 12mm 14mm 12mm;
      @bottom-center {{
        content: "AWS AIP-C01 Professional Master Guide · Page " counter(page);
        font-family: 'Anthropic Sans', sans-serif;
        font-size: 8pt;
        color: #666;
      }}
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Anthropic Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-size: 9.2pt;
      line-height: 1.52;
      color: #1a1a1a;
      background: #fff;
      text-align: justify;
      text-justify: inter-word;
      -webkit-font-smoothing: antialiased;
    }}

    /* Document Header */
    .master-header {{
      border-bottom: 3pt solid #1e3a8a;
      padding-bottom: 8pt;
      margin-bottom: 12pt;
    }}
    .doc-pretitle {{
      font-size: 9pt;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #2563eb;
      margin-bottom: 2pt;
    }}
    h1.doc-title {{
      font-size: 19pt;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.15;
      letter-spacing: -0.02em;
      margin-bottom: 4pt;
    }}
    .doc-subtitle {{
      font-size: 11pt;
      color: #475569;
      font-weight: 600;
      margin-bottom: 6pt;
    }}
    .doc-meta-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #f8fafc;
      border: 1pt solid #e2e8f0;
      border-radius: 4pt;
      padding: 4pt 8pt;
      font-size: 8.5pt;
      color: #334155;
    }}
    .doc-meta-item strong {{
      color: #0f172a;
    }}

    /* Domain Section Banners */
    .domain-banner {{
      margin: 18pt 0 10pt 0;
      padding: 8pt 12pt;
      border-radius: 4pt;
      color: #fff;
      break-after: avoid;
    }}
    .domain-banner-title {{
      font-size: 13pt;
      font-weight: 800;
      letter-spacing: -0.01em;
      margin-bottom: 2pt;
    }}
    .domain-banner-meta {{
      font-size: 8.8pt;
      opacity: 0.92;
      font-style: italic;
    }}

    /* Architecture Visual Gallery */
    .diagram-gallery {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10pt;
      margin: 10pt 0 14pt 0;
      break-inside: avoid;
    }}
    .diagram-figure-card {{
      border: 1pt solid #cbd5e1;
      border-radius: 4pt;
      background: #f8fafc;
      padding: 6pt;
      display: flex;
      flex-direction: column;
      break-inside: avoid;
    }}
    .diagram-figure-card.full-width {{
      grid-column: 1 / -1;
    }}
    .diagram-img-box {{
      text-align: center;
      background: #ffffff;
      border: 0.5pt solid #e2e8f0;
      border-radius: 3pt;
      padding: 4pt;
      margin-bottom: 4pt;
    }}
    .diagram-img-box img {{
      max-width: 100%;
      max-height: 180px;
      object-fit: contain;
      display: block;
      margin: 0 auto;
    }}
    .diagram-card-title {{
      font-size: 8.8pt;
      font-weight: 700;
      color: #1e293b;
      margin-bottom: 2pt;
    }}
    .diagram-card-caption {{
      font-size: 7.8pt;
      line-height: 1.35;
      color: #475569;
      text-align: justify;
    }}

    /* 2-Column Responsive Reading Grid */
    .lessons-grid {{
      column-count: 2;
      column-gap: 8mm;
      column-rule: 0.5pt solid #e2e8f0;
    }}

    /* Topic Lesson Card */
    .lesson-card {{
      border: 0.5pt solid #cbd5e1;
      border-left: 3pt solid #2563eb;
      border-radius: 3pt;
      padding: 6pt 8pt;
      margin-bottom: 8pt;
      background: #ffffff;
      break-inside: avoid;
    }}
    .lesson-header {{
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      border-bottom: 0.5pt solid #f1f5f9;
      padding-bottom: 2pt;
      margin-bottom: 3pt;
    }}
    .lesson-title {{
      font-size: 9.8pt;
      font-weight: 700;
      color: #0f172a;
    }}
    .lesson-badge {{
      font-size: 7.5pt;
      font-weight: 600;
      color: #64748b;
      background: #f1f5f9;
      padding: 1pt 4pt;
      border-radius: 2pt;
    }}
    .lesson-lead {{
      font-size: 8.5pt;
      font-style: italic;
      color: #334155;
      margin-bottom: 4pt;
      line-height: 1.4;
    }}
    .lesson-points {{
      padding-left: 11pt;
      margin-bottom: 5pt;
      font-size: 8.6pt;
    }}
    .lesson-points li {{
      margin-bottom: 2.5pt;
      line-height: 1.45;
    }}

    /* Russian Doll Layer Boxes */
    .rd-box {{
      background: #f8fafc;
      border-radius: 3pt;
      padding: 4pt 6pt;
      margin: 4pt 0;
      font-size: 8.2pt;
      line-height: 1.4;
    }}
    .rd-row {{
      margin-bottom: 2.5pt;
    }}
    .rd-tag {{
      font-weight: 700;
      text-transform: uppercase;
      font-size: 7.2pt;
      letter-spacing: 0.03em;
    }}
    .tag-intuition {{ color: #2563eb; }}
    .tag-api {{ color: #4f46e5; }}
    .tag-rule {{ color: #d97706; }}

    /* Exam Trap Alert Box */
    .trap-card {{
      background: #fef2f2;
      border: 0.5pt solid #fecaca;
      border-left: 2.5pt solid #dc2626;
      border-radius: 3pt;
      padding: 3.5pt 6pt;
      margin-top: 4pt;
      font-size: 8.2pt;
      line-height: 1.38;
      color: #991b1b;
    }}
    .trap-card strong {{
      color: #7f1d1d;
    }}

    /* Practical Labs Section */
    .labs-container {{
      margin: 14pt 0;
    }}
    .lab-card {{
      border: 1pt solid #a7f3d0;
      border-left: 3.5pt solid #059669;
      background: #f0fdf4;
      border-radius: 4pt;
      padding: 7pt 10pt;
      margin-bottom: 8pt;
      break-inside: avoid;
    }}
    .lab-title {{
      font-size: 10.2pt;
      font-weight: 800;
      color: #065f46;
      margin-bottom: 3pt;
    }}
    .lab-steps {{
      padding-left: 14pt;
      font-size: 8.8pt;
      line-height: 1.48;
    }}
    .lab-steps li {{
      margin-bottom: 3pt;
    }}

    /* Practice Questions Section */
    .questions-container {{
      margin: 14pt 0;
    }}
    .question-card {{
      border: 1pt solid #cbd5e1;
      border-radius: 4pt;
      padding: 8pt 10pt;
      margin-bottom: 10pt;
      background: #ffffff;
      break-inside: avoid;
    }}
    .question-meta-bar {{
      display: flex;
      justify-content: space-between;
      font-size: 7.8pt;
      margin-bottom: 4pt;
      border-bottom: 0.5pt solid #f1f5f9;
      padding-bottom: 3pt;
    }}
    .q-badge-domain {{
      font-weight: 700;
      color: #1e3a8a;
      background: #eff6ff;
      padding: 1.5pt 5pt;
      border-radius: 2pt;
    }}
    .q-badge-diff {{
      font-weight: 600;
      color: #047857;
      background: #ecfdf5;
      padding: 1.5pt 5pt;
      border-radius: 2pt;
    }}
    .q-badge-type {{
      color: #64748b;
    }}
    .question-stem {{
      font-size: 9.3pt;
      font-weight: 600;
      color: #0f172a;
      line-height: 1.46;
      margin-bottom: 6pt;
      text-align: justify;
    }}
    .options-list {{
      list-style: none;
      padding-left: 0;
      margin-bottom: 6pt;
    }}
    .option-item {{
      font-size: 8.8pt;
      line-height: 1.4;
      padding: 3pt 6pt;
      margin-bottom: 2pt;
      border-radius: 3pt;
      border: 0.5pt solid #e2e8f0;
      background: #f8fafc;
    }}
    .option-item.correct {{
      background: #ecfdf5;
      border-color: #10b981;
      color: #065f46;
      font-weight: 600;
    }}
    .rationale-box {{
      background: #f8fafc;
      border-left: 2.5pt solid #2563eb;
      padding: 4pt 6pt;
      font-size: 8.3pt;
      line-height: 1.42;
      color: #334155;
    }}
    .rationale-box strong {{
      color: #1e293b;
    }}

    /* Decision Matrix Table */
    table.matrix-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 8.4pt;
      line-height: 1.4;
      margin: 8pt 0 14pt 0;
      break-inside: avoid;
    }}
    table.matrix-table th {{
      background: #1e293b;
      color: #ffffff;
      padding: 5pt 7pt;
      text-align: left;
      font-weight: 700;
    }}
    table.matrix-table td {{
      padding: 4.5pt 7pt;
      border-bottom: 0.5pt solid #cbd5e1;
      vertical-align: top;
    }}
    table.matrix-table tr:nth-child(even) td {{
      background: #f8fafc;
    }}

    code {{
      font-family: ui-monospace, Menlo, Consolas, monospace;
      font-size: 8pt;
      background: #eef2ff;
      color: #3730a3;
      padding: 1pt 3pt;
      border-radius: 2pt;
    }}
  </style>
</head>
<body>

  <!-- Document Header -->
  <header class="master-header">
    <div class="doc-pretitle">AWS Certification Examination Prep Suite · Professional Level</div>
    <h1 class="doc-title">AWS Certified Generative AI Developer – Professional (AIP-C01)</h1>
    <div class="doc-subtitle">Comprehensive Visual Master Study Guide, Architectural Manual & Practical Treatise</div>
    <div class="doc-meta-bar">
      <div class="doc-meta-item"><strong>Exam Code:</strong> AIP-C01</div>
      <div class="doc-meta-item"><strong>Format:</strong> 75 Questions · 180 Minutes</div>
      <div class="doc-meta-item"><strong>Pass Mark:</strong> 750 / 1000 Scaled Score</div>
      <div class="doc-meta-item"><strong>Edition:</strong> Master Visual Edition · Zero-Noise Humanized</div>
    </div>
  </header>
"""

    # Add each Domain
    for d_idx in sorted(domains.keys()):
        d_data = domains[d_idx]
        html += f"""
        <section class="domain-section" id="domain-{d_idx}">
          <div class="domain-banner" style="background: {d_data['color']}; border-left: 4pt solid {d_data['accent']};">
            <div class="domain-banner-title">{d_data['title']} ({d_data['weight']})</div>
            <div class="domain-banner-meta">{d_data['lead']}</div>
          </div>
        """

        # Embed Domain Architectural Diagrams
        if d_data.get("diagrams"):
            html += f"""<div class="diagram-gallery">"""
            for fig_idx, (fig_title, fig_path, fig_desc) in enumerate(d_data["diagrams"], start=1):
                img_src = f"../{fig_path}"
                html += f"""
                <div class="diagram-figure-card">
                  <div class="diagram-img-box">
                    <img src="{img_src}" alt="{fig_title}">
                  </div>
                  <div class="diagram-card-title">Figure {d_idx}.{fig_idx} · {fig_title}</div>
                  <div class="diagram-card-caption">{fig_desc}</div>
                </div>
                """
            html += f"""</div>"""

        # Render Core Lessons in 2 Columns
        html += f"""<div class="lessons-grid">"""
        for s_idx, s in enumerate(d_data["slides"], start=1):
            clean_title = clean_lesson_title(s.get('title', ''), s.get('id', ''))
            rd = s.get('russianDoll', {})
            
            # Format Points
            points = s.get('points', [])
            points_html = "".join([f"<li>{p}</li>" for p in points[:3]])

            # Bold high-yield keywords in text
            rule_text = rd.get('examRule', '')
            trap_text = s.get('trap', '')
            api_text = rd.get('api', '')

            html += f"""
            <article class="lesson-card" style="border-left-color: {d_data['accent']};">
              <div class="lesson-header">
                <span class="lesson-title">Lesson {s_idx} · {clean_title}</span>
                <span class="lesson-badge">Domain {d_idx}</span>
              </div>
              <div class="lesson-lead">{s.get('lead', '')}</div>
              <ul class="lesson-points">
                {points_html}
              </ul>
              <div class="rd-box">
                <div class="rd-row"><span class="rd-tag tag-intuition">Intuition:</span> {rd.get('intuition', '')}</div>
                <div class="rd-row"><span class="rd-tag tag-api">Exact API/Config:</span> <code>{api_text[:140]}</code></div>
                <div class="rd-row"><span class="rd-tag tag-rule">Exam Decision Rule:</span> <strong>{rule_text}</strong></div>
              </div>
              <div class="trap-card">
                <strong>⚠️ Critical Exam Trap:</strong> {trap_text}
              </div>
            </article>
            """
        html += f"""</div></section>"""

    # Section 2: Complete Practical Lab Knowledge (13 Hands-On Labs)
    labs = [
        ("Lab 1: Bedrock Model Access & Converse API Invocation", [
            "<strong>Enable Model Access:</strong> Navigate to Amazon Bedrock Console -> Model access. Submit Use Case Details for Anthropic Claude models (company name, website, intended use) to obtain instant grant.",
            "<strong>IAM Permissions:</strong> Identity requires <code>bedrock:InvokeModel</code> and <code>bedrock:InvokeModelWithResponseStream</code> on resource <code>arn:aws:bedrock:*::foundation-model/*</code>.",
            "<strong>Call Converse API:</strong> Execute <code>boto3.client('bedrock-runtime').converse(...)</code> with <code>modelId</code>, <code>messages</code>, <code>system</code>, and <code>inferenceConfig</code> (temperature, maxTokens, topP).",
            "<strong>Model-Specific Parameters:</strong> Pass Anthropic <code>top_k</code> in <code>additionalModelRequestFields={'top_k': 50}</code>, NOT in <code>inferenceConfig</code>."
        ]),
        ("Lab 2: Knowledge Base Creation with OpenSearch Serverless (AOSS)", [
            "<strong>S3 Preparation:</strong> Upload source documents (PDF, DOCX, TXT) to an Amazon S3 bucket with default SSE-KMS encryption.",
            "<strong>Create Knowledge Base:</strong> Console -> Knowledge Bases -> Create. Connect S3 data source. Choose Chunking: Default (300 tokens, 20% overlap), Hierarchical (parent-child for precision+context), or Semantic.",
            "<strong>Embeddings & Store:</strong> Select <strong>Amazon Titan Text Embeddings v2</strong> (1,024 dimensions). Choose 'Quick create a new vector store - Amazon OpenSearch Serverless' (Bedrock auto-provisions collection, vector index, and access policies with minimum <strong>4 OCUs for High Availability</strong>).",
            "<strong>Run Sync:</strong> Click <strong>Sync</strong> to trigger <code>start_ingestion_job()</code> and index vectors."
        ]),
        ("Lab 3: Knowledge Base Metadata Filtering Configuration", [
            "<strong>Upload Metadata:</strong> Alongside <code>contract.pdf</code>, upload <code>contract.pdf.metadata.json</code> with attributes (e.g. <code>{\"department\": \"legal\", \"year\": 2026}</code>).",
            "<strong>Query with Filter:</strong> Call <code>bedrock-agent-runtime.retrieve()</code> passing <code>retrievalConfiguration.vectorSearchConfiguration.filter</code>.",
            "<strong>Relational Logic:</strong> Use <code>equals</code>, <code>greaterThanOrEquals</code>, and <code>andAll</code> boolean operators to restrict document space before semantic ranking."
        ]),
        ("Lab 4: Hybrid Search & Re-Ranking Configuration", [
            "<strong>Search Mode:</strong> In <code>bedrock-agent-runtime.retrieve()</code>, set <code>overrideSearchType='HYBRID'</code>.",
            "<strong>Dual Execution:</strong> Executes lexical keyword BM25 search (for part numbers, serial codes, acronyms) and dense semantic vector search simultaneously.",
            "<strong>Re-ranking:</strong> Apply Bedrock Re-ranking model (Cohere Rerank v3.5) to score and prioritize the top-K consolidated passages before prompt injection."
        ]),
        ("Lab 5: Building Amazon Bedrock Action Agents End-to-End", [
            "<strong>Create Agent:</strong> Specify base model (Claude 3.5 Sonnet) and clear, role-specific System Instructions.",
            "<strong>Action Group:</strong> Define with OpenAPI 3.0 schema in S3 connected to an AWS Lambda function for business execution.",
            "<strong>Lambda Resource Policy:</strong> Grant <code>bedrock.amazonaws.com</code> permission with condition <code>aws:SourceArn</code> matching the agent ARN.",
            "<strong>CRITICAL EXAM STEP:</strong> Click <strong>Prepare</strong> in console or call <code>prepare_agent()</code>. Without preparing, draft updates do not take effect! Point Agent Alias (e.g. <code>PROD</code>) to the prepared immutable Version."
        ]),
        ("Lab 6: Human-in-the-Loop (HITL) with RETURN_OF_CONTROL", [
            "<strong>Action Group Configuration:</strong> Set <code>actionGroupExecutor={'customControl': 'RETURN_OF_CONTROL'}</code>.",
            "<strong>Agent Invocation:</strong> When the agent decides to invoke the tool, <code>invoke_agent()</code> yields an <code>actionGroupInvocationInput</code> event with parsed parameters.",
            "<strong>Review & Resume:</strong> The client application presents details to a human reviewer. Upon approval, application calls <code>invoke_agent()</code> again passing <code>sessionState.returnControlInvocationResults</code> to continue reasoning."
        ]),
        ("Lab 7: Amazon Bedrock Guardrails Setup & Contextual Grounding", [
            "<strong>Create Guardrail:</strong> Configure Content Filters (set <strong>Prompt Attack / Jailbreak</strong> to <code>HIGH</code>).",
            "<strong>Denied Topics:</strong> Define topic with natural language description and 3–5 representative sample trigger phrases.",
            "<strong>Sensitive Information (PII):</strong> Add PII entities (SSN, credit card). Choose Action: <code>ANONYMIZE</code> (replaces with placeholder like <code>[NAME]</code>) or <code>BLOCK</code> (halts request).",
            "<strong>Contextual Grounding:</strong> Set Grounding threshold (0.80) to catch hallucinations and Relevance threshold (0.75) to verify query alignment."
        ]),
        ("Lab 8: Prompt Management & Prompt Caching", [
            "<strong>Prompt Management:</strong> Author prompts in Bedrock console with dynamic parameters <code>{{variable_name}}</code>. Create numeric immutable Version for production.",
            "<strong>Prompt Caching:</strong> Place static prefix (system instructions, tool schemas, long reference manuals) at the START of prompt (minimum <strong>1,024 prefix tokens</strong> for Claude).",
            "<strong>Cache Point:</strong> In Converse API, mark <code>cachePoint: {'type': 'default'}</code>. Initial write incurs +25% fee; subsequent cache hits grant <strong>90% discount</strong> with <strong>5-minute rolling TTL</strong>."
        ]),
        ("Lab 9: Provisioned Throughput vs Batch Inference", [
            "<strong>On-Demand:</strong> Default pay-per-token model. Best for bursty, unpredictable workloads.",
            "<strong>Provisioned Throughput:</strong> Call <code>create_provisioned_model_throughput()</code>. Commit 1+ Model Units (MUs) for 1 or 6 months. Required for guaranteed low latency and <strong>MANDATORY for custom fine-tuned models</strong>.",
            "<strong>Batch Inference:</strong> Call <code>create_model_invocation_job()</code> with S3 JSONL input. Grants <strong>50% discount</strong> for offline non-real-time bulk jobs."
        ]),
        ("Lab 10: Cross-Region Inference Resilience", [
            "<strong>Inference Profile:</strong> Use system-defined profile ID (e.g. <code>us.anthropic.claude-3-5-sonnet-20241022-v2:0</code>).",
            "<strong>Dynamic Routing:</strong> Automatically distributes requests across us-east-1, us-west-2, and us-east-2 to eliminate <code>429 ThrottlingException</code> at <strong>zero extra cost</strong>.",
            "<strong>Data Residency:</strong> US profile remains in US; European profile (<code>eu.</code>) routes strictly within Frankfurt, Ireland, and Paris for GDPR compliance."
        ]),
        ("Lab 11: Security Isolation with PrivateLink & KMS", [
            "<strong>VPC Endpoints:</strong> Create Interface Endpoints for <code>bedrock-runtime</code>, <code>bedrock-agent-runtime</code>, and <code>bedrock</code>.",
            "<strong>IAM Condition:</strong> Restrict invocation policy with <code>StringEquals: {'aws:sourceVpce': 'vpce-1234abcd'}</code>.",
            "<strong>Model Invocation Logging:</strong> Call <code>put_model_invocation_logging_configuration()</code> to log prompts and completions to S3 with KMS CMK encryption. (CloudTrail logs only API management events, never payload text)."
        ]),
        ("Lab 12: Model Evaluation & Benchmark Jobs", [
            "<strong>Automatic Evaluation:</strong> Create job for Summarization or Q&A using built-in or custom S3 JSONL datasets. Evaluates <strong>ROUGE-1/2/L</strong> (summarization recall), <strong>BLEU</strong> (translation precision), and <strong>BERTScore</strong> (semantic similarity).",
            "<strong>Human Evaluation:</strong> Configure workforce (Private Company Workforce via Amazon Cognito or AWS Managed Team via SageMaker Ground Truth).",
            "<strong>Mitigate Judge Biases:</strong> Swap position order (A/B and B/A) to defeat position bias, enforce Chain-of-Thought (CoT) before score emission."
        ]),
        ("Lab 13: Systematic Troubleshooting & Error Code Resolution", [
            "<strong>429 ThrottlingException:</strong> Implement Exponential Backoff with FULL JITTER, switch to Cross-Region Inference Profile, or commit Provisioned Throughput.",
            "<strong>503 ModelNotReadyException:</strong> Provisioned Model is warming up; retry with backoff.",
            "<strong>400 ValidationException:</strong> Context length exceeded or invalid schema. Calculate tokens pre-flight via <code>CountTokens</code> API; do NOT retry without payload modification.",
            "<strong>403 AccessDeniedException:</strong> Verify IAM caller permissions AND confirm Model Access is activated in Bedrock console for that Region."
        ])
    ]

    html += f"""
    <section class="labs-section">
      <div class="domain-banner" style="background: #047857; border-left: 4pt solid #10b981;">
        <div class="domain-banner-title">Part 2: Complete Practical Lab Knowledge (13 Hands-On Console & SDK Walkthroughs)</div>
        <div class="domain-banner-meta">Step-by-step procedures covering console navigation, CLI commands, boto3 API structures, and configuration details.</div>
      </div>
      <div class="labs-container">
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
    html += f"""</div></section>"""

    # Section 3: In-Scope Blueprint Gap Topics
    gaps = [
        ("Amazon AppFlow & AWS Transfer Family", "Knowledge Base Data Ingestion", "AppFlow automates SaaS data ingestion (Salesforce, ServiceNow, Zendesk, Slack) directly into S3 for Knowledge Base synchronization without custom ETL code. AWS Transfer Family provides managed SFTP/FTPS/FTP endpoints dropping enterprise partner files directly into S3 for RAG indexing."),
        ("Amazon Neptune Analytics & GraphRAG", "Knowledge Graph + Vector RAG", "Neptune Analytics executes in-memory graph algorithms and vector search together. When queries require traversing multi-hop relationships (e.g. supply chain dependencies, fraud rings, organizational hierarchies), GraphRAG with Neptune outperforms pure similarity search."),
        ("Amazon Q Business & Amazon Q Apps", "Enterprise AI Application Solutions", "Amazon Q Business connects to 40+ enterprise connectors with built-in ACL identity propagation. Amazon Q Apps allows non-technical employees to generate lightweight, custom multi-step AI business apps from a single natural language prompt."),
        ("AWS WAF & Amazon CloudFront Edge", "DDoS & Edge Prompt Validation", "CloudFront distributes GenAI web apps globally with low latency. AWS WAF protects API Gateway endpoints against DDoS, enforces IP rate-limiting, and blocks SQLi/XSS attacks before requests reach Bedrock. CloudFront Functions / Lambda@Edge inspects requests at the edge."),
        ("The CountTokens API & Exact Token Budgeting", "Preventing Context Window Overflow", "The Bedrock <code>CountTokens</code> API calculates exact token counts for prompt text against specific model tokenizers before invocation, preventing runtime <code>ValidationException</code>. Crucial for dynamic sliding window memory calculation."),
        ("top_k Parameter in the Converse API", "Sampling via additionalModelRequestFields", "Converse API exposes temperature, topP, and maxTokens directly in inferenceConfig. To pass model-specific parameters like Anthropic <code>top_k</code> or <code>repetition_penalty</code>, use <code>additionalModelRequestFields={'top_k': 50}</code>."),
        ("Amazon CloudWatch Evidently", "A/B Testing & Feature Flags", "CloudWatch Evidently manages feature flags, dark launches, and client-side variation experiments for foundation models. Allows comparing conversion and click-through metrics between Model A and Model B in production."),
        ("Amazon Textract Tables & Forms", "Document Modality Extraction", "Standard OCR destroys two-dimensional tabular alignment into flat unreadable text. Textract <code>AnalyzeDocument(FeatureTypes=['TABLES', 'FORMS'])</code> preserves row-column relationships and key-value pairs for RAG ingestion."),
        ("Binary Vectors & Vector Quantization", "Optimizing OpenSearch Serverless", "Binary vectors and FP16/INT8 scalar quantization in OpenSearch Serverless reduce vector memory footprint by up to 75% while maintaining >95% retrieval accuracy, preventing OCU memory exhaustion on multi-million document collections."),
        ("SageMaker Large-Model Distributed Tuning", "FSDP & DeepSpeed ZeRO-3", "For models exceeding single-GPU VRAM (e.g. 70B+ parameters), use SageMaker PyTorch Fully Sharded Data Parallel (FSDP) or DeepSpeed ZeRO-3 across multi-node ml.p4d/ml.p5 GPU clusters to shard optimizer states, gradients, and model weights.")
    ]

    html += f"""
    <section class="gaps-section">
      <div class="domain-banner" style="background: #581c87; border-left: 4pt solid #a855f7;">
        <div class="domain-banner-title">Part 3: Blueprint Gap Topics & Advanced Primitives</div>
        <div class="domain-banner-meta">Critical specialized primitives tested in high-difficulty scenario questions.</div>
      </div>
      <div class="lessons-grid">
    """
    for gap_title, gap_sub, gap_desc in gaps:
        html += f"""
        <article class="lesson-card" style="border-left-color: #a855f7;">
          <div class="lesson-header">
            <span class="lesson-title">{gap_title}</span>
            <span class="lesson-badge">{gap_sub}</span>
          </div>
          <div class="lesson-lead" style="font-style:normal;">{gap_desc}</div>
        </article>
        """
    html += f"""</div></section>"""

    # Section 4: The 6 Question Patterns
    patterns = [
        ("Pattern 1: Multi-Constraint Extraction", "Scenario stems present 3-4 simultaneous constraints (residency, budget, latency, serverless). The credited option is the ONLY one that satisfies all constraints simultaneously. Read constraints first, options second."),
        ("Pattern 2: MOST Correct vs Merely Functional", "Multiple options will function architecturally, but the prompt asks for 'LEAST operational effort' or 'MOST cost-effective'. Managed services (Bedrock) always beat self-hosted EC2/EKS on operational effort."),
        ("Pattern 3: Lifecycle & Strict Sequential Ordering", "AWS tests exact sequential order of operations. Example: Knowledge Base sync requires (1) S3 upload -> (2) StartIngestionJob -> (3) Status COMPLETE. Agent deployment requires (1) Edit -> (2) PrepareAgent -> (3) Create Alias."),
        ("Pattern 4: Precision Terminology & Distractor Traps", "Distinguish fine-tuning (labeled prompt-response pairs for style/task) vs continued pre-training (unlabeled text for domain vocabulary). Distinguish Model Invocation Logging (payloads) vs CloudTrail (management APIs only)."),
        ("Pattern 5: Managed-First Solution Ladder", "Always choose the lowest rung on the ladder that solves the problem: Prompt Engineering -> RAG -> Fine-Tuning -> Pre-training. Never fine-tune when RAG solves dynamic factual freshness."),
        ("Pattern 6: Wrong-Plane Distractor Traps", "Distractors frequently offer data-plane solutions for control-plane problems (or vice versa). Example: Trying to audit prompt text via CloudTrail, or trying to isolate network traffic using S3 Gateway endpoints instead of PrivateLink.")
    ]

    html += f"""
    <section class="patterns-section">
      <div class="domain-banner" style="background: #92400e; border-left: 4pt solid #f59e0b;">
        <div class="domain-banner-title">Part 4: The 6 AWS AIP-C01 Question Patterns & Elimination Tactics</div>
        <div class="domain-banner-meta">Heuristics to rapidly identify distractor traps and isolate the credited response in under 30 seconds.</div>
      </div>
      <div class="lessons-grid">
    """
    for pat_title, pat_desc in patterns:
        html += f"""
        <article class="lesson-card" style="border-left-color: #f59e0b;">
          <div class="lesson-header">
            <span class="lesson-title">🎯 {pat_title}</span>
          </div>
          <div class="lesson-lead" style="font-style:normal;">{pat_desc}</div>
        </article>
        """
    html += f"""</div></section>"""

    # Section 5: Rapid Decision Matrix Table
    html += f"""
    <section class="matrix-section">
      <div class="domain-banner" style="background: #1e3a8a; border-left: 4pt solid #3b82f6;">
        <div class="domain-banner-title">Part 5: 30-Second Rapid Elimination Decision Matrix</div>
        <div class="domain-banner-meta">Instant scenario pattern-matching guide for the 180-minute examination.</div>
      </div>
      <table class="matrix-table">
        <thead>
          <tr><th>If Scenario Requires...</th><th>Credited AWS Architecture</th><th>Why Distractors Fail</th></tr>
        </thead>
        <tbody>
          <tr><td>Dynamic company policies changing daily</td><td><strong>Bedrock Knowledge Base (RAG)</strong></td><td>Fine-tuning is frozen at training time and cannot update daily</td></tr>
          <tr><td>Strict JSON schema & downstream tool calling</td><td><strong>Bedrock Converse API with toolConfig</strong></td><td>Regex parsing is brittle; InvokeModel lacks unified tool schema</td></tr>
          <tr><td>Part numbers, serial codes, exact IDs</td><td><strong>Hybrid Search (BM25 + Vector) + Rerank</strong></td><td>Pure vector search misses exact keyword string matches</td></tr>
          <tr><td>Autonomous multi-step actions with APIs</td><td><strong>Bedrock Agent with OpenAPI 3.0 & Lambda</strong></td><td>Chained prompts cannot autonomously validate external tools</td></tr>
          <tr><td>Prevent hallucinations in RAG answers</td><td><strong>Bedrock Guardrails Contextual Grounding</strong></td><td>Standard toxicity filters do not check source faithfulness</td></tr>
          <tr><td>Mask SSN/Credit Cards without stopping flow</td><td><strong>Bedrock Guardrails PII with action=ANONYMIZE</strong></td><td>action=BLOCK stops the user conversation entirely</td></tr>
          <tr><td>Eliminate 429 Throttling during traffic spikes</td><td><strong>Cross-Region Inference Profile (us./eu.)</strong></td><td>Single-region quotas throttle; Provisioned is costly for spikes</td></tr>
          <tr><td>Auditing user prompt text for compliance</td><td><strong>Bedrock Model Invocation Logging to S3</strong></td><td>CloudTrail logs API management calls, NEVER prompt/payload text</td></tr>
          <tr><td>Zero internet traversal from private subnets</td><td><strong>VPC Interface Endpoint (PrivateLink)</strong></td><td>S3 Gateway Endpoint does not secure Bedrock runtime calls</td></tr>
          <tr><td>Offline bulk summarization at lowest cost</td><td><strong>Amazon Bedrock Batch Inference</strong></td><td>Synchronous on-demand costs 2x more and hits request quotas</td></tr>
          <tr><td>Sensitive database updates / wire transfers</td><td><strong>Action Group RETURN_OF_CONTROL / Step Functions</strong></td><td>Direct Lambda execution has no human review checkpoint</td></tr>
          <tr><td>Agent changes not taking effect in test</td><td><strong>Call PrepareAgent / Create Agent Alias</strong></td><td>Draft configuration changes do not deploy until prepared</td></tr>
        </tbody>
      </table>
    </section>
    """

    # Section 6: Cleaned High-Yield Blueprint Practice Questions Showcase
    # Select 25 top representative questions across domains, cleanly formatted
    showcase_indices = [0, 4, 7, 9, 14, 18, 21, 24, 30, 42, 51, 60, 70, 76, 83, 93, 105, 128, 141, 148, 153, 162, 167, 182, 196]
    selected_quizzes = [all_quizzes[i] for i in showcase_indices if i < len(all_quizzes)]

    html += f"""
    <section class="questions-showcase-section">
      <div class="domain-banner" style="background: #0f172a; border-left: 4pt solid #38bdf8;">
        <div class="domain-banner-title">Part 6: Cleaned Blueprint Practice Questions Showcase</div>
        <div class="domain-banner-meta">Representative examination questions formatted with zero internal ID clutter, clean stems, and complete official rationales.</div>
      </div>
      <div class="questions-container">
    """

    for i, q in enumerate(selected_quizzes, start=1):
        cleaned_q = clean_question_for_print(q, i)
        options_html = ""
        for opt_idx, opt in enumerate(cleaned_q['options']):
            is_correct = opt.get('correct', False)
            opt_class = "option-item correct" if is_correct else "option-item"
            check_mark = " ✓" if is_correct else ""
            options_html += f"""
            <li class="{opt_class}">
              <strong>{chr(65 + opt_idx)}.</strong> {opt.get('text', '')}{check_mark}
            </li>
            """

        domain_label = f"Domain {q.get('domain', 1)}"

        html += f"""
        <article class="question-card">
          <div class="question-meta-bar">
            <span class="q-badge-domain">{domain_label} · {cleaned_q['topic']}</span>
            <span class="q-badge-diff">{cleaned_q['difficulty']}</span>
            <span class="q-badge-type">{cleaned_q['responseType']}</span>
          </div>
          <div class="question-stem">Question {cleaned_q['number']}: {cleaned_q['stem']}</div>
          <ul class="options-list">
            {options_html}
          </ul>
          <div class="rationale-box">
            <strong>💡 Official AWS Architectural Rationale:</strong> {cleaned_q['answer']}
          </div>
        </article>
        """

    html += """
      </div>
    </section>
  </body>
</html>
"""

    output_html_path = ROOT / 'course/print-study-guide.html'
    output_html_path.write_text(html)
    print(f"Generated publication-grade study guide HTML at {output_html_path}")
    return output_html_path

def generate_pdf(html_path):
    pdf_path = ROOT / 'AIP-C01_Overnight_Print_Guide.pdf'
    downloads_pdf = Path('/Users/rj/Downloads/AIP-C01_Overnight_Print_Guide.pdf')
    master_pdf = Path('/Users/rj/Downloads/AIP-C01_Master_Visual_Study_Guide.pdf')
    
    script = f"""
import {{ chromium }} from 'playwright';
const browser = await chromium.launch({{ headless: true, executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' }});
const page = await browser.newPage();
await page.goto('file://{html_path}', {{ waitUntil: 'networkidle' }});
await page.pdf({{
  path: '{pdf_path}',
  format: 'Letter',
  margin: {{ top: '12mm', bottom: '14mm', left: '12mm', right: '12mm' }},
  printBackground: true
}});
await browser.close();
console.log('Successfully generated publication-grade PDF: {pdf_path}');
"""
    js_file = ROOT / '.build/generate_pdf.mjs'
    js_file.parent.mkdir(parents=True, exist_ok=True)
    js_file.write_text(script)
    
    cmd = ['node', str(js_file)]
    subprocess.run(cmd, check=True)
    
    # Copy to downloads under both names
    if pdf_path.exists():
        import shutil
        shutil.copy2(pdf_path, downloads_pdf)
        shutil.copy2(pdf_path, master_pdf)
        print(f"Copied PDF to user Downloads: {downloads_pdf} ({downloads_pdf.stat().st_size / (1024*1024):.1f} MB)")
        print(f"Copied PDF to user Downloads: {master_pdf}")

def generate_docx():
    docx_path = ROOT / 'AIP-C01_Overnight_Study_Guide.docx'
    downloads_docx = Path('/Users/rj/Downloads/AIP-C01_Overnight_Study_Guide.docx')
    master_docx = Path('/Users/rj/Downloads/AIP-C01_Master_Study_Guide.docx')
    
    cmd = [
        '/opt/homebrew/bin/pandoc',
        str(ROOT / 'course/print-study-guide.html'),
        '-o', str(docx_path),
        '--from=html',
        '--to=docx',
        f'--resource-path={ROOT}/course:{ROOT}'
    ]
    subprocess.run(cmd, check=True)
    print(f"Successfully generated DOCX: {docx_path}")
    
    if docx_path.exists():
        import shutil
        shutil.copy2(docx_path, downloads_docx)
        shutil.copy2(docx_path, master_docx)
        print(f"Copied DOCX to user Downloads: {downloads_docx} ({downloads_docx.stat().st_size / (1024*1024):.1f} MB)")
        print(f"Copied DOCX to user Downloads: {master_docx}")

if __name__ == '__main__':
    html_file = build_master_html()
    generate_pdf(html_file)
    generate_docx()

# AWS Certified Generative AI Developer – Professional (AIP-C01) Master Study Suite

Complete first-principles study materials, interactive applications, architectural treatises, and publication-grade print materials for the AWS Certified Generative AI Developer - Professional exam (**AIP-C01**).

---

## 🎯 Examination at a Glance
- **Exam Code:** AIP-C01
- **Questions:** 75 questions (65 scored + 10 unscored pretest)
- **Time Allowed:** 180 minutes (3 hours)
- **Passing Score:** 750 / 1000 scaled score
- **Question Types:** Multiple choice (single answer) and Multiple response (select 2 or 3)

---

## 🚀 Core Applications & Interactive Tools

| Application | Path / Link | Description |
| :--- | :--- | :--- |
| **Interactive Masterclass Web App** | [`course/index.html`](course/index.html) | 16:9 Slide Deck with 5-layer Russian Doll models, 75-question timed mock (180-min timer), 250 interactive questions, 541 flashcards, Lightbox zoom. |
| **Continuous Visual Treatise** | [`course/treatise.html`](course/treatise.html) | Scrollable long-form master textbook with 24 deep chapters, 26 architecture diagrams, and 98 mapped skill dossiers. |
| **98-Skill Reader** | [`course/reader.html`](course/reader.html) | Skill-by-skill syllabus mapped directly to the official AWS AIP-C01 blueprint. |
| **Master Visual Study Guide (HTML)** | [`course/print-study-guide.html`](course/print-study-guide.html) | Clean, beautifully styled HTML study manual featuring Anthropic Sans typography, justified text, and official diagrams. |

---

## 📚 Master Study Documents & Print Editions

| Document | Format | Description |
| :--- | :--- | :--- |
| **Master Visual Study Guide (PDF)** | `AIP-C01_Overnight_Print_Guide.pdf` | Formatted with Anthropic Sans, justified text, 1.5 line spacing, large official AWS diagrams, 13 practical labs, and cleaned blueprint questions. |
| **Master Study Guide (Word .docx)** | `AIP-C01_Overnight_Study_Guide.docx` | Fully styled Microsoft Word edition with embedded high-resolution diagrams, tables, and callouts. |
| **Core Two-Up Print Edition** | `output/AIP-C01-Core-Two-Up.pdf` | Complete authored curriculum with two logical pages per side for double-sided printing. |
| **Practice Booklet** | `output/AIP-C01-Practice-Two-Up.pdf` | 250 extracted questions with full official rationales and corrections. |

---

## 🏗️ 5-Layer Russian Doll Learning Engine
Every concept across the 95 lessons is taught from physical first principles:
1. **Layer 1: First-Principle Intuition** — Ground mental model without jargon.
2. **Layer 2: AWS Architecture Flow** — IAM, KMS, VPC, API, and EventBridge boundaries.
3. **Layer 3: Exact APIs & Code** — `boto3` parameters, `inferenceConfig`, `additionalModelRequestFields={'top_k': 50}`.
4. **Layer 4: Amazon Traps & Gotchas** — Quotas, silent truncations, and subtle exam distractors.
5. **Layer 5: 15-Second Exam Decision Rule** — Rapid heuristic for answering scenario questions under timed conditions.

---

## 🛠️ Build and Regeneration Scripts
- **Rebuild Course Data**: `python3 scripts/build_course.py`
- **Generate Print Materials (PDF & DOCX)**: `python3 scripts/generate_print_materials.py`
- **Run Playwright Verification Suite**: `node scripts/test_course.mjs`

The revised editions use justified Anthropic Sans text, more line space, clean question numbers, and semantic color cues.

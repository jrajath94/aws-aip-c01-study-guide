# AIP-C01 Writer Brief (shared by all volume writers)

## What you are building
Study volumes for the AWS Certified Generative AI Developer – Professional (AIP-C01) exam.
The learner is a visual learner with ADHD studying 4+ hours/day, strong software engineer, assumed ZERO prior AWS GenAI knowledge.

## Source of truth
Read `~/workspace/your_files/aws-aip-c01-cert/EXAM-BLUEPRINT.md` first. It lists every topic for your domain, how AWS asks about it, and the trap patterns. Cover EVERY topic it lists for your volume. Nothing may be dropped.

## Depth rule (mandatory)
Every topic must contain ALL of:
1. What it is — plain words, from zero. Define every term on first use. Expand every acronym on first use.
2. Why it exists — the problem it solves, what fails without it.
3. How it works under the hood — step-by-step mechanics, no hand-waving.
4. Concrete numbers or a worked example — real limits, quotas, defaults, pricing math, latency numbers, a traced example. If a number is unverifiable, label it "illustrative".
5. Common misunderstanding — the trap AWS exploits, stated explicitly.
6. A visual — diagram with a "How to read this diagram" walkthrough (numbered steps tracing the figure in order, per-component meaning, what breaks if a component fails).
7. "How AWS asks this" — exam-relevance line: the question style, the scenario framing, the distractor AWS will offer.

Potent, not padded. High signal density, short plain sentences, simple words. No fluff, but never sacrifice depth.

## Visual style (must match the existing library)
- Single self-contained HTML file. No external fonts, stylesheets, scripts, or hotlinked images. Everything base64-inlined or inline CSS. Must open fully offline.
- Reuse this palette: paper #F8F7F3, ink #24292F, muted #5C6570, blue #1F5FBF, board #163D7A, amber #A15C07, card #FFFFFF, codebg #EFF0EA, rule #E3E0D8. Flat colors only. NO gradients anywhere.
- Layout: sticky left rail with chapter nav, main column max-width ~72ch. See `~/workspace/your_files/rrk-prep/v2/RRK_Agentic_AI_Textbook_v2.html` for the exact CSS family. Clean, minimal, no AI slop.
- Zero em dashes (—) anywhere in the file. No emojis in prose.

## Diagrams (mandatory, one per topic minimum)
Priority: (1) internet-sourced AWS architecture diagrams — fetch with `/opt/hatch/bin/image-search "<query>" --max-results 5`, download the media_url with curl, verify it decodes (Pillow), credit the source site in the caption, embed as base64 data URI. (2) Generated with `~/workspace/skills/openrouter/bin/gen_image.py --model meta/muse-image` using deep concrete prompts, flat minimal style, minimal text in the image. Compress to max 1400px wide before embedding. (3) ASCII diagrams in styled `<pre>` blocks as the guaranteed fallback — welcome everywhere.
Every significant figure gets the "How to read this diagram" walkthrough directly under it.
Never hotlink images. Never put key material in prompts, logs, or files.

## Questions
Your volume ends with a per-topic question set: easy, medium, and hard questions, BOTH multiple-choice (one answer) and multiple-response (select all that apply / select TWO), 4 plausible options each, written in AWS's "choose the MOST correct answer" style with scenario framing. Every question explains why the correct answer is right AND why each distractor is wrong.

## Stephane Maarek style
For every service/feature: "here is the service, here is how AWS will ask about it on the exam, here is the trap." Explicit trap callouts per topic.

## Content rules
- GENERIC content only. No names, no employers, no personal identifiers. This reads as pure learning material (it will be copied to an office laptop).
- No invented facts, quotes, or statistics. Unverifiable numbers are labeled illustrative.
- No placeholders: no lorem ipsum, no TODO, no "coming soon", no empty sections.
- Collapsible `<details>` sections are welcome to keep the surface scannable.

## Before you finish (QA)
- Parse-check HTML (balanced tags), unique ids, zero em dashes, zero gradients, every img is a data URI that decodes, internal anchors resolve, no placeholders, every topic has a visual + walkthrough + the seven depth elements.
- Write your volume to `~/workspace/your_files/aws-aip-c01-cert/<your-assigned-filename>.html` and report: filename, topic count, image count, QA checklist results (what passed, what is open).

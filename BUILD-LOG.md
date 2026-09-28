# AIP-C01 Study Guide — Build Log

Built: 2026-09-28. Coordinator: AWS certification coordinator. Track: aws-aip-c01-cert.

## Pipeline
1. Research worker produced EXAM-BLUEPRINT.md (6,177 words): verified exam facts (75 questions, 65 scored + 10 unscored, 180 min, $300, pass 750/1000, Pearson VUE, MC + multiple response + ordering + matching, compensatory scoring, domain weights 31/26/20/12/11 from the official exam guide), question-style guidance, cross-cutting decision ladders, all 5 domains with "what AWS tests / how AWS asks / trap patterns" per topic, 15-item master trap list, sources consulted.
2. WRITER-BRIEF.md written: shared rules for all volume writers (zero-to-one, depth rule, visual treatise, Maarek style, generic content, QA checklist).
3. 7 writer workers fanned out in parallel: 5 domain volumes, question bank, system design guide. Each read the blueprint and brief; each ran QA before handoff.
4. Coordinator assembly: index.html (study guide home page, domain-weighted, suggested 14-day study plan).
5. Labs volume worker mined the Maarek course lab files into volume-maarek-labs.html (9 guided lab chapters, all 41 labs mapped in COVERAGE-MAP.md).
6. Question-patterns worker analyzed public sample questions and wrote volume-question-patterns.html (81 ORIGINAL questions in all 4 exam formats + pattern guide). No source text copied.
7. Completionist worker wrote volume-appendix-gaps.html (17 peripheral topics, 18 figures, 17 questions) closing every gap from the three-way coverage check.
8. Two independent fact-check verifiers checked all volumes against live AWS docs (2026-09-28): ~140 claims. Real errors fixed: nonexistent au./jp. inference prefixes removed (D4), eval JSONL key corrected to referenceResponse (D5), Automated Reasoning checks corrected to detect-only (D3). "Last verified: 2026-09-28" banners added. Distractor audit of 1,001 options: zero fictional services. Honest UNVERIFIED markers only where a claim could not be confirmed.
9. Design-system update (user directive): DESIGN-SYSTEM.md codified the Hallmark pitch-black dark mode spec; 3 restyle workers converted all 11 HTML files (exact tokens, sidebar with scroll-spy/search/checkmarks/progress/keyboard/mobile drawer, learning components, print stylesheet, accessibility gates). Content diff-verified byte-identical; QA re-run on every file.
10. Watermark cleaning: wm_clean.py Layer A over all final HTML files (details below).
11. Zip packaging: aws-aip-c01-study-guide.zip (zip first, per user delivery order).
12. GitHub: publish to private repo aws-aip-c01-study-guide via the github skill (bin/gh_publish.py), private only.

## Deliverables
| File | Size | Contents |
|---|---|---|
| index.html | 31 KB | Study guide home page, study order, exam facts, links to all volumes |
| volume-d1-foundation-models.html | 1.3 MB | Domain 1 (31%): 18 topics, diagrams, 108 questions |
| volume-d2-implementation-integration.html | 1.2 MB | Domain 2 (26%): 15 topics, 20 figures, 90 questions + 20-item trap list |
| volume-d3-safety-security-governance.html | 0.9 MB | Domain 3 (20%): 10 topics, figures, 60 questions + cheat sheet + glossary |
| volume-d4-optimization.html | 2.6 MB | Domain 4 (12%): 13 topics, 14 figures, 78 questions |
| volume-d5-testing-validation.html | 2.2 MB | Domain 5 (11%): 12 topics, 12 figures, 36 questions |
| volume-question-bank.html | 0.3 MB | 140 questions exam-weighted + 75-question mock exam + answer key + scoring guide |
| volume-question-patterns.html | 0.2 MB | 81 original questions (MC/MR/ordering/matching) + "how AWS asks" pattern guide + 15-trap catalog |
| volume-system-design.html | 1.5 MB | 8 end-to-end designs, 4 embedded + 13 ASCII diagrams, 24 questions |
| volume-maarek-labs.html | 0.1 MB | 9 hands-on lab chapters from the Maarek course labs, 9 practice questions |
| volume-appendix-gaps.html | 0.1 MB | 17 peripheral topics (AppFlow, Transfer Family, QuickSight, Neptune Analytics, Q Apps, etc.), 18 figures, 17 questions |
| EXAM-BLUEPRINT.md | 47 KB | Research: verified facts, per-topic exam notes, trap lists |
| COVERAGE-MAP.md | 16 KB | Three-way completeness proof (exam weights, Maarek topics, all 41 labs) |
| DESIGN-SYSTEM.md | 4 KB | Shared Hallmark dark-mode design spec |
| BUILD-LOG.md | — | This file |

Totals: ~460 original practice questions (108+90+60+78+36 in domain volumes, 140+81 in banks, 24 in system design, 9 labs, 17 appendix; some overlap by design), 100+ figures, all self-contained HTML (offline-capable, no external deps).

## QA summary
- Each writer ran the shared QA checklist (balanced tags, unique ids, zero em dashes, zero gradients, data-URI images that decode, anchors resolve, no placeholders, per-topic 7 depth elements + visual + walkthrough, generic content only). All reported PASS with nothing open.
- Coordinator spot checks: zero em dashes across all volumes (grep), zero gradient references (grep), zero external http src/href in HTML (grep). Passed.
- Fact verification (2026-09-28): two independent verifiers, ~140 claims checked against live AWS docs; 3 real errors fixed in place; UNVERIFIED markers used honestly where needed; 1,001 distractor options scanned, zero fictional services.
- Restyle QA: all 11 files re-checked after the dark-theme conversion (tag balance, unique ids, anchors resolve, single h1, no skipped levels, print stylesheet, focus states, images decode). Content diff-verified identical.
- Watermark cleaning: Layer A run over all final HTML files; see per-file results below.

## Watermark cleaning results (2026-09-28, final pass)
wm_clean.py Layer A over all 11 HTML files: all exit 0. Ten files byte-identical after cleaning (no marks present). One file changed: volume-system-design.html had Adobe XMP metadata embedded in one base64 PNG (an AWS marketing image); the cleaner stripped it and the cleaned copy was promoted as canonical; the PNG was verified to still decode in PIL with XMP gone. No invisible Unicode found in any file. All *.cleaned.html scratch copies removed.

## Known limitations
- Volatile numbers (Bedrock pricing, some service defaults/limits) are labeled "illustrative" throughout; principles are taught first. Learner should check AWS docs for current values.
- Some figures are model-generated ("Generated diagram" credited in captions) rather than AWS-official diagrams; captions credit internet-sourced diagrams where used.
- Content is generic learning material only: no personal identifiers anywhere (verified by scan; "raj" hits were base64 image-data coincidences).
- D4's lite-model worked pricing example uses retired Claude 3 Haiku rates, explicitly labeled illustrative; current Haiku 4.5 global rates are $1.00/$5.00 per 1M. Flagged to the learner in the parent report.

## AUDIT-REPORT: Professional-Bar Question-Bank Audit (2026-09-28)

**Auditor:** QUESTION-BANK PROFESSIONAL-BAR AUDITOR subagent. **File:** volume-question-bank.html.

**Audit method.** All 140 stems extracted and graded against the professional bar from QUESTION-PATTERNS-RESEARCH.md (20 real-exam patterns: no single-fact "which service does X" softballs, multi-constraint scenario stems, plausible-but-wrong distractors, signature polarity traps). Pre-audit mix: 58 EASY / 54 MEDIUM / 28 HARD. **55 questions failed the bar** (pure trivia or single-fact stems with no scenario constraints) and were rewritten. Post-audit mix: 8 EASY / 137 MEDIUM / 47 HARD.

**55 questions rewritten in place (same ids, same Q numbers, same correct letters; mock-exam links and 75-row answer key verified byte-consistent after the change):**
- D1 (15): q-d1-006, q-d1-008, q-d1-011, q-d1-015, q-d1-016, q-d1-018, q-d1-019, q-d1-021, q-d1-025, q-d1-026, q-d1-027, q-d1-032, q-d1-034, q-d1-038, q-d1-040
- D2 (18): q-d2-001, q-d2-002, q-d2-004, q-d2-005, q-d2-008, q-d2-013, q-d2-015, q-d2-016, q-d2-018, q-d2-020, q-d2-021, q-d2-023, q-d2-026, q-d2-027, q-d2-032, q-d2-033, q-d2-034, q-d2-035
- D3 (11): q-d3-001, q-d3-002, q-d3-003, q-d3-008, q-d3-011, q-d3-013, q-d3-014, q-d3-018, q-d3-019, q-d3-024, q-d3-027
- D4 (6): q-d4-001, q-d4-004, q-d4-006, q-d4-008, q-d4-013, q-d4-015
- D5 (5): q-d5-001, q-d5-002, q-d5-003, q-d5-009, q-d5-011
- All 55 kept their original format (ONE ANSWER) and correct letter (A). Mock-table Type labels for the 31 rewritten questions that appear in the mock exam were updated to match the new difficulty. Rewrites verified: no em dashes, no external URLs, no fictional services, per-distractor "why wrong" notes preserved.

**52 new professional-bar questions added (Q141-Q192, new section "Bonus Professional-Bar Practice Questions" before the mock exam; ids q-d1-201..216, q-d2-201..213, q-d3-201..211, q-d4-201..206, q-d5-201..206).** Each has a multi-constraint scenario stem, per-distractor reasoning, and an explicit trap line. Seven are multi-response (SELECT 2, correct AB); the rest are single-answer.

**3 hardest new questions (by design):**
- q-d1-210 (Q150): fine-tune vs continued pre-training vs distillation ladder across three lifecycle stages; distractors swap the correct technique to the wrong stage.
- q-d3-204 (Q174): multi-account Guardrails governance via Organizations SCP + StackSets + bedrock:GuardrailIdentifier (SELECT 2); the "organization policy" decoy tests knowledge that Bedrock lacks org-level policy objects.
- q-d4-201 (Q181): three-way Provisioned Throughput vs batch inference vs on-demand tier assignment (SELECT 2) with an idle-cost constraint that kills the peak-sized-PT decoy.

**Mechanical verification (scripted, all PASS):** 192 question blocks, ids unique, Q numbers sequential 1-192, all 140 original answer keys byte-identical to the pre-audit backup, mock 75-row key consistent, all mock anchors resolve, intro paragraph and FACT-CHECK comment updated, head / design-system style / DS_TRACK+DS_MANIFEST+ds.js scripts byte-identical (surgical edits confined to <main>), zero em dashes and zero external URLs in question content, HTML tag balance clean.

**Notes.** The 11 em dashes in the file are pre-existing boilerplate (title tag, design-system CSS comments, ds.js comments), untouched per the no-touch rule. A full pre-audit backup is kept at /tmp/qbank/backup-before-audit.html (ephemeral; the canonical file is the deliverable).

## Remediation pass (2026-09-28, ~15:00-19:45 EDT)

**Overflow defect (fixed, shared ds.css).** `p code, li code {white-space:nowrap}` caused long identifiers/ARNs to spill out of the content column. Fixed: `overflow-wrap:anywhere` on inline code, `overflow-wrap:break-word` on `#ds-content`, `min-width:0` on `.ds-prevnext a` / `.ds-prev-empty` and `.vol.row > *`. All 38 tables wrapped in `.table-wrap`, all `pre` have overflow-x, all `img` max-width:100%.

**Screenshot QA.** Headless Chromium (system google-chrome via Playwright) at 1440/768/390 for all 11 pages: **zero container spills, zero page-level horizontal scroll** on all 33 page-widths. Full-page + figure-section + bottom screenshots reviewed visually; fig-light white cards, mermaid dark diagrams, and stat ladders all render clean.

**Images embedded (24 total).** 15 internet figures via `:::figure` (Bedrock overview, Kendra arch, OpenSearch ingestion, KB arch, chunking pipeline, prompt anatomy, RAG-vs-finetune quadrant, inference-params infographic, Agents arch, Strands multi-agent, agent router, Guardrails arch, responsible-AI Bedrock, LLM-as-judge, prompt CI/CD). Rejected 4 (AI-generated slop x3, corrupted text x1). 9 mermaid SVGs rendered with dark theme.json (RAG pipeline, agent orchestration, sync/async decision, guardrails flow, cost ladder, eval loop, grounding decision, troubleshoot tree, question-bank domain mix). mermaid-cli installed durably at ~/workspace/.mermaid (npm global at /usr was wiped mid-session).

**PDF.** Combined hyperlinked PDF: cover + hyperlinked TOC (11 entries, all resolve to internal destinations) + all 11 volumes, 950 pages, Letter, light-paper print CSS, page-number footers. Producer/Creator metadata stripped via pypdf (title retained), text layer verified intact.

**Watermark hygiene.** wm_clean.py Layer A on all 11 final HTML files: all byte-identical after cleaning (zero watermarks found).

**Deliverables.** Zip rebuilt: ~/workspace/your_files/aws-aip-c01-study-guide.zip (39.6 MB, 161 files: 11 HTML + assets + src + labs-src + PDF + docs). GitHub: jrajath94/aws-aip-c01-study-guide (public per user request) — 178 blobs, verified 0 missing vs local. Push notes: gh_publish.py takes bare repo name (not owner/repo); filenames with spaces break its URL building (renamed 2 labs-src duplicates); api.github.com dropped connections repeatedly — small batches with sleeps got through.

## Remediation pass 2: humanizer gate, code standard, field research, crash course (2026-09-28, evening EDT)

**Humanizer QA gate (wired into build).** New `src/humanize_check.py`: HARD FAIL on em dashes, banned AI tells (delve, leverage-as-verb, furthermore, moreover, additionally-as-sentence-starter, tapestry, seamless, robust, game-changer, supercharge, deep dive, "it's worth noting", "in conclusion", "in today's", elevate), throat-clearing openers. Warnings (non-blocking) on sentences >35 words and non-Python code fences. Skips data URIs/base64, fenced code, front-matter; quoted product vocabulary exempt. Fixed: 224 em dashes to colons/commas; "robustness" to "stability" (one quoted Bedrock metric label kept); "highest-leverage" to "highest-impact". ~12 worst long sentences rewritten by hand; semicolon-only auto-split for the rest. build.py fails the build if the gate fails. Current: 0 failures, gate PASS, 0 build warnings. REPO READMEs already clean.

**Code standard.** Audit: zero JavaScript/Java anywhere; zero AWS CLI samples. All 5 existing Python samples rewritten with thorough comments (what each block does, why written that way, what breaks if changed). 4 new boto3 samples added, each paired with an existing diagram: Converse + guardrailConfig (D1 ch5, API decision matrix), RetrieveAndGenerate (D1 ch12, RAG pipeline), invoke_agent (D2 ch1, agent orchestration), batch inference create_model_invocation_job (D2 ch10, sync/async decision). All 9 Python samples verified with ast.parse.

**Field research (Sept 2026 passer reports).** Research subagent findings in EXAM-PATTERNS-INTERNET.md: 35 numbered trap patterns, multi-response phrasing patterns, service pairs tested together, stem conventions, 10 most-tested facts, 2026 Bedrock features (Automated Reasoning, cross-region profiles, prompt caching, supervisor/collaborator agents, BDA). Trap catalog in question-patterns.md expanded 15 to 30 (proactive-vs-reactive, fabricated features, CloudTrail-vs-CloudWatch-vs-invocation-logging, Standard-vs-Express, vector-store-by-scale, perceived-vs-real latency, caching precondition, PT misuse, detect-vs-block, SCP-vs-boundary, PII pipeline, no-public-internet, eval ladder, adjective precision). 8 new questions Q193-Q200 added to the bank (ids q-d3-212/213, q-d4-207/208, q-d5-207, q-d1-217, q-d2-214/215). Bank now 200 questions.

**Crash course volume.** New `volume-crash-course.html` (12th volume): per-domain rapid-fire sheets D1-D5 by weight, "if stem says X, pick Y" decision rules, must-memorize numbers table, all 30 traps in one line each, 30 rapid-fire self-test questions with one-line answers (details/collapsible). Also added `:::details` directive support in build.py (was dead code) plus page-scoped CSS for the QA cards; shared ds.css untouched.

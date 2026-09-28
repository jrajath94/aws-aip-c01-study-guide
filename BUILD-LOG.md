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

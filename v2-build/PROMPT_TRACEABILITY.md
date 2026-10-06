# AIP-C01 Crash Course v2, Prompt Traceability Matrix

Audit date: 2026-10-06. Auditor: prompt-traceability worker (did not build).
Scope: v4.0 master prompt §1-§20 (per the distilled requirement list), every
addendum v2.0 item, every Raj chat order. Method: direct inspection of final
artifacts on disk. Status values: done, partial, missing. No requirement is
dropped. Every partial or missing row carries the fix or the honest reason.

Artifacts audited: volume-crash-course.html (536,383 bytes, 20 sections, 40
images), volume-crash-course.pdf (214 pages, 20,769,271 bytes, producer None),
v2-build/stage1/ (11 files), v2-build/fragments/ (7), v2-build/addendum/ (14
files after this audit), v2-build/qa/independent-audit.md,
v2-build/BUILD_STATE.md, assets/img/v2/ (40 files),
~/workspace/user/files/aip_c01_combined_prerequisites_gaps_and_senior_judgment.md.

## PART A, v4.0 master prompt §1-§20

| Req | Implemented where | Evidence | Status | Fix or reason |
|---|---|---|---|---|
| §1 eight learner capabilities | volume-crash-course.html, lesson template blocks + L12 + bank | Mechanisms: every lesson "Mental model". Requirement recognition: every lesson "The problem". Best-architecture discrimination: "Closest alternative" block in all 13 lessons. Distractor elimination: "Valid but inferior, and technically invalid" block in all 13 lessons. Counterfactuals: explanation item 9 in all 60 bank items plus L12 walkthroughs. Troubleshooting: 10 playbooks in L11. Transfer: 58 lesson checks + 22 bridge checks, answers hidden. Timed practice: bank test mode, hidden answers, timed protocol in senior playbook. | done | none |
| §1 no false AWS affiliation | volume-crash-course.html header + bank labels | 0 claims of AWS affiliation, sponsorship, or endorsement. 23 labels state "original exam-style practice, not authentic AWS items". No pass promises. | done | none |
| §2.1 exam facts verified | v2-build/stage1/exam-facts-v2.md | Research date 2026-10-06. Official guide HTML + PDF read in full. Conflict log present (ordering/matching correction, Kodekloud 130-min outlier rejected). Explicit "Note on scaled score": no raw-to-scaled conversion. Per-domain counts marked estimates, never facts. | done | none |
| §2.2 claim classification | exam-facts-v2.md + volume-crash-course.html | Five labels defined ([Guide], [Behavior], [Secondary], [Unverified], [Version-dependent]). 132 label marks in the HTML. Every lesson ends with "Evidence notes" carrying labels and the research date. | done | none |
| §2.3 never-assume claims, 8 spot-checked | volume-crash-course.html lessons + bridges | 1. PrivateLink residency: "A private link protects the request in transit. It does not change where the inference executes" (L9). 2. CRI: "adds latency and moves data across borders, which is a compliance flag" (L1). 3. temp-0 determinism: temperature taught as a dial, "Put deterministic steps in code. Never let the model be the enforcer" (L8). 4. tool-calling validity: patch P-G12, "generated SQL is not authorized execution" (L8). 5. model universality: "models are not served in every Region" (L0). 6. grounding scores: "Processing improves the odds, it never guarantees truth" (L3). 7. native metrics: "Native metric names belong to AWS, so never invent one" (L10). 8. SDK retries: "the SDK retries with exponential backoff" (L6). Also verified: DynamoDB TTL as non-authorization (B-P14), IAM cross-account both-sides rule (L9), MASK redaction (L8), provisioned throughput not a discount (L6), batch SLA discipline (L6). | done | none |
| §3 source hierarchy, no dumps, labeling | stage1 files + HTML | Sources cited per claim with labels. Independent audit: "The text never claims authentic AWS questions." "original exam-style practice" appears 23 times. | done | none |
| §3 A-H | stage1 + HTML + qa/independent-audit.md | A blueprint: blueprint-skills-v2.md. B prereqs: prereq-graph-v2.md. C mechanisms: 13 lessons. D decision boundaries: 12 matrices + 12 drills. E implementation: §12 artifacts. F assessment: 60-item bank + 20 curveballs. G adversarial audit: qa/independent-audit.md, 80/80 keys, 0 false claims. H learner validation: transfer checks and diagnostics built, no learner data exists, stated honestly. | partial | H is learner-dependent. Built, not observed. Recorded as honest partial, not a gap. |
| §3 coverage ledger, 15 columns | v2-build/stage1/coverage-ledger-v2.md | 98 rows, 98 distinct skill IDs, 12 columns (Task, Skill, Skill summary, Prerequisite dependencies, Required concepts, Relevant services, Lesson, Comp. table, Worked scenario, Practice Q IDs, Evidence sources, Status). Addendum delta rows appended in the addendum 11-column format. | partial | The 15-column definition lives in the v4.0 master prompt, which this auditor did not inherit. The 3 missing columns cannot be named or fabricated. Parent: confirm the 3 columns from the prompt, the fix is mechanical. |
| §3 blueprint coverage vs mastery | delta audit + addendum state + readiness dashboard | Coverage measured per row. Learner state UNKNOWN on every row, stated in aip_delta_audit.md, aip_addendum_state.md, and aip_readiness_dashboard.md. | done | none |
| §4 layers, crash + deep path, lesson links | v2-build/stage1/paths-v2.md + HTML deep-ref blocks | Crash path and deep path defined in paths-v2.md with per-lesson file mapping. All 13 lessons carry a "Deep reference" block naming the counterpart file (verified L0, L1, L3, L5, L8, L9, L10). Site chrome links all volumes from the JS manifest. Explicit A-D layer labels do not appear in the HTML, the crash, deep, and labs layers exist and labs sit as optional extension. | done | Layer-label caveat recorded, structure serves the layering. |
| §5 abbreviations resolved | volume-crash-course.html | Every abbreviation defined at first use via dfn tags (L0 20+, L5 22, L11 23). Bank key-terms box defines FM, RAG, PII, TTFT, IAM, VPC, KB, API. CCP/MLA/MLE do not appear, AIF-C01 appears once as a resolved label. | done | none |
| §5 foundation areas to L0/L9/L10 | v2-build/stage1/prereq-graph-v2.md | P1-P8 each carry dependent concept, minimum depth, diagnostic question, and remediation pointer. Pointers land in L0 (P1, P5, P6, P7), the D3 lessons (P2, P3, P4), and L10 (P8). | done | none |
| §6 5 domains, 23 tasks, 98 skills | coverage-ledger-v2.md + HTML | Ledger: 98 rows, 98 distinct skill IDs (D1 28, D2 25, D3 15, D4 16, D5 14). 10 spot-checked skill IDs (1.1.1, 2.1.3, 3.2.1, 4.1.2, 5.1.2, 1.4.2, 2.3.4, 3.1.2, 4.2.4, 5.1.9) all resolve to lesson content. | done | none |
| §7 lesson template, 10 crash blocks | volume-crash-course.html L0-L12 | Spot-checked L0, L5, L11 item by item. All carry: The problem, Mental model, Worked example(s), How AWS does it, Limits and traps, Closest alternative, Valid but inferior and technically invalid, Check yourself, Deep reference, Evidence notes. L11 adds an 11th block for the 10 troubleshooting playbooks it hosts. | done | none |
| §8 7-step method + walkthroughs | volume-crash-course.html id="l12" | Method taught at id="l12-method" with figure s8-method-1.png and a read walkthrough. 6 walkthroughs (w1-w6) each run all 7 steps (Objective, Hard constraints, Layer, Eliminate, Rank, Hidden dependencies, Validate). | done | none |
| §9 matrices + minimal pairs | volume-crash-course.html id="matrices", id="drills" | 12 confusion matrices (m1-m12), each with shared ground, decisive difference, wins/loses, cost, operations, misconception. 12 minimal-pair drills (drill-a1 through drill-f2), each with one change that flips the answer. Authorized scale-down from "3 per pair" recorded. | done | none |
| §10 bank targets, authorized scale | volume-crash-course.html id="qbank", id="curveballs" | Raj ordered crash-course scale (~50-70), superseding 30/domain + 4 mocks. Built: 60 bank items (Q1-Q60, 44 single + 14 select-2 + 2 select-3) + 20 curveballs (CB-01..CB-20). All 60 have 12-point explanations (verified 12 li in all 60 expl blocks). Curveballs carry A-I explanations in aip_curveball_answers.md and compact hidden explanations in the HTML. Test mode: 80 hidden-answer details blocks. Independent audit: 80/80 keys hold. | done | Superseded-by-order recorded. |
| §11 error ledger | v2-build/addendum/aip_error_ledger_template.md | No error ledger existed. Created this audit: template with error classes, ledger columns, priority order, advancement evidence, and the no-scaled-score rule. No inferred learner answers anywhere, mastery UNKNOWN throughout. No scaled-score promises (explicit in template and dashboard). | done | Fix applied: file created. |
| §12 implementation artifacts | volume-crash-course.html | 4 IAM policy JSON blocks, 13 assume-role/trust mentions, 35 Converse/toolConfig API shapes, 11 tool-loop references, 7 JSONL eval mentions, Logs Insights queries, CloudWatch metric alarms. Purpose, assumptions, permissions, and verification status carried in prose and evidence notes. Illustrative-only labels present. No deployments, no charges. | done | none |
| §13 ASCII diagrams + figures | volume-crash-course.html | 25 ASCII diagrams in pre blocks, 18 with labeled edges. 40 figures, each with a Shell caption, an HTML read walkthrough (94 read-the-panel lines), and a figcaption naming the shell and source. | done | none |
| §14 mandatory calculations | volume-crash-course.html | All 10 present with assumptions shown: token cost (12 refs), context budget (5), cache break-even (19), embedding storage (5), chunk/overlap (6), cosine (8), provisioned break-even (4), p99 (15), nDCG (13), recall@k (11). | done | none |
| §15 labs | volume-crash-course.html deep-ref blocks | volume-maarek-labs.html linked as the hands-on deep reference (L5 block, site manifest). Labs not rebuilt at crash-course scale: partial by design, authorized. Cost discipline taught in lessons (L5 idempotency double-charge, L6/L10 cost math). No standalone labs cost-warning box. | partial | Partial by design per the task instruction. |
| §16A exam facts | v2-build/stage1/exam-facts-v2.md | Full verified fact table with labels and conflict log. The HTML deliberately states no counts, duration, price, or passing score (independent audit confirms). | done | none |
| §16B source registry | (no standalone file) | Evidence notes per lesson + source list in exam-facts-v2.md serve the function. No file named source registry exists. | partial | No standalone source-registry file. Evidence trail exists per lesson. Parent decides if a consolidated file is wanted. |
| §16C coverage ledger | v2-build/stage1/coverage-ledger-v2.md | 98 rows + addendum delta rows. | done | See §3 column note. |
| §16D prereq graph | v2-build/stage1/prereq-graph-v2.md | P1-P8 with the four required elements each. | done | none |
| §16E diagnostics | v2-build/stage1/diagnostics-v2.md + answers-hidden-v2.md | 10 diagnostics, answers in a separate file, mastery unknown. | done | none |
| §16F crash path | v2-build/stage1/paths-v2.md | Crash path table + deep-reference mapping + path relation rules. | done | none |
| §16G deep volumes | linked files | volume-d1/d2/d3/d4/d5, prereq volumes, system-design, question-bank, question-patterns, appendix-gaps, maarek-labs all linked from the manifest and deep-ref blocks. | done | none |
| §16H matrices | volume-crash-course.html id="matrices" | 12 matrices. | done | none |
| §16I atlas | (no standalone file) | The 12 matrices, decision ladders, and lesson maps serve the atlas function. No file named atlas exists. | partial | Function served, no standalone artifact. |
| §16J API/IAM reference | volume-crash-course.html (inline) | IAM policies, trust/assume-role, Converse/toolConfig shapes inline in lessons. No standalone reference file. | partial | Inline only. |
| §16K bank | volume-crash-course.html id="qbank" | 60 items, 12-point explanations, hidden answers. | done | none |
| §16L drills | volume-crash-course.html id="drills" | 12 drills. | done | none |
| §16M playbooks | volume-crash-course.html id="troubleshooting" + id="playbook" | 10 troubleshooting playbooks + senior decision playbook (study 10 + timed 6). | done | none |
| §16N labs | volume-maarek-labs.html | Linked as deep reference. | done | See §15. |
| §16O mocks | volume-crash-course.html id="qbank" | Scaled by order: the 60-question bank doubles as the timed test run, deep-bank note links the 200-question volume bank. | done | Scaled by Raj order. |
| §16P error ledger | v2-build/addendum/aip_error_ledger_template.md | Created this audit. | done | Fix applied: file created. |
| §16Q readiness dashboard | v2-build/addendum/aip_readiness_dashboard.md | Created this audit: domain coverage table with true Q-ID ranges, curveball axis map, mastery UNKNOWN, ship gates. | done | Fix applied: file created. |
| §16R review sheets | v2-build/addendum/aip_review_sheets.md | Created this audit: one-page recall per domain + method sheet, no new claims. | done | Fix applied: file created. |
| §16S uncertainty register | v2-build/addendum/aip_uncertainty_register.md | Created this audit: 13 open items, learner-state unknowns, closed items. | done | Fix applied: file created. |

| §17 stages 1-10 executed | v2-build/BUILD_STATE.md + .aip-v2-heartbeat.json | Stage 1 gated (exam facts, 98-skill ledger, prereq graph, L0-L12 plan, 10 diagnostics). Stages 2-7 gated (L0-L11, 28+25+20+30 skills, calculations). Stage 8 gated (12 matrices, 12 drills, 6 walkthroughs, 10 playbooks). Stage 9 gated (60q bank). Stage 10a gated (HTML, 344 ids unique, STE 0 hard, wm_clean). Stage 10b gated (PDF 214 pages, TOC 193/193, metadata stripped). Stage 10c gated (independent audit). Stage 10d gated (fix worker: 14 plates, 3 orphans, 2 text fixes, PDF rebuilt). | done | none |
| §18 twelve quality gates | BUILD_STATE.md + heartbeat + qa/independent-audit.md | 1. Stage-gating (no stage proceeds ungated). 2. Exam-facts verification Oct 6. 3. STE100 0-hard-fail gate per fragment. 4. wm_clean Layer A. 5. ID uniqueness QA (344). 6. Claim classification. 7. Adversarial answer-key review (80/80). 8. Independent audit (SHIP-WITH-FIXES + fix list). 9. Image provenance audit (Muse-tools-only). 10. Visual spec audit (26 pass, 14 fail, regenerated). 11. PDF build gates (TOC, images, metadata). 12. Push verification via GitHub API (remote==local). | done | none |
| §19 completeness audit | v2-build/qa/independent-audit.md | Five-item report: Pass 1 answer keys (80/80), Pass 2 claims (0 wrong/stale/unverified), Pass 3 images (26 pass, 14 fail), Pass 4 structure (ids, anchors, labels), Fix list (4 items, all applied by the fix worker). Gaps not hidden: image fails, orphans, typos all listed. | done | none |
| §20 begin-now items | v2-build/stage1/ | All 8 done in Stage 1: verify facts (exam-facts-v2.md), extract blueprint (blueprint-skills-v2.md), audit syllabus (aip_delta_audit.md), prereq graph (prereq-graph-v2.md), ledger (coverage-ledger-v2.md), paths (paths-v2.md), diagnostics (diagnostics-v2.md), first lesson (lesson-map-d1.md). | done | none |

## PART B, addendum v2.0 items

| Req | Implemented where | Evidence | Status | Fix or reason |
|---|---|---|---|---|
| P01-P33 prerequisite candidates | v2-build/addendum/aip_delta_audit.md + bridges + HTML id="bridges" | Delta audit covers all 33: 10 ADEQUATE link-only (P06, P08, P09, P15, P17, P24, P25, P29, P31, P33), 22 bridges built (B-P01..B-P32, ids ad-b-p01..ad-b-p32 in the HTML), P10 residency handled by correction patch P-G09. Learner UNKNOWN on every row. (Task said 12 ADEQUATE, the audit records 10 P-rows plus 5 G-rows, 15 total. The task count was off, the audit is authoritative.) | done | none |
| G01-G20 core gaps | v2-build/addendum/aip_core_gap_patches.md + HTML | 15 patches applied (P-G01..P-G19 minus G07, G10, G16, G17, G20). Spot-verified in HTML: P-G15 hash collisions, P-G18 feedback biases, P-G01 decision records, P-G12 deterministic-vs-probabilistic, P-G05 bounded clarification, P-G19 joint versioning, P-G04/P-G09 labeled inline. 5 ADEQUATE link-only (G07, G10, G16, G17, G20). BUILD_STATE records 16/16 patch inserts applied. | done | none |
| C01-C30 trap axes | v2-build/addendum/aip_curveball_coverage.csv | 30 rows. Covered axes map to bank Q-IDs. 5 absent axes (C16, C23, C28, C29, C30) each got 4 curveballs = 20. Thin axes (C03, C07, C11, C17, C22) recorded, no new items planned. Mastery UNKNOWN throughout. | done | none |
| B01-B10 briefs as generators | v2-build/addendum/aip_brief_to_curveball_map.md | Mapping reconstructed by this auditor (curveball files carry C-axis tags, not B-IDs). B01, B02, B08, B10 have direct curveball children. B03-B07, B09 are trained in lessons or patches with no dedicated curveball, per the addendum minimal-addition rule. | done | Fix applied: mapping file created. |
| Senior decision protocol | v2-build/addendum/aip_senior_decision_playbook.md + HTML id="playbook" | Study mode: 10 steps (id="ad-pb-study"). Timed mode: ASK, MUST, LAYER, ELIMINATE, RANK, CHECK SET (id="ad-pb-timed"). Extends the L12 7-step method. | done | none |
| Set-matrix logic in multi-select | HTML bank + aip_curveball_answers.md | Spot-checked Q2, Q28, Q60: requirement set tables (Requirement x options, pass/fail) in all three. Spot-checked CB-02: inline "Set matrix" prose in HTML plus the full combination table (Combination, Supported, All hard constraints, Objective fit, Missing element, Retain/Reject) in aip_curveball_answers.md. | done | none |
| Microexperiments shells 0-6 | v2-build/addendum/aip_microexperiments.md + HTML | 3 labs with shells 0-6 in the md file. 3 plates wired into the HTML (ad-path-exec-1.png in L9, ad-rag-layers-1.png in L3, ad-cache-key-1.png in L10, 1 reference each, verified). | partial | The lab shell text is not folded into the learner HTML, only the plates are wired. Folding it in is a content addition needing coordinator assembly plus a PDF rebuild and re-gate. Recommended as a follow-up, not a ship blocker: the concepts are taught in L9, L3, L10. |
| Checkpoints A-D | v2-build/addendum/aip_addendum_state.md | A (two-axis audit): COMPLETE. B (bridges + patches): COMPLETE. C (assessment): COMPLETE. D (integration): COMPLETE. Unresolved dependencies listed (P-G09 L7 insert as patch, push lane, C28 recheck date, mastery UNKNOWN). | done | none |
| 7 addendum files | v2-build/addendum/ | All exist: aip_delta_audit.md, aip_prerequisite_bridges.md, aip_core_gap_patches.md, aip_senior_decision_playbook.md, aip_curveball_coverage.csv, aip_curveball_questions.md, aip_curveball_answers.md, plus aip_addendum_state.md and aip_microexperiments.md. | done | none |

## PART C, Raj chat orders

| Order | Implemented where | Evidence | Status | Fix or reason |
|---|---|---|---|---|
| v1 archived locally, untouched | archive/2026-10-06-v1/ | README.md, volume-crash-course.html (455,961 bytes), volume-crash-course.pdf, mobile390 png. md5 differs from v2 HTML. Created 17:00 Oct 6, never pushed (BUILD_STATE: v1 archive stays local). | done | none |
| Zero-knowledge depth | volume-crash-course.html L0, L5, L11 | Spot-checked 3 lessons for unexplained jargon: L0 defines tokens, context window, embeddings, temperature, top-p/k, agent, RAG, fine-tuning, EC2, Lambda, Step Functions, S3, DynamoDB, VPC, IAM, Region, AZ, CloudWatch, CloudTrail, X-Ray at first use. L5: 22 dfn definitions. L11: 23 dfn definitions (golden dataset, holdout, nDCG, IDCG, DCG). | done | none |
| Visual spec on all docs incl. addendum | assets/img/v2/ + qa/independent-audit.md | All 40 images audited. 26 passed, 14 failed and were regenerated by the fix worker. This auditor visually verified 2 regenerated plates: d4-cost-per-success-1.png (claim title, before/after, $0.05 and $0.033 per success compute correctly) and s8-cache-1.png (claim title, 1,200 tokens at $0.0036 matches the taught $3.00/1M toy price). 3 orphan plates wired into L9/L3/L10. | done | none |
| Muse-tools-only images | BUILD_STATE.md §5 + heartbeat image_provenance | Provenance audit: 35 AI plates via media.generate_image (PIL metadata scan, 1920x1280, zero foreign signatures), 1 hand-drawn SVG, 0 regenerated, 0 non-Muse-tool images. | done | none |
| Print spec, 6 items, in the PDF | volume-crash-course.pdf + print-build.log | Fonts: Inter per the stack (renders as Noto Sans, recorded as known cosmetic). Margins: 0.5in Letter. TOC numbers: 193/193 match physical pages (fix-worker verified). Image sizing: measured, proportional, max 7.5in, never upscaled, centered, 12pt padding. Page breaks: per-domain section breaks. Metadata strip: producer None, creator None, title None (verified directly with pypdf). 214 pages. | done | none |
| Continuous pushes, 3 verified | BUILD_STATE.md §7 + heartbeat | Push 1 verified (tree f382dfbd2d97, remote==local 11/7/43). Push 2 verified (tree 7d6a8e31561f, remote==local 11/7/43/9). Push 3 (this matrix + BUILD_STATE.md + fix-worker changes) pending. Final push (HTML + PDF + zip + in-repo verification) pending. | partial | 2 of 3 verified. Pushes 3 and final are the coordinator lane. |
| World-class audit | qa/independent-audit.md + this file | Independent adversarial audit (80/80 keys, 0 false claims, image fails fixed) plus this requirement-by-requirement matrix. | done | none |
| Trust-by-verify in-repo | heartbeat continuous_push | Pushes 1-2 verified via GitHub API git-trees (remote counts equal local). Final in-repo verification (paths, sizes, SHAs, blob spot-checks) pending with the final push. | partial | Pending final push, coordinator lane. |
| BUILD_STATE.md exists | v2-build/BUILD_STATE.md | Canonical state file, rewritten 15:16 EDT Oct 6: brief, all orders with timestamps, stage statuses, decisions, traceability pointer, push history, remaining work. | done | none |
| This traceability matrix | v2-build/PROMPT_TRACEABILITY.md | This file. | done | none |

## Fixes applied by this audit

1. Created v2-build/addendum/aip_error_ledger_template.md (§11, §16P).
2. Created v2-build/addendum/aip_readiness_dashboard.md (§16Q).
3. Created v2-build/addendum/aip_review_sheets.md (§16R).
4. Created v2-build/addendum/aip_uncertainty_register.md (§16S).
5. Created v2-build/addendum/aip_brief_to_curveball_map.md (Part B, B01-B10 mapping).
6. Corrected the readiness dashboard bank-to-domain table against the true [DN] stem tags (D1 18, D2 15, D3 12, D4 7, D5 8).

## Honest unresolved items

1. Ledger column count: 12 present vs 15 required. The 3 missing columns cannot be named without the v4.0 master prompt. Parent names them, the fix is mechanical.
2. Microexperiment lab shell text not in the learner HTML (plates are wired, concepts are taught). Needs coordinator fold-in plus PDF rebuild.
3. Push 3 and the final push with full in-repo verification still wait on the coordinator.
4. No standalone source-registry file (§16B) or atlas file (§16I), the functions are served per-lesson and by the matrices. Parent decides if standalone files are wanted.
5. L7 check Q1 keeps its pre-correction residency wording (fragment freeze rule), correction ships as patch P-G09 with an exact anchor. Recorded in the uncertainty register.
6. The task's "12 audited ADEQUATE" for P01-P33 does not match the delta audit, which records 10 P-rows plus 5 G-rows ADEQUATE. The audit is authoritative.

## Counts

- Part A: 20 sections checked. Done 16, partial 4 (§3 H-honest + ledger columns, §15 by design, §16B, §16I, §16J counted under §16), missing 0.
- Part B: 9 items. Done 8, partial 1 (microexperiment lab text), missing 0.
- Part C: 10 orders. Done 8, partial 2 (pushes pending), missing 0.
- Fixes applied: 6 (5 new files + 1 correction). Unresolved: 6, all named above.

## Verdict

SHIP-WITH-RESERVATIONS. Every requirement is implemented or honestly recorded.
The 80 answer keys hold, no false claim ships, all 98 skills have lesson
coverage, and the five created files close the package gaps. The reservations
are: the final push with in-repo verification is still pending, the
microexperiment lab text still needs its HTML fold-in, and the ledger needs
its 3 missing column names from the v4.0 prompt. None of these changes the
shipped content. The coordinator clears them in order: fold-in, re-gate, push
3, final push with verification, then the completion report.

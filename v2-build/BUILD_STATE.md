# AIP-C01 Crash Course v2 — Canonical Build State

Single source of truth. Any agent reading only this file must know exactly what to do.
Last updated: 2026-10-06 15:16 EDT by coordinator 966438e5.

## 1. Build brief

Rebuild the AWS AIP-C01 crash course (volume-crash-course.html) from Raj's
"AIP-C01 First-Principles Mastery Engine v4.0" prompt, zero prior knowledge
assumed, crash-course pacing, step-by-step small-to-big. Learner: Raj, strong
software engineer, ~zero AWS knowledge, goal: pass AWS Certified Generative AI
Developer – Professional (AIP-C01).

Work area: ~/workspace/your_files/aws-aip-c01-cert/
Staging: v2-build/ (stage1/, fragments/, images/, addendum/, qa/, patched/)
Final HTML: volume-crash-course.html (repo root, same path as v1)
Final PDF: volume-crash-course.pdf (repo root)
Images: assets/img/v2/ (40 files)
Repo: jrajath94/aws-aip-c01-study-guide (PUBLIC, branch main)
v1 archive: archive/2026-10-06-v1/ — LOCAL ONLY, never pushed, never touched.

## 2. Raj's orders (chronological, EDT 2026-10-06)

- ~13:00 — Archive the v1 crash course; build NEW v2 from the v4.0 prompt.
  Everything covered deeply, zero previous knowledge, step-by-step,
  crash-course pacing. Strictly enforce visual_system_generic.md on all
  figures; generate as many AI images as possible.
- ~13:07 — PDF print spec (standing for all course PDFs): Inter (Anthropic
  Sans not installed; stack authorizes fallback), 10/14/18pt, line height
  1.3-1.4, 0.5in margins, widow/orphan control, page break per domain,
  keep-with-next on headers/diagrams/KEY TAKEAWAYs, nested clickable TOC
  with physical page numbers, images measured + proportionally resized
  (max 7.5in, never upscale, centered, 12pt padding), monospace no-wrap
  code, keep ALL content (dense, never cut).
- ~14:03 — Apply the AIP-C01 addendum
  (~/workspace/user/files/aip_c01_combined_prerequisites_gaps_and_senior_judgment.md,
  v2.0) at the next clean checkpoint as a SUPPLEMENT: no restart, no
  renumbering. Prerequisite bridges at the SAME depth as core lessons
  (mechanism, toy, choose/not-choose, trap, transfer check with separate
  answer, source/date, next core use). Two-axis validation gate. File set:
  aip_delta_audit.md, aip_prerequisite_bridges.md, aip_core_gap_patches.md,
  aip_senior_decision_playbook.md, aip_curveball_coverage.csv,
  aip_curveball_questions.md + aip_curveball_answers.md (separate),
  aip_addendum_state.md.
- ~14:07 — Top priority, finish ASAP. World-class audit: genuinely
  adversarial independent audit (per-question status, unresolved stays
  unresolved), trust-by-verify end to end INCLUDING inside the GitHub repo
  (paths, sizes, SHAs, spot-checked blob content). Browser shots of HTML
  (desktop + 390px). Visual PDF pass. Gates are the product; cut idle, not
  checks.
- ~14:12 — Image provenance rule (standing): ALL AI images from Muse native
  tools (media.generate_image, Meta pipeline) only. No OpenRouter, no
  external generators. 36 existing images audited: PASS (35 via Muse tools,
  1 hand-drawn SVG); 0 regenerated.
- ~14:25 — Continuous pushes: push every gated stage to the repo
  immediately (research, fragments, images, addendum files, bank, final
  HTML+PDF), not only at the end. Resilient pattern: Contents API, retry
  x15/8s, per-subdirectory, verify remote counts. v1 archive stays local.
- ~15:16 — Prompt traceability audit (v2-build/PROMPT_TRACEABILITY.md):
  requirement-by-requirement matrix over v4.0 §1-§20, every addendum item,
  every chat order; columns requirement | implemented where | evidence |
  status | fix/unresolved reason. SHIP GATE. Plus this file rewritten as
  the no-amnesia canonical state.

## 3. Standing laws (no exceptions)

1. visual_system_generic.md is LAW for every figure in every doc.
2. ASD-STE100 on all text; ste_check.py gate, 0 hard fails on learner content.
3. wm_clean.py Layer A on final HTML before delivery (Layer B rejected).
4. No exam dumps; all practice labeled "original exam-style practice".
5. No AWS deployments, no charges, no communications; all illustrative.
6. Sequential workers, one at a time. Box is free (Stanford pipeline done).
7. Lane discipline: touch ONLY aws-aip-c01-cert/ + the study-guide repo.
8. Claim classification on consequential claims ([Guide]/[Behavior]/
   [Secondary]/[Version-dependent]/[Unverified]); research date 2026-10-06.
9. Strip pdfTeX Producer/Creator from PDFs; verify producer is None.

## 4. Stage status

- STAGE 1 — GATED. Exam facts re-verified Oct 6 from AWS guide HTML+PDF:
  75 questions (65 scored + 10 unscored), MC + multiple response ONLY
  (no ordering/matching — baseline corrected), 750/1000 pass, compensatory
  scoring, weights 31/26/20/12/11. Duration/price NOT in official guide
  (secondary-sourced). 98 skills in coverage-ledger-v2.md. Prereq graph
  (8 prereqs). L0-L12 lesson plan with deep-reference file mapping.
  10 diagnostics, answers hidden.
- STAGES 2-7 — GATED. L0-L4 (D1, 28 skills), L5-L7 (D2, 25 skills),
  L8-L9 (D3, 20 skills + full P2/P3/P4 teach), L10-L11 (D4+D5, 30 skills
  + full P8 teach). Mandatory calculations done. STE 0 hard fails each.
- STAGE 8 — GATED. 12 confusion matrices, 12 minimal-pair drills,
  6 L12 7-step walkthroughs, 10 troubleshooting playbooks.
- STAGE 9 — GATED. 60 questions (44 single + 14 select-2 + 2 select-3),
  12-point explanations, STE 0 hard.
- ADDENDUM A-D — GATED. Delta audit, 21 bridges, 15 patches (all applied),
  20 curveball questions (answers separate), senior playbook, 3
  microexperiments (+3 ad-*.png plates), adversarial self-audit pass
  (59/60 keys held; Q27 fixed in place).
- STAGE 10a (assembly) — GATED. volume-crash-course.html, 534,021 bytes,
  20 sections, 37 images, 16/16 patches applied, STE 0 hard (learner
  content), wm_clean Layer A PASS, QA 341/341 ids unique.
- STAGE 10b (PDF) — GATED. volume-crash-course.pdf, 16,595,532 bytes,
  210 pages, Letter, TOC 193 entries 0 mismatches, 37/37 images render,
  producer None. Honest gaps: Chromium PUA text-layer mapping on some
  punctuation (visual fine); footer number also on TOC pages.
- STAGE 10c (independent audit) — GATED, verdict SHIP-WITH-FIXES.
  80/80 keys PASS; 0 false claims; 14 image FAILs; 3 orphan images.
  Report: v2-build/qa/independent-audit.md.
- STAGE 10d (audit fixes) — IN PROGRESS (fix worker 72ddb6d5):
  regenerate 14 plates with corrected numbers/titles, wire 3 orphans
  into L9/L3/L10, fix Q35 typo + Q23 Lambda overstatement, re-gate,
  rebuild PDF.

## 5. Key decisions

- v1 chrome (design-system shell) reused for v2; content fully replaced.
- Inter for PDF (Anthropic Sans not installed/unlicensed; stack fallback).
- Chromium print-to-PDF (WeasyPrint uninstallable; LaTeX conversion too
  lossy for this HTML). Two-pass TOC for physical page numbers.
- Ordering/matching question types dropped (not in official guide).
- Q27 fixed in place during adversarial review (residency overstatement).
- coverage-ledger-v2.md: 101 pre-existing STE hard fails fixed mechanically
  (semicolons to commas); table shape verified unchanged.
- Image provenance: instruction chain + worker reports + PIL metadata scan
  (36 PNGs 1920x1280, zero foreign signatures; OpenRouter defaults to
  1024x1024) = PASS, 0 regenerated.

## 6. Traceability

v2-build/PROMPT_TRACEABILITY.md — requirement-by-requirement matrix
(v4.0 §1-§20, all addendum items, all chat orders). SHIP GATE. Built by a
dedicated worker AFTER the fix worker gates (audits final artifacts).

## 7. Push history (all verified via GitHub API git-trees, remote==local)

- Push 1 (18:26-18:38Z): v2-build/stage1 (11), fragments (7), images (43).
  Retries: images OK attempt 3. Tree f382dfbd2d97.
- Push 2 (18:39-18:45Z): stage1 (11), fragments (7, Q27 fix), images (43,
  +3 ad-*.png), addendum (9). All attempt 1. Tree 7d6a8e31561f.
- Push 3 (pending): PROMPT_TRACEABILITY.md + BUILD_STATE.md (with next
  continuous push).
- Final push (pending): volume-crash-course.html + volume-crash-course.pdf
  + rebuilt zip, with full in-repo verification (paths, sizes, SHAs,
  blob spot-checks).

## 8. What remains (in order) — updated 2026-10-06 ~20:15 UTC

1. Fix worker GATED: 14 plates regenerated, 3 orphans wired, Q35/Q23 fixed,
   re-gated (STE 0 hard), PDF rebuilt (214 pages, 20,769,271 bytes).
2. Traceability worker GATED: PROMPT_TRACEABILITY.md, 66 rows, 55 done /
   9 partial / 0 missing, verdict SHIP-WITH-RESERVATIONS. Worker-created:
   aip_error_ledger_template.md, aip_readiness_dashboard.md,
   aip_review_sheets.md, aip_uncertainty_register.md,
   aip_brief_to_curveball_map.md.
3. Coordinator-resolved: ledger now 15 columns (106 rows, STE 0 hard).
   L7-Q1 reservation DISSOLVED (final HTML verified clean; P-G09 insert 2
   was applied at assembly). Honest reservations remaining: no standalone
   source-registry/atlas files (functions served per-lesson); full
   microexperiment shell text in MD only (plates + walkthroughs in HTML).
4. Push 3: traceability + BUILD_STATE.md + new addendum files + ledger fix.
5. Final push: volume-crash-course.html + volume-crash-course.pdf + rebuilt
   zip; in-repo verification (paths, sizes, SHAs, blob spot-checks).
6. Final sanity: desktop + 390px browser shots; PDF visual pass.
7. Final report to parent: bad news first.

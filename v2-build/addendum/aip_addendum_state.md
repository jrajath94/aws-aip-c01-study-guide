# AIP-C01 Addendum State v1.0

Date: 2026-10-06. Worker: addendum worker (subagent). Parent: v2 build coordinator.

## Checkpoint status

Checkpoint A (two-axis audit): COMPLETE. `aip_delta_audit.md` covers P01-P33 and G01-G20 against the built fragments. `aip_curveball_coverage.csv` maps C01-C30 to bank questions. Learner state UNKNOWN on every row (no learner data exists).

Checkpoint B (bridges and patches): COMPLETE. `aip_prerequisite_bridges.md` holds 21 bridge cards (B-P01 through B-P32). `aip_core_gap_patches.md` holds 15 patches (P-G01 through P-G19, with P-G09 as a correction). Learner-facing HTML in `fragments/addendum.html`, section `bridges` (placeholders for playbook and curveballs filled at Checkpoint C).

Checkpoint C (assessment): COMPLETE.
- 20 curveball questions in `aip_curveball_questions.md` (CB-01 to CB-20), answers strictly separate in `aip_curveball_answers.md` with A-I explanations and set matrices for multi-select items.
- Playbook in `aip_senior_decision_playbook.md` and in `fragments/addendum.html`, section `playbook`.
- Curveball learner HTML in `fragments/addendum.html`, section `curveballs` (questions with hidden-answer details, skill tags inside the hidden block only).
- Russian-doll microexperiments in `aip_microexperiments.md` with 3 AI plates (`images/ad-path-exec-1.png`, `images/ad-rag-layers-1.png`, `images/ad-cache-key-1.png`), all visually verified 2026-10-06, first-attempt pass.
- Adversarial answer-key review: separate self-audit pass over 60 bank items plus 20 curveballs. 59 of 60 bank keys hold. Q27 fixed in place in `fragments/qbank.html`. No item UNRELEASED.

Checkpoint D (integration): COMPLETE.
- All 17 patch anchors verified to exist in the fragments.
- All 20 curveball questions have separate answers in the answers file and hidden-answer blocks in the HTML.
- No id collisions across `fragments/addendum.html`.
- STE100: 0 hard fails on every new and edited file (ste_check.py).
- `stage1/coverage-ledger-v2.md` extended with prerequisite, core-gap, assessment, and correction delta rows.
- No fragment edited except `fragments/qbank.html` (Q27 fix, authorized by the adversarial-review instruction). Lesson fragments otherwise untouched. No renumbering. No git. No AWS calls.

## Unresolved dependencies

1. P-G09 insert 2 (L7 check Q1 answer replacement in `fragments/d2-lessons.html`) is specified as a patch, not applied. The no-fragment-edit rule forbids in-place lesson edits. The coordinator or assembler applies it from `aip_core_gap_patches.md`.
2. All 15 core patches (P-G01 to P-G19) are specified with exact anchors and marked ready. None is applied to the lesson fragments yet. Application order: patch-ID order.
3. `fragments/addendum.html` is a standalone fragment. Assembly into the final volume (ordering, TOC, asset paths for the three ad-*.png plates) belongs to the coordinator.
4. Learner mastery is UNKNOWN everywhere. No diagnostic data exists. The transfer checks and curveball items are built for future mastery tracking, not as evidence of it.
5. C28 items (CB-09 to CB-12) cite "current docs (2026-10)" as [Version-dependent]. Recheck them if the build ships much later than October 2026.
6. Raj's continuous-push order (2026-10-06, ~14:25 EDT) asks for gated pushes to jrajath94/aws-aip-c01-study-guide. Pushing is the coordinator's lane. This worker touched only v2-build files and ran no git.

## Next step

Coordinator: apply the 15 patches at their anchors (P-G09 insert 2 included), fold `fragments/addendum.html` into the final volume with the three plates, push per the continuous-push order, and resume the v2 build stage.

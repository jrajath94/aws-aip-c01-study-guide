# AIP-C01 Readiness Dashboard v1.0

Date: 2026-10-06. Purpose: one honest view of course coverage and learner state.
Rule: coverage and mastery are separate. Coverage is measured from built
content. Mastery is UNKNOWN for the learner on every row below. No inference
from counts.

## Coverage (measured from volume-crash-course.html, 2026-10-06)

| Domain | Weight | Skills | Lessons | Bank items | Curveballs | Matrices | Drills |
|---|---|---|---|---|---|---|---|
| D1 Foundation models, data, compliance | 31% | 28 | L0-L4 | Q1-Q18 (18) | CB-09..CB-16 (C28, C29) | M1-M4 | Stage 8B drills, pairs A-F (cross-domain) |
| D2 Implementation and integration | 26% | 25 | L5-L7 | Q19-Q33 (15) | CB-17, CB-20 (C30) | M5-M7 | (same Stage 8B drills) |
| D3 Safety, security, governance | 20% | 20 | L8-L9 | Q34-Q45 (12) | (none) | M8-M9 | (same Stage 8B drills) |
| D4 Optimization | 12% | 12 | L10 | Q46-Q52 (7) | CB-01..CB-04 (C16) | M10-M11 | (same Stage 8B drills) |
| D5 Testing, validation, troubleshooting | 11% | 13 | L11 | Q53-Q60 (8) | CB-18, CB-19 (C30) | M12 | 10 troubleshooting playbooks, L12 walkthroughs W1-W6 |
| Addendum: bridges, senior playbook, curveballs | n/a | 22 bridges, 15 patches | Addendum A-C | 20 curveballs (axes C16, C23, C28, C29, C30) | n/a | n/a | n/a |
Curveballs test trap axes, not single domains. Axis to official skills: C16 (4.1.4,
3.2.1), C23 (1.2.3, 2.4.3, 3.1.2), C28 (2.2.1, 1.2.1, 2.1.3, 2.4.2), C29 (2.4.3,
1.5.4, 3.2.1, 4.2.1), C30 (2.3.4, 4.2.1, 3.3.4, 2.2.1). Rows above name the
axes most tied to each domain's skills. Full axis map: addendum
aip_curveball_coverage.csv.

Skill ledger: 98 of 98 skills have lesson coverage in coverage-ledger-v2.md.
Bank: 60 items, 12-point explanations, hidden answers, test mode.
Curveballs: 20 items, A-I explanations, answers in a separate file.
Independent audit: 80 of 80 keys hold, 0 false claims (qa/independent-audit.md).

## Mastery (learner-dependent)

| Area | State | Evidence |
|---|---|---|
| All 98 skills | UNKNOWN | No learner data exists. |
| Transfer checks (58 lesson checks + 22 bridge checks) | UNKNOWN | Built, not attempted. |
| Timed practice | UNKNOWN | No timed runs recorded. |

## Ship gates

- Prompt traceability: v2-build/PROMPT_TRACEABILITY.md (this audit). Required.
- Fix-worker re-gate: 14 plates regenerated, 3 orphans wired, Q35 and Q23
  fixed, HTML re-gated, PDF rebuilt (214 pages, metadata stripped).
- Push 3: traceability + BUILD_STATE.md + fix-worker changes to the repo.
- Final push: HTML + PDF + zip, in-repo API verification, browser shots.

## What the dashboard does not claim

It does not claim exam coverage beyond the official guide. It does not
convert practice counts or percentages into a scaled score. It does not
predict a pass. It states what exists and what the learner has not done.

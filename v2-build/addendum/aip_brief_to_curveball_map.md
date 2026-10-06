# B01-B10 Brief to Curveball Mapping v1.0

Date: 2026-10-06. Auditor reconstruction. The addendum briefs B01-B10 are
generative prompts, not delivered content. The 20 curveballs (CB-01 to CB-20)
were generated for the five ABSENT trap axes (C16, C23, C28, C29, C30), per
the addendum rule: add only what the audit found absent. Briefs whose
decision boundary was already trained got no dedicated curveball by design.
The mapping below is verified by topic and stem, not by B-ID labels, because
the curveball files carry C-axis tags, not B-brief tags.

## Direct curveball children

| Brief | Decision boundary | Curveball child | Evidence |
|---|---|---|---|
| B01 | Private network plus single-Region processing vs failover | CB-06 (fallback must preserve residency), CB-17 (absolute residency vs Bedrock) | Both stems test path vs processing geography, patch P-G09 is the lesson source. |
| B02 | Fresh tenant authorization vs cached answers after revocation | CB-01 (tenant-scoped cache keys), CB-02 (hit-time authorization, Select TWO), CB-03 (prompt version in key), CB-04 (role-scoped answers) | All four are C16, CB-02 explanation cites B-P14. |
| B08 | Sensitive text in output vs prohibited input and log retention | CB-08 (Guardrails on every tier) | Partial. Stem tests control placement across tiers, full input-vs-output placement is taught in L8. |
| B10 | Select TWO complementary controls, one complete set | CB-02 (Select TWO), CB-07 (Select TWO), CB-19 (Select TWO) | Each has the addendum set matrix with exact-cardinality combinations retained or rejected. |

## Briefs covered without a dedicated curveball (by design)

| Brief | Decision boundary | Where it is trained | Why no curveball |
|---|---|---|---|
| B03 | Agent timeout after a possible account update | L5 retry/idempotency, L11 troubleshooting playbooks | Decision boundary already trained in lessons. |
| B04 | Long prompts vs long replies under one RPS | L6 streaming/p99, L10 capacity, Q47 | Already trained, no absent axis. |
| B05 | Right chunks wrong answer vs no chunks retrieved | L3 diagnostic chain, L11 retrieval troubleshooting | Already trained, no absent axis. |
| B06 | Valid JSON with a wrong financial total | Patch P-G12, L8 deterministic-vs-probabilistic | Covered by core-gap patch, no absent axis. |
| B07 | Low average cost with p99 and burst | L10 percentiles, Q47/Q48 cost math | Already trained, no absent axis. |
| B09 | Embedding change with joint version gates | Patch P-G04, Q11 | Covered by core-gap patch, no absent axis. |

## Verdict

4 of 10 briefs have direct curveball children. 6 of 10 are trained in
lessons or patches with no dedicated curveball, which follows the addendum's
own minimal-addition rule. No brief's decision boundary is untrained.

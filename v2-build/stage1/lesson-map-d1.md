# D1 Lesson-to-Skill Map (v2 build, Stage 1)

Research date: 2026-10-06. Fragment: `fragments/d1-lessons.html`. Ledger rows refer to line numbers in `stage1/coverage-ledger-v2.md` (Domain 1 table starts at line 15).

| Lesson slot | Section id | Title | Skills covered | Ledger rows |
|---|---|---|---|---|
| L0 | `l0` | Foundation ramp: AI basics + AWS compute/storage/network/IAM/observability minimums | Prereqs only: P1 (regions/AZs), P5 (compute limits/timeouts), P6 (S3/DynamoDB), P7 (tokens, embeddings, temperature/top-p/top-k, agents, fine-tune vs RAG), P8 one-liner (metrics/logs/traces/audit) | n/a (prereq ramp; callbacks feed rows 15-42) |
| L1 | `l1` | D1: Requirements, model selection, resilience, customization lifecycle | 1.1.1, 1.1.2, 1.1.3, 1.2.1, 1.2.2, 1.2.3, 1.2.4 | 15, 16, 17, 18, 19, 20, 21 |
| L2 | `l2` | D1: Data validation and processing pipelines | 1.3.1, 1.3.2, 1.3.3, 1.3.4 | 22, 23, 24, 25 |
| L3 | `l3` | D1: Vector stores and retrieval mechanisms (RAG core) | 1.4.1, 1.4.2, 1.4.3, 1.4.4, 1.4.5, 1.5.1, 1.5.2, 1.5.3, 1.5.4, 1.5.5, 1.5.6 | 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36 |
| L4 | `l4` | D1: Prompt engineering, management, and governance | 1.6.1, 1.6.2, 1.6.3, 1.6.4, 1.6.5, 1.6.6 | 37, 38, 39, 40, 41, 42 |

## Coverage notes for the coordinator

- All 28 D1 skills (1.1.1-1.6.6) are taught across L1-L4. L0 carries no blueprint skill; it teaches the P1/P5/P6/P7/P8 minimums the D1 lessons assume (per `stage1/prereq-graph-v2.md`).
- Skill statements in the lessons are faithful paraphrases of the official guide text (per `stage1/blueprint-skills-v2.md`); no verbatim copying.
- Mandatory worked calculations live in: L1 (token cost + context budget), L3 (embedding storage, chunk/overlap count, cosine + unit-vector distance identity with 2-D derivation), L2 and L4 (supporting toy arithmetic).
- IAM actions named per lesson; actions the builder could not verify are marked `[Unverified]` inline (see each lesson evidence note).
- Figures: 7 AI plates in `images/` named `d1-<topic>-1.png`, referenced as `assets/img/v2/d1-<topic>-1.png`. All visually verified 2026-10-06.

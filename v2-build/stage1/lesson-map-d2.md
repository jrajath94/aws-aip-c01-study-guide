# D2 Lesson-to-Skill Map (v2 build, Stage 1)

Research date: 2026-10-06. Fragment: `fragments/d2-lessons.html`. Ledger rows refer to line numbers in `stage1/coverage-ledger-v2.md` (Domain 2 table starts at line 50).

| Lesson slot | Section id | Title | Skills covered | Ledger rows |
|---|---|---|---|---|
| L5 | `l5` | D2: Agentic AI: agents, safeguards, human in the loop, MCP | 2.1.1, 2.1.2, 2.1.3, 2.1.4, 2.1.5, 2.1.6, 2.1.7, 2.5.5 | 50, 51, 52, 53, 54, 55, 56, 73 |
| L6 | `l6` | D2: Model deployment strategies and FM API integrations | 2.2.1, 2.2.2, 2.2.3, 2.4.1, 2.4.2, 2.4.3, 2.4.4, 2.5.1 | 57, 58, 59, 65, 66, 67, 68, 69 |
| L7 | `l7` | D2: Enterprise integration, CI/CD, GenAI gateway, dev tools | 2.3.1, 2.3.2, 2.3.3, 2.3.4, 2.3.5, 2.5.2, 2.5.3, 2.5.4, 2.5.6 | 60, 61, 62, 63, 64, 70, 71, 72, 74 |

## Coverage notes for the coordinator

- All 25 D2 skills are taught across L5-L7: L5 carries 8 (2.1.1-2.1.7, 2.5.5), L6 carries 8 (2.2.1-2.2.3, 2.4.1-2.4.4, 2.5.1), L7 carries 9 (2.3.1-2.3.5, 2.5.2-2.5.4, 2.5.6).
- Prereq callbacks used (taught in L0/D3, never re-taught): P5 compute limits (Lambda minutes cap, Step Functions waits), P3 IAM least privilege (full teach in D3), P1 regions/AZs (Outposts/Wavelength), P8 metrics/logs/traces (X-Ray, Logs Insights). D1 callbacks in one clause: tokens/pricing (L1), DynamoDB session state (L0), RAG APIs (L3), prompt regression gates (L4), AppConfig routing (L1).
- Skill statements in the lessons are faithful paraphrases of the official guide text (per `stage1/blueprint-skills-v2.md`); no verbatim copying, no exam dumps.
- Mandatory worked calculations live in: L5 (agent-loop token cost with max-steps worst case), L6 (provisioned break-even at stated utilization + p99 latency budget for a 3-turn agent loop), L7 (queue backpressure backlog).
- IAM actions named per lesson; actions the builder could not verify are marked `[Unverified]` inline (see each lesson evidence note).
- Figures: 5 AI plates + 1 hand-drawn SVG (break-even, after 2 failed AI attempts on axis numbers) in `images/` named `d2-<topic>-1.*`, referenced as `assets/img/v2/d2-<topic>-1.*`. All visually verified 2026-10-06.

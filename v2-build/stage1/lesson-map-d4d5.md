# D4+D5 Lesson-to-Skill Map (v2 build, Stage 1)

Research date: 2026-10-06. Fragment: `fragments/d4d5-lessons.html`. Ledger rows refer to line numbers in `stage1/coverage-ledger-v2.md` (Domain 4 table rows at lines 104-119, Domain 5 at lines 127-140).

| Lesson slot | Section id | Title | Skills covered | Ledger rows |
|---|---|---|---|---|
| L10 | `l10` | D4: Cost optimization, performance, monitoring | 4.1.1, 4.1.2, 4.1.3, 4.1.4, 4.2.1, 4.2.2, 4.2.3, 4.2.4, 4.2.5, 4.2.6, 4.3.1, 4.3.2, 4.3.3, 4.3.4, 4.3.5, 4.3.6 | 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119 |
| L11 | `l11` | D5: Evaluation systems and troubleshooting | 5.1.1, 5.1.2, 5.1.3, 5.1.4, 5.1.5, 5.1.6, 5.1.7, 5.1.8, 5.1.9, 5.2.1, 5.2.2, 5.2.3, 5.2.4, 5.2.5 | 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140 |

## Coverage notes for the coordinator

- All 16 D4 skills (4.1.1-4.3.6) are taught in L10; all 14 D5 skills (5.1.1-5.2.5) in L11. L10 carries the full P8 teach (metrics vs logs vs traces vs audit, custom metrics, dashboards, alarms, anomaly detection, correlation IDs, token-usage and cost tracking); L11 callbacks P8 without re-teaching.
- Provisioned-throughput break-even is referenced in one clause only (full worked example lives in L6); tiered routing/cascade, batch inference, streaming, TTFT, RAG/reranker, chunking, Guardrails, CloudTrail-audit, KMS, and endpoint policies are one-clause callbacks to L0-L9, never re-taught.
- Mandatory worked calculations live in: L10 (prompt-cache break-even with hit-rate framing, cost per successful task, p50/p95/p99 on a 10-sample toy), L11 (nDCG@5 + recall@5 + MRR on a 5-item toy, precision/recall/F1 toy).
- Skill statements are faithful paraphrases of the official guide text (per `stage1/blueprint-skills-v2.md`); no verbatim copying.
- IAM actions named per lesson; actions the builder could not verify are marked `[Unverified]` inline (`xray:PutTraceSegments`, `bedrock:StartIngestionJob`, Bedrock agent evaluation details). All invented metric names are labeled custom; no native metric names invented.
- Figures: 9 AI plates in `images/` named `d4-<topic>-1.png` / `d5-<topic>-1.png`, referenced as `assets/img/v2/d4-<topic>-1.png` / `d5-...`. All visually verified 2026-10-06. STE gate: 0 hard fails.

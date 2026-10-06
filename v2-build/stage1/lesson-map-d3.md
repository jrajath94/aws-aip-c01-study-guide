# D3 Lesson-to-Skill Map (v2 build, Stage 1)

Research date: 2026-10-06. Fragment: `fragments/d3-lessons.html`. Ledger rows refer to line numbers in `stage1/coverage-ledger-v2.md` (Domain 3 table starts at line 78; skill rows at lines 82-96).

| Lesson slot | Section id | Title | Skills covered | Ledger rows |
|---|---|---|---|---|
| L8 | `l8` | D3: Input/output safety controls and defense in depth | 3.1.1, 3.1.2, 3.1.3, 3.1.4, 3.1.5 | 82, 83, 84, 85, 86 |
| L9 | `l9` | D3: Data security, privacy, governance, compliance, responsible AI | 3.2.1, 3.2.2, 3.2.3, 3.3.1, 3.3.2, 3.3.3, 3.3.4, 3.4.1, 3.4.2, 3.4.3 | 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 |

## Coverage notes for the coordinator

- All 15 D3 skills (3.1.1-3.4.3) are taught across L8-L9. Per `stage1/prereq-graph-v2.md`, L9 also carries the FULL teach of P2 (VPC, subnets, security groups vs NACLs, interface vs gateway endpoints, endpoint policies), P3 (IAM policy evaluation: identity vs resource vs trust policies, explicit deny wins, permission boundaries, SCPs, cross-account, confused deputy + external ID, KMS key policies and grants), and P4 (envelope encryption, data keys vs KMS keys, key types, encryption context, rotation/deletion, cross-account encrypted access). These prereqs have no ledger rows; they remediate the D3 lessons that need them.
- Skill statements in the lessons are faithful paraphrases of the official guide text (per `stage1/blueprint-skills-v2.md`); no verbatim copying.
- Mandatory worked calculations live in: L8 (content-filter strength thresholds with false positive/negative trade arithmetic and review-labor cost), L9 (security-group stateful vs NACL stateless packet trace, Alice permission evaluation with deny-source identification, envelope encryption two-step flow with 32-byte data key / 40-byte note toy).
- IAM actions named per lesson; actions the builder could not verify are marked `[Unverified]` inline (see each lesson evidence note): `bedrock:ApplyGuardrail`, `sagemaker:StartHumanLoop`. Standard documented actions are marked `[Behavior]`: `kms:GenerateDataKey`, `kms:Decrypt`, `comprehend:DetectPiiEntities`.
- Figures: 8 AI plates in `images/` named `d3-<topic>-1.png`, referenced as `assets/img/v2/d3-<topic>-1.png`. All visually verified 2026-10-06; one pill-text zoom check confirmed clean rendering.
- STE gate: `ste_check.py` reports 0 hard fails on `fragments/d3-lessons.html` (warning count comparable to D2 baseline; residual warnings are linter tag-soup artifacts on raw HTML plus legitimate domain gerunds).
- No re-teach of D1/D2 material: tokens, context windows, RAG, prompts, agents, Bedrock APIs, and gateways appear in one-clause callbacks only (L3 grounding, L4 prompt governance, L5 tool-result trust boundary and erasure path, L6/L7 API and gateway references).

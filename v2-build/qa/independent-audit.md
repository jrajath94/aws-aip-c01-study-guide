# Independent audit: AIP-C01 crash course v2

Auditor: an independent adversarial auditor. The auditor took no part in the build.
Audit date: 2026-10-06.
Scope: volume-crash-course.html, the two addendum curveball files, the 40 images in assets/img/v2, the stage1 research files.

## Verdict: SHIP-WITH-FIXES

All 80 answer keys hold. The lesson text holds no false technical claim. 14 of 40 images fail the visual spec. 3 images have no reference in the HTML. 1 question stem holds a typo. Fix the items in the fix list, then ship.

Counts:
- Pass 1, 80 questions: 80 PASS, 0 FIXED, 0 UNRELEASED.
- Pass 2, claims: 0 WRONG, 0 STALE, 0 UNVERIFIED.
- Pass 3, 40 images: 26 PASS, 14 FAIL.
- Pass 4, structure: 5 checks pass, 1 finding (3 orphan images).

## Pass 1: answer key review

Method: for each question the auditor tried to make a distractor correct. The auditor looked for ambiguous requirements, hidden assumptions, double answers, wrong cardinality, missing permissions, bad cost math, and stale limits.

Status per question:

| ID | Key | Status | Note |
|---|---|---|---|
| Q01 | B | PASS | |
| Q02 | A,B,D | PASS | |
| Q03 | C | PASS | |
| Q04 | C | PASS | |
| Q05 | A,B | PASS | Cardinality softness, see note |
| Q06 | C | PASS | |
| Q07 | B,D | PASS | |
| Q08 | C | PASS | |
| Q09 | B | PASS | |
| Q10 | B | PASS | |
| Q11 | B | PASS | |
| Q12 | B | PASS | |
| Q13 | B | PASS | |
| Q14 | B | PASS | |
| Q15 | B | PASS | |
| Q16 | A,C | PASS | |
| Q17 | A | PASS | |
| Q18 | B | PASS | Math verified: $31,500 |
| Q19 | B | PASS | |
| Q20 | B | PASS | |
| Q21 | B | PASS | |
| Q22 | C | PASS | |
| Q23 | B | PASS | Explanation overstates Lambda limit, see note |
| Q24 | B | PASS | |
| Q25 | C | PASS | Math verified: 72% cheaper |
| Q26 | B | PASS | |
| Q27 | C | PASS | |
| Q28 | A,B,D | PASS | |
| Q29 | B | PASS | |
| Q30 | C | PASS | |
| Q31 | B | PASS | |
| Q32 | B | PASS | |
| Q33 | B | PASS | |
| Q34 | B | PASS | |
| Q35 | C | PASS | Stem typo, see note |
| Q36 | A | PASS | |
| Q37 | B | PASS | |
| Q38 | C | PASS | |
| Q39 | C | PASS | |
| Q40 | B | PASS | |
| Q41 | B | PASS | |
| Q42 | C | PASS | |
| Q43 | B | PASS | |
| Q44 | C | PASS | |
| Q45 | A | PASS | |
| Q46 | B | PASS | Math verified: $12,000 saving |
| Q47 | B | PASS | Math verified: $2,300 saving |
| Q48 | C | PASS | |
| Q49 | C | PASS | |
| Q50 | B | PASS | |
| Q51 | A,B | PASS | |
| Q52 | C | PASS | |
| Q53 | B | PASS | |
| Q54 | B | PASS | |
| Q55 | C | PASS | |
| Q56 | C | PASS | |
| Q57 | B | PASS | |
| Q58 | B | PASS | |
| Q59 | C | PASS | |
| Q60 | A,B,D | PASS | |
| ad-cb-01 | C | PASS | |
| ad-cb-02 | A,B | PASS | |
| ad-cb-03 | B | PASS | |
| ad-cb-04 | B | PASS | |
| ad-cb-05 | A | PASS | |
| ad-cb-06 | B | PASS | |
| ad-cb-07 | B | PASS | |
| ad-cb-08 | B | PASS | |
| ad-cb-09 | C | PASS | |
| ad-cb-10 | B | PASS | |
| ad-cb-11 | C | PASS | |
| ad-cb-12 | C | PASS | |
| ad-cb-13 | C | PASS | |
| ad-cb-14 | B | PASS | |
| ad-cb-15 | B | PASS | |
| ad-cb-16 | C | PASS | |
| ad-cb-17 | C | PASS | Minimal pair with Q27, both hold |
| ad-cb-18 | C | PASS | |
| ad-cb-19 | B | PASS | |
| ad-cb-20 | B | PASS | |

Notes on soft spots. None break a key.
- Q5: A alone (Glue Data Quality) may meet the objective, since Glue DQ emits per-rule metrics. B adds custom checks. All other options fail, so the key stands. Minor cardinality softness.
- Q23: the explanation says the Lambda time limit kills the 10-minute job. Lambda allows 15 minutes, so the job fits the limit. Cost still favors ECS for steady load, so the key stands. The explanation overstates the limit.
- Q35: the stem says "Q&.A". It should read "Q&A". Typo only. The key stands.

Curveball consistency: the 20 curveball items in the HTML match the addendum stems. All 20 keys match aip_curveball_answers.md. CB-13 through CB-16 paraphrase bank mechanisms by design (axis C29). CB-17 forms a minimal pair with Q27: Q27 allows Outposts plus private routing for data at rest, while CB-17 rejects Bedrock for data that must never leave the building. Both keys hold.

Format check: the bank holds single-answer and multi-select items only. Multi-select items use 2 or 3 correct answers out of 6 options. This matches the official guide: multiple choice plus multiple response. No ordering or matching items appear. The bank label states this.

## Pass 2: claim verification

Method: the auditor extracted consequential claims (service capabilities, IAM actions, limits, prices, API behavior) and checked them against the stage1 research files and current AWS behavior.

- Prices: every toy price carries a [Version-dependent] mark in lessons and explanations. No price is stated as current. No finding.
- IAM actions: every action named as verified is a real action. The list includes bedrock:InvokeModel, bedrock:Converse, bedrock:ConverseStream, bedrock:ApplyGuardrail, bedrock:Retrieve, bedrock:RetrieveAndGenerate, bedrock:StartIngestionJob, bedrock:CreatePrompt, bedrock:InvokeAgent, transcribe:StartTranscriptionJob, textract:DetectDocumentText, comprehend:DetectEntities, lambda:InvokeFunction, kms:Decrypt, sagemaker:StartHumanLoop, codepipeline:StartPipelineExecution, xray:PutTraceSegments, cloudwatch:PutMetricData. Evidence lines mark the rest [Unverified] with honesty. No invented action is stated as verified.
- Limits: context windows are labeled toy. The Lambda minutes-scale cap is taught as a decision rule, with exact seconds marked [Version-dependent]. No invented limit is stated as fact.
- Guarantees: lesson L9 states the honest bounds. Guardrails enforce policy but never certify legal compliance. Macie finds PII but never quarantines. Anonymization cuts risk but never guarantees it. No overstated RAG, guardrail, or latency guarantee found.
- Exam facts: the HTML states no question count, no duration, no price, no passing score. No stale exam fact can ship. The bank label correctly says the guide lists no ordering or matching items.
- Skill mappings: all 61 distinct skill numbers cited across the 60 bank questions exist in blueprint-skills-v2.md. All 20 curveball skill tags exist there too.
- Exam-dump check: the text never claims authentic AWS questions. Every bank label says the items are original exam-style practice.

Totals: WRONG: 0. STALE: 0. UNVERIFIED: 0.

## Pass 3: image review

Method: the auditor opened all 40 files. The auditor checked flat fills, palette, banned elements, label length, one rule per plate, before/after structure, computed numbers, and HTML captions.

FAIL items (14):

1. d2-cicd-1.png. Panel labels read "LEFT PANEL" and "RIGHT PANEL" with bullets. The spec wants before/after labels. The center arrow is double-headed.
2. d2-deploy-ladder-1.png. "Flat Vector Diagram" sits at the top. That is generator meta text, not a claim title. Two of three arrows lack operation labels.
3. d2-gateway-1.png. Panel labels read "LEFT PANEL / DIRECT" and "RIGHT PANEL / VIA GATEWAY". The title holds an em dash.
4. d4-agent-trace-1.png. The title is prompt leakage ("Flat vector diagram" plus a font, grid, and stroke spec line). No claim title.
5. d4-cost-per-success-1.png. Number mismatch. Model A shows 2 solid of 15 squares at $0.01 per call. That is $0.075 per success. The plate prints $0.05.
6. d4-prompt-cache-1.png. Number mismatch. The after panel prints $0.008 per call. With the 3000-token prefix cached and the same user text as the $0.0315 before panel, the math gives about $0.0225, not $0.008.
7. d5-ndcg-1.png. Number inconsistency. The ideal panel reuses the left panel gains (3.50, 1.89, 0.39) sorted by grade. At ideal positions the gains are 4.42, 1.50, and 0.43. The IDCG total (13.35) and nDCG (0.96) are correct, but the chips disagree with their positions.
8. s8-api-1.png. The title names the plate type, not the claim. It holds an em dash.
9. s8-cache-1.png. The title names the plate type ("Lesson plate: Before & After"), not the claim. "1,200 tokens" paired with "$0.024" does not compute at the taught $3.00 per 1M toy price, which gives $0.0036.
10. s8-ladder-1.png. The title names the plate type, not the claim. It holds an em dash.
11. s8-loop-gate-1.png. The title names the plate type ("Lesson plate, before and after"), not the claim.
12. s8-method-1.png. The title names the plate type ("Lesson plate"), not the claim.
13. s8-rag-call-1.png. The title names the plate type, not the claim.
14. s8-retrieval-1.png. The title names the plate type, not the claim. It holds an em dash.

PASS items (26): d1-tokens-1.png, d1-context-budget-1.png, d1-data-pipeline-1.png, d1-model-switch-1.png, d1-prompt-gov-1.png, d1-rag-1.png, d1-chunking-1.png, d2-agent-loop-1.png, d2-break-even-1.svg, d2-mcp-1.png, d3-detect-block-1.png, d3-envelope-1.png, d3-guardrail-1.png, d3-guardrail-anatomy-1.png, d3-injection-1.png, d3-macie-1.png, d3-policy-eval-1.png, d3-vpc-endpoint-1.png, d4-latency-tail-1.png, d4-observability-1.png, d5-holdout-leak-1.png, d5-judge-bias-1.png, d5-troubleshoot-1.png, ad-cache-key-1.png, ad-path-exec-1.png, ad-rag-layers-1.png.

Minor notes on passes: d3-guardrail-anatomy-1.png holds an em dash in its corner tag. d3-policy-eval-1.png writes "s3.GetObject" with a dot. d4-latency-tail-1.png holds a semicolon in its footer. d4-observability-1.png lacks a center arrow. None break the spec.

Captions: all 37 referenced images have an HTML caption that names the shell and the source.

## Pass 4: structural sanity

- Ids: 341 ids, all unique. No duplicates.
- Anchors: the volume has no nav block and no in-page anchors. The single link is a relative internal link to volume-question-bank.html. Nothing dangles.
- Dashes in learner text: 0 em dashes, 0 en dashes.
- External URLs: 0.
- Image references: 37 img tags, all resolve to files that exist. 3 files have no reference: ad-cache-key-1.png, ad-path-exec-1.png, ad-rag-layers-1.png. All three pass the visual spec, but no figure points at them.
- Labels: "original exam-style practice" appears 23 times. The text never claims authentic AWS questions. No ordering or matching items exist.

## Fix list

1. Regenerate the 14 failed images with claim titles, computed numbers, and no meta text.
2. Wire the 3 orphan images into the addendum, or drop them from assets.
3. Fix "Q&.A" to "Q&A" in Q35.
4. Optional: soften the Q23 explanation on the Lambda limit, and note the Q5 cardinality.

# AIP-C01 v2: Two Paths - Crash-Course vs Deep-Reference (Stage 1)

Research date: 2026-10-06.

## Crash-course path (shortest defensible route through all 98 blueprint skills)

Proposed lesson order with skill coverage. Every lesson carries a mandatory link to its deep-reference counterpart (exact file mapping below).

| Lesson slot | Title | Blueprint skills covered | Prereqs taught just-in-time |
|---|---|---|---|
| L0 | Foundation ramp: AI basics + AWS compute/storage/network/IAM/observability minimums | (prereqs only: P1, P5, P6, P7, P8 one-liner) | P1, P5, P6, P7 |
| L1 | D1: Requirements, model selection, resilience, customization lifecycle | 1.1.1-1.1.3, 1.2.1-1.2.4 | P1 callback |
| L2 | D1: Data validation and processing pipelines | 1.3.1-1.3.4 | P6 callback |
| L3 | D1: Vector stores and retrieval mechanisms (RAG core) | 1.4.1-1.4.5, 1.5.1-1.5.6 | P7 embedding refresher inside lesson |
| L4 | D1: Prompt engineering, management, and governance | 1.6.1-1.6.6 | P3 pointer (full teach in D3) |
| L5 | D2: Agentic AI - agents, safeguards, human-in-the-loop, MCP | 2.1.1-2.1.7, 2.5.5 | P5 callback, P6 callback |
| L6 | D2: Model deployment strategies and FM API integrations | 2.2.1-2.2.3, 2.4.1-2.4.4, 2.5.1 | P5 decision ladder |
| L7 | D2: Enterprise integration, CI/CD, GenAI gateway, dev tools | 2.3.1-2.3.5, 2.5.2-2.5.4, 2.5.6 | P2 pointer, P3 pointer |
| L8 | D3: Input/output safety controls and defense in depth | 3.1.1-3.1.5 | (Guardrails decision matrix is the core of this lesson) |
| L9 | D3: Data security, privacy, governance, compliance, responsible AI | 3.2.1-3.2.3, 3.3.1-3.3.4, 3.4.1-3.4.3 | P2 (full teach), P3 (full teach), P4 (full teach) |
| L10 | D4: Cost optimization, performance, monitoring | 4.1.1-4.1.4, 4.2.1-4.2.6, 4.3.1-4.3.6 | P8 (full teach) |
| L11 | D5: Evaluation systems and troubleshooting | 5.1.1-5.1.9, 5.2.1-5.2.5 | P8 callback |
| L12 | Worked-scenario drills: most-correct-answer walkthroughs across all domains | (synthesis of 1.1.1, 2.x, 3.x decision ladders) | none new |

## Deep-reference path (existing volumes, already built)

All files live in ~/workspace/your_files/aws-aip-c01-cert/.

## Crash-course to deep-reference mapping (exact file per lesson)

| Crash lesson | Deep-reference file(s) | Notes |
|---|---|---|
| L0 | prereq-aws-cloud-foundations.html (AWS basics), prereq-ml-specialty.html (AI basics), prereq-aif-c01.html (AI on AWS basics) | Split the ramp across the three prereq volumes; no single D-volume covers this |
| L1 | volume-d1-foundation-models.html | Requirements, model selection, resilience, customization |
| L2 | volume-d1-foundation-models.html | Data pipeline sections |
| L3 | volume-d1-foundation-models.html | Vector store + retrieval sections (the D1 volume's core) |
| L4 | volume-d1-foundation-models.html | Prompt engineering sections |
| L5 | volume-d2-implementation-integration.html | Agent sections; volume-maarek-labs.html for hands-on agent labs |
| L6 | volume-d2-implementation-integration.html | Deployment and API sections |
| L7 | volume-d2-implementation-integration.html | Enterprise integration sections |
| L8 | volume-d3-safety-security-governance.html | Safety controls sections |
| L9 | volume-d3-safety-security-governance.html | Security, privacy, governance, responsible AI sections |
| L10 | volume-d4-optimization.html | Cost, performance, monitoring |
| L11 | volume-d5-testing-validation.html | Evaluation and troubleshooting |
| L12 | volume-question-bank.html | Scenario drills; volume-maarek-labs.html for hands-on; volume-appendix-gaps.html for topics the D-volumes under-covered |

## How the two paths relate

- The crash course is the exam-passing route: every blueprint skill, mechanism + decision rule + application example + diagnostic, in ~12 lessons.
- The deep-reference volumes are the "why underneath": full detail, labs, appendices. A crash-course lesson that a learner fails twice routes them to the matching volume section before re-attempt.
- The question bank volume (volume-question-bank.html) supplies the assessment layer for both paths; the practice-question IDs column in coverage-ledger-v2.md is filled from it at build time.

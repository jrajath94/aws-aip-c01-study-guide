# AIP-C01 treatise: audit

## Decision

The treatise is usable for overnight reading and a printout. It is not yet verified line by line. Read the domain tables and the "Not in source" items before you rely on them for an answer.

## Files

| File | Use | Size |
|---|---|---|
| aip-c01-print-2up.pdf | Print. Letter landscape, 78 sides, two 5.5 x 8.5 in pages per side | 9.8 MB |
| aip-c01-print.docx | Edit. Page size 5.5 x 8.5 in, 0.5 in margins | 3.9 MB |
| print.html | Source for both files | 269 KB |

## Print settings

1. Open aip-c01-print-2up.pdf.
2. Print at 100 percent scale. Do not fit to page.
3. Turn on two-sided printing.
4. Choose the flip edge that gives a book layout in landscape view. Print sheet 1 first and check it.
5. Print sheets 1 to 39 with two-sided printing, or sides 1 to 78 with one-sided printing.

The file has 156 pages on 78 sides. Every side holds two pages. The file has no blank page.

## Coverage

| Item | Count | Note |
|---|---|---|
| Learning units | 79 | Each unit has a "I understand this unit" check in the web view. |
| Diagrams | 87 | Built as SVG for this treatise. Not AWS images. |
| Official AWS images | 36 files | Each caption names its source page. |
| Exam trap callouts | 120 | Each trap names the wrong answer AWS uses. |
| Major sections | 16 | Exam, reading, atlas, course, services, units, practical, domains 1 to 5, traps, method, gaps. |
| "Not in source" markers | 44 | The official page did not confirm the claim, or no official step exists. |

## Checks done

- Rendered the full print file. Found 153 half-letter pages and no blank page.
- Found one page with a screenshot and no text. It is valid content.
- Reworded unit claims that the official pages did not confirm.
- Added console and API steps for the practical topics, with official screenshots where AWS published one.
- Set PDF and DOCX author, title, creator, and producer to "Author".

## Verdict

Not yet. Most exam facts are confirmed. Official sample questions are still not found. Several console and pricing details are still Not in source.

## Checks done

- Domain weights, exam counts, pass mark, length, and fee match the official AWS pages.
- Every task number in the treatise exists in the official guide. Each domain reference matches its domain.
- Units 55 to 68 were checked against the official task statements. Seven exam-tie lines were corrected.
- Kendra, Q Business, SageMaker Model Monitor, and Bedrock Agents Classic are closed to new customers. The treatise states this correctly.
- The 200 repo questions were parsed. Eleven terms in their answers were missing from the treatise. Each now has a section (8A) with an official source, except BLEU, ROUGE, and Pricing. Those stay Not in source.
- All 391 domain and reference table rows were read. Three rows still said "No unit yet" after units 55 to 57 were added. Those labels are removed.
- The batch discount claim was not on the official batch docs page. The treatise now says Not in source for the exact percentage. Batch is not supported for provisioned models. The treatise now says so.
- ElastiCache durability matches the official durability page. Durability needs node-based clusters.

## Sample questions

- The official exam guide (docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html) has no sample question section.
- The official AWS certification page (aws.amazon.com/certification/certified-generative-ai-developer-professional/) lists an "AWS Certification Official Practice Question Set" and an "Official Practice Exam". It does not say whether either covers AIP-C01. Not in source.
- The Skill Builder exam-prep page (skillbuilder.aws/category/exam-prep/generative-ai-developer-professional-AIP-C01) did not load in this build. The contents of the practice set are Not in source.
- Searches returned third-party banks only. Their accuracy is unverified, and some sites offer leaked "dumps". They are not used here.

## Checks done on console steps

- Provisioned Throughput purchase: console steps confirmed (section 8B).
- Lambda timeout: default 3 seconds, maximum 900 seconds, console and CLI steps confirmed (section 8B).
- SageMaker Model Registry approval: console and API steps confirmed (section 8B).
- Guardrail creation: the official page fetched did not show steps. Still Not in source.


## Master content scope (this pass)

- Gemini question set (250+ questions): not found. The repo, its branches, and origin/main have no such set. Upload it to check it.
- Branch codex/aip-c01-visual-course: not on origin for aws-aip-c01-study-guide. It may sit in another repo, which this session cannot reach. Not checked.
- Branch cursor/visual-treatise-3ba5: reachable. It holds eleven volumes and the same 200-question bank. Heading screen: 1,739 headings. 47 have no keyword match in the master. Most are verification logs, a glossary, and a cheat sheet. The master now has a glossary (section 8C). Real topic gaps still open: binary vectors and FP16 quantization, transparency as a design topic, red-teaming basics with AWS tooling, security hardening chapter, and decision ladders chapter. The keyword screen is weak. It does not check claims.
- Question check: the 200-question bank was checked earlier by term. Eleven terms were missing. Section 8A covers nine. Two stay Not in source.
- Confidence the master covers the exam alone: 3 of 10. The exam has 75 questions. The sample sets were not available. The official sample questions are not in source.

## Checks not done

- The remaining "Not in source" items. Most are console-field gaps in the practical units. The official pages fetched did not answer them.
- Official sample questions. The practice set is named but not available in this build.
- Table rows were checked for consistency. Most claims were not fetched one by one.
- API Gateway 29 second integration timeout. Not on the quotas page.
- Knowledge Base web crawler end date. Not on the docs page.
- Several units give design guidance, not AWS facts. Those units say so.
- The brand font is not installed. The files use Inter.
- The publication-clean and watermark-remover skills are not present in this environment, so no watermark pass ran.

## Gaps for the exam

- Many topics have no console steps. Those topics say "Not in source."
- The treatise does not replace official sample questions. Work the AWS sample questions before the exam.

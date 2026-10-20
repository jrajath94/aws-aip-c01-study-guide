# AIP-C01 treatise: audit

## Decision

The treatise is usable for overnight reading and a printout. It is not yet verified line by line. Read the domain tables and the "Not in source" items before you rely on them for an answer.

## Files

| File | Use | Size |
|---|---|---|
| aip-c01-print-2up.pdf | Print. Letter landscape, 77 sides, two 5.5 x 8.5 in pages per side | 9.8 MB |
| aip-c01-print.docx | Edit. Page size 5.5 x 8.5 in, 0.5 in margins | 3.9 MB |
| print.html | Source for both files | 269 KB |

## Print settings

1. Open aip-c01-print-2up.pdf.
2. Print at 100 percent scale. Do not fit to page.
3. Turn on two-sided printing.
4. Choose the flip edge that gives a book layout in landscape view. Print sheet 1 first and check it.
5. Print sheets 1 to 77.

Side 77 holds one page only. The right half of that side is blank. The file has no blank page.

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

Not yet. The exam facts and service status are now confirmed. The bank coverage, domain tables, and official sample questions are not closed.

## Checks done

- Domain weights (31, 26, 20, 12, 11 percent) match the official AWS exam guide.
- The exam has 75 questions: 65 scored and 10 unscored. The pass mark is 750 on a 100 to 1,000 scale. The official guide confirms both.
- The exam length is 180 minutes. The fee is 300 USD. The official AWS certification page confirms both.
- Every task number in the treatise (1.1 to 5.2) exists in the official guide. Each "Domain N task X.Y" reference matches its domain.
- Units 55 to 68 were checked against the official task statements. Five exam-tie lines were corrected.
- Amazon Kendra, Amazon Q Business, SageMaker Model Monitor, and Bedrock Agents Classic are closed to new customers. The treatise states this correctly for each.
- The 200 repo questions were parsed. Terms in their answer explanations were compared with the treatise text. Eleven terms are absent: CloudFormation, Textract, Cognito, Clarify, continued pre-training, top-p, max tokens, BLEU, ROUGE, Verified Permissions, and Pricing. Twenty-two questions use at least one of them.

## Checks not done

- Official sample questions. None were found. Search returns third-party banks only.
- Domain tables. Task numbers are checked. Claims are not checked line by line against the official skill wording.
- Question-to-unit mapping. The term check above is not a per-question map.
- The 44 "Not in source" items. Most are console-field gaps in the practical units, or per-domain sample-question gaps. None were closed.
- API Gateway 29 second integration timeout. Not confirmed on the quotas page in this build.
- Knowledge Base web crawler date (after 2026-09-30). It comes from one search result. Not confirmed.
- Several units give design guidance, not AWS facts. Those units say so.
- The brand font is not installed. The files use Inter.
- The publication-clean and watermark-remover skills are not present in this environment, so no watermark pass ran.

## Gaps for the exam

- Many topics have no console steps. Those topics say "Not in source."
- The treatise does not replace official sample questions. Work the AWS sample questions before the exam.

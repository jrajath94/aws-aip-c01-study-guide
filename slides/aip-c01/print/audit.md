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
5. Print sheets 1 to 78.

Side 78 holds one page only. The right half of that side is blank. The file has no blank page.

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

## Checks not done

- Official sample questions. None were found. Search returns third-party banks only.
- Table rows were read for consistency. Four rows were then fetched and checked: intelligent prompt routing, CloudWatch metric names, Provisioned Throughput billing, and the Comprehend size limit. Three were confirmed. The Comprehend row was corrected. The PII-only limit is Not in source as a separate line.
- The 44 "Not in source" items. Most are console-field gaps in the practical units. The official pages fetched in this pass did not answer them. Resolving them needs the console pages, which this build could not read.
- API Gateway 29 second integration timeout. The quotas page does not list it. It stays Not in source.
- Knowledge Base web crawler end date. The docs page gave no date. It stays Not in source.
- Whether Amazon Bedrock uses prompts for model training is resolved. The Bedrock FAQ says no, for Amazon Nova, Amazon Titan, and third-party models.
- Several units give design guidance, not AWS facts. Those units say so.
- The brand font is not installed. The files use Inter.
- The publication-clean and watermark-remover skills are not present in this environment, so no watermark pass ran.

## Gaps for the exam

- Many topics have no console steps. Those topics say "Not in source."
- The treatise does not replace official sample questions. Work the AWS sample questions before the exam.

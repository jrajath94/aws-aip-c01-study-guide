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

## Checks done on the exam facts

- Domain weights (31, 26, 20, 12, 11 percent) match the official AWS exam guide.
- The exam has 65 scored and 10 unscored questions. The pass mark is 750 on a 100 to 1,000 scale. The official guide confirms both.
- Every task number in the treatise (1.1 to 5.2) exists in the official guide. Each "Domain N task X.Y" reference matches its domain.
- Units 55 to 68 were checked against the official task statements. Four exam-tie lines were corrected. Unit 55 now cites tasks 1.3, 3.1, and 5.2. Unit 57 now cites task 1.5. Unit 61 now cites task 1.4. Unit 64 now cites tasks 3.2 and 3.3. Unit 66 now cites tasks 3.3 and 3.4.

## Checks not done

- The domain tables are checked for task numbers only. Their claims are not checked line by line against the official skill wording.
- Exam length (180 minutes in the repo README, 130 minutes in a third-party guide) and the 300 USD fee are Not in source on the official guide page.
- The API Gateway 29 second integration timeout is a default. It is not confirmed in this build.
- The Knowledge Base web crawler change after 2026-09-30 comes from one search result. Confirm it before the exam.
- Model Monitor status, and the closure status of Amazon Q Business, Amazon Kendra, and Bedrock Agents Classic, need a current check.
- Several units give design guidance, not AWS facts. Those units say so.
- The brand font is not installed. The files use Inter.
- The publication-clean and watermark-remover skills are not present in this environment, so no watermark pass ran.

## Gaps for the exam

- Many topics have no console steps. Those topics say "Not in source."
- The treatise does not replace official sample questions. Work the AWS sample questions before the exam.

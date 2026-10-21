# AIP-C01 visual study course

Open the [complete HTML treatise](output/AIP-C01-Visual-Treatise.html).
Reader: A candidate who needs first-principles explanations and two-day exam review.

## Files

| File | Use |
|---|---|
| [HTML treatise](output/AIP-C01-Visual-Treatise.html) | Offline study, diagrams, practical walkthroughs, source archive, and interactive questions |
| [Core print book](output/AIP-C01-Core-Two-Up.pdf) | Complete authored course, skill cases, practical procedures, and architecture reference |
| [Practice booklet](output/AIP-C01-Practice-Two-Up.pdf) | 250 extracted questions with reviewed corrections |
| [Word book](output/AIP-C01-Study-Book.docx) | Editable course and practice appendix |
| [Final audit](output/AIP-C01-Audit.md) | Coverage evidence, limitations, and print procedure |

The HTML includes 24 chapters, 98 skill cases, 24 practical walkthroughs, 17 official diagrams, and 11 official console screenshots.
It also includes 439 source sections, 250 interactive questions, 541 recall cards, and a timed mock.
The source archive remains separate from the authored course.
Use the linked core print book for the complete authored curriculum.

## Print

1. Open the two-up core PDF.
2. Select landscape US Letter.
3. Select actual size.
4. Select one PDF page per printed side.
5. Select duplex with short-edge flip.
6. Print a test sheet.

Each printed side already contains two logical pages.
The core book uses 58 duplex sheets.
Print the separate practice booklet only when needed.
Use the HTML enlargement control for dense source diagrams.

## Scope

The course maps all 98 published skills.
The audit does not certify undisclosed exam coverage or a passing result.
The official practice set requires sign-in, so its hidden question bodies remain unaudited.
Eight unsettled keys remain discussion cases. The timed mock excludes them.
Proposed lab procedures do not prove hands-on competence.

The file review checks known Unicode carriers and supported metadata indicators.
Pixel and proprietary statistical watermarks remain unverified.
Clear metadata locally before external upload.

## Rebuild

Run `scripts/build_course.py` with Beautiful Soup available.
Run `scripts/export_study_book.py` with python-docx, ReportLab, pypdf, Pillow, and lxml available.
Run `scripts/package_treatise.py` to create a standalone HTML source for file cleanup.
The exporter embeds the local Anthropic Sans fonts.
The source originals remain preserved.

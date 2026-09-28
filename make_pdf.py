#!/usr/bin/env python3
"""Build combined hyperlinked PDF for AIP-C01 (CCAR-P's PDF goes first per user order;
this builds ours so it's ready for the zip; delivery sequencing noted in report)."""
import os, re, sys
from bs4 import BeautifulSoup

TRACK = os.path.expanduser("~/workspace/your_files/aws-aip-c01-cert")
PAGES = [
    ("index", "index.html", "Study Guide Home"),
    ("d1", "volume-d1-foundation-models.html", "D1 · Foundation Model Integration, Data Management, and Compliance (31%)"),
    ("d2", "volume-d2-implementation-integration.html", "D2 · Implementation and Integration (26%)"),
    ("d3", "volume-d3-safety-security-governance.html", "D3 · AI Safety, Security, and Governance (20%)"),
    ("d4", "volume-d4-optimization.html", "D4 · Operational Efficiency and Optimization (12%)"),
    ("d5", "volume-d5-testing-validation.html", "D5 · Testing, Validation, and Troubleshooting (11%)"),
    ("bank", "volume-question-bank.html", "Question Bank + 75-Question Mock Exam (192 questions)"),
    ("patterns", "volume-question-patterns.html", "How AWS Asks: Pattern Guide + Original Questions"),
    ("design", "volume-system-design.html", "System Design Guide"),
    ("labs", "volume-maarek-labs.html", "Hands-On Labs (Maarek Course Labs)"),
    ("appendix", "volume-appendix-gaps.html", "Gap Appendix: Peripheral Services"),
]

sections = []
for slug, fname, title in PAGES:
    soup = BeautifulSoup(open(os.path.join(TRACK, fname), encoding="utf-8", errors="replace").read(), "html.parser")
    content = soup.select_one("#ds-content .ds-content-inner") or soup.select_one("#ds-content")
    html = str(content)
    # prefix ids + anchor hrefs so they're unique document-wide
    html = re.sub(r'id="([a-zA-Z0-9][a-zA-Z0-9\-_]*)"', lambda m: 'id="%s-%s"' % (slug, m.group(1)), html)
    html = re.sub(r'href="#([a-zA-Z0-9][a-zA-Z0-9\-_]*)"', lambda m: 'href="#%s-%s"' % (slug, m.group(1)), html)
    sections.append((slug, title, html))

toc_items = "\n".join(
    '<li><a href="#pdf-%s">%s</a></li>' % (slug, title) for slug, title, _ in sections)

body_sections = "\n".join(
    '<section class="pdf-vol" id="pdf-%s">\n<h1 class="pdf-vol-title">%s</h1>\n%s\n</section>' % (slug, title, html)
    for slug, title, html in sections)

out = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>AWS Certified Generative AI Developer - Professional (AIP-C01) Study Guide</title>
<base href="file://%s/">
<style>
  /* cover + TOC for print */
  .pdf-cover { page-break-after: always; text-align: center; padding-top: 180px; }
  .pdf-cover p { text-align: center !important; }
  .pdf-cover h1 { font-size: 28pt; margin-bottom: 12pt; }
  .pdf-cover p { font-size: 12pt; color: #444; }
  .pdf-toc { page-break-after: always; }
  .pdf-toc h2 { font-size: 20pt; margin-bottom: 16pt; }
  .pdf-toc ol { font-size: 12pt; line-height: 2.2; }
  .pdf-vol { page-break-before: always; }
  .pdf-vol-title { font-size: 22pt; border-bottom: 3px solid #f0b429; padding-bottom: 8pt; margin-bottom: 20pt; }
  @media print { .pdf-vol:first-of-type { page-break-before: avoid; } }
</style>
</head>
<body>
<div class="pdf-cover">
  <h1>AWS Certified Generative AI Developer &ndash; Professional</h1>
  <p><strong>(AIP-C01) Complete Study Guide</strong></p>
  <p>11 volumes &middot; 192 exam-style questions &middot; 75-question mock exam &middot; system design guide &middot; hands-on labs</p>
  <p>Verified exam identity: 75 questions (65 scored + 10 unscored), 180 min, pass 750/1000, $300</p>
  <p>Built September 28, 2026 &middot; self-contained, generic learning content</p>
</div>
<div class="pdf-toc">
  <h2>Contents</h2>
  <ol>%s</ol>
  <p>Tip: every entry above is a hyperlink &mdash; click to jump straight to that volume.</p>
</div>
%s
</body></html>""" % (TRACK, toc_items, body_sections)

# reuse the built page shell: copy head styles/scripts from index.html
idx = BeautifulSoup(open(os.path.join(TRACK, "index.html"), encoding="utf-8", errors="replace").read(), "html.parser")
shell = BeautifulSoup(out, "html.parser")
head = shell.head
for tag in idx.head.find_all(["style", "link"]):
    head.append(tag.__copy__() if hasattr(tag, "__copy__") else tag)
# append ds print-friendly: hide sidebar root etc. (already in ds.css print rules)

combined_path = os.path.join(TRACK, "aip-c01-combined-print.html")
open(combined_path, "w", encoding="utf-8").write(str(shell))
print("combined html:", os.path.getsize(combined_path), "bytes")

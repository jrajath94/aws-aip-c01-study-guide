#!/usr/bin/env python3
"""Print aip-c01-combined-print.html to PDF via headless Chromium, then strip metadata."""
import os, sys
from playwright.sync_api import sync_playwright

TRACK = os.path.expanduser("~/workspace/your_files/aws-aip-c01-cert")
SRC = os.path.join(TRACK, "aip-c01-combined-print.html")
OUT = os.path.join(TRACK, "AIP-C01-Study-Guide.pdf")

with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/meta-chromium/chrome", args=["--no-sandbox", "--disable-dev-shm-usage"])
    pg = b.new_page()
    pg.goto("file://" + SRC, wait_until="networkidle")
    pg.pdf(path=OUT, format="Letter", print_background=True,
           display_header_footer=True,
           header_template="<span></span>",
           footer_template='<span style="font-size:8pt;color:#666;width:100%;text-align:center"><span class="pageNumber"></span> / <span class="totalPages"></span></span>',
           margin={"top": "18mm", "bottom": "18mm", "left": "14mm", "right": "14mm"})
    b.close()
print("pdf:", os.path.getsize(OUT), "bytes")

# strip Producer/Creator metadata via pypdf, keep title
from pypdf import PdfReader, PdfWriter
r = PdfReader(OUT)
w = PdfWriter()
for page in r.pages:
    w.add_page(page)
if r.metadata and r.metadata.title:
    w.add_metadata({"/Title": r.metadata.title})
    # remove pypdf's default producer stamp
    w._info.get_object().pop("/Producer", None)
tmp = OUT + ".clean"
with open(tmp, "wb") as f:
    w.write(f)
os.replace(tmp, OUT)
r2 = PdfReader(OUT)
print("producer:", r2.metadata.producer, "| creator:", r2.metadata.creator,
      "| title:", r2.metadata.title, "| pages:", len(r2.pages))

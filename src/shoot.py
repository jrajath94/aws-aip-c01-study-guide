#!/usr/bin/env python3
"""Screenshot QA: render each AIP-C01 page at 3 widths, detect container spill."""
import os, sys, json
from playwright.sync_api import sync_playwright

TRACK = os.path.expanduser("~/workspace/your_files/aws-aip-c01-cert")
OUT = os.path.expanduser("~/workspace/your_files/aws-aip-c01-cert/.qa-shots")
os.makedirs(OUT, exist_ok=True)
PAGES = ["index.html", "volume-d1-foundation-models.html", "volume-d2-implementation-integration.html",
         "volume-d3-safety-security-governance.html", "volume-d4-optimization.html",
         "volume-d5-testing-validation.html", "volume-maarek-labs.html",
         "volume-question-bank.html", "volume-question-patterns.html",
         "volume-system-design.html", "volume-appendix-gaps.html"]
WIDTHS = [1440, 768, 390]

SPILL_JS = """() => {
  const bad = [];
  const inner = document.querySelector('#ds-content .ds-content-inner') || document.querySelector('#ds-content');
  if (!inner) return ['no-content'];
  const cw = inner.getBoundingClientRect().width;
  document.querySelectorAll('#ds-content p, #ds-content li, #ds-content pre, #ds-content table, #ds-content img, #ds-content .pq, #ds-content figure').forEach(el => {
    if (el.closest('.table-wrap')) return;  // tables scroll inside their wrapper by design
    const r = el.getBoundingClientRect();
    if (r.width > cw + 2) {
      bad.push(el.tagName + '.' + (el.className || '').toString().slice(0,40) + ' w=' + Math.round(r.width) + ' > col=' + Math.round(cw) + ' :: ' + (el.textContent||'').slice(0,60));
    }
  });
  return bad.slice(0, 20);
}"""

results = {}
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/usr/bin/google-chrome",
                                args=["--no-sandbox", "--disable-dev-shm-usage"])
    for page in PAGES:
        results[page] = {}
        for w in WIDTHS:
            ctx = browser.new_context(viewport={"width": w, "height": 900},
                                      device_scale_factor=1)
            pg = ctx.new_page()
            pg.goto("file://" + os.path.join(TRACK, page))
            pg.wait_for_timeout(1200)
            h = pg.evaluate("document.body.scrollHeight")
            shot = os.path.join(OUT, page.replace(".html", "") + f"-{w}.png")
            try:
                if w == 1440 and h < 30000:
                    pg.screenshot(path=shot, full_page=True)
                elif w == 1440:
                    # very tall page: top + a figure section + bottom
                    pg.screenshot(path=shot)
                    fig = pg.evaluate("""() => { const f = document.querySelector('#ds-content figure');
                        if (!f) return null; const r = f.getBoundingClientRect();
                        return r.top + window.scrollY; }""")
                    if fig:
                        pg.evaluate(f"window.scrollTo(0, {max(0, fig - 200)})")
                        pg.wait_for_timeout(400)
                        pg.screenshot(path=shot.replace(".png", "-fig.png"))
                    pg.evaluate(f"window.scrollTo(0, {h})")
                    pg.wait_for_timeout(400)
                    pg.screenshot(path=shot.replace(".png", "-bottom.png"))
                else:
                    pg.screenshot(path=shot)
            except Exception as e:
                print(f"  screenshot failed: {str(e)[:80]}")
            spill = pg.evaluate(SPILL_JS)
            hscroll = pg.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
            results[page][w] = {"shot": shot, "spill": spill, "hscroll": hscroll}
            print(f"{page} @ {w}: spill={len(spill)} hscroll={hscroll}")
            for s in spill[:5]:
                print("   ", s)
            ctx.close()
    browser.close()

json.dump(results, open(os.path.join(OUT, "results.json"), "w"), indent=1)
print("done ->", OUT)

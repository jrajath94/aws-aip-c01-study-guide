#!/usr/bin/env python3
"""html2md.py — mechanically convert themed AIP-C01 HTML volumes to Markdown sources.

Reads the canonical-DS HTML (built by themer.py), walks #ds-content, and emits
src/volumes/<slug>.md with YAML front-matter plus :::directives the build.py
renderer understands.

Directives:
  :::exam-ask / :::takeaway / :::panel     — callout blocks
  :::pq                                     — reveal-answer question widget
  :::ladder                                 — numbered decision ladder
  :::walkthrough                            — "how to read this diagram" steps
  :::volumes                                — index volume cards (from manifest)
  :::figure <src>                           — image with caption/credit

Usage: python3 src/html2md.py [file.html ...]   (default: all volumes except
question-bank, which is being rewritten by the auditor — convert it after)
"""
import re, sys, glob, os, html as ihtml
from bs4 import BeautifulSoup, NavigableString

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_VOL = os.path.join(ROOT, "src", "volumes")
os.makedirs(SRC_VOL, exist_ok=True)

SKIP_FILES = set()

# ---------------------------------------------------------------- inline ---

def inline(node):
    """Render phrasing content of a node as Markdown."""
    parts = []
    for ch in node.children:
        parts.append(inline_node(ch))
    return "".join(parts).strip()

def inline_node(ch):
    if isinstance(ch, NavigableString):
        t = str(ch)
        # collapse whitespace runs but keep single spaces
        return re.sub(r"[ \t\r\f\v]+", " ", t)
    name = ch.name
    if name in ("strong", "b"):
        return "**" + inline(ch) + "**"
    if name in ("em", "i"):
        return "*" + inline(ch) + "*"
    if name == "code":
        t = inline(ch)
        return "`" + t + "`" if "`" not in t else "`` " + t + " ``"
    if name in ("kbd", "samp", "var"):
        return "`" + inline(ch) + "`"
    if name == "a":
        href = ch.get("href", "")
        txt = inline(ch) or href
        if ch.get("id") and not txt.strip():
            return '<a id="%s"></a>' % ch["id"]
        return "[%s](%s)" % (txt, href)
    if name == "br":
        return "  \n"
    if name == "img":
        alt = ch.get("alt", "")
        src = ch.get("src", "")
        return "![%s](%s)" % (alt, src)
    if name in ("sub", "sup"):
        return "<%s>%s</%s>" % (name, inline(ch), name)
    if name == "span":
        cls = ch.get("class") or []
        if "def" in cls:
            return "**" + inline(ch) + "**"
        return inline(ch)
    if name in ("abbr", "cite", "dfn", "mark", "small", "time", "u"):
        return inline(ch)
    # unknown inline: unwrap
    if ch.name:
        return inline(ch)
    return ""

# ---------------------------------------------------------------- blocks ---

class Ctx:
    def __init__(self):
        self.out = []
        self.warnings = []

    def emit(self, text=""):
        self.out.append(text)

def md_table(table):
    rows = []
    for tr in table.find_all("tr"):
        cells = [inline(td).replace("\n", " ") for td in tr.find_all(["th", "td"])]
        rows.append(cells)
    if not rows:
        return ""
    # escape pipes outside backticks
    def esc(cell):
        out, in_bt, buf = [], False, ""
        for ch in cell:
            if ch == "`":
                in_bt = not in_bt
                buf += ch
            elif ch == "|" and not in_bt:
                buf += "\\|"
            else:
                buf += ch
        return buf.strip()
    rows = [[esc(c) for c in r] for r in rows]
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    lines = ["| " + " | ".join(rows[0]) + " |",
             "|" + "|".join(["---"] * width) + "|"]
    for r in rows[1:]:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)

def convert_pre(pre):
    code = pre.find("code")
    lang = ""
    if code:
        for cl in code.get("class") or []:
            if cl.startswith("language-"):
                lang = cl[len("language-"):]
    txt = pre.get_text()
    # strip trailing newline noise, keep interior
    txt = txt.strip("\n")
    return "```" + lang + "\n" + txt + "\n```"

def extract_qstem(qstem_div):
    """Return (stem_paras, opts) from a div.qstem (or similar wrapper)."""
    stem_paras, opts = [], []
    ol = qstem_div.find(["ol", "ul"], class_="opts")
    for ch in qstem_div.children:
        nm = getattr(ch, "name", None)
        if nm == "p":
            stem_paras.append(inline(ch))
        elif nm == "pre":
            stem_paras.append(convert_pre(ch))
        elif nm in ("ol", "ul") and "opts" in (ch.get("class") or []):
            for li in ch.find_all("li", recursive=False):
                opts.append(inline(li).strip())
    if ol is None and not opts:
        # maybe opts list without class
        for lst in qstem_div.find_all(["ol", "ul"], recursive=False):
            lis = lst.find_all("li", recursive=False)
            if lis and re.match(r"^[A-H]\.", inline(lis[0]).strip()):
                for li in lis:
                    opts.append(inline(li).strip())
                break
    return stem_paras, opts

def convert_pq_div(div, ctx, fname):
    """Auditor's canonical form: div.pq > p.pq-question + button + div.pq-answer(ul.pq-options)."""
    pid = div.get("id")
    lines = [":::pq" + (" {#%s}" % pid if pid else "")]
    q = div.find("p", class_="pq-question")
    if q:
        constraints = [sp.get_text(strip=True) for sp in q.find_all("span", class_="constraint")]
        # muted id/blueprint span (not a constraint)
        blue = ""
        for sp in q.find_all("span"):
            if "constraint" not in (sp.get("class") or []):
                t = sp.get_text(" ", strip=True)
                if t:
                    blue = t
                sp.decompose()
        for sp in q.find_all("span", class_="constraint"):
            sp.decompose()
        stem = inline(q).strip()
        # strip leading "Q12." — keep it, it's the question number
        lines.append("")
        if constraints:
            meta = "*" + " · ".join(constraints) + "*"
            if blue:
                meta += " — " + blue
            lines.append(meta)
            lines.append("")
        lines.append(stem)
    else:
        ctx.warnings.append("%s: div.pq without pq-question" % fname)
    ans = div.find("div", class_="pq-answer")
    if ans:
        opt_ul = ans.find("ul", class_="pq-options")
        opts = []
        if opt_ul:
            for li in opt_ul.find_all("li", recursive=False):
                licls = li.get("class") or []
                is_c = "correct" in licls
                note_el = li.find("span", class_="pq-note")
                note = inline(note_el).strip() if note_el else ""
                if note_el:
                    note_el.decompose()
                strong = li.find("strong")
                letter = ""
                if strong:
                    m = re.match(r"\s*([A-H])\)", strong.get_text())
                    if m:
                        letter = m.group(1)
                    strong.decompose()
                text = inline(li).strip()
                opts.append((letter, text, note, is_c))
            opt_ul.decompose()
        # correctness fallback from answer text if no li marked correct
        ans_text = ans.get_text(" ", strip=True)
        if not any(c for _, _, _, c in opts):
            m = re.search(r"Why ([A-Z](?:\s*(?:and|,|&)\s*[A-Z])*) is correct", ans_text)
            if m:
                stated = set(re.findall(r"[A-Z]", m.group(1)))
                opts = [(l, t, n, l in stated) for l, t, n, c in opts]
            else:
                ctx.warnings.append("%s: pq %s has no correct option" % (fname, pid))
        if opts:
            lines.append("")
            for letter, text, note, is_c in opts:
                mark = " <!-- correct -->" if is_c else ""
                lines.append("- %s. %s%s" % (letter, text, mark))
                if note:
                    lines.append("  > %s" % note)
        lines.append("")
        for ch in ans.children:
            nm = getattr(ch, "name", None)
            if nm == "p":
                lines.append(inline(ch))
                lines.append("")
            elif nm in ("ul", "ol"):
                for li in ch.find_all("li", recursive=False):
                    lines.append("- " + inline(li))
                lines.append("")
    else:
        ctx.warnings.append("%s: div.pq without pq-answer" % fname)
    lines.append(":::")
    return "\n".join(lines).rstrip() + "\n"

def convert_pq(details, stem_paras, opts, ctx, fname):
    """details.pq / details.ans -> :::pq directive.
    stem_paras: list of markdown paragraphs (or None); opts: list of option strings (or None)."""
    lines = [":::pq" + (" {#%s}" % details.get("id") if details.get("id") else "")]
    if stem_paras:
        lines.append("")
        lines.extend(stem_paras)
    else:
        ctx.warnings.append("%s: pq without stem" % fname)
    # correctness from answer text
    ans_text = details.get_text(" ", strip=True)
    m = re.search(r"Correct:\s*([A-Z](?:\s*(?:and|,|&)\s*[A-Z])*)", ans_text)
    correct = set(re.findall(r"[A-Z]", m.group(1))) if m else set()
    if opts:
        lines.append("")
        for t in opts:
            letter = t[:1] if t[:1] in "ABCDEFGH" else ""
            mark = " <!-- correct -->" if letter in correct else ""
            lines.append("- " + t + mark)
        if not correct:
            ctx.warnings.append("%s: could not parse Correct: letters" % fname)
    else:
        ctx.warnings.append("%s: pq without options" % fname)
    lines.append("")
    for p in details.find_all(["p", "ul", "ol"], recursive=False):
        if p.name == "p":
            lines.append(inline(p))
        else:
            for li in p.find_all("li", recursive=False):
                lines.append("- " + inline(li))
        lines.append("")
    lines.append(":::")
    return "\n".join(lines).rstrip() + "\n"

def convert_ladder(div):
    lines = [":::ladder", ""]
    for i, rung in enumerate(div.select(".rung"), 1):
        n = rung.select_one(".rung-n")
        num = (n.get_text(strip=True) if n else str(i))
        inner = rung.find("div")
        b = inner.find("b") if inner else None
        title = inline(b) if b else ""
        rest = inner.find("span") if inner else None
        desc = inline(rest) if rest else ""
        lines.append("%s. **%s** — %s" % (num, title, desc))
    lines += ["", ":::"]
    return "\n".join(lines)

def convert_walkthrough(div):
    lines = [":::walkthrough", ""]
    head = div.find(["h2", "h3", "h4", "p", "strong"])
    items = div.find("ol") or div.find("ul")
    if head and (not items or div.find("ol").find_previous_sibling() == head):
        pass  # keep simple: just convert children as blocks below
    return None  # handled by generic path instead

def block_children(node, ctx, fname):
    for ch in node.children:
        block_node(ch, ctx, fname)

def block_node(node, ctx, fname):
    if isinstance(node, NavigableString):
        t = str(node).strip()
        if t:
            ctx.emit(t)
            ctx.emit("")
        return
    name = node.name
    cls = node.get("class") or []
    if name in ("script", "style"):
        return
    if name == "h1":
        ctx.emit("# " + inline(node) + (" {#%s}" % node["id"] if node.get("id") else ""))
        ctx.emit("")
    elif name in ("h2", "h3", "h4"):
        lvl = {"h2": "##", "h3": "###", "h4": "####"}[name]
        if "q" in cls:
            # question heading: badges -> italic meta line, title stays a heading
            badges = [b.get_text(strip=True) for b in node.find_all(class_="badge")]
            for b in node.find_all(class_="badge"):
                b.decompose()
            ctx.emit("%s %s%s" % (lvl, inline(node), " {#%s}" % node["id"] if node.get("id") else ""))
            ctx.emit("")
            if badges:
                ctx.emit("*%s*" % " · ".join(badges))
                ctx.emit("")
        else:
            ctx.emit("%s %s%s" % (lvl, inline(node), " {#%s}" % node["id"] if node.get("id") else ""))
            ctx.emit("")
    elif name == "p":
        t = inline(node)
        if re.fullmatch(r"[=─\-*~#]{5,}", t.strip()):
            ctx.emit("---")
        else:
            ctx.emit(t)
        ctx.emit("")
    elif name == "ul":
        for li in node.find_all("li", recursive=False):
            ctx.emit("- " + li_block(li, ctx, fname))
        ctx.emit("")
    elif name == "ol":
        for i, li in enumerate(node.find_all("li", recursive=False), 1):
            ctx.emit("%d. %s" % (i, li_block(li, ctx, fname)))
        ctx.emit("")
    elif name == "pre":
        ctx.emit(convert_pre(node))
        ctx.emit("")
    elif name == "blockquote":
        for line in inline(node).split("\n"):
            ctx.emit("> " + line)
        ctx.emit("")
    elif name == "hr":
        ctx.emit("---")
        ctx.emit("")
    elif name == "table":
        ctx.emit(md_table(node))
        ctx.emit("")
    elif name == "figure":
        img = node.find("img")
        cap = node.find("figcaption")
        if img:
            ctx.emit(":::figure %s" % img.get("src", ""))
            ctx.emit("")
            ctx.emit(img.get("alt", ""))
            if cap:
                ctx.emit("")
                ctx.emit("*" + inline(cap) + "*")
            ctx.emit(":::")
            ctx.emit("")
        else:
            block_children(node, ctx, fname)
    elif name == "img":
        ctx.emit("![%s](%s)" % (node.get("alt", ""), node.get("src", "")))
        ctx.emit("")
    elif name == "details" and ("pq" in cls or "ans" in cls):
        # grouped by parent loop; here = standalone (no stem/opts found)
        ctx.emit(convert_pq(node, None, None, ctx, fname))
        ctx.emit("")
    elif name == "details":
        summ = node.find("summary")
        ctx.emit(":::details %s" % (inline(summ) if summ else "More"))
        ctx.emit("")
        if summ:
            summ.decompose()
        block_children(node, ctx, fname)
        # strip trailing blank inside directive
        while ctx.out and ctx.out[-1] == "":
            ctx.out.pop()
        ctx.emit(":::")
        ctx.emit("")
    elif name == "div" and "pq" in cls:
        ctx.emit(convert_pq_div(node, ctx, fname))
        ctx.emit("")
    elif name == "div" and not cls and node.find("b", recursive=False):
        # intro panel: <div><b>Title.</b> prose...</div> -> :::panel
        if not node.find(["p", "ul", "ol", "pre", "table", "div"], recursive=False):
            ctx.emit(":::panel")
            ctx.emit("")
            ctx.emit(inline(node))
            ctx.emit("")
            ctx.emit(":::")
            ctx.emit("")
        else:
            block_children(node, ctx, fname)
    elif name == "div" and "exam-ask" in cls:
        ctx.emit(":::exam-ask")
        ctx.emit("")
        block_children(node, ctx, fname)
        while ctx.out and ctx.out[-1] == "":
            ctx.out.pop()
        ctx.emit(":::")
        ctx.emit("")
    elif name == "div" and "takeaway" in cls:
        ctx.emit(":::takeaway")
        ctx.emit("")
        block_children(node, ctx, fname)
        while ctx.out and ctx.out[-1] == "":
            ctx.out.pop()
        ctx.emit(":::")
        ctx.emit("")
    elif name == "div" and "ladder" in cls:
        ctx.emit(convert_ladder(node))
        ctx.emit("")
    elif name == "div" and "diagram-walkthrough" in cls:
        ctx.emit(":::walkthrough")
        ctx.emit("")
        block_children(node, ctx, fname)
        while ctx.out and ctx.out[-1] == "":
            ctx.out.pop()
        ctx.emit(":::")
        ctx.emit("")
    elif name == "div" and "table-wrap" in cls:
        tbl = node.find("table")
        if tbl:
            ctx.emit(md_table(tbl))
            ctx.emit("")
    elif name == "a" and "vol" in cls:
        # index volume card -> handled at page level; skip here
        return
    elif name in ("div", "section", "article", "main", "span", "figcaption"):
        block_children(node, ctx, fname)
    elif name == "a" and node.get("id") and not inline(node).strip():
        ctx.emit('<a id="%s"></a>' % node["id"])
        ctx.emit("")
    else:
        # unknown: try children, else inline as paragraph
        if list(node.find_all(["p", "ul", "ol", "pre", "table", "h2", "h3", "div"], recursive=False)):
            block_children(node, ctx, fname)
        else:
            t = inline(node)
            if t:
                ctx.emit(t)
                ctx.emit("")

def li_block(li, ctx, fname):
    """Render an <li>: first line inline, nested blocks indented."""
    parts = []
    first = []
    nested = []
    for ch in li.children:
        if isinstance(ch, NavigableString):
            if str(ch).strip():
                first.append(inline_node(ch))
        elif ch.name in ("ul", "ol", "pre", "blockquote"):
            nested.append(ch)
        else:
            first.append(inline_node(ch))
    text = "".join(first).strip()
    lines = [text] if text else []
    for n in nested:
        sub = Ctx()
        block_node(n, sub, fname)
        for ln in "\n".join(sub.out).split("\n"):
            lines.append(("    " + ln) if ln.strip() else "")
    return "\n".join(lines)

def convert_file(fname):
    s = open(os.path.join(ROOT, fname), encoding="utf-8", errors="replace").read()
    soup = BeautifulSoup(s, "html.parser")
    content = soup.select_one("#ds-content")
    inner = content.select_one(".ds-content-inner") or content
    ctx = Ctx()

    # front-matter from title + manifest
    title = soup.title.get_text(strip=True) if soup.title else fname
    m = re.search(r"window\.DS_MANIFEST\s*=\s*\[(.*?)\];", s, re.S)
    label, order = "", []
    if m:
        entries = re.findall(r'\{\s*file:\s*"([^"]+)",\s*label:\s*"([^"]+)"', m.group(1))
        order = [f for f, _ in entries]
        for f, lab in entries:
            if f == fname:
                label = lab
    track = re.search(r'DS_TRACK\s*=\s*"([^"]+)"', s)
    track = track.group(1) if track else "aipc01"

    # index volume cards -> :::volumes directive (from manifest order)
    vols = inner.select("a.vol")

    # sequential walk with pq grouping (stem p + ol.opts + details.pq/ans)
    children = [ch for ch in inner.children if not (isinstance(ch, NavigableString) and not str(ch).strip())]
    i = 0
    # detect index page: has vol cards
    if vols and fname == "index.html":
        # emit everything, replacing vol anchors with :::volumes
        for ch in children:
            if getattr(ch, "name", None) == "a" and "vol" in (ch.get("class") or []):
                if "::volumes-emitted::" not in ctx.out:
                    ctx.emit(":::volumes")
                    ctx.emit(":::")
                    ctx.emit("")
                    ctx.out.append("::volumes-emitted::")
                continue
            block_node(ch, ctx, fname)
        ctx.out = [l for l in ctx.out if l != "::volumes-emitted::"]
    else:
        # pre-pass: group (stem p | div.qstem)? + (ol.opts)? + details.pq/ans
        consumed = set()
        pq_at = {}   # child index -> (details, stem_paras, opts)
        for j, ch in enumerate(children):
            nm = getattr(ch, "name", None)
            cls = (ch.get("class") or []) if nm else []
            if nm == "details" and ("pq" in cls or "ans" in cls):
                stem_paras, opts = None, None
                if j - 1 >= 0 and (j - 1) not in consumed:
                    p1 = children[j - 1]
                    p1n = getattr(p1, "name", None)
                    p1c = (p1.get("class") or []) if p1n else []
                    if p1n in ("ol", "ul") and "opts" in p1c:
                        opts = [inline(li).strip() for li in p1.find_all("li", recursive=False)]
                        consumed.add(j - 1)
                        if j - 2 >= 0 and getattr(children[j - 2], "name", None) == "p" \
                                and (j - 2) not in consumed:
                            stem_paras = [inline(children[j - 2])]
                            consumed.add(j - 2)
                    elif p1n == "div" and ("qstem" in p1c or p1.find(class_="opts")):
                        stem_paras, opts = extract_qstem(p1)
                        consumed.add(j - 1)
                pq_at[j] = (ch, stem_paras, opts)
        for j, ch in enumerate(children):
            if j in consumed:
                continue
            if j in pq_at:
                det, stem_paras, opts = pq_at[j]
                ctx.emit(convert_pq(det, stem_paras, opts, ctx, fname))
                ctx.emit("")
            else:
                block_node(ch, ctx, fname)

    body = "\n".join(ctx.out).strip() + "\n"
    # collapse 3+ blank lines
    body = re.sub(r"\n{3,}", "\n\n", body)

    slug = fname.replace(".html", "")
    fm = ["---",
          "slug: %s" % slug,
          "file: %s" % fname,
          "title: \"%s\"" % title.replace('"', "'"),
          "label: \"%s\"" % label.replace('"', "'"),
          "track: %s" % track,
          "---", ""]
    out = "\n".join(fm) + "\n" + body
    dest = os.path.join(SRC_VOL, slug.replace("volume-", "") + ".md")
    open(dest, "w", encoding="utf-8").write(out)
    print("wrote %s  (%d bytes, %d warnings)" % (dest, len(out), len(ctx.warnings)))
    for w in ctx.warnings[:10]:
        print("   WARN:", w)
    return dest

if __name__ == "__main__":
    files = sys.argv[1:] or (["index.html"] + sorted(glob.glob(os.path.join(ROOT, "volume-*.html"))))
    files = [os.path.basename(f) for f in files]
    for f in files:
        if f in SKIP_FILES:
            print("SKIP (auditor active):", f)
            continue
        convert_file(f)

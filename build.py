#!/usr/bin/env python3
"""build.py — render src/volumes/*.md -> canonical-DS HTML.

Single source of truth: ONE ds.css + ONE ds.js (from
~/workspace/your_files/shared/design-system/), inlined at build time.

Markdown directives (produced by html2md.py, hand-authorable):
  :::exam-ask / :::takeaway / :::panel / :::walkthrough / :::details <summary>
  :::figure <src>            — alt text line, then optional *credit* line
  :::volumes                 — volume cards built from manifest.yaml
  :::ladder                  — lines:  1. **Title** — description
  :::pq {#id}                — stem para(s), "- A. opt <!-- correct -->" list,
                              answer paragraphs ("Correct: X." / "Y is wrong:")

Usage: python3 src/build.py [md ...]   (default: all volumes in manifest order)
"""
import re, os, sys, html as ihtml
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DS_DIR = "/home/hatch/workspace/your_files/shared/design-system"
SRC_VOL = os.path.join(ROOT, "src", "volumes")

MD_EXT = ["tables", "fenced_code", "attr_list", "sane_lists", "toc"]

def md(text):
    return markdown.markdown(text, extensions=MD_EXT)

def parse_front_matter(text):
    meta = {}
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            for line in text[4:end].split("\n"):
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"').strip("'")
            text = text[end + 4:].lstrip("\n")
    return meta, text

# ------------------------------------------------------- directive parsing ---

def split_directives(text):
    """Split markdown into ('md', text) and ('dir', name, params, inner) chunks."""
    chunks, lines = [], text.split("\n")
    i, buf = 0, []
    while i < len(lines):
        m = re.match(r"^:::\s*([a-z-]+)\s*(.*)$", lines[i])
        if m:
            if buf:
                chunks.append(("md", "\n".join(buf)))
                buf = []
            name, params = m.group(1), m.group(2).strip()
            inner = []
            i += 1
            while i < len(lines) and lines[i].strip() != ":::":
                inner.append(lines[i])
                i += 1
            i += 1  # skip closing :::
            chunks.append(("dir", name, params, "\n".join(inner)))
        else:
            buf.append(lines[i])
            i += 1
    if buf:
        chunks.append(("md", "\n".join(buf)))
    return chunks

def render_pq(params, inner, warnings, fname):
    idm = re.search(r"\{#([^}]+)\}", params)
    pid = ' id="%s"' % idm.group(1) if idm else ""
    lines = inner.split("\n")
    # meta badges line: *A · B · C* — optional trailing ref
    meta_html = ""
    if lines and re.match(r"^\*([^*]+)\*\s*(—\s*(.+))?$", lines[0].strip()):
        m = re.match(r"^\*([^*]+)\*\s*(?:—\s*(.+))?$", lines[0].strip())
        chips = "".join('<span class="constraint">%s</span>' % ihtml.escape(c.strip())
                        for c in m.group(1).split("·"))
        ref = ' <span class="pq-ref">%s</span>' % ihtml.escape(m.group(2)) if m.group(2) else ""
        meta_html = '<p class="pq-meta">%s%s</p>' % (chips, ref)
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]
    # find option list boundaries
    opt_idx = [n for n, l in enumerate(lines) if re.match(r"^- [A-H]\.\s", l.strip())]
    if not opt_idx:
        warnings.append("%s: :::pq with no options" % fname)
        return '<div class="pq"%s>%s%s</div>' % (pid, meta_html, md(inner))
    # parse options with attached note lines ("  > note")
    opts, i = [], opt_idx[0]
    n = len(lines)
    while i < n:
        m = re.match(r"^- ([A-H])\.\s?(.*)$", lines[i].strip())
        if not m:
            break
        letter, text = m.group(1), m.group(2)
        is_c = "<!-- correct -->" in text
        text = text.replace("<!-- correct -->", "").strip()
        note_parts, j = [], i + 1
        while j < n and (lines[j].startswith("  ") or lines[j].strip().startswith(">")):
            note_parts.append(re.sub(r"^\s*>?\s?", "", lines[j]).strip())
            j += 1
        opts.append((letter, text, " ".join(note_parts), is_c))
        i = j
        if i < n and not lines[i].strip():
            k = i + 1
            while k < n and not lines[k].strip():
                k += 1
            if k < n and re.match(r"^- [A-H]\.\s", lines[k].strip()):
                i = k
                continue
            break
    stem = "\n".join(lines[:opt_idx[0]]).strip()
    answer = "\n".join(lines[i:]).strip()

    marked = {l for l, _, _, c in opts if c}
    m = (re.search(r"Correct:\s*([A-Z](?:\s*(?:and|,|&)\s*[A-Z])*)", answer)
         or re.search(r"Why ([A-Z](?:\s*(?:and|,|&)\s*[A-Z])*) is correct", answer))
    stated = set(re.findall(r"[A-Z]", m.group(1))) if m else set()
    if stated and marked != stated:
        warnings.append("%s: pq correct-marker %s != answer key %s" % (fname, sorted(marked), sorted(stated)))

    # answer spans
    def spanify(text):
        out = []
        for ln in text.split("\n"):
            s = ln.strip()
            s = re.sub(r"^(Correct:[^.]*\.)", r'<span class="correct">\1</span>', s)
            s = re.sub(r"^(Why [A-Z][^.]*is correct:?)", r'<span class="correct">\1</span>', s)
            s = re.sub(r"^([A-Z] is wrong:)", r'<span class="wrong">\1</span>', s)
            out.append(s)
        return "\n".join(out)

    opt_html = []
    for letter, t, note, is_c in opts:
        cls = "pq-option correct" if is_c else "pq-option wrong"
        note_h = ' <span class="pq-note">%s</span>' % md(note).replace("<p>", "").replace("</p>", "") if note else ""
        opt_html.append('<li class="%s"><strong>%s) </strong>%s%s</li>'
                        % (cls, letter, md(t).replace("<p>", "").replace("</p>", ""), note_h))
    return (
        '<div class="pq"%s>\n%s\n'
        '<p class="pq-question">%s</p>\n'
        '<ul class="pq-options">\n%s\n</ul>\n'
        '<button class="pq-reveal" type="button">Reveal answer</button>\n'
        '<div class="pq-answer">\n%s\n</div>\n</div>'
    ) % (pid, meta_html, md(stem).replace("<p>", "").replace("</p>", ""),
         "\n".join(opt_html), md(spanify(answer)))

def render_vol(params, inner):
    parts = [p.strip() for p in params.split("|")]
    weight = parts[0] if len(parts) > 0 else ""
    link = parts[1] if len(parts) > 1 else "#"
    title = parts[2] if len(parts) > 2 else ""
    return ('<a class="vol" href="%s"><span class="row"><h3>%s</h3>'
            '<span class="w">%s</span></span>%s</a>'
            % (ihtml.escape(link), ihtml.escape(title), ihtml.escape(weight), md(inner)))

def render_ladder(inner):
    items = []
    for line in inner.split("\n"):
        m = re.match(r"^\s*\d+\.\s*(.*)$", line)
        if not m:
            continue
        rest = m.group(1)
        tm = re.match(r"^\*\*(.+?)\*\*\s*[—–-]\s*(.*)$", rest)
        if tm:
            title, desc = tm.group(1), tm.group(2)
        else:
            title, desc = rest, ""
        n = len(items) + 1
        items.append(
            '<div class="rung"><span class="rung-n">%d</span>'
            '<div><b>%s</b><span>%s</span></div></div>' % (n, md(title).replace("<p>", "").replace("</p>", ""), md(desc).replace("<p>", "").replace("</p>", "")))
    return '<div class="ladder">\n' + "\n".join(items) + '\n</div>'

def render_figure(params, inner):
    parts = params.split()
    src = parts[0] if parts else ""
    light = "light" in parts[1:]
    cls = ' class="fig-light"' if light else ""
    lines = [l for l in inner.split("\n") if l.strip()]
    alt = re.sub(r"<[^>]+>", "", md(lines[0])).strip() if lines else ""
    credit = ""
    if len(lines) > 1:
        credit = '<figcaption class="credit">%s</figcaption>' % md(" ".join(lines[1:])).replace("<p>", "").replace("</p>", "")
    cap = '<figcaption>%s</figcaption>%s' % (ihtml.escape(alt), credit) if (alt or credit) else ""
    return '<figure%s><img src="%s" alt="%s" loading="lazy">%s</figure>' % (cls,
        ihtml.escape(src), ihtml.escape(alt), cap)

def render_volumes(manifest):
    cards = []
    for v in manifest["volumes"]:
        m = re.search(r"\((\d+%)\)", v["label"])
        badge = '<span class="w">%s</span>' % m.group(1) if m else ""
        title = re.sub(r"\s*\(\d+%\)\s*$", "", v["label"])
        cards.append(
            '<a class="vol" href="%s"><span class="row"><span>%s</span>%s</span></a>'
            % (v["file"], ihtml.escape(title), badge))
    return "\n".join(cards)

SIMPLE_DIVS = {
    "exam-ask": "exam-ask",
    "takeaway": "takeaway",
    "panel": "panel",
    "walkthrough": "diagram-walkthrough",
}

def render_chunks(chunks, manifest, warnings, fname):
    out = []
    for ch in chunks:
        if ch[0] == "md":
            out.append(md(ch[1]))
        else:
            _, name, params, inner = ch
            if name == "pq":
                out.append(render_pq(params, inner, warnings, fname))
            elif name == "ladder":
                out.append(render_ladder(inner))
            elif name == "figure":
                out.append(render_figure(params, inner))
            elif name == "volumes":
                out.append(render_volumes(manifest))
            elif name == "vol":
                out.append(render_vol(params, inner))
            elif name in SIMPLE_DIVS:
                cls = SIMPLE_DIVS[name]
                extra = ""
                if name == "details":
                    extra = "<summary>%s</summary>" % ihtml.escape(params or "More")
                    cls = ""
                out.append('<div class="%s">%s%s</div>' % (cls, extra, md(inner)) if cls
                           else '<details>%s%s</details>' % (extra, md(inner)))
            else:
                warnings.append("%s: unknown directive :::%s" % (fname, name))
                out.append(md(inner))
    html = "\n".join(out)
    # wrap every table in the DS scroll container
    html = re.sub(r"<table>(.*?)</table>",
                  r'<div class="table-wrap"><table>\1</table></div>',
                  html, flags=re.S)
    return html

# ------------------------------------------------------------- assembly ---

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<title>{title}</title>
<style>
/* ==== DS canonical design system — do not edit per-file (build.py inlines) ==== */
{css}
</style>
</head>
<body>
<div id="ds-sidebar-root"></div>
<main id="ds-content"><div class="ds-content-inner">
{content}
</div></main>
<script>
window.DS_TRACK = "{track}";
window.DS_MANIFEST = [
{manifest}
];
</script>
<script>
/* ==== DS runtime — do not edit per-file (build.py inlines) ==== */
{js}
</script>
</body>
</html>
"""

def load_manifest():
    import yaml
    with open(os.path.join(ROOT, "src", "manifest.yaml")) as f:
        return yaml.safe_load(f)

def build_one(manifest, mvol, css, js, warnings):
    md_path = os.path.join(SRC_VOL, mvol["md"])
    if not os.path.exists(md_path):
        warnings.append("missing source: %s (skipped)" % mvol["md"])
        return None
    raw = open(md_path, encoding="utf-8").read()
    meta, body = parse_front_matter(raw)
    title = meta.get("title", mvol["label"])
    chunks = split_directives(body)
    content = render_chunks(chunks, manifest, warnings, mvol["md"])
    man_lines = ",\n".join(
        '  { file: "%s", label: "%s" }' % (v["file"], v["label"].replace('"', '\\"'))
        for v in manifest["volumes"])
    page = PAGE.format(title=ihtml.escape(title), css=css, js=js,
                       track=manifest["track"], manifest=man_lines, content=content)
    dest = os.path.join(ROOT, mvol["file"])
    open(dest, "w", encoding="utf-8").write(page)
    return dest

def main():
    import yaml  # noqa - ensures pyyaml present
    css = open(os.path.join(DS_DIR, "ds.css"), encoding="utf-8").read()
    js = open(os.path.join(DS_DIR, "ds.js"), encoding="utf-8").read()
    assert "</script" not in js and "</style" not in css, "literal closing tag in DS!"
    manifest = load_manifest()
    only = set(sys.argv[1:])
    warnings = []
    built = []
    for v in manifest["volumes"]:
        if only and v["md"] not in only and v["file"] not in only:
            continue
        d = build_one(manifest, v, css, js, warnings)
        if d:
            built.append(d)
            print("built %s (%d KB)" % (d, os.path.getsize(d) // 1024))
    print("warnings:", len(warnings))
    for w in warnings[:30]:
        print("  WARN:", w)
    print("done: %d pages" % len(built))

if __name__ == "__main__":
    main()

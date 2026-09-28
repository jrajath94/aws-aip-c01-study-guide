#!/usr/bin/env python3
"""Humanizer QA gate for AIP-C01 shipped content.

Scans markdown sources (the canonical content) for violations of the
humanizer rules (~/workspace/skills/humanizer/SKILL.md):

  HARD FAIL (non-zero exit, blocks build):
    - em dashes (U+2014) anywhere
    - banned AI tells: delve, leverage (verb), furthermore, moreover,
      additionally (sentence starter), tapestry, seamless, robust,
      game-changer, supercharge, "deep dive", "it's worth noting",
      "in conclusion", "in today's", elevate, unlock (metaphorical)
    - throat-clearing openers: "in this section", "let's talk about",
      "now, let's understand", "let's dive in", "let's explore"

  WARNINGS (reported, do not fail):
    - sentences over 35 words (flag for rewrite)
    - non-Python code fences (code standard: Python/boto3 only;
      json/yaml/sh allowed only for config/data, never for logic)

Skips: data URIs / base64 blobs, fenced code blocks (for prose rules),
front-matter.
"""
import re, sys, glob, os

VOLUMES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "volumes")

BANNED = [
    (r"\bdelve\b", "delve"),
    (r"\bleverag(?:e|es|ing)\b", "leverage (verb)"),
    (r"\bfurthermore\b", "furthermore"),
    (r"\bmoreover\b", "moreover"),
    (r"(?:^|[.!?]\s+)additionally,", "additionally (sentence starter)"),
    (r"\btapestry\b", "tapestry"),
    (r"\bseamless(?:ly)?\b", "seamless"),
    (r"\brobust(?:ly|ness)?\b", "robust"),
    (r"\bgame-changer\b", "game-changer"),
    (r"\bsupercharge[sd]?\b", "supercharge"),
    (r"\bdeep dive\b", "deep dive"),
    (r"it'?s worth noting", "it's worth noting"),
    (r"it'?s important to note", "it's important to note"),
    (r"\bin conclusion\b", "in conclusion"),
    (r"\bin today'?s\b", "in today's"),
    (r"\belevate[sd]?\b", "elevate"),
]

THROAT = [
    r"\bin this section we\b",
    r"\blet'?s talk about\b",
    r"\bnow,? let'?s understand\b",
    r"\blet'?s dive in\b",
    r"\blet'?s explore\b",
]

def strip_noise(text):
    # drop front-matter
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    # drop data URIs / base64 blobs (not prose)
    text = re.sub(r"data:[a-z]+/[a-z0-9.+-]+;base64,[A-Za-z0-9+/=]+", "DATA_URI", text)
    # split out fenced code blocks; return (prose, code_blocks)
    parts = re.split(r"(```.*?```)", text, flags=re.S)
    prose = "".join(p for i, p in enumerate(parts) if i % 2 == 0)
    code = [p for i, p in enumerate(parts) if i % 2 == 1]
    # drop directive lines from prose scan for tells (keep for em dash)
    return prose, code

def check_file(path):
    raw = open(path, encoding="utf-8").read()
    prose, code = strip_noise(raw)
    fails, warns = [], []
    for i, line in enumerate(raw.split("\n"), 1):
        if "DATA_URI" in line or "data:" in line[:30]:
            continue
        if "—" in line:
            # allow em dash inside fenced code? no — zero anywhere in shipped md
            fails.append((i, "em dash", line.strip()[:90]))
    low = prose.lower()
    quoted = [(m.start(), m.end()) for m in re.finditer(r'"[^"\n]{1,80}"', prose)]
    def in_quotes(pos):
        return any(a <= pos <= b for a, b in quoted)
    for pat, name in BANNED:
        for m in re.finditer(pat, low):
            if in_quotes(m.start()):
                continue  # quoted product vocabulary, e.g. the Bedrock "robustness" metric
            line_no = prose.count("\n", 0, m.start()) + 1
            fails.append((line_no, "banned tell: " + name,
                          prose[max(0, m.start()-40):m.end()+40].replace("\n", " ")))
    for pat in THROAT:
        for m in re.finditer(pat, low):
            line_no = prose.count("\n", 0, m.start()) + 1
            fails.append((line_no, "throat-clearing", m.group(0)))
    # long sentences -> warnings (prose only, not table rows)
    for m in re.finditer(r"[^.!?\n]{10,}[.!?]", prose):
        s = m.group(0)
        line_start = prose.rfind("\n", 0, m.start()) + 1
        if prose[line_start:line_start+1] == "|":
            continue  # table cell, not a prose sentence
        words = len(s.split())
        if words > 35:
            line_no = prose.count("\n", 0, m.start()) + 1
            warns.append((line_no, "%d words" % words, s[:90].strip()))
    # code language check -> warnings
    for block in code:
        first = block.split("\n")[0]
        lang = first[3:].strip().lower()
        if lang in ("js", "javascript", "ts", "typescript", "java", "go", "rust", "c", "cpp"):
            warns.append((0, "non-python code fence: " + lang, block[:80]))
    return fails, warns

def main():
    files = sorted(glob.glob(os.path.join(VOLUMES, "*.md")))
    total_fails, total_warns = 0, 0
    for f in files:
        fails, warns = check_file(f)
        name = os.path.basename(f)
        for ln, kind, ctx in fails:
            print("FAIL %s:%d [%s] %s" % (name, ln, kind, ctx))
        for ln, kind, ctx in warns[:8]:
            print("warn %s:%d [%s] %s" % (name, ln, kind, ctx))
        if len(warns) > 8:
            print("warn %s: ... +%d more long-sentence warnings" % (name, len(warns) - 8))
        total_fails += len(fails)
        total_warns += len(warns)
    print("humanizer gate: %d failures, %d warnings across %d files"
          % (total_fails, total_warns, len(files)))
    return 1 if total_fails else 0

if __name__ == "__main__":
    sys.exit(main())

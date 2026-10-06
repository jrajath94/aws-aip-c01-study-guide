# AIP-C01 Design System (Hallmark discipline) — applies to ALL HTML volumes

Shared across tracks. Implement these tokens and behaviors EXACTLY. Do not improvise.

## Theme: pitch-black dark mode (default, only theme)

```css
:root{
  --bg:#000000;
  --surface:#0d0d0d;
  --border:#262626;
  --text:#ececec;
  --muted:#a8a8a8;
  --accent:#f0b429;   /* warm amber, used sparingly: key highlights, active states */
  --link:#6cb2ff;
  --code-bg:#111111;
}
```

Rules: no gradients anywhere. No decorative filler. No generic AI-slop visuals. Flat surfaces, 1px `--border` separators. Amber is an accent, not a background wash.

## Typography

- System font stack ONLY (must render on an office laptop with no webfont access):
  `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`
- Code: `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`
- Body: 17px, line-height 1.75, max content width 72ch.
- ALL paragraphs `text-align: justify`.
- Headings: always roman (never italic), clear size/weight hierarchy (h1 > h2 > h3, weight 700/600/600).

## Sidebar navigation (must be awesome)

- Sticky full-height left sidebar, `--surface` background, right border `--border`.
- Collapsible chapter groups (chapters collapse/expand; state may persist in localStorage).
- Scroll-spy: active section highlighted in the nav as the reader scrolls (IntersectionObserver).
- Filter/search box at top of sidebar filtering nav items by text.
- Per-section completion checkmarks, persisted in `localStorage` (namespaced per volume file).
- Reading progress bar (thin `--accent` bar at top of viewport).
- Prev/next chapter footer links at the bottom of the content column.
- Keyboard navigation: arrow keys move between sections when sidebar focused; `/` focuses the filter box; Esc clears.
- Mobile: sidebar becomes a slide-in drawer (hamburger button, focus trap not required but Esc closes).
- No horizontal scrolling at any width (`overflow-x: clip` on body, responsive images `max-width:100%`, code blocks scroll internally).

## Learning components

- "How the exam asks" callout boxes (Maarek style): `--surface` box, left `--accent` border, bold label.
- Key-takeaway boxes: `--surface` box, left `--link` border.
- Practice-question widgets: question card + click-to-reveal answer (keep accessible `<details>`/`<summary>`), answer shows why-correct plus why-each-distractor-wrong. Style consistently.
- Copy buttons on every code block (small button, clipboard API, fallback selects text).
- Every diagram paired with a numbered "how to read this diagram" walkthrough (already in content; keep styling consistent: muted numbered list under the figure).
- Definition styling on first-use terms: `<dfn>` styled with dotted underline + `--accent` color on first use.

## Accessibility

- Contrast: body text `--text` on `--bg` (excellent); `--muted` on `--bg` (~7:1, body-large minimum); `--accent`/`--link` used for large/bold text and UI, never small muted text.
- Visible focus states: 2px `--accent` outline offset on all interactive elements.
- Semantic heading order: exactly one h1 per page, no skipped levels.
- Images: meaningful `alt` text; decorative images `alt=""`.
- `prefers-reduced-motion`: disable smooth scroll and transitions.

## Print stylesheet

`@media print`: hide sidebar/drawer/progress bar/filter/copy buttons; black-on-white; expand `<details>` answers (print all); avoid breaking figures and question cards across pages (`break-inside: avoid`); show link URLs for external references.

## Implementation notes for restyle workers

- Rewrite each volume's `<style>` block to these tokens; keep all content, ids, and anchors intact (nav depends on them).
- Upgrade the existing left rail into the full sidebar spec above; add the single shared JS (vanilla, no libraries) implementing: collapsible groups, scroll-spy, filter, checkmarks+localStorage, progress bar, prev/next links, keyboard nav, mobile drawer.
- Convert existing callout/question/code markup to the component styles above where trivially mappable; do not restructure content.
- Keep zero em dashes, zero gradients, zero external dependencies (the JS/CSS must be inline).
- After restyle, re-run the QA checklist: balanced tags, unique ids, anchors resolve, images decode, no placeholders, plus the new gates: mobile-responsiveness sanity (no horizontal scroll at 360px), focus states visible, heading order valid, print stylesheet present.

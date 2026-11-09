# Agent task: transcribe one solve PDF → a `solves/` entry

You convert a single handwritten solution scan into a clean Markdown file plus
any extracted figures, keyed so the static site can join it to its puzzle.

**Input:** `raw-solve-docs/<collection>/<n>.pdf` (e.g. `raw-solve-docs/mbmalp/1.pdf`).
**Output:** `solves/<collection>/<n>/index.md` (+ `fig-*.png` when there are drawings).

---

## Procedure

### 1. Read the scan
Open the PDF directly with the Read tool — you can see the handwriting and
drawings natively. Note the page count (some solves span 2 pages).

Every solve follows a loose format:
- a **date** at the top (the day it was written),
- the **problem number**,
- the natural-language solution, often with math and sometimes drawings.

### 2. Transcribe the text
Write faithful Markdown of the written solution. Rules:
- Preserve the author's wording and reasoning; fix only obvious **slips of the
  pen** (misspellings, dropped letters). Do **not** rewrite, expand, or "improve"
  the argument.
- **Preserve factual/conceptual errors verbatim.** If the author writes
  "dodecahedron" where "dodecagon" is clearly meant, leave it as written —
  correcting it would alter the argument, not fix a pen slip. Transcribe what's
  on the page, not what's correct.
- **Math → TeX.** Inline math uses `$...$`; displayed/centered equations use
  `$$...$$` on their own line. Transcribe every formula, fraction, subscript,
  set symbol (`\mathbb{N}`), etc. faithfully. Example from `mbmalp/1`:
  `$$r = 1 + \frac{1}{2c\pi}$$` and inline `for $c \in \mathbb{N}$`.
- **Multi-letter subscripts use `\text{}`** for KaTeX readability, e.g.
  `A_{\text{star}}` not `A_{star}`.
- Keep the author's paragraph breaks. Lists → Markdown lists.
- **Multi-page solves:** only add a `---` horizontal rule between pages if the
  author's own text explicitly signals the page break (e.g. "I show this
  derivation on the next page" or "continued on the next page"). If the text
  says nothing about it, don't add a rule — just let the content flow
  continuously, even across a page boundary.
- Do **not** include the title/attribution/problem statement here — those live on
  the puzzle entry. The solve is only the solution.

### 3. Handle figures (only if there are hand-drawn visual aids / diagrams)
Skip this whole step for text-only solves.

a. Render the page(s) to PNG:
```
python3 scripts/render.py raw-solve-docs/<collection>/<n>.pdf
```
This prints a work dir, e.g. `.work/<n>/` containing `page-1.png`, `page-2.png`.

b. For each figure, determine a **normalized bounding box** `[x0, y0, x1, y1]`
   — fractions of page width/height, origin top-left — that tightly contains the
   drawing (a little margin is fine; `crop.py --pad` can add more). To get the
   box, look at the rendered `page-*.png` and estimate the fractions.
   If the solution *is* a full-page drawing, use a near-full-page box.

c. Write a `figures.json` (anywhere, e.g. the work dir):
```json
{
  "pages_dir": ".work/<n>",
  "figures": [
    {"id": "fig-1", "page": 1, "bbox": [0.10, 0.45, 0.92, 0.72],
     "out": "solves/<collection>/<n>/fig-1.png"}
  ]
}
```

d. Crop:
```
python3 scripts/crop.py figures.json
```

e. Reference each figure in the Markdown at the right spot with a **relative**
   path (Astro's content loader optimizes these):
```markdown
![Short description of the drawing](./fig-1.png)
```

### 4. Write `solves/<collection>/<n>/index.md`
Frontmatter (nothing more — title/attribution come from the puzzle):
```yaml
---
collection: <collection>
problem: <n>
date: <YYYY-MM-DD>        # from the handwritten date; infer century as 20xx
source: raw-solve-docs/<collection>/<n>.pdf
---
```
Then the transcribed body (with `$...$` math and any `![](./fig-N.png)`).

### 5. Verify
- The `date` is ISO `YYYY-MM-DD`. A handwritten `10/1/26` → `2026-10-01`.
- Every referenced `./fig-N.png` exists in the folder.
- Re-read your math: delimiters balanced, no stray `$`.

Don't touch `.work/` cleanup — it's gitignored scratch.

---

## Batch mode
If asked to do several, repeat per PDF. `python3 scripts/status.py <collection>`
lists which solve PDFs are not yet transcribed.

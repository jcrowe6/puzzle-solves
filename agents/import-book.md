# Agent task: import a book scan → the `puzzles/` catalog

You turn a single large book-scan PDF into one puzzle entry per problem:
its number, title, and a **rephrased problem statement**. This is the catalog
the site lists and joins your solves against.

**Input:** `raw-book-scans/<collection>.pdf` and `books/<collection>.yaml`.
**Output:** `puzzles/<collection>/<n>/index.md`.

> ⚠️ **Copyright — read first.** The source books are in copyright. Do **not**
> reproduce their text verbatim, and do **not** render, crop, OCR, or otherwise
> extract their images. Your job is to restate each problem **in your own words**
> (fair use) and to replace any printed figure with a short **bracketed text
> description**. See the "Sources & copyright" notice in
> [README.md](../README.md).

> Capture **problem statements only** — not the book's answers. The site's
> hidden reveal shows the author's *own* solve (from `solves/`).

---

## Procedure

### 1. Orient yourself in the scan
Open the PDF with the Read tool. Gardner-style books put all the **problems**
in one section and the **answers/solutions** in a later section — you want only
the problems section, though usually I will upload a scan including only the problems anyways. Read `pdfinfo raw-book-scans/<collection>.pdf` for the page
count; work in page ranges with `scripts/render.py --pages a-b` so you never load
the whole book at once.

Read `books/<collection>.yaml` for the title/author/year (attribution).

### 2. For each puzzle in the problems section
Identify its **number** and **name/title** (e.g. "1. The Returning Explorer").

**Rephrase** the statement into clean Markdown — do **not** transcribe it
verbatim:
- Restate the setup, givens, and the question **in your own words**. Preserve
  every fact, number, and constraint needed to solve it, but change the sentence
  structure and phrasing. The aim is a faithful *problem*, not a copy of the
  author's *expression*. Don't lift distinctive turns of phrase, framing
  anecdotes, or flavor text — summarize them only if they matter to the puzzle.
- Keep it tight: the premise as a setup for the solve, not a reproduction of the
  page.
- Math → TeX (`$...$` inline, `$$...$$` display), same conventions as
  `transcribe-solve.md`. (Formulas are facts, not expression — restate them
  accurately.)
- **Figures: describe, never extract.** Do **not** render, crop, or OCR the
  book's diagrams. In place of each printed figure, write a bracketed
  description detailed enough for a reader to reconstruct it, e.g.
  `[Figure: a 3×3 grid of dots; the top-left and bottom-right dots are circled.]`
  If a diagram is essential and your description can't fully carry it, say so and
  point the reader to the original (linked in the README sources). Puzzle folders
  must contain **no `fig-*.png`**.

### 3. Write `puzzles/<collection>/<n>/index.md`
```yaml
---
collection: <collection>
problem: <n>
title: "<puzzle name>"
# attribution is inherited from books/<collection>.yaml.
# For ad-hoc puzzles with no book, add here instead:
#   source_title: "..."
#   source_author: "..."
---
```
Then the problem statement body (with math / figures).

### 4. Verify
- Numbers are contiguous and match the book (flag any you skipped).
- **No verbatim copying:** each statement reads in your own words, not the
  book's phrasing, while keeping every solving-relevant fact.
- **No extracted imagery:** no `fig-*.png` in any puzzle folder; every diagram
  is a bracketed `[Figure: ...]` description instead.
- Statements only — no answers leaked in.
- `python3 scripts/status.py <collection>` now shows the puzzles as present, and
  lights up ✓ in the "solve" column wherever a matching solve already exists.

---

## Ad-hoc puzzles (no book)
For a one-off puzzle you read elsewhere, skip the scan: hand-write
`puzzles/adhoc/<slug-or-n>/index.md` with `collection: adhoc`, a `title`, and
`source_title` / `source_author` in the frontmatter. No `books/adhoc.yaml` needed
unless you want shared attribution across several. The same copyright rules
apply — **rephrase** the statement in your own words and **describe** any figure
rather than copying it, and add the source to the README "Sources" list if it
isn't already there.

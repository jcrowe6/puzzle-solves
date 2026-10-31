# gardner-solves — agent entry point

This repo turns handwritten recreational-math solution scans (and, later, book
scans) into clean Markdown that a static Astro site consumes.

Two independent pipelines, joined by `(collection, problem number)`:

1. **Transcribe a solve** — a single `raw-solve-docs/<col>/<n>.pdf` →
   `solves/<col>/<n>/index.md`. Follow **[agents/transcribe-solve.md](agents/transcribe-solve.md)**.
2. **Import a book** — a big `raw-book-scans/<col>.pdf` →
   `puzzles/<col>/<n>/index.md` (problem statements). Follow
   **[agents/import-book.md](agents/import-book.md)**. ⚠️ Source books are in
   copyright: **rephrase** statements in your own words and **describe** figures
   rather than extracting them (`raw-book-scans/` is gitignored).

Shared scripts: `scripts/render.py` (PDF → page PNGs), `scripts/crop.py`
(bbox → figure PNGs), `scripts/status.py` (what's done vs pending).

When the user asks to "transcribe"/"convert" a solve, or "import"/"process" a
book, open the matching instruction file above and follow it exactly.

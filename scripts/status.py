#!/usr/bin/env python3
"""Show conversion progress: which raw PDFs have become puzzles / solves.

For each collection it reconciles three things by problem number:
  - raw solve PDFs in   raw-solve-docs/<col>/<n>.pdf
  - imported puzzles in puzzles/<col>/<n>/index.md   (statement, from book)
  - transcribed solves  solves/<col>/<n>/index.md    (your solution)

Usage:
    python3 scripts/status.py            # all collections
    python3 scripts/status.py mbmalp     # one collection
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_SOLVES = ROOT / "raw-solve-docs"
PUZZLES = ROOT / "puzzles"
SOLVES = ROOT / "solves"


def numbers_from_pdfs(d):
    if not d.is_dir():
        return set()
    out = set()
    for p in d.glob("*.pdf"):
        m = re.fullmatch(r"\d+", p.stem)
        if m:
            out.add(int(p.stem))
    return out


def numbers_from_tree(d):
    if not d.is_dir():
        return set()
    out = set()
    for idx in d.glob("*/index.md"):
        m = re.fullmatch(r"\d+", idx.parent.name)
        if m:
            out.add(int(idx.parent.name))
    return out


def collections():
    found = set()
    for base in (RAW_SOLVES, PUZZLES, SOLVES):
        if base.is_dir():
            found.update(p.name for p in base.iterdir() if p.is_dir())
    return sorted(found)


def report(col):
    raw = numbers_from_pdfs(RAW_SOLVES / col)
    puz = numbers_from_tree(PUZZLES / col)
    sol = numbers_from_tree(SOLVES / col)
    allnums = sorted(raw | puz | sol)

    print(f"\n{col}  (puzzles: {len(puz)}, solves: {len(sol)}, raw solve PDFs: {len(raw)})")
    print(f"  {'#':>4}  {'puzzle':^7} {'solve':^7} {'raw pdf':^8}")
    for n in allnums:
        print(f"  {n:>4}  {'  ✓' if n in puz else '  ·':^7}"
              f" {'  ✓' if n in sol else '  ·':^7}"
              f" {'  ✓' if n in raw else '  ·':^8}")

    todo = sorted(raw - sol)
    if todo:
        print(f"  solve PDFs not yet transcribed: {', '.join(map(str, todo))}")
    orphans = sorted(sol - puz)
    if orphans:
        print(f"  solves with no puzzle entry (awaiting book import): {', '.join(map(str, orphans))}")


def main():
    cols = sys.argv[1:] or collections()
    if not cols:
        print("no collections found under raw-solve-docs/, puzzles/, or solves/")
        return
    for col in cols:
        report(col)


if __name__ == "__main__":
    main()

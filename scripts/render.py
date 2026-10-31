#!/usr/bin/env python3
"""Render a PDF's pages to PNGs for transcription / figure cropping.

Thin wrapper over poppler's `pdftoppm`. Normalizes output to `page-<n>.png`
(1-indexed, no zero padding) so downstream tools can map a page number to a
file deterministically.

Usage:
    python3 scripts/render.py <pdf> [--dpi 220] [--out <dir>] [--pages 1-2]

Defaults:
    --dpi 220      good balance of legibility vs size for handwriting
    --out .work/<pdf-stem>/
    --pages all

Prints the output directory on the last line.
"""
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


def parse_pages(spec, default_last):
    """'1-3' -> (1, 3); '4' -> (4, 4); None -> (1, default_last or None)."""
    if not spec:
        return 1, default_last
    m = re.fullmatch(r"(\d+)(?:-(\d+))?", spec.strip())
    if not m:
        sys.exit(f"error: --pages must look like '2' or '1-3', got {spec!r}")
    first = int(m.group(1))
    last = int(m.group(2)) if m.group(2) else first
    return first, last


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pdf", type=Path)
    ap.add_argument("--dpi", type=int, default=220)
    ap.add_argument("--out", type=Path, default=None)
    ap.add_argument("--pages", default=None, help="e.g. '2' or '1-3'")
    args = ap.parse_args()

    if not args.pdf.is_file():
        sys.exit(f"error: no such file: {args.pdf}")

    # Prefer Xpdf's pdftopng (writes PNG directly); fall back to poppler's
    # `pdftoppm -png`. Both accept -r/-f/-l and emit <root>-<n>.png.
    # -q silences "No display font" noise (scans are images); real errors still
    # surface via a non-zero exit code.
    if shutil.which("pdftopng"):
        base_cmd = ["pdftopng", "-q", "-r", str(args.dpi)]
        tail = lambda root: [str(args.pdf), str(root)]
    elif shutil.which("pdftoppm"):
        base_cmd = ["pdftoppm", "-png", "-q", "-r", str(args.dpi)]
        tail = lambda root: [str(args.pdf), str(root)]
    else:
        sys.exit("error: need pdftopng or pdftoppm (install xpdf-tools or poppler-utils)")

    out = args.out or Path(".work") / args.pdf.stem
    out.mkdir(parents=True, exist_ok=True)

    first, last = parse_pages(args.pages, None)
    prefix = out / "raw"
    cmd = base_cmd + ["-f", str(first)]
    if last:
        cmd += ["-l", str(last)]
    cmd += tail(prefix)

    # Xpdf spews "Config Error: No display font for ..." for scans (which have no
    # embedded fonts). Filter that noise but keep any genuine diagnostics.
    proc = subprocess.run(cmd, stderr=subprocess.PIPE, text=True)
    for line in proc.stderr.splitlines():
        if "No display font" not in line:
            print(line, file=sys.stderr)
    if proc.returncode != 0:
        sys.exit(f"error: {cmd[0]} exited {proc.returncode}")

    # Tools emit raw-1.png / raw-000001.png etc. Normalize to page-<n>.png.
    produced = sorted(out.glob("raw-*.png"))
    if not produced:
        sys.exit("error: pdftoppm produced no pages")
    for p in produced:
        n = int(re.search(r"(\d+)$", p.stem).group(1))
        p.rename(out / f"page-{n}.png")

    pages = sorted(int(re.search(r"(\d+)$", p.stem).group(1))
                   for p in out.glob("page-*.png"))
    print(f"rendered {len(pages)} page(s) [{pages[0]}..{pages[-1]}] at {args.dpi} dpi",
          file=sys.stderr)
    print(out)


if __name__ == "__main__":
    main()

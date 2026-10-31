#!/usr/bin/env python3
"""Crop hand-drawn / printed figures out of rendered PDF pages.

Reads a small JSON spec (produced by the transcribing agent) describing each
figure as a *normalized* bounding box over a page, and writes a cropped PNG to
the solve/puzzle folder with Pillow.

Normalized bbox = [x0, y0, x1, y1] as fractions of page width/height in [0, 1],
origin top-left. This keeps the spec independent of render DPI.

Spec format (figures.json):
    {
      "pages_dir": ".work/1",
      "figures": [
        {"id": "fig-1", "page": 1, "bbox": [0.10, 0.40, 0.92, 0.70],
         "out": "solves/mbmalp/1/fig-1.png"}
      ]
    }

Usage:
    python3 scripts/crop.py figures.json
    python3 scripts/crop.py figures.json --pad 0.01   # grow boxes 1% each side
"""
import argparse
import json
import sys
from pathlib import Path

from PIL import Image


def clamp(v, lo=0.0, hi=1.0):
    return max(lo, min(hi, v))


def crop_one(pages_dir, fig, pad):
    page_path = pages_dir / f"page-{fig['page']}.png"
    if not page_path.is_file():
        sys.exit(f"error: missing rendered page {page_path} for {fig['id']}")
    x0, y0, x1, y1 = fig["bbox"]
    x0, y0 = clamp(x0 - pad), clamp(y0 - pad)
    x1, y1 = clamp(x1 + pad), clamp(y1 + pad)
    if x1 <= x0 or y1 <= y0:
        sys.exit(f"error: {fig['id']} has an empty bbox after padding: {fig['bbox']}")

    with Image.open(page_path) as im:
        W, H = im.size
        box = (round(x0 * W), round(y0 * H), round(x1 * W), round(y1 * H))
        out = Path(fig["out"])
        out.parent.mkdir(parents=True, exist_ok=True)
        im.crop(box).save(out)
    return out, box


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("spec", type=Path, help="figures.json")
    ap.add_argument("--pad", type=float, default=0.0,
                    help="extra margin (fraction of page) added to every side")
    args = ap.parse_args()

    spec = json.loads(args.spec.read_text())
    pages_dir = Path(spec["pages_dir"])
    figures = spec.get("figures", [])
    if not figures:
        print("no figures in spec; nothing to crop", file=sys.stderr)
        return

    for fig in figures:
        out, box = crop_one(pages_dir, fig, args.pad)
        print(f"{fig['id']}: page {fig['page']} {box} -> {out}", file=sys.stderr)
    print(f"cropped {len(figures)} figure(s)", file=sys.stderr)


if __name__ == "__main__":
    main()

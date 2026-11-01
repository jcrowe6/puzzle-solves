---
collection: mbmalp
problem: 3
date: 2026-10-04
source: raw-solve-docs/mbmalp/3.pdf
---

No, it is impossible.

**Lemma 1:** Every domino will cover exactly 1 white square and 1 black square. This is clear to see.

The altered board has 30 white squares and 32 black squares. Assume it is completely tiled. Then, 30 dominos are covering all 30 white squares and 30 of the black squares. Then there are 2 black squares that must be covered by 1 domino. By Lemma 1 this is a contradiction, and the board cannot be tiled.

This can easily be extended to show it's impossible for any even $n$ $n \times n$ board modified similarly. $n^2/2$ black tiles, $n^2/2 - 2$ white tiles, $n^2/2 - 1$ dominoes. $n^2/2 - 2$ dominoes cover all $n^2/2 - 2$ white tiles and $n^2/2 - 2$ black tiles, leaving $(n^2/2) - (n^2/2 - 2) = 2$ black tiles to be covered by the $(n^2/2 - 1) - (n^2/2 - 2) = 1$ remaining domino, and the same contradiction applies.

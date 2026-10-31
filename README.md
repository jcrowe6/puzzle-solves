# puzzle-solves

Raw scans of my handwritten recreational-math puzzle solutions and a small
pipeline that turns them into clean Markdown for my Astro site
([jcrowell.net](https://jcrowell.net)). Currently starting with
Martin Gardner's *My Best Mathematical and Logic Puzzles* (`mbmalp`).



## Layout

```
raw-solve-docs/     <collection>/<n>.pdf          # my solution scans 
solves/             <collection>/<n>/index.md     # my solutions as clean md's (+ fig-*.png)
puzzles/            <collection>/<n>/index.md     # rephrased problem statements
books/              <collection>.yaml             # per-collection registry (title/author/year)
```

Each solve/puzzle is a **folder ("page bundle")**: a text-only entry is just
`index.md`; entries with drawings co-locate their `fig-*.png` so the images
travel with the text and get Astro image optimization. (Figures come only from
*my own* solve scans — book imagery is never extracted; see below.)

## Sources & copyright

Puzzles in this repository are drawn from published collections. All rights in
the original puzzles and their text belong to the respective authors and
publishers.

Where puzzles appear here, the problem statements are restated in my own
words as the setup for my original solutions and commentary, and any printed
diagram is replaced by a short text description rather than a reproduced image.
This repo is not a substitute for the books, and I encourage you to buy them.
The solutions, explanations, and code are my own work.

If you are a rightsholder and believe any content here exceeds fair use or
should be removed, please open an issue or email <jeremiahpcrowell@gmail.com> and
I will take it down promptly.

### Sources
- *My Best Mathematical and Logic Puzzles* — Martin Gardner (Dover
  Publications, 1994). Purchase: [Amazon](https://a.co/d/08faRm4J)
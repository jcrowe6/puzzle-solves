---
collection: mbmalp
problem: 5
date: 2026-10-05
source: raw-solve-docs/mbmalp/5.pdf
---

1 draw. Take 1 marble from the box labelled WB.

If white, the setup is:

![If white: the "WB" box holds two white marbles, the "WW" box two black, and the "BB" box one white and one black](./fig-1.png)

If black, the setup is:

![If black: the "WB" box holds two black marbles, the "WW" box one white and one black, and the "BB" box two white](./fig-2.png)

This is because the boxes must be labelled incorrectly. So the "WB" box must contain either WW or BB marbles. Then, picking 1 marble is enough to know it's full contents.

Knowing the state of the "WB" box we are left the "WW" and "BB" boxes. Assume WLOG that the "WB" box contained the WW marbles. That leaves us with the BB and WB marbles to determine the locations of. The BB marbles cannot be in the "BB" box (as that would be "correctly labelled"), so they must be in the "WW" box. That leaves the WB marbles to be in the "BB" box.

The same logic applies for if the "WB" box contains the BB marbles.

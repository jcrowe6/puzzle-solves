---
collection: mbmalp
problem: 9
date: 2026-10-14
source: raw-solve-docs/mbmalp/9.pdf
---

It can be done with one weighing, with the following configuration: First, label each pile 1 through 10. Then put on the scale the same amount of coins from each pile as it's label - that is, 1 from the "1" pile, 2 from the "2" pile, and so on.

Now let's call the normal weight of a single real coin $x$. If none of the coins here were fake, the total weight would be $x + 2x + 3x \ldots + 10x = x(1 + 2 + 3 \ldots + 10) = 55x$. However, knowing that exactly one full pile is fake, and weighs 1g more per coin, then if the "1" pile is fake, the total weight will be $55x + 1$, the "2" pile: $55x + 2$ and so on. So simply weigh the coins in this configuration to get the weight $W$, and $W - 55x$ gives the excess weight which is the same as the label of the fake pile of coins.

As a demonstration, say a real coin weighs 10g, and the 6th pile is fake. The total weight of this configuration of coins is

$$10 + 20 + 30 + 40 + 50 + 66 + 70 + 80 + 90 + 100$$
$$= 556$$
$$556 - 550 = 6$$

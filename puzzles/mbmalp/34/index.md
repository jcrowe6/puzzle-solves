---
collection: mbmalp
problem: 34
title: "The Game of Googol"
---

A betting game: someone writes a different positive number on each of as many
slips of paper as they like. The numbers can be tiny fractions or enormous (a
googol, which is 1 followed by 100 zeros, or even bigger). The slips are
shuffled face down. You turn them over one at a time, and you must stop on the
one you think is the largest of all. You can't go back to an earlier slip, and
if you reach the last slip you are stuck with it.

Naive odds against you finding the maximum look like 5 to 1 or worse, yet with
the best strategy your chance is a bit better than 1 in 3. Two questions:
1. What is the best strategy? (This is not the same as maximizing the *value* of
   the number you pick.)
2. How do you compute your chance of winning if you follow it?

With two slips the chance is 1/2 whatever you do. As the number of slips grows
the best-strategy chance falls but flattens out fast, changing little past ten
slips and never dropping below 1/3. Only the ordering of the numbers matters,
not their size.

Application: a woman expects to meet ten men who would propose before year's
end; once she turns a man down, he won't ask again. What strategy maximizes her
chance of accepting the best of the ten, and what is that chance?

The strategy has the form: reject a certain number of the first slips (or
proposals), then take the first one that beats everything rejected so far. Find
a formula for how many to reject given the total number of slips.

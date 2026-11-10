---
collection: mbmalp
problem: 52
title: "Playing Twenty Questions when Probability Values Are Known"
---

In Twenty Questions, one player picks an object and the other tries to identify
it with at most twenty yes/no questions. The best questions split the remaining
candidates into two groups as close to equal in size as possible. For example, a
number from 1 to 9 can always be found in at most four questions, and with
twenty questions any number up to $2^{20} = 1{,}048{,}576$ can be found.

Now suppose the candidates are **not** equally likely, and each has a known
probability of having been chosen. As an example, take a deck of 45 spade cards:
one ace, two deuces, three threes, and so on up to nine nines. The deck is
shuffled and a card is drawn. You must identify the card's *rank* with yes/no
questions. How should you ask them so as to minimize the expected number of
questions?

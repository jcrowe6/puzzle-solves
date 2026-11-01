---
collection: mbmalp
problem: 7
date: 2026-10-08
source: raw-solve-docs/mbmalp/7.pdf
---

The Bronx train must come 1 minute after the Brooklyn train.

Since they both arrive every 10 minutes, the gap between arrivals never changes.

Assume for simplicity that the Brooklyn train arrives and departs instantly the moment the ones' place of the minute turns to 0 - that is, X:00, X:10, X:20... X:50, and the Bronx train the moment it turns to 1 e.g. X:01, X:11, X:21... X:51.

The man shows up at a random time. If the ones' place of the minute is 1, 2, 3... 9, then he has missed the Bronx train and the next train will be to Brooklyn at X:X0.

Only if he arrives when the ones' place of the minute is 0 will the next train be to the Bronx when it turns to X:X1.

Since it's equally likely for the ones' place of the minute to be any of the 10 digits, he has just $\frac{1}{10}$ chance of going to the Bronx and consequently a $\frac{9}{10}$ chance of going to Brooklyn with this strategy, and if the Bronx train comes 1 min after the Brooklyn.

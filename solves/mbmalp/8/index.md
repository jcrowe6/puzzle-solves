---
collection: mbmalp
problem: 8
date: 2026-10-13
source: raw-solve-docs/mbmalp/8.pdf
---

He must have walked for 55 minutes.

Note I am not totally satisfied with the following derivation, it just kind of "falls out" of the equations, and I think there must be a more geometric / visual way to see this. Anyways. Let the arrival time home on a normal day be $A_N$ and the arrival time today be $A_T$

we have $A_T = A_N - 10$ (the algebra throughout is in minutes)

Define the driving time in minutes, one way (from home to station or vice versa), on a normal day as $T_{\text{DN}}$. We are given $5{:}00 + T_{\text{DN}} = A_N$. 

Define the time in minutes spent today walking, then driving as $T_W$ and $T_{\text{DT}}$ respectively. We are given $4{:}00 + T_W + T_{\text{DT}} = A_T$.

Finally define the wife's departure time as $D$.

We have $A_N = D + 2T_{\text{DN}}$ and $A_T = D + 2T_{\text{DT}}$. See that

$$A_T = A_N - 10$$
$$D + 2T_{\text{DT}} = D + 2T_{\text{DN}} - 10$$
$$2T_{\text{DT}} = 2T_{\text{DN}} - 10$$
$$T_{\text{DT}} = T_{\text{DN}} - 5$$

Or in other words, the wife spends 5 minutes less driving each way than usual. Now see

$$A_T = A_N - 10$$
$$4{:}00 + T_W + T_{\text{DT}} = 5{:}00 + T_{\text{DN}} - 10$$

and see that this implies

$$T_W + T_{\text{DT}} = T_{\text{DN}} - 10 + 60$$
$$T_W + T_{\text{DT}} = T_{\text{DN}} + 50$$

Or in other words, the amount of travel time from the station to home is 50 minutes longer today than it normally is

Finally, substitute in

$$T_W + (T_{\text{DN}} - 5) = T_{\text{DN}} + 50$$

from earlier. This is essentially saying "5 minutes less than the usual driving time plus some amount of walking equals the usual amount of driving plus 50 minutes" which is a trippy thing to think about. It easily follows that

$$T_W = T_{\text{DN}} + 50 - T_{\text{DN}} + 5$$
$$T_W = 55$$

So the amount of time walking must have been 55 minutes.

Interestingly, it doesn't matter how far away the home is, that is, when the wife leaves or how long she drives. If $T_W = 55$ then $A_T = A_N - 10$ is preserved.

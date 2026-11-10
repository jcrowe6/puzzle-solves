---
collection: mbmalp
problem: 40
title: "A Switching Puzzle"
---

A locomotive and two railroad cars, A and B, sit on a track layout. The problem:
use the locomotive to swap the positions of cars A and B, then bring the
locomotive back to its starting position, using as few operations as possible.

[Figure: a track diagram. Two long horizontal lines run left to right, an upper
one and a lower one, joined at the left by a curved connection that forms an
oval loop with two switches. The loop curves around at the right end, where a
tunnel sits. The locomotive stands on the upper track at the far left, outside
the loop. Car A is on the upper line near the middle, and car B is on the lower
line near the middle. The cars are drawn too near the switches; assume they are
actually far enough east that there is ample room for the locomotive and the
other car between each car and its switch. Consult the original for the exact
layout.]

Rules:
- The tunnel fits the locomotive but neither car.
- Either end of the locomotive can push or pull, and the two cars may be coupled
  to each other.
- An "operation" is any movement of the locomotive between stops, where it stops
  when it reverses direction, reaches a car to push it, or uncouples from a car it
  was pulling. Throwing the switches does not count as an operation.
- No "flying switch" moves: you can't throw a switch just after the engine has
  pushed an uncoupled car past it so that the car goes one way and the engine,
  without stopping, goes another.

A tip: use three coins (say a penny, a dime and a nickel) on the diagram, with
the penny as the locomotive since only it can go through the tunnel.

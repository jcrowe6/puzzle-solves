---
collection: mbmalp
problem: 54
title: "Find the Hexahedrons"
---

A polyhedron is a solid bounded by flat polygons called faces. The simplest is
the tetrahedron, with four triangular faces. If we treat the network of edges as
topological (edge lengths and angles may change but the pattern of connections
must not), there is only one basic kind of tetrahedron.

There are two basic kinds of five-sided polyhedron: the Great Pyramid style
(a quadrilateral base with four triangular faces), and a tetrahedron with one
corner sliced off (three quadrilateral faces and two triangles).

[Figure: three solids side by side. Left, a tetrahedron. Middle, a square-based
pyramid. Right, a tetrahedron with a corner cut off, giving a tall five-faced
solid with a triangular top.]

John McClellan, an artist, asks: how many basic kinds of **convex hexahedron**
(six-sided solid) exist in all? A solid is convex if each face can be laid flat
on a tabletop; the cube is the familiar example.

Be careful when hunting by chopping off corners of simpler solids: different
chops can produce topologically identical results (for example, the Great
Pyramid with its apex sliced off has the same skeleton as the cube). Also avoid
candidates that could only exist with warped faces.

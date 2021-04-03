# Jump flooding for Voronoi diagrams

Jump flooding[1] implementation in Python on CPU for Voronoi diagrams. Jump flooding is an approximate solution to propagate distance information in parallel.

This version respects the description of the Rong and Tan but **is not parallel**. A GPU compatible port of the code should be straightforward.

![Voronoi diagram](voronoi.png)

[1]G. Rong and T.-S. Tan, “Jump flooding in GPU with applications to Voronoi diagram and distance transform,” in Proceedings of the 2006 symposium on Interactive 3D graphics and games  - SI3D ’06, Redwood City, California, 2006, p. 109, doi: 10.1145/1111411.1111431.

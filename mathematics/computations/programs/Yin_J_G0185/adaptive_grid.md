---
author: Yin
---

# Rational grids fitted to initial pole congruences

<a id="trials"></a>
## Exact reconstruction after fitting the leading coefficients

The [movable-grid theorem](../../../claims/Yin_C_G0345_v889.md#statement) gives a sufficient degree at which the simultaneous conditions on a prescribed number of leading coefficients can be realized.
For smaller degrees the [program](adaptive_grid.py) uses the same target moments to propose grids, then applies [exact reconstruction with pole weights](trace_grid.md#pole-weights) at \(M=q(q+1)\), \(K=4M+1\).

| \(q\) | Trace degree | Moments fitted | First coefficient excluded |
| ---: | ---: | ---: | ---: |
| 5 | 121 | 4 | 5 |
| 5 | 481 | 8 | 10 |
| 5 | 981 | 16 | 17 |
| 6 | 643 | 12 | 14 |
| 40 | 1643 | 4 | 5 |

For \(q=5,n=981\) the first sixteen reconstruction steps admit an integer of the specified residue, and the seventeenth interval contains none.
At \(q=5,n=481\) and \(q=6,n=643\) one coefficient beyond those targeted also passes.
Each rejection concerns that particular grid.

The reference for the moment of index \(j\) is \(\phi_j(1/M)\), since the midpoint cosine sum vanishes.
The program uses rational Newton sums to choose the closest compatible trace target, resolving ties by rounding the lattice offset to the nearest even integer.
Starting at zero amplitudes, it numerically fits the \(k\) target sums of the [sine deformation](../../../claims/Yin_C_G0345_v889.md#deformation) with the positive root fixed at \(1/M\).
This is a grid proposal step.
The program rounds each proposed trace node to a multiple of \(2^{-40}\), checks strict ordering, then uses only rational and integer arithmetic to determine the first failed coefficient.
The finite conclusions use these rational nodes and do not require error bounds for the trigonometric proposal or existence of a polynomial on its unrounded grid.
Run the five checks from the repository root with Python 3.10 or later.

~~~sh
python -B mathematics/computations/programs/Yin_J_G0185/adaptive_grid.py
~~~

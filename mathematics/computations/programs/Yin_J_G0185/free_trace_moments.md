---
author: Yin
---

# Trace moment searches over all separating grids

<a id="census"></a>
## Degree ranges excluded at the first nonunit pole

Let \(q,n\ge2\), \(M=q(q+1)\), and seek a monic integral polynomial \(H\) of degree \(n\) with \(M^nH(1/M)=4M+1\), with one simple root in \((0,1/M)\) and the other \(n-1\) simple roots in \((-4,0)\).
The [complete moment search](../../../claims/Yin_C_G0345_v892.md#statement) takes no grid as input.
Its empty search tree excludes a point on every possible grid at that height and degree.
The following ranges were exhausted by [free_trace_moments.py](free_trace_moments.py), using integer arithmetic throughout the exclusions.

| \(q\) | Trace degrees \(n\), inclusive | Degrees excluded | Last Newton sum needed |
| ---: | --- | ---: | ---: |
| 5 | 2–70 | 69 | 12 |
| 6 | 2–100 | 99 | 13 |
| 8 | 2–160 | 159 | 12 |
| 12 | 2–350 | 349 | 11 |
| 40 | 2–4500 | 4499 | 14 |

At \(q=40\) the counts of exclusions at successive Newton sums \(1,\ldots,14\) are \(541,549,2,16,1074,10,597,219,163,564,320,131,232,80\).
The remaining degree \(n=3\) is rejected by the final pole and signature test.
It is the only degree reaching that test at each of the five heights.
The program reports a final rejection as stage \(n+1\), so its stage-four bin also includes this cubic.
A depth limit reached with a surviving proper prefix would leave that degree undecided.
The program also uses \(\Theta_j>2-2(n-1)\), since the exterior pair contributes more than two and each other pair contributes at least minus two.
To reproduce each row, run the following from this directory, replacing the height and upper degree by the two entries for that row.

~~~
python -B free_trace_moments.py 40 2 4500 --depth 15
~~~

<a id="controls"></a>
## A positive control with a different prescribed norm

For \(q=2,n=3,K=109\), the full search gives \(H(x)=x^3+6x^2+8x-1\).
Here \(6^3H(1/6)=109\), and the respective values at \(-4,-3,0\) are \(-1,2,-1\).
These values and the positive pole give one root in each required open interval.
For general positive \(K\equiv1\bmod M\) the implementation uses the elementary exterior and interior bounds, with the error-one estimate only for \(K<M^2\).
It uses the root-of-unity resultant bounds only for \(K=4M+1\), where the [irreducibility argument](../../../claims/Yin_C_G0345_v891.md#return) applies.
Exact endpoint, squarefreeness and Sturm checks use SymPy when a full coefficient vector survives.

The [integral-grid implementation](dual_grid_moments.py) applies the [independent rational matrix criterion](../../../claims/Yin_C_G0345_v893.md#residues) to the grid polynomial \(x(x+3)(x+4)\).
The positive control has three positive leading principal minors.
At the requested \(K=25\) on the same grid the second minor vanishes despite both individual nonconstant moments satisfying their scalar bounds.
The [independent matrix review](../../../audits/reviews/Yin_R_G0562_v1239.md#finding) includes further exact comparisons.

~~~
python -B free_trace_moments.py 2 3 3 --norm 109
python -B dual_grid_moments.py
~~~

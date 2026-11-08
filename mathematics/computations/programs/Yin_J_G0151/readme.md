---
author: Yin
---

# Complete moment enumeration at conductor 27 and a third-moment bound at 243

<a id="complete-27"></a>
## The entire prescribed class at conductor 27

Use the full odd trace grid, \(k=\lfloor p/\log p\rfloor\) negative residues at the smallest poles, and the [ternary integral representative](../../../ledger/Yin_L_G0464_v8.md#integral-sign-representative).
At \(p=27,\ k=8,\ \Delta=|\operatorname{Res}(B,Q)|=32\), the [layer valuation criterion](../../../ledger/Yin_L_G0464_v11.md#layer-valuations-and-orbits) makes every integral input of those signs and norm a totally positive unit multiple of this representative.
The [square representation and moment ellipsoid](../../../ledger/Yin_L_G0464_v10.md#moment-ellipsoid) therefore cover the whole class, including all exponent sizes.
Write \(n=13,\ a=2x,\ K=x^2+2,\ L=-4x\).
The separator \(1/2\) gives the integral form \(G=(2J-I)h_0(J)\) with determinant \(372384\).
The table counts square-root vectors up to their common sign.

| \(x\) | \(2L-K\) | Vectors on the shell | Also satisfy both moments | Also units | Also \(P(-1)>0\) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| \(-2\) | 10 | 1481 | 18 | 2 | 0 |
| \(-1\) | 5 | 37 | 1 | 0 | 0 |
| 0 | \(-2\) | 0 | 0 | 0 | 0 |
| 1 | \(-11\) | 0 | 0 | 0 | 0 |
| 2 | \(-22\) | 0 | 0 | 0 | 0 |

Both unit inputs are at \((K,L)=(6,8)\).
Their full degree-28 lifts give the following strict outward enclosures.

| \(P(-1)\) | Lower bound for \(M(P)\) | Upper bound for \(M(P)\) |
| ---: | ---: | ---: |
| \(-1\) | 5.74403664066 | 5.74403664068 |
| \(-33\) | 7.77397364529 | 7.77397364531 |

Each remainder is recovered by the witness option below, which outputs the adjusted \(h\) in ascending monomial order for \(C=D h\bmod B\).
The [unit-word calculation](../Yin_J_G0150/readme.md#whole-measures) gives both inputs independently within its finite box.
The [endpoint inequalities](../../../ledger/Yin_L_G0464_v11.md#finite-exclusions) also exclude every strict endpoint at \(p=27\) for the specified first two moments, even when \(\Delta\) varies.

<a id="enumeration"></a>
## Exact traversal and full root products

The [program](shell.py) builds \(h_0\) by the sign bits and the integral cosine-quotient product.
In the monic \(U_i(t/2)\) basis let \(H=h_0(J)\).
Use FLINT to propose a reduced basis and verify its unimodular change matrix \(A\) and the exact identity \(G'=AGA^t\).
For one-based index \(i\) let \(D_i\) be the leading minors of \(G'\), with \(D_0=1\), and \(c_{ij}\) the integer mixed minors returned in row \(i\) by fraction-free symmetric elimination.
The contribution from coordinate \(i\) in the completed square is
\[
   \frac{(D_i z_i+\sum_{j>i}c_{ij}z_j)^2}{D_iD_{i-1}}.
\]
The program verifies positive pivots and exact divisions when constructing the rows.
Starting at the last coordinate, if the remaining budget is \(s/D_i\), all admissible integers \(z_i\) satisfy
\[
    |D_i z_i+\sum_{j>i}c_{ij}z_j|\le\lfloor\sqrt{sD_{i-1}}\rfloor .
\]
Subtracting that square leaves a budget of the form \(s'/D_{i-1}\) with \(s'\) integral by the same Schur-complement identity.
The shell consists of the leaves with zero remaining budget, counting one sign by requiring the last nonzero coordinate to be positive.
The second independent equation uses \(AHA^t\), and unit status is checked by the exact resultant of the square-root polynomial with \(B\).
For every surviving unit, the program forms \(C,Q,P\), checks both leading-coefficient identities on \(C\) and the original absolute resultant, and computes \(P(-1)\).
It encloses \(\prod_\lambda\max(1,|\lambda|)\) over all roots of \(P\), retaining multiplicities even when the endpoint fails.
It verifies the total root count and that the final real ball has radius less than \(10^{-13}\).
The library returns each complex root as a ball with its multiplicity, and real ball operations enclose their exact inputs. [Polynomial roots](https://python-flint.readthedocs.io/en/latest/fmpz_poly.html#flint.fmpz_poly.complex_roots) and [real balls](https://python-flint.readthedocs.io/en/latest/arb.html).

<a id="quadratic-separator"></a>
## The next moment at conductor 243

At \(p=243,\ k=44\) the [two-moment and endpoint sieve](../../../ledger/Yin_L_G0464_v11.md#layer-valuations-and-orbits) leaves \(x=0\) and two possible positive-unit orbits at \(\Delta=2^{53}\).
Here we test a consequence for every integral input in the sign chamber satisfying the first two moments for \(x=0\).
Write \(N=\sum b_j^2 r_j\).
The [arcsine profile](../../../ledger/Yin_L_G0464_v7.md#prefix-cut) would require \(N=\int t^4\,d\alpha=6\) to match through this next moment.
Take \(F(t)=4+4t-t^2\), whose smaller root is \(2-2\sqrt2\) and whose other root exceeds 2.
The rationals \(-5/6\) and \(-33/40\) both have exactly 77 poles above them, as one checks by sign variation in the odd-grid recurrence.
The values of \(F\) there have opposite signs, so \(F(b_j)h(b_j)>0\) throughout the grid.
The integer \(S=\sum F(b_j)r_j\) equals \(4K+4L-N=8-N\) here.
Integrality follows either from the expansion of \(C/B\) at infinity or from the integer Jacobi matrix.
The arithmetic-geometric mean and \(\prod(4-b_j^2)=p\) give
\[
    S\ \ge\ \frac{n}{p}\left(p\,\Delta\,|\operatorname{Res}(B,F)|\right)^{1/n},
    \qquad n=121.
\]
The program checks by exact integer powering that this lower bound exceeds 2 already at \(\Delta=1\), and exceeds 3 at the prescribed \(\Delta=2^{53}\).
Consequently every such double-moment hit has \(N\le5\) for any nonzero resultant and \(N\le4\) at the prescribed resultant.
The latter inequality holds on both surviving orbits even before imposing the endpoint.
This forces a failure of the next profile coefficient at this conductor and does not count the double-moment hits or give a uniform gap at larger conductors.

<a id="next-conductor"></a>
## The profile to test at 6561

For \(p=6561,\ k=746\), the same Sturm recurrence puts \(y=-68/45\) inside the gap, with 2534 poles above it and \(p|B(y)|>2\).
Assume in addition to the two prescribed moments that \(N=6+2x^2\), as required for agreement with the next arcsine moment.
The [positive sums](../../../ledger/Yin_L_G0464_v12.md#negative-one) \(W=(2+y)L-2yK-N\) and \(E=N-yL-6(L-yK)+16(K-(2+y)U)\) must both exceed \(1/2\), by their full-grid norm bounds for any nonzero resultant.
At \(x=0,1,2\) the first sum is respectively \(2/45,-8/9,2/9\).
At \(x=-2\) the integer endpoint bound \(U\ge-1-2x\) gives \(E\le-34/9\).
At \(x=-1\) both \(W\) and the corresponding upper bound on \(E\) are \(136/45\).
Thus only \(x=-1\) survives these necessary tests for a matching third moment.
This additional arithmetic check was self-checked after the fixed reviews of the smaller conductors.
The double-moment family without that extra assumption has a wider scope.

<a id="replay"></a>
## Reproduction

Run from the repository root with Python, python-flint, NumPy and SymPy.
These commands print the complete table and its witnesses at 27 and the separator certificates at 243 and 6561.

~~~text
python -B mathematics/computations/programs/Yin_J_G0151/shell.py 27 --x -2 -1 0 1 2 --witnesses
python -B mathematics/computations/programs/Yin_J_G0151/shell.py 243 --separator
python -B mathematics/computations/programs/Yin_J_G0151/shell.py 6561 --separator
~~~

The raw shell interface also accepts the five profiles at 81 and 243 with separators \(-1/3\) and \(-5/6\), respectively, at the original representative.
At 81 the raw \(x=0\) shell of target 2 was empty.
The raw traversals at \(81,x=-1\) and \(243,x=0\) were stopped before completion; the counts in the [finite unit boxes](../Yin_J_G0150/readme.md#two-orbits-243) have their own explicit scopes.
The [full exterior inequalities](../../../ledger/Yin_L_G0464_v12.md#pairing) cover both strata at 243 without enumerating those raw shells.

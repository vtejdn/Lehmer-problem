---
author: Yin
---

# Complete moment enumeration at conductor 27 and a third-moment bound at 243

<a id="integer-pole-first-shell"></a>
## Integer pole and the first residual positive shell at conductor 19683

The [fixed rational-pole calculation](rational_pole.md) checks all five retained N=7 triples and forces \(h(-1)=32\) under their original integer, cut, resultant and small-measure hypotheses.
All four residual-matrix tests then pass, and the five inherited separate layer minima do not improve.
The [complete pole-pair cover](pole_pair.md) adds the actual integer contribution to the four retained continuous duals, covering all 4096 cells with first-success counts \((3739,203,66,17,71)\) and no unresolved cell.
The new pole-gap lower bound exceeds \(0.0043619\) in all 71 previously unresolved cells.
The [adopted C882v10 theorem](../../../claims/Yin_C_G0882_v10.md#decision-fixed-pole-first-shell) excludes \(1<M(P)\le101/100\) only for \((O,V,W)=(10,18,27)\), retaining measure one and the other four triples as unresolved.
The [independent native finding](../../../audits/reviews/Yin_R_G1107_v27.md#integer-pole-native-review) reproduces both programs at their full fixed scope.

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

<a id="conductor-19683"></a>
## Integer combinations at the next logarithmic cut

The [exact standard-library program](conductor19683.py) treats \(p=19683\), \(k=1990\), \(y=-161/100\) and the sign-representative norm \(\Delta=2^{4391}\).
It verifies the logarithmic cut by a rational series bound, counts all 7851 poles above the separator, and derives the nine layer parities.
Exact integer-root bounds for positive normalized layer traces are minimized over every nonnegative valuation vector of the required parity and total norm exponent.
The resulting rational inequalities, the strict endpoint, strict Cauchy--Schwarz and a cubic separator give the [necessary integer table](../../../claims/Yin_C_G0882_v3.md#statement).
The minimum unweighted layer mass is 15407, and the cubic-weighted minimum is 219942.
The dynamic program and its incumbent cutoff are justified in the [complete argument](../../../claims/Yin_C_G0882_v3.md#argument).
These finite arithmetic filters test all valuation allocations, without asserting realization by an integral input.

Requiring \(N=6+2x^2\) leaves \(x=-1,N=8,U=1\) and \(x=2,N=14,-5\le U\le13\).
The [second exact program](exterior19683.py) verifies the new quartic Sturm inequalities giving \(M(P)>25/16\) for \(x=-1,N=9\) and \(M(P)>49/25\) for \(x=-1,N=10\).
It also checks an endpoint and square-root argument for \(N\in\{7,8,9,10\}\) at every nonzero resultant in this branch.
The original \(6561\) quartic has negative real-line separation at \(N=8\) on the new cut.
The [scope of that failure](../../../claims/Yin_C_G0882_v3.md#remaining-cases) leaves the corresponding whole-measure inequality unresolved.
Both new programs use only Python integers and `fractions.Fraction`; no floating-point value supplies a certificate.

<a id="higher-19683"></a>
## Complete exterior costs from higher integral moments

The [fourth-moment program](higher_moments19683.py) uses the same conductor, signs and norm for \(x=2,K=6,L=-8,N=14\).
The positive weight \((b-y)(b-2/3)^2r\) gives the exact minimum weighted layer trace 14032098 and forces \(O=\sum b^3r\ge-20\).
Its fixed fifth-degree polynomial then certifies the [complete bound \(M(P)>5/4\)](../../../claims/Yin_C_G0882_v4.md#whole-measure) at every strict endpoint, without assuming that the exceptional trace roots are nonreal.
The program checks its factorization, Chebyshev expansion, trace difference, negative-variation value and strict rational cost margin.
The [independent finding](../../../audits/reviews/Yin_R_G1107_v9.md#fourth-moment-whole-19683) also verifies the mathematical coverage and the exhaustive valuation minimization.

The [negative-one program](negative_one_higher.py) treats \(x=-1,K=3,L=4,U=1\), using exact positive moment matrices with no further profile-matching assumption.
For \(N=8\) it leaves \(O=11,\ldots,15\); the \(O=14\) case additionally uses \(V=\sum b^4r\in\{26,27,28,29\}\).
Five fixed integer Chebyshev polynomials and rational Bernstein enclosures on 1024 subintervals give the [complete bound \(M(P)>23/20\)](../../../claims/Yin_C_G0882_v5.md#whole-measure) for all these cases.
Their strict certificate margins exceed respectively 6544, 2562, 53, 386 and 11815.
The [independent negative-one finding](../../../audits/reviews/Yin_R_G1107_v10.md#negative-one-higher-19683) checks the complete argument and reproduces these bounds by separate rational interpolation and subdivision.
The exact pole bracket is \(-161/100<b_{7851}<-1006/625\), checked by the recurrence's respective counts 7851 and 7850.
For \(N=7\), that program retains the [necessary 18 triples](../../../claims/Yin_C_G0882_v5.md#statement) of \(O,V,W=\sum b^5r\), without asserting realization.
The positive weight \((b-y)(b-1)^2(b-2)^2r\) has the normalized bound \(593881/656100\) at the specified norm.

The subsequent [degree-seven certificate set](negative_one_seven.md#full-measure-certificates) proves \(M(P)>26/25\) for eleven of the eighteen triples and \(M(P)>101/100\) for two more.
The [five remaining triples](negative_one_seven.md#exact-relaxed-models) admit exact positive-mass and fractional-occupancy models throughout the certified cut interval.
They rule out a positive margin from the stated degree-seven negative-variation and twice-maximum interface, without constructing an original integral polynomial.
The [independent finding](../../../audits/reviews/Yin_R_G1107_v16.md#negative-one-seven-review) reproduces all thirteen rational margins and forty exact model systems by separate methods.
The [complete C882v6 statement and argument](../../../claims/Yin_C_G0882_v6.md#statement) retain this thirteen/five partition and the exact method boundary.
The [two-unit-atom refinement](two_atom_models.md#scope) restores two different rational atoms, each of mass one, in all five residual models.
Its forty exact occupancy-control systems still satisfy all degree-seven identities throughout the cut interval, as stated in [C882v7](../../../claims/Yin_C_G0882_v7.md#statement) and checked by the [independent complete finding](../../../audits/reviews/Yin_R_G1107_v19.md#two-atom-models-review).
Actual pole-pairing intervals, integer coefficients and the complete resultant remain outside these relaxed models.
The [quadratic-sign refinement](../../../claims/Yin_C_G0882_v8.md#statement) localizes the actual exceptional roots, including both exterior components and the nonreal case.
The fixed [common-location certificates](diagonal_atom_scan.py) nevertheless give exact admissible double-atom models for all five residual triples, with the finite discovery scope and the rejected pole location retained in [L464v14](../../../ledger/Yin_L_G0464_v14.md#fixed-scan).
The [genuine terminal-interval test](../../../ledger/Yin_L_G0464_v15.md#existence-certificate) restores all 9840 actual root-to-pole intervals for the first triple, but its [endpoint diagnostic](../../../ledger/Yin_L_G0464_v15.md#endpoint-value) proves \(0.022<U<0.023\), failing the original \(U=1\).
The [endpoint-log comparison](endpoint_model.md#endpoint-value) also rejects the old step witnesses for that additional equation and retains one numerical proposal failure without an integer-domain exclusion.
The [independent terminal-interval review](../../../audits/reviews/Yin_R_G1107_v23.md#terminal-interval-review) verifies the complete native certificate and a separate reconstruction on the same fixed parameter box.

The default higher-moment and residual-model verifiers completed using only standard-library integer and rational arithmetic.
The separate terminal-interval verifier uses python-flint ball arithmetic for its existence and endpoint certificates.
The negative-one program's optional `--explore` mode uses sampled SciPy linear programs to propose coefficients, but is not called by the fixed certificate path and supplies no proof.
These tests produce neither an actual integral moment hit nor an arbitrarily small positive Mahler shell.

<a id="continuous-endpoint-duals"></a>
## Continuous endpoint constraints for the first residual triple

The [complete moving-pair reduction](../../../claims/Yin_C_G0882_v9.md#decision-endpoint-domain-19683) supplies exact polynomial moments, the original logarithmic endpoint equality and a safe nonreal pair domain for all five residual triples.
The [continuous dual calculation](endpoint_dual.md#scope) selects only \((10,18,27)\) and retains four rational degree-six polynomials in [the native input](inputs/endpoint_first_duals.json).
Exact root isolation and outward integration certify their four stated fixed positions without restricting the density to a numerical grid.
The [two moving-pair covers](endpoint_dual.md#moving-cover) leave 71 cells unresolved at target \(101/100\) and 86 at \(1001/1000\), so neither proves a new complete-measure lower bound.
The [independent finding](../../../audits/reviews/Yin_R_G1107_v25.md#fixed-dual-cover-review) reproduces both covers and all four fixed certificates, with historical LP proposals outside its reproduction scope.
The [native reproduction instructions](endpoint_dual.md#reproduction) distinguish the three solver-free checks from the optional bounded proposals and identify the required arithmetic libraries.

<a id="replay"></a>
## Reproduction

Run from the repository root with Python, python-flint, NumPy and SymPy.
These commands print the complete table and its witnesses at 27, check the later separator bounds, and verify the fixed higher-moment and residual-model certificates.

~~~text
python -B mathematics/computations/programs/Yin_J_G0151/shell.py 27 --x -2 -1 0 1 2 --witnesses
python -B mathematics/computations/programs/Yin_J_G0151/shell.py 243 --separator
python -B mathematics/computations/programs/Yin_J_G0151/shell.py 6561 --separator
python -B mathematics/computations/programs/Yin_J_G0151/conductor19683.py
python -B mathematics/computations/programs/Yin_J_G0151/exterior19683.py
python -B mathematics/computations/programs/Yin_J_G0151/higher_moments19683.py
python -B mathematics/computations/programs/Yin_J_G0151/negative_one_higher.py
python -B mathematics/computations/programs/Yin_J_G0151/negative_one_seven.py
python -B mathematics/computations/programs/Yin_J_G0151/two_atom_models.py
python -B mathematics/computations/programs/Yin_J_G0151/diagonal_atom_scan.py
python -B mathematics/computations/programs/Yin_J_G0151/terminal_intervals.py
~~~

The raw shell interface also accepts the five profiles at 81 and 243 with separators \(-1/3\) and \(-5/6\), respectively, at the original representative.
At 81 the raw \(x=0\) shell of target 2 was empty.
The raw traversals at \(81,x=-1\) and \(243,x=0\) were stopped before completion; the counts in the [finite unit boxes](../Yin_J_G0150/readme.md#two-orbits-243) have their own explicit scopes.
The [full exterior inequalities](../../../ledger/Yin_L_G0464_v12.md#pairing) cover both strata at 243 without enumerating those raw shells.

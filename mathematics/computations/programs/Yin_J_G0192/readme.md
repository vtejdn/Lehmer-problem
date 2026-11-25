---
author: Yin
---

# Exact comparison of small Mahler measures with squares of real exterior roots

<a id="comparison"></a>
## Primitive polynomials through degree 44

The [verifier](real_exterior_squares.py) checks the finite coefficient census used in the [real exterior square classification](../../../claims/Yin_C_G0901_v116.md#statement).
Run it from the checkout root with standard Python.

~~~text
python -B mathematics/computations/programs/Yin_J_G0192/real_exterior_squares.py
~~~

The program reads the [native coefficient catalogue](../../../literature/pdf/Mos26/AllSmallMeasures_200.txt) and reuses the [reciprocal reconstruction, Sturm and Graeffe routines](../Yin_J_G0188/readme.md#signatures).
Only the degree and half coefficients are used for the arithmetic.
The [catalogue completeness](../../../audits/literature/Mos26/readme.md#complete-small-cores) through degree 44 for primitive irreducible noncyclotomic minima of multiplicative measure below \(13/10\) is an external input.
All comparisons in the verifier use integer or rational arithmetic, and its results are printed to standard output.

For each reciprocal row \(P=X^{d/2}Q(X+X^{-1})\), the Sturm signature of \(Q\) gives the number of real roots on each side of \([-2,2]\) and the number of nonreal trace pairs.
There are 534 rows without a real exterior root, 46 with a single real exterior root and all other inverse pairs neutral, and 364 remaining rows having a real exterior root.
For a row in the second group the square of that root exceeds the measure because its absolute value already equals the measure.

For the remaining rows let \(G_j=\sum_i g_i X^i\) be the monic Graeffe polynomial after \(j\) root squarings.
The elementary symmetric functions and the maximum of \(G_j\) on the unit circle give
\[
        \max_i |g_i|/\binom di\ \le M(P)^{2^j}\le \sum_i |g_i| .
\]
Put \(S=2^{22}\).
Enclose the middle term on the grid \(S^{-1}\mathbb Z\), rounding the lower endpoint down and the upper endpoint up.
Taking \(j+1\) successive square roots, rounding each endpoint outwards by integer square roots, gives an enclosure \([l/S,h/S]\) of \(\sqrt{M(P)}\).
When \(1<l/S\le h/S<2\), the monotone transformation \(r\mapsto r+r^{-1}\) gives the corresponding interval for the absolute trace of a prospective real root.
The verifier counts the real trace roots below and above this interval in absolute value and outside \([-2,2]\), using both signs and exact Sturm variations at its endpoints and at \(\pm2\).
It verifies that all the real exterior roots have been counted and checks that the rational endpoints are not trace roots.

The 364 rows first separated in the implemented test at steps \(6,7,8,9,10,11,12,13,16\), with respective counts \(55,169,87,20,15,13,3,1,1\).
Across all 944 source rows, 304 real exterior roots had square strictly below the measure and 123 strictly above it, counting the 46 single-exterior rows.
There were no equalities.

<a id="lifts"></a>
## The Salem rows giving real square roots in the degree range

Of the 46 signed Salem rows, the following 27 have degree at most 22.
Line numbers refer to the native text file, starting at one.

| Degree | Source lines |
| ---: | --- |
| 8 | 152 |
| 10 | 154, 155, 156, 157, 160 |
| 12 | 163 |
| 14 | 168, 169, 170, 172 |
| 16 | 182 |
| 18 | 195, 198, 203, 204, 208, 210, 214 |
| 20 | 223, 226, 240, 248 |
| 22 | 257, 268, 280, 300 |

Let \(Q\) denote the chosen row polynomial oriented to have positive exterior root \(\theta\), by replacing \(X\) with \(-X\) exactly when its exterior root is negative.
Only line 154 already has the positive orientation.
Since \(\theta\) is the unique real root of \(Q\) above one and is simple, \(Q\) is negative on \((1,\theta)\) and positive on \((\theta,\infty)\).
Homogeneous integer evaluations at \(8/7\) and \(59/50\) show that all 27 roots exceed \(8/7\), and only the root on line 154 is below \(59/50\).
The [degree and irreducibility argument](../../../claims/Yin_C_G0901_v116.md#all-inputs) shows why these rows, with the single substitution \(Q(X^2)\), give the full list of uncompressed equality cases.

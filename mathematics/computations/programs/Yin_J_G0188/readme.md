---
author: Yin
---

# A degree-bounded search for conjugate groups of radial rank at least two

<a id="cut"></a>
## Two rational cuts in the primitive catalogue

Run the [verifier](radial_cores.py) from the checkout root with standard Python.

~~~text
python -B mathematics/computations/programs/Yin_J_G0188/radial_cores.py
~~~

The source is Mossinghoff's [native 31 May 2026 full table](../../../literature/pdf/Mos26/AllSmallMeasures_200.txt), with its [degree coverage](../../../audits/literature/Mos26/readme.md#complete-small-cores).
The verifier reads degree and polynomial coefficients through the [source parser](../Yin_J_G0185/pole_catalogue.py).
All comparisons use only the coefficients, independently of the decimal measure and the reported number of exterior roots.
The [Graeffe implementation](../Yin_J_G0144/pilot.py) successively squares all roots.
After \(j\) steps its monic degree-\(d\) output \(G=\sum_k g_kX^k\) satisfies
\[
       \max_k |g_k|/\binom dk \le M(G)=M(P)^{2^j}\le\sum_k|g_k|.
\]
The lower bound follows from the elementary symmetric functions and the upper bound from the supremum on the unit circle.
As in the [single-cut certificate](../Yin_J_G0187/readme.md#cut), multiplying by the positive denominator to the power \(2^j\) gives strict integer comparisons.

The executed upper cut at \(3049/2500=1.2196\) put fourteen of the 944 degree-at-most-44 rows below the threshold and 930 above it.
The five higher degree lists \(46,48,50,52,54\) had respectively \(107,80,76,66,66\) rows, all above that cutoff.
The per-degree minimizing polynomials in those lists have been [matched to the published minima](../../../audits/reviews/Yin_R_G0562_v1113.md#computation).
For the fourteen survivors, the second cut at \(12193/10000=1.2193\) put thirteen below and only line 197 above.
All comparisons terminated with at most sixteen root squarings.

<a id="signatures"></a>
## Real and complex exterior places below the upper cut

For each survivor the verifier constructs the degree-\(n=d/2\) trace polynomial \(Q\) from the leading half of \(P=X^nQ(X+X^{-1})\) using the [trace recurrence](../Yin_J_G0187/small_cores.py).
It uses [exact rational Sturm chains](../Yin_J_G0144/checks/independent_trace56_review.py) and checks that the final remainder is a nonzero constant and that neither endpoint is a root.
Its four arguments are \(-B,-2,2,B\) with \(B=2+\max_{0\le i<n}|[X^i]Q|\), beyond the monic Cauchy bound.
Successive differences count trace roots below \(-2\), in \((-2,2)\), and above two, respectively.
The remaining trace roots come in nonreal conjugate pairs.

| Source lines | Degree | Sturm variations | Real trace counts, left to right | Nonreal trace pairs |
| --- | ---: | --- | --- | ---: |
| 154 | 10 | \(5,5,1,0\) | \(0,4,1\) | 0 |
| 155 | 10 | \(5,4,0,0\) | \(1,4,0\) | 0 |
| 168, 169 | 14 | \(7,6,0,0\) | \(1,6,0\) | 0 |
| 195 | 18 | \(9,8,0,0\) | \(1,8,0\) | 0 |
| 196 | 18 | \(8,8,1,1\) | \(0,7,0\) | 1 |
| 197 | 18 | \(8,7,1,1\) | \(1,6,0\) | 1 |
| 219, 220, 221 | 20 | \(9,9,1,1\) | \(0,8,0\) | 1 |
| 255 | 22 | \(10,10,1,1\) | \(0,9,0\) | 1 |
| 304, 305 | 24 | \(11,11,1,1\) | \(0,10,0\) | 1 |
| 413 | 28 | \(13,13,1,1\) | \(0,12,0\) | 1 |

The thirteen rows below the lower cut have five single real exterior roots and eight single complex-conjugate exterior pairs, one such root or pair per polynomial.
Line 197 alone has both types.

<a id="frobenius"></a>
## The sign change over thirteen

The witness has leading through central coefficients \((1,1,1,0,-1,-1,-1,0,0,1)\).
For its trace \(Q\) and reciprocal lift \(P\), each reported reduction has derivative gcd one.
The verifier uses [finite-field polynomial division and Frobenius factor degrees](../Yin_J_G0166/split_traces.py).
Successive gcds with \(X^{p^j}-X\) detect the irreducible degrees dividing \(j\), with the lower-degree factors removed at each step.
The actual results are

| Polynomial | Prime | Degrees of irreducible factors |
| --- | ---: | --- |
| \(Q\) | 2 | 9 |
| \(Q\) | 13 | 2, 7 |
| \(P\) | 13 | 4, 14 |

The [group argument at this candidate](../../../claims/Yin_C_G0901_v63.md#group) uses the fourteenth power of the last Frobenius to flip exactly two inverse pairs.
The catalogue bounds describe the executed finite comparisons and use the published classification at its stated range.

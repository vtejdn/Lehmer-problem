---
author: Yin
---

# Degree-specific Mahler measure cutoffs for the two-value test at 251

<a id="census"></a>
## Four reciprocal polynomial enumerations

For each degree \(D\) in the table, no monic irreducible noncyclotomic reciprocal integer polynomial has degree \(D\) and Mahler measure at most \(T_D\).
Write \(s_k\) for the \(k\)-th power sum of all roots and \(h=D/2\).
The table counts the sign-normalized polynomials after excluding power substitutions and records the survivors at successive stages.

| Degree and full summary | \(T_D\) | First-half representatives | Through \(s_{h+1}\) | Through \(s_{h+9}\) | Reach exact classification |
| ---: | ---: | ---: | ---: | ---: | ---: |
| [56](../../../../outputs/Yin_J_G0179/versions/v12/d56/summary.json) | \(1101/1000\) | 3,627,987,860 | 456,165,873 | 52,685,101 | 7,181 |
| [58](../../../../outputs/Yin_J_G0179/versions/v12/d58/summary.json) | \(2193/2000\) | 4,524,093,746 | 407,549,351 | 37,847,314 | 6,930 |
| [68](../../../../outputs/Yin_J_G0179/versions/v12/d68/summary.json) | \(541/500\) | 1,918,206,514 | 155,887,643 | 15,530,267 | 11,587 |
| [70](../../../../outputs/Yin_J_G0179/versions/v12/d70/summary.json) | \(431/400\) | 2,004,938,344 | 86,545,439 | 8,896,192 | 9,553 |

Of the 12,075,226,464 representatives, 35,251 reached exact classification.
Exact divisibility by a cyclotomic polynomial excluded 35,250 of them.
For the remaining degree-56 polynomial the coefficient of \(X^6\) after eight Graeffe steps was \(37360284721810959382\), exceeding the integer upper bound \(1618136021964206191\).

<a id="prime"></a>
## Excluding the three remaining degree pairs

For two different qualifying measures at \(p=251\), the [prior degree restriction](../../../../../claims/Yin_C_G0345_v429.md#primes) gives the unordered degree pair \(\{56,68\},\{56,70\}\) or \(\{58,68\}\).
At width \(b=126\) that same strict derivative budget gives
\[
      M(P_1)M(P_2)<2^{1/4}
            \left(\frac{pb+1}{2pb+1}\right)^{1/p}.
\]
The products of the tabulated thresholds for the three pairs are \(595641/500000,\ 474531/400000,\ 1186413/1000000\), respectively.
For each such product \(z\) the [driver](sieve.py) verifies \(z^{4p}(2pb+1)^4>2^p(pb+1)^4\) by integer arithmetic, as well as \((b-1)^8<p^7<b^8\).
Both qualifying polynomials would exceed their respective tabulated thresholds, contradicting the strict budget.

<a id="bounds"></a>
## Certified boxes and exhaustive searches

The [ellipse certificates](../v7/readme.md#weights) supply two maxima \(u,v\) for the same rational auxiliary weights at radii \(1,R^j\), with \(R=1091/1000\).
For the current cutoff \(T_D\), compute the least integer \(a\) with \(R^a\ge T_D^{10000}\) by exact bisection.
In increasing degree the four values of \(a\) are 11048, 10578, 9049 and 8571, respectively.
For every \(k\le h\), choose the least upper bound on \(|s_k|\) among rows satisfying \(R^j\ge T_D^k\) from the [convex chord](../v11/readme.md#boxes)
\[
           h u+\min\{1,ak/(10000j)\}\max\{0,v-u\}.
\]
The [power-field descent](../../../../../ledger/Yin_L_G0462_v270.md#descent) and the [published small-degree theorem](../../../../../audits/literature/MRW08/Yin_U001.md#degree) require every power field of a candidate to have degree at least 56, since all four cutoffs are below Lehmer's measure.
An auxiliary vanishing on a signed trace would give degree at most sixteen, so the necessary resultants are nonzero.
The same published theorem excludes \(P=S(X^q)\) for \(q>1\), since \(S\) would have the same positive measure and degree at most 35.
The generated boxes.json for each degree records all selected rows, exact cutoffs on the traces, and the tensor count.

Degrees 56 and 58 use the [two-list native enumeration](../v10/readme.md#enumeration).
Here every upper bound \(B_j\) for \(j>16\) satisfies \(j\le2B_j+1<2j\), so the suffix enumeration and the tests for power substitutions in the prefix apply.
The certified integer caps on the first nine reflected numerators are 11,071,513 and 13,512,514 respectively.
Degrees 68 and 70 use the [direct coefficient recursion](../v11/readme.md#enumeration), computing all reflected Newton numerators with signed 64-bit arithmetic.
At every degree the configuration checks the coefficient and numerator bounds before starting the native search.
The post-center exclusions use reciprocal trace bounds through \(s_{120}\), the endpoint and quadratic cyclotomic factors, and ten modular Graeffe comparisons at the actual rational cutoff.

<a id="verification"></a>
## Independent count and divisor checks

The [verifier](verify.py) checked the number of representatives in all 151 disjoint \((s_1,s_2)\) slices by Newton congruence tensors and inclusion–exclusion over the prime divisors of \(D\).
It compares the individual filter stages on selected prefix subtrees with unrestricted-integer Newton recursion and direct Graeffe convolution.
Each slice also supplies the first half of every polynomial reaching final classification and its reported exclusion.
The verifier checks a claimed divisor \(\Phi_n\) by summing \(|P(\zeta_n^u)|^2\) over units \(u\bmod n\), using the exact Ramanujan sum expressed in terms of the divisors of \(n\).
This sum vanishes precisely when the monic cyclotomic polynomial divides \(P\).
The reported coefficient from any final Graeffe exclusion is recalculated by full integer convolution.

From the repository root use Python with NumPy and the .NET Framework C# compiler on Windows, or Mono on Unix.
Regenerate the v7 certificates if needed, run the four finite searches, then use the last command at each of the degrees 56, 58, 68 and 70.

~~~text
python -B mathematics/computations/programs/Yin_J_G0179/versions/v7/larger_boxes.py
python -B mathematics/computations/programs/Yin_J_G0179/versions/v12/sieve.py --workers 6
python -B mathematics/computations/programs/Yin_J_G0179/versions/v12/verify.py --degree 56
~~~

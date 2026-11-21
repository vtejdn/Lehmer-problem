---
author: Yin
---

# Degree 66 at Mahler measure 1.091

<a id="census"></a>
## Complete classification

There is no monic irreducible noncyclotomic reciprocal polynomial in \(\mathbb Z[X]\) of degree 66 with \(M(P)\le T=1091/1000\).
The [version-seven bounds](../v7/readme.md#bounds) contain 51,979,784,484 primitive representatives up to \(X\mapsto-X\).
Here primitive means that the polynomial admits no nontrivial power substitution.
A substitution \(P(X)=S(X^q)\), \(q>1\), would give \(1<M(S)=M(P)\le T\) in degree at most 33, contrary to the [published sub-Lehmer degree bound](../../../../../audits/literature/MRW08/Yin_U001.md#degree).

| Applied condition | Representatives remaining |
| --- | ---: |
| First-half box, power substitutions removed, up to sign | 51,979,784,484 |
| First reflected sum \(s_{34}\) | 3,222,528,314 |
| All reflected sums through \(s_{42}\) | 193,654,198 |
| Nonzero at \(1\) and \(-1\) | 86,134,151 |
| All reflected sums through \(s_{120}\) | 23,657,396 |
| Indivisible by \(\Phi_3,\Phi_4,\Phi_6\) | 5,942,923 |
| Also pass the modular Graeffe comparisons | 19,799 |
| Also pass exact cyclotomic division | 5 |
| Also pass exact Graeffe comparisons | 0 |

The five polynomials in the last comparison violate the coefficient bound at the eighth Graeffe iteration.
The [summary](../../inputs/versions/v9/summary.json) gives each of their 34 first-half coefficients, the index and value of a violating coefficient after squaring, and its exact integer upper bound.

<a id="suffix"></a>
## Power substitutions and reflected tests

Fix the first seventeen Newton sums.
For \(q=2,3,11\), suppose all \(s_k\) with \(q\nmid k\), \(1\le k\le17\), vanish.
For the next \(j\le33\) outside the multiples of \(q\), all proper divisors are also outside them, and by induction their sums vanish.
The [integrality congruences](../../readme.md#counts) imply \(j\mid s_j\), and \(B_j<j\) forces \(s_j=0\).
Newton's identities then give zero for each \(c_j\) with \(q\nmid j\) through the center, and reciprocity gives zero throughout, since \(q\mid66\).
Conversely \(P\in\mathbb Z[X^q]\) has vanishing sums outside the multiples of \(q\).
These three prefix tests cover all nontrivial power substitutions, including their intersections.
After excluding them the first nonzero odd sum through 17 fixes the sign.

The [degree-64 suffix argument](../v8/readme.md#suffix) now starts at \(j=18\) and reflects about \(h=33\).
The low block comprises \(18,\ldots,25\), and the high block comprises \(26,\ldots,33\).
The first-half sums in each coordinate are spaced by \(j\), with one or two choices per index.
For the new reflected range \(34\le k\le42\), \(-\log(1-U)\) still needs only \(U+U^2/2\), since \(U\) has order at least 18.
All pairs \(i+j\le42\) in the quadratic part belong to the low block, and \(V_iV_j/P_0^2=X^{i+j}+O(X^{52})\).
Thus the two short lists give all nine reflected sums as in degree 64, with the reflection \(c_{66-t-j}\) replacing \(c_{64-t-j}\).

The [native program](Sieve66.cs) uses the [same integer and modular comparisons](../v8/readme.md#finishing) with the degree-66 caps \(\lfloor64+T^k+T^{-k}\rfloor\) and binomials \(\binom{66}{i}\).
Here \(C_{33}=516675\), \(\sum_{i=0}^{33} C_i=2852947\), and the first-half absolute Newton numerators are bounded by \(91294304\).
Conditional on passing earlier traces, the largest absolute-numerator bounds are \(52377291\) for indices 34 through 42 and \(12030141857\) for indices 43 through 120.
This justifies the centered 32-bit lift for the list comparisons and direct signed 64-bit Newton arithmetic thereafter.
In the endpoint evaluations the odd middle coefficient \(c_{33}\) contributes only once.
The [driver](sieve.py) then applies the exact residue lower bounds from up to ten Graeffe iterations, cyclotomic division over \(\mathbb Z\) and, as needed, exact integer Graeffe iterates.

<a id="reproduction"></a>
## Reproduction and independent calculations

From the repository root use Python and NumPy, with the .NET Framework C# compiler on Windows or Mono on Unix.
The first command regenerates the incoming certificates from the tracked weights.

~~~text
python -B mathematics/computations/programs/Yin_J_G0179/versions/v7/larger_boxes.py
python -B mathematics/computations/programs/Yin_J_G0179/versions/v9/sieve.py --workers 6
python -B mathematics/computations/programs/Yin_J_G0179/versions/v9/verify.py
~~~

The [verification program](verify.py) independently counts each of the 39 first-sum pairs by the [congruence tensors](../v2/cyclotomic_prefixes.py), using inclusion and exclusion over all subsets of \(\{2,3,11\}\).
For \(s_1=0\) each surviving sign pair lies in the same \((s_1,s_2)\) slice, so the count there is divided by two.
It also compares complete classifications on six fixed seventeen-sum prefixes using direct, unrestricted-precision Newton recurrences.
Three of these prefixes force the respective substitutions with exponents 2, 3 and 11, tested by examining the actual completed coefficients.
For each of the five final witnesses it rebuilds all eight iterates by ordinary integer convolution and checks the coefficient and rational bound independently of the packed-integer squaring used by the search.

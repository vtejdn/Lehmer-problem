---
author: Yin
---

# Reciprocal degrees 68 through 84 at Mahler measure 1.06

<a id="census"></a>
## Complete enumeration

No monic irreducible noncyclotomic reciprocal integer polynomial of any even degree \(D=68,70,\ldots,84\) has Mahler measure at most \(T=53/50\).
The computation enumerated 2,302,738,123 representatives, of which 46,846 reached exact cyclotomic division.
Every one of those final candidates had a cyclotomic factor.
The degree-68 case applies to the [remaining square pair at 277](../../../../../claims/Yin_C_G0345_v429.md#primes), since \(53^{12}>2\cdot50^{12}\).

| Degree and full summary | Initial representatives | First reflected trace | First nine reflected traces | Reach modular Graeffe | Reach exact cyclotomic division |
| ---: | ---: | ---: | ---: | ---: | ---: |
| [68](../../inputs/versions/v11/d68/summary.json) | 19,318,022 | 1,596,030 | 374,045 | 2,970 | 2,479 |
| [70](../../inputs/versions/v11/d70/summary.json) | 25,449,483 | 2,015,752 | 457,297 | 3,242 | 2,557 |
| [72](../../inputs/versions/v11/d72/summary.json) | 38,241,010 | 2,919,101 | 557,054 | 3,804 | 2,768 |
| [74](../../inputs/versions/v11/d74/summary.json) | 31,098,523 | 2,508,848 | 506,923 | 3,848 | 2,698 |
| [76](../../inputs/versions/v11/d76/summary.json) | 44,937,813 | 3,320,272 | 675,589 | 5,152 | 3,325 |
| [78](../../inputs/versions/v11/d78/summary.json) | 148,088,202 | 8,393,381 | 1,310,253 | 9,787 | 5,516 |
| [80](../../inputs/versions/v11/d80/summary.json) | 192,066,671 | 12,888,956 | 1,709,707 | 13,497 | 6,544 |
| [82](../../inputs/versions/v11/d82/summary.json) | 628,575,637 | 21,137,921 | 2,780,864 | 18,820 | 8,459 |
| [84](../../inputs/versions/v11/d84/summary.json) | 1,174,962,762 | 40,981,529 | 4,224,413 | 30,897 | 12,500 |

<a id="boxes"></a>
## Bounds from larger ellipses

Set \(h=D/2\), \(R=1091/1000\), and \(s_k=\sum_\alpha\alpha^k\) over all roots with multiplicity.
For each \(k\le h\), the [driver](sieve.py) considers each [v7 weight row](../v7/readme.md#weights) with outer radius \(R^j\ge T^k\).
Write \(u,v\) for the certified upper bounds for that same weight row at radii \(1,R^j\), respectively.
An auxiliary vanishing at either signed power trace would give a power field of degree at most sixteen, contrary to the [power-field lower bound](../../../../../claims/Yin_C_G0345_v429.md#degree).
The [radial maximum](../../readme.md#ellipse) is even and convex as a function of the logarithm of the radius, hence nondecreasing for radii at least one.
Thus \((h-1)u+v\) bounds \(|s_k|\) in all nine degrees.
The first three enumerations use the least such bound for each \(k\).
For \(D\ge74\) the program sharpens the same calculation by the convex chord.
The integer inequality \(T^{10000}<R^{6691}\) gives
\[
       |s_k|\le h u+\min\{1,6691k/(10000j)\}\max\{0,v-u\}.
\]
Indeed the chord fraction at radius \(T^k\) is \(k\log T/(j\log R)\), which the displayed minimum bounds from above.
The driver takes the integer part after minimizing over all available rows with adequate radius.
Each degree's generated boxes.json records its bounds, chosen v7 rows, numerator bounds and independent congruence count.

<a id="enumeration"></a>
## Newton recursion and exclusions

The [native worker](Reciprocal.cs) chooses each \(s_k\) in its certified interval subject to the divisibility by \(k\) in Newton's identity for the next monic coefficient.
The first \(h\) coefficients determine the full reciprocal polynomial.
Changing \(X\) to \(-X\) permits a positive first nonzero odd-indexed sum.
If all odd-indexed sums through \(h\) vanish, the coefficient recursion and reciprocity put the polynomial in \(\mathbb Z[X^2]\).
For each odd prime \(q\mid D\) the code also tests membership in \(\mathbb Z[X^q]\) directly on the chosen coefficients through \(h\), since reflection about \(D\) preserves divisibility of an index by \(q\).
A power substitution would have the same positive measure in degree at most 42, contradicting the [published small-degree theorem](../../../../../audits/literature/MRW08/Yin_U001.md#degree).

The reflected trace bound through \(k=120\) is \(\lfloor D-2+T^k+T^{-k}\rfloor\) by [reciprocal pairing and convexity](../../../../../ledger/Yin_L_G0462_v266.md#linear).
After the first nine reflections the worker excludes zeros at \(1,-1\), and after the last trace it checks the integer remainders at \(\Phi_3,\Phi_4,\Phi_6\).
It applies the [modular Graeffe coefficient test](../v8/readme.md#finishing) at ten successive squarings, with the threshold \(\binom Di T^{2^g}\) at step \(g\).
All these exclusions use necessary conditions.
The [final classification](../v10/sieve.py) tests exact cyclotomic divisibility over \(\mathbb Z[X]\), using the degree and the present cutoff.

Before enumeration the driver computes upper bounds \(C_0=1,\ C_i=\lfloor\sum_{j=1}^i B_jC_{i-j}/i\rfloor\) on the absolute first-half coefficients from the box \(B_j\).
It reflects these bounds and uses the preceding exact trace caps to bound each Newton numerator by the triangle inequality.
Across the nine degrees the first-half coefficients fit in signed 32 bits and all Newton numerators in signed 64 bits.
Endpoint sums and the coefficients of the three quadratic remainders are bounded by the full coefficient one-norm since the powers of \(X\) modulo those quadratics have coefficients in \(\{0,1,-1\}\).
Unsigned 64-bit wraparound is used only for Graeffe residues.

<a id="verification"></a>
## Verification and reproduction

The [verification program](verify.py) checked all 454 disjoint \((s_1,s_2)\) counts by Newton congruence tensors and inclusion–exclusion over the prime divisors of each degree.
It compared selected complete prefix subtrees against unrestricted-precision Newton recurrences, integer cyclotomic division and direct Graeffe convolution, including all filter stages and examples reaching exact division.
For degree 68 one such example was \(\Phi_{15}\Phi_{21}\Phi_{105}=(X^{70}+X^{35}+1)/\Phi_3\).
The linked summaries give the exact divisors by order, classification counts and direct checks.

From the repository root use Python with NumPy and the .NET Framework C# compiler on Windows, or Mono on Unix.
First regenerate the v7 certificates if needed, then run the enumeration and verify each desired degree, replacing 68 in the last command with that degree.

~~~text
python -B mathematics/computations/programs/Yin_J_G0179/versions/v7/larger_boxes.py
python -B mathematics/computations/programs/Yin_J_G0179/versions/v11/sieve.py --workers 6
python -B mathematics/computations/programs/Yin_J_G0179/versions/v11/verify.py --degree 68
~~~

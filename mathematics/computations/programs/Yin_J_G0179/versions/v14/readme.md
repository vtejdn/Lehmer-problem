---
author: Yin
---

# Degree 72 at multiplicative measure 1.068

<a id="census"></a>
## A complete degree-72 census

There is no monic reciprocal irreducible noncyclotomic integer polynomial of degree 72 with multiplicative Mahler measure at most \(T=267/250\).
The [enumeration](census.py) and [verified summary](../../../../outputs/Yin_J_G0179/versions/v14/d72/summary.json) give the following counts.

| Stage | Count |
| --- | ---: |
| Sign-normalized first-half tuples after removal of substitutions | 243,366,685 |
| Pass first reflected trace | 3,114,043 |
| Pass nine reflected traces | 331,518 |
| Of these, vanish at \(1\) or \(-1\) | 280,301 |
| Excluded by a later trace, through index 120 | 951 |
| Divisible by \(\Phi_3,\Phi_4\) or \(\Phi_6\) after the trace tests | 46,745 |
| Reach full integer division | 3,521 |
| Of these, have an exact cyclotomic divisor | 3,446 |
| Exceed a Graeffe coefficient bound after seven or eight squarings | 74 or 1, respectively |

<a id="bounds"></a>
## Trace bounds and reduction

The [existing degree theorem](../../../../../claims/Yin_C_G0345_v429.md#degree) gives degree at least 68 for every power field of a candidate, since \(T<1.091\).
A zero of a signed trace auxiliary of degree at most eight would force the corresponding power-field degree to be at most sixteen.
Consequently the nonzero-resultant argument of the [ellipse bounds](../v11/readme.md#boxes) applies to every positive power and to both signs.
A nontrivial substitution \(Q(X^m)\) would have the same positive measure in degree at most 36, excluded by the same degree theorem.

Put \(R=1091/1000\).
The integer powers give \(R^{7553}<T^{10000}\le R^{7554}\).
For each row in the [v7 certificates](../v7/readme.md#weights) with radii \(1,R^j\) and \(R^j\ge T^k\), use the same row's certified bounds \(u,v\) and the chord
\[
 |s_k|\le 36u+\min(1,7554k/(10000j))\max(0,v-u).
\]
The unweighted bound is \(70+T^k+T^{-k}\).
Taking the floor of the least applicable bound for each \(1\le k\le120\) gives the [census bounds and selected rows](../../../../outputs/Yin_J_G0179/versions/v14/d72/census.json).
The selected bounds for \(k\le43\) come from ellipse rows and all later ones from the unweighted formula.

The [v13 recursion](../v13/readme.md#enumeration) constructs integral first-half coefficients by the prime-power Newton congruences, reflects them, and tests the necessary trace conditions and the linear and quadratic cyclotomic factors.
Its signed machine-integer and counting bounds are checked with the present degree and all 120 present limits.
The [final classifier](../v12/sieve.py) uses exact cyclotomic division and, when needed, exact Graeffe squaring at the present \(T\).
After \(g\) squarings a candidate's coefficient of \(X^i\) has absolute value at most \(\binom{72}{i}T^{2^g}\), by the elementary symmetric formula for the powered roots.

<a id="verification"></a>
## Independent calculations and reproduction

The [verifier](check.py) checks the 120 selected bounds by rational arithmetic against the v7 rows and the unweighted formula.
It compares each of the 46 first-pair counts with a tensor count using inclusion and exclusion for divisibility of the nonzero coefficient indices by 2 or 3.
It checks sign, length, first-half Newton sums, slice membership and substitution exclusions for each of the 3,521 final polynomials.
The integer Ramanujan energy vanishes at each claimed cyclotomic divisor and exact convolution reproduces all 75 Graeffe witnesses. [Integer tests](../v12/verify.py)
A separate unrestricted-integer Newton recurrence checks the whole subtree with first twelve traces \((0,-2,0,2,0,4,7,-6,0,8,0,-4)\), including its 64 representatives, two through nine reflections, one endpoint zero and one final candidate.
The verifier also computes the exact [degree deficits and prime comparisons](../../../../../claims/Yin_C_G0345_v454.md#sums).

From the repository root use Python with NumPy and the C# compiler and runtime specified for the [v13 enumeration](../v13/readme.md#verification).
When the v7 certificates are absent, first regenerate them from the [retained weights](../v7/readme.md#weights).

~~~text
python -B mathematics/computations/programs/Yin_J_G0179/versions/v7/larger_boxes.py
python -B mathematics/computations/programs/Yin_J_G0179/versions/v14/census.py --workers 5
python -B mathematics/computations/programs/Yin_J_G0179/versions/v14/check.py
~~~

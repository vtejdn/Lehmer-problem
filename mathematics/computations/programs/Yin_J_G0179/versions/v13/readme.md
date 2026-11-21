---
author: Yin
---

# Small reciprocal measures in even degrees 86 through 110

<a id="census"></a>
## Thirteen complete enumerations

For each degree \(D\) below, the enumeration excludes every monic reciprocal irreducible noncyclotomic integer polynomial of that degree with multiplicative Mahler measure at most the indicated \(T\).
The first count is the number of admissible first-half Newton tuples after sign normalization and removal of power substitutions.
The next two columns give the counts after one and nine reflected traces.
All 818 final polynomials have a cyclotomic divisor.

| Degree and summary | \(T\) | First-half tuples | One reflection | Nine reflections | Exact division |
| ---: | ---: | ---: | ---: | ---: | ---: |
| [86](../../inputs/versions/v13/d86/summary.json) | 1.042 | 5,282,539 | 286,483 | 109,803 | 422 |
| [88](../../inputs/versions/v13/d88/summary.json) | 1.04 | 5,512,495 | 309,183 | 125,860 | 297 |
| [90](../../inputs/versions/v13/d90/summary.json) | 1.036 | 3,935,653 | 273,261 | 114,991 | 93 |
| [92](../../inputs/versions/v13/d92/summary.json) | 1.027 | 717,446 | 88,397 | 42,829 | 0 |
| [94](../../inputs/versions/v13/d94/summary.json) | 1.027 | 1,206,016 | 109,337 | 63,158 | 1 |
| [96](../../inputs/versions/v13/d96/summary.json) | 1.027 | 2,004,645 | 152,542 | 84,310 | 0 |
| [98](../../inputs/versions/v13/d98/summary.json) | 1.027 | 2,440,226 | 173,176 | 94,633 | 3 |
| [100](../../inputs/versions/v13/d100/summary.json) | 1.022 | 1,281,522 | 117,454 | 66,642 | 0 |
| [102](../../inputs/versions/v13/d102/summary.json) | 1.02 | 1,185,995 | 114,112 | 51,711 | 0 |
| [104](../../inputs/versions/v13/d104/summary.json) | 1.02 | 1,420,032 | 150,788 | 64,838 | 0 |
| [106](../../inputs/versions/v13/d106/summary.json) | 1.02 | 2,247,980 | 219,301 | 92,093 | 0 |
| [108](../../inputs/versions/v13/d108/summary.json) | 1.02 | 4,812,815 | 296,140 | 118,514 | 2 |
| [110](../../inputs/versions/v13/d110/summary.json) | 1.02 | 5,402,700 | 332,350 | 141,725 | 0 |
| Total | | 37,450,064 | 2,622,524 | 1,171,107 | 818 |

<a id="bounds"></a>
## Bounding the reflected traces on smaller ellipses

Write \(h=D/2\), \(R=1091/1000\), and let \(s_k\) be the \(k\)-th Newton sum.
The [driver](sieve.py) computes bounds through \(k=120\), including the reflected part of the search.
For each [v7 weight row](../v7/readme.md#weights) with certified maxima \(u,v\) at radii \(1,R^j\) and \(R^j\ge T^k\), the [convex chord](../v11/readme.md#boxes) gives
\[
    |s_k|\le h u+\min(1,ak/(10000j))\max(0,v-u),
\]
where \(a\) is the smallest nonnegative integer with \(R^a\ge T^{10000}\).
The [power-field norm bound](../../../../../claims/Yin_C_G0345_v438.md#degree) gives degree at least 86 for every power field of a candidate because \(T<1.06\).
An auxiliary of trace degree at most eight cannot vanish on a signed power trace, as that would give the corresponding power degree at most sixteen.
For every \(k\) the driver also uses \(D-2+T^k+T^{-k}\), which follows by concentrating the logarithms of the reciprocal-pair radii at one pair. [Unweighted trace estimate](../../../../../ledger/Yin_L_G0462_v266.md#linear)
It takes the floor of the smallest available bound using rational arithmetic.
The generated degree census records each selected row, with \((0,0)\) denoting the unweighted bound.

<a id="enumeration"></a>
## Enumeration and exact exclusions

The [native recursion](Reciprocal.cs) uses the [Newton congruences](../../readme.md#counts)
\(s_k\equiv s_{k/p}\pmod{p^a}\) for every \(p^a\Vert k\).
These conditions are equivalent to integrality of all prefix coefficients.
The Chinese remainder theorem gives a single class modulo \(k\) from the earlier traces.
For each member in the interval the program forms the next coefficient by Newton's identity, then reflects the full first half to obtain a reciprocal polynomial.
It chooses the sign giving a positive first nonzero odd-indexed sum.
If all such sums vanish, the polynomial is in \(\mathbb Z[X^2]\).
The gcd of \(D\) and the nonzero coefficient indices through \(h\) detects the remaining power substitutions, since reflection preserves divisibility by every factor of \(D\).
Any such substitution would preserve the positive measure in degree at most 55, excluded by the [earlier degree theorem](../../../../../claims/Yin_C_G0345_v438.md#degree).

After nine successful reflected traces the recursion tests \(P(1)P(-1)=0\).
It tests the remaining traces through \(120\) and the exact remainders at \(\Phi_3,\Phi_4,\Phi_6\).
Among the 1,171,107 polynomials passing nine reflected traces, the respective counts excluded by these three stages were 913,231, 248,030 and 9,028.
The [exact division routine](../v12/sieve.py) classified every remaining half-polynomial by an integer cyclotomic divisor.

For each degree the driver computes \(C_0=1,\ C_k=\lfloor\sum_{j=1}^k B_j C_{k-j}/k\rfloor\) for \(k\le h\), where \(B_j\) is the certified bound on \(|s_j|\).
Thus \(N=2\sum_{i=0}^h C_i\) bounds the full coefficient one-norm, and \(N(D+\max_{k\le120}B_k)<2^{63}\) bounds all signed Newton accumulators.
The powers of \(X\) modulo each quadratic have coefficients in \(\{-1,0,1\}\), giving the same coverage for their two remainder coordinates and each addition of two such coordinates.
For the Chinese remainder calculation each of at most \(k\) multipliers is at most \(k\), and \(D^2\max B_k<2^{31}\).
The product \(\prod_{k=1}^h\lceil(2B_k+1)/k\rceil<2^{63}\) bounds every count.
The driver checks these inequalities before starting the search.

<a id="verification"></a>
## Counts, divisors and reproduction

The [verification program](verify.py) compares all 960 disjoint \((s_1,s_2)\)-slice counts against the [separate tensor count](../v10/verify.py), using inclusion and exclusion for the prime divisors of each degree.
It checks the coefficients, sign, substitution condition and slice membership of each final polynomial.
For every reported divisor \(\Phi_m\), it independently evaluates the sum of \(|P(\zeta)|^2\) over primitive \(m\)-th roots by the [integer Ramanujan formula](../v12/verify.py) and obtains zero.
In each degree it also compares a complete eight-trace prefix subtree with an unrestricted-integer Newton recursion that visits all trace values and uses integer remainders.
For a degree with surviving coefficients it selects a subtree containing one of them.
The same verifier checks the seven prime widths, the strict derivative-budget comparisons for every admissible ordered degree triple, and the upper cutoff at prime 499. [Prime consequences](../../../../../claims/Yin_C_G0345_v449.md#primes)

From the repository root, use Python with NumPy and a .NET Framework C# compiler on Windows, or Mono on Unix.
If the v7 output is absent, first regenerate it from the [retained v7 weights](../v7/readme.md#weights).
The last two commands each accept an optional list of selected degrees after `--degree`.

~~~text
python -B mathematics/computations/programs/Yin_J_G0179/versions/v7/larger_boxes.py
python -B mathematics/computations/programs/Yin_J_G0179/versions/v13/sieve.py --workers 5
python -B mathematics/computations/programs/Yin_J_G0179/versions/v13/verify.py
~~~

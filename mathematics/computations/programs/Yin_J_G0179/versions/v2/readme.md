---
author: Yin
---

# Cyclotomic resultant tests on the first fifteen power sums at degrees 56 and 58

<a id="counts"></a>
## Complete candidates removed by the prefix tests

The [certified trace boxes](../../readme.md) contain the reciprocal candidates for the smaller factor in the [prime-223 alternatives](../../../../../ledger/Yin_L_G0462_v264.md#frontier).
Their respective starting counts are 1,356,059,655 at degree 56 and 3,492,875,690 at degree 58, after removal of power substitutions and identification of \(P(X)\) with \(P(-X)\).
The table counts complete representatives removed by some [cyclotomic resultant test](../../../../../ledger/Yin_L_G0462_v266.md#linear) on a prefix of length at most the indicated horizon.
The orders tested are \(m=1,2,3,4,6\).
The geometric tail uses the original bound and the trace-box tail also uses the certified bounds on the remaining sums through the middle coefficient.

| Largest prefix length | Geometric tail, degree 56 | Geometric tail, degree 58 | Trace-box tail, degree 56 | Trace-box tail, degree 58 |
| ---: | ---: | ---: | ---: | ---: |
| 10 | 2,153,472 | 2,097,152 | 346,031,440 | 772,929,232 |
| 12 | 50,678,208 | 85,781,280 | 395,813,030 | 895,541,824 |
| 15 | 218,701,744 | 457,035,920 | 441,549,438 | 1,015,981,224 |

The last pair of tests removes 1,457,530,662 representatives and leaves 914,510,217 at degree 56 and 2,476,894,466 at degree 58.
With the trace-box tail, the two orders \(1,2\) alone remove 431,486,878 and 995,849,960 through length fifteen.
The remaining representatives still require the irreducibility and measure tests.

<a id="sieve"></a>
## Rational prefix inequalities

Write \(D=56\) or \(58\), \(h=D/2\), and take \(B_k\) from the full certified box \(|s_k|\le B_k\).
Use \(r=21/25,\ T=1089/1000\), and the [verified bound](../../../../../ledger/Yin_L_G0462_v266.md#linear) \(\log(1/r)<7/40\).
For each order let \(w_k=r^kc_m(k)/(k\varphi(m))\) for the Ramanujan sum \(c_m(k)\).
If \(g_N\) denotes the three geometric tails on the right of the cited inequality after division by \(\varphi(m)\), excluding its logarithm term, the two tested rational caps on \(\sum_{k\le N}w_ks_k\) are
\[
  7D/80+g_N,\qquad
  7D/80+\min\!\left(g_N,\ \sum_{k=N+1}^h |w_k|B_k+g_h\right).
\]
The second bound follows by applying the length-\(h\) inequality and moving the terms with index greater than \(N\) to its right side.
Any strict violation excludes the complete vector.
The sign change sends \(s_k\) to \((-1)^ks_k\).
Multiplication of the primitive roots by \(-1\) interchanges orders 1 and 2, interchanges orders 3 and 6, and preserves order 4.
The two order sets used in the comparisons are thus stable under the sign change.

All weights and caps are rational.
For speed use \(S=10^{10}\) and initially compare the integer score \(\sum_{k\le N}\lfloor S w_k\rfloor s_k\) with the floor of the scaled cap.
The absolute score error is at most \(\sum_{k\le N} B_k\).
Outside this margin the decision is exact, and any overlapping comparison uses the common integer denominator of the original inequality.
For the stated boxes the scaled scores fit in signed 64-bit integers, since \(S+1\) bounds each absolute scaled coefficient and \(\sum_{k\le15}B_k<200\).

<a id="extensions"></a>
## Counting all extensions of a rejected prefix

By the [Newton and Witt relations](../../readme.md#counts), the vectors in the starting box are exactly the integer assignments satisfying \(s_k\equiv s_{k/q}\pmod{q^{v_q(k)}}\) for each prime \(q\mid k\).
Each edge carrying one of these congruences gives a two-variable indicator.
For indices greater than fifteen, multiply the indicator tables containing one index and sum out that index.
Continue until only tables on prefix coordinates remain.
Their product at a legal prefix counts all its extensions, since this procedure is repeated application of the distributive law for finite sums.
The largest intermediate table in these eliminations has 17,625 entries in either unrestricted box.
Enumeration up through index fifteen, grouped by the first two sums, yields 5,468,051 legal prefixes at degree 56 and 7,523,731 at degree 58.
Weight each rejected prefix by its extension count.
Unsigned 64-bit table operations preserve these counts modulo \(2^{64}\), and each final nonnegative count is at most its original full-box count, below \(2^{64}\).
Summing all weights recovers the two full-box counts in version one.

For power substitutions repeat the count in the intersections defined by \(s_k=0\) for every \(k\) not divisible by a selected prime divisor of \(D\).
Inclusion and exclusion remove all powers before division by two for the sign action, which has no fixed vector once \(P\in\mathbb Z[X^2]\) is removed.
The cap always uses the original certified bounds, including in these intersections, so the same rejection criterion is counted throughout.

There is an independent extension count for the [explicitly excluded prefix](../../../../../ledger/Yin_L_G0462_v266.md#linear) \(s_1=\cdots=s_{10}=6\).
In the integer Euler exponents \(e_j\) with \(s_k=\sum_{j\mid k}j e_j\), the prefix gives \(e_1=6\) and \(e_2=\cdots=e_{10}=0\).
Through index 29 the only dependencies between different unfixed exponents involve the pairs \((j,2j)\) with \(j=11,12,13,14\) when \(2j\le h\).
For each pair count the choices \(s_j\equiv6\pmod j\) and \(s_{2j}\equiv s_j\pmod{2j}\) in their two intervals.
Every remaining index \(k>10\) contributes its independent count of \(s_k\equiv6\pmod k\).
The resulting products give 262,144 and 524,288 representatives, respectively, for the named prefix together with its sign mate.
The nonzero first coefficient excludes a power substitution, and each sign orbit in this pair has exactly one vector with \(s_1=6\).

<a id="reproduction"></a>
## Reproduction

Generate the [version-one inputs](../../readme.md#reproduction), then run the [prefix sieve](cyclotomic_prefixes.py) from the repository root.

~~~text
python mathematics/computations/programs/Yin_J_G0179/versions/v2/cyclotomic_prefixes.py
~~~

The program uses Python and NumPy and reads the [certified full-box bounds and counts](../../inputs/prefixes.json).
The [version-two results](../../inputs/versions/v2/results.json) give the two order sets at each horizon, the counts before and after removal of power substitutions and sign duplicates, and the direct prefix controls.

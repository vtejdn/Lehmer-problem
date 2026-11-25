---
author: Yin
---

# Exact trace exclusions with a common discriminant bound

<a id="census"></a>
## All separating grids at heights forty and one hundred

For \(M=q(q+1)\), the [common Newton sum bound](../../../claims/Yin_C_G0345_v896.md#statement) excludes a monic integral \(H\) with \(M^nH(1/M)=4M+1\), one simple root in \((0,1/M)\) and the other \(n-1\) simple roots in \((-4,0)\), in the following ranges.
No separating nodes are prescribed.

| \(q\) | Trace degrees \(n\) | Degrees excluded | Counts rejected at successive moments starting at one | Degrees reaching the terminal test |
| ---: | --- | ---: | --- | --- |
| 40 | 2 through 100000 | 99999 | 9870, 17608, 20315, 20730, 18076, 7469, 3145, 1805, 977 | 2, 3, 4, 5 |
| 100 | 2 through 200000 | 199999 | 139468, 36344, 2333, 18230, 3620 | 2, 3, 4, 5 |

The [previous all-grid enumeration](free_trace_moments.md#census) reached degree 4500 at height forty.
The integer-only prefix calculation in [reflected_trace_search.py](reflected_trace_search.py) uses the bound on the **sum** of the squared distances through the current depth.
At each height the only terminal candidate in each of the four degrees is \(x^{n-1}(x+4)\), which satisfies the pole equation and has roots at both excluded endpoints.
An unfinished prefix at depth 16 would be reported as open.

~~~
python -B reflected_trace_search.py 40 2 100000 --depth 16
python -B reflected_trace_search.py 100 2 200000 --depth 16
~~~

<a id="integers"></a>
## Rational enlargements and the pole carry

Put \(d=2n,\ k=\min(16,n)\) for these runs, \(e_j=\lfloor E_j\rfloor\) and \(U_j=\max(0,\Theta_j-e_j-1,e_j-3-\Theta_j)\).
Enlarging the interval defining \(a_j\) gives \(U_j\le a_j\).
Using \((1-1/d)^j\ge(d-k)/d\) and \(\log d\le (7/10)\lceil\log_2 d\rceil\), every actual prefix satisfies
\[
 \sum_{j\ {\rm chosen}}\frac{U_j^2}{j}
 \le\frac{d^2}{d-k}\left(\frac7{10}\lceil\log_2 d\rceil+\frac12+\frac2q\right).
\]
Multiplying by the least common multiple of \(1,\ldots,k\) makes each charge integral.
The script keeps the floor of this scaled upper bound and subtracts the individual charges, using an integer square root for the next interval.
These enlargements can retain extra candidates and preserve every solution.

If \(H=\sum_{i=0}^n c_i x^{n-i}\) and a prefix through \(j-1\) has been fixed, the pole gives \(c_j\) congruent modulo \(M\) to the carry \((K-\sum_{i<j}c_i M^i)/M^j\).
From the lower coefficients \(s_j\) of \(z^nH(z+z^{-1}-2)\), the change between \(s_j\) and \(c_j\) is the known shift \(\sum_{i<j}(-1)^{j-i}\binom{2n-2i}{j-i}c_i\).
Newton's identity then gives \(\Theta_j\bmod jM\).
A zero final carry checks the exact pole, after which endpoint tests, squarefreeness and exact real root counts use the [existing routine](free_trace_moments.py).

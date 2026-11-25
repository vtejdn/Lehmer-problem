---
author: Yin
---

# The eight remaining coefficient rows in the test for argument rank three

<a id="exhaustion"></a>
## Scope and first exclusions

Run the separate [rank-three verifier](rank_three.py) from the checkout root with standard Python.

~~~text
python -B mathematics/computations/programs/Yin_J_G0191/rank_three.py
~~~

The [native catalogue](../../../literature/pdf/Mos26/AllSmallMeasures_200.txt) provides coefficients and its [stated completeness](../../../audits/literature/Mos26/readme.md#complete-small-cores) applies through degree 44 below \(13/10\).
The verifier reads all 944 rows of that degree range and ignores the source's measure and exterior-count columns.
It uses the [rational Sturm and finite-field routines](../Yin_J_G0188/readme.md#signatures) on the full reciprocal polynomial \(P=X^nQ(X+1/X)\) and its trace polynomial \(Q\).
For \(u\) roots of \(Q\) in \((-2,2)\), a hypothetical root of argument rank at most three has \(u\le3(n-u)\) and total conjugate class rank \(b\le\lfloor3n/u\rfloor\), by the [signature inequality](../../../claims/Yin_C_G0901_v90.md#dimension).
The first comparison excluded 519 rows.
On all remaining rows the integer bound on \(b\) was at most six.

For each rank bound the verifier forms the possible finite orders of a rational matrix: take least common multiples of indices of distinct cyclotomic factors with sum of their degrees at most the rank bound.
The full lists of indices at degrees \(1,2,4,6\) are respectively \((1,2),(3,4,6),(5,8,10,12),(7,9,14,18)\).
The list follows from Euler's totient product formula: the only possible primes dividing such an index are \(2,3,5,7\), and their powers and products must have totient at most six.
Squarefree reductions of \(P\) give root-cycle orders by the least common multiple of their factor degrees.
The primes \(2,3,5,11,13\) first excluded \(369,40,6,1,1\) rows respectively, under the faithful-class hypothesis for compressed witnesses.
This left exactly the eight source lines \(152,158,159,162,164,165,166,193\).

<a id="flips"></a>
## Simultaneous cycle data on signed roots and inverse pairs

For each of the following seven rows the table gives the number \(n\) of inverse-pair labels.
For \(n=5\) transitivity on a prime number of labels gives primitivity.
In the other rows the indicated cycle prime gives the exact squarefree degrees \((1,n-1)\) for \(Q\), proving double transitivity.
At the flip prime the two polynomials are both squarefree.
If \(e\) is the least common multiple of the degrees for \(Q\), raising a Frobenius element to \(e\) fixes all labels.
The number of labels flipped is half the sum of the full root-cycle lengths which do not divide \(e\).
The last column is the resulting exact argument rank, using the [sign-character proof](../../../claims/Yin_C_G0901_v92.md#signs).

| Source line | \(n\) | Cycle prime | Flip prime | \(Q\) degrees | \(P\) degrees | Labels flipped | Argument rank |
| ---: | ---: | ---: | ---: | --- | --- | ---: | ---: |
| 158 | 5 |  | 5 | 2, 3 | 3, 3, 4 | 2 | 4 |
| 159 | 5 |  | 5 | 2, 3 | 3, 3, 4 | 2 | 4 |
| 162 | 6 | 19 | 2 | 2, 4 | 4, 8 | 4 | 5 |
| 164 | 6 | 3 | 5 | 2, 4 | 4, 8 | 4 | 5 |
| 165 | 6 | 5 | 7 | 1, 5 | 2, 5, 5 | 1 | 5 |
| 166 | 6 | 17 | 37 | 1, 2, 3 | 2, 4, 6 | 2 | 5 |
| 193 | 8 | 29 | 11 | 1, 2, 5 | 2, 4, 5, 5 | 2 | 6 |

The Sturm signature has no real exterior root and one pair of nonreal exterior conjugates in each of the first six rows.
The last row has no real exterior root and two pairs of nonreal exterior conjugates.
The verifier computes these signatures independently of the modular factorizations.

<a id="winner"></a>
## Root isolation for the one remaining row

Source line 152 has \(P=X^8+X^5-X^4+X^3+1\).
The Sturm computation gives one trace below \(-2\), three in \((-2,2)\), no trace above two and no nonreal trace.
There is a single exterior conjugate and it is negative real.
Its absolute value is the unique exterior real root of \(P(-X)\) greater than one.
Exact rational evaluations of \(P(-X)\) at \(12806/10000,12807/10000\) give opposite signs in that order, negative then positive.
The [attainment argument](../../../claims/Yin_C_G0901_v92.md#attainment) computes argument rank three directly from this signature.

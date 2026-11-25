---
author: Yin
---

# Signatures and Frobenius orders in the complete degree-44 small-measure catalogue

<a id="exhaustion"></a>
## Testing all rows for a faithful representation of argument rank at most two

Run the [verifier](argument_cores.py) from the checkout root with standard Python.

~~~text
python -B mathematics/computations/programs/Yin_J_G0191/argument_cores.py
~~~

The input is the [original coefficient table](../../../literature/pdf/Mos26/AllSmallMeasures_200.txt), with its [reported completeness](../../../audits/literature/Mos26/readme.md#complete-small-cores) for primitive irreducible reciprocal cores of multiplicative measure below \(13/10\) through degree 44, up to variable sign.
The verifier uses the [existing parser and rational signature routines](../Yin_J_G0188/readme.md#signatures); it does not use the numerical measure or exterior count in the source rows.
For each degree \(2n\) polynomial, rational Sturm variations at \(-2,2\) give the number \(u\) of interior trace roots, one for each neutral inverse pair, and \(l=n-u\) is the number of individual exterior roots.
There were 944 rows, all with \(0<u<n\).

The [radial dimension inequality](../../../claims/Yin_C_G0901_v64.md#degree) and the complementary argument-rank identity imply \(k\ge\lceil u/l\rceil\), while \(k\le2\) would give total class rank \(b\le\lfloor2n/u\rfloor\).
The strict signature comparison \(u>2l\) excluded 810 rows.
For the other 134 rows the hypothetical rank bound was three in 132 cases and four in two cases.

For each remaining coefficient vector, the verifier uses the [squarefree factor-degree procedure](../Yin_J_G0188/readme.md#frobenius) on the **full reciprocal polynomial** at the primes \(2,3,11\) in that order.
It skips a prime when the polynomial and its derivative have a common factor.
At a squarefree reduction the least common multiple of the finite-field factor degrees is the order of an actual splitting-group element, since the action on all roots is faithful.
The verifier compares that order with the finite orders in the rational matrix group of the indicated rank bound; it is the [torsion-class compression](../../../claims/Yin_C_G0901_v90.md#order) that makes this comparison necessary for a putative small-rank witness.
Every coefficient vector requiring such a test received an excluding order, with 123 first certified at two, ten at three and one at eleven.

| Prime | Source line | Rank bound | Degrees of irreducible factors | Order |
| ---: | ---: | ---: | --- | ---: |
| 3 | 164 | 3 | 2, 10 | 10 |
| 3 | 251 | 3 | 6, 6, 8 | 24 |
| 3 | 286 | 3 | 22 | 22 |
| 3 | 321 | 3 | 3, 3, 9, 9 | 9 |
| 3 | 332 | 3 | 8, 8, 8 | 8 |
| 3 | 535 | 3 | 30 | 30 |
| 3 | 658 | 3 | 8, 13, 13 | 104 |
| 3 | 861 | 3 | 19, 19 | 19 |
| 3 | 1021 | 3 | 5, 5, 6, 6, 20 | 60 |
| 3 | 1082 | 3 | 44 | 44 |
| 11 | 193 | 4 | 2, 4, 5, 5 | 20 |

The other 123 certificates are regenerated from the specified source polynomials at the single prime two.
The calculation establishes the finite tests; the [degree-bounded claim](../../../claims/Yin_C_G0901_v90.md#statement) explains why compression and sign substitution suffice for arbitrary inputs in the stated range.

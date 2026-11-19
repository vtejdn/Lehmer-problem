---
author: Yin
---

# Degrees 60 and 62 in the small-measure search

<a id="boxes"></a>
## Certified first-half Newton sums

For \(T=1089/1000\) the following bounds on \(|s_k|\), in increasing order of \(k\), apply to each monic irreducible noncyclotomic reciprocal integer polynomial of the given degree with \(M(P)\le T\).
They use the [ellipse inequality](../../readme.md#ellipse) with both signs for every \(1\le k\le D/2\).
Even where five divides the input degree, the [relative norm into the power field](../../../../../ledger/Yin_L_G0462_v270.md#descent) excludes zeros at all eleven auxiliary polynomials.
Their degrees are at most five, while the published degree threshold alone assures \([\mathbb Q(\alpha^k):\mathbb Q]\ge56\).
The root of unity case is already excluded by the positive measure.

| Degree | Bounds through the central coefficient | Complete representatives |
| ---: | --- | ---: |
| 60 | 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 14, 14, 15, 15, 16, 17, 18, 19, 19, 20, 21, 22, 23, 25, 26 | 10,746,811,495 |
| 62 | 6, 7, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 13, 13, 14, 14, 15, 16, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28 | 37,483,781,331 |

The [program](next_degrees.py) reuses the degree-58 rational weights at each index through 29 and the last vector for indices 30 and 31.
At radius one and at \(T^k\) it certifies the maximum on the whole ellipse before taking the integer part of \((D/2-1)U(0)+U(k\log T)\).
The [certificate output](../../../../outputs/Yin_J_G0179/versions/v6/boxes.json) records each rational witness, upper bound, subdivision size and depth.
The [integer congruence count](../../readme.md#counts) includes all complete vectors in the symmetric boxes and then removes power substitutions and identifies \(P(X)\) with \(P(-X)\).
Any nontrivial substitution would lower the degree to at most 31 at the same positive measure, contrary to the published degree theorem.
These are the two smallest degrees needed for the [prime tests beyond 223](../../../../../ledger/Yin_L_G0462_v270.md#primes).

From the repository root run the following with Python and NumPy.

~~~text
python -B mathematics/computations/programs/Yin_J_G0179/versions/v6/next_degrees.py
~~~

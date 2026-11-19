---
author: Yin
---

# Degree-64 and degree-66 Newton boxes at measure 1.091

<a id="bounds"></a>
## A cutoff covering every prime in the fixed-budget count

Let \(P\) be a monic irreducible reciprocal noncyclotomic integer polynomial of degree \(D=64\) or 66 with \(M(P)\le1091/1000\).
With a companion of degree at least 56 in the [signed-row test](../../../../../ledger/Yin_L_G0462_v270.md#primes), the total-degree bound must reach 120 for degree 64 and 122 for degree 66.
At every prime of the [original count](../../../../../claims/Yin_C_G0345_v420.md#upper), two different qualifying measures have sum strictly below \((\log2)/4\).
The smaller multiplicative measure is therefore less than \(2^{1/8}<1091/1000\), by \(1091^8>2\cdot1000^8\).
This cutoff also applies at unbounded primes whenever the degree under consideration occurs.

| Degree | Upper bounds for the absolute first-half Newton sums | Complete representatives |
| ---: | --- | ---: |
| 64 | 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 13, 13, 14, 15, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 30 | 20,557,031,095 |
| 66 | 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 11, 11, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 29, 30, 32 | 51,979,784,484 |

The counts use [Newton integrality, power-substitution exclusion and sign symmetry](../../readme.md#counts) through the central coefficient.
Each representative is a complete reciprocal integer polynomial, whose actual measure and irreducibility still need to be tested.
A nontrivial power substitution would give a polynomial of degree at most 33 with the same positive measure, below Lehmer's number, contrary to the published Mossinghoff–Rhin–Wu theorem.

<a id="weights"></a>
## Enlarging the auxiliary family

The [34 monic auxiliary polynomials and 65 integer weight rows](weights.json) are given explicitly, with coefficients in descending order and weights measured in units of \(10^{-8}\).
The choices start with the eleven [earlier auxiliaries](../../readme.md#ellipse) and add the trace polynomials of the cyclotomic polynomials with order at least three and degree at most sixteen.
The relation \(\varphi(n)^2\ge n/2\) bounds these orders by 512.
Also include the monic sign transform of each polynomial, removing duplicates.
Every auxiliary has degree at most eight.
If it vanished at a signed power trace, the corresponding power field would have degree at most sixteen.
The [power-field descent](../../../../../ledger/Yin_L_G0462_v270.md#descent) with the published threshold 56 excludes this throughout the stated measure range, since \(1.091<\rho\).
Both signed resultants needed by the ellipse method are therefore nonzero.

For the optional weight search use 1,100 midpoints in the upper semicircle at radii one and \((1091/1000)^k\).
The linear program minimizes \((D/2-1)u_0+u_k\) over bounds on the sampled maxima, with each auxiliary weight in \([0,3]\).
The [verification program](larger_boxes.py) uses the rounded weights as rational inputs and certifies the full maxima with the [rational Bernstein and logarithm bounds](../../readme.md#certificate).
The squared moduli now have degree at most sixteen, so the Bernstein polynomials use degree sixteen and its exact binomial coefficients throughout.
At each of the 65 layers the program separately certifies the full interval at the two radii before taking the integer part.
The [output](../../../../outputs/Yin_J_G0179/versions/v7/boxes.json) gives all 130 certificates and the two congruence counts.

On a fixed twenty-sum prefix the [affine suffix formula](../../../../../ledger/Yin_L_G0462_v271.md#affine) supplies the first reflected tests simultaneously.
The [comparison program](affine_tail.py) checks its exact results against direct Newton recursions for all 256 and 512 completions in that example. [Comparison output](../../../../outputs/Yin_J_G0179/versions/v7/affine.json)

From the repository root, the following command uses the stored weights and requires Python and NumPy.
The optional flag \(\texttt{--choose-weights}\) on the first command regenerates the weights using SymPy and SciPy before certifying them.

~~~text
python -B mathematics/computations/programs/Yin_J_G0179/versions/v7/larger_boxes.py
python -B mathematics/computations/programs/Yin_J_G0179/versions/v7/affine_tail.py
~~~

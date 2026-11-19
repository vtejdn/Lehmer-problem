---
author: Yin
---

# Modular approximation for a quartic Salem unit at the first extra width

<a id="approximation"></a>
## Exact minima and quotient orders

For the two quartics \(P=X^4-X^3-X^2-X+1\) and \(P_2=X^4-3X^3+X^2-3X+1\), the [first-extra-width formula](../../../../../claims/Yin_C_G0345_v464.md#plane) reduces the short-row problem at width nine to a congruence \(s+vt=0\bmod J\) for each sign.
We computed its modulus \(J\) and its least nonzero \(\mu=\max(|s|,|t|)\) at all 50 primes between 13 and 257 inclusive and at the five additional exponents \(16,32,64,128,256\).
In every one of the 110 congruences, \(1\le J/\mu^2<212\).
At each exponent at least one of the signs has \(J/\mu^2<26\).
The greatest ratio for the positive sign lies strictly between 211 and 212 at \(n=193\), and the greatest for the negative sign lies strictly between 83 and 84 at \(n=167\).
The largest of the two-sign minima of the ratio lies strictly between 25 and 26 at \(n=173\).
These are finite checks of how closely \(\mu\) approaches the square-root scale, with no asserted asymptotic lower bound for \(\mu\).

In the following table \(L(z)=1+\lfloor\log_2 z\rfloor\) and each pair lists the positive sign first.
The last column divides the absolute scalar determinant \(|a_n|\) by \(\operatorname{lcm}(J_+,J_-)\).

| \(n\) | \(L(J_+),L(J_-)\) | \(L(\mu_+),L(\mu_-)\) | Remaining factor |
| ---: | ---: | ---: | ---: |
| 13 | 104, 112 | 52, 54 | 4 |
| 17 | 193, 200 | 96, 98 | 1410 |
| 61 | 725, 735 | 363, 367 | 26 |
| 127 | 1672, 1680 | 836, 840 | 6 |
| 251 | 3322, 3330 | 1661, 1664 | 39 |
| 256 | 3235, 3235 | 1617, 1617 | 5 |
| 257 | 3399, 3408 | 1699, 1703 | 34 |

Across all 55 exponents the remaining factor is at most 1410, attained at \(n=17\).
The two quotient orders have gcd four at 38 exponents and gcd two at the other 17.

<a id="method"></a>
## Recovering and checking the modular witnesses

The program recomputes both [primitive width-eight generators](../v5/readme.md#sample) and multiplies them by \(1+\sigma Y\) and \(1-\sigma Y\), respectively.
Their order \(J\) is the gcd of the two-column minors.
A Bézout identity for the first column gives \(v\), and direct reduction checks the proportionality in every coefficient.
The lattice of the scalar congruence has basis \((J,0),(-v,1)\).
Gauss reduction preserves the determinant \(J\) and supplies a nonzero vector of sup norm \(R\).
The [plane enumerator](../../readme.md#method) exhausts the one-norm ball of radius \(2R\), which contains the entire sup-norm square of radius \(R\).
Minimizing the sup norm of those candidates gives the reported \(\mu\).

An independent integer count checks that the square of radius \(\mu-1\) contains no nonzero solution and that the square of radius \(\mu\) does.
For \(0\le2R<J\), count \(1\le t\le R\) with \(vt\bmod J\) at distance at most \(R\) from zero.
At each of the two slopes \(a=v,-v\), the difference \(\lfloor(at+R)/J\rfloor-\lfloor at/J\rfloor\) detects crossing a multiple of \(J\).
The two events are disjoint, and the residue is nonzero since \(v\) is a unit and \(0<t<J\).
Division with remainder and exchange of the axes in the resulting lattice triangle evaluate the two floor sums exactly.
A nonzero solution with second coordinate zero would require \(R\ge J\).

Run the [Python program](cyclic_quotients.py) from the repository root with Python 3.10 or later.

~~~text
python -B mathematics/computations/programs/Yin_J_G0177/versions/v7/cyclic_quotients.py
~~~

The [generated data](../../../../outputs/Yin_J_G0177/versions/v7/results.json) contain both moduli, residues, minima, witness coordinates, the determinant scalar and its unaccounted factor at every exponent.

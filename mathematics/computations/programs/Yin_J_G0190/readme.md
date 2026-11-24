---
author: Yin
---

# Small reciprocal polynomials through degree twelve with at most one neutral inverse pair

<a id="exhaustion"></a>
## The rational cutoff and complete coefficient enumeration

Run the [integer verifier](small_reciprocal.py) from the checkout root with standard Python.

~~~text
python -B mathematics/computations/programs/Yin_J_G0190/small_reciprocal.py
~~~

Let \(C=53/40\).
Among monic reciprocal integer polynomials of positive even degree at most twelve and multiplicative Mahler measure at most \(C\), every polynomial without a cyclotomic factor has at least three inverse pairs on the unit circle.
The claim applies in particular to nontorsion irreducible inputs; the enumeration includes both choices of variable sign.
The cutoff exceeds the plastic number because \(C^3-C-1>0\) and \(X^3-X-1\) is strictly increasing for \(X\ge1\).

Write \(P=X^d+a_1X^{d-1}+\cdots+a_d\), \(d=2n\), with \(a_0=a_d=1\), \(a_j=a_{d-j}\), and put \(s_j=\sum_{P(\alpha)=0}\alpha^j\), with multiplicities.
Real endpoints of a reciprocal input with a cyclotomic factor need not be retained.
For any input of interest the roots come in \(n\) inverse pairs, whose nonnegative exterior log moduli \(u_i\) sum to \(\log M(P)\le\log C\).
Thus
\[
       |s_j|\le \sum_i 2\cosh(ju_i)\le d-2+C^j+C^{-j}.
\]
For nonnegative \(x,y\), \(\cosh(x+y)-1\ge(\cosh x-1)+(\cosh y-1)\), which proves the second inequality by induction, including neutral pairs.
The script computes the integer floors of these rational bounds for \(1\le j\le32\).

For each \(1\le j\le n\), Newton's identities make \(s_j=-j a_j-\sum_{i=1}^{j-1}a_i s_{j-i}\).
With the earlier coefficients fixed, the integer interval for \(a_j\) is therefore exact for this test.
Each leading half surviving the first \(n\) tests occurs once; reflection supplies its remaining coefficients.
Newton's identities and then the linear recurrence for the full polynomial compute all later \(s_j\) exactly up to \(j=32\).
Passing these necessary conditions does not determine the Mahler measure.

The program discards any multiple of a cyclotomic polynomial of degree at most \(d\) by monic division over the integers.
It enumerates all orders \(q\le2d^2\), since \(\varphi(q)^2/q\ge1/2\) by prime powers, with only the local factor for \(2^1\) smaller than one.
In the division of \(X^q-1\) only divisors \(j\mid q\) are needed, and \(\varphi(j)\le\varphi(q)\), so the retained degree range includes them when constructing \(\Phi_q\).
The remaining candidates are compared to \(C\) by the [exact Graeffe coefficient tests](../Yin_J_G0188/readme.md#cut).
These use upper and lower integer coefficient bounds after root squaring; no rounded measure decides a case.
For each candidate below \(C\), the [trace recurrence and rational Sturm tests](../Yin_J_G0188/readme.md#signatures) certify simplicity of its trace polynomial and count its roots in \((-2,2)\).
These are exactly the distinct unit-circle inverse pairs.

| Degree | Leading halves | Through power 32 | Without cyclotomic factors | Below \(53/40\) | Neutral pairs at the last step |
| ---: | ---: | ---: | ---: | ---: | --- |
| 2 | 5 | 5 | 0 | 0 | none |
| 4 | 41 | 19 | 0 | 0 | none |
| 6 | 373 | 59 | 0 | 0 | none |
| 8 | 3,931 | 185 | 20 | 2 | 2 with three |
| 10 | 44,485 | 621 | 102 | 16 | 6 with three, 10 with four |
| 12 | 530,345 | 2,383 | 450 | 22 | 16 with four, 6 with five |

Every strict comparison terminated, and no candidate at or below the cutoff has at most one neutral pair after the cyclotomic exclusion.
This finite search starts from Newton intervals and requires no precomputed polynomial catalogue.

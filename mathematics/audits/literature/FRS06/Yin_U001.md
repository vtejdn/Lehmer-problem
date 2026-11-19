---
author: Yin
---

<a id="frs06-u001"></a>
<a id="auxiliary"></a>
# Trace bounds from weighted integer polynomials

In the [inspected journal edition](readme.md#edition), put \(P(X)=X^dQ(X+1/X)\) for a monic reciprocal integer polynomial of degree \(2d\) with \(M(P)<M\).
Choose one root \(\alpha_i\) of modulus at least one from each reciprocal pair, and put \(\gamma_i=\alpha_i+\alpha_i^{-1}\) and \(a_i=\log|\alpha_i|/\log M\).
Then \(\sum a_i\le1\), and \(\gamma_i\) lies in the closed ellipse \(E_{a_i}\) with semiaxes \(M^{a_i}\pm M^{-a_i}\), using \(E_0=[-2,2]\).
For the positive real weights \(e_j\) and integer polynomials \(Q_j\), equations (5.1)–(5.2) define \(f(z)=\operatorname{Re}z-\sum_j e_j\log|Q_j(z)|\) and \(g(a)=\min_{E_a}f\), with value \(+\infty\) for \(f\) at an active zero.
If \(Q\) is coprime to each active \(Q_j\), their integer resultants have absolute value at least one, giving \(s_1=\sum\gamma_i\ge\sum f(\gamma_i)\ge\sum g(a_i)\).
When all \(a_i\le1/2\), every decreasing affine minorant \(h\le g\) on \([0,1/2]\) therefore gives \(s_1\ge(d-2)h(0)+2h(1/2)\) by summing \(h(0)+a_i h'\).
A larger exterior root is real and unique, and its sign can be normalized by replacing \(P(X)\) with \(P(-X)\).
Sections 2d and 5e split its logarithmic modulus into six ranges and bound its trace contribution separately.
For higher traces §2b requires coprimality with the trace polynomial of each signed power used, and §§5c and 5e replace \(M\) by \(M^k\). [Ellipses and coprimality](../../../literature/pdf/FRS06.pdf#page=3) · [Definitions and Lemma 1](../../../literature/pdf/FRS06.pdf#page=7) · [Equation (5.6)](../../../literature/pdf/FRS06.pdf#page=8) · [First case and powers](../../../literature/pdf/FRS06.pdf#page=9)

<a id="printed-example"></a>
## The degree-34 example on the real interval

For \(2d=34\), §5a, p. 1534, specifies these eleven active terms for the lower bound on \(s_1\) in the case \(a_i\le1/2\).
The integer weights below are \(10^8 e_j\) from that passage, and the coefficients are in descending degree order from Table 3, p. 1536. [Weights and stated minima](../../../literature/pdf/FRS06.pdf#page=8) · [Polynomial rows](../../../literature/pdf/FRS06.pdf#page=10)

| \(j\) | Coefficients of \(Q_j\) | \(10^8 e_j\) |
| --- | --- | ---: |
| 1 | 1, 0 | 14768307 |
| 2 | 1, 1 | 49117397 |
| 4 | 1, 2 | 56247516 |
| 8 | 1, 0, −2 | 3015563 |
| 9 | 1, 1, −1 | 22586214 |
| 11 | 1, 0, −3 | 5159352 |
| 13 | 1, 1, −2, −1 | 15415127 |
| 14 | 1, 0, −3, 1 | 2119227 |
| 17 | 1, 1, −4, −4, 1 | 5373559 |
| 20 | 1, 1, −4, −3, 3, 1 | 4126272 |
| 21 | 1, 1, −5, −5, 4, 3 | 4828564 |

Immediately after these weights the paper gives \(g(0)=-0.20529481\ldots\), \(g(1/2)=-0.67503341\ldots\) and \((d-2)g(0)+2g(1/2)=-4.42948908\ldots\).
It reports thirteen steps for an affine lower bound with loss \(1/10\) and concludes \(s_1\ge-4\).
Yet at \(x=-30253/20000\in[-2,2]\) the tabulated terms give
\[
 -0.2700<f(x)<-0.2699.
\]
Thus the actual minimum for these printed data is at most \(f(x)\), strictly below the quoted \(g(0)\). [The example in §5a](../../../literature/pdf/FRS06.pdf#page=8)

I checked this enclosure by Horner evaluation over the rationals and interval addition.
For each nonzero \(y=|Q_j(x)|\), write \(y=2^k u\) with \(1\le u<2\).
For \(1\le v\le2\) put \(t=(v-1)/(v+1)\) and \(S=2\sum_{j=0}^{14}t^{2j+1}/(2j+1)\).
The power series gives \(S\le\log v\le S+2t^{31}/(31(1-t^2))\).
Using this interval at \(v=u,2\) in \(\log y=\log u+k\log2\), reversing endpoints for negative multipliers, encloses the weighted sum for \(f(x)\) between the two displayed rational bounds.
This tests the printed data at one point and supplies no revised value for either minimum or for the optimal trace bound.

<a id="scope"></a>
## Exhaustive degrees and the degree-56 and degree-58 searches

The authors report a complete list of monic irreducible primitive polynomials with \(1<M(P)<\theta_0\) through degree 36 and \(1<M(P)<1.31\) at degrees 38 and 40, with \(\theta_0\) the positive root of \(X^3-X-1\).
Their introduction separately credits earlier heuristic searches through degree 180.
Sections 2 and 5–8 describe choosing power-sum bounds, converting them to coefficient ranges with Newton's identities, sieving candidates and using Schur–Cohn and modified Graeffe tests.
I checked the scope in the abstract and §1 and inspected the method through §8.
The historical enumeration itself was outside this source check. [Reported ranges](../../../literature/pdf/FRS06.pdf#page=1) · [Historical searches and method](../../../literature/pdf/FRS06.pdf#page=2) · [Final tests](../../../literature/pdf/FRS06.pdf#page=11)

For degree 56 or 58 the affine-minorant argument above applies with \(d=28\) or \(29\), after checking its hypotheses at the chosen \(M\), powers and signs.
A bound for a new search requires certified lower bounds throughout the relevant ellipses and real intervals, including the distinct large-real-root case when present.
The published degree-34 example supplies neither its quoted real minimum for the displayed weights nor bounds for all those new cases.
The reported exhaustive degree range ends at 40.
[The later MRW08 theorem](../MRW08/Yin_U001.md#degree) independently gives a lower degree bound of 56 for a polynomial whose measure is strictly between one and Lehmer's.

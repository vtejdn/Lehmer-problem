---
author: Yin
---

# The Mahler measure of low-degree trace factors on the odd grid

<a id="statement"></a>
## Factor measures and the degree at the sign change

Use the [full odd-grid chamber](Yin_C_G0893_v1.md#statement) with \(p=2n+1\), traces \(b_j=2\cos(2\pi j/p)\), residues \(\rho_j\) positive through \(c\) and negative thereafter, and strict endpoint \(Q(-2)/B_n(-2)<0\).
Write \(\kappa=n-c\) and use the [integral representative](Yin_C_G0881_v3.md#prefix-coordinates) \(h\in\mathbb Z[t]\), \(\deg h<n\), with \(p\rho_j=(4-b_j^2)h(b_j)\).
For a nonzero trace polynomial \(F\), put \(F^*(z)=z^{\deg F}F(z+z^{-1})\).
Consider any sequence \(p\to\infty\) with \(1<M(P)\to1\) for the original whole lifts.
For every choice of nonzero integral divisors \(F\mid h\) with \(d=\deg F=o(\sqrt{p/\log p})\),
\[
                           \limsup M(F^*)\le149/100.                    \tag{1}
\]
In particular these factors have leading coefficient of absolute value one eventually, including constant divisors.
This conclusion uses ordinary polynomial divisibility of the canonical \(h\).

For any fixed \(0<\epsilon<1/2\), take the product of **all** primitive irreducible factors of \(h\) of degree at most \(p^{1/2-\epsilon}\), with their multiplicities.
The upper limit of the Mahler measure of its lift is also at most \(149/100\), even when this product has large total degree.
The content of \(h\) is one eventually.

There is at least one real zero \(y\) of \(h\) strictly between \(b_{c+1}\) and \(b_c\).
For every such zero, the degree \(d_y=[\mathbb Q(y):\mathbb Q]\) satisfies, with an absolute positive implied constant,
\[
     d_y\ \gg\ \left(\frac{\log(p/\kappa)}
                            {\log(2+\log(p/\kappa))}\right)^2            \tag{2}
\]
along the sequence.
In particular the degrees tend to infinity.
For a bounded-degree factor, (1) leaves only finitely many possibilities up to sign, by the elementary coefficient bounds for its lifted polynomial.
As a special case every rational root of \(h\) eventually belongs to \(\{-2,-1,0,1,2\}\), since an integer root outside that set has a quadratic lift of measure at least \((3+\sqrt5)/2\).

<a id="cofactor"></a>
## Polynomial sizes on the circle

Put \(a=2\cos((2c+1)\pi/p)\) and \(X_j=(b_j-a)(4-b_j^2)h(b_j)>0\).
The [first moments and grid variation estimate](../ledger/Yin_L_G0464_v5.md#endpoint-index-exponent) give \(\sum|\rho_j|=O(p)\) on this sequence.
In the expression \(h=\sum_{i<n}a_iE_i\), the degree-\((p-3)\) [semicircle quadrature](../ledger/Yin_L_G0464_v5.md#odd-grid-product) gives \(a_i=\sum_j E_i(b_j)\rho_j\), by orthogonality.
Indeed \(\deg(E_i h)\le2n-2=p-3\), and the ordinary semicircle orthogonality follows from the sine representation of \(E_i\).
Consequently \(|a_i|=O(p(i+1))\), since \(|E_i|\le i+1\) on \([-2,2]\).
On the unit circle \(h^*\) has supremum norm \(O(p^4)\).
In particular \(\log M(F^*)=O(\log p)\), by multiplicativity and \(M((h/F)^*)\ge1\) for a nonzero integer polynomial.

Put \(G=h/F\).
Uniformly over such divisors one has
\[
                  \log^+\|G^*\|_{\infty,\mathbb T}=O((d+1)\log p).     \tag{3}
\]
To see this, the coefficients of \(h^*\) are bounded by its circle norm by Fourier inversion.
For a polynomial of degree at most \(p\) divisible by \(z-\xi\), synthetic division increases its coefficient maximum by at most a factor \(p+1\).
For \(|\xi|\le1\) use the recursion starting at the highest coefficient; for \(|\xi|>1\) start at the constant coefficient, dividing by \(\xi\) at each step.
Divide out all \(2d\) linear factors of \(F^*\) this way and then divide by its nonzero integer leading coefficient.
The supremum norm of the resulting \(G^*\) is at most \(p+1\) times its coefficient maximum, proving (3).

<a id="partial-product"></a>
## A lower bound on a product with the nearest nodes removed

For each of the \(2d\) roots \(\xi\) of \(F^*\) counted with multiplicity, choose a nearest \(p\)-th root of unity in argument.
There are no zero roots since \(F^*(0)\) is the leading coefficient of \(F\).
Delete the chosen nodes, their conjugates and the node 1 from the full circle grid.
Denote the deleted set by \(S\), with \(s=|S|\le4d+1\), and write \(J\) for the surviving indices on the original half grid.
No nontrivial grid node is a root of \(F^*\) or \(G^*\), by strictness.

For one root \(\xi\), normalize the modulus of its linear factor by \(\max(1,|\xi|)\).
After rotation about its nearest node the product of those normalized moduli over the remaining \(p-1\) nodes is
\[
   |1+w+\cdots+w^{p-1}|,\qquad |w|=\min(|\xi|,|\xi|^{-1}),\quad
                                |\arg w|\le\pi/p .
\]
For \(|\xi|>1\) this uses reciprocal conjugation, which preserves the angular position and the normalized distances to every unit node.
The identity follows from \(z^p-1\), with the value \(p\) at \(w=1\).
Projecting the terms on the ray of angle \((p-1)\arg(w)/2\) gives a lower bound \(\sin(\pi/(2p))\sum_{\ell=0}^{p-1}|w|^\ell\ge1/p\).
Deleting further nodes costs at most a factor two per node for this normalized linear factor.
Factoring \(F^*\) and pairing conjugate nodes therefore gives
\[
 \frac1n\sum_{j\in J}\log |F(b_j)|
 \ \ge\ \frac{p-s}{2n}\log M(F^*)
           -\frac{2d}{2n}\bigl(\log p+s\log2\bigr).                   \tag{4}
\]
The product of \(|G(b_j)|\) over **all** half-grid nodes is the absolute nonzero integer resultant of \(G\) and the monic integral \(B_n\).
By (3) the deleted terms can lower the surviving sum of logs by at most \(O((d+1)^2\log p)\).
The product over the full half grid of \(|(b_j-a)(4-b_j^2)|\) is \(p|B_n(a)|\ge1\) by the [midpoint and sine products](../ledger/Yin_L_G0464_v5.md#odd-grid-product).
Every such factor is at most 16 in absolute value, so deleting the same nodes decreases its log product by at most \(s\log16\).
Combining these estimates with (4), \(2n=p-1\) and \(\log M(F^*)=O(\log p)\) proves
\[
           \frac1n\sum_{j\in J}\log X_j
                  \ \ge\ \log M(F^*)-O((d+1)^2\log(p)/p).             \tag{5}
\]
The constants in these estimates are independent of the chosen divisors.

<a id="transfer"></a>
## Applying the arithmetic limit law after deletion

If \(d=o(\sqrt{p/\log p})\), the error in (5) tends to zero.
Choose a subsequence approaching the upper limit of the divisor measures, extracting one of the five coefficient profiles and a joint weak limit \(\lambda\) of \((b_j,X_j)\) as in the [normalized residue law](Yin_C_G0893_v1.md#normalization).
The deleted part of the empirical probability has mass \(O((d+1)/n)\to0\).
The positive logarithms of \(X_j\) are uniformly integrable by their bounded mean and \(\log y=o(y)\).
The surviving subprobabilities therefore have the same weak limit, and lower truncation of the logarithm gives
\[
        \limsup\frac1n\sum_{j\in J}\log X_j\ \le\ \int\log X\,d\lambda
                          =\int\log u\,d\eta\ \le\log(149/100).
\]
Here \(\eta\) is the normalized residue law of that subsequence; the final inequality is the [six-polynomial scalar bound](Yin_C_G0893_v1.md#scalar) on the **limit law**.
The limsup estimate for the full resultant alone would not justify deleting potentially tiny sampled values.
Equation (5) now proves (1).

For the assertion about all factors up to \(p^{1/2-\epsilon}\), discard factors whose lifts have measure one, which do not change the product measure.
Every remaining primitive irreducible trace factor of degree at most \(p\) has a lift with logarithmic measure at least \(c_0/(\log p)^3\) for some fixed \(c_0>0\) and all large \(p\).
A nonmonic lift costs at least \(\log 2\); a monic lift of positive measure has a noncyclotomic monic irreducible factor of degree at most \(2p\).
Apply the [adopted numerical Dobrowolski bound](Yin_C_G0147_v5.md#argument) to such a root at large degree.
For bounded degree the same weaker bound follows from finiteness of monic integral polynomials with bounded Mahler measure and the [measure-one characterization](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization).
If the whole product exceeded \(149/100+\delta\) infinitely often for any \(\delta>0\), multiply factors with repetitions until first exceeding \(149/100+\delta/2\).
This uses \(O_\delta((\log p)^3)\) factors.
The resulting divisor has degree \(O_\delta(p^{1/2-\epsilon}(\log p)^3)=o(\sqrt{p/\log p})\), contradicting (1).
Taking \(F\) to be the content in (1) proves the content assertion.

<a id="endpoint-degree"></a>
## An algebraic zero close to the endpoint

A real zero \(y\) in the indicated gap exists by continuity and strict opposite signs.
Its primitive irreducible polynomial \(F\) divides \(h\) by Gauss's lemma.
Write \(D=2d_y\), \(S=F^*\) up to sign, and take the root \(\xi\) of \(z^2-yz+1\) with positive imaginary part.
The field \(\mathbb Q(y)\) in this embedding is real, and \(y^2-4<0\).
Thus \([\mathbb Q(\xi):\mathbb Q(y)]=2\) and \(S\) is irreducible of degree \(D\).
Since \(y\) lies in the transition gap, the angle of \(\xi\) differs from \(\pi\) by at most \((2\kappa+1)\pi/p\), so \(|1+\xi|\le(2\kappa+1)\pi/p\).

If \(d_y>p^{1/3}\), (2) already follows since \(\log(p/\kappa)\le\log p\).
On the remaining indices (1) gives a monic \(S\) with \(M(S)\le2\) eventually.
Here the leading coefficient is eventually one in absolute value since the upper limit in (1) is strictly below two.
Write the distinct roots as \(\xi_1=\xi,\xi_2,\ldots,\xi_D\).
Since the discriminant of \(S\) is a nonzero integer and \(|\xi|=1\),
\[
 \prod_{2\le i<j\le D}|\xi_j-\xi_i|
    \ge \left(\prod_{i=2}^D|\xi_i-\xi|\right)^{-1}
    \ge 2^{-(D-1)}M(S)^{-1}.                                         \tag{6}
\]
Let \(k=\lceil\sqrt D\rceil\), \(N=D-1+k\).
Form a confluent Vandermonde matrix with evaluation rows at \(\xi_2,\ldots,\xi_D\) and evaluation of derivatives of orders \(0,\ldots,k-1\) divided by their factorials at \(-1\), using the monomials through degree \(N-1\).
The absolute determinant is the left side of (6) times \(\prod_{i=2}^D|1+\xi_i|^k\).
Indeed in the ordinary Vandermonde determinant, let the last \(k\) distinct nodes tend to \(-1\), dividing by their mutual Vandermonde product first; successive divided differences tend to the indicated normalized derivatives.
Each ordinary row has Euclidean norm at most \(\sqrt N\max(1,|\xi_i|)^{N-1}\).
The normalized derivative row of order \(r\) has norm at most \(\sqrt N N^r\) by the binomial formula.
Hadamard's inequality, (6) and \(M(S)\le2\) give
\[
 k\sum_{i=2}^D\log |1+\xi_i|
 \ \le\ \frac{N+k(k-1)}2\log N + N\log 2 +(D-1)\log2 .
\]
As \(S(-1)\) is a nonzero integer, \(-\log|1+\xi|\) is at most the sum on the left divided by \(k\).
Consequently \(\log(p/\kappa)\le C\sqrt D\log(2D)\) with an absolute constant, using \(\kappa\ge1\).
Writing \(L=\log(p/\kappa)\), which tends to infinity by [endpoint localization](../ledger/Yin_L_G0464_v5.md#endpoint-index-exponent), consider \(D\ge L^2\) and \(D<L^2\) separately to obtain (2).

## Assessment history

### Decision trace-factor-transfer

| Field | Value |
| --- | --- |
| date | 2026-11-16T09:50 |
| status | open |
| reason | Retain the partial grid product and endpoint separation bounds for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Factor and separating-degree bounds](#statement) | Small divisors, the combined measure of the lower-degree factors and every real zero in the transition gap. |
| argument | [Cofactor size](#cofactor) | Integral coefficient chart, polynomial size and uniform division bound. |
| argument | [Partial products](#partial-product) | Angular deletion, binomial products, cofactor resultant and finite lower bound. |
| argument | [Measure transfer](#transfer) | Deleting negligible mass, the scalar limit law, content and accumulated lower-degree factors. |
| argument | [Endpoint separation](#endpoint-degree) | Monic irreducible unit-circle factor, confluent determinant and degree inversion. |
| dependency | [Arithmetic law](Yin_C_G0893_v1.md#decision-normalized-residue-tests-reviewed) | Bounded positive grid mass, normalized law and its integral logarithmic ceiling. |
| dependency | [Numerical Dobrowolski input](Yin_C_G0147_v5.md#argument) | Weak polylogarithmic bound for each noncyclotomic monic factor with its recorded external scope. |


### Decision trace-factor-transfer-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T09:57 |
| status | proved |
| reason | Adopt the trace factor measure transfer and the quantitative degree obstruction at the sign change. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Factor and separating-degree bounds](#statement) | Small divisors, the combined measure of the lower-degree factors and every real zero in the transition gap. |
| argument | [Cofactor size](#cofactor) | Integral coefficient chart, polynomial size and uniform division bound. |
| argument | [Partial products](#partial-product) | Angular deletion, binomial products, cofactor resultant and finite lower bound. |
| argument | [Measure transfer](#transfer) | Deleting negligible mass, the scalar limit law, content and accumulated lower-degree factors. |
| argument | [Endpoint separation](#endpoint-degree) | Monic irreducible unit-circle factor, confluent determinant and degree inversion. |
| dependency | [Arithmetic law](Yin_C_G0893_v1.md#decision-normalized-residue-tests-reviewed) | Bounded positive grid mass, normalized law and its integral logarithmic ceiling. |
| dependency | [Numerical Dobrowolski input](Yin_C_G0147_v5.md#argument) | Weak polylogarithmic bound for each noncyclotomic monic factor with its recorded external scope. |
| review | [Independent proof finding](../audits/reviews/Yin_R_G1107_v64.md#trace-factor-review) | Independent assessment of the deleted product, joint law, all low-degree factors with multiplicities, and confluent determinant degree bound. |

## Current assessment
[Selected decision](#decision-trace-factor-transfer-reviewed)

---
author: Yin
---

# Exact prime-index factorization of a reciprocal template with cyclotomic leading coefficient

This project deduction arose from the search for positive irreducible factors of degree \(o(p)\) after the [odd-prime square-family obstruction](Yin_C_G0877_v1.md#statement).
Here \(m=\log M\) denotes total logarithmic Mahler measure.

<a id="statement"></a>
## The unique positive factor

Set \(a(z)=z^4+z^2+1=\Phi_3(z)\Phi_6(z)\), \(b(z)=z^4+1\), and \(q(z,t)=a(z)(t^2+1)-b(z)t\).
The polynomials \(a,b\) are coprime because \(a-b=z^2\) and both have constant term one.
In particular \(M(a)=1\).
Let \(D_0=2\), \(D_1=Y\), \(D_{n+1}=YD_n-D_{n-1}\).
For every odd prime \(p\) the complete monic irreducible factorization over the rationals is
\[
 q(z,z^{2p})=(z^4+1)L_p(z),\qquad
 L_p(z)=z^{2p}G_p(z^2+z^{-2}),\qquad
 G_p(Y)=(Y+1)D_p(Y)/Y-1 .
\]
The polynomial \(G_p\) is monic irreducible of degree \(p\), and \(L_p\) is monic reciprocal irreducible of degree \(4p\).
The sole positive factor is \(L_p\).
Its logarithmic Mahler measure tends to a strictly positive limit, so the set of all positive factor measures has a positive lower bound.
For example \(L_3=z^{12}+z^{10}-2z^6+z^2+1\).

<a id="trace-reduction"></a>
## An irreducible finite-field trace equation

The recurrence gives \(D_n(w+w^{-1})=w^n+w^{-n}\) and makes \(D_n\) monic of degree \(n\) for \(n\ge1\).
For odd \(p\), \(D_p\) is odd and is divisible by \(Y\).
With \(Y=z^2+z^{-2}\), \(a=z^2(Y+1)\) and \(b=z^2Y\), the identity
\[
 q(z,z^{2p})=z^{2p+2}\big((Y+1)D_p(Y)-Y\big)
\]
gives the asserted factorization.
The displayed expression for \(L_p\) has integer coefficients, leading and constant coefficients one and degree \(4p\), since \(G_p\) is monic of degree \(p\).
It is reciprocal by inversion of \(z\).

In characteristic \(p\), \(D_p(Y)=Y^p\), by applying Frobenius to the Laurent identity and using injectivity of \(Y\mapsto w+w^{-1}\).
That injectivity follows by inspecting the highest Laurent exponent of the image of a nonzero polynomial.
Consequently \(\overline G_p(Y)=Y^p+Y^{p-1}-1\).
Up to a nonzero scalar its reversed polynomial is \(V^p-V-1\).
For any root \(v\) in an algebraic closure of \(\mathbb F_p\), one has \(v^{p^j}=v+j\), with \(j\) read in \(\mathbb F_p\).
The first positive \(j\) that fixes \(v\) is \(p\), so its degree is \(p\) by the Frobenius orbit criterion.
This proves irreducibility of the degree-\(p\) polynomial and its reversal over the prime field.
Monicity and reduction of an integral factorization give irreducibility of \(G_p\) over \(\mathbb Q\).

<a id="quartic-lift"></a>
## Recovering the entire degree over the trace field

Let \(u\) be a root of \(G_p\) and \(K=\mathbb Q(u)\).
The recurrence gives \(D_p(2)=2\) and \(D_p(-2)=-2\), hence \(G_p(2)=2\) and \(G_p(-2)=-2\).
Since \(p\) is odd, the rational norms of \(u-2,u+2,(u-2)(u+2)\) are respectively \(-2,2,-4\).
None is a square in \(\mathbb Q\), so none of these three elements is a square in \(K\).
The two square classes are therefore independent and \([K(\sqrt{u+2},\sqrt{u-2}):K]=4\).
Indeed if the second square root belonged to the first quadratic extension, squaring its expression \(r+s\sqrt{u+2}\) would give \(rs=0\) and make either \(u-2\) or \((u+2)(u-2)\) a square in \(K\).

Choose a nonzero \(z\) satisfying \(z^2+z^{-2}=u\).
Then \(z+z^{-1}\) and \(z-z^{-1}\) are square roots of \(u+2\) and \(u-2\).
Conversely their sum is \(2z\).
Thus \(\mathbb Q(z)=K(\sqrt{u+2},\sqrt{u-2})\) has degree \(4p\) over \(\mathbb Q\).
This accounts for the full degree of \(L_p\) and proves irreducibility.

<a id="positive-measure"></a>
## Excluding torsion and computing the sign of the limiting measure

One has \(L_p(1)=G_p(2)=2\).
If \(L_p=\Phi_m\), then \(m>1\) and \(\Phi_m(1)=2\) would force \(m\) to be a power of two.
Indeed \(\Phi_{\ell^k}(1)=\ell\) for prime powers, by the geometric-sum formula.
The identity \(m=\prod_{d\mid m,\,d>1}\Phi_d(1)\), obtained by evaluating \((X^m-1)/(X-1)\) at one, then forces \(\Phi_m(1)=1\) for every \(m>1\) with at least two different prime divisors, by induction.
The degree of a cyclotomic polynomial of order a power of two is a power of two, whereas \(4p\) is not.
Hence \(L_p\) is noncyclotomic and has \(M(L_p)>1\) by the [Kronecker characterization](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization).
The other factor is \(\Phi_8\) and has measure one.

The [Boyd--Lawton specialization theorem](../audits/literature/Den09/Yin_U002.md#specializations-and-remaining-source-reports), in the same \((1,2p)\) form as the [earlier prime construction](../ledger/Yin_L_G0458_v4.md#prime-square-fixed-template), gives \(m(L_p)=m(q(z,z^{2p}))\to m_2(q)\).
Its least nonzero integer relation has sup norm \(2p\).
On \(|z|=1\), \(Y=z^2+z^{-2}\) runs over \([-2,2]\).
For \(Y\ne-1\), Jensen's formula in \(t\) gives the inner logarithmic measure as
\[
 \log|a(z)|+
 \log M_t\!\left(t^2-\frac{Y}{Y+1}t+1\right).
\]
The second term is nonnegative and strictly positive if \(|Y/(Y+1)|>2\), in particular on an open arc meeting \(Y=-3/2\).
It is integrable because it is bounded above by \(\log(2+|Y/(Y+1)|)\) and the finitely many simple poles on the circle have integrable logarithms.
The first term averages to \(m(a)=0\).
Integrating gives \(m_2(q)>0\).
The convergence and the strict positivity for the finitely many smaller primes yield the family lower bound.
The proof supplies no numerical value of that lower bound.

## Assessment history

### Decision whole-proof

| Field | Value |
| --- | --- |
| date | 2026-11-07T17:25 |
| status | proved |
| reason | The independent review verified the exact trace and quartic factorizations, positivity at every odd prime and the positive specialization limit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Complete rational irreducible factorization, unique positive factor of degree 4p and its positive logarithmic measure limit. |
| argument | [Proof section](#trace-reduction) | The trace recurrence and the length-p Frobenius orbit after reduction modulo p. |
| argument | [Proof section](#quartic-lift) | Independence of the two square classes over the trace field and the full quartic lift. |
| argument | [Proof section](#positive-measure) | Torsion exclusion and the positive Boyd--Lawton and Jensen limit. |
| review | [Independent finding](../audits/reviews/Yin_R_G1103_v1.md#whole-proof) | All of the selected statement and argument at the source scope specified in the finding. |

## Current assessment

[Selected decision](#decision-whole-proof)


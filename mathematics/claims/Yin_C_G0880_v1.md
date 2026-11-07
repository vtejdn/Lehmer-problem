---
author: Yin
---

# A Mahler gap from bounded total variation at cyclotomic trace poles

This project deduction arose from agent-S's proposal to control the exterior roots of a reciprocal polynomial by interlacing its traces.
The argument uses [Sanders, Theorem 1.1](https://doi.org/10.1007/s00041-020-09732-y) and the [Dobrowolski–Smyth fixed-support gap](../audits/literature/DS17/Yin_U001.md#ds17-u001) at their statement and application scopes.
The [Sanders source unit](../audits/literature/San20/Yin_U001.md#san20-u001) records the normalized Fourier transform used below.

<a id="statement"></a>
## The whole reciprocal lift

Let \(B\in\mathbb Z[t]\) be monic of degree \(n\ge1\) with distinct real roots \(b_1<\cdots<b_n\) in \([-2,2]\).
For \(a\in\mathbb Z\) and \(C\in\mathbb Z[t]\) of degree less than \(n\), including \(C=0\), put
\[
 Q(t)=(t-a)B(t)+C(t),\qquad P(z)=z^{n+1}Q(z+z^{-1}),\qquad
 r_i=C(b_i)/B'(b_i).
\]
For each fixed \(K<\infty\), the class with \(\sum_i|r_i|\le K\) has a uniform gap above zero for the positive total logarithmic measures \(m(P)\).
There is also a uniform gap over the entire class with every \(r_i>0\), with no bound assumed on their sum.
The conclusions apply to whole lifts, permitting all degrees, integral \(a\), reducible \(B\) and endpoint poles.
They do not give individual lower bounds for factors of a lift with several positive-measure factors.

<a id="fourier"></a>
## Integral Fourier coefficients of bounded norm

The monic polynomial \(B^*(z)=z^nB(z+z^{-1})\) is integral with constant coefficient one and all roots on the unit circle.
By Kronecker's theorem they are roots of unity.
Choose a single order \(N\) divisible by the orders of all these roots and write \(b_i=\xi_i+\xi_i^{-1}\) with \(\xi_i^N=1\).
Set \(k=\sum r_i\) and \(H_j=\sum_i r_i(\xi_i^j+\xi_i^{-j})\) on \(\mathbb Z/N\mathbb Z\).
The expansion at infinity of
\[
             C(t)/B(t)=\sum_i r_i/(t-b_i)
\]
has integral Laurent coefficients by monic division, so \(\sum_i r_i b_i^h\in\mathbb Z\) for every \(h\ge0\), in particular \(k\in\mathbb Z\).
The integer polynomials defined by \(D_0=2,D_1=t,D_{j+1}=tD_j-D_{j-1}\) give \(D_j(b_i)=\xi_i^j+\xi_i^{-j}\).
Consequently every \(H_j\) is an integer.
With normalized counting measure on the cyclic group its Fourier algebra norm is at most \(2\sum|r_i|\), by the displayed character expansion, counting an endpoint twice.
Sanders' theorem therefore expresses \(H_j\) as a sum of at most \(L(K)\) signed coset indicators, uniformly in the conductor.
Here one uses the theorem with norm bound \(\max(1,2K)\), splitting integer coefficients into signed repetitions.
Every coset lifts to a congruence \(j\equiv u_\ell\bmod s_\ell\), where \(s_\ell\mid N\) and \(0\le u_\ell<s_\ell\).

<a id="sparse-completion"></a>
## Clearing the cosets preserves the whole measure

For \(|z|<1\), the geometric series of those cosets gives
\[
        S(z)=\sum_{j\ge0}H_jz^j=\sum_{\ell=1}^{L}
                      \frac{\epsilon_\ell z^{u_\ell}}{1-z^{s_\ell}}.
\]
For each \(\xi_i\), summing the two geometric series and subtracting one gives
\((1-z^2)/(1-b_i z+z^2)\).
Summing with weights \(r_i\) yields \(C(z+z^{-1})/B(z+z^{-1})=z(S(z)-k)/(1-z^2)\) as a rational identity.
With \(D=\prod_\ell(1-z^{s_\ell})\), it follows that
\[
 \begin{aligned}
 U(z)&=(1-az+z^2)(1-z^2)D
       +z^2\left(\sum_\ell\epsilon_\ell z^{u_\ell}
                       \frac{D}{1-z^{s_\ell}}-kD\right)\\
     &=(1-z^2)D\,P(z)/B^*(z).
 \end{aligned}
\]
The first expression is an integer polynomial with constant term one and at most \((7+L)2^L\) nonzero terms, including \(L=0\).
In the cross-multiplied second expression \(B^*,1-z^2,D\) all have logarithmic measure zero.
Hence \(m(U)=m(P)\) by additivity, even when factors cancel.
The fixed-support gap applies to \(U\) itself, proving the first assertion independently of the size of \(a\) or the conductor.

<a id="positive-residues"></a>
## Positive residues force bounded mass near zero measure

It suffices to consider \(m(P)\le\log 2\).
For each trace root \(q\) of \(Q\), the two lifted roots solve \(z^2-qz+1=0\).
Their larger radius is at most \(M(P)\le2\), hence \(|q|\le2+1/2=5/2=:R\).
For \(r_i>0\) the secular function \(Q(t)/B(t)=t-a+\sum_i r_i/(t-b_i)\) runs from positive infinity to negative infinity across each open pole gap.
Choose a zero \(c_i\in(b_i,b_{i+1})\) for each \(i<n\), and denote the two remaining roots, with multiplicities, by \(u,v\).
The formula for the leading two terms, or expansion of the logarithmic derivative at infinity, gives
\[
     a=\sum c_i+u+v-\sum b_i,\qquad
     2k=a^2+\sum b_i^2-\sum c_i^2-u^2-v^2 .
\]
Indeed the coefficient of \(t^{n-1}\) in \(Q-(t-a)B=C\) is \(k\), which gives the second identity by Newton's formula.
Interlacing gives \(b_1\le\sum b_i-\sum c_i\le b_n\), so \(|a|\le 2+2R=7\).
Pairing each \(c_i\) with \(b_i\) leaves \(b_n^2\le4\), and the variation of \(t^2\) on the disjoint intervals \([b_i,c_i]\) is at most its total variation \(8\) on \([-2,2]\).
Thus \(\big|\sum b_i^2-\sum c_i^2\big|\le12\), including \(n=1\).
It follows that \(0<k\le(49+12+2R^2)/2<37\).
Apply the first assertion with \(K=37\) and combine its lower bound with \(\log2\) outside the tested range.
This establishes a qualitative gap without evaluating its size.

## Assessment history

### Decision whole-residue-gap

| Field | Value |
| --- | --- |
| date | 2026-11-07T18:06 |
| status | proved |
| reason | Independent review checked both whole-lift assertions, the exact measure identity and the two external theorem applications. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Whole-lift gap](#statement) | Bounded total variation and unrestricted strictly positive residues at all trace poles. |
| argument | [Integral moments](#fourier) | Finite cyclic character norm and uniform coset decomposition. |
| argument | [Sparse completion](#sparse-completion) | The integer polynomial has the exact original total measure. |
| argument | [Positive residues](#positive-residues) | Interlacing and Newton identities bound the total mass near measure one. |
| dependency | [Sanders' theorem](../audits/literature/San20/Yin_U001.md#san20-u001) | Uniform signed-coset bound at fixed normalized algebra norm. |
| dependency | [Dobrowolski–Smyth](../audits/literature/DS17/Yin_U001.md#ds17-u001) | The qualitative positive gap for an integer polynomial with bounded support size. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1105_v1.md#whole-lift-review) | Both assertions with primary-source normalization and application checks. |

## Current assessment

[Selected decision](#decision-whole-residue-gap)

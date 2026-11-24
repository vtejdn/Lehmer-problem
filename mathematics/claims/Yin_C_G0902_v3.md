---
author: Yin
---

# Finite ramification in the Chebyshev quadratic trace extension

2026-11-24T19:22 UTC.

<a id="statement"></a>
## A relative discriminant bound independent of the coefficient size

Let \(q\ge1,\ p=q+1,\ M=pq,\ L=2q+1\), and take any even \(n\ge4\) with \(4^{n-1}\le2M\).
For the [Chebyshev trace polynomial](Yin_C_G0902_v1.md#conjugates) put \(d_0=n-3\) and
\[
 C(x)=U_{d_0}((x+2)/2)+U_{d_0-1}((x+2)/2),\qquad
 H(x)=x^{n-1}(x+4)+2(Mx-1)C(x).
\]
Let \(0<w<1/M\) be its positive root, \(B=\mathbb Q(w)\), and \(K=B(T)\) for \(T+T^{-1}=2+w\).
The norm of the relative discriminant ideal satisfies
\[
   N_{B/\mathbb Q}\mathfrak d_{K/B}
       \ \mid\ 4(2n-5)\gcd(2q+1,2^{\,2n-1}-1)^2.                       \tag{1}
\]
Its exact 2-part is four.
For \(2q+1\) a power of three this norm divides \(4(2n-5)\) for every allowed \(n\).
Consequently as \(n\to\infty\), its contribution \((N_{B/\mathbb Q}\mathfrak d_{K/B})^{1/(2n)}\) to the absolute root discriminant of \(K\) has upper limit at most four in general and tends to one on the powers of three.

<a id="two"></a>
## The dyadic integral basis

The [trace calculation](Yin_C_G0902_v1.md#conjugates) shows that \(H\) is Eisenstein at two, that \([B:\mathbb Q]=n\), and that \(K/B\) is quadratic.
There is a unique place \(\mathfrak p\mid2\) of \(B\), with residue degree one, and the local valuation normalized to have value group \(\mathbb Z\) satisfies \(v_{\mathfrak p}(w)=1,\ v_{\mathfrak p}(2)=n\).
Over \(B_{\mathfrak p}\), the element \(x=T-1\) has Eisenstein polynomial \(x^2-wx-w\).
It therefore gives a totally ramified quadratic extension with \(x\) a uniformizer.
In the local basis \(1,x\), the two summands of \(a+bx\), \(a,b\in B_{\mathfrak p}\), have valuations of opposite parity whenever both are nonzero.
Thus \(a+bx\) is integral exactly when both \(a,b\) are integral.
The basis discriminant \(w^2+4w\) has valuation two in \(B_{\mathfrak p}\), giving the asserted dyadic part of the norm.

<a id="odd"></a>
## Odd valuation at a trace endpoint

At an odd residue characteristic the quadratic field \(K=B(\sqrt{w(w+4)})\) ramifies precisely at places where the valuation of \(w(w+4)\) is odd, each with discriminant exponent one.
Indeed, after removing a square power of a uniformizer, an odd valuation gives a tamely ramified quadratic extension, while for a unit the residual quadratic has distinct roots over the residue algebraic closure and the extension is unramified or split.
The two elements \(w,w+4\) cannot both have positive valuation at an odd place.

Since \(n\) is even and \(d_0\) is odd, \(C(0)=2d_0+1=2n-5\) and \(C(-4)=-1\).
Thus
\[
 N_{B/\mathbb Q}(w)=H(0)=-2(2n-5),\qquad
 N_{B/\mathbb Q}(w+4)=H(-4)=2L^2 .
\]
The contribution from odd places where \(w\) has odd valuation therefore divides \(2n-5\).
It remains to bound the odd places where \(w+4\) has odd valuation.

Fix an odd prime \(\ell\mid L\), let \(a=v_\ell(L)\), and set \(t=v_\ell(2^{2n-1}-1)\).
Over \(\overline{\mathbb Q}_\ell\) normalize the valuation by \(v_\ell(\ell)=1\).
The \(n\) roots of \(H(Z-4)\) are the conjugates of \(w+4\), all of nonnegative valuation, whose valuations sum to \(2a\).
For a prime \(\mathfrak l\mid\ell\) of \(B\) with ramification index \(e_{\mathfrak l}\) and residue degree \(f_{\mathfrak l}\), each of its \(e_{\mathfrak l}f_{\mathfrak l}\) embeddings contributes valuation \(v_{\mathfrak l}(w+4)/e_{\mathfrak l}\).
In particular the total of all \(f_{\mathfrak l}\) belonging to odd valuations at this endpoint is at most \(2a\).

The linear coefficient of \(H(Z-4)\) is
\[
 H'(-4)=(-4)^{n-1}-2M-2L^2C'(-4)
       =\frac{1-2^{2n-1}}2-L^2\left(\tfrac12+2C'(-4)\right).
\]
If \(t\ge a\), the preceding estimate \(2a\) already bounds the discriminant exponent by \(2\min(a,t)\).
Suppose \(t<a\), so \(v_\ell(H'(-4))=t\).
In the elementary symmetric sum giving the linear coefficient up to sign, the least possible valuation of a product of \(n-1\) roots is the sum of the smallest \(n-1\) valuations.
By the ultrametric inequality this sum is at most \(t\).
The largest root valuation is therefore at least \(2a-t>a\), and it occurs only once.
All local conjugates have the same valuation, so that root is linear over \(\mathbb Q_\ell\), corresponding to \(e_{\mathfrak l}=f_{\mathfrak l}=1\).
The remaining places with odd valuation contribute total residue degree at most \(t\).
If \(t=0\) the largest valuation equals \(2a\), so that place too is unramified.
If \(t\ge1\) the large place contributes at most one, giving total at most \(t+1\le2t\).
Combining all odd primes and the dyadic calculation proves (1).
The [order discriminant at the two endpoints](Yin_C_G0345_v73.md#relative) alone includes the full \(L^2\) factor.
The linear coefficient permits replacing it by the gcd in (1).

Finally, \(2^{2n-1}-1\) is not divisible by three, proving the assertion for \(L\) a power of three.
In general the gcd is smaller than \(2^{2n-1}\).
Taking \(2n\)-th roots gives the limits stated above via the tower formula \(|\Delta_K|=|\Delta_B|^2N_{B/\mathbb Q}\mathfrak d_{K/B}\).

<a id="index"></a>
## What field discriminants would imply about the saturation index

For the parameters at which the [radical-closure index test](Yin_C_G0902_v2.md#index) holds, let \(\mathcal F\) consist of \(K\) and all its index-three subfields.
If \(3\nmid n\), then \(\mathcal F=\{K\}\).
For \(F\in\mathcal F\) write \(D_F=[F:\mathbb Q]\) and define
\[
 c_F=\max\left\{\frac{\log2}{4D_F},
     \frac{\log|\Delta_F|-D_F\log D_F}{2(D_F-1)}\right\}.
\]
With \(c=\min_{F\in\mathcal F}c_F\), the least positive measure \(\mu\) in the radical closure and the index \(I\) of the two generated units satisfy
\[
                            \mu\ge c,\qquad I\le4D_H/c^2 ,
\]
where \(D_H\) is the area defined in [the index test](Yin_C_G0902_v2.md#statement).
Indeed the [exterior-place count](Yin_C_G0902_v2.md#fields) makes each nontorsion relative unit a generator of some such \(F\).
The house bound gives the first term of \(c_F\).
For its monic minimum \(P\) one has
\[
 |\Delta_F|\le|\operatorname{disc}P|\le D_F^{D_F}\exp(2(D_F-1)m(P)).
\]
The first inequality follows from the index of the order generated by the unit.
For the second, Hadamard's inequality bounds the Vandermonde row at a root \(z\) by \(\sqrt{D_F}\max(1,|z|)^{D_F-1}\), and the square of the determinant gives the absolute polynomial discriminant.
These bounds apply at the actual field degrees, and (1) supplies an upper bound on the relative factor in \(|\Delta_K|\).
A uniform lower bound for \(c\) would exclude a counterexample within the saturated family.
The required lower bounds for the absolute discriminants of the varying trace fields, and potentially the index-three subfields, have not been established.

## Assessment history

### Decision finite-relative-ramification

| Field | Value |
| --- | --- |
| date | 2026-11-24T19:30 |
| status | proved |
| reason | The dyadic extension has an integral uniformizer basis. The valuations of the endpoint conjugates constrain odd ramification, and the field discriminant bounds the discriminant of a generating unit from below. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The dyadic discriminant, the odd-prime divisibility bound, and the implications for the least measure and the index in terms of absolute field discriminants. |
| argument | [two](#two) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [odd](#odd) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [index](#index) | Proof of the conclusions in this section under its stated hypotheses. |
| dependency | [Input](Yin_C_G0902_v1.md#conjugates) | The Chebyshev trace and quadratic extension. |
| dependency | [Input](Yin_C_G0902_v2.md#fields) | The possible generator fields for relative units. |
| dependency | [Input](Yin_C_G0902_v2.md#index) | The relation between area, least measure and unit-group index. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1063.md#finding) | The statement, proofs and qualifications at the checked input interfaces. |

## Current assessment

[Selected decision](#decision-finite-relative-ramification)

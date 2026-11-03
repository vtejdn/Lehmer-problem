---
author: Yin
---

# G0001: Frobenius resultants and actual orbit minors

Date: 2026-10-06.
A bounded arithmetic test for the existing Lehmer Task.
This is a proof/interface draft, not a new Task or Claim.
No enumeration, new source download or execution run was performed.

The exact reused input is the repaired powered-conjugate resultant in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001), Section F1.
Its original Dobrowolski proof remains outside the source audit.
The actual-orbit notation and maximal-minor identities come from [C215](../claims/Yin_C_G0215_v1.md#integer-orbit-constraints), with the sum-of-squared-minors Gram identity from [C209](../claims/Yin_C_G0209_v1.md#gram-lower-certificate).
Those interfaces were read before this calculation.
All deductions below are direct specializations or displayed algebra; no novelty is claimed.

## 1. The same resultant, with multiplicity and the correct sign

Let \(p(t)=\sum_{r=0}^d a_rt^r\in\mathbb Z[t]\) be monic irreducible, with nonzero constant coefficient, and not cyclotomic.
The unit hypothesis \(a_0=\pm1\) can be retained for the Task but is not needed in this section.
Let \(\alpha_i\) be its conjugate roots, \(A\) its integral companion matrix, and \(\ell\) a prime.
Define
\[
Q_\ell(z)=\prod_{i=1}^d(z-\alpha_i^\ell).
\]
The source input retains all \(d\) factors, including coincidences.
Equivalently,
\[
Q_\ell=P_{\alpha^\ell}^{[\mathbb Q(\alpha):\mathbb Q(\alpha^\ell)]}.
\]
Replacing it by the minimal polynomial without that exponent can destroy the \(\ell^d\) divisibility.

Since the powers of \(A\) commute, Frobenius modulo \(\ell\) gives
\[
p(A^\ell)\equiv p(A)^\ell=0\pmod\ell.
\]
Thus \(B_\ell=p(A^\ell)/\ell\) is an integer matrix.
Its determinant satisfies
\[
D_\ell:=\det p(A^\ell)
=\prod_i p(\alpha_i^\ell)
=\operatorname{Res}(p(t),p(t^\ell))
=\operatorname{Res}(Q_\ell,p)
=(-1)^d\operatorname{Res}(p,Q_\ell). \tag{1}
\]
The last sign is the interchange sign for two degree-\(d\) polynomials.
It is positive in the even-degree reciprocal core, but need not be silently omitted in the general domain stated here.

The determinant is nonzero.
A zero would give \(\alpha_i^\ell=\alpha_j\) for two conjugates.
A Galois automorphism of the normal closure sending \(\alpha_i\) to \(\alpha_j\), iterated through its finite order, would give \(\alpha_i^{\ell^k-1}=1\).
That contradicts irreducibility and noncyclotomicity.
Consequently
\[
0\ne D_\ell\in\ell^d\mathbb Z,\qquad |D_\ell|\ge\ell^d,\qquad
0\ne\det B_\ell\in\mathbb Z. \tag{2}
\]
This is the audited Frobenius resultant interface in an actual companion-matrix representation, not an independent new source theorem.

<a id="bounded-length-gap"></a>
## 2. A positive restricted conclusion from coefficient length

Put \(S=\|p\|_1=\sum_r|a_r|\).
For each conjugate,
\[
|p(\alpha_i^\ell)|\le S\max(1,|\alpha_i|)^{\ell d}.
\]
Multiplication over \(i\), together with (2), yields
\[
\ell^d\le |D_\ell|\le S^d M(p)^{\ell d},
\qquad
m(p)\ge\frac{\log(\ell/S)}{\ell}. \tag{3}
\]
Thus for every fixed finite \(S_0\), choosing one prime \(\ell>S_0\) gives a positive degree-independent lower bound throughout the family \(S\le S_0\).
For example,
\[
S\le5\quad\Longrightarrow\quad m(p)\ge\frac{\log(13/5)}{13}>0.
\]
This is a restricted closure, not merely a failed estimate.
The fixed coefficient-length family \(t^{2r}-4t^r+1\) has \(S=6\), consistently with its constant entropy in L G0009.

**Known-result identification.** The coordinator followed the existing Smy08 Section 5.4 report to the already retained Mig78.
[Proposition 5 and its proof](../audits/literature/Mig78/Yin_U001.md#proposition-5-length), printed 39-04 / PDF p.5, were freshly read and visually checked.
They use this same prime-norm argument and state the explicit bound \(m(p)\ge\log(2)/(2S)\), choosing a prime between \(2S\) and \(4S\).
The original prime-existence input is the standard Bertrand theorem, not newly proved here.
This is a verified attribution of the bounded-length mechanism; equation (3)'s fixed-prime proof above is complete without that interval theorem.
The local entropy and Gram deductions below remain separately proved, and no novelty is asserted for them.

The full reciprocal-unit core has no bound on \(S\).
A bound on the individual coefficient height alone does not bound \(S\) independently of degree.
In particular (3) does not settle Lehmer.
Any hypothetical sequence of positive measures tending to zero must have \(S\to\infty\); this necessary condition follows by applying (3) for each fixed \(S_0\).
No new assertion about the existence of such a sequence is made.

## 3. The direct long-window orbit-minor interface

Let \(v_j=A^je_0\), and let \(V_N\) have these columns for \(0\le j<N\).
Choose
\[
N=(\ell+1)d.
\]
Let \(E_\ell\) be the integer \(N\times d\) matrix whose \(j\)-th column is the coefficient vector of \(t^j p(t^\ell)\), \(0\le j<d\), padded with zeros.
Its largest possible exponent is \(\ell d+d-1=N-1\).
Reduction modulo \(p\) gives the exact matrix identity
\[
V_NE_\ell=p(A^\ell).
\]
Applying Cauchy--Binet and then Cauchy--Schwarz to the maximal minors gives
\[
|D_\ell|^2
\le\left(\sum_{|I|=d}\det(V_N[:,I])^2\right)
     \left(\sum_{|I|=d}\det(E_\ell[I,:])^2\right)
=G_N\det(E_\ell^{\mathsf T}E_\ell).
\]
Hence
\[
G_{(\ell+1)d}\det(E_\ell^{\mathsf T}E_\ell)\ge\ell^{2d}. \tag{4}
\]
This involves precisely the actual minors used in L G0010, not minors of a generic matrix.

The coefficient cost is explicit.
Write \(D_n(p)\) for the Gram determinant of the coefficient vectors of \(p,tp,\ldots,t^{n-1}p\), and \(D_0(p)=1\).
If \(d=q\ell+s\), \(0\le s<\ell\), then
\[
\det(E_\ell^{\mathsf T}E_\ell)
=D_{q+1}(p)^sD_q(p)^{\ell-s}. \tag{5}
\]
Indeed the columns with different indices modulo \(\ell\) have disjoint supports.
Within one residue class, deleting the common residue and dividing exponents by \(\ell\) gives the usual shifted coefficient vectors of \(p\).
There are \(s\) blocks of size \(q+1\) and \(\ell-s\) blocks of size \(q\), including empty blocks.

For \(\ell\ge d\), (5) is \(\|p\|_2^{2d}\).
In general Hadamard also gives the bound \(\det(E_\ell^{\mathsf T}E_\ell)\le\|p\|_2^{2d}\).
The prime gain survives in (4), but at a window growing with \(\ell d\) and with this coefficient/Gram cost.
No estimate making its resulting entropy certificate uniform over the full core was obtained.

<a id="short-window-cancellation"></a>
## 4. Why the most direct short-window transfer loses the prime factor

The alternative source representation is \(F_\ell=Q_\ell-p=\ell R_\ell\), with \(R_\ell\in\mathbb Z[t]\), \(\deg R_\ell\le d-1\).
It is nonzero because \(D_\ell\ne0\).
At
\[
N=2d-1,
\]
form \(E_F\) from the coefficient columns \(t^jF_\ell\), \(0\le j<d\), and \(E_R=E_F/\ell\).
The exponent bound is \(j+\deg F_\ell\le2d-2=N-1\).
Thus
\[
V_NE_F=F_\ell(A)=Q_\ell(A),\qquad E_F=\ell E_R.
\]
Using the same maximal-minor inequality and \(|\det Q_\ell(A)|=|D_\ell|\) gives
\[
G_N\ge
\frac{|\det R_\ell(A)|^2}{\det(E_R^{\mathsf T}E_R)}. \tag{6}
\]
All factors \(\ell^{2d}\) have canceled **before** any Hadamard bound.
The \(d\) shifts of a nonzero polynomial are linearly independent, so \(\det(E_R^{\mathsf T}E_R)\) is a positive integer.
Keeping only the known lower bound \(|\det R_\ell(A)|\ge1\) supplies \(1/\det(E_R^{\mathsf T}E_R)\le1\), no improvement on the existing \(G_N\ge1\).

The cruder coefficient version exhibits the same cancellation:
\[
G_N\ge\frac{\ell^{2d}}{\|F_\ell\|_2^{2d}}
=\|R_\ell\|_2^{-2d}\le1.
\]
This locates the missing information: a stronger comparison would have to retain a quantitatively large \(\det R_\ell(A)\), use a sharper joint collection of primes, or exploit the actual minor correlations.
Merely repeating divisibility after dividing every column by \(\ell\) cannot do it.
This is a limitation of this specific transfer, not of all resultant methods.

## 5.
The separate pairwise estimate and its exact loss

For comparison, the root-by-root estimate is
\[
|D_\ell|=\prod_{i,j}|\alpha_i^\ell-\alpha_j|
\le2^{d^2}M(p)^{d(\ell+1)}.
\]
Combined with (2), it yields only
\[
m(p)\ge b_d(\ell):=\frac{\log\ell-d\log2}{\ell+1}. \tag{7}
\]
This lower bound is positive only for \(\ell>2^d\).
Put \(y=\ell/2^d>1\); then
\[
b_d(\ell)\le\frac{\log y}{2^d y}\le\frac1{e\,2^d}.
\]
Thus even optimizing the prime in this particular bound cannot produce a degree-independent positive constant.
Multiplying these same separate upper and lower bounds over any finite nonempty multiset of primes gives the \((\ell+1)\)-weighted average of the numbers \(b_d(\ell)\), so it has the same obstruction.
This does not address joint determinant estimates that remove some of the \(d^2\log2\) cost.

<a id="restricted-rational-capture"></a>
## 6. Return to the primary entropy route under the same restriction

Use exactly the rational finite-entropy setting of [L G0002](Yin_L_G0002_v1.md#rational-primary-formula): a rational vector space \(V\) of arbitrary dimension, a rational linear endomorphism \(T\), and \(h(T)<\infty\).
For each monic irreducible primary polynomial \(q\in\mathbb Q[t]\), write \(q_{\mathbb Z}\) for its primitive integral associate with positive leading coefficient, \(w_q=m(q_{\mathbb Z})\), and \(\ell_q\) for its positive-weight composition multiplicity.

Assume there is one fixed finite \(S_0\) such that **every occurring positive-weight primary factor whose primitive integral associate is monic** satisfies \(\|q_{\mathbb Z}\|_1\le S_0\).
Choose one prime \(\ell>S_0\) and put
\[
c=\frac{\log(\ell/S_0)}{\ell}>0,\qquad
\eta=\min(c,\log2)>0.
\]
Equation (3) gives \(w_q\ge c\) for all these monic factors.
If nonmonic primitive integral factors are also allowed, their positive integral leading coefficient is at least 2, so \(w_q\ge\log2\).
Thus every positive weight is at least \(\eta\).
The exact formula in L G0002 gives
\[
h(T)=\sum_{w_q>0}\ell_qw_q
\ge\eta\sum_{w_q>0}\ell_q,\qquad
\sum_{w_q>0}\ell_q\le h(T)/\eta<\infty.
\]
There are consequently only finitely many positive primary components, with finite total composition multiplicity.
Their sum is a finite-dimensional invariant rational space carrying the entire entropy; L G0002's accepted finite-dimensional realization interface supplies a finite set \(F\) with \(H(T,F)=h(T)\).
Zero-weight primary components may still have arbitrary dimension.
When \(h(T)=0\), \(F=\{0\}\) suffices.

This closes the indicated **bounded-coefficient-length class of rational flows**, not all finite-entropy flows.
The full Task lacks the uniform \(S_0\) hypothesis.
No bound on the entire group's rank, no general abelian primary decomposition, and no unrestricted finite-attainment theorem is inferred.

## Scope of the result and stop

The useful outputs are the known bounded-\(\|p\|_1\) gap (3) and its restricted rational-flow attainment consequence, the exact longer-window bridge (4)--(5), and the explicit short-window cancellation (6).
The full-degree, unbounded-coefficient-length Lehmer problem remains untouched by a uniform conclusion.
The original contributor/coordinator and separate Section4 findings are retained at [R508](../audits/reviews/Yin_R_G0508_v1.md#original-frobenius-contributor-checks), at their actual original scope and day precision.
The complete current statement and argument are in [C217v2](../claims/Yin_C_G0217_v2.md#statement), with the explicit positive coefficient bound and [actual whole self-review](../audits/reviews/Yin_R_G0508_v1.md#current-frobenius-minor-finding).
The restricted closure, full-core limitation and actual failed transfer remain exploration here; no further mathematical branch or enumeration is authorized by this placement.

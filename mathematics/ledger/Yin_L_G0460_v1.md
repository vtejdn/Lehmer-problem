---
author: Yin
---

# Integer coefficient finite free variants and their Mahler costs

Date: 2026-11-07.
Human author: Yin.
This bounded comparison follows the finite free integer-closure question and the [arithmetic Brown-measure synthesis](Yin_L_G0459_v1.md#finite-arithmetic-constraints).
The coordinating AI agent inspected the sources specified below and performed the direct coefficient and example checks in this discussion.
This is a synthesis of source inputs, ordinary specializations and useful failed implications, with no novelty claim, independent project review or new Claim assessment.
The [unrestricted Lehmer question](../tasks/Yin_T_G0001_v1.md#contract) remains unresolved.

<a id="scope-and-source-interfaces"></a>
## Question and source interfaces

Can a finite free convolution or a related operation preserve monicity, integer coefficients and real-rootedness while retaining root bounds useful for the original total Mahler gap?
These properties must be distinguished from preservation of a near-unit Mahler budget and from coverage of arbitrary reciprocal integer inputs.

| Input | Exact scope used |
| --- | --- |
| [MSS15-U001](../audits/literature/MSS15/Yin_U001.md#finite-free-definitions) | Retained arXiv:1504.00350v2, Definitions 1.1, 1.4 and 1.7 and Theorems 1.3 and 1.6, printed/PDF pp. 2-4: coefficient normalizations and real/nonnegative-root preservation with endpoint bounds. The existing source check is reused. |
| [GW96 published PDF](../literature/pdf/GW96--published.pdf) | Garloff--Wagner, Journal of Mathematical Analysis and Applications 202 (1996), 797-809. Ordinary Hadamard product on printed p. 798/PDF p. 2, standard-polynomial convention on printed p. 799/PDF p. 3, and Theorem 4(a) on printed p. 800/PDF p. 4. These complete selected pages were text-read and visually checked. Theorem 4(a) is accepted as an established statement; its proof chain was not audited. |
| [LR17 arXiv v1](../literature/pdf/LR17--arxiv-v1.pdf) | Leake--Ryder, arXiv:1712.02499v1, 7 December 2017, printed/PDF pp. 1-2: the unnormalized finite-difference convolution, backward-difference convention and Theorem 1.4 on b-mesh preservation. Both pages were text-read and visually checked; the theorem's proof was not audited. |
| [Smy08 restricted height gap](../audits/literature/Smy08/Yin_U002.md#smy08-restricted-height-gap) | Reused source report of Schinzel's totally real gap, with its original algebraic-integer, nonzero and non-torsion restrictions. |
| [MS12 symmetric-matrix interface](../audits/literature/MS12/Yin_U001.md#ms12-u001) and [L454 full trace-lift cost](Yin_L_G0454_v1.md#returning-every-error-to-total-mahler-measure) | Existing exact matrix-gap, excluded-measure and trace-cost interfaces, at their retained statement/applicability and proof-inspection limits. |

The selected [GW96 edition notes](../audits/literature/GW96/readme.md) and [LR17 edition notes](../audits/literature/LR17/readme.md) distinguish the originals and actual publication metadata.
The bounded search covered integer/integral finite free convolution, binomial coefficient restrictions, Hadamard/Schur--Szego products and finite-difference mesh variants.
It stopped once the two positive arithmetic constructions and the precise normalization/Lehmer obstructions below were identified.
No exhaustive classification or claim that no other useful variant exists is made.

<a id="binomial-coefficient-classes"></a>
## The original operations on coefficient-divisibility classes

**Definition (binomial coefficient restriction at dimension d).**
For d>=1, consider monic integer polynomials with coefficients of the form
\[
 p(x)=\sum_{i=0}^d(-1)^i\binom di A_i x^{d-i},
 \qquad A_i\in\mathbb Z,\quad A_0=1.
\tag{1}
\]
This is an explicit coefficient restriction on the original polynomial, not a change in the ordinary monomial-basis meaning of integer coefficients.
For a second such polynomial q, use integers B_i with B_0=1.
Direct substitution in MSS15's symmetric convolution formulas gives
\[
 \begin{aligned}
 (p\boxplus_dq)(x)
 &=\sum_{k=0}^d(-1)^k\binom dk
   \left(\sum_{i+j=k}\binom ki A_iB_j\right)x^{d-k},\\
 (p\boxtimes_dq)(x)
 &=\sum_{i=0}^d(-1)^i\binom di A_iB_i x^{d-i}.
 \end{aligned}
\tag{2}
\]
For the additive identity, the original weight times binomial(d,i)binomial(d,j) is binomial(d,k)binomial(k,i), where k=i+j.
This proves closure of (1) under both operations, preserving monicity and degree d.
For real-rooted inputs the additive output is real-rooted; for nonnegative real-rooted inputs the multiplicative output has nonnegative real roots.
The operations are unchanged, so the original applicable root bounds remain available, in particular
\[
 \lambda_{\max}(p\boxplus_dq)
 \le\lambda_{\max}(p)+\lambda_{\max}(q),
 \qquad
 \lambda_{\max}(p\boxtimes_dq)
 \le\lambda_{\max}(p)\lambda_{\max}(q)
\tag{3}
\]
under their respective real-root and nonnegative-root hypotheses.
No additional dimension factor is introduced by restricting to (1).

For MSS15's asymmetric additive operation, the analogous square-binomial restriction
\[
 a_i=\binom di^2 A_i,\qquad b_i=\binom di^2 B_i
\]
gives the output coefficients
\[
 c_k=\binom dk^2\sum_{i+j=k}\binom ki^2 A_iB_j.
\tag{4}
\]
It is therefore another integral monic closed subclass, with the source's nonnegative-root preservation under the stated input hypotheses.
These are direct coefficient specializations, not new preservation theorems beyond the cited source results.

The restrictions do not cover arbitrary monic integer polynomials.
For example x^2-3x+1 fails (1) at i=1, since 2 does not divide 3.
A general way to force (1) is to replace p by
\[
 p_c(x)=c^d p(x/c),\qquad c=d!.
\]
Its coefficient indexed by i is c^i a_i, divisible by binomial(d,i), because every binomial(d,i) divides d!.
But if p(0)=1 or -1 and d>=2, then
\[
 |p_c(0)|=c^d,\qquad m(p_c)\ge d\log c.
\tag{5}
\]
Thus this universal forcing step already spends a large total Mahler budget on unit inputs.
The cost cannot be discarded when returning to the original polynomial.

<a id="hadamard-variant"></a>
## A Hadamard variant with integer coefficients and nonnegative roots

**Definition (signed coefficientwise product).**
For monic degree-d polynomials
\[
 p(x)=\sum_{i=0}^d(-1)^ia_i x^{d-i},\qquad
 q(x)=\sum_{i=0}^d(-1)^ib_i x^{d-i},
\]
put
\[
 H_d(p,q)(x)=\sum_{i=0}^d(-1)^ia_i b_i x^{d-i}.
\tag{6}
\]
This removes the binomial denominator from MSS15's multiplicative convolution.
It preserves monicity, degree and integer coefficients on all monic integer inputs.
If p and q have only nonnegative real roots, then H_d(p,q) also has only nonnegative real roots.
Indeed F(x)=(-1)^d p(-x) and G(x)=(-1)^d q(-x) are monic with only nonpositive real zeros.
GW96 Theorem 4(a) applies to their ordinary coefficientwise product F*G, and H_d(p,q)(x)=(-1)^d(F*G)(-x).
The source convention standard means positive leading coefficient, which holds here.
This uses the ordinary Hadamard product defined on printed p. 798 and Theorem 4(a), not a different factorial-weighted product.

The exact relation to finite free multiplication is
\[
 H_d(p,q)=(p\boxtimes_dq)\boxtimes_dh_d,
 \qquad
 h_d(x)=\sum_{i=0}^d(-1)^i\binom di^2x^{d-i}.
\tag{7}
\]
It follows by applying the multiplicative coefficient formula twice.
Also h_d=H_d((x-1)^d,(x-1)^d), so its roots are positive, and their sum is d^2.
Consequently lambda_max(h_d)<=d^2 and (3) yields the coarse explicit bound
\[
 \lambda_{\max}(H_d(p,q))
 \le d^2\lambda_{\max}(p)\lambda_{\max}(q).
\tag{8}
\]
This is a dimension-dependent comparison, not a claim that the original multiplicative root bound survives without a factor.

There is a decisive zero-Mahler control:
\[
 p=q=(x-1)^2,\qquad
 H_2(p,q)=x^2-4x+1,\qquad
 m(H_2(p,q))=\log(2+\sqrt3)>0,
 \quad m(p)=m(q)=0.
\tag{9}
\]
More generally the roots of h_d have sum d^2, so its largest root is at least d and m(h_d)>=log d.
Thus this variant can add positive, even unbounded, total Mahler measure to zero-measure inputs.
In particular it cannot satisfy m(H_d(p,q))<=C(m(p)+m(q)) on all such inputs for any finite C.
The variant supplies a genuine arithmetic real-rooted operation, but its extra factor h_d must be paid for in a Lehmer comparison.

<a id="finite-difference-normalization-check"></a>
## Finite-difference convolution: mesh preservation does not give monic integer closure

For b>0, LR17 uses the backward difference
\[
 \Delta_b f(x)=\frac{f(x)-f(x-b)}b,
\]
and defines
\[
 T_{b,d}(p,q)(x)=\sum_{k=0}^d
    (\Delta_b^kp)(x)(\Delta_b^{d-k}q)(0).
\tag{10}
\]
The source's b-mesh condition means real roots with minimum pairwise spacing at least b.
Theorem 1.4 states that b-mesh is preserved under (10) when both inputs satisfy it.
This is not an unconditional real-rootedness assertion for arbitrary real-rooted inputs.

For monic degree-d inputs, the leading coefficient of (10) is d!, because only the k=0 term contributes at degree d and Delta_b^d q=d!.
At b=1 integer inputs give an integer polynomial, but it is not monic for d>=2.
Dividing by d! does not generally preserve integer coefficients, even within the mesh domain.
For the exact example
\[
 d=2,\quad b=1,\quad p=q=x^2-2x,
\]
the input mesh is 2, while
\[
 \Delta_1p=2x-3,\quad\Delta_1^2p=2,
 \qquad
 T_{1,2}(p,p)=2x^2-10x+9.
\]
The monic output is x^2-5x+9/2, which fails integer closure.
Its real roots differ by sqrt(7), in agreement with the source's mesh-preservation statement.
Thus this particular mesh generalization does not by itself solve the original normalization obstruction.
The source's q-multiplicative branch was located but is not adopted here as an arithmetic closure construction.

<a id="lehmer-use-and-missing-transfer"></a>
## What a Lehmer application would still require

Directly real-rooted integer inputs form a restricted part of the classical problem.
The existing Smy08 source account already reports Schinzel's positive height gap for nonzero nontorsion totally real algebraic integers.
It does not supply a gap for arbitrary complex conjugate sets by changing the root-preserving operation.

For a monic integer Q(t) of degree n with real roots t_j, the reciprocal lift is
\[
 P(z)=z^nQ(z+z^{-1}).
\]
It is monic integer of degree 2n and constant coefficient one.
Its exact total Mahler cost, also used in the existing L454 comparison, is
\[
 m(P)=\sum_{j=1}^n G(t_j),\qquad
 G(t)=\begin{cases}
 0,&|t|\le2,\\
 \operatorname{arcosh}(|t|/2),&|t|>2.
 \end{cases}
\tag{11}
\]
For each real t, the corresponding quadratic z^2-tz+1 has either two unit-circle roots or a reciprocal real pair, giving precisely the indicated contribution.
An endpoint root estimate is not by itself a uniform comparison of the full sum (11) with the original m(P).
Extra factors, degree changes and altered coefficients all retain their actual contribution.
For arbitrary reciprocal integer P, its trace polynomial need not be real-rooted: z^4+3z^2+1=z^2((z+z^-1)^2+1) has trace polynomial t^2+1.
Thus a real-root preservation theorem for Q does not cover every original reciprocal input.

Integer symmetric matrix models are useful for restricted constructions, but their reciprocal lifts already satisfy the accepted MS12 gap at Lehmer's number.
That source also records an explicit small-measure reciprocal polynomial excluded from the matrix-measure list.
A padded realization containing the desired polynomial as a factor does not transfer a lower bound on the whole product to that factor; all additional factors must be charged.
No assertion of a universal measure-preserving symmetric realization is used here.

The binomial-divisibility class is the cleanest option when an actual input already belongs to it, since the source operation and root bounds remain unchanged.
The Hadamard variant is an explicit arithmetic operation on nonnegative-root inputs, with a quantified extra root factor and the zero-measure inflation obstruction.
The finite-difference mesh variant keeps its different leading coefficient and its failure after monic normalization.
None of these checks supplies a uniform total-Mahler gap for all integer polynomials or a small-positive-to-zero family.
A further application needs an actual original-input realization and a degree-independent comparison at the full Green-cost scale in (11), with all arithmetic and factor costs included.
[L461](Yin_L_G0461_v1.md#finite-free-contractive-kernels) supplies a complementary Mahler contraction for multiplicative measure-one kernels, including normalized derivatives on their actual integer coefficient domain, and distinguishes this from indefinitely repeatable positive descent.

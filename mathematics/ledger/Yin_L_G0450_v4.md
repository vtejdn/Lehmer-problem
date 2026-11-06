---
author: Yin
---

# Fixed cubic mixed all-pass iteration: an ordinary-height floor from two limiting measures

Date: 2026-11-06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The coordinating contributor proposed the fixed cubic backward tree and the incompatible-measures test.
The source-applicability contributor checked the published dynamical equidistribution statements and assembled the complete argument below, including the zero-height and full-factor accounting steps.
These are ordinary author-development checks, not an independent project review or a new Claim assessment.
The coordinating and construction contributors subsequently read the complete argument (D1)--(D14), with no substantive defect found in the full-orbit limits, local pullback contradiction or factor-degree accounting.
That ordinary cross-check does not audit the BR06 original proofs or independently reproduce J141.

<a id="cubic-allpass-revision-scope"></a>
## Scope and fixed predecessors

[V3](Yin_L_G0450_v3.md#mixed-allpass-revision-scope) remains fixed with its quadratic mixed-map norm escape, complete root costs, integral-binomial obstruction and conditional bounded-degree extension.
This version tests the actual fixed cubic map used in [J141](../computations/programs/Yin_J_G0141/readme.md).
Its conclusion covers all depths and every irreducible factor of those actual iterates without assuming their irreducibility.
The finite degree-30 and degree-90 factorizations in J141 are not premises of the argument, and their uncertified numerical root measures are not used.

The [v2 factor-proliferation bridge](Yin_L_G0450_v2.md#fixed-source-proliferation-revision) asks for bounded total logarithmic Mahler cost together with an unbounded number of positive irreducible factors within the same inputs.
For this fixed cubic iteration there is a stronger obstruction: a positive ordinary-height floor on its complete backward tree forces total measure to grow at least linearly with the actual degree.
The constant is not made effective and is not uniform over changing rational maps.
No assertion about arbitrary growing-degree mixed maps is deduced.

<a id="cubic-allpass-actual-polynomials"></a>
## The actual integer recursion and its backward tree

Use the fixed Lehmer polynomial from [v3](Yin_L_G0450_v3.md#mixed-allpass-revision-scope),
\[
 P_L(z)=z^{10}+z^9-z^7-z^6-z^5-z^4-z^3+z+1,
\]
which is monic and irreducible over Q, has constant coefficient one, and satisfies P_L(1)=-1 and P_L(-1)=1.
Its Galois orbit contains a positive real root lambda>1.
Put
\[
 g(z)=z^3-z-1,\qquad g^*(z)=z^3g(1/z)=1-z^2-z^3,
 \qquad R(z)=g^*(z)/g(z),
 \tag{D1}
\]
and define
\[
 P_0=P_L,\qquad D_n=10\cdot3^n,\qquad
 P_{n+1}(z)=g(z)^{D_n}P_n(R(z)).
 \tag{D2}
\]
The rational function in (D1) has degree exactly three.
Indeed g+g*=-z(z+1), while g(0)=g(-1)=-1, so g and g* have no common root.

For every n, (D2) is a monic integer polynomial of degree D_n with constant coefficient one and
\[
                        P_n(1)=-1,\qquad P_n(-1)=1.
 \tag{D3}
\]
Here is the induction, including the absence of degree cancellation.
If P_n has even degree D_n, its homogenization evaluated at (g*,g) is an integer polynomial of degree at most 3D_n.
Its coefficient of z^(3D_n) is P_n(-1)=1 because the leading coefficients of g*,g are -1,1.
Its constant coefficient is (-1)^(D_n) P_n(-1)=1 because their constants are 1,-1.
Finally g(1)=g*(1)=-1 and g(-1)=-1, g*(-1)=1, so the two endpoint values in (D3) are preserved.
This proves (D3), even degree, primitivity and the exact degree at each step; no integer content is silently removed.

If g(beta)=0, coprimality gives g*(beta) nonzero and the homogenized polynomial in (D2) takes the value g*(beta)^(D_n), since P_n is monic.
Thus no root of P_(n+1) is a pole of R.
Every root beta of P_n has R^n(beta) equal to some root of P_L, and conversely every projective inverse image of such a source root appears in the polynomial, with its algebraic multiplicity.
There is no root at infinity, by the nonzero leading coefficient.
Let
\[
 \mathcal B=\bigcup_{n\ge0}\{\beta\in\overline{\mathbb Q}:P_n(\beta)=0\}
 \tag{D4}
\]
be this complete backward tree, with repetitions removed only for set notation.
Each bounded-depth part is finite.

<a id="cubic-allpass-no-zero-height"></a>
## No ordinary-height-zero point occurs

The map R preserves the unit circle T and has no pole on it.
For |z|=1, real coefficients give g*(z)=z^3 conjugate(g(z)).
If g had a root on T, the same identity would make it a common root of g and g*, contradicting coprimality.
Consequently |R(z)|=1 throughout T, and every iterate of R maps T into itself.

Suppose a root of unity beta belonged to B and R^n(beta)=alpha', with alpha' a root of P_L.
Choose a Q-automorphism of Qbar carrying alpha' to lambda>1; it carries beta to another root of unity and commutes with R.
Its image of the displayed equality would put lambda in T, a contradiction.
The points 0 and infinity also cannot occur: R is defined over Q, so all their projective forward iterates are Q-rational, whereas every root of P_L has degree ten.
By the ordinary-height zero criterion in the accepted [height normalization](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization), every point of B therefore has h(beta)>0.
In particular no P_n has a cyclotomic factor, and every irreducible factor has positive logarithmic Mahler measure.
This argument uses the full target Galois orbit, including lambda; it does not incorrectly assume that a selected source root on T has positive radial contribution by itself.

<a id="cubic-allpass-measures-differ"></a>
## The complex canonical measure is not circle Haar measure

Let mu_R be the complex canonical probability measure of R, and let nu_T be normalized angular measure on T.
The accepted [BR06 measure statement](../audits/literature/BR06/Yin_U001.md#br06-height-and-measure), Theorem 2.1(B), gives the pullback balance
\[
                              R^*\mu_R=3\mu_R.
 \tag{D5}
\]
This is a pullback with preimages counted by their local degrees; mere forward invariance would not suffice below.
Direct differentiation of (D1) gives
\[
                             R(0)=-1,\qquad R'(0)=1.
 \tag{D6}
\]
The holomorphic inverse function theorem therefore gives a sufficiently small open neighborhood U of 0, disjoint from T and from the poles of R, on which R is one-to-one onto an open neighborhood V of -1.
There is a nonempty open circle arc I contained in V intersect T, and its inverse branch lies in U with local degree one.
The measure definition of pullback gives
\[
 (R^*\nu_T)(U)
   =\int\sum_{R(x)=y}e_x(R)\mathbf 1_U(x)\,d\nu_T(y)
   \ge\nu_T(I)>0,
 \qquad 3\nu_T(U)=0.
 \tag{D7}
\]
Equivalently the same strict inequality follows by a nonnegative continuous test function supported in U and positive along a smaller inverse arc.
Thus nu_T fails (D5), and
\[
                              \mu_R\ne\nu_T.
 \tag{D8}
\]
No classification of rational maps with circular Julia sets or invariant measures is invoked.

<a id="cubic-allpass-height-floor"></a>
## Equidistribution excludes arbitrarily small ordinary height

Fix one root alpha of P_L and put H=hat h_R(alpha).
Canonical height is Galois invariant because R is defined over Q.
Consequently, if beta is a root at depth n, the canonical functional equation gives
\[
                         \widehat h_R(\beta)=3^{-n}H.
 \tag{D9}
\]
The height definitions and identities are supplied by [Smy08](../audits/literature/Smy08/Yin_U004.md#smy08-canonical-height), also checked in the published BR06 pp.628--629.
No assumption H>0 is needed: if the source were preperiodic, (D9) would instead vanish at every depth and the same small-point theorem would apply.

Suppose that the positive numbers h(beta), beta in B, had infimum zero.
Choose a sequence of distinct beta_j with h(beta_j) tending to zero.
Distinctness is possible because every fixed finite subset of B has positive minimum height.
Choose their least depths n_j; bounded-depth parts are finite, so n_j tends to infinity after retaining a subsequence.
Equation (D9) gives hat h_R(beta_j) tending to zero.
Let nu_j give equal weight to all conjugates of beta_j over Q, which form the root set of its own irreducible minimal polynomial, not necessarily that of the entire P_(n_j).
The [BR06 full-orbit theorem](../audits/literature/BR06/Yin_U001.md#br06-galois-small-point-equidistribution), Theorem 2.3 with k=Q, gives
\[
                                 \nu_j\Longrightarrow\mu_R.
 \tag{D10}
\]
Applying the same theorem to z^2, equivalently its Theorem 2.4 ordinary-height specialization, gives
\[
                                 \nu_j\Longrightarrow\nu_T.
 \tag{D11}
\]
Both limits are weak limits of the same probability measures on the Riemann sphere, so uniqueness of weak limits contradicts (D8).
We have proved the existence of a constant epsilon>0, depending on this fixed R and this fixed target orbit, such that
\[
                         h(\beta)\ge\epsilon
                         \quad\hbox{for every }\beta\in\mathcal B.
 \tag{D12}
\]
No lower bound on degrees is assumed in applying the theorem; its distinct-small-point hypotheses already force orbit degrees to tend to infinity by Northcott.
The source-point nonexceptionality condition used for complex entire-fiber equidistribution is not needed for (D10).
If a backward tree were finite, the ordinary-height conclusion would instead follow immediately from positivity at its finitely many points.

<a id="cubic-allpass-full-factor-cost"></a>
## Every factor and the complete cost

Factor the actual monic integer polynomial as
\[
                      P_n=\prod_f f^{e_f}
\]
with monic irreducible integer factors, retaining all multiplicities e_f.
For any root beta of f, the normalization of logarithmic Mahler measure gives
\[
                       m(f)=\deg(f)h(\beta)
                             \ge\epsilon\deg(f)>0.
 \tag{D13}
\]
Thus summing over every factor, or equivalently over every exterior-root contribution of P_n, yields
\[
 \begin{split}
 m(P_n)
   &=\sum_f e_f m(f)
     =\sum_{P_n(\beta)=0}\log\max\{1,|\beta|\}\\
   &\ge\epsilon\sum_f e_f\deg(f)
     =10\epsilon\,3^n.
 \end{split}
 \tag{D14}
\]
Roots in the middle sum are counted with multiplicity.
There is no omitted leading-coefficient term because P_n is monic, and no omitted cyclotomic degree because the zero-height argument excludes it.
The positive-factor count may still vary or grow; no all-depth irreducibility or uniform count bound is asserted.
Nevertheless bounded total measure is impossible, and selecting any individual positive irreducible factor cannot produce total measure tending to zero because (D13) is at least epsilon.
This uses complete measure, not a normalized-height substitution for the Lehmer target.

<a id="cubic-allpass-source-and-remaining-boundary"></a>
## Source adoption and remaining boundary

The accepted external inputs are the exact published BR06 Theorem 2.3 and its z^2 specialization, together with the complex pullback balance in Theorem 2.1(B), at the scope retained in [BR06 U001](../audits/literature/BR06/Yin_U001.md#br06-inspection-limit).
The original proofs of Theorem 2.1 in Lyubich and Freire--Lopes--Mane, and BR06's full proof and potential-theory dependencies in Sections 3--6, were not audited.
Their use here is acceptance of established external statements after source and hypothesis checking, not a claim of independent source-proof verification.
The local arguments (D1)--(D14) were checked in ordinary author development.

The conclusion excludes this one complete fixed cubic backward-tree construction independently of the two finite J141 factorizations.
It gives neither a numerical value of epsilon nor a uniform epsilon when R changes with the construction index.
A moving-map or moving-target construction would require new simultaneous control and cannot reuse (D9)--(D11) with a changing limiting canonical measure as if it were fixed.
This is a failed counterexample mechanism with an exact scope, not a proof of the unrestricted Lehmer conjecture.

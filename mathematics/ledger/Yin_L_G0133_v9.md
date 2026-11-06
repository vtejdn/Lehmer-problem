---
author: Yin
---

# Natural trace Grams and the arithmetic loss of cheap real realizations

Date: 2026-11-05.
Prepared for Yin under the [unrestricted G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
The coordinating agent proposed testing the natural integral trace Gram and supplied the explicit scalar multipliers for the cheap real comparison.
The witt_moment_compatibility delegate checked and developed the trace-Gram identities, the exact block-metric perturbation and the first-coefficient irrationality proof.
Both contributors checked these deductions on the author side.
This is a retained original-input construction comparison, not an independent review or a new Claim assessment.

<a id="trace-gram-cost-scope"></a>
## Scope and adequate existing inputs

The question is whether a natural positive integral metric on the actual reciprocal order can supply the matrix analytic-germ realization with total determinant price comparable to the original total Mahler measure.
The comparison below keeps the original degree, every conjugate and its full quadratic pair.
It concerns irreducible reciprocal inputs with all trace roots real, including Salem polynomials; it is not a covering reduction of unrestricted G0001.

[L133 v8](Yin_L_G0133_v8.md#matrix-original-input-scope) retains the preceding actual matrix realizations and their failure mechanisms.
Its [integral trace-basis calculation](Yin_L_G0133_v8.md#integral-trace-basis-countercontrol) supplies the nearby order construction, without claiming a cheap Schur realization after changing the basis.
Versions v1--v8 remain fixed.
The new comparison belongs to the same original-input realization-cost question.

The analytic estimate used is the [complete singular-value determinant bound in C868 v4](../claims/Yin_C_G0868_v4.md#gram-loewner-determinant), at its [adopted scope](../claims/Yin_C_G0868_v4.md#decision-whole-integral-metric-review-2026-11-05).
Its [primitive-Gram normalization](../claims/Yin_C_G0868_v4.md#primitive-gram-covariance) and [original-input boundary](../claims/Yin_C_G0868_v4.md#gram-original-input-boundary) remain in that Claim.
No later version of C868 is an input here.

The positive integral trace-form construction is already retained in [C227](../claims/Yin_C_G0227_v1.md#neutral-rational-symmetric-realization).
The exact reciprocal trace field and order are retained in [C243](../claims/Yin_C_G0243_v1.md#reciprocal-trace-domain), including its [signed discriminant identity](../claims/Yin_C_G0243_v1.md#reciprocal-trace-order-index) and [distinct original and trace measure costs](../claims/Yin_C_G0243_v1.md#reciprocal-trace-entropy-boundary).
The rational-centralizer and mixed-conjugate normality obstruction is already proved in [C228](../claims/Yin_C_G0228_v1.md#mixed-conjugate-normal-obstruction).
Those exact existing arguments are reused, not treated as new external results.
No new source acquisition, numerical root computation or literature-priority claim is made.

<a id="actual-trace-order-and-gram"></a>
## The actual order and its natural positive integral Gram

Let
\[
 P(t)=t^d q(t+t^{-1})\in\mathbb Z[t]
 \tag{1}
\]
be monic, irreducible, reciprocal of degree \(2d\ge2\), with \(P(0)=1\) and \(m(P)>0\).
Assume q is monic integral of degree d, all its roots \(s_1,\ldots,s_d\) are real, and \(q(0)\ne0\).
The trace-field conclusion in C243 makes q irreducible and separable.
Also no \(s_i\) equals \(2\) or \(-2\), since that would give a root \(1\) or \(-1\) of the positive-measure irreducible P.

Let S be the standard column companion of q in the basis \(1,s,\ldots,s^{d-1}\) of \(\mathbb Z[s]/q\).
Define
\[
 (H_q)_{ij}=\operatorname{Tr}_{\mathbb Q(s)/\mathbb Q}(s^{i+j}),
 \qquad 0\le i,j<d.
 \tag{2}
\]
These traces are integers: they are traces of the integer matrices \(S^{i+j}\).
With \(V_{ij}=s_i^j\), evaluation gives
\[
 H_q=V^TV>0,\qquad VS=\operatorname{diag}(s_1,\ldots,s_d)V,
 \qquad S^TH_q=H_qS.
 \tag{3}
\]
The Vandermonde V is invertible because the trace roots are distinct.
Thus (3) proves positivity, not merely nonnegativity.

The full original order is identified without enlarging it:
\[
 \mathbb Z[t]/P
 \cong\mathbb Z[s,t]/(q(s),t^2-st+1).
 \tag{4}
\]
On the left t is a unit because \(P(0)=1\), and \(s=t+t^{-1}\) gives the forward map.
On the right \(t^{-1}=s-t\), and (1) gives the reverse map.
They are inverse on both generators.
Monic division in s and then in t makes
\[
 1,s,\ldots,s^{d-1},\quad t,ts,\ldots,ts^{d-1}
 \tag{5}
\]
an actual integer basis of that order.
Its change from the original power basis is unimodular; no maximal order, rational enlargement or deleted factor is used.

Multiplication by t in (5) has the integral unimodular matrix
\[
 C=\begin{pmatrix}0&-I_d\\I_d&S\end{pmatrix},\qquad
 C^{-1}=\begin{pmatrix}S&I_d\\-I_d&0\end{pmatrix}.
 \tag{6}
\]
Its complete characteristic polynomial is P, either from (4) or from
\[
 \det(tI_{2d}-C)
   =t^d\det((t+t^{-1})I_d-S)=P(t)
\]
first for \(t\ne0\), then as a polynomial identity.
The natural Gram on this same rank-\(2d\) lattice is
\[
 H=\operatorname{diag}(H_q,H_q).
 \tag{7}
\]
This is a positive product of two trace forms, not a replacement of the original field by a smaller characteristic polynomial.

For comparison only, the usual signed discriminants satisfy the already proved C243 identity
\[
 \operatorname{disc}P=(\operatorname{disc}q)^2q(2)q(-2).
 \tag{8}
\]
Since \(H_q=V^TV\), one has \(\det H_q=\operatorname{disc}q>0\), and hence
\[
 \det H=(\operatorname{disc}q)^2
       =\frac{|\operatorname{disc}P|}{|q(2)q(-2)|}.
 \tag{9}
\]
These are discriminants of the displayed polynomial orders, not silently substituted field discriminants.
If g is the greatest common divisor of the entries of \(H_q\), the primitive integral representative of the ray through H is \(H/g\), with determinant \((\operatorname{disc}q)^2/g^{2d}\).
Scalar normalization does not alter any adjoint or cost below.
No measure-discriminant inequality is used.

<a id="natural-trace-gram-price"></a>
## The natural Gram preserves the integer germ and forces a full-degree price

Use the H-adjoint
\[
 C^\dagger=H^{-1}C^TH.
\]
Equation (3) gives the exact integer formulas
\[
 C^\dagger=\begin{pmatrix}0&I_d\\-I_d&S\end{pmatrix},
 \qquad
 (C^\dagger)^{-1}=\begin{pmatrix}S&-I_d\\I_d&0\end{pmatrix}.
 \tag{10}
\]
Consequently
\[
 G_H(z)=\bigl(I-z(C^\dagger)^{-1}\bigr)(I-zC)^{-1}
       =I+zD+O(z^2),\qquad
 D=C-(C^\dagger)^{-1}=\operatorname{diag}(-S,S).
 \tag{11}
\]
The whole germ is integral, despite a possibly large Gram determinant.
Indeed, for any fixed integer C,
\[
 G_H(z)=I+\sum_{n\ge1}z^nD C^{n-1};
 \tag{12}
\]
thus integrality of this germ is equivalent to integrality of its first coefficient D.
Here (10)--(11) supply that condition exactly.
Since \(q(0)\ne0\), S and D are invertible, so the first positive nonzero coefficient occurs at index one and has rank \(2d\).

Let Q and U be any disk-holomorphic matrix functions with \(Q(0)\) invertible, \(U=G_HQ\) near zero, and
\[
 Q(z)^*H Q(z)\le H,\qquad U(z)^*H U(z)\le H.
 \tag{13}
\]
Set \(\tau=-\log|\det Q(0)|\).
Both inequalities in (13) hold throughout the open unit disk.
The matrix \(H_q^{1/2}SH_q^{-1/2}\) is real symmetric with eigenvalues \(s_i\).
Therefore the squared H-singular values of D in (11) are \(s_i^2\), each twice.
The adopted C868 v4 determinant estimate gives
\[
 \tau\ge\sum_{i=1}^d\log(1+s_i^2/4).
 \tag{14}
\]
Because
\[
 \prod_{i=1}^d s_i^2=q(0)^2\ge1,
\]
the same elementary convexity used in C868 v4 yields
\[
 \boxed{\displaystyle
 \tau\ge d\log\!\left(1+\frac{|q(0)|^{2/d}}4\right)
       \ge d\log(5/4).}
 \tag{15}
\]
This uses the actual complete spectrum and the integer norm \(q(0)\), not a small Gram determinant or a condition-number bound.
The price is not divided by d or by \(2d\).

For every fixed original P, finite-price realizations of (13) exist.
Put \(h(z)=\det(I-zC)\), and choose a sufficiently small real \(\eta>0\).
Then
\[
 Q=\eta h I_{2d},\qquad
 U=\eta\bigl(I-z(C^\dagger)^{-1}\bigr)\operatorname{adj}(I-zC)
 \tag{16}
\]
are polynomial matrices, satisfy \(U=G_HQ\) near zero, and have \(Q(0)=\eta I_{2d}\).
Their H-operator norms on the closed disk are finite, so scaling makes both at most one.
This verifies that the lower-cost statement is not based on an empty realization class.

For a proposed upper bound \(\tau\le C_{\rm tr}m(P)\), the actual input must therefore satisfy
\[
 d\log(5/4)\le C_{\rm tr}m(P).
 \tag{17}
\]
In particular this natural construction cannot have one uniform finite \(C_{\rm tr}\) on any actual family in this domain whose total measures stay bounded while d tends to infinity.
This is a conditional family exclusion; it does not assert an actual sequence of positive measures tending to zero.
Nor does (15) apply unchanged to a new germ formed after changing the adjoint metric.

<a id="real-block-metric-perturbation"></a>
## A positive real perturbation makes neutral blocks orthogonal

The map \(\operatorname{diag}(V,V)\), followed by a permutation of coordinates, identifies C with the direct sum of real blocks
\[
 C_s=\begin{pmatrix}0&-1\\1&s\end{pmatrix},
 \qquad s=s_i.
 \tag{18}
\]
For a real number b with \(|b|<1\), put
\[
 H_b(s)=\begin{pmatrix}1&b\\b&1\end{pmatrix}>0.
\]
A direct two-by-two computation gives
\[
 D_b(s):=C_s-(C_s^{\dagger_b})^{-1}
   =\frac{2b-s}{1-b^2}
       \begin{pmatrix}1&b\\-b&-1\end{pmatrix},
 \qquad C_s^{\dagger_b}=H_b(s)^{-1}C_s^TH_b(s).
 \tag{19}
\]
Moreover,
\[
 H_b(s)D_b(s)=(2b-s)\operatorname{diag}(1,-1),\qquad
 D_b(s)^2=\frac{(s-2b)^2}{1-b^2}I_2.
 \tag{20}
\]
Thus \(D_b(s)\) is self-adjoint in this positive metric, and its two squared metric singular values equal \((s-2b)^2/(1-b^2)\).

Choose
\[
 b(s)=
 \begin{cases}
 s/2,& |s|<2,\\
 2/s,& |s|>2.
 \end{cases}
 \tag{21}
\]
Both cases satisfy \(|b(s)|<1\).
For \(|s|<2\), direct multiplication gives \(C_s^TH_b(s)C_s=H_b(s)\), so
\[
 C_s^{\dagger_b}=C_s^{-1},\qquad D_b(s)=0.
 \tag{22}
\]
For \(|s|>2\), one instead has \(H_b(s)C_s=C_s^TH_b(s)\), so
\[
 C_s^{\dagger_b}=C_s,\qquad
 D_b(s)=C_s-C_s^{-1}
       =\begin{pmatrix}-s&-2\\2&s\end{pmatrix}.
 \tag{23}
\]
Thus the neutral blocks are orthogonal and the hyperbolic blocks are self-adjoint.
Each block, and hence their complete direct sum, is normal in its chosen positive real metric.

In the original basis (5), this real Gram is explicitly
\[
 H_{\rm real}
 =\begin{pmatrix}H_q&K\\K&H_q\end{pmatrix},
 \qquad
 K=V^T\operatorname{diag}(b(s_1),\ldots,b(s_d))V.
 \tag{24}
\]
It is positive because it is the pullback of the positive blocks above.
Every original trace root and both members of its reciprocal pair are retained.
Let \(\dagger_{\rm real}\) denote this adjoint, and form \(G_{\rm real}\) by (11) with that adjoint.
Then C is \(H_{\rm real}\)-normal, \(G_{\rm real}\) is the identity on every neutral block, and its first coefficient is \(C_s-C_s^{-1}\) on each hyperbolic block.

<a id="cheap-real-schur-realization"></a>
## An actual real-metric realization has total price exactly twice the original measure

First take a Salem polynomial of degree \(2d\ge4\).
Its roots are \(\beta,\beta^{-1}\), with \(\beta>1\), and \(2d-2\) roots on the unit circle.
On the two real eigendirections, normality gives the scalar germs
\[
 f_\lambda(z)=\frac{1-z/\lambda}{1-z\lambda},
 \qquad\lambda=\beta,\beta^{-1}.
 \tag{25}
\]
On every unit-circle eigendirection the germ is one, because the inverse of the adjoint eigenvalue is the original eigenvalue.

Put \(a=\beta^{-1}\in(0,1)\).
For the exterior eigendirection use
\[
 q_\beta(z)=\frac{a-z}{1-az},\qquad u_\beta(z)=a.
 \tag{26}
\]
For the interior eigendirection use
\[
 q_a(z)=a,\qquad u_a(z)=\frac{a-z}{1-az}.
 \tag{27}
\]
The scalar identities \(u_\lambda=f_\lambda q_\lambda\) follow by cancellation near zero.
The rational function \((a-z)/(1-az)\) is holomorphic in the disk and has modulus at most one there, since
\[
 |1-az|^2-|a-z|^2=(1-a^2)(1-|z|^2)\ge0.
\]
The constants a are also contractions.
On every neutral block take Q and U equal to the identity.

Conjugating C by \(H_{\rm real}^{1/2}\) gives a real normal matrix, which can be unitarily diagonalized.
Place (26)--(27) and the neutral identities on this diagonal and conjugate back.
This supplies actual disk-holomorphic Q and U satisfying (13) with \(H_{\rm real}\), and \(U=G_{\rm real}Q\) near zero.
Conjugation does not change \(\det Q(0)\).
Its only nonunit constant diagonal entries are the two copies of a, so
\[
 |\det Q(0)|=a^2,\qquad
 \boxed{\tau=2\log\beta=2m(P).}
 \tag{28}
\]
No limit, truncation or unproved matrix completion is used.

The same construction works for several hyperbolic trace roots and either sign of the real exterior root.
For a real exterior root \(\beta\) with \(|\beta|>1\), put \(a=\beta^{-1}\) and
\[
 b_a(z)=|a|\frac{1-z/a}{1-az}.
\]
This is a disk contraction with \(b_a(0)=|a|\), and \(f_\beta b_a=|a|\), while \(f_a|a|=b_a\).
Indeed, \(b_a=(|a|/a)(a-z)/(1-az)\), so the same modulus calculation applies for either real sign of a.
Each reciprocal pair therefore contributes \(2\log|\beta|\), and all neutral pairs contribute zero.
The complete original root formula retained in C243 gives
\[
 \tau=2\sum_{\text{exterior real pairs}}\log|\beta|=2m(P)
 \tag{29}
\]
for the whole all-real-trace domain in (1).
This is a true analytic price comparison, but its arithmetic eligibility remains to be checked.

<a id="cheap-real-first-coefficient-irrationality"></a>
## The exact arithmetic failure is already in the first coefficient

Assume now that P has both a hyperbolic reciprocal pair and a neutral pair.
This includes every Salem polynomial of degree at least four.
Let h be the number of hyperbolic trace roots, so \(1\le h<d\), and put
\[
 D_{\rm real}=C-(C^{\dagger_{\rm real}})^{-1}.
\]
Equations (22)--(23) show that \(D_{\rm real}\) is zero on all \(2(d-h)\) neutral eigendirections and invertible on each of the h hyperbolic two-dimensional blocks.
Consequently
\[
 D_{\rm real}\ne0,\qquad
 \operatorname{rank}D_{\rm real}=2h<2d.
 \tag{30}
\]
Since C is normal in this metric, it commutes with its adjoint and with the inverse adjoint.
Thus
\[
 D_{\rm real}C=CD_{\rm real}.
 \tag{31}
\]

Suppose for contradiction that \(D_{\rm real}\) were rational.
The rational matrix C has irreducible characteristic polynomial P and is cyclic.
Its rational centralizer is exactly \(\mathbb Q[C]\): choose a cyclic vector v, express any commuting operator's value at v uniquely as \(f(C)v\), with \(\deg f<2d\), and then commute with C on the whole cyclic basis.
Because P is irreducible, \(\mathbb Q[C]\cong\mathbb Q[t]/P\) is a field.
Every nonzero rational matrix commuting with C is therefore invertible.
This contradicts the nonzero singular matrix in (30).
Hence
\[
 \boxed{D_{\rm real}\notin M_{2d}(\mathbb Q).}
 \tag{32}
\]

The first coefficient of \(G_{\rm real}\) is exactly \(D_{\rm real}\), so its germ is not integral.
This is stronger than observing that a convenient diagonalizing matrix or the metric itself has irrational entries.
It identifies a necessary coefficient of the proposed original-input germ that fails rationality.

Nor does the ray through \(H_{\rm real}\) contain a positive integral Gram matrix.
If a positive scalar multiple were rational, its adjoint would equal the original adjoint, since scalar multiples cancel in \(H^{-1}C^TH\).
With C rational, that would make \(C^{\dagger_{\rm real}}\), its inverse and \(D_{\rm real}\) rational, contradicting (32).
Thus primitive integral normalization is unavailable for this cheap mixed-conjugate realization.

This centralizer mechanism is the same precise arithmetic obstruction used in C228, now applied to the actual first coefficient rather than only to the existence of a rational normalizing metric.
The neutral pair is essential.
A quadratic reciprocal polynomial with two real roots has no such neutral direction and does not satisfy the singularity premise of (30).
Likewise the proof does not apply when all trace roots are hyperbolic, or when all pairs are neutral and \(D_{\rm real}=0\).

<a id="rational-gram-perturbation-control"></a>
## Clearing a rational metric does not ensure an integer germ

A concrete interpolation keeps this remaining issue visible.
For rational \(\rho\) with \(|\rho|\max_i|s_i|<1\), take \(b(s)=\rho s\) instead of (21).
Then
\[
 H_\rho=
 \begin{pmatrix}H_q&\rho H_qS\\\rho H_qS&H_q\end{pmatrix}>0
 \tag{33}
\]
is rational and can be scaled to a positive integral Gram.
Writing \(\rho=a/b\) with integers \(b>0\), one such integral representative has determinant
\[
 \det\begin{pmatrix}bH_q&aH_qS\\aH_qS&bH_q\end{pmatrix}
   =(\operatorname{disc}q)^2
       \prod_{i=1}^d(b^2-a^2s_i^2).
 \tag{34}
\]
A primitive representative may divide out common content; no bound for that primitive determinant is supplied.

Equation (19) shows that the first coefficient of the resulting germ contains
\[
 (2\rho-1)S(I-\rho^2S^2)^{-1}
\]
on its first diagonal block, and \(\rho\) times that matrix multiplied by S on its first off-diagonal block.
These matrices are rational but need not be integral.
Scalar clearing of the Gram leaves the adjoint and these coefficients unchanged.

For an exact positive-measure control, take \(P=t^2-3t+1\), \(q=s-3\), and \(\rho=1/4\).
The corresponding primitive positive integral Gram and original integer C are
\[
 H_\rho^{\rm int}=\begin{pmatrix}4&3\\3&4\end{pmatrix},
 \qquad
 C=\begin{pmatrix}0&-1\\1&3\end{pmatrix}.
\]
The Gram determinant is seven, but direct inversion gives
\[
 C-(C^{\dagger_\rho})^{-1}
   =\frac17\begin{pmatrix}-24&-18\\18&24\end{pmatrix}.
 \tag{35}
\]
The germ fails integrality at its first coefficient, despite an actual positive integral Gram on the original lattice.
By (12), this is a decisive arithmetic failure of that particular interpolation.
It does not exclude every rational perturbation or prove a large-cost theorem for arbitrary positive integral metrics.

<a id="trace-gram-original-return"></a>
## What the comparison returns to the original task

The natural trace Gram gives an actual integer germ on the original order, but every compatible contraction realization pays at least \(d\log(5/4)\).
The piecewise positive real Gram gives actual disk contractions of total price \(2m(P)\), but on the mixed-conjugate irreducible domain its first nonzero coefficient is not even rational.
A rational interpolation can restore a primitive integral Gram while still losing the integer germ.

These findings distinguish the specific failed constructions.
They do not provide an arbitrary-metric lower bound, a positive-measure sequence tending to zero, a blanket exclusion of all trace-based methods, or a realization covering unrestricted G0001.
The unresolved requirement is one actual construction that simultaneously preserves the integer germ and supplies the necessary analytic price and arithmetic metric comparison.

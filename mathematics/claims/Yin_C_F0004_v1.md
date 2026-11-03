---
author: Yin
---

# All complex affine semicircular pencils: unrestricted positive-matrix infimum with a unique inner complex maximum; direct full MS24 recovery

## Current assessment
[Selected decision](#decision-finding-owned-review)

## A Positive-Matrix Infimum for Every Affine Semicircular Pencil

<a id="statement"></a>

<a id="yin_c_f0004"></a>
Record kind: authoritative statement and complete proof of [Yin_C_F0004](#decision-candidate-0004).
Date: 2026-09-13.
Author: yin_t_f0008-contract agent, in collaboration with root.
Goal: Yin_T_F0008.
The [selected assessment](#decision-candidate-0004) records the mathematical and review assessments, and the [independent audit](../audits/reviews/Yin_R_F0002_v1.md) records verification.
No mathematical Role is assigned.

This is an independent continuation of the signed Schur route.
The proof does not use Spe26 or Yin_C_F0082.
Root derived the general off-diagonal quadratic action, its strict concavity, and the final rescaling that removes regularization from the formula; this author derived the coercivity and positive Stein-equation argument that make every regularized critical point physical.
The earlier circular comparison proof motivated the continuation but is not a proof dependency.
A second agent checked the Stein and block-inverse algebra during development; that preliminary collaboration is distinct from a complete independent audit.

## Inputs and their scope

The analytic input is the physical matrix Dyson equation, its uniqueness in the appropriate half-plane, and the logarithmic primitive established in [Yin_C_F0002](Yin_C_F0002_v1.md#yin_c_f0002).
The [signed Schur factorization](../ledger/Yin_L_F0001_v1.md#signed-schur-linearization) supplies the relation to Yin_C_F0079's real-gap action.
The norm identity \(\|\Psi\|=\|\Psi(I)\|\) for a completely positive map is available in the [MS24 analytic dependency audit](../ledger/Yin_L_F0002_v1.md); below it is only used to sum a finite-dimensional positive-map geometric series.
The remaining arguments are finite-matrix differentiation, Schur inversion, polar decomposition, and scalar spectral calculus.
Neither the centered MS24 determinant equality nor Yin_C_F0078's identification with capacity is a premise.

Before this deduction, local Yin_C_F0002-Yin_C_F0079 records and external deterministic-equivalent literature were searched in the circular exploration.
That search found a related stationary logarithmic formula, but not a usable theorem proving the present free-matrix global minimum.
No novelty or priority claim follows from that bounded search.

## Setting and primary unregularized formula

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state, and let \(s_1,\ldots,s_n\) be free standard semicircular elements.
For arbitrary complex matrices \(a,a_1,\ldots,a_n\in M_m(\mathbb C)\), set
\[
 S=a\otimes1+\sum_{j=1}^n a_j\otimes s_j,
 \quad \eta(X)=\sum_ja_jXa_j^*,
 \quad \rho(X)=\sum_ja_jXa_j.
\]
The empty noise family is allowed.
Write \(\operatorname{tr}_m=\operatorname{Tr}/m\) and \(\varphi=\operatorname{tr}_m\otimes\tau\).
All finite traces and determinants in the optimization formulas below are unnormalized.

For every freely chosen positive definite \(R\in M_m(\mathbb C)\), put
\[
 H_R=I+\eta(R),\qquad
 \mathcal T_R(Y)=H_RYR^{-1}+\rho(Y^*),\qquad
 Z_R=\mathcal T_R^{-1}(a).
\]
This inverse always exists as a real-linear operator on all complex matrices, as proved below.
The determinant formula is
\[
 \Delta_\varphi(S)=e^{-1/2}\inf_{R>0}
   \left[\frac{\det(I+\eta(R))}{\det R}\right]^{1/(2m)}
   \exp\!\left[\frac1{2m}\operatorname{Re}\operatorname{Tr}(a^*Z_R)\right].
                                                            \tag{B}
\]
The infimum may be zero.
For the proof, define the logarithmic objective
\[
 \mathcal V(R)=\log\det H_R-\log\det R-m
                   +\operatorname{Re}\operatorname{Tr}(a^*Z_R).
\]
The equivalent logarithmic identity is
\[
 \log\Delta_\varphi(S)=\frac1{2m}\inf_{R>0}\mathcal V(R).
                                                            \tag{A}
\]
The extended-real value \(-\infty\) in (A) corresponds to \(\Delta(S)=0\) in (B).
The equation labels are retained for the existing proof and review references; (B) is the primary statement.
All positive definite matrices are admissible.
There is no remaining regularization parameter, Hilbert-Schmidt feasibility constraint, or prescribed Dyson solution in (A)-(B).
The finite real-linear solve defining \(Z_R\) is performed separately for each trial matrix.
General attainment is not asserted.
If \(S\) is boundedly invertible, the infimum is attained at \(R=E[(S^*S)^{-1}]\).

At \(a=0\), one has \(Z_R=0\) identically.
The elementary scaling \(R=tB\), \(t\to\infty\), then gives
\[
 \inf_{R>0}\frac{\det(I+\eta(R))}{\det R}
    =\inf_{B>0}\frac{\det\eta(B)}{\det B}
    =\operatorname{cap}(\eta).                              \tag{C}
\]
Thus (B) reduces directly to MS24 at its full original coefficient scope.
The proof below includes singular outputs and zero capacity.

## Regularized minimum used in the proof

Put
\[
 \log\Delta_\varepsilon(S)=\frac12\varphi\log(SS^*+\varepsilon^2I),
 \qquad\varepsilon>0.
\]
For every freely chosen \(Q>0\), define
\[
 C_Q=\varepsilon^2I+\eta(Q)>0,
 \qquad
 \mathcal L_Q(Y)=C_QYQ^{-1}+\rho(Y^*).                         \tag{1}
\]
The map \(\mathcal L_Q\) is a real-linear, positive definite, selfadjoint operator on \(M_m(\mathbb C)\), with real inner product \(\operatorname{Re}\operatorname{Tr}(X^*Y)\).
Hence
\[
 Y_Q=\mathcal L_Q^{-1}(a)                                   \tag{2}
\]
is a uniquely defined finite-matrix calculation for every trial \(Q>0\).
This is a real-linear solve; no complex-linearity of the term \(\rho(Y^*)\) is asserted.

Put
\[
 F_\varepsilon(Q)=\log\det C_Q-\log\det Q+\operatorname{Tr}Q-m
                  +\operatorname{Re}\operatorname{Tr}(a^*Y_Q).
                                                               \tag{3}
\]
Then
\[
 \boxed{
 \log\Delta_\varepsilon(S)
       =\frac1{2m}\min_{Q>0}F_\varepsilon(Q).
 }                                                          \tag{4}
\]
The minimum is attained uniquely, and its minimizer is
\[
 Q_0=\varepsilon^2E[(S^*S+\varepsilon^2I)^{-1}],
 \qquad E=\operatorname{id}\otimes\tau.                       \tag{5}
\]
Thus \(0<Q_0\le I\).
No Dyson equality, Hilbert-Schmidt superoperator inequality, or previously found optimizer is a constraint on the trial matrices in (4).

An equivalent expression with a freely chosen inner variable is
\[
 \begin{aligned}
 F_\varepsilon(Q)
 ={}&\log\det C_Q-\log\det Q+\operatorname{Tr}Q-m\\
 &+\max_{Y\in M_m(\mathbb C)}
 \left\{2\operatorname{Re}\operatorname{Tr}(a^*Y)
       -\operatorname{Tr}(Y^*C_QYQ^{-1})
       -\operatorname{Re}\operatorname{Tr}(Y^*\rho(Y^*))\right\}.
 \end{aligned}                                               \tag{6}
\]
The inner maximum is unique and is attained at (2).
It is taken before the outer minimum.
An exchange of extremum order is not claimed.

## The inner quadratic form is positive for every trial matrix

Define
\[
 B_Q(Y)=\operatorname{Tr}(Y^*C_QYQ^{-1})
                 +\operatorname{Re}\operatorname{Tr}(Y^*\rho(Y^*)).
\]
For \(Z_j=Q^{-1/2}Y^*a_jQ^{1/2}\), cyclicity and Hilbert-Schmidt Cauchy-Schwarz give
\[
 \left|\operatorname{Tr}(Y^*a_jY^*a_j)\right|
     =|\operatorname{Tr}(Z_j^2)|
     \le\operatorname{Tr}(Z_j^*Z_j)
     =\operatorname{Tr}(Y^*a_jQa_j^*YQ^{-1}).                  \tag{7}
\]
Summing (7) therefore yields
\[
 B_Q(Y)\ge\varepsilon^2\operatorname{Tr}(Y^*YQ^{-1})>0
       \quad\text{if }Y\ne0.                               \tag{8}
\]
The first term of \(\mathcal L_Q\) is selfadjoint for the complex Hilbert-Schmidt pairing.
The second is selfadjoint for its real part: expand the real bilinear form and use cyclicity in each summand containing \(a_j\).
Differentiating \(B_Q\) then gives \(2\mathcal L_Q(Y)\) with respect to that real pairing.
This proves all assertions surrounding (1), (2), and (6); at the maximum the quadratic expression equals \(\operatorname{Re}\operatorname{Tr}(a^*Y_Q)\).

In particular the maximum in (6) is nonnegative, by the trial \(Y=0\).
Since \(C_Q\ge\varepsilon^2I\),
\[
 F_\varepsilon(Q)
  \ge m\log\varepsilon^2-\log\det Q+\operatorname{Tr}Q-m.
                                                               \tag{9}
\]
Each scalar summand \(\lambda-\log\lambda\) tends to infinity both at zero and at infinity.
Hence every sublevel set of \(F_\varepsilon\) is contained in a compact subset of the positive cone.
The real-linear inverse in (2) depends smoothly on \(Q>0\), so \(F_\varepsilon\) is smooth and attains a global minimum in that cone.

## Every critical point has the required two signs

Let \(Q>0\) be any critical point, abbreviate \(C=C_Q\), \(Y=Y_Q\), and set
\[
 P=C^{-1}-YQ^{-1}Y^*.
\]
At this stage \(P\) is merely Hermitian.
Differentiating (6) in a Hermitian direction while holding the maximizing \(Y\) fixed is valid because its first variation vanishes.
The resulting gradient equation is
\[
 Q^{-1}=I+\eta^*(P)+Q^{-1}Y^*CYQ^{-1}.                       \tag{10}
\]
Here \(\eta^*(X)=\sum_ja_j^*Xa_j\).
The two differentiated quadratic terms contribute \(-\eta^*(YQ^{-1}Y^*)\) and \(+Q^{-1}Y^*CYQ^{-1}\); the pseudo-covariance term is independent of \(Q\) when \(Y\) is held fixed.

The following positive-map argument proves \(P>0\) without assuming it as a feasibility condition.
Define
\[
 U=C^{1/2}YQ^{-1/2},\qquad K=I-U^*U,\qquad W=I-UU^*,
\]
\[
 \Phi(X)=C^{-1/2}\eta(Q^{1/2}XQ^{1/2})C^{-1/2}.
\]
Then \(\Phi\) is completely positive and
\[
 \Phi(I)=I-\varepsilon^2C^{-1}<I,
 \qquad
 P=C^{-1/2}WC^{-1/2}.
\]
Congruence of (10) by \(Q^{1/2}\) gives exactly
\[
 K=Q+\Phi^*(W).                                             \tag{11}
\]
Choose a unitary extension of the polar factor of the square matrix \(U\), so that \(U=V|U|\).
Such an extension exists even when \(U\) is singular because the two complementary kernel dimensions agree.
Then \(W=VKV^*\).
Set
\[
 \Lambda(X)=\Phi^*(VXV^*).
\]
This is completely positive, and its adjoint satisfies
\[
 \Lambda^*(I)=V^*\Phi(I)V<I.
\]
The completely positive map norm identity gives \(\|\Lambda^*\|<1\) for the norm induced by the ordinary matrix operator norm.
Thus the spectral radius of \(\Lambda\) is strictly below one.
Equation (11) consequently has the norm-convergent expansion
\[
 K=(I-\Lambda)^{-1}(Q)=\sum_{k=0}^\infty\Lambda^k(Q)>0.       \tag{12}
\]
The first term is already positive definite and every other term is positive semidefinite.
Hence \(W>0\) and
\[
 P>0.                                                       \tag{13}
\]
This argument concerns the actual finite-dimensional spectral radius of \(\Lambda\); it does not identify complete positivity with positivity of its Hilbert-Schmidt quadratic form.
The strictness comes from the positive regularization.

## Identification with the physical Dyson solution

Construct
\[
 q=\begin{pmatrix}P&Y\\Y^*&-Q\end{pmatrix}.
\]
Its Schur complement relative to \(-Q\) is \(P+YQ^{-1}Y^*=C^{-1}>0\), so it is invertible.
Its inverse is
\[
 q^{-1}=
 \begin{pmatrix}
 C&CYQ^{-1}\\
 Q^{-1}Y^*C&-Q^{-1}+Q^{-1}Y^*CYQ^{-1}
 \end{pmatrix}.                                             \tag{14}
\]
Let
\[
 A=\begin{pmatrix}\varepsilon^2I&a\\a^*&-I\end{pmatrix},
 \quad B_j=\begin{pmatrix}0&a_j\\a_j^*&0\end{pmatrix},
 \quad\Theta(X)=\sum_jB_jXB_j,
\]
and put \(\widetilde\rho(X)=\sum_ja_j^*Xa_j^*\).
Explicitly,
\[
 \Theta\begin{pmatrix}X&Y\\Z&W\end{pmatrix}
   =\begin{pmatrix}\eta(W)&\rho(Z)\\
              \widetilde\rho(Y)&\eta^*(X)\end{pmatrix}.       \tag{15}
\]
Equations (2), (10), and (14) show \(q^{-1}=A-\Theta(q)\).
No uniqueness at an unregularized real spectral parameter is being assumed.
Instead form
\[
 \mathcal R=\begin{pmatrix}i\varepsilon P&Y\\Y^*&iQ/\varepsilon\end{pmatrix}.
                                                               \tag{16}
\]
Its imaginary part is \(\operatorname{diag}(\varepsilon P,Q/\varepsilon)>0\) by (13).
Direct block multiplication using (14) gives
\[
 \mathcal R^{-1}=H_a-\Theta(\mathcal R)-i\varepsilon I_{2m},
 \qquad H_a=\begin{pmatrix}0&a\\a^*&0\end{pmatrix}.           \tag{17}
\]
Thus \(-\mathcal R\) is exactly the Yin_C_F0002 physical solution for the hermitization \(H_S=\left(\begin{smallmatrix}0&S\\S^*&0\end{smallmatrix}\right)\) at \(i\varepsilon\).
The sign of its imaginary part selects this solution uniquely.
In particular
\[
 \mathcal R=E[(H_S-i\varepsilon I)^{-1}],
\]
which identifies the lower-right block with (5) and the upper-left block with \(E[(SS^*+\varepsilon^2I)^{-1}]\).
Every critical point has this same \(Q\) and \(Y\).
Combined with existence from (9), this proves that there is exactly one critical point and that it is the unique global minimizer.
No convexity of the reduced objective is asserted.

## Value and normalization

Write
\[
 b_\rho=\operatorname{Re}\operatorname{Tr}(Y^*\rho(Y^*)).
\]
The Schur determinant in (14) and the elementary diagonal factors changing \(q\) into \(\mathcal R\) give
\[
 |\det\mathcal R|=|\det q|=\det(C^{-1})\det Q.
\]
Indeed \(\mathcal R=\operatorname{diag}(i\sqrt\varepsilon I,\varepsilon^{-1/2}I)\,q\, \operatorname{diag}(\sqrt\varepsilon I,-i\varepsilon^{-1/2}I)\), and both diagonal factors have determinant of modulus one.
Direct multiplication in (15) gives
\[
 \tfrac12\operatorname{Re}\operatorname{Tr}(\Theta(\mathcal R)\mathcal R)
     =-\operatorname{Tr}(P\eta(Q))+b_\rho.                   \tag{18}
\]
The Yin_C_F0002 primitive with the normalized \(2m\)-dimensional trace therefore yields
\[
 2m\log\Delta_\varepsilon(S)
   =\log\det C-\log\det Q-\operatorname{Tr}(P\eta(Q))+b_\rho.
                                                               \tag{19}
\]
On the other hand, (2) and the trace of (10) multiplied by \(Q\) give
\[
 \operatorname{Re}\operatorname{Tr}(a^*Y)
   =\operatorname{Tr}(Y^*CYQ^{-1})+b_\rho,
\]
\[
 m=\operatorname{Tr}Q+\operatorname{Tr}(P\eta(Q))
                         +\operatorname{Tr}(Y^*CYQ^{-1}).
\]
Substitution in (3) identifies its minimum with the right side of (19), proving (4) with the stated factor \(1/(2m)\).

## The signed Schur action and its extremum order

There is also an explicit positive/negative Schur formulation closer to the Yin_C_F0079 action.
For freely chosen \(P_s,Q>0\) and \(Y\in M_m(\mathbb C)\), put
\[
 q(P_s,Q,Y)=
 \begin{pmatrix}P_s-YQ^{-1}Y^*&Y\\Y^*&-Q\end{pmatrix}.        \tag{20}
\]
It has \(m\) positive and \(m\) negative eigenvalues.
Substitution into
\[
 -\log|\det q|+\operatorname{Tr}(Aq)
                   -\tfrac12\operatorname{Tr}(q\Theta(q))-2m
\]
gives
\[
 \begin{aligned}
 \mathcal A_\varepsilon(P_s,Q,Y)
 ={}&-\log\det P_s-\log\det Q
       +\operatorname{Tr}(P_sC_Q)+\operatorname{Tr}Q-2m\\
   &+2\operatorname{Re}\operatorname{Tr}(a^*Y)
       -\operatorname{Tr}(Y^*C_QYQ^{-1})
       -\operatorname{Re}\operatorname{Tr}(Y^*\rho(Y^*)).
 \end{aligned}                                               \tag{21}
\]
For fixed \(P_s,Q\), (8) gives the unique inner maximum over \(Y\).
For each \(Q\), the remaining minimum over \(P_s\) is attained uniquely at \(P_s=C_Q^{-1}\), and its value is (3).
Thus
\[
 \boxed{
 \log\Delta_\varepsilon(S)
  =\frac1{2m}\min_{P_s,Q>0}\max_{Y\in M_m(\mathbb C)}
                          \mathcal A_\varepsilon(P_s,Q,Y).
 }                                                          \tag{22}
\]
The maximum comes first.
Both positive variables and the complex off-diagonal variable are free trial matrices.
Positivity of the upper-left block in (20) emerges at the optimizer from (11)-(13), rather than being silently imposed or inferred from inertia alone.

The centered signed Schur pencil \(\left(\begin{smallmatrix}\varepsilon^2I&S\\S^*&-I\end{smallmatrix}\right)\) is indefinite even when all coefficients of \(S\) are selfadjoint.
Formula (22) therefore links the selfadjoint indefinite target to the general complex-coefficient target through one proved mechanism.
It is not Yin_C_F0082's Hilbert-Schmidt feasibility condition in renamed coordinates.

## Rescaling removes the regularization parameter

For each \(\varepsilon>0\), make the positive-cone bijection \(Q=\varepsilon^2R\).
Then
\[
 C_Q=\varepsilon^2(I+\eta(R))=\varepsilon^2H_R,
 \qquad C_QYQ^{-1}=H_RYR^{-1}.
\]
Thus the inner real-linear solve becomes exactly \(\mathcal T_R(Z_R)=a\), independently of \(\varepsilon\).
Both factors of \(\varepsilon^{2m}\) cancel from the determinant ratio, and
\[
 F_\varepsilon(\varepsilon^2R)
       =\mathcal V(R)+\varepsilon^2\operatorname{Tr}R.        \tag{23}
\]
In particular \(\mathcal T_R\) is the already proved positive definite operator \(\mathcal L_R\) at \(\varepsilon=1\), so its inverse exists for every \(R>0\).

Let \(c=\inf_{R>0}\mathcal V(R)\), allowing \(c=-\infty\).
Equation (23) implies
\[
 \inf_R(\mathcal V(R)+\varepsilon^2\operatorname{Tr}R)\ge c.
\]
For every fixed \(R>0\), its left side is at most \(\mathcal V(R)+\varepsilon^2\operatorname{Tr}R\), whose limit is \(\mathcal V(R)\).
Taking the limit and then the infimum over fixed trials proves
\[
 \lim_{\varepsilon\downarrow0}
       \inf_{R>0}(\mathcal V(R)+\varepsilon^2\operatorname{Tr}R)
       =\inf_{R>0}\mathcal V(R),                             \tag{24}
\]
including \(-\infty\).
Scalar spectral calculus gives \(\log\Delta_\varepsilon(S)\downarrow\log\Delta(S)\).
Combining (4), (23), and (24) proves (A), and exponentiation proves (B).
This is a justified limit after a scale-dependent change of trial variable; it is not the generally invalid operation of substituting zero into the original fixed-\(Q\) objective.

## Direct MS24 reduction and bounded-inverse attainment

When \(a=0\), strict positivity of \(\mathcal T_R\) makes \(Z_R=0\) for every trial \(R\).
For each \(R>0\), determinant monotonicity gives
\[
 \frac{\det(I+\eta(R))}{\det R}
     \ge\frac{\det\eta(R)}{\det R}\ge\operatorname{cap}(\eta).
\]
Conversely, for each fixed \(B>0\),
\[
 \frac{\det(I+\eta(tB))}{\det(tB)}
     =\frac{\det(t^{-1}I+\eta(B))}{\det B}
     \longrightarrow\frac{\det\eta(B)}{\det B}
     \quad(t\to\infty).
\]
Taking an infimum over \(B\) proves (C), even if \(\eta(B)\) is singular or capacity is zero.
Formula (B) therefore becomes
\[
 \Delta\!\left(\sum_ja_j\otimes s_j\right)
      =e^{-1/2}\operatorname{cap}(\eta)^{1/(2m)}.              \tag{25}
\]
This is the original MS24 coefficient scope and normalization.
The pseudo-covariance drops out because the mean is zero, not because it was omitted from the affine problem.
No special Dyson optimizer or positive-capacity assumption enters this reduction.

If \(S\) is boundedly invertible, the minimizers in the rescaled problem satisfy
\[
 R_\varepsilon=\varepsilon^{-2}Q_0
      =E[(S^*S+\varepsilon^2I)^{-1}]
      \longrightarrow R_*=E[(S^*S)^{-1}]>0.
\]
The convergence is in matrix norm, and \(\varepsilon^2\operatorname{Tr}R_\varepsilon\to0\).
Continuity of \(\mathcal V\), (23), and convergence of the regularized determinant prove \(\mathcal V(R_*)=2m\log\Delta(S)\).
Hence the direct infimum is attained at \(R_*\).
The inner optimizer tends to
\[
 Z_{R_*}=E[(SS^*)^{-1}S]=E[(S^*)^{-1}].
\]
We make no general uniqueness claim for the unregularized infimum.
In the strictly positive selfadjoint regime of Yin_C_F0079, these variables become \(R_*=E[S^{-2}]\) and \(Z_{R_*}=E[S^{-1}]\).
In particular the new positive trial variable is not the square of the older inverse expectation; an expectation does not preserve that product.

For the deterministic case \(\eta=\rho=0\), one has \(Z_R=aR\) and \(\mathcal V(R)=-\log\det R-m+\operatorname{Tr}(Ra^*a)\).
If \(a\) is invertible its minimum is \(\log\det(a^*a)\), attained at \(R=(a^*a)^{-1}\).
If \(a\) is singular, scaling on its kernel makes the infimum \(-\infty\).
This checks (A) in both deterministic cases without assuming normality of \(a\).

If \(\rho=0\), the inner solve is explicit:
\[
 Z_R=(I+\eta(R))^{-1}aR,
\]
and the direct one-variable objective is
\[
 \mathcal V(R)=\log\det(I+\eta(R))-\log\det R-m
               +\operatorname{Tr}(Ra^*(I+\eta(R))^{-1}a).
\]
This recovers the circular case after the same rescaling, with no remaining regularization parameter.

## Scope, historical tests, and review boundary

This module supplies a direct infimum over all positive definite matrices for every affine complex-coefficient semicircular pencil, including zero determinant, and a unique minimum for every positive regularization.
The direct zero-mean simplification is (C)/(25), and bounded invertibility gives the stated unregularized attainment result.
It does not assert general unregularized attainment or uniqueness, a Brown-support/spectrum equality, or a particular regularization convergence rate.
Those are separate questions if selected by the goal contract.

Before the positive Stein argument was found, a numerical search used NumPy seed 913006, 60 random size-two full complex coefficient families with one to four coefficients, regularizations in \(\{0.07,0.2,0.7,1.5\}\), and six positive-matrix optimization starts per family.
Each inner maximizer was computed by an eight-dimensional real-linear solve.
The candidate value at the physical point matched the Yin_C_F0002 primitive within \(10^{-6}\), and no lower trial value was found; the smallest discrepancy was approximately \(-6.22\times10^{-15}\).
These calculations are historical motivation and are not used as proof evidence.

The previous circular module retains its Jensen comparison as an independent proof for that restricted case.
The general proof here instead uses existence of a minimum and the positive Stein equation to identify every critical point.
The coordinating agent must obtain a complete audit of this assembled artifact before recording an independently reviewed result.


## Assessment history


### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#the-inner-quadratic-form-is-positive-for-every-trial-matrix) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact material](Yin_C_F0004_v1.md) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0002_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original review classification and limitations: independently reviewed; collaborative derivation disclosed; proof independent of Spe26/Yin_C_F0082

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

### Decision candidate-0004

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-09-28T02:52 |
| status | proved |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#the-inner-quadratic-form-is-positive-for-every-trial-matrix) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact material](Yin_C_F0004_v1.md) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0002_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:14 |
| status | proved |
| reason | Select the actual complete finding and distinct later presentation finding with their known contributor/shared-context relationships, preserving the exact mathematical statement, both argument locators and assessment. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#the-inner-quadratic-form-is-positive-for-every-trial-matrix) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact material](Yin_C_F0004_v1.md) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Complete signed-Schur finding](../audits/reviews/Yin_R_F0002_v1.md#general-signed-schur-finding) | Actual complete original argument review with known shared mathematical context, retained source and unregularized-scope limits; no new independent review. |
| review | [Determinant-first presentation finding](../audits/reviews/Yin_R_F0007_v1.md#determinant-presentation-finding) | Original later contributor self-review of the determinant-first reordering and zero-determinant equivalence, without extending its scope to a whole-proof review. |

## Historical assessments


These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

Original review classification and limitations: independently reviewed; collaborative derivation disclosed; proof independent of Spe26/Yin_C_F0082

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0002_v1.md).

Material covered by that review: [Exact material](Yin_C_F0004_v1.md).

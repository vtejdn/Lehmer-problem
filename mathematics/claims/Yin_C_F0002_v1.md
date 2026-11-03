---
author: Yin
---

# Exact affine Dyson determinant functional and monotone scalar infimum; ordinary covariance alone is insufficient

## Current assessment
[Selected decision](#decision-finding-scopes)

## Affine Semicircular Determinants

<a id="statement"></a>

<a id="yin_c_f0002"></a>
## Yin_C_F0002: Exact Affine Formula and the Missing Covariance Information

Record kind: project deduction and exploration record.
Date: 2026-09-12.
Owner: root.
Authorization: the user asked for the simplest exact affine extension of the MS24 determinant/capacity identity and explicitly prohibited network searches for this exploration.
This record follows that restriction and uses local source files and existing audits only.
No claim of novelty or priority is made.

This is a new deduction for the user-assigned question, not extraction of a lemma from an existing project Claim and not designation of a main theorem.
The [selected assessment](#decision-finding-scopes) records the mathematical status and exact argument/review selections; the [main contributor review](../audits/reviews/Yin_R_F0001_v1.md#scope-of-the-passed-review) and [monotonicity author check](../audits/reviews/Yin_R_F0006_v1.md#monotonicity-self-review) retain their distinct scopes.
The centered input is [MS24-U003](../audits/literature/MS24/Yin_U003.md#ms24-u003).
This question does not change the contracts of the existing boundedness goals.

### Setting and exact statement

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state, and let \(s_1,\ldots,s_n\in M\) be freely independent standard semicircular elements.
Allow \(n=0\) for the deterministic case.
Let \(m\geq1\), \(a_0,\ldots,a_n\in M_m(\mathbb C)\), and
\[
 S=a_0\otimes1+\sum_{j=1}^n a_j\otimes s_j\in M_m(M).
\]
The coefficient matrices need not be selfadjoint.
All operator determinants use \(\varphi_m=\operatorname{tr}_m\otimes\tau\), where \(\operatorname{tr}_m=\operatorname{Tr}_m/m\), and include zero atoms in the logarithmic integral.
See the [audited determinant convention](../audits/literature/MS24/Yin_U001.md#determinant-convention).

Set \(d=2m\), and form finite selfadjoint matrices
\[
 A=\begin{pmatrix}0&a_0\\a_0^*&0\end{pmatrix},
 \qquad
 B_j=\begin{pmatrix}0&a_j\\a_j^*&0\end{pmatrix},
 \qquad
 \Theta(R)=\sum_{j=1}^n B_jRB_j
 \quad(R\in M_d(\mathbb C)).
\]
For each \(\varepsilon>0\), there exists exactly one \(G_\varepsilon\in M_d(\mathbb C)\) satisfying
\[
 \boxed{\quad
 G_\varepsilon^{-1}=i\varepsilon I_d-A-\Theta(G_\varepsilon),
 \qquad \operatorname{Im}G_\varepsilon<0.
 \quad}                                                    \tag{1}
\]
The strict inequality is negative definiteness of \((G_\varepsilon-G_\varepsilon^*)/(2i)\).
It is the condition selecting the resolvent solution; an arbitrary algebraic solution at \(\varepsilon=0\) is not an equivalent substitute.

Define the following finite-dimensional functional for this record:
\[
 \boxed{\quad
 \mathcal C_{\mathrm{aff}}(a_0;a_1,\ldots,a_n)
 =
 \lim_{\varepsilon\downarrow0}
 \frac{\exp\!\left[-\frac12\operatorname{Re}
                    \operatorname{Tr}_d(AG_\varepsilon)\right]}
      {|\det G_\varepsilon|}.
 \quad}                                                     \tag{2}
\]
The limit exists in \([0,\infty)\), and
\[
 \boxed{\quad
 \Delta_{\varphi_m}(S)
 =e^{-1/2}\mathcal C_{\mathrm{aff}}(a_0;a_1,\ldots,a_n)^{1/(2m)}.
 \quad}                                                     \tag{3}
\]
No injectivity, flatness, irreducibility, spectral gap, or positive-capacity hypothesis is imposed.
A zero limit gives zero determinant.

The symbol \(\mathcal C_{\mathrm{aff}}\) is local notation for (2), not an attribution of a standard generalized capacity from the literature.
Formula (2) is defined by finite matrices and the unique solution of (1), independently of the operator determinant.
This argument does not establish that (2) is the infimum of a positive-matrix optimization problem.

For zero drift,
\[
 \mathcal C_{\mathrm{aff}}(0;a_1,\ldots,a_n)
 =\operatorname{cap}\!\left(b\mapsto\sum_j a_jba_j^*\right).
                                                               \tag{4}
\]
Thus (3) has the same normalization and exponent as MS24.
However, for arbitrary complex coefficients the affine determinant cannot be determined from \(a_0\) and the map \(\eta(b)=\sum_j a_jba_j^*\) alone.
The explicit counterexample below is part of the scope of this Claim.

## Local Inputs and Search Boundary

Before derivation, the existing MS24 determinant, scaling and analytic dependency audits and relevant local records were inspected.
The local [MS17 book](../literature/pdf/MS17.pdf) supplies the operator-valued semicircular cumulant and Cauchy-transform interfaces:

- Chapter 9, Definition 10 and Theorem 11(1), (2), (4), printed p. 239 / PDF p. 248, especially equation (9.20).
- Proposition 13, printed pp. 241-242 / PDF pp. 250-251, for matrix/scalar cumulant compatibility.
- Equation (9.5), printed p. 231 / PDF p. 240, and the continuation discussion on printed p. 232 / PDF p. 241.

The assigned analytic reviewer extracted these passages and visually checked PDF p. 248.
The existing [MS24 analytic supplement](../ledger/Yin_L_F0002_v1.md) supplies the tracial spectral, hermitization and semicircular moment conventions.

The logarithmic formula below is derived explicitly from that Dyson equation.
Its form is a stationary Dyson action, but no unverified outside attribution or global extremum theorem is imported.
The user's offline restriction leaves any broader literature/priority comparison for another authorized round.

## The Full Covariance Retained by Hermitization

Let
\[
 H=\begin{pmatrix}0&S\\S^*&0\end{pmatrix}
   =A\otimes1+\sum_j B_j\otimes s_j
   \in M_d(M),
 \qquad E=\operatorname{id}_{M_d(\mathbb C)}\otimes\tau.
\]
Then \(H=H^*\).
In addition to \(\eta\), set
\[
 \rho(b)=\sum_j a_jba_j,\qquad
 \widetilde\rho(b)=\sum_j a_j^*ba_j^*,
 \qquad \eta^*(b)=\sum_j a_j^*ba_j.
\]
Direct block multiplication gives
\[
 \Theta\begin{pmatrix}p&q\\r&t\end{pmatrix}
 =
 \begin{pmatrix}
   \eta(t)&\rho(r)\\
   \widetilde\rho(q)&\eta^*(p)
 \end{pmatrix}.                                               \tag{5}
\]
Here \(\eta^*\) is the Hilbert-Schmidt adjoint.
These formulas are complete definitions; no familiarity with the optional term “pseudo-covariance” is required.

At \(a_0=0\), the matrix expectation of the resolvent at \(i\varepsilon\) is block diagonal: centered semicircular sign symmetry makes the off-diagonal blocks vanish.
With drift, the off-diagonal information in (5) generally participates in equation (1).
This explains why the centered formula can forget \(\rho\), while its affine extension cannot.

## Resolvent Existence and Pointwise Uniqueness

For \(z\) in the open upper half-plane, define
\[
 G(z)=E[(zI_d-H)^{-1}].
\]
It is analytic and has strictly negative imaginary part.
Indeed, writing \(v=\operatorname{Im}z>0\),
\[
 -\operatorname{Im}G(z)
 =vE[((z-H)^*(z-H))^{-1}]>0;
\]
a positive scalar lower bound follows from boundedness of \(H\).
Hence \(G(z)\) is invertible.

The local operator-valued cumulant rule gives first cumulant \(A\), second cumulant \(\Theta\), and no higher cumulants, so
\[
 G(z)^{-1}=zI_d-A-\Theta(G(z)).                                \tag{6}
\]
Equivalently, this can be read directly from the noncrossing-pairing recursion for the moments \(Q_k=E[H^k]\):
\[
 Q_0=I_d,\qquad
 Q_k=AQ_{k-1}+
       \sum_{\substack{r,s\geq0\\r+s=k-2}}\Theta(Q_r)Q_s
 \quad(k\geq1),
\]
where the sum is empty for \(k=1\).
The convergent large-\(|z|\) series \(G(z)=\sum_{k\geq0}Q_kz^{-k-1}\) satisfies (6), and analyticity extends the identity throughout the upper half-plane.
The deterministic insertion order is retained in this recursion.

There is an elementary uniqueness proof at every \(z=i\varepsilon\), so no separate uniqueness theorem is needed.
Suppose \(G_1,G_2\) solve (1) and put \(V_j=-\operatorname{Im}G_j>0\).
Taking imaginary parts of the inverse relation gives both identities
\[
 V_j=G_j(\varepsilon I_d+\Theta(V_j))G_j^*
     =G_j^*(\varepsilon I_d+\Theta(V_j))G_j.                    \tag{7}
\]
The difference \(D=G_1-G_2\) satisfies
\[
 D=G_1\Theta(D)G_2.
\]
Put \(W=V_1^{-1/2}DV_2^{-1/2}\) and
\[
 L_i=V_1^{-1/2}G_1B_iV_1^{1/2},\qquad
 R_i=V_2^{1/2}B_iG_2V_2^{-1/2}.
\]
Then
\[
 W=\sum_iL_iWR_i,\qquad
 \sum_iL_iL_i^*<I_d,\qquad \sum_iR_i^*R_i<I_d,
\]
where strictness follows from the \(\varepsilon\)-terms in (7).
The row/column operator norm inequality yields
\[
 \|W\|\leq
 \left\|\sum_iL_iL_i^*\right\|^{1/2}
 \left\|\sum_iR_i^*R_i\right\|^{1/2}\|W\|,
\]
with coefficient strictly below one.
Thus \(W=0\), proving uniqueness.
When \(n=0\), the sum is empty and the same conclusion is immediate.

## A Finite-Dimensional Primitive of the Cauchy Transform

Because \(B_i=B_i^*\), the covariance is symmetric for the **bilinear** trace pairing:
\[
 \operatorname{Tr}_d(\Theta(X)Y)
 =\operatorname{Tr}_d(X\Theta(Y)).
                                                               \tag{8}
\]
No adjoint is inserted in this identity.

Since \(G(z)\) is invertible and the upper half-plane is simply connected, choose an analytic logarithm of \(\det G(z)\) using the asymptotic \(G(z)\sim z^{-1}I_d\).
Define
\[
 F(z)=-\frac1d\log\det G(z)
       +\frac1{2d}\operatorname{Tr}_d(\Theta(G(z))G(z)).          \tag{9}
\]
Differentiating (6) and multiplying under the trace gives
\[
 \operatorname{Tr}_dG
 =-\operatorname{Tr}_d(G^{-1}G')
   +\operatorname{Tr}_d(\Theta(G)G').
\]
Together with (8), this proves \(F'(z)=\operatorname{tr}_dG(z)\).

On the other hand,
\[
 L(z)=(\operatorname{tr}_d\otimes\tau)\Log(zI_d-H)
\]
has the same derivative by scalar spectral calculus.
Both \(F(z)\) and \(L(z)\) are \(\log z+o(1)\) as \(z=iR\), \(R\to\infty\), so
\[
 F(z)=L(z).                                                   \tag{10}
\]
This argument fixes the additive constant; stationarity alone would not.

For
\[
 \Delta_\varepsilon(S)
 =\exp\!\left[\frac12\varphi_m
                    \log(S^*S+\varepsilon^2I_m)\right],
\]
the two diagonal blocks of \(H^2\) have the same normalized spectral distribution.
Taking real parts of (10) at \(i\varepsilon\) therefore gives
\[
 \boxed{\quad
 \log\Delta_\varepsilon(S)
 =-\frac1{2m}\log|\det G_\varepsilon|
  +\frac1{4m}\operatorname{Re}\operatorname{Tr}_d
                     (\Theta(G_\varepsilon)G_\varepsilon).
 \quad}                                                       \tag{11}
\]
This identity is exact for every \(\varepsilon>0\).
Truncated spectral integration gives \(\Delta_\varepsilon(S)\downarrow\Delta(S)\), including the value zero.

## Recovering the Capacity-Shaped Expression

Taking the trace of (6) times \(G_\varepsilon\) gives
\[
 \operatorname{Tr}_d(\Theta(G_\varepsilon)G_\varepsilon)
 =\operatorname{Tr}_d((i\varepsilon I_d-A)G_\varepsilon)-2m.
\]
Thus, if \(K_\varepsilon\) denotes the expression inside the limit in (2),
\[
 K_\varepsilon
 =e^m\Delta_\varepsilon(S)^{2m}
   \exp\!\left[-\frac12\operatorname{Re}
                      \operatorname{Tr}_d(i\varepsilon G_\varepsilon)\right].
                                                               \tag{12}
\]
Let \(\mu_H\) be the scalar probability spectral measure of \(H\).
Then
\[
 0\leq
 \operatorname{Re}\operatorname{Tr}_d(i\varepsilon G_\varepsilon)
 =d\int_{\mathbb R}\frac{\varepsilon^2}{x^2+\varepsilon^2}
                     \,d\mu_H(x)
 \leq d.                                                       \tag{13}
\]
If \(\Delta(S)>0\), the measure has no zero atom, so (13) tends to zero by dominated convergence.
Equation (12) then tends to \(e^m\Delta(S)^{2m}\).
If \(\Delta(S)=0\), the exponential in (12) is between \(e^{-m}\) and one, so the same zero limit follows.
This proves existence of (2) and identity (3) in all cases.

The omission of the \(i\varepsilon G_\varepsilon\) term is justified **after** this limit argument.
Expression (2) without its limit is not the exact regularized identity.

When \(a_0=0\), (2) becomes \(\lim_{\varepsilon\downarrow0}|\det G_\varepsilon|^{-1}\).
Combining (3) with the audited centered MS24 identity proves (4), including zero capacity.
This use of MS24 identifies the centered limit; it is not a premise of the derivation of (11)-(12).

## Explicit Obstruction to Using Only the Original Covariance

Let \(m=n=1\), \(a_0=t>2\), and let \(s\) be a standard semicircular element.
The two operators
\[
 S_1=t+s,\qquad S_2=t+is
\]
have the same constant and the same entire covariance map \(\eta(b)=b\).
Strict scalar Jensen gives
\[
 \log\Delta(S_1)=\tau\log(t+s)<\log t,
\]
whereas
\[
 \log\Delta(S_2)=\frac12\tau\log(t^2+s^2)>\log t.
\]
Both strict inequalities follow because the semicircular law is nonconstant.
Thus no function of \((a_0,\eta)\) alone can give the general affine determinant.
The missing maps in (5) are \(\rho=\widetilde\rho=\operatorname{id}\) for \(S_1\) and \(-\operatorname{id}\) for \(S_2\).

For a numerical-free exact check inside the support, take \(a_0=1\).
The elementary semicircular potential is
\[
 U(z)=\int_{\mathbb R}\log|z-x|\,d\mu_{\rm sc}(x)
     =-\log|g(z)|+\frac12\operatorname{Re}g(z)^2,\qquad
 g(z)=\frac{z-\sqrt{z^2-4}}2,                                  \tag{14}
\]
with the branch \(g(z)\sim z^{-1}\).
The formula follows by differentiation from \(g+g^{-1}=z\) and matching \(\log|z|\) at infinity.
On the interval \([-2,2]\), the continuous boundary value gives \(U(x)=x^2/4-1/2\).
Consequently
\[
 \log\Delta(1+s)=-\frac14,\qquad
 \log\Delta(1+is)
 =\log\frac{1+\sqrt5}{2}-\frac{3-\sqrt5}{4}>0.                  \tag{15}
\]
No circular Brown-measure theorem is needed for this obstruction.

Treating \(a_0\) as one additional Kraus coefficient would give the same augmented capacity for these examples and therefore fails.
A second check is deterministic noise: when all \(a_j=0\) for \(j\geq1\), the answer is \(|\det a_0|^{1/m}\), so using the augmented ordinary capacity with the unchanged factor \(e^{-1/2}\) already gives a wrong constant.

## Basic Checks and Simpler Cases

1. **Pure constant.**
   If \(a_0\) is invertible and \(n=0\), then \(G_\varepsilon=(i\varepsilon I_d-A)^{-1}\), \(G_0=-A^{-1}\), and
   \[
   \mathcal C_{\mathrm{aff}}=e^m|\det a_0|^2.
   \]
   Formula (3) gives precisely \(|\det a_0|^{1/m}\).
   A singular \(a_0\) gives zero by (12).

2. **One semicircular variable.**
   If \(n=1\) and \(a_1\) is invertible, let \(\lambda_1,\ldots,\lambda_m\) be the eigenvalues of \(a_1^{-1}a_0\), counted with algebraic multiplicity.
   The abelian spectral model of \(s\) gives
   \[
   \log\Delta(a_0+a_1\otimes s)
   =\frac1m\log|\det a_1|
     +\frac1m\sum_{j=1}^m U(-\lambda_j).
   \]
   This follows from integrating the ordinary determinant of \(a_0+xa_1\); normality of \(a_1^{-1}a_0\) is unnecessary.

3. **Selfadjoint coefficients.**
   If all \(a_j=a_j^*\), including \(a_0\), the same primitive proof can be carried out directly in \(M_m(\mathbb C)\) using \(g_\varepsilon^{-1}=i\varepsilon I_m-a_0-\eta(g_\varepsilon)\), \(\operatorname{Im}g_\varepsilon<0\).
   The smaller formula is
   \[
   \log\Delta(S)
   =\lim_{\varepsilon\downarrow0}
       \left[-\frac1m\log|\det g_\varepsilon|
             +\frac1{2m}\operatorname{Re}
                       \operatorname{Tr}_m(\eta(g_\varepsilon)g_\varepsilon)
       \right].
   \]
   Hermitization is what allows the arbitrary complex-coefficient statement.

These checks concern exact formulas, not finite random-matrix approximation or numerical certificates.

## What Remains Open in This Exploration

The exact finite-dimensional formula is established above.
A comparably simple **optimization** formula such as the original \(\inf_{b>0,\det b=1}\det\eta(b)\) has not been established here.

The natural action is stationary at the Dyson solution, but the algebraic equation alone has other boundary branches.
Already for the scalar shifted semicircle, \(g^{-1}=z-g\) has two real roots for \(z>2\); the resolvent selects the small root.
Its continuation inside the support is nonreal.
Therefore an unrestricted infimum or supremum of the real action cannot be asserted merely from its critical-point equation.
Condition (1) supplies the checked selection rule.

This result also gives no spectral gap or inverse \(L^2\) estimate.
No extension to arbitrary operator families is claimed.
A future search may identify existing names or sharper variational formulations, but no network search was performed in this round.

<a id="determinant-only-form"></a>
## Equivalent Form Using a Single Matrix Determinant

Added 2026-09-12 at the user's request to combine the exponential trace and normalized root.
This is an algebraic rewriting of Yin_C_F0002, with no new hypothesis, Claim or optimization assertion.
The exploration remains offline.

For any complex square matrix \(X\), triangularization gives \(\det(e^X)=e^{\operatorname{Tr}X}\), hence \(\lvert\det(e^X)\rvert=e^{\operatorname{Re}\operatorname{Tr}X}\).
By multiplicativity of the ordinary determinant, equation (2) becomes
\[
 \mathcal C_{\mathrm{aff}}
 =\lim_{\varepsilon\downarrow0}
   \left|\det\!\left(G_\varepsilon^{-1}
                         e^{-AG_\varepsilon/2}\right)\right|.
                                                               \tag{16}
\]
Consequently, a version of (3) containing a single ordinary determinant is
\[
 \boxed{\quad
 \Delta_{\varphi_m}(S)
 =\lim_{\varepsilon\downarrow0}
   \left|\det\!\left(
       G_\varepsilon^{-1}e^{-(I_d+AG_\varepsilon)/2}
   \right)\right|^{1/d},\qquad d=2m.
 \quad}                                                        \tag{17}
\]
The factor \(e^{-1/2}\) has been absorbed as the scalar matrix \(e^{-1/2}I_d\).
Only the identity matrix is commuted inside the exponential; no commutation of \(A\) and \(G_\varepsilon\) is required, and no matrix logarithm or fractional-power branch is chosen.

On \(M_d(\mathbb C)\) with normalized trace, \(\Delta_{\operatorname{tr}_d}(T)=|\det T|^{1/d}\).
Using that same determinant convention on both sides gives the more compact form
\[
 \boxed{\quad
 \Delta_{\varphi_m}(S)
 =\lim_{\varepsilon\downarrow0}
   \Delta_{\operatorname{tr}_d}\!\left(
      G_\varepsilon^{-1}e^{-(I_d+AG_\varepsilon)/2}
   \right).
 \quad}                                                        \tag{18}
\]
The scalar quantities inside these limits agree exactly with the rewritten expression (3) for every positive \(\varepsilon\).
As with (3), this does not identify them with the regularized determinant \(\Delta_\varepsilon(S)\) before taking the limit.
Equations (17)-(18) require convergence only of the determinant values, not of the matrices themselves, and retain the zero-determinant case.

<a id="monotonicity-and-scalar-infimum"></a>
## Monotonicity and the Difference Between Two Infima

Added 2026-09-12 in response to the user's question whether the limit differs substantively from the infimum in ordinary capacity.
The following refinement of Yin_C_F0002 proves that its determinant values are monotone, so the limit can itself be written as an infimum.
It does not supply an unconstrained positive-matrix variational principle.
The derivation uses only the preceding proof and elementary spectral calculus, with no network search.

Put \(Q=S^*S\in M_m(M)\), retain the normalized tracial state \(\varphi_m\), and define for \(\varepsilon>0\)
\[
 F(\varepsilon)
 =\Delta_{\operatorname{tr}_d}\!\left(
       G_\varepsilon^{-1}e^{-(I_d+AG_\varepsilon)/2}
   \right)=e^{-1/2}K_\varepsilon^{1/d}>0,
 \qquad d=2m.
\]
Equations (12)-(13), and equality of the normalized spectral distributions of the two diagonal blocks of \(H^2\), give the exact identity
\[
 \log F(\varepsilon)
 =\frac12\varphi_m\!\left(
     \log(Q+\varepsilon^2I_m)
       -\varepsilon^2(Q+\varepsilon^2I_m)^{-1}
   \right).                                                   \tag{19}
\]
At any fixed positive \(\varepsilon\), the spectral integrands and their derivatives are uniformly bounded on the compact spectrum of Q, locally uniformly in \(\varepsilon\).
Differentiation under the spectral integral is therefore legitimate.
The two first-order resolvent terms cancel, leaving
\[
 \frac{d}{d\varepsilon}\log F(\varepsilon)
 =\varepsilon^3\varphi_m\!\left((Q+\varepsilon^2I_m)^{-2}\right)
 >0.                                                          \tag{20}
\]
Strict positivity also follows directly from \((Q+\varepsilon^2I_m)^{-2}\geq(\|Q\|+\varepsilon^2)^{-2}I_m\).
Thus F is strictly increasing on \((0,\infty)\).
Together with (18), this proves
\[
 \boxed{\quad
 \Delta_{\varphi_m}(S)
 =\inf_{\varepsilon>0}
   \Delta_{\operatorname{tr}_d}\!\left(
       G_\varepsilon^{-1}e^{-(I_d+AG_\varepsilon)/2}
   \right).
 \quad}                                                       \tag{21}
\]
Likewise, \(K_\varepsilon=e^{d/2}F(\varepsilon)^d\) is strictly increasing, and
\[
 \mathcal C_{\mathrm{aff}}
 =\inf_{\varepsilon>0}
   \left|\det\!\left(G_\varepsilon^{-1}e^{-AG_\varepsilon/2}\right)\right|.
                                                               \tag{22}
\]
These infima are approached only as \(\varepsilon\downarrow0\); none is attained at a positive parameter.
This includes singular Q and zero determinant.
For example, Q=0 gives \(F(\varepsilon)=e^{-1/2}\varepsilon\), consistent with (19)-(20).

The remaining distinction from ordinary capacity is structural.
The source definition \(\operatorname{cap}(\eta)=\inf_{b>0}\det\eta(b)/\det b\) allows every positive definite matrix b as a trial point.
In (21)-(22), each trial value instead requires the unique solution of the Dyson equation at that parameter.
The feasible matrices form the prescribed one-parameter family \(G_\varepsilon\), not the entire positive cone.
Both infima give upper bounds at trial values; ordinary capacity can also have a positive definite minimizer, whereas strict monotonicity precludes an interior minimizer for the regularization parameter here.

Consequently the symbols lim and inf are interchangeable in Yin_C_F0002, but this monotonicity result does not resolve the earlier open question of a comparably direct matrix optimization formula.
No nonexistence assertion about such a formula is made.
The earlier open-boundary discussion concerns that matrix variational problem, not the scalar infimum now proved.


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
| argument | [Exact material](#resolvent-existence-and-pointwise-uniqueness) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact material](#monotonicity-and-scalar-infimum) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0001_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |
| review | [Exact material](../audits/reviews/Yin_R_F0006_v1.md#monotonicity-self-review) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original review classification and limitations: main identity independently reviewed, preliminary collaboration disclosed; monotonicity refinement self-reviewed

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
| argument | [Exact material](#resolvent-existence-and-pointwise-uniqueness) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact material](#monotonicity-and-scalar-infimum) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0001_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |
| review | [Exact material](../audits/reviews/Yin_R_F0006_v1.md#monotonicity-self-review) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-scopes

| Field | Value |
| --- | --- |
| date | 2026-10-20T21:19 |
| status | proved |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact affine statement](#statement) | Unchanged affine semicircular determinant identity with arbitrary complex matrix coefficients and zero determinants; ordinary covariance alone is insufficient. |
| argument | [Complete main argument](#resolvent-existence-and-pointwise-uniqueness) | Equations (1)-(15), resolved recorded local tracial and source inputs, uniqueness, logarithmic normalization, singular limit and covariance counterexample. |
| argument | [Determinant form](#determinant-only-form) | Equations (16)-(18), with determinant values converging and no premature regularized identity. |
| argument | [Monotone scalar infimum](#monotonicity-and-scalar-infimum) | Equations (19)-(22), positive-parameter derivative and constrained one-parameter infima, including zero determinant; no unrestricted positive-matrix optimization. |
| review | [Main contributor review](../audits/reviews/Yin_R_F0001_v1.md#scope-of-the-passed-review) | Actual 2026-09-12 complete main-argument check, with the reviewer's primitive/uniqueness contributions disclosed as self-review; no independent acceptance is inferred. |
| review | [Notation checks](../audits/reviews/Yin_R_F0001_v1.md#review-of-the-determinant-notation-addendum) | Actual same-date determinant notation checks (16)-(18); combined author checks and another agent's rereading, without an isolated-context independence claim. |
| review | [Monotonicity author check](../audits/reviews/Yin_R_F0006_v1.md#monotonicity-self-review) | Actual 2026-09-12 self-review only of refinement (19)-(22), preserving its normalization, derivative sign, singular endpoints and scalar-versus-matrix optimization limits. |

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

Original review classification and limitations: main identity independently reviewed, preliminary collaboration disclosed; monotonicity refinement self-reviewed

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0001_v1.md); [Exact material](../audits/reviews/Yin_R_F0006_v1.md#monotonicity-self-review).

Material covered by that review: [Exact material](Yin_C_F0002_v1.md).

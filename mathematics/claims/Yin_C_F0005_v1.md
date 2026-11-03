---
author: Yin
---

# The Yin_C_F0004 infimum is attained exactly for boundedly invertible pencils, with unique minimizer; nonattainment detects the full operator spectrum

## Current assessment
[Selected decision](#decision-isolated-review-20261022)

## Attainment of the Affine Positive-Matrix Infimum

<a id="yin_c_f0005"></a>
Record kind: project deduction and spectral-interface record.
Date: 2026-09-13.
Author: indefinite-variation agent, with root independently identifying the stationary Stein equation and its possible spectral consequence.
Goal: Yin_T_F0008.
Registered as [Yin_C_F0005](#yin_c_f0005); the [selected assessment](#decision-isolated-review-20261022) owns the current assessment, and the [original attainment finding](../audits/reviews/Yin_R_F0010_v1.md#historical-affine-attainment) retains its 2026-09-13 verification.
This continues the independent [general signed-Schur formula](Yin_C_F0004_v1.md).
It does not use Spe26 or Yin_C_F0082.
No mathematical Role is assigned.

## Reuse Check and Exact New Interface

The equivalence between an existing square-integrable rational inverse and a bounded inverse is already available in [Yin_C_F0001](Yin_C_F0001_v1.md#yin_c_f0001), including finite matrix pencils in semicircular generators.
That result uses the audited [Miy26 rational-\(L^2\) theorem](../audits/literature/Miy26/Yin_U002.md#miy26-u002).
The more general Yin_C_F0049 also covers mixed free-Poisson/semicircular models, but is not needed here.
We do not re-register or claim to discover that spectral criterion.

The new interface proved below is that attainment of the general positive-matrix determinant infimum is equivalent to bounded invertibility of the affine pencil, and its minimizer is unique.
A finite critical point is itself a certificate for an actual gap in the hermitized spectrum.
This proof uses the physical Dyson uniqueness from Yin_C_F0002 and the analytic-gap criterion already verified in [Yin_C_F0003](Yin_C_F0003_v1.md).
The \(L^2\) restatement is then a direct reuse of Yin_C_F0001.

## Statement

Let
\[
 S=a+\sum_{j=1}^n a_j\otimes s_j\in M_m(M),
 \qquad \eta(X)=\sum_j a_jXa_j^*,\qquad
 \rho(X)=\sum_j a_jXa_j,
\]
with arbitrary complex coefficient matrices and free standard semicircular variables, including the empty noise family.
Use the faithful normalized trace \(\varphi=\operatorname{tr}_m\otimes\tau\).
For \(R>0\), define
\[
 H_R=I+\eta(R),\qquad
 Y_R=(Y\mapsto H_RYR^{-1}+\rho(Y^*))^{-1}(a)
\]
as the uniquely solvable real-linear equation in the general formula, and put
\[
 \mathcal V_a(R)=\log\det H_R-\log\det R-m
                      +\operatorname{Re}\operatorname{Tr}(a^*Y_R).
                                                               \tag{1}
\]
The following conditions are equivalent:

1. The infimum of \(\mathcal V_a\) over all \(R>0\) is attained.
2. The function \(\mathcal V_a\) has a critical point in that domain.
3. \(S\) has a bounded everywhere-defined inverse in \(M_m(M)\).

When these hold, the critical point and minimizer are unique and are
\[
 R_* = E((S^*S)^{-1}),\qquad
 Y_{R_*}=E((S^*)^{-1}),\qquad E=\operatorname{id}\otimes\tau.
                                                               \tag{2}
\]
By the existing Yin_C_F0001 criterion, these conditions are also equivalent to existence of an affiliated inverse \(S^{-1}\in L^2(M_m(M),\varphi)\).
The latter equivalence is reused, not independently claimed as a new rational-boundedness result.

## What a Critical Point Forces

The inner quadratic maximum defining \(Y_R\) is strictly concave for each positive trial \(R\), by the covariance Cauchy--Schwarz argument in the general formula.
Its optimizer depends smoothly on \(R\).
Thus \(\mathcal V_a\) is smooth, and the envelope derivative at a critical point gives
\[
 R^{-1}=\eta^*(P)+R^{-1}Y^*H_RYR^{-1},
 \qquad
 P=H_R^{-1}-YR^{-1}Y^*,\qquad Y=Y_R.                       \tag{3}
\]
There is no identity term on the right of (3), because the unregularized objective has no linear term \(\operatorname{Tr}R\).

Define
\[
 U=H_R^{1/2}YR^{-1/2},\quad
 K=I-U^*U,\quad W=I-UU^*,
\]
\[
 \Phi(X)=H_R^{-1/2}\eta(R^{1/2}XR^{1/2})H_R^{-1/2}.
\]
Then \(P=H_R^{-1/2}WH_R^{-1/2}\), and (3) becomes
\[
 K=\Phi^*(W).                                               \tag{4}
\]
The square matrix \(U\) has a polar decomposition \(U=V|U|\) with a unitary extension \(V\), even if \(U\) is initially singular.
Hence \(W=VKV^*\).
The map \(\Lambda=\Phi^*\operatorname{Ad}V\) is completely positive, and
\[
 \Lambda^*(I)=V^*\Phi(I)V
           =V^*(I-H_R^{-1})V<I.
\]
Its spectral radius is strictly less than one by the norm identity for a completely positive map, applied to its adjoint.
Equation (4) says \(K=\Lambda(K)\), so \(K=0\).
Consequently \(U\) is unitary, \(W=P=0\), and \(Y\) is invertible.

The identity \(U^*U=I\) and the inner equation now simplify to
\[
 R=Y^*(I+\eta(R))Y,\qquad
 a=Y^{-*}+\rho(Y^*),\qquad Y^{-*}=(Y^*)^{-1}.              \tag{5}
\]
These are consequences of an arbitrary finite critical point.
They do not yet identify it with the physical inverse, which is the next obligation.

## A Positive Stability Certificate on the Full Hermitization

Let
\[
 \mathcal T_R(X)=Y^*\eta(X)Y.
\]
Equation (5) supplies the positive strict defect
\[
 R-\mathcal T_R(R)=Y^*Y>0.
\]
Similarity by \(R^{1/2}\) makes this completely positive map strictly subunital, so its spectral radius is less than one.
Its adjoint is \(\eta^*\operatorname{Ad}Y\).
Because \(Y\) is invertible, the map \(\mathcal T_P=\operatorname{Ad}Y\,\eta^*\) is similar to that adjoint and also has spectral radius less than one.
Therefore
\[
 P_0=(I-\mathcal T_P)^{-1}(YY^*)
       =\sum_{k\ge0}\mathcal T_P^k(YY^*)>0                 \tag{6}
\]
is a well-defined finite positive matrix.

Hermitize the original pencil:
\[
 \mathscr H=\begin{pmatrix}0&S\\S^*&0\end{pmatrix}
       =A+\sum_jB_j\otimes s_j,\quad
 A=\begin{pmatrix}0&a\\a^*&0\end{pmatrix},\quad
 B_j=\begin{pmatrix}0&a_j\\a_j^*&0\end{pmatrix},
 \quad \Theta(X)=\sum_jB_jXB_j.
\]
Set
\[
 G_0=-\begin{pmatrix}0&Y\\Y^*&0\end{pmatrix}=G_0^*.
\]
The second equation in (5), and its adjoint, are exactly
\[
 G_0^{-1}=-A-\Theta(G_0).                                  \tag{7}
\]
The full matrix-space map \(\mathcal S=\operatorname{Ad}G_0\,\Theta\) is completely positive.
Equations (5)--(6) give a positive strict subinvariant matrix on that full space:
\[
 Z=\operatorname{diag}(P_0,R)>0,\qquad
 Z-\mathcal S(Z)=\operatorname{diag}(YY^*,Y^*Y)=G_0^2>0.
                                                               \tag{8}
\]
Thus \(r(\mathcal S)<1\).
No inference from a block restriction to the full spectrum is needed: (8) proves the full contraction by a direct positive-definite matrix.

## The Certificate Selects the Actual Spectral Gap

Apply the finite-dimensional holomorphic implicit-function theorem to
\[
 G^{-1}=zI-A-\Theta(G)
\]
at \((z,G)=(0,G_0)\).
Multiplication of its linearized equation by \(G_0\) on both sides reduces invertibility of the derivative to \(I-\mathcal S\), which is invertible by (8).
There is a unique analytic branch \(g(z)\) near zero with \(g(0)=G_0\).
Differentiating gives
\[
 g'(0)=-(I-\mathcal S)^{-1}(G_0^2)=-Z<0.                   \tag{9}
\]
The last equality follows from (8).
Since the data are selfadjoint, uniqueness also gives \(g(\bar z)=g(z)^*\).

For sufficiently small positive \(\varepsilon\), equation (9) implies \(\operatorname{Im}g(i\varepsilon)=-\varepsilon Z+O(\varepsilon^2)<0\).
The Yin_C_F0002 half-plane uniqueness theorem therefore identifies \(g(i\varepsilon)\) with the actual physical Cauchy transform \(E((i\varepsilon-\mathscr H)^{-1})\).
The identity theorem identifies the analytic functions throughout a small upper half-disk.
The branch continues across its real interval with selfadjoint values.
The Yin_C_F0003 Stieltjes-inversion argument then gives an actual gap in the scalar spectral measure of \(\mathscr H\), and faithfulness identifies that gap with the operator spectrum.

Thus \(\mathscr H\) is boundedly invertible.
Since \(\mathscr H^2=\operatorname{diag}(SS^*,S^*S)\), the original \(S\) is boundedly invertible.
This proves condition 2 implies condition 3.
The proof excludes nonphysical algebraic branches rather than simply calling any real Dyson solution a gap.

## Attainment and Uniqueness

If \(S\) is boundedly invertible, the unique regularized minimizers from the general formula, after its rescaling, satisfy
\[
 R_\varepsilon=E((S^*S+\varepsilon^2I)^{-1})\longrightarrow R_*,
\qquad
 Y_\varepsilon=E((SS^*+\varepsilon^2I)^{-1}S)
                 \longrightarrow E((S^*)^{-1})
\]
in finite-matrix norm.
The limit \(R_*>0\).
Continuity of (1) and the regularized minimum identity show that it attains the unregularized infimum.
This is also the bounded-invertibility attainment argument already written in the main general-formula module.
Every attained minimum is a critical point because the domain is open.
This establishes all three implications.

To see uniqueness, any critical point has just been identified with an actual spectral gap and the analytic physical branch.
The value at zero gives \(Y=E((S^*)^{-1})\).
Moreover
\[
 g'(0)=-E(\mathscr H^{-2})
 =-\operatorname{diag}\big(E((SS^*)^{-1}),E((S^*S)^{-1})\big).
\]
Comparison with (9) identifies its bottom block with the candidate \(R\), proving \(R=R_*\).
Thus there is at most one critical point and exactly one minimizer whenever the infimum is attained.

## Existing \(L^2\) Criterion and a Variational Spectrum Test

Yin_C_F0001 applies to the present matrix pencil in a finite semicircular family, including complex coefficients: its entries are polynomial, hence matrix rational, and its inverse, whenever affiliated, stays in the corresponding matrix rational ring.
That result says precisely that an existing \(L^2\) inverse is bounded.
Conversely bounded inverses are square integrable in a finite tracial algebra.
This supplies the \(L^2\) equivalence in the statement without reproducing the stronger rational theorem.

For \(T=\sum_j a_j\otimes s_j\), use \(a=-zI\) in (1).
Then
\[
 z\notin\sigma(T)
 \quad\Longleftrightarrow\quad
 \inf_{R>0}\mathcal V_{-zI}(R)\ \hbox{is attained}.          \tag{10}
\]
Thus failure of attainment detects the full operator spectrum, not only the support of its Brown measure.
The feasible cone remains independent of \(z\); only the inner source matrix changes.

The canonical regularized minimizing matrices give a related exact boundary test:
\[
 z\in\sigma(T)
 \quad\Longleftrightarrow\quad
 \|E(((T-z)^*(T-z)+\varepsilon^2I)^{-1})\|
                       \longrightarrow\infty.             \tag{11}
\]
Indeed the matrices increase as \(\varepsilon\downarrow0\).
Their normalized trace tends to the squared \(L^2\) norm of the affiliated inverse, with infinity assigned when there is a kernel.
Bounded trace in finite matrix size is equivalent to bounded matrix norm; Yin_C_F0001 then identifies it with the resolvent condition.
At a point in the spectrum, the canonical minimizing sequence therefore escapes to infinity.
It stays uniformly away from the zero boundary, since it is bounded below by \((\|T-z\|^2+1)^{-1}I\) for \(0<\varepsilon\le1\).

## Relation to the Positive-Pencil Variable in Yin_C_F0079

If \(S>0\), Yin_C_F0079 uses \(q=E(S^{-1})\).
The minimizer here is instead
\[
 R_*=E(S^{-2}).
\]
These are different finite matrices.
With selfadjoint coefficients, \(Y=q=q^*\), and (5) becomes
\[
 R_*=q^2+q\eta(R_*)q.                                      \tag{12}
\]
Equivalently \(R_*\) is the derivative at zero of \(E((S-tI)^{-1})\).
Equation (12) is the same derivative/stability equation already appearing in the positive-pencil proof.
The new attainment statement extends the spectral interpretation to arbitrary complex affine pencils; it does not identify \(R_*\) with \(q\) or equate the two variational domains.

This complete proof has passed the independent review linked above.
The existing rational \(L^2\) criterion and Stieltjes-gap interface are explicitly reused; new content is their connection to finite critical points, unique attainment and escape of the minimizing matrices in the independent determinant formula.
No Brown-support/spectrum equality, convergence rate or formal verification is claimed.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:32 |
| status | proved |
| reason | Select the exact retained finding with its actual relationship and original mathematical scope. The statement, argument, status, original review date and historical decisions remain unchanged; no new whole-proof review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#a-positive-stability-certificate-on-the-full-hermitization) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact argument](#existing-l2-criterion-and-a-variational-spectrum-test) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact review](../audits/reviews/Yin_R_F0010_v1.md#historical-affine-attainment) | Complete arbitrary-complex-coefficient attainment equivalence, unique critical point/minimizer, full-space stability and physical gap, rational-L2 and full-spectrum tests, canonical sequence and positive-pencil comparison; no Brown-support equality. |


### Decision isolated-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:33 |
| status | proved |
| reason | Adopt the newly performed isolated complete attainment inspection completed at 2026-10-22T20:28; the fixed arbitrary-complex-coefficient proof, existing L2 interface and precise spectral boundaries are unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete attainment/critical-point/bounded-inverse equivalence and unique matrices, including empty noise and the existing affiliated-L2 restatement. |
| argument | [Critical-point equation](#what-a-critical-point-forces) | Smooth inner solve, envelope derivative and the finite critical point's stationary identities. |
| argument | [Full-space stability and physical gap](#a-positive-stability-certificate-on-the-full-hermitization) | Entire positive strict full-hermitization certificate and following analytic branch selection and genuine operator-gap argument. |
| argument | [Attainment and uniqueness](#attainment-and-uniqueness) | Regularized limiting attainment and physical value/derivative identification of every critical point. |
| argument | [L2, spectrum and comparison](#existing-l2-criterion-and-a-variational-spectrum-test) | Existing-inverse rational-L2 interface, full-spectrum/canonical-sequence tests and the following positive-pencil variable comparison. |
| review | [Isolated whole finding](../audits/reviews/Yin_R_F0010_v1.md#current-affine-attainment) | Actual 2026-10-22 independent whole inspection of all specified mathematics and necessary C_F0004/C_F0077/C_F0003/C_F0001/C_F0079 interfaces, without Brown-support equality or broader external source audits. |

## Historical assessments


<a id="decision-candidate-0004"></a>
### Historical assessment candidate-0004

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T02:52 |
| status | proved |
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#a-positive-stability-certificate-on-the-full-hermitization) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact material](#existing-l2-criterion-and-a-variational-spectrum-test) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0010_v1.md#historical-affine-attainment) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).



<a id="decision-candidate-0002"></a>
### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#a-positive-stability-certificate-on-the-full-hermitization) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact material](#existing-l2-criterion-and-a-variational-spectrum-test) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0010_v1.md#historical-affine-attainment) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original review classification and limitations: independently reviewed; stationary-equation collaboration disclosed; existing Yin_C_F0001 L2 criterion reused

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).



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

Original review classification and limitations: independently reviewed; stationary-equation collaboration disclosed; existing Yin_C_F0001 L2 criterion reused

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Original review finding, dated 2026-09-13: [retained same historical finding](../audits/reviews/Yin_R_F0010_v1.md#historical-affine-attainment).
Its relocation does not substitute the new 2026-10-22 review into earlier decisions.

Material covered by that review: [Exact material](Yin_C_F0005_v1.md).

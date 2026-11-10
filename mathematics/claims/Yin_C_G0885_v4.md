---
author: Yin
---

# Bounded-word Mahler gaps and complete four-factor exterior tests

<a id="statement"></a>
## Exact statements and retained scope

Let \(H\) be a positive definite symmetric integral Gram matrix of rank \(g\ge1\), and let
\[
L=H\oplus U,\qquad e^2=f^2=0,\quad(e,f)=1.
\]
Extend \(R\in O(H,\mathbb Z)\) to fix \(e,f\).
For every integral \(v\) of even squared norm, write
\[
E_v(x)=x-(v,x)e+(e,x)v-\tfrac12(v,v)(e,x)e
\]
and define \(F_v\) by exchanging \(e,f\).
All norms and inner products below use \(H\) on its positive summand.

The [adopted v3 bounded-word theorem](Yin_C_G0885_v3.md#decision-bounded-word-bounded-norm-gap) is retained unchanged.
For each fixed integer \(k\ge1\) and real \(B\ge1\), all words with at most \(k\) such transvections of squared norm at most \(B\), and arbitrary intervening positive integral isometries, satisfy
\[
m(P_A)=0\quad\hbox{or}\quad m(P_A)\ge\eta(k,B)>0.          \tag{1}
\]
Its rank, lattice, determinant, isometry-order and parameter uniformity, zero and dependent parameters, empty positive summand, and presentation-level sequence conclusion retain exactly their v3 scope.
The separate absolute gap \(\eta_*>0\) for at most three transvections without a norm bound is also retained.

For the new four-factor statements, put
\[
A=R E_vF_wE_uF_t,\qquad P_A(z)=\det(zI-A),\qquad
\chi_R(z)=\det(zI-R).                                    \tag{2}
\]
The parameters may be zero or linearly dependent.
For a real inner-product space, vectors \(a,b\) and a subspace \(W\), define
\[
\mathcal D(a,b\mid W)
=\|a_\perp\|\|b_\perp\|-(a_\perp,b_\perp),                \tag{3}
\]
where \(a_\perp,b_\perp\) are their orthogonal projections to \(W^\perp\).
This is a nonnegative real number and is defined even when \(W\) or either projection is zero.

Fix any real \(z>1\), and put
\[
\widehat q=(zI-R)^{-1}q\quad(q\in H_{\mathbb R}).
\]
Each of the following conditions forces the complete polynomial \(P_A\) to have a real root at least \(z\), and therefore forces \(M(P_A)\ge z\):
\[
\mathcal D(\widehat t,\widehat v\mid
                  \operatorname{span}_{\mathbb R}\{\widehat u,\widehat w\})
                    \ge \frac1z,                       \tag{4}
\]
or the more directly checkable condition
\[
\mathcal D(t,v\mid\operatorname{span}_{\mathbb R}\{u,w\})
                    \ge \frac{(z+1)^2}{z}.              \tag{5}
\]
In particular, \(M(P_A)<6/5\) requires
\[
\mathcal D(t,v\mid\operatorname{span}\{u,w\})<121/30.     \tag{6}
\]
These conditions hold also for each of the four twisted cyclic presentations
\[
\sigma^j(v,w,u,t),\qquad 0\le j<4,\qquad
\sigma(v,w,u,t)=(R^{-1}t,v,w,u),                         \tag{7}
\]
which have the same complete characteristic polynomial after the indicated integer conjugacy and cusp exchange.
Neither (4) nor (5) is asserted to be necessary for a large root, and their failure is not a small-measure certificate.

For permitted parameters \(p,q\) in the positive lattice, also define the integer cusp defect
\[
\kappa(p,q)=1-(p,q)+\tfrac14(p,p)(q,q).                  \tag{8}
\]
It is nonnegative.
If either parameter is zero, it equals one.
For nonzero even-norm integral parameters,
\[
\kappa(p,q)=0
\quad\Longleftrightarrow\quad p=q,\quad (p,p)=2.          \tag{9}
\]
If the middle pair of any presentation in (7) has zero cusp defect, the complete word is integrally conjugate to one with at most two transvections at the original two cusps, allowing a cusp exchange.
It therefore has the retained absolute gap \(\eta_*\), independently of the other parameter norms.
A zero parameter gives the same conclusion by the existing at-most-three reduction.

More generally, for every real \(K\ge0\) and nonzero permitted \(p,q\),
\[
\kappa(p,q)\le K
\quad\Longrightarrow\quad
(p,p),(q,q)\le 2(1+\sqrt K)^2.                           \tag{10}
\]
Thus bounded cusp defects for the two disjoint pairs \((v,w)\), \((u,t)\) imply the bounded-norm gap (1), with a constant depending only on \(K\).
These are restricted conclusions, not an absolute gap for all four-factor words or an effective exclusion of every \(1<M<6/5\) input.

<a id="argument"></a>
## Complete new argument and inherited input

The full proof of (1), its source interfaces and its separate short-word assertion remain in [v3](Yin_C_G0885_v3.md#argument), with [R1114 v9](../audits/reviews/Yin_R_G1114_v9.md#bounded-word-bounded-norm-review).
The new deductions below use only the actual transvection formulas, real positive orthogonality, full characteristic determinants and the [addition and covariance identities](../ledger/Yin_L_G0462_v14.md#short-word-reduction).
No new external theorem, numerical root calculation or mathematical program is used.

<a id="four-scalar-determinant"></a>
### A four-by-four determinant for the entire characteristic polynomial

Set
\[
(q_1,q_2,q_3,q_4)=(t,u,w,v),\qquad
K_R(z)=(zI-R)^{-1}R,\qquad
Q_{ij}=(q_i,q_j).
\]
Define the lower-triangular matrix \(L_Q\) by
\[
(L_Q)_{ii}=Q_{ii}/2,\qquad
(L_Q)_{ij}=Q_{ij}\ (i>j),\qquad
(L_Q)_{ij}=0\ (i<j),
\]
and define \(F(z)_{ij}=(q_i,K_R(z)q_j)\).
Finally put
\[
J(z)=
\begin{pmatrix}
0&1&0&-1/z\\
-1&0&1&0\\
0&-1&0&1\\
z&0&-1&0
\end{pmatrix},
\qquad
\mathcal M(z)=L_Q+F(z)+J(z).
\]
Then the exact full rational-function identity is
\[
P_A(z)=-z\,\chi_R(z)\det\mathcal M(z).                   \tag{11}
\]
It requires neither independent parameters nor an inverse Gram matrix on their span.

Here is a direct determinant verification, retaining the normalization and sign.
Write an original vector as \(x+\alpha e+\beta f\), and follow the rightmost factors \(F_t,E_u,F_w,E_v\).
Let \(\beta_1\) be the f-coordinate after \(F_t\), \(\alpha_1\) the e-coordinate after \(E_u\), and \(\beta_2\) the f-coordinate after \(F_w\).
The positive coordinate before applying \(R\) is
\[
x+\alpha t+\beta_1u+\alpha_1w+\beta_2v.
\]
The eigenvector equations and the three definitions give
\[
\begin{aligned}
0={}&(zI-R)x-R(\alpha t+\beta_1u+\alpha_1w+\beta_2v),\\
0={}&\beta_1-\beta+(t,x)+\tfrac12(t,t)\alpha,\\
0={}&\alpha_1-\alpha+(u,x)+(u,t)\alpha+\tfrac12(u,u)\beta_1,\\
0={}&\beta_2-\beta_1+(w,x)+(w,t)\alpha+(w,u)\beta_1
                                    +\tfrac12(w,w)\alpha_1,\\
0={}&z\alpha-\alpha_1+(v,x)+(v,t)\alpha+(v,u)\beta_1
                          +(v,w)\alpha_1+\tfrac12(v,v)\beta_2,\\
0={}&z\beta-\beta_2.
\end{aligned}                                                        \tag{12}
\]
Start with columns \((x,\alpha,\beta,\beta_1,\alpha_1,\beta_2)\), and rows consisting of the positive, final-e and final-f eigenvector equations followed by the three intermediate definitions.
The last three columns in the last three rows have a unit lower-triangular block.
Its Schur complement recovers exactly \(zI-A\), so this augmented determinant is \(P_A\).

Reordering the last five rows into their order in (12) is the even permutation \((3,4,5,1,2)\).
Moving the original \(\beta\) column to the end crosses three columns and changes the sign.
Eliminating that final column with the last equation supplies the pivot \(z\) and substitutes \(\beta=\beta_2/z\).
Eliminating \(x\) then supplies \(\chi_R(z)\) and
\[
x=K_R(z)(\alpha t+\beta_1u+\alpha_1w+\beta_2v).
\]
The remaining four equations in \((\alpha,\beta_1,\alpha_1,\beta_2)\) have precisely matrix \(\mathcal M(z)\).
The two pivots and the one column sign prove (11).
This establishes a determinant identity, not just an equivalence of eigenvector equations.
It holds on the resolvent domain and hence over the rational-function field, retaining the complete polynomial after clearing denominators.

As an endpoint check, if every parameter is zero then
\(\det J(z)=-(z-1)^2/z\), so (11) gives \(\chi_R(z)(z-1)^2\), as required.

<a id="symmetric-part"></a>
### The exact symmetric part and a projected two-vector test

Let \(\widehat Q_{ij}=(\widehat q_i,\widehat q_j)\), and let \(C_{14}\) have entries one in positions \((1,4)\), \((4,1)\) and zero elsewhere.
The positive-isometry resolvent identity gives
\[
Q+F(z)+F(z)^{\mathsf T}=(z^2-1)\widehat Q.
\]
For example, the diagonal identity follows by expanding
\(q=(zI-R)\widehat q\) and using that \(R\) preserves the positive inner product; polarization gives all off-diagonal entries.
Since \(L_Q+L_Q^{\mathsf T}=Q\) and
\(J(z)+J(z)^{\mathsf T}=(z-1/z)C_{14}\), it follows that
\[
\frac{\mathcal M(z)+\mathcal M(z)^{\mathsf T}}2
=\frac{z^2-1}{2}\left(\widehat Q+\frac1z C_{14}\right).   \tag{13}
\]

For any four vectors \(q_i\) in a positive real inner-product space and any \(\delta>0\),
\[
Q+\delta C_{14}\succeq0
\quad\Longleftrightarrow\quad
\mathcal D(q_1,q_4\mid\operatorname{span}\{q_2,q_3\})
                      \ge\delta.                       \tag{14}
\]
To see this without a Gram inverse, fix the first and fourth coefficients and minimize the squared norm of their combination plus \(x_2q_2+x_3q_3\).
The available middle combinations fill their actual span, even when the vectors are zero or dependent.
The minimum is
\(\|x_1q_{1,\perp}+x_4q_{4,\perp}\|^2\).
Writing \(a=\|q_{1,\perp}\|^2\), \(b=\|q_{4,\perp}\|^2\) and \(c=(q_{1,\perp},q_{4,\perp})\), the remaining quadratic matrix is
\[
\begin{pmatrix}a&c+\delta\\c+\delta&b\end{pmatrix}.
\]
Its diagonal is nonnegative and \(-\sqrt{ab}\le c\le\sqrt{ab}\).
As \(\delta>0\), its positive-semidefinite condition is exactly
\(c+\delta\le\sqrt{ab}\), or (14).
This also handles vanishing projections: both sides of (14) then fail when their defect is zero.

A real square matrix whose symmetric part is positive semidefinite has nonnegative determinant.
Indeed write it as \(S+K\), with \(S\succeq0\) symmetric and \(K\) skew-symmetric.
For every \(\varepsilon>0\) and \(0\le s\le1\), the matrix \(S+\varepsilon I+sK\) is nonsingular, because its quadratic form on a real kernel vector would be strictly positive.
Its determinant has the positive sign of \(\det(S+\varepsilon I)\) throughout this continuous path.
Letting \(\varepsilon\) decrease to zero proves the nonnegative conclusion, including singular matrices.

Apply (14) to \(\widehat Q\) with \(\delta=1/z\).
Condition (4) makes (13) positive semidefinite, hence \(\det\mathcal M(z)\ge0\).
For real \(z>1\), \(\chi_R(z)>0\): real orthogonal eigenvalues are \(1\) or \(-1\), and nonreal eigenvalues contribute positive conjugate-pair factors.
Equation (11) therefore gives \(P_A(z)\le0\).
Since \(P_A\) is monic and tends to positive infinity on the positive real axis, it has a real root at least \(z\).
This proves (4), including its non-strict boundary.

For the original-metric criterion, orthogonality gives
\[
\|(zI-R)y\|\le(z+1)\|y\|.
\]
Thus the Gram matrices satisfy
\[
\widehat Q\succeq \frac{1}{(z+1)^2}Q.
\]
Condition (5), together with (14) for \(\delta=(z+1)^2/z\), gives
\[
\frac{1}{(z+1)^2}Q+\frac1zC_{14}\succeq0.
\]
Consequently \(\widehat Q+C_{14}/z\succeq0\), and the same determinant argument proves (5).
Taking the contrapositive at \(z=6/5\) yields (6).
No assertion that the projected vectors span an integer direct summand is needed.

<a id="twisted-cyclic-presentations"></a>
### All four cyclic positions have the same complete polynomial

Conjugating (2) by its last factor gives
\[
F_t A F_{-t}
=F_t R E_vF_wE_u
=R F_{R^{-1}t}E_vF_wE_u.
\]
The integral isometry exchanging \(e,f\) and fixing the positive part commutes with \(R\), and changes this into
\[
R E_{R^{-1}t}F_vE_wF_u.
\]
This is exactly the transformation \(\sigma\) in (7).
Every transformation is an integer conjugacy, so the whole characteristic polynomial and measure are unchanged.
Iteration gives all four stated positions.
A fourth iteration transforms every vector by \(R^{-1}\), also a positive-isometry conjugacy.
This proves the cyclic applicability of the exterior tests without a presentation-independent word invariant.

<a id="cusp-defect-reduction"></a>
### Discrete cusp defects and the exact short-pair reduction

Put \(a=(p,p)/2\), \(b=(q,q)/2\), and \(c=(p,q)\).
For nonzero permitted integer parameters, \(a,b\) are positive integers.
Cauchy--Schwarz gives
\[
\kappa(p,q)=1-c+ab\ge(\sqrt{ab}-1)^2\ge0.                \tag{15}
\]
All terms in \(\kappa\) are integral.
If it is zero, then \(ab=1\), hence \(a=b=1\), and equality forces \(c=2\).
Positive definiteness then gives \(p=q\) and squared norm two.
The converse follows by substitution.
If a parameter is zero, the defining formula gives one directly.
This proves (9) and all zero cases.

The geometric meaning follows from the actual intermediate cusp:
\[
F_qE_p f=-a e+(p-aq)+\kappa(p,q)f,\qquad
(p-aq,p-aq)=2a\,\kappa(p,q).                            \tag{16}
\]
Thus precisely the zero-defect nonzero pair sends \(f\) to \(-e\).
For a norm-two vector \(h\), let \(s_hx=x-(h,x)h\) on the positive summand and put \(g=F_hE_h\).
Direct use of the formulas gives
\[
g^{-1}e=-f,\qquad
g^{-1}v=s_hv+(h,v)f.
\]
Adding a multiple of the isotropic base vector to the transvection parameter leaves the transvection unchanged.
Covariance therefore gives
\[
g^{-1}E_vg=F_{-s_hv},
\]
and hence the entire four-factor identity
\[
E_vF_hE_hF_t=F_hE_hF_{\,t-s_hv}.                       \tag{17}
\]
The reflection \(s_h\) is integral because \(H\) is integral and \(h^2=2\), and it preserves the positive pairing.
All parameters on the right remain integral of even norm.

Multiplying (17) by \(R\) leaves an alternating three-factor word.
The [existing exact short-word conjugacy](../ledger/Yin_L_G0462_v14.md#short-word-reduction) reduces it to two transvections while preserving the complete polynomial, with a cusp exchange when needed.
The adopted unbounded-norm two-factor theorem therefore supplies \(\eta_*\).
The twisted cyclic presentations already proved allow the same reduction whenever any of their middle pairs has defect zero.
No statement that every four-factor word admits this reduction is made.

Finally, (15) implies \(ab\le(1+\sqrt K)^2\) when \(\kappa\le K\).
Since \(a,b\ge1\), each is at most their product, giving (10).
Apply this to the two disjoint nonzero pairs to bound all four squared norms by the same \(2(1+\sqrt K)^2\).
The retained theorem (1), at \(k=4\), gives the asserted gap.
If a parameter vanishes, the separate at-most-three theorem already applies.

<a id="limits"></a>
## What the four-factor test does and does not decide

For a candidate of complete measure below \(6/5\), all four actual cyclic presentations must pass the projected-defect inequalities.
The inequalities force the outer projections to remain sufficiently close to the same direction, or sufficiently small, after removal of the middle span.
They are only necessary conditions; a zero projected defect occurs whenever all four parameters lie in the middle span and is not evidence of low measure.

The cusp-defect reduction removes an exact short relation that can hide arbitrarily large outer parameters.
Bounded disjoint cusp defects return to the already controlled bounded-norm domain.
When these defects grow, the projected tests still permit substantial rank dependence and cancellation; no uniform low-measure reduction or all-four-factor gap has been proved.

The new determinant and sign test retain the complete characteristic polynomial.
They supply no new nonneutral value and do not revive sampling in the [already covered integral orthogonal-basis domain](Yin_C_G0886_v3.md#decision-neutral-integral-embedding-cover).
An actual counterexample construction still requires integer input outside the relevant exclusions, nonneutrality and a complete measure estimate tending to one.
The [unrestricted G0001 objective](../tasks/Yin_T_G0001_v1.md#contract) remains unresolved.

## Assessment history

### Decision four-factor-exterior-tests

| Field | Value |
| --- | --- |
| date | 2026-11-10T04:41 |
| status | proved |
| reason | The complete independent review found no unresolved gap in the full four-scalar determinant, exact symmetric part, projected-defect equivalence, real-root boundaries, twisted cyclic conjugacies, discrete cusp reductions or unchanged inherited gap statements. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained gaps and four-factor tests](#statement) | All lattices, parameters and real exterior thresholds, every degenerate case and cyclic position, complete-measure consequences and precise restrictions. |
| argument | [Complete new argument](#argument) | Full determinant normalization, projection and sign proofs, root existence, cyclic conjugacies and discrete cusp reductions. |
| dependency | [Adopted bounded-word theorem](Yin_C_G0885_v3.md#decision-bounded-word-bounded-norm-gap) | Unchanged bounded-count/bounded-norm gap, separate at-most-three assertion and their exact uniformity and sequence scopes. |
| dependency | [Integral transvections](../ledger/Yin_L_G0462_v13.md#integer-generators) | Original pairing-preserving integer formulas and negative-vector inverses under even parameter norm. |
| dependency | [Addition and short-word conjugacy](../ledger/Yin_L_G0462_v14.md#short-word-reduction) | Norm-preserving covariance, parameter addition, integer conjugacies and the exact three-to-two transfer. |
| review | [Complete independent exterior finding](../audits/reviews/Yin_R_G1114_v11.md#four-factor-exterior-test-review) | Every stated test, full argument, exact inherited input and nonconclusion, including singular spans and non-strict boundary cases. |

## Current assessment

[Selected decision](#decision-four-factor-exterior-tests)

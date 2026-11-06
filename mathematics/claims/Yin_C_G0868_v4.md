---
author: Yin
---

# Integral Gram metrics and rank costs for matrix analytic damping

Date: 2026-11-05.
This project deduction extends the matrix analytic-germ mechanism of C868 v3 to positive integral Gram metrics with an explicit determinant and rank price.
The total normalization expense is \(-\log|\det Q(0)|\), without division by matrix size.
The argument supplies arithmetic metric control, not a construction of the required original-polynomial realization.

The coordinating agent proposed the integral-Gram arithmetic normalization and the rank refinement through the highest nonzero determinant coefficient.
The witt_moment_compatibility delegate checked those mechanisms, and both contributors derived the Loewner and determinant strengthening of the existing column estimate.
The delegate prepared and checked the complete argument and controls below, with the coordinating agent contributing their original-input scope.
These are author-side development checks; no independent review or assessment of this version is asserted here.

## Inputs and retained versions

[C868 v3](Yin_C_G0868_v3.md#statement) retains its matrix-germ theorem, arbitrary positive-metric conditioning price, scalar replication, companion identities and rational circle-pole rigidity under its [selected assessment](Yin_C_G0868_v3.md#decision-whole-matrix-review-2026-11-05).
Versions v1--v3 remain fixed, with their own exact statements, arguments and review scopes.
The direct analytic input here is the [v3 column Parseval inequality](Yin_C_G0868_v3.md#matrix-column-determinant-gap), before its reduction to the smallest singular value.
The proof below retains the matrix order and the finite-germ justification of that step.

The [v3 metric calculation and varying-metric control](Yin_C_G0868_v3.md#matrix-metric-and-copy-costs) provide the precise comparison: arbitrary real positive metrics need not have bounded arithmetic determinant.
The new conclusion uses the integrality of the Gram form and of the first nonzero coefficient together.
It does not replace a real positive metric by an integral one for free.

[C228](Yin_C_G0228_v1.md#statement) is only a comparison for ordinary normal integral matrices and the rational positive-metric mixed-conjugate obstruction.
Its entropy theorem and source inputs are not premises of the new damping estimates.
No result in a later exploratory ledger is a dependency here.
No new external theorem is adopted, and no literature-priority or optimal-constant claim is made.

## Statement

Let \(r\ge1\), let \(\mathbb D\) be the open unit disk, and let
\[
 F(z)=I_r+\sum_{n\ge1}C_nz^n,\qquad C_n\in M_r(\mathbb Z),
 \tag{IG0}
\]
be an analytic germ at zero.
Let H be a fixed real symmetric positive definite \(r\)-by-\(r\) matrix.
Suppose Q and U are holomorphic on \(\mathbb D\) and satisfy
\[
 Q(z)^*H Q(z)\le H,\qquad U(z)^*H U(z)\le H,
 \qquad Q(0)\ \hbox{invertible},\qquad U=FQ\ \hbox{near zero}.
 \tag{IG1}
\]
All inequalities between Hermitian matrices use the Loewner order.
Both contraction inequalities hold for every \(z\in\mathbb D\).
Put
\[
 \tau=-\log|\det Q(0)|,\qquad S=H^{1/2}.
\]
Then \(\tau\ge0\).
For the remaining assertions assume \(F\not\equiv I_r\), let N be its first positive index with \(C_N\ne0\), and write
\[
 C=C_N,\quad k=\operatorname{rank}C\ge1,\quad
 D=SCS^{-1},\quad Q'_0=SQ(0)S^{-1}.
\]

### IG2. The full singular-value determinant bound

Without requiring H to be integral,
\[
 I_r+\frac14D^*D\le Q_0'^{-*}Q_0'^{-1},
 \qquad
 \det\!\left(I_r+\frac14D^*D\right)\le e^{2\tau}.
 \tag{IG2}
\]
The determinant assertion is equivalently the following bound, where \(\lambda_1,\ldots,\lambda_k>0\) are the nonzero eigenvalues of \(D^*D\), with multiplicity:
\[
 \tau\ge\frac12\sum_{i=1}^k\log(1+\lambda_i/4).
 \tag{IG3}
\]
The other \(r-k\) eigenvalues contribute factors one to the complete determinant.
There is no normalization by r or k, no full-disk analyticity requirement on F, and no boundary \(H^2\) assumption on F.

### IG4. An integral Gram determinant supplies a rank price

Assume in addition \(H\in M_r(\mathbb Z)\), and put \(\Delta=\det H\in\mathbb Z_{>0}\).
Then
\[
 \boxed{\displaystyle
 \tau\ge\frac{k}{2}
       \log\!\left(1+\frac{1}{4\Delta^{1/k}}\right).}
 \tag{IG4}
\]
In particular,
\[
 \Delta=1\quad\Longrightarrow\quad
 \tau\ge k\,c_{\rm mat},\qquad c_{\rm mat}=\frac12\log(5/4),
 \tag{IG5}
\]
independently of the condition number of H.
For every positive integral H there is also the convenient rank-free consequence
\[
 \tau\ge\frac12\log\!\left(1+\frac1{4\Delta}\right).
 \tag{IG6}
\]
The proof does not require an integral factorization \(H=A^TA\).

### IG7. Primitive normalization and integral changes of basis

If H is positive definite and lies on a ray containing a positive integral matrix, replace it by the unique primitive positive integral matrix \(H_{\rm prim}\) on that ray.
Here primitive means that the greatest common divisor of all its integer entries is one.
The hypotheses (IG1), the value of \(\tau\), and all \(\lambda_i\) are unchanged by this scalar replacement.
Thus (IG4)--(IG6) apply with
\[
 \Delta_{\rm prim}=\det H_{\rm prim}.
 \tag{IG7}
\]
In particular this applies to every positive definite rational symmetric H.

For any \(A\in\operatorname{GL}_r(\mathbb Z)\), the simultaneous transformation
\[
 H\longmapsto A^THA,\qquad
 (F,Q,U)\longmapsto(A^{-1}FA,A^{-1}QA,A^{-1}UA)
 \tag{IG8}
\]
preserves the complete hypotheses, the total price \(\tau\), k, primitive Gram determinant and the polynomial
\[
 \frac{\det(H+tC^THC)}{\det H}.
 \tag{IG9}
\]
No Euclidean contraction is asserted after this transformation unless its actual metric warrants it.

### IG10. Two controls and a conditional original-input return

There are fixed nonconstant integer germs and primitive integral metrics of determinant one whose condition numbers tend to infinity while (IG1) has finite-price realizations.
There are also fixed nonconstant integer germs satisfying (IG1) with primitive integral metrics of unbounded determinant and \(\tau\to0\).
Therefore the integral-metric arithmetic hypothesis matters, and its determinant expense cannot be removed for all positive integral metrics.
Even the numerical normalization \(\det H=1\) is insufficient if H is allowed to be nonintegral.

If an actual original polynomial P has a realization satisfying (IG0)--(IG1), with \(F\not\equiv I_r\),
\[
 \Delta_{\rm prim}\le\Delta_*,\qquad
 \tau\le C_{\rm tr}\,m(P),\qquad
 \Delta_*\ge1,\quad C_{\rm tr}>0,
\]
then
\[
 m(P)\ge\frac1{2C_{\rm tr}}
                  \log\!\left(1+\frac1{4\Delta_*}\right).
 \tag{IG10}
\]
A broader sufficient arithmetic comparison is
\[
 \Delta_{\rm prim}^{1/k}\le A k,\qquad A>0.
\]
Under this comparison and the same actual price upper bound,
\[
 \tau\ge\frac1{8A+2},\qquad
 m(P)\ge\frac1{C_{\rm tr}(8A+2)}.
 \tag{IG11}
\]
No such realization or arithmetic comparison for all original inputs is supplied here.
The unrestricted [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract) remains outside the proved coverage.

### IG12. A fixed-positive-measure block family still has growing full price

For \(n\ge1\), let \(S_n\) be the standard column companion of
\[
 q_n(s)=s^{n+1}-3s^n,
\]
and put
\[
 C_n^{\rm tr}=\begin{pmatrix}0&-I_{n+1}\\I_{n+1}&S_n\end{pmatrix},\qquad
 G_n(z)=(I-z(C_n^{\rm tr})^{-T})(I-zC_n^{\rm tr})^{-1}.
 \tag{IG12}
\]
The matrix \(C_n^{\rm tr}\) is integral unimodular of size \(2n+2\), with complete characteristic polynomial
\[
 P_n(t)=(t^2-3t+1)(1+t^2)^n,\qquad
 m(P_n)=\log\frac{3+\sqrt5}{2}>0.
\]
Every realization of \(G_n\) satisfying (IG1) with \(H=I_{2n+2}\) has
\[
 \tau\ge\log(7/2)+(n-1)\log(5/4)\longrightarrow\infty.
 \tag{IG13}
\]
Its first nonzero coefficient nevertheless has operator-norm square exactly ten for all n.
Thus controlling only that operator norm misses a genuine full determinant expense.
These are particular reducible inputs with removable cyclotomic content, and particular matrix realizations.
No conclusion about every integral basis or the irreducible hard class follows.

<a id="argument"></a>
## Complete argument

<a id="gram-loewner-determinant"></a>
### 1. The complete column inequality and determinant

Conjugate all three analytic functions by the positive square root \(S=H^{1/2}\).
Write \(F'=SFS^{-1}\), \(Q'=SQS^{-1}\), \(U'=SUS^{-1}\).
The two inequalities (IG1) become ordinary Euclidean contractions for \(Q'\) and \(U'\).
The relation \(U'=F'Q'\) is still needed only near zero, and \(\det Q'_0=\det Q(0)\).
Consequently the singular values \(s_1,\ldots,s_r\) of \(Q'_0\) lie in \((0,1]\), and \(\tau=-\sum_i\log s_i\ge0\).

Write \(Q'_j\) and \(U'_j\) for the Taylor coefficients of \(Q'\) and \(U'\).
For completeness, vector Parseval on every radius \(\rho<1\), followed by monotone convergence of the nonnegative coefficient sums as \(\rho\uparrow1\), gives for every \(v\in\mathbb C^r\)
\[
 \|Q'_N v\|^2\le\|v\|^2-\|Q'_0v\|^2,\qquad
 \|U'_N v\|^2\le\|v\|^2-\|Q'_0v\|^2.
 \tag{1}
\]
Here \(U'_0=Q'_0\), since \(F'(0)=I_r\).
The absence of all earlier positive coefficients of \(F'-I_r\) gives the exact finite-germ identity
\[
 U'_N-Q'_N=DQ'_0.
 \tag{2}
\]
Thus the v3 column estimate, with its multiplication order unchanged, is
\[
 \|DQ'_0v\|^2
 \le2\|U'_Nv\|^2+2\|Q'_Nv\|^2
 \le4(\|v\|^2-\|Q'_0v\|^2).
 \tag{3}
\]
Substituting \(v=Q_0'^{-1}w\) for arbitrary w yields
\[
 D^*D\le4(Q_0'^{-*}Q_0'^{-1}-I_r).
 \tag{4}
\]
This proves the first inequality in (IG2) before replacing any singular value by a scalar lower bound.

If \(0<X\le Y\) are Hermitian positive definite, then \(Y^{-1/2}XY^{-1/2}\le I_r\), so all its positive eigenvalues are at most one.
Taking their product gives \(\det X\le\det Y\).
Apply this to (4) after dividing by four and adding \(I_r\), and use
\[
 \det(Q_0'^{-*}Q_0'^{-1})
       =|\det Q'_0|^{-2}=e^{2\tau}.
\]
This proves the determinant assertion in (IG2) and its full singular-value form (IG3).

<a id="integral-gram-rank-price"></a>
### 2. The highest nonzero coefficient has only one Gram denominator

Assume now that H is integral, symmetric and positive definite.
The matrix
\[
 B=H^{-1}C^THC
\]
is similar to \(D^*D\), since
\[
 SBS^{-1}=S^{-1}C^THCS^{-1}=D^*D.
 \tag{5}
\]
Although B need not be symmetric, it therefore has exactly k positive eigenvalues \(\lambda_1,\ldots,\lambda_k\) and \(r-k\) zero eigenvalues.

Consider the actual integer polynomial
\[
 f_H(t)=\det(H+tC^THC)\in\mathbb Z[t].
\]
Its constant coefficient is \(\Delta>0\), and
\[
 f_H(t)=\Delta\det(I_r+tB)
       =\Delta\prod_{i=1}^k(1+t\lambda_i).
 \tag{6}
\]
In particular its degree is exactly k.
Its highest nonzero coefficient is
\[
 a_k=\Delta\prod_{i=1}^k\lambda_i\in\mathbb Z_{>0},
\]
so
\[
 \prod_{i=1}^k\lambda_i\ge\Delta^{-1}.
 \tag{7}
\]
The denominator here is \(\Delta\), not \(\Delta^k\); it comes from one determinant identity.
No kernel labels or dimensions have been removed from the underlying matrix model.

The function
\[
 \varphi(x)=\log(1+e^x/4)
\]
is increasing and strictly convex, because
\[
 \varphi'(x)=\frac{e^x}{4+e^x}>0,\qquad
 \varphi''(x)=\frac{4e^x}{(4+e^x)^2}>0.
\]
Convexity applied to \(\log\lambda_1,\ldots,\log\lambda_k\), followed by (7), gives
\[
 \begin{aligned}
 \sum_{i=1}^k\log(1+\lambda_i/4)
 &\ge k\log\!\left(1+\frac{(\prod_i\lambda_i)^{1/k}}4\right)\\
 &\ge k\log\!\left(1+\frac1{4\Delta^{1/k}}\right).
 \end{aligned}
 \tag{8}
\]
Combining (8) with (IG3) proves (IG4), and \(\Delta=1\) gives (IG5).

The coefficient of t in (6) is also a positive integer:
\[
 a_1=\Delta\,\operatorname{tr}(H^{-1}C^THC)
     =\Delta\|D\|_{\rm HS}^2\in\mathbb Z_{>0}.
 \tag{9}
\]
All the elementary symmetric coefficients of the positive \(\lambda_i\) are nonnegative.
It follows that
\[
 e^{2\tau}\ge\prod_{i=1}^k(1+\lambda_i/4)
          \ge1+\frac14\sum_i\lambda_i
          \ge1+\frac1{4\Delta},
 \tag{10}
\]
which proves (IG6).
The argument uses integer Gram data in place of a condition-number bound.
It also gives the rank refinement when H is the identity, without changing the existing v3 operator-norm conclusion.

<a id="primitive-gram-covariance"></a>
### 3. Scalar normalization and genuine integral covariance

Multiplying H by any positive scalar leaves (IG1) unchanged.
It also leaves \(SCS^{-1}\) unchanged, because the square root changes by a scalar.
Thus \(\tau\), all \(\lambda_i\) and the normalized polynomial (IG9) are unchanged.

If H is rational, clear its denominators by a positive integer, then divide the resulting integer matrix by the greatest common divisor of all its entries.
The result \(H_{\rm prim}\) is positive definite, integral and primitive.
More generally this construction applies whenever the positive ray through H contains an integral matrix.

To check uniqueness, suppose \(\widetilde H=cH_{\rm prim}\) is another integral matrix on that ray.
Because the entries of \(H_{\rm prim}\) have greatest common divisor one, an integer linear combination of them equals one.
The same linear combination of the entries of \(\widetilde H\) equals c, hence \(c\in\mathbb Z_{>0}\).
Therefore every integral matrix on the ray is a positive integer multiple of \(H_{\rm prim}\).
Its determinant is \(c^r\Delta_{\rm prim}\), so primitive normalization gives the least positive integral determinant on that ray.

For \(A\in\operatorname{GL}_r(\mathbb Z)\), set
\[
 \widetilde H=A^THA,\qquad \widetilde C=A^{-1}CA.
\]
The transformed germ still has integer coefficients, and \(\widetilde C\) has rank k.
Direct substitution shows
\[
 \widetilde Q(z)^*\widetilde H\,\widetilde Q(z)
       =A^TQ(z)^*HQ(z)A\le\widetilde H,
\]
and the identical calculation applies to U.
The germ product, invertibility of \(Q(0)\) and its determinant are preserved.

Moreover,
\[
 \widetilde C^T\widetilde H\,\widetilde C=A^TC^THCA,
\]
so
\[
 \det(\widetilde H+t\widetilde C^T\widetilde H\,\widetilde C)
   =\det(A)^2\det(H+tC^THC)=f_H(t).
 \tag{11}
\]
In particular \(\det\widetilde H=\Delta\).
The common divisor of the entries of H is also preserved: integral congruence makes every new entry an integer linear combination of the old ones, and the integral inverse congruence gives the converse divisibility.
Thus \(\Delta_{\rm prim}\) and all assertions in (IG7)--(IG9) are invariant under this simultaneous integral change of basis.

Rescaling H to numerical determinant one generally destroys integrality and does not supply an integral Gram matrix of determinant one.
The arithmetic conclusion is about the primitive integral representative, not an arbitrarily normalized covolume.

<a id="gram-metric-controls"></a>
### 4. Large condition number at fixed Gram determinant, and genuine determinant degeneration

Let \(E=E_{12}\in M_2(\mathbb Z)\), so \(E^2=0\), and fix
\[
 F(z)=I_2+zE.
\]
For \(w\in\mathbb C\), the two squared singular values of
\(\left(\begin{smallmatrix}1&w\\0&1\end{smallmatrix}\right)\)
have product one and sum \(2+|w|^2\).
Solving that quadratic gives its operator norm
\[
 \ell(|w|)=\frac{\sqrt{4+|w|^2}+|w|}{2},
 \tag{12}
\]
which is increasing in \(|w|\).
This is the same exact shear calculation retained in v3.

For an integer \(N\ge1\), put
\[
 A_N=\begin{pmatrix}1&N\\0&1\end{pmatrix},\qquad
 H_N=A_N^TA_N=\begin{pmatrix}1&N\\N&N^2+1\end{pmatrix}.
 \tag{13}
\]
The matrix \(H_N\) is primitive positive integral with determinant one.
Its largest eigenvalue is at least \(N^2+1\), while its smallest is the reciprocal of the largest.
Consequently its condition number tends to infinity.

Since \(A_N=I_2+NE\) commutes with F, conjugation by \(A_N\) identifies the H-metric norm of F with its original Euclidean norm.
Set
\[
 L=\ell(1)=\frac{\sqrt5+1}{2},\qquad
 Q=L^{-1}I_2,\qquad U=FQ.
 \tag{14}
\]
Equation (12) proves both contractions in (IG1) for every \(H_N\).
The first nonzero integer coefficient has rank one, \(Q(0)\) is invertible, and
\[
 \tau=2\log L
\]
is finite and independent of N.
Thus the determinant-one conclusion has actual nonconstant examples even when the condition number is arbitrarily large.
No sharpness of (IG5) is asserted by this example.

For the opposite control, let the integer \(K\ge1\) tend to infinity and put
\[
 \widehat H_K=\operatorname{diag}(1,K),\qquad
 a_K=K^{-1/2},\qquad
 L_K=\ell(a_K),\qquad
 Q_K=L_K^{-1}I_2,\qquad U_K=FQ_K.
 \tag{15}
\]
Now \(S_K=\operatorname{diag}(1,\sqrt K)\) conjugates F to \(I_2+a_KzE\).
Equation (12) again proves all hypotheses (IG1), and
\[
 \Delta_{\rm prim}=K,\qquad
 \tau_K=2\log L_K
       =2\operatorname{arsinh}\!\left(\frac1{2\sqrt K}\right)
       \longrightarrow0.
 \tag{16}
\]
This is precisely the v3 varying-metric mechanism after scalar normalization to an integral primitive Gram form.
Here k is one, its sole positive \(\lambda\) is \(1/K\), and \(\Delta\lambda=1\).
The arithmetic coefficient lower bound is attained, but the displayed realization has \(\tau_K\) of order \(K^{-1/2}\), whereas (IG6) has order \(K^{-1}\).
No optimality claim for the analytic price follows.

Finally, replace \(\widehat H_K\) in (15) by
\[
 H_K^\circ=K^{-1/2}\widehat H_K
         =\operatorname{diag}(K^{-1/2},K^{1/2}).
 \tag{17}
\]
This positive metric has numerical determinant one, with the same contractions and the same \(\tau_K\to0\).
For \(K>1\) it is not integral; its primitive integral representative is still \(\widehat H_K\), of determinant K.
Therefore determinant-one covolume alone cannot replace the integral-Gram hypothesis.

<a id="trace-block-full-price"></a>
### 5. Full determinant cost for an actual block companion family

Let \(r=n+1\), with \(n\ge1\).
In the standard column convention, \(S_ne_j=e_{j+1}\) for \(0\le j<r-1\), and \(S_ne_{r-1}=3e_{r-1}\).
Consequently its last two columns are \(e_{r-1}\) and \(3e_{r-1}\), while the other \(r-2\) columns are mutually orthogonal unit vectors orthogonal to those two.
Its squared singular values are therefore ten once, one with multiplicity \(n-1\), and zero once.

The inverse and first coefficient for the actual matrix in (IG12) are
\[
 (C_n^{\rm tr})^{-1}=\begin{pmatrix}S_n&I_r\\-I_r&0\end{pmatrix},\qquad
 D_n=C_n^{\rm tr}-(C_n^{\rm tr})^{-T}
       =\begin{pmatrix}-S_n^T&0\\0&S_n\end{pmatrix}.
 \tag{18}
\]
Thus \(C_n^{\rm tr}\) is integral unimodular, and \(G_n=I+zD_n+\cdots\) is a nonconstant integer analytic germ.
The squared singular values of \(D_n\) are ten twice, one with multiplicity \(2(n-1)\), and zero twice.
In particular \(\|D_n\|_{\rm op}^2=10\), but its rank is \(2n\).
Apply the full determinant bound (IG2), with \(H=I_{2r}\), to obtain
\[
 e^{2\tau}\ge\det(I_{2r}+D_n^TD_n/4)
             =(7/2)^2(5/4)^{2(n-1)}.
 \tag{19}
\]
This proves (IG13).

The complete characteristic polynomial is checked directly, without a premise about a change of basis.
For \(t\ne0\), a block Schur complement gives
\[
 \begin{aligned}
 \det(tI_{2r}-C_n^{\rm tr})
 &=t^r\det((t+t^{-1})I_r-S_n)\\
 &=t^{n+1}q_n(t+t^{-1})\\
 &=(t^2-3t+1)(1+t^2)^n.
 \end{aligned}
 \tag{20}
\]
Both sides are polynomials, so the identity holds at zero as well.
The two roots of \(t^2-3t+1\) are positive reciprocals, with larger root \((3+\sqrt5)/2\); all roots of \(1+t^2\) lie on the unit circle.
This proves the stated exact fixed positive total measure, retaining all \(2n+2\) original roots and multiplicities.

For each fixed n, finite-price realizations exist.
Indeed, put \(h_n(z)=\det(I-zC_n^{\rm tr})\), and take
\[
 Q(z)=\eta h_n(z)I_{2r},\qquad
 U(z)=\eta\bigl(I-z(C_n^{\rm tr})^{-T}\bigr)
                  \operatorname{adj}(I-zC_n^{\rm tr})
\]
with a sufficiently small real \(\eta>0\).
Both are polynomial matrices, so scaling makes their Euclidean norms at most one on the closed disk.
They satisfy \(U=G_nQ\) near zero and \(Q(0)=\eta I_{2r}\), with finite total price.
This supplies no upper bound in terms of \(m(P_n)\), and (19) excludes one uniform finite bound \(\tau\le C_{\rm tr}m(P_n)\) for this particular family of germs.

The full-spectrum cost does not contradict the bounded first-coefficient operator norm.
It uses the increasing number of nonzero singular values that the operator norm alone does not count.
Nor does it rule out another matrix candidate, a different integral basis, or removal of cyclotomic content before constructing a realization.

<a id="gram-original-input-boundary"></a>
### 6. Conditional return and the unchanged realization obligation

If a genuine original-input realization has \(\Delta_{\rm prim}\le\Delta_*\), then (IG6) and \(\tau\le C_{\rm tr}m(P)\) immediately give (IG10).
For the broader comparison \(\Delta_{\rm prim}^{1/k}\le Ak\), equation (IG4) gives
\[
 \tau\ge\frac{k}{2}\log\!\left(1+\frac1{4Ak}\right)
       \ge\frac{k}{2(4Ak+1)}
       =\frac1{8A+2/k}\ge\frac1{8A+2}.
 \tag{21}
\]
The middle inequality uses \(\log(1+x)\ge x/(1+x)\) for \(x\ge0\).
The claimed original-measure consequence in (IG11) follows upon applying the actual upper bound for \(\tau\).
This allows growing primitive Gram determinant when its relation to the actual first-coefficient rank is paid.
It supplies no such relation or realization for arbitrary P.

The integer-Gram argument repairs the condition-number loss for a realization already satisfying its hypotheses.
It does not repair the normalized companion all-pass candidate.
For clarity, let \(C_0\) be a real invertible matrix, let
\[
 C_0^\dagger=H^{-1}C_0^TH,\qquad
 G_H(z)=\bigl(I-z(C_0^\dagger)^{-1}\bigr)(I-zC_0)^{-1}.
 \tag{22}
\]
Conjugation by \(S=H^{1/2}\), with \(T=SC_0S^{-1}\), gives
\[
 SG_HS^{-1}=(I-zT^{-T})(I-zT)^{-1}.
\]
The [v3 normalized-companion identity](Yin_C_G0868_v3.md#companion-reversal-cost), whose algebraic unitary equivalence does not require integral entries, shows that \(G_H\) is H-unitary at almost every regular circle point exactly when
\[
 T^{-T}=T,\qquad\hbox{equivalently}\qquad C_0^\dagger C_0=I.
 \tag{23}
\]
In that case T is orthogonal, all eigenvalues of \(C_0\) lie on the unit circle, and its monic characteristic polynomial has zero Mahler measure.
Thus positive original measure still excludes this all-pass shortcut.
For a general integral H of determinant greater than one, \(H^{-1}\) can also introduce denominators, so the function \(G_H\) in (22) does not automatically have an integer germ.

Similarly, requiring a rational matrix to be normal in a rational positive metric meets the already retained [C228 mixed-real/nonreal obstruction](Yin_C_G0228_v1.md#statement).
Its exact scope is an irreducible mixed-conjugate factor occurring once, also with a coprime rational padding factor; it includes Salem minimal polynomials of degree at least four with cyclotomic padding.
This comparison uses the exact [adopted C228 statement and scope](Yin_C_G0228_v1.md#decision-complete-retained-proof-adoption); that obstruction is not a proof input for the new damping estimates.

The remaining original-input requirement is an actual nonconstant integer germ and compatible disk-holomorphic Q and U, together with a paid primitive Gram determinant or rank comparison and an upper bound \(\tau\le C_{\rm tr}m(P)\).
Neither an arbitrary basis change, a rational metric, a covolume normalization, nor the present conditional inequalities supplies those data.

## Assessment history

### Decision whole-integral-metric-review-2026-11-05

| Field | Value |
| --- | --- |
| date | 2026-11-05T20:06 |
| status | proved |
| reason | Adopt the complete integral-Gram matrix damping theorem after the independent whole-proof finding R1091 v4. The full singular-value determinant bound yields the rank price k/2*log(1+1/(4*Delta^(1/k))), with primitive normalization and integral covariance. All metric controls, the actual fixed-positive block-family cost, conditional original-input returns and comparison limits are included. No unrestricted original-input realization or G0001 gap is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete integral Gram statement](#statement) | IG0-IG13, all exact hypotheses, determinant and rank prices, normalization, covariance, controls and conditional original-input scope. |
| argument | [Complete integral Gram proof](#argument) | All six sections, including the integer determinant coefficient, full singular spectrum, actual finite-price constructions and final comparison boundaries. |
| dependency | [V3 column estimate](Yin_C_G0868_v3.md#matrix-column-determinant-gap) | Exact finite-germ coefficient identity and vector Parseval defect before reduction to the least singular value; the new determinant and arithmetic refinements are proved in v4. |
| support | [V3 metric and shear calculation](Yin_C_G0868_v3.md#matrix-metric-and-copy-costs) | Positive-metric conjugation and the exact shear norm used in the controls, with no inherited arithmetic Gram or rank conclusion. |
| dependency | [V3 companion algebra](Yin_C_G0868_v3.md#companion-reversal-cost) | Normalized circle-unitary equivalence, including its directly checked real-invertible extension for the final metric-adjoint comparison. |
| support | [C228 comparison](Yin_C_G0228_v1.md#statement) | Only the rational positive-metric mixed-conjugate normality obstruction, including a single occurrence and coprime padding; not its entropy theorem or an input to the new damping inequalities. |
| review | [Independent integral Gram whole-proof finding](../audits/reviews/Yin_R_G1091_v4.md#integral-gram-whole-proof-finding) | Entire exact statement and argument, all controls and fixed mathematical interfaces; no substantive proof repair supplied by the reviewer. |

## Current assessment

[Selected decision](#decision-whole-integral-metric-review-2026-11-05)


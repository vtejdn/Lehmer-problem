---
author: Yin
---

# Coefficient dependence of a single-Haar determinant on a fixed exponent interval

Date: 2026-10-13.
Human author: Yin.
Responsible working draft by the assigned coefficient-dependence AI for the authorized F0010 run.
Scope: fixed finite complex coefficient spaces, continuity across degree and zero changes, valid derivative domains, circle crossings, and matrix determinant-polynomial transfer.
This is an author-complete proof draft awaiting independent whole review; no novelty or independent-review claim is made.
G0001 remains paused.

## Responsible scope and starting inputs

The exact contract is F0010.
The existing scalar [Jensen and determinant convention](../audits/literature/Luc22/Yin_U001.md#luc22-kernel-removed-determinant), [single-Haar positive-weight baseline](Yin_L_G0431_v1.md#single-haar-formulation), and [regularization](Yin_L_G0431_v1.md#regularization-and-direction) are starting inputs.
Their scope is preserved; this draft does not claim an integer Mahler gap.

## Current complete-proof home

Placement maintenance: 2026-10-21T02:33.
The substantial complete supporting argument is now retained in [C7](../claims/Yin_C_F0007_v1.md#statement), with the applicable original mathematical finding adopted at its actual unknown initial-context relationship.
The full original proof, questions, classical attribution, source-access limits, failed reductions and author freezes remain below because the old R findings, completed Task and other fixed consumers actually use these inputs.
The dated independent wording below remains its historical self-description, rather than a new certification of initial isolation.
This placement allocates no new classical discovery, theorem role or Task objective and changes no historical completion decision.

<a id="coefficient-reuse-and-scope"></a>
## 1. Reuse, definitions and exact scope

The bounded local reuse check read the Task and starting F draft, the linked G scalar working formulation, Luc22-U001, and the coefficient/continuity passages of Den09-U002.
Searches in existing C/L/U and the bibliography for coefficient continuity, Mahler continuity and plurisubharmonicity found the classical root formula and restricted operator-potential statements, but no single existing account of this Task's full fixed-interval boundary.
The external primary check then read [Sin07-U001](../audits/literature/Sin07/Yin_U001.md#sin07-fixed-degree-continuity), including Theorem 1.1 and its Mahler example.
This supplies adequate attribution for established coefficient continuity; no novelty claim is made.
A Chern--Vaaler continuity estimate and broader noncommutative potential results were search leads, not theorem inputs.
No numerical experiment or source-priority claim is made.

Fix integers l<=u, put n=u-l, and let a belong to C^(n+1).
Set
\[
p_a(z)=\sum_{j=l}^u a_jz^j,
\quad f_a(z)=z^{-l}p_a(z)=\sum_{j=0}^n a_{l+j}z^j.
\]
Haar measure mu on T has mass one.
Define D(a)=exp L(a), where
\[
L(a)=\int_{\mathbb T}\log|p_a|\,d\mu,
\qquad L(0)=-\infty,\quad D(0)=0.
\tag{1}
\]
For nonzero a, the logarithmic singularities at the finitely many circle roots are integrable.
Multiplication by z^l changes neither functional.
Jensen gives, for the actual degree d and leading coefficient c of f_a,
\[
D(a)=|c|\prod_{j=1}^d\max(1,|\alpha_j|).
\tag{2}
\]
This classical identity is used at its established scope; roots at zero and repeated roots are counted with multiplicity.
All continuity, compactness and perturbation assertions below fix n.
No bound uniform in growing degree, coefficient scale or matrix size is claimed.

The following is a self-contained coefficient account built from (2), elementary finite-dimensional algebra and explicitly justified integration.
Its proper fixed home is a synthesis/analysis record, not a new Claim merely re-registering classical continuity.

<a id="coefficient-global-continuity"></a>
## 2. Global continuity, including degree loss and the zero vector

**Statement.**
D is continuous and strictly positive off zero on the whole fixed coefficient space.
L is finite and continuous off zero and tends to -infinity when a tends to zero.
Thus L is continuous with values in [-infinity,infinity) in the extended-real topology.
For every a,
\[
2^{-n}\|a\|_\infty\le D(a)\le \sum_{j=l}^u|a_j|.
\tag{3}
\]

**Proof.**
For n=0 these are the facts D(a)=|a_l|.
For n>0 homogenize to the binary form
\[
F_a(X,Y)=\sum_{j=0}^n a_{l+j}X^jY^{n-j}.
\]
Every nonzero F_a factors over C as
\[
F_a=c\prod_{j=1}^n(\alpha_jX+\beta_jY),
\qquad \max(|\alpha_j|,|\beta_j|)=1.
\tag{4}
\]
Factors with alpha_j=0 retain the roots at infinity responsible for degree drops.
Jensen for the linear factor, including its constant case, gives D(alpha_j z+beta_j)=max(|alpha_j|,|beta_j|)=1.
Multiplicativity in (2) therefore gives D(a)=|c|.
Each coefficient in (4) has modulus at most binomial(n,j)|c|, proving the lower bound in (3).
The pointwise estimate |p_a|<=sum|a_j| and (1) give its upper bound.

Let a^(k)->a.
When a^(k) is nonzero, choose any normalized factorization (4).
Its c_k are bounded by (3), and all normalized pairs belong to the compact set {max(|alpha|,|beta|)=1}.
Every subsequence therefore has a further subsequence on which c_k and each of the finitely many ordered pairs converge.
Their polynomial products converge coefficientwise to
\[
F_a=c\prod_{j=1}^n(\alpha_jX+\beta_jY),
\qquad \max(|\alpha_j|,|\beta_j|)=1.
\]
If a is nonzero, c is nonzero and (2) gives D(a)=|c|=lim D(a^(k)).
If a=0, the upper bound (3) gives the same conclusion directly.
Zero members of a sequence cause no problem.
Every subsequence has a subsubsequence with the claimed limit, so the entire sequence converges in D.
Positivity, continuity of log away from zero, and the upper bound at zero prove the assertions for L.
No global labeling or differentiability of roots, and no fixed effective degree, was assumed.

In particular a small highest coefficient need not be handled by ignoring the roots it sends to infinity: the homogeneous factorization keeps their compensating leading-coefficient factors.
This is why (2) at the current degree alone must not be differentiated across a degree drop without a separate argument.

<a id="coefficient-regularized-variation"></a>
## 3. Regularized variations and potential-theoretic properties

For epsilon>0 let
\[
L_\varepsilon(a)=\frac12\int\log(|p_a|^2+\varepsilon^2)\,d\mu,
\qquad D_\varepsilon(a)=e^{L_\varepsilon(a)}.
\tag{5}
\]
These are real analytic in the real and imaginary coefficient coordinates: near any fixed coefficient vector the positive denominator is bounded below by epsilon^2, and convergent local power series or bounded derivatives can be integrated on the compact circle.
If h and k are coefficient directions, write p_h and p_k for the corresponding Laurent polynomials and s=|p_a|^2+epsilon^2.
The real first and mixed second variations are
\[
DL_\varepsilon(a)[h]
=\operatorname{Re}\int\frac{p_h\overline{p_a}}s\,d\mu,
\tag{6}
\]
\[
D^2L_\varepsilon(a)[h,k]
=\int\left(
\frac{\operatorname{Re}(p_h\overline{p_k})}s
-\frac{2\operatorname{Re}(p_h\overline{p_a})
\operatorname{Re}(p_k\overline{p_a})}{s^2}
\right)d\mu.
\tag{7}
\]
These follow by differentiating (5) under the integral.
On a holomorphic affine line a+t h, the complex mixed derivative at t=0 is
\[
\partial_t\partial_{\bar t}L_\varepsilon(a+t h)\big|_0
=\frac{\varepsilon^2}{2}\int
\frac{|p_h|^2}{(|p_a|^2+\varepsilon^2)^2}\,d\mu\ge0.
\tag{8}
\]
For nonzero h it is strictly positive, because a nonzero Laurent polynomial has only finitely many zeros on T.
Thus each regularization is strictly plurisubharmonic, although its real Hessian (7) is not asserted positive semidefinite.

For a!=0, the integrable logarithm in (1) and monotone convergence applied to a common upper constant minus log(|p_a|^2+epsilon^2) give L_epsilon(a) down to L(a).
At zero, L_epsilon(0)=log epsilon down to -infinity.
The functions are locally bounded above uniformly for 0<epsilon<=1.
Passing to the decreasing limit in the submean inequality on any complex coefficient line is justified by monotone convergence of a common upper constant minus the boundary values.
The limit is upper semicontinuous by Section 2 and is not identically -infinity on the coefficient space.
Consequently **L is plurisubharmonic**, in the standard definition of upper semicontinuity and subharmonic restrictions to complex lines.
The proof is given here as an elementary consequence of (8); no general noncommutative plurisubharmonicity theorem is being invoked.

Exponentiation also gives **D plurisubharmonic**: the same holds for D_epsilon, since the Laplacian of exp(v) is exp(v)(Delta v+|grad v|^2) on each complex line; their decreasing limit D is continuous and satisfies the submean inequality by bounded convergence.
This property does not imply real convexity.

There is a useful fixed-support uniformity statement.
For any compact K avoiding a=0,
\[
\sup_{a\in K}(L_\varepsilon(a)-L(a))\longrightarrow0.
\tag{9}
\]
Indeed, for a given positive delta and each a choose epsilon_a with L_epsilon_a(a)-L(a)<delta/2.
Continuity supplies a neighborhood on which the difference is less than delta.
A finite subcover and the smallest of its epsilon_a, together with monotonicity, proves (9).
The same proof for the continuous functions D_epsilon and D proves uniform convergence of D_epsilon on every compact coefficient set, including zero.
This argument supplies no derivative convergence at a circle crossing and no quantitative rate uniform in n.

<a id="coefficient-zero-free-derivatives"></a>
## 4. The precise smooth domain and ordinary variations

Let
\[
\Omega=\{a:p_a(z)\ne0\text{ for every }z\in\mathbb T\}.
\tag{10}
\]
It is open, because the minimum circle modulus is positive at each of its points.
Both D and L are real analytic on Omega, regardless of repeated roots away from T or changes of effective degree.
If a belongs to Omega and p_h is small uniformly on T, the power series for log(1+p_h/p_a) gives
\[
L(a+h)-L(a)
=\operatorname{Re}\int\log(1+p_h/p_a)\,d\mu.
\tag{11}
\]
The series is uniformly absolutely convergent after shrinking the coefficient neighborhood.
Its integrated expression is holomorphic in h, so L is pluriharmonic there.
In particular
\[
DL(a)[h]=\operatorname{Re}\int\frac{p_h}{p_a}\,d\mu,
\qquad
D^2L(a)[h,k]=-\operatorname{Re}\int\frac{p_hp_k}{p_a^2}\,d\mu.
\tag{12}
\]
For a twice real-differentiable curve a(t) staying in Omega,
\[
\frac{dL}{dt}=\operatorname{Re}\int\frac{\dot p}{p}\,d\mu,
\qquad
\frac{d^2L}{dt^2}=\operatorname{Re}\int
\left(\frac{\ddot p}{p}-\frac{\dot p^2}{p^2}\right)d\mu.
\tag{13}
\]
Finally
\[
DD(a)[h]=D(a)DL(a)[h],\quad
D^2D(a)[h,k]=D(a)\bigl(D^2L(a)[h,k]+DL(a)[h]DL(a)[k]\bigr).
\tag{14}
\]
On every compact subset of Omega, the circle modulus has a uniform positive lower bound.
Formulas (6)--(8) and their further fixed-order derivatives therefore converge uniformly to the corresponding ordinary derivatives as epsilon goes to zero.
Mere nonvanishing of the determinant value, which holds at every nonzero scalar polynomial, is a weaker condition than membership in Omega.

The function D is real-valued, and it is not a holomorphic determinant in its coefficient variables.
A positive real-valued holomorphic function would be locally constant, whereas scaling p by positive real numbers scales D.
L is the real part of a local holomorphic function on Omega, not itself a nonconstant holomorphic function.

<a id="coefficient-circle-crossings"></a>
## 5. Circle crossings, repeated roots and failure of unrestricted differentiation

**Every nonzero polynomial with a circle root is a point of real nondifferentiability of L and D in the full coefficient space.**
To see this without assuming simple roots, consider the smooth coefficient curve
\[
p_t(z)=p_a(e^{-t}z)=\sum_{j=l}^u e^{-jt}a_jz^j.
\tag{15}
\]
Write f_a(z)=c product_(j=1)^d(z-alpha_j) at its actual degree.
Jensen gives the exact formula
\[
L(p_t)=\log|c|-(l+d)t
+\sum_{\alpha_j\ne0}\max(0,\log|\alpha_j|+t).
\tag{16}
\]
The zero roots contribute zero.
The difference of the right and left derivatives at t=0 is exactly the total multiplicity of roots on T.
A Frechet derivative in coefficient space would give a single two-sided derivative along (15), so it cannot exist.
As D(a)>0, exponentiation gives the same derivative jump multiplied by D(a).
At a=0, D is also not real Frechet differentiable: D(th)=|t|D(h) for every nonzero h, whose opposite one-sided derivatives cannot be values of a single linear map.
L has no finite value there.
Together with Section 4, this identifies the exact real differentiability locus of D as Omega, and that of the finite-valued L as Omega.

For an explicit root-level directional description, suppose that a one-real-parameter family has fixed degree d, a nonzero differentiable leading coefficient c(t), and differentiable root labels alpha_j(t) near t=0.
These hypotheses hold, for example, when all roots are simple and the coefficients are C^1; the local simple-root implicit equation supplies the labels.
They are not assumed at an arbitrary repeated-root family.
Put v_j=Re(alpha'_j(0)/alpha_j(0)) for the roots that are outside or on T at zero.
Then
\[
L'_+(0)=\operatorname{Re}\frac{c'(0)}{c(0)}
+\sum_{|\alpha_j(0)|>1}v_j
+\sum_{|\alpha_j(0)|=1}\max(v_j,0),
\tag{17}
\]
\[
L'_-(0)=\operatorname{Re}\frac{c'(0)}{c(0)}
+\sum_{|\alpha_j(0)|>1}v_j
+\sum_{|\alpha_j(0)|=1}\min(v_j,0).
\tag{18}
\]
Here the left derivative is the usual quotient with t<0.
The formulas follow term by term from (2) and log|alpha_j(t)|=t v_j+o(t) at a circle root.
Interior roots stay strictly inside, so even zero interior roots require no quotient by alpha_j.
Tangential crossings v_j=0 can have a two-sided first derivative along that particular curve, without restoring Frechet differentiability in all coefficient directions or a second derivative.

The basic affine crossing p_t(z)=z-(1+t), for small real t, has
\[
D(p_t)=\max(1,|1+t|),\qquad
L(p_t)=\max(0,\log|1+t|).
\tag{19}
\]
Its first derivatives at zero are 0 from the left and 1 from the right.
In contrast, (6) at t=0 gives
\[
\frac{d}{dt}L_\varepsilon(p_t)\big|_0
=\int\frac{1-\cos\theta}{2(1-\cos\theta)+\varepsilon^2}\,
\frac{d\theta}{2\pi}\longrightarrow\frac12.
\tag{20}
\]
The integrand is between zero and one half and tends to one half away from theta=0.
Thus even a convergent regularized gradient at a crossing is not a derivative of L there.
Formally putting epsilon=0 in a nonintegrable quotient or ignoring the moving zero would give an invalid general derivative rule.

Repeated roots create a stronger obstruction.
Let p_s(z)=(z-1)^2-s.
For 0<s<1 the roots 1+sqrt(s) and 1-sqrt(s) give
\[
D(p_s)=1+\sqrt s,\qquad L(p_s)=\log(1+\sqrt s).
\tag{21}
\]
For s<0 the two roots have modulus sqrt(1-s), hence D(p_s)=1-s and L(p_s)=log(1-s).
The coefficient distance to p_0 is |s|, but the increase for s>0 is of order sqrt(s).
Neither D nor L is locally Lipschitz at this nonzero coefficient vector, and the positive directional difference quotient is unbounded.

More generally, for an integer m>=2 and s>0, the roots of (z-1)^m-s are 1+s^(1/m)zeta_j for the m-th roots of unity zeta_j.
The finite Taylor expansions of log|1+r zeta_j|, with r=s^(1/m), give
\[
L((z-1)^m-s)=b_m s^{1/m}+O(s^{2/m}),
\quad b_m=\sum_{j=1}^m\max(\operatorname{Re}\zeta_j,0)>0.
\tag{22}
\]
The positive-part map is Lipschitz, so the O(r^2) remainder survives taking positive parts even when Re zeta_j=0.
Consequently no local Holder estimate with exponent greater than 1/m holds at this vector for D or L.
This is an obstruction, not a claim of an optimal positive Holder theorem throughout the coefficient space.

Effective-degree change alone has no such implication.
The family 1+t z lies in Omega for |t|<1 and has D=1, L=0 even at its degree drop t=0.
The monomial family t z^j has D=|t| and L=log|t|, displaying instead the zero-polynomial boundary.
Repeated roots off T remain covered by (11), regardless of the failure of individual root labels to be differentiable.

<a id="coefficient-optimizer-degeneration"></a>
## 6. Optimizer degeneration and value versus derivative limits

The positive-weight baseline has the exact regularized optimizer
\[
w_\varepsilon(z)=(|p_a(z)|^2+\varepsilon^2)^{-1},
\qquad
\frac{dL_\varepsilon}{d\varepsilon}
=\varepsilon\int w_\varepsilon\,d\mu.
\tag{23}
\]
For a in Omega the weights converge uniformly to |p_a|^-2, which is bounded above and below.
If p_a has any circle root, their essential suprema are epsilon^-2 and no bounded limiting optimizer exists.
Although a point has zero measure, continuity makes every neighborhood contain values arbitrarily close to that supremum.
This explains why D(a)>0 at a circle-zero polynomial does not imply bounded invertibility or attainment in the bounded-weight class.

There is also an exact order of degeneration for each fixed nonzero polynomial.
If its largest circle-root multiplicity is k>=1, then as epsilon goes to zero,
\[
\int w_\varepsilon\,d\mu
=\Theta_p(\varepsilon^{1/k-2}),
\qquad
L_\varepsilon(p)-L(p)=\Theta_p(\varepsilon^{1/k}).
\tag{24}
\]
To prove this, select disjoint short arcs about the distinct circle roots.
At a root of multiplicity q, factorization and the nonvanishing remaining factor give constants 0<c<C, depending on p and the arc, with c|theta-theta_0|^q <= |p(e^(i theta))| <= C|theta-theta_0|^q.
Comparing the integral of w_epsilon on this arc with integrals of (c^2 x^(2q)+epsilon^2)^-1 and (C^2 x^(2q)+epsilon^2)^-1, and substituting x=epsilon^(1/q)y, gives order epsilon^(1/q-2).
The integrals of (1+y^(2q))^-1 over the expanding scaled arcs have positive finite limits, since 2q>1.
The complement of the root arcs contributes O_p(1).
The largest multiplicity k has the most negative exponent, so the finite sum gives the first assertion.
Integrate (23) from eta to epsilon and let eta decrease to zero, using the value convergence already proved.
The positive integrand has order t^(1/k-1), integrable at zero, which proves the second assertion.

For a zero-free nonzero polynomial, w_epsilon stays uniformly bounded and the error is O_p(epsilon^2), directly from log(1+x)<=x.
For p=0, L_epsilon=log epsilon and D_epsilon=epsilon, so an error relative to the value L(0)=-infinity is not a finite expression.
All constants in (24) are input-dependent; they must not be read as degree-uniform or as preserving an integer Mahler gap.

<a id="coefficient-convexity-controls"></a>
## 7. Convexity controls

L is neither real convex nor real concave, already on nonzero constant polynomials.
For convexity, p=1 and q=3 have midpoint 2, with log2>(log1+log3)/2.
For concavity, p=1+i and q=1-i have midpoint 1, with log1<(log|1+i|+log|1-i|)/2.
These examples avoid the extended value -infinity altogether.

D is not real concave on any coefficient space: opposite nonzero constant coefficients have a zero midpoint.
For an exponent interval of length n>=2, it is also not real convex.
Indeed
\[
p(z)=(z+1)^2,\quad q(z)=-(z-1)^2,
\quad D(p)=D(q)=1,\quad D((p+q)/2)=D(2z)=2.
\tag{25}
\]
Multiplication by z^l places these examples in any such interval.
For n=0, D=|a_l|, and for n=1, D=max(|a_l|,|a_(l+1)|); these particular small spaces are convex norm examples.
Thus the nonconvexity assertion has its proper support threshold.
None of these real convexity failures conflicts with the complex-line submean inequalities in Section 3.

<a id="coefficient-matrix-transfer"></a>
## 8. Finite-matrix coefficient transfer and its singular locus

Fix r>=1 and the same finite interval.
Let
\[
P_A(z)=\sum_{j=l}^u A_jz^j,
\qquad q_A(z)=\det P_A(z).
\]
Its scalar Laurent exponent interval is contained in {r l,...,r u}; the coefficient map A -> coefficients(q_A) is a holomorphic polynomial map of the finite collection of matrix entries.
With the ordinary normalized trace tr_r tensor tau, the [accepted abelian reduction](../audits/literature/Luc22/Yin_U002.md#luc22-abelian-matrix-approximation) and the Task's ordinary-kernel convention give
\[
L_r(A)=\frac1r L(q_A),\qquad
D_r(A)=D(q_A)^{1/r},
\tag{26}
\]
where L_r=-infinity and D_r=0 if q_A is identically zero.
In that latter case every circle matrix is singular, so the ordinary determinant does include zero spectral mass.
For q_A!=0, the matrix is invertible except at finitely many circle points, and (26) is finite.
The unnormalized total logarithm is r L_r=L(q_A), never silently L_r.

It follows from Sections 2--3 and the polynomial coefficient map that **D_r is continuous on the entire matrix coefficient space**.
The extended-real L_r is continuous, finite exactly where q_A is not identically zero, and tends to -infinity on approach to the identically singular determinant locus.
Thus continuity at a singular matrix polynomial is stronger than a formula limited to a generic invertible coefficient tuple.

The function L_r is plurisubharmonic.
One direct proof, avoiding any smoothness assumption on the determinant zero set, replaces L(q_A)/r by
\[
\frac1{2r}\int\log(|q_A(z)|^2+\varepsilon^2)\,d\mu.
\tag{27}
\]
For a holomorphic affine line in A, q_A(z) is a holomorphic polynomial in its line parameter, and its complex mixed derivative in (27) is epsilon^2 |partial_t q_A|^2/[2r(|q_A|^2+epsilon^2)^2]>=0.
Pass to the decreasing limit in the submean inequality as in Section 3.
A line contained in the identically singular locus has the allowed value -infinity everywhere; the ambient function is not identically -infinity, as P_A=z^l I_r is a control.
Similarly D_r is plurisubharmonic by exponentiation and passage to the continuous limit.
Formula (27) is a scalar determinant-polynomial regularization used for this proof; it is not identified with the matrix singular-value regularization (1/(2r))int log det(P_A^*P_A+epsilon^2 I_r).

On the open set
\[
\Omega_r=\{A:\det P_A(z)\ne0\text{ for every }z\in\mathbb T\},
\tag{28}
\]
L_r is real analytic and pluriharmonic, with
\[
DL_r(A)[H]=\frac1r\operatorname{Re}\int
\operatorname{Tr}(P_A^{-1}P_H)\,d\mu,
\tag{29}
\]
\[
D^2L_r(A)[H,K]=-
\frac1r\operatorname{Re}\int
\operatorname{Tr}(P_A^{-1}P_H P_A^{-1}P_K)\,d\mu.
\tag{30}
\]
Indeed, the circle inverses are uniformly bounded.
The finite-dimensional expansion log det(I+B)=Tr(B)-Tr(B^2)/2+... converges uniformly when the operator norm of B is less than one.
Apply it to B=P_A^-1 P_H and integrate its real part.
The mixed term is (30), using cyclicity of the finite trace.
For a C^2 real curve there is the corresponding extra (1/r)Re int Tr(P_A^-1 ddot P) term and the quadratic subtraction (1/r)Re int Tr((P_A^-1 dot P)^2).
Variations of D_r follow (14) with D,L replaced by D_r,L_r.
This proof remains valid across effective-degree changes of det P_A while it has no zeros on T.

Unlike the scalar case, **no converse smoothness classification for all matrix tuples on the boundary of Omega_r is asserted**: the determinant-coefficient map can be critical and can change which scalar directions are accessible at first order.
Exact controls nevertheless force the necessary distinctions.
If P_A=diag(p,1,...,1), then D_r=D(p)^(1/r), L_r=L(p)/r, so all scalar circle-crossing and repeated-root failures survive.
The constant family diag(t,1,...,1) has D_r=|t|^(1/r), L_r=(log|t|)/r and is identically singular at t=0.
Finally, the triangular coupled polynomial
\[
P_t(z)=\begin{pmatrix}z-(1+t)&1\\0&z-2\end{pmatrix}
\]
has D_2=(2 max(1,|1+t|))^(1/2), L_2=(log2+max(0,log|1+t|))/2.
Its off-diagonal entry changes singular values and inverse matrices but not the determinant-polynomial value.
These are exact finite-matrix checks, not an assumption that every matrix variation diagonalizes coefficientwise.

<a id="coefficient-outcome-and-limits"></a>
## 9. Outcome and remaining boundaries

This account provides a complete fixed-support coefficient synthesis: all-space determinant continuity and extended logarithmic continuity; valid zero-free first/second variations; global plurisubharmonicity; the exact scalar smooth locus; simple and repeated circle-root boundaries; degree-drop and zero controls; regularized value/optimizer behavior; and the matrix transfer at its stated normalization and domains.
Classical continuity is attributed to the checked source, and Jensen to the existing accepted interface.
The elementary variation, factorization and counterexample calculations are all retained above.

It does not supply a new capacity description, a rate uniform in degree or matrix size, a complete stratum-by-stratum matrix differentiability classification, or any integer Mahler gap.
A capacity construction may use these coefficient and degeneration controls, but it must establish its own global extremum, admissible variables, determinant exponent and limiting direction.
At this writing no independent whole review has yet been performed.

<a id="coefficient-entire-author-freeze"></a>
## Entire author freeze

2026-10-13T06:37: the assigned coefficient-dependence AI self-checked and froze this entire draft, including the opening scope, all nine mathematical sections, equations (1)--(30), source roles, failures and explicit remaining limits.
The source unit and this draft both passed their scoped material checks.
Those checks validate structure, not proof.
No computer experiment, formal verification or independent whole/extraction review is claimed.
The coordinator supplied no proof steps for this account.


<a id="fixed-f0010-first-round-account"></a>
## Fixed first-round account and current inspection scope

2026-10-13T06:55.
Root fixes the ENTIRE original account above after [the separate whole independent finding](../audits/reviews/Yin_R_F0003_v1.md#coefficient-whole-independent-finding).
Only the D_G0001 same-folder links are rebased to their identical target in drafts, and outside newlines normalized.
Every formula, question, source account, unsuccessful reduction, bound, example, author check and freeze remains.
Original working-stage and pending-review wording is historical.
The fixed R owns the actual independent checks and source limits; structural validation and relocation do not add proof evidence.

The complete fixed-support coefficient synthesis passes whole review at its exact scalar and finite-matrix domains.
No new continuity theorem is claimed; full matrix boundary-stratum classification and degree-uniform estimates are outside the established scope.
This is a fixed synthesis/exploration account for F0010, not a duplicate Claim merely re-registering classical formulas.
No mathematical statement has been strengthened by organization.
The assembled Task still requires a contract-level reconciliation and corresponding completion review before any completed decision; no Task completion, G0001 resumption, native numerical run or formal verification is asserted here.


<a id="f0010-contract-closeout"></a>
## Subsequent contract closeout

2026-10-13T07:12.
The pending assembled-contract review condition recorded in the dated first-round fixed account above is now fulfilled by [R5](../audits/reviews/Yin_R_F0005_v1.md#f0010-fixed-chain-completion-finding).
The completed Task decision selects the unchanged mathematical account at its exact scope.
This status-only addition preserves every original proof, source limitation, failed candidate and historical review statement; it asserts no new theorem or enlarged review scope.

---
author: Yin
---

# Same-input tensor traces, simultaneous power tails and finite logarithmic tests

Date: 2026-11-05.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The witt_moment_compatibility delegate developed the simultaneous two-prime control and assembled this version.
The global_synthesis delegate contributed the finite tensor/truncation argument, the inspected OS23 source interface and the three-variable test.
Both contributors performed ordinary checks of their author work; the assembling delegate also checked the merged formulas and domains.
These are author-development contributions, not independent review or a new Claim assessment.

<a id="joint-tensor-tail-scope"></a>
## Question, retained input and common content decision

Does coupling several complete power resultants, or using multivariate integer logarithmic tests on the same original conjugates, supply a quantitative restriction on the complete boundary tail that the doubling comparison lacks?
The original degree and total logarithmic Mahler measure remain d and m throughout.
Neither a normalized height nor the degree of a tensor polynomial replaces them.
The intended reciprocal endpoint is an irreducible nontorsion algebraic unit whose every positive power preserves degree, but each calculation below states whether that stronger condition is actually used.

[L453 v1](Yin_L_G0453_v1.md#tensor-ghost-doubling-scope) remains fixed.
Its [same-input tensor identity](Yin_L_G0453_v1.md#same-input-tensor-and-mahler-cost), [raw/contracted comparison and finite tail](Yin_L_G0453_v1.md#contracted-trace-error-and-finite-tail), [complete Phi-2p control](Yin_L_G0453_v1.md#cyclotomic-full-ghost-and-linear-tail-control) and [negative endpoint quartic](Yin_L_G0453_v1.md#negative-quartic-original-endpoint-control) are reused at their full stated scopes.
Their complete proofs are not copied into this extension.
In particular, the old negative quartic has fixed positive total measure and the old cyclotomic control is torsion; neither establishes a small-positive-measure sequence.
The complete ghost equivalence remains at [L10 v3](Yin_L_G0010_v3.md#all-prime-ghost-equivalence).

This version extends the same raw-arithmetic versus complete logarithmic-tail inquiry, rather than introducing a new family.
[C477](../claims/Yin_C_G0477_v1.md#full-ratio-orbits) already supplies full pair-orbit integrality and multiplicities, and its [same-resultant identity](../claims/Yin_C_G0477_v1.md#symmetrized-mixed-resultant-identity) retains the original-field norm degree and the full quadratic population.
[C231](../claims/Yin_C_G0231_v1.md#mixed-power-resultant-identities) already owns the complete mixed-power composition laws, including powered-degree drops.
Its [cyclic extraction](../claims/Yin_C_G0231_v1.md#cyclic-resultant-extraction) and [gcd-corrected surplus](../claims/Yin_C_G0231_v1.md#explicit-cyclic-surplus-bound) preclude counting a shared valuation twice.
[C1](../claims/Yin_C_G0001_v1.md#doubling-exact-radial-angular-split) supplies the exact original radial/angular split, and [C4](../claims/Yin_C_G0004_v1.md#growing-band-resultant-localization) retains its growing-band complete-tail requirement.

The nonzero-spectrum product and logarithmic cutoff mechanism are also old.
The directly inspected [Sch01 source unit](../audits/literature/Sch01/Yin_U001.md#finite-quotient-determinant-proof), under "Integer products and truncated logarithms", equations (3)--(4), keeps the first nonzero integer characteristic coefficient, the kernel-mass cutoff term and the order of limits.
The closing comparison of [C110 v2](../claims/Yin_C_G0110_v2.md#original-root-precision-floor) uses the same integer nonzero-spectrum product.
The new finite calculation below applies that mechanism to the commuting tensor actions of the original P, retaining explicit zero counts and costs.
The variable-by-variable finite-grid zero bound is proved directly here; no novelty or newly acquired Schwartz--Zippel theorem is claimed.

<a id="simultaneous-two-three-full-tail"></a>
## One cyclotomic input with simultaneous doubling and tripling tails

Let p be a prime greater than three, put \(d=2(p-1)\), and take
\[
 P(X)=\Phi_{6p}(X),\qquad m(P)=0.
 \tag{1}
\]
Write \(\eta=e^{i\pi/3}\) and \(\zeta=\zeta_p\).
The full distinct roots are
\[
 \alpha_{\epsilon,j}=\eta^\epsilon\zeta^j,
 \qquad \epsilon\in\{1,-1\},\quad j\in\mathbb F_p^\times.
 \tag{2}
\]
This follows from the coprimality of 6 and p and the orders of the two displayed components.
All full integer ghost congruences and initialized polynomial recurrences hold.
Every signed-frequency moment matrix is positive semidefinite, since its quadratic form is the sum of squared absolute values over the actual unit-circle roots, exactly as in the v1 control.

For \((a,b)\) equal to \((1,2),(1,3)\) or \((2,3)\), define the entire ordered-pair polynomial
\[
 D_{ab}(t)=\prod_{i,j}(1-t\alpha_i^a/\alpha_j^b),
 \qquad
 R_{ab}=\prod_{i,j}(\alpha_i^a-\alpha_j^b).
 \tag{3}
\]
Here i and j run over all d roots, including all labels that give equal ratio values.
The root product is one, so \(|D_{ab}(1)|=|R_{ab}|\).
The ratio multiset is closed under inversion; hence its power sums are
\[
 u_{ab,n}=s_{an}s_{bn},
 \qquad s_n=\sum_i\alpha_i^n=s_{-n}.
 \tag{4}
\]
No contraction is needed for this control.

For each fixed pair of sixth-root components, the p-component \(aj-bk\) has \(p-1\) representations when it is zero and \(p-2\) when it is nonzero.
Indeed, with nonzero k fixed, j is uniquely determined; at a nonzero target exactly one k forces j to be zero.
All a and b here are nonzero modulo p.
The four sixth-root ratios are \(\eta^{a\epsilon-b\delta}\), with their repetitions retained.
Their factor polynomials are
\[
 \begin{aligned}
 H_{12}(t)&=(1+t)(1+t^3)=(1+t)^2\Phi_6(t),\\
 H_{13}(t)&=(1+t+t^2)^2=\Phi_3(t)^2,\\
 H_{23}(t)&=(1-t+t^2)^2=\Phi_6(t)^2.
 \end{aligned}
 \tag{5}
\]
For example, the first ratio list is \(\eta,\eta^{-1},-1,-1\).
The other lists are the two primitive third roots twice and the two primitive sixth roots twice, respectively.

For any one sixth-root ratio c, the p-component contribution is
\[
 (1-tc)^{p-1}\prod_{k=1}^{p-1}(1-tc\zeta^k)^{p-2}
 =(1-tc)(1-t^pc^p)^{p-2}.
\]
Since \(p\equiv1\) or \(-1\pmod6\), raising the sixth-root ratio list to p permutes it with multiplicity.
Multiplying the four contributions proves the exact identities
\[
 D_{ab}(t)=H_{ab}(t)H_{ab}(t^p)^{p-2}.
 \tag{6}
\]
Each degree is \(4+4p(p-2)=d^2\).
At the endpoint this gives simultaneously
\[
 |R_{12}|=2^d,\qquad |R_{13}|=3^d,\qquad |R_{23}|=1.
 \tag{7}
\]
Thus all three complete resultants are nonzero on the same original polynomial.

The possible shared factors can also be seen exactly:
\[
 \begin{aligned}
 D_{12}&=\Phi_2^{\,2p-2}\Phi_{2p}^{\,2p-4}
          \Phi_6^{\,p-1}\Phi_{6p}^{\,p-2},\\
 D_{13}&=\Phi_3^{\,2p-2}\Phi_{3p}^{\,2p-4},\\
 D_{23}&=\Phi_6^{\,2p-2}\Phi_{6p}^{\,2p-4}.
 \end{aligned}
 \tag{8}
\]
These follow from \(\Phi_n(t^p)=\Phi_n(t)\Phi_{np}(t)\) for \(n=2,3,6\) and \(p\nmid n\), which here is also immediate by comparing the two root-order lists.
In particular
\[
 \gcd(D_{12},D_{13})=\gcd(D_{13},D_{23})=1,
 \qquad
 \gcd(D_{12},D_{23})=\Phi_6^{\,p-1}\Phi_{6p}^{\,p-2}.
 \tag{9}
\]
The latter gcd evaluates to one at t equal to one: \(\Phi_6(1)=1\), and the displayed substitution identity gives \(\Phi_{6p}(1)=1\).
Thus this actual shared-factor structure creates no extra evaluation income beyond (7).
This is a polynomial-factor calculation, not an identification of a common ideal norm with the gcd of separately computed integer norms.

For \(0<r<1\), the complete contracted logarithmic sums are
\[
 K_{ab}(r)=-\sum_{n\ge1}\frac{r^n u_{ab,n}}n
 =\log H_{ab}(r)+(p-2)\log H_{ab}(r^p).
 \tag{10}
\]
All three H are positive on \([0,1]\).
The series is absolutely convergent at each such r, and the per-input Abel endpoint is the logarithm of (7).
For fixed r, the second term tends to zero as p tends to infinity.
In contrast, at \(r=e^{-c/p}\), with fixed \(c>0\),
\[
 \frac{K_{ab}(r)}d\longrightarrow
 \frac12\log H_{ab}(e^{-c}).
 \tag{11}
\]
In particular both base-prime energies retain a positive linear fraction at this smoothing scale.
No family-uniform interchange of the boundary and degree limits is being made.

The complete tails admit an exact finite-band description.
Set
\[
 A_N=\sum_{n=1}^N\frac{(-1)^{n+1}}n,\qquad
 H_N^{\rm harm}=\sum_{n=1}^N\frac1n,\qquad
 A_0=H_0^{\rm harm}=0.
\]
For every integer \(1\le N<p\), the factor \(H_{ab}(t^p)^{p-2}\) has no nonconstant logarithmic coefficient below p.
Expanding the elementary factors in (5) therefore gives
\[
 \begin{aligned}
 -\sum_{n=1}^N\frac{u_{12,n}}n
   &=A_N+A_{\lfloor N/3\rfloor},\\
 -\sum_{n=1}^N\frac{u_{13,n}}n
   &=2\bigl(H_N^{\rm harm}-H_{\lfloor N/3\rfloor}^{\rm harm}\bigr),\\
 -\sum_{n=1}^N\frac{u_{23,n}}n
   &=2\bigl(A_{\lfloor N/3\rfloor}-A_N\bigr).
 \end{aligned}
 \tag{12}
\]
The first quantity lies in \((0,2]\).
The second is at most three.
For the latter bound, within a block \(N=3k,3k+1,3k+2\) the difference is maximal at \(3k+2\); these maxima decrease because
\[
 \frac1{3k+3}+\frac1{3k+4}+\frac1{3k+5}
       -\frac1{k+1}<0.
\]
The first maximum is \(H_2^{\rm harm}=3/2\).
This proves the stated bound including \(N=1,2\).

Define the complete Abel tails with no deleted frequencies by
\[
 {\cal T}_{ab,N}
 =-\lim_{r\uparrow1}\sum_{n>N}\frac{r^n u_{ab,n}}n.
\]
The finite endpoint products and (12) prove
\[
 \begin{aligned}
 {\cal T}_{12,N}
   &=d\log2-A_N-A_{\lfloor N/3\rfloor}
     \ge d\log2-2,\\
 {\cal T}_{13,N}
   &=d\log3
       -2\bigl(H_N^{\rm harm}-H_{\lfloor N/3\rfloor}^{\rm harm}\bigr)
     \ge d\log3-3.
 \end{aligned}
 \tag{13}
\]
One may take \(N=p-1=d/2\), so both linear incomes escape the same degree-linear initial band.
The cross-resultant's full energy is zero and its finite band is the bounded third expression of (12); its tail is exactly the negative of that expression.
The calculation retains their actual joint dependence rather than treating the three spectra as independent.

This control remains outside the nontorsion all-power endpoint.
Every root is torsion, and cubing a root of order 6p gives order 2p, decreasing the minimal degree from \(2(p-1)\) to \(p-1\).
The full powered polynomial in the resultant still retains all original labels, with the corresponding repeated images.
The control also does not satisfy nonvanishing for all positive powers: whenever q is coprime to 6p, \(P^{[q]}=P\) and \(R_{1q}=0\).
For instance q may be five when \(p\ne5\).
No perturbation producing small positive integral total measure is supplied.

<a id="joint-resultant-reuse-and-original-cost"></a>
## Existing arithmetic relations and the original-input price

Non-torsion distinguishes the preceding cyclotomic model qualitatively, but simultaneous fixed-prime saturation alone does not.
[C146](../claims/Yin_C_G0146_v1.md#two-prime-reuse-stopping-boundary) and [C226](../claims/Yin_C_G0226_v1.md#lehmer-joint-prime-control) retain the actual Lehmer input with both base norms \(2^{10}\) and \(3^{10}\).
[C231's exact surplus control](../claims/Yin_C_G0231_v1.md#explicit-cyclic-surplus-bound) additionally retains \(|R_{23}|=1\), \(I_2^2=9\), \(I_3^2=1\), and normalized base resultants of absolute value one.
Its cyclic data \(c_1=c_2=c_3=c_5=c_6=-1\), \(c_4=-9\) give \(t_2=t_3=1\); the nine in the cyclic factor at p equal to three is already contained in its \(3^{10}\) floor.
The original input is an irreducible Salem unit with one outside root, so the unique-outside-root argument preserved in v1 proves all-positive-power degree preservation.
Its total measure is fixed and positive.
It therefore prevents inferring torsion or a universal extra factor from these two saturated floors and the unit cross-resultant, without deciding what happens under an additional small-total-measure hypothesis.

The nearby mixed-defect approach already retains genuinely joint information.
[C149](../claims/Yin_C_G0149_v1.md#integral-three-defect-identity) proves the nonvanishing alternative for the original normalized second, third and fifth powers, and its [original polynomial norms](../claims/Yin_C_G0149_v1.md#original-polynomials-and-norms) retain degrees \(6d,10d,15d\) and denominators \(72,800,30375\).
[C150](../claims/Yin_C_G0150_v1.md#weighted-valuation-comparison) compares the weighted ideals by \(125{\cal A}\subseteq{\cal D}\subseteq{\cal A}\), with equality away from five and index at most \(5^{3d}\).
Its [actual reciprocal unit control](../claims/Yin_C_G0150_v1.md#actual-unit-defect-ideal-control) realizes zero extra common-ideal income.
[C151](../claims/Yin_C_G0151_v1.md#untransformed-three-defect-energy-obstruction) already excludes the named below-one quadratic certificates for that untransformed tuple.
Those full arguments are reused rather than redeveloped as a new mixed-defect norm construction.

For a genuine reciprocal nontorsion original input, let \(\ell_i=\log|\alpha_i|\), so \(\sum_i\ell_i=0\) and \(\sum_i|\ell_i|=2m\).
For distinct positive a,b the complete radial split is
\[
 B_{ab}=\frac12\sum_{i,j}|a\ell_i-b\ell_j|
       \le(a+b)dm,\qquad
 K_{ab}=\log|R_{ab}|-B_{ab}.
 \tag{14}
\]
This is C1's split with the displayed exponents; every one of the \(d^2\) labels remains.
The two existing Frobenius floors give only
\[
 K_{12}+K_{13}\ge d\log6-7dm.
 \tag{15}
\]
No extra income follows merely by adding them.

For completeness, the v1 comparison applies with its exact exponent cost.
Put \(\beta_{ij}=\alpha_i^a/\alpha_j^b\), let \(z_{ij}\) have the same argument and modulus \(e^{-|\log|\beta_{ij}||}\), and set
\[
 u_{ab,n}=s_{an}s_{bn},\qquad C_{ab,n}=\sum_{i,j}z_{ij}^n.
\]
Conjugation makes both quantities real.
The proved v1 contraction step with \(|\log|\beta_{ij}||\le(a+b)m\) gives
\[
 |u_{ab,n}-C_{ab,n}|\le2n e^{(a+b)nm}B_{ab}.
 \tag{16}
\]
Consequently, for every \(0<r<1\) and \(N\ge1\),
\[
 \left|K_{ab,r}+\sum_{n=1}^N\frac{r^nu_{ab,n}}n\right|
 \le2B_{ab}\sum_{n=1}^N(re^{(a+b)m})^n
       +\frac{d^2r^{N+1}}{(N+1)(1-r)}.
 \tag{17}
\]
Here \(K_{ab,r}=\sum_{i,j}\log|1-rz_{ij}|\).
This is a direct substitution into the existing finite proof, not an additional convergence theorem.
For \((1,2),(1,3),(2,3)\), the exponential costs are respectively \(3m,4m,5m\).
All complete tails and actual radial smoothing survive the coupling.

<a id="finite-tensor-truncation"></a>
## Finite multivariate integer tests with their zero penalty

Let P be any monic separable integer polynomial of degree \(d\ge1\), with distinct roots \(\alpha_1,\ldots,\alpha_d\).
Define the empirical probability measure
\[
 \nu_P=\frac1d\sum_i\delta_{\alpha_i}.
\]
Fix a nonzero \(Q\in\mathbb Z[x_1,\ldots,x_r]\), with \(r\ge1\), total degree s, and cutoff \(M>0\).
This finite statement allows reducible P and zero roots; the later applications restore the original irreducible unit domain.

On the free integer module \((\mathbb Z[X]/(P))^{\otimes r}\), let \(A_a\) be the companion action in the a-th tensor coordinate and the identity in every other coordinate.
These are commuting integer matrices of size \(d^r\).
Separability simultaneously diagonalizes them in the tensor eigenbasis over a splitting field.
Thus
\[
 T_Q=Q(A_1,\ldots,A_r)
\]
has exactly the \(d^r\) eigenvalues
\[
 q_{\boldsymbol i}=Q(\alpha_{i_1},\ldots,\alpha_{i_r}),
 \qquad \boldsymbol i\in\{1,\ldots,d\}^r,
 \tag{18}
\]
including every repeated value and every zero label.

Let Z be the number of zero values in (18).
The integer characteristic polynomial has the form
\[
 \det(tI-T_Q)=t^Z(C_Q+O(t)),\qquad
 C_Q=(-1)^{d^r-Z}\prod_{q_{\boldsymbol i}\ne0}q_{\boldsymbol i}
       \in\mathbb Z\setminus\{0\}.
 \tag{19}
\]
If all values are zero, \(C_Q=1\) is the empty product.
Taking absolute values therefore gives
\[
 \sum_{q_{\boldsymbol i}\ne0}\log|q_{\boldsymbol i}|
       =\log|C_Q|\ge0.
\]
This is exactly the reused nonzero-spectrum coefficient mechanism.

For the continuous truncated logarithm
\[
 g_M(\boldsymbol z)=\log\max(|Q(\boldsymbol z)|,e^{-M}),
\]
the same product probability, with no conditioning or removed labels, satisfies
\[
 \begin{aligned}
 d^r\int g_M\,d\nu_P^{\otimes r}
 &=-MZ+\sum_{q_{\boldsymbol i}\ne0}
                     \max(\log|q_{\boldsymbol i}|,-M)\\
 &\ge\log|C_Q|-MZ.
 \end{aligned}
 \tag{20}
\]

The elementary finite-grid root bound is
\[
 Z\le s d^{r-1}.
 \tag{21}
\]
For r equal to one this is the univariate root bound.
For \(r>1\), write
\[
 Q=\sum_{j=0}^t q_j(x_1,\ldots,x_{r-1})x_r^j,
 \qquad q_t\ne0,\qquad \deg q_t\le s-t.
\]
By induction the number B of preceding tuples where \(q_t\) vanishes is at most \((s-t)d^{r-2}\).
Each such tuple contributes at most d zeros.
Every other tuple gives a nonzero univariate polynomial of degree t and at most t zeros.
It follows that
\[
 Z\le Bd+(d^{r-1}-B)t
   \le Bd+t d^{r-1}
   \le s d^{r-1}.
\]
This also covers \(t=0\) and constant nonzero Q.
If \(s\ge d\), the estimate may be trivial but remains valid.

Combining (20)--(21) proves the finite bound
\[
 \int g_M\,d\nu_P^{\otimes r}
 \ge\frac{\log|C_Q|}{d^r}-\frac{MZ}{d^r}
 \ge-\frac{Ms}{d}.
 \tag{22}
\]
The original unnormalized cutoff expense is \(MZ\le Ms d^{r-1}\), not \(O(Ms)\).
Neither tensor multiplicity nor sampling normalization has been changed.

<a id="fixed-test-limits-and-os23-scope"></a>
## Fixed tests, order of limits and the actual OS23 interface

Suppose monic separable \(P_j\) have \(d_j\to\infty\), all roots in one compact set K, and \(\nu_{P_j}\) converge weakly to \(\mu\).
For fixed Q, r and M, \(g_M\) is continuous and bounded on \(K^r\).
Product weak convergence and (22) give
\[
 \int g_M\,d\mu^{\otimes r}\ge0.
 \tag{23}
\]
Choose \(C\ge\max(0,\sup_{K^r}\log|Q|)\).
Then \(C-g_M\) increases nonnegatively as M tends to infinity.
Monotone convergence proves
\[
 \int\log|Q|\,d\mu^{\otimes r}\ge0,
 \tag{24}
\]
and in particular the negative part is integrable.
The order is degree/weak limit at fixed cutoff, then cutoff removal.
This is not determinant convergence and supplies no rate uniform in a moving Q, r or M.

For example \(Q_j=P_j(x_1)\) has \(s_j=d_j\) and \(Z=d_j^r\).
Its untruncated empirical integral is minus infinity and (22) gives only the cutoff value \(-M\).
Thus the condition \(\int\log|A|\,d\mu\ge0\) for every nonzero integer univariate A cannot be applied directly to the finite empirical measure \(\nu_P\), since A may be P itself.

The inspected external comparison is Orloski--Sardari, *Limiting Distributions of Conjugate Algebraic Integers*, OS23, [arXiv:2302.02872v2](https://arxiv.org/html/2302.02872v2), 5 April 2024.
The global_synthesis contributor actually read Theorem 1.8, Section 2.4 Proposition 2.12 and its proof, the Theorem 1.8 induction and equations (37)--(41), and the directly used displayed approximation from Proposition 2.11.
This is bounded source preparation, not a whole-source audit.
No MS26 source statement is used for the finite-grid zero estimate.

At that version's compact-support and conjugation-invariance scope, Theorem 1.8 identifies the nonnegative integer univariate logarithmic-test condition with the corresponding condition for all arities and nonzero integer Q under product measure.
Proposition 2.12 regularizes a measure already in the source's arithmetic class \(B_\Sigma\) to a Holder measure while retaining that property.
It does not prove that a small-radius smoothing of an arbitrary finite \(\nu_P\) lies in that class.

In the inspected induction, after factoring and reducing to an irreducible genuinely mixed Q, fixed \(\mu\) and Q give a root-fiber measure \(\mu_Q\) whose mass is \(\deg_{x_r}Q\), and a nonnegative leading-coefficient integral.
The source's Proposition 2.11 supplies an auxiliary polynomial of degree at most N and a potential approximation.
The nonnegative leading-coefficient integral permits replacing that degree by N in the lower estimate in equations (40)--(41).
Integration and the lower-arity integer resultant give an error of the form
\[
 -C\,\deg_{x_r}(Q)/N^\eta,
\]
followed by \(N\to\infty\).
This N is the source's auxiliary degree, not the original degree d.
The regularity and approximation constants do not provide a uniform finite-input rate for the discrete measures \(\nu_P\).
Moving-test coefficients, degrees, arities, test norms and convergence dependencies therefore remain actual expenses.

The diagonal example makes the sampling distinction explicit.
For \(Q=x-y\), exactly d ordered labels on the original separable grid are zero.
The absolute nonzero product is \(|\operatorname{disc}P|\ge1\), but the full empirical logarithmic integral is minus infinity.
Keeping \(\nu_P^{\otimes2}\) gives the cutoff penalty \(-M/d\) in (20).
Deleting the diagonal and dividing by \(d(d-1)\), when \(d>1\), instead samples conditioned distinct labels.
That different probability is not the product measure in the source theorem.

<a id="finite-doubling-logarithmic-test"></a>
## The two-variable test returns exactly the old doubling floor

Take \(Q(x,y)=x-y^2\) and the actual irreducible nontorsion unit P.
The full ratio result of C477 excludes every equality \(\alpha_i=\alpha_j^2\), so Z is zero.
The complete ordered product is the original mixed resultant, and hence
\[
 \int\log|x-y^2|\,d\nu_P^{\otimes2}
 =\frac{\log|\operatorname{Res}(P,P^{[2]})|}{d^2}
 \ge\frac{\log2}{d}.
 \tag{25}
\]
It is also the absolute field norm of \(P(\alpha^2)\), with original norm degree d and auxiliary \(P(X^2)\) of degree \(2d\).
Those original-field facts do not remove the \(d^2\) logarithmic pair population.

For reciprocal P, its radial term is
\[
 B=\frac12\sum_{i,j}|\ell_i-2\ell_j|\le3dm,
\]
and the angular remainder is exactly C1's \(K\ge d\log2-3dm\).
All v1 contraction and complete-tail costs remain.
The fixed limiting lower bound zero in (24) discards the normalized \((\log2)/d\) floor in (25), rather than adding income.
The Haar product logarithmic integral is zero, by integrating first in x on the unit circle using the retained [Jensen identity](../audits/literature/Den09/Yin_U001.md#mahler-measure).
A sufficient comparison with that value to contradict (25) would be an upper discrepancy \(o(1/d)\) on the same singular logarithmic test, equivalently \(o(d)\) before dividing by the full pair count.
A strict coefficient improvement at the corresponding \(1/d\) scale would also suffice; qualitative convergence to zero alone would not.
The inspected source supplies no such rate.

<a id="three-variable-test-full-cost"></a>
## A three-variable test distinguishes torsion through zeros but retains a larger norm

Take \(Q(x,y,z)=x^4-yz\) and any actual monic irreducible noncyclotomic algebraic unit P.
This section does not require reciprocity or all-positive-power degree preservation.
The retained [Smy08 Kronecker normalization input](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization), at its stated source scope, gives a largest root modulus \(R>1\).
If \(\alpha_i^4=\alpha_j\alpha_k\), a splitting-field automorphism sending \(\alpha_i\) to a root of modulus R would give \(R^4\le R^2\), a contradiction.
Thus all \(d^3\) ordered-label values are nonzero, including tuples with repeated labels.

Define
\[
 H_P(t)=\prod_{j,k}(t-\alpha_j\alpha_k),\qquad
 H_{\rm off}(t)=\prod_{j<k}(t-\alpha_j\alpha_k).
\]
The coefficients are Galois-invariant algebraic integers, hence integers.
Repeated product values are retained.
Separating the diagonal from its two copies of each unordered pair gives
\[
 H_P=P^{[2]}H_{\rm off}^{\,2},\qquad
 \deg H_P=d^2,\qquad
 \deg H_{\rm off}=d(d-1)/2.
 \tag{26}
\]
For an original root \(\alpha\), take the complete norm in its degree-d field:
\[
 \begin{aligned}
 {\cal N}_4
 &=\prod_{i,j,k}(\alpha_i^4-\alpha_j\alpha_k)\\
 &=\operatorname{Norm}_{\mathbb Q(\alpha)/\mathbb Q}H_P(\alpha^4)\\
 &=R_{4,2}\,
   \bigl(\operatorname{Norm}_{\mathbb Q(\alpha)/\mathbb Q}
                         H_{\rm off}(\alpha^4)\bigr)^2.
 \end{aligned}
 \tag{27}
\]
All factors are nonzero integers.
The full auxiliary \(H_P(X^4)\) has degree \(4d^2\); the residual auxiliary \(H_{\rm off}(X^4)\) has degree \(2d(d-1)\).
[C231's old prime-power floor](../claims/Yin_C_G0231_v1.md#mixed-power-resultant-identities) gives \(2^d\mid R_{4,2}\).
The extra residual norm is a nonzero integer, but neither the source nor this factorization makes its absolute value uniformly greater than one.
Thus (27) isolates the additional quantity that would need a new quantitative lower bound.

The exact radial term of this complete three-variable product is
\[
 \begin{aligned}
 B_4
 &=\sum_{i,j,k}\max(4\ell_i,\ell_j+\ell_k)\\
 &=\frac12\sum_{i,j,k}|4\ell_i-\ell_j-\ell_k|
 \le6d^2m.
 \end{aligned}
 \tag{28}
\]
Indeed \(\sum_i\ell_i=0\) removes the half-sum in the maximum identity, while \(\sum_i|\ell_i|=2m\) gives the final triangle bound.
Its angular remainder is
\[
 K_4=\log|{\cal N}_4|-B_4.
 \tag{29}
\]
Writing \(\alpha_i=e^{\ell_i+i\theta_i}\), it is the sum over all \(d^3\) labels of
\[
 \log\left|1-
 e^{-|4\ell_i-\ell_j-\ell_k|
       +i(4\theta_i-\theta_j-\theta_k)}\right|.
\]
Factoring the larger radial modulus gives this expression; reversing its phase when necessary leaves its absolute value unchanged.
No three-variable test may retain only the old pair population or the doubling radial price \(3dm\).

On the old torsion control \(P=\Phi_{2p}\), with p odd prime and \(\alpha_i=-\zeta_p^i\), this test has exactly
\[
 Z=(p-1)(p-2)=d(d-1)
 \tag{30}
\]
zero ordered triples.
For fixed \(i\ne0\), the equation \(j+k=4i\pmod p\) permits \(p-2\) nonzero j, each with a unique nonzero k.
Here \(4i\ne0\) since p is odd.
The zero fraction is \((d-1)/d^2\); the full untruncated integral is minus infinity.
With the same sampling, (20) retains the original cutoff penalty \(Md(d-1)\).
Thus this test distinguishes that finite torsion control from a genuine noncyclotomic unit through nonvanishing, but the zero fraction tends to zero.
Its Haar product logarithmic integral remains zero, since for fixed unit-circle y,z the Jensen integral of \(x^4-yz\) is zero.
The limiting nonnegative test constraint therefore does not exclude the torsion boundary distribution.
For actual nontorsion input the precise finite distinction returns to (27), where the larger residual norm has no supplied quantitative improvement beyond integrality.

<a id="joint-tensor-return-boundary"></a>
## Result and first unsupported bridge

The simultaneous Phi-6p calculation proves that full ghost arithmetic, all signed-frequency positive moment constraints, two nonzero saturated base resultants, a nonzero cross-resultant and their actual shared polynomial factors can coexist with two complete degree-linear boundary tails.
Its torsion, tripling degree drop and failure of all-power nonvanishing are essential domain exclusions.
The actual Lehmer input separately prevents turning the two saturated base floors and a unit cross-resultant into a universal torsion test.
That fixed-positive-measure input supplies no small-total-measure sequence.

The general tensor truncation bound has explicit finite constants, original multiplicities and zero penalties.
Its limiting version uses fixed tests and the correct order of limits.
OS23 supplies no finite empirical-measure smoothing theorem or moving-logarithmic-test rate at the scale needed by (25).
The three-variable test detects a zero pattern absent for genuine noncyclotomic units, but its exact norm factors through an old prime-power resultant and a higher-degree residual norm, with all \(d^3\) labels and \(6d^2m\) radial expense retained.

The first missing step is quantitative same-input use of nontorsion, all-power stability and small total m to bound the joint complete contracted tails from above, or to force additional norm income that survives every original degree, multiplicity, radial and auxiliary cost.
Qualitative nonvanishing gives no uniform distance from the cyclotomic boundary.
Fixed-test weak limits, separate integer feasibility, assumed signs or probabilistic independence do not supply that missing estimate.
No uniform positive Mahler gap, genuine zero-gap family or unrestricted Task completion follows.

The contributors' checks covered the sixth-root multiplicities, full factorization and gcd evaluations, both exact tails, all stated degree drops, original-norm conventions, finite tensor eigenvalue labels, the zero-count induction, cutoff normalization and order of limits, and the three-variable factorization and radial price.
The OS23 source inspection has exactly the passage scope stated above; no whole-source audit, new native mathematical program or numerical experiment is claimed.
All checking has the author-development relationship already identified, not independent review.

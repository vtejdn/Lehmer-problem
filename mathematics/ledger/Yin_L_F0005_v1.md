---
author: Yin
---

# Coefficient convolution capacities for a scalar single-Haar polynomial

Date: 2026-10-13.
Human author: Yin.
Current author: assigned scalar-capacity AI agent under the authorized F0010 run.
This responsible working draft investigates exact coefficient-defined convolution/prediction capacities, finite matrix realizations, attainment and degenerations for the scalar part of F0010.
It is an author working document awaiting whole independent review.
It makes no novelty claim for classical prediction or Szego formulas, does not resume G0001, and does not assert Task completion.

## Current complete-proof home

Placement maintenance: 2026-10-21T02:33.
The substantial complete supporting argument is now retained in [C6](../claims/Yin_C_F0006_v1.md#statement), with the applicable original mathematical finding adopted at its actual unknown initial-context relationship.
The full original proof, questions, classical attribution, source-access limits, failed reductions and author freezes remain below because the old R findings, completed Task and other fixed consumers actually use these inputs.
The dated independent wording below remains its historical self-description, rather than a new certification of initial isolation.
This placement allocates no new classical discovery, theorem role or Task objective and changes no historical completion decision.

<a id="scalar-capacity-question"></a>
## Question and current scope

For an arbitrary complex Laurent polynomial on a fixed finite exponent interval, construct finite coefficient matrices and explicitly constrained extrema that recover the ordinary determinant of the polynomial in one Haar unitary, including circle zeros, degree drops and the zero polynomial.
Separate finite attainment, infinite analytic attainment and the completion of a weighted analytic space.
State approximation directions and costs.

<a id="scalar-capacity-reuse"></a>
## Bounded reuse inventory

Read the F0010 contract, S_F0025, the two elementary weight interfaces of [scalar weight baseline](Yin_L_G0431_v1.md#single-haar-formulation), [L_G4, Sections 2--4](Yin_L_G0004_v1.md#gram-lower-certificate), and [Den09-U002](../audits/literature/Den09/Yin_U002.md#finite-section-determinant).
The latter retains classical scalar Toeplitz/Szego convergence for bounded nonnegative symbols positive on a set of positive measure and the exact finite Schur residual formulas.
Its cited original Simon proof is not audited here.
These already supply the needed prediction limit, so it is an attributed baseline, not a project discovery.
Local bibliography search also located Amo97's prediction discussion; its sharper arithmetic theorem is not used.

The present assignment requires explicit arbitrary-complex-coefficient construction, constant-term normalization, all singular/zero cases and optimizer behavior, which are not supplied as one interface by the old integer orbit argument.
The direct outer-polynomial reduction and finite algebra below provide those specializations; all limits are fixed-input unless an explicit bound is displayed.

<a id="scalar-capacity-normalization"></a>
## 1. Coefficients, outer factor and normalization

Fix integers l<=u, put s=u-l and write p(z)=z^l b(z), where b(z)=sum_{j=0}^s a_j z^j.
Padding by zero coefficients is deliberate: s is the fixed input width, not a possibly discontinuous effective degree.
Write D=exp integral_T log|p|, with D=0 for p=0, and Haar probability measure throughout.
For nonzero b, factor b=A z^k product_{nu=1}^m(z-alpha_nu), where alpha_nu are the nonzero roots, counted with multiplicity.
Thus k+m<=s.
Set
\[
 D=|A|\prod_{\nu=1}^m\max(1,|\alpha_\nu|),\qquad
 g(z)=D\prod_{\nu=1}^m(1-\beta_\nu z),\quad
 \beta_\nu=\begin{cases}\overline{\alpha_\nu},&|\alpha_\nu|\le1,\\
 \alpha_\nu^{-1},&|\alpha_\nu|>1.
 \end{cases}                                                    \tag{1}
\]
Elementary factorwise modulus comparison on T gives |g|=|b|, g(0)=D>0, and g has no zero in the open unit disk.
This is the scalar outer polynomial, with the positive-at-zero normalization; it can have circle zeros.
Its degree can be smaller than s.
Jensen's one-variable root formula gives the displayed D and integral log|g|=log g(0), including repeated circle zeros.
The factor at alpha=0 is removed into z^k, whose circle modulus is one.

The classical scalar Fejer--Riesz/reciprocal-conjugate root convention is already source-checked in [DR10-U001](../audits/literature/DR10/Yin_U001.md#dr10-u001); its original historical proofs are not re-audited.
Equation(1) is only a proof device and does not enter the coefficient-defined optimization below.
Uniqueness of the normalized g follows by taking the ratio of two such factors, canceling common circle roots (equal boundary modulus gives equal multiplicity), and applying the maximum modulus principle to the ratio and its inverse on the closed disk.
Their ratio is a unimodular constant, fixed to 1 at0.

<a id="scalar-capacity-finite-sdp"></a>
## 2. An exact finite coefficient Gram capacity

Define the autocorrelations and the compact spectrahedron
\[
 c_k=\sum_{j=0}^{s-k}\overline{a_j}a_{j+k}\quad(0\le k\le s),
\]
\[
 \mathcal G_s(a)=\left\{Q\in\operatorname{Herm}_{s+1}:Q\succeq0,
       \ \sum_{j=0}^{s-k}Q_{j,j+k}=c_k\ (0\le k\le s)\right\}.
                                                               \tag{2}
\]
Only finite additions, conjugations and products of the input coefficients construct this SDP.
Let
\[
 \operatorname{Cap}^{\rm G}_s(a)=\max_{Q\in\mathcal G_s(a)}Q_{00}.
                                                               \tag{3}
\]
Then
\[
 \boxed{\operatorname{Cap}^{\rm G}_s(a)=D(p)^2,\qquad
        L(p)=\tfrac12\log\operatorname{Cap}^{\rm G}_s(a).}       \tag{4}
\]
The logarithm is -infinity at capacity0.
The optimizer is unique: for nonzero p it is
\[
 Q_* = \overline{\boldsymbol g}\,\boldsymbol g^{\mathsf T},
 \quad \boldsymbol g=(g_0,\ldots,g_s)^{\mathsf T},\quad g_0=D,
                                                               \tag{5}
\]
of rank 1; for p=0 it is Q=0.
In particular the finite maximum remains attained when p has a circle zero.
It is a maximum over PSD matrices, not an infimum over bounded inverse weights.

**Proof of both inequalities and uniqueness.**
Put v=(1,z,...,z^s)^T.
The diagonal constraints say exactly v^*Qv=|b(z)|^2 on T.
The matrix Q_a=conjugate(a) a^T is feasible.
Every feasible Q has trace c_0 and entries bounded by c_0 by PSD Cauchy--Schwarz, so the feasible set is nonempty and compact.
If c_0=0 then all a_j=0 and Q=0, proving the zero branch.

For p nonzero, factor a feasible Q into a sum of rank-one PSD matrices and write
\[
 Q=\sum_{t=1}^{s+1}\overline{\boldsymbol f_t}
              \boldsymbol f_t^{\mathsf T},\qquad
 \sum_t|f_t(z)|^2=|g(z)|^2\quad(z\in\mathbb T).                \tag{6}
\]
Zero summands are harmless.
At a circle zero zeta of g of order m, the bound |f_t|<=|g| along the circle implies that f_t vanishes at zeta to order at least m: otherwise the quotient of the two modulus orders would diverge along that arc.
Therefore F_t=f_t/g has removable singularities at those zeros and is analytic on a neighborhood of the closed disk, since all other zeros of g lie outside.
On the circle, sum_t|F_t|^2=1.
Applying Parseval to their Taylor series gives
\[
 \sum_t|F_t(0)|^2\le1,\qquad
 Q_{00}=D^2\sum_t|F_t(0)|^2\le D^2.                            \tag{7}
\]
The rank-one matrix(5) is feasible and has Q_00=D², proving equality.
Equality in Parseval in(7) forces every nonconstant Taylor coefficient of every F_t to vanish.
Thus F_t is a constant gamma_t with sum|gamma_t|²=1, so(6) equals exactly(5).
This proves uniqueness, not just existence of a rank-one optimum.

The capacity is homogeneous of degree 2: Cap^G(lambda a)=|lambda|² Cap^G(a), including lambda=0.
Laurent shifts and zero padding do not change its value, though they can change the displayed matrix size.
The maximum matrix itself need not share the original coefficient field (spectral factorization is over C).
Nothing in(4) asserts a rational optimizer, exact numerical recovery by an SDP solver, or a size bound independent of the coefficient support.
Its dimension is precisely s+1.

**Known-form attribution.**
A bounded primary search after the local inventory identifies this as the established maximum-first-Gram-entry spectral factorization construction, not a new SDP theorem.
The primary publisher record for Bogdan Dumitrescu, *Positive Trigonometric Polynomials and Signal Processing Applications*,2nd edition, chapter 2 (2017), confirms the Gram-matrix chapter and its spectral factorization content; indexed book text identifies Theorem 2.15 as the maximum q_00 rank-one/minimum-phase assertion.
The publisher full-text endpoint returned a subscription preview, so that indexed theorem locator is currently an attribution lead rather than an accepted inspected original theorem.
A second primary publisher record confirms J.W.McLean and H.J.Woerdeman, *Spectral Factorizations and Sums of Squares Representations via Semidefinite Programming*, SIAM J.Matrix Anal.Appl.23(3),646--655, DOI10.1137/S0895479800371177, with January2002 issue identity; its full PDF returned403.
The author's Drexel full-text link was located but could not be fetched (web timeout/local DNS11001).
No claim to have inspected either complete proof is made.
The self-contained argument(1)--(7) proves the exact local scalar result independently of those unchecked theorem bodies.
The later [verified primary attribution alternative in C6](../claims/Yin_C_F0006_v1.md#verified-maximum-gram-attribution) identifies MW02 Proposition 2.3 and Algorithm 1 at text-only statement/construction depth.
The original access failures and uninspected Dumitrescu lead above remain historical source limits, without imposing a missing premise on the local proof.

<a id="scalar-capacity-dual"></a>
## 3. Finite Toeplitz dual, exact equality and its attainment boundary

Let h_a=conjugate(a) be the conjugate coefficient column and E_00=e_0e_0^*.
The matching dual coefficient problem is
\[
 \operatorname{Cap}^{\rm T}_s(a)
  =\inf\{h_a^*Hh_a:H\in\operatorname{Herm}_{s+1}\text{ Toeplitz},
                         \ H\succeq E_{00}\}.                  \tag{8}
\]
It has the same value D², with the zero branch included.
It is always feasible (H=I), and the infimum is attained for nonzero p exactly when p has no unit-circle zero.
For p=0 it is attained by every feasible H.
This singular-boundary contrast is substantive: the primal maximum always exists whereas its Toeplitz dual can have no minimizer.

For weak duality, all matrices in(2) have the same pairing with every Hermitian Toeplitz H.
Thus
\[
 h_a^*Hh_a=\operatorname{tr}(HQ)\ge Q_{00}
\]
for feasible H,Q.
Taking Q=Q_* gives value at least D².

For the reverse inequality take 0<r<1, replace g(z) by g(rz), and define
\[
 (H_r)_{ij}=D^2\int_{\mathbb T}
                  \frac{z^{i-j}}{|g(rz)|^2}\,d\mu(z).
                                                               \tag{9}
\]
It is finite and Hermitian Toeplitz.
For any polynomial f of degree<=s, f/g(rz) is analytic on a neighborhood of the closed disk, and its constant term is f(0)/D.
Parseval gives h_f^*H_r h_f>=|f(0)|², so H_r>=E_00.
Its objective is
\[
 h_a^*H_rh_a=D^2\int|g(z)/g(rz)|^2\,d\mu(z)\longrightarrow D^2.
                                                               \tag{10}
\]
To justify this even at circle zeros, use(1): for |beta|<=1 and |z|=1,
|1-beta z|/|1-r beta z|<=2 by the triangle inequality and
1-r|beta|>=(1-r)|beta|.
The product is bounded by 2^s and tends to 1 off the finite zero set.
Dominated convergence proves(10).
No abstract SDP strong-duality theorem is needed.

If p has no circle zero, set r=1 in(9); the matrix is finite and gives exact equality.
Conversely every feasible Toeplitz H is positive definite.
Indeed if x is in its kernel, H>=E_00 implies x_0=0.
Let k be the first nonzero coordinate of a nonzero such x; shift the coordinates left by k and pad by zero at the end.
Toeplitz structure preserves its quadratic norm, which stays0, whereas H>=E_00 bounds it below by |x_k|²>0, a contradiction.

Suppose now equality occurs at a feasible H for nonzero p.
Complementarity with(5) gives
\[
 (H-E_{00})h_g=0,\qquad Hh_g=D e_0.                            \tag{11}
\]
Use the positive-definite polynomial inner product induced by H; conjugating coefficient columns only fixes its convention and does not affect norms.
Equation(11) says that g is orthogonal to every polynomial with zero constant term and degree<=s.
If g has a root alpha with |alpha|<=1, alpha!=0 because g(0)>0; write g=(z-alpha)f.
The polynomials f and zf both have degree<=s.
Toeplitz structure implies ||zf||_H=||f||_H, while orthogonality to zf yields
\[
 \|f\|_H^2=|\alpha|\,|\langle f,zf\rangle_H|
             < |\alpha|\,\|f\|_H^2\le\|f\|_H^2.
\]
The strict inequality is Cauchy--Schwarz for the linearly independent polynomials f,zf in a positive-definite inner product.
This contradiction excludes a circle zero.
(The equality before the strict inequality is an equality of absolute values obtained from the orthogonality equation.)
Thus the stated nonattainment is proved.

<a id="scalar-capacity-prediction"></a>
## 4. Finite convolution/prediction capacities and the exact infimum

For N>=0, form the (N+s+1)-by-(N+1) coefficient convolution matrix
\[
 (C_N(a))_{ij}=a_{i-j}\quad(0\le i\le N+s,\ 0\le j\le N),
\]
where missing coefficients are0, and put T_N=C_N^*C_N.
Define
\[
 \kappa_N(a)=\min\{\|C_N(a)q\|_2^2:q\in\mathbb C^{N+1},\ q_0=1\}.
                                                               \tag{12}
\]
For p nonzero, polynomial multiplication is injective, so T_N>0; the unique minimizer and value are
\[
 q^{(N)}=\frac{T_N^{-1}e_0}{e_0^*T_N^{-1}e_0},\qquad
 \kappa_N=\frac1{e_0^*T_N^{-1}e_0}
          =\frac{\det T_N}{\det T_{N-1}},\quad \det T_{-1}:=1.
                                                               \tag{13}
\]
Indeed q=q^(N)+v with v_0=0 makes the mixed quadratic term vanish; the cofactor formula gives the reciprocal inverse entry.
The complementary principal block is T_{N-1} by Toeplitz structure.
This is a finite positive-definite quadratic problem constructed directly from the original coefficient data.

For all inputs, including p=0,
\[
 \kappa_0\ge\kappa_1\ge\cdots\downarrow
 \operatorname{Cap}^{\rm pred}(a):=\inf_{N\ge0}\kappa_N(a)
   =D(p)^2=\operatorname{Cap}^{\rm G}_s(a).                     \tag{14}
\]
Monotonicity follows by appending a zero to an admissible q.
For nonzero p, any trial polynomial q with q(0)=1 satisfies
\[
 \|p q\|_2^2=\|gq\|_2^2\ge|g(0)q(0)|^2=D^2,                \tag{15}
\]
by the nonnegative Taylor-coefficient squares in Parseval.
For the opposite inequality take q_r(z)=D/g(rz).
Its constant term is1.
For fixed r<1 its Taylor polynomials converge uniformly on the closed disk, and hence their energies converge to ||p q_r||².
The dominated argument(10) gives ||p q_r||²->D² as r increases to 1.
This proves(14) directly, including the correct order of approximations: fix r, take polynomial degree to infinity, then take r to 1.
For the zero polynomial every q is a minimizer of value 0; inverse/determinant ratios in(13) are deliberately not used.

The positive scalar determinant also satisfies the fixed-input finite-section formula
\[
 \lim_{N\to\infty}(\det T_N)^{1/(N+1)}=D^2,                \tag{16}
\]
since det T_N=product_{j=0}^N kappa_j and the logarithmic Cesaro mean of the positive sequence kappa_j tends to logD².
For p=0, every displayed positive-size determinant is0, so(16) remains true without logarithmic division.
Equations(13)--(16) are classical prediction/Szego structure already retained by Den09-U002 and L4; their role here is explicit arbitrary-complex-coefficient and singular-case organization, not a claim of discovery.

For nonzero p, a finite N has kappa_N=D² if and only if p is a monomial.
Equality in(15) requires gq=D identically.
Since g,q are polynomials and D!=0, both must be constants.
Conversely for a monomial p, g=D and q=1 attains D² at every N.
Thus every finite prediction energy is strictly above D² for a nonmonomial, even when the finite Gram SDP(3) already has its exact maximum.
The two constructions have different optimization directions and different finite attainment properties.

<a id="scalar-capacity-analytic-attainment"></a>
## 5. Analytic admissible classes and an explicit approximation bound

The same value D² is the infimum of ||p q||² over either q in H² with q(0)=1 or q in H-infinity with q(0)=1.
The unique possible minimizer for nonzero p is
\[
 q_*(z)=D/g(z).                                                 \tag{17}
\]
Multiplication by g maps H² into H², so the proof of(15) and its equality condition apply.
The polynomial trials from Section4 prove the value in both larger classes.
If g has no circle zero, q_* is rational and analytic on a neighborhood of the closed disk, hence belongs to both classes and is the unique minimizer.
If g has a circle zero of multiplicitym>=1, 1/g has a boundary pole of that order; its squared modulus is not locally integrable there.
Consequently q_* is in neither H² nor H-infinity, and neither infimum is attained.
For p=0 every admissible q attains0.

For clarity, the weighted analytic completion is a different admissible space.
Let H²(|p|²) be the completion of analytic polynomials under ||q||_p²=integral|p q|².
For p nonzero this is a norm.
Inequality(15), without setting q(0)=1, shows that q->q(0) extends continuously.
Multiplication by g is an isometry from this completion onto H²: its closed range contains the constant 1 by the radial and Taylor approximation above after dividing byD, and multiplication by z then shows that it contains every analytic polynomial, which is dense in H².
The constraint q(0)=1 corresponds to the constant coefficient of gq beingD.
It therefore always has the unique minimizer represented almost everywhere by(17), including circle zeros.
Allowing this completion changes attainment; it does not mean that the optimizer has become bounded or has an ordinary H² norm.

An explicit finite error is available under a fixed-input spectral separation.
Suppose g has no zero in |z|<=rho for some rho>1, and set
\[
 M_\rho=\max_{|z|=\rho}|D/g(z)|.
\]
Cauchy's coefficient estimate for q_*=sum t_j z^j gives |t_j|<=M_rho rho^{-j}.
Its degree-N truncation q_N has q_N(0)=1 and
\[
 0\le\kappa_N-D^2
 \le \|p\|_\infty^2 M_\rho^2
       \frac{\rho^{-2(N+1)}}{1-\rho^{-2}}.                     \tag{18}
\]
Indeed gq_N-D=g(q_N-q_*) has zero constant coefficient, so its square norm adds orthogonally to D²; bound multiplication by g using ||g||_infinity=||p||_infinity and sum the squared coefficient tail.
The parameters rho and M_rho are actual input costs.
Equation(18) supplies no exponential bound with uniform constants across a family acquiring circle zeros.
Nothing here rules out separate fixed-support uniform estimates by other means.

<a id="scalar-capacity-controls"></a>
## 6. Exact controls, phase retention and failed reductions

**Monomials and the zero boundary.**
For p=c z^k, D=|c| and c_0=|c|²,c_j=0 for j>0.
The unique finite Gram maximizer is |c|² E_00, every kappa_N=|c|², and q_*=1 for c!=0.
For c=0 the unique Gram matrix is0, all prediction problems have value 0 with arbitrary minimizers, and L=-infinity.
Scaling c to0 is included without invoking matrix inverses at the endpoint.

**A root crossing T.**
For p=1-a z, let t=|a|² and take the fixed width s=1.
Every feasible Gram matrix has the form
\[
 Q=\begin{pmatrix}x&-a\\-\overline a&1+t-x\end{pmatrix},
 \qquad x(1+t-x)\ge t.
\]
Its maximal x is max(1,t), so D=max(1,|a|).
The convolution Gram T_N is tridiagonal with diagonal1+t and off-diagonal entries conjugate to -a.
Its determinant obeys Delta_{-1}=1,Delta_0=1+t and Delta_N=(1+t)Delta_{N-1}-t Delta_{N-2}, giving
\[
 \det T_N=\sum_{j=0}^{N+1}t^j,\qquad
 \kappa_N=\frac{\sum_{j=0}^{N+1}t^j}{\sum_{j=0}^{N}t^j}.       \tag{19}
\]
At |a|=1 this is (N+2)/(N+1)>1, tending toD²=1 at the explicit rate1/(N+1).
The finite SDP maximum is nevertheless already1 and attained.
The analytic q_* has a circle pole and the Toeplitz dual infimum is not attained.
For a=0 the effective degree drops and every kappa_N=1, with all formulas still valid.

For the real control p=1-z and s=1, every feasible dual is H=[[h,w],[conjugate(w),h]] with h>=1 and |w|²<=h(h-1).
Its objective is2h-2Re(w), whose infimum is1 and whose finite values are strictly greater than1: 2h-2sqrt(h(h-1))>1 and tends to 1 as h->infinity.
Thus failure of dual attainment is explicit already in size 2.

**Repeated circle roots.**
For p=(1-z)^m with m>=1, D=1, g=p and the exact finite Gram maximizer is conjugate(gcoeff)gcoeff^T at size m+1.
The Toeplitz dual and both ordinary analytic infima have no optimizer; their values are still1.
The weighted completion admits q_*=(1-z)^(-m).
Every finite kappa_N is strictly greater than1.
No simple-root assumption enters any theorem above.

**Why coefficient energy alone is insufficient.**
The coefficient lists of p_+(z)=1+z+z² and p_-(z)=1+z-z² have identical entrywise squared moduli and total energy3.
The first has both roots on T, hence D(p_+)=1.
The second has roots(1+sqrt5)/2 and(1-sqrt5)/2, hence D(p_-)=(1+sqrt5)/2.
Therefore the scalar coefficient covariance map X->sum_j a_j X conjugate(a_j)=3X is the same for both but does not determine the determinant.
This refutes that reduction class only.
The Gram constraints(2) retain the actual signed/complex autocorrelations and distinguish the two inputs.

<a id="scalar-capacity-current-boundary"></a>
## Current result and review boundary

The scalar coefficient problem now has a finite SDP maximum with exact value D² and a unique optimizer, an equal finite Toeplitz dual with a completely proved attainment boundary, and a decreasing coefficient prediction hierarchy with its finite/analytic/weighted-completion distinctions and explicit controls.
None is a new positivity gap for integer polynomials.
These arguments concern a fixed finite scalar support; matrix coefficients and coefficient differentiability are the other assigned agents' work.
A final F0010 decision requires separately organized inspection of the assembled scope.
This whole working artifact currently has author self-check only; no independent review, numerical solver run or formal proof verification is asserted.


<a id="scalar-capacity-entire-author-freeze"></a>
## Entire author freeze

2026-10-13T06:36.
The assigned scalar author reread the complete artifact from the initial scope through Sections 1--6 and the current boundary.
The self-check explicitly reconstructed coefficient/conjugation orientation, the compact primal feasibility and unique optimizer, circle-zero cancellation in the vector rational quotient, finite Toeplitz dual feasibility and nonattainment, both prediction-limit directions, all three analytic admissible spaces, the geometric-error constants, and each control.
No unresolved mathematical defect was found in that author self-check.
The known maximum-Gram-entry source-body attribution remains explicitly outstanding at the bounded failed-access scope above; no external theorem body is needed for the self-contained proof.
This entire artifact is now frozen for independent whole-argument review.
Source/locator organization may be appended with its actual later inspection without rewriting this original freeze or implying it was known now.

<a id="fixed-f0010-first-round-account"></a>
## Fixed first-round account and current inspection scope

2026-10-13T06:52.
Root fixes the ENTIRE original account above after [the separate whole independent finding](../audits/reviews/Yin_R_F0004_v1.md#scalar-capacity-whole-independent-finding).
Only the D_G0001 same-folder links are rebased to their identical target in drafts, and outside newlines normalized.
Every formula, question, source account, unsuccessful reduction, bound, example, author check and freeze remains.
Original working-stage and pending-review wording is historical.
The fixed R owns the actual independent checks and source limits; structural validation and relocation do not add proof evidence.

The complete scalar finite Gram/Toeplitz capacity, prediction hierarchy and attainment account passes mathematical whole review.
The known maximum-Gram construction still has an explicitly unresolved original-theorem-body attribution check; its local proof does not rely on the inaccessible body.
This is a fixed synthesis/exploration account for F0010, not a duplicate Claim merely re-registering classical formulas.
No mathematical statement has been strengthened by organization.
The assembled Task still requires a contract-level reconciliation and corresponding completion review before any completed decision; no Task completion, G0001 resumption, native numerical run or formal verification is asserted here.


<a id="f0010-contract-closeout"></a>
## Subsequent contract closeout

2026-10-13T07:12.
The pending assembled-contract review condition recorded in the dated first-round fixed account above is now fulfilled by [R5](../audits/reviews/Yin_R_F0005_v1.md#f0010-fixed-chain-completion-finding).
The completed Task decision selects the unchanged mathematical account at its exact scope.
This status-only addition preserves every original proof, source limitation, failed candidate and historical review statement; it asserts no new theorem or enlarged review scope.

<a id="single-haar-analytic-question"></a>
## Combined scalar and finite-matrix analytic question

The coefficient and assembled-chain findings use the combined mathematical scope stated here.
This section contains the analytic objects, four questions and mathematical sufficiency criteria, separately from Task lifecycle and execution authority.

### Objects and determinant conventions

Let (M,tau) be a finite von Neumann algebra with faithful normal tracial state and U a Haar unitary:
\[
\tau(U^n)=0\quad(n\in\mathbb Z\setminus\{0\}),\qquad U^*U=UU^*=1.
\]
No free-independence hypothesis is imposed on the powers of U.
Fix a finite integer exponent interval I={l,...,u}.
The scalar coefficient space is C^I, with
\[
p_a(z)=\sum_{j\in I}a_jz^j,\qquad
D(a)=\Delta_\tau(p_a(U)),\qquad L(a)=\log D(a).
\]
Coefficients may be arbitrary complex numbers, including zero coefficients and changing effective degree.
The zero polynomial has D=0 and L=-infinity.
For nonzero p, use Haar probability mu on T and natural logarithms:
\[
L(a)=\int_{\mathbb T}\log|p_a(z)|\,d\mu(z).
\]
Nonzero polynomials with unit-circle zeros remain in scope.

The finite-matrix extension, within the same single-variable framework, is
\[
P_A(z)=\sum_{j\in I}A_jz^j,\qquad A_j\in M_r(\mathbb C),\quad r\ge1,
\]
with ordinary FK determinant under phi_r=tr_r tensor tau.
Thus
\[
L_r(A)=\log\Delta_{\phi_r}(P_A(U))
=\frac1r\int_{\mathbb T}\log|\det P_A(z)|\,d\mu(z)
\]
when det P_A is not identically zero, and L_r=-infinity otherwise.
This is the ordinary determinant including zero spectral mass; the kernel-removed determinant is a distinct quantity.
For comparison with integer group-ring conventions, the unnormalized logarithmic determinant is r L_r(A).
No dimension-normalized quantity may silently replace that total value.

### Questions

1. **Variational formulas.**
   Derive and compare exact infimum, minimum or correctly ordered saddle representations for D and L, with explicit freely variable weights, positive matrices or structured operators and admissible domains.
   State whether a formula is finite-dimensional, genuinely infinite-dimensional, or a controlled limit of finite problems.
   Prioritize descriptions built directly from coefficient data; identify what additional simplification is achieved beyond the original circle integral and scalar pointwise log identity.
   Prove both inequality directions, attainment or nonattainment, and the correct limiting convention at circle zeros and the zero polynomial.
   Investigate the matrix extension with the same explicit scope.
2. **Capacity formulas.**
   Find a coefficient-defined positive-map, Toeplitz/convolution or other explicit capacity functional whose relation to D is rigorously established.
   Specify variables, normalization, coefficient construction, homogeneity and exact determinant exponent, and test degeneration and zero capacity.
   A definition that merely renames the unknown determinant or Mahler integral as capacity is not a formula resolving this objective.
   Do not assume that the semicircular covariance map controls a Haar polynomial.
   If a natural proposed capacity class fails, retain a precise obstruction for that class and continue toward an appropriate alternative; a restricted failure does not exclude every possible capacity description.
3. **Dependence on coefficients.**
   For each fixed finite exponent interval, determine the valid continuity and regularity statements for D and extended-real L.
   Derive directional/parameter derivatives and, where justified, second variations or convexity/concavity and potential-theoretic properties.
   Treat zero crossings on T, repeated roots, effective-degree changes and the zero-polynomial boundary explicitly.
   Establish the corresponding matrix-coefficient statements on their actual valid domains, including the identically singular determinant locus.
   Distinguish holomorphic coefficient dependence from real differentiability of a real-valued determinant.
   Clearly separate fixed-support results from estimates uniform in degree or matrix size.
4. **Interaction of the formulas.**
   Explain how optimizers, regularized inverse-square expectations and capacity degenerations reflect coefficient perturbations.
   Give exact checks on representative scalar and matrix examples and identify any losses in finite approximations or linearizations.
   Numerical evidence may guide a conjecture but does not replace an exact formula or a proof of coefficient regularity.

The scalar objectives are the core deliverables.
Finite-matrix coefficients are an explicit extension target, not a replacement for the scalar problem.
Covered scalar results and still-open matrix generalizations are distinguished; mathematical coverage requires accounting for both at their recorded scope.

### Starting mathematical inputs and reuse boundaries

- [Single-Haar scalar identification and trace convention](../audits/literature/Luc22/Yin_U001.md#luc22-kernel-removed-determinant), and [abelian matrix reduction](../audits/literature/Luc22/Yin_U002.md#luc22-abelian-matrix-approximation).
- [General affine semicircular formula](../claims/Yin_C_F0004_v1.md#statement), [attainment criterion](../claims/Yin_C_F0005_v1.md#yin_c_f0005), and [regularized proof](../claims/Yin_C_F0004_v1.md#regularized-minimum-used-in-the-proof).
  These supply methods and comparisons at their actual distributional hypotheses; they do not assert a Haar formula.
- [Earlier single-Haar formulation](Yin_L_G0431_v1.md#single-haar-formulation), including [regularization and estimate direction](Yin_L_G0431_v1.md#regularization-and-direction).
  This G account records self-checked elementary baselines and no independent review; listing it here supplies no new fixed-theorem adoption.
- [L_G4 finite-section and Gram analysis](Yin_L_G0004_v1.md#degree-window-tests), with the [Den09 finite-section source interface](../audits/literature/Den09/Yin_U002.md#finite-section-determinant).
  Reuse their exact approximation direction and input-dependent costs.

Perform a bounded local and primary-source reuse check before claiming a new formula or coefficient theorem.
Existing Jensen/root expressions, circle integrals, scalar log variation and fixed-input Toeplitz limits are baselines to be used and attributed, not presumed novel results.
These boundaries supply no new source intake, proof re-audit or novelty claim.

### Mathematical sufficiency and partial progress

Retain complete arguments for the stated variational and capacity descriptions, their domains, normalization, degeneration and attainment boundaries, together with a coherent coefficient-dependence account.
State exactly which scalar and matrix coefficient classes are covered.
A fixed-degree sample, a numerical minimum, the scalar log identity alone, a stationary equation without an extremum proof, or a formula excluding circle zeros cannot silently complete the unrestricted core.

For an explicitly proposed formula class that cannot cover the assigned domain, retain the exact failed implication and proof or counterexample, and identify the corresponding unresolved alternative.
Partial formulas and coefficient theorems receive their actual scope; failure of one proposed class alone does not establish the requested mathematical coverage.

### Relationship to the integer-gap problem

Complex coefficient dependence is the primary analytical setting.
Integer/Laurent coefficient specializations may supply later inputs to [S_G3](../strategies/Yin_S_G0003.md#single-haar-analytic-focus), but this analytic question does not require proving a Lehmer gap.
A connection back to an integer gap must retain the full polynomial, actual trace normalization and every approximation or small-singular-value cost.


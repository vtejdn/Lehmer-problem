---
author: Yin
---

# Scalar Haar coefficient Gram and Toeplitz capacities with complete prediction and attainment boundaries

## Current assessment
[Selected decision](#decision-adopted-retained-proof)

## Exact retained scope and provenance

<a id="statement"></a>

Fix an arbitrary finite integer exponent interval and all complex Laurent coefficients, including zero input, degree loss and repeated circle roots.
Retain the complete scalar coefficient-Gram maximum with unique outer rank-one optimizer, equal finite Toeplitz dual and its nonattainment boundary, decreasing convolution/prediction hierarchy, all ordinary H2/H-infinity versus weighted-completion optimizer distinctions and the paid fixed-input approximation bound.
This responsible home retains the substantial complete supporting argument and exact boundary controls, without claiming a new classical maximum-Gram, Jensen, prediction or Szego theorem, integer gap, numerical implementation or growing-degree uniformity.
The inaccessible original maximum-Gram theorem body remains a source-attribution limit, not a mathematical premise.
The complete fixed argument below is retained from [Yin_L_F0005_v1](../ledger/Yin_L_F0005_v1.md) at 2026-10-21T02:32.
Its original mathematical development, attribution, review dates and historical status statements remain in that fixed L.
This placement preserves existing mathematics; it selects no Task, objective change, new theorem role, novelty or publication claim.

Dated candidate, draft and review-pending sentences in the retained text describe the original development.
The selected current decision owns present mathematical adoption and actual review scope.

## Complete retained argument

<a id="argument"></a>

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
<a id="verified-maximum-gram-attribution"></a>
On 2026-11-03, the maintenance agent directly text-read the author-uploaded [MW02 paper](https://www.researchgate.net/publication/2459893_Spectral_Factorizations_and_Sums_of_Squares_Representations_via_Semidefinite_Programming), Section 2, Proposition 2.3 and the following spectral-factor paragraph and Algorithm 1.
Proposition 2.3 maximizes trace F_00 over positive semidefinite block Gram matrices with prescribed diagonal sums, giving rank F=rank F_00<=rank Q_0.
For scalar coefficients this is precisely maximization of the first Gram entry, with a rank-one optimizer for nonzero input.
The following paragraph and Algorithm 1 identify the maximizing construction with spectral factorization.
This verifies an adequate primary attribution alternative; Dumitrescu's indexed Theorem 2.15 remains an uninspected lead and is not needed for that attribution.
The author-uploaded text is not asserted identical to the publisher rendering; its displayed page 4 contains the Proposition 2.3 proof, and Algorithm 1 follows in Section 2.
The reading was text-only, without a retained PDF, rendered-page check, complete paper-proof audit or review of its cited factorization foundations.
The local all-degenerate-case value and uniqueness argument above remains the mathematical proof; source attribution adds no new premise or solver guarantee.

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

## Assessment history

### Decision retained-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:32 |
| status | open |
| reason | Retain the exact complete argument in its responsible Claim home before selecting its applicable fixed review findings. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact scope](#statement) | Exact retained scope and hypotheses above and in the complete original statement below. |
| argument | [Complete retained argument](#argument) | Complete original argument, failed implications and limitations retained below. |
| dependency | [Exact input](../audits/literature/Luc22/Yin_U001.md#luc22-u001) | Nonzero Laurent Haar/Jensen formula with leading coefficient and multiplicities, at the kernel-removed convention section; the ordinary zero branch is independently specified here. |
| dependency | [Exact input](../audits/literature/DR10/Yin_U001.md#dr10-u001) | Classical scalar Fejer–Riesz name, reciprocal-conjugate root and open-disk outer convention at its exact nonzero statement/attribution scope; no rational coefficient or optimizer assertion. |

### Decision adopted-retained-proof

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:33 |
| status | proved |
| reason | Adopt the applicable original complete mathematical finding on the unchanged retained supporting argument, at its actual unknown initial-context relationship. Preserve classical attribution, complete source and failed-inference boundaries, normalized zero/singular cases and all historical inputs; no new classical theorem, Task decision or aggregate independent certification. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact retained scope and hypotheses above and in the complete original statement below. |
| argument | [Exact material](#argument) | Complete original argument, failed implications and limitations retained below. |
| dependency | [Exact material](../audits/literature/Luc22/Yin_U001.md#luc22-u001) | Nonzero Laurent Haar/Jensen formula with leading coefficient and multiplicities, at the kernel-removed convention section; the ordinary zero branch is independently specified here. |
| dependency | [Exact material](../audits/literature/DR10/Yin_U001.md#dr10-u001) | Classical scalar Fejer–Riesz name, reciprocal-conjugate root and open-disk outer convention at its exact nonzero statement/attribution scope; no rational coefficient or optimizer assertion. |
| review | [Actual finding](../audits/reviews/Yin_R_F0004_v1.md#scalar-capacity-whole-independent-finding) | Whole unchanged Sections 1–6 and equations (1)–(19): padded scalar coefficient domain, outer normalization, compact Gram maximum and unique optimizer, exact Toeplitz dual and nonattainment, convolution/prediction finite formulas and decreasing limit, all analytic-space and weighted-completion boundaries, geometric costs and phase/zero/circle controls. The original maximum-Gram theorem-body attribution limitation remains; no growing-degree or novelty assertion. |


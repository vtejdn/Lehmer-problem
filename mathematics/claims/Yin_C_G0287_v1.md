---
author: Yin
---

# Posterior leverage, finite Gram--Jensen entropy comparison and sharp basis-block bounds

This retains the complete original2026-10-07 [L94 argument](../ledger/Yin_L_G0094_v1.md), including its full covariance, finite Gram--Jensen and Holder proofs.
The assigned ms25_source agent developed the posterior argument; the coordinator contributed the finite Gram--Jensen bridge, explicit comparison and independent-basis-block estimates.
The [original R25](../audits/reviews/Yin_R_G0025_v1.md#punctured-leverage-reuse-review) owns those actual old checking accounts, with their exact scopes and limitations.
No source, computation or Task is newly executed.

## Statement

All logarithms are natural and TV is half the l1 distance.
For independent fair bits X in{0,1}^N and a real row-rank-r matrix V, observe Y=VX.
Put Z=X-1/2, U=E[Z given Y], Pi=V^T(VV^T)^(-1)V, Q=I-Pi and lambda_j=Pi_jj.
For g(x)=((1+x)/2)log(1+x)+((1-x)/2)log(1-x) on[-1,1] and f(t)=g(sqrt(t)) on[0,1],

    Cov(U)=Pi/4+Cov(QU)>=Pi/4,
    I(X_j;Y)>=f(lambda_j)>=lambda_j/2,
    TV(law(Y given X_j=0),law(Y given X_j=1))>=lambda_j,
    sum_j I(X_j;Y)>=N f(r/N)>=r/2,
    sum_j TV(law(Y given X_j=0),law(Y given X_j=1))>=r.

No conditional independence of bits is asserted.

For every nonzero algebraic integer alpha, let P be its monic irreducible polynomial, d its degree, m=log M(P)>=0, v_j=t^j mod P in Z^d and S_N=sum_(j<N)X_jv_j.
Set H0=0,H_N=H(S_N),Delta_N=H_N-H_(N-1).
Injectivity of multiplication by alpha and independent bits give decreasing increments with limit h1=lim H_N/N.
If2k-1>=d, Delta_k>=f(d/(2k-1))>=d/[2(2k-1)]; for k<=d,Delta_k=log2.
For0<delta<log2, Delta_k<=delta requires k>=1/2+d/(4delta), with the sharper condition2k-1>=d/f^(-1)(delta).
If N>=d and every punctured conditional pair has TV<=eta, then N eta>=d.

For N>=d put G_N=det(V_NV_N^T).
For N>d the last leverage is1-G_(N-1)/G_N and

    G_N/G_(N-1)>=exp(2m),
    Delta_N>=B(m):=f(1-exp(-2m)) for every N>=1,
    h1>=B(m)>=3 min(m,log2)/(8log2).

The determinant identity and monic residual/Jensen inequality are finite, allow real monic multipliers and unit-circle roots, and use no Toeplitz limit or BV20 lower theorem.
Moreover B(m)=m-(2/3)m²+O(m³).
For the nontorsion unit target, h1<=min(m,log2), so h1/m tends to1 along any hypothetical sequence with m tending to0.
This neither constructs nor excludes such a sequence.
The retained fair-group comparison separately gives every-N H_infinity(S_N),H2(S_N)>=N B(m)/2; it is not needed to prove B.

For an integer fair weighted sum in Z^d containing q disjoint rational-basis blocks, q>=1, its collision probability is at most b_q^d, where b_q=binom(2q,q)4^(-q)<=(q+1)^(-1/2).
Additional independent bits are allowed.
With2r rational-basis blocks, r>=1, its maximum atom is at most b_r^d.
Nonunimodular basis matrices suffice.
For powers of any nonzero degree-d algebraic integer, use q=floor(N/d) or r=floor(N/(2d)) when positive.
The exact collision and atom bounds are attained by P(t)=t^d+1,d=2^a,a>=0, at the stated complete-block lengths.
These m=0 controls prove the rank-only limitation, not a counterexample in the nontorsion core or a positive entropy rate.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:44 |
| status | open |
| reason | Entire original posterior, finite residual and rank-block proof retained; a current complete check and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Entire real-cube covariance/information/TV theorem, nonzero-algebraic-integer rank/time and every-N finite B(m) comparison, fair min/collision consequence and sharp nonunimodular basis-block bounds with all zero-measure and uniformity limits. |
| argument | [Complete argument](#argument) | Full original1–19, including exact cross terms, nonlinear convex series, punctured submodularity, dual integral kernel, real monic Jensen residual, all-time/limit constants and expansion, Haar/Holder proof and cyclotomic equality controls. |
| dependency | [Finite dual Gram identity](Yin_C_G0209_v1.md#gram-lower-certificate) | Only exact monic polynomial-division kernel basis and coefficient/orbit dual determinant identity at finite N, not the Den09 limit or fixed-support completion. |
| dependency | [Finite real-monic Jensen method](Yin_C_G0214_v1.md#argument) | Only the complete finite Parseval/Jensen residual inequality for a real monic multiplier; no Schinzel reduction, asymptotic Toeplitz theorem or source-proof extension. |
| dependency | [Independent-sum submodularity](Yin_C_G0282_v1.md#entropy-set-function-thinning) | Exact arbitrary-abelian independent partial-sum submodularity; local injectivity of multiplication by nonzero alpha supplies the stated nonunit power-interval argument. |
| dependency | [Fair-group entropy comparison](Yin_C_G0280_v1.md#abelian-binary-entropy-comparison) | Exact H_infinity and H2 at least half Shannon for finite independent fair sums, used only for17 and the consequent atom/collision exponent, not the local B(m) proof. |
| support | [Unit binary increment and resource interface](Yin_C_G0283_v1.md#punctured-binary-near-invariance) | Original unit-domain punctured matching and effective time comparison, preserving its actual domain; the local proof explicitly uses only injectivity for its nonzero-integer extension. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:51 |
| status | proved |
| reason | Adopt the complete original posterior/finite Gram--Jensen theorem and sharp rational-basis-block controls after actual whole self-review, including the proved nonzero-algebraic-integer domain, exact constants and zero-measure/uniformity limits; no source-proof extension or new substantive repair. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire real-cube covariance/information/TV theorem, nonzero-algebraic-integer rank/time and every-N finite B(m) comparison, fair min/collision consequence and sharp nonunimodular basis-block bounds with all zero-measure and uniformity limits. |
| argument | [Argument](#argument) | Full original1–19, including exact cross terms, nonlinear convex series, punctured submodularity, dual integral kernel, real monic Jensen residual, all-time/limit constants and expansion, Haar/Holder proof and cyclotomic equality controls. |
| dependency | [Dependency](Yin_C_G0209_v1.md#gram-lower-certificate) | Only exact monic polynomial-division kernel basis and coefficient/orbit dual determinant identity at finite N, not the Den09 limit or fixed-support completion. |
| dependency | [Dependency](Yin_C_G0214_v1.md#argument) | Only the complete finite Parseval/Jensen residual inequality for a real monic multiplier; no Schinzel reduction, asymptotic Toeplitz theorem or source-proof extension. |
| dependency | [Dependency](Yin_C_G0282_v1.md#entropy-set-function-thinning) | Exact arbitrary-abelian independent partial-sum submodularity; local injectivity of multiplication by nonzero alpha supplies the stated nonunit power-interval argument. |
| dependency | [Dependency](Yin_C_G0280_v1.md#abelian-binary-entropy-comparison) | Exact H_infinity and H2 at least half Shannon for finite independent fair sums, used only for17 and the consequent atom/collision exponent, not the local B(m) proof. |
| support | [Support](Yin_C_G0283_v1.md#punctured-binary-near-invariance) | Original unit-domain punctured matching and effective time comparison, preserving its actual domain; the local proof explicitly uses only injectivity for its nonzero-integer extension. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0537_v1.md#current-posterior-gram-finding) | Entire exact current statement, complete retained original argument and every selected interface, self-reviewed; old findings keep only their actual fixed inputs and exact relationship scopes. |


### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:59 |
| status | proved |
| reason | Adopt the actual fresh complete mathematical review, formed before the full old-account comparison, at every original statement/proof/necessary-input boundary. Preserve all old decisions and self/unknown facts; no substantive repair, source-depth expansion or unrestricted completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire real-cube covariance/information/TV theorem, nonzero-algebraic-integer rank/time and every-N finite B(m) comparison, fair min/collision consequence and sharp nonunimodular basis-block bounds with all zero-measure and uniformity limits. |
| argument | [Argument](#argument) | Full original1–19, including exact cross terms, nonlinear convex series, punctured submodularity, dual integral kernel, real monic Jensen residual, all-time/limit constants and expansion, Haar/Holder proof and cyclotomic equality controls. |
| dependency | [Dependency](Yin_C_G0209_v1.md#gram-lower-certificate) | Only exact monic polynomial-division kernel basis and coefficient/orbit dual determinant identity at finite N, not the Den09 limit or fixed-support completion. |
| dependency | [Dependency](Yin_C_G0214_v1.md#argument) | Only the complete finite Parseval/Jensen residual inequality for a real monic multiplier; no Schinzel reduction, asymptotic Toeplitz theorem or source-proof extension. |
| dependency | [Dependency](Yin_C_G0282_v1.md#entropy-set-function-thinning) | Exact arbitrary-abelian independent partial-sum submodularity; local injectivity of multiplication by nonzero alpha supplies the stated nonunit power-interval argument. |
| dependency | [Dependency](Yin_C_G0280_v1.md#abelian-binary-entropy-comparison) | Exact H_infinity and H2 at least half Shannon for finite independent fair sums, used only for17 and the consequent atom/collision exponent, not the local B(m) proof. |
| support | [Support](Yin_C_G0283_v1.md#punctured-binary-near-invariance) | Original unit-domain punctured matching and effective time comparison, preserving its actual domain; the local proof explicitly uses only injectivity for its nonzero-integer extension. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0537_v1.md#current-posterior-gram-finding) | Entire exact current statement, complete retained original argument and every selected interface, self-reviewed; old findings keep only their actual fixed inputs and exact relationship scopes. |
| review | [Actual complete independent finding](../audits/reviews/Yin_R_G0545_v1.md#f-g288) | Entire actual statement and complete original proof independently inspected, with exact domains, all useful old whole/partial obligations, original source-depth, failed comparisons, costs and limit order; no new mathematical experiment or reconstructed historical isolation. |


## Complete retained argument

<a id="argument"></a>
<a id="posterior-covariance-leverage"></a>
### Linear observations of a fair cube

Let \(X=(X_0,\ldots,X_{N-1})\) consist of independent fair bits, let \(V\) be a real \(r\)-by-\(N\) matrix of row rank \(r\), and observe \(Y=VX\).
Put

\[
 Z=X-\tfrac12\mathbf1,\quad U=\mathbb E[Z\mid Y],\quad
 \Pi=V^{\mathsf T}(VV^{\mathsf T})^{-1}V,\quad Q=I-\Pi,
 \quad \lambda_j=\Pi_{jj}.                               \tag{2}
\]

Here \(\Pi\) is the orthogonal row-space projection, \(0\le\lambda_j\le1\), and \(\sum_j\lambda_j=r\).
Since \(\Pi Z\) is determined by \(Y\), \(\Pi U=\Pi Z\).
Moreover,

\[
 \mathbb E[(\Pi Z)(QU)^{\mathsf T}]
 =\mathbb E[(\Pi Z)(QZ)^{\mathsf T}]
 =\tfrac14\Pi Q=0.
\]

The first equality uses conditional expectation and the \(Y\)-measurability of \(\Pi Z\); the last uses \(\operatorname{Cov}(Z)=I/4\).
Thus the exact decomposition is

\[
 \operatorname{Cov}(U)=\tfrac14\Pi+
          \operatorname{Cov}(QU)\ \succeq\ \tfrac14\Pi.   \tag{3}
\]

For the posterior bias \(b_j(Y)=2\mathbb P(X_j=1\mid Y)-1=2U_j\), this gives \(\mathbb E b_j^2\ge\lambda_j\).
Write \(p_j,q_j\) for the conditional laws of \(Y\) given \(X_j=0,1\).
The fair prior and the definition of mutual information give

\[
 I_j:=I(X_j;Y)=\mathbb E g(b_j(Y)),\qquad
 \operatorname{TV}(p_j,q_j)=\mathbb E|b_j(Y)|.             \tag{4}
\]

Both formulas include atoms occurring in only one conditional law, with the convention \(0\log0=0\).
To check the TV formula, the unconditional atom weight is \((p_j+q_j)/2\), whereas its posterior bias is \((q_j-p_j)/(q_j+p_j)\).

Let \(f(t)=g(\sqrt t)\), \(0\le t\le1\).
This function is increasing and convex.
Indeed, integrating \(g''(x)=1/(1-x^2)\) twice gives

\[
 f(t)=\sum_{a=1}^{\infty}\frac{t^a}{2a(2a-1)}\quad(0\le t<1),
\]

and continuity gives the endpoint value \(f(1)=\log2\).
Every coefficient is positive, so monotonicity and convexity extend to the closed interval.
Jensen's inequality and \(|b_j|\ge b_j^2\) now prove

\[
 I_j\ge f(\mathbb E b_j^2)\ge f(\lambda_j)
       \ge\lambda_j/2,\qquad
 \operatorname{TV}(p_j,q_j)\ge\lambda_j,
\]
\[
 \boxed{\ \sum_j I_j\ge Nf(r/N)\ge r/2,\qquad
          \sum_j\operatorname{TV}(p_j,q_j)\ge r.\ }       \tag{5}
\]

The information bound is a lower bound on a sum of marginal informations.
It does not assert independence of the bits after conditioning on their weighted sum.

<a id="punctured-information-time-cost"></a>
### A degree cost for near-full punctured matching

Let \(\alpha\ne0\) be an algebraic integer with monic irreducible polynomial \(P\) of degree \(d\), and use the power basis of \(\mathbb Z[\alpha]\).
Put

\[
 v_j=t^j\bmod P\in\mathbb Z^d,\quad
 S_N=\sum_{j=0}^{N-1}X_jv_j,\quad H_N=H(S_N),\quad
 \Delta_N=H_N-H_{N-1},\quad H_0=0.                        \tag{6}
\]

Coordinates in the power basis preserve exactly the fibers of the algebraic sum \(\sum X_j\alpha^j\), including for a nonreal \(\alpha\).
For \(N\ge d\), the matrix \(V_N=[v_0\ \cdots\ v_{N-1}]\) has rank \(d\), since its first \(d\) columns are the identity.
The conditional laws in (4) are the punctured law and its translate by \(v_j\).
Therefore \(I_j\) is exactly \(I_{N,j}\) of L G0092.

The interval submodularity proved there uses only independence of the input bits and injectivity of multiplication by \(\alpha\).
It gives

\[
 I_{N,j}\le\Delta_{\max(j+1,N-j)}
            \le\Delta_{\lceil(N+1)/2\rceil},\qquad
 \Delta_N\downarrow h_1:=\lim_N H_N/N.                   \tag{7}
\]

Consequently, for \(2k-1\ge d\),

\[
 \boxed{\ \Delta_k\ge
 f\!\left(\frac{d}{2k-1}\right)
 \ge\frac{d}{2(2k-1)}.\ }                               \tag{8}
\]

If \(k\le d\), the stronger exact identity is \(\Delta_k=\log2\), because the first \(k\) powers are linearly independent.
In particular, for \(0<\delta<\log2\), \(\Delta_k\le\delta\) necessarily implies

\[
 k\ge\tfrac12+\frac{d}{4\delta}.                        \tag{9}
\]

This is a necessary time cost, not a sufficient mixing bound.
More precisely (8) gives \(2k-1\ge d/f^{-1}(\delta)\).
For \(N\ge d\), if every punctured matching has overlap fraction at least \(1-\eta\), its two conditional laws have TV at most \(\eta\).
Equation (5) then implies \(N\eta\ge d\).
These statements concern simultaneous weighted mass overlap, rather than only the existence of a height-one relation.

<a id="endpoint-gram-mahler-entropy"></a>
### Endpoint leverage and the existing dual Gram residual

For \(N\ge d\), write

\[
 W_N=V_NV_N^{\mathsf T},\qquad G_N=\det W_N>0.
\]

The endpoint leverage of the last column, for \(N>d\), is

\[
 \lambda_{N-1}=v_{N-1}^{\mathsf T}W_N^{-1}v_{N-1}
            =1-\frac{G_{N-1}}{G_N}.                     \tag{10}
\]

Indeed, \(W_{N-1}=W_N-v_{N-1}v_{N-1}^{\mathsf T}\), and the rank-one determinant formula gives (10).
The last-bit information equals \(\Delta_N\); no information from another coordinate or embedding is multiplied into it.
Equations (4)--(5) already give the finite bound

\[
 \Delta_N\ge f\!\left(1-\frac{G_{N-1}}{G_N}\right).
                                                               \tag{11}
\]

We reuse the exact [dual Gram identity](Yin_C_G0209_v1.md#gram-lower-certificate) and the complete [monic-residual argument](Yin_C_G0214_v1.md#argument).
For completeness, the needed finite identities are as follows.
If \(k=N-d\), the coefficient vectors of \(P,tP,\ldots,t^{k-1}P\) form an integral basis of \(\ker V_N\).
Monic polynomial division proves spanning; the bottom \(k\)-by-\(k\) block is triangular with diagonal 1.
Writing \(V_N=[I_d\ B]\), a second kernel basis is \([-B;I_k]\).
The change between the bases is unimodular, whence

\[
 G_N=D_k:=\det\operatorname{Gram}(P,tP,\ldots,t^{k-1}P),
 \qquad D_0=1.                                         \tag{12}
\]

Here the Gram inner product is the ordinary coefficient Euclidean inner product.
The determinant equality also follows directly from \(\det(I_k+B^{\mathsf T}B)=\det(I_d+BB^{\mathsf T})\).
The last Gram--Schmidt residual is \(Pq\), where \(q\) is a real monic polynomial of degree \(k-1\).
Thus

\[
 \frac{G_N}{G_{N-1}}=\frac{D_k}{D_{k-1}}=\|Pq\|_2^2
 \ \ge\ M(Pq)^2=M(P)^2M(q)^2\ \ge\ M(P)^2.              \tag{13}
\]

The multiplier need not be integral.
Monicity alone gives \(M(q)\ge1\).
To see the middle inequality directly, Parseval identifies \(\|Pq\|_2^2\) with the circle integral of \(|Pq|^2\).
The arithmetic/geometric mean inequality for this integral and the root-by-root identity \(\int_0^1\log|e^{2\pi it}-\beta|\,dt=\log^+|\beta|\) give \(\log\|Pq\|_2\ge\log M(Pq)\).
The logarithmic singularities from unit-circle roots are integrable, so the inequality covers those roots as well.
This is the same finite Jensen residual calculation already used in L G0009; no Toeplitz limit or asymptotic ratio is required.

Since \(f\) is increasing, (11)--(13) prove

\[
 \boxed{\ \Delta_N\ge B(m)=f(1-e^{-2m})\quad\text{for every }N\ge1,
 \qquad h_1\ge B(m).\ }                                 \tag{14}
\]

For \(N\le d\), use \(\Delta_N=\log2\ge B(m)\); for later \(N\), use (13); finally use (7).
The proof does not require reciprocality, a unique expanding conjugate, all-power degree preservation, or a bound on the degree.
It holds for every nonzero algebraic integer.
The target application is the irreducible algebraic-unit core, where the retained upper bound is \(h_1\le\min(m,\log2)\).

<a id="explicit-mahler-binary-comparison"></a>
### What the comparison changes, and what it leaves open

The elementary inequality \(f(t)\ge t/2\) gives

\[
 B(m)\ge\tfrac12(1-e^{-2m})
 \ge\frac{3}{8\log2}\min(m,\log2).                      \tag{15}
\]

For \(0\le m\le\log2\), the second inequality is the chord bound for the concave function \((1-e^{-2m})/2\); for larger \(m\), use monotonicity and its value \(3/8\) at \(\log2\).
The exact formula is stronger.
Expanding at zero gives

\[
 1-e^{-2m}=2m-2m^2+O(m^3),\quad
 f(t)=t/2+t^2/12+O(t^3),\quad
 B(m)=m-\tfrac23m^2+O(m^3).                              \tag{16}
\]

Consequently, along any hypothetical sequence of nontorsion algebraic units with \(m\to0\), regardless of their degrees, \(h_1/m\to1\).
This is a statement conditional on such a sequence existing.
It does not produce one or exclude one.

The already proved fair-binary comparison in [C280](Yin_C_G0280_v1.md#mahler-to-binary-min-entropy) also gives, for all \(N\),

\[
 H_\infty(S_N)\ge H_1(S_N)/2\ge NB(m)/2,\qquad
 H_2(S_N)\ge NB(m)/2.                                   \tag{17}
\]

Thus its max-atom and collision estimates may use the explicit exponent \(B(m)/2\), and the already proved thinning argument may use \(B(m)\) as its full-input Shannon lower rate.
These are deductions from the retained Li26-based comparison, not claims that support entropy equals Shannon entropy or Mahler entropy.
The local result (14) itself uses none of the BV20 entropy lower-bound theorem, Li26, or the thinning argument.

The finite lower bound (8) also changes the time diagnosis: an increment of order \(m\) cannot occur before order \(d/m\).
The existing constructive upper time in L G0092 has order \((d/m)\log(d/m)\).
No removal of its logarithm is proved.
The new entropy comparison still vanishes with \(m\); the missing uniform arithmetic step remains exclusion of small positive \(m\), rather than transfer between these entropy rates.

<a id="independent-basis-block-collision"></a>
### A separate sharp rank-only collision bound

The coordinating agent supplied the following complementary rank bound.
Suppose an integer weighted sum in \(\mathbb Z^d\) contains \(q\) disjoint blocks of \(d\) columns, each forming a basis over \(\mathbb Q\).
Additional independent bits may be present.
Write

\[
 b_q=\binom{2q}{q}4^{-q},\qquad q\ge1.
\]

Fourier inversion and orthogonality on \(\mathbb T^d\) give the collision probability \(\operatorname{Col}(S)=\int\prod_j\cos^2(\pi\langle y,v_j\rangle)\,dy\).
Discard additional factors, which lie in \([0,1]\), and group the retained ones as \(F_1,\ldots,F_q\), one per basis.
Holder's inequality gives

\[
 \operatorname{Col}(S)\le
       \prod_{a=1}^q\left(\int_{\mathbb T^d}F_a(y)^q\,dy\right)^{1/q}
       =b_q^d.                                         \tag{18}
\]

For the equality on the right, the integer basis matrix has nonzero determinant, so the associated map on \(\mathbb T^d\) pushes Haar measure to Haar measure.
This can be checked on characters: the pullback of a nontrivial integer character is nontrivial because the matrix has zero rational kernel.
The integral then separates into \(d\) copies of \(\int_0^1\cos^{2q}(\pi t)\,dt=b_q\), as follows by expanding exponentials and taking the constant term.
A unimodular matrix is not required.

Similarly, Fourier inversion gives \(p_{\max}(S)\le\int\prod_j|\cos(\pi\langle y,v_j\rangle)|\,dy\).
With \(2r\) independent basis blocks and Holder exponent \(2r\), this yields

\[
 p_{\max}(S)\le b_r^d.                                 \tag{19}
\]

For powers of any nonzero algebraic integer of degree \(d\), each consecutive block of \(d\) powers is such a rational basis: multiplication by a power of \(\alpha\) is injective.
Thus (18) holds with \(q=\lfloor N/d\rfloor\), and (19) holds with \(r=\lfloor N/(2d)\rfloor\), whenever these integers are positive.
The bounds have an elementary simpler form \(b_q\le(q+1)^{-1/2}\).
To verify it, use \(b_q/b_{q-1}=(2q-1)/(2q)\) and \((2q-1)^2(q+1)\le4q^3\), and induct from \(b_0=1\).

Both exact binomial bounds are sharp among these rank-only data.
Take \(P(t)=t^d+1\) with \(d=2^a\), \(a\ge0\).
This is the cyclotomic polynomial \(\Phi_{2^{a+1}}\), and \(\alpha^d=-1\).
In \(q\) consecutive basis blocks each coordinate is a sum of \(q\) independently signed fair bits; changing a minus bit to its complement alters only a constant.
Each coordinate therefore has a translated binomial law, independently of the other coordinates.
Its collision probability is \(\binom{2q}{q}4^{-q}\), by Vandermonde's identity.
For \(q=2r\), its maximal atom is \(\binom{2r}{r}4^{-r}\).
Hence equality holds in (18)--(19).

These examples have \(m=0\) and are outside the nontorsion all-power-stable target core.
They demonstrate the precise rank-only limitation; they do not refute a stronger arithmetic bound on the core.
In particular, the polynomial decay in (18)--(19) cannot by itself supply a positive entropy rate.

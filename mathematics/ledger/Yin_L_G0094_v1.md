---
author: Yin
---

# Punctured binary information, orbit leverage and Mahler entropy

The current complete mathematical proof is retained in [C287](../claims/Yin_C_G0287_v1.md#argument).
The original mathematical text below remains the fixed old input; current Claim adoption does not rewrite its old date or review bindings.

Date: 2026-10-07.
Bounded direct continuation of G0001 by the assigned AI ms25_source for Yin.
The coordinating agent contributed the finite Gram--Jensen reuse bridge, the explicit uniform comparison, and the independent-basis-block Holder bound below.
The posterior covariance argument and its punctured-information application were developed by the assigned agent.
No computation or new external source is used; no novelty or solution of Lehmer is claimed.

The question is whether the near-full punctured matching in [L G0092](Yin_L_G0092_v1.md#punctured-binary-near-invariance) has a simultaneous rank cost.
It does: the sum of its bit informations is at least half the rank, with a stronger nonlinear bound.
Applying the same calculation at the last coordinate and reusing the exact orbit/dual Gram identity also gives the degree-independent Shannon comparison

\[
 h_1(\alpha)\ \ge\ B(m):=
 g\!\left(\sqrt{1-e^{-2m}}\right),\qquad
 g(x)=\frac{1+x}{2}\log(1+x)+\frac{1-x}{2}\log(1-x),
 \quad m=\log M(P).                                      \tag{1}
\]

In particular, \(B(m)=m-\tfrac23m^2+O(m^3)\) near zero.
This compares two entropies; its right side still tends to zero, so it supplies no degree-independent positive entropy gap.

<a id="posterior-covariance-leverage"></a>
## Linear observations of a fair cube

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
## A degree cost for near-full punctured matching

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
## Endpoint leverage and the existing dual Gram residual

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

We reuse the exact [dual Gram identity](../claims/Yin_C_G0209_v1.md#gram-lower-certificate) and the complete [monic-residual argument](../claims/Yin_C_G0214_v1.md#argument).
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
## What the comparison changes, and what it leaves open

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

The already proved fair-binary comparison in [L G0089](Yin_L_G0089_v1.md#mahler-to-binary-min-entropy) also gives, for all \(N\),

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
## A separate sharp rank-only collision bound

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


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0025_v1.md#punctured-leverage-reuse-review), with its original inspected scope and relationship.

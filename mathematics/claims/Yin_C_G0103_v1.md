---
author: Yin
---

# Exact single-Haar Gram certificates and coefficient-field barriers

Date: 2026-10-15.
Human author Yin.
Continuing author inquiry under the explicitly resumed G0001 goal.
This working material carries no independent review or adopted theorem.

## Responsible question and starting scope

Develop the F0010 original-polynomial Gram maximum as a G0001 lower-certificate interface.
Begin with the discussed minimal-width rational-face obstruction for irreducible circle-root inputs; investigate zero padding, coefficient-field reduction and ways to construct exact certificates without assuming the unknown Mahler measure.
Preserve the distinction from integer-value auxiliary packets.
Initial inputs: L_F0005, C34, C75 and the unchanged G0001 contract.
The prior chat's short proof is a starting author contribution by root, with a read-only check, not an adopted project theorem.

<a id="gram-field-reuse-and-contributions"></a>
## 1. Reuse, source scope and author contributions

The assigned author read the unchanged G0001 contract, the complete scalar capacity account [L_F5](../ledger/Yin_L_F0005_v1.md#scalar-capacity-finite-sdp), its matrix counterpart [L_F7](../ledger/Yin_L_F0007_v1.md#matrix-finite-gram-capacity), [C34](Yin_C_G0034_v1.md#statement), [C75](Yin_C_G0075_v1.md#statement), the reciprocal trace domain in [L66](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain), and the quartic Salem control in [L8](../ledger/Yin_L_G0008_v1.md#quartic-projection-obstruction).
The current complete proof homes of these identical retained inputs are [C_F6 scalar finite Gram capacity](Yin_C_F0006_v1.md#scalar-capacity-finite-sdp) and [C_F8 matrix finite Gram capacity](Yin_C_F0008_v1.md#matrix-finite-gram-capacity).
The original input-reading record above and all dated review bindings remain fixed.
The F formulas give real/complex exact maxima, not coefficient-field descent.
C34 supplies strict-positive rational-interior construction, explicitly excluding boundary descent.
C75 prices an open-convolution replacement by its actual inverse-boundary correction; it is a different interface from the finite coefficient-Gram maximum below.
Neither its matrix obstruction nor its scope is silently enlarged.

A bounded local search for rational Gram boundaries, zero padding, Galois factors and Salem trace constructions found those interfaces, [PP08-U001](../audits/literature/PP08/Yin_U001.md#pp08-u001) and [MSEDSV22-U001](../audits/literature/MSEDSV22/Yin_U001.md#msedsv22-u001).
Their inspected strict-feasibility hypotheses are retained.
No adequate existing statement for the field-constrained capacity below was located; this is not a novelty claim.

For recognized classical Gram/field mechanisms, the author directly text-read Chua--Plaumann--Sinn--Vinzant, *Gram Spectrahedra*, actual [arXiv:1608.00234v3, 2 May 2018](https://arxiv.org/pdf/1608.00234), 24 PDF pages, printed/PDF pp.5--6: Lemma1.6, Remark1.7 and Remark1.8.
These passages cover rational Gram diagonalization, dependence on field orderings, and minimal-polynomial removal of real zeros.
They provide attribution, not the unit-circle maximum, the padded field-forced face or the block-minor conclusion here.
The earlier v2 and HTML endpoints failed; the successful primary PDF explicitly identifies v3.
No source bytes were acquired, canonical U extended, whole-paper proof audited or historical-priority assertion made.
The complete needed elementary adaptations are given below; no theorem about rational unweighted squares over a number field is imported.

Root subsequently retained the actual v3 source and independently read the same selected passages.
The canonical [CPSV18-U001](../audits/literature/CPSV18/Yin_U001.md#cpsv18-u001) now owns that attribution-only source scope and links the actual artifact.
This source organization does not supply independent review of the present mathematics or erase the author's earlier online-only inspection.

Contributions: root supplied the minimal-width irreducible rational singleton argument before this round, and during the round supplied the all-embedding-positivity trace lead and the Salem identity at parameter b=1 in Section7.
The assigned author supplies the complete weighted-PSD proof and all-padding extension, the general field-saturated factor/closure theorem, the arbitrary-size rational block-Gram obstruction, the all-padding proof of the trace lead, and the explicit cofinal b-parametrized Salem certificates with their inertia and field-attainment consequences.
Root and this author are contributors, not independent reviewers.
No native numerical computation is used.

## Statement

All scalar symbols below are formed on the full coefficient block 1,z,...,z^n, with exact lag sums, Haar probability, total Mahler measure M, and ordinary PSD Grams including singular ones.
A field contained in R always has its specified embedding; positivity at that embedding is not total positivity.

**A. Field-constrained face and supremum.**
For any subfield K of R, nonzero p in K[z] with p(0) nonzero, and n>=deg p, let G_K(p;n) be the exact real symmetric K-entry PSD Gram set for |p|^2.
Let c be the monic product, with full multiplicities, of those K-irreducible factors of p having at least one circle root; put r=p/c, e=deg c, and let T_c be coefficient multiplication by c.
Then G_K(p;n)=T_c G_K(r;n-e) T_c^T, with unique preimage.
Its real closure is the closed face T_c G_R(r;n-e) T_c^T of G_R(p;n).
In particular sup Q00=c(0)^2 M(r)^2, at every such width.
Attainment is equivalent to the unique real outer maximizing Gram of r having entries in K; no unconditional attainment or denominator bound is asserted.

**B. Rational irreducible ceiling, including every finite padding.**
If p in Q[z] is irreducible, p(0) nonzero, and p has a circle root, then max_(G_Q(p;n)) Q00=p(0)^2 for every n>=deg p, with unique maximizing Gram aa^T for the padded coefficient vector a of p.
At n=deg p the entire rational feasible set is this singleton; at larger width it is not.
The same ceiling holds for Gaussian-rational Hermitian scalar Grams.
Conversely, for rational p with no circle roots, the rational supremum is M(p)^2, so an individual such input with M(p)>1 has a rational certificate Q00>1, with no uniform quantitative cost claimed.

**C. Same-scalar rational matrix ceiling.**
Under B's assumptions, for every rational r-by-r Laurent matrix A with det A=epsilon z^b p, epsilon in{1,-1}, any common monomial shift to an ordinary matrix Ahat, and any finite padded block width containing Ahat, every REAL RATIONAL symmetric PSD block Gram for Ahat^* Ahat satisfies det Q00<=p(0)^2.
This permits arbitrary r, width and coefficient height and uses the full determinant, not its dimension-normalized root.
It is not a theorem about arbitrary complex algebraic block Grams or every matrix lower-bound method.

**D. All-embedding positivity ceiling.**
Under B's assumptions, let K/Q be any finite totally real field, n>=deg p, and Q in G_K(p;n).
If sigma(Q) is PSD for every real embedding sigma of K, then Q00<=p(0)^2, with equality only for the padded aa^T.
At minimal width every such Q is aa^T.
No irreducibility of p over K is required for this assertion.

**E. Exact Salem construction and trace-field nonattainment.**
For a monic irreducible Salem polynomial p of degree d>=4, with roots lambda>1, lambda^(-1) and d-2 circle roots, put t=lambda+lambda^(-1), K=Q(t), C=p/(z^2-tz+1).
For every rational b>=1 with s=b+b^(-1)<t, the three weighted squares in(20) give an explicit rank-three Gram Q_b in G_K(p;d), using only C, b and t.
Its objective is b^2+(t-s)(t+s-2)>b^2.
These objectives increase to lambda^2=M(p)^2 as rational b increases to lambda, but lambda^2 is not attained by a K-entry Gram at ANY finite padded width.
At b=1 the objective is (t-1)^2; the Gram has exactly two positive and one negative eigenvalue at every nonidentity real embedding, all other eigenvalues being zero.
The rank-three construction is not asserted to have minimum rank, and only the stated trace-field nonattainment is proved, not a general minimum-degree coefficient-field theorem.

The unit reciprocal specialization of B--D has p(0)^2=1.
Statement E supplies actual per-input lower certificates and a cofinal family, not a uniform positive Mahler gap.
All field, denominator, embedding-selection and approximation costs remain those of the actual input.
The complete proofs, constructions, controls, useful failed shortcuts and source/contribution boundaries follow in the same original account.

## Argument

<a id="gram-field-conventions"></a>
## 2. Exact objects and weighted positive decomposition

Let K be a subfield of R with its specified inclusion, let p in K[z] be nonzero with p(0) nonzero, and write d=deg p.
For every integer n>=d, pad the coefficients of p by zeros to width n and put v_n(z)=(1,z,...,z^n)^T.
Define

\[
 \mathcal G_K(p;n)=\{Q\in\operatorname{Sym}_{n+1}(K):Q\succeq0,
               \ v_n(z)^*Qv_n(z)=|p(z)|^2\ (|z|=1)\}.          \tag{1}
\]

Here positivity is in the stated REAL embedding.
The identity is equivalently the exact diagonal-sum constraints from L_F0005, including the zero higher lags.
The set of K points need not be closed in the real topology.
The notation G_R denotes the full real symmetric spectrahedron.
Its maximum Q00 is M(p)^2 by L_F0005: taking the real part of a complex Hermitian feasible matrix preserves positivity on real vectors, the real coefficient constraints and Q00, so the real symmetric maximum has the same value.
All measures use Haar probability and total scalar Mahler measure.

Every Q in Sym_m(K) with Q>=0 admits

\[
 Q=\sum_{j=1}^{\operatorname{rank}Q} d_j u_j u_j^T,
 \qquad u_j\in K^m,\quad d_j\in K,\quad d_j>0.                 \tag{2}
\]

This is a WEIGHTED decomposition.
No square root of d_j is asserted to lie in K.
For completeness, if Q is nonzero PSD then it has a positive diagonal entry: otherwise every 2-by-2 principal minor forces every off-diagonal entry zero.
Permute such an entry to the first position and write Q=[[a,b^T],[b,C]], a>0.
Completing the square gives a rank-one term a(1,b/a)(1,b/a)^T and a PSD Schur complement C-bb^T/a.
All its entries stay in K.
Repeat on the smaller matrix, omitting zero remainders.
This proves (2), including singular Q.

Consequently (1) is equivalent to a finite identity

\[
 |p(z)|^2=\sum_j d_j |f_j(z)|^2,\qquad
 f_j\in K[z],\quad \deg f_j\le n,\quad d_j>0,                 \tag{3}
\]

with the actual Q equal to the sum of the weighted coefficient outer products.
Polynomial vanishing at a circle point is forced separately in every summand of (3); the positivity of d_j is indispensable.

<a id="field-forced-gram-face"></a>
## 3. The exact field-forced factor and closure of feasible K points

Factor p in K[z].
Let c be the product of the MONIC K-irreducible factors that have at least one root on the unit circle in C, each to its FULL multiplicity in p.
Put

\[
             p=c r,\qquad e=\deg c.                           \tag{4}
\]

The empty product is c=1.
No root at zero occurs.
The polynomial r has no circle root; c can have many roots off the circle, because its whole K-irreducible factors are retained.
The factorization depends on K and on its specified real embedding.

Let T_c be the (n+1)-by-(n-e+1) coefficient matrix for multiplication by c.
It has full column rank.
Then

\[
 \boxed{\mathcal G_K(p;n)=
       \{T_c R T_c^T:R\in\mathcal G_K(r;n-e)\}.}              \tag{5}
\]

The map is one-to-one.
Moreover

\[
 \boxed{\overline{\mathcal G_K(p;n)}=
       \{T_c R T_c^T:R\in\mathcal G_{\mathbb R}(r;n-e)\},}
                                                                    \tag{6}
\]
\[
 \boxed{\sup_{Q\in\mathcal G_K(p;n)} Q_{00}
                 =c(0)^2 M(r)^2.}                            \tag{7}
\]

The closure is in the real matrix topology.
It is a closed face of G_R(p;n), possibly a proper face, and (7) is a supremum rather than an unconditional attainment statement.

**Forced divisibility with multiplicities.**
In (3), suppose a circle root zeta of p has order m.
The remaining analytic factor of p is nonzero near zeta, so |p(z)|=O(|z-zeta|^m) along the circle.
Each term satisfies |f_j(z)|<=d_j^(-1/2)|p(z)|.
If f_j had a smaller vanishing order, its leading nonzero Taylor term along that arc would contradict this estimate.
Thus (z-zeta)^m divides f_j over C.

Let q be the monic K-minimal polynomial of zeta, appearing to exponent m in p.
In characteristic zero, q is separable.
In the factorization f_j=q^a u with q not dividing u, one has u(zeta) nonzero by minimality; hence the vanishing order of f_j at zeta is precisely a.
Therefore q^m divides f_j in K[z].
Applying this to every circle-containing K-factor proves c divides each f_j.
Write f_j=c g_j.
Cancellation of |c|^2 off its finite circle zero set in (3), then continuity on the circle, gives |r|^2=sum d_j|g_j|^2.
Taking coefficient outer products gives (5).
Conversely any R on the right plainly gives a feasible Q.
Multiplication by c is injective; a left inverse of T_c exists over K (for example its first n-e+1 rows are triangular with diagonal c(0)), proving uniqueness of R.

**Density on the residual strictly positive fiber.**
The needed extension of C34's arithmetic step from Q to K is elementary and is stated explicitly.
For any real self-star Laurent symbol h with coefficients in K that is strictly positive on the circle, and any monomial width m-1 at least its support radius, there is a real PD Gram of size m.
Indeed choose rational 0<gamma<min h, apply the real scalar factorization step of C34 to h-gamma, pad its real factor to width m-1, and add (gamma/m)I to its coefficient Gram.
C34's root-pair proof of this REAL factorization uses no rationality premise.
The result represents h and has eigenvalues at least gamma/m.

The exact affine fiber has K points arbitrarily near any real point X.
Approximate the independent entries of X by elements of K to entry error at most eta; this is possible since Q is contained in K.
Let e_k be the error in lag k of the resulting symmetric matrix Y.
Since the target coefficients and Y lie in K, every e_k lies in K, and |e_k|<=m eta.
Add e_0 at (0,0) and e_k at BOTH (0,k),(k,0) for k>=1, choosing the sign that restores the target sums.
Each positive lag is corrected exactly once, and symmetry restores the negative lags.
The resulting K matrix differs from X in operator norm by at most m(m+1)eta.
If X is PD, eta below lambda_min(X)/(2m(m+1)) preserves PD.

Obtain a PD K point R_int this way.
For any PSD real point R, the mixture (1-t)R+t R_int is PD for 0<t<1; approximate it within the exact fiber as above and let t decrease to zero.
Thus the K PSD points are dense in the entire real residual fiber.
Taking h=|r|^2 proves (6), since that real fiber is compact and the map T_c R T_c^T is continuous and injective.
Its image consists exactly of real feasible Grams whose ranges lie in the coefficient subspace of multiples of c.
The latter is a face: it is exposed in the PSD cone by the orthogonal projection onto that subspace's orthogonal complement, and intersecting with the affine Gram fiber retains the face property.

Finally the first row of T_c has only its entry c(0), so Q00=c(0)^2 R00.
L_F0005 gives max R00=M(r)^2, proving (7).
The real unrestricted value is M(p)^2=M(c)^2 M(r)^2.
Therefore the ratio of the field-constrained supremum to the unrestricted value is exactly

\[
                    \frac{c(0)^2}{M(c)^2}.                   \tag{8}
\]

It is at most one by the root formula.
This quantifies the loss caused by the inside roots that field divisibility forces into every summand.
It does not claim that the K supremum is attained.
L_F0005's unique real maximizing Gram makes residual attainment equivalent to that particular outer Gram having entries in K.

<a id="irreducible-all-padding-obstruction"></a>
## 4. Irreducible circle-root inputs: every finite padding is obstructed

Let p in Q[z] be irreducible, p(0) nonzero, and suppose it has a circle root.
For EVERY n>=d,

\[
 \boxed{\max_{Q\in\mathcal G_{\mathbb Q}(p;n)}Q_{00}=p(0)^2.} \tag{9}
\]

The unique maximizing Q is aa^T, where a is the coefficient column of p padded to width n.
At n=d the ENTIRE rational feasible set is this singleton.
At n>d the feasible set is not a singleton, but its maximum still has that unique optimizer.

A direct proof highlights why zero padding fails.
Rational weighted factorization (2) and any circle root force f_j=p g_j in (3).
Thus

\[
             \sum_j d_j|g_j(z)|^2=1\quad(|z|=1).              \tag{10}
\]

Integrating and expanding the finite Fourier polynomials gives

\[
 1=\sum_j d_j\sum_{k\ge0}|[z^k]g_j|^2
       \ge\sum_j d_j|g_j(0)|^2,
 \qquad Q_{00}=p(0)^2\sum_j d_j|g_j(0)|^2.                    \tag{11}
\]

The coefficient outer product aa^T attains the bound.
Equality forces every nonconstant coefficient of every g_j to vanish, because all d_j are positive.
Then (10) forces sum d_j g_j(0)^2=1 and Q=aa^T.
At n=d every g_j was constant already.
For n>=d+1 and rational 0<theta<1, the two summands sqrt(theta) p and sqrt(1-theta) zp are represented without irrational coefficients by weights theta,1-theta: their Gram is theta aa^T+(1-theta)(Sa)(Sa)^T and has Q00=theta p(0)^2.
This explicitly exhibits padded freedom without gain.

For the monic irreducible reciprocal unit core, p(0)=1.
Thus every rational PSD finite Gram has Q00<=1 even when M(p)>1.
The rational feasible set is nonempty, but its closure does not contain the real optimum.
Rounding the real optimizer and correcting lag equations therefore cannot preserve positivity while retaining objective greater than one.
This is a failure of the strict-feasibility premise, not of rational arithmetic or of the real F0010 maximum theorem.

The scalar conclusion also excludes Gaussian-rational Hermitian Grams: their entrywise real parts are real rational symmetric PSD, satisfy the same real diagonal-sum constraints and preserve Q00.
For arbitrary complex number fields no analogous real-part descent is asserted here.

There is a sharp complementary scope.
If p has NO circle root, c=1 in (7), so rational feasible Grams have supremum M(p)^2 at the original width d.
In particular each particular such p with M(p)>1 has an exact rational feasible Q00>1.
No denominator, bit complexity, objective separation or uniform quantitative construction is supplied by this density statement.
Near-circle conditioning remains an actual cost.

<a id="rational-block-gram-obstruction"></a>
## 5. Arbitrary-size same-scalar rational matrix presentations do not evade the obstruction

Let p be as in Section4 and let A(z) be an r-by-r rational Laurent polynomial matrix such that det A=epsilon z^b p with epsilon in{1,-1}.
Shift all entries by a COMMON monomial so that Ahat is an ordinary polynomial matrix; write det Ahat=epsilon z^ell p with ell>=0.
Put B=Ahat^* Ahat on T.
For ANY finite padded coefficient width n containing Ahat, consider a REAL RATIONAL symmetric PSD block Gram Q=(Qij)_(0<=i,j<=n), with r-by-r blocks, satisfying

\[
       \sum_{i=0}^{n-k}Q_{i,i+k}=B_k\quad(0\le k\le n).
                                                                    \tag{12}
\]

Then

\[
                   \boxed{\det Q_{00}\le p(0)^2.}             \tag{13}
\]

There is no bound on r, n, coefficient height or the chosen presentation.
The statement concerns the finite coefficient-Gram capacity of L_F0007, not C75's open-convolution determinant comparison.
The unrestricted Hermitian maximum in this very problem is M(p)^2, independently of r, because max det Q00=D_r(Ahat)^(2r)=M(det Ahat)^2.
Thus rational same-scalar matrix enlargement cannot yield a finite capacity certificate greater than one for the unit circle-root core.

**Proof.**
Apply (2) to the full real rational PSD matrix Q and write Q=F^T D F, where D=diag(d_1,...,d_m) has positive rational entries and F is rational.
Group the columns into blocks and define the m-by-r polynomial matrix F(z)=sum_(i=0)^n F_i z^i.
Equation(12) says

\[
                F(z)^* D F(z)=B(z).                          \tag{14}
\]

Since det B is not identically zero, m>=r.
For every r-element row subset S put d_S=product_(j in S)d_j>0 and f_S(z)=det F_S(z) in Q[z].
Weighted Cauchy--Binet gives, on T,

\[
 |p(z)|^2=\det B(z)=\sum_{|S|=r}d_S|f_S(z)|^2,
 \qquad \det Q_{00}=\sum_{|S|=r}d_S f_S(0)^2.                 \tag{15}
\]

At any circle root of p all terms in the first sum vanish.
Irreducibility over Q forces p to divide EVERY f_S (zero minors cause no problem).
Write f_S=p u_S.
Cancel |p|^2 off its finite zero set and extend by continuity to obtain sum d_S|u_S|^2=1 on T.
Integration and the coefficient square sum give sum d_S u_S(0)^2<=1.
Substitute into the second identity in(15) to prove (13).
This retains the full determinant and never divides its logarithm by r.

Only real rational block Grams are covered by the stated proof; no unproved determinant monotonicity under entrywise real parts is invoked to enlarge this matrix scope.
Algebraic coefficients with a specified real embedding can evade rational divisibility, as Section7 shows already for r=1.

<a id="all-embedding-positive-gram-obstruction"></a>
## 6. Requiring positivity at every real embedding restores the obstruction

Keep p rational irreducible with a circle root.
Let K/Q be a finite TOTALLY REAL extension, and let Q in G_K(p;n) have the additional property that sigma(Q)>=0 for EVERY embedding sigma:K->R.
Then

\[
                          Q_{00}\le p(0)^2,                  \tag{16}
\]

with equality only for the padded aa^T.
In minimal width n=d every such Q is aa^T.
Thus a nontrivial algebraic scalar certificate Q00>p(0)^2 over a totally real field necessarily has a non-PSD conjugate matrix.

**Proof, including padding.**
The normalized field trace R=(1/[K:Q])sum_sigma sigma(Q) is real rational symmetric PSD and feasible for the SAME rational symbol |p|^2.
By Section4's divisibility proof its range lies in the real subspace W of coefficient columns of multiples of p.
If y in W-perp is real, then

\[
 0=y^T R y=\frac1{[K:\mathbb Q]}
                    \sum_\sigma y^T\sigma(Q)y.               \tag{17}
\]

Every summand is nonnegative, so all vanish.
A PSD matrix whose quadratic form vanishes at y annihilates y, as follows from (2) over R.
Hence every sigma(Q), and Q itself, has range in W.
Factor Q over R and express every summand polynomial as p times a real polynomial.
The cancellation/Parseval proof (10)--(11) now applies WITHOUT asking p to stay irreducible over K, and gives (16) and its equality characterization.
At n=d, W is one-dimensional, forcing Q to be a scalar multiple of aa^T; the exact symbol makes that scalar one.

The assumption on all embeddings is essential.
Positive pivots in one embedding need not be totally positive, and averaging an indefinite conjugate would not preserve PSD.
This is compatible with the ordering distinction in the inspected Gram Spectrahedra Remark1.7.
The theorem does not declare algebraic certificates invalid; it identifies the price of requiring a trace descent that preserves positivity everywhere.

<a id="explicit-salem-trace-field-certificates"></a>
## 7. Explicit positive Salem certificates over the trace field

Let p be a monic irreducible Salem polynomial of degree d=2h>=4: its roots are lambda>1, lambda^(-1), and d-2 roots on T, and p(0)=1.
Define

\[
 t=\lambda+\lambda^{-1}>2,\qquad K=\mathbb Q(t),\qquad
 h_t(z)=z^2-tz+1,\qquad C(z)=p(z)/h_t(z).                     \tag{18}
\]

The trace construction in L66 gives [K:Q]=h and identifies the conjugates of t with the inverse-pair traces.
In this Salem specialization they are all real, with every nonidentity conjugate in(-2,2); hence K is totally real.
Division by the monic h_t shows C in K[z], deg C=d-2, C(0)=1.
In fact ordinary polynomial long division constructs its coefficients in Z[t] from p and t.
No spectral factor or square root of t^2-4 is required to form C.

Choose ANY rational b>=1 and set s=b+b^(-1), with the exact specified-embedding inequality

\[
                              s<t.                           \tag{19}
\]

Set g_b(z)=b-2z+b^(-1)z^2.
On T, g_b has the same modulus as h_s(z)=(z-b)(z-b^(-1)).
Writing x=z+z^(-1) in[-2,2] gives the identity

\[
 \begin{aligned}
 |h_t(z)|^2
 &=|g_b(z)|^2+2(t-s)|z-1|^2+(t-s)(t+s-4),\\
 |p(z)|^2
 &=|C(z)g_b(z)|^2
       +2(t-s)|C(z)(z-1)|^2
       +(t-s)(t+s-4)|C(z)|^2.                                \tag{20}
 \end{aligned}
\]

Indeed |h_t|^2=(t-x)^2 and |h_s|^2=(s-x)^2, so their difference is (t-s)(t+s-2x); insert 2-x=|z-1|^2.
The equality of |g_b| and |h_s| follows directly from replacing the root b by its reciprocal in the circle modulus, or from g_b=b(1-z/b)^2.

All three weights in(20) are strictly positive: t-s>0 and t+s-4>0.
Their three polynomial coefficient columns lie in K, have degrees d,d-1,d-2, and are linearly independent because C is nonzero and the remaining degrees are 2,1,0.
Equation(20) therefore constructs an EXACT rank-three PSD Gram Q_b in G_K(p;d).
Its objective is explicitly

\[
 \boxed{(Q_b)_{00}
       =b^2+(t-s)(t+s-2)>b^2\ge1.}                           \tag{21}
\]

In particular the root-supplied b=1 case is

\[
 |p(z)|^2=|C(z)(z-1)^2|^2
       +2(t-2)|C(z)(z-1)|^2+(t-2)^2|C(z)|^2,
 \qquad (Q_1)_{00}=(t-1)^2>1.                                \tag{22}
\]

Equations(20)--(22) supply a genuine explicit lower certificate for each actual Salem input, not a tautological choice of the unknown maximizing Gram.

**Approach to the real optimum within the trace field.**
Since x+x^(-1) is strictly increasing for x>1, (19) is equivalent to b<lambda for b>=1.
Rational choices b increasing to lambda exist.
Formula(21) then tends to lambda^2=M(p)^2.
For b>=1 its value is strictly increasing, since after substituting s=b+b^(-1) its derivative is 2-2b^(-2)+2b^(-3)>0.
Thus these explicit K certificates are cofinal in the real maximum.
For an actual exact certificate, supply rational b and verify (19) using the specified real algebraic t; a formal limit alone is not such a certificate.
Denominators of b, the number-field representation of C, isolation of the chosen embedding, and any cost of checking PSD remain actual input costs.

**Nonattainment over K.**
The unique real maximizing Gram in L_F0005 is the coefficient outer product of

\[
       G(z)=C(z)(\lambda-2z+\lambda^{-1}z^2),\qquad G(0)=\lambda.
                                                                    \tag{23}
\]

It is an outer polynomial: C has only circle roots, and the displayed quadratic has its double root at lambda>1.
Already its (0,0) Gram entry lambda^2 does not belong to K: otherwise lambda=(lambda^2+1)/t would belong to K, contradicting [Q(lambda):K]=2 from L66.
Hence no matrix with entries in K can attain this objective, in ANY padded finite width.
The cofinal rank-three family avoids that exact optimal field requirement while preserving exact identities.

**Exactly what fails under other embeddings.**
For b=1 and any nonidentity embedding sigma, put t_j=sigma(t) in(-2,2), C_j=sigma(C).
The three weights in(22) become 1, 2(t_j-2), (t_j-2)^2.
Their signs are +,-,+ and none is zero.
The three coefficient columns remain linearly independent because their degrees are d,d-1,d-2.
Sylvester inertia, or an invertible basis change extending those columns, shows sigma(Q_1) has exactly TWO positive and ONE negative eigenvalue, with all remaining eigenvalues zero.
Thus the construction evades Section6 in a precisely controlled way: one negative direction at each nonidentity real place.
No norm inequality can discard these directions as though the certificate were totally positive.

**Scale of the basic gain.**
If m=log lambda, then t=2 cosh m and (Q_1)00-1=2(t-2)+(t-2)^2=2m^2+O(m^4) as m tends to zero.
Consequently the direct bound m>=log(t-1) is only of quadratic size in a hypothetical small-m regime.
The cofinal family can approach the first-order true value, but selecting b sufficiently close to lambda carries the same input dependence; no uniform b>1 has been supplied for every Salem input.
The construction proves neither that Salem inputs exhaust all reciprocal inputs nor a positive Lehmer gap.

<a id="gram-field-controls-and-boundaries"></a>
## 8. Controls, failed shortcuts and useful next questions

The quartic p(z)=z^4-z^3-z^2-z+1 from L8 is a concrete exact control: t=(1+sqrt(13))/2>2, C(z)=z^2-((1-sqrt(13))/2)z+1.
Section4 gives rational maximum1 in every width, while(22) gives the trace-field feasible value (t-1)^2=(7-sqrt(13))/2>1 in width4.
The other embedding has one negative Gram direction as proved above.
This uses the retained exact root/irreducibility control; no numerical experiment or J output is asserted.

For p=z-1, the rational maximum is1 and equals M(p)^2, so a circle zero alone does not imply a strict field-capacity loss.
For p=z^2-3z+1, there are no circle roots; Section3 gives the full real optimum as the rational supremum, without asserting rational attainment.
These controls distinguish forced field factors from generic conditioning and from cyclotomic measure1.

The following tempting approaches are now decided at their stated scopes.

- Adding arbitrarily many zero coefficients to the original circle-root irreducible scalar Gram does not create rational gain; all-padding Parseval proves the sharp cap and unique maximizer.
- Replacing the scalar by any rational same-scalar matrix presentation and applying the finite block-Gram capacity does not create rational gain; the full determinant minors preserve the same divisibility obstruction.
  This is an additional exact interface, not an assertion that every matrix inequality is covered by C75 or by Section5.
- Applying C34's rational rounding/projection to the singular real optimum without a positive interior margin fails.
  Equation(6) identifies exactly which face rational/field points can approximate; a successful near-optimal numerical matrix need not admit rational correction within the positive cone.
- Requiring every conjugate of an algebraic certificate to remain PSD prevents scalar gain as well.
  The explicit Salem construction instead controls, but does not remove, its negative directions at the other real places.
- The exact trace-field construction gives per-input lower certificates and an explicit cofinal sequence.
  It does not make the field degree bounded, the denominators free, t-2 uniformly positive or the G0001 target solved.

The most focused continuation is to exploit the one-negative-direction description without pretending it is positive: seek a signed or compensating all-place inequality that retains the exact original polynomial and pays the negative-place contribution.
A useful positive result would relate that contribution to independently available original-field arithmetic and produce a net lower bound uniform in degree; the present Gram identities alone do not do this.
A separate possibility is an exact field-degree/precision bound for certificates below a specified objective threshold.
Both remain open questions, not promised outcomes.
The existing arithmetic same-index income route is neither replaced nor weakened by these results.


These are author-complete deductions and constructions awaiting a separately organized whole review; the status of their fixed inputs is not copied onto the new arguments.

<a id="gram-field-entire-author-freeze"></a>
## 9. Entire author freeze

2026-10-14T19:18.
The assigned author freezes the entire current account, Sections1--8 and equations(1)--(23), for separate whole review.
The author reread the actual body and checked weighted singular LDL without field square roots; full vanishing multiplicities; exact convolution orientation, injectivity, closure and field-density correction; all-padding equality and unique optimizer; full block determinant and weighted minors; trace positivity at every embedding and its kernel implication; Salem coefficient field, all three positive weights, exact objective, monotonicity, nonattainment and conjugate inertia; and the actual scope of every source/input and failed shortcut.
The matrix comparison is explicitly against the unrestricted Hermitian maximum and proves its obstruction for REAL RATIONAL block Grams; no determinant comparison under entrywise real parts is silently presumed.
No unresolved proof gap was found by this author check, which is not independent review.
No mathematical result, unlimited approximation cost, original discovery, task completion or new execution authority is inferred from this freeze.

2026-10-14T19:19.
At root's request for direct whole-original retention, the author adds the explicit Statement A--E and Argument anchors above within this same original account.
Every quantified domain and conclusion was compared against Sections2--7, including finite padding, the real-rational matrix restriction, total positivity, and cofinality versus attainment.
No proof or theorem was strengthened.
The entire ACTUAL current body, including this statement interface and the unchanged source/contribution history, is now frozen for the separate noncontributor review.
The earlier freeze retains its original narrower packaging scope; no review has yet been performed by this author.

## Fixed organization

The entire author original above is retained at its actual final freeze, including source searches, contributor accounts, unsuccessful methods and all limitations.
Author-stage wording records history.
This actual fixed artifact, including the exact statement and complete argument, awaits a separately organized noncontributor whole review.
Allocation asserts no accepted mathematics.

## Current assessment
[Selected decision](#decision-current-isolated-whole-review-20261022-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:22 |
| status | open |
| reason | Register the entire author-frozen statement and argument from the resumed parallel G0001 round for independent review of this actual fixed artifact. Preserve all hypotheses, failures, source limits and contributor accounts. No unrestricted gap, automatic near-one coverage or Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | All enumerated conclusions at their stated domains and limits. |
| argument | [Complete argument](#argument) | All retained proofs, controls, boundaries and actual source interfaces. |
| dependency | [Exact input](../ledger/Yin_L_F0005_v1.md#scalar-capacity-finite-sdp) | Exact scalar maximum and unique outer-Gram optimizer. |
| dependency | [Exact input](../ledger/Yin_L_F0007_v1.md#matrix-finite-gram-capacity) | Exact block-Gram maximum and full determinant normalization. |
| dependency | [Exact input](Yin_C_G0034_v1.md#statement) | Real strict-positive factorization and interior projection; field adaptation proved locally. |
| dependency | [Exact input](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | Actual reciprocal trace field and inverse-pair degree. |
| dependency | [Exact input](../ledger/Yin_L_G0008_v1.md#quartic-projection-obstruction) | Exact quartic Salem control. |
| support | [Exact input](../audits/literature/CPSV18/Yin_U001.md#cpsv18-u001) | Known mechanism attribution only; new capacity results proved locally. |

### Decision current-quartic-control-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:00 |
| status | proved |
| reason | Select the adopted C213 v2 as the current responsible home of the identical retained L8 quartic control at the exact anchor below. Its actual selected adoption and complete quartic projection section were read, including the exact polynomial, inverse/circle root pattern and trace values; the explicitly selected C206 Section6 supplies the complete modulo-2 irreducibility argument and was read at that scope. Mathematical status, statement, complete argument, selected finding and every relation scope are inherited unchanged; this is current locator maintenance and supplies no new mathematical or independent review. The selected finding now declares unknown initial context, while the older dated decision and its R bindings retain their actual original L8 inputs and fields. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | All enumerated conclusions at their stated domains and limits. |
| argument | [Complete argument](#argument) | All retained proofs, controls, boundaries and actual source interfaces. |
| dependency | [Exact input](../ledger/Yin_L_F0005_v1.md#scalar-capacity-finite-sdp) | Exact scalar maximum and unique outer-Gram optimizer. |
| dependency | [Exact input](../ledger/Yin_L_F0007_v1.md#matrix-finite-gram-capacity) | Exact block-Gram maximum and full determinant normalization. |
| dependency | [Exact input](Yin_C_G0034_v1.md#statement) | Real strict-positive factorization and interior projection; field adaptation proved locally. |
| dependency | [Exact input](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | Actual reciprocal trace field and inverse-pair degree. |
| dependency | [Exact input](Yin_C_G0213_v2.md#quartic-projection-obstruction) | Exact quartic Salem control. |
| support | [Exact input](../audits/literature/CPSV18/Yin_U001.md#cpsv18-u001) | Known mechanism attribution only; new capacity results proved locally. |
| review | [Actual whole review](../audits/reviews/Yin_R_G0796_v1.md#gram-field-actual-whole-independent-finding) | Complete actual statement, entire retained argument, every declared direct input and the precise source and scope limitations. |


### Decision current-haar-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:44 |
| status | proved |
| reason | Select the adopted complete C_F6/C_F7/C_F8 responsible homes, as applicable below, for the unchanged retained scalar finite Gram maximum and unique optimizer plus matrix block-Gram maximum. The actual selected adoptions and complete needed interface sections were read and matched to the original fixed L_F5/L_F6/L_F7 text. Mathematical status, statement, full argument, selected findings and every relation scope remain unchanged; this is current proof-location maintenance with no new mathematical or independent review. Original dated decisions and all R bindings keep their actual old inputs and declarations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | All enumerated conclusions at their stated domains and limits. |
| argument | [Complete argument](#argument) | All retained proofs, controls, boundaries and actual source interfaces. |
| dependency | [Exact input](Yin_C_F0006_v1.md#scalar-capacity-finite-sdp) | Exact scalar maximum and unique outer-Gram optimizer. |
| dependency | [Exact input](Yin_C_F0008_v1.md#matrix-finite-gram-capacity) | Exact block-Gram maximum and full determinant normalization. |
| dependency | [Exact input](Yin_C_G0034_v1.md#statement) | Real strict-positive factorization and interior projection; field adaptation proved locally. |
| dependency | [Exact input](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | Actual reciprocal trace field and inverse-pair degree. |
| dependency | [Exact input](Yin_C_G0213_v2.md#quartic-projection-obstruction) | Exact quartic Salem control. |
| support | [Exact input](../audits/literature/CPSV18/Yin_U001.md#cpsv18-u001) | Known mechanism attribution only; new capacity results proved locally. |
| review | [Actual whole review](../audits/reviews/Yin_R_G0796_v1.md#gram-field-actual-whole-independent-finding) | Complete actual statement, entire retained argument, every declared direct input and the precise source and scope limitations. |

### Decision current-local-trace-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:51 |
| status | proved |
| reason | Select C241/C243 as the complete current responsible homes for the identical already used L64 unramified local or L66 reciprocal trace/order/module interfaces at the exact selected anchors below. The full original arguments, current extracted statements and used guards were read; this is same-content locator adoption. Status, selected statement/argument/finding, all relation scopes and every other current proof home remain unchanged. Prior dated decisions and R bindings keep their actual L64/L66 inputs; no new independent review, local assumption, cheaper entropy normalization or stronger arithmetic estimate is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All enumerated conclusions at their stated domains and limits. |
| argument | [Argument](#argument) | All retained proofs, controls, boundaries and actual source interfaces. |
| dependency | [Dependency](Yin_C_F0006_v1.md#scalar-capacity-finite-sdp) | Exact scalar maximum and unique outer-Gram optimizer. |
| dependency | [Dependency](Yin_C_F0008_v1.md#matrix-finite-gram-capacity) | Exact block-Gram maximum and full determinant normalization. |
| dependency | [Dependency](Yin_C_G0034_v1.md#statement) | Real strict-positive factorization and interior projection; field adaptation proved locally. |
| dependency | [Dependency](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Actual reciprocal trace field and inverse-pair degree. |
| dependency | [Dependency](Yin_C_G0213_v2.md#quartic-projection-obstruction) | Exact quartic Salem control. |
| support | [Support](../audits/literature/CPSV18/Yin_U001.md#cpsv18-u001) | Known mechanism attribution only; new capacity results proved locally. |
| review | [Review](../audits/reviews/Yin_R_G0796_v1.md#gram-field-actual-whole-independent-finding) | Complete actual statement, entire retained argument, every declared direct input and the precise source and scope limitations. |


### Decision current-isolated-whole-review-20261022-m04

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:29 |
| status | proved |
| reason | Adopt the current isolated whole statement/argument review in R796 after direct mathematical initial judgment and subsequent complete comparison of the original findings. The new finding is independently reviewed and the complete superseded original account retains its actual unknown relationship, date, bindings, source depth and limitations in that R. Preserve the exact statement, complete argument, proved status, every selected support/dependency and its scope, all prior decisions and all fixed mathematics. No historical relationship is promoted, original external proof or native computation is newly certified, unrestricted coverage or Task completion is inferred, or stopped research resumed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All enumerated conclusions at their stated domains and limits. |
| argument | [Argument](#argument) | All retained proofs, controls, boundaries and actual source interfaces. |
| dependency | [Dependency](Yin_C_F0006_v1.md#scalar-capacity-finite-sdp) | Exact scalar maximum and unique outer-Gram optimizer. |
| dependency | [Dependency](Yin_C_F0008_v1.md#matrix-finite-gram-capacity) | Exact block-Gram maximum and full determinant normalization. |
| dependency | [Dependency](Yin_C_G0034_v1.md#statement) | Real strict-positive factorization and interior projection; field adaptation proved locally. |
| dependency | [Dependency](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Actual reciprocal trace field and inverse-pair degree. |
| dependency | [Dependency](Yin_C_G0213_v2.md#quartic-projection-obstruction) | Exact quartic Salem control. |
| support | [Support](../audits/literature/CPSV18/Yin_U001.md#cpsv18-u001) | Known mechanism attribution only; new capacity results proved locally. |
| review | [Current isolated whole finding](../audits/reviews/Yin_R_G0796_v1.md#fresh-c0103-whole-finding) | Entire exact current statement and complete retained argument, every finite/conditional/asymptotic scope, decisive direct input interfaces, controls, original arithmetic costs and source/negative/execution limitations. Current isolated whole review after fixed-input initial judgment, with complete original unknown account preserved separately in the same R; no mathematical repair or scope enlargement. |

## Historical assessments

<a id="decision-whole-reviewed-2026-10-15"></a>

### Historical assessment whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:28 |
| status | proved |
| review-status | independently reviewed |
| reason | Adopt the separately organized whole review of this actual fixed statement and entire retained original. The coefficient-field face and supremum, arbitrary-padding rational and real-rational block barriers, total-real-place scalar obstruction, and explicit Salem trace-field cofinal certificates are proved at the stated domains. No uniform positive gap, free arithmetic precision, generic minimum field or near-one coverage is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | All enumerated conclusions at their stated domains and limits. |
| argument | [Complete argument](#argument) | All retained proofs, controls, boundaries and actual source interfaces. |
| dependency | [Exact input](../ledger/Yin_L_F0005_v1.md#scalar-capacity-finite-sdp) | Exact scalar maximum and unique outer-Gram optimizer. |
| dependency | [Exact input](../ledger/Yin_L_F0007_v1.md#matrix-finite-gram-capacity) | Exact block-Gram maximum and full determinant normalization. |
| dependency | [Exact input](Yin_C_G0034_v1.md#statement) | Real strict-positive factorization and interior projection; field adaptation proved locally. |
| dependency | [Exact input](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | Actual reciprocal trace field and inverse-pair degree. |
| dependency | [Exact input](../ledger/Yin_L_G0008_v1.md#quartic-projection-obstruction) | Exact quartic Salem control. |
| support | [Exact input](../audits/literature/CPSV18/Yin_U001.md#cpsv18-u001) | Known mechanism attribution only; new capacity results proved locally. |
| review | [Actual whole independent review](../audits/reviews/Yin_R_G0796_v1.md#gram-field-actual-whole-independent-finding) | Complete actual statement, entire retained argument, every declared direct input and the precise source and scope limitations. |

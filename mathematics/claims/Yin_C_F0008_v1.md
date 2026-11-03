---
author: Yin
---

# Matrix Haar coefficient Gram capacities, field variation and exact convolution limits

## Current assessment
[Selected decision](#decision-adopted-retained-proof)

## Exact retained scope and provenance

<a id="statement"></a>

For every fixed finite Laurent support and finite square matrix size, retain the complete coefficient block-Gram maximum and outer-factor matching proof, positive bounded matrix-field variational identity with exact attainment/nonattainment, regularized sensitivities and all finite convolution-capacity optimizer and singular branches with the two-direction limit.
Arbitrary complex coefficients, degree drops, circle zeros and identically singular determinants are included with ordinary zero spectral mass and exact r,N normalization.
Retain all coupled, phase and covariance-only failure controls and actual approximation costs.
The only nontrivial existence input is DR10’s exact accepted matrix Fejer–Riesz statement/outer convention; no new classical factorization theorem, rational optimizer, uniqueness of every matrix Gram, numerical solver or degree/size-uniform bound is claimed.
The complete fixed argument below is retained from [Yin_L_F0007_v1](../ledger/Yin_L_F0007_v1.md) at 2026-10-21T02:32.
Its original mathematical development, attribution, review dates and historical status statements remain in that fixed L.
This placement preserves existing mathematics; it selects no Task, objective change, new theorem role, novelty or publication claim.

Dated candidate, draft and review-pending sentences in the retained text describe the original development.
The selected current decision owns present mathematical adoption and actual review scope.

## Complete retained argument

<a id="argument"></a>

<a id="matrix-capacity-question"></a>
## 1. Question, scope and normalization

The exact F0010 contract permits arbitrary complex coefficients, degree drops, circle zeros and an identically singular matrix polynomial.
This draft supplies three compatible descriptions: an attained finite coefficient-Gram capacity, positive matrix-field log variation, and coefficient-convolution capacities with an exact limit.
The finite formula is the principal additional simplification beyond a circle integral.
These are classical spectral-factorization mechanisms organized for the assigned contract, not a novelty claim or a transfer from a free-semicircular distribution.
G0001 remains paused.

Fix integers l<=u, let s=u-l, and write P(z)=sum_{j=l}^u A_j z^j, with A_j in M_r(C), r>=1.
Multiplication by z^{-l} does not change B(z)=P(z)^*P(z) on T, or the ordinary normalized FK determinant.
Thus in coefficient constructions put A_j=0 outside 0<=j<=s after that shift.
Define
\[
 B(z)=\sum_{k=-s}^s B_kz^k,\qquad
 B_k=\sum_{j=0}^{s-k}A_j^*A_{j+k}\quad(0\le k\le s),
 \qquad B_{-k}=B_k^*.
 \tag{1}
\]
Use Haar probability measure mu, natural logarithms, and normalized trace tr_r=Tr/r.
Write
\[
 L_r(P)=\frac1r\int_T\log|\det P(z)|\,d\mu,
 \qquad D_r(P)=e^{L_r(P)},
 \tag{2}
\]
with L_r=-infinity and D_r=0 when det P is identically zero.
The unnormalized logarithmic determinant is rL_r.
This is the ordinary determinant including zero spectral mass, never the kernel-removed convention.

If det P is not identically zero, its zero set on T is finite.
Factoring the scalar Laurent determinant shows that log|det P| is integrable, including the logarithmic singularities at circle zeros.
All singular values of P are bounded above; since the sum of their logarithms is integrable, each negative logarithmic part is integrable as well.
In particular integral Tr log B=2rL_r is finite.
If det P is identically zero, B has a zero eigenvalue everywhere and integral Tr log B=-infinity.
These facts justify the extended-real conventions below.

<a id="matrix-capacity-reuse"></a>
## 2. Reuse, source checking and methodological boundary

The local search read the Task, S_F0025, the [scalar field baseline](../ledger/Yin_L_G0431_v1.md#single-haar-formulation), its [regularization](../ledger/Yin_L_G0431_v1.md#regularization-and-direction), [Den09-U002](../audits/literature/Den09/Yin_U002.md#finite-section-determinant), [Luc22-U002](../audits/literature/Luc22/Yin_U002.md#luc22-abelian-matrix-approximation), [HP03-U001](../audits/literature/HP03/Yin_U001.md#hp03-u001), and [DR10-U001](../audits/literature/DR10/Yin_U001.md#dr10-u001).
The bibliography and registry were searched for matrix Szego, spectral factorization and operator Jensen.
The scalar Den09 theorem alone does not assert the needed block-matrix limit; Luc22 supplies the trace and determinant-polynomial interface, not a coefficient capacity.
HP03 supplies an inspected operator-Jensen mechanism at its recorded scope.
The elementary compression argument below spells out the required adaptation.

The recognized matrix Fejer--Riesz theorem triggered a further source check.
The retained 33-page DR10 author survey was directly text-read on printed/PDF pp.4--7: Theorem 2.1, outer definition and Toeplitz convention, its surrounding proof, and the uniqueness remark.
The exact theorem gives B=H^*H with a square analytic polynomial H of degree at most s that is outer.
Here outer means that the closure of the range of its analytic Toeplitz multiplier is H^2(F) for a fixed subspace F of C^r.
This established theorem is accepted at the statement and finite-matrix applicability level; reading the proof is not claimed as an independent audit of its full operator proof.
The [new DR10-U002 interface](../audits/literature/DR10/Yin_U002.md#dr10-u002) owns that exact acceptance; the earlier scalar U001 is not silently enlarged.

An external lead for a Bingham matrix-prediction survey timed out.
A suggested arXiv:1212.2260 was directly identified as an unrelated quantum-physics paper and discarded.
A primary search corrected the matrix-Szego attribution lead to Derevyagin--Holtz--Khrushchev--Tyaglov, arXiv:1104.4999, published J. Approx. Theory 164 (2012), 1238--1261.
Its abstract and author publication page were read only as an attribution lead; no theorem from it is a premise.
The local Den09/HP03 mechanism and the actual retained DR10 theorem are sufficient, so no further source or novelty search is needed for this round.

<a id="matrix-finite-gram-capacity"></a>
## 3. An attained finite coefficient-Gram capacity

Let Q=(Q_{ij})_{0<=i,j<=s} be a Hermitian positive semidefinite matrix of size r(s+1), partitioned into r-by-r blocks.
Define the coefficient spectrahedron
\[
 \mathcal G(B)=\left\{Q\succeq0:
       \sum_{i=0}^{s-k}Q_{i,i+k}=B_k\ (0\le k\le s)\right\}.
 \tag{3}
\]
The negative-index equations follow by adjoint.
All entries on the right are the explicit coefficient sums (1); there is no unknown Mahler integral in this definition.
The set is nonempty: Q_{ij}=A_i^*A_j is feasible.
It is compact: the k=0 equation gives Tr Q=Tr B_0, while Q>=0 bounds every matrix entry by the diagonal entries.
It is closed in a finite-dimensional space.

Define
\[
 \operatorname{Cap}_{\rm Gram}(A)
       =\max_{Q\in\mathcal G(B)}\det(Q_{00})^{1/r}.
 \tag{4}
\]
The maximum exists, including at zero capacity.
Then, for every coefficient tuple in the Task's matrix domain,
\[
 \boxed{\operatorname{Cap}_{\rm Gram}(A)=D_r(P)^2.}
 \tag{5}
\]
Thus D_r is the square root of a completely finite coefficient-defined capacity.
Equivalently max det Q00=D_r^{2r}; when positive, L_r=(1/(2r)) max log det Q00.
The feasible problem has a semidefinite constraint and affine block-sum equations.
Its determinant or log-determinant objective is not claimed to be a linear semidefinite-program objective.
In dimension r=1 the objective Q00 is linear.
The determinant-to-the-1/r objective is concave on positive semidefinite matrices, but the proof of (5) does not rely on that convex-optimization fact.

### Upper bound for every feasible matrix

Factor any Q=F^*F and partition F=[F_0 ... F_s], where each F_i has r columns; the number m of rows can be r(s+1).
Set F(z)=sum F_i z^i.
Equations (3) say F(z)^*F(z)=B(z) on T.
The vector v(z) of all r-by-r minors of this m-by-r polynomial matrix is analytic, and Cauchy--Binet gives
\[
 \|v(z)\|^2=\det B(z)\quad(z\in T),
 \qquad \|v(0)\|^2=\det Q_{00}.
 \tag{6}
\]
If det P is not identically zero and v(0)!=0, use the scalar analytic polynomial g(z)=<v(z),v(0)>/||v(0)||, with the inner-product convention chosen so g is analytic.
Then g(0)=||v(0)|| and |g(z)|<=||v(z)||.
Scalar Jensen, obtained also by factoring g and integrating each root factor, yields
\[
 \log\|v(0)\|\le\int\log|g|\,d\mu
       \le\int\log\|v\|\,d\mu
       =\frac12\int\log\det B\,d\mu.
 \tag{7}
\]
All scalar logarithms here are integrable; det B=|det P|^2 on T.
If v(0)=0, the required determinant bound is immediate.
Squaring/exponentiating (7) proves det Q00<=D_r^{2r}.

If det P is identically zero, (6) gives v(z)=0 on T.
Each polynomial minor is identically zero by infinitely many zeros, hence v(0)=0.
Therefore every feasible Q00 is singular and the maximum in (4) is zero.
This handles the entire singular locus, including nonzero P with a kernel and P=0; no limiting nondegeneracy assumption is hidden.

### Matching feasible matrix and the outer boundary

Suppose det P is not identically zero.
Apply the checked DR10 matrix Fejer--Riesz statement to B and choose the outer square polynomial H(z)=sum_{i=0}^s H_i z^i with B=H^*H.
Its determinant is not identically zero, because |det H|^2=det B on T.
By the source's outer definition, closure ran T_H=H^2(F) for a subspace F.
If F were proper, the values of every H(z)x would lie in F, contradicting nonzero determinant.
Thus F=C^r and T_H has dense range in H^2(C^r).

For every a in the open disk, evaluation at a is continuous and onto C^r.
If a row vector annihilated H(a), it would annihilate the values at a of every Hf, then by density every H^2 vector, a contradiction.
Hence det H has no zero in the open disk, and H_0 is invertible.
Scalar Jensen for the polynomial det H now gives
\[
 \int\log|\det H|\,d\mu=\log|\det H_0|.
 \tag{8}
\]
Zeros on T are permitted in (8).
The feasible Gram Q^H_{ij}=H_i^*H_j has det Q^H_00=|det H_0|^2=exp integral log det B=D_r^{2r}.
This proves the matching inequality and attainment in (5).

No explicit formula for the coefficients H_i is presumed: (3)--(4) is the finite coefficient optimization that recovers the value.
The theorem establishes existence of an attaining rank-r Gram when D_r>0; no uniqueness of the entire feasible maximizer is asserted here.
In the zero-capacity branch all feasible Grams have the same zero determinant objective.

### Scaling and changes of presentation

Multiplying every A_j by c multiplies G(B) by |c|^2, so Cap_Gram scales by |c|^2 and D_r by |c|, including c=0.
A common Laurent shift changes no B_k.
Enlarging the exponent interval by zero coefficients changes the feasible matrix size but not (5).
Constant left or right unitary multiplication preserves the determinant.
For a direct sum P=P_1 direct-sum P_2 of sizes r1,r2, formula (2) gives D_r=D_{r1}^{r1/r}D_{r2}^{r2/r}, with r=r1+r2, including zero factors; the corresponding Gram capacity is its square.
This retains total versus normalized determinant exponents explicitly.

<a id="matrix-field-variation"></a>
## 4. Positive matrix-field variation and attainment

Let W_r be measurable Hermitian fields W(z) with aI<=W(z)<=bI almost everywhere for some constants 0<a<=b<infinity depending on W.
Define
\[
 \Phi_B(W)=\int\operatorname{tr}_r(BW-\log W-I)\,d\mu.
\]
Then, with extended-real infimum,
\[
 \boxed{2L_r(P)=\inf_{W\in\mathcal W_r}\Phi_B(W).}
 \tag{9}
\]
When det P is nonzero as a polynomial, equality for a particular W occurs precisely when W=B^{-1} almost everywhere.
Such W belongs to W_r exactly when det P has no zero on T.
Hence (9) is attained uniquely in that circle-zero-free case and is finite but unattained at circle zeros.
If det P is identically zero, the infimum is -infinity, while every admissible value is finite, so it is unattained.

For the lower bound on the nonsingular-polynomial branch, apply x-log x-1>=0 to the eigenvalues of S=B^{1/2}WB^{1/2}.
Trace cyclicity and det S=det B det W give
\[
 \operatorname{Tr}(BW-\log W-I)-\operatorname{Tr}\log B
       =\operatorname{Tr}(S-\log S-I)\ge0
\]
almost everywhere.
Equality holds exactly when S=I.
This uses a trace and determinant identity, not the generally false matrix equation log(BW)=log B+log W.
Integrating gives the bound and its equality condition.

For either determinant branch use W_delta=(B+delta I)^{-1}, delta>0.
It is admissible and
\[
 \Phi_B(W_\delta)=\frac1r\int
   \bigl[\log\det(B+\delta I)-\delta\operatorname{Tr}(B+\delta I)^{-1}\bigr]d\mu.
 \tag{10}
\]
The log integral decreases to integral Tr log B by monotone convergence after subtracting a common upper constant.
The second integrand is between 0 and r; it tends to zero almost everywhere in the nonsingular-polynomial branch, so dominated convergence applies.
On the singular branch the first integral tends to -infinity and the bounded second term cannot change that conclusion.
This proves (9) in every case.
At a circle zero, continuity of the least singular value makes B^{-1} essentially unbounded, even though the exceptional zero itself has measure zero; deleting that point cannot produce attainment in W_r.

<a id="matrix-regularized-interface"></a>
## 5. Regularization, coefficients and optimizer interaction

For epsilon>0 put R_epsilon=(B+epsilon^2 I)^{-1} and
\[
 L_{r,\varepsilon}(P)=\frac1{2r}\int\log\det(B+\varepsilon^2I)\,d\mu.
\]
The regularized version of (9) is an attained unique minimum at R_epsilon, and L_{r,epsilon} decreases to L_r with the extended-real convention.
Its epsilon derivative and, on the finite-L branch, exact error are
\[
 \partial_\varepsilon L_{r,\varepsilon}
  =\frac\varepsilon r\int\operatorname{Tr}R_\varepsilon\,d\mu,
\qquad
 L_{r,\varepsilon}-L_r
  =\frac1{2r}\int\log\det(I+\varepsilon^2B^{-1})\,d\mu\ge0.
 \tag{11}
\]
Differentiation under the integral is valid at every epsilon>0 because the inverse is uniformly bounded.
The error is finite by logarithmic integrability, and has only fixed-input convergence here.
On the identically singular branch L_r=-infinity, so a finite numerical error relative to L_r is not defined; one must use the extended-real limit instead.

For a real coefficient direction H(z)=sum H_j z^j, differentiating B gives C_H=H^*P+P^*H and
\[
 D L_{r,\varepsilon}[H]
      =\frac1r\operatorname{Re}\int\operatorname{Tr}(R_\varepsilon P^*H)\,d\mu.
 \tag{12}
\]
This is an exact regularized sensitivity formula, not a claim that epsilon can be removed inside the integral at a circle zero.
The coefficient-regularity draft owns the general unregularized boundary analysis.
Formula (12) connects the optimizer R_epsilon from (9) directly to perturbation of the original coefficients.
A trial W gives an upper value in (9); neither a trial nor stationarity alone supplies a lower certificate.

The finite Gram construction also applies to B+epsilon^2 I by adding epsilon^2 I to B_0 in (3).
The same proof gives max det Q00=exp(2r L_{r,epsilon}); it uses Fejer--Riesz on this positive polynomial B+epsilon^2I and its scalar determinant, without needing to express it as a square polynomial of the original size beforehand.
Thus both regularized descriptions agree exactly.
At zero capacity the unregularized finite maximum still exists, whereas the matrix-field log infimum is -infinity and has no bounded optimizer.
These distinct attainment statements are compatible.

<a id="matrix-convolution-capacities"></a>
## 6. Finite convolution capacities and their exact limit

For N>=1 let C_N map a vector polynomial x(z)=sum_{j=0}^{N-1}x_jz^j to the full coefficient vector of P(z)x(z), including all output degrees 0,...,N+s-1.
It is the explicit block-convolution matrix (C_N)_{ij}=A_{i-j}.
Set
\[
 G_N=C_N^*C_N=(B_{i-j})_{0\le i,j<N},
 \qquad d_N=rN.
 \tag{13}
\]
The displayed Toeplitz orientation follows by integral z^{-i}B(z)z^j; it is B_{i-j}.
Define a second finite capacity
\[
 c_N(A)=\inf\left\{\frac1{d_N}\operatorname{Tr}(G_N X):
             X\succ0,\ \det X=1\right\}.
 \tag{14}
\]
If G_N>0, arithmetic--geometric mean for the eigenvalues of G_N^{1/2}XG_N^{1/2} gives
\[
 c_N=(\det G_N)^{1/d_N},\qquad
 X_N=(\det G_N)^{1/d_N}G_N^{-1},
 \tag{15}
\]
and equality makes X_N the unique optimizer.
If G_N is singular of rank k with 0<k<d_N, take X=tI on its range and X=t^{-k/(d_N-k)}I on its kernel.
This has determinant 1 and objective tending to 0 as t decreases to 0.
Every positive X has positive trace pairing, so c_N=0 is unattained.
If G_N=0, every admissible X attains zero.
These cases exhaust the finite problem.

For every P in the Task domain,
\[
 \boxed{\lim_{N\to\infty}c_N(A)=\inf_{N\ge1}c_N(A)=D_r(P)^2.}
 \tag{16}
\]
The individual Nth-root sequence is not claimed to be monotone.
Formula (16) is a controlled limit/infimum of finite positive-matrix problems, unlike the single finite Gram maximum (4).
All of its finite values are upper approximations to D_r^2.
The proof below retains both directions and circle-zero behavior.

### A compression logarithm inequality

Let M_B be multiplication by B on L^2(T;C^r), and E_N the isometric inclusion of span{1,z,...,z^{N-1}} tensor C^r.
Then G_N=E_N^*M_BE_N.
For any bounded positive invertible operator T and isometry E, the variational identity
\[
 \langle T^{-1}x,x\rangle
   =\sup_y\{2\operatorname{Re}\langle x,y\rangle-\langle Ty,y\rangle\}
\]
follows by completing the square.
Restricting the right-hand side to y in ran E gives
\[
 (E^*TE)^{-1}\preceq E^*T^{-1}E.
\]
Apply this to T+tI and integrate the norm-convergent representation
\[
 \log x=\int_0^\infty\left((1+t)^{-1}-(x+t)^{-1}\right)dt
\]
on a compact strictly positive spectral interval.
The result is
\[
 \log(E^*TE)\succeq E^*(\log T)E.
 \tag{17}
\]
This is the needed Jensen-compression specialization of the recognized HP03 mechanism, with its proof supplied here.
No inverse of a singular operator is used.

For delta>0, T=M_B+delta I in (17) yields
\[
 \frac1{rN}\log\det(G_N+\delta I)
       \ge\frac1r\int\log\det(B+\delta I)\,d\mu.
 \tag{18}
\]
Each of the N Fourier diagonal blocks of the compressed logarithm is its constant Fourier coefficient, explaining the exact N factor.

If det P is not identically zero, every G_N is positive definite: a vector polynomial x with C_Nx=0 satisfies Px=0 as a polynomial identity, and invertibility over the rational function field forces x=0.
Letting delta decrease to zero in (18), with the finite matrix on the left and logarithmic integrability on the right, gives
\[
 \frac1{rN}\log\det G_N\ge 2L_r(P).
 \tag{19}
\]
This proves the lower bound on every finite capacity.

### Matching regularized upper limit

For each fixed delta>0 the spectra of G_N+delta I and B(z)+delta I lie in the same compact interval [delta,M+delta], where M=sup_T||B||.
For every fixed integer k>=0, finite bandwidth gives
\[
 \lim_{N\to\infty}\frac1{rN}\operatorname{Tr}(G_N+\delta I)^k
       =\frac1r\int\operatorname{Tr}(B+\delta I)^k\,d\mu.
 \tag{20}
\]
Indeed, for a diagonal block indexed at distance at least ks from both ends, every path of k block-multiplication steps stays in the section and equals the infinite multiplication operator's block.
At most 2ks boundary indices remain, and their normalized trace contribution is bounded in absolute difference by 4ks(M+delta)^k/N.
The assertion for small N is irrelevant to the limit.
Linear combinations give (20) for polynomials, and uniform polynomial approximation to log on [delta,M+delta] gives
\[
 \lim_N\frac1{rN}\log\det(G_N+\delta I)
       =\frac1r\int\log\det(B+\delta I)\,d\mu.
 \tag{21}
\]
This carries out the regularized finite-section mechanism already identified in Den09, including its block adaptation.

Determinant monotonicity gives log det G_N<=log det(G_N+delta I), with -infinity allowed on the left.
Take limsup in N using (21), then let delta decrease to zero.
The result is limsup (rN)^{-1}log det G_N<=2L_r.
Combined with (19), this proves the finite-valued limit.
If det P is identically zero, the same upper argument has right-hand limit -infinity and proves c_N->0; nonnegativity supplies the other bound.
Every finite c_N>=D_r^2, and therefore its infimum is the limit.
No rate uniform in degree, size or coefficients is inferred.

In fact on the identically singular polynomial locus, G_N is singular for all sufficiently large N.
A square singular matrix over C(z) has a nonzero rational vector in its kernel by field Gaussian elimination.
Clearing denominators gives a nonzero polynomial vector x with Px=0.
It belongs to the N-dimensional coefficient window for all N larger than its degree, so G_N has a kernel.
The statement does not incorrectly require small sections to be singular: for P(z)=[[1,z],[0,0]], G_1=I_2 even though det P is identically zero; G_N is singular once N>=2.

<a id="matrix-capacity-controls"></a>
## 7. Exact controls, phase obstruction and approximation costs

### Coupled triangular matrix and finite-section boundary

For P_t(z)=[[1,tz],[0,1]], det P_t=1, so L_2=0 and D_2=1 for every complex t.
For t!=0 this is a coupled matrix example: its constant coefficient is I and its linear coefficient is the nonnormal matrix tE12, so no pair of constant unitary changes of input and output can make both diagonal.
Its two coefficients do commute; noncommuting coefficient controls appear separately in (24).
P_t itself is an outer polynomial: its inverse [[1,-tz],[0,1]] is an analytic polynomial, so its Toeplitz multiplier is onto H^2(C^2).
Its coefficient Gram in (3) attains det Q00=1.

For N>=1 the convolution Gram, after grouping the x and y coordinates, is
\[
 G_N=\begin{pmatrix}I&tS_N\\\overline t S_N^*&(1+|t|^2)I\end{pmatrix},
\]
where S_N is the truncated forward shift, so S_N^*S_N has N-1 eigenvalues 1 and one eigenvalue 0.
Its Schur complement gives det G_N=1+|t|^2.
Hence
\[
 c_N=(1+|t|^2)^{1/(2N)},\qquad
 c_N^{1/2}=(1+|t|^2)^{1/(4N)}\downarrow1.
 \tag{22}
\]
Thus the finite convolution approximation pays a visible boundary cost even on a genuinely coupled polynomial with constant determinant.
The finite Gram maximum is already exact.
A polynomial P=diag(z,1) has B=I and every c_N=1; finite exactness is not restricted to constant or monomial scalar polynomials in the matrix setting.

### Circle-zero and ordinary singular controls

For P=diag(1-z,1), D_2=1 and the finite Gram maximum equals 1.
The bounded-field infimum is not attained, since B^{-1}=diag(|1-z|^{-2},1) is unbounded.
In the convolution formula the scalar tridiagonal block for |1-z|^2 has determinant N+1 (recursion d_N=2d_{N-1}-d_{N-2}, d_0=1,d_1=2); the other block is I.
Hence c_N=(N+1)^{1/(2N)} and tends to 1.
This verifies both logarithmic integrability and the nonuniform finite-boundary cost at a circle zero.

For P=diag(1,0), the ordinary determinant is zero, every feasible Q00 in (3) is singular, and every G_N has rank N<2N.
Therefore both capacities are zero, while the positive-matrix-field logarithmic infimum is -infinity.
Discarding the zero direction would instead give a different determinant equal to 1; that convention is excluded here.

### Failure of a coefficient covariance map

A proposed universal formula depending only on the completely positive map
\[
 \Psi_A(X)=\sum_j A_j^*XA_j
 \tag{23}
\]
(or its adjoint version sum A_j X A_j^*) cannot recover D_r.
Fix c!=0 and take
\[
 P_+(z)=\begin{pmatrix}1+z+z^2&cz\\0&1\end{pmatrix},
 \qquad
 P_-(z)=\begin{pmatrix}1+z-z^2&cz\\0&1\end{pmatrix}.
 \tag{24}
\]
Only the coefficient of z^2 changes by a scalar sign; thus the maps (23) agree for all X, as do the adjoint maps, on the same support interval and with the same matrix size.
The matrices in a tuple need not commute because c!=0.
Yet det P_+=1+z+z^2 has both roots on T and Mahler measure 1, whereas det P_-=1+z-z^2 has roots phi and -1/phi, phi=(1+sqrt(5))/2.
Consequently D_2(P_+)=1 and D_2(P_-)=sqrt(phi)>1.
This is an exact obstruction to every proposed capacity depending only on that coefficient covariance map, even with fixed support and matrix size.
It is not an obstruction to all positive-map constructions or to the explicit Gram capacity (3), which retains cross-coefficient products and distinguishes the two inputs.

<a id="matrix-capacity-boundaries"></a>
## 8. Current result, proof-input and continuation boundaries

The finite coefficient-Gram maximum (5) covers the full scalar and square finite-matrix Laurent coefficient domain of the determinant/capacity part of F0010.
Its nontrivial external existence input is the inspected matrix Fejer--Riesz statement from the retained DR10 artifact; no full audit of the external theorem or priority claim is supplied.
Formula (9) provides the complete global matrix-field variation and its actual attainment boundary.
Formulas (14)--(21) provide a separate exact coefficient-convolution limit with full ordinary-kernel scope and both inequalities.
Exact hand calculations (22)--(24) distinguish normalization, boundary losses and the failed covariance-only class; no numerical computation or J artifact is being claimed.

This draft does not establish new coefficient regularity at circle crossings; that parallel component is separately responsible.
No degree-uniform approximation rate, matrix-size-uniform cost, free-semicircular formula, integer Mahler gap, or completion of the whole F0010 contract is asserted.
Before fixed adoption the entire draft and its source interface require the arranged independent review, followed by review of any actual extraction.

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
| dependency | [Exact input](../audits/literature/DR10/Yin_U002.md#dr10-u002) | Exact same-degree square outer matrix polynomial factor for every nonnegative circle symbol, including singularity, at accepted statement/applicability depth only. |
| dependency | [Exact input](../audits/literature/Luc22/Yin_U002.md#luc22-u002) | Complex determinant-polynomial and trace interface at the precise abelian approximation section; original kernel-removed convention is not substituted for the local ordinary singular branch. |

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
| dependency | [Exact material](../audits/literature/DR10/Yin_U002.md#dr10-u002) | Exact same-degree square outer matrix polynomial factor for every nonnegative circle symbol, including singularity, at accepted statement/applicability depth only. |
| dependency | [Exact material](../audits/literature/Luc22/Yin_U002.md#luc22-u002) | Complex determinant-polynomial and trace interface at the precise abelian approximation section; original kernel-removed convention is not substituted for the local ordinary singular branch. |
| review | [Actual finding](../audits/reviews/Yin_R_F0004_v1.md#matrix-capacity-whole-independent-finding) | Whole unchanged matrix Sections 1–8 and equations (1)–(24): arbitrary fixed finite Laurent matrix input, exact finite block-Gram capacity and DR10 outer matching, positive-field variation and attainment, regularized sensitivities, complete block-convolution finite rank cases and both limit inequalities, ordinary singular/zero branches, coupled and covariance-only controls. Accepted DR10 statement depth and all normalization/cost limits retained. |


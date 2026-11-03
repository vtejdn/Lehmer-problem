---
author: Yin
---
# Joint projection control with a paid low-eigenvalue rank and a multiscale obstruction

Current complete mathematical home: [C506](../claims/Yin_C_G0506_v1.md#statement), actually adopted after the [entire current SELF](../audits/reviews/Yin_R_G0715_v1.md#complete-joint-cutoff-whole-self-finding).
The complete original four-section/fourteen-formula body and all eight input roles remain below without mathematical change.
The original [R409 whole finding](../audits/reviews/Yin_R_G0409_v1.md#joint-cutoff-whole-independent-finding), its22:58 date, separate noncontributing arrangement, upstream roles, source limits and original declaration remain at their exact old inputs; the currently unestablished extra-context/initial-order relationship is UNKNOWN and is not resolved by this later SELF.
The dated unresolved moving-family checkpoint below is historical: [C171](../claims/Yin_C_G0171_v1.md#two-block-torus-statement) later proves actual divergence by a separate argument, while this count/trace theorem alone supplies no coherence lower bound.
The existing [DMS84-U001](../audits/literature/DMS84/Yin_U001.md#dms84-matrix-power-support) owns the actual manuscript attribution depth; there is no new PDF, source-proof or numerical inspection.

Date: 2026-10-18T14:56.
Human author Yin.
Root assigned the next substantive joint signed-Fourier direction after the two-factor Toeplitz comparison.
The loglog_cyclic_review agent develops the finite spectral cutoff and multiple-mode test here.
Root's joint-budget direction is credited; root and loglog_cyclic_review are proof contributors.
This fixed bounded exploration asserts no automatic new arithmetic coverage.
No mathematical program or numerical spectral evaluation is used.

<a id="joint-spectral-cutoff-reuse"></a>
## Reuse and the changed paid quantity

[L404](Yin_L_G0404_v1.md#joint-boundary-symbol) already gives H_P B_n=n W C_q and kappa=(n/d)(||W C_q||_W-1).
Its [separated-factor failure](Yin_L_G0404_v1.md#boundary-factor-budget-and-failure) shows why separately bounding ||W||_W cannot supply new near-one coverage beyond C92.
The current direction keeps the full matrix product A f(A^tA) A^t before taking coefficients.
It permits small eigenvalues, but pays the number of those modes through a positive matrix remainder.

[C160](../claims/Yin_C_G0160_v1.md#fixed-seed-original-factor-projection) already combines uniform Gram coercivity, polynomial growth of matrix-power support and bounded-rank original-factor correction.
[L402](Yin_L_G0402_v1.md#moving-exponent-gram-feasibility) gives an actual moving-exponent Salem family where the smallest raw Gram eigenvalue tends to zero, leaving open the normalized joint symbol.
A bounded search of G-line claims, ledgers and drafts for low eigenvalues, spectral cutoffs/outliers and polynomial-support projection estimates found no retained version of the bounded-low-mode replacement developed here.
This is a bounded reuse finding, not a novelty claim.
The classical matrix-power support mechanism is attributed at the existing [DMS84-U001](../audits/literature/DMS84/Yin_U001.md#dms84-matrix-power-support) scope; the full finite cutoff proof and its constants are supplied locally below.

<a id="joint-cutoff-target"></a>
## 1. Full finite criterion with the low modes paid separately

Let N>=r>=1 be integers and A a full-column-rank real N-by-r matrix, let G=A^tA, and choose a positive upper spectral scale B with G<=B I.
Let d>=1 be the ORIGINAL integer normalization degree; it need not equal N-r if A is a larger numerator's relation matrix.
Put

    X=A/sqrt(B), H=G/B, U=2H-I,
    Pi=A G^(-1)A^t, R=I-Pi,
    kappa_d(R)=(2/d)sum_(h=1)^(N-1)
                              abs(sum_i R_(i,i+h)).

The square root of B is a real analytic normalization only; it creates no integral auxiliary or arithmetic norm.
Assume an integer nu>=0 and C>=1 satisfy this ACTUAL finite support condition for every integer k>=0:

    every row of X T_k(U) X^t has at most C(k+1)^nu
    possibly nonzero entries.                              (1)

Here T_k is the Chebyshev polynomial characterized by T_k(cos theta)=cos(k theta), including T_0=1.
One may verify (1) by bounding the union of all supports X H^j X^t for 0<=j<=k.
Numerical smallness of an entry is not a support zero.
This is a finite polynomial-support hypothesis, not ordinary linear bandwidth or a circulant assumption.

Fix 0<delta<=1, set s=nu+2, and define

    J_s(u)=[integral_0^u v^s(1-v)^s dv]
                       /[integral_0^1 v^s(1-v)^s dv],
    chi_delta(x)=0                         for 0<=x<=delta/2,
                =J_s(2x/delta-1)          for delta/2<x<delta,
                =1                        for delta<=x<=1,
    f_delta(0)=0, f_delta(x)=chi_delta(x)/x for x>0.

This is an explicit C^s function on [0,1], with 0<=chi_delta<=1.
The derivatives of J_s of orders 1 through s vanish at each joining endpoint, while its endpoint values are 0 and 1.
The division causes no singularity because chi_delta is identically zero near zero.
Define the fixed scalar function and constant

    F(theta)=f_delta((1+cos theta)/2),
    M_s=(1/(2pi))integral_0^(2pi) abs(F^(s)(theta)) dtheta,
    K_(delta,nu,C)=C[2/delta+2^(nu+2)M_s].                  (2)

Every quantity in (2) is supplied by the displayed elementary piecewise polynomial/rational cutoff and depends only on delta and nu, and then C.
M_s is finite and dimension independent; no hidden input-dependent approximation constant is being assumed.
No numerical evaluation of it is needed.
Let b_delta be the number of eigenvalues of H STRICTLY below delta, with multiplicity.
The finite conclusion is

    kappa_d(R) <= (N/d)K_(delta,nu,C)
                           +((N-1)/d)b_delta.             (3)

Thus at N=2d, fixed delta,nu,C and bounded b_delta give a uniform joint projection coefficient bound even when lambda_min(G)/B tends to zero.
All these hypotheses remain actual costs; none is asserted automatically for an arithmetic input class.

### Complete smooth-polynomial and matrix proof

F is real, even, C^s and 2pi-periodic.
Let its Fourier coefficients be a_k=(1/(2pi))integral F(theta)exp(-ik theta)dtheta.
Integrating by parts s times, with matching periodic derivatives, gives |a_k|<=M_s/|k|^s for k!=0.
Also |a_0|<=2/delta because 0<=f_delta(x)<=2/delta.
The derivative at a joining point is understood by the matching C^s extensions; the piecewise smooth derivatives are integrable.
The resulting Fourier series is absolutely convergent because s>=2.
It equals F: its Fejer means converge uniformly to F by positivity, integral one and concentration of the finite Fejer kernels, while absolute convergence makes the same means converge to that series.
For the concentration assertion, away from a fixed neighborhood of zero the elementary formula |sum_(j=0)^L exp(ij theta)|^2/(L+1) is O(1/(L+1)); uniform continuity handles the remaining neighborhood.
This supplies the needed Fourier identity without an imported approximation-rate theorem.

Therefore the Chebyshev expansion is exactly

    f_delta(x)=c_0+sum_(k>=1)c_k T_k(2x-1),
    c_0=a_0, c_k=2a_k,
    |c_0|<=2/delta, |c_k|<=2M_s/k^(nu+2).                (4)

The coefficients are real because F is real and even.
The finite spectral theorem, applied to H with spectrum in (0,1], turns (4) into an operator-norm convergent matrix series.
For each k, ||T_k(U)||_op<=1 and ||X||_op<=1.
Hence every entry of X T_k(U) X^t has modulus at most1.
By (1), the absolute sum of all its matrix entries is at most N C(k+1)^nu.
The coefficient sum of its circle symbol v_N(z^-1)^t X T_k(U) X^t v_N(z) is no larger: each signed coefficient is a sum over one matrix diagonal, before taking its absolute value.
Using (4) and

    sum_(k>=1)(k+1)^nu/k^(nu+2)
       <=2^nu sum_(k>=1)k^-2<=2^(nu+1)

gives the absolute convergence and full joint-symbol estimate

    ||v_N(z^-1)^t X f_delta(H) X^t v_N(z)||_W
                                    <=N K_(delta,nu,C).    (5)

This estimates the ACTUAL matrix product before its Fourier coefficients, rather than multiplying separate Wiener norms of a density and a boundary factor.
It is still a sufficient upper estimate, not the exact coefficient mass.

For an orthonormal eigenvector v_i of H with eigenvalue lambda_i>0, put u_i=Xv_i/sqrt(lambda_i).
The u_i are orthonormal, and direct substitution gives

    Pi=sum_i u_i u_i^t,
    X f_delta(H) X^t=sum_i chi_delta(lambda_i)u_i u_i^t,
    E_delta:=Pi-X f_delta(H)X^t
                   =sum_i[1-chi_delta(lambda_i)]u_i u_i^t.
                                                               (6)

Consequently 0<=E_delta<=I, its rank is at most b_delta, and trace E_delta<=b_delta.
For ANY positive semidefinite N-by-N matrix E,

    sum_(i!=j)|E_ij| <= (N-1)trace E.                    (7)

Indeed |E_ij|<=sqrt(E_ii E_jj), and the square of the sum of diagonal square roots is at most N trace E.
Subtracting trace E proves (7).
The nonconstant Fourier mass of E's circle symbol is at most this off-diagonal entry sum.
The nonconstant coefficients of R=I-Pi are the negatives of those of Pi.
Combining (5)--(7), retaining both signs and dividing by d, proves (3).
A sharper supplied correction is ((N-1)/d)trace E_delta; it too is an actual paid quantity.
No sign of an individual off-diagonal entry, independent-mode law or arithmetic norm floor has been inferred from positivity.

<a id="original-factor-cutoff-price"></a>
## 2. Actual polynomial windows, classical relation and original-factor correction

For a polynomial F of degree D<N, take A to be the FULL coefficient columns F,tF,...,t^(N-D-1)F.
The usual coefficient derivation from L321 identifies its relation-projection symbol with H_F B_(N-D).
In particular when F=P is the original polynomial, the present joint product is exactly L404's n W C_q; it does not introduce a different circle function or reduce the original P modulo itself.
The B normalization cancels inside the matrix product just as the primitive predictor scalar cancels in L404.

If F=P C has degree D=d+c, with the original window N=2d and c<d, its relation subspace is contained in the full P relation subspace.
The difference of their residual projections is positive semidefinite of rank c, exactly as in C160.
Using (7) on this difference gives

    kappa_(2d)(P) <= 2K_(delta,nu,C)
                         +(2-1/d)b_delta+(2-1/d)c.       (8)

The same original d occurs in all three terms.
The symbols for the raw numerator and original minimal polynomial are not silently identified, and the correction is not recomputed at degree D.
The count b_delta belongs to the ACTUAL raw Gram in that common window.

The mechanism extends the local C160 geometric-series test: a uniform lower normalized eigenvalue makes b_delta=0, but (3) permits finitely many exceptional small modes.
Polynomial approximation plus support propagation is classical, already identified by DMS84-U001.
Its inspected theorem assumes a bounded inverse and is NOT imported to justify the present low-mode replacement; (2)--(7) give the full local proof.
No novelty or whole original-source audit is claimed.
The positive-rank correction (7) is the same established matrix estimate used in C160, with a positive contraction in place of a projection.

The criterion does not itself identify a new near-one arithmetic class.
For example a uniformly sparse annihilator of width O(d), including L402's raw 48-term numerator, is already in C92's restricted gap domain.
Here the gain is a weaker sufficient way to CONTROL a joint projection symbol on specified inputs, not a new source of small total measure or an uncharged arithmetic coverage theorem.
The parameters delta, support growth and exceptional rank must all be supplied before (8) has a uniform consequence.

<a id="moving-exponent-low-mode-packing"></a>
## 3. The moving-exponent family has many low modes, not just one

Use exactly L402's actual family and notation, writing the raw numerator as F_j rather than N_j to avoid confusing it with the window:

    F_j(x)=A_j(x)+x^(c_j)B_j(x),
    L_j=K+a_j+b_j+2, deg A_j,deg B_j<=L_j,
    A_j(1)=B_j(1)=0,
    ||A_j||_1+||B_j||_1<=64,
    c_j>(L_j+1)^2,
    D_j=c_j+L_j, d_j=D_j-3,
    N_j=2d_j, r_j=N_j-D_j=c_j+L_j-6.

These are the SAME original irreducible Salem inputs and the SAME complete cyclotomic removal (x-1)^3 as L402.
In particular L_j>=6 and L_j tends to infinity.
Let T_j have the r_j full shifts of F_j in N_j coordinates, and let G_j=T_j^tT_j.
The columns are independent and all displayed product coefficients fit in this original window.
Finite convolution gives ||T_j||_op<=||F_j||_1<=64, so B=4096 is a supplied upper spectral scale.
This is an analytic inequality, not an evaluated matrix.

The matrix-power support condition (1) also holds with fixed parameters

    nu=4, C=27(2K+5).                                 (9)

Indeed every exponent difference of F_j is of the form e_0+e_1 a_j+e_2 b_j+e_3 c_j, with |e_0|<=K+2 and |e_i|<=1.
A nonzero entry of T_j G_j^h T_j^t therefore has an offset which is a sum of at most h+1 such differences.
For 0<=h<=k these are all contained in the single integer box with bounds (k+1)(K+2) and k+1.
Its number of represented offsets is at most

    [2(k+1)(K+2)+1](2k+3)^3<=27(2K+5)(k+1)^4.

Coinciding represented offsets and finite-window truncations only reduce this count.
The same support bound applies to a Chebyshev polynomial of degree k in 2G_j/4096-I, proving (9) for every actual row.
Neither a Euclidean bandwidth assumption nor a source estimate on a limiting Toeplitz operator is used.

Now fix ANY real 0<a<=4096 and put

    ell_j=ceil(32768 L_j/a), p_j=ell_j+L_j,
    J_j=floor(c_j/p_j),
    X_(j,t)(x)=x^(t p_j)(1+x+...+x^(ell_j-1)),
                       0<=t<J_j.                       (10)

If J_j=0 the following count is vacuous; it becomes positive and unbounded along the family.
The vectors X_(j,t) have pairwise disjoint quotient supports and squared norm ell_j.
Their largest exponent is J_j p_j-L_j-1<=c_j-L_j-1<r_j, so every one is a legal quotient vector for this SAME T_j.

Set U_j=A_j/(1-x), V_j=B_j/(1-x), as in L402.
They have degree at most L_j-1 and

    ||U_j||_2+||V_j||_2<=64 sqrt(L_j).

The exact image of each test vector is

    F_j X_(j,t)
       =x^(t p_j)(1-x^(ell_j))(U_j+x^(c_j)V_j).          (11)

Its first endpoint band is contained in [t p_j,(t+1)p_j-1] and its second is that interval translated by c_j.
All first bands lie in [0,c_j-1], and all second bands in [c_j,2c_j-1].
Thus the image supports are disjoint for DISTINCT t, INCLUDING between the unshifted and c_j-shifted bands.
The extra L_j tails are included in p_j, rather than discarded at the band boundary.
Also 2c_j-1<N_j because L_j>=6, so no coefficient is lost beyond the original window.
The individual norm estimate is

    ||F_j X_(j,t)||_2^2<=16384 L_j,
    ||F_j X_(j,t)||_2^2/||X_(j,t)||_2^2
                    <=16384 L_j/ell_j<=a/2.             (12)

Since BOTH the test vectors and their images are pairwise orthogonal, every nonzero linear combination satisfies the same Rayleigh upper bound a/2.
This verifies a J_j-dimensional low-Rayleigh SUBSPACE, not merely J_j separate scalar tests.
The finite spectral decomposition consequently gives at least J_j eigenvalues of G_j at most a/2: otherwise that subspace would intersect the span of eigenvectors with eigenvalues greater than a/2 nontrivially, a contradiction.
In particular

    #{lambda(G_j)<a}>=J_j
       =floor(c_j/[ceil(32768 L_j/a)+L_j]) -> infinity.  (13)

For the limit, the denominator is at most (32768/a+1)L_j+1 while c_j>(L_j+1)^2 and L_j tends to infinity.
Every constant and threshold is fixed before j varies.
No prime selection, matrix computation or numerical eigenvalue calculation was performed.

For the cutoff (2) with delta=a/4096, chi_delta is zero on every normalized eigenvalue at most a/(2*4096).
Thus the SAME subspace also gives

    trace E_delta>=J_j -> infinity.                     (14)

So this family defeats even the sharper trace-paid remainder certificate at every fixed positive relative threshold, not merely a proposed bound on its rank.
The actual Fourier mass of E_delta can still be much smaller than the entrywise estimate (7).
Neither (13) nor (14) is a lower bound for the actual original kappa.

<a id="joint-cutoff-outcome"></a>
## 4. Exact gain, failed implication and next boundary

The new conditional estimate permits a bounded number of arbitrarily small normalized Gram eigenvalues while controlling the FULL joint projection through (3) or (8).
It preserves L404's original symbol and primitive-normalization boundary, and does not recycle the separate factor product ||W||_W ||C_q||_W.
For L402 the support geometry (9) is uniformly available, but the number and trace of low modes diverge by the explicit all-combinations packing argument.
The complete original rank-three correction is still only the last term c=3 in (8); it does not absorb that unbounded collection of raw Gram modes.

This closes the particular hope that a fixed number of degenerating modes is the only obstruction in L402.
It does not settle L402's actual joint coefficient norm, nor does it reject a method that keeps cancellation WITHIN the low-mode projection or between its symbol and the good-mode symbol.
Allowing delta to vary with j changes the explicit cutoff constant M_s and 2/delta in (2); those costs cannot be declared uniform for free.
No optimized varying-threshold estimate is proved here.
A further useful estimate would have to control the joint low-mode symbol itself, rather than replace it solely by its rank or trace.
No new arithmetic norm income, uniform small-measure coverage, numerical scan or Task stop follows.

<a id="joint-cutoff-fixed-inputs"></a>
## Exact inputs and reuse boundaries

| Role | Target | Scope |
| --- | --- | --- |
| Same joint symbol | [L404](Yin_L_G0404_v1.md#joint-boundary-symbol) | Actual two-boundary normalization, H_P B_n=n W C_q and original d/window convention; the present matrix split estimates this same product. |
| Failed separate estimate | [L404 comparison](Yin_L_G0404_v1.md#boundary-factor-budget-and-failure) | C92 already blocks the individual normalized annihilator Wiener bound; no reuse of that estimate as a new route. |
| Existing finite projection mechanism | [C160](../claims/Yin_C_G0160_v1.md#fixed-seed-original-factor-projection) | Uniform coercivity and matrix-power support as comparison, and the actual same-window positive-rank correction reused in (8). |
| Exact coefficient identity | [L321](Yin_L_G0321_v1.md#residual-laurent-square-identity) | Full-column relation projection and signed Fourier diagonal normalization, with the pure coefficient identity applied to the actual numerator. |
| Classical attribution | [DMS84-U001](../audits/literature/DMS84/Yin_U001.md#dms84-matrix-power-support) | Polynomial approximation and matrix-power support mechanism only; no bounded-inverse theorem or external approximation constant is used for the new cutoff. |
| Actual family and original factor | [L402 schedule](Yin_L_G0402_v1.md#fixed-trace-moving-exponent-schedule) | Same genuine Salem minimal polynomial, full degree and cyclotomic removal, fixed K and moving prime schedule; prior source acceptance unchanged. |
| Two-block coefficients and scale | [L402 Gram argument](Yin_L_G0402_v1.md#moving-exponent-gram-feasibility) | A_j(1)=B_j(1)=0, exact 64 and L_j bounds, c_j>(L_j+1)^2, quotient window and prior one-vector norm estimate. |
| Scope of old arithmetic coverage | [C92](../claims/Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Uniformly sparse annihilators of width O(d) already give a restricted gap; no new near-one class is claimed merely from the L402 control. |

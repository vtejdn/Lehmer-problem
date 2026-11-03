---
author: Yin
---
# Actual Toeplitz boundary predictors and the remaining signed coefficient budget

Current complete mathematical home: [C499](../claims/Yin_C_G0499_v1.md#statement), adopted at its actual current decision after the [entire current SELF](../audits/reviews/Yin_R_G0711_v1.md#complete-toeplitz-boundary-whole-self-finding).
The original five-section/twelve-formula author body, contribution and source account remain below without mathematical change.
The original [R405 whole finding](../audits/reviews/Yin_R_G0405_v1.md#toeplitz-boundary-whole-independent-finding), its actual22:41 record and disclosed fixed-proof/scope/retention arrangement remain at their original inputs; this current SELF does not backdate a new isolated inspection.
The complete original source-reading occurrence is retained in [Sim08-U001](../audits/literature/Sim08/Yin_U001.md#original-toeplitz-boundary-reading-20261018), with the individual reader/minute unestablished and no new primary PDF or source-proof audit.

Date: 2026-10-18T14:40.
Human author Yin.
Root proposed the bounded S3/S8 test of the full finite Gohberg--Semencul formula, actual boundary predictors and their primitive denominator cost.
The loglog_cyclic_review agent develops the finite matrix proof, normalized symbol identities and expense comparison below.
Both are proof contributors.
The complete bounded exploration is retained here; no automatic coverage theorem is asserted.
No mathematical program, numerical evaluation, new J or source acquisition is used.

<a id="toeplitz-boundary-reuse"></a>
## Reuse, source attribution and actual remaining question

[L4](Yin_L_G0004_v1.md#gram-lower-certificate), [L56](Yin_L_G0056_v1.md#polynomial-relation-lifts) and [L241](Yin_L_G0241_v1.md#joint-determinant-equals-old-certificate) already retain saturation, the relation/orbit Gram identity, the full evaluation discriminant factor and the optimized scalar-volume ceiling.
Those results are not re-proved here.
[L321](Yin_L_G0321_v1.md#residual-laurent-square-identity) gives the actual normalized residual symbol in terms of the whole inverse relation Gram.
[L363](Yin_L_G0363_v1.md#primitive-prediction-normalizer) gives the actual predictor, primitive cofactor gcd and least denominator, while its [cokernel formula](Yin_L_G0363_v1.md#cokernel-denominator-identity) identifies the responsible boundary-element order.
[L364](Yin_L_G0364_v1.md#selected-element-index) distinguishes this selected order from the entire Gram cokernel size.
The finite optimizer remains an upper Mahler approximation; [L365](Yin_L_G0365_v1.md#circle-zero-prediction-candidate) already warns against reversing that direction.

The bounded G-line search/read found no retained complete boundary-product formula with the normalized signed coefficient expense derived below.
This is not an assertion of mathematical novelty.
The actual retained Simon arXiv0806.1528v1 was text-read at printed/PDF pages 8--11, particularly the page 9 attribution that the Toeplitz Gohberg--Semencul formula is equivalent to the CD formula.
The existing [Sim08-U001](../audits/literature/Sim08/Yin_U001.md#sim08-u001) already owns that exact attribution and its restricted projection statements.
The source does not print the finite inverse-matrix formula used below at that passage, and the nearby OPUC conventions are not silently substituted for our matrix orientation.
The complete local proof below uses only block inversion and finite shifts; no uninspected inverse-Toeplitz estimate, source-proof upgrade or new U is needed.

The question is whether the actual two-boundary representation supplies signed cancellation beyond the scalar determinant already exhausted by L241.
A fixed formula alone will not be called a coefficient bound, and the original integral normalization is retained before considering any conditional budget.

<a id="finite-real-gohberg-semencul"></a>
## 1. Full finite real symmetric Toeplitz identity

Let T_n=(g_(i-j))_(0<=i,j<n) be a REAL symmetric positive definite Toeplitz matrix, with g_(-h)=g_h and n>=1.
Let M=T_n^(-1), let e_0 be the first coordinate vector, and put

    x=M e_0=(x_0,...,x_(n-1))^t, x_0>0.

Let J reverse the n coordinates and let S be the nilpotent downward shift, S e_j=e_(j+1) for j<n-1 and S e_(n-1)=0.
Persymmetry gives JT_nJ=T_n and hence MJ=JM, so the LAST inverse column is exactly Jx.
Define the lower triangular Toeplitz matrix L_n(a) to have successive columns a,Sa,...,S^(n-1)a, and set

    y=SJx=(0,x_(n-1),...,x_1)^t.

Then the entire inverse matrix is

    T_n^(-1)=[L_n(x)L_n(x)^t-L_n(y)L_n(y)^t]/x_0.  (1)

The minus sign, direction of the shift and division by x_0 are essential.
The two actual boundary columns are x and Jx; the shifted second column y enters (1), not Jx without the shift.

For a direct proof with n>=2, the Schur complement in M at its first entry gives

    M-xx^t/x_0 = diag(0,T_(n-1)^(-1)).

This follows by multiplying the usual block inverse, or because the Schur complement of the first inverse block is the inverse of the complementary block of T_n.
By persymmetry the corresponding last-entry identity is

    M-(Jx)(Jx)^t/x_0 = diag(T_(n-1)^(-1),0).

Shifting the second equation by S on the left and S^t on the right, then subtracting, yields

    M-SMS^t=(xx^t-yy^t)/x_0.                       (2)

Sum S^j(2)(S^t)^j for 0<=j<n.
The left side telescopes to M because S^n=0, while the right side is exactly (1).
For n=1, y=0 and (1) reads M=x_0, proving the omitted endpoint directly.
This establishes the complete finite formula without positivity of the rank-two difference on the right of (2).

<a id="primitive-two-boundary-normalization"></a>
## 2. Actual polynomial weight and the least integer predictor denominator

Now let P be a nonzero REAL integer polynomial of degree d, with nonzero constant coefficient, and use the actual autocorrelation weight H_P(z)=P(z)P(z^-1) on the circle with normalized Haar measure.
Let T_n be its n-by-n coefficient Gram, so T_n is positive definite even if P has circle zeros.
The finite Gram and inverse entries, predictor coefficients and energies below are rational, and every Gram determinant is positive.
Write D_n=det T_n, D_0=1.

Use L363's predictor of degree at most n-1, normalized by q(0)=1:

    q=q_(n-1), r=||Pq||_2^2=D_n/D_(n-1),
    q=x/x_0 as coefficient vectors, x_0=1/r.

The degree is allowed to be LESS than n-1; all boundary vectors are padded to the full length n.
Every zero of q lies strictly outside the closed unit disk by L363's normal-equation argument.
Let k=k_(n-1) be its LEAST positive integer denominator and let Q=kq be the corresponding primitive integer polynomial with Q(0)=k.
For n=1 use q=Q=1 and k=1.
For n>=2, with b_(n-1)=(g_1,...,g_(n-1))^t, the exact old arithmetic identity is

    k=ord_((Z^(n-1))/T_(n-1)Z^(n-1))([b_(n-1)]).

This is the actual boundary class, not the size or exponent of that finite group.
Put

    E=||P Q||_2^2=k^2 r in Z_(>0),
    Q_vec=(Q_0,...,Q_(n-1))^t,
    Q_flat=(0,Q_(n-1),...,Q_1)^t.

The reversed boundary predictor has the same minimum clearing integer k.
Substituting x=q/r in (1) gives the completely integer-numerator matrix identity

    T_n^(-1)=[L_n(Q_vec)L_n(Q_vec)^t
                    -L_n(Q_flat)L_n(Q_flat)^t]/E. (3)

In particular the scalar k has NOT supplied arithmetic income: both boundary products and the predictor energy scale by k^2, which cancels exactly.
E is a supplied common inverse-matrix denominator; no assertion is made that it is minimal after further cancellation among its entries.
No original resultant or field norm is extracted from these matrix denominators.

<a id="joint-boundary-symbol"></a>
## 3. Exact circle diagonal, derivative form and positive root representation

Let v_n(z)=(1,z,...,z^(n-1))^t and define the actual Laurent polynomial

    B_n(z)=v_n(z^-1)^t T_n^(-1)v_n(z).

Write q(z)=sum_(a=0)^(n-1)q_a z^a, with q_0=1 and permitted trailing zeros.
For 0<=ell<n, (1) gives the coefficient identity

    [z^ell](r B_n)
       =sum_(a=0)^(n-1-ell)(n-ell-2a)q_a q_(a+ell). (4)

Indeed L_n(q)^t v_n has j-th component z^j sum_(a=0)^(n-1-j)q_a z^a.
Summing its product with the inverted-variable component gives the coefficient weight n-a-ell.
For the shifted reversal, reindexing a to n-a-ell gives weight a on the same products, excluding the zero a=0 contribution.
Their difference is n-ell-2a, proving (4); negative coefficients follow by symmetry.
Thus the FULL Laurent identity is

    r B_n(z)=n q(z)q(z^-1)
       -z q'(z)q(z^-1)-z^-1 q'(z^-1)q(z).         (5)

The coefficient weights have both signs; replacing them separately by absolute values can destroy the proposed gain.
For the primitive integer predictor, the same formula is

    B_n(z)=[n Q(z)Q(z^-1)
       -z Q'(z)Q(z^-1)-z^-1 Q'(z^-1)Q(z)]/E.      (6)

Every coefficient, phase and denominator in this formula is exact.

Let ell_q be the ACTUAL degree of q, and let zeta_1,...,zeta_(ell_q) be all its zeros with multiplicity, each with |zeta_j|>1.
On the circle put

    W(z)=|P(z)Q(z)|^2/E=|P(z)q(z)|^2/r,
    K_q(z)=n-2 Re[z q'(z)/q(z)], C_q(z)=K_q(z)/n.

Then W>=0 and integral W=1.
For each |z|=1 and |zeta|>1,

    1-2 Re[z/(z-zeta)]=(|zeta|^2-1)/|z-zeta|^2.

Using the logarithmic derivative of q therefore gives

    K_q(z)=n-ell_q
       +sum_(j=1)^(ell_q)(|zeta_j|^2-1)/|z-zeta_j|^2>0,
    integral K_q=n, integral C_q=1.                (7)

The constant n-ell_q is at least 1; formal padding is not mistaken for a root at infinity with an extra cost.
For a constant predictor the sum is empty and C_q=1.
No quantitative separation of the zeros from the circle is inferred from their strict exterior location.
Equations (5)--(7) give

    H_P(z) B_n(z)=n W(z) C_q(z).                   (8)

The left side is a finite rational Laurent polynomial.
Although C_q is generally a rational circle function, its denominators cancel in this product exactly as in (6), not by omitting poles or circle zeros.
The original P remains in W; no reduced remainder is substituted on the circle.

For an ACTUAL monic irreducible nontorsion integer unit P, let N=d+n and use the full relation shifts in that coefficient window.
The already proved L321 identity yields the normalized residual symbol

    N k_R=N-H_P B_n=N-n W C_q,
    integral(H_P B_n)=n,
    kappa_R=[||H_P B_n||_W-n]/d
             =(n/d)(||W C_q||_W-1).               (9)

The integral n follows from the trace of the relation projection, and also records the exact compatibility of the two factors: their separate means 1 do not imply their product has mean 1 for arbitrary positive functions.
Here the compatibility is supplied by the actual predictor and inverse Gram.
No original field-norm floor is attached to H_P B_n, which vanishes at every original root.
The identities do not replace the original degree d or the actual window N by a different field or a predictor degree.

<a id="boundary-factor-budget-and-failure"></a>
## 4. An explicit two-factor conditional bound and its old near-one obstruction

For each fixed input, C_q has an absolutely convergent Fourier series because all zeros of q lie strictly outside the circle.
If s_j=sum_(a=1)^(ell_q)zeta_a^(-j), then the geometric-series expansion of the logarithmic derivative gives

    C_q(z)=1+(1/n)sum_(j>=1)[s_j z^j+conjugate(s_j)z^-j],
    tau_q=(2/n)sum_(j>=1)|s_j|,
    ||C_q||_W=1+tau_q,
    tau_q<=(2/n)sum_a 1/(|zeta_a|-1).              (10)

All root multiplicities remain, and a finite value at each input is not a uniform bound.
Let A_W=||W||_W, which is the absolute coefficient sum of the ACTUAL finite normalized product square, with its signed autocorrelations already collected.
It is not replaced by the usually larger effective-support bound ||PQ||_1^2/E.
Finite/infinite absolutely convergent coefficient convolution in (8) gives the complete conditional estimate

    kappa_R<=(n/d)[A_W(1+tau_q)-1].                (11)

Thus at n=d, uniform supplied bounds for BOTH A_W and tau_q would imply a bounded actual kappa, to which the old L318/L321 restricted gap criterion applies with its original arithmetic bundle and frequency prices.
This is a coefficient condition, not an automatic consequence of positive definiteness, predictor stability or finite displacement rank.
It pays the normalized density and the summed inverse-root Fourier tails separately.

However this separated-factor sufficient condition DOES NOT open a new near-one class beyond the old short-annihilator mechanism.
The decisive reason is that

    W(z)=P(z)P(z^-1)Q(z)Q(z^-1)/E

is a NONZERO rational Laurent polynomial with W(alpha)=0 at every original root alpha.
Its constant coefficient is integral W=1.
Since P and Q have nonzero endpoints, its actual exponent span is

    A=2(d+ell_q)<=2(d+n-1).

By Parseval ||W||_2^2>=1, so its effective support satisfies

    rho(W)=A_W^2/||W||_2^2<=A_W^2.

Apply the actual [C92 zero-value theorem](../claims/Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) at h=A m(P)/d in its declared domain 0<h<=h_0.
It gives

    A_W>=sqrt((1+epsilon(h))/(epsilon(h)+2h)).       (12)

This is a direct application to a vanishing Laurent polynomial, not a nonzero-resultant logarithm at zero.
At n=d, a hypothetical positive-total-measure sequence m(P)->0 has 2m<=h<4m, so the right side tends to infinity.
In particular a uniform A_W bound alone already excludes that class through C92, without needing tau_q or the new inverse formula.
Any product-norm upper certificate in (11) is at least (n/d)(A_W-1), since tau_q>=0.
At n=d this supplied certificate therefore cannot stay bounded along such a hypothetical sequence.
This is a failure of the SEPARATED absolute-factor estimate, not a lower bound on the actual kappa and not a construction of a near-one sequence.

The conclusion does not rule out cancellation in the actual Fourier convolution W C_q before taking absolute values.
Equation (9) shows precisely where any useful genuinely new estimate would have to act: the joint coefficients of these two linked factors, rather than their individual coefficient norms or the scalar determinant.
Controlling only tau_q, only the least integer denominator k, or only the product of eigenvalues does not pay A_W.
No such joint arithmetic bound has been obtained in this round.

<a id="classical-boundary-scope-and-stopping-point"></a>
## 5. Existing controls, retained costs and the bounded outcome

The actual [C143 construction](../claims/Yin_C_G0143_v1.md#statement) consists of monic irreducible reciprocal nontorsion integer inputs whose N=2d projection coherence has square-root degree growth.
All their autocorrelation Grams satisfy the finite formula (1) and their predictors satisfy L363's strict exterior-zero theorem.
Thus positive definiteness, stability and this exact two-boundary formula cannot by themselves imply a universal dimension-free kappa bound even on the original algebraic domain.
C143 also already records the analogous failure of rank-two shift structure alone.
Those controls have growing positive measure, so they are not counterexamples to a separately proved sufficiently-small-total-measure joint estimate.

Conversely [C160](../claims/Yin_C_G0160_v1.md#statement) already supplies bounded actual kappa and cubic Wiener mass on a fixed positive-measure Salem family of growing degree.
Neither the new predictor formulas nor C92 should be misread as proving Wiener divergence on every bounded-measure family.
The small-total-measure limit is essential to (12)'s divergence conclusion.

The useful new retained interface is the complete finite boundary normalization (1)--(6), the exact normalized product representation (7)--(10), and the identification of the separated-budget failure through the already accepted C92 theorem.
The least predictor denominator is the actual old cokernel element order, but it cancels from the normalized symbol through the integer energy E.
No extra integer norm income, cheap moving-test transfer, new automatic coverage, new source theorem or Task completion follows.
The next discriminating estimate would have to bound the JOINT signed Fourier convolution in (9) on an explicitly justified input class and with its original window costs.
Merely renaming that unknown sum as a boundary cancellation budget is not such an estimate.

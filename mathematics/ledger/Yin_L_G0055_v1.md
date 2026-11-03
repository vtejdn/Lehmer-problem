---
author: Yin
---

# G0001: the exact geometric limit of the two-prime coefficient space

Current complete proof: [C226](../claims/Yin_C_G0226_v1.md#joint-prime-exterior-cost), adopted at its actual current decision.
The original dated mathematical argument remains below as a fixed historical input; it supplies no Task resumption.

Date: 2026-10-07.
Bounded calculation by assigned AI review_matrix_completion for Yin, with the coordinating AI's contributions and the exact computations identified below.
This examines the original companion-lattice proposal in [L G0054](Yin_L_G0054_v1.md#joint-frobenius-minor-test).
No Perron, bounded-degree or fixed-shortness restriction is added to its linear-algebra statements.
No new external source is used.

The full coefficient space, rather than just its displayed generators, has a computable exact ceiling for the proposed certificate.
On the retained Lehmer input that ceiling is below one after discriminant and window normalization.
Consequently the proposed uniform positive certificate fails even after arbitrary mixing, scaling or replacement of auxiliary columns within that space.
The original orbit Gram certificate remains positive on the same input.
This closes a specific finite-window mechanism; it neither gives a counterexample to Lehmer nor rules out a different arithmetic estimate on the original Gram determinant.

<a id="joint-prime-exterior-cost"></a>
## Coefficient rank and the optimal exterior cost

Use exactly the setup of L G0054.
Let p be monic irreducible reciprocal noncyclotomic in Z[t], of degree d>=2 and constant coefficient one.
Let A be its original companion matrix, N=4d, and V=V_N the d by N matrix with columns t^j mod p for 0<=j<N in the power basis.
Set

    F_ell=p(A^ell),       F=[F_2 F_3],
    E=[E_2 E_3],         VE=F,
    W=VV^T,              G_N=det W,
    J=det(FF^T),         T=E^T E.

The j-th column of E_ell is the coefficient vector of t^j p(t^ell), 0<=j<d, padded to length N.
The retained Frobenius argument makes F_2 and F_3 nonsingular.
The first d columns of V are the identity, so W is positive definite.
None of the arguments below requires the additional small-measure or power-degree hypotheses of the proposed uniform test.

The 2d by 2d submatrix of E on rows 2d,...,4d-1 is block upper triangular.
Its E_2 block on rows 2d,...,3d-1 and its E_3 block on rows 3d,...,4d-1 are triangular with diagonal one, and E_2 vanishes on the last d rows.
Thus this maximal minor has determinant one.
In particular E has rank 2d and det T is a positive integer at least one.

Write the eigenvalues of T as lambda_1>=...>=lambda_(2d)>0, and put

    C=C_d(E)=e_d(T)
      =sum_(|I|=|K|=d) det(E[I,K])^2,
    K=K_d(E)=product_(i=1)^d lambda_i,
    B_d=binom(2d,d).

The notation K_d denotes a scalar exterior operator cost, not the polynomial relation matrix of L G0004.
The singular values of the d-th exterior power of E are precisely the square roots of the d-fold eigenvalue products.
Consequently

    K=||exterior^d E||_op^2,
    K<=C<=B_d K,
    K>=sqrt(det T)>=1,
    C>=B_d sqrt(det T)>=B_d.                            (1)

For the third inequality compare the product of the largest d eigenvalues to that of the smallest d.
For the fourth, each eigenvalue occurs in binom(2d-1,d-1) of the B_d products, so their geometric mean is sqrt(det T); apply the arithmetic-geometric mean inequality.
These estimates keep all mixed minors.

The d-th exterior power of a d-row full-rank matrix V has squared operator norm det(VV^T).
Applying operator submultiplicativity to VE gives the sharper comparison

    J<=G_N K<=G_N C.                                   (2)

K is the least constant depending only on E for which the first inequality holds for every real full-rank d by N matrix V: choose orthonormal rows of V along the d leading left singular vectors of E.
This characterization does not assert that the original companion V has that row space.

In the entropy certificate with N=4d, replacing C by K improves the lower estimate by exactly log(C/K)/[2(4d-1)].
Its possible size obeys

    0<=log(C/K)/[2(4d-1)]
       <=log B_d/[2(4d-1)] -> (log 2)/4.                (3)

This is a bound on the difference between two sufficient estimates, not a new lower bound on entropy.

<a id="coefficient-subspace-optimum"></a>
## Exact optimization over every column choice in the fixed space

Let S=col(E), a 2d-dimensional subspace of R^N.
Its orthogonal projection and the compressed orbit Gram matrix are

    P_S=E T^(-1) E^T,
    T_S=V P_S V^T=F T^(-1) F^T,
    H=det T_S>0.                                       (4)

Positivity follows because F has row rank d.
We claim that H is the exact maximum of both normalized certificates when all auxiliary columns are required to lie in S, with their number and images otherwise unrestricted.

Precisely, let L be any real N by m matrix, m>=d, all of whose columns lie in S, such that VL has row rank d.
Define

    J_L=det(VL L^T V^T),
    C_d(L)=sum_(|I|=|K|=d) det(L[I,K])^2,
    K_d(L)=product of the d largest squared singular values of L.

Then

    J_L<=H K_d(L)<=H C_d(L).                            (5)

To prove this, choose an N by 2d matrix U whose columns are an orthonormal basis of S, and write L=U R and B=VU.
We have BB^T=T_S.
Isometric multiplication by U leaves singular values and the minor-square sum unchanged.
Therefore

    ||exterior^d(VL)||_op^2
       <=||exterior^d B||_op^2 ||exterior^d R||_op^2
       =H K_d(L),

which is (5).
This proof allows any finite number m of columns, arbitrary dependencies among them and arbitrary real weights.

Both bounds are attained by the same d-column matrix

    L_*=P_S V^T.

Indeed VL_*=T_S and L_*^T L_*=T_S.
Thus

    J_(L_*)=H^2,       C_d(L_*)=K_d(L_*)=H.

Consequently

    max_(cols(L) in S, rank(VL)=d) J_L/C_d(L)
      =max_(cols(L) in S, rank(VL)=d) J_L/K_d(L)=H.      (6)

The maximum is unchanged if one restricts to rational L, since E and V are integral and L_*=E T^(-1) F^T is rational.
It is also unchanged if one restricts to integral linear combinations of the original columns of E, without fixing the image VL.
A common positive integer multiple of T^(-1) F^T is integral.
Multiplying L_* by this integer multiplies J_L, C_d(L) and K_d(L) by the same factor to the power 2d, so their ratios remain H.
Thus integrality alone does not improve the unrestricted-image ceiling in (6).

For comparison, if the original image F is fixed, its rational lift of minimum cost inside S is

    L_0=P_S V^T T_S^(-1) F,
    VL_0=F,
    C_d(L_0)=K_d(L_0)=J/H.                              (7)

To verify the cost, L_0 has rank d and L_0^T L_0=F^T T_S^(-1) F.
The product of its nonzero eigenvalues is det(T_S^(-1/2)FF^T T_S^(-1/2))=J/H.
Inequality (5) shows that no smaller cost is possible.
This rational minimizer need not be integral at the fixed image F; clearing denominators changes that image.
No claim of uniqueness for the operator-cost minimizer is needed here.
The general fixed-image minimum over the entire ambient coefficient space, and its integral equality condition, are the distinct results of the [projection calculation](Yin_L_G0056_v1.md#unique-minimum-lift).

Applying (5) to the original E, and using (1), gives

    J/C<=J/K<=H<=G_N.                                   (8)

The last inequality also has an exact geometric explanation.
Put Q=V^T W^(-1/2), so Q^T Q=I_d.
Then

    H/G_N=det(Q^T P_S Q),       0<H/G_N<=1.              (9)

The symmetric matrix Q^T P_S Q is positive definite and at most I_d.
Its eigenvalues measure how much of each orthonormal row direction of V survives projection into S; their product is the displayed loss.
No dimension-independent lower bound for this product is proved.

<a id="original-gram-certificate-boundary"></a>
## What the optimum means for the original entropy bound

The retained inequality in [L G0004](Yin_L_G0004_v1.md#gram-lower-certificate) is

    m(p)>=[log(Delta G_N)-d log N]/[2(N-1)],
    Delta=|disc p|.

Substituting any normalized column certificate J_L/C_d(L) or J_L/K_d(L), with its columns in S, gives a lower estimate no larger than

    [log(Delta H)-d log N]/[2(N-1)]
      =[log(Delta G_N)-d log N]/[2(N-1)]
          +log(H/G_N)/[2(N-1)].                         (10)

Thus optimization inside the entire two-prime coefficient space still retains the nonpositive projection term (9).
The value H is invariant under any invertible change of the 2d displayed coefficient columns, with the corresponding change of F.
In particular scaling the separate prime blocks cannot create an additional gain after this exact optimization.

Optimizing rational lifts in the full ambient space instead yields the original G_N, as proved in the separate projection calculation.
This is recovery of the known Gram certificate, not a new entropy mechanism.
A new arithmetic argument may still prove that this original Gram determinant has sufficient uniform surplus.
Nothing here rules that out, and no assertion is made about all collections of primes, all time windows, or all arithmetic entropy methods.

<a id="lehmer-joint-prime-control"></a>
## An exact target-domain input defeats the entire fixed-space test

Take the retained standard Lehmer polynomial

    p_L=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1,
    d=10,       N=40.

Its irreducible Salem classification is a reused control premise, including its explicit identification in [L G0036](Yin_L_G0036_v1.md#excess-two-salem-classification); it is not inferred from numerical roots in this computation.
The exact endpoint values are

    p_L(1)=-1,
    p_L(13/10)=68226578579/10000000000>0.

Since a Salem polynomial has exactly one positive expanding root, these signs put 1<M(p_L)<13/10.
The one-expanding-conjugate fiber argument in [L G0016](Yin_L_G0016_v1.md#expanding-prime-count) also gives degree preservation under every positive power, hence under every prime exponent.
Explicitly, a conjugate above alpha^n has modulus alpha>1 and must be the unique expanding conjugate alpha; this embedding fiber has size one, and all fibers have the common field index [Q(alpha):Q(alpha^n)], so that index is one.
This control is therefore inside the exact domain of L G0054's proposed uniform certificate.

The two independently implemented exact computations retained for [J G0008](../computations/programs/Yin_J_G0008/readme.md) give

    Delta=1332031009,
    J=1142106771578809,
    C=32705007016634,
    G_40=18006972477,
    det T=515004740860,
    det F_2=1024=2^10,       det F_3=59049=3^10.

In particular the raw minor-square certificate is

    R_C=Delta J/(40^10 C)
       =1521321635331853475288281
          /342936854374740131840000000000 <1.            (11)

Even replacing C by the optimal exterior cost K for the same E fails positivity.
There is no eigenvalue approximation in this check: (1) gives Delta J/(40^10 K)<=binom(20,10) R_C, and the exact integer comparison is

    Delta J binom(20,10)=281073300057371920680361644436
       <342936854374740131840000000000=40^10 C.          (12)

More strongly, exact rational evaluation of (4) gives

    H=75593455205376240/25750237043,
    Delta H/40^10
      =1258660330137670189897827
         /3375135069700096000000000 <1.                 (13)

By (6), every choice of auxiliary columns confined to this full two-prime coefficient space fails even positivity of the normalized finite certificate, for either the full minor-square cost or the exterior operator cost.
This includes arbitrary mixing, scaling, choosing different numbers of columns, and arbitrary integral combinations; it is not just a failure of the original generating matrix or of an estimate on its singular values.

On exactly the same input the original Gram certificate satisfies

    Delta G_40/40^10
       =23985845717573539293/10485760000000000 >1.        (14)

The projected two-prime span therefore omits directions that matter to this finite certificate.
Equations (11)--(13) refute the proposed universal positive target of L G0054, even with the specified within-space optimizations.
They do not refute the true inequalities (2), (5) or (10), and do not supply an upper bound contradicting positive algebraic entropy.

<a id="joint-prime-geometry-review"></a>
## Retained review and native-evidence ownership

The original full author/collaborator checks are retained in [R513](../audits/reviews/Yin_R_G0513_v1.md#historical-geometry-author-finding), with the coordinator's actual subspace-optimum and L_* contributions disclosed.
The original separate whole-proof check is retained in [its exact R513 finding](../audits/reviews/Yin_R_G0513_v1.md#historical-geometry-whole-finding), including its decisive-payload inspection and unknown initial arrangement.
Both retain the original2026-10-07 date and scope.
[J8](../computations/programs/Yin_J_G0008/readme.md) owns the original programs, executions, full outputs,29 comparisons and failed determinant-only screen; this organization runs no new computation.

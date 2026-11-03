---
author: Yin
---

# Phase-sensitive collars and linear-degree energy windows

Date: 2026-10-08.
Joint bounded G0001 derivation by the assigned entropy_status AI and the coordinating AI for Yin.
The coordinating AI requested retaining the actual central phases in L G0144's projected Gramian rather than its coarse 32q/m loss.
The assigned AI derived the finite rank-two formula, the phase-distance bound and the two-scale projection estimate below.
The coordinator then derived the Hankel sampling bound, the Fejer central Gramian estimate and the linear-degree actual-family construction.
The assigned AI checked and assembled that full contribution, using a slightly coarser elementary square-sum estimate with the same final constants.
Both are contributors; complete independent review is recorded below.
No numerical mathematical run, root approximation, optimization or new external source is a premise.
The coordinator accepted this reviewed proof for fixed-ledger preservation on 2026-10-08.

Use the exact Salem domain, matrices and finite collar conventions of [L G0144](Yin_L_G0144_v1.md#full-collar-projected-gramian).
Thus 0<m<=1, alpha=exp(m), r=exp(-m), q=d-2>=2, and beta_1,...,beta_q are the distinct central roots.
They occur in conjugate pairs and none is real: a real central root would be 1 or -1, contrary to the positive Mahler irreducible input.
Put

    D_C=max_i sum_(k!=i) 2/|beta_i-beta_k|.

Every statement below retains this actual separation cost.
In particular the result is not a separation-free or degree-uniform observability claim.

<a id="phase-resolved-projected-gramian"></a>
## 1. The exact finite rank-two loss

For an integer L>=2 retain the L by q central matrix U_(t,i)=beta_i^t and the two-column hyperbolic matrix

    H_(t,1)=r^t,     H_(t,2)=r^(L-1-t),       0<=t<L.

Write G_L=U^*U, g_L=lambda_min(G_L),

    S_L=(1-r^(2L))/(1-r^2),       T_L=L r^(L-1),
    C_L=U^*[I-H(H^*H)^(-1)H^*]U,  eta_L=lambda_min(C_L).

As in L G0144, S_L>T_L>0 and eta_L>=0.
Define the actual finite geometric sums and two scalar phase aggregates

    a_i(L)=(1-(r beta_i)^L)/(1-r beta_i),
    A_L=sum_i |a_i(L)|^2,
    B_L=sum_i beta_i^(-(L-1)) a_i(L)^2.                  (1)

Conjugate pairing makes B_L real.
The two rows of H^*U have entries a_i(L) and beta_i^(L-1) overline(a_i(L)), respectively.
Therefore

    (H^*U)(H^*U)^*=[[A_L,B_L],[B_L,A_L]],
    H^*H=[[S_L,T_L],[T_L,S_L]].

These two real symmetric matrices are simultaneously diagonalized by the symmetric and antisymmetric two-coordinate vectors.
The nonzero eigenvalues of U^*H(H^*H)^(-1)H^*U are those of the corresponding two by two normalized Gramian.
Its operator norm is exactly

    mu_L=max{(A_L+B_L)/(S_L+T_L),
             (A_L-B_L)/(S_L-T_L)}.                     (2)

Here A_L+B_L and A_L-B_L are nonnegative.
Zero eigenvalues do not affect (2).
Weyl's elementary quadratic-form estimate gives

    eta_L>=g_L-mu_L>=L-D_C-mu_L.                        (3)

Formula (2) retains all finite phases and the cancellation between the nearly parallel hyperbolic columns when mL is small.
It can be used with exact algebraic arithmetic for a supplied P,L, or with certified rational enclosures.
No such computation is executed here.
It is a two-scalar loss calculation in addition to the central Gramian, not a claim that an unknown full Gramian has already been optimized.

## 2. A phase-distance bound already paid for by D_C

Choose beta_0 minimizing |1-beta_i| among the central roots.
For i!=0, the triangle inequality and this minimality imply

    |beta_i-beta_0|<=2|1-beta_i|.

The conjugate overline(beta_0) is another distinct central root and |beta_0-overline(beta_0)|<=2|1-beta_0|.
The other-root sum and the omitted root can thus each be charged to the D_C row at beta_0:

    sum_i 1/|1-beta_i|<=2D_C.                            (4)

In particular the center cannot approach the point 1 without a corresponding separation charge: its conjugate supplies another root.
The proof uses actual conjugate symmetry and would not hold for an arbitrary one-sided list of unit phases.

For later use put

    A_infinity=sum_i |1-r beta_i|^(-2).

The identity |1-r beta|^2=(1-r)^2+r|1-beta|^2 and arithmetic-geometric mean give

    m/|1-r beta|^2
       <=m/[2(1-r)sqrt(r)] * 1/|1-beta|
       <=exp(m)/2 * 1/|1-beta|.

The last step follows from 2(1-r)sqrt(r)=4exp(-m)sinh(m/2) and sinh(m/2)>=m/2.
Consequently

    m A_infinity<=exp(m) D_C.                           (5)

This improves the q/m^2 resolvent bound by retaining the same phase geometry already present in the central Gramian.
No assumption on P(1) or on independent phases is required.

## 3. Large mL: retaining the resolvent mass

Suppose mL>=4.
The inequalities e<3 and e^4>50 imply

    S_L>(1-1/2500)/(2m),
    T_L<12/(50m),
    S_L-T_L>1/(4m).                                    (6)

Indeed 1-r^2<=2m, r^(2L)<=e^(-8)<1/2500, and T_L=exp(m)(mL)exp(-mL)/m.
The function t exp(-t) decreases for t>=4.
For completeness e>8/3 follows from the first five terms of its series, and (8/3)^4=4096/81>50.
No decimal estimate is needed.

The trace bound for the normalized two-column Gramian, or direct Cauchy--Schwarz, gives

    mu_L<=2 A_L/(S_L-T_L)
         <8m(1+r^L)^2 A_infinity
         <9m A_infinity<=9exp(m)D_C<27D_C.              (7)

The finite geometric numerator in (1) is bounded by 1+r^L, and 8(51/50)^2<9.
Thus the same-window estimate can keep the actual 9m A_infinity term when that is smaller.
In particular (3) gives eta_L>=L-28D_C in this scale.
This estimate already removes q/m from the loss, but the next section also removes the mL>=4 guard.

## 4. Small mL: normalize the symmetric and antisymmetric columns first

Suppose mL<=4 and put ell=L-1.
The two real sequences

    f_+(t)=r^t+r^(ell-t),
    f_-(t)=r^t-r^(ell-t),           0<=t<=ell

are nonzero and orthogonal by reflection t -> ell-t.
Their normalized versions h_+,h_- form an orthonormal basis of range H.
Let M denote the largest absolute entry of either one normalized sequence, as needed.
Both unnormalized sequences attain their largest absolute value at the endpoints.

Put a=m ell/2, so 0<a<2.
At every integer 0<=t<=ell/4, the absolute value relative to its endpoint maximum is at least

    cosh(a/2)/cosh(a)>1/[2cosh(a/2)]>1/4     for f_+,
    sinh(a/2)/sinh(a)=1/[2cosh(a/2)]>1/4     for f_-.

Here cosh(1)<2 follows from e<3 and e^(-1)<1.
Reflection gives the same bound in the last quarter.
Each end quarter contains floor((L-1)/4)+1=ceil(L/4) points.
They are disjoint for L>=2 and together contain at least L/2 points.
After normalization this proves

    M^2<=32/L.                                          (8)

The symmetric sequence is positive, decreases towards its middle and then increases.
The antisymmetric sequence decreases monotonically from its positive maximum to its negative minimum.
For either normalized sequence h, its total variation is therefore at most 2M.
Finite summation by parts yields, for every beta!=1 on the unit circle,

    |sum_(t=0)^(L-1) h(t) beta^t|<=4M/|1-beta|.

Cauchy--Schwarz independently bounds that sum by sqrt(L).
Combining the two bounds and (8) gives

    |sum_t h(t) beta^t|^2
       <=min{L,512/[L|1-beta|^2]}
       <=16sqrt(2)/|1-beta|.                            (9)

The projection-loss operator is positive semidefinite.
Its norm is at most its trace, which is the sum of these squared correlations for the two orthonormal columns and all central roots.
Equations (4), (9) therefore give

    mu_L<=64sqrt(2) D_C<91D_C.                           (10)

The last rational comparison follows by squaring: 8192<8281.
This proof cancels the near-parallel-column degeneracy before applying absolute-value bounds.
It does not estimate an antisymmetric norm by the smallest hyperbolic eigenvalue while dropping its numerator.

<a id="uniform-phase-observability-loss"></a>
## 5. A uniform same-window bound and finite cube exclusion

Combining the two scales proves, at the same integer L and with no additional inverse-m guard,

    eta_L>=L-92D_C,          L>=2, 0<m<=1.               (11)

Negative right sides remain valid; no positive definiteness for short windows is being asserted.
For a supplied L one may retain the maximum of all available lower bounds: zero, g_L-mu_L from (2)--(3), L-92D_C, the large-scale L-D_C-9m A_infinity when mL>=4, and the earlier L G0144 bound L-D_C-32q/m when its L>=8/m guard holds.
A nonnegative certified lower bound for eta_L from any of these is interchangeable in the actual endpoint test; all are bounds for the same matrix and window.

The finite cube application uses exactly L G0144's indices.
A nonzero P-divisible defect cluster [a,b] has two disjoint raw zero-defect collars of length L inside [-R,R].
Its nonzero integer response w has support [a+d,b].
The homogeneous v=x-w is defined on [a-L,b+L+d], and equals x on both raw collars.
When eta_L>0, those collars share B and give the same central coefficient bound and scalar hyperbolic interpolation as in that fixed proof:

    |v_j|<=sqrt(B/L)+sqrt(2qB/eta_L),       a<=j<=b.      (12)

Thus any certified eta_lower>0 with the right side, using eta_lower, strictly below 1/2 excludes the integer-response branch at that actual L.
This is a sufficient same-window certificate, not an assertion that it has been evaluated on an input.

In particular define the integer length

    L_phase(P,B)=1+ceil[92D_C+32qB+16B].                 (13)

Since |beta_i-beta_k|<=2, D_C>=q-1.
Consequently (13) is at least d and at least 2.
For every L>=L_phase, (11) gives eta_L>32qB and L>16B.
Both terms in (12) are strictly below 1/4, contradicting the cube at a nonzero integer coordinate of w.
This is the same strict finite contradiction as L G0144; no infinite x extension or uncharged observation coordinate is introduced.

One may safely take the minimum with the old L_obs endpoint length.
The new length need not be smaller on every input.
Before ceilings, its cost improves the old coarse expression whenever

    91D_C<32q/m.                                        (14)

Under this strict comparison the new integer length is no greater; ceilings can hide a strict reduction.
The existing explicit degree,m upper bound for D_C in L G0144 remains available.
The exact phase/root cost has not become a new unspecified fixed-input constant.

## 6. What changes in the early-window cost test

At lambda=2m/q, formula (13) has the explicit upper cost

    lambda L_phase
      <=184mD_C/q+64mB+32mB/q+4m/q.                     (15)

Hence if the displayed right side is below one, this endpoint length passes the scaled-length inequality that the old explicit choice could never pass: the old choice had lambda L_obs>64.
More generally, keeping the actual integer-defect budget K=floor(||P||_1^2 B), a sufficient condition for lambda K L_phase<1 is that K times the right side of (15) is below one.
This displays every coefficient, degree, B and m factor relevant to that ENDPOINT contribution.

These are conditional inequalities for actual input data.
No Salem family satisfying them, no lower bound for eta_L sharp enough for a specified product window, and no near-one coverage is asserted.
The full Fourier test still contains the norm/flux term and the actual finite-window cutoff.
Passing (15) for the endpoint alone does not make the complete collar or the balanced radius pass its criterion.

For direct use with fixed records, replace only L_obs by min(L_obs,L_phase) in the safe L G0144 maximum/minimum collar construction; all other flux constants and integer guards stay in place.
The new local exclusion holds for every nonzero P-divisible cluster, so the every-cluster quantifier required by L G0143 is preserved.
An additional minimum with any supplied exact same-window certificate must retain that certificate's actual length and positive-definiteness guards.

The bounded parameter question has a positive answer: the inverse-m loss and its observation-length guard were artifacts of discarding the actual central phases and the symmetric/antisymmetric cancellation.
The replacement still pays a constant multiple of D_C, with the finite rank-two alternative available at any supplied L.
Whether those actual costs and the separate flux costs fit a useful same-input product window remains unresolved; no numerical run, uniform gap, or G0001 resolution is claimed.

<a id="plastic-family-uniform-flux"></a>
## 7. Uniform flux cost on the adopted plastic family

There is also an actual varying-input consequence, rather than only the conditional endpoint regime above.
Use exactly the irreducible family of [L G0131](Yin_L_G0131_v1.md#linear-exponent-cyclic-coverage) and the phase-separation proof of [L G0144](Yin_L_G0144_v1.md#plastic-family-endpoint-cost):

    P_N=t^N(t^3-t-1)+(1-t^2-t^3),
    N=9 mod120, N>=129, d=N+3>=132, q=d-2>=130,
    W=||P_N||_1=6,   1/5<m<log(4/3)<1,
    delta=2pi/(d+18).                                   (16)

Here delta is a lower bound for the circular angular separation of consecutive central roots, not their chord distance.
The lower bound on m follows from the retained exterior-root bound alpha>theta>5/4 and log(5/4)>1/5.
For cyclic rank distance k<=floor(q/2), the fixed phase argument gives |beta_i-beta_j|>=4k/(d+18), including the wrap.

First consider any n-term polynomial f(theta)=sum_(k=0)^(n-1)c_k exp(ik theta) and any delta-separated collection of circle nodes.
Center disjoint length-delta circular arcs at those nodes.
For g=|f|^2 and each such arc I with center theta_i,

    g(theta_i)<=delta^(-1) integral_I g+integral_I |g'|.

Summing, applying Parseval and Cauchy--Schwarz, and using ||f'||_2<=(n-1)||f||_2 proves the sampling bound

    ||E_n||_op^2<=2pi/delta+4pi(n-1),
    (E_n)_(i,k)=beta_i^k.                                (17)

The norms in the proof are unnormalized L2 norms on a full period, so Parseval contributes exactly 2pi.
This bound does not charge each arc's variation more than once.

Write H_P for the d by d Hankel matrix with entries p_(j+k+1), extended by zero when j+k+1>d.
The exact boundary-row identity in L G0141 gives B_c=E_d H_P.
Reversing the columns of H_P changes it into a triangular convolution compression with coefficients p_d,p_(d-1)...,p_1.
Young's inequality therefore gives ||H_P||_op<=sum_(i=1)^d|p_i|=W-1=5.
Consequently the actual fixed flux constant obeys

    Phi<=||B_c||_op^2/q
         <=25[d+18+4pi(d-1)]/q
         <25(14d+18)/(d-2)<360.                         (18)

For the last step use 4pi<13 and d>=132: the preceding rational expression is 350+1150/(d-2)<360.
Thus this family has a uniform flux constant, improving the earlier O(d) coefficient-only bound.
This is an exact norm bound, not a computed value of Phi.

## 8. A linear-degree physical endpoint collar on the same inputs

For an odd window 2T+1, center the central Gramian at indices -T,...,T.
Use nonnegative Fejer weights 1-|t|/(T+1), which are at most one.
The weighted Gramian has diagonal T+1.
Its off-diagonal entry is

    (1/(T+1)) |sum_(j=0)^T (overline(beta_i)beta_k)^j|^2,

and hence at most 4/[(T+1)|beta_i-beta_k|^2].
For each cyclic rank there are at most two roots.
The chord bound following (16), together with sum_(k>=1)1/k^2<=2, gives a row sum at most (d+18)^2/(T+1).
Gershgorin therefore supplies the lower bound (T+1)-(d+18)^2/(T+1).
The weighted matrix is no larger than the raw Gramian in positive-semidefinite order.

For any L use its largest odd subwindow; its T+1 is at least L/2.
Unitary diagonal phase shifts preserve all eigenvalues.
Thus

    g_L>=L/2-2(d+18)^2/L,
    g_L>=L/3 whenever L>=4(d+18).                       (19)

The first inequality is allowed to be negative for small windows.
For the second, L>=4(d+18) in fact gives the stronger 3L/8 lower bound.
The elementary square-sum estimate suffices, so no exact zeta value is needed.

For this family the already fixed L G0144 Schur subtraction bound can be used directly: when L>=8/m its operator norm is at most 32q/m<160q.
If L>=1920d, all those guards hold, and (19) yields

    eta_L>=g_L-160q>=L/4.                               (20)

Indeed 4(d+18)<=1920d, m>1/5 ensures 8/m<40, and 160q<=L/12.
The proof of this actual-family assertion does not require the new general constant 92 in (11).

Fix any rational B>0 and define the physical endpoint length

    L_end=1+ceil[d max(1920,128B)+16B]
          <=d(1922+144B).                               (21)

For every L>=L_end, one has L>16B and L>128qB.
Substituting (20) in the finite endpoint estimate (12) makes its two terms strictly less than 1/4.
Thus every nonzero P-divisible cluster is excluded when its two actual zero-defect collars have this length.
This endpoint length is O_B(d), not O_B(d log d).

<a id="linear-degree-energy-coercivity"></a>
## 9. An actual O_B(d) coercivity radius, and its matching order control

Keep B fixed and K=floor(36B).
If K=0 the original integer budget already makes E_R>B for every R.
Suppose K>=1.
Use the exact L G0141 flux/norm term, specialized to h=2,

    A_*(ell)=min(K,3(ell+1)),
    J(ell)=2B Phi A_*(ell)^(4/q) exp(2m ell/q),
    L(ell)=max{d[1+ceil J(ell)],L_end}.                  (22)

This is a positive integer nondecreasing collar function.
Its first branch forces P|Z_c by the fixed flux/norm argument.
Its second branch excludes the resulting nonzero integer response by Section 8.
Both proofs apply to every nonempty consecutive actual defect cluster; the finite indices and global B,K budgets are unchanged.

Since q>=130, K^(4/q)<=K.
Also 2m/q<=4/d for d>=4 and m<=1.
Equations (18), (21) therefore give

    L(ell)<=d C_B exp(4ell/d),
    C_B=max{2+720BK,1922+144B}.                         (23)

Now apply precisely the balanced radius of [L G0143](Yin_L_G0143_v1.md#every-cluster-balanced-radius).
Define real finite comparison constants depending only on B by

    f_1=0,
    f_n=(n-1)C_B exp(4 f_floor(n/2)),       2<=n<=K,
    A_B=K C_B exp(4 f_K).                               (24)

For the actual integer balanced recursion F(1)=0, F(n)=(n-1)L(F(floor(n/2))), induction using (23) proves F(n)<=d f_n.
Hence the actual integer sufficient radius satisfies

    R_bal=K L(F(K))<=d A_B,
    E_R(P_N)>B for every integer R>=R_bal.               (25)

The constants may be very large as B grows, but they are finite, explicit and independent of N and d.
Their nested dependence retains the 1+floor(log_2 K) balanced depth.
This is a genuine varying-input linear-degree energy-window theorem on the stated infinite family.
No E_R optimization or value of its minimum has been computed.

Let R_first(P_N,B) be the least nonnegative integer R with E_R(P_N)>B.
It exists by (25).
The actual closed-cube witness in [L G0137](Yin_L_G0137_v1.md#actual-salem-bounded-energy-window) gives E_R(P_N)<=3/2 for 0<=R<=d-7.
Therefore, for every fixed rational B>=3/2,

    d-6<=R_first(P_N,B)<=R_bal<=d A_B.                  (26)

In particular the first threshold radius is Theta_B(d) on these actual unbounded-degree inputs, including the equality case B=3/2 because the threshold is strict.
This matches the order of the earlier plateau without asserting its endpoint is optimal or determining its constant.

The family has logarithmic measures bounded away from zero and tending to the plastic-number measure.
No claim about the 16m transition target, a sufficiently near-one subfamily, a product-window lower bound or the unrestricted G0001 contract follows from (25)--(26).
The separate general phase-sensitive estimates (1)--(15) remain available with their actual D_C costs; this actual-family theorem does not erase that restriction.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0048_v1.md#contributions-and-review-status), with its original inspected scope and relationship.

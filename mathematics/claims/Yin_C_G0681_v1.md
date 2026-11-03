---
author: Yin
---

# Actual weighted phase bands and a degree two-thirds contact criterion

Human author Yin.
Root derived the new weighted Mobius coefficient, moving local witness and modulation candidate, and proposed the full-band count and critical strip.
Phase_bands independently checked every coefficient, sign, neighborhood, derivative, kernel tail and full returned cost, and supplied explicit thresholds and two-sided degree-logarithm constants.
Both are contributors, not independent reviewers.
The actual weighted family and complete finite return are the adopted C678v1 inputs, not a conditional unconstructed family.
No native computation, external source acquisition or new original-source proof audit is used.

## Statement

Use the actual composite integer K and the complete weighted family, indexed by integers j>=4K:

    K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))),
    a_j=min{p prime:p>(j+1)K}, L_j=K+a_j+2,
    c_j=min{p prime:p>(L_j+1)^2}, M_j=floor(a_j/4),
    d_j=K+a_j+c_j=c_j+L_j-2, j>=4K.

For e=(K,a_j,c_j), weights w=(1,1,2), and all three factors, set

    Qraw_j(x)=(x^2-1)product_(i=1)^3(x^e_i-1)
       -(x/2)sum_(i=1)^3 w_i(x^e_i+1)product_(l!=i)(x^e_l-1),
    P_j(x)=Qraw_j(x)/(x-1)^2.                              (WP1)

C678 proves that these are the actual monic integral irreducible Salem minimal polynomials, with even degree d_j, trace0, exact cyclotomic removal and

    log2<m(P_j)<log4, 16M_j^2<d_j<2^10 M_j^2.

All source hypotheses and their retained inspection depths remain those of that adopted weighted construction.
Use ALL d=d_j relation columns in the ORIGINAL2d window:

    A_rel=[P_j,xP_j,...,x^(d-1)P_j], G=A_rel^T A_rel,
    Pi=A_rel G^-1 A_rel^T, v_n(z)=(1,z,...,z^(n-1))^T,
    h_orig=v_(2d)^*Pi v_(2d)/(2d),
    f_(j,tau)=(1-h_orig/tau)_+.

All Haar measures have mass1, Fourier coefficients use negative exponentials and angular coordinates use radians.
Write W_*(f)=sum_(n!=0)abs(fhat(n)).
For fixed j,tau>0 this is finite; for0<tau<=1 the value at each actual unit-circle root of P_j is1 and exceeds the Haar mean by at least1/2.

For z,u,w in T, the ACTUAL weighted torus phase and cap are

    R(z,u)=(z^K-1)(u-1), S(z,u)=2(z^K u-1),
    Acal=-(z^2-1)R-zR+zS/2,
    Bcal= (z^2-1)R-zR-zS/2,
    g_0=abs(Acal)^2+abs(Bcal)^2,
    U=Acal/Bcal off their common zeros, U=0 at common zeros,
    V(z,u)=U(z^-1,u^-1), g=g_0(z^-1,u^-1),
    h=(1+Re(wV))/2, F_tau=(1-h/tau)_+,
    iota_j(z)=(z,z^a_j,z^c_j),
    H_j(gamma)=gamma_0+a_j gamma_1+c_j gamma_2.             (WP2)

Every translated original law is the pushforward through z to t*iota_j(z), for every t in T^3.
Those laws remain correlated.

### Exact coefficients and actual finite local bands

For integers k,m>=1 define

    F_(k,m)(z)=integral_T U(z,u)^k u^m dnu_1(u).

For z=exp(it) away from the finite poles, put

    b(t)=4sin t+cot(Kt/2),
    alpha=(1-ib)/(3-ib), lambda=(1+ib)/(3-ib),
    P_(k,m)(x)=sum_(l=1)^min(k,m) binom(k,l)binom(m-1,l-1)x^l.

The exact actual coefficient is

    F_(k,m)(exp(it))=lambda^k alpha^m
                                  P_(k,m)(-8/(1+b(t)^2)). (WP3)

Let q=sqrt(km), N=k+m, and let t_(k,m) be the unique point in(0,1/(8K)) such that b(t_(k,m))=32q.
Set

    delta_(k,m)=1/(10000Kq),
    theta_(k,m)(t)=(k-m)arctan b(t)+N arctan(b(t)/3),
    n_(k,m)=floor(theta_(k,m)'(t_(k,m))+1/2),
    C_band=ceil(320000pi K).

The entire interval abs(t-t_(k,m))<=delta_(k,m) lies in(0,1/(8K)); there24q<=b(t)<=40q and

    F_(k,m)(exp(it))=-A_(k,m)(t)exp(i theta_(k,m)(t)),
    A_(k,m)(t)>=1/(256m),
    abs(n_(k,m))<=25K(k+m).                               (WP4)

For every integer radius R>=C_band sqrt(k)m^(5/6), the ACTUAL two-torus coefficients satisfy

    sum_(abs(p-n_(k,m))<=R) abs((U^k)hat(p,-m))
                                              >=1/(1024m). (WP5)

This is a finite band centered at the actual derivative above, not an assertion that an unmodulated cutoff captures the coefficient.

### Entire selected support and complete original return

Use the following exact C678 constants, with angular derivatives:

    D_l=||partial_l Acal||_infinity+||partial_l Bcal||_infinity, l=1,2,
    G_K=sqrt(||g||_infinity),
    C_w=6pi[1+10(D_1+D_2)+2(G_K+1)],
    C_s=3pi[18*96^(2/3)(D_1+D_2)+4^(2/3)],
    C_2=512C_w+2C_s,
    delta_*=[28(1+60pi)]^-2,
    C_obs=2/delta_*, C_stab=33C_obs+3, E_w=8(3+3pi).

For actual j with M=M_j>=max{2,C_w}, set L_raw=L_j,c=c_j,d=d_j and

    epsilon_j=(4L_raw-3)/(2d)
                   +[1+pi L_raw(5+2log c)]/(2c),
    ell_M=1+log M, rho=(C_w/M)^2,
    B_w(j,tau)=min{1,(C_stab epsilon_j)^(2/3)}
                                          +C_2 M^-1 tau^(-1/6),
    epsilon_j<=E_w ell_M/M.                               (WP6)

This B_w retains the entire five-cost budget of C678: original2d comparison, TWO regularizations and TWO smoothings, with every translated law and rho/tau branch paid.
Its finite return applies to EVERY Gamma in the CLOSED[-M,M]^3 box with cost5 card(Gamma)^(2/3)B_w.

For0<tau<=1/64, let L_tau=floor(1/(4sqrt(tau))).
For every integer J>=1 define

    R=ceil(C_band sqrt(L_tau)J^(5/6)),
    Gamma_(tau,J)={(-p,m,k):1<=k<=L_tau,1<=m<=J,
                                  abs(p-n_(k,m))<=R},
    N_sel=card Gamma_(tau,J)=L_tau J(2R+1)
                 <=3(C_band+1)L_tau^(3/2)J^(11/6).         (WP7)

Whenever the COMPLETE conditions

    L_tau,J<=M, 25K(L_tau+J)+R<=M                          (WP8)

hold, every selected original frequency is distinct and strictly positive, and

    W_*(f_(j,tau))>=3log(J+1)/(65536pi)
                                  -5N_sel^(2/3)B_w(j,tau). (WP9)

Every coefficient in every supplied band is counted.
In particular the full error is at most

    (5/4)[3(C_band+1)]^(2/3)J^(11/9)
       *[(C_stab E_w)^(2/3)M^(-2/3)ell_M^(2/3)tau^(-1/2)
                               +C_2 M^-1 tau^(-2/3)].    (WP10)

### Explicit uniform critical strip and actual degree condition

Define fixed thresholds and the full error constant

    M_band=ceil(max{2^16,C_w,(75K/4)^3,(75K)^(11/8),
                                     [3(C_band+1)/2]^(3/2)}),
    j_band=max{4K,ceil(4M_band/K)},
    C_error=(5/4)[3(C_band+1)]^(2/3)
                              max{(C_stab E_w)^(2/3),C_2}.

For EVERY actual j with M=M_j>=M_band and EVERY real H,tau satisfying

    2<=H<=M^(4/3)/(64ell_M^(4/3)),
    M^(-4/3)ell_M^(4/3)H<=tau<=1/64,                     (WP11)

the choice J=floor(H^(9/44)) satisfies all(WP8) and gives

    W_*(f_(j,tau))>=27log H/(2883584pi)
       -C_error[H^(-1/4)
                  +M^(-1/9)ell_M^(-8/9)H^(-5/12)].       (WP12)

This is uniform over the ENTIRE strip, whose H interval is nonempty at the stated threshold.
Every integer j>=j_band satisfies its actual M_j threshold.

For EVERY actual j in the family, the degree comparison is

    2^(-4/3) M_j^(4/3)/(1+log M_j)^(4/3)
       < d_j^(2/3)/(1+log d_j)^(4/3)
       < 2^(16/3) M_j^(4/3)/(1+log M_j)^(4/3).            (WP13)

Consequently, for EVERY positive shrinking sequence tau_j->0 with

    d_j^(2/3)tau_j/(1+log d_j)^(4/3)->infinity,            (WP14)

one has W_*(f_(j,tau_j))->infinity.
Equivalently M_j^(4/3)tau_j/(1+log M_j)^(4/3) tends to infinity.
No monotonicity or prescribed divergence speed is required, and the entry index into(WP11) may depend on the sequence.
This is a theorem only for the explicit actual weighted family(WP1), retaining log2<m(P_j)<log4 and the full original2d normalization.
It is not a bounded-H endpoint, logarithm-free degree criterion, every-degree theorem, optimality assertion, near-one construction or unrestricted G0001 conclusion.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Complete argument

### 1. Exact weighted Mobius expansion and its coefficient sign

Use the actual Acal,Bcal in(WP2), with u=exp(is).
Their equal-modulus quotient, without replacing the weighting by the old phase, is

    U=(2+i[b(t)+cot(s/2)])/(2-i[b(t)+cot(s/2)]).

Put v=u^-1.
Since cot(s/2)=i(1+v)/(1-v), direct algebra gives

    U=[(1+ib)-(3+ib)v]/[(3-ib)-(1-ib)v]
       =lambda[1-(1-abs(alpha)^2)v/(conjugate(alpha)(1-alpha v))].

Here abs(alpha)^2=abs(lambda)^2=(1+b^2)/(9+b^2)<1 and alpha!=0.
For each finite b the geometric expansion converges absolutely on abs(v)=1.
Expand the kth power by the finite binomial theorem; for1<=l<=min(k,m), the coefficient of v^m in v^l(1-alpha v)^(-l) is binom(m-1,l-1)alpha^(m-l).
Since(1-abs(alpha)^2)/abs(alpha)^2=8/(1+b^2), this gives exactly(WP3).
The single angular pole of cot(s/2) is filled by its bounded limiting rational value and does not alter the integral.
At all z, including the exceptional finite z set, the original convention has abs(U)<=1, so abs(F_(k,m))<=1 globally.

For the local formula b>0, the actual arguments are

    arg lambda=arctan b+arctan(b/3),
    arg alpha=-arctan b+arctan(b/3),
    theta=(k-m)arctan b+N arctan(b/3)
          =k pi-(k-m)arctan(1/b)-N arctan(3/b).           (WP15)

The sign of the remaining finite polynomial will be checked on the entire neighborhood, rather than absorbed into an unverified varying phase.

### 2. The actual moving witness and full neighborhood amplitude

K>=16, so b'(t)=4cos t-(K/2)csc^2(Kt/2)<0 on(0,1/(8K)).
As t decreases to0, b(t) tends to positive infinity.
At the other endpoint, cot(1/16)<16 and4sin(1/(8K))<=1/(2K), so b<17<32q.
There is therefore a unique t0=t_(k,m) in that interval with b(t0)=32q.

For0<x<=1/16, cot x<=1/x and cot x>=1/(2x).
Using these at Kt0/2, along with4sin t0<=1, gives

    1/(32Kq)<t0<=2/[K(32q-1)]<=2/(31Kq)<1/(12Kq).

Thus delta=1/(10000Kq)<t0 and t0+delta<1/(8K).
Set x0=cot(Kt0/2)=32q-4sin t0; then31q<x0<33q.
For abs(h)<=delta, the exact addition identity gives

    cot(K(t0+h)/2)=(x0-tan(Kh/2))/(1+x0 tan(Kh/2)).

The elementary small-angle bound abs(tan(Kh/2))<=Kabs(h)<=1/(10000q) shows that its denominator is at least1-33/10000.
Consequently

    abs(cot(K(t0+h)/2)-x0)
       <=1090q/9967<q/8.

The remaining4sin t changes by at most4delta, so throughout this full interval24q<=b(t)<=40q.

Let a_b=8/(1+b^2) and r_b=km a_b.
Then

    k a_b>=8/(1601m)>1/(201m),
    r_b<=1/72.

For l>=2, the absolute lth term of P_(k,m)(-a_b), divided by its first magnitude k a_b, is at most

    r_b^(l-1)/[l!(l-1)!]<=r_b^(l-1).

The sum of all these ratios is at most r_b/(1-r_b)<=1/71.
The first term is negative; hence the complete finite polynomial is strictly negative and has magnitude at least(70/71)k a_b, including the cases where no further term exists.

N=k+m<=2km=2q^2 and N/2>=1.
Bernoulli's elementary convexity inequality therefore gives

    abs(lambda)^k abs(alpha)^m
       =(1-8/(9+b^2))^(N/2)
       >=1-4N/(9+b^2)>=71/72.

Combining the two bounds, the amplitude in(WP15) is greater than70/(201*72m)>1/(256m).
This proves the complete local factorization and amplitude in(WP4), with no phase cancellation left unpaid.

### 3. Actual phase derivatives and the centered finite convolution

For abs(t)<=1/(8K) write

    S_*(t)=sin(Kt/2),
    B_*(t)=cos(Kt/2)+4sin t sin(Kt/2).

For a in{1,3}, the function phi_a=arg(B_*+iaS_*) is smooth on this entire interval because

    B_*>=1-1/512-1/(32K)>9/10.

On the witness interval it is exactly arctan(a/b).
Direct differentiation gives

    abs(B_*')<=4K, abs(B_*'')<=3K^2,
    abs((aS_*)')<=3K/2, abs((aS_*)'')<=3K^2/4.

For example B_*''=-(K^2/4)cos(Kt/2)-4sin t sin(Kt/2)
              +4Kcos t cos(Kt/2)-K^2sin t sin(Kt/2),
whose displayed bound follows from K>=16; the first-derivative bound follows by the same product differentiation.
The argument derivative formulas, applied to W_a=B_*+iaS_*, give

    abs(phi_a')<=abs(W_a')/abs(W_a)<=12K,
    abs(phi_a'')<=abs(W_a'')/abs(W_a)
                        +abs(W_a')^2/abs(W_a)^2<=64K^2.

For the second, the crude upper sum is(25/6+3025/81)K^2<64K^2; thus no singular argument branch estimate is used.
Equation(WP15) then implies abs(theta')<=24KN and abs(theta'')<=128K^2N.
Rounding its ACTUAL derivative at t0 gives abs(n_(k,m))<=25KN.
For abs(h)<=delta, Taylor's integral remainder and the rounding error yield

    abs(theta(t0-h)-theta(t0)+n_(k,m)h)
       <=abs(h)/2+64K^2N h^2
       <=1/(20000Kq)+128/10^8<1/16.                      (WP16)

Use the exact C637 probability kernel

    Fej_n(h)=n^-1 abs(sum_(r=0)^(n-1)exp(irh))^2,
    P_R=Fej_(floor(R/2)+1)^2/
                       [(2(floor(R/2)+1)^2+1)/(3(floor(R/2)+1))].

For every integer R>=2 it has closed support[-R,R], multipliers in[0,1] and angular tail at most4pi^3/(R^3 delta^3).
Our R>=C_band sqrt(k)m^(5/6) implies

    R delta>=32pi m^(1/3),
    p_tail=integral_(abs(h)>delta)P_R(h)dnu_1(h)<=1/(8192m).

Evaluate the actual finite modulated convolution

    I=integral P_R(h)exp(i n_(k,m)h)F_(k,m)(exp(i(t0-h)))dnu_1(h).

After rotation by -exp(-i theta(t0)), the central real part is at least1/(512m), by(WP4), (WP16) and cos(1/16)>=1/2.
The global bound abs(F_(k,m))<=1 pays the entire tail.
Thus

    abs(I)>=(1-p_tail)/(512m)-p_tail>=1/(1024m).

On the other hand, finite kernel expansion and Fubini give exactly

    I=sum_p (U^k)hat(p,-m)exp(i p t0)Phat_R(p-n_(k,m)).

Every multiplier is in[0,1] and is zero outside the closed centered band.
This proves(WP5) as a genuine finite Fourier sum, without using a point-restriction norm or any old four-coordinate band.

### 4. All harmonics, scalar cap coefficients and complete support

For L_tau and J in the statement, the common R is at least the radius required by(WP5) for EVERY1<=k<=L_tau and1<=m<=J.
Different k,m give disjoint triples even if their p bands overlap.
With x=sqrt(L_tau)J^(5/6)>=1, ceil(C_band x)<=(C_band+1)x gives

    N_sel=L_tau J(2R+1)
            <=3(C_band+1)L_tau^(3/2)J^(11/6).

There is no thinning of these bands.

Let g_tau(exp(i theta))=(1-(1+cos theta)/(2tau))_+.
Around theta=pi its support is abs(x)<=2arcsin sqrt(tau), and for abs(x)<=sqrt(tau) its value is at least3/4.
For1<=k<=L_tau, throughout its support

    abs(kx)<=arcsin sqrt(tau)/(2sqrt(tau))<=pi/4,

so cos(kx)>=1/2 and no negative part of the scalar integral is discarded.
Its Fourier coefficient therefore satisfies

    abs(ghat_tau(k))
       >=(1/(2pi))*(2sqrt(tau))*(3/4)*(1/2)
        =3sqrt(tau)/(8pi),                              (WP17)

with common sign(-1)^k.
Integrating first in w in F_tau(z,u,w)=g_tau(wV(z,u)), and then inverting both phase coordinates, gives for k>=1 exactly

    Fhat_tau(-p,m,k)=ghat_tau(k)(U^k)hat(p,-m).

At the common-zero convention, both sides of the w-coefficient identity vanish in the stated tau range; alternatively that set is Haar null.
No infinite Fourier expansion of the cap is required for this coefficient calculation.

Since L_tau sqrt(tau)>=1/8 for tau<=1/64, (WP5) and(WP17) give the full torus mass

    sum_(gamma in Gamma_(tau,J))abs(Fhat_tau(gamma))
       >=3/(65536pi)sum_(m=1)^J 1/m
       >=3log(J+1)/(65536pi).                            (WP18)

Under(WP8), abs(p)<=25K(L_tau+J)+R<=M, while k,m also lie in the closed-M interval.
Thus every selected gamma lies in C678's CLOSED three-box.
The adopted actual-family alias theorem gives distinct H_j(gamma); moreover

    H_j(-p,m,k)=-p+a_j m+c_j k>=c_j-M>0.

Here c_j>(L_j+1)^2>M_j, as verified by the actual size bounds.
Hence all returned coefficients contribute to W_* without the zero mode.
Apply the complete C678 finite return to the entire Gamma, and combine with(WP18), proving(WP9).

The exact count gives N_sel^(2/3)<=[3(C_band+1)]^(2/3)L_tau J^(11/9).
Using L_tau<=tau^-1/2/4 and epsilon_j<=E_w ell_M/M in the FULL B_w proves(WP10).
The min with1 is bounded by the displayed power without an additional smallness assumption.
Thus the original comparison and all four regularization/smoothing costs are still present.

### 5. Explicit full-box threshold and uniform critical estimate

Assume(WP11) and J=floor(H^(9/44)).
Since H>=2, J>=1.
All floors and ceilings are paid by

    L_tau<=(1/4)M^(2/3)ell_M^(-2/3)H^(-1/2)<=M^(2/3)/4,
    J<=H^(9/44)<=M^(3/11),
    sqrt(L_tau)J^(5/6)
          <=(1/2)M^(1/3)ell_M^(-1/3)H^(-7/88),
    R<=(C_band+1)sqrt(L_tau)J^(5/6)
          <=(1/2)(C_band+1)M^(1/3).                      (WP19)

The ceiling inequality uses sqrt(L_tau)J^(5/6)>=1, which holds because L_tau>=2.
In particular L_tau,J<=M.
The center-plus-radius bound is

    25K(L_tau+J)+R
       <=(25K/4)M^(2/3)+25K M^(3/11)
                                      +(C_band+1)M^(1/3)/2.

At M>=M_band, the three terms are separately at most M/3, respectively by the three thresholds(75K/4)^3, (75K)^(11/8) and[3(C_band+1)/2]^(3/2).
This proves ALL(WP8) uniformly for every H,tau in the strip.
Also M>=C_w provides the actual finite-return premise.
For j>=j_band, a_j>(j+1)K>4M_band, so M_j=floor(a_j/4)>=M_band and the family condition j>=4K holds.

The H interval is nonempty at the stated threshold.
Indeed1+log M<=2sqrt(M) for M>=1; for M>=2^16 this gives

    M^(4/3)/(64ell_M^(4/3))
       >=M^(2/3)/(64*2^(4/3))>=2^(10/3)>2.

For the complete errors in(WP10), J^(11/9)<=H^(1/4).
Substituting the lower allowed tau gives the first factor

    M^(-2/3)ell_M^(2/3)
          *M^(2/3)ell_M^(-2/3)H^(1/4-1/2)=H^(-1/4),

and the second factor

    M^-1*M^(8/9)ell_M^(-8/9)H^(1/4-2/3)
              =M^(-1/9)ell_M^(-8/9)H^(-5/12).

The stated C_error bounds both full coefficients.
Finally J+1>H^(9/44), so the positive term in(WP9) is at least27log H/(2883584pi).
This proves(WP12), with no uncharged logarithm or omitted finite coefficient.

### 6. Actual degree comparison and every shrinking sequence

The adopted weighted construction gives16M^2<d<2^10 M^2 for every actual j.
For T_d=1+log d and ell_M=1+log M, these inequalities imply

    2ell_M<T_d<8ell_M.

The lower follows from log16>1, and the upper from1+10log2<8 and log M>=0.
Combining these with the degree bounds gives

    16^(2/3)M^(4/3)/(8ell_M)^(4/3)
       <d^(2/3)/T_d^(4/3)
       <2^(20/3)M^(4/3)/(2ell_M)^(4/3),

which is precisely(WP13).
It concerns the actual minimal-polynomial degree, not c_j or the raw numerator degree.

For any positive shrinking sequence satisfying(WP14), put

    H_j^enl=M_j^(4/3)tau_j/(1+log M_j)^(4/3).

By(WP13) this tends to infinity.
Eventually M_j>=M_band, H_j^enl>=2 and tau_j<=1/64; also H_j^enl<=M_j^(4/3)/[64(1+log M_j)^(4/3)].
All(WP11) conditions then hold with H=H_j^enl and equality in its lower width bound.
The main term in(WP12) diverges, its first error tends to zero, and its second error tends to zero since M_j tends to infinity and H_j^enl does also.
The proof imposes no rate or monotonicity, and it makes no sequence-independent assertion about this entry index.
This proves the claimed original-family Wiener divergence.

## Reuse, source and remaining boundaries

C678's adopted exact weighted source construction, original Gram/rank/pole estimates, all translated laws and entire five-cost finite theorem are used at their stated scope.
Its odd-unweighted-factor obstruction and log2..log4 measure boundary are not removed by the new phase estimate.
The present argument independently derives the weighted Mobius coefficients, their neighborhood phases, the one-dimensional modulation center and all actual band counts.
C665 supplies only a previously understood local convolution idea, not its old four-coordinate coefficients, witnesses, rectangles, mass or count as a premise.
The positive finite kernel and its bounded classical attribution are those of adopted C637; its complete normalization, closed support, multiplier and tail statements suffice here.
No new external interpolation, rational Bernstein, stationary-phase or model-space theorem is invoked.
The fixed K remains the actual composite killer exponent, the original window remains2d, and the probability-law and source-depth limitations of C678 are unchanged.
The new degree criterion includes its logarithmic denominator and is sufficient only for the constructed actual family.
Bounded H, a stronger logarithm-free degree endpoint, optimality and near-one coverage remain unproved.

## Assessment history

### Decision weighted-phase-bands-open

| Field | Value |
| --- | --- |
| date | 2026-10-24T03:37 |
| status | open |
| reason | Register the complete new weighted Mobius coefficient and actual moving-witness modulation, full one-dimensional band support and scalar harmonic mass, exact original finite return with all five costs, explicit uniform critical strip and actual degree/logarithm sequence criterion. Root and phase_bands are contributors; the author-checked theorem awaits fresh independent whole review. The adopted C678 actual family, original2d normalization and log2..log4/source restrictions remain; no old-band substitution, bounded enlargement, logarithm-free endpoint or unrestricted completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire weighted-band statement](#statement) | WP1--WP14: complete actual-family and original-law contract, exact coefficients and local bands, entire selected support, all five returned costs, explicit finite thresholds, uniform H/tau region and every shrinking-sequence degree criterion. |
| argument | [Complete weighted-band proof](#complete-argument) | Sections1--6/WP15--WP19: exact algebra and signs, every witness/neighborhood/derivative/tail, scalar harmonics and full support, original closed-box/positivity, each error power and all degree/logarithm/entry quantifiers. |
| dependency | [Adopted actual weighted family and return](Yin_C_G0678_v1.md#decision-whole-reviewed-2026-10-24) | Whole weighted(1,1,2) source-certified actual family and full2d objects, degree and total measure, exact original epsilon and all-width stability, every translated law and all five costs in the finite closed-three-box return. |
| dependency | [Positive finite kernel](Yin_C_G0637_v1.md#complete-argument) | Exact squared-Fejer normalization, closed support, multipliers in[0,1] and4pi^3/(R^3 delta^3) tail, independently applied to the new one-dimensional modulation. |
| support | [Kernel source attribution](Yin_C_G0637_v1.md#source-and-reuse-boundary) | Existing bounded classical Jackson-kernel account; no new source proof is imported or inspection upgraded. |
| support | [Actual reuse and limitations](#reuse-source-and-remaining-boundaries) | New weighted bands distinguished from C665's old phase, entire original-family/source/window restrictions, retained logarithmic degree cost and unresolved bounded-H/near-one boundaries. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T03:48 |
| status | proved |
| reason | The complete fixed WP1--WP19 statement and six-section argument were directly read, followed by the whole fresh isolated R902. Adopt the actual weighted Mobius bands, complete support and all five returned costs, explicit uniform critical strip, exact actual-degree logarithmic comparison and every positive shrinking-sequence conclusion. No old C665 band is substituted, and no new external source-proof scope is claimed. The logarithmic denominator, original2d window and positive Mahler interval remain; bounded H, a logarithm-free endpoint, optimality, near-one coverage and unrestricted completion remain unproved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire weighted-band statement](#statement) | WP1--WP14: complete actual-family and original-law contract, exact coefficients and local bands, entire selected support, all five returned costs, explicit finite thresholds, uniform H/tau region and every shrinking-sequence degree criterion. |
| argument | [Complete weighted-band proof](#complete-argument) | Sections1--6/WP15--WP19: exact algebra and signs, every witness/neighborhood/derivative/tail, scalar harmonics and full support, original closed-box/positivity, each error power and all degree/logarithm/entry quantifiers. |
| dependency | [Adopted actual weighted family and return](Yin_C_G0678_v1.md#decision-whole-reviewed-2026-10-24) | Whole weighted(1,1,2) source-certified actual family and full2d objects, degree and total measure, exact original epsilon and all-width stability, every translated law and all five costs in the finite closed-three-box return. |
| dependency | [Positive finite kernel](Yin_C_G0637_v1.md#complete-argument) | Exact squared-Fejer normalization, closed support, multipliers in[0,1] and4pi^3/(R^3 delta^3) tail, independently applied to the new one-dimensional modulation. |
| support | [Kernel source attribution](Yin_C_G0637_v1.md#source-and-reuse-boundary) | Existing bounded classical Jackson-kernel account; no new source proof is imported or inspection upgraded. |
| support | [Actual reuse and limitations](#reuse-source-and-remaining-boundaries) | New weighted bands distinguished from C665's old phase, entire original-family/source/window restrictions, retained logarithmic degree cost and unresolved bounded-H/near-one boundaries. |
| review | [Fresh isolated whole mathematical review](../audits/reviews/Yin_R_G0902_v1.md#whole-weighted-phase-bands-degree-finding) | Entire new coefficient, sign, full-neighborhood, modulation, finite support and cost proof, every threshold and degree/sequence quantifier; unchanged C678 input uses only corrected R1067v2. |

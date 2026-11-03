---
author: Yin
---
# Uniform original Wiener ceilings at every fixed positive width in the two-factor Salem family

Human author Yin.
Root supplied the fixed-width question and contributed the already adopted two-factor construction in C682.
The paid_comparison contributor supplied and checked the present cellwise threshold-crossing, derivative-return and complete Wiener-ceiling argument.
This is author development, not an independent review; the new fixed record is initially open pending fresh whole review.

The input is exactly [the adopted actual C682v1 family](Yin_C_G0682_v1.md#decision-whole-reviewed-2026-10-24), with its [complete construction and original-window proof](Yin_C_G0682_v1.md#argument).
No new family or changed parameter schedule is introduced.
Local reuse supplies the generic finite variation mechanism already rechecked there from [C663](Yin_C_G0663_v1.md#complete-argument), and the weighted Fourier Cauchy estimate in [C174 Section 4, equation (11)](Yin_C_G0174_v1.md#narrow-contact-wiener-model).
The latter is used only at its elementary absolutely-continuous L2-derivative scope; none of C174's varying-family limit statements is substituted.

## Statement

### Same actual polynomials, projection and fixed phase

Fix the actual even integer

    K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))).

For every integer j>=4K let c=c_j be the least rational prime greater than (j+1)K.
Set L=K+2 and

    Q(z)=(z^2-1)(z^K-1)(z^c-1)
          -(z/2)[(z^K+1)(z^c-1)+(z^c+1)(z^K-1)],
    P(z)=Q(z)/(z-1), d=c+K+1=c+L-1.

The adopted C682 input supplies the actual monic integral irreducible Salem P, of even degree d and trace zero, with no further cyclotomic removal.
Its exterior root beta satisfies (1+sqrt(5))/2<beta, beta+beta^(-1)<=3 and beta<3; thus this is not a near-one family.
One has c<d<2c and d/c tends to one.
Use ALL d columns P,zP,...,z^(d-1)P in the ORIGINAL 2d coefficient coordinates, writing

    A_rel=[P,zP,...,z^(d-1)P], G=A_rel^t A_rel,
    Pi=A_rel G^(-1)A_rel^t,
    v_N(z)=(1,z,...,z^(N-1))^t,
    h(z)=v_(2d)(z)^*Pi v_(2d)(z)/(2d),
    G_d(z)=v_d(z)^*G^(-1)v_d(z), f_tau=(1-h/tau)_+.

The polynomial columns are linearly independent, so G is positive definite.
Circle Haar has mass one, derivatives are angular, Fourier coefficients use negative exponentials, and

    ||a||_A=sum_(n in Z)|ahat(n)|,
    W_*(a)=sum_(n in Z,n!=0)|ahat(n)|.

Define the fixed polynomials and phase

    A(z)=-(z^2-1)(z^K-1)+z,
    B(z)=(z^2-1)(z^K-1)-z^(K+1),
    V(z)=B(z)/A(z)=exp(i psi(t)), z=exp(it), psi(0)=pi,
    D_psi=||psi'||_infinity,
    h_0(z)=(1+Re(z^c V(z)))/2, F_tau=(1-h_0/tau)_+.

Here A and B are nonzero on the circle, V is fixed smooth unimodular, psi is a smooth lift with winding K, and 0<psi'<=D_psi<=34K+8<c.
All these are exact accepted C682 inputs, including the full original projection and the phase orientation.
Put

    A_1=sum_(n in Z)|n|*|Vhat(n)|<infinity,
    E_K=2L-1+A_1,
    delta_*=[28(1+60pi)]^(-2), C_obs=2/delta_*,
    C_stab=33C_obs+3.

### Uniform small-width ceiling and the fixed-width obstruction

Put

    S_0=C_obs(E_K+32), D_cell=(1+60pi)S_0+3,
    C_cross=1+2D_cell, A_rank=(3L-1)/2,
    C_interp=L-1+A_1,
    D_e=4sqrt(A_rank)+2C_interp,
    C_f=sqrt(C_stab E_K), D_g=D_e+sqrt(C_cross),
    C_V=sqrt((1+pi)(1+D_psi^2)),
    C_g=sqrt((1+pi)(C_f^2+D_g^2)).

All are fixed independently of c and tau.
The quantitative upper bound, for every declared c and 0<tau<=1/64, is

    W_*(f_tau)<=||f_tau||_A
       <=1+10C_V tau^(-1/4)+C_g tau^(-1/2).             (FW1)

In fact every fixed tau>0 has a finite upper bound independent of c.
This rules out fixed-positive-width degree divergence in this actual family, while retaining C682's shrinking-width divergence.
It does not claim an optimal shrinking-width exponent, a ceiling uniform over other phases/K/families, or an unrestricted Lehmer conclusion.


For explicit bounds on the remaining positive widths define, for 0<tau<1,

    delta_tau=min{1/2,(1-tau)/(1+tau)},
    B_tau=max{delta_tau^(-1),56/(pi sqrt(3))*sqrt(tau/(1-tau))},
    C_cross(tau)=1+B_tau D_cell,
    C_g(tau)=sqrt((1+pi)[C_f^2+(D_e+sqrt(C_cross(tau)))^2]),
    C_b(tau)=1/(2tau)+1/(pi sqrt(tau)),
    C_h=sqrt(17(1+pi)A_rank)+(1+C_V)/2.

For EVERY actual member c and every positive tau one has the complete bounds

    ||f_tau||_A<=1+6C_V C_b(tau)+C_g(tau)tau^(-1/2), 0<tau<1,
    W_*(f_tau)<=C_h/tau, tau>=1.

In particular, for every fixed tau>0,

    sup_(j>=4K) W_*(f_(j,tau))<infinity.

The numerical small-width ceiling FW1 applies simultaneously for every 0<tau<=1/64, not only for a fixed width or an eventual degree range.
C682's lower bound at shrinking widths remains unchanged; its conclusion at every tau_j tending to zero with d_j^2 tau_j tending to infinity is compatible with this ceiling.

## Argument

### 1. Cellwise relative-error budget, including the genuine pole

C682 proves the exact positive ratio h=r h_0 off t=0, with

    r=u+sigma, u=kappa/[4sin^2(t/2)], 0<kappa<=4/c^2,
    deg(sigma)<3c, ||sigma-1||_1<=S_0/c.

The finite variation estimate gives V(sigma)<=60pi S_0.
Partition the circle into c equal closed cells with disjoint interiors, choosing I_0=[-pi/c,pi/c].
Cell endpoints do not affect integrals.
On I_0's complement the pole has integral at most 1/c.
The inequality sin(pi/(2c))>=1/c gives u(pi/c)<=1.
The pole is decreasing on (0,pi) and even, so its total angular variation off I_0 is at most 2.
For each noncentral cell let delta_l=sup_(I_l)|r-1|.
On each such cell a continuously differentiable function has supremum at most its cell mean plus its angular variation.
Apply this separately to sigma-1 and u and sum to obtain

    sum_(l!=0)delta_l
      <=c||sigma-1||_1+V(sigma)
           +c integral_(I_0^c)u+V_(I_0^c)(u)
      <=D_cell.                                         (FW2)

No bound on the pole in I_0 and no lower bound on r are assumed.

### 2. Exact threshold-crossing price

Let E_tau be the symmetric difference of {h<tau} and {h_0<tau}.
The central cell contributes at most 1/c.
If delta_l>=1/2, its entire contribution is at most 1/c<=2delta_l/c.
If delta_l<1/2, then a mismatch implies

    tau/(1+delta_l)<=h_0<=tau/(1-delta_l).

The interval has length at most (8/3)tau delta_l and is contained in [2tau/3,2tau].
For 0<tau<=1/64 the derivative of (1+cos Theta)/2 on this interval has magnitude sqrt(h_0(1-h_0))>=sqrt(tau)/2.
Each of its two phase-side preimages therefore has length at most 6sqrt(tau)delta_l.
The phase Theta=ct+psi(t) increases with derivative at least c and increment at most 4pi in a cell.
It intersects at most seven full contact bands, a conservative bound valid also at endpoints.
Thus the mismatch probability in this cell is at most

    84sqrt(tau)delta_l/(2pi c)<=2delta_l/c.

Here sqrt(tau)<=1/8 and pi>3 were used.
Together with FW2 this proves

    nu(E_tau)<=C_cross/c.                                (FW3)

For completeness every fixed 0<tau<1 has the analogous bound.
Define

    delta_tau=min{1/2,(1-tau)/(1+tau)},
    B_tau=max{delta_tau^(-1),
                    56/(pi sqrt(3))*sqrt(tau/(1-tau))},
    C_cross(tau)=1+B_tau D_cell.

For delta_l>=delta_tau pay the full cell by delta_l/(delta_tau c).
For delta_l<delta_tau the threshold interval lies in [2tau/3,(1+tau)/2].
The phase derivative magnitude is at least sqrt(tau(1-tau)/3).
Its width in h is at most (8/3)tau delta_l.
The two phase-side lengths, seven possible bands, and normalized probability therefore give at most
56sqrt(tau/(1-tau))delta_l/(pi sqrt(3)c).
Consequently nu(E_tau)<=C_cross(tau)/c for every 0<tau<1.
This bound may deteriorate as tau approaches 1; the exact tau>=1 case is handled separately below.

### 3. Raw derivative comparison before clipping

Let h_V=v_(2d)^*Pi_V v_(2d)/(2d)=(c/d)h_q,
where h_q=(1+Re(z^c q_c))/2 and q_c is C682's FULL-grid Fejer interpolant of V.
Put T=h-h_V.
The same-window trace-rank estimate gives

    |T|<=1, ||T||_1<=(3L-1)/(2d)<=A_rank/c,
    deg(T)<=2d-1<4c.

Finite Parseval hence gives

    ||T||_2<=sqrt(A_rank/c),
    ||T'||_2<=4sqrt(A_rank)sqrt(c).                       (FW4)

For a character z^n with 0<|n|<c, the exact interpolation error is
(|n|/c)(z^(n-sign(n)c)-z^n).
Its supremum is at most 2|n|/c and its derivative supremum at most |n|, since the absolute frequencies in the difference sum to c.
For |n|>=c, interpolation has at most two frequencies of absolute size below c, with nonnegative coefficients summing to one; this follows by reducing n modulo c in the exact grid values.
The corresponding error supremum is at most 2<=2|n|/c, and derivative supremum at most c+|n|<=2|n|.
The input constant mode n=0 is exact.
Absolute summation using A_1=sum |n||Vhat(n)| gives

    ||q_c-V||_infinity<=2A_1/c,
    ||(q_c-V)'||_infinity<=2A_1.                         (FW5)

Inputs n in cZ other than zero interpolate to the constant one and obey the stated tail bounds.
All original cyclic samples are retained, including V(1)=-1.
The fixed smoothness of V justifies both derivative and function summation.
Since h_q has degree below 2c and 0<=h_q<=1, ||h_q'||_2<=2c.
Therefore

    ||(h_V-h_0)'||_2
      <=(L-1)||h_q'||_2/d
           +(1/2)[c||q_c-V||_infinity+||(q_c-V)'||_infinity]
      <=2(L-1)+2A_1=2C_interp.

For e=h-h_0, FW4 yields

    ||e'||_2<=D_e sqrt(c).                               (FW6)

### 4. Clipped derivative and the entire Fourier sum

Both clipped functions are absolutely continuous along the actual one-dimensional circle.
The original h is a nonconstant trigonometric polynomial and h_0 has strictly monotone phase, so for 0<tau<1 their threshold sets are finite.
Their a.e. path derivatives give, with g=f_tau-F_tau,

    g'=-e'/tau *1_(h<tau)
         -h_0'/tau*[1_(h<tau)-1_(h_0<tau)].

Also |h_0'|<=(c+D_psi)/2<=c.
For small widths, FW3 and FW6 imply

    ||g'||_2<=D_g sqrt(c)/tau,
    ||g||_2<=C_f/sqrt(c).                               (FW7)

The second bound is C682 TF2 and is uniform over ALL widths.
For a fixed arbitrary 0<tau<1 replace D_g by D_e+sqrt(C_cross(tau)) in FW7.

C174 Section 4 equation (11) states, for every absolutely continuous periodic a with a' in L2 and every eta>0,

    ||a||_A<=[1+pi/eta]^(1/2)
                   [||a||_2^2+eta^2||a'||_2^2]^(1/2).

It follows by finite-set weighted Cauchy, Parseval and the elementary integral comparison for sum_n(1+eta^2 n^2)^(-1); increasing finite sets needs no prior absolute Fourier summability.
Apply it to FW7 with eta=tau/c.
Since 0<tau<1 and c>=1,

    ||f_tau-F_tau||_A<=C_g tau^(-1/2)                    (FW8)

for the small-width constants, and the same formula with
C_g(tau)=sqrt((1+pi)[C_f^2+(D_e+sqrt(C_cross(tau)))^2]) for arbitrary 0<tau<1.
Thus the whole original Fourier sum is controlled, not just a finite coefficient window.

### 5. Fixed-phase Wiener estimate and all positive fixed widths

For each integer k!=0, apply the same weighted inequality with eta=1/|k| to V^k.
Its L2 norm is one and its derivative L2 norm is at most |k|D_psi.
This proves ||V^k||_A<=C_V sqrt(|k|).

Let b_tau(s)=(1-(1+cos s)/(2tau))_+.
For 0<tau<=1/64 its mean is at most sqrt(tau), because its contact probability is (2/pi)arcsin(sqrt(tau))<=sqrt(tau).
Writing s=pi+x, its support is |x|<=a=2arcsin(sqrt(tau)), and inside that support b_tau=1-sin^2(x/2)/tau.
Its derivative has two jumps of magnitude at most tau^(-1/2), and interior variation at most 2tau^(-1/2), since a<pi/2.
Piecewise integration by parts twice, including those actual endpoint jumps, gives

    |bhat_tau(k)|<=min{sqrt(tau),2/[pi sqrt(tau)k^2]}, k!=0.

Take N=ceil(tau^(-1/2)), so tau^(-1/2)<=N<=2tau^(-1/2).
The finite part is bounded by sqrt(tau)N^(3/2)<=2sqrt(2)tau^(-1/4).
The tail is at most [2/(pi sqrt(tau))] integral_N^infinity x^(-3/2)dx<=4tau^(-1/4)/pi.
It follows that

    sum_(k>=1)sqrt(k)|bhat_tau(k)|<=5tau^(-1/4).

The expansion

    F_tau(z)=sum_(k in Z)bhat_tau(k) z^(ck) V(z)^k

converges absolutely in A, because multiplication gives the elementary coefficient-convolution inequality and monomial multiplication preserves the A norm.
It identifies the actual phase cap by the absolutely convergent scalar Fourier series of b_tau.
All aliases are allowed and paid by the triangle inequality; no injectivity is needed for an upper bound.
Both signs and the zero mode give

    ||F_tau||_A<=1+10C_V tau^(-1/4).                     (FW9)

FW8 and FW9 prove FW1.

For every fixed 0<tau<1, without assuming tau<=1/64, the interior derivative variation is at most pi/tau and the two jumps total at most 2/sqrt(tau).
Thus |bhat_tau(k)|<=C_b(tau)/k^2 where

    C_b(tau)=1/(2tau)+1/(pi sqrt(tau)).

Using sum_(k>=1)k^(-3/2)<=3 gives ||F_tau||_A<=1+6C_V C_b(tau).
Combining with the general FW8 yields the explicit finite ceiling

    ||f_tau||_A<=1+6C_V C_b(tau)+C_g(tau)tau^(-1/2),
                                                 0<tau<1. (FW10)

Finally for tau>=1, f_tau=1-h/tau since 0<=h<=1.
Applying C174's inequality to T in FW4 with eta=1/c gives
||T||_A<=sqrt(17(1+pi)A_rank).
The full-grid interpolation maps every character to a convex combination of at most two characters, hence ||q_c||_A<=||V||_A<=C_V.
Therefore ||h_V||_A<=(1+C_V)/2 and, with

    C_h=sqrt(17(1+pi)A_rank)+(1+C_V)/2,

one has

    W_*(f_tau)=W_*(h)/tau<=C_h/tau, tau>=1.              (FW11)

This also handles tau=1 exactly without taking a singular limit in FW10.
Every fixed positive width consequently has a uniform original Wiener ceiling along all actual degrees in C682.
The quantitative small-width upper exponent 1/2 need not be sharp; C682's returned shrinking-width lower exponent is 1/4 in its declared domain.


## Exact dependency and unresolved scope

C682's adopted actual-family argument is used in full only for its declared original polynomials, full 2d window, same-window rank bound, complete cyclic interpolant, positive Gram ratio with its genuine pole, and cap L2 stability.
Its accepted MS05 source-construction scope is inherited through that exact input; there is no new prime selection, factor removal or source-proof inspection claim here.
The finite variation estimate is already proved and checked for these new phase cells in C682 Section 4; C663 is its mechanism-level supporting home.
C174 equation (11) supplies the complete weighted Fourier estimate from finite-set Cauchy and Parseval, with its retained classical Parseval source boundary unchanged.
The original threshold-crossing and derivative combination are the new ingredients retained here.
No native experiment, prime enumeration, general Wiener composition theorem, stationary-phase theorem or uninspected external result is used.
The constants may depend on the fixed K and fixed phase; no ceiling over changing K, the older weighted three-factor family, the four-factor family, or unrestricted Salem inputs is asserted.
The quantitative gap between the small-width upper exponent 1/2 and the C682 returned lower exponent 1/4 remains open.
Neither this fixed-width obstruction nor the earlier shrinking-width divergence completes the unrestricted Lehmer Task.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-24T04:27 |
| status | open |
| reason | Register the complete original Wiener ceiling for every fixed positive width in the adopted actual two-factor Salem family, including the uniform small-width estimate, genuine-pole cell budget, threshold-crossing costs, raw and clipped derivative return, all Fourier modes and exact tau>=1 case. Fresh isolated whole review is required. C682 and other families remain fixed, and no optimal-width or unrestricted Lehmer conclusion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [All original inputs and every positive-width ceiling](#statement) | Exact actual K/c/P/d family and full 2d projection; simultaneous FW1, remaining-width constants and every fixed positive tau uniformly over actual degrees. |
| argument | [Complete five-part argument](#argument) | Genuine-pole cell budget, all threshold bands, full-grid derivative interpolation, original clipped derivative and whole Fourier norm, both Fourier signs and every positive-width endpoint. |
| dependency | [Adopted actual two-factor family](Yin_C_G0682_v1.md#decision-whole-reviewed-2026-10-24) | Exact actual source construction, full original window, same-window rank and all-sample interpolant, fixed smooth phase, true pole with finite sigma and TF2 cap L2 stability; no old family substitution. |
| dependency | [Weighted complete Fourier Cauchy estimate](Yin_C_G0174_v1.md#narrow-contact-wiener-model) | Section 4 equation (11), absolutely continuous periodic function with L2 derivative, any positive eta, finite Fourier sets before the full sum; no fixed-input asymptotic limit is used. |
| support | [Finite derivative-variation mechanism](Yin_C_G0663_v1.md#complete-argument) | Generic degree-n finite reproduction and variation inequality, already rechecked in C682's exact phase cells; none of C663's distinct family assumptions is imported. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T04:37 |
| status | proved |
| reason | The complete fixed FW1--FW11 statement and five-section argument were directly read, followed by all of fresh isolated R910. Adopt the original two-factor fixed-width Wiener ceiling, including the true-pole cell budget, every crossing/derivative cost, all Fourier coefficients and aliases, simultaneous small-width bound and exact tau>=1 branch. The constants belong to this fixed family and phase; its shrinking-width divergence remains unchanged and no optimal-width, other-family or unrestricted conclusion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [All original inputs and every positive-width ceiling](#statement) | Exact actual K/c/P/d family and full 2d projection; simultaneous FW1, remaining-width constants and every fixed positive tau uniformly over actual degrees. |
| argument | [Complete five-part argument](#argument) | Genuine-pole cell budget, all threshold bands, full-grid derivative interpolation, original clipped derivative and whole Fourier norm, both Fourier signs and every positive-width endpoint. |
| dependency | [Adopted actual two-factor family](Yin_C_G0682_v1.md#decision-whole-reviewed-2026-10-24) | Exact actual source construction, full original window, same-window rank and all-sample interpolant, fixed smooth phase, true pole with finite sigma and TF2 cap L2 stability; no old family substitution. |
| dependency | [Weighted complete Fourier Cauchy estimate](Yin_C_G0174_v1.md#narrow-contact-wiener-model) | Section 4 equation (11), absolutely continuous periodic function with L2 derivative, any positive eta, finite Fourier sets before the full sum; no fixed-input asymptotic limit is used. |
| support | [Finite derivative-variation mechanism](Yin_C_G0663_v1.md#complete-argument) | Generic degree-n finite reproduction and variation inequality, already rechecked in C682's exact phase cells; none of C663's distinct family assumptions is imported. |
| review | [Fresh isolated whole mathematical review](../audits/reviews/Yin_R_G0910_v1.md#two-factor-fixed-width-wiener-ceiling-whole-independent-finding) | Entire FW1--FW11, all five proof sections, exact original-window inputs and every declared width/member, complete pole/crossing/derivative/Fourier costs and retained family boundaries. |

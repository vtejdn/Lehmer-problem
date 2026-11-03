---
author: Yin
---

# Local modulation of actual phase bands and complete original support cost

Human author Yin.
Root supplied the local phase-factorization and modulation proposal, including the corrected cotangent convention.
The phase_bands contributor checked and completed the actual neighborhood, amplitude, phase, tail, support and original-return calculations.
Both are contributors; this initial fixed theorem is open pending independent whole review.
The complete original arithmetic input, coordinate dimension and probability law are retained.
No numerical scan or new computation group is used.

## Statement

Fix the same even integer K as the actual four-exponent construction,
K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))).
Define psi_tau(s)=max{0,1-(1-s)/tau} for0<tau<=1 and W_*(f)=sum_(h in Z,h!=0)|fhat(h)|.
Choose the actual primes

    a_j=min{p prime:p>(j+1)K},
    b_j=min{p prime:p>(K+a_j+3)^2},
    c_j=min{p prime:p>(K+a_j+b_j+3)^2},
    ell_j=(K,a_j,b_j,c_j), d_j=K+a_j+b_j+c_j-1.

The exact original monic irreducible Salem input is

    P_j(x)=[2(x^2-1)product_(i=0)^3(x^ell_(j,i)-1)
       -x sum_(q=0)^3(x^ell_(j,q)+1)product_(i!=q)(x^ell_(j,i)-1)]/[2(x-1)^3].

On the three-torus define the explicit polynomials

    R=(z^K-1)(u-1)(v-1),
    S=(z^K+1)(u-1)(v-1)+(z^K-1)(u+1)(v-1)+(z^K-1)(u-1)(v+1),
    Acal=-(z^2-1)R-zR/2+zS/2,
    Bcal=(z^2-1)R-zR/2-zS/2.
Set U=Acal/Bcal off their common-zero set and0 on that set, g=abs(Acal)^2+abs(Bcal)^2 and Ncal=2Acal conjugate(Bcal).
All Haar measures have mass1, Fourier coefficients use exp(-i gamma dot theta), and angular derivatives use radians.
For an actual degree-d_j Salem P_j of the specified schedule, set N_coeff,j=2d_j and let A_rel,j be the N_coeff,j-by-d_j full coefficient matrix of P_j,tP_j,...,t^(d_j-1)P_j.
The original rank-d_j residual projection and its actual single-circle symbol are

    R_j=I-A_rel,j(A_rel,j^T A_rel,j)^-1 A_rel,j^T,
    v_j(t)=(1,t,...,t^(2d_j-1))^T,
    k_j(t)=(2d_j)^-1 v_j(t^-1)^T R_j v_j(t).
Thus the kernel below uses every original coefficient, with no cyclic or conjugate-distribution replacement.

Use L_j=K+a_j+b_j+2, M_j=floor(a_j/4), E_j=[1+pi L_j(5+2log c_j)]/c_j and epsilon_j=(4L_j-5)/(2d_j)+E_j/2.
For every actual j with M_j>=2 put omega_j=(1+log M_j)/M_j.
Define the fixed original-polynomial constants

    A_der,K=1+sum_(l=1)^3(||partial_l Acal||_infinity
                                  +||partial_l Bcal||_infinity),
    D_reg,K=4pi A_der,K.

Define

    D_0(z)=-2(z-z^-1)+(z^K+1)/(z^K-1),
    b(z)=Im D_0(z), z_0=exp(i pi/K), delta_0=pi/(4K),
    I=[pi/K-delta_0,pi/K+delta_0],
    D(z,u)=D_0(z)+(u+1)/(u-1),
    C_loc,K=ceil(32000pi+1024pi(K+4)).

For positive integers k,m, let

    F_(k,m)(z,u)=integral_(v in T) U(z,u,v)^k v^m dHaar(v),

the actual negative-v coefficient of U^k.
All such integrals use the bounded definition of U already stated, including its common zeros.

For EVERY k,m>=1, put q0=sqrt(km), N=k+m, and choose the unique t_0=t_(k,m) in (-pi,0) satisfying

    -cot(t_0/2)=16q0-b(z_0).

Set delta_u=1/(1000q0).
On the entire local rectangle arg(z) in I and |t-t_0|<=delta_u, write

    x(t)=-cot(t/2), d(z,t)=b(z)+x(t),
    phi_z(t)=arctan(2/d(z,t)).

Then 12q0<=d<=20q0, and the complete coefficient has the fixed-sign phase form

    F_(k,m)(z,exp(it))
       =(-1)^(k+1) A_(k,m)(z,t) exp(iN phi_z(t)),
    A_(k,m)(z,t)>=1/(128m).                                      (M1)

Define the actual integer center

    n_(k,m)=floor(N phi_(z0)'(t_0)+1/2).

It satisfies |n_(k,m)|<=14(k+m).
For EVERY integer radii R_z,R_u>=2 satisfying

    R_z>=C_loc,K m^(1/3), R_u>=C_loc,K sqrt(k)m^(5/6),

the CLOSED finite coefficient band satisfies

    sum_(|p|<=R_z,|q-n_(k,m)|<=R_u)
       |(U^k)hat(p,q,-m)|>=1/(512m).                              (M2)

The center is part of the support and is not replaced by zero.
The local estimate concerns these actual three-torus coefficients, not a point-restriction norm.

For positive integers L,J choose the common radii

    R_z(L,J)=ceil(C_loc,K J^(1/3)),
    R_u(L,J)=ceil(C_loc,K sqrt(L)J^(5/6)),

and define the complete four-dimensional set

    G_(L,J)={(-p,-q,m,k): 1<=k<=L, 1<=m<=J,
                  |p|<=R_z(L,J), |q-n_(k,m)|<=R_u(L,J)}.

Its exact cardinality and complete upper bound are

    N_sel=LJ(2R_z(L,J)+1)(2R_u(L,J)+1)
       <=9(C_loc,K+1)^2 L^(3/2)J^(13/6).                         (M3)

The bands for different k,m remain distinct because their fourth and third coordinates differ.

For the original finite return, put

    V(z,u,v)=U(z^-1,u^-1,v^-1),
    Kcal=(1-Re(wV))/2, F_tau=psi_tau(Kcal),
    f_(j,tau)=psi_tau(k_j),
    H_j(gamma)=gamma_0+a_j gamma_1+b_j gamma_2+c_j gamma_3.

For 0<tau<=1/64 use L=L_tau=floor(1/(4sqrt(tau))).
Whenever

    R_z(L,J),J,L<=M_j,
    14(L+J)+R_u(L,J)<=M_j,                                      (M4)

all of G_(L,J) lies in the original CLOSED four-box and its original H_j frequencies are distinct and strictly positive.
For every 0<lambda<=1 put rho=tau lambda and

    E_2(j,tau,lambda)=sqrt(epsilon_j/tau)+8lambda^(1/3)
       +2sqrt(D_reg,K)sqrt(omega_j)lambda^(-1/4)
       +2D_reg,K omega_j/(tau sqrt(rho)).

The complete original Wiener norm then satisfies

    W_*(psi_tau(k_j))
       >=3log(J+1)/(32768pi)
          -sqrt(N_sel)E_2(j,tau,lambda).                         (M5)

Every selected coefficient and its full quadratic return cost is paid.
If omega_j<=tau^(3/2), the choice lambda=(omega_j/tau^(3/2))^(6/5) gives the valid substitution

    E_2<=E_bal
       :=sqrt(epsilon_j/tau)
           +(8+2D_reg,K)omega_j^(2/5)tau^(-3/5)
           +2sqrt(D_reg,K)omega_j^(1/5)tau^(9/20).

Consequently fix ANY real 0<theta<16/39 and put

    Delta_theta=2/5-39theta/40>0,
    zeta_theta=6Delta_theta/13>0,
    sigma_theta=min(Delta_theta/2,39theta/80)>0.

There exist j0,C_error depending only on theta,K such that, for EVERY j>=j0 and EVERY width M_j^-theta<=tau<=1/64,

    W_*(psi_tau(k_j))
       >=[3zeta_theta/(32768pi)]log M_j
          -C_error M_j^-sigma_theta(1+log M_j)^(1/2).              (M6)

For example theta=2/5 is included and exceeds the preceding strict range theta<4/11.
Every shrinking sequence eventually satisfying the lower inequality has actual Wiener norms tending to infinity, with a possibly sequence-dependent entry index into the uniform strip.
No equality assertion at theta=16/39, arbitrary faster thinning, or optimality of this sufficient exponent is claimed.
The original full 2d_j window, actual contact-minus-Haar margin at least 1/2, finite fixed-j norms and log 2<m(P_j)<log 4 remain unchanged.
No near-one family or unrestricted Mahler-gap conclusion follows.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Complete argument

<a id="argument"></a>

<a id="local-modulation-inputs-and-correction"></a>
### Exact inputs, corrected development and source scope

The complete actual [C629 finite coefficient formula](Yin_C_G0629_v2.md#power-band-amplitude), its fixed interval and [averaged-v derivative calculation](Yin_C_G0629_v3.md#witness-specific-anisotropic-refinement) were read before this local refinement.
An initial exploratory proposal wrote d=b+cot(t/2).
That expression has the wrong sign for C(w)=(w+1)/(w-1), because C(exp(it))=-i cot(t/2).
It is retained here solely as corrected development history and is excluded from every mathematical premise.
The actual convention throughout the theorem and proof is x=-cot(t/2), D=i(b+x).
The exploratory witness 8sqrt(km) is replaced by the stated 16sqrt(km), which pays a complete fixed neighborhood.
No conclusion from the unfinished initial sign convention is adopted.

For the local smoothing, use exactly the adopted [C637 positive kernel](Yin_C_G0637_v1.md#exact-positive-kernel-and-closed-support).
For integer N>=1 and normalized Haar measure it is built from

    Fej_N(h)=N^-1 |sum_(l=0)^(N-1)exp(ilh)|^2,
    c_N=(2N^2+1)/(3N),
    J_N(h)=Fej_N(h)^2/c_N,
    P_R=J_(floor(R/2)+1), R>=2.

It is nonnegative, even and has integral one.
Its Fourier multipliers lie in [0,1], its support lies in the CLOSED interval [-R,R], and

    integral |h|P_R(h)dHaar(h)<=3pi/R,
    integral_(|h|>=delta)P_R(h)dHaar(h)
       <=4pi^3/(R^3 delta^3), 0<delta<=pi.

The complete finite identities, constants and direct proof at that fixed input were read.
The [C637 source account](Yin_C_G0637_v1.md#source-and-reuse-boundary) retains its actually checked classical Jackson attribution, exact probability normalization and limited primary-passage scope.
No new external proof, general approximation theorem or source-proof upgrade is invoked here.

The original coefficient-error comparison is separately the adopted [C635 complete finite quadratic theorem](Yin_C_G0635_v1.md#whole-box-finite-projection), using its own exact omega_j and full E_2 budget.
The local P_R construction changes the selected finite coefficient bands; every original return term remains the one actually proved in C635.
Only the declared local kernel properties and original finite-set return are combined.
The original contact, arithmetic-family and historical source-review scopes remain unchanged.

<a id="complete-local-modulation-calculation"></a>
### Complete local phase, convolution and original-return calculation

Set

    a_amp=1/128,
    C_loc,K=ceil(32000pi+1024pi(K+4)),
    delta_0=pi/(4K).

For every positive integer k,m, write q0=sqrt(km), N=k+m, b(z)=Im D_0(z), z_0=exp(i pi/K), and choose the unique t_0 in (-pi,0) such that

    x_0=-cot(t_0/2)=16q0-b(z_0).

Then 11q0<=x_0<=21q0.
Use delta_u=1/(1000q0).
For |h|<=delta_u, put s_h=tan(h/2).
The exact addition identity is

    x(t_0+h)=(x_0+s_h)/(1-x_0 s_h),
    x(t_0+h)-x_0=s_h(1+x_0^2)/(1-x_0 s_h).

The estimate |s_h|<=|h| follows from |sin(h/2)|<=|h|/2 and cos(h/2)>=1/2.
Thus the denominator is at least 1-21/1000>1/2 and

    |x(t_0+h)-x_0|<=884q0/1000<q0.

This also keeps the whole interval on the regular branch, away from u=1.
For every z angle in I, |b(z)-b(z_0)|<=(K+4)delta_0<=pi/2<2, since actual K>=4.
Therefore throughout the full local z,u rectangle,

    12q0<=d(z,t_0+h)<=20q0.                                      (LM1)

The interval is deliberately wider than the strict bounds just obtained.

The exact finite coefficient formula from C629 is

    F_(k,m)=(-1)^k lambda_D^N P_(k,m)(4/D^2),
    lambda_D=D/(D+2),
    P_(k,m)(v)=sum_(l=1)^min(k,m)
                       binom(k,l)binom(m-1,l-1)v^l.              (LM2)

All exponents in the underlying finite binomial formula are nonnegative; (LM2) is only used where d>0.
Here 4/D^2=-4/d^2 is negative real.
The leading term has magnitude 4k/d^2>=1/(100m).
With r=4km/d^2<=1/36, the sum of all remaining term magnitudes divided by the leading magnitude is at most

    sum_(l>=2) r^(l-1)/[l!(l-1)!]<=r/(1-r)<=1/35.

This includes an empty tail when k=1 or m=1.
Hence P is strictly negative, with its complete magnitude at least (34/35)/(100m).
For r=N/2>=1, the derivative of (1-y)^r is at least -r on 0<=y<1, so integration gives (1-y)^r>=1-r y.
Since N<=2km, this elementary inequality gives

    |lambda_D|^N=(1-4/(d^2+4))^(N/2)
       >=1-2N/(d^2+4)>=35/36.

Consequently the complete coefficient has the representation

    F_(k,m)(z,exp(it))=(-1)^(k+1) A_(k,m)(z,t)
                                     exp(iN phi_z(t)),
    A_(k,m)>=17/(1800m)>1/(128m),
    phi_z(t)=arctan(2/d(z,t)),                                   (LM3)

on the whole local rectangle.
No asymptotic leading-term equality is used.

For x=-cot(t/2) one has x'=(1+x^2)/2.
Differentiation gives exactly

    phi_z'=-(1+x^2)/[(x+b)^2+4],
    phi_z''=-(1+x^2)[b x^2+(b^2+3)x-b]/[(x+b)^2+4]^2.

The bounds |b|<=5, x=d-b and |x|<=(1+x^2)/2 imply

    1+x^2<=13(d^2+4),
    |b x^2+(b^2+3)x-b|<=24(1+x^2).

Thus |phi_z'|<=13 and |phi_z''|<=4056<4096.
Let n_(k,m)=floor(N phi_(z0)'(t_0)+1/2), so

    |n_(k,m)-N phi_(z0)'(t_0)|<=1/2,
    |n_(k,m)|<=14N.                                              (LM4)

For convolution in the displacement h, use the factor exp(+i n_(k,m)h), with input F(z_0,exp(i(t_0-h))).
Taylor's formula bounds the residual phase by

    |h|/2+2048N h^2
       <=1/2000+4096/1000000<1/16.

After multiplication by the single constant rotation

    xi_(k,m)=(-1)^(k+1)exp(-iN phi_(z0)(t_0)),

the real part of the full modulated integrand is at least a_amp/(2m) on |h|<=delta_u.
The sign is positive because the modulation cancels the actual negative displacement's linear phase.

For any integer radii R_z>=C_loc,K m^(1/3) and R_u>=C_loc,K sqrt(k)m^(5/6), use the exact adopted P_R kernels of C637.
Let p_u and p_z be their tails outside delta_u and delta_0.
Their tail estimates give

    p_u<=4pi^3*10^9/(C_loc,K^3 m)<=a_amp/(64m),
    p_z<=4pi^3/(C_loc,K^3 delta_0^3 m)<=a_amp/(64m).               (LM5)

The first follows from C_loc,K>=32000pi=32pi*1000.
The second follows from C_loc,K>=128K=32pi/delta_0.
All these radii are at least two, as required by the kernel definition.

On the same local rectangle, the actual averaged-v derivative identity already proved in C629 yields

    |partial_arg(z) F_(k,m)(z,exp(it))|
       <=4k(K+4)/(d^2+4)<=(K+4)/(36m).

Thus the z first moment has cost at most

    3pi(K+4)/(36m R_z)
       <=1/(12288m)<=a_amp/(64m),                               (LM6)

using C_loc,K>=1024pi(K+4).
The global almost-everywhere bound |F_(k,m)|<=1 pays every complementary region.

First set

    G(z)=integral P_(R_u)(h)exp(i n_(k,m)h)
                           F_(k,m)(z,exp(i(t_0-h)))dHaar(h).

Then Re(xi G(z_0))>=a_amp(1-p_u)/(2m)-p_u.
Now convolve G in z with P_(R_z), evaluated at z_0, and call the result H_(k,m).
On |s|<=delta_0 and |h|<=delta_u compare the z variation at that fixed u using (LM6).
On the union of the two tail regions use the global difference bound two.
This proves

    |H_(k,m)-G(z_0)|<=z_moment+2p_u+2p_z.

All tail costs remain present even when their regions overlap.
By (LM5)--(LM6), p_u<=1/64 and therefore

    Re(xi H_(k,m))
       >=a_amp(1-p_u)/(2m)-3p_u-2p_z-z_moment
       >=51a_amp/(128m)>=a_amp/(4m)=1/(512m).                    (LM7)

The exact constant 51/128 comes from 63/128 for the retained central mass minus 12/128 for the five tail units and one moment unit.

For a Fourier character exp(i p arg(z)+i q t), the modulation contributes the multiplier

    Phat_(R_z)(p) Phat_(R_u)(q-n_(k,m)).

It is supported in the CLOSED rectangle |p|<=R_z,|q-n_(k,m)|<=R_u and has magnitude at most one.
Fubini identifies Fhat_(k,m)(p,q) with (U^k)hat(p,q,-m).
Thus (LM7) proves the actual finite coefficient mass

    sum_(|p|<=R_z,|q-n_(k,m)|<=R_u)
           |(U^k)hat(p,q,-m)|>=1/(512m).                         (LM8)

The point values are used only after positive finite convolution; no slice norm replaces these original three-torus coefficients.

For positive integers L,J choose

    R_z=ceil(C_loc,K J^(1/3)),
    R_u=ceil(C_loc,K sqrt(L)J^(5/6)).

Sum every band (LM8), then use the original positive scalar cap harmonics for 1<=k<=L_tau with L=L_tau.
The resulting four-dimensional selection has exact cardinality

    N_sel=LJ(2R_z+1)(2R_u+1)
       <=9(C_loc,K+1)^2 L^(3/2)J^(13/6).                        (LM9)

Different k,m have different fourth and third coordinates respectively, so this count does not identify or merge overlapping u intervals.
The whole actual selection lies in the CLOSED original four-box if

    R_z,J,L<=M_j, 14(L+J)+R_u<=M_j.                             (LM10)

Its H_j frequencies are pairwise distinct by the exact 2M_j difference theorem and positive by the unchanged c_j dominance.
The complete original torus mass is at least3log(J+1)/(32768pi).
C635's arbitrary-finite-set theorem therefore yields

    W_*(psi_tau(k_j))>=3log(J+1)/(32768pi)
                      -sqrt(N_sel) E_2(j,tau,lambda).            (LM11)

This finite estimate charges all coefficients and all original L2 return costs.
The balanced E_bal version is legal under omega_j<=tau^(3/2).

For fixed 0<theta<16/39, put

    Delta=2/5-39theta/40>0, zeta=6Delta/13>0,
    sigma=min(Delta/2,39theta/80)>0,
    J=floor(M_j^zeta), L=L_tau.

The closed-box conditions (LM10) hold uniformly for M_j^-theta<=tau<=1/64, because the relevant upper powers are

    zeta<1, zeta/3<1, theta/2<1,
    theta/4+5zeta/6=2/13-theta/8<1.

Constants and ceiling errors are fixed and all maxima have exponent strictly below one.
The balanced parameter is legal eventually since theta<16/39<2/3.
From (LM9), sqrt(N_sel)<=3(C_loc,K+1)tau^(-3/8)J^(13/12).
The three complete balanced-return errors have M_j exponents

    -1+7theta/8+13zeta/12=-4/5+31theta/80<-25/39,
    -2/5+39theta/40+13zeta/12=-Delta/2,
    -1/5+13zeta/12=-39theta/80,                                  (LM12)

and logarithmic powers1/2,2/5,1/5.
For the last error the remaining factor tau^(3/40) is positive and is bounded by one.
Thus they are all at most a fixed multiple of M_j^-sigma(1+log M_j)^(1/2), uniformly in the strip.
Since log(J+1)>zeta log M_j, (LM11) supplies

    W_*(psi_tau(k_j))>=3zeta log M_j/(32768pi)
                     -C_error(theta,K)M_j^-sigma
                                          (1+log M_j)^(1/2).     (LM13)

The upper/lower cutoff thresholds are uniform within the strip, while sequence entry may depend on the sequence.
All original input, full coefficient dimension, actual contact and total-measure boundaries remain unchanged.
This physical version requires independent whole review before adoption; no conclusion is asserted at theta=16/39.


## Assessment history

### Decision local-modulation-registration

| Field | Value |
| --- | --- |
| date | 2026-10-23T20:42 |
| status | open |
| reason | Register the complete corrected-sign local amplitude and phase theorem, explicit modulated positive convolution with all tail costs, centered closed-band coefficient mass and exact original support count. The full adopted finite quadratic return gives every strict exponent below16/39 with a uniform error. This new contributor theorem awaits independent whole review; the wrong initial sign is retained only as corrected development history. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact theorem](#statement) | Every k,m and local rectangle, actual phase centers, every allowed closed band and exact support count, full finite original return and every uniform strip for fixed0<theta<16/39, including all original input and endpoint limits. |
| argument | [Whole complete argument](#argument) | Corrected cotangent sign, exact finite coefficient formula, full amplitude domination, phase derivatives/modulation, explicit radius constants, every central/tail/moment cost, closed Fourier support and original error exponents. |
| dependency | [Exact finite power coefficient](Yin_C_G0629_v2.md#power-band-amplitude) | Actual U^k finite binomial formula and three-torus Fourier identity; the larger witness and whole local amplitude are proved here. |
| dependency | [Actual fixed interval](Yin_C_G0629_v2.md#many-phase-setting) | Same actual D0, b, z0, I, K>=4 and original regular-coordinate domains. |
| dependency | [Exact averaged-v derivative](Yin_C_G0629_v3.md#witness-specific-anisotropic-refinement) | Complete average abs(partial_D U^k)=4k/(d^2+4), used at every actual local u and z; no whole-u derivative improvement is assumed. |
| dependency | [Adopted positive finite kernel](Yin_C_G0637_v1.md#exact-positive-kernel-and-closed-support) | Exact P_R definition, nonnegative unit mass, closed support, multipliers, 3pi/R first moment and 4pi^3/(R^3 delta^3) tails. |
| dependency | [Kernel direct proof and source scope](Yin_C_G0637_v1.md#source-and-reuse-boundary) | Actual classical attribution/normalization and explicitly limited primary reading; exact kernel calculations are at the fixed input, with no external proof upgrade. |
| dependency | [Full finite quadratic return](Yin_C_G0635_v1.md#whole-box-finite-projection) | Every finite Gamma in the original closed four-box, all five E_2 costs and legal balanced E_bal, including the actual sqrt(epsilon_j/tau). |
| dependency | [Scalar harmonics and inverse phase](Yin_C_G0629_v3.md#many-harmonic-transfer) | Positive k cap coefficients, exact phase inversion and L_tau bounds, applied to every centered selected band. |
| dependency | [Actual original aliases](Yin_C_G0565_v2.md#moving-band-exact-alias) | Closed2M_j difference theorem and original positive-frequency dominance, with centers and radii both checked. |
| dependency | [Original schedule asymptotic](Yin_C_G0569_v2.md#static-phase-original-return) | True epsilon_j rate from lower prime separations, used in the full first quadratic-return error. |
| dependency | [Original fixed contacts](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Actual finite fixed-j Wiener norms, margin at least1/2 and separate fixed-input thin-limit order. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T20:55 |
| status | proved |
| reason | Adopt the entire local-modulation theorem after main reading of complete C638 and isolated whole R845. The corrected actual phase, full local amplitude, integer center and every positive-kernel tail/moment support the closed shifted coefficient bands. All original center-plus-radius and finite quadratic costs prove every fixed theta<16/39 on its complete uniform strip. The old omega return, source limits, original2d/Haar/sequence scope and unrestricted Task boundary remain unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact theorem](#statement) | Every k,m and local rectangle, actual phase centers, every allowed closed band and exact support count, full finite original return and every uniform strip for fixed0<theta<16/39, including all original input and endpoint limits. |
| argument | [Whole complete argument](#argument) | Corrected cotangent sign, exact finite coefficient formula, full amplitude domination, phase derivatives/modulation, explicit radius constants, every central/tail/moment cost, closed Fourier support and original error exponents. |
| dependency | [Exact finite power coefficient](Yin_C_G0629_v2.md#power-band-amplitude) | Actual U^k finite binomial formula and three-torus Fourier identity; the larger witness and whole local amplitude are proved here. |
| dependency | [Actual fixed interval](Yin_C_G0629_v2.md#many-phase-setting) | Same actual D0, b, z0, I, K>=4 and original regular-coordinate domains. |
| dependency | [Exact averaged-v derivative](Yin_C_G0629_v3.md#witness-specific-anisotropic-refinement) | Complete average abs(partial_D U^k)=4k/(d^2+4), used at every actual local u and z; no whole-u derivative improvement is assumed. |
| dependency | [Adopted positive finite kernel](Yin_C_G0637_v1.md#exact-positive-kernel-and-closed-support) | Exact P_R definition, nonnegative unit mass, closed support, multipliers, 3pi/R first moment and 4pi^3/(R^3 delta^3) tails. |
| dependency | [Kernel direct proof and source scope](Yin_C_G0637_v1.md#source-and-reuse-boundary) | Actual classical attribution/normalization and explicitly limited primary reading; exact kernel calculations are at the fixed input, with no external proof upgrade. |
| dependency | [Full finite quadratic return](Yin_C_G0635_v1.md#whole-box-finite-projection) | Every finite Gamma in the original closed four-box, all five E_2 costs and legal balanced E_bal, including the actual sqrt(epsilon_j/tau). |
| dependency | [Scalar harmonics and inverse phase](Yin_C_G0629_v3.md#many-harmonic-transfer) | Positive k cap coefficients, exact phase inversion and L_tau bounds, applied to every centered selected band. |
| dependency | [Actual original aliases](Yin_C_G0565_v2.md#moving-band-exact-alias) | Closed2M_j difference theorem and original positive-frequency dominance, with centers and radii both checked. |
| dependency | [Original schedule asymptotic](Yin_C_G0569_v2.md#static-phase-original-return) | True epsilon_j rate from lower prime separations, used in the full first quadratic-return error. |
| dependency | [Original fixed contacts](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Actual finite fixed-j Wiener norms, margin at least1/2 and separate fixed-input thin-limit order. |
| review | [Independent whole local-modulation finding](../audits/reviews/Yin_R_G0845_v1.md#whole-local-modulation-finding) | Entire M1--M6 and LM1--LM13, actual branch/sign, every local rectangle and amplitude/phase constant, modulation and tail costs, all closed support centers/cardinalities and original return exponents; kernel attribution and previous review/source scopes retained. |


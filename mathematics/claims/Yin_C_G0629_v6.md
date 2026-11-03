---
author: Yin
---

# Critical-power logarithmic corridors for the original contact kernel

This is a joint project deduction by the coordinating agent and the phase_bands contributor for Yin under the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
This physical version retains the complete earlier mathematics and adds a conditional general coefficient-budget theorem together with its actual adopted square-root-budget application.
It is registered open pending a new independent whole review.
The [v4 adoption](Yin_C_G0629_v4.md#decision-whole-reviewed-2026-10-23) and [R837v1](../audits/reviews/Yin_R_G0837_v1.md#whole-sharper-return-finding) remain limited to their exact physical predecessor.
All earlier statements, proofs, decisions and review scopes remain preserved at their own fixed versions.
The actual new application uses only the adopted C632 input and the complete balancing calculation retained below.
No unregistered coefficient-rate result, new arithmetic family, numerical scan, source acquisition or computation group is used.
The [initial critical-log version](Yin_C_G0629_v5.md#statement) is preserved; this version disambiguates its budget constant from the already fixed derivative constant without changing the theorem or rate.

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
Define

    A_K=1+||g||_infinity+||Ncal||_infinity
        +sum_(l=1)^3(||partial_l g||_infinity+||partial_l Ncal||_infinity),
    D_K=8pi A_K^2.
For an actual degree-d_j Salem P_j of the specified schedule, set N_coeff,j=2d_j and let A_rel,j be the N_coeff,j-by-d_j full coefficient matrix of P_j,tP_j,...,t^(d_j-1)P_j.
The original rank-d_j residual projection and its actual single-circle symbol are

    R_j=I-A_rel,j(A_rel,j^T A_rel,j)^-1 A_rel,j^T,
    v_j(t)=(1,t,...,t^(2d_j-1))^T,
    k_j(t)=(2d_j)^-1 v_j(t^-1)^T R_j v_j(t).
Thus the kernel below uses every original coefficient, with no cyclic or conjugate-distribution replacement.


Use L_j=K+a_j+b_j+2, M_j=floor(a_j/4), and the exact original approximation budget

    E_j=[1+pi L_j(5+2log c_j)]/c_j,
    epsilon_j=(4L_j-5)/(2d_j)+E_j/2,
    omega_j=(1+log M_j)/M_j,
    beta_j=epsilon_j+(64+3D_K)omega_j^(1/13).

These definitions are used for sufficiently large j so M_j>=2.
The symbol beta_j denotes the approximation budget, not an exterior Salem root.
The original schedule gives beta_j=O_K(((1+log M_j)/M_j)^(1/13)).
Put f_(j,tau)=psi_tau(k_j).

For every pair of positive integers k,m, the negative-v coefficient F_(k,m) of U^k satisfies an actual witness bound

    |F_(k,m)(exp(i pi/K),u_(k,m))|>=1/(8m)

for some actual regular u_(k,m) on the circle.
On the fixed z interval |arg z-pi/K|<=delta=pi/(4K), it has the uniform derivative bound

    |partial_arg(z) F_(k,m)|+|partial_arg(u) F_(k,m)|
       <=C_K(k+m), C_K=10000(K+1).

For integers R>=2,J>=2,L>=1 satisfying

    16 C'_K J(L+J)(1+log R)<=R, C'_K=2pi C_K+2pi/delta,

the explicit finite set

    B_(R,J)={(p,q,-m): |p|,|q|<=R-1, 1<=m<=J}

has at most 4R^2J elements and satisfies, simultaneously for every 1<=k<=L,

    sum_(gamma in B_(R,J))|(U^k)hat(gamma)|>=log(J+1)/16.

In particular, for every sufficiently large actual j and every 0<tau<=1/64, set L_tau=floor(1/(4sqrt(tau))).
Whenever R,J,L_tau<=M_j and the preceding finite-cutoff condition holds with L=L_tau, the complete original kernel satisfies

    W_*(f_(j,tau))
       >=3log(J+1)/(1024pi)-R^2 J beta_j/tau^(3/2).                  (A)

Every original frequency used to prove (A) is nonzero and positive.
The bound pays the entire finite four-dimensional selected support and the original coefficient comparison.

Consequently fix ANY real theta with 0<theta<2/65 and set

    Delta=1/13-(5/2)theta>0,
    zeta=Delta/10, alpha=theta/2+2zeta.

There exist j0 and C depending only on theta,K such that, for EVERY j>=j0 and EVERY width M_j^-theta<=tau<=1/64,

    W_*(psi_tau(k_j))
       >=[3zeta/(1024pi)]log M_j
          -C M_j^(-Delta/2)(1+log M_j)^(1/13).                     (B)

In particular, for EVERY sequence tau_j->0 with tau_j>=M_j^-theta eventually, the actual norms W_*(psi_(tau_j)(k_j)) tend to infinity.
Such a sequence enters the stated strip at a possibly sequence-dependent index; the finite bound and its error are uniform within that strip.
For example (B) covers tau_j=M_j^-1/100 and every eventually larger shrinking width.
All these original contact transforms retain their actual contact-minus-Haar margin at least 1/2 and finite Wiener norms at each fixed j,tau.
The positive total-measure range log 2<m(P_j)<log 4 is unchanged.
No arbitrary simultaneous thin-corridor theorem, near-one family or unrestricted Mahler-gap conclusion is asserted.
The exponent 2/65 is a sufficient boundary of these estimates, not a necessary threshold for actual divergence.


### Additional unequal-cutoff statement

Retain all the preceding actual objects, original normalization and conclusions.
For each k,m choose the actual witness with Im D(z_0,u_(k,m))=+4sqrt(km), where z_0=exp(i pi/K) and D is defined in the argument.
Then throughout the same fixed z interval I=[pi/K-delta,pi/K+delta], at that FIXED u_(k,m),

    |partial_arg(z) F_(k,m)(z,u_(k,m))|<=(K+4)/m.                    (C)

The earlier uniform u derivative 8192(k+m) remains valid for every u and every z in I.
For integers R_z,R_u>=2, J>=2,L>=1, define

    T_K(R_z,R_u,J,L)
       =8192pi J(L+J)(1/2+log R_u)/R_u
          +pi(K+4)(1/2+log R_z)/R_z+2pi J/(R_z delta).

If T_K<=1/16, then simultaneously for every 1<=k<=L,

    sum_(|p|<=R_z-1,|q|<=R_u-1,1<=m<=J)
       |(U^k)hat(p,q,-m)|>=log(J+1)/16.                            (D)

This set has (2R_z-1)(2R_u-1)J<=4R_z R_u J elements, all of which are retained in the cost.
For every sufficiently large actual j and every 0<tau<=1/64, use the same L_tau=floor(1/(4sqrt(tau))).
Whenever R_z,R_u,J,L_tau<=M_j and T_K(R_z,R_u,J,L_tau)<=1/16, the complete original-window kernel satisfies

    W_*(psi_tau(k_j))
       >=3log(J+1)/(1024pi)-R_z R_u J beta_j/tau^(3/2).             (E)

In particular fix ANY real theta_prime with 0<theta_prime<1/26 and define

    Delta_prime=1/13-2theta_prime>0, zeta_prime=Delta_prime/10.

There exist j1 and C1 depending only on theta_prime,K such that, for EVERY j>=j1 and EVERY width M_j^-theta_prime<=tau<=1/64,

    W_*(psi_tau(k_j))
       >=[3zeta_prime/(1024pi)]log M_j
          -C1 M_j^(-Delta_prime/2)(1+log M_j)^(1/13).               (F)

Thus every sequence tau_j->0 that eventually satisfies tau_j>=M_j^-theta_prime has actual Wiener norms tending to infinity.
Its index of entry into the uniform strip may depend on that sequence.
For example theta_prime=1/30 is allowed and is strictly larger than 2/65, so (F) includes a genuinely smaller-width corridor than (B).
All original input, full 2d_j coefficient, margin, finite fixed-j norm and positive total-measure boundaries stated above remain unchanged.
The sufficient exponent 1/26 is not asserted to be optimal or necessary, and the arbitrary simultaneous thin-width question remains unresolved.


### Additional sharper-return statement

Retain all original objects, the explicit finite condition T_K and conclusions (A)--(F).
For the same original phase polynomials define

    A_der,K=1+sum_(l=1)^3(||partial_l Acal||_infinity
                                  +||partial_l Bcal||_infinity),
    D_reg,K=4pi A_der,K,
    beta_new,j=epsilon_j+12sqrt(omega_j)[1+log(1/omega_j)]^2
                              +3D_reg,K sqrt(omega_j),
    hlog_j=1+log(1/omega_j), rho_opt,j=omega_j/hlog_j^2,
    beta_opt,j=epsilon_j
       +12sqrt(rho_opt,j)[1+log(1/rho_opt,j)]^2
       +3D_reg,K omega_j/sqrt(rho_opt,j).

Here M_j>=2, so 0<omega_j<1, hlog_j>=1 and 0<rho_opt,j<=1.
The label opt denotes this particular balancing choice and makes no optimality assertion.
Both beta_new,j/tau and beta_opt,j/tau bound EVERY original-to-four-torus coefficient error at gamma in [-M_j,M_j]^4 for every 0<tau<=1.
They satisfy

    beta_new,j=O_K(M_j^-1/2(1+log M_j)^(5/2)),
    beta_opt,j<=epsilon_j+(48+3D_reg,K)sqrt(omega_j)hlog_j
              =O_K(M_j^-1/2(1+log M_j)^(3/2)).                    (G)

Each is a valid individual-coefficient estimate; no infinite coefficient sum is controlled without its finite support price.

For every sufficiently large actual j and 0<tau<=1/64, if
R_z,R_u,J,L_tau<=M_j and T_K(R_z,R_u,J,L_tau)<=1/16, then for EITHER choice budget_j in {beta_new,j,beta_opt,j},

    W_*(psi_tau(k_j))
       >=3log(J+1)/(1024pi)-R_z R_u J budget_j/tau^(3/2).               (H)

The symbol budget_j denotes the chosen complete coefficient-error budget.

In particular fix ANY real theta_new with 0<theta_new<1/4 and set

    Delta_new=1/2-2theta_new>0, zeta_new=Delta_new/10.

There exist j2 and C2 depending only on theta_new,K such that, for EVERY j>=j2 and EVERY width M_j^-theta_new<=tau<=1/64,

    W_*(psi_tau(k_j))
       >=[3zeta_new/(1024pi)]log M_j
          -C2 M_j^(-Delta_new/2)(1+log M_j)^(3/2).                 (I)

Every sequence tau_j->0 eventually satisfying tau_j>=M_j^-theta_new therefore has actual original Wiener norms tending to infinity.
Its entry into the uniform strip may occur at a sequence-dependent index.
For example theta_new=1/8 lies strictly beyond the preceding exponent range theta_prime<1/26.
The original 2d_j coefficient dimension, probability Haar law, actual contact-minus-Haar margin at least 1/2, finite fixed-j Wiener norms and log 2<m(P_j)<log 4 remain unchanged.
Statement (I) does not assert the unmodified critical width M_j^-1/4, an optimal exponent, an arbitrary simultaneous thin-width theorem, a near-one family or an unrestricted Mahler-gap conclusion.


### Additional general critical-power statement and actual application

Retain the SAME original k_j,F_tau,H_j,M_j, Fourier conventions, finite support and explicit condition T_K.
Suppose a nonnegative sequence mathcal_B_j, constants C_budget>0 and j_budget, and fixed real parameters

    0<b_decay<4, p_log>=0

satisfy, for EVERY j>=j_budget,

    mathcal_B_j<=C_budget M_j^-b_decay(1+log M_j)^p_log,

and, for EVERY 0<tau<=1/64 and EVERY gamma in [-M_j,M_j]^4 intersection Z^4,

    |fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma)|
       <=mathcal_B_j/tau.                                        (J)

The budget is independent of the chosen tau and gamma.
This is an explicit premise of the general theorem; no arbitrary new coefficient rate is asserted.

For EVERY fixed a_log>(p_log+1)/2, define

    eps_log=a_log-(p_log+1)/2>0, r_log=eps_log/5.

There exist j3 and C3 depending only on K,b_decay,p_log,a_log,C_budget and j_budget such that, for EVERY j>=j3 and EVERY width

    M_j^(-b_decay/2)(log M_j)^a_log<=tau<=1/64,

the actual original kernel satisfies

    W_*(psi_tau(k_j))
       >=[3r_log/(1024pi)]loglog M_j
          -C3(log M_j)^(-eps_log).                                (K)

The threshold includes log M_j>1, and the width strip is nonempty for all sufficiently large j.
A sequence eventually in this strip has actual Wiener norms tending to infinity.
Any index at which a prescribed sequence enters the strip may depend on the sequence.

For the ACTUAL adopted budget beta_opt,j in (G), premise (J) holds with b_decay=1/2 and p_log=3/2.
Thus, for EVERY fixed a_log>5/4, put eps_log=a_log-5/4 and r_log=eps_log/5.
There exist j4,C4 depending only on K,a_log such that, for EVERY j>=j4 and EVERY width

    M_j^-1/4(log M_j)^a_log<=tau<=1/64,

one has

    W_*(psi_tau(k_j))
       >=[3r_log/(1024pi)]loglog M_j
          -C4(log M_j)^(-eps_log).                                (L)

In particular, the actual sequence tau_j=M_j^-1/4(log M_j)^a_log eventually lies in the strip and has norms tending to infinity.
For example a_log=3/2 is permitted.
These widths are eventually smaller than M_j^-theta for EVERY fixed theta<1/4, so this is a further corridor beyond the earlier fixed-power result.
The equality a_log=5/4, the unmodified critical width M_j^-1/4 and arbitrary faster thinning remain unclassified here.
The original family, complete 2d_j coordinates, actual normalized Haar law, contact-minus-Haar margin at least 1/2, fixed-j finiteness and log 2<m(P_j)<log 4 remain unchanged.
No stronger coefficient rate is used for this actual application.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Complete author argument

<a id="argument"></a>

<a id="many-phase-reuse"></a>
## Question, exact inputs and source boundary

The [complete C569v2 argument](Yin_C_G0569_v2.md#argument) gives a logarithmic finite coefficient sum for U itself, but its use of only the first w harmonic leaves a factor sqrt(tau).
The question is whether several positive w harmonics remove that loss while paying every original coefficient-comparison error.
The fixed inputs below are read at their actual retained scopes.
The ordinary finite binomial, geometric-series and quotient calculations do not require a new source theorem.
The rational derivative estimate below is proved directly by a finite rational comparison and Cauchy's integral estimate; no general rational Bernstein inequality is imported.
A local search by rational Bernstein, Blaschke, maximum modulus and Cauchy derivatives found the existing [GMR18 unit](../audits/literature/GMR18/Yin_U001.md#gmr18-u001), whose actual inspected finite-Blaschke normalization and boundary derivative scope is retained as attribution only.
That unit does not state the new uniform derivative bound below.
The needed classical complex-analysis interface was then checked directly in the retained [Deb15 author notes](../literature/pdf/Deb15.pdf).
On 2026-10-23 the contributor text-read printed/PDF p.10 Theorem 4.1, pp.11--12 the differentiated integral formula and Corollary 4.3, and p.24 Corollaries 9.6--9.7.
For a function holomorphic near a closed radius-h disk, the n=1 integral formula gives |f'(z_0)|<=sup_boundary|f|/h.
For a function holomorphic near the closed unit disk, the maximum-modulus principle bounds its modulus by its boundary supremum; a constant function satisfies the same conclusion directly.
These established interfaces are accepted for the pole-free rational functions actually used below, including the exterior quotient after inversion.
The displayed Cauchy-inequality text suppresses modulus notation in its supremum, but its differentiated integral formula and triangle-inequality derivation give the stated absolute-value bound directly.
The complete surrounding lecture proofs, later source results and the original historical proofs were not audited, and no source acquisition or source-byte change was made.
The exact rational comparison, location of every pole and constants below are project deductions, not assertions attributed to Deb15 or GMR18.

The exact fixed inputs are:

- [C565v2 equation (11)](Yin_C_G0565_v2.md#moving-band-fejer-budget): for EVERY gamma in [-M_j,M_j]^4, the original-circle coefficient differs from the exact four-torus coefficient by at most beta_j/tau.
- [C565v2 exact alias proof](Yin_C_G0565_v2.md#moving-band-exact-alias): H_j is injective on that entire integer box, because every nonzero difference with coordinates at most 2M_j has nonzero H_j.
- [C569v2 exact rational phase](Yin_C_G0569_v2.md#static-phase-geometric-band), its [fixed z interval](Yin_C_G0569_v2.md#static-phase-local-derivatives) and [Fejer bounds](Yin_C_G0569_v2.md#static-phase-finite-support).
- [C569v2 original schedule estimate](Yin_C_G0569_v2.md#static-phase-original-return): beta_j=O_K(((1+log M_j)/M_j)^(1/13)), with the same original primes and no upper prime-gap premise.
- [C174 original contacts](Yin_C_G0174_v1.md#narrow-contact-fixed-statement): every fixed original Wiener norm is finite and the actual contact-minus-Haar margin is at least 1/2.

No first-band statement is applied to a different harmonic without verifying its actual scope.
Only the already universal four-dimensional coefficient comparison is reused; the new power coefficients, simultaneous harmonic selection and total support payment are proved here.

<a id="many-phase-setting"></a>
## Exact original setting

Fix the same even K and the original primes a_j,b_j,c_j from C565v2, with

    a_j=min{p prime:p>(j+1)K},
    b_j=min{p prime:p>(K+a_j+3)^2},
    c_j=min{p prime:p>(K+a_j+b_j+3)^2},
    d_j=K+a_j+b_j+c_j-1, M_j=floor(a_j/4).

The original P_j, its full rank-d_j residual projection in 2d_j coefficient coordinates and k_j are unchanged.
Write f_(j,tau)=psi_tau(k_j), where psi_tau(s)=(1-(1-s)/tau)_+.
Write W_*(f)=sum_(h in Z,h!=0)|fhat(h)|, with normalized circle Haar measure and the exp(-ih theta) Fourier convention.
The original family satisfies log 2<m(P_j)<log 4.

Keep the exact three-torus phase U=Acal/Bcal from C565v2, defined to be zero on its null common-zero set, and define

    V(z,u,v)=U(z^-1,u^-1,v^-1),
    Kcal=(1-Re(wV))/2, F_tau=psi_tau(Kcal),
    H_j(eta,k)=eta_0+a_j eta_1+b_j eta_2+c_j k.

All torus Fourier coefficients use probability Haar measure and exp(-i gamma dot theta).
For regular circle points set C(w)=(w+1)/(w-1) and

    D_0(z)=-2(z-z^-1)+C(z^K), D=D_0(z)+C(u),
    lambda=D/(D+2), Q=-4/(D+2)^2.

These D values are purely imaginary.
C569v2 gives the exact absolutely convergent v expansion

    U=-lambda+Q sum_(m>=1)lambda^(m-1)v^-m.

Use theta_0=pi/K, z_0=exp(i theta_0), delta=pi/(4K), and I=[theta_0-delta,theta_0+delta].
On I, |D_0|<=5 and |partial_theta D_0|<=K+4.

<a id="power-band-amplitude"></a>
## Exact power coefficients and a uniform witness

For positive integers k,m, let F_(k,m)(z,u) be the negative-v coefficient of U(z,u,v)^k.
For regular z,u the convergent geometric expansion and a finite binomial expansion give

    F_(k,m)=sum_(l=1)^min(k,m)
       binom(k,l) binom(m-1,l-1) (-lambda)^(k-l) Q^l lambda^(m-l).        (1)

Whenever D is nonzero and purely imaginary, set a=4/|D|^2.
Then Q/(-lambda^2)=4/D^2=-a, so (1) becomes

    F_(k,m)=(-lambda)^k lambda^m
       sum_(l=1)^min(k,m) binom(k,l)binom(m-1,l-1)(-a)^l.                (2)

At z=z_0, Im D ranges over the whole real line as u runs through its regular circle points.
Choose an actual u_(k,m) with |D|^2=16km, so a=1/(4km).
The absolute value of the l=1 term in (2) is 1/(4m).
For l>=2, binom(k,l)<=k^l/l! and binom(m-1,l-1)<=m^(l-1)/(l-1)! give

    sum_(l=2)^min(k,m) binom(k,l)binom(m-1,l-1)a^l
       <=(1/m) sum_(l>=2) 4^-l/[l!(l-1)!]
       <=1/(12m).                                                    (3)

This bound remains valid when the sum is empty.
Moreover |lambda|^2=(1+a)^-1 and

    |lambda|^(k+m)
       >=exp(-(k+m)/(8km))>=exp(-1/4)>=3/4.                           (4)

Here log(1+a)<=a and k^-1+m^-1<=2; the last inequality follows from exp(1/4)<=sum_(r>=0)(1/4)^r=4/3.
Consequently, for EVERY k,m>=1,

    |F_(k,m)(z_0,u_(k,m))|>=1/(8m).                                  (5)

This uses different actual evaluation points for different k,m, which is legitimate because the later Fejer estimate is uniform in u.
No point restriction is substituted for a torus coefficient.
Since |U^k|=1 almost everywhere, |F_(k,m)|<=1 almost everywhere, and Fubini identifies

    (F_(k,m))hat(p,q)=(U^k)hat(p,q,-m).                               (6)

<a id="power-band-derivative"></a>
## A direct rational derivative bound

On I define the degree-one polynomials

    L=(D_0+3)u-(D_0+1), A=(D_0+1)u+(1-D_0).

Then lambda=A/L and Q=-4(u-1)^2/L^2.
For N=k+m, every summand in (1) has denominator L^N and a numerator of degree at most N.
All powers k+m-2l in that numerator are nonnegative.
Therefore, after w=u^-1, F_(k,m)(z,w^-1) has the form

    f(w)=P(w)/(1-a_0 w)^N, deg P<=N,
    a_0=(D_0+1)/(D_0+3), |a_0|<=sqrt(26/34)<7/8.                     (7)

The final strict bound is the exact inequality 26*64<34*49.
The denominator has no zero on the closed unit disk.
By (6), its continuous boundary values have modulus at most 1, hence the maximum-modulus principle gives |f|<=1 in that disk.
For the exterior, define B(w)=(w-conjugate(a_0))/(1-a_0 w).
The quotient f/B^N=P(w)/(w-conjugate(a_0))^N is holomorphic in the exterior of the unit disk including infinity and has boundary modulus at most 1.
Apply the maximum-modulus principle after inversion to obtain |f(w)|<=|B(w)|^N outside the disk, wherever f has no pole.

Set h=1/(4096N).
For 1<=|w|<=1+h, we have |1-a_0 w|>=1/16 and |w|^2-1<=3h.
The elementary identity

    |B(w)|^2=1+(|w|^2-1)(1-|a_0|^2)/|1-a_0 w|^2

therefore implies |B(w)|^N<=exp(384Nh)=exp(3/32)<2.
The radius-h disk around any unit-circle point lies in the pole-free region and has |f|<=2.
Cauchy's integral formula for f' gives |f'|<=2/h=8192N at that point.
Angular differentiation and inversion preserve the derivative's modulus, proving

    |partial_t F_(k,m)|<=8192(k+m).                                   (8)

For the z derivative, use the exact Cayley form

    U=(1-D-C(v))/(1+D+C(v)), partial_D U=-2/(1+D+C(v))^2.

For regular circle u,v and theta in I, D+C(v) is imaginary, so |partial_D U|<=2.
Differentiating U^k under the v integral is justified by the uniform bound 2k(K+4); alternatively integrate the bounded difference quotient and pass by dominated convergence.
Thus

    |partial_theta F_(k,m)|<=2k(K+4).                                (9)

The rational formula extends both bounds through u=1.
Choose C_K=10000(K+1), so (8)--(9) imply

    |partial_theta F_(k,m)|+|partial_t F_(k,m)|<=C_K(k+m).              (10)

Outside I, only the global almost-everywhere bound |F_(k,m)|<=1 is used.
No global derivative bound across the original common-zero set is claimed.

<a id="power-band-finite-cutoff"></a>
## Finite support with separately paid power and band cutoffs

Let R>=2, J>=2 and L>=1 be integers.
Apply the two-coordinate product Fejer convolution of degree R-1 to F_(k,m), with 1<=k<=L and 1<=m<=J.
The exact C569v2 first-moment and tail bounds give, at (z_0,u_(k,m)),

    |P_(R,k,m)-F_(k,m)|
       <=2pi C_K(k+m)(1+log R)/R+2pi/(R delta)
       <=C'_K(k+m)(1+log R)/R,                                     (11)
    C'_K=2pi C_K+2pi/delta.

The tail uses a difference at most 2 outside the z displacement interval; the u displacement may wrap around the circle because (7) is smooth and periodic there.
Every Fejer coefficient multiplier lies in [0,1].
Accordingly, if

    16 C'_K J(L+J)(1+log R)<=R,                                    (12)

then (5)--(6) and (11) give

    sum_(|p|,|q|<=R-1)|(U^k)hat(p,q,-m)|>=1/(16m)                   (13)

for all the stated k,m.
The negative-v bands are disjoint, so for

    B_(R,J)={(p,q,-m): |p|,|q|<=R-1, 1<=m<=J}

we have

    |B_(R,J)|=(2R-1)^2 J<=4R^2 J,
    sum_(gamma in B_(R,J))|(U^k)hat(gamma)|>=log(J+1)/16             (14)

for EVERY 1<=k<=L.
The last inequality follows by comparing sum_(m=1)^J 1/m with integral_1^(J+1) dx/x.
All coefficients in the entire rectangle are paid for; there is no sparsity assumption.

<a id="many-harmonic-transfer"></a>
## Several actual w harmonics with one complete error sum

Let a_k(tau) be the k-th Fourier coefficient of theta mapped to psi_tau((1-cos theta)/2).
After translation by pi, the cap is g_tau(t)=(1-sin^2(t/2)/tau)_+.
For 0<tau<=1/64 set

    L_tau=floor(1/(4sqrt(tau)))>=2.

The cap's support is |t|<=2arcsin(sqrt(tau))<=pi sqrt(tau).
For 1<=k<=L_tau, this implies |kt|<=pi/4 on its entire support, hence cos(kt)>=1/2.
On |t|<=sqrt(tau), the cap is at least 3/4.
The imaginary coefficient vanishes by symmetry, and the translation contributes only (-1)^k.
Therefore

    |a_k(tau)|>=3sqrt(tau)/(8pi),
    L_tau sqrt(tau)>=1/8.                                           (15)

For almost every (z,u,v), integrate in the w angle after translation by the phase of V to obtain the exact identity

    Fhat_tau(eta,k)=a_k(tau)(V^k)hat(eta)
                  =a_k(tau)(U^k)hat(-eta).                         (16)

Suppose R,J,L_tau<=M_j and (12) holds with L=L_tau.
Select ALL four-dimensional frequencies

    G={(eta,k): -eta in B_(R,J), 1<=k<=L_tau}.

They lie in [-M_j,M_j]^4.
They have distinct actual circle frequencies H_j(eta,k), because their differences lie in the no-alias 2M_j box.
Every such frequency is positive, since k>=1 and c_j>M_j(1+a_j+b_j).
Thus none is the omitted constant coefficient of W_*.
The total number is at most 4L_tau R^2 J.
Apply C565v2's universal equation (11) to each selected gamma and sum its actual error beta_j/tau.
Equations (14)--(16) now give the finite original-window estimate

    W_*(f_(j,tau))
       >=[3/(8pi)]sqrt(tau)L_tau log(J+1)/16
                       -4L_tau R^2 J beta_j/tau
       >=3log(J+1)/(1024pi)-R^2 J beta_j/tau^(3/2).                  (17)

This is a sum over finite actual positive original-circle frequencies.
There is no exchange of an infinite Fourier series with the moving schedule, no cyclic replacement, and no extra factor of 2 from the unused negative frequencies.

<a id="polynomial-contact-corridor"></a>
## A polynomial shrinking corridor for the unchanged original family

Fix ANY real theta with 0<theta<2/65.
Define

    Delta=1/13-(5/2)theta>0,
    zeta=Delta/10>0, alpha=theta/2+2zeta,
    R_j=floor(M_j^alpha), J_j=floor(M_j^zeta).

For any j and width M_j^-theta<=tau<=1/64, use L_j^*=floor(1/(4sqrt(tau))).
The symbol L_j^* is only the harmonic count and does not replace the original schedule's L_j=K+a_j+b_j+2.
All estimates in this paragraph are uniform over that width strip.
All chosen cutoffs eventually exceed their necessary fixed lower bounds and lie at most M_j, because alpha,zeta,theta/2 are strictly between 0 and 1.
Using floor x>=x/2 for x>=2, the left side of (12) divided by R_j is bounded by a fixed multiple of

    [M_j^(zeta+theta/2-alpha)+M_j^(2zeta-alpha)](1+log M_j)
       =[M_j^-zeta+M_j^(-theta/2)](1+log M_j)->0.                    (18)

Thus (12) holds eventually, uniformly over all the allowed widths at that j.
The original schedule estimate for beta_j gives

    R_j^2 J_j beta_j/tau^(3/2)
       =O_K(M_j^(2alpha+zeta+(3/2)theta-1/13)(1+log M_j)^(1/13))
       =O_K(M_j^(-Delta/2)(1+log M_j)^(1/13))->0.                   (19)

Every selected coefficient is included in this price.
Since J_j+1>M_j^zeta, (17) proves

    W_*(psi_tau(k_j))
       >=[3zeta/(1024pi)]log M_j-o(1).                             (20)

There is a j0(theta,K) after which (18)--(20) hold for every width M_j^-theta<=tau<=1/64, with a uniform error bounded as in (19).
Every sequence tau_j->0 satisfying tau_j>=M_j^-theta eventually enters this strip, but the index of entry may depend on that sequence.
Its norms therefore tend to infinity.
For a concrete example theta=1/100 is permitted, so the conclusion includes tau_j=M_j^-1/100 and every eventually larger shrinking width.
This improves the earlier sufficient corridor tau_j(log M_j)^2->infinity, which does not include a negative fixed power of M_j.
The complete original 2d_j coordinate window and actual contact-minus-Haar margin at least 1/2 are unchanged.
The positive total-measure range log 2<m(P_j)<log 4 is also unchanged.
Neither the arbitrary simultaneous thin corridor nor any near-one family or unrestricted Mahler gap is established.
Widths below all the displayed power corridors remain unclassified by this argument.


<a id="witness-specific-anisotropic-refinement"></a>
## Exact witness derivative and unequal coordinate cutoffs

The coordinating agent supplied the following refinement of the already fixed witness calculation.
The contributor checked the elementary integral, the fixed-interval derivative, the complete product-convolution split and all cutoffs before registration.
No external convolution theorem is used.

For every real d, define

    I(d)=(1/pi) integral_R dt/[(1+t^2)(1+(t-d)^2)].

The exact value is

    I(d)=2/(d^2+4).                                                 (21)

For d!=0 set B=1/(d^2+4) and A=2/[d(d^2+4)].
Multiplying denominators shows the exact partial-fraction identity

    1/[(1+t^2)(1+(t-d)^2)]
       =(A t+B)/(t^2+1)+[-A(t-d)+B]/[(t-d)^2+1].                  (22)

In fact the coefficients of t^2 and t cancel, and the remaining numerator is B(d^2+4)=1.
The linear terms are not integrated separately as absolutely convergent integrals.
Integrating their paired sum on [-T,T] gives logarithmic boundary differences tending to zero as T tends to infinity.
The two constant terms each integrate to pi B, including the shifted one.
This proves (21) for d!=0.
For d=0 the antiderivative t/[2(1+t^2)]+arctan(t)/2 gives total integral pi/2, and hence I(0)=1/2 as required.

Under normalized v-circle Haar measure, t=cot(arg(v)/2) has density 1/[pi(1+t^2)].
This follows directly by substituting the angle in (0,2pi): dt/darg(v)=-(1+t^2)/2, and the orientation reverses the endpoints.
For regular v, C(v)=-it and D=id, so the earlier exact Cayley derivative and |U|=1 give

    |partial_D U^k|=2k/[1+(d-t)^2],
    average_v |partial_D U^k|=2k I(d)=4k/(d^2+4).                   (23)

These identities include every k>=1.
The earlier uniform bound 2k on |partial_D U^k| justifies differentiating the actual negative-v coefficient under the integral; the integrable character has modulus one.
No unproved regularity at the exceptional v=1 point is needed.

Choose the positive witness d(z_0)=+4sqrt(km).
This choice has the same |D|^2=16km as in equations (2)--(5), so the amplitude 1/(8m) remains valid.
On I, the actual fixed K>=4 gives

    |D_0(z)-D_0(z_0)|<=(K+4)delta<=pi/2,
    d(z)>=4sqrt(km)-pi/2>=2sqrt(km).

The last inequality uses sqrt(km)>=1 and pi<4.
Consequently (23) and |partial_arg(z) D_0|<=K+4 prove, at the same fixed u_(k,m) throughout I,

    |partial_arg(z) F_(k,m)(z,u_(k,m))|
       <=4k(K+4)/(d(z)^2+4)<=(K+4)/m.                             (24)

This is a neighborhood bound, not just the derivative at the witness point.
It does not replace the global almost-everywhere modulus bound outside I.
The old bound |partial_arg(u) F_(k,m)|<=8192(k+m) holds throughout I and for every u, as proved in (8).

Take the probability-Haar product Fejer convolution with z cutoff R_z>=2 and u cutoff R_u>=2.
Evaluate it at (z_0,u_(k,m)), and denote its value by P_(R_z,R_u,k,m).
For z displacement |s|<=delta, split the integrand difference exactly as

    F(z_0 exp(-is),u_(k,m) exp(-it))-F(z_0,u_(k,m))
      =[F(z_0 exp(-is),u_(k,m) exp(-it))-F(z_0 exp(-is),u_(k,m))]
       +[F(z_0 exp(-is),u_(k,m))-F(z_0,u_(k,m))].

The first bracket is bounded by 8192(k+m)|t| along the shortest u-circle arc.
The second is bounded by (K+4)|s|/m from (24).
For |s|>delta, bound the unsplit difference by 2 using the global almost-everywhere bound |F|<=1.
Integrating against the product kernels, using their normalization, and enlarging the two nonnegative local moment integrals to full-circle moments gives

    |P_(R_z,R_u,k,m)-F_(k,m)(z_0,u_(k,m))|
       <=8192pi(k+m)(1/2+log R_u)/R_u
          +pi(K+4)(1/2+log R_z)/(m R_z)
          +2pi/(R_z delta).                                       (25)

No u derivative is used in the exceptional z region.
The periodic rational formula handles an arc wrapping through u=1, and the ignored measure-zero original phase set changes no Fourier coefficient or convolution.

Multiplying (25) by m and maximizing over 1<=k<=L,1<=m<=J gives the explicit upper bound T_K in the statement.
Therefore T_K<=1/16 leaves at least 1/(16m) of the amplitude 1/(8m).
Each product Fejer coefficient multiplier lies in [0,1].
The convolution value is consequently at most the absolute coefficient sum over |p|<=R_z-1,|q|<=R_u-1.
Summing over all 1<=m<=J proves (D), using exactly the same harmonic comparison as (14).

For the original-kernel return, select all four-dimensional frequencies

    G_prime={(eta,k): -eta=(p,q,-m),
             |p|<=R_z-1, |q|<=R_u-1, 1<=m<=J, 1<=k<=L_tau}.

When R_z,R_u,J,L_tau<=M_j, these lie in the exact comparison box.
Their differences lie in its 2M_j difference box, so they have distinct actual original-circle frequencies.
Every such frequency is positive by c_j>M_j(1+a_j+b_j) and k>=1.
Thus none is the constant coefficient omitted from W_*.
There are at most 4L_tau R_z R_u J selected coefficients.
Using (15)--(16), (D), the universal beta_j/tau comparison, L_tau sqrt(tau)>=1/8 and 4L_tau<=1/sqrt(tau) gives

    W_*(psi_tau(k_j))
       >=3log(J+1)/(1024pi)-R_z R_u J beta_j/tau^(3/2),             (26)

which is (E).
Every term in this finite rectangular support has been paid.

<a id="anisotropic-uniform-strip"></a>
## Uniform strip with every exponent below 1/26

Fix 0<theta_prime<1/26 and the positive Delta_prime,zeta_prime from the statement.
For the following choices the symbols Q_z,j,Q_u,j are scalar Fourier cutoffs and are distinct from the original residual projection R_j:

    Q_z,j=floor(M_j^(2zeta_prime)),
    Q_u,j=floor(M_j^(theta_prime/2+2zeta_prime)),
    J_prime,j=floor(M_j^zeta_prime).                               (27)

Use R_z=Q_z,j, R_u=Q_u,j, J=J_prime,j and L=L_tau.
For every width M_j^-theta_prime<=tau<=1/64, one has L_tau<=M_j^(theta_prime/2)/4.
All cutoff exponents are positive and less than one, so the Fourier cutoffs eventually meet their fixed lower bounds and are all at most M_j.
The harmonic count is already at least two because tau<=1/64.

Using floor x>=x/2 for x>=2, the three terms of T_K are bounded, uniformly over the permitted width strip, by fixed multiples of

    [M_j^-zeta_prime+M_j^(-theta_prime/2)](1+log M_j),
    M_j^(-2zeta_prime)(1+log M_j),
    M_j^-zeta_prime,                                               (28)

respectively.
For the first expression, the exponents are
zeta_prime+theta_prime/2-(theta_prime/2+2zeta_prime)=-zeta_prime and
2zeta_prime-(theta_prime/2+2zeta_prime)=-theta_prime/2.
Each expression tends to zero.
Hence T_K<=1/16 beyond a threshold depending only on theta_prime,K, uniformly for every width in the strip.

The complete selected coefficient error in (26) is at most

    Q_z,j Q_u,j J_prime,j beta_j/tau^(3/2)
       =O_K(M_j^(2theta_prime+5zeta_prime-1/13)
                  (1+log M_j)^(1/13))
       =O_K(M_j^(-Delta_prime/2)(1+log M_j)^(1/13)).                (29)

The equality of exponents follows from 2theta_prime-1/13=-Delta_prime and 5zeta_prime=Delta_prime/2.
The original beta_j constant is independent of tau.
Finally J_prime,j+1>M_j^zeta_prime.
Inserting these estimates into (26) proves (F) with an actual uniform j1,C1 depending only on theta_prime,K.

Any stated sequence tau_j->0 eventually enters the upper cutoff 1/64, and its lower inequality is assumed only eventually.
After that possibly sequence-dependent entry index, the fixed uniform estimate applies and tends to infinity.
The example theta_prime=1/30 satisfies 2/65<1/30<1/26.
No general quantitative thin-peak theorem, new source input, numerical approximation or change to the original arithmetic family is used in this refinement.


<a id="balanced-original-return-consumer"></a>
## The improved original-return input and a balanced rho choice

The complete fixed C632v1 argument was read as a mathematical input before this consumer was prepared.
It uses the same K, arithmetic schedule, full 2d_j kernel, Acal,Bcal, inverse phase, probability Haar conventions and finite box.
Its independent-product comparison is confined to the actual product three-torus.
Its original-circle return is obtained by the finite no-alias polynomial comparison with all errors paid; independence of pushed-circle coordinates is not assumed.
The consumer does not change any of those objects or infer control of an infinite Fourier series.

Specifically, [C632v1 (PR4)](Yin_C_G0632_v1.md#improved-universal-coefficient-return) gives, for every original j with M_j>=2, every 0<tau<=1, every 0<rho<=1 and every integer gamma in [-M_j,M_j]^4,

    |fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma)|
       <=[epsilon_j+12sqrt(rho)[1+log(1/rho)]^2
                      +3D_reg,K omega_j/sqrt(rho)]/tau.           (30)

The constant D_reg,K is computed from the same original phase polynomial derivatives as stated above.
The complete C632 proof supplies its product sublevel/shell estimate, amplitude-sensitive derivative bound, all four-coordinate regularized Fejer errors and original comparison.
Those inspected fixed results are accepted dependencies, not results reconstructed from an author summary or a new source-law substitution.

The choice rho=omega_j gives the stated beta_new,j.
For the second choice, 0<omega_j<1 follows from 1+log M_j<M_j for M_j>1.
Put hlog_j=1+log(1/omega_j)>=1 and rho_opt,j=omega_j/hlog_j^2.
This is a legal rho in (0,1], and

    1+log(1/rho_opt,j)=hlog_j+2log(hlog_j)<=2hlog_j.                (31)

For completeness, x/2-log x has its minimum at x=2 and the minimum is 1-log 2>0.
Therefore 2log x<=x for every x>0, in particular at x=hlog_j.
Substitution into (30) proves that beta_opt,j is an actual error budget and gives

    12sqrt(rho_opt,j)[1+log(1/rho_opt,j)]^2
       <=48sqrt(omega_j)hlog_j,
    3D_reg,K omega_j/sqrt(rho_opt,j)
       =3D_reg,K sqrt(omega_j)hlog_j.                              (32)

These inequalities establish the first beta_opt bound in (G).
Moreover hlog_j=1+log M_j-log(1+log M_j)<=1+log M_j.
Thus sqrt(omega_j)hlog_j<=M_j^-1/2(1+log M_j)^(3/2).
The original epsilon_j=O_K((1+log M_j)/M_j^2) is smaller than that scale for large j.
This proves the beta_opt asymptotic in (G), while C632 (PR5) gives the beta_new asymptotic.
No pointwise comparison beta_opt,j<=beta_new,j is needed or asserted.
No claim of an optimal rho or optimal rate is made.

<a id="sharper-budget-finite-support"></a>
## The same full finite support with the new budgets

Under the unchanged condition T_K<=1/16, the complete coefficient lower bound (D) holds for every 1<=k<=L_tau.
The set G_prime used for (26) has at most 4L_tau R_z R_u J elements, all inside the very same box in (30).
Its frequencies H_j(eta,k) are still distinct and strictly positive by the exact old alias proof.
The scalar coefficients and inverse phase still satisfy (15)--(16).
Consequently the triangle inequality for each selected actual coefficient, summed over this entire set, now gives, for either selected budget_j,

    W_*(psi_tau(k_j))
       >=[3/(8pi)]sqrt(tau)L_tau log(J+1)/16
          -4L_tau R_z R_u J budget_j/tau
       >=3log(J+1)/(1024pi)
          -R_z R_u J budget_j/tau^(3/2).                           (33)

The two budgets are substituted into a full-function coefficient comparison valid on that box.
They do not alter the selected support or remove any of its coefficients.
No extra factor is gained from negative original frequencies, and no individual error is omitted.
This proves (H).

<a id="quarter-exponent-uniform-strip"></a>
## Uniform strip with every exponent below one quarter

Fix 0<theta_new<1/4, Delta_new=1/2-2theta_new>0 and zeta_new=Delta_new/10.
Take the scalar Fourier cutoffs

    Q_z,new,j=floor(M_j^(2zeta_new)),
    Q_u,new,j=floor(M_j^(theta_new/2+2zeta_new)),
    J_new,j=floor(M_j^zeta_new),

and set R_z=Q_z,new,j, R_u=Q_u,new,j, J=J_new,j.
These do not rename the original residual projection R_j.
Uniformly over M_j^-theta_new<=tau<=1/64, use the same L_tau=floor(1/(4sqrt(tau))).
The bound L_tau<=M_j^(theta_new/2)/4 remains valid.

All exponents 2zeta_new, theta_new/2+2zeta_new, zeta_new and theta_new/2 are strictly between zero and one.
In particular theta_new/2+2zeta_new=1/10+theta_new/10<1.
The cutoffs eventually exceed their required fixed lower bounds and lie at most M_j.
Applying floor x>=x/2 for x>=2, the three terms in T_K are bounded by fixed multiples of

    [M_j^-zeta_new+M_j^(-theta_new/2)](1+log M_j),
    M_j^(-2zeta_new)(1+log M_j),
    M_j^-zeta_new,

respectively.
The exponents arise from the same exact differences as in (28), with the new positive parameters.
All expressions tend to zero.
Thus a threshold depending only on theta_new,K supplies the finite condition and the entire box containment uniformly over the permitted strip.

Use beta_opt,j in (33).
The complete selected error satisfies

    Q_z,new,j Q_u,new,j J_new,j beta_opt,j/tau^(3/2)
       =O_K(M_j^(2theta_new+5zeta_new-1/2)
                    (1+log M_j)^(3/2))
       =O_K(M_j^(-Delta_new/2)(1+log M_j)^(3/2)).                   (34)

Indeed 2theta_new-1/2=-Delta_new and 5zeta_new=Delta_new/2.
All numerator floors only reduce this error, and the beta_opt constant is independent of tau.
The harmonic main term obeys log(J_new,j+1)>zeta_new log M_j.
Equations (33)--(34) therefore give actual constants j2,C2 depending only on theta_new,K and prove (I) for every j>=j2 and every width in the stated strip.

A shrinking sequence with the lower inequality eventually enters the upper cutoff at its own eventual index.
The same uniform estimate then applies and its positive logarithmic term diverges while the error tends to zero.
The example theta_new=1/8 is strictly between 1/26 and 1/4.
The power boundary 1/4 belongs only to these sufficient estimates.
At its endpoint Delta_new and the chosen logarithmic-mass cutoff exponent vanish, so this fixed-power argument makes no endpoint conclusion.


<a id="general-paid-budget-interface"></a>
## General finite return under an explicit actual-box budget

Assume exactly premise (J), with the same original functions and frequency map.
For any j>=j_budget, 0<tau<=1/64 and cutoffs satisfying T_K<=1/16 and R_z,R_u,J,L_tau<=M_j, the coefficient lower bounds, scalar harmonic identity and frequency selection in (33) are unchanged.
Every selected frequency belongs to the box quantified in (J), and the number of selected coefficients is at most 4L_tau R_z R_u J.
Applying (J) to each of them gives

    W_*(psi_tau(k_j))
       >=3log(J+1)/(1024pi)
          -R_z R_u J mathcal_B_j/tau^(3/2).                        (35)

This follows by exactly the displayed finite triangle inequality in (33), with mathcal_B_j replacing its selected budget.
The distinct positive actual frequencies, omission of the constant mode, original inverse phase and coefficient count have all already been established for this same selection.
No new support optimization, negative-frequency factor or infinite-series conclusion is introduced.
In particular, (35) is conditional on the actual uniform all-box error in (J), not merely on a numerical upper bound assigned to a formal sequence.

<a id="critical-power-logarithmic-consumer"></a>
## Every allowed critical-power logarithmic strip

Fix 0<b_decay<4, p_log>=0 and a_log>(p_log+1)/2.
Let eps_log=a_log-(p_log+1)/2 and r_log=eps_log/5, both positive.
For sufficiently large j write T_j=log M_j>1 and choose

    J_crit,j=floor(T_j^r_log),
    Q_z,crit,j=floor(T_j^(2r_log)),
    Q_u,crit,j=floor(M_j^(b_decay/4)
                         T_j^(2r_log+1-a_log/2)).                 (36)

The Q symbols are scalar Fourier cutoffs and do not rename the residual projection R_j.
Take J=J_crit,j,R_z=Q_z,crit,j,R_u=Q_u,crit,j and L=L_tau.
For every width in the strip of (K),

    L_tau<=M_j^(b_decay/4)T_j^(-a_log/2)/4.                        (37)

The lower width M_j^(-b_decay/2)T_j^a_log tends to zero since b_decay>0.
Thus the strip is nonempty eventually.
Every power of T_j grows more slowly than every fixed positive power of M_j; for this use, take logarithms and use log T_j/T_j->0.
It follows from 0<b_decay/4<1 that all four coordinate cutoffs are at most M_j eventually.
Also J_crit,j and Q_z,crit,j tend to infinity.
The u cutoff tends to infinity even when 2r_log+1-a_log/2 is negative, because its positive power M_j^(b_decay/4) dominates that logarithmic factor.
Hence all fixed lower cutoff requirements eventually hold, and the floor inequality floor x>=x/2 applies to each denominator.
The harmonic count is already at least two throughout tau<=1/64.

Moreover log Q_u,crit,j=O(T_j), with a constant depending only on the displayed fixed exponents.
The first term of T_K, after inserting (36)--(37) and the floor lower bound, is bounded by a fixed multiple of

    [J_crit,j(L_tau+J_crit,j)(1+log Q_u,crit,j)]/Q_u,crit,j
       <=C[T_j^-r_log+M_j^(-b_decay/4)T_j^(a_log/2)].              (38)

Indeed the J_crit,j L_tau summand has logarithmic exponent
r_log-a_log/2+1-(2r_log+1-a_log/2)=-r_log.
The J_crit,j^2 summand has logarithmic exponent
2r_log+1-(2r_log+1-a_log/2)=a_log/2 and retains M_j^(-b_decay/4).
Both terms tend to zero.
The second and third terms of T_K are bounded respectively by fixed multiples of

    (1+log T_j)/T_j^(2r_log), T_j^-r_log.                           (39)

They also tend to zero.
Consequently the full finite condition T_K<=1/16 and actual box containment hold beyond a threshold independent of the chosen width in the strip.

Use the premise mathcal_B_j<=C_budget M_j^-b_decay(1+T_j)^p_log.
For T_j>=1, (1+T_j)^p_log<=2^p_log T_j^p_log, with p_log>=0.
All numerator floors reduce the support upper bound.
The complete error in (35) is therefore bounded by a fixed multiple of

    M_j^(b_decay/4-b_decay+3b_decay/4)
       T_j^(2r_log+(2r_log+1-a_log/2)+r_log
                              +p_log-3a_log/2)
      =T_j^(5r_log+1+p_log-2a_log)
      =T_j^-eps_log.                                              (40)

The M_j powers cancel exactly.
The logarithmic equality uses 1+p_log-2a_log=-2eps_log and 5r_log=eps_log.
Every factor in this error is the actual selected-support price; none is replaced by an asymptotic sparsity claim.

Finally J_crit,j+1>T_j^r_log, hence

    log(J_crit,j+1)>r_log log T_j=r_log loglog M_j.                 (41)

Insert (40)--(41) into (35).
This proves (K) with actual constants j3,C3 depending only on the fixed parameters, budget constant and budget starting index stated there.
Within the strip, the positive loglog M_j term tends to infinity and the error tends to zero.
An eventually admitted sequence therefore has diverging actual Wiener norms, with no uniform assertion about when an arbitrary sequence first enters the strip.
No source theorem beyond the retained finite argument is required for the cutoff and exponent calculations.

<a id="actual-square-root-critical-corridor"></a>
## The adopted square-root-budget application

The exact beta_opt,j from (G) is nonnegative, independent of tau and gamma, and bounds the original coefficient error for every gamma in the same box and every 0<tau<=1.
The complete accepted C632 input and the balancing proof (30)--(32) establish

    beta_opt,j<=C_budget,K M_j^-1/2(1+log M_j)^(3/2)

for all sufficiently large j, with the positive constant C_budget,K and onset depending only on the original fixed K.
This budget constant is distinct from the previously fixed derivative constant C_K=10000(K+1).
Thus premise (J) holds for the actual original functions with

    mathcal_B_j=beta_opt,j, b_decay=1/2, p_log=3/2.                 (42)

No better coefficient-rate premise is assumed.
The general logarithmic threshold is then (p_log+1)/2=5/4, and b_decay/2=1/4.
Substituting these exact values into (K) proves (L), including its constants depending only on K,a_log.

For each fixed a_log>5/4, the lower-bound sequence M_j^-1/4(log M_j)^a_log tends to zero and is eventually at most 1/64.
It is therefore an actual allowed sequence.
For any fixed theta<1/4, its ratio to M_j^-theta is
M_j^(-(1/4-theta))(log M_j)^a_log, which tends to zero.
Hence (L) covers a narrower actual-width corridor than every fixed exponent in (I).
The example a_log=3/2 satisfies the required strict inequality.
At a_log=5/4 this choice gives eps_log=r_log=0 and no growing band count, so no equality-case conclusion is supplied.
The unmodified critical width corresponds to a_log=0 and is likewise outside this actual application.

The original k_j, P_j, rank, full coefficient dimension, probability measure and contact interpretation have not been changed.
C174's fixed-j finiteness and actual contact-minus-Haar bound remain valid.
The total Mahler range log 2<m(P_j)<log 4 remains the same.
This is a conditional general finite-budget theorem with a separately discharged actual instance; it does not solve arbitrary simultaneous thin widths or the unrestricted G0001 Task.

<a id="many-phase-remaining"></a>
## Remaining work and method limits

The direct estimate has a threshold only for this proof's selected support and error budget.
None of the sufficient exponent or logarithmic thresholds is asserted to be a physical transition or to give bounded actual Wiener norms outside its proved strip.
The fixed-input very thin theorem of C174 retains its separate order of limits.
The current proof uses the individual coefficient error and does not claim the optimized finite Bessel error for this multiband selection.
The predecessor whole reviews apply only to their exact fixed versions.
New independent whole review of this physical version, including the complete retained chain and new (35)--(42) with statements (J)--(L), remains outstanding at initial registration.

## Assessment history

### Decision critical-log-budget-notation-registration

| Field | Value |
| --- | --- |
| date | 2026-10-23T20:05 |
| status | open |
| reason | Disambiguate the application budget constant C_budget,K from the earlier fixed derivative constant C_K, preserving v5 and its unchanged theorem/rate. Retain the complete adopted v4 mathematics and prove a general conditional critical-power/logarithmic corridor under an explicit uniform original-four-box coefficient budget. Its exact adopted square-root-budget instance gives every a_log>5/4 at width M_j^-1/4(log M_j)^a_log, with a uniform loglog lower bound and fully paid error. The physical version awaits new independent whole review; no unregistered rate or pure critical-width endpoint is used. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire expanded statement](#statement) | Complete retained (A)--(I), explicit quantified actual-box budget premise (J), every 0<b_decay<4,p_log>=0,a_log>(p_log+1)/2 conclusion (K), actual square-root application (L), all source, original-family, sequence-entry and equality-case boundaries. |
| argument | [Entire complete argument](#argument) | Complete retained (1)--(34), general finite triangle inequality (35), every mixed-power/log cutoff and box condition (36)--(39), full cost and harmonic mass (40)--(41), and discharged actual budget (42). |
| dependency | [Adopted complete predecessor](Yin_C_G0629_v4.md#argument) | Exact original phase, power coefficients, derivative and anisotropic cutoff estimates, original frequency selection, legal budgets and balancing proof retained in full; predecessor review is not upgraded. |
| dependency | [Improved all-rho original return](Yin_C_G0632_v1.md#improved-universal-coefficient-return) | Exact adopted PR4 on the same original family, every legal rho,tau and entire four-box, used to discharge the actual square-root application only. |
| dependency | [Improved original polynomial constants](Yin_C_G0632_v1.md#square-root-regularization-derivative) | Exact A_der,K,D_reg,K and complete amplitude-sensitive derivative constants used in the actual budget. |
| dependency | [C565v2 original return](Yin_C_G0565_v2.md#moving-band-fejer-budget) | Older universal error retained for earlier fixed conclusions, with the same original 2d kernel and normalization. |
| dependency | [C565v2 exact aliases](Yin_C_G0565_v2.md#moving-band-exact-alias) | Full difference-box injectivity, original frequency positivity and exact finite coefficient comparison, including the new logarithmic cutoffs. |
| dependency | [C569v2 exact phase](Yin_C_G0569_v2.md#static-phase-geometric-band) | Exact actual phase and geometric expansion retained by the complete earlier argument. |
| dependency | [C569v2 local domain](Yin_C_G0569_v2.md#static-phase-local-derivatives) | Fixed actual interval and D0/rational-coordinate bounds, with the full local refinement retained. |
| dependency | [C569v2 Fejer inputs](Yin_C_G0569_v2.md#static-phase-finite-support) | Normalized moments, global tail and finite coefficient multipliers, with every selected coefficient counted. |
| dependency | [C569v2 schedule costs](Yin_C_G0569_v2.md#static-phase-original-return) | Original epsilon_j and older budget asymptotics, from the unchanged lower prime separations. |
| dependency | [C174 original contacts](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Actual fixed-j finite norms, margin at least 1/2 and preserved order of thin limits. |
| dependency | [Accepted Deb15 interface](#many-phase-reuse) | Actual retained source statement checks and pole-free rational applicability, without any source-proof upgrade. |
| support | [GMR18 attribution](../audits/literature/GMR18/Yin_U001.md#gmr18-u001) | Existing finite-Blaschke attribution and unchanged historical source/review limits. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T20:14 |
| status | proved |
| reason | Adopt the whole physicalv6 after main reading of its complete additions, exact comparison with already read v4, and whole independent R839. The general all-box conditional premise and all mixed-power/logarithmic cutoffs pay every support cost; the actual adopted square-root budget discharges the instance a_log>5/4. Retained versions, source limits, full original2d normalization and uniform-strip versus sequence-entry quantifiers remain exact. Neither the equality case nor unmodified critical width or unrestricted Task completion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire expanded statement](#statement) | Complete retained (A)--(I), explicit quantified actual-box budget premise (J), every 0<b_decay<4,p_log>=0,a_log>(p_log+1)/2 conclusion (K), actual square-root application (L), all source, original-family, sequence-entry and equality-case boundaries. |
| argument | [Entire complete argument](#argument) | Complete retained (1)--(34), general finite triangle inequality (35), every mixed-power/log cutoff and box condition (36)--(39), full cost and harmonic mass (40)--(41), and discharged actual budget (42). |
| dependency | [Adopted complete predecessor](Yin_C_G0629_v4.md#argument) | Exact original phase, power coefficients, derivative and anisotropic cutoff estimates, original frequency selection, legal budgets and balancing proof retained in full; predecessor review is not upgraded. |
| dependency | [Improved all-rho original return](Yin_C_G0632_v1.md#improved-universal-coefficient-return) | Exact adopted PR4 on the same original family, every legal rho,tau and entire four-box, used to discharge the actual square-root application only. |
| dependency | [Improved original polynomial constants](Yin_C_G0632_v1.md#square-root-regularization-derivative) | Exact A_der,K,D_reg,K and complete amplitude-sensitive derivative constants used in the actual budget. |
| dependency | [C565v2 original return](Yin_C_G0565_v2.md#moving-band-fejer-budget) | Older universal error retained for earlier fixed conclusions, with the same original 2d kernel and normalization. |
| dependency | [C565v2 exact aliases](Yin_C_G0565_v2.md#moving-band-exact-alias) | Full difference-box injectivity, original frequency positivity and exact finite coefficient comparison, including the new logarithmic cutoffs. |
| dependency | [C569v2 exact phase](Yin_C_G0569_v2.md#static-phase-geometric-band) | Exact actual phase and geometric expansion retained by the complete earlier argument. |
| dependency | [C569v2 local domain](Yin_C_G0569_v2.md#static-phase-local-derivatives) | Fixed actual interval and D0/rational-coordinate bounds, with the full local refinement retained. |
| dependency | [C569v2 Fejer inputs](Yin_C_G0569_v2.md#static-phase-finite-support) | Normalized moments, global tail and finite coefficient multipliers, with every selected coefficient counted. |
| dependency | [C569v2 schedule costs](Yin_C_G0569_v2.md#static-phase-original-return) | Original epsilon_j and older budget asymptotics, from the unchanged lower prime separations. |
| dependency | [C174 original contacts](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Actual fixed-j finite norms, margin at least 1/2 and preserved order of thin limits. |
| dependency | [Accepted Deb15 interface](#many-phase-reuse) | Actual retained source statement checks and pole-free rational applicability, without any source-proof upgrade. |
| support | [GMR18 attribution](../audits/literature/GMR18/Yin_U001.md#gmr18-u001) | Existing finite-Blaschke attribution and unchanged historical source/review limits. |
| review | [Independent whole critical-log finding](../audits/reviews/Yin_R_G0839_v1.md#whole-critical-log-finding) | Entire physicalv6 retained and new mathematics, exact unchanged-v4 comparison, full C632 reread, all (J)--(L) and (35)--(42), negative-log-exponent cutoffs, complete support cancellation and actual budget discharge; every previous review remains at its original scope. |


---
author: Yin
---

# Many phase bands force divergence throughout a polynomial shrinking contact corridor

This is a joint project deduction by the coordinating agent and the phase_bands contributor for Yin under the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
The exact author argument is registered open pending independent whole review.
No new arithmetic input family, numerical scan or computation group is selected.

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

For EVERY sequence tau_j->0 with tau_j>=M_j^-theta eventually, one has

    W_*(psi_(tau_j)(k_j))
       >=[3zeta/(1024pi)]log M_j-o(1)->infinity.                    (B)

The o(1) is bounded by a fixed multiple of M_j^(-Delta/2)(1+log M_j)^(1/13), uniformly over the allowed widths once the fixed cutoffs apply.
For example (B) covers tau_j=M_j^-1/100 and every eventually larger shrinking width.
All these original contact transforms retain their actual contact-minus-Haar margin at least 1/2 and finite Wiener norms at each fixed j,tau.
The positive total-measure range log 2<m(P_j)<log 4 is unchanged.
No arbitrary simultaneous thin-corridor theorem, near-one family or unrestricted Mahler-gap conclusion is asserted.
The exponent 2/65 is a sufficient boundary of these estimates, not a necessary threshold for actual divergence.

## Current assessment

[Selected decision](#decision-many-phase-registration)

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

For EVERY sequence tau_j->0 satisfying tau_j>=M_j^-theta for all sufficiently large j, use L_j^*=floor(1/(4sqrt(tau_j))).
The symbol L_j^* is only the harmonic count and does not replace the original schedule's L_j=K+a_j+b_j+2.
All chosen cutoffs eventually exceed their necessary fixed lower bounds and lie at most M_j, because alpha,zeta,theta/2 are strictly between 0 and 1.
Using floor x>=x/2 for x>=2, the left side of (12) divided by R_j is bounded by a fixed multiple of

    [M_j^(zeta+theta/2-alpha)+M_j^(2zeta-alpha)](1+log M_j)
       =[M_j^-zeta+M_j^(-theta/2)](1+log M_j)->0.                    (18)

Thus (12) holds eventually, uniformly over all the allowed widths at that j.
The original schedule estimate for beta_j gives

    R_j^2 J_j beta_j/tau_j^(3/2)
       =O_K(M_j^(2alpha+zeta+(3/2)theta-1/13)(1+log M_j)^(1/13))
       =O_K(M_j^(-Delta/2)(1+log M_j)^(1/13))->0.                   (19)

Every selected coefficient is included in this price.
Since J_j+1>M_j^zeta, (17) proves

    W_*(psi_(tau_j)(k_j))
       >=[3zeta/(1024pi)]log M_j-o(1)->infinity.                    (20)

The constants and onset may depend on the fixed theta and K, but not on the particular allowed width sequence.
For a concrete example theta=1/100 is permitted, so the conclusion includes tau_j=M_j^-1/100 and every eventually larger shrinking width.
This improves the earlier sufficient corridor tau_j(log M_j)^2->infinity, which does not include a negative fixed power of M_j.
The complete original 2d_j coordinate window and actual contact-minus-Haar margin at least 1/2 are unchanged.
The positive total-measure range log 2<m(P_j)<log 4 is also unchanged.
Neither the arbitrary simultaneous thin corridor nor any near-one family or unrestricted Mahler gap is established.
Widths below all the displayed power corridors remain unclassified by this argument.

<a id="many-phase-remaining"></a>
## Remaining work and method limits

The direct estimate has a threshold only for this proof's selected support and error budget.
It does not assert a physical transition at exponent 2/65 or bounded actual Wiener norms for smaller widths.
The fixed-input very thin theorem of C174 retains its separate order of limits.
The current proof uses the individual coefficient error and does not claim the optimized finite Bessel error for this multiband selection.
Independent whole review of the new coefficient, derivative, simultaneous-band and exponent calculations remains outstanding at initial registration.


## Assessment history

### Decision many-phase-registration

| Field | Value |
| --- | --- |
| date | 2026-10-23T19:30 |
| status | open |
| reason | Register the complete actual power-coefficient, rational-derivative, finite many-harmonic transfer and polynomial shrinking-width argument for independent whole review. The exact original Salem family, full 2d coefficient window, contact margin and every support/error cost are preserved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | All positive k,m witnesses, uniform local derivatives, every finite cutoff and actual multiband bound, every fixed 0<theta<2/65 and all allowed shrinking widths, with original-family and unresolved-corridor limits. |
| argument | [Entire complete argument](#argument) | Full exact coefficient expansion, witness/tail calculation, elementary rational comparison, classical source interface, Fejer cutoff, inverse phase, aliases, cap coefficients, total support price and exponent/floor calculation. |
| dependency | [C565v2 universal return](Yin_C_G0565_v2.md#moving-band-fejer-budget) | Equation (11) for every gamma in the entire four-dimensional box, with complete original 2d comparison and beta_j/tau cost. |
| dependency | [C565v2 exact aliases](Yin_C_G0565_v2.md#moving-band-exact-alias) | Nonzero H_j on all nonzero differences in the 2M_j box and positive selected original frequencies; no infinite-series substitution. |
| dependency | [C569v2 rational phase](Yin_C_G0569_v2.md#static-phase-geometric-band) | Exact geometric expansion, actual z0 and full original phase; powers and uniform coefficient witnesses are proved here. |
| dependency | [C569v2 local domain](Yin_C_G0569_v2.md#static-phase-local-derivatives) | Fixed z interval, D0 bounds and nonsingular rational u coordinates; new power derivative estimate proved here. |
| dependency | [C569v2 finite Fejer input](Yin_C_G0569_v2.md#static-phase-finite-support) | Normalized first moment and global-tail bounds, used with all selected rectangular coefficients. |
| dependency | [C569v2 schedule cost](Yin_C_G0569_v2.md#static-phase-original-return) | beta_j asymptotic from the unchanged original prime schedule, without any upper prime-gap estimate. |
| dependency | [C174 exact contact scope](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Each finite original Wiener norm and actual margin at least 1/2; no exchange of its fixed-input thin limit. |
| dependency | [Accepted Deb15 interface](#many-phase-reuse) | Actually inspected retained author notes, printed/PDF pp10--12 and24: disk Cauchy derivative bound and maximum-modulus principle, matched to the pole-free rational functions, with original proof-depth limits. |
| support | [GMR18 attribution](../audits/literature/GMR18/Yin_U001.md#gmr18-u001) | Existing finite-Blaschke normalization/derivative attribution only, not a source assertion of the new rational derivative estimate or corridor. |

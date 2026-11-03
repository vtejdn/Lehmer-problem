---
author: Yin
---

# Contact-aligned discrete Fejer return and logarithm-free critical enlargement

Human author Yin.
Root supplied the signed rational-phase energy, aligned discrete interpolation and contact-adapted cap comparison.
The phase_bands contributor checked and completed the phase orientation, two-sided energy normalization, quadrature, missing sample, full original2d costs, finite support and both actual-degree consumers.
Both are contributors, not independent reviewers.
The square and25/11-separated schedules below are two distinct actual polynomial families.
No numerical experiment, prime enumeration, new external acquisition or original-source proof upgrade is used.

## Statement

Fix the same even integer

    K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))).

For every integer j>=1 set

    a_j=min{p prime:p>(j+1)K},
    b_j=min{p prime:p>(K+a_j+3)^2},
    L_j=K+a_j+b_j+2, M_j=floor(a_j/4).

Use TWO separately named choices of the last exponent:

    c_j^square=min{p prime:p>(L_j+1)^2},
    n_j=min{N positive integer:N^11>=(L_j+1)^25},
    c_j^balanced=min{p prime:p>n_j}.

The second threshold is exactly n_j=ceil((L_j+1)^(25/11)).
For sigma in{square,balanced}, put ell^sigma=(K,a_j,b_j,c_j^sigma) and

    Qraw_j^sigma(x)=(x^2-1)product_(i=0)^3(x^ell_i^sigma-1)
       -(x/2)sum_(q=0)^3(x^ell_q^sigma+1)product_(i!=q)(x^ell_i^sigma-1),
    P_j^sigma=Qraw_j^sigma/(x-1)^3,
    d_j^sigma=c_j^sigma+L_j-3.

These are the actual monic integral irreducible Salem minimal polynomials certified for the two schedules in the adopted inputs.
There is no further cyclotomic factor.
They have even degree, trace-1 and log2<m(P_j^sigma)<log4.

In the ORIGINAL2d_j^sigma coefficient window let A_rel,j^sigma have ALL d_j^sigma columns P_j^sigma,xP_j^sigma,...,x^(d_j^sigma-1)P_j^sigma, and put

    R_j^sigma=I-A_rel,j^sigma[(A_rel,j^sigma)^T A_rel,j^sigma]^-1
                                                    (A_rel,j^sigma)^T,
    v_j^sigma(z)=(1,z,...,z^(2d_j^sigma-1))^T,
    k_j^sigma(z)=(2d_j^sigma)^-1(v_j^sigma(z^-1))^T
                                         R_j^sigma v_j^sigma(z).

For0<tau<=1 define psi_tau(s)=(1-(1-s)/tau)_+ and f_(j,tau)^sigma=psi_tau(k_j^sigma).
All circle and torus Haar measures have mass one, Fourier coefficients use exp(-i gamma dot theta), and angular derivatives use radians.
Write W_*(f)=sum_(h in Z,h!=0)abs(fhat(h)).

The common fixed-K torus polynomials are

    R=(z^K-1)(u-1)(v-1),
    S=(z^K+1)(u-1)(v-1)+(z^K-1)(u+1)(v-1)+(z^K-1)(u-1)(v+1),
    Acal=-(z^2-1)R-zR/2+zS/2,
    Bcal=(z^2-1)R-zR/2-zS/2,
    g_0=abs(Acal)^2+abs(Bcal)^2, Ncal=2Acal conjugate(Bcal).

Set U=Acal/Bcal off the common-zero set and U=0 on it.
Define

    V(z,u,v)=U(z^-1,u^-1,v^-1),
    g(z,u,v,w)=g_0(z^-1,u^-1,v^-1),
    h=(1+Re(wV))/2, Kcal=1-h, F_tau=(1-h/tau)_+,
    iota_j^sigma(z)=(z,z^a_j,z^b_j,z^(c_j^sigma)),
    H_j^sigma(gamma)=gamma_0+a_j gamma_1+b_j gamma_2+c_j^sigma gamma_3.

Let nu_1 and nu_4 be circle and four-torus Haar.
Every translated original law mu_(j,a)^sigma is the pushforward of nu_1 through z to a*iota_j^sigma(z), for a in T^4.

### The actual smooth phase and aligned original cap error

Put A_j(z)=Acal(z,z^a_j,z^b_j) and B_j(z)=Bcal(z,z^a_j,z^b_j).
Their common factor is exactly(z-1)^2.
Let U_j=A_j/B_j be the smooth circle extension after cancellation, so U_j(1)=-1, and define

    varphi_j(z)=U_j(z^-1), m_j=L_j-2.

This phase is independent of the choice of c_j^sigma.
For integer c=c_j^sigma let theta_l=2pi l/c,0<=l<c, and set

    Fej_c(t)=c^-1 abs(sum_(r=0)^(c-1)exp(irt))^2,
    I_c varphi(theta)=c^-1 sum_(l=0)^(c-1)
                          varphi_j(exp(i theta_l))Fej_c(theta-theta_l),
    q_j^sigma(exp(i theta))=c^-1 sum_(l=1)^(c-1)
                          varphi_j(exp(i theta_l))Fej_c(theta-theta_l).

Thus the ACTUAL sample at1 is replaced by0 in q_j^sigma.
Both interpolants have modulus at most1.
Define

    Delta_j^sigma=integral_T[1-Re(conjugate(varphi_j)q_j^sigma)]dnu_1,
    Delta_bar,j^sigma=[(1+4pi)(L_j-2)+1]/c_j^sigma,
    E_j^sigma=[1+pi L_j(5+2log c_j^sigma)]/c_j^sigma,
    A_cap,j^sigma=(4L_j-5)/(2d_j^sigma)+4Delta_bar,j^sigma,
    eta_cap^sigma(j,tau)=A_cap,j^sigma/tau+E_j^sigma/sqrt(tau).

Then, with BOTH positive and negative Fourier frequencies retained,

    sum_(n in Z) abs(n)abs(varphihat_j(n))^2<=L_j-2,
    0<=Delta_j^sigma<=Delta_bar,j^sigma,
    ||q_j^sigma-varphi_j||_(L1(nu_1))<=E_j^sigma.                (CA1)

For every0<tau<=1,

    ||f_(j,tau)^sigma-F_tau composed with iota_j^sigma||_1
       <=eta_cap^sigma(j,tau),
    ||f_(j,tau)^sigma-F_tau composed with iota_j^sigma||_(4/3)
       <=[eta_cap^sigma(j,tau)]^(3/4).                         (CA2)

The compared scalar functions take values in[0,1], including the original common-zero convention, so their difference is bounded by1 pointwise.
The original rank and finite cyclic corrections are fully included in A_cap,j^sigma.
No logarithm-free unweighted L1 estimate for q_j^sigma-varphi_j or for k_j^sigma-Kcal composed with iota_j^sigma is asserted.

### Complete arbitrary finite-set Fourier return

Set the common finite constants

    D_l=||partial_l Acal||_infinity+||partial_l Bcal||_infinity, l=1,2,3,
    G_K=sqrt(||g||_infinity),
    c_weight,K=6pi[1+10sum_l D_l+2(G_K+1)],
    C_smooth,K=3pi[24*64^(3/4)sum_l D_l+4^(3/4)],
    C_return2,K=2*2048^(3/4)c_weight,K+2C_smooth,K.

For a probability measure mu use

    N_mu(v)=sup_(E measurable,mu(E)>0) mu(E)^(-1/4)integral_E abs(v)dmu.

For every actual j with M=M_j>=max{2,c_weight,K}, set rho=(c_weight,K/M)^2 and

    V_rho=Ncal(z^-1,u^-1,v^-1)/(g+rho),
    h_rho=(1+Re(wV_rho))/2, F_(tau,rho)=(1-h_rho/tau)_+.

Let Q_(tau,rho) be F_(tau,rho) convolved with the four-coordinate product of the adopted probability kernel

    P_M=J_(floor(M/2)+1),
    J_N=Fej_N^2/[(2N^2+1)/(3N)].

Here Fej_N uses the preceding Fejer formula with c=N.
This kernel has CLOSED support[-M,M] and first angular moment at most3pi/M.
It is distinct from the c-grid interpolation q_j^sigma.
For EVERY0<tau<=1/64 define

    B_align^sigma(j,tau)=[eta_cap^sigma(j,tau)]^(3/4)
                                     +C_return2,K M^-1 tau^-1/8.

Then

    N_nu1(f_(j,tau)^sigma-Q_(tau,rho) composed with iota_j^sigma)
       +N_nu4(F_tau-Q_(tau,rho))<=B_align^sigma(j,tau).          (CA3)

For EVERY finite Gamma in the CLOSED integer box[-M,M]^4,

    sum_(gamma in Gamma)
       abs(fhat_(j,tau)^sigma(H_j^sigma(gamma))-Fhat_tau(gamma))
       <=8 card(Gamma)^(3/4) B_align^sigma(j,tau).              (CA4)

The empty set, zero and negative harmonics and all endpoints are included.
All original characters in the supplied set are distinct.
Both regularizations, both smoothings and the complete new original cap comparison are paid.

### The entire centered support and uniform schedule costs

Use the actual C638 centers, defined by

    D_0(z)=-2(z-z^-1)+(z^K+1)/(z^K-1), b(z)=Im D_0(z),
    z_0=exp(i pi/K),
    -cot(t_(k,m)/2)=16sqrt(km)-b(z_0), t_(k,m) in(-pi,0),
    phi_z(t)=arctan(2/[b(z)-cot(t/2)]),
    n_(k,m)=floor((k+m)phi_(z0)'(t_(k,m))+1/2),
    C_loc,K=ceil(32000pi+1024pi(K+4)).

The local phase is evaluated on its actual regular neighborhood and abs(n_(k,m))<=14(k+m).
For L_tau=floor(1/(4sqrt(tau))) and integer J>=2 set

    R_z=ceil(C_loc,K J^(1/3)),
    R_u=ceil(C_loc,K sqrt(L_tau)J^(5/6)),
    G_(L_tau,J)={(-p,-q,m,k):1<=k<=L_tau,1<=m<=J,
                               abs(p)<=R_z,abs(q-n_(k,m))<=R_u},
    N_sel=L_tau J(2R_z+1)(2R_u+1)
       <=9(C_loc,K+1)^2 L_tau^(3/2)J^(13/6),
    C_support,K=8[9(C_loc,K+1)^2]^(3/4)4^(-9/8).

Whenever

    R_z,J,L_tau<=M, 14(L_tau+J)+R_u<=M,                        (CA5)

all selected original frequencies are distinct and strictly positive, and

    W_*(f_(j,tau)^sigma)>=3log(J+1)/(32768pi)
                              -8N_sel^(3/4)B_align^sigma(j,tau). (CA6)

Define fixed constants and schedule exponents

    A_cap=20(1+pi), E_square=10(1+pi), E_balanced=100(1+pi),
    alpha_square=2, alpha_balanced=28/11, T_M=1+log M,
    C_align,sigma,K=C_support,K
                    [A_cap^(3/4)+(2E_sigma)^(3/4)+C_return2,K].

For EVERY M=M_j>=2 in the indicated actual schedule,

    A_cap,j^sigma<=A_cap M^(-alpha_sigma),
    E_j^sigma<=2E_sigma M^(-alpha_sigma)T_M.                    (CA7)

Consequently the ENTIRE subtracted term in(CA6) is at most

    C_support,K J^(13/8)[
       A_cap^(3/4)M^(-3alpha_sigma/4)tau^(-21/16)
       +(2E_sigma)^(3/4)M^(-3alpha_sigma/4)T_M^(3/4)tau^(-15/16)
       +C_return2,K M^-1 tau^(-11/16)].                        (CA8)

### Both critical enlargements and actual degrees

Put

    M_balanced,K=ceil(max{2,c_weight,K,(C_loc,K+1)^(33/29),
                                7^(11/3),(C_loc,K+29)^(11/7)}),
    M_square,K=ceil(max{2,c_weight,K,(C_loc,K+1)^(21/19),
                                7^(7/3),(C_loc,K+29)^(7/5)}).

For EVERY actual j with M=M_j>=M_balanced,K and EVERY real H,tau satisfying

    16<=H<=M^(16/11)/64, M^(-16/11)H<=tau<=1/64,                (CA9)

the choice J=floor(H^(1/4)) satisfies ALL conditions(CA5) and

    W_*(f_(j,tau)^balanced)>=3log H/(131072pi)
       -C_align,balanced,K[
          H^(-29/32)+M^(-6/11)T_M^(3/4)H^(-17/32)+H^(-9/32)].  (CA10)

Separately, for EVERY actual j with M=M_j>=M_square,K and EVERY H,tau satisfying

    16<=H<=M^(8/7)/64, M^(-8/7)H<=tau<=1/64,                   (CA11)

the SAME choice J=floor(H^(1/4)) satisfies ALL conditions(CA5) and

    W_*(f_(j,tau)^square)>=3log H/(131072pi)
       -C_align,square,K[
          H^(-29/32)+M^(-3/7)T_M^(3/4)H^(-17/32)
                                      +M^(-3/14)H^(-9/32)].   (CA12)

These bounds are uniform over their entire H,tau strips.
For the same ACTUAL minimal-polynomial degrees, the adopted estimates are

    M_j^(50/11)<d_j^balanced<2^33 M_j^(50/11),
    256M_j^4<d_j^square<2^21 M_j^4, M_j>=2.                   (CA13)

Thus EVERY shrinking sequence tau_j->0 with

    (d_j^balanced)^(8/25)tau_j->infinity

has W_*(f_(j,tau_j)^balanced)->infinity, and EVERY shrinking sequence with

    (d_j^square)^(2/7)tau_j->infinity

has W_*(f_(j,tau_j)^square)->infinity.
These conditions are respectively equivalent to M_j^(16/11)tau_j->infinity and M_j^(8/7)tau_j->infinity.
There is no prescribed logarithmic enlargement and no monotonicity requirement.
Sequence entry may depend on the sequence.
Neither a bounded-H endpoint, an every-large-degree theorem, width optimality nor a near-one family is asserted.
For each fixed input and width the Wiener sum is finite, and the actual contact-minus-Haar margin remains at least1/2 in the full original2d_j^sigma window.
The unrestricted G0001 conclusion remains outside this result.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Complete argument

<a id="actual-family-and-cyclic-costs"></a>
### 1. Actual inputs and every original projection cost

The two families are the adopted [C644 actual balanced construction and separate square comparison](Yin_C_G0644_v1.md#statement), with the original square family also fixed in [C641v2](Yin_C_G0641_v2.md#statement).
Their exact source-certified polynomials, complete factor removal, original degrees and positive Mahler-measure interval are unchanged.
In particular all three moving exponents are distinct odd primes>K and coprime to K.
Both choices satisfy c>(L+1)^2, L>6 and d=c+L-3.
The source applicability and accepted original-proof limits remain those of C644; this argument does not recertify a larger arithmetic class.

Suppress j,sigma temporarily.
Write Qraw=(x-1)^3P=A+x^c B, where

    R_0=(x^K-1)(x^a-1)(x^b-1),
    S_0=sum_(e in {K,a,b})(x^e+1)product_(v in {K,a,b},v!=e)(x^v-1),
    A=-(x^2-1)R_0-xR_0/2+xS_0/2,
    B= (x^2-1)R_0-xR_0/2-xS_0/2.

Both A and B have degree L, with constant and leading coefficients-1 for A and1 for B.
The raw relation matrix T consists of r=2d-deg Qraw=c+L-6=d-3 columns Qraw,xQraw,...,x^(r-1)Qraw in the SAME N=2d coordinates.
Their leading degrees prove independence.
Let Pi_P,Pi_Q be the full P and raw relation projections.
Since the raw space is contained in the full relation space, Pi_P-Pi_Q is a rank3 orthogonal projection.

For S_c e_i=e_(i+1 mod c), let

    V_c=[A(S_c);B(S_c);0_(2L-6)-by-c],

and let Pi_V project onto its actual range.
The first c columns T_0 of T agree with V_c for0<=i<c-L; at most L columns differ.
Their ranges therefore have a common subspace of codimension at most L in each, so their projection difference has rank at most2L.
The remaining L-6 columns extend im T_0 by exactly L-6 dimensions.
Differences of orthogonal projections have operator norm at most1.
The trace-norm triangle inequality consequently gives

    ||Pi_Q-Pi_V||_trace<=3L-6,
    ||Pi_P-Pi_V||_trace<=3L-3.                                 (CA14)

These are the actual cyclic-boundary and original rank-three prices.

The exact common-zero and equal-modulus calculation in C644 gives rank V_c=c-1.
At every nontrivial c-th root omega, none of omega^K,omega^a,omega^b equals1, while at omega=1 both A and B vanish.
The cyclic eigenvectors omega^-i give diagonal blocks(I_c-J_c/c)/2 and off-diagonal block

    Pi_V,12(i,l)=(1/(2c))sum_(omega^c=1)
                         U(omega,omega^a,omega^b)omega^(l-i).

The common-zero sample is0.
Reindexing omega=exp(-i theta_l) gives precisely the q_j^sigma in the statement, with the inverse phase varphi_j.
In particular the cross term is z^c q_j^sigma(z), not z^c U_j(z).
Direct block evaluation therefore gives

    v_(2d)(z)^*Pi_V v_(2d)(z)
       =c-abs(sum_(r=0)^(c-1)z^r)^2/c+c Re(z^c q_j^sigma(z)).  (CA15)

Define k_V=1-(2d)^-1 v^*Pi_Vv and K_q=(1-Re(z^c q_j^sigma))/2.
Both lie in[0,1].
For self-adjoint H, abs(v^*Hv)<=v^*abs(H)v, and integral vv^*dnu_1=I_(2d).
Thus(CA14) gives

    ||k_j^sigma-k_V||_1<=(3L-3)/(2d).                          (CA16)

Since q_j^sigma has Fourier degree at most c-1, z^c q_j^sigma has zero Haar mean.
Equation(CA15) yields the pointwise nonnegative correction

    k_V-K_q=((d-c)/(2d))(1+Re(z^c q_j^sigma))
                                      +Fej_c(arg z)/(2d)>=0.

Its EXACT integral is

    ||k_V-K_q||_1=(d-c+1)/(2d)=(L-2)/(2d).                    (CA17)

The normalization is2d throughout, not2c or deg Qraw.
The missing mode and the finite Fejer term have not been discarded or charged as a free contact contribution.

<a id="two-sided-rational-phase-energy"></a>
### 2. Actual rational factors and two-sided Dirichlet energy

The [complete C172 phase factorization](Yin_C_G0172_v1.md#moving-cubic-phase-variation), also rebuilt for both present schedules in C644, depends only on A and B.
Indeed A+B=-zR_0 and neither constant coefficient vanishes.
All common roots are roots of unity; pairwise coprimality forces their only location to be1.
The exact values after order-two division are

    [A/(z-1)^2](1)=Ka+Kb+ab,
    [B/(z-1)^2](1)=-(Ka+Kb+ab).

They are nonzero.
Equal modulus of A and B on the circle then excludes all other circle roots.
With reciprocal conjugation in degree L, B=-A^*.
Consequently, after cancellation, m=L-2 and

    U_j(z)=lambda product_(l=1)^m (z-alpha_l)/(1-conjugate(alpha_l)z),
    abs(lambda)=1,

where every alpha_l is off the unit circle and multiplicities are retained.
No assumption that all roots are inside the disk is made.

For an outside root alpha, put beta=1/conjugate(alpha).
The exact identity

    (z-alpha)/(1-conjugate(alpha)z)
       =(alpha/conjugate(alpha))/B_beta(z),
    B_beta(z)=(z-beta)/(1-conjugate(beta)z)

replaces it by a unimodular constant times a reciprocal disk Blaschke factor.
Also B_beta(z^-1)=1/B_(conjugate(beta))(z).
Thus after the actual inversion defining varphi_j its boundary form is

    varphi_j=lambda_0 B_plus conjugate(B_minus), abs(lambda_0)=1,

where B_plus,B_minus are finite disk Blaschke products of degrees p,q>=0 with p+q=m.
Degree-zero products are constants.
Both are analytic on a neighborhood of the closed disk.
This transformation retains every inside and outside factor.

For a degree-r finite disk Blaschke B(z)=sum_(n>=0)b_n z^n, the exact weighted coefficient identity is

    sum_(n>=0)n abs(b_n)^2
       =integral_T conjugate(B(z))zB'(z)dnu_1(z)=r.             (CA18)

For clarity, its complete finite-product justification is as follows.
On the circle conjugate(B)=1/B, and logarithmic differentiation gives the sum of the r Poisson terms
(1-abs(beta)^2)/abs(z-beta)^2.
Each has normalized circle mean1 by its two geometric series.
The differentiated series converge uniformly because all poles are outside the closed disk.
Circle orthogonality gives the first equality.
This is exactly the weighted identity and bounded attribution retained in L264/GMR18-U001.

Use ordinary planar area dA and Wirtinger derivatives
partial=(partial_x-i partial_y)/2, barpartial=(partial_x+i partial_y)/2.
Define

    E_D(F)=pi^-1 integral_(abs(z)<1)
                             (abs(partial F)^2+abs(barpartial F)^2)dA.

Termwise radial integration and(CA18) give
pi^-1 integral_disk abs(B')^2dA=sum n abs(b_n)^2=r.
For the smooth disk extension F=lambda_0 B_plus conjugate(B_minus),

    partial F=lambda_0 B_plus' conjugate(B_minus),
    barpartial F=lambda_0 B_plus conjugate(B_minus').

Since both products have modulus at most1 in the disk,

    E_D(F)<=p+q=m.                                            (CA19)

Let f_n=varphihat_j(n) and define the explicit harmonic extension

    H(z)=f_0+sum_(n>=1)[f_n z^n+f_(-n)conjugate(z)^n].

The smooth boundary phase has rapidly decreasing Fourier coefficients by repeated angular integration by parts.
Its Fourier series and all derivatives needed here converge uniformly; circle Fourier uniqueness identifies its boundary values with varphi_j.
Thus H is smooth on the closed disk and has the same boundary values as F.
Direct radial integration, retaining BOTH signs, gives

    E_D(H)=sum_(n in Z)abs(n)abs(f_n)^2.                       (CA20)

Put G=F-H, which vanishes on the boundary.
The cross term in E_D(H+G) is exactly

    pi^-1 Re integral_disk[partial_x H conjugate(partial_x G)
                         +partial_y H conjugate(partial_y G)]dA.

It is zero.
Integrating each coordinate by parts gives the boundary term with G=0 minus the integral of Delta H times conjugate(G), which is zero because H is harmonic.
Thus E_D(F)=E_D(H)+E_D(G)>=E_D(H).
Together with(CA19)--(CA20) this proves the first line of(CA1), including its exact normalization and negative-frequency contribution.
No general area formula or uninspected theorem about one-sided analytic phases is substituted for this argument.

Inversion of circle orientation preserves total variation.
Each original factor also has angular phase derivative
(1-abs(alpha)^2)/abs(exp(it)-alpha)^2.
Its absolute integral is2pi, including an outside root by reflection.
Therefore the UNNORMALIZED total variation satisfies

    V(varphi_j):=integral_0^(2pi)abs(d/dt varphi_j(exp(it)))dt
       <=2pi m.                                               (CA21)

This is uniform in how close the roots lie to the circle.

<a id="aligned-discrete-fejer-defect"></a>
### 3. Aligned continuous and discrete defects, with the actual omitted sample

For integer c>=2 the Fejer kernel has nonnegative unit mass and Fourier multipliers
(1-abs(n)/c)_+.
Since varphi_j is unimodular, circle orthogonality gives

    1-Re integral conjugate(varphi_j)(Fej_c*varphi_j)dnu_1
       =sum_(n in Z)min{abs(n)/c,1}abs(varphihat_j(n))^2
       <=m/c.                                                 (CA22)

The term n=c and its negative counterpart are included with multiplier1 in the defect.
The inequality uses(CA20), not an unweighted modulus-of-continuity estimate.

For a smooth periodic complex function G_quad, the c equal arcs starting at theta_l give

    abs(c^-1 sum_l G_quad(theta_l)-integral G_quad dnu_1)
       <=V(G_quad)/c.                                        (CA23)

To check the normalization, on each arc the difference from its left endpoint is bounded by that arc's variation.
Integration over the arc of length2pi/c, summation and division by2pi give exactly V(G_quad)/c.
This holds for complex G_quad by the triangle inequality.

Apply this with

    G_quad(theta)=varphi_j(exp(i theta))
                         (Fej_c*conjugate(varphi_j))(theta).

The kernel is real, even and nonnegative, so the two factors have modulus at most1.
Differentiation under convolution and integration give
V(Fej_c*conjugate(varphi_j))<=V(varphi_j).
The product rule therefore yields

    V(G_quad)<=2V(varphi_j)<=4pi m.                            (CA24)

Finite interchange and evenness of the kernel identify its grid sum exactly as

    c^-1 sum_l G_quad(theta_l)
       =integral conjugate(varphi_j)I_c varphi_j dnu_1.

Its Haar integral has the same real value as
integral conjugate(varphi_j)(Fej_c*varphi_j)dnu_1.
Thus(CA22)--(CA24) bound the aligned I_c defect by(1+4pi)m/c.

Grid orthogonality gives c^-1 sum_l Fej_c(theta-theta_l)=1.
It follows that abs(I_c varphi_j)<=1 and abs(q_j^sigma)<=1.
The actual omitted value is varphi_j(1)=-1, so

    q_j^sigma=I_c varphi_j+Fej_c/c.

The absolute change in its aligned integral is at most1/c, since abs(varphi_j)=1 and Fej_c has mass one.
Also1-Re(conjugate(varphi_j)q_j^sigma)>=0 pointwise.
Consequently

    0<=Delta_j^sigma<=[(1+4pi)m+1]/c=Delta_bar,j^sigma.         (CA25)

Every grid point and the missing zero mode are paid.

The separate unweighted estimate is still the complete adopted C172/C644 bound E_j^sigma.
Its constants can be recovered directly: equal-grid arc counting gives
c^-1 sum_l abs(varphi(theta_l+t)-varphi(theta_l))
<=V(varphi)(abs(t)/(2pi)+1/c).
The bound Fej_c(t)<=min{c,pi^2/(ct^2)} on[-pi,pi], split at pi/c, gives first moment at most pi(1/2+log c)/c.
Therefore

    ||I_c varphi_j-varphi_j||_1
       <=V(varphi_j)(5/4+(log c)/2)/c.

Use V(varphi_j)<=2pi(L-2) and pay the additional1/c sample term.
The stated larger E_j^sigma follows.
This proves all of(CA1) and preserves its logarithmic L1 term.
The improved aligned integral alone is not claimed to remove that logarithm from the unweighted estimate.

<a id="pointwise-contact-cap-and-full-original-return"></a>
### 4. The pointwise contact cap inequality and scalar sign

For any complex u,q,w with abs(u)=abs(w)=1 and abs(q)<=1, write

    conjugate(u)q=1-a+ib, v=-wu,
    h=(1-Re(v))/2=(1+Re(wu))/2,
    h_q=(1-Re(v(1-a+ib)))/2=(1+Re(wq))/2.

Then a>=0, b^2<=2a-a^2<=2a, and

    abs(h_q-h)<=a/2+abs(b)sqrt(h).                             (CA26)

Indeed h_q-h=(a Re(v)+b Im(v))/2 and
abs(Im(v))=2sqrt(h(1-h))<=2sqrt(h).
For F_tau^scalar(h)=(1-h/tau)_+ and EVERY0<tau<=1 we claim

    abs(F_tau^scalar(h)-F_tau^scalar(h_q))
       <=4a/tau+abs(q-u)/sqrt(tau).                            (CA27)

If h<=tau, global1/tau Lipschitz continuity and(CA26) prove this with a/2 in place of4a.
If h>tau and h_q>=tau the left side is zero.
In the remaining crossing case h>tau>h_q, put x=sqrt(h).
Equation(CA26) gives x^2<=tau+a/2+abs(b)x and hence
x<=abs(b)+sqrt(tau)+sqrt(a/2).
The difference is at most(h-h_q)/tau, bounded by

    a/(2tau)+abs(b)x/tau
       <=(7/2)a/tau+abs(b)/sqrt(tau),

because b^2<=2a and abs(b)sqrt(a/2)<=a.
Finally abs(b)<=abs(q-u).
The endpoint equalities are included in the preceding non-strict cases.
This proves(CA27) at the SAME point, without phase averaging.

Apply it with u=varphi_j(z), q=q_j^sigma(z) and w=z^(c_j^sigma).
Then h=1-K_phase, where

    K_phase=(1-Re(z^(c_j^sigma)varphi_j(z)))/2,

so F_tau^scalar(h)=psi_tau(K_phase).
The minus sign in v=-wu is essential and is retained explicitly.
Likewise F_tau^scalar(h_q)=psi_tau(K_q).
Integrating(CA27), using(CA25) and the separate E_j^sigma estimate, gives

    ||psi_tau(K_phase)-psi_tau(K_q)||_1
       <=4Delta_bar,j^sigma/tau+E_j^sigma/sqrt(tau).           (CA28)

On the other two comparisons use only the ordinary1/tau Lipschitz bound.
Equations(CA16)--(CA17) cost exactly at most

    [(3L-3)+(L-2)]/(2d tau)=(4L-5)/(2d tau).

Adding this to(CA28) proves the first inequality of(CA2).
K_phase equals Kcal composed with iota_j^sigma except at z=1, where the smooth extension and original common-zero convention differ.
That single point is Haar null.
Every compared scalar function takes values in[0,1], so its difference is bounded by1.
Raising this bounded difference to the4/3 power and integrating shows its L^(4/3) norm is at most the3/4 power of the L1 bound.
This proves the second inequality of(CA2).
Neither a rank correction nor a finite cyclic term has been assigned a cheaper tangential price.

### 5. All remaining costs and every finite original coefficient

The remaining four costs are exactly the adopted joint-shell and contact-supported estimates.
For the square family they are in [C641v2](Yin_C_G0641_v2.md#complete-additional-joint-shell-argument).
For the balanced family their complete translated-law premises were rebuilt and adopted in [C644](Yin_C_G0644_v1.md#complete-argument).
Both retain the SAME torus g and phase and the exact kernel P_M.
At rho=(c_weight,K/M)^2 with M>=max{2,c_weight,K}, one has0<rho<=1 and the required resolution M sqrt(rho)=c_weight,K.
On EACH of the actual original and product spaces these inputs give

    ||F_tau-F_(tau,rho)||_(4/3)
       <=2048^(3/4)rho^(1/2)tau^(-1/8),
    N_mu(F_(tau,rho)-Q_(tau,rho))
       <=C_smooth,K M^-1 tau^(-1/8).                          (CA29)

They include every translated original circle, every clipping path and the branch rho/tau>1.
Their proof uses the joint contact/amplitude event law at every s>=rho, including large shells, and does not assume coordinate independence on an original curve.
The first term bounds its event norm by Holder.
Adding the TWO regularizations and TWO smoothings gives exactly
C_return2,K M^-1 tau^-1/8.
The new original cost is(CA2), so the event-norm triangle gives(CA3) with all FIVE costs.

For completeness, both schedules satisfy the closed alias inequalities

    a>2M, b>2M(1+a), c>2M(1+a+b).

These follow from M=floor(a/4), b>(K+a+3)^2 and c>(L+1)^2.
In any nonzero integer delta in[-2M,2M]^4, its highest nonzero weighted coordinate dominates the others.
Thus H_j^sigma(delta)!=0.
A finite Q_(tau,rho) supported in the closed M box consequently has the EXACT selected coefficient after pullback at every gamma in that same box; its difference indices remain in the closed2M box.
This also proves distinctness of every selected original character.
No nonlinear mean identity is inferred here.

The adopted direct finite weak Fourier calculation in C641v2 applies to arbitrary probability spaces with finite orthonormal modulus-one characters.
For a function of event norm B it bounds the ENTIRE N-character coefficient sum by8B N^(3/4); its proof includes B=0, empty sets and ties.
Apply it to f_(j,tau)^sigma-Q_(tau,rho) composed with iota_j^sigma and to F_tau-Q_(tau,rho).
Their intermediate coefficients agree exactly, so(CA3) proves(CA4).
This reuses an already fixed finite proof, without importing a strong Hausdorff--Young assertion for a merely weak source.

### 6. The complete support and both schedule bounds

The [adopted C638 local theorem](Yin_C_G0638_v1.md#complete-local-modulation-calculation) is a statement about the common fixed-K torus phase.
Its corrected cotangent sign, exact integer centers and local radii apply unchanged to BOTH families.
For every k,m its closed shifted rectangle has coefficient mass at least1/(512m).
The chosen common radii dominate every one of these required local radii.
The distinct third and fourth coordinates keep all k,m bands distinct, including when their second-coordinate intervals overlap.
Thus the complete count is precisely N_sel, with BOTH endpoints included.

The bound abs(n_(k,m))<=14(k+m) and(CA5) put the entire selected set in the closed M box.
Moreover H_j^sigma(gamma)>=c-M(1+a+b)>0 whenever gamma lies in that box with fourth coordinate k>=1.
The selected frequencies are pairwise distinct by the closed alias exclusion.
The same cap harmonics and inverse-phase identity as C638 give the entire torus mass3log(J+1)/(32768pi), since L_tau>=2 and1/8<=L_tau sqrt(tau)<=1/4.
Apply(CA4) to every selected coefficient.
This proves(CA6), without dropping any center, tail of a band or original frequency.

Now d>=c and

    Delta_bar=[(1+4pi)(L-2)+1]/c<=(1+4pi)L/c.

Consequently

    A_cap,j^sigma<=(6+16pi)L/c<=A_cap L/c.                     (CA30)

For the balanced schedule c>(L+1)^(25/11) and L>b>a^2>=16M^2, so
L/c<=L^(-14/11)<=M^(-28/11).
For the square schedule c>(L+1)^2 similarly gives L/c<=L^-1<=M^-2.
This proves the first line of(CA7) with the stated common constant.

For the second line, retain the exact previous numerical quantity

    epsilon_j^sigma=(4L_j-5)/(2d_j^sigma)+E_j^sigma/2.

The adopted bounds are epsilon_j^balanced<=E_balanced M^(-28/11)T_M from C644 and epsilon_j^square<=E_square M^-2 T_M from C641v2.
The nonnegative rank term gives E_j^sigma<=2epsilon_j^sigma.
Thus the second line of(CA7) is valid for every M>=2.
It is used only to estimate the old tangential L1 quantity E_j^sigma, not as the improved full cap error.

For nonnegative x,y, (x+y)^(3/4)<=x^(3/4)+y^(3/4).
Therefore(CA2) and(CA7) bound the original event-norm cost by

    A_cap^(3/4)M^(-3alpha_sigma/4)tau^(-3/4)
       +(2E_sigma)^(3/4)M^(-3alpha_sigma/4)
                                         T_M^(3/4)tau^(-3/8).

Also L_tau<=1/(4sqrt(tau)), so the full support multiplier is

    8N_sel^(3/4)<=C_support,K J^(13/8)tau^(-9/16).              (CA31)

Multiplication gives precisely ALL THREE costs in(CA8).
The radial rank/aligned error, tangential interpolation error and joint-shell/smoothing error remain separate.

<a id="both-critical-strips-and-actual-degrees"></a>
### 7. Every floor, ceiling and center in the two strips

Under(CA9) put J=floor(H^(1/4))>=2.
The complete bounds, with all ceilings paid by ceil(Cx)<=(C+1)x for x>=1, are

    L_tau<=M^(8/11)H^(-1/2)/4,
    J<=M^(4/11),
    R_z<=(C_loc,K+1)M^(4/33),
    R_u<=(C_loc,K+1)M^(4/11)H^(-1/24)/2.                     (CA32)

Indeed sqrt(L_tau) contributes H^-1/4 while J^(5/6) contributes H^(5/24).
Since H>=1,

    14(L_tau+J)+R_u
       <=(7/2)M^(8/11)+[(C_loc,K+29)/2]M^(4/11).

The first term is at most M/2 when M^(3/11)>=7.
The second is at most M/2 when M^(7/11)>=C_loc,K+29.
Also R_z<=M when M^(29/33)>=C_loc,K+1.
These are exactly the displayed M_balanced,K conditions.
Separately L_tau,J<=M, and all lower bounds on the radii follow from their definitions.
Thus EVERY centered closed-box condition(CA5) holds uniformly over(CA9).

Under(CA11), the corresponding complete bounds are

    L_tau<=M^(4/7)H^(-1/2)/4,
    J<=M^(2/7),
    R_z<=(C_loc,K+1)M^(2/21),
    R_u<=(C_loc,K+1)M^(2/7)H^(-1/24)/2.                      (CA33)

The two center-plus-radius terms are at most M/2 when respectively
M^(3/7)>=7 and M^(5/7)>=C_loc,K+29.
The separate radius condition is M^(19/21)>=C_loc,K+1.
These are precisely M_square,K.
Thus all square-family conditions hold uniformly as well.
The absence of logarithms here follows from the newly stated strips; no old logarithmic hypothesis is silently dropped.

### 8. All error powers and the actual-degree implications

For both strips J^(13/8)<=H^(13/32), and J+1>H^(1/4).
In the balanced family the three M exponents obtained from(CA8) and tau>=M^(-16/11)H are respectively

    -21/11+(16/11)(21/16)=0,
    -21/11+(16/11)(15/16)=-6/11,
    -1+(16/11)(11/16)=0.

Their H exponents are respectively

    13/32-21/16=-29/32,
    13/32-15/16=-17/32,
    13/32-11/16=-9/32.

Only the middle error retains T_M^(3/4).
The defined C_align,balanced,K dominates every fixed coefficient in these three terms.
Together with log(J+1)>(1/4)log H, this proves(CA10).

For the square family alpha_square=2 and tau>=M^(-8/7)H give M exponents

    -3/2+(8/7)(21/16)=0,
    -3/2+(8/7)(15/16)=-3/7,
    -1+(8/7)(11/16)=-3/14.

The three H exponents are unchanged.
Using C_align,square,K proves(CA12).
No coefficient cardinality or logarithmic power has been suppressed.

The degree bounds(CA13) are the adopted actual minimal-polynomial bounds in C644, obtained with integer-threshold Bertrand and complete factor removal.
They imply directly

    M^(16/11)<(d^balanced)^(8/25)<2^(264/25)M^(16/11),
    2^(16/7)M^(8/7)<(d^square)^(2/7)<2^6 M^(8/7).

Hence the stated degree and M conditions are equivalent for ANY positive width sequence, by two-sided multiplication with fixed positive constants.
They concern the actual2d coefficient windows, not the raw numerator degrees or a replacement of d by c.

For a balanced-family sequence satisfying the condition, take H=M_j^(16/11)tau_j.
Eventually H>=16, tau_j<=1/64 and M_j>=M_balanced,K, so(CA9) holds.
The logarithmic main term tends to infinity.
The first and third errors tend to zero because H->infinity; the middle error is at most M_j^(-6/11)(1+log M_j)^(3/4), which tends to zero.
The square-family argument uses H=M_j^(8/7)tau_j and(CA11); its middle and final errors tend to zero with their displayed negative powers of M_j.
This proves both divergence statements with possibly sequence-dependent entry indices.

Finally each R_j^sigma is a rank-d_j^sigma projection in2d_j^sigma dimensions, so integral k_j^sigma=1/2 and0<=k_j^sigma<=1.
At every unit-circle root of the actual P_j^sigma all original relation columns annihilate the evaluation vector, so k_j^sigma=1.
Since psi_tau(s)<=s on[0,1], the contact-minus-Haar margin is at least1/2.
For fixed j,tau the cap is periodic Lipschitz and its square-integrable weak derivative gives absolute Fourier summability by finite derivative Bessel and sum_(n!=0)n^-2<infinity, as in the adopted fixed-input argument.
These unchanged facts do not give a bounded-H endpoint, near-one family, optimal exponent or unrestricted Task conclusion.

<a id="bounded-source-and-reuse-account"></a>
### 9. Exact classical attribution and reuse limits

The bounded reuse check read C172's full actual rational factorization, inverse sampling orientation, variation, missing-mode and original2d comparison, and the corresponding complete reconstruction in adopted C644.
The needed Blaschke coefficient identity was read in [L264](../ledger/Yin_L_G0264_v1.md#exact-blaschke-two-moment-budget).
Its [GMR18-U001 source account](../audits/literature/GMR18/Yin_U001.md#original-blaschke-author-reading) retains the actually inspected arXiv1512.05444v2,2016-07-07 normalization and printed p14, Section7 equations7.1--7.4, with the boundary Poisson identity at7.2--7.3.
The2018 typeset chapter and a whole original-source proof were not newly inspected.
The accepted source unit attributes only the exact finite-Blaschke derivative and its applicability.
The differentiated coefficient identity, radial integration, mixed analytic/conjugate extension, two-sided Fourier energy and integration-by-parts comparison are explicitly supplied locally above.
No uninspected area formula or general energy-minimization theorem is imported.

The classical Fejer normalization, full discrete L1 mechanism and omitted sample are the exact C172 inputs, with the aligned quadrature refinement proved here.
The positive squared kernel, contact-supported paths, all-scale shell estimates and finite weak Fourier argument retain their complete C637/C641v2 proof and bounded source scopes.
C644 supplies the changed family's actual translated-law applicability rather than a renaming of the old schedule.
The prior source certification of the two Salem families, integer Bertrand input and actual degree conversion is reused at C644's declared depth.
No source-version substitution, acquired-source mutation, new original-source audit, general optimality or novelty claim follows.
The new project deduction is the contact-aligned original cap estimate and its fully paid two-family consequences.

## Assessment history

### Decision contact-aligned-return-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T22:10 |
| status | open |
| reason | Register the two-sided actual rational-phase energy, complete aligned discrete Fejer defect including the missing sample, pointwise contact cap comparison, full original2d five-cost finite return and entire centered support. The balanced actual-degree8/25 and separate square-family2/7 conditions now need only arbitrary diverging enlargement without a prescribed logarithmic factor. Root and phase_bands are contributors; this new fixed theorem awaits fresh independent whole review. No unweighted logarithm-free L1 estimate, bounded-H endpoint, wider source proof, every-large-degree theorem, optimality, near-one family or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire aligned-return statement](#statement) | CA1--CA13, both exact prime schedules and actual minimal polynomials, full2d windows, signed phase energy, missing sample, all finite Gamma and full centered bands, explicit constants/thresholds and all H,tau/sequence/actual-degree quantifiers. |
| argument | [Whole complete argument](#complete-argument) | CA14--CA33 and all proofs: complete cyclic and rank-three prices, inside/outside factors and both Fourier signs, exact Dirichlet normalization, continuous/discrete alignment, quadrature and omitted sample, cap crossing signs, every original and joint-shell cost, support/thresholds/exponents and two distinct actual degrees. |
| dependency | [Adopted actual balanced and square interfaces](Yin_C_G0644_v1.md#decision-whole-reviewed-2026-10-23) | Exact two schedules, certified minimal-polynomial degrees and factor removal, full finite matrix/phase comparison, changed-family aliases and all translated laws, explicit schedule rates, integer-Bertrand degree bounds and original source-depth limits. |
| dependency | [Adopted joint-shell and finite weak mechanism](Yin_C_G0641_v2.md#combined-argument) | On the square family and as rebuilt in C644 on the balanced family, all-scale joint probabilities, both regularizations and contact-supported smoothings, every-path clipping and finite weak Fourier constants; only the original cap comparison is improved here. |
| dependency | [Actual rational phase and variation](Yin_C_G0172_v1.md#moving-cubic-phase-variation) | Exact A/B cancellation, off-circle roots with full multiplicities, inverse-phase convention and complete total variation; no all-inside hypothesis. |
| dependency | [Original discrete interpolation](Yin_C_G0172_v1.md#moving-cubic-discrete-fejer) | Exact grid partition, normalized Fejer kernel, complete old logarithmic L1 estimate and missing sample; the aligned defect is newly proved here. |
| dependency | [Full original projection return](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | Same2d normalization, rank-three correction and exact finite cyclic correction, explicitly reconstructed for the two adopted families. |
| dependency | [Finite Blaschke weighted identity](../ledger/Yin_L_G0264_v1.md#exact-blaschke-two-moment-budget) | Complete differentiated orthogonality and Poisson mean proof for a finite disk Blaschke product; mixed signed-phase energy is supplied here. |
| support | [Bounded original Blaschke attribution](../audits/literature/GMR18/Yin_U001.md#gmr18-u001) | Actual2016 arXiv v2, printed p14 equations7.2--7.4 and retained passage-level source applicability only; no new2018 typeset or whole original-proof audit. |
| dependency | [Entire torus modulated bands](Yin_C_G0638_v1.md#complete-local-modulation-calculation) | Corrected cotangent sign, every actual integer center, closed rectangles, exact support count and torus mass; each actual original return is paid by the new finite theorem. |
| dependency | [Normalized squared positive kernel](Yin_C_G0637_v1.md#exact-positive-kernel-and-closed-support) | Exact P_M definition, unit mass, closed support and3pi/M first moment with its adopted proof and attribution limits. |
| dependency | [Generic fixed-input contacts](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Full-window projection/contact identity, scalar range and fixed-j Lipschitz/Fourier argument; no change in the original probability law or unrestricted conclusion. |
| support | [Actual reuse and classical limits](#bounded-source-and-reuse-account) | Fixed-source and fixed-proof interfaces, exact newly proved signed-energy/aligned/cap steps and complete retained inspection limits. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T22:18 |
| status | proved |
| reason | Adopt the complete CA1--CA33 theorem after main reading of entire C648 and isolated whole R856. The full signed rational-phase energy, discrete aligned defect with omitted sample, pointwise cap comparison and all original2d/five-return costs are paid. Every finite closed-box coefficient and actual centered band is included. The new balanced actual-degree8/25 and separate square-family2/7 criteria require arbitrary diverging enlargement without a prescribed logarithmic factor. The unweighted L1 logarithm, source-depth boundaries and all bounded-H/optimality/near-one/unrestricted Task exclusions remain intact. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire aligned-return statement](#statement) | CA1--CA13, both exact prime schedules and actual minimal polynomials, full2d windows, signed phase energy, missing sample, all finite Gamma and full centered bands, explicit constants/thresholds and all H,tau/sequence/actual-degree quantifiers. |
| argument | [Whole complete argument](#complete-argument) | CA14--CA33 and all proofs: complete cyclic and rank-three prices, inside/outside factors and both Fourier signs, exact Dirichlet normalization, continuous/discrete alignment, quadrature and omitted sample, cap crossing signs, every original and joint-shell cost, support/thresholds/exponents and two distinct actual degrees. |
| dependency | [Adopted actual balanced and square interfaces](Yin_C_G0644_v1.md#decision-whole-reviewed-2026-10-23) | Exact two schedules, certified minimal-polynomial degrees and factor removal, full finite matrix/phase comparison, changed-family aliases and all translated laws, explicit schedule rates, integer-Bertrand degree bounds and original source-depth limits. |
| dependency | [Adopted joint-shell and finite weak mechanism](Yin_C_G0641_v2.md#combined-argument) | On the square family and as rebuilt in C644 on the balanced family, all-scale joint probabilities, both regularizations and contact-supported smoothings, every-path clipping and finite weak Fourier constants; only the original cap comparison is improved here. |
| dependency | [Actual rational phase and variation](Yin_C_G0172_v1.md#moving-cubic-phase-variation) | Exact A/B cancellation, off-circle roots with full multiplicities, inverse-phase convention and complete total variation; no all-inside hypothesis. |
| dependency | [Original discrete interpolation](Yin_C_G0172_v1.md#moving-cubic-discrete-fejer) | Exact grid partition, normalized Fejer kernel, complete old logarithmic L1 estimate and missing sample; the aligned defect is newly proved here. |
| dependency | [Full original projection return](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | Same2d normalization, rank-three correction and exact finite cyclic correction, explicitly reconstructed for the two adopted families. |
| dependency | [Finite Blaschke weighted identity](../ledger/Yin_L_G0264_v1.md#exact-blaschke-two-moment-budget) | Complete differentiated orthogonality and Poisson mean proof for a finite disk Blaschke product; mixed signed-phase energy is supplied here. |
| support | [Bounded original Blaschke attribution](../audits/literature/GMR18/Yin_U001.md#gmr18-u001) | Actual2016 arXiv v2, printed p14 equations7.2--7.4 and retained passage-level source applicability only; no new2018 typeset or whole original-proof audit. |
| dependency | [Entire torus modulated bands](Yin_C_G0638_v1.md#complete-local-modulation-calculation) | Corrected cotangent sign, every actual integer center, closed rectangles, exact support count and torus mass; each actual original return is paid by the new finite theorem. |
| dependency | [Normalized squared positive kernel](Yin_C_G0637_v1.md#exact-positive-kernel-and-closed-support) | Exact P_M definition, unit mass, closed support and3pi/M first moment with its adopted proof and attribution limits. |
| dependency | [Generic fixed-input contacts](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Full-window projection/contact identity, scalar range and fixed-j Lipschitz/Fourier argument; no change in the original probability law or unrestricted conclusion. |
| support | [Actual reuse and classical limits](#bounded-source-and-reuse-account) | Fixed-source and fixed-proof interfaces, exact newly proved signed-energy/aligned/cap steps and complete retained inspection limits. |
| review | [Independent entire contact-aligned finding](../audits/reviews/Yin_R_G0856_v1.md#contact-aligned-return-whole-independent-finding) | Entire CA1--CA33 and Sections1--9, actual two-family inputs, every signed energy/quadrature/sample/cap case, full original costs and centered supports, both uniform strips and every sequence/actual-degree implication, with all retained source and review-relationship limits. |


---
author: Yin
---

# An actual square-log weighted Salem family and a degree-over-log width criterion

Human author Yin.
Phase_bands proposed the square-log balance after the exact localized comparison, checked its integer thresholds and constants, and reconstructed the new source, original-window and probability-law interfaces below.
This is author development, not independent review.
The adopted C696 localized mechanisms and C693 fixed torus patch are used only after their actual premises are established for the new last prime and degree.
The prior C684/C696 polynomial families remain unchanged.
No native computation, prime enumeration or new source-proof audit is used.

## Statement

Fix the actual composite even integer and first prime

    K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))),
    j in Z, j>=4K, a_j=min{p prime:p>(j+1)K},
    L_j=K+a_j+2, M_j=floor(a_j/4), X_j=L_j+1.

Define the NEW last-prime schedule by

    ell_j=min{ell positive integer:2^ell>=X_j},
    c_j=min{p prime:p>X_j^2 ell_j},
    d_j=c_j+L_j-2=K+a_j+c_j.                             (SQ1)

The threshold X_j^2 ell_j is an integer product BEFORE prime selection.
For e=(K,a_j,c_j), w=(1,1,2), define

    Qraw_j(x)=(x^2-1)product_(i=1)^3(x^e_i-1)
       -(x/2)sum_(i=1)^3 w_i(x^e_i+1)product_(l!=i)(x^e_l-1),
    P_j(x)=Qraw_j(x)/(x-1)^2.                            (SQ2)

Then P_j is the ACTUAL monic integral irreducible Salem minimal polynomial, of even degree d_j and trace0, with no additional cyclotomic factor.
Its exterior root beta_j satisfies2<beta_j<4, and

    log2<m(P_j)=log beta_j<log4.                         (SQ3)

Use ALL d=d_j relation columns in the ORIGINAL2d coefficient coordinates:

    A_rel,j=[P_j,xP_j,...,x^(d-1)P_j],
    G_j=A_rel,j^T A_rel,j, Pi_j=A_rel,j G_j^-1 A_rel,j^T,
    v_n(z)=(1,z,...,z^(n-1))^T,
    h_orig,j=v_(2d)^*Pi_j v_(2d)/(2d),
    f_(j,tau)=(1-h_orig,j/tau)_+, tau>0.                 (SQ4)

All Haar measures have mass1 and Fourier coefficients use negative exponentials.
Write ||f||_A=sum_(n in Z)abs(fhat(n)) and W_*(f)=sum_(n!=0)abs(fhat(n)).
For each fixed j,tau the cap has finite A norm.
At every actual circle root it equals1, and for tau<=1 its margin above Haar mean is at least1/2.
For positive integers N, Fej_N(s)=N^-1 abs(sum_(r=0)^(N-1)exp(irs))^2 is the probability-normalized Fejer kernel used below.

### New original law, exact comparison and localized finite return

Define the fixed weighted torus data

    R(z,u)=(z^K-1)(u-1), S(z,u)=2(z^K u-1),
    Acal=-(z^2-1)R-zR+zS/2,
    Bcal= (z^2-1)R-zR-zS/2,
    U=Acal/Bcal off common zeros, U=0 at common zeros,
    V(z,u)=U(z^-1,u^-1), h(z,u,w)=(1+Re(wV(z,u)))/2,
    F_tau=(1-h/tau)_+,
    iota_j(z)=(z,z^a_j,z^c_j),
    H_j(gamma)=gamma_0+a_j gamma_1+c_j gamma_2.            (SQ5)

For every t in T^3 let mu_(j,t) be the pushforward of circle Haar by z to t*iota_j(z).
These are the NEW correlated original and translated laws.
For every actual j and0<eta<=1,

    mu_(j,t){h<=eta}<=2sqrt(eta) for EVERY t in T^3.       (SQ6)

Product Haar has the smaller constant1, and finite common-zero conventions affect none of these integrals.

Suppress j in a,c,d,L,M,X,ell and set

    A(z)=Acal(z,z^a), B(z)=Bcal(z,z^a),
    A_0=A/(z-1), B_0=B/(z-1),
    varphi(z)=(A/B)(z^-1) after cancellation,
    h_phase=(1+Re(z^c varphi))/2,
    epsilon_j=(4L-3)/(2d)+[1+pi L(5+2log c)]/(2c),
    E_sq=3(3+3pi),
    delta_*=[28(1+60pi)]^-2,
    C_obs=2/delta_*, C_stab=33C_obs+3.

The actual new original comparison is

    ||h_orig,j-h_phase||_1<=epsilon_j<=E_sq M^-1,
    ||f_(j,tau)-F_tau composed with iota_j||_1
                           <=min{1,C_stab epsilon_j},
    ||f_(j,tau)-F_tau composed with iota_j||_2
                           <=min{1,sqrt(C_stab epsilon_j)} (SQ7)

for EVERY tau>0.
The complete actual missing cyclic sample, pole and full inverse Gram are retained in the proof; no old-family projection is substituted.

Use the identical C693 fixed patch at x_*=(pi/K,pi), with real phase

    phi(t,s)=2arctan([4sin t+cot(Kt/2)+cot(s/2)]/2),
    -Hess(phi)>=lambda I on closed B_(4delta)(x_*),
    0<delta<min{pi/(8K),pi/8},
    chi(x)=exp[-1/(1-abs(x-x_*)^2/delta^2)] on B_delta(x_*),
    chi=0 elsewhere, periodically extended.

Set the same fixed constants

    s_chi=||chi||_2^2>0,
    D_phi,l=sup_(B_delta(x_*))abs(partial_l phi), l=1,2,
    B_der=[sum_(l=1)^2(||partial_l chi||_2+D_phi,l||chi||_2)^2]^(1/2),
    C_chi=||(1-Delta)^2 chi||_1, Delta=partial_t^2+partial_s^2,
    A_chi=13C_chi,
    C_osc>=1 with abs((chi U^k)hat(n))<=C_osc/k for all k>=1,n in Z^2,
    C_0=ceil(max{2,2B_der/sqrt(s_chi),24sqrt(3)C_osc C_chi/s_chi}),
    a_loc=3s_chi/(4C_osc), B_chi=||chi||_infinity,
    S_loc=sum_(l=1)^2||partial_l chi||_infinity+B_chi(D_phi,1+D_phi,2+1),
    C_sm=3pi sqrt(2)S_loc.

All k in the phase-power assertions here are positive integers.
The existence and source scope of C_osc, and the ENTIRE localized square mass

    sum_(abs(p),abs(q)<=C_0k)abs((chi U^k)hat(p,q))>=a_loc k

are the c-independent C693 conclusions at precisely the same K and torus phase.
Put

    b(z,u)=chi(z^-1,u^-1), b_j(z)=b(z,z^a_j),
    Phi_tau=b F_tau, f_loc,j,tau=b_j f_(j,tau),
    B_sq(j,tau)=B_chi min{1,sqrt(C_stab epsilon_j)}
                                  +2C_sm M^-1 tau^-1/4.

For M>=2,0<tau<=1/64 and EVERY finite Gamma in the closed integer box[-M,M]^3,

    sum_(gamma in Gamma)
      abs(fhat_loc,j,tau(H_j(gamma))-Phihat_tau(gamma))
                       <=sqrt(card(Gamma))B_sq(j,tau).   (SQ8)

All signs, zero, empty sets and closed-box endpoints are included.
The full new original comparison, TWO identically zero regularization differences for this exact localized phase and TWO paid L2 smoothings are included.
The original-function multiplication expense is

    ||b_j||_A<=A_chi,
    W_*(f_loc,j,tau)<=A_chi[W_*(f_(j,tau))+1].            (SQ9)

### Entire support, uniform strip and actual degree

For0<tau<=1/64 define

    L_tau=floor(1/(4sqrt(tau))),
    Gamma_tau={(p,q,k):1<=k<=L_tau,abs(p),abs(q)<=C_0 k},
    N_tau=sum_(k=1)^(L_tau)(2C_0 k+1)^2
                                       <=(2C_0+1)^2 L_tau^3,
    C_mass=3a_loc/(1024pi),
    C_err=(2C_0+1)/8 max{B_chi sqrt(C_stab E_sq),2C_sm},
    H=M^2tau.

If M>=2 and C_0 L_tau<=M, every original image in Gamma_tau is positive and distinct, and

    W_*(f_(j,tau))>=tau^-1/2/A_chi
                  *[C_mass-C_err(H^-1/4+H^-1/2)]-1.     (SQ10)

Define

    H_sq=max{1,C_0^2/16,(4C_err/C_mass)^4,(4C_err/C_mass)^2},
    M_sq=ceil(max{2,8sqrt(H_sq)}),
    j_sq=max{4K,ceil(4M_sq/K)}.

For EVERY actual j with M_j>=M_sq and EVERY width in the entire nonempty strip

    H_sq M_j^-2<=tau<=1/64,

one has

    W_*(f_(j,tau))>=C_mass tau^-1/2/(2A_chi)-1.           (SQ11)

Every j>=j_sq satisfies the actual M threshold.

For EVERY actual j, write T_M=1+log M_j and Z_j=d_j/(1+log d_j).
The genuine minimal-polynomial degree satisfies

    16M_j^2 T_M<d_j<2^12 M_j^2 T_M,
    M_j^2<Z_j<2^12 M_j^2.                               (SQ12)

Set D_sq=2^12 H_sq.
For every positive shrinking sequence tau_j->0 with

    [d_j/(1+log d_j)]tau_j>=D_sq eventually,             (SQ13)

the bound(SQ11) holds eventually and W_*(f_(j,tau_j)) tends to infinity.
For every FIXED h>=D_sq, taking the actual widths tau_j=h(1+log d_j)/d_j gives

    W_*(f_(j,tau_j))>=C_mass sqrt(d_j/(1+log d_j))
                                      /(2A_chi sqrt(h))-1
                                                   ->infinity. (SQ14)

No monotonicity is required, and entry times for arbitrary sequences may depend on the sequence.
The logarithm is paid by the actual prime schedule and is retained in the final criterion; no criterion involving d_j tau_j alone is asserted.
The actual log2<m(P_j)<log4 interval, full2d window and source-inspection limits remain.
No smaller-height optimum, every-degree theorem, near-one family or unrestricted G0001 completion follows.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Complete argument

### 1. Actual arithmetic and the entire closed alias box

The fixed K is even and at least16.
From j>=4K and a>(j+1)K one has a>4K^2, a>2K and L>4K^2.
Since M=floor(a/4),

    4M<=a<4M+4<=6M,
    4M<L<X<=2a<=12M, X>4K^2>=1024.                      (SQ15)

Here X=K+a+3<=2a because a>K+3.
The new threshold X^2 ell is an integer at least2.
Accepted integer Bertrand gives

    X^2 ell<c<2X^2 ell,
    c>X^2>a^2>L, c<d=c+L-2<2c.                         (SQ16)

Thus K,a,c are pairwise coprime, with a,c distinct odd primes exceeding K.
The composite nature of K is preserved.

For the NEW character H_j, a>2M and c>a^2>2M(1+a).
For a nonzero delta in the CLOSED[-2M,2M]^3 box, its highest nonzero coordinate therefore dominates all lower coordinates in H_j(delta), so H_j(delta)!=0.
Every difference between two closed-M indices is in that closed2M box.
Consequently there are no coefficient aliases for a closed-M polynomial and any tested closed-M coefficient, and all original images of such a set are distinct.
On every translated new circle, every nonconstant closed-M character has mean zero; translation multiplies it by a unit scalar.
These exact finite facts precede every nonlinear approximation below.

### 2. Weighted source, actual cyclotomic removal, integrality and minimality

Use the same weighted hypersurface

    h_w(x_0,x_1,x_2,x_3)=2(x_0^2-1)product_i(x_i-1)
                       -x_0 sum_i w_i(x_i+1)product_(l!=i)(x_l-1),
    w=(1,1,2).

Its defining support has size at most24 and diameter at most sqrt7 in dimension4.
The accepted general MS05 Theorem8/Corollary9 therefore gives the sufficient common torsion-coset exponent

    K_3^*=product_(p prime,p<=24)p * lcm(1,...,38416),
    38416=7^4*4^2.

The actual K is a multiple of K_3^*, since its prime product extends to48 and its lcm endpoint exceeds38416.
This uses the general source result on this weighted hypersurface; it does not apply the source's unweighted odd-q construction, which is not an accepted input.

The weighted torsion classification, proved in C678 and reapplied here, is independent of a,c.
Exactly one powered coordinate equal1 is impossible on h_w=0, because the one remaining summand has nonzero weight.
Two powered coordinates identically1 give the cosets B_il={x_i=x_l=1}.
For any other torsion coset with x_0 nonconstant, no powered coordinate is identically1.
Choose an integer monomial one-parameter specialization avoiding the finitely many nonzero exponent hyperplanes, oriented with positive x_0 exponent.
The identity

    x_0-x_0^-1=(1/2)sum_i w_i(x_i+1)/(x_i-1)

would then have unbounded left side and bounded right side as the parameter tends to infinity.
This contradiction shows that the nonconstant-x_0 maximal torsion cosets are exactly the B_il.
The case of exactly one identically1 coordinate is already excluded at a generic point by the polynomial equation.

Apply this to a torsion zero of h_w(x,x^K,x^a,x^c).
If its maximal coset is B_il, the actual pairwise coprimality of Section1 forces x=1.
Otherwise x_0 is constant on that coset and its value is killed by K.
Then x^K=1, and the impossibility of exactly one powered coordinate1 forces a second, again giving x=1.
Thus1 is the only root of unity of Qraw.
At1, its first term has order4, and its weighted sum has exact order2 with nonzero coefficient-(ac+Kc+2Ka).
The complete cyclotomic divisor is therefore precisely(x-1)^2.

Modulo2, the weighted summands reduce to the same product with total weight4, so their sum is divisible by2 over the integers.
Thus Qraw is integral, and division by the monic(x-1)^2 gives integral P.
For circular interlacing take

    p(x)=product_(e in {K,a,c})(x^e-1)/(x-1)^2,
    q_0/p=(1/2)[(x^K+1)/(x^K-1)+(x^a+1)/(x^a-1)
                                             +2(x^c+1)/(x^c-1)].

The denominator is monic with simple circle zeros and p(1)=0.
The positive residues prevent cancellation; the parity and monic-division calculation make q_0 integral as well.
The accepted general Proposition6 preserves circular interlacing under this positive rational sum, and Proposition5(a) applies to P=(x^2-1)p-xq_0.
It gives a Salem minimal factor, or the reciprocal quadratic alternative, possibly times a cyclotomic product.
The exact torsion exclusion removes the additional factors, while the actual degree greater than2 excludes the quadratic alternative.
Thus this NEW P is the irreducible Salem minimal polynomial.

The leading terms of Qraw are x^(K+a+c+2)-2x^(K+a+c+1).
After division by(x-1)^2, P has degree d=K+a+c and next coefficient0.
Its trace is0 and its degree is even, since K is even and a,c are odd.
At the exterior root beta, the weighted equation gives beta-beta^-1>2, hence beta>1+sqrt2>2.
Since each exponent is at least2, comparison with(beta^2+1)/(beta^2-1) gives (beta+beta^-1)^2-2(beta+beta^-1)-4<=0, and in particular beta+beta^-1<4.
Therefore beta<4 and m(P)=log beta, proving(SQ3).
No smallest-prime or every-large-degree source theorem is used.

### 3. The new full2d matrix, actual cyclic mode and interpolation expense

The fixed Acal,Bcal specialize to integral degree-L polynomials A,B with Qraw=A+x^cB.
A has constant coefficient1 and leading coefficient-1, while B has constant coefficient-1 and leading coefficient1.
Their sum is-2x(x^K-1)(x^a-1).
At exactly one powered root the S term is nonzero, and Section1 coprimality leaves1 as their only common root.
Moreover A_0(1)=K+a and B_0(1)=-(K+a), so their common factor is exactly x-1.
The fixed torus equal-modulus identity gives abs(A)=abs(B) on the circle; after cancellation neither A_0 nor B_0 has a circle zero.
Thus the new actual inverse phase varphi is smooth unimodular with varphi(1)=-1.

In the SAME2d coordinates, the raw relation matrix of Qraw has2d-deg Qraw=d-2=c+L-4 independent columns.
Its range is contained in the full d-column P relation space with codimension2, giving projection difference of rank2.
For the c-cycle shift S_c e_i=e_(i+1 mod c), form

    V_c=[A(S_c);B(S_c);0_(2L-4)-by-c].

The first c raw columns agree with V_c in its first c-L columns, so the matrix difference has rank at most L and the projection difference at most2L.
The remaining L-4 raw columns enlarge the range by exactly L-4.
Projection differences have operator norm at most1; therefore

    ||Pi_j-Pi_V||_trace<=2+2L+(L-4)=3L-2.                (SQ17)

The NEW c is coprime to K,a, so every nontrivial c-th root mode has nonzero equal-modulus A,B values.
Only the mode1 vanishes, and V_c has rank c-1.
Its two diagonal blocks are(I_c-J_c/c)/2, and its upper off-diagonal block is

    Pi_V,12(i,l)=(1/(2c))sum_(omega^c=1)
                                    U(omega,omega^a)omega^(l-i).

The other block is the adjoint and the final2L-4 coordinates vanish.
The actual trivial-mode sample is0, not the smooth inverse-phase value-1.
Hence, with the usual probability-normalized Fejer kernel,

    q(exp(it))=(1/c)sum_(r=1)^(c-1)
                  varphi(exp(2pi i r/c))Fej_c(t-2pi r/c),
    abs(q)<=1, deg_Fourier(q)<=c-1,
    v_(2d)^*Pi_V v_(2d)=c-Fej_c+c Re(z^c q).

If k_V=1-v^*Pi_Vv/(2d), direct subtraction gives

    k_V-(1-Re(z^c q))/2
        =[(d-c)/(2d)](1+Re(z^c q))+Fej_c/(2d)>=0.

Its integral is(L-1)/(2d), because z^c q has zero constant coefficient.
Combining this with(SQ17) and integral vv^*=I yields

    ||(1-h_orig,j)-(1-Re(z^c q))/2||_1<=(4L-3)/(2d).     (SQ18)

The original phase has total variation2pi(K+a-1)=2pi(L-3), by the lift checked in Section4 below.
The general finite grid-arc interpolation argument used in C684 applies to EVERY integer c and this actual smooth phase: arc multiplicity is at most c abs(t)/(2pi)+1 and the first angular Fejer moment is at most pi(1/2+log c)/c.
It bounds the full-grid interpolation error by V(varphi)[5/4+(log c)/2]/c.
Replacing the sample-1 at1 by the actual0 adds Fej_c/c and costs1/c in L1.
Consequently

    ||q-varphi||_1<=[1+pi L(5+2log c)]/c.

Adding half this cost to(SQ18) gives the first original inequality in(SQ7), before its numerical M bound.
All matrix dimensions, samples, phases and probabilities used here are those of the NEW c,d.

### 4. Full new inverse Gram, genuine pole and width-uniform cap comparison

All new relation columns are independent, so G_j is positive definite.
Let G_d(z)=v_d(z)^*G_j^-1v_d(z)>0.
The exact identities are

    h_orig,j=abs(P)^2G_d/(2d),
    h_phase=abs(z-1)^2 abs(P)^2/[4abs(A_0)^2],
    r=2abs(A_0)^2G_d/[d abs(z-1)^2],
    h_orig,j=r h_phase away from z=1.                   (SQ19)

The identity is derived without division by P and is valid at other phase contacts by the displayed expression.
P(1)!=0 gives h_0=h_orig,j(1)>0, so the ratio has a genuine pole at1.

For the actual first two exponents,

    D(t)=4sin t+cot(Kt/2)+cot(at/2),
    U_j(exp(it))=(2+iD)/(2-iD),
    varphi(exp(it))=exp(i psi(t)), psi(0)=pi,
    psi'=-4D'/(4+D^2)>0,
    Theta=ct+psi, Theta'>=c.

Here D'<=4-(K+a)/2<0 and the positive-residue pole extensions are smooth.
Pairwise coprimality gives K+a-1 distinct poles per circle, each complementary interval contributing2pi to the inverse-phase lift.
Thus Theta increases by2pi(c+L-3)=2pi(d-1), checking the variation used in Section3.

Put v_0=c+2/(1/K+1/a) and T(t)=2abs(A_0(exp(it)))^2G_d(exp(it)).
This numerator is real even and has Fourier degree at most d+L-2.
Finite cosine division gives

    r=u+sigma,
    sigma=(T(t)-T(0))/[4d sin^2(t/2)],
    u=kappa/[4sin^2(t/2)], kappa=T(0)/d=4h_0/v_0^2<=4/c^2,
    deg_Fourier(sigma)<=d+L-3=c+2L-5<3c.                 (SQ20)

The complete factor1/d in the polynomial remainder is retained.
The limit defining kappa is used only for its coefficient, not as an unproved joint local approximation.
For abs(t)<=pi/c, the elementary cotangent remainder gives

    D=R_*/t+E_*(t), R_*=2(1/K+1/a)>=2/K,
    abs(E_*)<=(L+4)abs(t),
    (L+4)t^2/R_*<pi^2/(4K)<1/2.

The sufficient inequalities c>L and L>4K^2 were proved for the NEW threshold in Section1.
Therefore p(t)=Theta(t)-pi=ct+2arctan(2/D(t)) satisfies

    c abs(t)<=abs(p(t))<=c abs(t)+4K abs(t)<=3c abs(t).

The extra phase cell I_0=[-t_*,t_*] has pi/(3c)<=t_*<=pi/c and probability at most1/c.
On it h_phase u<=9pi^2/4; outside it exact integration gives integral u<=12/(pi^2c)<2/c.
Thus integral h_phase u<32/c.

Every interval of length2pi/c has at most one pole from each cotangent family, because K,a<c.
Its inverse-phase increment is at most6pi and its Theta increment at most8pi.
The same seven-band estimate gives contact fraction at most7sqrt(delta) for h_phase<=delta, with endpoints and branch crossings included.
The fixed finite reproduction kernel2Fej_(2n)-Fej_n has derivative norm at most10n and gives V(T)<=60pi c||T||_1 for every complex trigonometric polynomial of degree at most3c.
Cell means and variation then bound its contact integral by7sqrt(delta)(1+60pi)||T||_1.
At delta=delta_* this is at most one quarter of the full L1 norm, and absorption yields

    ||T||_1<=C_obs integral h_phase abs(T).

Apply this to the actual sigma-1, using h_phase abs(sigma-1)<=abs(h_orig,j-h_phase)+h_phase u.
One obtains ||sigma-1||_1<=C_obs(epsilon_j+32/c).
For eta_r=abs(r-1)/max{1,r}, extended by1 at1, the central cell costs at most1/c and its complement at most ||sigma-1||_1+2/c.
Since epsilon_j>=(4L-3)/(2d)>1/c, its integral is at most(33C_obs+3)epsilon_j=C_stab epsilon_j.
The elementary scalar inequality

    abs((1-rx/tau)_+-(1-x/tau)_+)<=abs(r-1)/max{1,r}

for x,r>=0,tau>0 proves the all-width L1 cap comparison in(SQ7).
The cap difference is bounded by1, so its L2 norm is at most the square root of that L1 bound.
This proves the complete NEW original comparison without a uniform lower ratio or discarded pole.

### 5. Exact logarithmic payment and every new translated law

The displayed epsilon, using c<d and L>=1, satisfies

    epsilon_j<=(3+3pi)(L/c)(1+log c).

Now ell>=log X/log2 and ell<=X.
Since c<2X^2 ell and X>=1024,

    1+log c<1+log2+3log X<4log X,
    (1+log c)/ell<4log2<3.

Consequently epsilon_j<3(3+3pi)L/X^2<E_sq/M, proving the numerical bound in(SQ7).
The actual sample/interpolation logarithm has been paid by ell in the NEW prime threshold, not removed from its source estimate.

For an arbitrary translate write z=exp(i(t+alpha)), u=exp(i(at+beta)), w=exp(i(ct+gamma)).
Off its poles, the exact weighted inverse phase is

    V(z,u)=(2-iD_(alpha,beta))/(2+iD_(alpha,beta)),
    D_(alpha,beta)=4sin(t+alpha)+cot(K(t+alpha)/2)+cot((at+beta)/2).

Its derivative is at most4-(K+a)/2<0 on every regular interval.
There are N<=K+a distinct poles, with positive residues2/K,2/a, or their sum at a coincidence.
On each complementary interval D decreases from positive infinity to negative infinity.
The inverse Cayley phase extends smoothly through each pole with derivative limit4 divided by its residue and acquires precisely one turn per interval.
Its total winding is N, including all coincident-pole cases.
The common-zero convention changes only finitely many points of a translated circle and changes no integral.

The full phase Theta=ct+gamma+psi has derivative at least c and total increment2pi(c+N), with c+N<=c+K+a=d<2c by Section1.
Hence change of the increasing phase variable proves

    mu_(j,t){h<=eta}<=[(c+N)/c]*(2/pi)arcsin(sqrt(eta))
                                                   <=2sqrt(eta).

This establishes(SQ6) on EVERY NEW translated law, without original-coordinate independence.
Under product Haar, conditioning on w gives the smaller constant1.

### 6. Matched localized mechanisms and the complete finite support

The torus U, K and fixed patch are unchanged by the new c.
Thus C693's all-frequency localized estimate and its full square CB15 apply exactly, and the same constants chi,C_0,a_loc,A_chi are valid.
The new original probe b_j uses the actual first prime a, and the new f_loc uses the new full projection of(SQ4).
The all-width NEW comparison of Section4 bounds its original L2 error by B_chi min{1,sqrt(C_stab epsilon_j)}.

The same fixed function Phi_tau vanishes on neighborhoods of all common zeros and is globally Lipschitz for every fixed positive tau.
Its coordinate-path derivative envelopes for0<tau<=1/64 are

    [||partial_l chi||_infinity+B_chi D_phi,l]
                            tau^-1/2 1_(h<=tau), l=1,2,
    B_chi tau^-1/2 1_(h<=tau), l=3.

Both the amplitude derivatives and the third coordinate are included.
The NEW translated-law contact bound of Section5 gives their L2 norms at most sqrt(2) times the displayed constants times tau^-1/4 on every intermediate translation.
Use the exact squared-Fejer kernel

    P_M=Fej_N^2/[(2N^2+1)/(3N)], N=floor(M/2)+1,

which has mass1, is positive, has closed support[-M,M] and first shortest-angle moment at most3pi/M.
Coordinate-path FTC and L2 integral triangle therefore bound EACH of the original-circle and torus smoothing errors of Q_tau=Phi_tau*(P_M tensor P_M tensor P_M) by C_sm M^-1 tau^-1/4.
The TWO regularization differences are identically zero because the exact localized function itself is used as the intermediate function.
This asserts no zero regularization cost for the unlocalized torus cap.
Thus the sum of the original-circle and torus comparison norms is at most B_sq.

Q_tau is finite with closed-M support.
The NEW closed2M argument in Section1 identifies its selected original and torus coefficients exactly and gives distinct original characters.
Finite Bessel and finite Cauchy--Schwarz now prove(SQ8) for every finite Gamma, with all five terms and all endpoints included.
These are the generic localized mechanisms of C696, with every changed-family premise supplied here; its old original-law theorem has not been used by renaming c.

The absolutely convergent torus Fourier series of b has coefficient sum at most A_chi.
After u=z^a substitution, possible aliases only decrease the triangle upper bound, so ||b_j||_A<=A_chi.
Since0<=f<=1 and f has finite A norm, coefficient convolution gives

    W_*(b_jf)<=||b_jf||_A<=A_chi||f||_A<=A_chi(W_*(f)+1),

proving(SQ9), including all original probe coefficients and possible zero-frequency aliases.

For the ENTIRE Gamma_tau, product-Haar w integration gives

    Phihat_tau(p,q,k)=ghat_tau(k)(bV^k)hat(p,q).

Here g_tau is the scalar cap and abs(ghat_tau(k))>=3sqrt(tau)/(8pi) for1<=k<=L_tau.
The factor bV^k is the simultaneous inversion of chi U^k, so its closed square of radius C_0 k has mass at least a_loc k.
Consequently the entire selected torus mass is at least

    [3a_loc sqrt(tau)/(8pi)]sum_(k=1)^(L_tau)k
        >=[3a_loc sqrt(tau)/(16pi)]L_tau^2
        >=C_mass tau^-1/2.

The last inequality uses L_tau>=1/(8sqrt(tau)) when tau<=1/64.
Different k give disjoint triples, and the exact count satisfies N_tau<=(2C_0+1)^2 L_tau^3.
Under C_0 L_tau<=M all selected coordinates are in the closed-M box, every original frequency is at least c-M(1+a)>0, and all images are distinct.
No maximum-coefficient or sparse-subset replacement is made.

Using sqrt(N_tau)<=(2C_0+1)/(8tau^(3/4)), the ENTIRE returned error before division by A_chi is at most

    (2C_0+1)/8
       *[B_chi sqrt(C_stab E_sq)M^-1/2 tau^-3/4
                                     +2C_sm M^-1 tau^-1].

Relative to tau^-1/2 these are exactly H^-1/4 and H^-1/2 for H=M^2tau.
Apply(SQ8), subtract the full error from the mass, and then apply(SQ9) to obtain(SQ10), including its additive loss-1.

### 7. Uniform finite strip and genuine degree-over-log endpoint

For H>=H_sq, the two error terms times C_err are each at most C_mass/4.
The same threshold gives C_0 L_tau<=C_0 M/(4sqrt(H))<=M.
Thus the whole support and error budget hold at the actual critical equality.
M>=M_sq ensures M>=2 and H_sq M^-2<=1/64, so the strip is nonempty and(SQ11) follows uniformly.
For j>=j_sq, a_j>(j+1)K>4M_sq implies the actual floor M_j>=M_sq.

The arithmetic(SQ15)--(SQ16) gives

    16M^2<X^2<=144M^2,
    1+log M<ell<5+2log M<=5(1+log M),
    X^2 ell<c<d<2c<4X^2 ell.

Therefore16M^2 T_M<d<2880M^2 T_M<2^12 M^2 T_M.
Using log(1+log M)<=log M for M>=1,

    1+log d<1+12log2+3log M<12T_M.

Also1+log d>T_M.
Dividing the exact genuine-degree inequalities gives

    Z=d/(1+log d)>(16/12)M^2>M^2,
    Z<2^12 M^2,

proving(SQ12).
These are actual minimal-polynomial degree bounds, not a replacement by raw degree or c.

If Z_j tau_j>=D_sq=2^12 H_sq then M_j^2tau_j>H_sq.
For every positive shrinking sequence with that eventual property, its M_j eventually meets M_sq and its tau_j eventually meets1/64.
Then(SQ11) applies eventually and tends to infinity.
For fixed h>=D_sq, substitution tau_j=h/Z_j gives(SQ14) directly.
No sequence-independent entry index or monotonicity assumption is introduced.

Finally rank(Pi_j)=d_j in2d_j coordinates gives integral h_orig,j=1/2 and0<=h_orig,j<=1.
At an actual circle root all relation polynomials vanish under evaluation, hence h_orig,j=0 and f_(j,tau)=1.
For tau<=1, f_(j,tau)<=1-h_orig,j proves the stated margin.
For fixed j,tau, the cap is continuous piecewise smooth with square-integrable derivative, because the original trigonometric level equation has finitely many zeros unless it is identically constant.
Integration by parts, derivative Bessel and sum_(n!=0)n^-2<infinity give its finite A norm.

## Source and scope boundary

The new arithmetic, source eligibility, actual minimality/degree, raw/cyclic/sample/full-Gram/pole and every translated-law premise are reconstructed above for the new square-log last prime.
MS05-U001 supplies only its accepted general torsion-coset exponent and circular-interlacing interfaces; the odd weighted adaptation remains the locally proved C678 mechanism, explicitly reapplied here.
The unweighted even-q source construction is not silently extended, and the actual K remains composite.
Integer Bertrand is used at its already accepted C356/C217/Mig78 statement depth for the new INTEGER threshold, with no fresh proof audit or prime enumeration.
C684 is used as a checked home of the generic finite grid interpolation and original geometric mechanisms, not as a theorem about this different polynomial family.
C696 supplies the generic localized paths, finite coefficient and probe-removal mechanisms after their new-law hypotheses have been proved.
C693 supplies only the identical c-independent torus patch and complete localized power square, retaining Tao26-U003v2's primary-statement/applicability depth and unreviewed full-source proof.
C637 supplies the exact positive finite kernel, and C681 the direct scalar cap harmonics.
No new global unlocalized regularization theorem is needed or claimed.
The final logarithm is part of the actual prime schedule and cannot be dropped from(SQ13).
The positive interval log2<m(P_j)<log4, the still-open smaller-height and optimality questions, and the unrestricted Task boundary remain explicit.

## Assessment history

### Decision square-log-family-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T06:26 |
| status | open |
| reason | Register the complete NEW square-log weighted actual family, rebuilding source/killer/parity/minimality/degree, all original2d raw/cyclic/sample/Gram/pole/observability premises, and every translated contact/finite-return law. Exact matched localization and the full selected support give a fixed-large degree-over-log width criterion, with all five costs, probe expense and explicit thresholds retained. The author-checked result awaits fresh independent whole review; logarithmic degree normalization, positive Mahler interval, source depths and unrestricted limits remain. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire new actual square-log theorem](#statement) | SQ1--SQ14: exact integer prime schedule and actual Salem minimal polynomial/full2d law, complete comparison/localized return, full support, explicit uniform strip and genuine-degree fixed-height/sequence conclusion. |
| argument | [Complete new-family reconstruction](#complete-argument) | Sections1--7/SQ15--SQ20: new arithmetic and source eligibility, every raw/cyclic/sample/Gram/pole and translated-law premise, matched localized five-cost return, all support/cardinality/error constants and genuine-degree conversion. |
| dependency | [Accepted general source interfaces](../audits/literature/MS05/Yin_U001.md#ms05-u001) | General torsion-coset exponent and circular-interlacing statements at their retained inspection depth; the weighted adaptation and actual new-family eligibility are supplied here. |
| dependency | [Integer Bertrand input](Yin_C_G0356_v1.md#argument) | Accepted integer n>=2 prime interval n<p<2n at its retained C217/Mig78 scope, applied to the new integer X_j^2 ell_j. |
| dependency | [Weighted source adaptation](Yin_C_G0678_v1.md#decision-whole-reviewed-2026-10-24) | The c-independent weighted hypersurface classification, parity and equal-modulus identities only; no square-family original-law conclusion is substituted. |
| dependency | [Checked generic original mechanisms](Yin_C_G0684_v1.md#complete-argument) | Finite grid-arc Fejer interpolation and elementary pole/cell/observability mechanisms, with every changed c,d hypothesis and original matrix reconstructed above. |
| dependency | [Adopted localized comparison mechanisms](Yin_C_G0696_v1.md#decision-whole-reviewed-2026-10-25) | Generic exact-localization path estimates, finite L2 coefficient comparison and full original probe multiplication after NEW original/translated-law and alias premises are established here. |
| dependency | [Fixed actual torus patch](Yin_C_G0693_v2.md#decision-whole-reviewed-2026-10-24) | The identical K and c-independent phase, fixed bump/constants, all-frequency localized estimate and complete localized square CB15; no old actual-family return is used by renaming c. |
| dependency | [Exact scalar harmonics](Yin_C_G0681_v1.md#decision-whole-reviewed-2026-10-24) | Direct scalar cap harmonic lower bound for0<tau<=1/64 and1<=k<=floor(1/(4sqrt(tau))). |
| dependency | [Positive finite kernel](Yin_C_G0637_v1.md#complete-argument) | Exact squared-Fejer probability normalization, positivity, closed support and first angular moment. |
| support | [Retained stationary-phase source scope](../audits/literature/Tao26/Yin_U003.md#tao26-u003) | Existing primary-statement/applicability depth underlying the unchanged C693 patch; no new numerical implicit constant or whole-source proof audit. |
| support | [Source and scope boundary](#source-and-scope-boundary) | New actual-family reconstruction versus matched generic reuse, retained prime logarithm and positive Mahler interval, and no unrestricted completion. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T06:36 |
| status | proved |
| reason | Adopt the entire fixed square-log actual-family theorem after main reading of complete C701 and fresh isolated whole R922. The new integer prime schedule, weighted source/minimality, original full2d matrix and missing cyclic sample, complete Gram pole with its 1/d remainder, all translated laws and five-cost localized return are checked. The full support yields the fixed-large degree-over-log width criterion with exact degree, constants and sequence quantifiers. Source inspection depths, the positive Mahler interval and all unrestricted Task limits remain; no logarithm-free criterion or near-one family is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire new actual square-log theorem](#statement) | SQ1--SQ14: exact integer prime schedule and actual Salem minimal polynomial/full2d law, complete comparison/localized return, full support, explicit uniform strip and genuine-degree fixed-height/sequence conclusion. |
| argument | [Complete new-family reconstruction](#complete-argument) | Sections1--7/SQ15--SQ20: new arithmetic and source eligibility, every raw/cyclic/sample/Gram/pole and translated-law premise, matched localized five-cost return, all support/cardinality/error constants and genuine-degree conversion. |
| dependency | [Accepted general source interfaces](../audits/literature/MS05/Yin_U001.md#ms05-u001) | General torsion-coset exponent and circular-interlacing statements at their retained inspection depth; the weighted adaptation and actual new-family eligibility are supplied here. |
| dependency | [Integer Bertrand input](Yin_C_G0356_v1.md#argument) | Accepted integer n>=2 prime interval n<p<2n at its retained C217/Mig78 scope, applied to the new integer X_j^2 ell_j. |
| dependency | [Weighted source adaptation](Yin_C_G0678_v1.md#decision-whole-reviewed-2026-10-24) | The c-independent weighted hypersurface classification, parity and equal-modulus identities only; no square-family original-law conclusion is substituted. |
| dependency | [Checked generic original mechanisms](Yin_C_G0684_v1.md#complete-argument) | Finite grid-arc Fejer interpolation and elementary pole/cell/observability mechanisms, with every changed c,d hypothesis and original matrix reconstructed above. |
| dependency | [Adopted localized comparison mechanisms](Yin_C_G0696_v1.md#decision-whole-reviewed-2026-10-25) | Generic exact-localization path estimates, finite L2 coefficient comparison and full original probe multiplication after NEW original/translated-law and alias premises are established here. |
| dependency | [Fixed actual torus patch](Yin_C_G0693_v2.md#decision-whole-reviewed-2026-10-24) | The identical K and c-independent phase, fixed bump/constants, all-frequency localized estimate and complete localized square CB15; no old actual-family return is used by renaming c. |
| dependency | [Exact scalar harmonics](Yin_C_G0681_v1.md#decision-whole-reviewed-2026-10-24) | Direct scalar cap harmonic lower bound for0<tau<=1/64 and1<=k<=floor(1/(4sqrt(tau))). |
| dependency | [Positive finite kernel](Yin_C_G0637_v1.md#complete-argument) | Exact squared-Fejer probability normalization, positivity, closed support and first angular moment. |
| support | [Retained stationary-phase source scope](../audits/literature/Tao26/Yin_U003.md#tao26-u003) | Existing primary-statement/applicability depth underlying the unchanged C693 patch; no new numerical implicit constant or whole-source proof audit. |
| support | [Source and scope boundary](#source-and-scope-boundary) | New actual-family reconstruction versus matched generic reuse, retained prime logarithm and positive Mahler interval, and no unrestricted completion. |
| review | [Fresh independent whole square-log finding](../audits/reviews/Yin_R_G0922_v1.md#whole-square-log-independent-finding) | Entire fixed statement and proof, all changed-family premises, full original laws and costs, every finite endpoint and degree/sequence quantifier; exact external-input inspection depth and limitations retained. |


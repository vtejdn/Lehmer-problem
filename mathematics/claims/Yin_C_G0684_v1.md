---
author: Yin
---

# A logarithmically balanced weighted Salem family and its twelve-seventeenths degree criterion

Human author Yin.
Root proposed the new17/8 logarithmic prime schedule to balance the complete weighted-band costs.
Phase_bands independently checked the finite constants, reconstructed all source and original-law premises at the new actual degree, and completed the uniform support, threshold and sequence argument.
Both are contributors, not independent reviewers.
The fixed phase and band theorem of adopted C681 are used only at their actual torus scope.
The polynomials and original laws of C678/C681 are not changed in place.
No native computation, prime enumeration, new source acquisition or original-source proof audit is used.

## Statement

For integers j>=4K use the SAME actual composite integer K, first prime and scale

    K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))),
    a_j=min{p prime:p>(j+1)K}, L_j=K+a_j+2,
    M_j=floor(a_j/4).

Define the NEW integer thresholds and last prime by

    n_j=min{n positive integer:n^8>=(L_j+1)^17},
    ell_j=min{ell positive integer:2^ell>=L_j+1},
    c_j=min{p prime:p>n_j ell_j}, d_j=c_j+L_j-2.           (WL1)

Thus n_j=ceil((L_j+1)^(17/8)) and ell_j=ceil(log_2(L_j+1)), and their product is taken BEFORE selecting the prime.
For e=(K,a_j,c_j) and weights w=(1,1,2), set

    Qraw_j(x)=(x^2-1)product_(i=1)^3(x^e_i-1)
       -(x/2)sum_(i=1)^3 w_i(x^e_i+1)product_(l!=i)(x^e_l-1),
    P_j(x)=Qraw_j(x)/(x-1)^2.                              (WL2)

The full weighted source applicability and factor argument below prove that P_j is its ACTUAL monic integral irreducible Salem minimal polynomial, of even degree d_j and trace0, with no additional cyclotomic factor.
Its exterior root beta_j satisfies

    2<beta_j<4, log2<m(P_j)=log beta_j<log4.                (WL3)

Use ALL d=d_j relation columns in the ORIGINAL2d coordinates:

    A_rel,j=[P_j,xP_j,...,x^(d-1)P_j], G_j=A_rel,j^T A_rel,j,
    Pi_j=A_rel,j G_j^-1 A_rel,j^T, v_n(z)=(1,z,...,z^(n-1))^T,
    h_orig,j=v_(2d)^*Pi_j v_(2d)/(2d),
    k_j=1-h_orig,j, f_(j,tau)=(1-h_orig,j/tau)_+.

All Haar measures have mass1, angular variation is unnormalized, and Fourier coefficients use negative exponentials.
Write nu_r for probability Haar on T^r.
Write W_*(f)=sum_(n!=0)abs(fhat(n)).
For each fixed j,tau>0 this sum is finite.
For0<tau<=1 every actual circle root of P_j has cap value1 and value minus Haar mean at least1/2.

For z,u,w in T define the unchanged weighted torus phase and cap

    R(z,u)=(z^K-1)(u-1), S(z,u)=2(z^K u-1),
    Acal=-(z^2-1)R-zR+zS/2,
    Bcal= (z^2-1)R-zR-zS/2,
    g_0=abs(Acal)^2+abs(Bcal)^2, Ncal=2Acal conjugate(Bcal),
    U=Acal/Bcal off common zeros, U=0 at common zeros,
    V(z,u)=U(z^-1,u^-1), g(z,u)=g_0(z^-1,u^-1),
    h(z,u,w)=(1+Re(wV))/2, F_tau=(1-h/tau)_+,
    iota_j(z)=(z,z^a_j,z^c_j),
    H_j(gamma)=gamma_0+a_j gamma_1+c_j gamma_2.             (WL4)

For EVERY t in T^3, mu_(j,t) is the pushforward of circle Haar under z to t*iota_j(z).
These are the NEW original and translated laws; no independence is assumed under them.

### Actual original comparison and complete finite return

Suppress j, writing a,c,d,L,M for its actual values.
Let A(z)=Acal(z,z^a), B(z)=Bcal(z,z^a), A_0=A/(z-1), B_0=B/(z-1), and varphi(z)=(A/B)(z^-1) after cancellation of their exact common factor z-1.
The phase is smooth and unimodular with varphi(1)=-1.
Set

    h_phase=(1+Re(z^c varphi))/2,
    E=[1+pi L(5+2log c)]/c,
    epsilon_j=(4L-3)/(2d)+E/2,
    E_bal=4(3+3pi),
    delta_*=[28(1+60pi)]^-2,
    C_obs=2/delta_*, C_stab=33C_obs+3.

For EVERY actual j,

    ||h_orig,j-h_phase||_1<=epsilon_j<=E_bal M^(-9/8).      (WL5)

For EVERY tau>0 on the SAME original circle,

    ||f_(j,tau)-(1-h_phase/tau)_+||_1<=min{1,C_stab epsilon_j},
    ||f_(j,tau)-(1-h_phase/tau)_+||_(3/2)
                         <=min{1,(C_stab epsilon_j)^(2/3)}. (WL6)

The actual interpolation logarithm in E remains; it is paid by ell_j inside the prime threshold.
The full new Gram pole and local observability expenses are retained in the proof.

Define fixed angular derivative constants from this unchanged two-coordinate phase:

    D_l=||partial_l Acal||_infinity+||partial_l Bcal||_infinity, l=1,2,
    G_K=sqrt(||g||_infinity),
    C_w=6pi[1+10(D_1+D_2)+2(G_K+1)],
    C_s=3pi[18*96^(2/3)(D_1+D_2)+4^(2/3)],
    C_2=512C_w+2C_s.

For a probability measure mu let N_mu(v)=sup_(E measurable,mu(E)>0)mu(E)^(-1/3)integral_E abs(v)dmu.
For actual M>=max{2,C_w}, put rho=(C_w/M)^2 and

    V_rho=Ncal(z^-1,u^-1)/(g+rho),
    h_rho=(1+Re(wV_rho))/2, F_(tau,rho)=(1-h_rho/tau)_+,
    Fej_N(t)=N^-1 abs(sum_(r=0)^(N-1)exp(irt))^2,
    P_M=Fej_N^2/[(2N^2+1)/(3N)], N=floor(M/2)+1,
    Q_(tau,rho)=F_(tau,rho)*(three-coordinate product of P_M),
    B_bal(j,tau)=min{1,(C_stab epsilon_j)^(2/3)}
                                          +C_2 M^-1 tau^(-1/6).

For every0<tau<=1/64,

    N_nu1(f_(j,tau)-Q_(tau,rho) composed with iota_j)
        +N_nu3(F_tau-Q_(tau,rho))<=B_bal(j,tau).            (WL7)

For EVERY finite Gamma in the CLOSED integer box[-M,M]^3,

    sum_(gamma in Gamma)
       abs(fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma))
          <=5 card(Gamma)^(2/3)B_bal(j,tau).               (WL8)

The original images are distinct; empty sets, zero and signed indices and all endpoints are included.
The original comparison, TWO regularizations and TWO smoothings are all paid on the NEW actual laws, including rho/tau>1.

### Complete weighted bands and uniform critical enlargement

For each k,m>=1 let t_(k,m) be the unique point in(0,1/(8K)) such that

    b(t)=4sin t+cot(Kt/2), b(t_(k,m))=32sqrt(km),
    theta_(k,m)(t)=(k-m)arctan b(t)+(k+m)arctan(b(t)/3),
    n_(k,m)=floor(theta_(k,m)'(t_(k,m))+1/2),
    C_band=ceil(320000pi K).

These are the ACTUAL fixed-torus C681 centers, independent of a_j,c_j, and abs(n_(k,m))<=25K(k+m).
For the following finite-support conclusions assume the actual M>=max{2,C_w}.
For0<tau<=1/64 and integer J>=1 set

    L_tau=floor(1/(4sqrt(tau))),
    R=ceil(C_band sqrt(L_tau)J^(5/6)),
    Gamma_(tau,J)={(-p,m,k):1<=k<=L_tau,1<=m<=J,
                                  abs(p-n_(k,m))<=R},
    N_sel=L_tau J(2R+1)
                 <=3(C_band+1)L_tau^(3/2)J^(11/6).         (WL9)

Whenever

    L_tau,J<=M, 25K(L_tau+J)+R<=M,                         (WL10)

every selected original frequency is strictly positive and distinct, and

    W_*(f_(j,tau))>=3log(J+1)/(65536pi)
                               -5N_sel^(2/3)B_bal(j,tau). (WL11)

The ENTIRE returned error is at most

    (5/4)[3(C_band+1)]^(2/3)J^(11/9)
       *[(C_stab E_bal)^(2/3)M^(-3/4)tau^(-1/2)
                                 +C_2 M^-1 tau^(-2/3)].  (WL12)

Define explicit thresholds and the complete constant

    M_bal=ceil(max{32,C_w,(75K/4)^4,(75K)^(88/61),
                                      [3(C_band+1)/2]^(8/5)}),
    j_bal=max{4K,ceil(4M_bal/K)},
    C_bal=(5/4)[3(C_band+1)]^(2/3)
                                max{(C_stab E_bal)^(2/3),C_2}.

For EVERY actual j with M=M_j>=M_bal and EVERY real H,tau such that

    2<=H<=M^(3/2)/64, M^(-3/2)H<=tau<=1/64,              (WL13)

the choice J=floor(H^(9/44)) satisfies all(WL10) and gives

    W_*(f_(j,tau))>=27log H/(2883584pi)
                              -C_bal[H^(-1/4)+H^(-5/12)]. (WL14)

This estimate is uniform over the ENTIRE strip, which is nonempty at the displayed threshold.
Every integer j>=j_bal satisfies M_j>=M_bal.

### Actual degree and every positive shrinking sequence

For EVERY actual j, with T_M=1+log M_j,

    M_j^(17/8)T_M<d_j<2^15 M_j^(17/8)T_M,
    M_j^(17/8)/16<d_j/(1+log d_j)<2^15 M_j^(17/8).         (WL15)

Thus for EVERY positive shrinking sequence tau_j->0 satisfying

    (d_j/(1+log d_j))^(12/17)tau_j->infinity,              (WL16)

one has W_*(f_(j,tau_j))->infinity.
Equivalently M_j^(3/2)tau_j tends to infinity.
No monotonicity or divergence speed is imposed, and sequence entry into(WL13) may depend on the sequence.
The degree logarithm remains attached to the actual prime schedule; no pure d_j^(12/17)tau_j criterion is asserted.
The previous square-schedule weighted theorems remain at their own actual degrees and laws.
The result retains log2<m(P_j)<log4, the complete original2d window and exact source scope, and supplies no bounded-H endpoint, every-degree theorem, optimality, near-one input or unrestricted G0001 completion.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Complete argument

### 1. Exact prime thresholds, actual hypotheses and the entire alias box

K is even and at least16, and j>=4K gives a>(j+1)K>4K^2.
In particular a>2K and K+a+3<=2a.
For M=floor(a/4), one has4M<=a<4M+4<=6M, so

    4M<L<L+1<=2a<=12M, L>4K^2.                            (WL17)

Put X=L+1, x=X^(17/8), n=ceil x and ell=ceil(log_2 X).
The integer n satisfies x<=n<2x and the actual integer prime threshold is n ell.
Integer Bertrand therefore gives

    x ell<c<2n ell<4x ell,
    c>X^2>L, c<d=c+L-2<2c.                               (WL18)

Thus a,c are distinct primes exceeding K, neither divides K, and K,a,c are pairwise coprime although K itself is composite.
These are all source and cyclic eligibility requirements, checked for the actual new prime.

For the new original character H_j, the strict inequalities

    a>2M, c>a^2>2M(1+a)

hold for every permitted j.
The highest nonzero coordinate in any nonzero delta in[-2M,2M]^3 then strictly dominates the sum of all lower weighted coordinates, proving H_j(delta)!=0.
This is the punctured CLOSED2M box, including endpoints.
Every difference between a closed-M polynomial support index and a closed-M coefficient index lies there, proving exact finite coefficient return and injectivity on that box.
For every translated new circle, each nonconstant closed-M character has mean zero; translation supplies only a unit scalar.
These mean and coefficient facts precede all nonlinear approximation arguments.

### 2. New actual weighted polynomial and retained source hypotheses

The relevant hypersurface remains the SAME weighted polynomial

    h_w(x_0,x_1,x_2,x_3)
       =2(x_0^2-1)product_(i=1)^3(x_i-1)
         -x_0 sum_(i=1)^3 w_i(x_i+1)product_(l!=i)(x_l-1),
    w=(1,1,2).

Its support has at most24 exponent vectors and diameter at most sqrt7 in ambient dimension4.
The accepted general MS05 Theorem8/Corollary9 gives the sufficient common torsion-coset exponent

    K_3^*=product_(p prime,p<=24)p * lcm(1,...,38416),
    38416=7^4*4^2.

The fixed actual K is a multiple of K_3^*: its prime product extends to48 and its lcm endpoint exceeds38416.
This remains an application to this weighted hypersurface, not the unweighted odd-q source construction.

The weighted classification argument does not involve a or c.
A point with exactly one powered coordinate equal1 cannot satisfy h_w=0, because the unique nonzero summand has nonzero weight.
A torsion coset with two powered coordinates identically1 lies in the corresponding B_il={x_i=x_l=1}.
For any other hypothetical coset with x_0 nonconstant, no powered coordinate is identically1; choose an integer monomial one-parameter specialization avoiding all nonzero exponent hyperplanes, with the sign making the x_0 exponent positive.
Then the identity

    x_0-x_0^-1=(1/2)sum_i w_i(x_i+1)/(x_i-1)

has unbounded left side and bounded right side as the parameter tends to infinity, a contradiction.
The case of exactly one powered coordinate identically1 is excluded by the same polynomial equation at a generic point.
Hence the maximal nonconstant-x_0 torsion cosets are exactly those B_il; this is the local weighted adaptation, as proved in C678 and explicitly applied here.

Every torsion zero of h_w(x,x^K,x^a,x^c) lies in a maximal torsion coset containing it.
On a B_il, pairwise coprimality from Section1 forces x=1.
Otherwise x_0 is constant on the coset, so its value is killed by K; then x^K=1 supplies a powered coordinate1, and the impossibility of exactly one forces another, again giving x=1.
Thus1 is the only root of unity in Qraw.
At1, Qraw has exact order2 with coefficient-(ac+Kc+2Ka), while its first term has order4.
Its complete cyclotomic divisor is exactly(x-1)^2.

Modulo2 the weighted summands reduce to the same product with total weight4, making Qraw integral.
Monic division by(x-1)^2 leaves integral P.
For the positive rational sum use

    p(x)=product_(e in {K,a,c})(x^e-1)/(x-1)^2,
    q_0/p=(1/2)[(x^K+1)/(x^K-1)+(x^a+1)/(x^a-1)
                                             +2(x^c+1)/(x^c-1)].

The denominator is monic with simple circle zeros and p(1)=0; positive residues prevent cancellation, and q_0 is integral by the same parity and monic division.
The accepted general circular-interlacing Proposition6, including positive scalar multiples, and Proposition5(a) therefore produce a Salem minimal factor with possible cyclotomic factors or the reciprocal quadratic alternative.
The exact torsion exclusion removes the extra factors and degree greater than2 excludes the quadratic alternative.
This proves that the NEW P is the actual irreducible Salem minimal polynomial.

The leading terms of Qraw are x^(K+a+c+2)-2x^(K+a+c+1).
After division by(x-1)^2 the next coefficient is0 and degree d=K+a+c is even, so the trace is0.
At the exterior root beta, the weighted identity has total weight4, giving beta>1+sqrt2>2 and beta+beta^-1<=4.
Thus beta<4 and m(P)=log beta, proving(WL3).
No every-large-degree theorem, prime K substitution or weighted theorem absent from the inspected source has been invoked.

### 3. Full original2d ranks, cyclic samples and interpolation cost

The fixed Acal,Bcal specialize to integral polynomials A,B of degree L with Qraw=A+x^cB.
A has constant coefficient1 and leading coefficient-1; B has constant coefficient-1 and leading coefficient1.
Their sum is-2x(x^K-1)(x^a-1).
At exactly one powered root the S term is nonzero, and pairwise coprimality leaves1 as their only common root.
The values [A/(x-1)](1)=K+a and[B/(x-1)](1)=-(K+a) prove that their exact common factor is x-1.
The fixed torus identity gives equal moduli of Acal and Bcal; their common zeros are exactly z^K=u=1.
After cancellation A_0,B_0 have no circle zero and the actual inverse phase has varphi(1)=-1.

In the SAME2d coordinates the raw relation matrix has2d-deg Qraw=c+L-4=d-2 independent columns.
Its range lies inside the full d-column original relation space with codimension2, so the projection difference has rank2.
With S_c e_i=e_(i+1 mod c), form

    V_c=[A(S_c);B(S_c);0_(2L-4)-by-c].

The first c raw columns agree with V_c in its first c-L columns, so their difference has rank at most L and their projection difference has rank at most2L.
The remaining L-4 raw columns extend the raw range by exactly L-4.
Using the operator norm bound1 for projection differences gives

    ||Pi_j-Pi_V||_trace<=2+2L+(L-4)=3L-2.                 (WL19)

The actual new c is coprime to K,a.
Thus all nontrivial c-th root modes have nonzero equal-modulus A,B values, and only the mode1 vanishes.
The range has rank c-1, diagonal blocks(I_c-J_c/c)/2, and off-diagonal block

    Pi_V,12(i,l)=(1/(2c))sum_(omega^c=1)
                                   U(omega,omega^a)omega^(l-i).

The other block is its adjoint, and the final2L-4 coordinates vanish.
The trivial-mode phase sample is0, not the smooth value-1.
Consequently the actual interpolant is

    q(exp(it))=(1/c)sum_(r=1)^(c-1)
                       varphi(exp(2pi i r/c))Fej_c(t-2pi r/c),
    abs(q)<=1, deg_Fourier(q)<=c-1.

Direct evaluation gives

    v^*Pi_Vv=c-Fej_c+c Re(z^c q),
    k_V-(1-Re(z^c q))/2
        =((d-c)/(2d))(1+Re(z^c q))+Fej_c/(2d)>=0.

Here k_V=1-v^*Pi_Vv/(2d).
The correction has integral(L-1)/(2d), because z^c q has zero constant coefficient.
The trace bound(WL19), with integral vv^*=I, proves

    ||k_j-(1-Re(z^c q))/2||_1<=(4L-3)/(2d).               (WL20)

The phase variation is exactly2pi(K+a-1)=2pi(L-3), independently of c, as seen from the two-cotangent lift in Section4.
The general grid-arc/Fejer proof applies to this new integer c: its arc multiplicity is at most c abs(t)/(2pi)+1 and its angular moment at most pi(1/2+log c)/c.
For the full-grid interpolant this yields error at most V(varphi)(5/4+(log c)/2)/c.
Replacing its sample-1 at1 by0 adds Fej_c/c, of norm1/c.
Therefore ||q-varphi||_1<=E, giving the first inequality in(WL5).
The original smooth phase and the torus convention differ only at1, a null point on this actual circle.

### 4. New full-Gram pole, local geometry and original cap stability

The entire new relation matrix has independent columns and real coefficients.
Its positive definite G_j gives

    G_d=v_d^*G_j^-1v_d>0,
    h_orig=abs(P)^2G_d/(2d),
    h_phase=abs(z-1)^2 abs(P)^2/[4abs(A_0)^2],
    r=2abs(A_0)^2G_d/[d abs(z-1)^2], h_orig=r h_phase.     (WL21)

This identity is obtained without dividing by P, and P(1)!=0 implies h_0=h_orig(1)>0.
The original ratio has its actual pole at1.
Write U_j=A/B after cancellation.
The phase itself has not changed with c:

    D(t)=4sin t+cot(Kt/2)+cot(at/2),
    U_j(exp(it))=(2+iD)/(2-iD),
    varphi(exp(it))=exp(i psi(t)), psi(0)=pi,
    psi'=-4D'/(4+D^2)>0,
    Theta=ct+psi, Theta'>=c.

D'<=4-(K+a)/2<0, and positive-residue pole extensions are smooth.
There are K+a-1 poles over one turn, each regular interval contributing2pi to the inverse-phase lift.
Thus the new Theta increment is2pi(c+L-3)=2pi(d-1).

Set v_0=c+2/(1/K+1/a).
The real even trigonometric numerator T(t)=2abs(A_0(exp(it)))^2G_d(exp(it)) has degree at most d+L-2.
Finite cosine division gives the exact decomposition

    r=u+sigma,
    sigma=(T(t)-T(0))/[4d sin^2(t/2)],
    u=kappa/[4sin^2(t/2)], kappa=T(0)/d=4h_0/v_0^2<=4/c^2,
    deg_Fourier(sigma)<=d+L-3=c+2L-5<3c.                  (WL22)

The factor1/d is retained in the actual polynomial remainder.
The coefficient identity uses the limit at0 only; uniform local control follows from explicit estimates at the new c.
For abs(t)<=pi/c, R_*=2(1/K+1/a)>=2/K and the cotangent remainder give

    D=R_*/t+E_*(t), abs(E_*)<=(L+4)abs(t),
    (L+4)t^2/R_*<pi^2/(4K)<1/2.

Here c>L and L>4K^2 from Section1 are exactly the sufficient hypotheses.
Thus

    p(t)=Theta(t)-pi=ct+2arctan(2/D(t)),
    c abs(t)<=abs(p(t))<=c abs(t)+4K abs(t)<=3c abs(t).

The extra phase cell I_0=[-t_*,t_*] therefore has pi/(3c)<=t_*<=pi/c and probability at most1/c.
On it h_phase u<=9pi^2/4; outside it exact pole integration gives integral u<=12/(pi^2c)<2/c.
Hence integral h_phase u<32/c.

Every interval of length2pi/c has at most one pole from each cotangent family because K,a<c.
Its inverse-phase increment is at most6pi, and its Theta increment at most8pi.
The weaker seven-band estimate gives contact fraction at most7sqrt(delta) for h_phase<=delta,0<delta<=1, with branches, poles and endpoints included.

The generic finite reproduction kernel2Fej_(2n)-Fej_n reproduces the closed[-n,n] interval and has derivative norm at most10n.
Thus every complex trigonometric polynomial T of degree at most3c satisfies V(T)<=60pi c||T||_1.
Cell means and cell variation then bound its contact-set integral by7sqrt(delta)(1+60pi)||T||_1.
With delta=delta_* this is at most one quarter of ||T||_1, so absorption gives

    ||T||_1<=C_obs integral h_phase abs(T).

Apply it to sigma-1, using h_phase abs(sigma-1)<=abs(h_orig-h_phase)+h_phase u.
It follows that ||sigma-1||_1<=C_obs(epsilon_j+32/c).
For eta_r=abs(r-1)/max{1,r}, define eta_r(1)=1.
It is at most1 inside I_0 and at most abs(sigma-1)+u outside, hence its integral is at most C_obs(epsilon_j+32/c)+3/c.
Since epsilon_j>=(4L-3)/(2d)>1/c, this is at most C_stab epsilon_j.
The scalar cap inequality abs((1-rx/tau)_+-(1-x/tau)_+)<=eta_r, for x,r>=0,tau>0, proves the L1 comparison(WL6).
The difference is bounded by1, so its strong3/2 norm is at most the2/3 power of its L1 norm.
All quantities are those of the new original G_j; no lower-ratio premise or old-family projection is substituted.

### 5. Exact logarithmic payment and the finite epsilon bound

The displayed epsilon_j, with c<d and L>=1, obeys

    epsilon_j<=(3+3pi)(L/c)(1+log c).

Section1 gives X=L+1>4K^2>=1024, ell>=log X/log2 and ell<=X.
Using c<4X^(17/8)ell,

    1+log c<1+log4+(25/8)log X
                 <(33/8)log X<5log X,
    (1+log c)/ell<5log2<4.

The middle step uses1+log4<log16<=log X, valid for every permitted actual j.
Consequently

    (L/c)(1+log c)<4L/X^(17/8)
                   <4L^(-9/8)<4M^(-9/8).

This proves the complete(WL5) with the stated E_bal.
The prime multiplier ell has paid the interpolation logarithm; no new unweighted logarithm-free estimate is asserted.

### 6. Every translated new law and all five return costs

The fixed torus amplitude and its pointwise derivative identities are unchanged: they depend only on K and(z,u), not on a_j,c_j.
C678's two-sided3/4 amplitude theorem in particular gives integral r_s dnu_2<=12s^(3/4) for0<s<=1, where r_s=s/(g+s).
We now establish its needed original-law consequences from the NEW alias theorem of Section1.

For0<rho<=1, s>=rho and0<eta<=1, let V_eta=eta/(eta+h_rho).
The equal-modulus derivative algebra gives

    sum_(l=1)^2 abs(partial_l r_s)/r_s<=(D_1+D_2)/sqrt(s),
    sum_(l=1)^3 abs(partial_l W)/W
       <=[10(D_1+D_2)+2(G_K+1)]/sqrt(rho),
                                    W=V_eta or r_s V_eta.

These smooth quantities include the common-zero convention and all s>=rho, even s>1.
P_M is positive of mass1, closed support[-M,M] and first angular moment at most3pi/M.
For I_W^*=sup_t integral W dmu_(j,t)<=1, finite convolution has exactly its torus mean on every new translated circle, by Section1.
Coordinate-path FTC and the moment bound give

    I_W^*<=integral W dnu_3
          +[3pi(10(D_1+D_2)+2(G_K+1))/(M sqrt(rho))]I_W^*.

At M sqrt(rho)=C_w the bracket is less than1/2, and the r_s-only argument also applies whenever M sqrt(s)>=C_w.
The independent w integration is used ONLY under product Haar:

    integral_w V_eta=eta/sqrt((eta+1/2)^2-(a_g/2)^2)<=sqrt(eta),
    a_g=g/(g+rho).

Thus on EVERY new translated law, and with no larger constants on the torus,

    integral r_s<=24s^(3/4) if s<=1 and M sqrt(s)>=C_w,
    integral V_eta<=2sqrt(eta),
    integral r_s V_eta<=24sqrt(eta)s^(3/4), s>=rho,
    mu{h_rho<=eta,g<=s}<=96sqrt(eta)s^(3/4), s>=rho.       (WL23)

For s>1 the trivial torus amplitude integral<=1 proves the same product bound.
Thus every dyadic shell used below is covered, and no nonlinear mean equality or original-coordinate independence has been assumed.

For w_tau=1_(h_rho<=tau)(g+rho)^(-1/2), (WL23) gives the tail bound96sqrt(tau)t^(-3/2): for t<=1 use the contact bound4sqrt(tau), for1<t<=rho^(-1/2) use s=t^-2, and for larger t the event is empty.
The direct event-norm layer-cake lemma therefore gives

    N_mu(w_tau)<=3*96^(2/3)tau^(1/3),
    N_mu(1_(h_rho<=tau))<=[4sqrt(tau)]^(2/3).

The pointwise contact derivative envelopes are6D_l tau^-1/2 w_tau for l=1,2 and tau^-1/2 1_(h_rho<=tau) for l=3.
Clipped FTC holds on every coordinate path by its open contact components.
Integrate first over each measurable event, then along paths and the positive kernels; every intermediate translation is in the family already covered by(WL23).
The resulting cost is C_s M^-1 tau^-1/6 for EACH of the two smoothings.

For regularization D_cap=F_tau-F_(tau,rho)>=0, its nonzero set lies in h<=tau, and

    D_cap<=min{1,rho/[2tau(g+rho)]}.

At common zeros both caps vanish in the stated tau range.
Set lambda=rho/tau without requiring lambda<=1.
The region g<rho costs at most48rho^(3/4) in integral D_cap^(3/2).
On disjoint shells s<=g<2s,s=2^k rho, (WL23) at2s and eta_s=tau+rho/(2s)<1 bounds the active shell probability.
The middle-shell sum rho<=s<=lambda is at most1792rho^(3/4)tau^-1/4, and the high-shell sum s>lambda at most384rho^(3/4)tau^-1/4, by the complete C678 geometric sums.
Their applicability here uses only(WL23), now proved for ALL new translations and all s>=rho.
The coefficient48+1792+384=2224<4096 gives EACH regularization norm at most256sqrt(rho)tau^-1/6.
Both lambda>1 and shells with2s>1 are included.

Strong3/2 controls N_mu by Holder, and the event-first triangle inequality now proves(WL7) from(WL6), the TWO regularizations and TWO smoothings.
Their complete four-cost sum is512sqrt(rho)tau^-1/6+2C_s M^-1tau^-1/6=C_2 M^-1tau^-1/6.

The finite weak Fourier lemma proved in C678 is a general probability-space statement: any N orthonormal modulus-one characters have coefficient sum at most5N^(2/3)N_mu(v).
Its direct height truncation/Bessel proof supplies this constant without a strong Hausdorff--Young premise.
For the new original circle the selected characters are distinct by the CLOSED2M alias theorem; the torus characters are also distinct.
The finite Q_(tau,rho) has closed-M support and its coefficients return exactly, so applying that lemma to the two errors in(WL7) proves(WL8), including all signs, zero, ties, empty sets and endpoints.

### 7. Fixed-torus bands, whole new support and critical strip

Only the c-independent torus portion of adopted C681 is used here.
Its actual U is exactly(WL4), with identical K, so its Mobius coefficient formula, witness b(t0)=32sqrt(km), local modulation center and positive-kernel proof give

    sum_(abs(p-n_(k,m))<=R)abs((U^k)hat(p,-m))>=1/(1024m)

for every integer R>=C_band sqrt(k)m^(5/6).
Its scalar cap coefficient calculation and inverse-coordinate signs are also unchanged:

    Fhat_tau(-p,m,k)=ghat_tau(k)(U^k)hat(p,-m),
    abs(ghat_tau(k))>=3sqrt(tau)/(8pi), 1<=k<=L_tau.

Since L_tau sqrt(tau)>=1/8, the ENTIRE Gamma_(tau,J) has mass at least3log(J+1)/(65536pi).
The sets for different k,m are disjoint triples, and the common radius ceiling gives exactly the count(WL9).
These statements are about the fixed torus and contain neither the old original c nor its degree.

Under(WL10), abs(p)<=25K(L_tau+J)+R<=M and k,m are also in the closed-M interval.
The new original character returns all these indices distinctly by Section1, with

    H_j(-p,m,k)=-p+a_j m+c_j k>=c_j-M>0.

Applying the NEW finite budget(WL8) to the full set gives(WL11).
No original-family consumer from C681 has been imported by replacing its c.

The count gives N_sel^(2/3)<=[3(C_band+1)]^(2/3)L_tau J^(11/9).
Use L_tau<=tau^-1/2/4 and(WL5) to obtain the complete(WL12).
The min with1 may be bounded by the indicated power without any additional smallness condition.

For(WL13), J=floor(H^(9/44))>=1 and all ceilings are controlled by

    L_tau<=(1/4)M^(3/4)H^(-1/2)<=M^(3/4)/4,
    J<=H^(9/44)<=M^(27/88),
    sqrt(L_tau)J^(5/6)<=(1/2)M^(3/8)H^(-7/88),
    R<=(1/2)(C_band+1)M^(3/8).                           (WL24)

Here ceil(C_band x)<=(C_band+1)x is valid because x=sqrt(L_tau)J^(5/6)>=1.
Thus L_tau,J<=M and

    25K(L_tau+J)+R
      <=(25K/4)M^(3/4)+25K M^(27/88)+(C_band+1)M^(3/8)/2.

The three explicit thresholds in M_bal bound the respective terms by M/3, so the entire center-plus-radius condition holds uniformly.
M>=C_w supplies the finite-return premise, and M>=32 gives M^(3/2)/64>=2^(3/2)>2, ensuring a nonempty H interval.
For j>=j_bal, a_j>(j+1)K>4M_bal, hence the actual M_j threshold holds while j>=4K is retained.

Finally J^(11/9)<=H^(1/4).
In(WL12), substituting tau>=M^-3/2 H gives first factor

    M^-3/4 M^((3/2)(1/2))H^(1/4-1/2)=H^-1/4,

and second factor

    M^-1 M^((3/2)(2/3))H^(1/4-2/3)=H^-5/12.

Both M powers cancel exactly; there is no remaining logarithm because Section5 already paid it with the actual prime multiplier.
The definition of C_bal bounds both complete coefficients.
Since J+1>H^(9/44), the full positive term is at least27log H/(2883584pi), proving(WL14).

### 8. Actual degree/logarithm comparison and arbitrary sequence entry

From4M<X<=12M<16M and x=X^(17/8),

    M^(17/8)<x<2^9 M^(17/8).

The actual integer logarithmic multiplier obeys

    1+log M<ell<5+2log M<=5(1+log M).

The lower bound follows from ell>=log_2 X>2+log M/log2, while the upper follows from ceil y<=y+1, X<16M and1/log2<2.
Combining these with x ell<c<d<2c<8x ell gives

    M^(17/8)T_M<d<40*2^9 M^(17/8)T_M<2^15 M^(17/8)T_M.

These are bounds for the genuine minimal-polynomial degree, not c or the raw degree.
Let T_d=1+log d.
The lower bound implies T_d>=T_M.
The upper bound, with log(1+log M)<=log M for M>=1, gives

    T_d<1+15log2+(25/8)log M<16T_M.

Dividing the two degree estimates by these bounds proves(WL15).
Raising its second line to12/17 shows that(d/(1+log d))^(12/17) is bounded above and below by positive fixed multiples of M^(3/2).
Thus(WL16) is equivalent to H_j^enl=M_j^(3/2)tau_j tending to infinity.

For any such positive shrinking sequence, eventually M_j>=M_bal, H_j^enl>=2 and tau_j<=1/64.
Also H_j^enl<=M_j^(3/2)/64, so all(WL13) conditions hold with H=H_j^enl.
The main term of(WL14) diverges and both error terms tend to zero, however slowly H_j^enl increases.
The entry index can depend on the sequence, and no monotonicity is needed.

The original rank-d projection has integral h_orig=1/2 and lies pointwise in[0,1].
At each actual circle root P vanishes under all relation-column evaluations, giving h_orig=0 and cap value1.
For0<tau<=1 the cap is at most1-h_orig, proving the margin.
For fixed j,tau the cap is continuous piecewise smooth with square-integrable derivative, because its trigonometric level equation is either constant or has finitely many zeros.
Integration by parts and derivative Bessel with sum_(n!=0)n^-2 finite prove absolute Fourier summability.
No uniform moving-width claim is inferred from this fixed-input derivative statement.

## Source, reuse and scope boundary

The retained MS05-U001 general torsion-exponent and circular-interlacing statements apply at their existing primary-statement/selected-proof depth.
The weighted classification and actual construction are the project deduction of C678, explicitly rechecked here for the new eligible prime; its unweighted EVEN-q source restriction is not waived.
The actual composite K is unchanged, and no original Mann/Schmidt or whole-source proof audit is added.
Integer Bertrand is used only at the existing accepted C356/C217/Mig78 statement depth, with the new product threshold an integer before use.
The original2d rank/cyclic/sample/Gram/pole and all new probability-law premises have been rebuilt in Sections1--6; no old-family theorem is extended merely by renaming c.
C678's fixed-torus amplitude and general pointwise/event/finite Fourier mechanisms are reused after their exact new-law hypotheses are verified.
C681 supplies only its unchanged weighted torus bands, scalar harmonic mass and count before the new original return is applied.
C637's positive squared-Fejer normalization and bounded classical source attribution remain unchanged.
The event-norm and height-splitting attribution stays at C678/C668's existing bounded Tao Notes1 account; no general external interpolation theorem is a new premise.
The new degree condition retains the prime multiplier's logarithm and the positive interval log2<m(P_j)<log4.
It supplies neither a near-one family nor an unrestricted G0001 solution.

## Assessment history

### Decision weighted-log-family-open

| Field | Value |
| --- | --- |
| date | 2026-10-24T03:58 |
| status | open |
| reason | Register the complete NEW17/8 logarithmic weighted actual family, with exact source/killer/parity/minimality/degree, full original2d cyclic/sample/Gram/pole and observability reconstruction, every translated-law premise and all five finite costs. The unchanged adopted weighted bands give the complete uniform critical strip and actual(d/(1+log d))^(12/17)tau criterion with explicit constants and arbitrary divergence speed. The author-checked result awaits fresh independent whole review; the degree logarithm, log2..log4, source limits and bounded-H/near-one/unrestricted boundaries remain. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire new weighted-family statement](#statement) | WL1--WL16: exact integer prime schedule, actual minimal polynomial/full2d law and measure, complete original and finite-return constants, entire band support, explicit uniform strip and actual degree/sequence criterion. |
| argument | [Complete new-family reconstruction](#complete-argument) | Sections1--8/WL17--WL24: new source/arithmetic/alias/degree eligibility, all raw/cyclic/sample/pole/observability and translated-law premises, every five-cost/support/threshold exponent and exact sequence entry. |
| dependency | [Accepted general source interface](../audits/literature/MS05/Yin_U001.md#ms05-u001) | General torsion-coset exponent and circular-interlacing statements at retained inspection depth; the odd weighted adaptation is explicitly proved locally, not attributed to unweighted Lemma12. |
| dependency | [Integer Bertrand statement](Yin_C_G0356_v1.md#argument) | Every integer n>=2 has n<p<2n, at the retained bounded source depth; applied to the actual integer n_j ell_j. |
| support | [Prime-source attribution limit](../audits/literature/Mig78/Yin_U001.md#mig78-u001) | Existing length-account attribution, with no new original Bertrand proof inspection. |
| dependency | [Adopted weighted mechanisms](Yin_C_G0678_v1.md#decision-whole-reviewed-2026-10-24) | Weighted hypersurface/source construction, unchanged torus amplitude and general pointwise/event/finite Fourier mechanisms; every new actual c,d and probability-law premise is reconstructed here rather than importing its square-family conclusion. |
| dependency | [Actual weighted torus bands](Yin_C_G0681_v1.md#decision-whole-reviewed-2026-10-24) | Its c-independent exact Mobius coefficient, witness and modulation, entire local bands/scalar mass/count only; its old original-law and degree consumer is not used for the new family. |
| dependency | [Positive finite kernel](Yin_C_G0637_v1.md#complete-argument) | Squared-Fejer normalization, closed support, first angular moment and unchanged finite convolution mechanism. |
| support | [Source and reuse boundary](#source-reuse-and-scope-boundary) | Accepted source depth, new family reconstruction versus fixed torus reuse, retained actual-degree logarithm and positive measure, and no bounded-H or unrestricted conclusion. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T04:15 |
| status | proved |
| reason | The complete fixed WL1--WL24 statement and Sections1--8 proof were directly read, followed by all of fresh isolated R905. Adopt the new weighted logarithmic prime schedule, rebuilt original 2d law, every translated-law premise and all five costs, complete finite bands and uniform strip, and the actual (d/(1+log d))^(12/17) shrinking-width criterion. All source-depth, logarithmic degree, positive-measure, bounded-H and unrestricted-realization limits remain. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire new weighted-family statement](#statement) | WL1--WL16: exact integer prime schedule, actual minimal polynomial/full2d law and measure, complete original and finite-return constants, entire band support, explicit uniform strip and actual degree/sequence criterion. |
| argument | [Complete new-family reconstruction](#complete-argument) | Sections1--8/WL17--WL24: new source/arithmetic/alias/degree eligibility, all raw/cyclic/sample/pole/observability and translated-law premises, every five-cost/support/threshold exponent and exact sequence entry. |
| dependency | [Accepted general source interface](../audits/literature/MS05/Yin_U001.md#ms05-u001) | General torsion-coset exponent and circular-interlacing statements at retained inspection depth; the odd weighted adaptation is explicitly proved locally, not attributed to unweighted Lemma12. |
| dependency | [Integer Bertrand statement](Yin_C_G0356_v1.md#argument) | Every integer n>=2 has n<p<2n, at the retained bounded source depth; applied to the actual integer n_j ell_j. |
| support | [Prime-source attribution limit](../audits/literature/Mig78/Yin_U001.md#mig78-u001) | Existing length-account attribution, with no new original Bertrand proof inspection. |
| dependency | [Adopted weighted mechanisms](Yin_C_G0678_v1.md#decision-whole-reviewed-2026-10-24) | Weighted hypersurface/source construction, unchanged torus amplitude and general pointwise/event/finite Fourier mechanisms; every new actual c,d and probability-law premise is reconstructed here rather than importing its square-family conclusion. |
| dependency | [Actual weighted torus bands](Yin_C_G0681_v1.md#decision-whole-reviewed-2026-10-24) | Its c-independent exact Mobius coefficient, witness and modulation, entire local bands/scalar mass/count only; its old original-law and degree consumer is not used for the new family. |
| dependency | [Positive finite kernel](Yin_C_G0637_v1.md#complete-argument) | Squared-Fejer normalization, closed support, first angular moment and unchanged finite convolution mechanism. |
| support | [Source and reuse boundary](#source-reuse-and-scope-boundary) | Accepted source depth, new family reconstruction versus fixed torus reuse, retained actual-degree logarithm and positive measure, and no bounded-H or unrestricted conclusion. |
| review | [Fresh isolated whole mathematical review](../audits/reviews/Yin_R_G0905_v1.md#whole-weighted-log-family-degree-finding) | Entire actual weighted logarithmic family, all WL1--WL24 and Sections1--8, original law and five costs, complete supports and arbitrary-sequence actual degree criterion. |

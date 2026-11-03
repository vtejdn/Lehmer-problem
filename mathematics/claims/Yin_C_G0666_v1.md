---
author: Yin
---

# An actual prime family with uniform cap stability and degree exponent8/17

Human author Yin.
Root proposed balancing the width-uniform original cap cost against the remaining four costs with the17/11 prime threshold and an actual logarithmic integer multiplier.
Phase_bands independently checked the balance and rebuilt the source, polynomial, full original-law, translated-law, support and degree interfaces below.
Both are contributors, not independent reviewers.
Only the applicable proved mechanisms of C663 and earlier fixed materials are reused, after checking their hypotheses for this NEW family.
No native computation, prime enumeration, new source acquisition or original-source proof audit is used.

## Statement

Fix the actual integer and prime data

    K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))),
    a_j=min{p prime:p>(j+1)K},
    b_j=min{p prime:p>(K+a_j+3)^2},
    L_j=K+a_j+b_j+2, M_j=floor(a_j/4), j>=1,
    n_j=min{n positive integer:n^11>=(L_j+1)^17},
    ell_j=min{ell positive integer:2^ell>=L_j+1},
    c_j=min{p prime:p>n_j ell_j}, d_j=c_j+L_j-3.             (SB1)

Thus the exact threshold is ceil((L_j+1)^(17/11))*ceil(log_2(L_j+1)), with the product taken BEFORE choosing the prime.
For e=(K,a_j,b_j,c_j), set

    Qraw_j(x)=(x^2-1)product_(i=0)^3(x^e_i-1)
       -(x/2)sum_(q=0)^3(x^e_q+1)product_(i!=q)(x^e_i-1),
    P_j(x)=Qraw_j(x)/(x-1)^3.                               (SB2)

At the accepted MS05 arbitrary-distinct-prime construction depth, this P_j is the ACTUAL monic integral irreducible Salem minimal polynomial, of even degree d_j and trace-1, with no further cyclotomic factor.
Its exterior root beta_j and total measure satisfy

    2<beta_j<4, log2<m(P_j)=log beta_j<log4.                 (SB3)

Use ALL d_j relation columns in the ORIGINAL2d_j coordinates:

    A_rel,j=[P_j,xP_j,...,x^(d_j-1)P_j],
    G_j=A_rel,j^T A_rel,j, Pi_j=A_rel,j G_j^-1 A_rel,j^T,
    v_n(z)=(1,z,...,z^(n-1))^T,
    h_orig,j(z)=v_(2d_j)(z)^*Pi_j v_(2d_j)(z)/(2d_j),
    k_j=1-h_orig,j, f_(j,tau)=(1-h_orig,j/tau)_+.

All Haar measures are probability measures, angular variation V is unnormalized, and Fourier coefficients use negative exponentials.
Write W_*(f)=sum_(h in Z,h!=0)abs(fhat(h)).
For each fixed j and tau>0, W_*(f_(j,tau)) is finite.
For0<tau<=1, every unit-circle root of P_j has cap value1 and value minus Haar mean at least1/2.

The fixed-K torus data, unchanged across j, are

    R_tor=(z^K-1)(u-1)(v-1),
    S_tor=(z^K+1)(u-1)(v-1)+(z^K-1)(u+1)(v-1)
                              +(z^K-1)(u-1)(v+1),
    Acal=-(z^2-1)R_tor-zR_tor/2+zS_tor/2,
    Bcal=(z^2-1)R_tor-zR_tor/2-zS_tor/2,
    g_0=abs(Acal)^2+abs(Bcal)^2, Ncal=2Acal conjugate(Bcal),
    U=Acal/Bcal off their common zeros, U=0 on those zeros,
    V(z,u,v)=U(z^-1,u^-1,v^-1), g=g_0(z^-1,u^-1,v^-1),
    h=(1+Re(wV))/2, F_tau=(1-h/tau)_+,
    iota_j(z)=(z,z^a_j,z^b_j,z^c_j),
    H_j(gamma)=gamma_0+a_j gamma_1+b_j gamma_2+c_j gamma_3.

Let nu_1,nu_4 be circle and four-torus Haar.
For EVERY t in T^4, mu_(j,t) is the pushforward of nu_1 through z to t*iota_j(z).
These are the actual new original and translated laws, not independent-coordinate substitutes.

### Exact original budget and width-uniform cap comparison

Suppress j and write L,c,d,M for its actual values.
Let A(z)=Acal(z,z^a,z^b), B(z)=Bcal(z,z^a,z^b), A_0=A/(z-1)^2 and B_0=B/(z-1)^2.
Their exact common factor is(z-1)^2; A_0 and B_0 have no circle zero.
The smooth unimodular phase is varphi(z)=(A/B)(z^-1), with varphi(1)=-1.
Put

    h_phase=(1+Re(z^c varphi))/2, K_phase=1-h_phase,
    Fej_c(t)=c^-1 abs(sum_(r=0)^(c-1)exp(irt))^2,
    theta_l=2pi l/c,
    q(exp(it))=c^-1 sum_(l=1)^(c-1)
                          varphi(exp(i theta_l))Fej_c(t-theta_l),
    E=[1+pi L(5+2log c)]/c,
    epsilon=(4L-5)/(2d)+E/2,
    E_bal=5(3+3pi),
    delta_*=[28(1+60pi)]^-2,
    C_obs=2/delta_*, C_stab=33C_obs+3.

The sample at1 in q is zero, as required by the actual cyclic projection.
For EVERY actual M>=2,

    ||h_orig-h_phase||_1<=epsilon<=E_bal M^(-12/11).         (SB4)

For EVERY tau>0 on the SAME original circle,

    ||f_(j,tau)-(1-h_phase/tau)_+||_1
                                    <=min{1,C_stab epsilon},
    ||f_(j,tau)-(1-h_phase/tau)_+||_(4/3)
                             <=min{1,(C_stab epsilon)^(3/4)}. (SB5)

The actual logarithm in E remains; the integer multiplier ell_j pays it.
The proof retains the full inverse-Gram identity, its pole at1, and every shrinking-cell estimate needed for(SB5).
No uniform lower bound on the ratio h_orig/h_phase is assumed.

### Every finite Fourier set and all five costs

Define constants from the SAME fixed torus, with all partial derivatives taken in angular coordinates, by

    D_l=||partial_l Acal||_infinity+||partial_l Bcal||_infinity, l=1,2,3,
    G_K=sqrt(||g||_infinity),
    C_w=6pi[1+10sum_l D_l+2(G_K+1)],
    C_s=3pi[24*64^(3/4)sum_l D_l+4^(3/4)],
    C_2=2*2048^(3/4)C_w+2C_s.

For a probability measure mu let N_mu(v)=sup_(E measurable,mu(E)>0)mu(E)^(-1/4)integral_E abs(v)dmu.
For M>=max{2,C_w}, take rho=(C_w/M)^2 and

    V_rho=Ncal(z^-1,u^-1,v^-1)/(g+rho),
    h_rho=(1+Re(wV_rho))/2, F_(tau,rho)=(1-h_rho/tau)_+,
    P_M=J_(floor(M/2)+1), J_N=Fej_N^2/[(2N^2+1)/(3N)],
    Q_(tau,rho)=F_(tau,rho)*(four-coordinate product of P_M),
    B_bal(j,tau)=min{1,(C_stab epsilon)^(3/4)}
                                        +C_2 M^-1 tau^(-1/8).

P_M is a positive mass-one kernel of CLOSED Fourier support[-M,M] and angular first moment at most3pi/M.
For EVERY0<tau<=1/64,

    N_nu1(f_(j,tau)-Q_(tau,rho) composed with iota_j)
          +N_nu4(F_tau-Q_(tau,rho))<=B_bal(j,tau).           (SB6)

For EVERY finite Gamma in the CLOSED integer box[-M,M]^4,

    sum_(gamma in Gamma)
       abs(fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma))
          <=8 card(Gamma)^(3/4) B_bal(j,tau).               (SB7)

All supplied original images are distinct.
Empty Gamma, zero and negative harmonics, and every box endpoint are included.
The five costs are the original comparison, TWO regularizations and TWO smoothings on the actual original and torus laws.

### Entire centered support and uniform critical strip

Define the actual fixed-torus centers by

    D_0(z)=-2(z-z^-1)+(z^K+1)/(z^K-1), b_0(z)=Im D_0(z),
    z_0=exp(i pi/K),
    -cot(t_(k,m)/2)=16sqrt(km)-b_0(z_0), t_(k,m) in(-pi,0),
    phi_z(t)=arctan(2/[b_0(z)-cot(t/2)]),
    n_(k,m)=floor((k+m)phi_(z0)'(t_(k,m))+1/2),
    C_loc=ceil(32000pi+1024pi(K+4)).

These evaluations use the actual regular local neighborhoods, and abs(n_(k,m))<=14(k+m).
In this entire support conclusion assume the actual M>=max{2,C_w} and0<tau<=1/64.
For L_tau=floor(1/(4sqrt(tau))) and integer J>=2, set

    R_z=ceil(C_loc J^(1/3)), R_u=ceil(C_loc sqrt(L_tau)J^(5/6)),
    G_(L_tau,J)={(-p,-q,m,k):1<=k<=L_tau,1<=m<=J,
                                abs(p)<=R_z,abs(q-n_(k,m))<=R_u},
    N_sel=L_tau J(2R_z+1)(2R_u+1)
                     <=9(C_loc+1)^2 L_tau^(3/2)J^(13/6),
    C_sup=8[9(C_loc+1)^2]^(3/4)4^(-9/8),
    C_first=(C_stab E_bal)^(3/4).

Whenever ALL conditions

    R_z,J,L_tau<=M, 14(L_tau+J)+R_u<=M                      (SB8)

hold, every selected original frequency is strictly positive and the entire finite set satisfies

    W_*(f_(j,tau))>=3log(J+1)/(32768pi)
                                -8N_sel^(3/4)B_bal(j,tau). (SB9)

The complete error in(SB9) is at most

    C_sup J^(13/8)[C_first M^(-9/11)tau^(-9/16)
                                  +C_2 M^-1 tau^(-11/16)]. (SB10)

Put

    M_bal=ceil(max{2,C_w,(C_loc+1)^(33/29),
                              7^(11/3),(C_loc+29)^(11/7)}),
    j_bal=max{1,ceil(4M_bal/K)},
    C_crit=C_sup(C_first+C_2).

For EVERY actual j with M=M_j>=M_bal and EVERY real H,tau such that

    16<=H<=M^(16/11)/64, M^(-16/11)H<=tau<=1/64,            (SB11)

J=floor(H^(1/4)) satisfies the full(SB8), and

    W_*(f_(j,tau))>=3log H/(131072pi)
                            -C_crit[H^(-5/32)+H^(-9/32)]. (SB12)

This is uniform over the whole stated H,tau strip.
Both powers of M cancel exactly, with no unpaid critical logarithm.
Every integer j>=j_bal satisfies the required actual condition M_j>=M_bal.

### Genuine degree and arbitrary diverging enlargement

For EVERY actual M=M_j>=2, write T_M=1+log M.
The actual minimal-polynomial degree satisfies

    M^(34/11)T_M<d_j<2^23 M^(34/11)T_M,
    M^(34/11)/24<d_j/(1+log d_j)<2^23 M^(34/11).            (SB13)

For EVERY positive shrinking sequence tau_j->0 such that

    (d_j/(1+log d_j))^(8/17)tau_j->infinity,                (SB14)

one has W_*(f_(j,tau_j))->infinity.
Condition(SB14) is equivalent to M_j^(16/11)tau_j->infinity, with no monotonicity or prescribed divergence speed.
The sequence may enter(SB11) at a sequence-dependent index.
This new family differs from the square,25/11 and21/11-log families; their old theorems remain in their stated scopes.
No bounded-H endpoint, criterion omitting the degree logarithm, every-large-degree assertion, uniform lower Gram ratio, global optimality, near-one input family or unrestricted G0001 completion is asserted.
The actual restriction log2<m(P_j)<log4 and full original2d normalization are retained.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Complete argument

### 1. New integer thresholds, prime eligibility and every closed-box alias

K is even and at least16.
Since a>2K and K>=3, K+a+3<=2a.
Integer Bertrand at(K+a+3)^2 gives

    a^2<b<2(K+a+3)^2<=8a^2, L+1<=b+2a<=2b.

For M>=2,4M<=a<4M+4<=6M, hence

    16M^2<L<L+1<2^10 M^2, L>4K^2.                         (SB15)

Set X=L+1 and x=X^(17/11).
The integer n=ceil x satisfies x<=n<2x.
Integer Bertrand at n ell now proves

    x ell<c<2n ell<4x ell, c>L, c<d<2c.                   (SB16)

All a,b,c are distinct odd primes exceeding K, so none divides K and the four exponents are pairwise coprime.
This verifies the actual arbitrary-prime source hypotheses before its use.

The complete no-alias inequalities are

    a>2M, b>2M(1+a), c>2M(1+a+b).                         (SB17)

Indeed a>=4M and a^2>2M(1+a) for M>=2.
Also

    L^(6/11)>(16M^2)^(6/11)>2M,
    c>L^(17/11)>2ML>2M(1+a+b).

The middle strict inequality follows from16^(6/11)M^(1/11)/2>1 for M>=2.
Thus in any nonzero integer delta in[-2M,2M]^4, its highest nonzero weighted coordinate strictly dominates all previous coordinates, proving H_j(delta)!=0.
This includes all endpoints, not just the open box.
Differences of two closed-M indices lie in this box, so coefficients of every closed-M polynomial return exactly.
Every nonconstant finite character supported in the closed-M box has mean zero on EVERY translated mu_(j,t); translation only supplies a unit-modulus scalar.
These facts are established for the new c, independently of any older r>2 schedule.

### 2. Actual source construction, exact factor removal and total measure

Use the accepted MS05-U001 arbitrary-distinct-prime construction with q=4, k_1=K and the three eligible primes just proved.
Its inspected arbitrary-prime section makes the smallest-prime condition of its original Lemma12 relevant only to that source's separate degree upper bound.
The torsion, integrality and interlacing statements used here hold for EVERY distinct eligible triple.
No conclusion invoked here requires c>(L+1)^2.

A torsion zero of the full source hypersurface either has two powered coordinates equal1, forcing x=1 by pairwise coprimality, or lies on a constant-x maximal torsion coset whose constant is killed by K.
In the latter case the K-coordinate is1, while exactly one powered coordinate1 cannot satisfy the hypersurface equation.
Thus1 is the only root of unity in Qraw.
At1 the second part of2Qraw has exact order3 with coefficient-2 sum_q product_(i!=q)e_i, which is nonzero; its first part has order5.
Therefore the exact cyclotomic factor is(x-1)^3.

The four summands in the half-sum have the same reduction modulo2, so Qraw is integral.
Division by the monic(x-1)^3 leaves an integral polynomial P.
The reduced denominator product_i(x^e_i-1)/(x-1)^3 is monic with simple circle zeros and vanishes at1.
The positive residues of the reduced rational sum prevent cancellation, and its numerator is integral by the same parity calculation.
The accepted circular-interlacing Proposition6 and Proposition5(a) apply with those conditions, yielding a Salem factor with possible cyclotomic factors, or a reciprocal quadratic alternative.
The root-of-unity exclusion removes every additional cyclotomic factor, and d>2 excludes the quadratic alternative.
Thus P is the actual irreducible Salem minimal polynomial, not just a reciprocal trial polynomial.

The leading terms of Qraw are x^(c+L)-2x^(c+L-1).
Division by(x-1)^3 gives degree d=c+L-3 and next coefficient1, hence trace-1.
Since K is even and a,b,c are odd, d=K+a+b+c-1 is even.
The actual exterior root beta>1 obeys

    beta-beta^-1=(1/2)sum_(e in {K,a,b,c})(beta^e+1)/(beta^e-1).

Each fraction is greater than1 and at most(beta+1)/(beta-1).
Consequently beta>1+sqrt2>2 and beta+beta^-1<=4, giving beta<4.
Because P is already known to be Salem and minimal, its total measure is log beta.
This is the accepted RY26 exterior-root algebra only, not that source's every-large-degree theorem.

### 3. All original2d rank, cyclic, sample and interpolation costs

Write R_0=(x^K-1)(x^a-1)(x^b-1) and

    S_0=sum_(e in {K,a,b})(x^e+1)product_(v in {K,a,b},v!=e)(x^v-1),
    A=-(x^2-1)R_0-xR_0/2+xS_0/2,
    B= (x^2-1)R_0-xR_0/2-xS_0/2.

Then Qraw=A+x^c B and these A,B are exactly the torus specializations in the statement.
They are integral of degree L; A has constant and leading coefficient-1, and B has both equal1.
In N=2d coordinates the raw coefficient matrix has r=N-deg Qraw=c+L-6=d-3 independent columns Qraw,...,x^(r-1)Qraw.
Its projection Pi_Q lies inside the full Pi_P=Pi_j with codimension3, so Pi_P-Pi_Q is an orthogonal projection of rank3.

Let S_c e_i=e_(i+1 mod c) and use the SAME2d coordinates to define

    V_c=[A(S_c);B(S_c);0_(2L-6)-by-c].

Its range projection is Pi_V.
The first c raw columns agree with V_c in columns0<=i<c-L, so their matrix difference has rank at most L.
Each range has codimension at most L over its intersection with the other, and their projection difference has rank at most2L.
The remaining L-6 independent raw columns enlarge the raw range by exactly L-6.
Differences of orthogonal projections have operator norm at most1, yielding

    ||Pi_Q-Pi_V||_trace<=3L-6,
    ||Pi_P-Pi_V||_trace<=3L-3.                              (SB18)

On the torus, Acal/(zR_tor)=-1/2+H and Bcal/(zR_tor)=-1/2-H with H purely imaginary.
Thus their moduli agree everywhere by continuity.
Direct substitution in S_tor shows their common zeros are exactly the points where at least two of z^K,u,v equal1.
For every nontrivial c-th root omega, none of omega^K,omega^a,omega^b equals1, by(SB16) and primality.
Only the trivial c-mode is zero.
For eigenvector entries omega^-i the cyclic blocks therefore are

    rank V_c=c-1,
    Pi_V,11=Pi_V,22=(I_c-J_c/c)/2,
    Pi_V,12(i,l)=(1/(2c))sum_(omega^c=1)
                            U(omega,omega^a,omega^b)omega^(l-i),
    Pi_V,21=Pi_V,12^*.

J_c is the all-ones matrix and the final2L-6 coordinates are zero.
The common-zero convention makes the sample at omega=1 zero.

Since A+B=-xR_0 and both constants are nonzero, every common root of A,B is a root of unity.
At a root of exactly one powered factor, the corresponding S_0 term is nonzero, so it is not common.
Pairwise coprimality leaves only1, and

    [A/(x-1)^2](1)=Ka+Kb+ab,
    [B/(x-1)^2](1)=-(Ka+Kb+ab).

This proves the exact common factor(z-1)^2.
Equal circle moduli exclude any other circle zero.
The reciprocal identity B=-A^*, with reciprocal degree L, gives the smooth unimodular phase and varphi(1)=-1.

The full-grid Fejer average I_c varphi has all c samples and mass-one weights.
The rational-factor variation bound gives V(varphi)<=2pi(L-2).
The finite arc-count estimate and Fejer moment, valid for every c>=2, are

    grid multiplicity of an oriented arc<=c abs(t)/(2pi)+1,
    integral abs(t)Fej_c(t)dnu_1<=pi(1/2+log c)/c.

They give ||I_c varphi-varphi||_1<=V(varphi)(5/4+(log c)/2)/c.
Changing the actual sample-1 at1 to0 adds Fej_c/c, so

    q=I_c varphi+Fej_c/c, abs(q)<=1,
    deg_Fourier(q)<=c-1, ||q-varphi||_1<=E.                 (SB19)

For a self-adjoint T, abs(v^*Tv)<=v^*abs(T)v and integral vv^*=I.
Thus(SB18), divided by the ORIGINAL2d, gives ||k-k_V||_1<=(3L-3)/(2d), where k_V=1-v^*Pi_Vv/(2d).
The displayed cyclic blocks give exactly

    v^*Pi_Vv=c-Fej_c+c Re(z^c q),
    k_V-(1-Re(z^c q))/2
           =((d-c)/(2d))(1+Re(z^c q))+Fej_c/(2d)>=0.

Since z^c q has no constant coefficient, the last nonnegative expression has integral(L-2)/(2d).
Consequently ||k-(1-Re(z^c q))/2||_1<=(4L-5)/(2d).
Adding E/2 proves the first part of(SB4).
The smooth phase and the original torus convention disagree only at1 on this actual circle, a Haar-null point.

### 4. Exact Gram pole and C663 observability for the new family

The full relation matrix has independent columns, so G is positive definite.
Directly applying A_rel^T to the evaluation vector gives the exact identities

    G_d(z)=v_d(z)^*G^-1v_d(z)>0,
    h_orig=abs(P)^2G_d/(2d),
    h_phase=abs(z-1)^2 abs(P)^2/[4abs(A_0)^2],
    r=2abs(A_0)^2G_d/[d abs(z-1)^2], h_orig=r h_phase.      (SB20)

The last equality uses polynomial multiplication, without division by P.
P(1)!=0 implies h_0=h_orig(1)>0; also h_0<=1.
The ratio has its actual pole at1, which is not discarded.

Write U_j=A/B after its exact cancellation.
On each cotangent regular interval the inverse phase has a continuous lift psi and

    D_phase(t)=4sin t+cot(Kt/2)+cot(at/2)+cot(bt/2),
    U_j(exp(it))=(1+iD_phase)/(1-iD_phase),
    psi'=-2D_phase'/(1+D_phase^2)>0,
    D_phase'<=4-(K+a+b)/2<0.

Every pole has positive residue, and the limiting inverse-phase derivative is positive, so psi extends smoothly across each pole without a jump in the lift.
There are exactly L-4 distinct cotangent poles over one turn, counting their common pole at0 only once.
Thus psi(t+2pi)-psi(t)=2pi(L-4), and Theta=ct+psi has degree d-1 and derivative at least c.
Choose psi(0)=pi and let I_0=[-t_*,t_*] be the extra phase cell abs(Theta-pi)<=pi around1.

All shrinking-cell estimates used here follow from c>L, L>4K^2 and K>=16, which(SB15)--(SB16) verify for the new family.
For abs(t)<=pi/c, put R_phase=2(1/K+1/a+1/b)>=2/K.
The elementary bound abs(cot x-1/x)<=pi abs(x)/6 for abs(x)<=pi/2, together with abs(sin t)<=abs(t), gives

    D_phase=R_phase/t+E_phase,
    abs(E_phase)<=(L+4)abs(t),
    (L+4)t^2/R_phase<pi^2/(4K)<1/2.

For the last inequality, c>L, L>4K^2 and L>=4 give
K(L+4)pi^2/(2c^2)<Kpi^2/L<pi^2/(4K).
Thus D_phase has the sign of t, and

    p(t)=Theta(t)-pi=ct+2arctan(1/D_phase(t)),
    c abs(t)<=abs(p(t))<=c abs(t)+2K abs(t)<=3c abs(t).

The branch is fixed by continuity from0 on both sides.
Monotonicity and p(pi/c)>=pi give

    pi/(3c)<=t_*<=pi/c, nu_1(I_0)<=1/c.                   (SB21)

Moreover v_0=Theta'(0)=c+2/R_phase=c+1/(1/K+1/a+1/b).
Because A_0 and G^-1 have real coefficients, T(t)=2abs(A_0(exp(it)))^2G_d(exp(it)) is a real even trigonometric polynomial of degree at most d+L-3.
The finite cosine recurrence shows that sigma=(T(t)-T(0))/[4d sin^2(t/2)] is a real even trigonometric polynomial of degree at most d+L-4.
Using(SB20) and h_phase(t)/t^2->v_0^2/4 identifies its exact decomposition as

    r=u+sigma,
    u=kappa/[4sin^2(t/2)], kappa=T(0)/d=4h_0/v_0^2<=4/c^2,
    deg_Fourier(sigma)<=d+L-4<3c.                          (SB22)

The limit identifies the coefficient only; the uniform cell estimates are(SB21), not a fixed-j Taylor remainder.

C663's every-cell argument now applies at verified hypotheses, as follows.
On any interval of length2pi/c, each of the three cotangent families has at most one pole, because K,a,b<c.
There are at most three distinct poles, splitting the interval into at most four regular pieces.
The inverse-phase increment on each is at most2pi, so the whole Theta increment is at most10pi, including all branch lifts and endpoints.
For0<delta<=1, a phase contact band h_phase<=delta has phase length4arcsin sqrt(delta)<=2pi sqrt(delta), and at most seven such bands meet that interval image.
As Theta'>=c, its contact fraction is at most7sqrt(delta).

For completeness the applicable finite derivative mechanism includes both Fourier endpoints.
For every integer n>=1 and degree-at-most n trigonometric polynomial T, Krep_n=2Fej_(2n)-Fej_n has multiplier1 on[-n,n], so T=T*Krep_n.
Writing Fej_n=abs(sum_(r=0)^(n-1)exp(irt))^2/n and applying finite Cauchy--Schwarz gives ||Fej_n'||_1<=2n.
Hence ||Krep_n'||_1<=10n and V(T)<=20pi n||T||_1.
The probability L1 and unnormalized angular V differ by the factor2pi in this last estimate.

Partition the original circle into c equal cells.
For the bad set h_phase<=delta, comparison with each cell mean and its variation gives

    integral_bad abs(T)<=7sqrt(delta)[||T||_1+V(T)/c].

For every complex trigonometric polynomial T of degree at most3c, V(T)/c<=60pi||T||_1.
Our delta_* makes the bad mass at most one quarter of ||T||_1.
Absorbing it and using h_phase>=delta_* on the complement yields

    ||T||_1<=C_obs integral h_phase abs(T).                 (SB23)

The finite reproducing kernel is used only for this derivative estimate; it does not replace the positive smoothing kernel in(SB6).

Let e=abs(h_orig-h_phase), so integral e<=epsilon by Section3.
From(SB20)--(SB22), h_phase abs(sigma-1)<=e+h_phase u.
On I_0, (SB21) gives h_phase=sin^2(p/2)<=9c^2t^2/4, and sin(abs(t)/2)>=abs(t)/pi.
Thus h_phase u<=9pi^2/4 there.
Outside I_0 the exact pole integral and(SB21) give

    integral_(T\I_0)u<=kappa cot(pi/(6c))/(2pi)
                         <=12/(pi^2c)<2/c.

Consequently integral h_phase u<32/c.
Apply(SB23) to sigma-1, to obtain ||sigma-1||_1<=C_obs(epsilon+32/c).
For eta_r=abs(r-1)/max{1,r}, set eta_r(1)=1.
It is at most1 on I_0 and at most abs(sigma-1)+u on the complement.
Therefore

    integral eta_r<=C_obs(epsilon+32/c)+3/c.

Since d<2c and L>4K^2>1024, epsilon>=(4L-5)/(2d)>(4L-5)/(4c)>1/c.
It follows that integral eta_r<=C_stab epsilon.
The exact scalar inequality, for r,x>=0 and tau>0, is

    abs((1-rx/tau)_+-(1-x/tau)_+)<=abs(r-1)/max{1,r}.

For r>=1 its maximum occurs at x=tau/r; for r<=1 it occurs at x=tau, including equality and r=0.
Apply it with x=h_phase on the original circle.
The difference is at most1, so its strong4/3 norm is at most its L1 norm to the power3/4.
This proves both bounds in(SB5) for every tau>0, with the actual pole and all cell costs paid.

### 5. Exact logarithmic budget at the new prime threshold

Using d>c,L>=1,1+log c>=1 in the exact epsilon formula gives

    epsilon<=(3+3pi)(L/c)(1+log c).

For X=L+1>=4, ell=ceil(log_2 X) satisfies ell>=log X/log2 and ell<=X.
The upper bound c<4X^(17/11)ell implies

    log c<log4+(17/11)log X+log ell
                       <=(39/11)log X<4log X,
    (1+log c)/ell<=5log2<5.

The last inequality uses log X>=1.
Consequently

    (L/c)(1+log c)<5L/X^(17/11)<5L^(-6/11)
                                             <=5M^(-12/11).

This proves all of(SB4).
The logarithm was paid by the actual ell factor inside the integer threshold; no unweighted logarithm-free interpolation estimate is asserted.

### 6. Every translated law, both regularizations and both smoothings

We reconstruct the general C641 probability argument at the NEW laws, rather than importing an old-family conclusion.
The fixed torus g,Acal,Bcal has not changed, so its adopted C633 log-free amplitude identity and C641 pointwise derivative calculations apply without a new source input.
The remaining arithmetic premise is exact finite-character averaging, already proved in Section1.

For0<rho<=1, s>=rho and0<eta<=1, set r_s=s/(g+s) and V_eta=eta/(eta+h_rho).
Their logarithmic derivative bounds are

    sum_l abs(partial_l r_s)/r_s<=sum_l D_l/sqrt(s),
    sum_l abs(partial_l W)/W
       <=[10sum_l D_l+2(G_K+1)]/sqrt(rho)
                                      for W=V_eta or r_s V_eta.

The latter sum includes all four coordinates.
The functions are smooth even at the old common-zero set; s is allowed to exceed1.
For I_W^*=sup_t integral W dmu_(j,t)<=1, positive convolution by the four P_M kernels, exact mean return and coordinate-path FTC give

    I_W^*<=integral W dnu_4
            +[3pi(10sum_l D_l+2(G_K+1))/(M sqrt(rho))]I_W^*.

The bracket is at most1/2 because M sqrt(rho)=C_w.
The same argument for r_s alone is valid whenever M sqrt(s)>=C_w.
No nonlinear function was itself assumed to have exactly equal torus and original means.

The fixed torus amplitude bound is integral r_s<=8s^(2/3) for s<=1, and the trivial bound1 applies for s>1.
Only under product Haar, averaging the independent w coordinate gives

    integral_w eta/[eta+(1+a cos(theta))/2]
       =eta/sqrt((eta+1/2)^2-(a/2)^2)<=sqrt(eta),
    a=g/(g+rho).

Absorption therefore gives, for EVERY new translated law,

    integral r_s<=16s^(2/3) if s<=1 and M sqrt(s)>=C_w,
    integral V_eta<=2sqrt(eta),
    integral r_s V_eta<=16sqrt(eta)s^(2/3), s>=rho,
    mu_(j,t){h_rho<=eta,g<=s}<=64sqrt(eta)s^(2/3).           (SB24)

For s>1 the displayed product bound follows from the trivial torus amplitude bound and s^(2/3)>=1.
This explains its use on all subsequent dyadic shells.

Here are the four costs with their full dependence.
For smoothing, set w_tau=1_(h_rho<=tau)(g+rho)^(-1/2).
For0<t<=1 its tail is at most4sqrt(tau), hence at most64sqrt(tau)t^(-4/3).
For1<t<=rho^(-1/2), apply(SB24) at s=t^-2>=rho to the event h_rho<=tau and g<t^-2.
For t>rho^(-1/2) the tail is zero.
Consequently

    N_mu(w_tau)<=4*64^(3/4)tau^(3/8),
    N_mu(1_(h_rho<=tau))<=[4sqrt(tau)]^(3/4).

The coordinate derivative envelopes for F_(tau,rho) are6D_l tau^(-1/2)w_tau for l=1,2,3, and tau^(-1/2)1_(h_rho<=tau) for the fourth coordinate.
Apply FTC first on each measurable event, then integrate coordinate displacements against the positive kernels.
Every intermediate translation is covered by(SB24); the event-norm triangle inequality and moment3pi/M yield C_s M^-1 tau^(-1/8) for EACH smoothing, on the actual original law and on the torus.

For regularization, on g>0 one has h_rho=a h+rho/[2(g+rho)] with a=g/(g+rho).
Every translated circle meets g=0 only finitely many times, because its three relevant powered coordinates have nonzero integer frequencies; the torus common-zero set also has measure zero.
At such common zeros the conventions give h=h_rho=1/2 and both caps vanish in the present range.
For tau<=1/64, D=F_tau-F_(tau,rho) is therefore nonnegative everywhere, its nonzero set is contained in h<=tau, and it satisfies

    D<=min{1,rho/[2tau(g+rho)]}.

Set lambda=rho/tau, with no assumption lambda<=1.
Partition g>=rho into the disjoint half-open shells s<=g<2s with s=2^k rho, k=0,1,...; every endpoint belongs to exactly one shell.
The low region g<rho contributes at most32rho^(2/3) to integral D^(4/3), because its indicator is at most2r_rho.
On each active shell h_rho<=eta_s=tau+rho/(2s)<1, and(SB24) at amplitude2s bounds its probability by64*2^(2/3)sqrt(eta_s)s^(2/3), including2s>1.
For the middle shells rho<=s<=lambda, eta_s<=3rho/(2s), so D<=1 and the backward geometric sum give a contribution less than

    160sqrt(rho) sum_(s<=lambda)s^(1/6)
                <1600sqrt(rho)lambda^(1/6)
                 =1600rho^(2/3)tau^(-1/6).

For the high shells s>lambda, eta_s<=3tau/2 and D^(4/3)<=(lambda/(2s))^(4/3), giving a contribution less than

    160*2^(-4/3)sqrt(tau)lambda^(4/3)sum_(s>lambda)s^(-2/3)
                <240sqrt(tau)lambda^(2/3)
                 =240rho^(2/3)tau^(-1/6).

These are the exact C641 geometric estimates1/(1-2^(-1/6))<10 and1/(1-2^(-2/3))<3.
They cover every shell even when lambda>1; the boundedness of g also makes only finitely many shells nonempty.
The total integral D^(4/3) is at most2048rho^(2/3)tau^(-1/6).
Thus EACH regularization has strong4/3 norm at most2048^(3/4)sqrt(rho)tau^(-1/8), both on the actual law and on the torus.

Strong4/3 controls N_mu by Holder.
Summing these TWO regularizations, TWO smoothings and the original(SB5), with sqrt(rho)=C_w/M, proves(SB6).
The full cost C_2 has no missing original-space or torus-space term.

For finite Gamma, Q_(tau,rho) has closed-M support, and all coefficient differences lie in the closed2M box of Section1.
Its torus and returned coefficients therefore agree exactly, including every endpoint.
The direct finite weak-Fourier lemma of C641, proved for every finite orthonormal modulus-one character family on a probability space, bounds the sum of N coefficient magnitudes by8N^(3/4)N_mu(v).
Apply it on the two spaces and use(SB6), proving(SB7).
This invokes the proved finite lemma, not a strong Hausdorff--Young theorem or a new external interpolation input.

### 7. Entire centered support, all floor/ceiling costs and every H

The adopted C638 calculation is a theorem on the unchanged fixed K-torus and therefore supplies exactly the stated centers, their bound14(k+m), and mass3log(J+1)/(32768pi) for the ENTIRE G_(L_tau,J).
There is no removal of unfavorable rectangles.
Under(SB8), all these indices belong to the new closed-M box, and Section1 gives distinct images.
Since k>=1, each image is at least c-M(1+a+b)>0.
Applying(SB7) to this entire set proves(SB9).

For tau<=1/64, L_tau>=2, L_tau sqrt(tau)>=1/8 and L_tau<=1/(4sqrt(tau)).
The ceilings obey

    2R_z+1<=3(C_loc+1)J^(1/3),
    2R_u+1<=3(C_loc+1)sqrt(L_tau)J^(5/6).

This gives the full stated N_sel, and

    8N_sel^(3/4)<=C_sup J^(13/8)tau^(-9/16).

Multiplication by(SB4)--(SB6) proves(SB10), including all five costs.

For(SB11), let J=floor(H^(1/4)); it is at least2.
The actual floor and ceiling bounds imply

    L_tau<=(1/4)M^(8/11)H^(-1/2), J<=M^(4/11),
    R_z<=(C_loc+1)M^(4/33),
    R_u<=(1/2)(C_loc+1)M^(4/11)H^(-1/24).

The last inequality uses sqrt(L_tau)J^(5/6)<=M^(4/11)H^(-1/24)/2 and ceil(C_loc x)<= (C_loc+1)x for x=sqrt(L_tau)J^(5/6)>=1.
The threshold M_bal makes R_z,J,L_tau<=M.
For every j>=j_bal, a_j>(j+1)K>4M_bal and therefore floor(a_j/4)>=M_bal, so this is also an explicit sufficient index threshold for the actual family.
It also makes

    14(L_tau+J)+R_u
       <=(7/2)M^(8/11)+(1/2)(C_loc+29)M^(4/11)<=M.

Specifically M>=7^(11/3) bounds the first term by M/2, and M>=(C_loc+29)^(11/7) bounds the second by M/2.
Thus the complete center-plus-radius condition is paid.

In the first error of(SB10), substituting J<=H^(1/4), tau>=M^(-16/11)H gives

    M^(-9/11) M^((16/11)(9/16)) H^(13/32-9/16)=H^(-5/32).

The second becomes

    M^-1 M^((16/11)(11/16)) H^(13/32-11/16)=H^(-9/32).

Both cancellations are exact and neither introduces a logarithm.
Finally J+1>H^(1/4), proving(SB12) with the displayed C_crit uniformly for every H,tau in the strip.

### 8. Actual degree constants, sequence quantifiers and scope of the balance

From(SB15), x=X^(17/11) satisfies

    M^(34/11)<x<2^16 M^(34/11).

The exact integer multiplier obeys

    T_M<ell<=11+(2/log2)log M<=11+3log M<=11T_M.

The lower inequality follows from ell>=log_2 X>4+2log M/log2>1+log M.
Together with x ell<c<d<2c<8x ell, this proves

    M^(34/11)T_M<d<88*2^16 M^(34/11)T_M
                                     <2^23 M^(34/11)T_M.

These bounds concern the actual minimal-polynomial degree d, not c or the raw degree.
Let T_d=1+log d.
The lower degree bound implies T_d>=T_M, and the upper one, with log(1+log M)<=log M, implies

    T_d<1+23log2+(45/11)log M<=24T_M.

Dividing the degree bounds by these estimates proves(SB13).
Raising its second line to8/17 compares(d/T_d)^(8/17) above and below with fixed positive multiples of M^(16/11).
Thus(SB14) is equivalent to H_j^enl=M_j^(16/11)tau_j tending to infinity.
For every such shrinking sequence, eventually M_j>=M_bal, H_j^enl>=16 and tau_j<=1/64; also H_j^enl<=M_j^(16/11)/64.
Apply(SB12) with H=H_j^enl: its main term diverges and both errors tend to zero at any divergence speed.
No uniform entry index for arbitrary sequences is claimed.

The original rank-d projection has integral h_orig=1/2 and0<=h_orig<=1.
At any genuine circle root of P, all d relation columns vanish under evaluation, giving h_orig=0 and cap value1.
For0<tau<=1, (1-h_orig/tau)_+<=1-h_orig, so its mean is at most1/2.
For fixed j,tau, the cap of the finite trigonometric h_orig is continuous and piecewise smooth with square-integrable derivative.
The level equation is either identically true or has only finitely many circle solutions.
Integration by parts across its pieces and finite derivative Bessel, followed by Cauchy--Schwarz with sum_(n!=0)n^-2<infinity, prove W_*<infinity.
No moving-width result is inferred from a fixed-j derivative bound.

For explanation only within THIS complete cost and support mechanism, a formal scale c approximately L^r times a logarithmic multiplier would yield epsilon approximately M^(-2(r-1)).
The two paid errors suggest theta_M<=min{8(r-1)/3,16/11}, and theta_degree<=min{4(r-1)/(3r),8/(11r)}.
These two degree expressions balance at r=17/11 and value8/17.
This arithmetic is not an all-r construction theorem or optimality over all methods.
The actual family, exact alias constants and surviving degree logarithm have been proved separately above.

## Reuse and source boundary

The inspected MS05-U001 accepts its retained2004 manuscript statements and selected torsion/construction applicability checks.
Its general interlacing and torsion-exponent propositions retain their external-statement depth; no original Mann/Schmidt or whole-source proof audit is added.
The integer Bertrand input remains the same accepted statement for every integer n>=2 that some prime satisfies n<p<2n, at the bounded C356/C217 and Mig78-U001 source account.
Every threshold used here is an integer before its application.
Its classical original proof is not newly inspected or attributed to Mignotte.
RY26 contributes only the accepted exterior-root formula at its inspected scope.
C171/C172's finite rank, cyclic and sample mechanisms are reconstructed in Section3 with the new dimensions and all coprimality conditions.
C660/C661's Gram and pole mechanisms are reconstructed in Section4; only the exact finite decomposition and explicit shrinking-cell conditions needed here are used, not an assumed uniform lower ratio.
C663 supplies its proved generic finite reproduction and same-cell absorption mechanisms after the new local phase premises are checked.
C633, C637 and C641 supply fixed-torus and general probability identities; all new translated-law averaging premises, five costs and finite indices are established in Section6.
C638 supplies the unchanged torus centers and full mass only; the new original support, positivity and exact degree calculation are paid here.
No old-family theorem is extended merely by changing its parameter name.
The fixed polynomials remain separated from Mahler measure zero by log2, and this does not resolve G0001 for arbitrary admissible input.

## Assessment history

### Decision stability-balanced-family-open

| Field | Value |
| --- | --- |
| date | 2026-10-24T01:35 |
| status | open |
| reason | Register the complete NEW17/11 logarithmic actual family with source-certified irreducible Salem polynomials, exact original2d Gram/cyclic/sample interfaces, the proved same-cell cap stability at newly checked hypotheses, all translated laws, all five costs and whole centered support. The uniform critical strip and actual degree criterion(d/(1+log d))^(8/17)tau diverging are author-checked and await fresh independent whole review. All measure/source/logarithm restrictions and bounded-H/unrestricted boundaries remain. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire new-family statement](#statement) | SB1--SB14: actual integer thresholds and minimal polynomials, full2d objects/laws, exact finite budgets, every signed closed-box set, entire support, uniform critical strip and genuine-degree arbitrary-sequence criterion. |
| argument | [Complete reconstruction](#complete-argument) | Sections1--8/SB15--SB24: all integer/source/factor/degree/alias/cyclic/pole/observability hypotheses, full translated-law joint-shell argument, every five-cost/support/threshold expense and sequence quantifier. |
| dependency | [Accepted arbitrary-prime source](../audits/literature/MS05/Yin_U001.md#ms05-u001) | The exact arbitrary-distinct-prime-construction and four-exponent-specialization sections at retained statement/selected-proof depth; new eligibility and exact factor removal checked here. |
| dependency | [Exterior-root identity](../audits/literature/RY26/Yin_U001.md#ry26-u001) | Exterior-root-measure-expense section only, after actual irreducibility; no source every-large-degree theorem. |
| dependency | [Accepted integer Bertrand input](Yin_C_G0356_v1.md#argument) | Every integer n>=2 has n<p<2n at the retained classical statement depth; thresholds are exact integers. |
| support | [Bertrand source limit](../audits/literature/Mig78/Yin_U001.md#mig78-u001) | Existing Proposition5 length account and associated attribution, with no new classical original-proof inspection. |
| dependency | [Finite cyclic mechanisms](Yin_C_G0171_v1.md#two-block-circulant-rank-transfer) | Original full2d block rank and Fourier projection mechanism, reconstructed at new c and d. |
| dependency | [Finite sample and original return](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | Exact inverse-grid orientation, missing sample and L1 interpolation mechanism after new cyclic hypotheses. |
| dependency | [Actual Gram mechanism](Yin_C_G0660_v1.md#decision-whole-reviewed-2026-10-24) | Exact Gram/phase identity without division by P, reconstructed for this new irreducible polynomial. |
| dependency | [Pole mechanism](Yin_C_G0661_v1.md#decision-whole-reviewed-2026-10-24) | Finite even pole remainder and shrinking-cell cotangent estimates, with all needed new-family hypotheses and bounds explicitly checked here. |
| dependency | [Adopted uniform cap stability](Yin_C_G0663_v1.md#decision-whole-reviewed-2026-10-24) | Finite endpoint reproduction, local phase count, same-cell absorption and scalar all-width cap inequality; new phase/degree/pole premises are checked in Section4. |
| dependency | [Fixed-torus amplitude bound](Yin_C_G0633_v2.md#additional-complete-logarithm-free-and-two-sided-argument) | Unchanged K-torus logarithm-free amplitude integral, not an independent-coordinate replacement of the new original law. |
| dependency | [Positive finite kernel](Yin_C_G0637_v1.md#complete-argument) | Normalization, closed support and angular moment for the squared-Fejer smoothing kernel. |
| dependency | [Finite weak return and smoothings](Yin_C_G0641_v2.md#combined-argument) | General event-norm FTC, two smoothings and finite weak-Fourier lemma, after reconstruction of every new translated law. |
| dependency | [Both joint-shell regularizations](Yin_C_G0641_v2.md#complete-additional-joint-shell-argument) | All rho/tau dyadic regularization estimates and constants on original/torus spaces, with the new all-shell premise proved in SB24. |
| dependency | [Entire centered torus support](Yin_C_G0638_v1.md#complete-local-modulation-calculation) | Actual unchanged centers, all rectangles, cardinality and torus mass; new closed-box alias, positivity and full original cost are paid here. |
| support | [Reuse and source limits](#reuse-and-source-boundary) | Exact inspection depths, no old schedule substitution, retained degree logarithm and log2..log4, no bounded-H or unrestricted completion. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T01:45 |
| status | proved |
| reason | Adopt the complete actual17/11 logarithmic family after full main-agent reading and fresh isolated whole R887. Exact source eligibility, cyclotomic removal and minimal degree, original2d cyclic/Gram/sample/pole interfaces, all translated laws and five comparison costs, entire centered support and explicit thresholds are established for this new family. The uniform critical strip gives the actual-degree criterion(d/(1+log d))^(8/17)tau tending to infinity at arbitrary speed. The degree logarithm, positive total measure above log2, fixed-input/sequence distinctions and source/SELF/UNKNOWN limits remain; no bounded-H endpoint, near-one family or unrestricted completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire new-family statement](#statement) | SB1--SB14: actual integer thresholds and minimal polynomials, full2d objects/laws, exact finite budgets, every signed closed-box set, entire support, uniform critical strip and genuine-degree arbitrary-sequence criterion. |
| argument | [Complete reconstruction](#complete-argument) | Sections1--8/SB15--SB24: all integer/source/factor/degree/alias/cyclic/pole/observability hypotheses, full translated-law joint-shell argument, every five-cost/support/threshold expense and sequence quantifier. |
| dependency | [Accepted arbitrary-prime source](../audits/literature/MS05/Yin_U001.md#ms05-u001) | The exact arbitrary-distinct-prime-construction and four-exponent-specialization sections at retained statement/selected-proof depth; new eligibility and exact factor removal checked here. |
| dependency | [Exterior-root identity](../audits/literature/RY26/Yin_U001.md#ry26-u001) | Exterior-root-measure-expense section only, after actual irreducibility; no source every-large-degree theorem. |
| dependency | [Accepted integer Bertrand input](Yin_C_G0356_v1.md#argument) | Every integer n>=2 has n<p<2n at the retained classical statement depth; thresholds are exact integers. |
| support | [Bertrand source limit](../audits/literature/Mig78/Yin_U001.md#mig78-u001) | Existing Proposition5 length account and associated attribution, with no new classical original-proof inspection. |
| dependency | [Finite cyclic mechanisms](Yin_C_G0171_v1.md#two-block-circulant-rank-transfer) | Original full2d block rank and Fourier projection mechanism, reconstructed at new c and d. |
| dependency | [Finite sample and original return](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | Exact inverse-grid orientation, missing sample and L1 interpolation mechanism after new cyclic hypotheses. |
| dependency | [Actual Gram mechanism](Yin_C_G0660_v1.md#decision-whole-reviewed-2026-10-24) | Exact Gram/phase identity without division by P, reconstructed for this new irreducible polynomial. |
| dependency | [Pole mechanism](Yin_C_G0661_v1.md#decision-whole-reviewed-2026-10-24) | Finite even pole remainder and shrinking-cell cotangent estimates, with all needed new-family hypotheses and bounds explicitly checked here. |
| dependency | [Adopted uniform cap stability](Yin_C_G0663_v1.md#decision-whole-reviewed-2026-10-24) | Finite endpoint reproduction, local phase count, same-cell absorption and scalar all-width cap inequality; new phase/degree/pole premises are checked in Section4. |
| dependency | [Fixed-torus amplitude bound](Yin_C_G0633_v2.md#additional-complete-logarithm-free-and-two-sided-argument) | Unchanged K-torus logarithm-free amplitude integral, not an independent-coordinate replacement of the new original law. |
| dependency | [Positive finite kernel](Yin_C_G0637_v1.md#complete-argument) | Normalization, closed support and angular moment for the squared-Fejer smoothing kernel. |
| dependency | [Finite weak return and smoothings](Yin_C_G0641_v2.md#combined-argument) | General event-norm FTC, two smoothings and finite weak-Fourier lemma, after reconstruction of every new translated law. |
| dependency | [Both joint-shell regularizations](Yin_C_G0641_v2.md#complete-additional-joint-shell-argument) | All rho/tau dyadic regularization estimates and constants on original/torus spaces, with the new all-shell premise proved in SB24. |
| dependency | [Entire centered torus support](Yin_C_G0638_v1.md#complete-local-modulation-calculation) | Actual unchanged centers, all rectangles, cardinality and torus mass; new closed-box alias, positivity and full original cost are paid here. |
| support | [Reuse and source limits](#reuse-and-source-boundary) | Exact inspection depths, no old schedule substitution, retained degree logarithm and log2..log4, no bounded-H or unrestricted completion. |
| review | [Independent entire finding](../audits/reviews/Yin_R_G0887_v1.md#stability-balanced-family-whole-independent-finding) | Whole SB1--SB24 and Sections1--8, exact new source/arithmetic/degree/full2d and probability premises, every finite coefficient and complete support/threshold, all five costs and arbitrary-sequence limits. |


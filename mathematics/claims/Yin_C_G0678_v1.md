---
author: Yin
---

# A weighted three-factor Salem family and its full finite Fourier return

Human author Yin.
Root requested checking whether fewer powered factors could give a genuine lower-dimensional family and warned that old phase-band conclusions cannot be transferred automatically.
Phase_bands found the exact unweighted odd-factor obstruction, proposed weights(1,1,2), and developed the source construction, actual projection and new finite-return argument below.
Root independently suggested the local3/4 amplitude scale as a candidate after the weighted repair was proposed.
Both are contributors, not independent reviewers.
No native prime search, numerical scan or new source acquisition is used.

## Statement

Use the SAME actual composite killer integer

    K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))).

It is not replaced by a prime or by2.
For every integer j>=4K, define

    a_j=min{p prime:p>(j+1)K}, L_j=K+a_j+2,
    c_j=min{p prime:p>(L_j+1)^2},
    M_j=floor(a_j/4), d_j=K+a_j+c_j=c_j+L_j-2.             (WT1)

For e=(K,a_j,c_j) and w=(1,1,2), put

    Qraw_j(x)=(x^2-1)product_(i=1)^3(x^e_i-1)
       -(x/2)sum_(i=1)^3 w_i(x^e_i+1)product_(l!=i)(x^e_l-1),
    P_j(x)=Qraw_j(x)/(x-1)^2.                              (WT2)

The weighted torsion classification and interlacing proof below establish that P_j is its ACTUAL monic integral irreducible Salem minimal polynomial, with even degree d_j, trace0 and no further cyclotomic factor.
Its exterior root beta_j satisfies

    2<beta_j<4, log2<m(P_j)=log beta_j<log4,
    16M_j^2<d_j<2^10 M_j^2.                               (WT3)

This is a new weighted construction from accepted general MS05 inputs, not an application of its even-q construction theorem to odd q.
In fact, for any three exponents e_i>=2, the UNWEIGHTED candidate obtained by retaining all three coefficients1/2 and dividing by(x-1)^2 is monic rational with next coefficient1/2.
It is not integral and cannot itself be an algebraic-integer minimal polynomial.
Clearing denominators does not repair its monic normalization.
This obstruction concerns that exact whole candidate, not every possible factor or every three-factor construction.

Use ALL d=d_j relation columns in the original2d coordinates:

    A_rel=[P_j,xP_j,...,x^(d-1)P_j], G=A_rel^T A_rel,
    Pi=A_rel G^-1 A_rel^T, v_n(z)=(1,z,...,z^(n-1))^T,
    h_orig=v_(2d)^*Pi v_(2d)/(2d),
    k_j=1-h_orig, f_(j,tau)=(1-h_orig/tau)_+.

All Haar measures are probability measures, angular variation is unnormalized and Fourier coefficients use negative exponentials.
For fixed j,tau>0, W_*(f)=sum_(n!=0)abs(fhat(n)) is finite.
For0<tau<=1, each actual unit-circle root of P_j has cap value1 and value minus Haar mean at least1/2.

The NEW two-coordinate phase and three-coordinate cap are

    R(z,u)=(z^K-1)(u-1),
    S(z,u)=(z^K+1)(u-1)+(u+1)(z^K-1)=2(z^K u-1),
    Acal=-(z^2-1)R-zR+zS/2,
    Bcal= (z^2-1)R-zR-zS/2,
    g_0=abs(Acal)^2+abs(Bcal)^2, Ncal=2Acal conjugate(Bcal),
    U=Acal/Bcal off their common zeros, U=0 at their common zeros,
    V(z,u)=U(z^-1,u^-1), g(z,u)=g_0(z^-1,u^-1),
    h(z,u,w)=(1+Re(wV(z,u)))/2, F_tau=(1-h/tau)_+,
    iota_j(z)=(z,z^a_j,z^c_j),
    H_j(gamma)=gamma_0+a_j gamma_1+c_j gamma_2.

Let nu_1,nu_2,nu_3 denote Haar in the corresponding dimensions.
For EVERY t in T^3, let mu_(j,t) be the pushforward of nu_1 through z to t*iota_j(z).
No independence is assumed under these correlated original and translated laws.

### Sharp torus amplitude order

For every0<s<=1,

    s^(3/4)/(256pi^2)<=nu_2{g<=s}<=3s^(3/4),
    rho^(3/4)/(512pi^2)
       <=integral rho/(g+rho)dnu_2<=12rho^(3/4), 0<rho<=1. (WT4)

The upper sublevel estimate3s^(3/4) remains valid for every s>0.
These are bounds for the NEW actual torus amplitude, not a claim about Fourier optimality or original-circle independence.

### Paid actual comparison and all five costs

Write A(z)=Acal(z,z^a), B(z)=Bcal(z,z^a), where a=a_j,c=c_j,L=L_j,M=M_j.
Their exact common factor is z-1, and A_0=A/(z-1), B_0=B/(z-1) have no circle zero.
Let varphi(z)=(A/B)(z^-1) extend smoothly with varphi(1)=-1, and set

    h_phase=(1+Re(z^c varphi))/2,
    E=[1+pi L(5+2log c)]/c,
    epsilon=(4L-3)/(2d)+E/2,
    E_w=8(3+3pi),
    delta_*=[28(1+60pi)]^-2,
    C_obs=2/delta_*, C_stab=33C_obs+3.

Then

    ||h_orig-h_phase||_1<=epsilon
                     <=E_w M^-1(1+log M),                  (WT5)
    ||f_(j,tau)-(1-h_phase/tau)_+||_1<=min{1,C_stab epsilon},
    ||f_(j,tau)-(1-h_phase/tau)_+||_(3/2)
                          <=min{1,(C_stab epsilon)^(2/3)}  (WT6)

for every tau>0 in(WT6).
The actual ratio, its pole, all original2d rank corrections and the zero cyclic sample at1 are paid in the proof.

Define angular derivative constants on the fixed two-torus by

    D_l=||partial_l Acal||_infinity+||partial_l Bcal||_infinity, l=1,2,
    G_K=sqrt(||g||_infinity),
    C_w=6pi[1+10(D_1+D_2)+2(G_K+1)],
    C_s=3pi[18*96^(2/3)(D_1+D_2)+4^(2/3)],
    C_2=512C_w+2C_s.

For a probability measure mu let

    N_mu(v)=sup_(E measurable,mu(E)>0)mu(E)^(-1/3)integral_E abs(v)dmu.

For every actual M>=max{2,C_w}, take rho=(C_w/M)^2 and define

    V_rho=Ncal(z^-1,u^-1)/(g+rho),
    h_rho=(1+Re(wV_rho))/2, F_(tau,rho)=(1-h_rho/tau)_+,
    Fej_N(t)=N^-1 abs(sum_(r=0)^(N-1)exp(irt))^2,
    P_M=Fej_N^2/[(2N^2+1)/(3N)], N=floor(M/2)+1,
    Q_(tau,rho)=F_(tau,rho)*(three-coordinate product of P_M),
    B_w(j,tau)=min{1,(C_stab epsilon)^(2/3)}
                                         +C_2 M^-1 tau^(-1/6).

P_M is positive with mass1, closed Fourier support[-M,M] and first angular moment at most3pi/M.
For every0<tau<=1/64,

    N_nu1(f_(j,tau)-Q_(tau,rho) composed with iota_j)
        +N_nu3(F_tau-Q_(tau,rho))<=B_w(j,tau).              (WT7)

For EVERY finite Gamma in the CLOSED integer box[-M,M]^3,

    sum_(gamma in Gamma)
       abs(fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma))
           <=5 card(Gamma)^(2/3) B_w(j,tau).               (WT8)

The original images are distinct, and the bound includes empty sets, signed and zero indices, and all endpoints.
The five terms are the original comparison, TWO regularizations and TWO smoothings, on their respective actual probability spaces.
All regularization estimates allow rho/tau>1.
The statement supplies no lower bound for a selected mass of the new Fourier coefficients, no new width-divergence exponent and no transfer of C629 v6's four-coordinate bands to this three-coordinate cap.
It leaves the explicit new band-capture problem at the precise finite price(WT8).
The fixed positive measure interval(WT3) also excludes any near-one or unrestricted G0001 conclusion.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Complete argument

### 1. Exact odd-factor obstruction and the weighted source adaptation

For three arbitrary e_i>=2, the unweighted Qraw has top two terms x^(2+sum e_i)-(3/2)x^(1+sum e_i).
At1 it has exact order2, since its half-sum has nonzero quadratic coefficient-sum_i product_(l!=i)e_l while its first term has order4.
Thus its monic rational quotient by(x-1)^2 has degree sum e_i and next coefficient2-3/2=1/2.
No constant rescaling preserves monicity while making that coefficient integral.
This checks why the EVEN-q premise of the inspected MS05 Lemma12 cannot be omitted.

For the repair define the Q-defined weighted hypersurface in(C^*)^4 by

    h_w(x_0,x_1,x_2,x_3)
       =2(x_0^2-1)product_(i=1)^3(x_i-1)
         -x_0 sum_(i=1)^3 w_i(x_i+1)product_(l!=i)(x_l-1),
    w=(1,1,2).

This is its entire defining polynomial; no denominator defines the variety.
Its exponent support lies in{0,1,2} times{0,1}^3, so its size is at most24 and its Euclidean diameter is at most sqrt7.
The accepted GENERAL MS05 Theorem8/Corollary9 therefore supplies the sufficient common torsion-coset exponent

    K_3^*=product_(p<=24)p * lcm(1,...,38416),
    38416=7^4*4^2.

The actual K is a multiple of K_3^*, since its prime product extends to48 and its lcm endpoint exceeds38416.
Indeed8^5*5^(5/2)>2*32768>38416.
This proves the killer property for this NEW weighted hypersurface, rather than assuming the old unweighted h_3 has the same zero set.

Here is the needed weighted torsion classification, proved as a local adaptation.
A point with exactly one powered coordinate equal1 cannot lie on h_w=0, because its unique remaining summand has nonzero weight.
If a torsion coset has x_0 nonconstant and two powered coordinates identically1, it lies in the corresponding B_il={x_i=x_l=1}.
Otherwise no powered coordinate is identically1.
On that coset choose an integer one-parameter monomial specialization avoiding all nonzero coordinate-exponent hyperplanes, and choose its sign so x_0 has positive exponent.
Where the powered factors do not vanish, its rational identity is

    x_0-x_0^-1=(1/2)sum_i w_i(x_i+1)/(x_i-1).

As the parameter tends to infinity, the left side is unbounded and every term on the right has a finite limit, including constant coordinates different from1.
This is impossible.
Thus every maximal torsion coset with x_0 nonconstant is a B_il.
A coset with exactly one powered coordinate identically1 is excluded by the same polynomial argument on a generic point.
These are the weighted analogues of Lemma10, proved here rather than attributed to the source's unweighted statement.

For every j>=4K, a>(j+1)K>4K^2 and c>(L+1)^2>a>K.
The primes a,c do not divide K and are distinct; K,a,c are pairwise coprime even though K is composite.
If a root of unity omega zeros h_w(omega,omega^K,omega^a,omega^c), put this point in a maximal torsion coset containing it.
Such a coset exists by maximizing its dimension among containing torsion cosets; proper containment increases dimension.
For a B_il, two powered coordinates1 and pairwise coprimality force omega=1.
Otherwise x_0 is constant and the common exponent K kills its value, so omega^K=1 supplies one powered coordinate1, which is impossible unless another is1.
Again omega=1.

At x=1 the raw weighted polynomial has exact order2 with nonzero coefficient-(ac+Kc+2Ka); its first term has order4.
Thus the complete cyclotomic factor is exactly(x-1)^2.
Modulo2 all weighted summands before division by2 reduce to the same product with total weight4, so Qraw is integral.
Monic division by(x-1)^2 leaves integral P.

For the weighted positive rational sum use the reduced denominator

    p(x)=product_(e in {K,a,c})(x^e-1)/(x-1)^2,
    q_0(x)/p(x)=(1/2)[(x^K+1)/(x^K-1)
                         +(x^a+1)/(x^a-1)+2(x^c+1)/(x^c-1)].

It has simple circle poles, including1, because the exponents are pairwise coprime.
Positive residues prevent cancellation; q_0 is integral by the parity calculation and monic division.
Positive scalar multiples preserve circular interlacing, so the accepted MS05 Proposition6 applies to these three positively weighted fractions.
The monic p has p(1)=0, and Proposition5(a) yields a Salem minimal polynomial times a possible cyclotomic factor, or the reciprocal quadratic alternative.
The exact torsion exclusion removes all extra factors, and the degree exceeds2, excluding the quadratic alternative.
This proves actual irreducibility and Salem eligibility for(WT2).

The raw leading terms are x^(K+a+c+2)-2x^(K+a+c+1).
Division by(x-1)^2 gives degree d=K+a+c with next coefficient0, so the trace is0.
K is even and a,c are odd, so d is even.
At the exterior root the weighted rational identity gives

    beta-beta^-1=(1/2)sum_i w_i(beta^e_i+1)/(beta^e_i-1).

The sum of weights is4, and each fraction lies strictly above1 and at most(beta+1)/(beta-1).
Thus beta>1+sqrt2>2 and beta+beta^-1<=4, proving(WT3)'s measure bounds.
This direct calculation does not invoke a new RY26 weighted theorem.

### 2. Actual sizes and the complete new alias box

For M=floor(a/4)>=2,4M<=a<4M+4<=6M.
Because a>2K and K>=3,

    4M<L<L+1=K+a+3<=2a<=12M,
    L>4K^2.

Integer Bertrand at(L+1)^2 gives

    (L+1)^2<c<2(L+1)^2,
    c<d=c+L-2<2c,
    16M^2<d<4(12M)^2<2^10 M^2.                            (WT9)

Moreover a>2M and c>a^2>2M(1+a).
The highest nonzero weighted coordinate in any nonzero delta in[-2M,2M]^3 dominates all lower coordinates, so H_j(delta)!=0 on the entire punctured CLOSED2M box.
Every difference of two closed-M indices lies there.
This proves exact finite coefficient return, injectivity on every selected box and exact finite mean equality on every translated mu_(j,t).
Translations multiply characters by unit scalars and do not alter this conclusion.

### 3. Complete original2d cyclic and interpolation reconstruction

Substitution of the new Acal,Bcal gives Qraw=A+x^c B.
They are integral of degree L: A has constant coefficient1 and leading coefficient-1, while B has constant coefficient-1 and leading coefficient1.
Their sum is A+B=-2x(x^K-1)(x^a-1).
At a root of exactly one of these two powered factors, the nonzero S term prevents a common root.
Since gcd(K,a)=1, their only common root is1, and

    [A/(x-1)](1)=K+a, [B/(x-1)](1)=-(K+a).

Their exact common factor is therefore x-1.
On the torus Acal/(zR)=-1-iD/2 and Bcal/(zR)=-1+iD/2 with real D, so their moduli agree.
Continuity and direct substitution show their common torus zeros are exactly z^K=u=1.
After cancellation, neither A_0 nor B_0 has a circle zero and varphi(1)=-1.

In the full2d window the raw relation matrix has2d-deg Qraw=c+L-4=d-2 independent columns.
Its range is contained in the original d-column P relation range with codimension2, so their projection difference has rank2.
Let S_c e_i=e_(i+1 mod c) and form

    V_c=[A(S_c);B(S_c);0_(2L-4)-by-c]

in the SAME2d coordinates.
The first c raw columns agree with V_c in columns0 through c-L-1, so their difference has rank at most L and the projection difference has rank at most2L.
The remaining L-4 raw columns extend the raw range by exactly L-4.
Thus, writing Pi_V for the range projection,

    ||Pi-Pi_V||_trace<=2+(2L)+(L-4)=3L-2.                 (WT10)

For every nontrivial c-th root omega, neither omega^K nor omega^a equals1 because c is coprime to K,a.
The c-mode at1 alone is zero; rank V_c=c-1.
Its two diagonal blocks are(I_c-J_c/c)/2 and its off-diagonal block is

    Pi_V,12(i,l)=(1/(2c))sum_(omega^c=1)
                              U(omega,omega^a)omega^(l-i).

The opposite block is its adjoint and the final2L-4 coordinates vanish.
The sample at omega=1 is zero, not the continuous phase value-1.
Define

    q(exp(it))=(1/c)sum_(l=1)^(c-1)
                           varphi(exp(2pi i l/c))Fej_c(t-2pi l/c).

The exact projection evaluation is

    v_(2d)^*Pi_Vv_(2d)=c-Fej_c+c Re(z^c q),
    k_V-(1-Re(z^c q))/2
         =((d-c)/(2d))(1+Re(z^c q))+Fej_c/(2d)>=0.

Here k_V=1-v^*Pi_Vv/(2d), abs(q)<=1 and deg_Fourier(q)<=c-1.
Since z^c q has zero mean, the last nonnegative correction has norm(L-1)/(2d).
The trace inequality from(WT10), using integral vv^*=I, therefore gives

    ||k_j-(1-Re(z^c q))/2||_1<=(4L-3)/(2d).               (WT11)

The actual phase has total variation2pi(K+a-1)=2pi(L-3), as also proved in Section4; in particular it is at most2pi L.
The finite grid-arc and Fejer moment argument, with oriented arc multiplicity at most c abs(t)/(2pi)+1 and moment at most pi(1/2+log c)/c, bounds the full-grid interpolation error by V(varphi)(5/4+(log c)/2)/c.
Changing its sample-1 at1 to0 adds Fej_c/c with norm1/c.
Thus ||q-varphi||_1<=E as defined in the statement.
This proves the first inequality(WT5) without a change of original normalization.

The exact budget satisfies epsilon<=(3+3pi)(L/c)(1+log c).
By(WT9), L/c<1/L<1/(4M), while c<288M^2 implies1+log c<7+2log M<=7(1+log M).
This is smaller than the stated E_w M^-1(1+log M).
The logarithmic unweighted interpolation cost remains present.

### 4. New actual phase, Gram pole and width-uniform original cap

On the original circle put

    D(t)=4sin t+cot(Kt/2)+cot(at/2),
    U_j(exp(it))=(2+iD)/(2-iD),
    varphi(exp(it))=exp(i psi(t)), psi(0)=pi,
    psi'=-4D'/(4+D^2)>0,
    Theta=ct+psi, h_phase=(1+cos Theta)/2.

Indeed D'<=4-(K+a)/2<0.
Each cotangent pole has positive residue, and the inverse phase extends smoothly with positive derivative there.
Over one turn there are K+a-1 distinct poles, counting the common pole0 once.
On each pole-free interval D decreases from positive to negative infinity and psi gains2pi, proving V(varphi)=2pi(L-3).
The full Theta increment is2pi(c+L-3)=2pi(d-1), with Theta'>=c.

The original positive definite Gram matrix gives the exact identity, without dividing by P,

    G_d=v_d^*G^-1v_d>0,
    h_orig=abs(P)^2G_d/(2d),
    h_phase=abs(z-1)^2 abs(P)^2/[4abs(A_0)^2],
    r=2abs(A_0)^2G_d/[d abs(z-1)^2], h_orig=r h_phase.      (WT12)

P(1)!=0, so h_0=h_orig(1)>0, and r has an actual pole at1.
The numerator T(t)=2abs(A_0(exp(it)))^2G_d(exp(it)) is a real even trigonometric polynomial of degree at most d+L-2.
Finite cosine division gives

    r=u+sigma,
    u=kappa/[4sin^2(t/2)],
    deg_Fourier(sigma)<=d+L-3=c+2L-5<3c,
    kappa=T(0)/d=4h_0/v_0^2<=4/c^2,
    v_0=c+2/(1/K+1/a).                                    (WT13)

Here the value of kappa follows from the exact limit at0; the uniform local bounds follow separately.
On abs(t)<=pi/c put R_*=2(1/K+1/a)>=2/K.
The elementary cotangent remainder bound gives D=R_*/t+E_*(t), abs(E_*)<=(L+4)abs(t).
Because c>L and L>4K^2,

    (L+4)t^2/R_*<pi^2/(4K)<1/2.

Consequently D has the sign of t and

    p(t)=Theta(t)-pi=ct+2arctan(2/D(t)),
    c abs(t)<=abs(p(t))<=c abs(t)+4K abs(t)<=3c abs(t).

The last step uses c>2K.
The extra cell I_0=[-t_*,t_*] defined by abs(p)<=pi therefore satisfies pi/(3c)<=t_*<=pi/c and nu_1(I_0)<=1/c.
On it h_phase=sin^2(p/2)<=9c^2t^2/4, so h_phase u<=9pi^2/4.
Off it, exact pole integration gives integral u<=12/(pi^2 c)<2/c.
Thus integral h_phase u<32/c.

On every angular interval of length2pi/c, each of the TWO cotangent families has at most one pole because K,a<c.
There are at most three regular pieces and inverse-phase increment at most6pi, so Theta increment is at most8pi.
In particular the weaker10pi and seven-contact-band bounds proved in C663 remain valid.
Every such interval has contact fraction at most7sqrt(delta) for h_phase<=delta,0<delta<=1, including endpoints and poles.

For every integer n>=1, the finite signed kernel2Fej_(2n)-Fej_n reproduces the CLOSED Fourier interval[-n,n].
The elementary Fejer square derivative estimate gives norm at most10n for its derivative, hence V(T)<=20pi n||T||_1 for every complex trigonometric polynomial of degree at most n.
Applying this at n=3c, cell means and cell variation give

    integral_(h_phase<=delta)abs(T)
        <=7sqrt(delta)[||T||_1+V(T)/c]
        <=7sqrt(delta)(1+60pi)||T||_1.

With delta=delta_* the right side is one quarter of ||T||_1.
Absorption proves ||T||_1<=C_obs integral h_phase abs(T).
Use this for T=sigma-1 in(WT13), with

    h_phase abs(sigma-1)<=abs(h_orig-h_phase)+h_phase u.

It yields ||sigma-1||_1<=C_obs(epsilon+32/c).
Set eta_r=abs(r-1)/max{1,r}, with eta_r(1)=1.
Inside I_0 it is at most1; outside, it is at most abs(sigma-1)+u, so integral eta_r<=C_obs(epsilon+32/c)+3/c.
Since epsilon>=(4L-3)/(2d)>1/c, this is at most C_stab epsilon.
The exact scalar inequality

    abs((1-rx/tau)_+-(1-x/tau)_+)<=abs(r-1)/max{1,r}

holds for x,r>=0,tau>0, by splitting r<=1 and r>=1.
It applies to(WT12) almost everywhere, and the cap difference is bounded by1.
Its L1 bound proves its strong3/2 bound by taking the power2/3, establishing(WT6).
No lower ratio or moving-input Taylor assumption has been used.

### 5. Exact two-sided3/4 amplitude estimate on the new torus

Write z=exp(it),u=exp(is), x=Kt/2,y=s/2, P_*=sin x sin y and Q_*=sin(x+y).
Direct substitution in the NEW Acal,Bcal gives

    g_0=32P_*^2+8[Q_*+4sin(t)P_*]^2.

Therefore, for G_*=P_*^2+Q_*^2,

    (32/33)G_*<=g_0<=288G_*.                              (WT14)

Indeed Q_*^2<=2[Q_*+4sin(t)P_*]^2+32P_*^2 proves the lower bound, and the square inequality proves the upper bound.
The comparison is uniform in sin t, so no independence of t and Kt is needed.

Modulo pi, x and y are independent uniform angles on the two-torus; the map t to Kt preserves circle Haar.
Use coordinates alpha=x and v=x+y, each represented in[-pi/2,pi/2); this linear change also preserves Haar.
Then Q_*^2=sin^2 v and abs(P_*)=abs(sin alpha sin(v-alpha)).
If G_*<=s<=1, abs(v)<=(pi/2)sqrt(s), abs(P_*)<=sqrt(s), and the sine Lipschitz bound gives

    sin^2 alpha<=sqrt(s)+abs(sin alpha)abs(v)
                  <=sqrt(s)+(sin^2 alpha+v^2)/2,
    sin^2 alpha<=2sqrt(s)+v^2<=5sqrt(s).

For a uniform angle on this pi-circle, the probability abs(sin angle)<=r is at most r for0<=r<=1.
Thus the set just described has probability at most sqrt5 s^(3/4), including when the alpha bound exceeds1 by using the trivial probability1.
Apply this with s replaced by(33/32)s in(WT14); for s<=32/33 it gives a bound less than3s^(3/4), and for s>32/33 the trivial bound1 proves the same estimate.
This proves the global upper sublevel bound in(WT4).

For the lower bound, in the(alpha,v) torus take

    abs(alpha)<=s^(1/4)/32, abs(v)<=s^(1/2)/32, 0<s<=1.

There abs(P_*)<=abs(alpha)(abs(alpha)+abs(v)), and abs(Q_*)<=abs(v).
Writing delta=1/32, one gets G_*<=(4delta^4+delta^2)s.
Since288(4delta^4+delta^2)<1, the whole rectangle lies in g_0<=s.
Its Haar measure is4delta^2 s^(3/4)/pi^2=s^(3/4)/(256pi^2).
The inverse-coordinate definition of g preserves these estimates.

Finally, layer cake gives for0<rho<=1

    integral rho/(g+rho)
       <=3rho^(3/4)integral_0^1 t^(-3/4)(1-t)^(3/4)dt
       <=12rho^(3/4).

On g<=rho the integrand is at least1/2, giving the lower bound in(WT4).
This proves both sides directly, without a named sublevel or interpolation theorem.

### 6. Every translated law and the new contact-weighted strong costs

The following pointwise estimates depend only on equal modulus of Acal,Bcal and their angular derivatives; they are re-applied with TWO phase coordinates and ONE cap coordinate.
For r_s=s/(g+s), s>=rho, and V_eta=eta/(eta+h_rho),0<eta<=1, the elementary derivative calculations give

    abs(partial_l g)<=2D_l sqrt(g),
    abs(partial_l r_s)/r_s<=D_l/sqrt(s),
    abs(partial_l h_rho)<=6D_l sqrt(h_rho)/sqrt(g+rho), l=1,2,
    abs(partial_3 h_rho)<=sqrt(h_rho),
    h_rho>=rho/[2(g+rho)].

For clarity, away from g=0 write V_rho=aV with a=g/(g+rho) and h_rho=a h+(1-a)/2.
Equal modulus gives abs(partial_l arg V)<=sqrt2 D_l/sqrt(g), while abs(partial_l h)<=sqrt(h)abs(partial_l arg V).
The a partial_l h term is at most sqrt2 D_l sqrt(h_rho)/sqrt(g+rho).
The partial_l a times(h-1/2) term is at most rho D_l sqrt(g)/(g+rho)^2, which is at most D_l sqrt(h_rho)/[sqrt2 sqrt(g+rho)] by h_rho>=rho/[2(g+rho)] and2sqrt(rho g)<=rho+g.
Their sum is below the stated6D_l envelope, and continuity of the smooth quotient Ncal/(g+rho) supplies g=0.
The last lower bound then yields logarithmic derivative sum at most

    A_w/sqrt(rho), A_w=10(D_1+D_2)+2(G_K+1)

for both W=V_eta and W=r_s V_eta, with all THREE coordinates included.

For I_W^*=sup_t integral W dmu_(j,t)<=1, telescope coordinate paths in convolution by the three positive P_M kernels.
The CLOSED box of Section2 makes this polynomial's mean exactly its torus mean on EVERY translated circle.
FTC and the kernel moments therefore imply

    I_W^*<=integral W dnu_3+[3pi A_w/(M sqrt(rho))]I_W^*.

Since M sqrt(rho)=C_w=6pi(1+A_w), the bracket is less than1/2.
For r_s alone the same argument applies whenever M sqrt(s)>=C_w.
All suprema are finite and all intermediate translations are included.

Under product Haar ONLY, the conditional w integral is

    integral_w V_eta=eta/sqrt((eta+1/2)^2-(a/2)^2)<=sqrt(eta).

Together with(WT4), positive absorption proves on every translated mu_(j,t), and with no larger constants on the torus,

    integral r_s<=24s^(3/4) if0<s<=1 and M sqrt(s)>=C_w,
    integral V_eta<=2sqrt(eta),
    integral r_s V_eta<=24sqrt(eta)s^(3/4), s>=rho,
    mu{h_rho<=eta,g<=s}<=96sqrt(eta)s^(3/4), s>=rho.       (WT15)

For s>1 the trivial torus amplitude integral<=1 proves the same displayed product bound.
Thus all amplitude shells are included, and nonlinear means have not been asserted equal without the paid absorption.

For the present event norm, a tail mu{abs(v)>t}<=(B/t)^(3/2) implies

    integral_E abs(v)<=integral_0^infinity min{mu(E),(B/t)^(3/2)}dt
                        =3B mu(E)^(1/3).

Thus N_mu(v)<=3B; Holder also gives N_mu(v)<=||v||_(3/2).
The event-first integral triangle inequality follows by Tonelli, and N_mu(1_E)=mu(E)^(2/3).
These are direct scalar facts, not an assumed strong Hausdorff--Young inequality.

Let w_tau=1_(h_rho<=tau)(g+rho)^(-1/2).
For0<t<=1 the tail is at most4sqrt(tau); for1<t<=rho^(-1/2), (WT15) at s=t^-2 bounds it by96sqrt(tau)t^(-3/2); for larger t it is empty.
Hence

    N_mu(w_tau)<=3*96^(2/3)tau^(1/3),
    N_mu(1_(h_rho<=tau))<=[4sqrt(tau)]^(2/3).

Every coordinate path satisfies the clipped FTC bound with envelopes6D_l tau^-1/2 w_tau for l=1,2 and tau^-1/2 1_(h_rho<=tau) for l=3.
This holds on every path by splitting its open contact components; it does not restrict an ambient almost-everywhere derivative to a singular circle.
Integrating first over a base event, then the path and positive kernels, with every intermediate translated law covered by(WT15), gives C_s M^-1 tau^-1/6 for EACH smoothing.

For regularization let D_cap=F_tau-F_(tau,rho) and lambda=rho/tau, with no assumption lambda<=1.
Because h_rho=a h+(1-a)/2 and tau<=1/64, D_cap>=0, its nonzero set lies in h<=tau and

    D_cap<=min{1,rho/[2tau(g+rho)]}.

At common zeros both caps vanish; on every translated circle these form only a finite set.
The region g<rho contributes at most48rho^(3/4) to integral D_cap^(3/2).
Partition its complement into disjoint half-open shells s<=g<2s, s=2^k rho,k>=0.
On an active shell h_rho<=eta_s=tau+rho/(2s)<1, so(WT15) at2s bounds its probability by96*2^(3/4)sqrt(eta_s)s^(3/4).
For rho<=s<=lambda, eta_s<=3rho/(2s), and96*2^(3/4)*sqrt(3/2)<256.
Summing D_cap<=1 over these shells gives at most

    256sqrt(rho) sum_(s<=lambda)s^(1/4)
          <1792sqrt(rho)lambda^(1/4)
           =1792rho^(3/4)tau^(-1/4).

Here1/(1-2^(-1/4))<7.
For s>lambda, eta_s<=3tau/2 and D_cap^(3/2)<=(lambda/(2s))^(3/2), giving at most

    256*2^(-3/2)sqrt(tau)lambda^(3/2)sum_(s>lambda)s^(-3/4)
          <384sqrt(tau)lambda^(3/4)
           =384rho^(3/4)tau^(-1/4).

The last bound uses2^(-3/2)<1/2 and1/(1-2^(-3/4))<3.
All shells, including2s>1 and lambda>1, have been included.
As tau<=1, the total coefficient48+1792+384=2224 is below4096.
Thus EACH of the original and torus regularizations satisfies

    ||D_cap||_(3/2)<=4096^(2/3)sqrt(rho)tau^(-1/6)
                         =256sqrt(rho)tau^(-1/6).          (WT16)

The TWO regularizations and TWO smoothings sum to C_2 M^-1 tau^-1/6.
Adding the actual original comparison(WT6) proves(WT7), with no discarded probability-space term.

### 7. Direct finite weak Fourier bound, every index and the remaining interface

We prove the finite coefficient estimate at this NEW event exponent.
Suppose N_mu(v)<=B on a probability space and chi_1,...,chi_N are orthonormal characters of modulus1.
For B=0 the result is immediate.
The event definition gives mu{abs(v)>t}<=(B/t)^(3/2).
For any height T>0, split v=v_low+v_high at abs(v)=T.
The event norm and tail give

    ||v_high||_1<=B^(3/2)T^(-1/2),
    ||v_low||_2^2<=integral_0^T 2t mu{abs(v)>t}dt
                                        <=4B^(3/2)sqrt(T).

Given alpha>0 choose T=4B^3/alpha^2, making every high-part coefficient at most alpha/2.
Finite Bessel then bounds the count of full coefficients greater than alpha by

    (4/alpha^2)||v_low||_2^2<=32(B/alpha)^3.

For decreasing coefficient magnitudes b_l, approach alpha=b_l from below to include ties and get b_l<=32^(1/3)B l^(-1/3).
Since sum_(l=1)^N l^(-1/3)<=(3/2)N^(2/3),

    sum_(l=1)^N b_l<=5B N^(2/3),                          (WT17)

using(3/2)*32^(1/3)<5.
The empty-set case is zero.
This proof uses only finite Bessel and scalar truncation, and no uninspected external interpolation theorem.

The three-coordinate Q has support in[-M,M]^3, and Section2 ensures exact returned coefficients and distinct H_j(gamma) for every supplied Gamma.
Apply(WT17) on the original circle and on the three-torus, then use(WT7), proving(WT8) including all signs and endpoints.

For fixed j,tau, the original cap is continuous piecewise smooth with square-integrable derivative.
The level equation for the trigonometric h_orig is either constant or has finitely many zeros, so integration by parts and derivative Bessel imply absolute Fourier summability.
The full original projection has rank d and integral h_orig=1/2; at every circle root P vanishes under all relation-column evaluations.
For tau<=1, f<=1-h_orig, proving the contact margin stated above.

The new3/4 amplitude order and p=3/2 finite return are fully established, but a lower bound for a useful finite sum of NEW Fhat_tau remains an additional obligation.
The old C629 v6 proof has two independently varying phase coordinates beyond its fixed z witness, whereas the present phase has only(z,u).
Neither its integer centers nor its k,m rectangles and cardinality are asserted to carry over.
Any future width-divergence claim must construct its actual new bands, pay their whole support in(WT8), and then substitute the actual degree(WT9) and original epsilon(WT5).
The present family has positive measure above log2 and cannot be used as an unproved near-one family.

## Source inspection and reuse boundary

The source is the retained MS05 arXiv:math/0308213v2,31March2004, title-page19February2004, at the existing MS05-U001 account.
This author round directly text-read the retained PDF's pages3--6 and8--10: circular-interlacing definition, Propositions5(a)/6, torsion-coset convention, Theorem8 statement, Corollary9, Lemmas10--12 and the stated finite-computation limitation.
No new rendered-page inspection, source acquisition or complete original-proof audit is claimed.
The existing accepted general interlacing and torsion-exponent statements retain their source depth; Mann/Schmidt proofs and the source's optimized degree theorem remain outside it.
The unweighted Lemma12 is used only to identify its explicit EVEN-q restriction.
The weighted hypersurface classification, killer applicability, parity, actual trace and construction are project deductions proved here, not attributed to an uninspected weighted MS05 theorem.
The precise numerical source input is integer Bertrand at the stated existing C356/C217/Mig78 account; every present threshold is an integer.
C663's generic finite reproduction and scalar absorption mechanism are applied only after the NEW phase, polynomial degree and pole estimates have been proved.
C637 provides the unchanged positive kernel normalization/support/moment.
C641 supplies equal-modulus pointwise derivative and event-first FTC mechanisms; their new dimensions, amplitude exponent, costs and every translated-law premise are paid above.
The classical event norm and height splitting retain C641's existing attribution account to Tao's245C Notes1, Section2 equation(9)/Exercise17 and the two-height decomposition in Section3 Theorem27.
That source account covers1<p<infinity for the event-integral norm; it is attribution only, while the present p=3/2 constants and all needed finite Fourier estimates are proved in Sections6--7.
No new primary inspection of those Tao passages or general interpolation proof is claimed in this round.
No C633 v2 two-sided amplitude function, C629 v6 four-coordinate witnesses, C635/C639 selected-support conclusion or old-family degree theorem is silently substituted.

## Assessment history

### Decision weighted-three-factor-open

| Field | Value |
| --- | --- |
| date | 2026-10-24T03:08 |
| status | open |
| reason | Register the exact odd-factor integrality obstruction and the complete weighted(1,1,2) actual Salem family, with source/killer/interlacing applicability, full original2d comparison and Gram pole, sharp two-sided3/4 torus amplitude, every translated-law estimate and all five costs in the new p=3/2 finite return. The entire author-checked result awaits fresh independent whole review. A new Fourier mass/band construction is explicitly unpaid, so no new width-divergence exponent, near-one family or unrestricted conclusion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire weighted-family statement](#statement) | WT1--WT8: actual new polynomials and degree/trace/measure, precise odd-factor obstruction, original2d laws, sharp amplitude, all-width original stability, all five finite costs and every closed three-box Gamma, with the band-capture boundary. |
| argument | [Complete weighted-family proof](#complete-argument) | Sections1--7/WT9--WT17: new torsion classification/killer/parity/interlacing, exact projection/sample/pole/local count, both amplitude bounds, every translated mean/path/shell and finite weak-Fourier proof. |
| dependency | [Accepted general MS05 inputs](../audits/literature/MS05/Yin_U001.md#ms05-u001) | Exact general circular-interlacing and torsion-coset-exponent sections at retained source depth; odd-factor restriction is respected and the weighted adaptation is proved here. |
| dependency | [Integer Bertrand statement](Yin_C_G0356_v1.md#argument) | Actual integer(L+1)^2 threshold, accepted bounded statement depth only. |
| support | [Bertrand source limit](../audits/literature/Mig78/Yin_U001.md#mig78-u001) | Existing length-account attribution and unchanged absence of a new classical proof audit. |
| dependency | [Finite cyclic projection mechanism](Yin_C_G0171_v1.md#two-block-circulant-rank-transfer) | Finite block/rank/Fourier algebra, rebuilt at new raw codimension2 and exact2d normalization. |
| dependency | [Finite Fejer interpolation mechanism](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | General grid-arc/moment and inverse sample orientation; new phase variation, zero mode and all new dimensions are explicit here. |
| dependency | [Adopted finite reproduction and absorption](Yin_C_G0663_v1.md#decision-whole-reviewed-2026-10-24) | Generic finite derivative/endpoint kernel and scalar cap mechanisms after the weighted new phase, degree and pole premises are checked. |
| dependency | [Positive finite kernel](Yin_C_G0637_v1.md#complete-argument) | Squared-Fejer mass, closed support and first angular moment in each coordinate. |
| dependency | [Pointwise and event-path mechanisms](Yin_C_G0641_v2.md#combined-argument) | Equal-modulus phase derivative algebra and pathwise clipped FTC only; all new amplitude/event exponents, three-coordinate translations, shell constants and finite Fourier proof are established here. |
| support | [Existing classical event-norm attribution](Yin_C_G0641_v2.md#reuse-and-source-boundary) | Its actual Tao Notes1 equation9/Exercise17/Theorem27 height-splitting source account, at attribution-only depth; no new source-proof coverage or imported strong Hausdorff--Young theorem. |
| support | [Exact source and reuse limits](#source-inspection-and-reuse-boundary) | Primary passages actually read, accepted external depth versus new weighted deductions, and the unpaid new Fourier band/mass interface. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T03:29 |
| status | proved |
| reason | The entire fixed WT1--WT17 statement and seven-section proof were directly read, including source applicability, weighted actual polynomial, original2d projection and Gram pole, all translated laws and every finite-return cost. Fresh isolated whole R899v2 was read in full and independently reconstructs the complete theorem. Adopt the whole actual family and finite return, using only corrected v2: its preserved v1 omitted 1/d in its own sigma prose, while the target normalization was correct. No new band-mass lower bound, width-divergence rate, near-one family or unrestricted completion is asserted by this adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire weighted-family statement](#statement) | WT1--WT8: actual new polynomials and degree/trace/measure, precise odd-factor obstruction, original2d laws, sharp amplitude, all-width original stability, all five finite costs and every closed three-box Gamma, with the band-capture boundary. |
| argument | [Complete weighted-family proof](#complete-argument) | Sections1--7/WT9--WT17: new torsion classification/killer/parity/interlacing, exact projection/sample/pole/local count, both amplitude bounds, every translated mean/path/shell and finite weak-Fourier proof. |
| dependency | [Accepted general MS05 inputs](../audits/literature/MS05/Yin_U001.md#ms05-u001) | Exact general circular-interlacing and torsion-coset-exponent sections at retained source depth; odd-factor restriction is respected and the weighted adaptation is proved here. |
| dependency | [Integer Bertrand statement](Yin_C_G0356_v1.md#argument) | Actual integer(L+1)^2 threshold, accepted bounded statement depth only. |
| support | [Bertrand source limit](../audits/literature/Mig78/Yin_U001.md#mig78-u001) | Existing length-account attribution and unchanged absence of a new classical proof audit. |
| dependency | [Finite cyclic projection mechanism](Yin_C_G0171_v1.md#two-block-circulant-rank-transfer) | Finite block/rank/Fourier algebra, rebuilt at new raw codimension2 and exact2d normalization. |
| dependency | [Finite Fejer interpolation mechanism](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | General grid-arc/moment and inverse sample orientation; new phase variation, zero mode and all new dimensions are explicit here. |
| dependency | [Adopted finite reproduction and absorption](Yin_C_G0663_v1.md#decision-whole-reviewed-2026-10-24) | Generic finite derivative/endpoint kernel and scalar cap mechanisms after the weighted new phase, degree and pole premises are checked. |
| dependency | [Positive finite kernel](Yin_C_G0637_v1.md#complete-argument) | Squared-Fejer mass, closed support and first angular moment in each coordinate. |
| dependency | [Pointwise and event-path mechanisms](Yin_C_G0641_v2.md#combined-argument) | Equal-modulus phase derivative algebra and pathwise clipped FTC only; all new amplitude/event exponents, three-coordinate translations, shell constants and finite Fourier proof are established here. |
| support | [Existing classical event-norm attribution](Yin_C_G0641_v2.md#reuse-and-source-boundary) | Its actual Tao Notes1 equation9/Exercise17/Theorem27 height-splitting source account, at attribution-only depth; no new source-proof coverage or imported strong Hausdorff--Young theorem. |
| support | [Exact source and reuse limits](#source-inspection-and-reuse-boundary) | Primary passages actually read, accepted external depth versus new weighted deductions, and the unpaid new Fourier band/mass interface. |
| review | [Corrected complete isolated whole review](../audits/reviews/Yin_R_G0899_v2.md#whole-weighted-three-factor-fourier-v2-finding) | Entire target and exact direct-input/source scope, full original normalization and all five costs; only v2 is selected, with its explicit reviewer normalization correction and original source-proof limits. |

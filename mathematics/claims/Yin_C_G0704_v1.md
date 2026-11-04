---
author: Yin
---

# Rational Fejer interpolation and a logarithm-free actual degree-width criterion

Human author Yin.
Root proposed the finite Hankel and Toeplitz-circulant comparison and its actual square-prime consequence.
Phase_bands checked the finite algebra, pole multiplicities, matrix orientation, original-law transfer and all costs below.
Both are contributors, not independent reviewers.
The actual polynomial family is exactly the adopted C678 square-prime weighted family; the earlier logarithmically balanced C684 family and square-log C701 family retain their separate scopes.
No native test, prime enumeration or new source theorem is used.

## Statement

### Rational interpolation with all finite endpoints

Let f=p/q be a complex rational function, written in reduced polynomial form, without poles on the unit circle.
Set D=max{deg p,deg q}, B=||f||_infinity on the circle, and use D=0 when f is zero.
For every positive integer c define

    Fej_c(z)=c^-1 abs(sum_(r=0)^(c-1)z^r)^2,
    F_c f=Fej_c*f,
    I_c f(z)=c^-1 sum_(omega^c=1)f(omega)Fej_c(z/omega).

All integrals and convolutions use circle Haar of mass1.
Then

    ||f-F_c f||_1<=DB/c,
    ||I_c f-F_c f||_1<=2DB/c,
    ||f-I_c f||_1<=3DB/c.                              (RF1)

Repeated poles, poles at zero, a polynomial part, c=1 and D=0 are included.
In particular, the result applies to a rational unimodular phase with B=1 and requires no one-sided pole restriction.

### The same actual square-prime weighted Salem family

Fix exactly

    K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))),
    j integer, j>=4K, a=a_j=min{p prime:p>(j+1)K},
    L=L_j=K+a+2, M=M_j=floor(a/4), X=L+1,
    c=c_j=min{p prime:p>X^2}, d=d_j=c+L-2=K+a+c.          (RF2)

For e=(K,a,c), w=(1,1,2), put

    Qraw_j(x)=(x^2-1)product_(i=1)^3(x^e_i-1)
       -(x/2)sum_(i=1)^3 w_i(x^e_i+1)product_(l!=i)(x^e_l-1),
    P_j(x)=Qraw_j(x)/(x-1)^2.                           (RF3)

These are precisely the adopted C678 actual polynomials, not changed exponents substituted into another family's conclusion.
Each P_j is its monic integral irreducible Salem minimal polynomial, of even degree d_j and trace0, with no further cyclotomic factor.
Its exterior root beta_j and genuine degree obey

    2<beta_j<4, log2<m(P_j)=log beta_j<log4,
    16M_j^2<d_j<2^10 M_j^2.                            (RF4)

Keep ALL d relation columns in the original2d coordinates:

    A_rel,j=[P_j,xP_j,...,x^(d-1)P_j],
    G_j=A_rel,j^T A_rel,j, Pi_j=A_rel,j G_j^-1 A_rel,j^T,
    v_n(z)=(1,z,...,z^(n-1))^T,
    h_orig,j=v_(2d)^*Pi_j v_(2d)/(2d),
    f_(j,tau)=(1-h_orig,j/tau)_+, tau>0.                 (RF5)

Every circle and torus Haar measure below has mass1, and Fourier coefficients use negative exponentials.
Write ||f||_A=sum_(n in Z)abs(fhat(n)) and W_*(f)=sum_(n!=0)abs(fhat(n)).
For fixed j,tau this original cap has finite A norm; it equals1 at every actual circle root, and for tau<=1 its value there minus its Haar mean is at least1/2.

Define the unchanged fixed torus phase and actual character by

    R(z,u)=(z^K-1)(u-1), S(z,u)=2(z^K u-1),
    Acal=-(z^2-1)R-zR+zS/2,
    Bcal= (z^2-1)R-zR-zS/2,
    U=Acal/Bcal off common zeros, U=0 at common zeros,
    V(z,u)=U(z^-1,u^-1), h(z,u,w)=(1+Re(wV(z,u)))/2,
    F_tau=(1-h/tau)_+,
    iota_j(z)=(z,z^a,z^c), H_j(gamma)=gamma_0+a gamma_1+c gamma_2.

For EVERY t in T^3, let mu_(j,t) be the pushforward of circle Haar by z to t*iota_j(z).
These are the actual correlated original and translated laws.
For every actual j and every0<eta<=1,

    mu_(j,t){h<=eta}<=2sqrt(eta) for EVERY t.             (RF6)

Product Haar has the smaller constant1.
Finite common-zero conventions change none of these integrals.

Put A(z)=Acal(z,z^a), B(z)=Bcal(z,z^a), A_0=A/(z-1), B_0=B/(z-1), and let varphi(z)=(A/B)(z^-1) be the smooth cancelled inverse phase, with varphi(1)=-1.
Define

    h_phase=(1+Re(z^c varphi))/2,
    epsilon_j=(4L-3)/(2d)+[3(L-1)+1]/(2c),
    delta_*=[28(1+60pi)]^-2,
    C_obs=2/delta_*, C_stab=33C_obs+3.

The new original comparison is

    ||h_orig,j-h_phase||_1<=epsilon_j<4L/c<1/M,
    ||f_(j,tau)-F_tau composed with iota_j||_1
                             <=min{1,C_stab epsilon_j},
    ||f_(j,tau)-F_tau composed with iota_j||_2
                             <=min{1,sqrt(C_stab epsilon_j)} (RF7)

for EVERY tau>0.
The genuine pole and full inverse Gram are retained; no uniform lower ratio is assumed.

### Complete localized finite return and degree criterion

Use exactly the adopted C693 fixed patch and bump

    x_*=(pi/K,pi),
    phi(t,s)=2arctan([4sin t+cot(Kt/2)+cot(s/2)]/2),
    -Hess(phi)>=lambda I on closed B_(4delta)(x_*),
    0<delta<min{pi/(8K),pi/8},
    chi(x)=exp[-1/(1-abs(x-x_*)^2/delta^2)] on B_delta(x_*),
    chi=0 elsewhere, periodically extended.

The following constants depend only on that fixed choice and K:

    s_chi=||chi||_2^2>0,
    D_phi,l=sup_(B_delta(x_*))abs(partial_l phi), l=1,2,
    B_der=[sum_(l=1)^2(||partial_l chi||_2+D_phi,l||chi||_2)^2]^(1/2),
    C_chi=||(1-Delta)^2 chi||_1, Delta=partial_t^2+partial_s^2,
    A_chi=13C_chi,
    C_osc>=1 with abs((chi U^k)hat(n))<=C_osc/k for all integers k>=1,n in Z^2,
    C_0=ceil(max{2,2B_der/sqrt(s_chi),24sqrt(3)C_osc C_chi/s_chi}),
    a_loc=3s_chi/(4C_osc), B_chi=||chi||_infinity,
    S_loc=sum_(l=1)^2||partial_l chi||_infinity+B_chi(D_phi,1+D_phi,2+1),
    C_sm=3pi sqrt(2)S_loc.

The existence and accepted source scope of C_osc and the ENTIRE localized square estimate

    sum_(abs(p),abs(q)<=C_0k)abs((chi U^k)hat(p,q))>=a_loc k

are precisely C693's c-independent conclusion at this same K and phase.
Put

    b(z,u)=chi(z^-1,u^-1), b_j(z)=b(z,z^a),
    Phi_tau=b F_tau, f_loc,j,tau=b_j f_(j,tau),
    B_rf(j,tau)=B_chi min{1,sqrt(C_stab epsilon_j)}
                                     +2C_sm M^-1 tau^-1/4.

For M>=2,0<tau<=1/64 and EVERY finite Gamma in the CLOSED integer box[-M,M]^3,

    sum_(gamma in Gamma)
      abs(fhat_loc,j,tau(H_j(gamma))-Phihat_tau(gamma))
                      <=sqrt(card(Gamma))B_rf(j,tau),   (RF8)
    ||b_j||_A<=A_chi,
    W_*(f_loc,j,tau)<=A_chi[W_*(f_(j,tau))+1].           (RF9)

This includes all signs, the empty set, zero and closed endpoints.
All five costs are paid: the original comparison, two identically zero regularization differences for the exact localized function, and two L2 smoothings.
No unlocalized regularization cost is set to zero.

For0<tau<=1/64 define

    L_tau=floor(1/(4sqrt(tau))),
    Gamma_tau={(p,q,k):1<=k<=L_tau, abs(p),abs(q)<=C_0 k},
    N_tau=sum_(k=1)^(L_tau)(2C_0 k+1)^2<=(2C_0+1)^2 L_tau^3,
    C_mass=3a_loc/(1024pi),
    C_err=(2C_0+1)/8 max{B_chi sqrt(C_stab),2C_sm},
    H=M^2tau.

If M>=2 and C_0 L_tau<=M, all selected original frequencies are positive and distinct, and

    W_*(f_(j,tau))>=tau^-1/2/A_chi
                   *[C_mass-C_err(H^-1/4+H^-1/2)]-1.   (RF10)

Set

    H_rf=max{1,C_0^2/16,(4C_err/C_mass)^4,(4C_err/C_mass)^2},
    M_rf=ceil(max{2,8sqrt(H_rf)}),
    j_rf=max{4K,ceil(4M_rf/K)}, D_rf=2^10 H_rf.

For EVERY actual j with M_j>=M_rf and EVERY width in the entire nonempty strip

    H_rf M_j^-2<=tau<=1/64,

one has

    W_*(f_(j,tau))>=C_mass tau^-1/2/(2A_chi)-1.          (RF11)

Every j>=j_rf meets that M threshold.
For EVERY positive shrinking sequence tau_j->0 with d_j tau_j>=D_rf eventually, (RF11) holds eventually and W_*(f_(j,tau_j)) tends to infinity.
In particular, for every FIXED h>=D_rf, the actual widths tau_j=h/d_j satisfy

    W_*(f_(j,tau_j))>=C_mass sqrt(d_j)/(2A_chi sqrt(h))-1
                                                        ->infinity. (RF12)

No monotonicity is required; arbitrary sequence entry times may depend on the sequence.
This removes the degree logarithm in the sufficient criterion for this actual square-prime family.
It asserts no sharp smaller-height threshold, optimality, every-degree coverage, near-one family or unrestricted G0001 completion.
The original positive interval log2<m(P_j)<log4 and source-inspection limits remain.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Complete argument

### 1. Finite Hankel contraction and the first interpolation cost

A rational function with no circle pole is holomorphic on an annulus about the circle.
Its Laurent coefficients a_n=fhat(n) therefore decay geometrically in both directions, so every series and limiting diagonal expansion below converges absolutely on the circle.
If f=0 the result is immediate; otherwise use its reduced degrees.
Polynomial division and partial fractions write f as a polynomial part of degree at most k=max{deg p-deg q,0}, possibly constant or zero, plus principal parts at the finitely many poles alpha of q.
If deg p<deg q the polynomial is zero and we take k=0.
Writing m_alpha for the pole multiplicities gives

    k+sum_alpha m_alpha=max{deg p,deg q}=D.

Constants contribute no Hankel entries and no interpolation error.

For positive integers c,N consider the two FINITE matrices

    H^+_(c,N)=(a_(i+j+1))_(0<=i<c,0<=j<N),
    H^-_(c,N)=(a_(-(i+j+1)))_(0<=i<c,0<=j<N).

Both have operator norm at most B.
For example, their positive-index sesquilinear form is the integral of

    f(z)[sum_i conjugate(y_i)z^(-i-1)] [sum_j x_j z^-j],

and the L2 Cauchy--Schwarz inequality bounds its modulus by B||x||_2||y||_2.
The negative-index case uses positive exponents instead.
This is a finite calculation, not an assumption about an unbounded formal Hankel operator.

An exterior pole alpha, abs(alpha)>1, contributes only nonnegative coefficients.
The coefficients of(z-alpha)^(-nu), n>=0, are

    (-alpha)^(-nu) binom(n+nu-1,nu-1) alpha^-n.

The whole principal part at a pole of order m therefore contributes a geometric sequence times a polynomial of degree at most m-1.
Substituting n=i+j+1 shows that all its columns lie in the span of the m vectors with coordinates i^r alpha^-i,0<=r<m.
Thus its TOTAL positive Hankel rank is at most m, including all lower powers at that pole.

An interior nonzero pole contributes only negative coefficients, with the coefficient of z^-n in(z-alpha)^(-nu) equal to

    binom(n-1,nu-1)alpha^(n-nu), n>=1.

This polynomial binomial is zero for1<=n<nu, so the displayed formula holds for every positive n.
Its whole order-m principal part again has total rank at most m in the negative block.
A pole at zero of order m is a negative polynomial of degree m and has Hankel rank at most m, because entries vanish when i+j+1>m.
The ordinary polynomial part has the same bound k in the positive block.
Consequently there are fixed integers r_+,r_- with r_++r_-<=D and

    rank H^+_(c,N)<=r_+, rank H^-_(c,N)<=r_-

for EVERY c,N.
Cancellation can reduce these ranks, which only strengthens the upper bound.

For any finite matrix H with singular-value decomposition sum_l s_l u_l v_l^*, its diagonal generating polynomial

    z sum_(i,j)H_ij z^(i+j)
      =z sum_l s_l(sum_i u_l,i z^i)(sum_j conjugate(v_l,j)z^j)

has L1 norm at most sum_l s_l by Cauchy--Schwarz and Parseval, since each singular vector has Euclidean norm1.
Apply this to H^+_(c,N) and H^-_(c,N), using z^-1 for the latter.
Their trace norms are bounded by r_+B and r_-B.
As N tends to infinity, the diagonal coefficient of a_n z^n is min{abs(n),c}a_n for n!=0.
Uniform convergence follows from the geometric Laurent decay.
After adding the two halves and dividing by c, the result is exactly

    f-F_c f=sum_(n!=0)min{abs(n)/c,1}a_n z^n.

Its L1 norm is at most(r_++r_-)B/c<=DB/c, proving the first part of(RF1).
This proof also covers c=1 and the polynomial-only cases without an infinite singular decomposition.

### 2. Finite Toeplitz-circulant rank with all repeated poles

Let v(z)=(1,z,...,z^(c-1))^T and form the c-by-c matrices

    T_ij=a_(j-i),
    B_c=c^-1 sum_(omega^c=1) f(omega)v(omega)v(omega)^*,
    0<=i,j<c.

Both have operator norm at most B.
For T this follows by compressing multiplication by f to the orthonormal functions1,z^-1,...,z^(-(c-1)); equivalently its finite quadratic/bilinear integral proves the same estimate.
For B_c the normalized discrete vectors v(omega)/sqrt(c) form an orthonormal basis, so it is unitarily diagonal with eigenvalues f(omega).

Let S be the upper nilpotent shift S_ij=1 when j=i+1, zero otherwise, and C=S+e_(c-1)e_0^T its cyclic completion.
For c=1 this means S=0,C=1 and the same formulas hold.
The vectors v(omega) are eigenvectors of C with eigenvalue omega, so B_c=f(C).
In particular rank(S-C)=1.

For an exterior pole alpha, the Toeplitz matrix of(z-alpha)^(-nu) is(S-alpha I)^(-nu), by its convergent nonnegative power expansion.
Its sampled matrix is(C-alpha I)^(-nu).
Let X=(S-alpha I)^-1 and Y=(C-alpha I)^-1.
The resolvent identity gives rank(X-Y)<=1; write X-Y=u v^* when it is nonzero.
For EVERY integer1<=nu<=m,

    X^nu-Y^nu=sum_(r=0)^(nu-1)X^r u v^* Y^(nu-1-r).

Thus all differences for the ENTIRE principal part of order m have ranges in the SAME span{u,Xu,...,X^(m-1)u}.
Its total rank contribution is at most m, not the sum1+...+m.

For an interior pole alpha, put R=S^*, Q=C^* and

    X=R(I-alpha R)^-1, Y=Q(I-alpha Q)^-1.

The Toeplitz and sampled matrices of(z-alpha)^(-nu) are respectively X^nu and Y^nu, from the negative-power expansion z^-nu(1-alpha z^-1)^(-nu).
All inverses exist since abs(alpha)<1, including alpha=0.
The exact identity

    X-Y=(I-alpha R)^-1(R-Q)(I-alpha Q)^-1

has rank at most1.
The same common-range power identity proves total rank at most m for the complete interior principal part.
In particular, poles at zero require no limiting argument.

For the whole polynomial part P of degree k, T=P(S) and B_c=P(C).
The power-difference identity, now based on S-C, places the range of P(S)-P(C) in the span of k vectors u,Su,...,S^(k-1)u.
This is valid even when k>=c, and constants cancel.
Adding the finitely many principal parts proves

    rank(T-B_c)<=k+sum_alpha m_alpha=D,
    ||T-B_c||_trace<=2DB,

because ||T-B_c||_op<=2B.

For any c-by-c matrix E, its singular decomposition and circle Parseval give

    integral abs(v(z)^*E v(z))<=||E||_trace.

Indeed each singular summand is a product of two trigonometric polynomials whose L2 norms are the two unit-vector norms.
The exact orientations above yield

    c^-1 v(z)^*T v(z)=F_c f(z),
    c^-1 v(z)^*B_c v(z)=I_c f(z).

The second identity uses abs(v(z)^*v(omega))^2=c Fej_c(z/omega).
Therefore ||I_c f-F_c f||_1<=2DB/c.
Together with Section1 this proves all of(RF1).

### 3. Exact adopted family and the improved original2d comparison

The polynomial inputs(RF2)--(RF3) agree literally with C678 WT1--WT2.
Its accepted general MS05 torsion-coset exponent divides the actual composite K; the weighted hypersurface classification excludes every torsion root except1, whose multiplicity is exactly2.
Its parity calculation uses total weight4, and its positive-residue circular interlacing gives the actual irreducible Salem minimal polynomial after this exact cyclotomic removal.
We use those already adopted actual-family conclusions, including trace0 and log2<m(P)<log4, at their existing source-inspection depth.
No new weighted source construction or unweighted odd-factor theorem is asserted.

For clarity the arithmetic and every changed comparison premise are checked explicitly.
For actual j>=4K,

    a>4K^2, L>4K^2, 4M<=a<4M+4<=6M,
    4M<L<X<=2a<=12M,
    X^2<c<2X^2, c>X^2>a^2>L, c<d<2c.

The strict prime bounds are the accepted integer Bertrand input at the integer X^2.
In particular K,a,c are pairwise coprime, K remains composite, and a>2M, c>a^2>2M(1+a).
The highest nonzero coordinate dominates on every punctured CLOSED[-2M,2M]^3 character box.
Thus all closed-M differences have nonzero image, all selected images are distinct, and every nonconstant closed-M character has mean zero on EVERY translated actual circle.
Also16M^2<X^2<c<d<2c<4X^2<=576M^2<2^10M^2, proving the degree bounds(RF4).

The actual specialized A,B have degree L, Qraw=A+z^cB, constants1,-1 and leading coefficients-1,1.
Their sum is-2z(z^K-1)(z^a-1), their only common root is1, and A_0(1)=K+a=-B_0(1).
Hence their common factor is exactly z-1 and A_0,B_0 have degree L-1 and no circle zero.
The actual inverse phase varphi=A_0(z^-1)/B_0(z^-1) is rational unimodular, with numerator and denominator degrees at most L-1 after multiplying both by z^(L-1).
Any further cancellation reduces that degree.
Thus(RF1) applies with B=1,D<=L-1.

The full raw Qraw relation space has d-2=c+L-4 independent columns in the SAME2d coordinates and codimension2 inside the d-column P space.
Compare its first c columns with

    V_c=[A(S_c);B(S_c);0_(2L-4)-by-c],

where S_c is the lower cyclic coefficient shift.
Their first c-L columns agree, so the projection correction is at most2L in trace norm; the remaining L-4 columns and the original codimension2 give

    ||Pi_j-Pi_V||_trace<=3L-2.

This lower coefficient shift is a separate matrix from the upper Toeplitz shift in Section2.
All nontrivial c-th root modes have nonzero equal-modulus A,B, while the mode1 vanishes, so rank(V_c)=c-1.
Its actual missing phase sample is0 at1, not varphi(1)=-1.
If

    q(z)=c^-1 sum_(omega^c=1,omega!=1)varphi(omega)Fej_c(z/omega),

then abs(q)<=1, its Fourier degree is at most c-1, and the exact block projection gives

    v_(2d)^*Pi_V v_(2d)=c-Fej_c+c Re(z^c q).

The nonnegative correction from 1-v^*Pi_Vv/(2d) to(1-Re(z^cq))/2 has mean(L-1)/(2d).
Combining it with the full trace correction yields

    ||h_orig,j-(1+Re(z^c q))/2||_1<=(4L-3)/(2d).

Replacing the full-grid sample-1 by0 adds Fej_c/c, with L1 norm1/c.
The new rational estimate therefore gives

    ||q-varphi||_1<=[3(L-1)+1]/c.

Adding half this cost proves the first bound of(RF7), with the EXACT displayed epsilon.
Since d>c and L>4M,

    epsilon_j<=(7L-5)/(2c)<4L/c<4/L<1/M.              (RF13)

No angular first-moment logarithm remains in this original comparison.

### 4. Full Gram ratio, its genuine pole and width-uniform observability

The complete Gram G_j is positive definite and G_d(z)=v_d(z)^*G_j^-1v_d(z)>0.
The actual exact identities, without division by P, are

    h_orig,j=abs(P)^2G_d/(2d),
    h_phase=abs(z-1)^2 abs(P)^2/[4abs(A_0)^2],
    r=2abs(A_0)^2G_d/[d abs(z-1)^2], h_orig,j=r h_phase. (RF14)

They hold away from1, including the other contacts by the displayed formulas.
Since P(1)!=0, h_0=h_orig,j(1)>0, and r has a genuine pole at1.
For D(t)=4sin t+cot(Kt/2)+cot(at/2), the inverse lift varphi=e^(i psi) has psi(0)=pi, psi'=-4D'/(4+D^2)>0 and Theta=ct+psi with Theta'>=c.
The distinct original poles number K+a-1, with smooth positive-residue extensions.
Let v_0=c+2/(1/K+1/a) and T(t)=2abs(A_0(e^(it)))^2G_d(e^(it)).
The same actual finite cosine division gives

    r=u+sigma,
    sigma=(T(t)-T(0))/[4d sin^2(t/2)],
    u=kappa/[4sin^2(t/2)], kappa=T(0)/d=4h_0/v_0^2<=4/c^2,
    deg_Fourier(sigma)<=d+L-3=c+2L-5<3c.                (RF15)

The full1/d normalization in sigma is retained.
This coefficient identity does not replace the ratio by a fixed-j Taylor approximation.

The adopted pole/cell calculation requires only c>L, L>4K^2 and K,a<c, all verified in Section3.
Explicitly, on abs(t)<=pi/c, D=R_*/t+E_*, R_*=2(1/K+1/a)>=2/K, abs(E_*)<=(L+4)abs(t), and (L+4)t^2/R_*<pi^2/(4K)<1/2.
Thus p(t)=Theta(t)-pi=ct+2arctan(2/D(t)) satisfies c abs(t)<=abs(p(t))<=3c abs(t).
The central phase cell has probability at most1/c and boundary t_* between pi/(3c) and pi/c.
On it h_phase u<=9pi^2/4; outside it integral u<=12/(pi^2c)<2/c.
In particular integral h_phase u<32/c.

Each interval of length2pi/c has at most one pole of each cotangent family, inverse-phase increment at most6pi and full Theta increment at most8pi.
The seven-band contact estimate is at most7sqrt(delta) of each cell length.
The finite reproduction kernel2Fej_(2n)-Fej_n, with derivative norm at most10n, gives V(T)<=60pi c||T||_1 for every complex trigonometric polynomial of degree at most3c.
Cell means and variation imply

    integral_(h_phase<=delta)abs(T)
                         <=7sqrt(delta)(1+60pi)||T||_1.

At delta=delta_* the right side is at most one quarter of the norm, giving ||T||_1<=C_obs integral h_phase abs(T).
Apply this to the ACTUAL sigma-1; (RF14) gives

    ||sigma-1||_1<=C_obs(epsilon_j+32/c).

For eta_r=abs(r-1)/max{1,r}, extended by1 at1, its central-cell integral is at most1/c, and outside it is bounded by ||sigma-1||_1+2/c.
The exact epsilon_j>(4L-3)/(2d)>1/c, because d<2c and L>=2.
Hence integral eta_r<=C_stab epsilon_j.
The scalar inequality

    abs((1-rx/tau)_+-(1-x/tau)_+)<=abs(r-1)/max{1,r}

for x,r>=0,tau>0 proves the second bound in(RF7).
The difference is bounded by1, so the L2 bound follows by taking the square root.
The improved epsilon is used only after its exact actual-law proof; the entire small-r absorption and pole expenses remain.

### 5. Every translated contact law and all five localized costs

For an arbitrary translate write z=e^(i(t+alpha)),u=e^(i(at+beta)),w=e^(i(ct+gamma)).
The exact weighted inverse phase is(2-iD_(alpha,beta))/(2+iD_(alpha,beta)), with

    D_(alpha,beta)=4sin(t+alpha)+cot(K(t+alpha)/2)+cot((at+beta)/2).

On each regular interval its derivative is at most4-(K+a)/2<0.
There are N<=K+a distinct poles, each with positive residue2/K,2/a, or their sum at a coincidence.
The inverse Cayley phase extends smoothly with derivative limit4 divided by that residue, and it turns once per complementary interval.
Thus the full phase Theta has Theta'>=c and total increment2pi(c+N), where c+N<=d<2c.
Changing this increasing phase variable gives

    mu_(j,t){h<=eta}<=[(c+N)/c]*(2/pi)arcsin(sqrt(eta))
                                                   <=2sqrt(eta).

This proves(RF6) for every translate, including all pole coincidences and finite common-zero exceptions.
Only on product Haar do we condition on an independent w to get the smaller constant1.

The actual K,U,phi and fixed chi are identical to C693, so its all-frequency estimate and localized full-square mass apply exactly.
The probe b is supported away from all common zeros, and Phi_tau=bF_tau vanishes in their neighborhoods.
It is globally Lipschitz for each fixed tau>0.
For0<tau<=1/64 its coordinate-path derivative envelopes are

    [||partial_l chi||_infinity+B_chi D_phi,l]
                                 tau^-1/2 1_(h<=tau), l=1,2,
    B_chi tau^-1/2 1_(h<=tau), l=3.

The cutoff derivatives and the third coordinate are both included.
The actual every-translate contact bound makes their L2 norms at most sqrt(2) times these constants times tau^-1/4 on every intermediate path law.
The same estimate holds on product Haar.
Use the accepted exact positive kernel

    P_M=Fej_N^2/[(2N^2+1)/(3N)], N=floor(M/2)+1,
    Q_tau=Phi_tau*(P_M tensor P_M tensor P_M).

Its mass is1, support is in the CLOSED[-M,M] box in each coordinate, and its first shortest-angle moment is at most3pi/M.
Coordinate-path FTC, L2 integral triangle and positivity bound EACH smoothing error, on the original circle and on the torus, by C_sm M^-1 tau^-1/4.
The weighted actual original error from(RF7) is at most B_chi min{1,sqrt(C_stab epsilon_j)}.
The two regularization differences vanish identically because the exact localized function itself is the intermediate function.
Thus the total of the five comparison costs is exactly bounded by B_rf.

For the finite Q_tau, Section3's CLOSED2M nonalias property identifies its tested original and torus coefficients exactly and makes all H_j(gamma) distinct.
Finite Bessel and finite Cauchy--Schwarz give(RF8) for any finite Gamma.
The fixed Fourier estimate ||b||_A<=13C_chi=A_chi is the same C693 cutoff estimate.
Specialization u=z^a can only reduce its coefficient triangle upper bound, so ||b_j||_A<=A_chi.
Convolution of the absolutely summable coefficients gives

    W_*(b_j f)<=||b_j f||_A<=A_chi||f||_A<=A_chi(W_*(f)+1),

proving(RF9) with the entire original probe expense and its additive1 term.

### 6. Full selected support, exact error powers and actual degree

For every1<=k<=L_tau, the adopted direct scalar cap coefficient has abs(ghat_tau(k))>=3sqrt(tau)/(8pi).
Product-Haar w integration gives

    Phihat_tau(p,q,k)=ghat_tau(k)(bV^k)hat(p,q).

The second factor is the simultaneous inversion of chi U^k, so its entire radius-C_0k square has mass at least a_loc k.
Since L_tau>=1/(8sqrt(tau)) for tau<=1/64, the full selected mass is at least

    [3a_loc sqrt(tau)/(8pi)]sum_(k=1)^(L_tau)k
                                              >=C_mass tau^-1/2.

All triples, not a sparse replacement, are retained.
Their exact count is N_tau=sum_(k=1)^(L_tau)(2C_0k+1)^2<=(2C_0+1)^2 L_tau^3, so sqrt(N_tau)<=(2C_0+1)/(8tau^(3/4)).
If C_0L_tau<=M, every coordinate is in the allowed box and every image is at least c-M(1+a)>0.
The entire returned error before division by A_chi is at most

    (2C_0+1)/8 [B_chi sqrt(C_stab) M^-1/2 tau^-3/4
                                           +2C_sm M^-1 tau^-1].

Relative to tau^-1/2 these are exactly H^-1/4 and H^-1/2 for H=M^2tau.
Subtracting the full error and using(RF9) proves(RF10).

For H>=H_rf, each relative error times C_err is at most C_mass/4 and C_0L_tau<=C_0M/(4sqrt(H))<=M.
If M>=M_rf, the strip is nonempty and(RF11) holds uniformly, including its critical lower endpoint.
For j>=j_rf, a_j>(j+1)K>4M_rf implies M_j>=M_rf, paying the floor exactly.
By(RF4), d_j tau_j>=D_rf=2^10H_rf implies M_j^2tau_j>H_rf.
Every positive shrinking sequence with that eventual condition also eventually has tau_j<=1/64 and M_j>=M_rf, so(RF11) applies and diverges.
The fixed-h substitution tau_j=h/d_j gives(RF12) directly.

Finally rank(Pi_j)=d_j in the original2d_j coordinates gives integral h_orig,j=1/2 and0<=h_orig,j<=1.
Every actual circle root annihilates all relation columns, giving h_orig,j=0 and f=1 there.
For tau<=1, f<=1-h_orig,j proves the margin assertion.
For fixed j,tau, the clipped trigonometric polynomial is continuous and piecewise smooth, with square-integrable derivative.
Derivative Bessel and sum_(n!=0)n^-2<infinity imply finite A norm, covering all uses of coefficient convolution.

## Source and scope boundary

The focused reuse check found the exact reduced rational-pole/finite-Hankel rank and Fourier-half conventions in [Par88-U001v2](../audits/literature/Par88/Yin_U001.md#par88-u001), including its source Theorem3.11 at printed37--38/PDF45--46 and its [symbol-convention account](../audits/literature/Par88/Yin_U001.md#hankel-symbol-conventions).
This provides classical attribution and already inspected conventions, not a new source reading or proof audit.
The present finite upper-rank calculations, uniform contraction, two diagonal L1 estimates and full repeated-pole Toeplitz-circulant proof are given above; no AAK, Nehari, infinite singular expansion or uninspected interpolation theorem is invoked.
No priority claim is made for a general rational approximation mechanism.

C678 supplies the literally identical actual square-prime weighted family and its accepted MS05 source/killer/minimality depth, not another family's polynomial.
C701 and C678 supply the checked finite full-Gram pole and observability mechanisms; their needed inequalities are established here and the improved epsilon is inserted only after(RF13).
C696 supplies the generic localization/finite-L2/probe mechanisms after every actual translated-law and alias premise is proved here.
C693 supplies only the unchanged c-independent fixed patch, constants and localized full-square mass, retaining [Tao26-U003v2](../audits/literature/Tao26/Yin_U003.md#tao26-u003)'s primary-statement/applicability scope and unreviewed full-source proof.
C681 supplies the scalar cap coefficients and C637 the exact positive finite kernel.
The original2d projection, missing cyclic sample, complete inverse Gram, genuine pole, all five errors and full selected support remain part of the result.
The theorem removes the degree logarithm from a sufficient width criterion; it does not establish optimality, bounded small-H behavior, a near-one polynomial family or unrestricted Task completion.

## Assessment history

### Decision rational-fejer-actual-degree-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T06:45 |
| status | open |
| reason | Register the complete finite rational Fejer comparison, including both Hankel halves, all repeated poles and polynomial parts, finite Toeplitz/circulant orientation and both diagonal L1 bounds. Its application to the exact adopted C678 actual family removes the original interpolation logarithm and gives a fixed-large d*tau criterion with full original2d/Gram/pole/translated-law and five-cost support accounting. Root and phase_bands are contributors; fresh independent whole review remains required. All source depths, positive Mahler interval and unrestricted limits remain. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire rational and actual-family theorem](#statement) | RF1--RF12, all finite endpoints and rational poles, exact original family, all-law comparison, full selected support and fixed-height/sequence genuine-degree conclusions. |
| argument | [Complete finite and actual-law proof](#complete-argument) | Sections1--6/RF13--RF15: finite Hankel and repeated-pole matrix algebra, all original2d costs, full inverse Gram and pole, translated laws, localized five-cost return, whole support and degree/floor conversion. |
| dependency | [Exact adopted square-prime family](Yin_C_G0678_v1.md#decision-whole-reviewed-2026-10-24) | Literal WT1--WT3 actual polynomials, accepted weighted source/killer/minimality and positive Mahler interval, same torus phase and original raw/cyclic identities. |
| dependency | [Checked generic full-Gram mechanisms](Yin_C_G0701_v1.md#decision-whole-reviewed-2026-10-25) | Sections3--4 raw/cyclic/Gram/pole/cell observability mechanisms under explicit c>L, L>4K^2, K,a<c; these premises and actual square-family matrices are checked here. No square-log family conclusion is renamed. |
| dependency | [Integer prime interval](Yin_C_G0356_v1.md#argument) | Accepted integer Bertrand scope for the actual integer X^2; no prime enumeration or wider source proof. |
| dependency | [Localized finite-return mechanisms](Yin_C_G0696_v1.md#decision-whole-reviewed-2026-10-25) | Exact localization, coordinate-path L2 estimates, finite Bessel/Cauchy--Schwarz and complete original probe cost after the actual law and alias checks here. |
| dependency | [Identical actual torus patch](Yin_C_G0693_v2.md#decision-whole-reviewed-2026-10-24) | The same K,U, fixed bump/constants, all-frequency localized estimate and entire CB15 square mass; no old-family return imported. |
| dependency | [Scalar cap harmonics](Yin_C_G0681_v1.md#decision-whole-reviewed-2026-10-24) | Direct harmonic lower bound for0<tau<=1/64 and1<=k<=floor(1/(4sqrt(tau))). |
| dependency | [Positive finite kernel](Yin_C_G0637_v1.md#complete-argument) | Squared-Fejer normalization, positivity, closed support and first shortest-angle moment. |
| support | [Classical rational Hankel account](../audits/literature/Par88/Yin_U001.md#par88-u001) | Exact reduced-pole/multiplicity and symbol-convention attribution at its retained inspection depth; all needed finite estimates are proved here. |
| support | [Retained stationary-phase source](../audits/literature/Tao26/Yin_U003.md#tao26-u003) | Unchanged primary-statement/applicability depth underlying the C693 fixed patch, with no new full-source proof claim. |
| support | [Source and scope boundary](#source-and-scope-boundary) | Actual inputs, explicit reuse versus new finite algebra, positive Mahler interval and no unrestricted or optimality assertion. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T06:55 |
| status | proved |
| reason | Adopt the entire fixed rational interpolation and actual-family theorem after main reading of complete C704 and isolated independent whole R925. Both finite Hankel halves, complete repeated-pole Toeplitz/circulant rank budgets and orientations prove the full interpolation estimate. On the literal C678 family the original2d projection, missing mode, full Gram pole, every translated law, five localized costs and complete support give the logarithm-free fixed-large d*tau criterion. All finite endpoints, actual degree/floor and sequence quantifiers, positive Mahler interval and retained source depths remain; no optimal threshold or unrestricted Task conclusion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire rational and actual-family theorem](#statement) | RF1--RF12, all finite endpoints and rational poles, exact original family, all-law comparison, full selected support and fixed-height/sequence genuine-degree conclusions. |
| argument | [Complete finite and actual-law proof](#complete-argument) | Sections1--6/RF13--RF15: finite Hankel and repeated-pole matrix algebra, all original2d costs, full inverse Gram and pole, translated laws, localized five-cost return, whole support and degree/floor conversion. |
| dependency | [Exact adopted square-prime family](Yin_C_G0678_v1.md#decision-whole-reviewed-2026-10-24) | Literal WT1--WT3 actual polynomials, accepted weighted source/killer/minimality and positive Mahler interval, same torus phase and original raw/cyclic identities. |
| dependency | [Checked generic full-Gram mechanisms](Yin_C_G0701_v1.md#decision-whole-reviewed-2026-10-25) | Sections3--4 raw/cyclic/Gram/pole/cell observability mechanisms under explicit c>L, L>4K^2, K,a<c; these premises and actual square-family matrices are checked here. No square-log family conclusion is renamed. |
| dependency | [Integer prime interval](Yin_C_G0356_v1.md#argument) | Accepted integer Bertrand scope for the actual integer X^2; no prime enumeration or wider source proof. |
| dependency | [Localized finite-return mechanisms](Yin_C_G0696_v1.md#decision-whole-reviewed-2026-10-25) | Exact localization, coordinate-path L2 estimates, finite Bessel/Cauchy--Schwarz and complete original probe cost after the actual law and alias checks here. |
| dependency | [Identical actual torus patch](Yin_C_G0693_v2.md#decision-whole-reviewed-2026-10-24) | The same K,U, fixed bump/constants, all-frequency localized estimate and entire CB15 square mass; no old-family return imported. |
| dependency | [Scalar cap harmonics](Yin_C_G0681_v1.md#decision-whole-reviewed-2026-10-24) | Direct harmonic lower bound for0<tau<=1/64 and1<=k<=floor(1/(4sqrt(tau))). |
| dependency | [Positive finite kernel](Yin_C_G0637_v1.md#complete-argument) | Squared-Fejer normalization, positivity, closed support and first shortest-angle moment. |
| support | [Classical rational Hankel account](../audits/literature/Par88/Yin_U001.md#par88-u001) | Exact reduced-pole/multiplicity and symbol-convention attribution at its retained inspection depth; all needed finite estimates are proved here. |
| support | [Retained stationary-phase source](../audits/literature/Tao26/Yin_U003.md#tao26-u003) | Unchanged primary-statement/applicability depth underlying the C693 fixed patch, with no new full-source proof claim. |
| support | [Source and scope boundary](#source-and-scope-boundary) | Actual inputs, explicit reuse versus new finite algebra, positive Mahler interval and no unrestricted or optimality assertion. |
| review | [Fresh independent whole rational Fejer finding](../audits/reviews/Yin_R_G0925_v1.md#whole-rational-fejer-review) | Entire RF1--RF15 statement and proof, all rational finite endpoints and matrix conventions, complete actual-family original laws/costs/support and genuine-degree thresholds, exact source attribution and limits. |


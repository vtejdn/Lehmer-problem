---
author: Yin
---

# Actual fast-phase occupation and a bounded-variation cap return

Human author Yin.
The phase_bands contributor developed and checked the same-circle weighted occupation estimate, the complete actual rank/interpolation variation, and the resulting finite return and degree consumers.
Root proposed investigating contact occupation after the exact C653 phase calculation.
These are contributors, not independent reviewers of the present argument.
No numerical experiment, native scan, prime enumeration or new original-source proof inspection is used.

## Statement

Use the two ACTUAL families in adopted [C648](Yin_C_G0648_v1.md#statement), with all the following data fixed.
Put

    K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))),
    a_j=min{p prime:p>(j+1)K},
    b_j=min{p prime:p>(K+a_j+3)^2},
    L_j=K+a_j+b_j+2, M_j=floor(a_j/4), j>=1,
    c_j^square=min{p prime:p>(L_j+1)^2},
    n_j=min{N positive integer:N^11>=(L_j+1)^25},
    c_j^balanced=min{p prime:p>n_j},
    d_j^sigma=c_j^sigma+L_j-3, sigma in{square,balanced}.

For ell^sigma=(K,a_j,b_j,c_j^sigma) the actual polynomial is

    Qraw_j^sigma(x)=(x^2-1)product_(i=0)^3(x^ell_i^sigma-1)
       -(x/2)sum_(q=0)^3(x^ell_q^sigma+1)product_(i!=q)(x^ell_i^sigma-1),
    P_j^sigma=Qraw_j^sigma/(x-1)^3.

Both are the source-certified monic integral irreducible Salem minimal-polynomial families of C648, with even degree, trace-1, no further cyclotomic factor, and

    log2<m(P_j^sigma)<log4.                                  (BV1)

The two schedules remain separately named.
In the ORIGINAL2d coordinates, where d=d_j^sigma, A_rel has ALL d columns P,xP,...,x^(d-1)P and

    R_orig=I-A_rel(A_rel^T A_rel)^-1 A_rel^T,
    v_(2d)(z)=(1,z,...,z^(2d-1))^T,
    k_j^sigma(z)=(2d)^-1 v_(2d)(z)^*R_orig v_(2d)(z),
    psi_tau(s)=(1-(1-s)/tau)_+,
    f_(j,tau)^sigma=psi_tau(k_j^sigma),
    W_*(f)=sum_(h in Z,h!=0)abs(fhat(h)).

All Haar measures have mass one, angular variation is UNNORMALIZED, and Fourier coefficients use the negative exponential convention.
On the torus define exactly

    R_tor=(z^K-1)(u-1)(v-1),
    S_tor=(z^K+1)(u-1)(v-1)+(z^K-1)(u+1)(v-1)
                              +(z^K-1)(u-1)(v+1),
    Acal=-(z^2-1)R_tor-zR_tor/2+zS_tor/2,
    Bcal=(z^2-1)R_tor-zR_tor/2-zS_tor/2,
    g_0=abs(Acal)^2+abs(Bcal)^2, Ncal=2Acal conjugate(Bcal).

Put U=Acal/Bcal off their common-zero set and U=0 on that set, and set

    V(z,u,v)=U(z^-1,u^-1,v^-1), g=g_0(z^-1,u^-1,v^-1),
    h=(1+Re(wV))/2, Kcal=1-h, F_tau=(1-h/tau)_+,
    iota_j^sigma(z)=(z,z^a_j,z^b_j,z^(c_j^sigma)),
    H_j^sigma(gamma)=gamma_0+a_j gamma_1+b_j gamma_2+c_j^sigma gamma_3.

The translated original laws are the pushforwards of circle Haar through z to t*iota_j^sigma(z), for EVERY t in T^4.
Their joint-shell inputs are the ones actually established for both schedules in C644/C648, not independence assumptions.

### Weighted occupation on the same original circle

Abbreviate a=a_j,b=b_j,L=L_j,c=c_j^sigma,d=d_j^sigma.
Let A(z)=Acal(z,z^a,z^b), B(z)=Bcal(z,z^a,z^b).
Cancel their exact common factor(z-1)^2 to extend U_j=A/B smoothly to the circle, with U_j(1)=-1, and put

    varphi_j(z)=U_j(z^-1),
    h_phase(z)=(1+Re(z^c varphi_j(z)))/2, K_phase=1-h_phase.

Thus (1-h_phase/tau)_+ equals the actual F_tau pullback outside its Haar-null point at1.
There is a smooth angular lift psi of varphi_j with

    psi'(t)>0, psi(t+2pi)=psi(t)+2pi(L-4),
    Theta(t)=ct+psi(t), Theta'(t)>=c,
    h_phase(exp(it))=(1+cos Theta(t))/2.                      (BV2)

For EVERY nonnegative continuous periodic weight w of bounded variation and EVERY eta>0,

    integral_T w 1_(h_phase<=eta)dnu_1
       <=sqrt(eta)[integral_T w dnu_1
                     +((L-4)sup(w)+V(w))/c].                 (BV3)

This bound uses the SAME original circle throughout.

### Actual variation and the new original cap cost

Use the actual c-grid Fejer interpolation, with the sample at1 replaced by0:

    Fej_c(t)=c^-1 abs(sum_(r=0)^(c-1)exp(irt))^2,
    theta_l=2pi l/c,
    q(exp(it))=c^-1 sum_(l=1)^(c-1)
                              varphi_j(exp(i theta_l))Fej_c(t-theta_l),
    K_q=(1-Re(z^c q))/2,
    E=[1+pi L(5+2log c)]/c,
    epsilon=(4L-5)/(2d)+E/2.

Define the explicit finite quantities

    V_bar=80pi L[1+log(4d)]+pi c E
             +26pi(L-4)[1+log(2c)]+2pi+pi(L-4),
    B_bar=epsilon+[V_bar+L-4]/c.                              (BV4)

For e=abs(k_j^sigma-K_phase), one has

    0<=e<=1, integral e<=epsilon, V(e)<=V_bar.                 (BV5)

Consequently, for EVERY0<tau<=1/64,

    ||f_(j,tau)^sigma-F_tau composed with iota_j^sigma||_(4/3)
       <=(32 B_bar)^(3/4)tau^(-3/8).                          (BV6)

In particular this comparison includes the actual full-rank error, cyclic finite correction, c-grid interpolation, missing sample, and product with z^c.
The unweighted error epsilon retains its logarithm.

### All five costs and arbitrary finite Fourier sets

Write the adopted fixed-K constants as

    D_l=||partial_l Acal||_infinity+||partial_l Bcal||_infinity, l=1,2,3,
    G_K=sqrt(||g||_infinity),
    C_w=6pi[1+10sum_l D_l+2(G_K+1)],
    C_s=3pi[24*64^(3/4)sum_l D_l+4^(3/4)],
    C_2=2*2048^(3/4)C_w+2C_s.

For a probability measure mu let

    N_mu(v)=sup_(E measurable,mu(E)>0)mu(E)^(-1/4)integral_E abs(v)dmu.

For EVERY actual j with M=M_j>=max{2,C_w}, put rho=(C_w/M)^2 and define

    V_rho=Ncal(z^-1,u^-1,v^-1)/(g+rho),
    h_rho=(1+Re(wV_rho))/2, F_(tau,rho)=(1-h_rho/tau)_+,
    P_M=J_(floor(M/2)+1), J_N=Fej_N^2/[(2N^2+1)/(3N)],
    Q_(tau,rho)=F_(tau,rho)*(four-coordinate product of P_M),
    B_BV^sigma(j,tau)=(32 B_bar)^(3/4)tau^(-3/8)
                                          +C_2 M^-1 tau^(-1/8).

The probability kernel P_M has CLOSED Fourier support[-M,M] and first angular moment at most3pi/M.
For EVERY0<tau<=1/64,

    N_nu1(f_(j,tau)^sigma-Q_(tau,rho) composed with iota_j^sigma)
          +N_nu4(F_tau-Q_(tau,rho))<=B_BV^sigma(j,tau).         (BV7)

For EVERY finite Gamma in the CLOSED integer box[-M,M]^4,

    sum_(gamma in Gamma)
       abs(fhat_(j,tau)^sigma(H_j^sigma(gamma))-Fhat_tau(gamma))
       <=8 card(Gamma)^(3/4) B_BV^sigma(j,tau).                (BV8)

All supplied original characters are distinct.
Empty sets, zero and negative harmonics, and the endpoints of the box are included.
The original comparison(BV6), TWO regularizations and TWO smoothings are all paid.

### Entire centered support and actual schedule bounds

Use the actual adopted C638 centers, with the following definitions:

    D_0(z)=-2(z-z^-1)+(z^K+1)/(z^K-1), b_0(z)=Im D_0(z),
    z_0=exp(i pi/K),
    -cot(t_(k,m)/2)=16sqrt(km)-b_0(z_0), t_(k,m) in(-pi,0),
    phi_z(t)=arctan(2/[b_0(z)-cot(t/2)]),
    n_(k,m)=floor((k+m)phi_(z0)'(t_(k,m))+1/2),
    C_loc=ceil(32000pi+1024pi(K+4)).

These are evaluated in their regular local neighborhoods, and abs(n_(k,m))<=14(k+m).
For L_tau=floor(1/(4sqrt(tau))) and integer J>=2 set

    R_z=ceil(C_loc J^(1/3)),
    R_u=ceil(C_loc sqrt(L_tau)J^(5/6)),
    G_(L_tau,J)={(-p,-q,m,k):1<=k<=L_tau,1<=m<=J,
                               abs(p)<=R_z,abs(q-n_(k,m))<=R_u},
    N_sel=L_tau J(2R_z+1)(2R_u+1)
       <=9(C_loc+1)^2 L_tau^(3/2)J^(13/6),
    C_sup=8[9(C_loc+1)^2]^(3/4)4^(-9/8).

Whenever the COMPLETE center-plus-radius conditions

    R_z,J,L_tau<=M, 14(L_tau+J)+R_u<=M                       (BV9)

hold, all selected original frequencies are distinct and strictly positive, and

    W_*(f_(j,tau)^sigma)>=3log(J+1)/(32768pi)
                              -8N_sel^(3/4)B_BV^sigma(j,tau). (BV10)

Define

    C_B=4+403pi+8pi^2, C_o=(2048 C_B)^(3/4),
    alpha_square=2, alpha_balanced=28/11, T_M=1+log M.

For EVERY actual M=M_j>=2 in either schedule,

    B_bar<=C_B (L/c)(1+log c)
          <=64 C_B M^(-alpha_sigma)T_M.                      (BV11)

Thus the ENTIRE subtracted term in(BV10) is at most

    C_sup J^(13/8)[
       C_o M^(-3alpha_sigma/4)T_M^(3/4)tau^(-15/16)
                             +C_2 M^-1 tau^(-11/16)].         (BV12)

### A common M critical strip and two actual-degree conclusions

Put

    M_BV=ceil(max{2,C_w,(C_loc+1)^(33/29),
                              7^(11/3),(C_loc+29)^(11/7)}),
    C_enl=C_sup(C_o+C_2),
    delta_square=3/22, delta_balanced=6/11.

For BOTH actual schedules, EVERY j with M=M_j>=M_BV, and EVERY pair H,tau of real numbers satisfying

    16<=H<=M^(16/11)/64, M^(-16/11)H<=tau<=1/64,              (BV13)

the choice J=floor(H^(1/4)) satisfies all(BV9) and gives

    W_*(f_(j,tau)^sigma)>=3log H/(131072pi)
       -C_enl[M^(-delta_sigma)T_M^(3/4)H^(-17/32)
                                                   +H^(-9/32)]. (BV14)

The constants and threshold are uniform over the ENTIRE two-parameter strip.
The actual degree estimates are

    256M_j^4<d_j^square<2^21 M_j^4,
    M_j^(50/11)<d_j^balanced<2^33 M_j^(50/11).                (BV15)

Consequently EVERY shrinking sequence tau_j->0 satisfying

    (d_j^square)^(4/11)tau_j->infinity                        (BV16)

has W_*(f_(j,tau_j)^square)->infinity.
Separately, EVERY shrinking sequence satisfying

    (d_j^balanced)^(8/25)tau_j->infinity                      (BV17)

has W_*(f_(j,tau_j)^balanced)->infinity.
For the corresponding schedule, each condition is equivalent to M_j^(16/11)tau_j->infinity.
No monotonicity or prescribed logarithmic enlargement is required.
The entry index for a sequence may depend on that sequence.
The square-family exponent4/11 strengthens its previous2/7 criterion; the balanced-family8/25 exponent is unchanged but the first error is smaller.

For every fixed input and width, the Wiener norm is finite and the original contact-minus-Haar margin is at least1/2 in the SAME2d window.
No bounded-H endpoint, optimality among all supports, every-large-degree family or unrestricted G0001 conclusion is asserted.
The exact total-measure restriction(BV1) remains essential to the scope.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Complete argument

### 1. Monotone actual phase and weighted occupation

The exact C653 calculation uses

    D_phase(t)=4sin t+cot(Kt/2)+cot(at/2)+cot(bt/2),
    U_j(exp(it))=(1+iD_phase(t))/(1-iD_phase(t)),
    D_phase'(t)<=4-(K+a+b)/2<0.                              (BV18)

The union of cotangent poles has exactly K+a+b-2=L-4 points.
Each pole has positive residue.
On every interval between successive poles, the argument derivative of U_j is2D_phase'/(1+D_phase^2)<0 and has integral-2pi.
At a pole t_0, write D_phase(t)=r/(t-t_0)+O(1) with r>0.
The derivative tends to-2/r<0, consistent with the smooth rational extension.
Thus inversion gives a smooth varphi_j phase with strictly positive derivative everywhere and total increment2pi(L-4).
This proves(BV2), including at the former poles.
It also gives V(varphi_j)=2pi(L-4).

For0<eta<=1, the set{(1+cos s)/2<=eta} occupies the fraction

    p_eta=(2/pi)arcsin(sqrt(eta))<=sqrt(eta)                  (BV19)

of EVERY interval of length2pi.
The inequality follows from convexity of arcsin on[0,1], by its chord from0 to1.
Change variables s=Theta(t) over any full t circle.
The inverse derivative is at most1/c; the s interval has exactly D_turn=c+L-4 full periods.
For W(s)=w(t(s)), on one such period I the deviation of W from its mean is at most its oscillation, hence at most V_I(W).
Therefore

    integral_(I intersect contact) W(s)ds
       <=p_eta integral_I W(s)ds+2pi p_eta V_I(W).

Sum over all D_turn periods, divide by2pi c, and use variation under increasing reparametrization to obtain

    integral w 1_contact dnu_1
       <=p_eta[(2pi c)^-1 integral_0^(2pi)w(t)(c+psi'(t))dt
                                                        +V(w)/c]
       <=p_eta[integral w dnu_1+((L-4)sup(w)+V(w))/c].

Here psi'>0 and its full integral is2pi(L-4).
This proves(BV3) for0<eta<=1.
For eta>1 the contact integral is at most integral w, while the displayed right side is larger.
Every step remains on the original circle; neither w nor any error function is averaged against an independent coordinate.

### 2. A complete cap lemma from that occupation

Keep the actual h_phase from(BV2), and let h_o be ANY continuous scalar in[0,1] on this circle.
The following argument applies for every0<tau<=1, and in particular throughout the stated tau<=1/64 range.
Let e=abs(h_o-h_phase), epsilon_e=integral e, V_e=V(e), assumed finite, and

    B_e=epsilon_e+[V_e+L-4]/c.

For0<s<=1 the continuous BV weight w_s=min(1,e/s) satisfies

    integral w_s<=epsilon_e/s, V(w_s)<=V_e/s, sup(w_s)<=1.

It is one on{e>=s}.
By(BV3) and s<=1,

    nu_1{e>=s,h_phase<=eta}<=sqrt(eta)B_e/s, eta>0.           (BV20)

Put D_cap=abs((1-h_o/tau)_+-(1-h_phase/tau)_+).
Then D_cap<=min(1,e/tau), and D_cap!=0 implies h_phase<=tau+e.
The set e=0 contributes zero.

On0<e<=tau split into disjoint shells s/2<e<=s, s=tau*2^-n,n>=0.
On a shell D_cap^(4/3)<=(s/tau)^(4/3), and the active set lies in{e>=s/2,h_phase<=2tau}.
Equation(BV20) bounds its measure by2sqrt(2)B_e sqrt(tau)/s.
Sum the geometric series to obtain

    integral_(0<e<=tau) D_cap^(4/3)
       <=[2sqrt(2)/(1-2^(-1/3))]B_e tau^(-1/2)
       <15 B_e tau^(-1/2).

On e>tau use the shells s<e<=2s, s=tau*2^n,n>=0, retaining only s<1.
The active set lies in{e>=s,h_phase<=3s};(BV20) remains valid even when3s>1.
Using D_cap<=1 and extending the resulting positive geometric sum gives

    integral_(e>tau) D_cap^(4/3)
       <=[sqrt(3)/(1-2^(-1/2))]B_e tau^(-1/2)
       <7 B_e tau^(-1/2).

The endpoint e=1 is in the final retained shell and e=tau is in the first low shell.
For the first numerical inequality use2^(-1/3)<4/5 and2sqrt(2)*5<15; for the second use2^(-1/2)<3/4 and4sqrt(3)<7.
Hence

    integral D_cap^(4/3)<=32 B_e tau^(-1/2).                  (BV21)

Taking the3/4 power proves the claimed generic norm bound.
No regularization or asymptotic estimate entered this lemma.

### 3. A finite Dirichlet derivative bound for the actual rank error

For integer N>=1 let D_N(t)=sum_(abs(n)<=N)exp(int).
If |t|<=1/N then |D_N'(t)|<=N(N+1)<=2N^2.
If1/N<=|t|<=pi, differentiate
D_N(t)=sin((N+1/2)t)/sin(t/2) and use sin(|t|/2)>=|t|/pi to get

    abs(D_N'(t))<=(3pi/2)N/abs(t)+pi^2/(2t^2).

The normalized integral is therefore at most

    2N/pi+(3/2)N log(pi N)+(pi/2)N
       <=10N[1+log(2N)].                                    (BV22)

The final loose inequality follows already from3<pi<4 and log2<1.
For any degree-N trigonometric polynomial T, finite orthogonality gives T'=T*D_N'.
Integrating the finite convolution by the triangle inequality yields
V(T)=2pi||T'||_1<=2pi||T||_1||D_N'||_1.

For the ACTUAL cyclic comparison, the adopted C648 rank and finite-correction bounds state

    ||k-k_V||_1<=(3L-3)/(2d),
    ||k_V-K_q||_1=(L-2)/(2d),
    ||k-K_q||_1<=(4L-5)/(2d)<2L/d.                           (BV23)

Both k and K_q are trigonometric polynomials of degree at most N=2d-1: k uses the full2d vector, q has degree c-1, and c<d.
Substituting this exact N into(BV22) proves

    V(k-K_q)<=80pi L[1+log(4d)].                             (BV24)

Thus the actual rank error is paid through its L1 bound AND its full degree.
No uninspected L1 Bernstein inequality is invoked.

### 4. Complete variation of the actual grid interpolation

Let g_step take the sample varphi_j(exp(i theta_l)) on the centered grid cell
[theta_l-pi/c,theta_l+pi/c), with periodic endpoints.
Its cyclic variation is the sum of adjacent sample differences and is at most V(varphi_j).
Direct integration on each cell gives, for every integer n,

    g_step_hat(n)=sinc(pi n/c)c^-1
                         sum_l varphi_j(exp(i theta_l))exp(-in theta_l),
    sinc(x)=sin(x)/x, sinc(0)=1.

For |n|<c define m_n=(1-|n|/c)/sinc(pi n/c), and put
T_c(t)=sum_(|n|<c)m_n exp(int).
The coefficient identity and the finite Fejer expansion give EXACTLY

    I_c varphi_j=g_step*T_c,                                 (BV25)

where I_c includes all c samples.
This identity is unaffected by the infinitely many other Fourier coefficients of the step function, because T_c has the stated finite support.

Here m_n=m(|n|/c), with m(x)=pi x(1-x)/sin(pi x), extended by m(0)=m(1)=1.
It is symmetric about1/2 and bounded by2: on0<=x<=1/2 use sin(pi x)>=2x and pi<4, then reflect.
For0<x<=1/2 its derivative is

    m'(x)=pi{[sin(pi x)-pi x cos(pi x)]
                     -2x sin(pi x)+pi x^2 cos(pi x)}/sin^2(pi x).

The first bracket has magnitude at most(pi x)^3/3, by integration of t sin t.
The other two terms together have magnitude at most3pi x^2.
Thus

    abs(m'(x))<=pi^4 x/12+3pi^2/4
               <=pi^4/24+3pi^2/4<24.

Symmetry gives this bound on the entire interval.
It follows that sum_(n=0)^(c-2)|m_n-m_(n+1)|<=24 and |m_(c-1)|<=2.
The elementary Dirichlet estimate

    ||D_n||_1<=1+log(2n+1)

holds also at n=0; for n>=1 integrate
|D_n(t)|<=min(2n+1,pi/|t|), splitting at pi/(2n+1).
Finite Abel summation gives

    T_c=m_(c-1)D_(c-1)+sum_(n=0)^(c-2)(m_n-m_(n+1))D_n,
    ||T_c||_1<=26[1+log(2c)].                               (BV26)

The endpoint coefficient m_(c-1)D_(c-1) pays the full cutoff jump to zero at abs(n)=c.
The continuous extension m(1)=1 does not remove that finite endpoint term.

For completeness this controls variation without a distributional-theorem input.
Integration by parts over the c step cells in(BV25) expresses its derivative as
(2pi)^-1 times the finite sum of each jump multiplied by the corresponding translate of T_c.
Integrating its absolute value over a full angular circle gives
V(I_c varphi_j)<=||T_c||_1 V(g_step).
Thus

    V(I_c varphi_j)<=26[1+log(2c)]2pi(L-4).

The actual missing sample is varphi_j(1)=-1, so q=I_c varphi_j+Fej_c/c, with the PLUS sign.
Write S_c=sum_(r=0)^(c-1)exp(irt).
The finite square formula and Cauchy--Schwarz give

    ||Fej_c'||_1<=(2/c)||S_c'||_2||S_c||_2<=2c,
    V(Fej_c/c)<=4pi.

We have proved the fully actual interpolation bound

    V(q)<=52pi(L-4)[1+log(2c)]+4pi.                         (BV27)

Every grid cell, both signed frequencies and the omitted sample have been included.

### 5. Product variation, exact error and schedule constants

The genuine unweighted comparison, unchanged from C648, is ||q-varphi_j||_1<=E.
Differentiate the ACTUAL product

    K_q-K_phase=-Re[z^c(q-varphi_j)]/2

and integrate to obtain

    V(K_q-K_phase)<=pi c E+[V(q)+V(varphi_j)]/2.              (BV28)

Adding(BV24), (BV27), and V(varphi_j)=2pi(L-4) gives precisely V_bar in(BV4).
The absolute-value map does not increase variation, so V(e)<=V_bar.
The actual orthogonal projection R_orig is a positive contraction and ||v_(2d)||^2=2d, so0<=k<=1.
The unimodular phase gives0<=K_phase<=1; hence their difference has absolute value at most1.
Equation(BV23) and the unchanged E/2 scalar error then give the remaining(BV5).
Take h_o=1-k in the generic lemma(BV21).
Its B_e is bounded by B_bar, proving(BV6).
The difference from the torus convention at1 is a null set and changes none of these norms.

Here is the complete constant simplification, with no suppressed dependence on j or sigma.
Both actual schedules have L<c and d<2c.
Put t_c=1+log c>=1.
Then1+log(4d)<=4t_c and1+log(2c)<=2t_c.
Using L>=1 and5+2log c<=5t_c in(BV4) gives

    V_bar<=(376pi+5pi^2)L t_c<=(400pi+8pi^2)L t_c,
    epsilon<=(3+3pi)(L/c)t_c,
    B_bar<=[4+403pi+8pi^2](L/c)t_c.

The first displayed coefficient comes from320pi for(BV24), pi+5pi^2 for pi c E,52pi for the main term in(BV27)/2,2pi for its sample term and pi for V(varphi_j)/2.
Thus(BV11)'s first inequality has exactly the declared C_B.

The ACTUAL integer-prime bounds retained in C644/C648 give

    L/c^square<=M^-2, L/c^balanced<=M^(-28/11),
    c^square<2^21 M^4, c^balanced<2^33 M^(50/11).

They also give(BV15) for the actual minimal degrees.
For M>=2 the two upper bounds imply1+log c<=64(1+log M).
Substituting proves all of(BV11).
In particular the original cap cost is bounded by
C_o M^(-3alpha_sigma/4)T_M^(3/4)tau^(-3/8), with C_o=(32*64*C_B)^(3/4) as stated.

### 6. All five terms, finite kernels and exact closed-box return

We apply only the established C641v2 joint-shell interface, already rebuilt for BOTH original laws in C644/C648.
On the original circle and separately on the torus, its regularization cost is

    ||F_tau-F_(tau,rho)||_(4/3)
                      <=2048^(3/4)sqrt(rho)tau^(-1/8).       (BV29)

On the circle this notation means composition with the actual iota.
The positive-kernel smoothing costs, on these same two spaces, are each

    N_mu(F_(tau,rho)-Q_(tau,rho))<=C_s M^-1 tau^(-1/8).       (BV30)

The original-circle proofs of(BV29)--(BV30) use the certified translated-law estimates; they do not equate nonlinear original means with product-Haar means.
Our choice0<rho<=1 and M sqrt(rho)=C_w meets their full resolution hypotheses, for every permitted tau even if rho/tau>1.
Holder's inequality gives N_mu(v)<=||v||_(4/3).
The event norm satisfies the triangle inequality directly from its definition.
The sum of(BV6), TWO copies of(BV29) and TWO copies of(BV30) is exactly(BV7).
This replaces only the first of the five costs.

For clarity the actual no-alias inequalities for BOTH schedules are

    a>2M, b>2M(1+a), c>2M(1+a+b).                           (BV31)

Any integer relation in the CLOSED[-2M,2M]^4 is trivial by considering its last nonzero coordinate.
Since Q has CLOSED support[-M,M]^4, finite orthogonality gives
Qhat_(pullback)(H_j^sigma(gamma))=Qhat(gamma) for every gamma in that box.
All H_j^sigma(gamma) in a supplied finite Gamma are distinct.
Apply the proved finite weak-Fourier inequality from C641v2 to the two differences in(BV7):
on either probability space the sum over N distinct characters is at most8N^(3/4)N_mu(v).
The two contributions add to the right side(BV8).
The empty family contributes zero; the same proof covers signed, zero and boundary indices.
There is no infinite-series return or coordinate truncation beyond this exact finite box.

### 7. Complete centered support, floors and every critical-strip cost

The exact C638 band theorem applies to the SAME U, centers, positive k and m, and radius definitions in the statement.
For0<tau<=1/64, L_tau>=2 and L_tau sqrt(tau) lies between1/8 and1/4.
It gives the full torus coefficient mass at least3log(J+1)/(32768pi).
The rectangles at each(k,m) contain exactly(2R_z+1)(2R_u+1) integer points.
Their full cardinality is N_sel, including every one of the L_tau J pairs.
Under(BV9) they fit in the closed box; (BV31) makes all their original images distinct.
Moreover gamma_3=k>=1 and the other coordinates have magnitude at most M, so H_j^sigma(gamma)>=c-M(1+a+b)>0.
The original Wiener sum therefore dominates their entire selected mass.
Applying(BV8) proves(BV10).

The ceiling bounds give the stated N_sel estimate, and L_tau<=1/(4sqrt(tau)) implies

    8N_sel^(3/4)<=C_sup J^(13/8)tau^(-9/16).                 (BV32)

Combine this with(BV6), (BV11), and the remaining C_2 cost.
The two resulting tau exponents are-3/8-9/16=-15/16 and-1/8-9/16=-11/16.
This proves(BV12), with no omitted support or rank/interpolation term.

Now take ANY H,tau in(BV13), and set J=floor(H^(1/4))>=2.
Uniformly over this strip,

    L_tau<=M^(8/11)H^-1/2/4, J<=M^(4/11),
    R_z<=(C_loc+1)M^(4/33),
    R_u<=(C_loc+1)M^(4/11)H^(-1/24)/2.                      (BV33)

The ceiling inequalities use ceil(Cx)<=(C+1)x for x>=1.
Since H>=16,

    14(L_tau+J)+R_u
       <=(7/2)M^(8/11)+(C_loc+29)M^(4/11)/2<=M.

The two summands are at most M/2 by respectively
M>=7^(11/3) and M>=(C_loc+29)^(11/7).
Also M>=(C_loc+1)^(33/29) ensures R_z<=M, while L_tau,J<=M are immediate.
Thus every part of(BV9), including centers plus radii, is paid by M_BV for BOTH schedules.

Substitute J^(13/8)<=H^(13/32) and tau>=M^(-16/11)H into the COMPLETE(BV12).
The original term has H exponent13/32-15/16=-17/32 and M exponent

    -3alpha_square/4+15/11=-3/22,
    -3alpha_balanced/4+15/11=-6/11.

The combined regularization/smoothing term has M exponent-1+11/11=0 and H exponent13/32-11/16=-9/32.
Finally J+1>H^(1/4), so the main term exceeds3log H/(131072pi).
This proves exactly(BV14).

For a sequence in(BV16) or(BV17), the actual two-sided degree comparisons(BV15) make the condition equivalent to H_j^enl=M_j^(16/11)tau_j tending to infinity.
Eventually tau_j<=1/64, M_j>=M_BV and H_j^enl>=16, with H_j^enl<=M_j^(16/11)/64.
Apply(BV14) with H=H_j^enl.
Its main term diverges, its second error tends to zero, and its first error tends to zero since delta_sigma>0 and M^(-delta_sigma)(1+log M)^(3/4)->0.
This proves both actual-degree conclusions without a uniform assertion about when an arbitrary sequence enters the strip.
The fixed-input Wiener finiteness and original contact margin are unchanged actual C648 properties.
Neither establishes a bounded-enlargement endpoint or changes(BV1).

## Source and reuse boundary

The focused reuse inputs are the actual C653 monotone phase and exact variation, C648's complete two-family original comparison, C641v2's paid joint-shell finite return as already transferred to both laws, and C638's entire centered band theorem.
The finite rank norm, missing sample and old logarithmic E remain exactly those adopted inputs.
The new contact occupation, dyadic cap calculation, Dirichlet derivative bound, finite interpolation-multiplier variation and their full combination are proved here.

The Dirichlet and Fejer finite expansions are the elementary kernels already used in C172/C648.
Their needed L1 bounds and every new constant are derived above.
This is not an invocation of a general L1 Bernstein theorem, an independently averaged contact law, or a new classical priority claim.
No uninspected general interpolation or distributional derivative theorem is needed.
The original MS05 arbitrary-prime construction, integer-Bertrand bounds and C172/L264/GMR18 phase-source scopes stay exactly at their existing accepted depth through C644/C648/C653.
This work does not upgrade inspection of any original source proof.

No original unweighted logarithm is removed, and the new square-family degree improvement relies on genuine same-circle contact occupation and the entire variation cost.

## Assessment history

### Decision original-contact-bv-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T23:42 |
| status | open |
| reason | Register the complete same-original-circle weighted contact/BV theorem, all actual rank and c-grid interpolation variation, finite five-cost return, entire centered support and uniform critical strip. The square family improves to actual degree4/11; balanced keeps8/25 with a smaller paid error. This is an author-checked argument awaiting fresh independent whole review. Neither original-circle independence, unweighted log removal, bounded enlargement, near-one inputs nor unrestricted completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | BV1--BV17 with both actual source-certified families, original2d matrices, probability conventions, same-circle weighted occupation, exact finite budgets, every finite Gamma and full centered support, uniform H/tau strips and separate actual degrees. |
| argument | [Complete argument](#complete-argument) | BV18--BV33 and all monotone-variable, dyadic shell, finite Dirichlet, exact grid multiplier, missing-sample, variation, five-cost, closed-box and full strip calculations. |
| dependency | [Adopted complete phase structure](Yin_C_G0653_v1.md#decision-whole-reviewed-2026-10-23) | Actual smooth phase with positive inverted angular derivative and exact variation2pi(L-4), retaining all actual signs and original source boundaries; pole derivatives are checked explicitly here. |
| dependency | [Adopted two-family original comparison](Yin_C_G0648_v1.md#decision-whole-reviewed-2026-10-23) | Both exact polynomial families, full original2d cyclic/rank errors, real E with missing sample, actual inverse phase and common zeros, all translated-law and alias premises, original contact margin and finite fixed-input Wiener norm. |
| dependency | [Actual schedules and degrees](Yin_C_G0644_v1.md#decision-whole-reviewed-2026-10-23) | Original and25/11 schedules, genuine minimal polynomials, integer prime bounds, actual degrees and reconstruction of all original probability interfaces; no new schedule or source-depth upgrade. |
| dependency | [Complete joint-shell return](Yin_C_G0641_v2.md#combined-argument) | Finite weak-Fourier theorem, two event-norm smoothings and original weak interfaces, as rebuilt for both laws in C644/C648. |
| dependency | [Joint-shell regularizations](Yin_C_G0641_v2.md#complete-additional-joint-shell-argument) | Both2048^(3/4)sqrt(rho)tau^(-1/8) regularizations with all-rho/tau scope and the complete original translated-law resolution hypotheses. |
| dependency | [Entire actual phase bands](Yin_C_G0638_v1.md#complete-local-modulation-calculation) | Same centers, all k,m rectangles, local squared-Fejer witness and total mass; complete support and every closed-box coordinate paid here. |
| support | [Bounded source and reuse account](#source-and-reuse-boundary) | Existing finite-kernel and arbitrary-prime/source depth only; all new variation/contact inequalities are explicitly proved and no uninspected named theorem is substituted. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T23:50 |
| status | proved |
| reason | Adopt the entire BV1--BV33 theorem after main reading of complete C656 and isolated whole R870. Same-original-circle monotone occupation and complete dyadic cap shells combine with paid original rank, finite interpolation, cutoff endpoint, missing sample and product variation. The full five-cost return and entire centered support give the uniform H/tau strip with actual square degree4/11 and balanced8/25 criteria for every shrinking sequence with diverging enlargement. All original laws, source-certified minimal polynomials, finite closed-box indices and logarithmic costs remain. No independent-circle averaging, bounded-H endpoint, width optimality, near-one family, new native work or unrestricted completion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | BV1--BV17 with both actual source-certified families, original2d matrices, probability conventions, same-circle weighted occupation, exact finite budgets, every finite Gamma and full centered support, uniform H/tau strips and separate actual degrees. |
| argument | [Complete argument](#complete-argument) | BV18--BV33 and all monotone-variable, dyadic shell, finite Dirichlet, exact grid multiplier, missing-sample, variation, five-cost, closed-box and full strip calculations. |
| dependency | [Adopted complete phase structure](Yin_C_G0653_v1.md#decision-whole-reviewed-2026-10-23) | Actual smooth phase with positive inverted angular derivative and exact variation2pi(L-4), retaining all actual signs and original source boundaries; pole derivatives are checked explicitly here. |
| dependency | [Adopted two-family original comparison](Yin_C_G0648_v1.md#decision-whole-reviewed-2026-10-23) | Both exact polynomial families, full original2d cyclic/rank errors, real E with missing sample, actual inverse phase and common zeros, all translated-law and alias premises, original contact margin and finite fixed-input Wiener norm. |
| dependency | [Actual schedules and degrees](Yin_C_G0644_v1.md#decision-whole-reviewed-2026-10-23) | Original and25/11 schedules, genuine minimal polynomials, integer prime bounds, actual degrees and reconstruction of all original probability interfaces; no new schedule or source-depth upgrade. |
| dependency | [Complete joint-shell return](Yin_C_G0641_v2.md#combined-argument) | Finite weak-Fourier theorem, two event-norm smoothings and original weak interfaces, as rebuilt for both laws in C644/C648. |
| dependency | [Joint-shell regularizations](Yin_C_G0641_v2.md#complete-additional-joint-shell-argument) | Both2048^(3/4)sqrt(rho)tau^(-1/8) regularizations with all-rho/tau scope and the complete original translated-law resolution hypotheses. |
| dependency | [Entire actual phase bands](Yin_C_G0638_v1.md#complete-local-modulation-calculation) | Same centers, all k,m rectangles, local squared-Fejer witness and total mass; complete support and every closed-box coordinate paid here. |
| support | [Bounded source and reuse account](#source-and-reuse-boundary) | Existing finite-kernel and arbitrary-prime/source depth only; all new variation/contact inequalities are explicitly proved and no uninspected named theorem is substituted. |
| review | [Independent entire finding](../audits/reviews/Yin_R_G0870_v1.md#original-contact-bv-whole-independent-finding) | Entire BV1--BV33 and Sections1--7, both actual families and original2d laws, every same-circle weight and cap shell, finite rank/interpolation/variation/constants, all five costs, full support/closed-box return and arbitrary-sequence actual-degree consequences. |


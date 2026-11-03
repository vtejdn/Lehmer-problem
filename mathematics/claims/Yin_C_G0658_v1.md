---
author: Yin
---

# A logarithmically balanced actual prime family and its degree-normalized contact layers

Human author Yin.
Root supplied the21/11 prime threshold with its logarithmic integer multiplier, the candidate balance and explicit degree comparisons.
Phase_bands independently checked these calculations as a contributor, reconstructed every new original-law input and completed the finite return and sequence theorem.
Both are contributors, not independent reviewers.
The adopted C656 same-circle mechanism is reused only after verifying its actual proof hypotheses at the NEW family below.
No native computation, prime enumeration, source acquisition or new original-source proof audit is performed.

## Statement

Fix

    K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))),
    a_j=min{p prime:p>(j+1)K},
    b_j=min{p prime:p>(K+a_j+3)^2},
    L_j=K+a_j+b_j+2, M_j=floor(a_j/4), j>=1.

Define the NEW exact integer thresholds and last prime by

    n_j=min{n positive integer:n^11>=(L_j+1)^21},
    ell_j=min{ell positive integer:2^ell>=L_j+1},
    c_j=min{p prime:p>n_j ell_j}, d_j=c_j+L_j-3.             (LB1)

Thus n_j=ceil((L_j+1)^(21/11)) and ell_j=ceil(log_2(L_j+1)).
The product n_j ell_j is an integer BEFORE applying Bertrand.
This differs from both the square and25/11 schedules.

For e=(K,a_j,b_j,c_j) define the COMPLETE numerator

    Qraw_j(x)=(x^2-1)product_(i=0)^3(x^e_i-1)
       -(x/2)sum_(q=0)^3(x^e_q+1)product_(i!=q)(x^e_i-1),
    P_j(x)=Qraw_j(x)/(x-1)^3.                               (LB2)

At the exact accepted MS05 arbitrary-distinct-prime construction depth, P_j is monic integral irreducible and is the ACTUAL Salem minimal polynomial, of even degree d_j and trace-1, with no additional cyclotomic factor.
Its exterior root beta_j satisfies

    2<beta_j<4, log2<m(P_j)=log beta_j<log4.                 (LB3)

In the ORIGINAL2d_j coordinates, let A_rel,j have ALL d_j columns P_j,xP_j,...,x^(d_j-1)P_j and set

    R_j=I-A_rel,j(A_rel,j^T A_rel,j)^-1 A_rel,j^T,
    v_(2d_j)(z)=(1,z,...,z^(2d_j-1))^T,
    k_j(z)=(2d_j)^-1 v_(2d_j)(z)^* R_j v_(2d_j)(z),
    psi_tau(s)=(1-(1-s)/tau)_+, f_(j,tau)=psi_tau(k_j).

All Haar measures are probability measures, angular variation V is UNNORMALIZED, and Fourier coefficients use the negative exponential convention.
Write W_*(f)=sum_(h in Z,h!=0)abs(fhat(h)).
For each fixed j and0<tau<=1 this sum is finite.
At every unit-circle root of P_j, f_(j,tau)=1, and its contact value minus Haar mean is at least1/2.

The fixed-K torus functions are

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
For EVERY t in T^4 let mu_(j,t) be the pushforward of nu_1 through z to t*iota_j(z).
These are the NEW original and translated laws.

### Exact finite original comparison and five-cost return

Suppress j and put L=L_j,c=c_j,d=d_j,M=M_j.
Let A(z)=Acal(z,z^a,z^b), B(z)=Bcal(z,z^a,z^b), and let U_j=A/B extend smoothly after cancellation of their exact common factor(z-1)^2.
Put varphi_j(z)=U_j(z^-1), with varphi_j(1)=-1.
Then

    h_phase=(1+Re(z^c varphi_j(z)))/2, K_phase=1-h_phase,
    Fej_c(t)=c^-1 abs(sum_(r=0)^(c-1)exp(irt))^2,
    theta_l=2pi l/c,
    q(exp(it))=c^-1 sum_(l=1)^(c-1)
                         varphi_j(exp(i theta_l))Fej_c(t-theta_l),
    K_q=(1-Re(z^c q))/2,
    E=[1+pi L(5+2log c)]/c,
    epsilon=(4L-5)/(2d)+E/2,
    V_bar=80pi L[1+log(4d)]+pi c E
              +26pi(L-4)[1+log(2c)]+2pi+pi(L-4),
    B_bar=epsilon+[V_bar+L-4]/c,
    C_B=4+403pi+8pi^2.

The actual q includes ALL nontrivial c-grid samples; its sample at1 is zero.
On the SAME new original circle, for every0<tau<=1/64,

    ||k_j-K_phase||_1<=epsilon,
    V(abs(k_j-K_phase))<=V_bar,
    ||f_(j,tau)-F_tau composed with iota_j||_(4/3)
                           <=(32 B_bar)^(3/4)tau^(-3/8).     (LB4)

For every actual M>=2, the complete finite budget obeys

    B_bar<=C_B(L/c)(1+log c)<=5C_B M^(-20/11).               (LB5)

The actual logarithmic interpolation cost E has not been deleted: the factor ell_j in the actual prime threshold pays it.

Define fixed constants using only the SAME K-torus phase:

    D_l=||partial_l Acal||_infinity+||partial_l Bcal||_infinity, l=1,2,3,
    G_K=sqrt(||g||_infinity),
    C_w=6pi[1+10sum_l D_l+2(G_K+1)],
    C_s=3pi[24*64^(3/4)sum_l D_l+4^(3/4)],
    C_2=2*2048^(3/4)C_w+2C_s, C_o=(160C_B)^(3/4).

Let N_mu(v)=sup_(E measurable,mu(E)>0)mu(E)^(-1/4)integral_E abs(v)dmu.
For M>=max{2,C_w}, set rho=(C_w/M)^2 and

    V_rho=Ncal(z^-1,u^-1,v^-1)/(g+rho),
    h_rho=(1+Re(wV_rho))/2, F_(tau,rho)=(1-h_rho/tau)_+,
    P_M=J_(floor(M/2)+1), J_N=Fej_N^2/[(2N^2+1)/(3N)],
    Q_(tau,rho)=F_(tau,rho)*(four-coordinate product of P_M),
    B_log(j,tau)=(32 B_bar)^(3/4)tau^(-3/8)
                                       +C_2 M^-1 tau^(-1/8).

The probability kernel P_M has CLOSED Fourier support[-M,M] and first angular moment at most3pi/M.
For every0<tau<=1/64,

    N_nu1(f_(j,tau)-Q_(tau,rho) composed with iota_j)
          +N_nu4(F_tau-Q_(tau,rho))<=B_log(j,tau).            (LB6)

For EVERY finite Gamma in the CLOSED integer box[-M,M]^4,

    sum_(gamma in Gamma)
       abs(fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma))
       <=8 card(Gamma)^(3/4) B_log(j,tau).                   (LB7)

All characters in the supplied set have distinct original images.
Empty sets, zero and negative harmonics, and box endpoints are included.
The original comparison, two regularizations and two smoothings are all paid, on the new actual laws.

### Complete support and every critical enlargement

Define the unchanged actual torus centers explicitly by

    D_0(z)=-2(z-z^-1)+(z^K+1)/(z^K-1), b_0(z)=Im D_0(z),
    z_0=exp(i pi/K),
    -cot(t_(k,m)/2)=16sqrt(km)-b_0(z_0), t_(k,m) in(-pi,0),
    phi_z(t)=arctan(2/[b_0(z)-cot(t/2)]),
    n_(k,m)=floor((k+m)phi_(z0)'(t_(k,m))+1/2),
    C_loc=ceil(32000pi+1024pi(K+4)).

The center evaluation uses the actual regular local neighborhoods, and abs(n_(k,m))<=14(k+m).
For L_tau=floor(1/(4sqrt(tau))) and integer J>=2 set

    R_z=ceil(C_loc J^(1/3)), R_u=ceil(C_loc sqrt(L_tau)J^(5/6)),
    G_(L_tau,J)={(-p,-q,m,k):1<=k<=L_tau,1<=m<=J,
                               abs(p)<=R_z,abs(q-n_(k,m))<=R_u},
    N_sel=L_tau J(2R_z+1)(2R_u+1)
          <=9(C_loc+1)^2 L_tau^(3/2)J^(13/6),
    C_sup=8[9(C_loc+1)^2]^(3/4)4^(-9/8).

Whenever the full conditions

    R_z,J,L_tau<=M, 14(L_tau+J)+R_u<=M                       (LB8)

hold, all selected original frequencies are distinct and strictly positive and

    W_*(f_(j,tau))>=3log(J+1)/(32768pi)
                               -8N_sel^(3/4)B_log(j,tau).   (LB9)

The ENTIRE error in(LB9) is at most

    C_sup J^(13/8)[C_o M^(-15/11)tau^(-15/16)
                                  +C_2 M^-1 tau^(-11/16)].  (LB10)

Put

    M_log=ceil(max{2,C_w,(C_loc+1)^(33/29),
                             7^(11/3),(C_loc+29)^(11/7)}),
    C_crit=C_sup(C_o+C_2).

For EVERY actual j with M=M_j>=M_log and EVERY pair of real parameters H,tau satisfying

    16<=H<=M^(16/11)/64, M^(-16/11)H<=tau<=1/64,             (LB11)

J=floor(H^(1/4)) satisfies the whole(LB8), and

    W_*(f_(j,tau))>=3log H/(131072pi)
                           -C_crit[H^(-17/32)+H^(-9/32)].   (LB12)

This is uniform over the ENTIRE H,tau strip.
Both critical powers of M cancel exactly, with no omitted logarithmic cost.

### Actual degree, logarithm and precise sequence condition

For EVERY actual j with M=M_j>=2, put T_M=1+log M.
The genuine minimal-polynomial degree satisfies

    M^(42/11)T_M<d_j<2^27 M^(42/11)T_M,
    M^(42/11)/32<d_j/(1+log d_j)<2^27 M^(42/11).             (LB13)

Consequently, for EVERY positive shrinking sequence tau_j->0 such that

    (d_j/(1+log d_j))^(8/21)tau_j->infinity,                 (LB14)

one has W_*(f_(j,tau_j))->infinity.
The condition is equivalent to M_j^(16/11)tau_j->infinity, with no monotonicity and no prescribed speed of divergence.
The entry index into(LB11) may depend on the sequence.
This is a NEW actual family; its degree and logarithmic scale are not those of the square or25/11 families.
No pure d^(8/21)tau criterion without the stated logarithmic factor, bounded-H endpoint, every-large-degree theorem, optimality over all methods, near-one family or unrestricted G0001 conclusion is asserted.
The positive total-measure interval(LB3) and full original2d normalization are retained.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Complete argument

### 1. Integer thresholds, eligibility and the full new alias box

The fixed K is even and at least16, and a>2K implies K+a+3<=2a.
Apply the accepted integer Bertrand statement to(K+a+3)^2.
It yields

    a^2<b<2(K+a+3)^2<=8a^2,
    L+1=b+K+a+3<=b+2a<=2b.

For M>=2,4M<=a<4M+4<=6M.
Thus

    16M^2<L<L+1<2^10 M^2.                                 (LB15)

Set X=L+1, x=X^(21/11), n=ceil x and ell=ceil(log_2 X).
All are the actual definitions in(LB1), with n and ell integral.
Since x>1, x<=n<=2x.
Bertrand at the INTEGER n ell>=2 gives a prime between n ell and2n ell.
The least prime above that threshold therefore satisfies

    x ell<c<4x ell, c>L, d=c+L-3, c<d<2c.                  (LB16)

The prime c is larger than b,a,K.
Hence a,b,c are distinct odd primes, all coprime to K.
No r>2 hypothesis is used.

The unchanged lower bounds imply a>2M and b>2M(1+a).
For the new c, since L>16M^2,

    L^(10/11)>2M,
    c>L^(21/11)>2ML>2M(1+a+b).                             (LB17)

For example the first inequality follows directly from
(16M^2)^(10/11)/(2M)=16^(10/11)M^(9/11)/2>1.
In any nonzero integer vector in[-2M,2M]^4, its highest nonzero weighted coordinate therefore strictly dominates the sum of all earlier coordinates.
This proves H_j(delta)!=0 on the entire punctured closed2M box.

Every difference between a closed-M coefficient index and a closed-M finite-polynomial support index lies in that closed2M box.
Thus selected finite coefficients return exactly.
On EVERY translated new circle, a nonconstant finite character with support in the closed-M box has mean zero; translation contributes only a unit-modulus scalar.
These facts establish the new finite coefficient and mean interfaces before any nonlinear smoothing argument.

### 2. Source applicability, exact factor removal and actual measure

Use MS05-U001's accepted arbitrary-distinct-prime construction with q=4, k_1=K and the three eligible primes from Section1.
The source unit explicitly establishes that the smallest-prime restriction in its original Lemma12 is used only for its separate degree upper bound.
Its torsion, integrality and interlacing interface holds for EVERY distinct eligible choice.
No source conclusion here requires c>(L+1)^2.

The precise factor check is retained.
A root of unity in the full source hypersurface either makes two powered coordinates1, forcing x=1 by pairwise coprimality, or lies on a constant-x maximal torsion coset whose constant is killed by K.
The latter makes the K-coordinate1, while exactly one powered coordinate1 cannot satisfy the source hypersurface equation.
Thus1 is the only root of unity in Qraw.
In2Qraw, the second part has at1 exact order3 and coefficient
-2 sum_q product_(i!=q)e_i, which is nonzero; its first part has order5.
Consequently the exact cyclotomic divisor is(x-1)^3.

The four summands have the same reduction modulo2 before division by2, so Qraw is integral.
Division by the monic(x-1)^3 leaves integral P.
For the reduced positive rational sum, the denominator product_i(x^e_i-1)/(x-1)^3 is monic with simple circle zeros and vanishes at1.
Positive residues prevent cancellation in that reduced rational sum, and its numerator is integral by the same parity calculation.
The accepted circular-interlacing Proposition6 and Proposition5(a) therefore apply at their stated conditions.
Their output is a Salem factor with possible cyclotomic factors, or a reciprocal quadratic alternative.
The preceding root-of-unity exclusion removes all additional factors, and d>2 removes the quadratic alternative.
Thus P is the ACTUAL irreducible Salem minimal polynomial.

The leading terms of Qraw are x^(c+L)-2x^(c+L-1).
After division by(x-1)^3 the degree is d=c+L-3 and the next coefficient is1, so the trace is-1.
Since K is even and a,b,c are odd, d=K+a+b+c-1 is even.

At the exterior root beta>1, divide the actual raw identity to obtain

    beta-beta^-1=(1/2)sum_(e in {K,a,b,c})(beta^e+1)/(beta^e-1).
                                                                    (LB18)

Each fraction exceeds1 and is at most(beta+1)/(beta-1).
The lower bound implies beta>1+sqrt(2)>2.
The upper bound simplifies to beta+beta^-1<=4 and hence beta<4.
The Salem measure is log beta, proving(LB3).
This is precisely the accepted RY26 exterior-root algebra, not its every-large-degree theorem.
All MS05/RY26 original-proof inspection limits remain unchanged.

### 3. Every original cyclic and interpolation premise for this c

Write Qraw=(x-1)^3P=A+x^c B, where

    R_0=(x^K-1)(x^a-1)(x^b-1),
    S_0=sum_(e in {K,a,b})(x^e+1)
                         product_(v in {K,a,b},v!=e)(x^v-1),
    A=-(x^2-1)R_0-xR_0/2+xS_0/2,
    B= (x^2-1)R_0-xR_0/2-xS_0/2.

These are exactly the stated torus specializations.
They are integral of degree L; A has both constant and leading coefficient-1, while B has both constant and leading coefficient1.
In N=2d coordinates, the raw coefficient matrix T has r=N-deg Qraw=c+L-6=d-3 columns Qraw,xQraw,...,x^(r-1)Qraw.
These columns are independent by their distinct leading degrees.
Let Pi_Q project onto its range and Pi_P=I-R_j project onto the full original relation space.
The raw relation space lies in the full P relation space with codimension3, so Pi_P-Pi_Q is an orthogonal projection of rank3.

Let S_c e_i=e_(i+1 mod c) and form in the SAME2d coordinates

    V_c=[A(S_c);B(S_c);0_(2L-6)-by-c].

Let Pi_V be its range projection.

There are at least c raw columns because L>6.
Their first c-column block T_0 agrees with V_c in all columns0<=i<c-L.
Only L boundary columns can differ, so rank(T_0-V_c)<=L.
Each of the two ranges has codimension at most L over their intersection; their projection difference has rank at most2L.
The remaining L-6 raw columns extend im T_0 inside im T by exactly L-6.
Differences of orthogonal projections have operator norm at most1.
Thus

    ||Pi_Q-Pi_V||_trace<=3L-6,
    ||Pi_P-Pi_V||_trace<=3L-3.                              (LB19)

All quantities use the actual new c,d,L, not a raw-degree normalization.

On the torus the quotients Acal/(zR_tor)=-1/2+H and Bcal/(zR_tor)=-1/2-H have purely imaginary H.
It follows by continuity that |Acal|=|Bcal| everywhere and that their common zeros are exactly the points where at least two of z^K,u,v equal1.
The latter assertion also follows directly by substituting the three possible vanishing factors in S_tor.
For every nontrivial c-th root omega, none of omega^K,omega^a,omega^b equals1 by the new coprimality.
Only the trivial root produces a zero cyclic mode.
With the eigenvector entries omega^-i, the cyclic Fourier blocks are therefore

    rank V_c=c-1,
    Pi_V,11=Pi_V,22=(I_c-J_c/c)/2,
    Pi_V,12(i,l)=(1/(2c))sum_(omega^c=1)
                              U(omega,omega^a,omega^b)omega^(l-i),
    Pi_V,21=Pi_V,12^*.

Here J_c is the all-ones c-by-c matrix, and the final2L-6 rows and columns are zero.
The phase sample at omega=1 is0.

The identity A+B=-xR_0 and nonzero constants show that every common root of A,B is a root of unity.
At a root of exactly one powered factor, the corresponding nonzero S_0 term prevents a common zero.
Pairwise coprimality makes1 their only common root.
The exact values

    [A/(x-1)^2](1)=Ka+Kb+ab,
    [B/(x-1)^2](1)=-(Ka+Kb+ab)

give precisely the common factor(x-1)^2.
Equality of moduli then prevents any further circle zero.
The reciprocal identity B=-A^*, with reciprocal degree L, gives the smooth unimodular phase and U_j(1)=-1.
These A,B and this phase depend only on K,a,b, which have not changed.

Define I_c varphi(t)=c^-1 sum_(l=0)^(c-1)varphi(exp(i theta_l))Fej_c(t-theta_l).
Grid orthogonality gives c^-1 sum_l Fej_c(t-theta_l)=1.
The rational-factor variation bound V(varphi)<=2pi(L-2) and the finite arc-count/Fejer moment argument give ||I_c varphi-varphi||_1<=V(varphi)(5/4+(log c)/2)/c.
Its needed estimates hold for every integer c>=2:
an oriented grid arc covers any point at most c|t|/(2pi)+1 times, and
integral |t|Fej_c(t)dnu_1<=pi(1/2+log c)/c.
Changing the actual sample-1 at1 to0 adds Fej_c/c, of L1 norm1/c.
Consequently

    q=I_c varphi+Fej_c/c, |q|<=1,
    deg_Fourier(q)<=c-1, ||q-varphi||_1<=E.                  (LB20)

This is exactly the inverse sampling orientation in the statement.

For self-adjoint T, |v^*Tv|<=v^*|T|v and integral vv^*dnu_1=I.
Thus(LB19), divided by the ORIGINAL2d, yields ||k-k_V||_1<=(3L-3)/(2d), where k_V=1-v^*Pi_Vv/(2d).
Direct evaluation of the just-displayed Fourier blocks gives

    v^*Pi_Vv=c-Fej_c+c Re(z^c q),
    k_V-K_q=((d-c)/(2d))(1+Re(z^c q))+Fej_c/(2d)>=0.

The polynomial z^c q has no constant coefficient, so

    ||k_V-K_q||_1=(L-2)/(2d),
    ||k-K_q||_1<=(4L-5)/(2d).                              (LB21)

Adding E/2 proves the original L1 portion of(LB4).
The torus common-zero convention differs from the smooth phase only at1 on this original circle; that Haar-null point affects none of the comparisons.

### 4. All same-circle BV hypotheses and the new logarithmic balance

We now apply only the elementary proof mechanisms in C656 Sections1--5, with their premises explicitly established.
The SAME A,B phase obeys

    D_phase(t)=4sin t+cot(Kt/2)+cot(at/2)+cot(bt/2),
    U_j(exp(it))=(1+iD_phase)/(1-iD_phase),
    D_phase'<=4-(K+a+b)/2<0.

Its L-4 cotangent poles have positive residues, and the smooth inverse phase has a lift psi with psi'>0 and increment2pi(L-4).
At a pole with residue r>0, the U argument derivative tends to-2/r, so no endpoint sign is omitted.
For THIS c set Theta=ct+psi; then Theta'>=c and its total increment is2pi(c+L-4).
C656's change of variables over these integer turns applies to every nonnegative continuous BV weight w, giving

    integral w 1_(h_phase<=eta)dnu_1
       <=sqrt(eta)[integral w+((L-4)sup(w)+V(w))/c], eta>0.   (LB22)

It is the same-circle inequality, with all extra winding and variation paid.

The polynomial k-K_q has degree at most2d-1 and the exact L1 bound(LB21).
For D_N(t)=sum_(abs(n)<=N)exp(int), the finite Dirichlet derivative bound proved in C656 is valid for EVERY degree N>=1:
||D_N'||_1<=10N[1+log(2N)].
It therefore gives V(k-K_q)<=80pi L[1+log(4d)] at this new d.

The C656 step-function interpolation identity holds for EVERY c>=2:
on centered grid cells, use the actual samples of varphi, with
T_c=sum_(|n|<c)[(1-|n|/c)/sinc(pi n/c)]exp(int).
Here sinc(x)=sin(x)/x for x!=0 and sinc(0)=1.
Then I_c varphi=g_step*T_c, V(g_step)<=V(varphi), and ||T_c||_1<=26[1+log(2c)].
The finite Abel endpoint term pays the jump to zero at |n|=c.
The omitted sample adds variation at most4pi, and V(varphi)=2pi(L-4).
Thus

    V(q)<=52pi(L-4)[1+log(2c)]+4pi,
    V(K_q-K_phase)<=pi c E+[V(q)+V(varphi)]/2.

These estimates prove the exact V_bar for THIS k,q,varphi.
Both k and K_phase lie in[0,1]: R_j is an orthogonal projection and ||v_(2d)||^2=2d, while varphi is unimodular.
Hence e=abs(k-K_phase)<=1, with mean at most epsilon and variation at most V_bar.

For clarity the generic C656 cap step uses w_s=min(1,e/s),0<s<=1, in(LB22), giving
nu{e>=s,h_phase<=eta}<=sqrt(eta)B_bar/s.
The cap difference is at most min(1,e/tau), with active set h_phase<=tau+e.
Its low shells tau*2^(-n-1)<e<=tau*2^-n contribute at most15B_bar tau^-1/2 to the fourth-thirds integral.
The high shells tau*2^n<e<=2tau*2^n with tau*2^n<1 contribute at most7B_bar tau^-1/2.
The endpoints e=0,tau,1 are included as in that complete lemma.
Taking the3/4 power of the larger32B_bar tau^-1/2 bound proves(LB4).
No old schedule rate has been substituted in this proof.

The algebraic simplification of these SAME finite expressions requires only L<c and d<2c, already proved in(LB16).
Exactly as can be checked term by term,

    V_bar<=(400pi+8pi^2)L(1+log c),
    epsilon<=(3+3pi)(L/c)(1+log c),
    B_bar<=C_B(L/c)(1+log c).                               (LB23)

We now pay the logarithm using the ACTUAL new prime threshold.
For X=L+1>=4, ell>=log X/log2 and ell<=X.
Equation(LB16) gives

    log c<log4+(21/11)log X+log ell
          <=(43/11)log X<4log X,
    (1+log c)/ell<=5log2<5.

The inequality1<=log X justifies the second line.
Since c>X^(21/11)ell,

    (L/c)(1+log c)<5L/X^(21/11)
                   <=5L^(-10/11)<=5M^(-20/11).             (LB24)

This proves(LB5).
There is NO assertion that the unweighted error has lost its logarithm; the changed actual c has absorbed that cost.

### 5. Every translated-law regularization and smoothing premise

The torus functions g,V,Ncal and all D_l,G_K are unchanged.
The positive kernel P_M and its exact support/moment are the adopted C637 kernel.
However its original-law use must employ the NEW alias(LB17), which Section1 already proves.

For0<rho<=1,s>=rho and0<eta<=1 put

    r_s=s/(g+s), V_eta=eta/(eta+h_rho).

The pointwise C641 derivative calculations depend only on those fixed torus functions:
sum_l |partial_l r_s|/r_s<=sum D_l/sqrt(s), and the logarithmic derivative sum for V_eta or r_s V_eta is at most
[10sum D_l+2(G_K+1)]/sqrt(rho).
These hold smoothly at common zeros and for ALL s>=rho, including s>1.

For any of those positive weights W let
I_W^star=sup_t integral W dmu_(j,t).
Convolution with P_M has its exact torus mean on each new translated circle by the proved finite alias.
Coordinatewise smooth FTC and the first moment3pi/M give

    I_W^star<=integral W dnu_4
       +[3pi(10sum D_l+2(G_K+1))/(M sqrt(rho))]I_W^star.

Every intermediate coordinate shift lies in the same supremum.
If M sqrt(rho)>=C_w, the bracket is at most1/2.
For r_s alone the same argument applies under M sqrt(s)>=C_w.

The unchanged product-Haar amplitude input C633v2 gives integral r_s<=8s^(2/3) for s<=1; for s>1 use r_s<=1<=8s^(2/3).
Only on product Haar, the exact conditional w integral is

    integral_w eta/[eta+(1+a cos(theta))/2]
       =eta/sqrt((eta+1/2)^2-(a/2)^2)<=sqrt(eta),
                  0<=a<1.

Here a=g/(g+rho).
Multiplication by the w-independent r_s is legitimate on that product space.
Absorption therefore establishes on EVERY NEW translated circle

    integral r_s<=16s^(2/3) if s<=1 and M sqrt(s)>=C_w,
    integral V_eta<=2sqrt(eta),
    integral r_s V_eta<=16sqrt(eta)s^(2/3),
    mu{h_rho<=eta,g<=s}<=64sqrt(eta)s^(2/3), s>=rho.          (LB25)

The torus has the same or smaller bounds.
No original-coordinate independence or nonlinear exact mean equality is assigned to mu_(j,t).

All hypotheses of the C641v2 joint-shell and every-path probability arguments are now verified for THIS law.
For precision, the smoothing proof uses
w_tau=1_(h_rho<=tau)(g+rho)^(-1/2).
Equation(LB25) gives its tail<=64sqrt(tau)t^(-4/3), its event norm<=4*64^(3/4)tau^(3/8), and
N_mu(1_(h_rho<=tau))<=[4sqrt(tau)]^(3/4).
The every-coordinate-path FTC envelopes are
6D_l tau^-1/2 w_tau for l=1,2,3 and
tau^-1/2 1_(h_rho<=tau) for l=4.
Their event-first triangle bound, integrated against the product kernel, gives on the circle and torus separately

    N_mu(F_(tau,rho)-Q_(tau,rho))<=C_s M^-1 tau^-1/8.         (LB26)

Every intermediate shift is an already controlled translated circle, so this is not a restriction of an ambient a.e. derivative to a singular law.

The regularization proof uses h_rho=(g/(g+rho))h+rho/[2(g+rho)].
For tau<=1/64 the difference F_tau-F_(tau,rho) is nonnegative, supported on h<=tau, and at most min{1,rho/[2tau(g+rho)]}.
The low set g<rho costs at most32rho^(2/3) by the first line of(LB25).
For the disjoint shells s<=g<2s, s=2^k rho, the active set lies in
h_rho<=tau+rho/(2s)<1.
Equation(LB25) applies also when2s>1.
The complete C641 sums through s<=lambda and s>lambda, lambda=rho/tau, cost respectively at most
1600rho^(2/3)tau^-1/6 and240rho^(2/3)tau^-1/6.
Together with the low term, their total is below2048rho^(2/3)tau^-1/6.
This remains valid when lambda>1, since the shells have no artificial scale-one truncation.
Thus on both new probability spaces

    ||F_tau-F_(tau,rho)||_(4/3)
                      <=2048^(3/4)sqrt(rho)tau^-1/8.        (LB27)

Set rho=(C_w/M)^2, so all stated resolutions hold.
Holder gives N_mu(v)<=||v||_(4/3), and the event norm has its direct triangle inequality.
Add the original(LB4), TWO copies of(LB26) and TWO copies of(LB27).
The result is exactly(LB6), with all five costs and the stated C_2.

The finite C641 height-truncation/Bessel lemma is a probability-space result for finite orthonormal modulus-one characters, with no arithmetic schedule premise.
It gives sum of N coefficient magnitudes<=8N^(3/4)N_mu(v), including zero norm and empty families.
The new H_j images are distinct by(LB17), so the original circle characters form such a family.
Exact finite Q coefficient equality and the two error functions in(LB6) give(LB7), with all signed and boundary indices.

### 6. All selected bands, centered box and exact critical balance

C638's band theorem concerns only the fixed K-torus U.
Its actual centers, radii and torus mass3log(J+1)/(32768pi) are unchanged; no old original-circle return is imported.
For each(k,m), its integer rectangle contains exactly(2R_z+1)(2R_u+1) points, so the entire set has exactly N_sel points.
Under(LB8) all four coordinates lie in the closed-M box.
The new aliases make all their original images distinct; k>=1 and c>2M(1+a+b) make every image positive.
Using(LB7) on this whole set proves(LB9).

For tau<=1/64, L_tau>=2 and L_tau sqrt(tau)>=1/8.
The exact cardinality bound and L_tau<=1/(4sqrt(tau)) give
8N_sel^(3/4)<=C_sup J^(13/8)tau^-9/16.
By(LB5), the original cap norm is at most C_o M^-15/11 tau^-3/8.
Multiplying the ENTIRE budget by the full support factor proves(LB10):
the two resulting width powers are-15/16 and-11/16.

For every H,tau in(LB11), set J=floor(H^(1/4))>=2.
All floors and ceilings obey

    L_tau<=M^(8/11)H^-1/2/4, J<=M^(4/11),
    R_z<=(C_loc+1)M^(4/33),
    R_u<=(C_loc+1)M^(4/11)H^(-1/24)/2.

Indeed ceil(Cx)<=(C+1)x for x>=1.
The threshold M_log gives R_z<=M and

    14(L_tau+J)+R_u
       <=(7/2)M^(8/11)+(C_loc+29)M^(4/11)/2<=M,

because its two summands are individually at most M/2.
Also L_tau,J<=M.
Thus every center-plus-radius condition in(LB8) holds uniformly on the full strip.

Now J^(13/8)<=H^(13/32) and tau>=M^(-16/11)H.
The two complete terms in(LB10) become respectively

    C_sup C_o H^(-17/32), C_sup C_2 H^(-9/32),

since their M powers are-15/11+(16/11)(15/16)=0 and
-1+(16/11)(11/16)=0.
There is no remaining logarithm, because(LB24) already paid it with the actual prime threshold.
Finally J+1>H^(1/4) gives the main term in(LB12).

### 7. Actual degree constants and arbitrary sequence entry

From(LB15) and x=(L+1)^(21/11),

    M^(42/11)<x<2^20 M^(42/11).

The exact integer ell satisfies

    1+log M<ell<=11+(2/log2)log M<=11+3log M<=11T_M.

The lower bound follows from
ell>=log_2(L+1)>4+2log M/log2>1+log M.
The upper bound uses L+1<2^10 M^2, ceil y<=y+1, and2/log2<3.
Together with x ell<c<d<2c<8x ell this gives

    M^(42/11)T_M<d<88*2^20 M^(42/11)T_M
                               <2^27 M^(42/11)T_M.

These are bounds for the ACTUAL minimal-polynomial degree, not c or the raw degree.
Let T_d=1+log d.
The lower degree estimate gives T_d>=T_M.
The upper one and log(1+log M)<=log M for M>=1 give

    T_d<1+27log2+(53/11)log M<=32T_M.

Dividing the two degree estimates proves both sides of(LB13).
Raising that comparison to8/21 proves that (d/T_d)^(8/21) is bounded above and below by fixed positive multiples of M^(16/11).
Hence(LB14) is exactly equivalent to H_j^enl=M_j^(16/11)tau_j tending to infinity.

For any such shrinking sequence, eventually M_j>=M_log, tau_j<=1/64 and H_j^enl>=16.
Also H_j^enl<=M_j^(16/11)/64, so(LB12) applies with H=H_j^enl.
Its main term diverges and both errors tend to zero, however slowly H_j^enl increases.
No uniform index of entry for arbitrary sequences has been asserted.

The original relation projection has rank d, giving integral k_j=1/2 and0<=k_j<=1.
At every unit-circle root of the genuine P_j all relation columns annihilate the evaluation vector, so k_j=1.
For0<tau<=1, psi_tau(s)<=s on[0,1]; this proves the stated contact margin.
For fixed j,tau the cap of the finite trigonometric polynomial is continuous and piecewise smooth, with a bounded derivative on each piece.
If the level equation k_j=1-tau is identically true the cap is constant; otherwise it has only finitely many circle solutions, which give the stated pieces.
Integration by parts on those pieces has cancelling boundary terms and gives the usual n*fhat(n) derivative-coefficient identity.
Finite derivative Bessel and Cauchy--Schwarz with sum_(n!=0)n^-2<infinity give absolute Fourier summability.
No uniform fixed-j derivative estimate enters the moving-width result.

### 8. Scope of the balance and retained source depth

The following is only an algebraic explanation of the chosen schedule inside THIS complete cost/support mechanism.
If a hypothetical prime scale were c approximately L^r times a logarithmic multiplier, L approximately M^2 and d approximately M^(2r), the two proved budget powers suggest

    theta_M<=min{8(r-1)/5,16/11},
    theta_degree<=min{4(r-1)/(5r),8/(11r)}.

The first degree expression increases in r>1 and the second decreases.
They agree when44(r-1)=40, namely r=21/11, at value8/21.
This formal comparison is not an all-r family theorem or a global optimum.
The exact schedule(LB1), all its prerequisites and its surviving degree logarithm have been proved separately above.
In particular it does not justify dropping1+log d in(LB14).

The inspected MS05-U001 source unit accepts its exact retained2004 manuscript statements and selected torsion/construction application checks.
Its general interlacing and torsion-exponent source propositions retain their stated external-statement depth; no original Mann/Schmidt or whole-source proof audit is added.
The accepted integer Bertrand statement, for every integer n>=2 there exists n<p<2n, is the same bounded source input retained in C356/C217 and Mig78-U001.
All present thresholds are integers, and its classical original proof is not newly inspected or attributed to Mignotte.
The RY26 input is solely the exterior-root formula and bound at the inspected unit's scope.
The exact C171/C172 finite comparison mechanisms have been rebuilt with all new dimensions and cyclic hypotheses in Section3.
C656 supplies its proved occupation, variation and cap lemmas only after Section4 verifies every relevant new-family hypothesis.
C641 supplies torus identities and general probability arguments only after Section5 reconstructs all translated-law premises.
C638 supplies only the unchanged TORUS mass and centers before the new alias, positivity and return are applied.
No old r>2 schedule theorem is imported by changing its symbols.

## Assessment history

### Decision log-balanced-family-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T23:59 |
| status | open |
| reason | Register the complete NEW21/11 logarithmically balanced prime family, actual source-certified Salem polynomial and exact factor removal, rebuilt original2d cyclic/rank/interpolation/BV and every translated-law interface. All five costs and entire support give the uniform critical strip and the actual degree criterion(d/(1+log d))^(8/21)tau diverging. This author-checked argument awaits fresh independent whole review. Source depths and log2<m(P)<log4 remain; no old schedule substitution, original logarithm deletion, bounded enlargement, near-one family, global optimum or unrestricted completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire new-family statement](#statement) | LB1--LB14: exact integer thresholds, actual minimal polynomial/full2d objects and measures, complete finite budgets and all signed closed-box indices, entire centered support, uniform strips, actual degrees/logarithms and arbitrary shrinking sequences. |
| argument | [Complete new-family reconstruction](#complete-argument) | Sections1--8/LB15--LB27: all integer/alias/source/factor/cyclic/variation/logarithm and translated-law prerequisites, five costs, exact support and degree/sequence computations, with restricted balance and no broad optimum. |
| dependency | [Accepted arbitrary-prime source interface](../audits/literature/MS05/Yin_U001.md#ms05-u001) | Exact arbitrary-distinct-prime-construction and four-exponent-specialization sections, complete factor removal and interlacing applicability at the retained statement/selected-proof depth; new eligibility checked here. |
| dependency | [Exterior-root identity](../audits/literature/RY26/Yin_U001.md#ry26-u001) | Exact exterior-root-measure-expense section and positive-root formula applied to the current four exponents; independent actual irreducibility is supplied before identifying total measure. |
| dependency | [Accepted integer Bertrand input](Yin_C_G0356_v1.md#argument) | Integer threshold n>=2 implies a prime n<p<2n, at the retained classical statement depth; no new source-proof audit or numerical prime search. |
| support | [Bertrand attribution boundary](../audits/literature/Mig78/Yin_U001.md#mig78-u001) | Existing Proposition5-length account of the accepted classical interval input, not attribution of its original proof to Mignotte. |
| dependency | [Finite cyclic-rank mechanism](Yin_C_G0171_v1.md#two-block-circulant-rank-transfer) | The finite mechanism, with all new dimensions, boundary-column ranks and actual c eligibility reconstructed in Section3. |
| dependency | [Actual cyclic phase blocks](Yin_C_G0171_v1.md#two-block-torus-phase) | Same fixed-K torus equal modulus/common zeros, new c-grid rank and missing mode with correct inverse orientation. |
| dependency | [Finite interpolation mechanism](Yin_C_G0172_v1.md#moving-cubic-discrete-fejer) | Any-c finite grid and original phase mechanism, with every new original-law and sample condition re-established before use. |
| support | [Earlier family reconstruction](Yin_C_G0644_v1.md#complete-argument) | Actual finite proof interfaces and source scopes only; its25/11 numerical bounds and old r>2 comparisons are not new-family conclusions. |
| dependency | [Adopted same-circle BV lemmas](Yin_C_G0656_v1.md#complete-argument) | Sections1--5 generic monotone occupation, finite Dirichlet/interpolation variation and cap-shell mechanisms, applied only after all new c,d and phase hypotheses are checked. |
| dependency | [Torus/probability return mechanisms](Yin_C_G0641_v2.md#combined-argument) | Exact relative derivatives, conditional product integral, every-path event-norm smoothing and finite weak Fourier lemma; all new translated-law prerequisites rebuilt here. |
| dependency | [All-scale joint-shell regularization](Yin_C_G0641_v2.md#complete-additional-joint-shell-argument) | Exact low/middle/high shell constants and all-rho/tau scope, after current laws satisfy every required amplitude/contact bound. |
| dependency | [Actual torus amplitude input](Yin_C_G0633_v2.md#additional-complete-logarithm-free-and-two-sided-argument) | Same fixed-K g and product-Haar integral r_s<=8s^(2/3); original circle bounds follow from newly proved finite-mean absorption. |
| dependency | [Positive finite kernel](Yin_C_G0637_v1.md#complete-argument) | Probability normalization, closed support and3pi/M first moment; current original mean and coefficient identities are separately proved. |
| dependency | [Entire torus phase bands](Yin_C_G0638_v1.md#complete-local-modulation-calculation) | Exact centers/radii, complete selected count and torus mass; new-family original return, center-plus-radius box and positivity are separately paid. |
| support | [Exact scope of balance and sources](#8-scope-of-the-balance-and-retained-source-depth) | Restricted algebraic motivation, actual degree logarithm, accepted source proof limits and no unchanged-schedule theorem transplanted to the new family. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T00:11 |
| status | proved |
| reason | Adopt the entire LB1--LB27 new-family theorem after main reading of complete C658 and isolated whole R873. The exact integer21/11 threshold with logarithmic multiplier meets arbitrary-prime source eligibility and every newly reconstructed original2d cyclic, sample, variation, translated-law and closed-box premise. The actual prime threshold pays the genuine interpolation logarithm; all five costs and complete centered support give the uniform critical strip with both M powers canceled. The exact actual-degree comparisons prove the criterion(d/(1+log d))^(8/21)tau tending to infinity for every positive shrinking sequence, with arbitrary divergence speed. The surviving degree logarithm and log2<m(P)<log4 scope remain. No old-schedule substitution, pure d criterion, bounded-H endpoint, near-one family, global optimum, native work or unrestricted completion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire new-family statement](#statement) | LB1--LB14: exact integer thresholds, actual minimal polynomial/full2d objects and measures, complete finite budgets and all signed closed-box indices, entire centered support, uniform strips, actual degrees/logarithms and arbitrary shrinking sequences. |
| argument | [Complete new-family reconstruction](#complete-argument) | Sections1--8/LB15--LB27: all integer/alias/source/factor/cyclic/variation/logarithm and translated-law prerequisites, five costs, exact support and degree/sequence computations, with restricted balance and no broad optimum. |
| dependency | [Accepted arbitrary-prime source interface](../audits/literature/MS05/Yin_U001.md#ms05-u001) | Exact arbitrary-distinct-prime-construction and four-exponent-specialization sections, complete factor removal and interlacing applicability at the retained statement/selected-proof depth; new eligibility checked here. |
| dependency | [Exterior-root identity](../audits/literature/RY26/Yin_U001.md#ry26-u001) | Exact exterior-root-measure-expense section and positive-root formula applied to the current four exponents; independent actual irreducibility is supplied before identifying total measure. |
| dependency | [Accepted integer Bertrand input](Yin_C_G0356_v1.md#argument) | Integer threshold n>=2 implies a prime n<p<2n, at the retained classical statement depth; no new source-proof audit or numerical prime search. |
| support | [Bertrand attribution boundary](../audits/literature/Mig78/Yin_U001.md#mig78-u001) | Existing Proposition5-length account of the accepted classical interval input, not attribution of its original proof to Mignotte. |
| dependency | [Finite cyclic-rank mechanism](Yin_C_G0171_v1.md#two-block-circulant-rank-transfer) | The finite mechanism, with all new dimensions, boundary-column ranks and actual c eligibility reconstructed in Section3. |
| dependency | [Actual cyclic phase blocks](Yin_C_G0171_v1.md#two-block-torus-phase) | Same fixed-K torus equal modulus/common zeros, new c-grid rank and missing mode with correct inverse orientation. |
| dependency | [Finite interpolation mechanism](Yin_C_G0172_v1.md#moving-cubic-discrete-fejer) | Any-c finite grid and original phase mechanism, with every new original-law and sample condition re-established before use. |
| support | [Earlier family reconstruction](Yin_C_G0644_v1.md#complete-argument) | Actual finite proof interfaces and source scopes only; its25/11 numerical bounds and old r>2 comparisons are not new-family conclusions. |
| dependency | [Adopted same-circle BV lemmas](Yin_C_G0656_v1.md#complete-argument) | Sections1--5 generic monotone occupation, finite Dirichlet/interpolation variation and cap-shell mechanisms, applied only after all new c,d and phase hypotheses are checked. |
| dependency | [Torus/probability return mechanisms](Yin_C_G0641_v2.md#combined-argument) | Exact relative derivatives, conditional product integral, every-path event-norm smoothing and finite weak Fourier lemma; all new translated-law prerequisites rebuilt here. |
| dependency | [All-scale joint-shell regularization](Yin_C_G0641_v2.md#complete-additional-joint-shell-argument) | Exact low/middle/high shell constants and all-rho/tau scope, after current laws satisfy every required amplitude/contact bound. |
| dependency | [Actual torus amplitude input](Yin_C_G0633_v2.md#additional-complete-logarithm-free-and-two-sided-argument) | Same fixed-K g and product-Haar integral r_s<=8s^(2/3); original circle bounds follow from newly proved finite-mean absorption. |
| dependency | [Positive finite kernel](Yin_C_G0637_v1.md#complete-argument) | Probability normalization, closed support and3pi/M first moment; current original mean and coefficient identities are separately proved. |
| dependency | [Entire torus phase bands](Yin_C_G0638_v1.md#complete-local-modulation-calculation) | Exact centers/radii, complete selected count and torus mass; new-family original return, center-plus-radius box and positivity are separately paid. |
| support | [Exact scope of balance and sources](#8-scope-of-the-balance-and-retained-source-depth) | Restricted algebraic motivation, actual degree logarithm, accepted source proof limits and no unchanged-schedule theorem transplanted to the new family. |
| review | [Independent whole new-family finding](../audits/reviews/Yin_R_G0873_v1.md#log-balanced-family-whole-independent-finding) | Entire LB1--LB27 and all eight proof sections, exact source/prime/factor/degree/measure, new original2d and every translated law, complete five-cost and closed-box support, actual logarithmic payment and degree constants, arbitrary sequence quantifiers and all source limits. |


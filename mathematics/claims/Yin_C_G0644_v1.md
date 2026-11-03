---
author: Yin
---

# Balanced prime separation and original-degree contact layers

Human author Yin.
Root supplied the actual-degree conversion, changed distinct-prime schedule, restricted balance and complete new scaling proposal.
Paid_comparison checked the arbitrary-prime source applicability, rebuilt the exact original finite comparison and translated inputs, and completed every numerical constant, support threshold and degree equivalence.
Both are contributors, not independent reviewers.
The complete fixed C641v2 input is [adopted through its whole-review decision](Yin_C_G0641_v2.md#decision-whole-reviewed-2026-10-23); this new family's reconstruction and conclusions require their own independent whole review.
The new schedule is a different actual family; no old fixed-schedule conclusion is applied merely by renaming c.
No prime enumeration, huge integer evaluation, new source acquisition or native experiment is used.

## Statement

Fix the same even killer exponent

    K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))).

For every integer j>=1 define

    a_j=min{p prime:p>(j+1)K},
    b_j=min{p prime:p>(K+a_j+3)^2},
    L_j=K+a_j+b_j+2, M_j=floor(a_j/4), r_sep=25/11,
    n_j=min{N positive integer:N^11>=(L_j+1)^25},
    c_j=min{p prime:p>n_j}.                                    (BS1)

Thus n_j=ceil((L_j+1)^(25/11)) is an exact integer definition.
All uses of Bertrand below are at integer thresholds.
With ell=(K,a_j,b_j,c_j), define the full raw numerator and actual polynomial

    Q_j(x)=(x^2-1)product_(i=0)^3(x^ell_i-1)
       -(x/2)sum_(q=0)^3(x^ell_q+1)product_(i!=q)(x^ell_i-1),
    P_j=Q_j/(x-1)^3,
    D_j=deg Q_j=c_j+L_j, d_j=deg P_j=c_j+L_j-3.                (BS2)

At the accepted MS05 arbitrary-distinct-prime statement and selected-proof/application depth, P_j is monic integral irreducible, is the actual Salem minimal polynomial, has trace-1 and even degree d_j, and has NO further cyclotomic factor.
Its exterior root beta_j satisfies2<beta_j<4, so log2<m(P_j)=log beta_j<log4.
These are bounded positive total measures, not a near-one family.

In the ORIGINAL2d_j coefficient window let A_rel,j have all d_j columns P_j,xP_j,...,x^(d_j-1)P_j, and set

    R_j=I-A_rel,j(A_rel,j^T A_rel,j)^-1 A_rel,j^T,
    v_j(z)=(1,z,...,z^(2d_j-1))^T,
    k_j(z)=(2d_j)^-1 v_j(z^-1)^T R_j v_j(z).

For0<tau<=1 put psi_tau(s)=(1-(1-s)/tau)_+ and f_(j,tau)=psi_tau(k_j).
All Fourier coefficients use probability Haar and exp(-i gamma dot theta); all angular derivatives use radians.
Write W_*(f)=sum_(h in Z,h!=0)|fhat(h)|.
For fixed j,tau this sum is finite, every unit-circle root of P_j has f_(j,tau)=1, and1-integral f_(j,tau)>=1/2.

The SAME torus phase, now pulled back through the NEW circle, is defined explicitly by

    R=(z^K-1)(u-1)(v-1),
    S=(z^K+1)(u-1)(v-1)+(z^K-1)(u+1)(v-1)+(z^K-1)(u-1)(v+1),
    Acal=-(z^2-1)R-zR/2+zS/2,
    Bcal=(z^2-1)R-zR/2-zS/2,
    U=Acal/Bcal off their common zeros, U=0 on those zeros,
    g_0=|Acal|^2+|Bcal|^2, Ncal=2Acal conjugate(Bcal),
    V(z,u,v)=U(z^-1,u^-1,v^-1),
    g(z,u,v,w)=g_0(z^-1,u^-1,v^-1),
    h=(1+Re(wV))/2, Kcal=1-h, F_tau=(1-h/tau)_+,
    iota_j(z)=(z,z^a_j,z^b_j,z^c_j),
    H_j(gamma)=gamma_0+a_j gamma_1+b_j gamma_2+c_j gamma_3.

Let nu_1,nu_4 be probability circle and four-torus Haar, and let mu_(j,a) be the pushforward of nu_1 through z to a*iota_j(z), for EVERY a in T^4.
Define

    E_j=[1+pi L_j(5+2log c_j)]/c_j,
    epsilon_j=(4L_j-5)/(2d_j)+E_j/2,
    E_sep=100(1+pi), T_M=1+log M.

The complete NEW original comparison and alias statements are

    ||k_j-Kcal composed with iota_j||_(L1(nu_1))<=epsilon_j,
    epsilon_j<=E_sep M_j^(-28/11)(1+log M_j), M_j>=2,            (BS3)
    H_j(delta)!=0 for EVERY nonzero integer delta in[-2M_j,2M_j]^4.
                                                                    (BS4)

The phase convention at the single original common-zero point does not affect the L1 comparison.
In particular every finite polynomial in the CLOSED M_j box has the exact selected Fourier coefficients after pullback and the exact torus mean on every translated circle.
No nonlinear mean equality or original-coordinate independence is asserted.

Put

    D_l=||partial_l Acal||_infinity+||partial_l Bcal||_infinity,
    G_K=sqrt(||g||_infinity),
    c_weight,K=6pi[1+10 sum_(l=1)^3 D_l+2(G_K+1)],
    C_smooth,K=3pi[24*64^(3/4)sum_l D_l+4^(3/4)],
    C_return2,K=2*2048^(3/4)c_weight,K+2C_smooth,K,
    C_loc,K=ceil(32000pi+1024pi(K+4)),
    C_support,K=8[9(C_loc,K+1)^2]^(3/4)4^(-9/8),
    C_sep,K=C_support,K(E_sep^(3/4)+C_return2,K),
    M_sep,K=ceil(max{2,c_weight,K,(C_loc,K+1)^(33/29),
                             7^(11/3),(C_loc,K+29)^(11/7)}).

These constants use only the fixed K-phase.
For rho>0 define V_rho=Ncal(z^-1,u^-1,v^-1)/(g+rho), h_rho=(1+Re(wV_rho))/2 and F_(tau,rho)=(1-h_rho/tau)_+.
Set r_s=s/(g+s), and on a probability space use N_mu(f)=sup_(mu(E)>0)mu(E)^(-1/4)integral_E|f|dmu.
The exact positive kernel used is P_M=J_(floor(M/2)+1), where Fej_N(t)=N^-1|sum_(l=0)^(N-1)e^(ilt)|^2 and J_N=Fej_N^2/[(2N^2+1)/(3N)].
Let Q_(tau,rho) be F_(tau,rho) convolved with its four-coordinate product.
This P_M has mass one, closed support[-M,M] and first angular moment at most3pi/M, at the adopted C637 normalization.
For M=M_j>=max{2,c_weight,K} and0<tau<=1/64, define

    B_sep(j,tau)=(epsilon_j/tau)^(3/4)
                                +C_return2,K M^-1 tau^-1/8.

For EVERY finite Gamma subset of the CLOSED[-M,M]^4 integer box,

    sum_(gamma in Gamma)
      |fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma)|
       <=8 card(Gamma)^(3/4)B_sep(j,tau).                     (BS5)

All zero/negative harmonics, empty sets, tied magnitudes and endpoints are included.
The proof below rebuilds every new original-law premise of this comparison; only the unchanged torus and probability-space arguments are reused.

Use the actual C638 integer centers, fixed by

    D_0(z)=-2(z-z^-1)+(z^K+1)/(z^K-1), b(z)=Im D_0(z),
    z_0=exp(i pi/K),
    -cot(t_(k,m)/2)=16sqrt(km)-b(z_0), t_(k,m) in(-pi,0),
    phi_z(t)=arctan(2/[b(z)-cot(t/2)]),
    n_(k,m)=floor((k+m)phi_(z0)'(t_(k,m))+1/2).

This local phase is evaluated only on its actual regular neighborhood; |n_(k,m)|<=14(k+m).
For L_tau=floor(1/(4sqrt(tau))) and integer J>=2 put

    R_z=ceil(C_loc,K J^(1/3)), R_u=ceil(C_loc,K sqrt(L_tau)J^(5/6)),
    G_(L_tau,J)={(-p,-q,m,k):1<=k<=L_tau,1<=m<=J,
                              |p|<=R_z,|q-n_(k,m)|<=R_u},
    N_sel=L_tau J(2R_z+1)(2R_u+1)
          <=9(C_loc,K+1)^2 L_tau^(3/2)J^(13/6).

Whenever

    R_z,J,L_tau<=M, 14(L_tau+J)+R_u<=M,                       (BS6)

all original frequencies are distinct and positive and

    W_*(f_(j,tau))>=3log(J+1)/(32768pi)
                                -8N_sel^(3/4)B_sep(j,tau).    (BS7)

For EVERY actual j with M=M_j>=M_sep,K and EVERY pair of real H,tau in

    16<=H<=M^(16/11)T_M^(-4/7)/64,
    M^(-16/11)T_M^(4/7)H<=tau<=1/64,                          (BS8)

one has

    W_*(f_(j,tau))>=3log H/(131072pi)
       -C_sep,K[H^(-29/32)+T_M^(-11/28)H^(-9/32)].            (BS9)

Consequently every actual shrinking sequence tau_j->0 with

    M_j^(16/11)(1+log M_j)^(-4/7)tau_j->infinity              (BS10)

has W_*(f_(j,tau_j))->infinity.
This entire conclusion concerns the changed family(BS1).

Its ACTUAL degree satisfies, for all j with M_j>=2,

    M_j^(50/11)<d_j<2^33 M_j^(50/11).                         (BS11)

Thus(BS10) is equivalent, for any positive width sequence, to

    d_j^(8/25)(1+log d_j)^(-4/7)tau_j->infinity.               (BS12)

For comparison ONLY, denote by c_j^square the least prime>(L_j+1)^2 and d_j^square=c_j^square+L_j-3, with the SAME a_j,b_j,M_j.
The unchanged family in C641v2 satisfies

    256M_j^4<d_j^square<2^21 M_j^4, M_j>=2.                   (BS13)

Its original C641v2 sequence condition M_j^(8/7)(1+log M_j)^(-4/7)tau_j->infinity is equivalently
(d_j^square)^(2/7)(1+log d_j^square)^(-4/7)tau_j->infinity.
The exponents2/7 and8/25 refer to different actual polynomial families and are not identified by a change of notation.
Neither exponent is claimed optimal.
There is no every-large-degree theorem, bounded-enlargement endpoint, removal of the stated logarithmic factor, near-one family or unrestricted G0001 conclusion.

## Sources, reuse and acceptance boundary

The exact arbitrary-distinct-prime construction and four-exponent killer were read in [MS05-U001](../audits/literature/MS05/Yin_U001.md#ms05-arbitrary-distinct-prime-construction), with its retained manuscript edition, primary-statement acceptance, selected construction proof/application checks and excluded general-original-proof audits unchanged.
The current [C494 source and schedule account](Yin_C_G0494_v1.md#fixed-trace-moving-exponent-source) was checked, but its fixed square schedule is not treated as already proving the new schedule.
The exterior-root identity was read at [RY26-U001](../audits/literature/RY26/Yin_U001.md#exterior-root-measure-expense) and is applied directly below.

The exact C171 Sections2--3 and C172 Sections2--4 were read for the complete cyclic-rank, common-zero, variation, missing-mode and normalized L1 comparison.
Their proof assumptions are re-established below for the new c; no statement restricted to their old schedule is silently generalized.
C565's original alias proof was read and repeated at the new lower separations.
C638 supplies only the unchanged TORUS bands and their actual centers; its fixed-family original return is not imported.
C641v2 supplies the complete weighted torus/probability-space mechanism only after the new original-law premises are established below.

The accepted integer Bertrand statement is the same retained input used by [C356](Yin_C_G0356_v1.md#argument), [C217v2](Yin_C_G0217_v2.md#bounded-length-gap) and [Mig78-U001](../audits/literature/Mig78/Yin_U001.md#proposition-5-length): for every integer n>=2 there is a prime n<p<2n.
Its classical original proof is not newly audited and it is not attributed as a new theorem of Mignotte.
The exact real thresholds here are rounded before applying that theorem.
No new download, source-version substitution, quantitative prime-distribution assumption or numerical prime search is made.
The accepted source depth does not expand through this application.

## Complete argument

### 1. New prime eligibility, complete factor removal and original measure

The exact K is even and at least3, and a_j>2K implies K+a_j+3<=2a_j.
All a_j,b_j,c_j are distinct primes>K, so are odd, coprime to K and pairwise coprime.
Also c_j>n_j>=(L_j+1)^(25/11)>(L_j+1)^2, hence L_j<c_j and L_j>6.
Existence follows from the accepted integer Bertrand theorem (or infinitude of primes); no actual values are computed.

Apply the exact MS05-U001 construction with q=4, k_1=K and the three eligible distinct primes just proved.
For completeness, the relevant applicability account is as follows.
A root of unity in the raw numerator either makes two powered coordinates equal1, forcing x=1 by pairwise coprimality, or lies on a constant-x maximal torsion coset killed by K.
The latter makes the K-coordinate equal1, while exactly one such coordinate cannot satisfy the displayed source hypersurface equation.
Thus1 is the only root of unity in Q_j.
In the undivided numerator2Q_j the second sum has at1 exact order3 and coefficient
-2 sum_q product_(i!=q)ell_i, which is nonzero; the first term has order5.
Therefore the exact cyclotomic divisor is(x-1)^3.
The four-term parity makes Q_j integral, and monic division gives integral P_j.
The source circular-interlacing conclusion has only a Salem factor plus possible cyclotomic factors, or a reciprocal quadratic exception.
The root-of-unity exclusion removes the additional factors, and actual d_j>2 removes the quadratic exception.
Consequently P_j is the ACTUAL irreducible Salem minimal polynomial, not an unspecified factor.
The leading terms give degree c_j+L_j-3 and trace-1, and parity makes this degree even.
These deductions reuse the accepted source interface at its existing proof depth.

For its exterior root beta>1, dividing the exact raw identity gives

    beta-beta^-1=(1/2)sum_(e in {K,a,b,c})(beta^e+1)/(beta^e-1).

Each summand exceeds1 and is at most(beta+1)/(beta-1).
Thus beta-beta^-1>2 and beta+beta^-1<=4, yielding2<beta<4.
A Salem minimal polynomial has total logarithmic measure log beta, proving the claimed interval.

### 2. Exact new cyclic comparison in the same original window

Suppress j and set Q=(x-1)^3P=A+x^c B, with

    R_0=(x^K-1)(x^a-1)(x^b-1),
    S_0=sum_(e in {K,a,b})(x^e+1)product_(v in {K,a,b},v!=e)(x^v-1),
    A=-(x^2-1)R_0-xR_0/2+xS_0/2,
    B= (x^2-1)R_0-xR_0/2-xS_0/2.

Both are integral, have degree L, constant coefficients-1 and1 and leading coefficients-1 and1.
The actual raw coefficient matrix T has r=2d-deg Q=c+L-6 columns Q,xQ,...,x^(r-1)Q in the SAME N=2d coordinates.
They are independent by their distinct leading degrees.
Write Pi_Q for their range projection and Pi_P=I-R_j for the original full P relation projection.
Since the raw relation space is contained in the P relation space with dimensions d-3 and d, Pi_P-Pi_Q is an orthogonal projection of rank3.

In R^c let S_c e_i=e_(i+1 mod c) and form

    V_c=[A(S_c);B(S_c);0_(2L-6)-by-c].

Let Pi_V be its actual range projection, with no full-rank assumption.
The first c columns T_0 of T agree with V_c for0<=i<c-L; only L columns can differ.
Thus rank(T_0-V_c)<=L, and the two corresponding range projections differ in rank by at most2L: each range has codimension at most L over their intersection.
The remaining L-6 columns extend im T_0 inside im T by exactly L-6.
Every difference of orthogonal projections has operator norm at most1, so

    ||Pi_Q-Pi_V||_trace<=3L-6,
    ||Pi_P-Pi_V||_trace<=3L-3.                                (BS14)

No spectral lower bound or omitted cyclic boundary is used.

On the unit torus, Acal/(zR)=-1/2+H and Bcal/(zR)=-1/2-H, where
H=-(z-z^-1)+(C(z^K)+C(u)+C(v))/2 is purely imaginary and C(w)=(w+1)/(w-1).
Hence |Acal|=|Bcal| everywhere by continuity, and their common zeros are exactly the points with at least two of z^K,u,v equal1.
At an actual c-th root omega!=1 none of omega^K,omega^a,omega^b equals1, because c is prime and coprime to all three exponents.
At omega=1 both A,B vanish.
The cyclic Fourier basis therefore gives rank V_c=c-1 and

    Pi_V,11=Pi_V,22=(I_c-J_c/c)/2,
    Pi_V,12(i,l)=(1/(2c))sum_(omega^c=1)U(omega,omega^a,omega^b)omega^(l-i),
    Pi_V,21=Pi_V,12^*.

The phase sample at omega=1 is exactly0; the final2L-6 rows and columns vanish.
The eigenvector entries omega^-i fix this sign convention.

### 3. Complete actual variation and Haar L1 return

A+B=-xR_0, and neither A nor B has zero constant coefficient.
Every common root is therefore a root of unity, and pairwise coprimality of K,a,b makes1 their only common root.
The exact values

    [A/(x-1)^2](1)=Ka+Kb+ab,
    [B/(x-1)^2](1)=-(Ka+Kb+ab)

show that their greatest common divisor is precisely(x-1)^2, up to scalar.
Their equal modulus on the circle prevents any other circle zero of either polynomial.
With the degree-L reciprocal conjugate one has B=-A^*.
After cancellation the smooth circle phase U_j=A/B has U_j(1)=-1 and is a unimodular product of L-2 factors (z-alpha)/(1-conjugate(alpha)z), with all alpha off the unit circle.
For each factor its angular argument derivative is(1-|alpha|^2)/|e^(it)-alpha|^2, whose absolute integral is2pi: inside the disk this is the Poisson geometric series; outside use1/conjugate(alpha).
Thus the UNNORMALIZED total variation is at most2pi(L-2)<=4pi L, independent of distances to the circle.
This argument uses A,B only, not the rule selecting c.

Let Fej_c(t)=c^-1|sum_(r=0)^(c-1)e^(irt)|^2, theta_l=2pi l/c, and
I_c f(theta)=c^-1 sum_l f(theta_l)Fej_c(theta-theta_l).
Grid orthogonality gives c^-1 sum_l Fej_c(theta-theta_l)=1.
Coordinate FTC and the fact that any point lies in at most c|t|/(2pi)+1 of the equally spaced oriented arcs give

    c^-1 sum_l |f(theta_l+t)-f(theta_l)|
       <=V(f)(|t|/(2pi)+1/c).

The elementary bound Fej_c(t)<=min(c,pi^2/(ct^2)) for|t|<=pi gives
integral|t|Fej_c(t)dHaar<=pi(1/2+log c)/c, by splitting at pi/c.
Consequently ||I_c f-f||_1<=V(f)(5/4+(log c)/2)/c.
For f(z)=U_j(z^-1), replace its value-1 at the single sample1 by0 and call the resulting polynomial q_j.
This costs EXACTLY1/c in Haar L1, and yields

    ||q_j-U_j(z^-1)||_1<=[1+pi L(5+2log c)]/c=E_j,
    |q_j|<=1, deg_Fourier(q_j)<=c-1.                           (BS15)

The sample convention and every cyclic zero mode are retained.

For any self-adjoint matrix H, |v^*Hv|<=v^*|H|v and integral vv^*dHaar=I_N.
Thus, with k_V=1-(2d)^-1 v^*Pi_Vv,
||k_j-k_V||_1<=(3L-3)/(2d) by(BS14).
The exact block evaluation gives

    v^*Pi_Vv=c-|sum_(r=0)^(c-1)z^r|^2/c+c Re(z^c q_j(z)).

For K_q=(1-Re(z^c q_j))/2,

    k_V-K_q=((d-c)/(2d))(1+Re(z^c q_j))+Fej_c(arg z)/(2d)>=0.

Since z^c q_j has no constant term, integration gives
||k_V-K_q||_1=(d-c+1)/(2d)=(L-2)/(2d).
Adding(BS15)/2 proves the exact first line of(BS3).
The smooth phase U_j and the torus definition differ at the original circle point1 only; this does not affect Haar L1.
All normalization is by2d, not2c or the raw degree.
Composing with psi_tau and using range[0,1] gives the true original L^(4/3) error at most(epsilon_j/tau)^(3/4).

### 4. New epsilon rate, aliases and every translated-law premise

Put r=25/11 and suppress j.
Use d>=c, c>(L+1)^r and the decreasing function(5+2log x)/x for x>1 to obtain

    epsilon<= [2L+1/2+(pi L/2)(5+2r log(L+1))]/(L+1)^r
       <=(3+5pi)(1+log L)L^(-14/11).

Here r<5/2, L>=2 and log(L+1)<=1+log L.
The function(1+log x)x^(-14/11) decreases for x>=1.
Since L>b>a^2>=16M^2 and log16<4,

    epsilon<=5(3+5pi)16^(-14/11)M^(-28/11)(1+log M)
            <=E_sep M^(-28/11)(1+log M).                       (BS16)

This proves the claimed convenient constant for every M>=2, with no additional asymptotic onset.
It uses only the lower separation for c.

Since2M<=a/2, one has

    a>2M,
    b>(K+a+3)^2>2M(1+a),
    c>(L+1)^2>2M(1+a+b).

In a nonzero delta in the closed2M box, its highest nonzero weighted coordinate therefore dominates the sum of all lower ones.
This proves(BS4) including endpoints.
Every difference of a selected closed-M index and a finite-polynomial closed-M support index lies in this closed2M box.
Thus exact coefficient equality follows, and translation multiplies a nonconstant zero-mean original character only by a^delta.
For selected gamma=(-p,-q,m,k) with k>=1, positivity follows from c>M(1+a+b), independently of the signs of the first three coordinates.

The torus polynomials, their amplitudes/derivatives, their common-zero convention and C638 bands are IDENTICAL to those in C641v2, because only the choice of c has changed.
The exact C637 squared positive kernel retains support[-M,M] and first moment3pi/M.
For0<rho<=1,0<eta<=1 and s>=rho, establish the new translated law by taking W to be r_s, V_eta=eta/(eta+h_rho), or r_s V_eta, with
 r_s=s/(g+s), h_rho=(1+Re(w Ncal(inverse)/(g+rho)))/2.
All these functions are positive and smooth at positive scales.
For r_s the logarithmic derivative sum is at most sum D_l/sqrt(s).
For the weighted product with s>=rho, the sum is at most
[10 sum D_l+2(G_K+1)]/sqrt(rho).
These are the identical pointwise torus derivative calculations CW11--CW14, independent of c.
By the NEW alias just proved, convolution has exactly its torus mean on EVERY new translated circle.
Smooth FTC along intermediate coordinate shifts and the kernel moment give

    sup_a integral W dmu_(j,a)<=integral W dnu_4
       +[3pi(10sum D_l+2(G_K+1))/(M sqrt(rho))]
                                      sup_a integral W dmu_(j,a).

For M sqrt(rho)>=c_weight,K the bracket is at most1/2.
The r_s-only version also applies when M sqrt(s)>=c_weight,K.
The torus law integral r_s<=8s^(2/3) for s<=1 is the SAME actual C633 amplitude law; for s>1 use r_s<=1.
The identical conditional w integral is at most sqrt(eta), with r_s independent of w on product Haar alone.
Therefore, on ALL new translated circles,

    integral r_s<=16s^(2/3) when s<=1 and M sqrt(s)>=c_weight,K,
    integral V_eta<=2sqrt(eta),
    integral r_s V_eta<=16sqrt(eta)s^(2/3), s>=rho,
    mu{h_rho<=eta,g<=s}<=64sqrt(eta)s^(2/3).                    (BS17)

No independence or nonlinear exact mean is assigned to the new original circle.

All remaining C641v2 arguments now have their actual hypotheses established at this NEW law.
Specifically, its every-path contact estimate uses only the pointwise smooth phase and the joint bound(BS17), so its four-coordinate smoothing event norm remains C_smooth,K M^-1 tau^-1/8.
Its low/middle/high shell proof uses only(BS17), the bounded g and the pointwise nonzero-set inclusion; it gives on each new translated circle and on the torus
integral|F_tau-F_(tau,rho)|^(4/3)<=2048rho^(2/3)tau^-1/6 for0<tau<=1/64, including rho/tau>1.
The event-first norm triangle and finite height-truncation/Bessel estimates are statements on arbitrary probability spaces with finite orthonormal modulus-one characters; they require no arithmetic schedule premise.
Using rho=(c_weight,K/M)^2, these give two regularizations, two smoothings and the rebuilt original composition cost(BS3), exactly B_sep.
The NEW finite-polynomial coefficient equality then proves(BS5).
This reconstructs every original-law and scalar input needed for the reused probability-space mechanism, without applying the old fixed-family theorem as a black box to a new schedule.

### 5. Complete support, balanced scale and uniform enlargement

C638's local phase proof is a statement about the fixed K-torus U, so its actual integer centers, radii, torus coefficient mass3log(J+1)/(32768pi) and exact band count apply unchanged.
Under(BS6), the NEW aliases and positive frequencies just proved allow every selected coefficient to be paid by(BS5).
This proves(BS7).
Using the ENTIRE N_sel bound, L_tau<=1/(4sqrt(tau)) and(BS16), its error is at most

    C_support,K J^(13/8)
       [E_sep^(3/4)M^(-21/11)tau^(-21/16)T_M^(3/4)
                         +C_return2,K M^-1tau^(-11/16)].       (BS18)

For(BS8) choose J=floor(H^(1/4))>=2.
The exact inequalities, retaining all ceilings, are

    L_tau<=M^(8/11)T_M^(-2/7)H^-1/2/4,
    J<=M^(4/11)T_M^(-1/7),
    R_z<=(C_loc,K+1)M^(4/33)T_M^(-1/21),
    R_u<=(C_loc,K+1)M^(4/11)T_M^(-1/7)H^-1/24/2.              (BS19)

Here ceil(Cx)<=(C+1)x for x>=1.
Since T_M,H>=1,
14(L_tau+J)+R_u<=(7/2)M^(8/11)+[14+(C_loc,K+1)/2]M^(4/11).
The explicit M_sep,K makes each term at most M/2, and separately makes R_z<=M.
Also L_tau,J<=M.
Thus the entire actual centered support fits the closed box uniformly, not just its unshifted widths.

Inserting J^(13/8)<=H^(13/32) and the lower width into(BS18), the first error has M exponent-21/11+(16/11)(21/16)=0 and logarithmic exponent3/4-(4/7)(21/16)=0.
Its H exponent is13/32-21/16=-29/32.
The second has M exponent-1+(16/11)(11/16)=0, logarithmic exponent-11/28, and H exponent13/32-11/16=-9/32.
These are exactly the two complete errors in(BS9), with C_sep,K covering their fixed coefficients.
Finally J+1>H^(1/4) gives the stated main term.
For every sequence in(BS10), choose H_enl,j=M_j^(16/11)(1+log M_j)^(-4/7)tau_j; all hypotheses eventually hold with H=H_enl,j and both errors tend to zero.
This proves the claimed uniform-to-sequence implication.

### 6. Actual degrees for the old and new families

The elementary inequalities K+a+3<=2a and b>a^2 hold for every j>=1.
Apply the accepted Bertrand statement to the INTEGER(K+a+3)^2 to obtain

    a^2<b<2(K+a+3)^2<=8a^2,
    L+1=K+a+b+3<=b+2a<=2b.

For the old square family its INTEGER threshold(L+1)^2 gives
 a^4<c^square<2(L+1)^2<=8b^2<512a^4.
Its ACTUAL degree satisfies c^square<d^square<2c^square<1024a^4.
For M>=2,4M<=a<4M+4<=6M.
Thus256M^4<d^square<1024*6^4 M^4<2^21M^4, proving(BS13).
No raw degree or replacement by c is used.

For the new family x=(L+1)^(25/11)>1 and n=ceil x satisfy x<=n<=2x.
Bertrand is applied to this integer n>=2, giving

    x<=n<c<2n<=4x,
    c<d<2c<8(L+1)^(25/11).

As L+1>a^2>=16M^2, the lower bound d>M^(50/11) follows.
For the upper bound, L+1<=2b<16a^2<576M^2<2^10M^2, so

    d<2^3(2^10M^2)^(25/11)
      =2^(283/11)M^(50/11)<2^33 M^(50/11).

This proves(BS11) with deliberately generous constants, for the ACTUAL d.

To make the logarithmic equivalences explicit, write T_d=1+log d.
For the old family, T_M<=T_d<=(1+21log2+4)T_M, and
2^(16/7)M^(8/7)<(d^square)^(2/7)<2^6M^(8/7).
Consequently its degree-normalized and M-normalized scale factors are bounded above and below by fixed positive multiples of one another.
In particular M^(8/7)T_M^(-4/7)>=2^-6(d^square)^(2/7)T_d^(-4/7).
For the new family, T_M<=T_d<=(1+33log2+50/11)T_M and

    M^(16/11)<d^(8/25)<2^(264/25)M^(16/11).

The same two-sided multiplication gives the exact equivalence(BS10)--(BS12), not merely one implication.
Combining this old-family equivalence with the actual C641v2 statement proves the separate old2/7 degree conclusion.
It does not convert that old family into the new8/25 family.

### 7. Restricted algebraic balance and remaining boundaries

Within this SPECIFIC support and five-cost argument, selecting c at a power r>2 of L+1 gives the power constraints

    theta_M<=min{8(r-1)/7,16/11},
    theta_degree<=min{4(r-1)/(7r),8/(11r)}.

These are an algebraic comparison of the two displayed error powers, not a new all-r endpoint theorem.
The first degree expression increases with r and the second decreases.
Their equality is44(r-1)=56, namely r=25/11, and the common value is8/25.
This identifies the balance inside this particular construction/return/support mechanism only.
It proves no optimality for other schedules, kernels, supports, original coefficient comparisons or Mahler bounds.

Finally the actual projection R_j has rank d_j, so integral k_j=1/2 and0<=k_j<=1.
At each of the d_j-2 unit-circle roots of the genuine Salem P_j, every original relation column annihilates the evaluation vector, hence k_j=1.
The scalar bound psi_tau(s)<=s on[0,1] gives the stated contact value minus Haar mean at least1/2.
For each fixed positive tau, the composition of this trigonometric polynomial with the scalar Lipschitz cap is periodic Lipschitz, hence has a square-integrable weak derivative.
The finite derivative Bessel bound followed by Cauchy--Schwarz with sum_(n!=0)n^-2<infinity gives absolute Fourier summability, exactly as in C174's generic fixed-input argument.
No uniform fixed-j derivative bound is used in the varying-j estimates.
These observations preserve the original probability, contact and fixed-input boundaries for the NEW family, while leaving the unrestricted Task unresolved.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision balanced-prime-family-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T21:34 |
| status | open |
| reason | Register the genuinely changed25/11 integer-threshold prime family, complete source factor/degree/trace/measure application and rebuilt original2d cyclic/variation/fullL1 and translated interfaces. All finite return and centered support costs yield logarithmic16/11 M-scale and8/25 actual-degree sequence conclusions; the old square-family2/7 comparison is separate. Root and paid_comparison are contributors. C641v2 is actually adopted, but its fixed-schedule theorem is not silently applied to new c. Fresh isolated whole review remains required. No source-proof upgrade, prime enumeration, near-one family, general optimum or unrestricted completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact balanced-family statement](#statement) | BS1--BS13, exact new integer threshold and actual Salem input/full2d window, all finite closed-box Gamma, full original comparison and explicit epsilon, actual centered support and full H,tau/sequence quantifiers, new8/25 and separate old2/7 degree equivalences. |
| argument | [Complete new-family reconstruction](#complete-argument) | Entire Sections1--7/BS14--BS19, accepted source applicability and complete factor removal, cyclic rank/missing-mode/variation/fullL1, new aliases and every translated input, five costs, support/degree/logarithmic constants and restricted balance. |
| dependency | [Accepted arbitrary-prime and killer interface](../audits/literature/MS05/Yin_U001.md#ms05-u001) | Exact arbitrary-distinct-prime construction and four-exponent specialization sections: actual retained manuscript, primary-statement and selected construction proof/application depth, complete2(x-1)^3 removal, irreducibility, original degree/trace and fixed K, without expanding excluded source-proof or every-large-degree claims. |
| dependency | [Exterior-root expense](../audits/literature/RY26/Yin_U001.md#ry26-u001) | Exact exterior-root-measure-expense section: positive-root identity for arbitrary exponent sizes yields2<beta<4 and total log measure once actual Salem irreducibility is supplied. |
| support | [Prior complete source account](Yin_C_G0494_v1.md#fixed-trace-moving-exponent-source) | Source-version, arbitrary-prime applicability and excluded source-proof scope only; its square schedule is not already a proof of the changed family. |
| dependency | [Finite cyclic-rank mechanism](Yin_C_G0171_v1.md#two-block-circulant-rank-transfer) | Exact finite same-window argument rebuilt here with new L,c,d,r and all boundary columns. |
| dependency | [Equal-modulus phase and missing mode](Yin_C_G0171_v1.md#two-block-torus-phase) | Same K-torus common zeros and correctly oriented cyclic Fourier blocks; new c coprimality and rank c-1 are explicitly checked. |
| dependency | [Variation and discrete interpolation](Yin_C_G0172_v1.md#moving-cubic-discrete-fejer) | Sections2--3 actual rational-factor variation, Fejer arc estimate and exact missing sample; all premises and costs rebuilt for the new c. |
| dependency | [Full original L1 mechanism](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | Rank3, same2d normalization and positive finite cyclic correction reconstructed before scalar composition; no old-family statement silently generalized. |
| support | [Earlier alias mechanism](Yin_C_G0565_v2.md#moving-band-exact-alias) | Lower-separation proof only; new closed2M exclusion and translated finite means are proved here. |
| dependency | [Adopted weighted torus/probability mechanism](Yin_C_G0641_v2.md#combined-argument) | Pointwise contact derivatives, conditional torus integral, every-path smoothing, all-scale shell bound and finite weak Fourier lemma, only after every changed original-law premise is reconstructed; all five costs paid. |
| dependency | [Old-family enlargement for degree comparison](Yin_C_G0641_v2.md#additional-joint-shell-statement) | Only the unchanged square-family logarithmic M8/7 conclusion used to obtain its separate degree2/7 statement; not applied to the new c schedule. |
| dependency | [Actual torus modulated bands](Yin_C_G0638_v1.md#statement) | M1--M3 local centers/radii and torus mass/support; new-family alias, positivity and original return are separately proved. |
| dependency | [Normalized positive kernel](Yin_C_G0637_v1.md#complete-argument) | Squared Fejer probability normalization, closed support and3pi/M first moment, with new original-circle coefficient/mean equalities proved here. |
| dependency | [Same actual torus amplitude bound](Yin_C_G0633_v2.md#additional-complete-logarithm-free-and-two-sided-argument) | Same fixed-K g and integral r_s<=8s^(2/3); no replacement by a conjugate or original-circle law. |
| dependency | [Accepted integer Bertrand statement](Yin_C_G0356_v1.md#argument) | For every integer n>=2, n<p<2n for some prime p, at the retained external-statement depth; all current thresholds are integers before use. |
| support | [Bertrand source-proof boundary](../audits/literature/Mig78/Yin_U001.md#mig78-u001) | Proposition5-length section retains the accepted classical prime-interval input; its original proof is not re-audited or attributed as a new theorem of Mignotte. |
| dependency | [Generic contact and fixed-input Fourier facts](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Projection/contact identity, scalar psi<=k and fixed-input derivative/Fourier argument rechecked for newly certified Salem inputs; no old moving-family conclusion transplanted. |
| support | [Sources and exact reuse boundaries](#sources-reuse-and-acceptance-boundary) | Actual inspected units and precise fixed-schedule versus reusable-proof distinctions, accepted classical statement depth, no new acquisition or computation. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T21:50 |
| status | proved |
| reason | Adopt the complete BS1--BS19 fixed new-family statement and proof after main reading of the entire C644 and isolated whole R852. The actual source-certified prime schedule, full original2d comparison, all translated laws, five costs and entire centered support are retained. The critical logarithmic16/11 M-scale is equivalent to the new actual-degree8/25 criterion; the old-family2/7 comparison remains separate. All source-depth and fixed-positive-measure restrictions remain; no bounded-enlargement endpoint, general optimum, near-one family or unrestricted Task completion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact balanced-family statement](#statement) | BS1--BS13, exact new integer threshold and actual Salem input/full2d window, all finite closed-box Gamma, full original comparison and explicit epsilon, actual centered support and full H,tau/sequence quantifiers, new8/25 and separate old2/7 degree equivalences. |
| argument | [Complete new-family reconstruction](#complete-argument) | Entire Sections1--7/BS14--BS19, accepted source applicability and complete factor removal, cyclic rank/missing-mode/variation/fullL1, new aliases and every translated input, five costs, support/degree/logarithmic constants and restricted balance. |
| dependency | [Accepted arbitrary-prime and killer interface](../audits/literature/MS05/Yin_U001.md#ms05-u001) | Exact arbitrary-distinct-prime construction and four-exponent specialization sections: actual retained manuscript, primary-statement and selected construction proof/application depth, complete2(x-1)^3 removal, irreducibility, original degree/trace and fixed K, without expanding excluded source-proof or every-large-degree claims. |
| dependency | [Exterior-root expense](../audits/literature/RY26/Yin_U001.md#ry26-u001) | Exact exterior-root-measure-expense section: positive-root identity for arbitrary exponent sizes yields2<beta<4 and total log measure once actual Salem irreducibility is supplied. |
| support | [Prior complete source account](Yin_C_G0494_v1.md#fixed-trace-moving-exponent-source) | Source-version, arbitrary-prime applicability and excluded source-proof scope only; its square schedule is not already a proof of the changed family. |
| dependency | [Finite cyclic-rank mechanism](Yin_C_G0171_v1.md#two-block-circulant-rank-transfer) | Exact finite same-window argument rebuilt here with new L,c,d,r and all boundary columns. |
| dependency | [Equal-modulus phase and missing mode](Yin_C_G0171_v1.md#two-block-torus-phase) | Same K-torus common zeros and correctly oriented cyclic Fourier blocks; new c coprimality and rank c-1 are explicitly checked. |
| dependency | [Variation and discrete interpolation](Yin_C_G0172_v1.md#moving-cubic-discrete-fejer) | Sections2--3 actual rational-factor variation, Fejer arc estimate and exact missing sample; all premises and costs rebuilt for the new c. |
| dependency | [Full original L1 mechanism](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | Rank3, same2d normalization and positive finite cyclic correction reconstructed before scalar composition; no old-family statement silently generalized. |
| support | [Earlier alias mechanism](Yin_C_G0565_v2.md#moving-band-exact-alias) | Lower-separation proof only; new closed2M exclusion and translated finite means are proved here. |
| dependency | [Adopted weighted torus/probability mechanism](Yin_C_G0641_v2.md#combined-argument) | Pointwise contact derivatives, conditional torus integral, every-path smoothing, all-scale shell bound and finite weak Fourier lemma, only after every changed original-law premise is reconstructed; all five costs paid. |
| dependency | [Old-family enlargement for degree comparison](Yin_C_G0641_v2.md#additional-joint-shell-statement) | Only the unchanged square-family logarithmic M8/7 conclusion used to obtain its separate degree2/7 statement; not applied to the new c schedule. |
| dependency | [Actual torus modulated bands](Yin_C_G0638_v1.md#statement) | M1--M3 local centers/radii and torus mass/support; new-family alias, positivity and original return are separately proved. |
| dependency | [Normalized positive kernel](Yin_C_G0637_v1.md#complete-argument) | Squared Fejer probability normalization, closed support and3pi/M first moment, with new original-circle coefficient/mean equalities proved here. |
| dependency | [Same actual torus amplitude bound](Yin_C_G0633_v2.md#additional-complete-logarithm-free-and-two-sided-argument) | Same fixed-K g and integral r_s<=8s^(2/3); no replacement by a conjugate or original-circle law. |
| dependency | [Accepted integer Bertrand statement](Yin_C_G0356_v1.md#argument) | For every integer n>=2, n<p<2n for some prime p, at the retained external-statement depth; all current thresholds are integers before use. |
| support | [Bertrand source-proof boundary](../audits/literature/Mig78/Yin_U001.md#mig78-u001) | Proposition5-length section retains the accepted classical prime-interval input; its original proof is not re-audited or attributed as a new theorem of Mignotte. |
| dependency | [Generic contact and fixed-input Fourier facts](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Projection/contact identity, scalar psi<=k and fixed-input derivative/Fourier argument rechecked for newly certified Salem inputs; no old moving-family conclusion transplanted. |
| support | [Sources and exact reuse boundaries](#sources-reuse-and-acceptance-boundary) | Actual inspected units and precise fixed-schedule versus reusable-proof distinctions, accepted classical statement depth, no new acquisition or computation. |
| review | [Independent entire fixed-target finding](../audits/reviews/Yin_R_G0852_v1.md#balanced-prime-family-whole-independent-finding) | Complete BS1--BS19, exact actual prime/degree/full-window inputs, source applicability at the retained depth, every finite support/translation and cost, uniform and all-sequence quantifiers, separate old/new actual-degree equivalences. |


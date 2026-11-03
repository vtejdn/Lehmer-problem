---
author: Yin
---

# Uniform translated-circle averages and averaged original Fourier return

Human author Yin.
Root supplied the relative-derivative translated-circle comparison, averaged L2 smoothing balance and truncated negative-half-moment companion.
Paid_comparison checked and developed the complete pathwise proof at clipping corners, bounded integral norm inequality, explicit resolution conditions, full coefficient comparisons and existing-rectangle strict12/23 consumer.
Both are contributors, not independent reviewers.
The same actual positive kernel and complete closed-box interfaces are adopted in [C637](Yin_C_G0637_v1.md#decision-whole-reviewed-2026-10-23).
The new translated-circle statement is proved here and is not inferred from product-coordinate independence.
No developing localized/modulated support theorem is used.
No numerical experiment or new native computation is used.

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
For an actual degree-d_j Salem P_j of the specified schedule, set N_coeff,j=2d_j and let A_rel,j be the N_coeff,j-by-d_j full coefficient matrix of P_j,tP_j,...,t^(d_j-1)P_j.
The original rank-d_j residual projection and its actual single-circle symbol are

    R_j=I-A_rel,j(A_rel,j^T A_rel,j)^-1 A_rel,j^T,
    v_j(t)=(1,t,...,t^(2d_j-1))^T,
    k_j(t)=(2d_j)^-1 v_j(t^-1)^T R_j v_j(t).
Thus the kernel below uses every original coefficient, with no cyclic or conjugate-distribution replacement.

Use L_j=K+a_j+b_j+2, M_j=floor(a_j/4), E_j=[1+pi L_j(5+2log c_j)]/c_j and epsilon_j=(4L_j-5)/(2d_j)+E_j/2.

Put

    D_l=||partial_l Acal||_infinity+||partial_l Bcal||_infinity, l=1,2,3,
    A_der,K=1+sum_l D_l, C_rel,K=3pi A_der,K,
    C_2,K=24pi A_der,K, C_1,K=600pi A_der,K.

For 0<s<=1 set r_s=s/(g+s), U_s=Ncal/(g+s) and
r_s^vee(z,u,v,w)=r_s(z^-1,u^-1,v^-1).
All angular paths and moments use representatives in [-pi,pi].
Define

    V(z,u,v)=U(z^-1,u^-1,v^-1),
    Kcal=(1-Re(wV))/2, F_tau=psi_tau(Kcal),
    Kcal_s=(1-Re(w U_s(z^-1,u^-1,v^-1)))/2,
    F_(tau,s)=psi_tau(Kcal_s),
    f_(j,tau)=psi_tau(k_j),
    iota_j(z)=(z,z^a_j,z^b_j,z^c_j),
    H_j(gamma)=gamma_0+a_j gamma_1+b_j gamma_2+c_j gamma_3.

For every a in T^4 let mu_(j,a) be the probability measure obtained by pushing original-circle Haar through z to a*iota_j(z).
Let nu_4 be probability four-torus Haar and nu_3 its first-three-coordinate marginal.
Write

    I_s(a)=integral r_s^vee dmu_(j,a), I_s^star=sup_(a in T^4) I_s(a).

Use the exact adopted positive kernel

    F_N(t)=N^-1 abs(sum_(l=0)^(N-1)exp(ilt))^2,
    J_N=F_N^2/[(2N^2+1)/(3N)],
    P_M=J_(floor(M/2)+1).

For integer M>=2, P_M has mass one, is nonnegative, has Fourier support in the closed [-M,M] interval and has first moment at most3pi/M.
Let Q_(tau,s) be the convolution of F_(tau,s) with the four-coordinate product of P_M.

### Translated means and averaged smoothing

For every actual j with M=M_j>=2 and every 0<s<=1 satisfying

    M sqrt(s)>=2C_rel,K,                                         (AV1)

one has

    I_s^star<=2 integral r_s dnu_3<=16s^(2/3).                    (AV2)

This is a uniform comparison for all translated original circles, not equality of their nonlinear means or independence of their coordinates.
For every 0<tau<=1, the same scale condition gives

    ||F_(tau,s)-Q_(tau,s)||_(L2(mu_(j,a)))
       <=C_2,K/(M tau s^(1/6)) for EVERY a,
    ||F_(tau,s)-Q_(tau,s)||_(L2(nu_4))
       <=C_2,K/(M tau s^(1/6)).                                 (AV3)

The assertions include all clipping corners via the pathwise argument below.
No restriction of an ambient almost-everywhere derivative to a singular curve is assumed.

### Complete finite quadratic return

For every actual j with M=M_j>=2, every 0<tau<=1/64 and 0<lambda<=1, put rho=tau lambda.
Assume BOTH resolutions

    M sqrt(lambda)>=2C_rel,K, M sqrt(rho)>=2C_rel,K.              (AV4)

For every finite Gamma subset of [-M,M]^4 intersect Z^4, including the empty set,

    [sum_(gamma in Gamma)
       |fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma)|^2]^(1/2)
       <=E_avg(j,tau,lambda),                                   (AV5)

where

    E_avg=sqrt(epsilon_j/tau)+10lambda^(1/3)
                  +2C_2,K/[M tau rho^(1/6)].

All signs and all fourth-coordinate harmonics are allowed.
Set

    A_bal,K=max{1,4C_rel,K^2},
    B_avg,K=10A_bal,K^(1/3)+2C_2,K A_bal,K^(-1/6).

Whenever lambda_bal=A_bal,K M^-2 tau^(-7/3)<=1, its choice is legal, rho_bal=tau lambda_bal satisfies BOTH conditions (AV4), and

    E_avg(j,tau,lambda_bal)
       <=sqrt(epsilon_j/tau)+B_avg,K M^(-2/3)tau^(-7/9)
       =:E_avg,bal(j,tau).                                      (AV6)

The explicit legality and resolution hypotheses are not waived at smaller scales.

### Existing complete rectangle and strict12/23 widths

Keep delta_0=pi/(4K) and the adopted positive-kernel witness condition

    T_J,K(R_z,R_u,J,L)
       =24576pi J(L+J)/R_u+3pi(K+4)/R_z
            +8pi^3 J/(R_z^3 delta_0^3).

For every sufficiently large actual j, every 0<tau<=1/64, and integers R_z,R_u>=2,J>=2, use L_tau=floor(1/(4sqrt(tau))).
If R_z,R_u,J,L_tau<=M_j and T_J,K(R_z,R_u,J,L_tau)<=1/16, then any legal lambda satisfying (AV4) gives

    W_*(psi_tau(k_j))
       >=3log(J+1)/(1024pi)
          -3sqrt(L_tau R_z R_u J)E_avg(j,tau,lambda).             (AV7)

The entire endpoint-inclusive set of
(2R_z+1)(2R_u+1)J L_tau<=9L_tau R_zR_uJ coefficients is paid.
The balanced version uses E_avg,bal only under its stated legality condition.

Fix any real 0<theta<12/23 and put

    Delta_theta=2/3-23theta/18>0, zeta_theta=Delta_theta/10.

There exist j0 and C depending only on theta,K such that for every j>=j0 and EVERY width M_j^-theta<=tau<=1/64,

    W_*(psi_tau(k_j))
       >=[3zeta_theta/(1024pi)]log M_j
          -C[M_j^(-3Delta_theta/4)
                  +M_j^(-11/23)(1+log M_j)^(1/2)].               (AV8)

Consequently every actual sequence tau_j->0 with tau_j>=M_j^-theta eventually has its original Wiener norms tending to infinity.
The strip estimate is uniform; the sequence's index of entry may depend on the sequence.
The equality theta=12/23 and arbitrary faster shrinking are not asserted.

### Truncated negative-half moment and a linear companion

For every actual j with M=M_j>=2, every 0<rho<=1 satisfying M sqrt(rho)>=2C_rel,K, every translation a and nu_4 as well,

    integral (g^vee+rho)^(-1/2)dmu_(j,a)<=97,
    integral (g^vee+rho)^(-1/2)dnu_4<=97.                         (AV9)

Here g^vee is g at the inverse first-three coordinates.
Only this truncated moment is asserted.
The untruncated g^(-1/2) need not be integrable on an original circle.

For every 0<tau<=1, the corresponding product-kernel smoothing has L1 errors at most C_1,K/(M tau) on EACH of these measures.
If M_j>=max{2,2C_rel,K}, choose rho_0=(2C_rel,K/M_j)^2.
For every integer gamma in the entire closed four-box and every 0<tau<=1,

    |fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma)|
       <=beta_lin,j/tau,                                        (AV10)

where the complete actual budget is

    beta_lin,j=epsilon_j
          +12(2C_rel,K)^(4/3)M_j^(-4/3)+2C_1,K/M_j
       =O_K(M_j^-1).

No finite or infinite coefficient sum is controlled by (AV10) without separately paying its actual support.
No localized-support or general critical-log consumer is invoked here.
The original full2d_j coefficient dimension, normalized law, fixed-j Wiener finiteness, actual contact-minus-Haar margin at least1/2 and log2<m(P_j)<log4 family remain unchanged.
Neither amplitude sharpness nor any of these sufficient Fourier estimates proves optimality of a width exponent or resolves the unrestricted Task.

## Reuse and source boundary

The complete actual C637 positive-kernel and finite-projection theorem, adopted C633v2 amplitude bounds, C632 derivative identities and C565 original comparison and closed alias interfaces were read before the refinement.
A focused local search found no previous uniform translated-circle or relative-derivative mean theorem at this scope.
The finite mixed-norm calculation in C512v2 is related but is not a substitute for the present continuous translated-curve argument.

The bounded L2 integral triangle inequality is proved directly below from Fubini and Cauchy--Schwarz.
For its classical attribution, the primary [Terence Tao, 245C Notes1: Interpolation of Lp spaces, 2009-03-30](https://terrytao.wordpress.com/2009/03/30/245c-notes-1-interpolation-of-lp-spaces/) was checked at Section4, the opening endpoint estimate in the proof of Lemma37.
That passage uses Minkowski's integral inequality for an L1-to-Lq integral operator with uniform row norm; q=2 matches the bounded norm estimate needed here.
Only that identification was inspected, not the full interpolation argument or historical proof.
No interpolation theorem is a premise.
Coordinatewise FTC is used only on the smooth r_s and Kcal_s; the scalar clipping is handled by its global Lipschitz inequality.
All required path, probability and integral-norm steps are written below.
No ambient null-set restriction, independent-coordinate replacement or unreviewed localized-support theorem is used.

## Complete argument

### 1. Relative derivatives and finite means on every translated circle

For every first-three coordinate l, the actual amplitude identities give

    |partial_l g|<=2D_l sqrt(g).

Since r_s is strictly positive and smooth for fixed s>0,

    |partial_l r_s|/r_s
       =|partial_l g|/(g+s)
       <=2D_l sqrt(g)/(g+s)<=D_l/sqrt(s).                        (AV11)

The final inequality follows from g+s>=2sqrt(gs), and includes g=0 directly.
The fourth-coordinate derivative of r_s^vee is zero; coordinate inversion preserves every absolute bound.

Let q_s be the convolution of r_s^vee with the four-coordinate product P_M.
Its Fourier support lies in the closedM box.
For any translation a, each nonconstant character indexed by delta in that support has mean
a^delta integral z^(H_j(delta))dHaar(z)=0 by the exact closed2M alias exclusion.
Hence

    integral q_s dmu_(j,a)=qhat_s(0)
       =integral r_s^vee dnu_4=integral r_s dnu_3.                (AV12)

The last equality uses the kernel's mass one and Haar inversion.
This is an equality only for the finite polynomial q_s, not for the original nonlinear r_s.

For any coordinate displacement h_l in [-pi,pi], smooth coordinatewise FTC for r_s^vee, followed by the triangle inequality and (AV11), gives

    integral |r_s^vee(a*iota_j(z))
         -r_s^vee(a*iota_j(z)*exp(-ih_l e_l))|dHaar(z)
       <=|h_l|D_l I_s^star/sqrt(s).

Indeed at every intermediate path parameter the law is another translated original circle, whose r_s^vee mean is bounded by the same I_s^star.
This reasoning is valid for each translation and for paths crossing an angular origin.
All integrands are bounded for fixed positive s, so the integrations may be exchanged.

Telescope the first-three coordinate displacements and integrate against the positive product kernel.
Its first moment is at most3pi/M in each coordinate.
Together with (AV12) this yields, for every a,

    I_s(a)<=integral r_s dnu_3
       +[3pi sum_l D_l/(M sqrt(s))] I_s^star.

One has I_s^star<=1, so it is finite, and taking the supremum is legitimate whether or not it is attained.
Under (AV1) the bracket is at most1/2.
Thus I_s^star<=2 integral r_s dnu_3<=16s^(2/3), by C633v2.
This proves (AV2) without assuming equality of the full nonlinear means.

### 2. A direct bounded integral norm inequality and pathwise clipping

The following restricted integral triangle inequality suffices.
Let nu be a finite positive measure on a parameter set and let v(u,x) be bounded and measurable on its product with a probability space (X,mu).
Fubini and Cauchy--Schwarz give

    ||integral v(u,.)dnu(u)||_(L2(mu))^2
       =integral integral <v(u,.),v(v',.)>_(L2(mu))dnu(u)dnu(v')
       <=[integral ||v(u,.)||_(L2(mu))dnu(u)]^2.                  (AV13)

The equality may be read with the real part of the inner product in the complex case.
The bound follows by the absolute value of that inner product.
All integrals are finite in the applications here, so no unproved vector-valued limiting interchange is needed.
For L1 the corresponding norm bound is directly the scalar triangle inequality and Fubini.

For fixed s>0, Kcal_s is smooth in each angular coordinate.
The clipping function psi_tau is globally1/tau-Lipschitz on[0,1].
For EVERY basepoint and any coordinate interval [a,b], smooth FTC applied to Kcal_s gives

    |psi_tau(Kcal_s(b))-psi_tau(Kcal_s(a))|
       <=tau^-1 integral_a^b |dKcal_s(t)/dt|dt                  (AV14)

with the interval reoriented if necessary.
This is a pointwise path inequality and needs no derivative of the clipped function on an ambient null set.
In particular it remains valid if a translated original circle lies in a clipping level set.

Quotient differentiation using |Ncal|<=g and both amplitude derivative bounds gives

    |partial_l U_s|<=4D_l sqrt(g)/(g+s).

Thus for the first three coordinates, (AV14) is dominated by the path integral of

    G_l=2D_l sqrt(g^vee)/[tau(g^vee+s)]
       <=2D_l sqrt(r_s^vee)/(tau sqrt(s)).                        (AV15)

For the fourth coordinate a constant envelope G_4=1/(2tau) suffices.
Under (AV1), (AV2) shows that on EVERY translated original circle

    ||G_l||_2<=8D_l s^(-1/6)/tau, l=1,2,3.

The product-Haar bound is no larger with this same constant.
The complete four-coordinate sum is at most
(8sum_l D_l+1/2)s^(-1/6)/tau<=8A_der,K s^(-1/6)/tau.
Apply (AV13) first to each path integral in (AV14), and then to the positive product-kernel average of the telescoped differences.
Every intermediate path is another translated circle already covered by (AV2).
Multiplication by the first moment3pi/M proves (AV3), with C_2,K=24pi A_der,K.
The torus proof uses its translation invariance and the same envelopes.
No torus-only derivative norm has been used on the original circle.

### 3. Complete finite quadratic return and its balanced resolution

Fix tau,lambda,rho as in (AV4).
The already proved scalar comparison, also valid at common zeros, is

    |F_tau-F_(tau,rho)|^2<=2r_lambda^vee.

For clarity it follows from the phase inequality and clipping at one:
with t_scale=g^vee/lambda+tau>0,
min{1,1/(4t_scale^2)}<=2/(1+t_scale)<=2r_lambda^vee.
The first inequality is immediate for t_scale<=1/2 and follows from
(1+t_scale)/(4t_scale^2)<=3/2 for t_scale>=1/2.

The product-Haar mean of r_lambda is at most8lambda^(2/3), while its original-circle mean is at most16lambda^(2/3) by the first resolution in (AV4).
The two regularization L2 costs therefore sum to at most

    (4+sqrt(32))lambda^(1/3)<=10lambda^(1/3).

The original composition cost remains sqrt(epsilon_j/tau), using its true L1 bound epsilon_j/tau and its range difference at most one.
The two smoothing costs are each at most C_2,K/(M tau rho^(1/6)) by the second resolution and (AV3).
These are precisely the five costs in E_avg.

For any finite Gamma in the closed box, its original characters H_j(gamma) are distinct.
The product-kernel Q_(tau,rho) has the same selected original and torus coefficients by the exact closed-M/closed2M argument.
For either probability space and its finite orthonormal character family, direct expansion gives

    ||h-sum_(gamma in Gamma) hhat(gamma)chi_gamma||_2^2
       =||h||_2^2-sum_(gamma in Gamma)|hhat(gamma)|^2>=0.

Apply this to the original-circle and torus difference functions from Q_(tau,rho), and then use the Euclidean triangle inequality for their finite coefficient vectors.
The full five-cost bound proves (AV5).
The empty set and arbitrary harmonic signs are included.
No infinite Fourier vector is compared.

For lambda_bal=A_bal,K M^-2 tau^(-7/3)<=1, rho_bal=A_bal,K M^-2 tau^(-4/3) lies in(0,1].
Moreover

    M sqrt(rho_bal)=sqrt(A_bal,K)tau^(-2/3)>=2C_rel,K,
    lambda_bal>=rho_bal.

Thus both resolutions hold, not merely one of them.
The exact terms are

    lambda_bal^(1/3)
       =A_bal,K^(1/3)M^(-2/3)tau^(-7/9),
    [M tau rho_bal^(1/6)]^-1
       =A_bal,K^(-1/6)M^(-2/3)tau^(-7/9).

Their sum gives (AV6) with the stated unambiguous B_avg,K.
No use of this balanced formula is authorized when lambda_bal>1.

### 4. The existing complete rectangle and strict12/23 strips

The adopted C637 witness theorem under T_J,K<=1/16 supplies the original phase mass on the entire closed rectangle.
Its selected set is exactly

    G={(eta,k): -eta=(p,q,-m),
         |p|<=R_z, |q|<=R_u, 1<=m<=J, 1<=k<=L_tau}.

The exact cardinality and upper bound are
(2R_z+1)(2R_u+1)J L_tau<=9L_tau R_zR_uJ.
Its original frequencies are positive and distinct; the same scalar cap harmonics and inverse phase give torus mass at least3log(J+1)/(1024pi).
Finite Cauchy--Schwarz charges at most sqrt(|G|)E_avg.
This proves (AV7), with every endpoint coefficient paid and no change to the original phase or arithmetic family.

Fix 0<theta<12/23 and the positive Delta_theta,zeta_theta from the statement.
Use

    J_j=floor(M_j^zeta_theta),
    Q_z,j=floor(M_j^(2zeta_theta)),
    Q_u,j=floor(M_j^(theta/2+2zeta_theta)),

and set R_z=Q_z,j,R_u=Q_u,j,J=J_j,L=L_tau.
For every permitted width, L_tau<=M_j^(theta/2)/4.
All cutoff exponents are positive and below one; in particular
theta/2+2zeta_theta=2/15+11theta/45<1.
The floors eventually satisfy the fixed lower bounds and the whole closed box.

With floor x>=x/2 for x>=2, the three T_J,K terms are bounded uniformly by fixed multiples of

    M_j^-zeta_theta+M_j^(-theta/2),
    M_j^(-2zeta_theta),
    M_j^(-5zeta_theta).

Hence the finite witness condition holds uniformly beyond a threshold depending only on theta,K.
The balancing choice is also uniformly legal because

    lambda_bal<=A_bal,K M_j^(-2+7theta/3)->0,

and theta<12/23<6/7.
Its two resolutions then hold by the already proved exact identities.

The entire square-root support satisfies

    3sqrt(L_tau R_zR_uJ)
       <=(3/2)M_j^(theta/4+5zeta_theta/2)tau^(-1/4).

The balanced new term in (AV6) therefore costs at most a constant times

    M_j^(-2/3+23theta/18+5zeta_theta/2)
       =M_j^(-3Delta_theta/4),

where the width power is tau^(-7/9-1/4)=tau^(-37/36).
The original sqrt(epsilon_j/tau) term, using the full schedule bound, costs at most

    C M_j^(-1+theta+5zeta_theta/2)(1+log M_j)^(1/2).

Its exponent is

    -1+theta+Delta_theta/4=-5/6+49theta/72<-11/23.

This yields precisely the two error terms in (AV8).
Finally J_j+1>M_j^zeta_theta, so the main logarithmic term is the stated one.
All estimates are uniform in the width strip; sequence entry is only eventual.
At theta=12/23 the present Delta_theta and growing-band exponent vanish, so this argument makes no endpoint assertion.

### 5. Truncated half moment and complete linear return

Assume 0<rho<=1 and M sqrt(rho)>=2C_rel,K.
For every t in[rho,1], the same resolution holds at t.
Since r_t>=1/2 on g<=t, (AV2) implies, uniformly in all translations,

    mu_(j,a){g^vee<=t}<=32t^(2/3).

The torus bound is no larger with that same constant.
For any nonnegative g, direct consideration of g<=rho, rho<g<=1 and g>1 gives

    (g+rho)^(-1/2)
       <=1+(1/2)integral_rho^1 1_(g<=t)t^(-3/2)dt.

The three right sides in those cases are rho^(-1/2), g^(-1/2) and1 respectively, each an upper bound for the left side.
Integration of this nonnegative finite expression yields

    integral (g^vee+rho)^(-1/2)
       <=1+16integral_rho^1 t^(-5/6)dt<=97.

This proves (AV9).
No information about sublevels below rho or the integrability of g^(-1/2) has been presumed.

The first-three path envelopes from (AV15) also satisfy

    G_l<=2D_l/[tau sqrt(g^vee+rho)].

Their total L1 norms on every translated original circle and on the torus are at most194sum_l D_l/tau.
The fourth coordinate adds at most1/(2tau), so a bound195A_der,K/tau suffices.
Use the pointwise path inequality (AV14), the direct L1 integral triangle bound and the positive kernel's first moment3pi/M.
The smoothing L1 error in each space is at most
585pi A_der,K/(M tau)<=C_1,K/(M tau).

For M>=max{2,2C_rel,K}, put rho_0=(2C_rel,K/M)^2.
It is legal and lies exactly at the stated resolution threshold.
The torus mean of r_rho0 is at most8rho_0^(2/3), and its original-circle mean is at most16rho_0^(2/3).
Thus the two ordinary L1 phase-regularization errors together cost at most12rho_0^(2/3)/tau.
The two new L1 smoothing errors cost2C_1,K/(M tau).
The complete original function comparison contributes epsilon_j/tau.
The finite intermediate coefficients agree on the entire closed box, so these five costs prove (AV10).
Using the same actual schedule epsilon_j=O_K(M_j^-2(1+log M_j)) gives beta_lin,j=O_K(M_j^-1).
No additional consumer or unpriced coefficient sum is inferred from this companion estimate.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision translated-averaged-return-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T20:54 |
| status | open |
| reason | Register the complete uniform translated-original-circle mean comparison, pathwise averaged L2 smoothing, full finite-Gamma quadratic return with both resolution conditions, original complete-rectangle strict12/23 width strips, and the truncated negative-half moment97 with fully paid O_K(M^-1) linear coefficient budget. Root and paid_comparison are contributors. All new claims remain pending fresh isolated whole review and adoption. No localized-support input, endpoint12/23, width optimality, near-one input or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire translated averaged-return statement](#statement) | AV1--AV10 with exact original K, prime schedule, full2d coefficient window, original and product probability laws, every translation, all scalar domains and resolutions, every finite closed-box Gamma including empty and signed harmonics, complete9L rectangle and uniform strict12/23 width/sequence quantifiers. |
| argument | [Complete translated-circle and return proof](#complete-argument) | AV11--AV15 and all proofs of AV1--AV10: relative-derivative absorption after exact finite means, bounded Fubini/Cauchy--Schwarz norm bound, every-path FTC and clipping, two regularizations and two smoothings plus original comparison, both balanced resolutions, full rectangle costs/exponents, truncated moment97 and all linear costs. |
| dependency | [Exact positive kernel and closed-box comparison](Yin_C_G0637_v1.md#complete-argument) | Adopted normalized squared Fejer kernel, support including endpoints and first moment3pi/M, exact finite-polynomial return, full existing witness T_J and endpoint-inclusive9L rectangle; all changed smoothing and coefficient budgets proved anew here. |
| dependency | [Adopted original amplitude law](Yin_C_G0633_v2.md#additional-complete-logarithm-free-and-two-sided-argument) | For the same original amplitude g, integral r_s<=8s^(2/3) for every0<s<=1; amplitude sharpness supplies no claim of Fourier or width optimality. |
| dependency | [Actual amplitude derivatives](Yin_C_G0632_v1.md#square-root-regularization-derivative) | The exact Acal,Bcal,g,Ncal and angular derivative conventions, common-zero scope, inversion and fourth-coordinate phase; relative derivative and every-path estimates written completely here. |
| dependency | [Original input and full coefficient kernel](Yin_C_G0565_v2.md#statement) | Actual K, prime schedule, monic irreducible Salem P_j, complete degree, original2d coefficient projection and single-circle law. |
| dependency | [True original function comparison](Yin_C_G0565_v2.md#moving-band-fejer-budget) | Exact epsilon_j L1 error, scalar Lipschitz conversion and range bound; no unproved pointwise original comparison. |
| dependency | [Closed2M arithmetic alias exclusion](Yin_C_G0565_v2.md#moving-band-exact-alias) | Nonzero H_j on every nonzero closed2M integer difference; translated means are deduced only for the finite intermediate polynomial. |
| dependency | [Exact witnesses and derivative scope](Yin_C_G0629_v3.md#witness-specific-anisotropic-refinement) | Original fixed witness interval, u derivative, fixed-witness z derivative and global amplitude bound underlying the adopted C637 complete rectangle. |
| dependency | [Scalar harmonic and inverse-phase identities](Yin_C_G0629_v3.md#many-harmonic-transfer) | Exact a_k bounds, L_tau normalization and the selected inverse-phase Fourier coefficients; all original frequencies and every selected coefficient remain paid. |
| dependency | [Actual schedule error](Yin_C_G0569_v2.md#static-phase-original-return) | epsilon_j=O_K(M_j^-2(1+log M_j)) from the original lower prime separations, without an upper prime-gap estimate. |
| dependency | [Original contact and fixed-input boundary](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | The original contact-minus-Haar margin, fixed-j Wiener finiteness and two-limit restrictions; no near-one or unrestricted conclusion. |
| support | [Reuse and classical norm-inequality attribution](#reuse-and-source-boundary) | Targeted prior reuse, exact inspected Tao Notes1 Section4 Lemma37 endpoint passage and its attribution-only scope; the bounded norm inequality and all pathwise probability steps are proved here. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T21:02 |
| status | proved |
| reason | Adopt the entire translated-circle and averaged-return theorem after main reading of complete C639 and isolated whole R846. Relative-derivative absorption controls every translated original circle; the every-path clipping proof and complete five-cost comparison establish both resolved averaged L2 returns and the existing-rectangle strict12/23 width strips. The truncated moment97 and complete O_K(M^-1) linear coefficient budget are retained at their exact finite-box scope. No endpoint, localized-support consumer, width optimality or unrestricted Mahler conclusion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire translated averaged-return statement](#statement) | AV1--AV10 with exact original K, prime schedule, full2d coefficient window, original and product probability laws, every translation, all scalar domains and resolutions, every finite closed-box Gamma including empty and signed harmonics, complete9L rectangle and uniform strict12/23 width/sequence quantifiers. |
| argument | [Complete translated-circle and return proof](#complete-argument) | AV11--AV15 and all proofs of AV1--AV10: relative-derivative absorption after exact finite means, bounded Fubini/Cauchy--Schwarz norm bound, every-path FTC and clipping, two regularizations and two smoothings plus original comparison, both balanced resolutions, full rectangle costs/exponents, truncated moment97 and all linear costs. |
| dependency | [Exact positive kernel and closed-box comparison](Yin_C_G0637_v1.md#complete-argument) | Adopted normalized squared Fejer kernel, support including endpoints and first moment3pi/M, exact finite-polynomial return, full existing witness T_J and endpoint-inclusive9L rectangle; all changed smoothing and coefficient budgets proved anew here. |
| dependency | [Adopted original amplitude law](Yin_C_G0633_v2.md#additional-complete-logarithm-free-and-two-sided-argument) | For the same original amplitude g, integral r_s<=8s^(2/3) for every0<s<=1; amplitude sharpness supplies no claim of Fourier or width optimality. |
| dependency | [Actual amplitude derivatives](Yin_C_G0632_v1.md#square-root-regularization-derivative) | The exact Acal,Bcal,g,Ncal and angular derivative conventions, common-zero scope, inversion and fourth-coordinate phase; relative derivative and every-path estimates written completely here. |
| dependency | [Original input and full coefficient kernel](Yin_C_G0565_v2.md#statement) | Actual K, prime schedule, monic irreducible Salem P_j, complete degree, original2d coefficient projection and single-circle law. |
| dependency | [True original function comparison](Yin_C_G0565_v2.md#moving-band-fejer-budget) | Exact epsilon_j L1 error, scalar Lipschitz conversion and range bound; no unproved pointwise original comparison. |
| dependency | [Closed2M arithmetic alias exclusion](Yin_C_G0565_v2.md#moving-band-exact-alias) | Nonzero H_j on every nonzero closed2M integer difference; translated means are deduced only for the finite intermediate polynomial. |
| dependency | [Exact witnesses and derivative scope](Yin_C_G0629_v3.md#witness-specific-anisotropic-refinement) | Original fixed witness interval, u derivative, fixed-witness z derivative and global amplitude bound underlying the adopted C637 complete rectangle. |
| dependency | [Scalar harmonic and inverse-phase identities](Yin_C_G0629_v3.md#many-harmonic-transfer) | Exact a_k bounds, L_tau normalization and the selected inverse-phase Fourier coefficients; all original frequencies and every selected coefficient remain paid. |
| dependency | [Actual schedule error](Yin_C_G0569_v2.md#static-phase-original-return) | epsilon_j=O_K(M_j^-2(1+log M_j)) from the original lower prime separations, without an upper prime-gap estimate. |
| dependency | [Original contact and fixed-input boundary](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | The original contact-minus-Haar margin, fixed-j Wiener finiteness and two-limit restrictions; no near-one or unrestricted conclusion. |
| support | [Reuse and classical norm-inequality attribution](#reuse-and-source-boundary) | Targeted prior reuse, exact inspected Tao Notes1 Section4 Lemma37 endpoint passage and its attribution-only scope; the bounded norm inequality and all pathwise probability steps are proved here. |
| review | [Independent whole translated-return finding](../audits/reviews/Yin_R_G0846_v1.md#translated-averaged-return-whole-independent-finding) | Entire AV1--AV15, every translation/path and both scale resolutions, all five quadratic and linear costs, complete rectangle and strict12/23 exponents, truncated moment97 and bounded classical attribution; unchanged source and earlier-review limits retained. |

